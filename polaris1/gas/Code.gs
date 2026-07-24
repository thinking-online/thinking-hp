/**
 * 英文法ポラリス1 完成問題集 ｜ 単元別フォーム自動生成ツール（GAS・全問マーク式版）
 * ------------------------------------------------------------------
 * マスターCSVを取り込んだスプレッドシートに紐づけて使います。
 * 全375問がマーク式（選択式）なので、Forms APIなどの追加設定は不要。
 * 単元（ユニット）ごとに Google フォーム（自動採点クイズ）を作成します。
 *
 * 【使い方】
 *   1. マスターCSV（英文法ポラリス1_問題集マスター.csv）を Google スプレッドシートに
 *      インポートする（1行目が見出し行）。
 *   2. 拡張機能 → Apps Script を開き、このコードを貼り付けて保存。
 *   3. スプレッドシートを再読み込みすると、メニュー「📝 フォーム作成」が出ます。
 *   4. メニューから作成したい範囲を選ぶ（初回はGoogleアカウントの承認が必要）。
 *
 * すべて選択式なので、空所補充・整序（正しい英文を選ぶ）・誤文訂正（下線部を選ぶ）・
 * 記述（語を選ぶ）のいずれも「自動採点」されます。
 */

// ===== 設定 =========================================================
var CONFIG = {
  SHEET_NAME: '',                              // 問題データのシート名。空なら「問題」または先頭シート
  FOLDER_ID: '1LlK8Ns9ounNfBMkYYtVhYayNJRfkOZxu', // 作成フォームの保存先フォルダID（空なら下のFOLDER_NAMEで作成）
  FOLDER_NAME: '英文法ポラリス1_単元フォーム',   // FOLDER_IDが空のときに作る/使うフォルダ名
  LIST_SHEET: 'フォーム一覧',                   // 作成フォームのURL出力先シート
  POINTS: 1,                                   // 1問あたりの配点
  INCLUDE_EXPLANATION: true,                   // フィードバックに解説を載せる
  SHUFFLE: false,                              // 問題の順番をシャッフル
  COLLECT_EMAIL: false,                        // 回答者メールの収集
  TITLE_PREFIX: '基礎英文法テスト｜',           // フォームのタイトル接頭辞（例: 基礎英文法テスト｜UNIT 1 時制(1)）
  AUTO_CONTINUE: true,                         // 一括作成が時間切れになったら約1分後に自動で続きを作成する
  MAX_RUNTIME_MS: 300000                       // 1回の実行で作業する上限（5分）。GASの6分制限より手前で安全停止
};

var COL = {
  num: '番号', chapter: 'チャプター', unit: 'ユニット', type: '形式', question: '問題文',
  c1: '選択肢1', c2: '選択肢2', c3: '選択肢3', c4: '選択肢4', c5: '選択肢5', c6: '選択肢6',
  answer: '正解', answerText: '正解の内容',
  kanseibun: '完成文', yaku: '訳', point: 'POINT',
  kaisetsu: '解説', check: '誤答チェック・補足', biko: '備考'
};

// ===== メニュー =====================================================
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('📝 フォーム作成')
    .addItem('選択中の行の「単元」を作成', 'createFormForActiveRow')
    .addItem('単元名を指定して作成', 'createFormForNamedUnit')
    .addSeparator()
    .addItem('チャプターを指定して一括作成', 'createFormsForChapter')
    .addItem('全単元を一括作成（続きから再開）', 'createAllForms')
    .addItem('自動作成を停止', 'stopAutoContinue')
    .addSeparator()
    .addItem('データの読み込みを確認', 'previewData')
    .addToUi();
}

// ===== データ読み込み ================================================
function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (CONFIG.SHEET_NAME) {
    var s = ss.getSheetByName(CONFIG.SHEET_NAME);
    if (s) return s;
  }
  var byName = ss.getSheetByName('問題');
  if (byName) return byName;
  return ss.getSheets()[0];
}

function getData_() {
  var sh = getSheet_();
  var values = sh.getDataRange().getValues();
  if (values.length < 2) throw new Error('データが見つかりません。1行目に見出し、2行目以降に問題を入れてください。');
  var header = values[0].map(function(h){ return String(h).trim(); });
  var idx = {};
  header.forEach(function(h, i){ idx[h] = i; });
  [COL.num, COL.unit, COL.question, COL.answer].forEach(function(need){
    if (!(need in idx)) throw new Error('必要な列「' + need + '」が見つかりません。見出し行を確認してください。');
  });
  var rows = [];
  for (var r = 1; r < values.length; r++) {
    if (!String(values[r][idx[COL.num]]).trim()) continue;
    var obj = {};
    header.forEach(function(h){ obj[h] = (idx[h] != null) ? String(values[r][idx[h]]) : ''; });
    rows.push(obj);
  }
  return rows;
}

