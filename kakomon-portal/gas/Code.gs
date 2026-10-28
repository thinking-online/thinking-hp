/**
 * THINKING 過去問ポータル — Google Apps Script（API＋運用メニュー）
 *
 * このファイルはスプレッドシート「【過去問ポータル】DB」に紐づく Apps Script に貼り付ける。
 * 設計の全体像は kakomon-portal/開発ガイド.md を参照。
 *
 * API（Webアプリとしてデプロイ）
 *   GET  ?action=ping
 *   GET  ?action=boot&token=<LINE IDトークン>&etag=<前回のetag>
 *   GET  ?action=boot&key=<確認用リンクのキー>&etag=<前回のetag>   LINEログインなしの確認用（塾生の表示／未購入者の表示）
 *   POST {action:"fav", token, book, on}     お気に入りの登録/解除
 *   POST {action:"log", token, book, title}  閲覧ログ
 *
 * 運用メニュー（スプレッドシート上部「過去問ポータル」）
 *   教材を追加 / 選択行のPDFを差し替え / フォルダから取り込み / 点検 / 初期セットアップ
 */

var VERSION = '1.2.0';

/** シートの構造（列・入力規則・トリガー）を変えたら1つ上げる。シートを開いたときに自動でセットアップが走る */
var SETUP_VERSION = 7;

var SHEET = {
  BOOKS: '問題集',
  ITEMS: '教材',
  UNIS: '大学',
  USERS: '利用者',
  CONFIG: '設定',
  FAVS: 'お気に入り',
  LOGS: '閲覧ログ'
};

var HEAD = {
  BOOKS: ['ID', 'グループ', '大学', '大学よみ', '問題集名', '対応する学部・日程', '検索キーワード', '公開', 'サンプル', '並び順', 'メモ'],
  ITEMS: ['問題集名', '区分', 'タイトル', 'ファイル', '公開', '並び順', '更新日', 'メモ', '無料公開'],
  UNIS: ['大学', '画像', 'ひとこと', 'メモ'],
  USERS: ['LINE表示名', 'LINE ID', '初回アクセス', '最終アクセス', '氏名メモ', '購入した問題集', '購入した大学（セット）', '期限', 'スタッフ', '停止', 'メモ'],
  FAVS: ['LINE ID', '問題集ID', '登録日時'],
  LOGS: ['日時', 'LINE ID', '種別', '問題集ID', 'タイトル']
};

var KINDS = ['戦略編', '大問別', '単語帳', '模試', '解説', 'その他'];

var DEFAULT_CONFIG = [
  ['ポータル名', 'THINKING 合格部屋', '画面上部の名前'],
  ['LINEチャネルID', '', 'LIFFアプリを作ったLINEログインチャネルの「チャネルID」（数字）'],
  ['CAMPUS_API_URL', 'https://script.google.com/macros/s/AKfycbwNuxYxMqk5rv4LXBHmp9QnafbowzEdGgfJv0AcZUXNJoy3zn8pfbFqD_XG0E4f4lJm/exec', '塾生判定に使う THINKING CAMPUS のAPI'],
  ['CAMPUS_URL', 'https://liff.line.me/2010454771-l3vZsfjz', '未登録の塾生に案内する THINKING CAMPUS'],
  ['購入案内URL', 'https://lin.ee/yJ8MFVb', 'ロック中の問題集の「購入はこちら」の飛び先'],
  ['公式LINE_URL', 'https://lin.ee/yJ8MFVb', '問い合わせ先'],
  ['グループ順', 'MARCH,関関同立,日東駒専,産近甲龍,国公立,その他', 'ホームに並ぶ順番（カンマ区切り）'],
  ['問題集リストURL', 'https://thinking-online.com/kakomon-portal/seed/books.csv', '問題集の一覧の元データ（GitHub）。シートを開くと差分が自動で反映される'],
  ['確認用リンク（塾生の表示）', '7ccc70f5d82bdef9e7848168a65cf1cc16d33c84cf3a278810e23aef4491a0d9', 'LINEログインなしで塾生と同じ表示を見るリンクのキー（スタッフ用）。「停止」で無効。新しい文字列を入れるとキーが変わる'],
  ['確認用リンク（未購入者の表示）', '950261aa90e0cd3cf92c0442f1672fce937f9910799634ec985f94d7808dc784', 'LINEログインなしで未購入者（ゲスト）と同じ表示を見るリンクのキー。「停止」で無効。新しい文字列を入れるとキーが変わる'],
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
    if (p.action === 'boot' && p.key) return json_(bootByKey_(p.key, p.etag || ''));
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

  return bootResponse_({ name: me.name, role: '' }, access_(me), favsOf_(me.uid), clientEtag);
}

