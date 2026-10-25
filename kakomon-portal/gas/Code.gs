/**
 * THINKING 過去問ポータル — Google Apps Script（API＋運用メニュー）
 *
 * このファイルはスプレッドシート「【過去問ポータル】DB」に紐づく Apps Script に貼り付ける。
 * 設計の全体像は kakomon-portal/開発ガイド.md を参照。
 *
 * API（Webアプリとしてデプロイ）
 *   GET  ?action=ping
 *   GET  ?action=boot&token=<LINE IDトークン>&etag=<前回のetag>
 *   POST {action:"fav", token, book, on}     お気に入りの登録/解除
 *   POST {action:"log", token, book, title}  閲覧ログ
 *
 * 運用メニュー（スプレッドシート上部「過去問ポータル」）
 *   教材を追加 / 選択行のPDFを差し替え / フォルダから取り込み / 点検 / 初期セットアップ
 */

var VERSION = '1.0.0';

var SHEET = {
  BOOKS: '問題集',
  ITEMS: '教材',
  USERS: '利用者',
  CONFIG: '設定',
  FAVS: 'お気に入り',
  LOGS: '閲覧ログ'
};

var HEAD = {
  BOOKS: ['ID', 'グループ', '大学', '大学よみ', '問題集名', '対応する学部・日程', '検索キーワード', '公開', 'サンプル', '並び順', 'メモ'],
  ITEMS: ['問題集名', '区分', 'タイトル', 'ファイル', '公開', '並び順', '更新日', 'メモ'],
  USERS: ['LINE表示名', 'LINE ID', '初回アクセス', '最終アクセス', '氏名メモ', '購入した問題集', '購入した大学（セット）', '期限', 'スタッフ', '停止', 'メモ'],
  FAVS: ['LINE ID', '問題集ID', '登録日時'],
  LOGS: ['日時', 'LINE ID', '種別', '問題集ID', 'タイトル']
};

var KINDS = ['戦略編', '大問別', '単語帳', '模試', '解説', 'その他'];

var DEFAULT_CONFIG = [
  ['ポータル名', 'THINKING 過去問ポータル', '画面上部の名前'],
  ['LINEチャネルID', '', 'LIFFアプリを作ったLINEログインチャネルの「チャネルID」（数字）'],
  ['CAMPUS_API_URL', 'https://script.google.com/macros/s/AKfycbwNuxYxMqk5rv4LXBHmp9QnafbowzEdGgfJv0AcZUXNJoy3zn8pfbFqD_XG0E4f4lJm/exec', '塾生判定に使う THINKING CAMPUS のAPI'],
  ['CAMPUS_URL', 'https://liff.line.me/2010454771-l3vZsfjz', '未登録の塾生に案内する THINKING CAMPUS'],
  ['購入案内URL', 'https://lin.ee/yJ8MFVb', 'ロック中の問題集の「購入はこちら」の飛び先'],
  ['公式LINE_URL', 'https://lin.ee/yJ8MFVb', '問い合わせ先'],
  ['グループ順', 'MARCH,関関同立,日東駒専,産近甲龍,その他', 'ホームに並ぶ順番（カンマ区切り）'],
  ['大問の種類', '長文読解,長文空所補充,会話文,会話文空所補充,対話文整序,文法・語法,文法・語彙,語彙,同意表現,整序英作文,正誤問題,1語補充,不要文選択,発音・アクセント,資料読解,複数資料読解,和訳,和文英訳,英作文,要約', '大問別の教材で選べる「内容」（カンマ区切り。ここに足せば選択肢が増える）'],
  ['NEW表示日数', '14', 'この日数以内に追加・更新された教材に NEW / 更新 を付ける'],
  ['保存先フォルダID', '', '初期セットアップで自動作成（触らない）']
];

/* ======================================================================
 * Webアプリ（API）
 * ==================================================================== */

function doGet(e) {
  var p = (e && e.parameter) || {};
  try {
    if (p.action === 'ping') return json_({ ok: true, version: VERSION, time: new Date().toISOString() });
    if (p.action === 'boot') return json_(boot_(p.token, p.etag || ''));
    return json_({ status: 'error', reason: 'unknown action' });
  } catch (err) {
    return json_({ status: 'error', reason: String(err && err.message || err) });
  }
}