function previewData() {
  var rows = getData_();
  var units = {}, order = [];
  rows.forEach(function(r){
    var u = r[COL.unit];
    if (!(u in units)) { units[u] = 0; order.push(u); }
    units[u]++;
  });
  var lines = order.map(function(u){ return '・' + u + '（' + units[u] + '問）'; });
  SpreadsheetApp.getUi().alert('読み込み結果',
    '合計 ' + rows.length + ' 問 ／ ' + order.length + ' 単元\n\n' + lines.join('\n'),
    SpreadsheetApp.getUi().ButtonSet.OK);
}

// ===== エントリーポイント ===========================================
/**
 * 全単元を一括作成（レジューム対応）。
 * ・1件ずつ作成して、その都度「フォーム一覧」シートに追記（途中で止まっても進捗が残る）
 * ・すでに作成済みの単元はスキップ（＝続きから再開）
 * ・GASの実行時間制限にかかる手前で安全停止
 * ・CONFIG.AUTO_CONTINUE=true なら約1分後に自動で続きを作成し、全部終わると自動停止
 */
function createAllForms() {
  var start = Date.now();
  var groups = groupByUnit_(getData_());
  var total = groups.order.length;
  var sh = ensureListSheet_();
  var doneSet = getDoneTitles_(sh);

  var remaining = groups.order.filter(function(u){ return !doneSet[CONFIG.TITLE_PREFIX + u]; });
  if (!remaining.length) {
    removeContinueTriggers_();
    toast_('全 ' + total + ' 単元、すでに作成済みです。');
    return;
  }

  for (var i = 0; i < remaining.length; i++) {
    if (Date.now() - start > CONFIG.MAX_RUNTIME_MS) break;  // 時間切れ手前で停止
    var u = remaining[i];
    var res;
    try { res = buildForm_(u, groups.map[u]); }
    catch (e) { res = { unit: u, title: CONFIG.TITLE_PREFIX + u, error: String(e), tab: getSheet_().getName() }; }
    writeOne_(sh, res);        // 1件ずつ即追記（途中終了でも進捗が残る）
  }

  var doneNow = getDoneTitles_(sh);
  var left = groups.order.filter(function(u){ return !doneNow[CONFIG.TITLE_PREFIX + u]; }).length;
  var doneCount = total - left;

  if (left > 0) {
    if (CONFIG.AUTO_CONTINUE) {
      scheduleContinue_();
      toast_('作成中… ' + doneCount + '/' + total + ' 完了。約1分後に自動で続きを作成します。（残り ' + left + ' 単元）', 10);
    } else {
      toast_(doneCount + '/' + total + ' 完了。残り ' + left + ' 単元。もう一度「全単元を一括作成」を実行すると続きから作成します。', 12);
    }
  } else {
    removeContinueTriggers_();
    toast_('🎉 全 ' + total + ' 単元のフォーム作成が完了しました！', 12);
  }
}

// 自動継続トリガー（時間ベース）を1つだけ張り直す
function scheduleContinue_() {
  removeContinueTriggers_();
  ScriptApp.newTrigger('createAllForms').timeBased().after(60 * 1000).create();
}

function removeContinueTriggers_() {
  ScriptApp.getProjectTriggers().forEach(function(t){
    if (t.getHandlerFunction() === 'createAllForms') ScriptApp.deleteTrigger(t);
  });
}

// 中断した自動継続を止めたいとき用（メニューからも呼べる）
function stopAutoContinue() {
  removeContinueTriggers_();
  toast_('自動作成を停止しました。');
}

function createFormsForChapter() {
  var ui = SpreadsheetApp.getUi();
  var rows = getData_();
  var chapters = uniq_(rows.map(function(r){ return r[COL.chapter]; }));
  var res = ui.prompt('チャプター指定', '作成するチャプター名（部分一致可）を入力してください。\n\n' + chapters.join('\n'), ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() != ui.Button.OK) return;
  var key = res.getResponseText().trim();
  if (!key) return;
  var target = rows.filter(function(r){ return r[COL.chapter].indexOf(key) >= 0; });
  if (!target.length) { ui.alert('該当するチャプターがありません。'); return; }
  var groups = groupByUnit_(target);
  var results = groups.order.map(function(u){
    try { return buildForm_(u, groups.map[u]); }
    catch (e) { return { unit: u, error: String(e) }; }
  });
  writeList_(results);
  toast_(groups.order.length + ' 単元のフォームを作成しました。');
}

