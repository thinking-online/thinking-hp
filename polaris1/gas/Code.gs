/**
 * 英文法ポラリス1 完成問題集 ｜ 単元別フォーム自動生成ツール（GAS）
 * ------------------------------------------------------------------
 * マスターCSVを取り込んだスプレッドシートに紐づけて使います。
 * 単元（ユニット）ごとに Google フォーム（自動採点クイズ）を作成します。
 *
 * 【使い方】
 *   1. マスターCSV（英文法ポラリス1_問題集マスター.csv）を Google スプレッドシートに
 *      インポートする（1行目が見出し行）。
 *   2. 拡張機能 → Apps Script を開き、このコードを貼り付けて保存。
 *   3. スプレッドシートを再読み込みすると、メニュー「📝 フォーム作成」が出ます。
 *   4. メニューから作成したい範囲を選ぶ（初回は権限の承認が必要）。
 *
 * 出題形式ごとの扱い：
 *   ・空所補充 / 誤文訂正 … 選択式で「自動採点」（正解＋解説フィードバック付き）
 *   ・整序 / 記述        … 記述式。解答と解説を送信後フィードバックで表示
 *                           （記述式はGASの制約で自動採点は付けられません）
 */

// ===== 設定 =========================================================
var CONFIG = {
  SHEET_NAME: '',          // 問題データのシート名。空なら先頭（または「問題」）シートを自動判定
  FOLDER_NAME: '英文法ポラリス1_単元フォーム',  // 作成先の Drive フォルダ名
  LIST_SHEET: 'フォーム一覧',  // 作成したフォームのURLを書き出すシート名
  POINTS: 1,               // 1問あたりの配点
  INCLUDE_EXPLANATION: true, // フィードバックに解説を載せる
  TEXT_AUTOGRADE: true,    // 整序・記述も自動採点する（Forms API 高度なサービスが必要）
  SHUFFLE: false,          // 問題の順番をシャッフルする
  COLLECT_EMAIL: false,    // 回答者のメール収集
  TITLE_PREFIX: '英文法ポラリス1｜'  // フォームのタイトル接頭辞
};

var COL = {
  num: '番号', chapter: 'チャプター', unit: 'ユニット', type: '形式',
  question: '問題文',
  c1: '選択肢1', c2: '選択肢2', c3: '選択肢3', c4: '選択肢4', c5: '選択肢5', c6: '選択肢6',
  answer: '正解', answerText: '正解の内容',
  kanseibun: '完成文', yaku: '訳', point: 'POINT',
  kaisetsu: '解説', check: '誤答チェック・補足', biko: '備考'
};

var CIRCLED = ['①','②','③','④','⑤','⑥','⑦','⑧','⑨'];

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
    .create();
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
  // 必須列チェック
  [COL.num, COL.unit, COL.type, COL.question].forEach(function(need){
    if (!(need in idx)) throw new Error('必要な列「' + need + '」が見つかりません。見出し行を確認してください。');
  });
  var rows = [];
  for (var r = 1; r < values.length; r++) {
    var raw = values[r];
    if (!String(raw[idx[COL.num]]).trim()) continue;
    var obj = {};
    header.forEach(function(h){ obj[h] = (idx[h] != null) ? String(raw[idx[h]]) : ''; });
    rows.push(obj);
  }
  return rows;
}

function previewData() {
  var rows = getData_();
  var units = {};
  rows.forEach(function(r){ units[r[COL.unit]] = (units[r[COL.unit]] || 0) + 1; });
  var lines = Object.keys(units).map(function(u){ return '・' + u + '（' + units[u] + '問）'; });
  SpreadsheetApp.getUi().alert(
    '読み込み結果',
    '合計 ' + rows.length + ' 問 ／ ' + Object.keys(units).length + ' 単元\n\n' + lines.join('\n'),
    SpreadsheetApp.getUi().ButtonSet.OK
  );
}

