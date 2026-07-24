/**
 * 英文解釈 確認テスト — Googleフォーム一括生成スクリプト(複数タブ / Drive フォルダ対応)
 *
 * このスプレッドシートの各タブ(入門60 / 英文熟考)から、
 * クイズ形式(自動採点・解説フィードバック付き)のGoogleフォームを生成し、
 * 指定した Drive フォルダに保存し、生成したフォームのURLを
 * 「フォームリンク」シートに書き戻します。
 *
 * 【使い方】
 * 1. 拡張機能 > Apps Script を開き、このコードを貼り付けて保存。
 * 2. スプレッドシートを再読み込みすると、上部メニューに「フォーム作成」が出る。
 * 3. 「フォーム作成 > 入門60 を作成」または「英文熟考 を作成」を実行。
 *    (初回のみ権限承認のダイアログが出るので許可する)
 * 4. 完了ダイアログのあと、「フォームリンク」シートにURLが追記される。
 *
 * ※ 実行するたびに新しいフォームが作られます(既存フォームは上書きしません)。
 */

// ===== 設定 =====================================================
// タブ名 → { フォルダID, フォームのタイトル }
var CONFIG = {
  '入門60': {
    folderId: '1-HUnBaaRudxmpuYvGlzxA4wEffiRGIJe',
    formTitle: '【夏期特訓】英文解釈 確認テスト 入門60',
  },
  '英文熟考': {
    folderId: '1QfxnyZ82NSpgdWiEygjHpMiKrcnZD7TF',
    formTitle: '【夏期特訓】英文解釈 確認テスト 英文熟考70',
  },
};

var MAX_QUESTIONS = 6;
// 1つのフォームに入れる英文(行)の数。0 なら「そのタブ全体を1つのフォーム」にする。
// 例: 10 にすると 10 英文ごとにフォームを分割する(入門60 なら 6 フォーム)。
var SENTENCES_PER_FORM = 10;
var LINK_SHEET = 'フォームリンク';
var FORM_DESCRIPTION =
  'それぞれの英文について、本当に理解できているかを確認するテストです。' +
  '訳の暗記ではなく、英文そのものを読んで答えてください。';
// ================================================================

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('フォーム作成')
    .addItem('入門60 を作成', 'createFor_Nyumon60')
    .addItem('英文熟考 を作成', 'createFor_Jukko')
    .addSeparator()
    .addItem('両方まとめて作成', 'createAll')
    .addToUi();
}

function createFor_Nyumon60() { runTab_('入門60'); }
function createFor_Jukko() { runTab_('英文熟考'); }
function createAll() {
  var msgs = [];
  Object.keys(CONFIG).forEach(function (tab) { msgs.push(runTab_(tab, true)); });
  SpreadsheetApp.getUi().alert(msgs.join('\n\n'));
}

/** 指定タブからフォームを生成する本体 */
function runTab_(tabName, silent) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var conf = CONFIG[tabName];
  if (!conf) throw new Error('CONFIG にタブ「' + tabName + '」の設定がありません。');
  var sheet = ss.getSheetByName(tabName);
  if (!sheet) throw new Error('タブ「' + tabName + '」が見つかりません。');
  var folder = DriveApp.getFolderById(conf.folderId); // フォルダIDが無効ならここでエラー

  var sentences = readSentences_(sheet, tabName);
  if (sentences.length === 0) throw new Error('タブ「' + tabName + '」にデータ行がありません。');

  var chunkSize = SENTENCES_PER_FORM > 0 ? SENTENCES_PER_FORM : sentences.length;
  var created = [];
  for (var i = 0; i < sentences.length; i += chunkSize) {
    var chunk = sentences.slice(i, i + chunkSize);
    var suffix = (chunkSize < sentences.length)
      ? '(No.' + chunk[0].no + '〜' + chunk[chunk.length - 1].no + ')' : '';
    var info = buildForm_(conf.formTitle + suffix, chunk, folder);
    created.push(info);
  }

  writeLinks_(ss, tabName, folder, created);
  var msg = 'タブ「' + tabName + '」から ' + created.length + ' 件のフォームを作成し、' +
    'フォルダ「' + folder.getName() + '」に保存しました。\nリンクは「' + LINK_SHEET + '」シートに書き込みました。';
  if (!silent) SpreadsheetApp.getUi().alert(msg);
  return msg;
}

/** シートを 1行=1英文 として読み取る */
function readSentences_(sheet, tabName) {
  var rows = sheet.getDataRange().getValues();
  var header = rows.shift().map(function (h) { return String(h).trim(); });
  var col = indexColumns_(header, tabName);
  var out = [];
  rows.forEach(function (row, ri) {
    var no = String(row[col.no]).trim();
    if (!no) return; // 空行スキップ
    var questions = [];
    for (var qi = 1; qi <= MAX_QUESTIONS; qi++) {
      var stem = String(row[col['q' + qi]] || '').trim();
      if (!stem) continue; // 設問文が空 = その番号の設問なし
      questions.push(buildQuestion_(row, col, stem, no, qi, ri + 2));
    }
    if (questions.length === 0) {
      throw new Error('タブ「' + tabName + '」の行 ' + (ri + 2) + '(No.' + no + ')に設問がありません。');
    }
    out.push({ no: no, en: String(row[col.en]), ja: String(row[col.ja]), questions: questions });
  });
  return out;
}