function doPost(e) {
  try {
    var body = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    var me = auth_(body.token);
    if (!me) return json_({ status: 'unauthorized' });
    if (body.action === 'fav') return json_(toggleFav_(me.uid, String(body.book || ''), !!body.on));
    if (body.action === 'log') { appendLog_(me.uid, 'view', String(body.book || ''), String(body.title || '')); return json_({ status: 'ok' }); }
    return json_({ status: 'error', reason: 'unknown action' });
  } catch (err) {
    return json_({ status: 'error', reason: String(err && err.message || err) });
  }
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/** 起動時の1リクエストで、本人・権限・一覧・お気に入りをまとめて返す */
function boot_(token, clientEtag) {
  var me = auth_(token);
  if (!me) return { status: 'unauthorized' };

  var cfg = config_();
  var access = access_(me);
  var full = catalog_();
  var etag = full.v + ':' + access.key;
  var res = {
    status: 'ok',
    user: { name: me.name, role: access.role },
    favs: favsOf_(me.uid),
    cfg: {
      title: cfg['ポータル名'],
      buyUrl: cfg['購入案内URL'],
      lineUrl: cfg['公式LINE_URL'],
      campusUrl: cfg['CAMPUS_URL'],
      newDays: Number(cfg['NEW表示日数']) || 14
    },
    etag: etag
  };
  if (clientEtag !== etag) res.catalog = filterCatalog_(full, access);
  return res;
}

/* ---------------- 認証（LINE IDトークンの検証） ---------------- */

function auth_(token) {
  if (!token) return null;
  var cache = CacheService.getScriptCache();
  var key = 'tok:' + sha_(token);
  var hit = cache.get(key);
  if (hit) return JSON.parse(hit);

  var channelId = config_()['LINEチャネルID'];
  if (!channelId) throw new Error('設定シートの「LINEチャネルID」が未入力です');
  var r = UrlFetchApp.fetch('https://api.line.me/oauth2/v2.1/verify', {
    method: 'post',
    payload: { id_token: token, client_id: String(channelId) },
    muteHttpExceptions: true
  });
  if (r.getResponseCode() !== 200) return null;
  var d = JSON.parse(r.getContentText());
  var me = { uid: d.sub, name: d.name || '' };
  var ttl = Math.max(60, Math.min(3000, Number(d.exp) - Math.floor(Date.now() / 1000)));
  cache.put(key, JSON.stringify(me), ttl);
  return me;
}

/* ---------------- 権限 ---------------- */

/**
 * 返り値: { role: staff|student|buyer|guest, books:{id:true}, unis:{大学:true}, key }
 * 塾生は THINKING CAMPUS の会員判定をそのまま使う（ここでの二重登録は不要）。
 */
function access_(me) {
  var cache = CacheService.getScriptCache();
  var ck = 'acc:' + userVer_() + ':' + me.uid;
  var hit = cache.get(ck);
  if (hit) return JSON.parse(hit);

  var row = findUser_(me.uid);
  var acc;
  if (row && row.staff && !row.stopped) {
    acc = { role: 'staff', books: {}, unis: {} };
  } else if (!(row && row.stopped) && isCampusMember_(me.uid)) {
    acc = { role: 'student', books: {}, unis: {} };
  } else if (row && !row.stopped && !row.expired && (row.books.length || row.unis.length)) {
    var ids = bookIdsByName_();
    var books = {};
    row.books.forEach(function (n) { if (ids[n]) books[ids[n]] = true; });
    var unis = {};
    row.unis.forEach(function (u) { unis[u] = true; });
    acc = { role: 'buyer', books: books, unis: unis };
  } else {
    acc = { role: 'guest', books: {}, unis: {} };
  }
  // 塾生は CAMPUS 側で管理しているので、ここに行を作るのは購入者・未登録の人だけ
  if (row) touchUser_(row);
  else if (acc.role === 'guest') addGuestRow_(me);

  acc.key = acc.role + '.' + sha_(Object.keys(acc.books).sort().join(',') + '|' + Object.keys(acc.unis).sort().join(',')).slice(0, 10);
  cache.put(ck, JSON.stringify(acc), 600);
  return acc;
}

function isCampusMember_(uid) {
  var cache = CacheService.getScriptCache();
  var ck = 'campus:' + uid;
  var hit = cache.get(ck);
  if (hit) return hit === '1';
  var url = config_()['CAMPUS_API_URL'];
  if (!url) return false;
  var ok = false;
  try {
    var r = UrlFetchApp.fetch(url + '?action=resolve&userId=' + encodeURIComponent(uid), { muteHttpExceptions: true, followRedirects: true });
    var d = JSON.parse(r.getContentText());
    ok = !!(d && d.ok && d.bound !== false && d.found !== false && !d.blocked);
  } catch (err) {
    ok = false;
  }
  cache.put(ck, ok ? '1' : '0', ok ? 3600 : 300);
  return ok;
}

function findUser_(uid) {
  var sh = sheet_(SHEET.USERS);
  var values = sh.getDataRange().getValues();
  var col = colIndex_(values[0]);
  for (var i = 1; i < values.length; i++) {
    var r = values[i];
    if (String(r[col['LINE ID']]) !== uid) continue;
    var limit = r[col['期限']];
    return {
      rowNo: i + 1,
      last: r[col['最終アクセス']],
      staff: r[col['スタッフ']] === true,
      stopped: r[col['停止']] === true,
      expired: limit instanceof Date && limit.getTime() < Date.now() - 86400000,
      books: splitList_(r[col['購入した問題集']]),
      unis: splitList_(r[col['購入した大学（セット）']])
    };
  }
  return null;
}

function addGuestRow_(me) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    if (findUser_(me.uid)) return;
    var sh = sheet_(SHEET.USERS);
    var now = new Date();
    var row = HEAD.USERS.map(function (h) {
      if (h === 'LINE表示名') return me.name;
      if (h === 'LINE ID') return me.uid;
      if (h === '初回アクセス' || h === '最終アクセス') return now;
      if (h === 'スタッフ' || h === '停止') return false;
      return '';
    });
    sh.appendRow(row);
  } finally {
    lock.releaseLock();
  }
}

/** 最終アクセスは1日1回だけ書く（書き込みは遅いので） */
function touchUser_(row) {
  var last = row.last instanceof Date ? row.last : null;
  if (last && Date.now() - last.getTime() < 86400000) return;
  var sh = sheet_(SHEET.USERS);
  var col = colIndex_(sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]);
  sh.getRange(row.rowNo, col['最終アクセス'] + 1).setValue(new Date());
}

/* ---------------- 一覧（カタログ） ---------------- */