// ===== 各エントリーポイント =========================================
function createAllForms() {
  var rows = getData_();
  var order = [];
  var groups = {};
  rows.forEach(function(r){
    var u = r[COL.unit];
    if (!groups[u]) { groups[u] = []; order.push(u); }
    groups[u].push(r);
  });
  var results = [];
  order.forEach(function(u){
    try {
      results.push(buildForm_(u, groups[u]));
    } catch (e) {
      results.push({ unit: u, error: String(e) });
    }
  });
  writeList_(results);
  toast_(order.length + ' 単元のフォームを作成しました。「' + CONFIG.LIST_SHEET + '」シートにURLを出力しました。');
}

function createFormsForChapter() {
  var ui = SpreadsheetApp.getUi();
  var rows = getData_();
  var chapters = uniq_(rows.map(function(r){ return r[COL.chapter]; }));
  var res = ui.prompt('チャプター指定',
    '作成するチャプター名（部分一致可）を入力してください。\n\n' + chapters.join('\n'),
    ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() != ui.Button.OK) return;
  var key = res.getResponseText().trim();
  if (!key) return;
  var target = rows.filter(function(r){ return r[COL.chapter].indexOf(key) >= 0; });
  if (!target.length) { ui.alert('該当するチャプターがありません。'); return; }
  var order = [], groups = {};
  target.forEach(function(r){
    var u = r[COL.unit];
    if (!groups[u]) { groups[u] = []; order.push(u); }
    groups[u].push(r);
  });
  var results = order.map(function(u){
    try { return buildForm_(u, groups[u]); }
    catch (e) { return { unit: u, error: String(e) }; }
  });
  writeList_(results);
  toast_(order.length + ' 単元のフォームを作成しました。');
}