/**
 * 確認用リンク（LINEログインなし）。スタッフが毎回ログインせずに、塾生の表示・未購入者の表示を確かめるためのもの。
 * キーは設定シートに入れる（64桁の16進ならキーのSHA-256、それ以外はキーそのもの）。お気に入りは端末の中だけに保存する。
 */
function bootByKey_(key, clientEtag) {
  var role = linkRole_(String(key));
  if (!role) return { status: 'unauthorized' };
  var access = { role: role, books: {}, unis: {}, key: 'link.' + role };
  return bootResponse_({ name: '確認用リンク', role: '', link: true }, access, [], clientEtag);
}

function linkRole_(key) {
  if (key.length < 16) return '';
  var cfg = config_();
  var hash = sha_(key);
  var roles = { '確認用リンク（塾生の表示）': 'student', '確認用リンク（未購入者の表示）': 'guest' };
  for (var name in roles) {
    var v = String(cfg[name] || '').trim();
    if (!v || v === '停止') continue;
    if (/^[0-9a-f]{64}$/.test(v) ? v === hash : v === key) return roles[name];
  }
  return '';
}

function bootResponse_(user, access, favs, clientEtag) {
  var cfg = config_();
  var full = catalog_();
  var etag = CATALOG_FORMAT + ':' + full.v + ':' + access.key;
  user.role = access.role;
  var res = {
    status: 'ok',
    user: user,
    favs: favs,
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
    appendSafe_(sh, row);
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
      fr: q[ic['無料公開']] === true,
      d: d instanceof Date ? Utilities.formatDate(d, 'Asia/Tokyo', 'yyyy-MM-dd') : '',
      o: Number(q[ic['並び順']]) || 9999
    });
  }

  books.sort(function (a, b) { return a.o - b.o; });
  items.sort(function (a, b) { return a.o - b.o; });
  var full = { v: v, groups: groups, kinds: KINDS, books: books, items: items, unis: uniCatalog_() };
  putChunked_(cache, 'cat:' + v, JSON.stringify(full), 21600);
  return full;
}

/** 一覧の形を変えたら1つ上げる（端末に残った古い一覧を取り直させる） */
var CATALOG_FORMAT = 2;

/** 本人が見てよい範囲だけを返す。ロック中の問題集は目次（区分・タイトル）だけ送り、ファイルIDは送らない */
function filterCatalog_(full, acc) {
  var staff = acc.role === 'staff';
  var open = {};
  var shown = {};
  var books = [];
  full.books.forEach(function (b) {
    if (!b.p && !staff) return;
    var allowed = staff || acc.role === 'student' || b.s || acc.books[b.id] || acc.unis[b.u];
    if (allowed) open[b.id] = true;
    shown[b.id] = true;
    books.push({ id: b.id, g: b.g, u: b.u, uy: b.uy, n: b.n, cov: b.cov, kw: b.kw, s: b.s, L: !allowed, h: !b.p });
  });
  var items = full.items
    .filter(function (it) { return (open[it.b] && (it.p || staff)) || (it.p && shown[it.b]); })
    .map(function (it) {
      if (open[it.b] || it.fr) return { b: it.b, k: it.k, t: it.t, f: it.f, d: it.d, h: !it.p, fr: it.fr || undefined };
      return { b: it.b, k: it.k, t: it.t, d: it.d, L: 1 };
    });
  var unis = {};
  books.forEach(function (b) { if (full.unis && full.unis[b.u]) unis[b.u] = full.unis[b.u]; });
  return { groups: full.groups, kinds: full.kinds, books: books, items: items, unis: unis };
}

/** 大学ごとの画像（ドライブのファイルID）とひとこと。返り値: {大学名: {i, c}}（どちらもないときは載せない） */
function uniCatalog_() {
  var sh = SpreadsheetApp.getActive().getSheetByName(SHEET.UNIS);
  var out = {};
  if (!sh || sh.getLastRow() < 2) return out;
  var v = sh.getDataRange().getValues();
  var c = colIndex_(v[0]);
  for (var i = 1; i < v.length; i++) {
    var name = String(v[i][c['大学']] || '').trim();
    var img = fileIdOf_(v[i][c['画像']]);
    var note = String(v[i][c['ひとこと']] || '').trim();
    if (name && (img || note)) out[name] = { i: img || undefined, c: note || undefined };
  }
  return out;
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
    if (on) appendSafe_(sh, [uid, book, new Date()]);
    return { status: 'ok', on: on };
  } finally {
    lock.releaseLock();
  }
}