/** シートから一覧を組み立ててキャッシュする。シートが編集されると版が上がり作り直される */
function catalog_() {
  var v = catalogVer_();
  var cache = CacheService.getScriptCache();
  var cached = getChunked_(cache, 'cat:' + v);
  if (cached) return JSON.parse(cached);

  var cfg = config_();
  var groups = splitList_(cfg['グループ順']);
  var books = [];
  var nameToId = {};

  var bs = sheet_(SHEET.BOOKS);
  var bv = bs.getDataRange().getValues();
  var bc = colIndex_(bv[0]);
  for (var i = 1; i < bv.length; i++) {
    var r = bv[i];
    var name = String(r[bc['問題集名']] || '').trim();
    var id = String(r[bc['ID']] || '').trim();
    if (!name || !id) continue;
    nameToId[name] = id;
    books.push({
      id: id,
      g: String(r[bc['グループ']] || 'その他'),
      u: String(r[bc['大学']] || ''),
      uy: String(r[bc['大学よみ']] || ''),
      n: name,
      cov: String(r[bc['対応する学部・日程']] || ''),
      kw: String(r[bc['検索キーワード']] || ''),
      p: r[bc['公開']] === true,
      s: r[bc['サンプル']] === true,
      o: Number(r[bc['並び順']]) || 9999
    });
  }

  var items = [];
  var is = sheet_(SHEET.ITEMS);
  var iv = is.getDataRange().getValues();
  var ic = colIndex_(iv[0]);
  for (var j = 1; j < iv.length; j++) {
    var q = iv[j];
    var bid = nameToId[String(q[ic['問題集名']] || '').trim()];
    var fid = fileIdOf_(q[ic['ファイル']]);
    if (!bid || !fid) continue;
    var d = q[ic['更新日']];
    items.push({
      b: bid,
      k: String(q[ic['区分']] || 'その他'),
      t: String(q[ic['タイトル']] || ''),
      f: fid,
      p: q[ic['公開']] === true,
      d: d instanceof Date ? Utilities.formatDate(d, 'Asia/Tokyo', 'yyyy-MM-dd') : '',
      o: Number(q[ic['並び順']]) || 9999
    });
  }

  books.sort(function (a, b) { return a.o - b.o; });
  items.sort(function (a, b) { return a.o - b.o; });
  var full = { v: v, groups: groups, kinds: KINDS, books: books, items: items };
  putChunked_(cache, 'cat:' + v, JSON.stringify(full), 21600);
  return full;
}

/** 本人が見てよい範囲だけを返す。ロック中の問題集はファイルIDを送らない */
function filterCatalog_(full, acc) {
  var staff = acc.role === 'staff';
  var open = {};
  var books = [];
  full.books.forEach(function (b) {
    if (!b.p && !staff) return;
    var allowed = staff || acc.role === 'student' || b.s || acc.books[b.id] || acc.unis[b.u];
    if (allowed) open[b.id] = true;
    books.push({ id: b.id, g: b.g, u: b.u, uy: b.uy, n: b.n, cov: b.cov, kw: b.kw, s: b.s, L: !allowed, h: !b.p });
  });
  var items = full.items
    .filter(function (it) { return open[it.b] && (it.p || staff); })
    .map(function (it) { return { b: it.b, k: it.k, t: it.t, f: it.f, d: it.d, h: !it.p }; });
  return { groups: full.groups, kinds: full.kinds, books: books, items: items };
}

/* ---------------- お気に入り・ログ ---------------- */

function favsOf_(uid) {
  var sh = sheet_(SHEET.FAVS);
  var last = sh.getLastRow();
  if (last < 2) return [];
  var values = sh.getRange(2, 1, last - 1, 2).getValues();
  var out = [];
  values.forEach(function (r) { if (String(r[0]) === uid) out.push(String(r[1])); });
  return out;
}

function toggleFav_(uid, book, on) {
  if (!book) return { status: 'error', reason: 'book is empty' };
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sh = sheet_(SHEET.FAVS);
    var last = sh.getLastRow();
    var values = last >= 2 ? sh.getRange(2, 1, last - 1, 2).getValues() : [];
    for (var i = values.length - 1; i >= 0; i--) {
      if (String(values[i][0]) === uid && String(values[i][1]) === book) {
        if (on) return { status: 'ok', on: true };
        sh.deleteRow(i + 2);
        return { status: 'ok', on: false };
      }
    }
    if (on) sh.appendRow([uid, book, new Date()]);
    return { status: 'ok', on: on };
  } finally {
    lock.releaseLock();
  }
}

function appendLog_(uid, kind, book, title) {
  sheet_(SHEET.LOGS).appendRow([new Date(), uid, kind, book, title]);
}

/* ======================================================================
 * 運用メニュー
 * ==================================================================== */

function onOpen() {
  SpreadsheetApp.getUi().createMenu('過去問ポータル')
    .addItem('教材を追加（PDFをアップロード）', 'menuUpload')
    .addItem('選択行のPDFを差し替え', 'menuReplace')
    .addSeparator()
    .addItem('フォルダから取り込み', 'menuImport')
    .addItem('点検（リンク切れ・設定ミスを探す）', 'menuCheck')
    .addItem('今すぐ全員に反映', 'menuPublish')
    .addSeparator()
    .addItem('初期セットアップ（最初の1回だけ）', 'menuSetup')
    .addToUi();
}

/** シートが編集されたら一覧の版を上げる（installable トリガー。セットアップで登録） */
function onSheetEdit(e) {
  var name = e && e.range ? e.range.getSheet().getName() : '';
  if (name === SHEET.USERS) bumpUserVer_();
  if (name === SHEET.BOOKS) fillBookIds_();
  if (name === SHEET.BOOKS || name === SHEET.ITEMS || name === SHEET.CONFIG) bumpCatalogVer_();
}