function createFormForNamedUnit() {
  var ui = SpreadsheetApp.getUi();
  var rows = getData_();
  var units = uniq_(rows.map(function(r){ return r[COL.unit]; }));
  var res = ui.prompt('単元指定',
    '作成する単元名（部分一致可）を入力してください。\n\n' + units.join('\n'),
    ui.ButtonSet.OK_CANCEL);
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
function buildForm_(unitName, rows) {
  var chapter = rows[0][COL.chapter] || '';
  var title = CONFIG.TITLE_PREFIX + unitName;
  var form = FormApp.create(title);
  form.setTitle(title);
  form.setDescription(
    (chapter ? chapter + '\n' : '') +
    unitName + '（全 ' + rows.length + ' 問）\n' +
    '英文法ポラリス1 完成問題集より'
  );
  form.setIsQuiz(true);
  form.setCollectEmail(CONFIG.COLLECT_EMAIL);
  form.setShuffleQuestions(CONFIG.SHUFFLE);
  form.setProgressBar(true);

  var gradeQueue = []; // 整序・記述の後処理用（自動採点）
  rows.forEach(function(row){
    try { addItem_(form, row, gradeQueue); }
    catch (e) { form.addSectionHeaderItem().setTitle('⚠ 問' + row[COL.num] + ' の作成に失敗: ' + e); }
  });

  // 記述系の採点を適用（Forms API があれば自動採点、無ければ解説フィードバックのみ）
  applyTextGrading_(form.getId(), gradeQueue);

  moveToFolder_(form);
  return {
    unit: unitName, chapter: chapter, count: rows.length, title: title,
    editUrl: form.getEditUrl(), liveUrl: form.getPublishedUrl()
  };
}

function addItem_(form, row, gradeQueue) {
  var type = row[COL.type];
  if (type === '空所補充') {
    addChoice_(form, row);
  } else if (type === '誤文訂正') {
    addErrorId_(form, row);
  } else {
    addText_(form, row, gradeQueue); // 整序・記述・その他
  }
}

function addChoice_(form, row) {
  var item = form.addMultipleChoiceItem();
  item.setTitle('問' + row[COL.num] + '　' + row[COL.question]);
  var texts = [row[COL.c1], row[COL.c2], row[COL.c3], row[COL.c4], row[COL.c5], row[COL.c6]];
  var correctN = parseInt(String(row[COL.answer]).replace(/[^0-9]/g, ''), 10);
  var choices = [];
  for (var i = 0; i < texts.length; i++) {
    var t = String(texts[i]).trim();
    if (!t) continue;
    choices.push(item.createChoice(t, (i + 1) === correctN));
  }
  item.setChoices(choices);
  item.setPoints(CONFIG.POINTS);
  applyFeedback_(item, row);
}

function addErrorId_(form, row) {
  var item = form.addMultipleChoiceItem();
  item.setTitle('問' + row[COL.num] + '（誤り探し）　下線部で誤っている箇所を選んでください。\n' + row[COL.question]);
  var segs = parseErrorSegments_(row[COL.question]);
  var correctMarker = String(row[COL.answer]).trim().charAt(0); // ①など
  var choices = [];
  if (segs.length >= 2) {
    segs.forEach(function(s){
      choices.push(item.createChoice(s.marker + ' ' + s.text, s.marker === correctMarker));
    });
  } else {
    // フォールバック：丸数字だけの選択肢
    CIRCLED.slice(0, 4).forEach(function(m){
      choices.push(item.createChoice(m, m === correctMarker));
    });
  }
  item.setChoices(choices);
  item.setPoints(CONFIG.POINTS);
  applyFeedback_(item, row);
}

function addText_(form, row, gradeQueue) {
  var isReorder = (row[COL.type] === '整序');
  var base = String(row[COL.answer]).trim();     // 整序=数字列, 記述=解答語
  var answers = buildAnswerVariants_(row[COL.type], base);
  var hint = isReorder
    ? ((/[ 　]/.test(base))
        ? '（〔　〕内を並べ替え、選んだ順に番号を入力。空所が2つある場合は間を半角スペースで区切る）'
        : '（〔　〕内を並べ替え、選んだ順に番号を続けて入力。例: 3241）')
    : '（英語で記入。スペル・大文字小文字はできるだけ正確に）';

  var item = form.addTextItem();
  item.setTitle('問' + row[COL.num] + '　' + row[COL.question] + '\n' + hint);

  var ans = row[COL.answerText] || base;         // フィードバックには完成文/解答を表示
  var fbText = '【正解】' + ans + (CONFIG.INCLUDE_EXPLANATION ? '\n' + explanationText_(row) : '');
  fbText = trimFeedback_(fbText);

  // 自動採点は Forms API で後付け。API が無ければ後処理で points＋一般フィードバックを設定
  gradeQueue.push({
    num: row[COL.num], item: item, answers: answers, feedbackText: fbText, points: CONFIG.POINTS
  });
}

/** 記述系の正解キーを適用。Forms API（高度なサービス）があれば自動採点、無ければフィードバックのみ。 */
function applyTextGrading_(formId, queue) {
  if (!queue || !queue.length) return;

  var useApi = false;
  if (CONFIG.TEXT_AUTOGRADE) {
    try { useApi = (typeof Forms !== 'undefined' && Forms.Forms && typeof Forms.Forms.get === 'function'); }
    catch (e) { useApi = false; }
  }

  if (!useApi) {
    // フォールバック：自動採点なし。配点＋解答/解説フィードバックだけ付ける
    queue.forEach(function(e){
      try {
        e.item.setPoints(e.points);
        var fb = makeFeedback_(e.feedbackText);
        if (fb) e.item.setGeneralFeedback(fb);
      } catch (err) {}
    });
    return;
  }

  // Forms API で正解キー（correctAnswers）＋配点＋一般フィードバックをまとめて設定
  var form = Forms.Forms.get(formId);
  var items = form.items || [];
  var byNum = {};
  for (var i = 0; i < items.length; i++) {
    var it = items[i];
    var m = String(it.title || '').match(/問\s*(\d{3})/);
    if (m && it.questionItem && it.questionItem.question) {
      byNum[m[1]] = { index: i, itemId: it.itemId, questionId: it.questionItem.question.questionId };
    }
  }

  var requests = [];
  queue.forEach(function(e){
    var info = byNum[e.num];
    if (!info) return;
    var grading = {
      pointValue: e.points,
      correctAnswers: { answers: e.answers.map(function(v){ return { value: v }; }) }
    };
    if (e.feedbackText) grading.generalFeedback = { text: e.feedbackText };
    requests.push({
      updateItem: {
        item: {
          itemId: info.itemId,
          questionItem: { question: { questionId: info.questionId, grading: grading } }
        },
        location: { index: info.index },
        updateMask: 'questionItem.question.grading'
      }
    });
  });
  if (requests.length) Forms.Forms.batchUpdate({ requests: requests }, formId);
}

/** 正解の表記ゆれを吸収して受理する解答リストを作る（完全一致・複数許容） */
function buildAnswerVariants_(type, base) {
  base = String(base).trim();
  var set = [];
  function add(v){ v = String(v).trim(); if (v && set.indexOf(v) < 0) set.push(v); }
  if (type === '整序') {
    add(base);
    if (/[ 　]/.test(base)) {
      add(base.replace(/[　]/g, ' ').replace(/\s+/g, ' ')); // 全角→半角・連続空白を1つに
      add(base.replace(/[\s　]+/g, ''));                    // 空白なしでもOK
    }
  } else {
    add(base);
    add(base.toLowerCase());
    add(base.charAt(0).toUpperCase() + base.slice(1).toLowerCase());
  }
  return set.length ? set : [base];
}

// ===== フィードバック ===============================================
function applyFeedback_(item, row) {
  if (!CONFIG.INCLUDE_EXPLANATION) return;
  var ans = row[COL.answerText] || row[COL.answer];
  var body = '【正解】' + ans + '\n' + explanationText_(row);
  var fb = makeFeedback_(body);
  if (fb) {
    item.setFeedbackForCorrect(fb);
    item.setFeedbackForIncorrect(fb);
  }
}

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
  text = trimFeedback_(text);
  if (!text) return null;
  return FormApp.createFeedback().setText(text).build();
}