function createFormForNamedUnit() {
  var ui = SpreadsheetApp.getUi();
  var rows = getData_();
  var units = uniq_(rows.map(function(r){ return r[COL.unit]; }));
  var res = ui.prompt('単元指定', '作成する単元名（部分一致可）を入力してください。\n\n' + units.join('\n'), ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() != ui.Button.OK) return;
  var key = res.getResponseText().trim();
  if (!key) return;
  var target = rows.filter(function(r){ return r[COL.unit].indexOf(key) >= 0; });
  if (!target.length) { ui.alert('該当する単元がありません。'); return; }
  var result = buildForm_(target[0][COL.unit], target);
  writeList_([result]);
  toast_('フォームを作成しました：' + result.title);
}

function createFormForActiveRow() {
  var rows = getData_();
  var sh = getSheet_();
  var active = SpreadsheetApp.getActiveRange();
  if (!active || active.getSheet().getName() !== sh.getName()) {
    SpreadsheetApp.getUi().alert('問題データのシート上で、対象の単元の行を選んでから実行してください。');
    return;
  }
  var header = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0].map(String);
  var unitCol = header.indexOf(COL.unit) + 1;
  var unitName = sh.getRange(active.getRow(), unitCol).getValue();
  if (!unitName) { SpreadsheetApp.getUi().alert('選択行から単元名を取得できませんでした。'); return; }
  var target = rows.filter(function(r){ return r[COL.unit] === unitName; });
  var result = buildForm_(unitName, target);
  writeList_([result]);
  toast_('フォームを作成しました：' + result.title);
}

// ===== フォーム構築 =================================================
function groupByUnit_(rows) {
  var map = {}, order = [];
  rows.forEach(function(r){
    var u = r[COL.unit];
    if (!map[u]) { map[u] = []; order.push(u); }
    map[u].push(r);
  });
  return { map: map, order: order };
}

function buildForm_(unitName, rows) {
  var chapter = rows[0][COL.chapter] || '';
  var title = CONFIG.TITLE_PREFIX + unitName;
  var form = FormApp.create(title);
  form.setTitle(title);
  form.setDescription((chapter ? chapter + '\n' : '') + unitName + '（全 ' + rows.length + ' 問）');
  form.setIsQuiz(true);
  form.setCollectEmail(CONFIG.COLLECT_EMAIL);
  form.setShuffleQuestions(CONFIG.SHUFFLE);
  form.setProgressBar(true);

  var made = 0;
  rows.forEach(function(row){
    try { addChoice_(form, row); made++; }
    catch (e) { form.addSectionHeaderItem().setTitle('⚠ 問' + row[COL.num] + ' の作成に失敗: ' + e); }
  });

  var folder = getFolder_();
  moveToFolder_(form, folder);

  var nums = rows.map(function(r){ return String(r[COL.num]).trim(); })
                 .filter(function(x){ return x; });
  var numRange = nums.length ? (nums[0] + '〜' + nums[nums.length - 1]) : '';

  return {
    tab: getSheet_().getName(),          // データのタブ名
    numRange: numRange,                  // 対象No.（例: 001〜013）
    unit: unitName, chapter: chapter,
    englishCount: rows.length,           // 英文数
    questionCount: made,                 // 設問数（実際に作成できた数）
    title: title,
    editUrl: form.getEditUrl(), liveUrl: form.getPublishedUrl(),
    folderName: folder.getName(), folderUrl: folder.getUrl()
  };
}

function addChoice_(form, row) {
  var item = form.addMultipleChoiceItem();
  var typeTag = row[COL.type] ? '［' + row[COL.type] + '］' : '';
  item.setTitle('問' + row[COL.num] + '　' + typeTag + '\n' + row[COL.question]);

  var texts = [row[COL.c1], row[COL.c2], row[COL.c3], row[COL.c4], row[COL.c5], row[COL.c6]];
  var correctN = parseInt(String(row[COL.answer]).replace(/[^0-9]/g, ''), 10);
  var choices = [];
  for (var i = 0; i < texts.length; i++) {
    var t = String(texts[i]).trim();
    if (!t) continue;
    choices.push(item.createChoice(t, (i + 1) === correctN));
  }
  if (choices.length < 2) throw new Error('選択肢が2つ未満です');
  item.setChoices(choices);
  item.setPoints(CONFIG.POINTS);

  if (CONFIG.INCLUDE_EXPLANATION) {
    var body = '【正解】' + (row[COL.answerText] || correctN) + '\n' + explanationText_(row);
    var fb = makeFeedback_(body);
    if (fb) { item.setFeedbackForCorrect(fb); item.setFeedbackForIncorrect(fb); }
  }
}