function appendLog_(uid, kind, book, title) {
  appendSafe_(sheet_(SHEET.LOGS), [new Date(), uid, kind, book, title]);
}

/* ======================================================================
 * 運用メニュー
 * ==================================================================== */

function onOpen() {
  SpreadsheetApp.getUi().createMenu('過去問ポータル')
    .addItem('フォルダから取り込み（目次どおりに登録）', 'menuImport')
    .addItem('教材を1つ追加・差し替え', 'menuUpload')
    .addSeparator()
    .addItem('点検（リンク切れ・設定ミスを探す）', 'menuCheck')
    .addItem('問題集リストを最新にする', 'menuSyncBooks')
    .addItem('今すぐ全員に反映', 'menuPublish')
    .addSeparator()
    .addItem('初期セットアップ（通常は自動）', 'menuSetup')
    .addToUi();
}

/** シートが編集されたら一覧の版を上げる（installable トリガー。セットアップで登録） */
function onSheetEdit(e) {
  var name = e && e.range ? e.range.getSheet().getName() : '';
  if (name === SHEET.USERS) bumpUserVer_();
  if (name === SHEET.BOOKS) { fillBookIds_(); fillUniRows_(); }
  if (name === SHEET.BOOKS || name === SHEET.ITEMS || name === SHEET.CONFIG || name === SHEET.UNIS) bumpCatalogVer_();
}

function menuPublish() {
  fillBookIds_();
  bumpCatalogVer_();
  bumpUserVer_();
  SpreadsheetApp.getActive().toast('全員の画面に反映しました（次にポータルを開いたときに最新になります）', '過去問ポータル', 5);
}

function menuUpload() {
  SpreadsheetApp.getUi().showSidebar(HtmlService.createHtmlOutputFromFile('Upload').setTitle('教材を1つ追加・差し替え'));
}

/** サイドバー用：問題集の一覧と、問題集ごとの登録済みタイトル */
function getUploadOptions() {
  var bv = sheet_(SHEET.BOOKS).getDataRange().getValues();
  var bc = colIndex_(bv[0]);
  var names = [];
  for (var i = 1; i < bv.length; i++) {
    var n = String(bv[i][bc['問題集名']] || '').trim();
    if (n) names.push(n);
  }
  var existing = {};
  itemRows_().forEach(function (r) { (existing[r.book] = existing[r.book] || []).push(r.title); });
  return { books: names, kinds: KINDS, existing: existing };
}

/**
 * サイドバーから呼ばれる。
 *   mode=replace : 登録済みの教材（book＋title）の中身を新しい版にする（リンクは変わらない）
 *   mode=add     : 新しく1つ登録する。タイトルは PDF の表紙・目次と同じ名前にする
 * 同じタイトルがすでにあれば、追加ではなく差し替えになる。
 */
function uploadMaterial(form) {
  var book = bookRow_(form.book);
  if (!book) throw new Error('問題集「' + form.book + '」が見つかりません');
  var title = normalizeTitle_(form.title);
  if (!title) throw new Error('タイトルがありません');
  var blob = Utilities.newBlob(Utilities.base64Decode(form.data), 'application/pdf', fileNameFor_(form.book, title));

  var hit = itemRows_().filter(function (r) { return r.book === form.book && r.title === title && r.fid; })[0];
  if (hit) {
    replaceContent_(hit, blob);
    bumpCatalogVer_();
    return { ok: true, replaced: true, title: title };
  }
  if (form.mode === 'replace') throw new Error('差し替える教材が見つかりません');

  var file = bookFolder_(book.uni, form.book).createFile(blob);
  share_(file);
  appendItem_(form.book, KINDS.indexOf(form.kind) >= 0 ? form.kind : kindOf_(title, ''), title, file, !!form.publish, nextOrder_(form.book));
  bumpCatalogVer_();
  return { ok: true, replaced: false, title: title };
}

/**
 * 保存先フォルダ / 大学 / 問題集名 / の中を見て、教材を登録する。
 * タイトルと並び順は、同じフォルダにある目次（links.txt など .txt）から取る。目次は問題集を作るときに一緒にできる
 * 「見出し → タイトルの行 → URLの行」の形式（kakomon/<大学>/links.txt と同じ）。URLの最後のファイル名でPDFと対応づける。
 *   ・目次にあって未登録のPDF        → 追加（公開は外した状態）
 *   ・目次のタイトルがすでに登録済み → 新しいPDFの中身で差し替え（リンクは変わらない）、置いたPDFはゴミ箱へ
 *   ・目次がない／目次にないPDF      → ファイル名を仮のタイトルにして「その他」で追加し、知らせる
 */