/** 分割された各列から 1問を組み立てる */
function buildQuestion_(row, col, stem, no, qi, rowNum) {
  var choices = {};
  var missing = [];
  ['A', 'B', 'C', 'D'].forEach(function (L) {
    var v = String(row[col['ch' + qi + L]] || '').trim();
    if (!v) missing.push(L);
    choices[L] = v;
  });
  if (missing.length) {
    throw new Error('行 ' + rowNum + ' 問題0' + qi + ': 選択肢 ' + missing.join(',') +
      ' の列が空です(列「問題0' + qi + '選択肢' + missing.join('」「問題0' + qi + '選択肢') + '」を確認)。');
  }
  var answer = String(row[col['a' + qi]] || '').trim().charAt(0).toUpperCase();
  if (['A', 'B', 'C', 'D'].indexOf(answer) === -1) {
    throw new Error('行 ' + rowNum + ' 問題0' + qi + 'の答えが A〜D ではありません: "' + row[col['a' + qi]] + '"');
  }
  return {
    title: '【No.' + no + '-問' + qi + '】 ' + stem,
    choices: choices,
    answer: answer,
    explanation: String(row[col['e' + qi]] || '').trim(),
  };
}

/** フォームを1つ生成し、指定フォルダに移動する */
function buildForm_(title, sentences, folder) {
  var form = FormApp.create(title);
  form.setDescription(FORM_DESCRIPTION);
  form.setIsQuiz(true);
  form.setProgressBar(true);
  form.setCollectEmail(false); // 運用に合わせて変更可
  form.setShuffleQuestions(false);

  sentences.forEach(function (s, si) {
    if (si > 0) form.addPageBreakItem().setTitle('No.' + s.no);
    form.addSectionHeaderItem()
      .setTitle('【No.' + s.no + '】 ' + s.en)
      .setHelpText('訳:' + s.ja);
    s.questions.forEach(function (q) {
      var item = form.addMultipleChoiceItem();
      item.setTitle(q.title).setRequired(true).setPoints(1);
      item.setChoices(['A', 'B', 'C', 'D'].map(function (L) {
        return item.createChoice(L + '. ' + q.choices[L], L === q.answer);
      }));
      if (q.explanation) {
        var fb = FormApp.createFeedback().setText(q.explanation).build();
        item.setFeedbackForCorrect(fb);
        item.setFeedbackForIncorrect(fb);
      }
    });
  });

  // 生成したフォーム(Driveファイル)を指定フォルダへ移動
  var file = DriveApp.getFileById(form.getId());
  try {
    file.moveTo(folder);
  } catch (e) {
    // 古い環境向けフォールバック
    folder.addFile(file);
    DriveApp.getRootFolder().removeFile(file);
  }

  return {
    title: title,
    editUrl: form.getEditUrl(),
    liveUrl: form.getPublishedUrl(),
    numSentences: sentences.length,
    numQuestions: sentences.reduce(function (n, s) { return n + s.questions.length; }, 0),
  };
}

/** 生成結果を「フォームリンク」シートに追記する */
function writeLinks_(ss, tabName, folder, created) {
  var out = ss.getSheetByName(LINK_SHEET);
  if (!out) out = ss.insertSheet(LINK_SHEET);
  if (out.getLastRow() === 0) {
    out.appendRow(['作成日時', 'タブ', 'タイトル', '英文数', '設問数', '回答用URL', '編集用URL', '保存フォルダ']);
    out.getRange(1, 1, 1, 8).setFontWeight('bold');
  }
  var now = new Date();
  created.forEach(function (f) {
    out.appendRow([now, tabName, f.title, f.numSentences, f.numQuestions, f.liveUrl, f.editUrl, folder.getUrl()]);
  });
}

/** ヘッダー行の列名から列番号を引く(CSVのヘッダーと同一) */
function indexColumns_(header, tabName) {
  var map = { no: '問題No', en: '問題', ja: '訳' };
  for (var i = 1; i <= MAX_QUESTIONS; i++) {
    map['q' + i] = '問題0' + i;
    map['ch' + i + 'A'] = '問題0' + i + '選択肢A';
    map['ch' + i + 'B'] = '問題0' + i + '選択肢B';
    map['ch' + i + 'C'] = '問題0' + i + '選択肢C';
    map['ch' + i + 'D'] = '問題0' + i + '選択肢D';
    map['a' + i] = '問題0' + i + 'の答え';
    map['e' + i] = '問題0' + i + 'の解説';
  }
  var col = {};
  Object.keys(map).forEach(function (key) {
    var idx = header.indexOf(map[key]);
    if (idx === -1) {
      throw new Error('タブ「' + tabName + '」のヘッダー行に列「' + map[key] + '」がありません。');
    }
    col[key] = idx;
  });
  return col;
}