function menuPublish() {
  fillBookIds_();
  bumpCatalogVer_();
  bumpUserVer_();
  SpreadsheetApp.getActive().toast('全員の画面に反映しました（次にポータルを開いたときに最新になります）', '過去問ポータル', 5);
}

function menuUpload() {
  var html = HtmlService.createTemplateFromFile('Upload');
  html.mode = 'add';
  html.target = null;
  SpreadsheetApp.getUi().showSidebar(html.evaluate().setTitle('教材を追加'));
}

function menuReplace() {
  var sh = SpreadsheetApp.getActiveSheet();
  var ui = SpreadsheetApp.getUi();
  if (sh.getName() !== SHEET.ITEMS) { ui.alert('「教材」シートで、差し替えたい行を選んでから実行してください。'); return; }
  var rowNo = sh.getActiveRange().getRow();
  if (rowNo < 2) { ui.alert('差し替えたい教材の行を選んでください。'); return; }
  var col = colIndex_(sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]);
  var r = sh.getRange(rowNo, 1, 1, sh.getLastColumn()).getValues()[0];
  var fid = fileIdOf_(r[col['ファイル']]);
  if (!fid) { ui.alert('この行にはファイルがありません。「教材を追加」を使ってください。'); return; }
  var html = HtmlService.createTemplateFromFile('Upload');
  html.mode = 'replace';
  html.target = { row: rowNo, book: r[col['問題集名']], title: r[col['タイトル']] };
  ui.showSidebar(html.evaluate().setTitle('PDFを差し替え'));
}

/** サイドバー用：選択肢と、問題集ごとの登録済みタイトル（重複チェック・模試の回数の自動提案に使う） */
function getUploadOptions() {
  var bv = sheet_(SHEET.BOOKS).getDataRange().getValues();
  var bc = colIndex_(bv[0]);
  var names = [];
  for (var i = 1; i < bv.length; i++) {
    var n = String(bv[i][bc['問題集名']] || '').trim();
    if (n) names.push(n);
  }
  var iv = sheet_(SHEET.ITEMS).getDataRange().getValues();
  var ic = colIndex_(iv[0]);
  var existing = {};
  for (var j = 1; j < iv.length; j++) {
    var b = String(iv[j][ic['問題集名']] || '').trim();
    if (b) (existing[b] = existing[b] || []).push(String(iv[j][ic['タイトル']] || ''));
  }
  return { books: names, kinds: KINDS, sections: splitList_(config_()['大問の種類']), existing: existing, year: new Date().getFullYear() };
}

/**
 * タイトルは選択肢から自動で作る（手入力させない。誰が入れても同じ書き方になる）。
 *   戦略編 → Vol.0 全体戦略・分析編
 *   大問別 → 大問1・2 長文読解（大問番号＋「設定」シートの「大問の種類」から選んだ内容）
 *   単語帳 → 必修英単語・熟語帳
 *   模試   → 総合模試 第1回
 *   解説   → 2025年度 大問1 解説
 *   その他 → 入力した名前（例外用）
 */
function buildTitle_(f) {
  var nums = (f.nums || []).map(Number).filter(function (n) { return n > 0; }).sort(function (a, b) { return a - b; });
  switch (f.kind) {
    case '戦略編': return 'Vol.0 全体戦略・分析編';
    case '大問別':
      if (!nums.length || !f.section) throw new Error('大問番号と内容を選んでください');
      return '大問' + nums.join('・') + ' ' + f.section;
    case '単語帳': return '必修英単語・熟語帳';
    case '模試':
      if (!(Number(f.round) > 0)) throw new Error('第何回かを選んでください');
      return '総合模試 第' + Number(f.round) + '回';
    case '解説':
      if (!f.year) throw new Error('年度を選んでください');
      return f.year + '年度' + (nums.length ? ' 大問' + nums.join('・') : '') + ' 解説';
    default:
      var t = String(f.free || '').trim();
      if (!t) throw new Error('名前を入力してください');
      return t;
  }
}

/** 並び順もタイトルの中身から決める（入れた順番に関係なく、戦略編→大問順→単語帳→模試→解説 に並ぶ） */
function orderFor_(f) {
  var nums = (f.nums || []).map(Number).filter(function (n) { return n > 0; });
  var first = nums.length ? Math.min.apply(null, nums) : 0;
  switch (f.kind) {
    case '戦略編': return 10;
    case '大問別': return 100 + first * 10;
    case '単語帳': return 800;
    case '模試': return 900 + Number(f.round || 0);
    case '解説': return 1000 + (3000 - Number(f.year || 0)) * 20 + first;
    default: return 5000;
  }
}

/**
 * サイドバーから呼ばれる：追加。
 * 同じ問題集に同じタイトルがすでにあれば、新しい行は作らずにその教材を差し替える（リンクは変わらない）。
 */