function menuImport() {
  SpreadsheetApp.getUi().alert(importCore_());
}

// Apps Script は1回の実行が約6分で強制終了されるので、その前に区切って「もう一度実行」を案内する
var IMPORT_BUDGET_MS = 4.5 * 60 * 1000;

function importCore_() {
  var started = Date.now();
  var root = rootFolder_();
  var rows = itemRows_();
  var known = {};
  rows.forEach(function (r) { if (r.fid) known[r.fid] = true; });
  var names = bookIdsByName_();
  var added = 0, replaced = 0, images = 0, newBooks = [], notes = [], unfinished = false;
  var uniImgs = uniImageMap_();
  function outOfTime() { return unfinished || (unfinished = Date.now() - started > IMPORT_BUDGET_MS); }

  var unis = root.getFolders();
  while (unis.hasNext() && !outOfTime()) {
    var uniFolder = unis.next();
    if (importUniImage_(uniFolder, uniImgs)) images++;
    var bookFolders = uniFolder.getFolders();
    while (bookFolders.hasNext() && !outOfTime()) {
      var bf = bookFolders.next();
      var bookName = bf.getName();
      if (!names[bookName]) { addBookRow_(uniFolder.getName(), bookName); names[bookName] = true; newBooks.push(bookName); }

      var pdfs = {};
      var it = bf.getFilesByType(MimeType.PDF);
      while (it.hasNext()) {
        var f = it.next();
        if (known[f.getId()]) continue;
        var prev = pdfs[f.getName()];
        if (!prev || prev.getLastUpdated() < f.getLastUpdated()) pdfs[f.getName()] = f;
      }
      if (!Object.keys(pdfs).length) continue;

      var toc = readToc_(bf);
      var byTitle = {};
      rows.forEach(function (r) { if (r.book === bookName) byTitle[r.title] = r; });

      toc.forEach(function (e) {
        var file = pdfs[e.file];
        if (!file) return;
        delete pdfs[e.file];
        if (outOfTime()) return; // 残りは次の実行で（ファイルはフォルダに残っている）
        var hit = byTitle[e.title];
        if (hit && hit.fid) {
          replaceContent_(hit, file.getBlob());
          file.setTrashed(true);
          replaced++;
          return;
        }
        // 先に登録する。途中で止まっても登録済みなら次の実行で二重に入らない（共有・名前は「点検」でも直る）
        appendItem_(bookName, e.kind, e.title, file, false, e.order);
        share_(file);
        file.setName(fileNameFor_(bookName, e.title));
        added++;
      });

      Object.keys(pdfs).forEach(function (name) {
        if (outOfTime()) return;
        var file = pdfs[name];
        var title = normalizeTitle_(name.replace(/\.pdf$/i, ''));
        appendItem_(bookName, 'その他', title, file, false, nextOrder_(bookName));
        share_(file);
        added++;
        notes.push(bookName + '：「' + name + '」は目次にないため仮のタイトルで追加しました');
      });
    }
  }
  fillBookIds_();
  fillUniRows_();
  bumpCatalogVer_();
  var msg = '追加 ' + added + '件 ／ 差し替え ' + replaced + '件\n（追加したものは公開を外した状態です。中身を確認して☑公開を付けてください）';
  if (images) msg += '\n\n大学の画像を ' + images + '件 登録しました（すぐに全員の画面に出ます）';
  if (unfinished) msg = '【まだ途中です】時間の上限が近いので、ここで区切りました。もう一度「フォルダから取り込み」を実行してください（続きから進みます）。\n\n' + msg;
  if (newBooks.length) msg += '\n\n新しい問題集を追加しました: ' + newBooks.join('、') + '（グループ・公開を設定してください）';
  if (notes.length) msg += '\n\n' + notes.join('\n');
  return msg;
}

/** 目次（.txt）を読む。返り値: [{title, kind, file, order}] */
function readToc_(folder) {
  var it = folder.getFilesByType(MimeType.PLAIN_TEXT);
  while (it.hasNext()) {
    var out = parseToc_(it.next().getBlob().getDataAsString('UTF-8'));
    if (out.length) return out;
  }
  return [];
}