// ===== フィードバック ===============================================
function explanationText_(row) {
  var parts = [];
  if (row[COL.kanseibun]) parts.push('【完成文】' + row[COL.kanseibun]);
  if (row[COL.yaku]) parts.push('【訳】' + row[COL.yaku]);
  if (row[COL.point]) parts.push('【POINT】' + row[COL.point]);
  if (row[COL.kaisetsu]) parts.push('【解説】' + row[COL.kaisetsu]);
  if (row[COL.check]) parts.push('【補足】' + row[COL.check]);
  return parts.join('\n');
}

function makeFeedback_(text) {
  text = String(text || '').trim();
  if (!text) return null;
  if (text.length > 1450) text = text.substring(0, 1430) + '…（続きは解説編を参照）';
  return FormApp.createFeedback().setText(text).build();
}

// ===== 出力・ユーティリティ =========================================
function moveToFolder_(form, folder) {
  var file = DriveApp.getFileById(form.getId());
  folder.addFile(file);
  var root = DriveApp.getRootFolder();
  var parents = file.getParents();
  while (parents.hasNext()) {
    var p = parents.next();
    if (p.getId() === root.getId()) root.removeFile(file);
  }
}

var _folderCache = null;
function getFolder_() {
  if (_folderCache) return _folderCache;
  if (CONFIG.FOLDER_ID) {
    try {
      _folderCache = DriveApp.getFolderById(CONFIG.FOLDER_ID);
      return _folderCache;
    } catch (e) {
      throw new Error('保存先フォルダ（FOLDER_ID）にアクセスできません。IDが正しいか、フォルダの共有権限を確認してください。\n' + e);
    }
  }
  var it = DriveApp.getFoldersByName(CONFIG.FOLDER_NAME);
  _folderCache = it.hasNext() ? it.next() : DriveApp.createFolder(CONFIG.FOLDER_NAME);
  return _folderCache;
}

var LIST_HEADER = ['作成日時', 'タブ', '対象No.', 'タイトル', '英文数', '設問数', '回答用URL', '編集用URL', '保存フォルダ'];
var COL_TITLE = 4;   // タイトル列（1始まり）
var COL_LIVE  = 7;   // 回答用URL列（1始まり）

// 「フォーム一覧」シートを用意し、見出し行を整える
function ensureListSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(CONFIG.LIST_SHEET);
  if (!sh) sh = ss.insertSheet(CONFIG.LIST_SHEET);
  sh.getRange(1, 1, 1, LIST_HEADER.length).setValues([LIST_HEADER]).setFontWeight('bold');
  sh.setFrozenRows(1);
  return sh;
}

// すでに作成済み（＝回答用URLが入っている）フォームのタイトル集合を返す
function getDoneTitles_(sh) {
  var last = sh.getLastRow();
  var done = {};
  if (last < 2) return done;
  var titles = sh.getRange(2, COL_TITLE, last - 1, 1).getValues();
  var urls = sh.getRange(2, COL_LIVE, last - 1, 1).getValues();
  for (var i = 0; i < titles.length; i++) {
    var t = String(titles[i][0]).trim();
    var u = String(urls[i][0]).trim();
    if (t && /^https?:\/\//.test(u)) done[t] = true;  // URL付きの行だけ「完了」扱い（エラー行は再挑戦）
  }
  return done;
}

// 1件を追記
function writeOne_(sh, r) {
  var now = new Date();
  if (r.error) {
    sh.appendRow([now, r.tab || '', r.numRange || '', r.title || (r.unit || ''), '', 'エラー', r.error, '', '']);
    return;
  }
  var folderCell = r.folderUrl
    ? '=HYPERLINK("' + r.folderUrl + '","' + String(r.folderName || 'フォルダ').replace(/"/g, '""') + '")'
    : (r.folderName || '');
  sh.appendRow([now, r.tab, r.numRange, r.title, r.englishCount, r.questionCount, r.liveUrl, r.editUrl, folderCell]);
}

// 単発・チャプター用（少数件をまとめて追記）
function writeList_(results) {
  var sh = ensureListSheet_();
  results.forEach(function(r){ writeOne_(sh, r); });
  sh.autoResizeColumns(1, LIST_HEADER.length);
}

function uniq_(arr) {
  var seen = {}, out = [];
  arr.forEach(function(x){ if (x && !seen[x]) { seen[x] = 1; out.push(x); } });
  return out;
}

function toast_(msg, sec) {
  SpreadsheetApp.getActiveSpreadsheet().toast(msg, '完了', sec || 8);
}