function uploadMaterial(form) {
  var book = bookRow_(form.book);
  if (!book) throw new Error('問題集「' + form.book + '」が見つかりません');
  var title = buildTitle_(form);
  var blob = Utilities.newBlob(Utilities.base64Decode(form.data), 'application/pdf', fileNameFor_(form.book, title));

  var sh = sheet_(SHEET.ITEMS);
  var values = sh.getDataRange().getValues();
  var col = colIndex_(values[0]);
  for (var i = 1; i < values.length; i++) {
    if (String(values[i][col['問題集名']]).trim() !== form.book || String(values[i][col['タイトル']]).trim() !== title) continue;
    var fid = fileIdOf_(values[i][col['ファイル']]);
    if (!fid) break;
    Drive.Files.update({ name: fileNameFor_(form.book, title) }, fid, blob); // 高度なサービス Drive API（v3）
    sh.getRange(i + 1, col['更新日'] + 1).setValue(new Date());
    bumpCatalogVer_();
    return { ok: true, replaced: true, title: title };
  }

  var file = bookFolder_(book.uni, form.book).createFile(blob);
  share_(file);
  var row = HEAD.ITEMS.map(function (h) {
    if (h === '問題集名') return form.book;
    if (h === '区分') return KINDS.indexOf(form.kind) >= 0 ? form.kind : 'その他';
    if (h === 'タイトル') return title;
    if (h === 'ファイル') return file.getUrl();
    if (h === '公開') return !!form.publish;
    if (h === '並び順') return orderFor_(form);
    if (h === '更新日') return new Date();
    return '';
  });
  sh.appendRow(row);
  bumpCatalogVer_();
  return { ok: true, replaced: false, title: title };
}

/** サイドバーから呼ばれる：選択行の差し替え（同じファイルIDのまま中身を新しい版にする＝リンクは変わらない） */
function replaceMaterial(form) {
  var sh = sheet_(SHEET.ITEMS);
  var col = colIndex_(sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]);
  var rowNo = Number(form.row);
  var fid = fileIdOf_(sh.getRange(rowNo, col['ファイル'] + 1).getValue());
  if (!fid) throw new Error('この行にはファイルがありません');
  var blob = Utilities.newBlob(Utilities.base64Decode(form.data), 'application/pdf', form.fileName);
  var name = fileNameFor_(sh.getRange(rowNo, col['問題集名'] + 1).getValue(), sh.getRange(rowNo, col['タイトル'] + 1).getValue());
  Drive.Files.update({ name: name }, fid, blob); // 高度なサービス Drive API（v3）。appsscript.json で有効化済み
  sh.getRange(rowNo, col['更新日'] + 1).setValue(new Date());
  bumpCatalogVer_();
  return { ok: true };
}

/**
 * 保存先フォルダの中を見て、まだ登録されていないPDFを「教材」に追加する。
 * フォルダ構成: 保存先フォルダ / 大学 / 問題集名 / *.pdf
 * 区分はファイル名から判定（kakomon/README.md のルール: vol0・manual→戦略編, q1-→大問別, vocab→単語帳, mock→模試）
 */
function menuImport() {
  var root = rootFolder_();
  var known = {};
  var sh = sheet_(SHEET.ITEMS);
  var values = sh.getDataRange().getValues();
  var col = colIndex_(values[0]);
  for (var i = 1; i < values.length; i++) {
    var f = fileIdOf_(values[i][col['ファイル']]);
    if (f) known[f] = true;
  }
  var names = bookIdsByName_();
  var added = 0, newBooks = [];
  var unis = root.getFolders();
  while (unis.hasNext()) {
    var uniFolder = unis.next();
    var bookFolders = uniFolder.getFolders();
    while (bookFolders.hasNext()) {
      var bf = bookFolders.next();
      var bookName = bf.getName();
      if (!names[bookName]) {
        addBookRow_(uniFolder.getName(), bookName);
        names[bookName] = true;
        newBooks.push(bookName);
      }
      var files = bf.getFilesByType(MimeType.PDF);
      var list = [];
      while (files.hasNext()) list.push(files.next());
      list.sort(function (a, b) { return a.getName() < b.getName() ? -1 : 1; });
      list.forEach(function (file) {
        if (known[file.getId()]) return;
        share_(file);
        var spec = specFromFileName_(titleFromFileName_(bookName, file.getName()));
        var title = buildTitle_(spec);
        file.setName(fileNameFor_(bookName, title));
        var row = HEAD.ITEMS.map(function (h) {
          if (h === '問題集名') return bookName;
          if (h === '区分') return spec.kind;
          if (h === 'タイトル') return title;
          if (h === 'ファイル') return file.getUrl();
          if (h === '公開') return false;
          if (h === '並び順') return orderFor_(spec);
          if (h === '更新日') return file.getLastUpdated();
          return '';
        });
        sh.appendRow(row);
        added++;
      });
    }
  }
  fillBookIds_();
  bumpCatalogVer_();
  var msg = added + '件の教材を追加しました（公開は外した状態です。中身を確認して☑公開を付けてください）。';
  if (newBooks.length) msg += '\n新しい問題集も追加しました: ' + newBooks.join('、') + '（グループ・公開を設定してください）';
  SpreadsheetApp.getUi().alert(msg);
}