/** 目次の文字列を読む。返り値: [{title, kind, file, order}] */
function parseToc_(text) {
  var out = [];
  {
    var lines = String(text).split(/\r?\n/);
    var section = '', pending = '';
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].trim();
      if (!line) continue;
      var h = line.match(/^-{2,}\s*(.+?)\s*-{2,}$/);
      if (h) {
        section = h[1];
        if (/URLのみ/.test(section)) break;
        pending = '';
        continue;
      }
      var u = line.match(/^https?:\/\/\S*\/([^\/\s?#]+\.pdf)/i);
      if (u) {
        if (pending) {
          var title = normalizeTitle_(pending);
          out.push({ title: title, kind: kindOf_(title, section), file: decodeURIComponent(u[1]), order: (out.length + 1) * 10 });
        }
        pending = '';
        continue;
      }
      pending = line; // URL の直前の行がタイトル
    }
  }
  return out;
}

/** 区分はタイトルと見出しから決める（模試・単語帳・戦略編・解説、それ以外は大問別） */
function kindOf_(title, section) {
  if (/模試/.test(title)) return '模試';
  if (/単語|熟語帳/.test(title)) return '単語帳';
  if (/^Vol\.0\b|戦略|分析|マニュアル/.test(title)) return '戦略編';
  if (/解説/.test(title) || /解説/.test(section)) return '解説';
  return '大問別';
}

/** 「Vol0 全体戦略」「vol.0全体戦略」→「Vol.0 全体戦略」。それ以外は前後の空白を取るだけ */
function normalizeTitle_(t) {
  return String(t || '').trim().replace(/^vol\s*\.?\s*(\d+)\s*/i, 'Vol.$1 ').trim();
}

/** 「教材」シートの行を読む */
function itemRows_() {
  var values = sheet_(SHEET.ITEMS).getDataRange().getValues();
  var col = colIndex_(values[0]);
  var out = [];
  for (var i = 1; i < values.length; i++) {
    var book = String(values[i][col['問題集名']] || '').trim();
    if (!book) continue;
    out.push({ rowNo: i + 1, book: book, title: String(values[i][col['タイトル']] || '').trim(), fid: fileIdOf_(values[i][col['ファイル']]), order: Number(values[i][col['並び順']]) || 0 });
  }
  return out;
}

/** 戦略編（Vol.0）は最初から無料公開にする（購入前に読める入口にするため。外したければ☑を外す） */
function appendItem_(book, kind, title, file, publish, order) {
  var row = HEAD.ITEMS.map(function (h) {
    if (h === '問題集名') return book;
    if (h === '区分') return kind;
    if (h === 'タイトル') return title;
    if (h === 'ファイル') return file.getUrl();
    if (h === '公開') return publish;
    if (h === '並び順') return order;
    if (h === '更新日') return new Date();
    if (h === '無料公開') return kind === '戦略編';
    return '';
  });
  appendSafe_(sheet_(SHEET.ITEMS), row);
}

/** 登録済みの教材の中身を新しい版にする（同じファイルIDのまま＝リンクは変わらない） */
function replaceContent_(row, blob) {
  Drive.Files.update({ name: fileNameFor_(row.book, row.title) }, row.fid, blob); // 高度なサービス Drive API（v3）
  var sh = sheet_(SHEET.ITEMS);
  var col = colIndex_(sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]);
  sh.getRange(row.rowNo, col['更新日'] + 1).setValue(new Date());
}

