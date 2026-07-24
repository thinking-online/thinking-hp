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
  FOLDER_NAME: '英文法ポラリス1_単元フォーム',   // 作成先の Drive フォルダ名
  LIST_SHEET: 'フォーム一覧',                   // 作成フォームのURL出力先シート
  POINTS: 1,                                   // 1問あたりの配点
  INCLUDE_EXPLANATION: true,                   // フィードバックに解説を載せる
  SHUFFLE: false,                              // 問題の順番をシャッフル
  COLLECT_EMAIL: false,                        // 回答者メールの収集
  TITLE_PREFIX: '英文法ポラリス1｜'             // フォームのタイトル接頭辞
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
    .addItem('全単元を一括作成（30単元）', 'createAllForms')
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
function createAllForms() {
  var groups = groupByUnit_(getData_());
  var results = groups.order.map(function(u){
    try { return buildForm_(u, groups.map[u]); }
    catch (e) { return { unit: u, error: String(e) }; }
  });
  writeList_(results);
  toast_(groups.order.length + ' 単元のフォームを作成しました。「' + CONFIG.LIST_SHEET + '」シートにURLを出力しました。');
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
  form.setDescription((chapter ? chapter + '\n' : '') + unitName + '（全 ' + rows.length + ' 問）\n英文法ポラリス1 完成問題集より');
  form.setIsQuiz(true);
  form.setCollectEmail(CONFIG.COLLECT_EMAIL);
  form.setShuffleQuestions(CONFIG.SHUFFLE);
  form.setProgressBar(true);

  rows.forEach(function(row){
    try { addChoice_(form, row); }
    catch (e) { form.addSectionHeaderItem().setTitle('⚠ 問' + row[COL.num] + ' の作成に失敗: ' + e); }
  });

  moveToFolder_(form);
  return {
    unit: unitName, chapter: chapter, count: rows.length, title: title,
    editUrl: form.getEditUrl(), liveUrl: form.getPublishedUrl()
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
function moveToFolder_(form) {
  var file = DriveApp.getFileById(form.getId());
  var folder = getFolder_();
  folder.addFile(file);
  var root = DriveApp.getRootFolder();
  var parents = file.getParents();
  while (parents.hasNext()) {
    var p = parents.next();
    if (p.getId() === root.getId()) root.removeFile(file);
  }
}

function getFolder_() {
  var it = DriveApp.getFoldersByName(CONFIG.FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(CONFIG.FOLDER_NAME);
}

function writeList_(results) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(CONFIG.LIST_SHEET);
  if (!sh) {
    sh = ss.insertSheet(CONFIG.LIST_SHEET);
    sh.appendRow(['作成日時', 'チャプター', '単元', '問題数', 'タイトル', '回答用URL', '編集用URL']);
    sh.getRange(1, 1, 1, 7).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  var now = new Date();
  results.forEach(function(r){
    if (r.error) sh.appendRow([now, r.unit || '', r.unit || '', '', 'エラー', r.error, '']);
    else sh.appendRow([now, r.chapter, r.unit, r.count, r.title, r.liveUrl, r.editUrl]);
  });
  sh.autoResizeColumns(1, 5);
}

function uniq_(arr) {
  var seen = {}, out = [];
  arr.forEach(function(x){ if (x && !seen[x]) { seen[x] = 1; out.push(x); } });
  return out;
}

function toast_(msg) {
  SpreadsheetApp.getActiveSpreadsheet().toast(msg, '完了', 8);
}