/** リンク切れ・共有設定ミス・名前の不一致を赤くする。更新日もドライブの最新に合わせる */
function menuCheck() {
  var ss = SpreadsheetApp.getActive();
  var problems = [];
  var red = '#f8d7d3';

  var bs = sheet_(SHEET.BOOKS);
  var bv = bs.getDataRange().getValues();
  var bc = colIndex_(bv[0]);
  var seen = {};
  var bookNames = {};
  bs.getRange(2, 1, Math.max(1, bv.length - 1), bv[0].length).setBackground(null);
  for (var i = 1; i < bv.length; i++) {
    var n = String(bv[i][bc['問題集名']] || '').trim();
    if (!n) continue;
    if (seen[n]) { bs.getRange(i + 1, bc['問題集名'] + 1).setBackground(red); problems.push('問題集名が重複: ' + n); }
    seen[n] = true;
    bookNames[n] = true;
  }

  var is = sheet_(SHEET.ITEMS);
  var iv = is.getDataRange().getValues();
  var ic = colIndex_(iv[0]);
  if (iv.length > 1) is.getRange(2, 1, iv.length - 1, iv[0].length).setBackground(null);
  var titleSeen = {};
  for (var j = 1; j < iv.length; j++) {
    var rowNo = j + 1;
    var bn = String(iv[j][ic['問題集名']] || '').trim();
    if (!bn) continue;
    if (!bookNames[bn]) { is.getRange(rowNo, ic['問題集名'] + 1).setBackground(red); problems.push(rowNo + '行目: 問題集「' + bn + '」が「問題集」シートにない'); }
    var tkey = bn + '\u0000' + String(iv[j][ic['タイトル']]).trim();
    if (titleSeen[tkey]) { is.getRange(rowNo, ic['タイトル'] + 1).setBackground(red); problems.push(rowNo + '行目: 同じ問題集に同じタイトルが2つある（' + iv[j][ic['タイトル']] + '）'); }
    titleSeen[tkey] = true;
    var fid = fileIdOf_(iv[j][ic['ファイル']]);
    if (!fid) { is.getRange(rowNo, ic['ファイル'] + 1).setBackground(red); problems.push(rowNo + '行目: ファイルのリンクがない'); continue; }
    try {
      var file = DriveApp.getFileById(fid);
      if (file.isTrashed()) throw new Error('ゴミ箱');
      if (file.getSharingAccess() !== DriveApp.Access.ANYONE_WITH_LINK) share_(file);
      var expected = fileNameFor_(bn, iv[j][ic['タイトル']]);
      if (file.getName() !== expected) file.setName(expected); // タイトルを直したらファイル名も揃える
      is.getRange(rowNo, ic['更新日'] + 1).setValue(file.getLastUpdated());
    } catch (err) {
      is.getRange(rowNo, ic['ファイル'] + 1).setBackground(red);
      problems.push(rowNo + '行目: ファイルが開けない（削除・権限なし）');
    }
  }

  var us = sheet_(SHEET.USERS);
  var uv = us.getDataRange().getValues();
  var uc = colIndex_(uv[0]);
  var uniNames = {};
  for (var k = 1; k < bv.length; k++) uniNames[String(bv[k][bc['大学']] || '')] = true;
  if (uv.length > 1) us.getRange(2, 1, uv.length - 1, uv[0].length).setBackground(null);
  for (var m = 1; m < uv.length; m++) {
    splitList_(uv[m][uc['購入した問題集']]).forEach(function (n) {
      if (!bookNames[n]) { us.getRange(m + 1, uc['購入した問題集'] + 1).setBackground(red); problems.push('利用者' + (m + 1) + '行目: 購入した問題集「' + n + '」が存在しない'); }
    });
    splitList_(uv[m][uc['購入した大学（セット）']]).forEach(function (u) {
      if (!uniNames[u]) { us.getRange(m + 1, uc['購入した大学（セット）'] + 1).setBackground(red); problems.push('利用者' + (m + 1) + '行目: 大学「' + u + '」が存在しない'); }
    });
  }

  fillBookIds_();
  bumpCatalogVer_();
  bumpUserVer_();
  SpreadsheetApp.getUi().alert(problems.length ? '要修正 ' + problems.length + '件（赤い欄）\n\n' + problems.slice(0, 30).join('\n') : '問題は見つかりませんでした。');
}

/** 最初の1回だけ：シート・入力規則・フォルダ・トリガーを作る（何度実行しても壊れない） */
function menuSetup() {
  var ss = SpreadsheetApp.getActive();
  ensureSheet_(SHEET.BOOKS, HEAD.BOOKS);
  ensureSheet_(SHEET.ITEMS, HEAD.ITEMS);
  ensureSheet_(SHEET.USERS, HEAD.USERS);
  ensureSheet_(SHEET.FAVS, HEAD.FAVS);
  ensureSheet_(SHEET.LOGS, HEAD.LOGS);

  var cs = ss.getSheetByName(SHEET.CONFIG) || ss.insertSheet(SHEET.CONFIG);
  if (cs.getLastRow() === 0) cs.appendRow(['項目', '値', '説明']);
  var existing = {};
  cs.getDataRange().getValues().forEach(function (r) { existing[r[0]] = true; });
  DEFAULT_CONFIG.forEach(function (r) { if (!existing[r[0]]) cs.appendRow(r); });
  cs.setFrozenRows(1);
  CacheService.getScriptCache().remove('cfg');

  rootFolder_();
  applyValidation_();

  var has = ScriptApp.getProjectTriggers().some(function (t) { return t.getHandlerFunction() === 'onSheetEdit'; });
  if (!has) ScriptApp.newTrigger('onSheetEdit').forSpreadsheet(ss).onEdit().create();

  ss.getSheetByName(SHEET.FAVS).hideSheet();
  ss.getSheetByName(SHEET.LOGS).hideSheet();
  bumpCatalogVer_();
  SpreadsheetApp.getUi().alert('セットアップが完了しました。\n「設定」シートの「LINEチャネルID」を入力してください。');
}