function nextOrder_(book) {
  var max = 0;
  itemRows_().forEach(function (r) { if (r.book === book) max = Math.max(max, r.order); });
  return max + 10;
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

  var ush = ss.getSheetByName(SHEET.UNIS);
  if (ush && ush.getLastRow() > 1) {
    var uvv = ush.getDataRange().getValues();
    var ucc = colIndex_(uvv[0]);
    ush.getRange(2, 1, uvv.length - 1, uvv[0].length).setBackground(null);
    for (var x = 1; x < uvv.length; x++) {
      var uname = String(uvv[x][ucc['大学']] || '').trim();
      if (uname && !uniNames[uname]) { ush.getRange(x + 1, ucc['大学'] + 1).setBackground(red); problems.push('大学シート' + (x + 1) + '行目: 大学「' + uname + '」が問題集シートにない'); }
      if (!String(uvv[x][ucc['画像']] || '').trim()) continue;
      var imgId = fileIdOf_(uvv[x][ucc['画像']]);
      try {
        if (!imgId) throw new Error('リンクの形が違う');
        var img = DriveApp.getFileById(imgId);
        if (img.isTrashed()) throw new Error('ゴミ箱');
        if (!/^image\//.test(img.getMimeType())) throw new Error('画像ではない');
        if (img.getSharingAccess() !== DriveApp.Access.ANYONE_WITH_LINK) share_(img);
      } catch (err) {
        ush.getRange(x + 1, ucc['画像'] + 1).setBackground(red);
        problems.push('大学シート' + (x + 1) + '行目: 「' + uname + '」の画像が開けない（' + err.message + '）');
      }
    }
  }

  fillBookIds_();
  fillUniRows_();
  bumpCatalogVer_();
  bumpUserVer_();
  SpreadsheetApp.getUi().alert(problems.length ? '要修正 ' + problems.length + '件（赤い欄）\n\n' + problems.slice(0, 30).join('\n') : '問題は見つかりませんでした。');
}

/** 最初の1回だけ手で実行する。以後はシートを開いたときに必要な分だけ自動で走る（何度実行しても壊れない） */
function menuSetup() {
  setupCore_();
  PropertiesService.getScriptProperties().setProperty('setupVer', String(SETUP_VERSION));
  syncBooks_(true);
  SpreadsheetApp.getUi().alert('セットアップが完了しました。');
}

/**
 * シートを開いたとき（installable トリガー）。
 * ① コードが新しくなってシートの構造が古ければセットアップし直す
 * ② GitHub の問題集リストが変わっていれば反映する
 * どちらも変化がなければ何もしない（開くのが遅くならないように）
 */
function onOpenInstalled() {
  var props = PropertiesService.getScriptProperties();
  if (Number(props.getProperty('setupVer') || 0) < SETUP_VERSION) {
    setupCore_();
    props.setProperty('setupVer', String(SETUP_VERSION));
  }
  var res = syncBooks_(false);
  if (res && res.changed) SpreadsheetApp.getActive().toast(res.summary, '問題集リストを更新しました', 8);
}

function setupCore_() {
  var ss = SpreadsheetApp.getActive();
  ensureSheet_(SHEET.BOOKS, HEAD.BOOKS);
  ensureSheet_(SHEET.ITEMS, HEAD.ITEMS);
  ensureSheet_(SHEET.UNIS, HEAD.UNIS);
  ensureSheet_(SHEET.USERS, HEAD.USERS);
  ensureSheet_(SHEET.FAVS, HEAD.FAVS);
  ensureSheet_(SHEET.LOGS, HEAD.LOGS);

  var cs = ss.getSheetByName(SHEET.CONFIG) || ss.insertSheet(SHEET.CONFIG);
  if (cs.getLastRow() === 0) appendSafe_(cs, ['項目', '値', '説明']);
  var existing = {};
  cs.getDataRange().getValues().forEach(function (r) { existing[r[0]] = true; });
  DEFAULT_CONFIG.forEach(function (r) { if (!existing[r[0]]) appendSafe_(cs, r); });
  cs.setFrozenRows(1);
  CacheService.getScriptCache().remove('cfg');

  // 問題集リストの読み込み先を GitHub からホームページに移す（リポジトリを非公開にしても読めるように）
  if (/raw\.githubusercontent\.com/.test(config_()['問題集リストURL'])) setConfig_('問題集リストURL', 'https://thinking-online.com/kakomon-portal/seed/books.csv');
  // グループに「国公立」を足す（その他の前）
  var groups = splitList_(config_()['グループ順']);
  if (groups.indexOf('国公立') < 0) {
    var at = groups.indexOf('その他');
    groups.splice(at < 0 ? groups.length : at, 0, '国公立');
    setConfig_('グループ順', groups.join(','));
  }

  // 表示名を「THINKING 合格部屋」に変える（2026/10。運営が手で変えた名前はそのまま）
  if (config_()['ポータル名'] === 'THINKING 過去問ポータル') setConfig_('ポータル名', 'THINKING 合格部屋');

  rootFolder_();
  fillUniRows_();
  applyValidation_();

  var handlers = ScriptApp.getProjectTriggers().map(function (t) { return t.getHandlerFunction(); });
  if (handlers.indexOf('onSheetEdit') < 0) ScriptApp.newTrigger('onSheetEdit').forSpreadsheet(ss).onEdit().create();
  if (handlers.indexOf('onOpenInstalled') < 0) ScriptApp.newTrigger('onOpenInstalled').forSpreadsheet(ss).onOpen().create();

  ss.getSheetByName(SHEET.FAVS).hideSheet();
  ss.getSheetByName(SHEET.LOGS).hideSheet();
  bumpCatalogVer_();
}

function menuSyncBooks() {
  var res = syncBooks_(true);
  SpreadsheetApp.getUi().alert(res.changed ? res.summary : '問題集リストは最新です。');
}

/**
 * GitHub の問題集リスト（seed/books.csv）を「問題集」シートに反映する。問題集名で突き合わせる。
 *   ・シートにない問題集 → 追加（公開・サンプルは外した状態）
 *   ・ある問題集 → グループ・大学・大学よみ・対応する学部・日程・検索キーワード・並び順をリストに合わせる
 *     （公開・サンプル・メモ・IDは触らない）
 *   ・グループが「削除」の行 → その問題集をシートから消す。教材が登録済みなら消さずに赤くして知らせる
 *   ・リストにない問題集（スタッフが手で足したもの）→ 触らない
 * force=false のときは、前回反映したリストから変わっていなければ何もしない。
 */
function syncBooks_(force) {
  var url = config_()['問題集リストURL'];
  if (!url) return { changed: false };
  var text;
  try {
    var r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return { changed: false };
    text = r.getContentText('UTF-8');
  } catch (err) {
    return { changed: false };
  }
  var props = PropertiesService.getScriptProperties();
  var hash = sha_(text);
  if (!force && props.getProperty('booksHash') === hash) return { changed: false };

  var list = Utilities.parseCsv(text.replace(/^﻿/, ''));
  var sh = sheet_(SHEET.BOOKS);
  var values = sh.getDataRange().getValues();
  var col = colIndex_(values[0]);
  var rowOf = {};
  for (var i = 1; i < values.length; i++) {
    var n = String(values[i][col['問題集名']] || '').trim();
    if (n) rowOf[n] = i + 1;
  }
  var used = {};
  itemRows_().forEach(function (it) { used[it.book] = true; });

  var FIELDS = ['グループ', '大学', '大学よみ', '対応する学部・日程', '検索キーワード', '並び順'];
  var added = [], updated = 0, removed = [], kept = [];
  var toDelete = [];
  list.forEach(function (c) {
    if (c.length < 10) return;
    var rec = { 'グループ': c[1], '大学': c[2], '大学よみ': c[3], '問題集名': String(c[4]).trim(), '対応する学部・日程': c[5], '検索キーワード': c[6], '並び順': Number(c[9]) || '' };
    var name = rec['問題集名'];
    if (!name) return;
    var rowNo = rowOf[name];
    if (rec['グループ'] === '削除') {
      if (!rowNo) return;
      if (used[name]) { sh.getRange(rowNo, col['問題集名'] + 1).setBackground('#f8d7d3'); kept.push(name); }
      else { toDelete.push(rowNo); removed.push(name); }
      return;
    }
    if (!rowNo) {
      var row = HEAD.BOOKS.map(function (h) {
        if (h === '公開' || h === 'サンプル') return false;
        return rec[h] !== undefined ? rec[h] : '';
      });
      appendSafe_(sh, row);
      added.push(name);
      return;
    }
    var diff = false;
    FIELDS.forEach(function (f) {
      var cell = sh.getRange(rowNo, col[f] + 1);
      if (String(cell.getValue()) !== String(rec[f])) { cell.setValue(rec[f]); diff = true; }
    });
    if (diff) updated++;
  });
  toDelete.sort(function (a, b) { return b - a; }).forEach(function (rowNo) { sh.deleteRow(rowNo); });

  fillBookIds_();
  fillUniRows_();
  bumpCatalogVer_();
  props.setProperty('booksHash', hash);
  var parts = [];
  if (added.length) parts.push('追加 ' + added.length + '件（' + added.join('、') + '）');
  if (updated) parts.push('更新 ' + updated + '件');
  if (removed.length) parts.push('削除 ' + removed.length + '件（' + removed.join('、') + '）');
  if (kept.length) parts.push('教材があるため削除しなかったもの: ' + kept.join('、') + '（赤い欄。教材を移してから消してください）');
  return { changed: parts.length > 0, summary: parts.join('\n') };
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
  is.getRange(2, ic['無料公開'] + 1, N).setDataValidation(CHECKBOX_());
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

/**
 * データの直後の行に書く。appendRow は使わない（チェックボックスに FALSE が残った行や、
 * 他の方法で広がった行の下に入ってしまうことがあるため）。空文字と FALSE だけの行は空行とみなす。
 */
function appendSafe_(sh, row) {
  var last = sh.getLastRow();
  if (last > 1) {
    var vals = sh.getRange(2, 1, last - 1, row.length).getValues();
    var i = vals.length;
    while (i > 0 && vals[i - 1].every(function (v) { return v === '' || v === false; })) i--;
    last = i + 1;
  }
  sh.getRange(last + 1, 1, 1, row.length).setValues([row]);
}

function sheet_(name) {
  var sh = SpreadsheetApp.getActive().getSheetByName(name);
  if (!sh) throw new Error('シート「' + name + '」がありません。メニューの「初期セットアップ」を実行してください。');
  return sh;
}

function ensureSheet_(name, head) {
  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) appendSafe_(sh, head);
  // 後から増えた列は右端に足す（列は見出しの名前で探すので、既存のデータは動かない）
  var have = sh.getRange(1, 1, 1, Math.max(1, sh.getLastColumn())).getValues()[0].map(String);
  head.forEach(function (h) { if (have.indexOf(h) < 0) { sh.getRange(1, have.length + 1).setValue(h); have.push(h); } });
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
  appendSafe_(sh, [key, value, '']);
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
  appendSafe_(sheet_(SHEET.BOOKS), row);
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

/** 「大学」シートに、問題集シートにある大学をすべて並べる（足りない行だけ足す。画像・ひとことは触らない） */
function fillUniRows_() {
  var ss = SpreadsheetApp.getActive();
  var us = ss.getSheetByName(SHEET.UNIS);
  if (!us) return;
  var have = {};
  if (us.getLastRow() > 1) us.getRange(2, 1, us.getLastRow() - 1, 1).getValues().forEach(function (r) { have[String(r[0]).trim()] = true; });
  var bv = sheet_(SHEET.BOOKS).getDataRange().getValues();
  var bc = colIndex_(bv[0]);
  for (var i = 1; i < bv.length; i++) {
    var u = String(bv[i][bc['大学']] || '').trim();
    if (!u || have[u]) continue;
    have[u] = true;
    appendSafe_(us, HEAD.UNIS.map(function (h) { return h === '大学' ? u : ''; }));
  }
}

/** 返り値: {大学名: {row, fid}}（「大学」シートの画像欄の今の値） */
function uniImageMap_() {
  var us = SpreadsheetApp.getActive().getSheetByName(SHEET.UNIS);
  var m = {};
  if (!us || us.getLastRow() < 2) return m;
  var v = us.getDataRange().getValues();
  var c = colIndex_(v[0]);
  for (var i = 1; i < v.length; i++) {
    var u = String(v[i][c['大学']] || '').trim();
    if (u) m[u] = { row: i + 1, fid: fileIdOf_(v[i][c['画像']]) };
  }
  return m;
}

/**
 * 大学のフォルダ（直下）に置いた画像を、その大学の画像として登録する。
 * 画像が複数あれば一番新しいもの。登録済みの画像と同じなら何もしない。返り値: 登録したら true
 */
function importUniImage_(uniFolder, map) {
  var latest = null;
  var files = uniFolder.getFiles();
  while (files.hasNext()) {
    var f = files.next();
    if (!/^image\//.test(f.getMimeType()) || f.isTrashed()) continue;
    if (!latest || latest.getLastUpdated() < f.getLastUpdated()) latest = f;
  }
  if (!latest) return false;
  var uni = uniFolder.getName();
  var cur = map[uni];
  if (cur && cur.fid === latest.getId()) return false;
  share_(latest);
  var us = sheet_(SHEET.UNIS);
  var col = colIndex_(HEAD.UNIS);
  var url = 'https://drive.google.com/file/d/' + latest.getId() + '/view';
  if (cur) us.getRange(cur.row, col['画像'] + 1).setValue(url);
  else {
    appendSafe_(us, HEAD.UNIS.map(function (h) { return h === '大学' ? uni : h === '画像' ? url : ''; }));
    map[uni] = { row: us.getLastRow(), fid: latest.getId() };
  }
  if (cur) cur.fid = latest.getId();
  return true;
}

/**
 * ドライブ上のファイル名は「問題集名_タイトル.pdf」に統一する（例：明治 商学部_大問1 長文読解.pdf）。
 * 生徒がダウンロードしたときに、どの大学の何の教材かが分かるようにするため。
 */
function fileNameFor_(book, title) {
  return (String(book).trim() + '_' + String(title).trim()).replace(/\//g, '／').replace(/[\\:*?"<>|]/g, '・') + '.pdf';
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