function trimFeedback_(text) {
  text = String(text || '').trim();
  if (text.length > 1450) text = text.substring(0, 1430) + '…（続きは解説編を参照）';
  return text;
}

// ===== 誤文訂正：下線セグメント解析 =================================
function parseErrorSegments_(qtext) {
  var s = String(qtext);
  var found = [];
  for (var i = 0; i < s.length; i++) {
    var ci = CIRCLED.indexOf(s.charAt(i));
    if (ci >= 0) found.push({ marker: s.charAt(i), pos: i });
  }
  var segs = [];
  for (var k = 0; k < found.length; k++) {
    var start = found[k].pos + 1;
    var end = (k + 1 < found.length) ? found[k + 1].pos : s.length;
    var text = s.substring(start, end).trim().replace(/[。.\s]+$/, '');
    if (text.length > 60) text = text.substring(0, 58) + '…';
    segs.push({ marker: found[k].marker, text: text });
  }
  return segs;
}

// ===== 出力・ユーティリティ =========================================
function moveToFolder_(form) {
  var file = DriveApp.getFileById(form.getId());
  var folder = getFolder_();
  folder.addFile(file);
  var root = DriveApp.getRootFolder();
  // ルート直下からは外す（重複配置を避ける）
  var parents = file.getParents();
  while (parents.hasNext()) {
    var p = parents.next();
    if (p.getId() === root.getId()) root.removeFile(file);
  }
}

function getFolder_() {
  var it = DriveApp.getFoldersByName(CONFIG.FOLDER_NAME);
  if (it.hasNext()) return it.next();
  return DriveApp.createFolder(CONFIG.FOLDER_NAME);
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
    if (r.error) {
      sh.appendRow([now, r.unit || '', r.unit || '', '', 'エラー', r.error, '']);
    } else {
      sh.appendRow([now, r.chapter, r.unit, r.count, r.title, r.liveUrl, r.editUrl]);
    }
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