function applyValidation_() {
  var bs = sheet_(SHEET.BOOKS), is = sheet_(SHEET.ITEMS), us = sheet_(SHEET.USERS);
  var bc = colIndex_(HEAD.BOOKS), ic = colIndex_(HEAD.ITEMS), uc = colIndex_(HEAD.USERS);
  var groups = splitList_(config_()['グループ順']);
  var N = 2000;

  bs.getRange(2, bc['グループ'] + 1, N).setDataValidation(SpreadsheetApp.newDataValidation().requireValueInList(groups, true).build());
  bs.getRange(2, bc['公開'] + 1, N).setDataValidation(CHECKBOX_());
  bs.getRange(2, bc['サンプル'] + 1, N).setDataValidation(CHECKBOX_());
  bs.getRange(1, bc['ID'] + 1, N + 1).setBackground('#eeeeee').setFontColor('#888888');

  var bookList = bs.getRange(2, bc['問題集名'] + 1, N);
  var uniList = bs.getRange(2, bc['大学'] + 1, N);
  is.getRange(2, ic['問題集名'] + 1, N).setDataValidation(SpreadsheetApp.newDataValidation().requireValueInRange(bookList, true).build());
  is.getRange(2, ic['区分'] + 1, N).setDataValidation(SpreadsheetApp.newDataValidation().requireValueInList(KINDS, true).build());
  is.getRange(2, ic['公開'] + 1, N).setDataValidation(CHECKBOX_());
  is.getRange(1, ic['更新日'] + 1, N + 1).setBackground('#eeeeee');

  us.getRange(2, uc['購入した問題集'] + 1, N).setDataValidation(SpreadsheetApp.newDataValidation().requireValueInRange(bookList, true).setAllowInvalid(true).build());
  us.getRange(2, uc['購入した大学（セット）'] + 1, N).setDataValidation(SpreadsheetApp.newDataValidation().requireValueInRange(uniList, true).setAllowInvalid(true).build());
  us.getRange(2, uc['スタッフ'] + 1, N).setDataValidation(CHECKBOX_());
  us.getRange(2, uc['停止'] + 1, N).setDataValidation(CHECKBOX_());
  us.getRange(1, uc['LINE表示名'] + 1, N + 1, 4).setBackground('#eeeeee');
}

/* ======================================================================
 * 共通ヘルパー
 * ==================================================================== */

/** 値を入れずにチェックボックスにする（insertCheckboxes は FALSE を書き込み、最終行の判定が狂うため使わない） */
function CHECKBOX_() {
  return SpreadsheetApp.newDataValidation().requireCheckbox().build();
}

function sheet_(name) {
  var sh = SpreadsheetApp.getActive().getSheetByName(name);
  if (!sh) throw new Error('シート「' + name + '」がありません。メニューの「初期セットアップ」を実行してください。');
  return sh;
}

function ensureSheet_(name, head) {
  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) sh.appendRow(head);
  sh.getRange(1, 1, 1, head.length).setFontWeight('bold').setBackground('#172642').setFontColor('#ffffff');
  sh.setFrozenRows(1);
  return sh;
}

function colIndex_(headRow) {
  var m = {};
  headRow.forEach(function (h, i) { m[String(h).trim()] = i; });
  return m;
}

function config_() {
  var cache = CacheService.getScriptCache();
  var hit = cache.get('cfg');
  if (hit) return JSON.parse(hit);
  var sh = SpreadsheetApp.getActive().getSheetByName(SHEET.CONFIG);
  var out = {};
  DEFAULT_CONFIG.forEach(function (r) { out[r[0]] = r[1]; });
  if (sh) sh.getDataRange().getValues().slice(1).forEach(function (r) { if (r[0]) out[String(r[0])] = String(r[1]); });
  cache.put('cfg', JSON.stringify(out), 600);
  return out;
}

function setConfig_(key, value) {
  var sh = sheet_(SHEET.CONFIG);
  var values = sh.getDataRange().getValues();
  for (var i = 1; i < values.length; i++) {
    if (values[i][0] === key) { sh.getRange(i + 1, 2).setValue(value); CacheService.getScriptCache().remove('cfg'); return; }
  }
  sh.appendRow([key, value, '']);
  CacheService.getScriptCache().remove('cfg');
}

function rootFolder_() {
  var id = config_()['保存先フォルダID'];
  if (id) { try { return DriveApp.getFolderById(id); } catch (err) { /* 作り直す */ } }
  var folder = DriveApp.createFolder('過去問ポータル（教材PDF）');
  setConfig_('保存先フォルダID', folder.getId());
  return folder;
}

function childFolder_(parent, name) {
  var it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

function bookFolder_(uni, bookName) {
  return childFolder_(childFolder_(rootFolder_(), uni || 'その他'), bookName);
}

function share_(file) {
  file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
}

function fileIdOf_(v) {
  var s = String(v || '').trim();
  if (!s) return '';
  var m = s.match(/\/d\/([A-Za-z0-9_-]{20,})/) || s.match(/[?&]id=([A-Za-z0-9_-]{20,})/);
  if (m) return m[1];
  return /^[A-Za-z0-9_-]{20,}$/.test(s) ? s : '';
}

function bookRow_(name) {
  var values = sheet_(SHEET.BOOKS).getDataRange().getValues();
  var col = colIndex_(values[0]);
  for (var i = 1; i < values.length; i++) {
    if (String(values[i][col['問題集名']]).trim() === name) return { uni: String(values[i][col['大学']] || '') };
  }
  return null;
}

function bookIdsByName_() {
  var values = sheet_(SHEET.BOOKS).getDataRange().getValues();
  var col = colIndex_(values[0]);
  var m = {};
  for (var i = 1; i < values.length; i++) {
    var n = String(values[i][col['問題集名']] || '').trim();
    if (n) m[n] = String(values[i][col['ID']] || '');
  }
  return m;
}

function addBookRow_(uni, name) {
  var row = HEAD.BOOKS.map(function (h) {
    if (h === '大学') return uni;
    if (h === '問題集名') return name;
    if (h === 'グループ') return 'その他';
    if (h === '公開' || h === 'サンプル') return false;
    return '';
  });
  sheet_(SHEET.BOOKS).appendRow(row);
}

/** 問題集のIDが空なら自動で振る（b0001, b0002, …）。一度振ったIDは変えない */
function fillBookIds_() {
  var sh = sheet_(SHEET.BOOKS);
  var values = sh.getDataRange().getValues();
  if (values.length < 2) return;
  var col = colIndex_(values[0]);
  var max = 0;
  values.slice(1).forEach(function (r) {
    var m = String(r[col['ID']] || '').match(/^b(\d+)$/);
    if (m) max = Math.max(max, Number(m[1]));
  });
  for (var i = 1; i < values.length; i++) {
    if (values[i][col['ID']] || !String(values[i][col['問題集名']] || '').trim()) continue;
    max++;
    sh.getRange(i + 1, col['ID'] + 1).setValue('b' + ('000' + max).slice(-4));
  }
}

/**
 * ドライブ上のファイル名は「問題集名_タイトル.pdf」に統一する（例：明治 商学部_大問1 長文読解.pdf）。
 * 生徒がダウンロードしたときに、どの大学の何の教材かが分かるようにするため。
 */
function fileNameFor_(book, title) {
  return (String(book).trim() + '_' + String(title).trim()).replace(/\//g, '／').replace(/[\\:*?"<>|]/g, '・') + '.pdf';
}

/** ファイル名からタイトルを作る。「問題集名_」で始まっていればその部分を外す */
function titleFromFileName_(book, fileName) {
  var base = String(fileName).replace(/\.pdf$/i, '').trim();
  var prefix = String(book).trim() + '_';
  return base.indexOf(prefix) === 0 ? base.slice(prefix.length) : base;
}

/**
 * フォルダから取り込むときに、ファイル名からタイトルの材料を読み取る（kakomon/README.md のファイル名ルール）。
 *   vol0-strategy / manual-p1 → 戦略編、q1-reading / q1-2-reading → 大問1(・2) 長文読解、
 *   vocab → 単語帳、mock-2 → 総合模試 第2回。読み取れないものは「その他」（ファイル名をそのまま名前にする）
 */
var SLUG_SECTION = {
  'reading': '長文読解', 'cloze': '長文空所補充', 'dialogue': '会話文', 'dialogue-cloze': '会話文空所補充',
  'dialogue-order': '対話文整序', 'grammar': '文法・語法', 'grammar-vocab': '文法・語彙', 'sentence-order': '整序英作文',
  'error': '正誤問題', 'translation': '和訳', 'writing': '英作文', 'summary': '要約', 'paraphrase': '同意表現',
  'one-word': '1語補充', 'irrelevant': '不要文選択', 'pronunciation': '発音・アクセント', 'multi-text': '複数資料読解',
  'vocab': '語彙'
};
function specFromFileName_(base) {
  var s = String(base).trim().toLowerCase();
  var m;
  if ((m = s.match(/(?:mock|模試)\D*(\d+)?/))) return { kind: '模試', round: Number(m[1] || 1) };
  if (!/^q\d/.test(s) && /vocab|単語/.test(s)) return { kind: '単語帳' };
  if (/^(vol\.?\s*0|manual|guide|strategy)/.test(s) || /戦略/.test(s)) return { kind: '戦略編' };
  if ((m = s.match(/^q((?:\d+-)*\d+)-([a-z-]+)$/))) {
    var nums = m[1].split('-').map(Number);
    var section = SLUG_SECTION[m[2]];
    if (section) return { kind: '大問別', nums: nums, section: section };
  }
  return { kind: 'その他', free: String(base).trim() };
}

function splitList_(v) {
  return String(v || '').split(/[,、，\n]/).map(function (s) { return s.trim(); }).filter(Boolean);
}

function sha_(s) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, s)
    .map(function (b) { return ('0' + (b & 255).toString(16)).slice(-2); }).join('');
}

function catalogVer_() {
  return PropertiesService.getScriptProperties().getProperty('catalogVer') || bumpCatalogVer_();
}
function bumpCatalogVer_() {
  var v = String(Date.now());
  PropertiesService.getScriptProperties().setProperty('catalogVer', v);
  CacheService.getScriptCache().remove('cfg');
  return v;
}
function userVer_() {
  return PropertiesService.getScriptProperties().getProperty('userVer') || '0';
}
function bumpUserVer_() {
  PropertiesService.getScriptProperties().setProperty('userVer', String(Date.now()));
}

/** CacheService は1件100KBまでなので分割して入れる */
function putChunked_(cache, key, str, ttl) {
  var size = 90000, n = Math.ceil(str.length / size), obj = {};
  for (var i = 0; i < n; i++) obj[key + ':' + i] = str.substr(i * size, size);
  obj[key] = String(n);
  cache.putAll(obj, ttl);
}
function getChunked_(cache, key) {
  var n = Number(cache.get(key));
  if (!n) return null;
  var keys = [];
  for (var i = 0; i < n; i++) keys.push(key + ':' + i);
  var parts = cache.getAll(keys);
  var out = '';
  for (var j = 0; j < n; j++) {
    if (parts[key + ':' + j] == null) return null;
    out += parts[key + ':' + j];
  }
  return out;
}
