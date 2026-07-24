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
// titlePrefix の後ろに通し番号(01, 02, …)が付く。
//   例)【入門レベル】英文解釈実践テスト01
// 番号は英文の位置から決まるので、SENTENCES_PER_FORM=1 なら No.と一致(01〜60 / 01〜70)。
var CONFIG = {
  '入門60': {
    folderId: '1-HUnBaaRudxmpuYvGlzxA4wEffiRGIJe',
    titlePrefix: '【入門レベル】英文解釈実践テスト',
  },
  '英文熟考': {
    folderId: '1QfxnyZ82NSpgdWiEygjHpMiKrcnZD7TF',
    titlePrefix: '【基礎レベル】英文解釈実践テスト',
  },
};

// 「送信直後に採点・各問フィードバック表示」のテンプレフォームのID(下の手順で用意)。
// このテンプレを複製して各フォームを作るので、テンプレのテスト設定(成績の発表=送信直後、
// 回答者の設定3つ=オン)がすべてのフォームに引き継がれる。
// 空文字のままだと、設定なしの通常フォームを新規作成する(採点表示は手動設定が必要になる)。
var TEMPLATE_FORM_ID = '1gG2CTC1WFH6P1V9dG-_jOmtDBUPun7uYQS7ixeoCfBk';

var MAX_QUESTIONS = 5; // 1英文あたりの最大設問数(問題01〜問題05)。実際の列数は自動検出する。
// 1つのフォームに入れる英文(行)の数。
//   1  … 1英文ごとに1フォーム(入門60→60フォーム / 英文熟考→70フォーム)
//   10 … 10英文ごとに1フォーム(入門60→6フォーム)
//   0  … そのタブ全体を1つのフォームに
var SENTENCES_PER_FORM = 1;
var LINK_SHEET = 'フォームリンク';
// 1回の実行で使う最大時間(ミリ秒)。GASの6分制限より手前で安全に中断する。
// 中断しても、もう一度同じメニューを実行すれば「続きから」再開できる(作成済みはスキップ)。
var TIME_LIMIT_MS = 5 * 60 * 1000;
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

/** 指定タブからフォームを生成する本体(再開・時間切れ対応) */
function runTab_(tabName, silent) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var conf = CONFIG[tabName];
  if (!conf) throw new Error('CONFIG にタブ「' + tabName + '」の設定がありません。');
  var sheet = ss.getSheetByName(tabName);
  if (!sheet) throw new Error('タブ「' + tabName + '」が見つかりません。');
  var folder = DriveApp.getFolderById(conf.folderId); // フォルダIDが無効ならここでエラー

  var sentences = readSentences_(sheet, tabName);
  if (sentences.length === 0) throw new Error('タブ「' + tabName + '」にデータ行がありません。');

  var linkSheet = getLinkSheet_(ss);
  var done = doneNoSet_(linkSheet, tabName); // すでに作成済みの No. 集合

  var chunkSize = SENTENCES_PER_FORM > 0 ? SENTENCES_PER_FORM : sentences.length;
  var start = new Date().getTime();
  var createdCount = 0, skipped = 0, remaining = 0, stopped = false;

  for (var i = 0; i < sentences.length; i += chunkSize) {
    var chunk = sentences.slice(i, i + chunkSize);
    // このかたまりが全て作成済みならスキップ(再開時の重複防止)
    var allDone = chunk.every(function (s) { return done[s.no]; });
    if (allDone) { skipped += chunk.length; continue; }
    // 時間切れが近ければ中断(次回の実行で続きから)
    if (new Date().getTime() - start > TIME_LIMIT_MS) { remaining += chunk.length; stopped = true; continue; }

    var first = chunk[0].no, last = chunk[chunk.length - 1].no;
    var formIndex = Math.floor(i / chunkSize) + 1;        // 位置から決まる通し番号(再開してもずれない)
    var title = conf.titlePrefix + pad2_(formIndex);      // 例)【入門レベル】英文解釈実践テスト01
    var target = (chunk.length === 1) ? String(first) : (first + '〜' + last);

    var info = buildForm_(title, chunk, folder);
    appendLink_(linkSheet, tabName, target, folder, info); // 1件ごとに追記(途中で止まっても進捗が残る)
    createdCount++;
  }

  var msg = 'タブ「' + tabName + '」: ' + createdCount + ' 件のフォームを作成しました' +
    (skipped ? '(作成済み ' + skipped + ' 英文はスキップ)' : '') + '。\n' +
    'フォルダ「' + folder.getName() + '」に保存し、リンクを「' + LINK_SHEET + '」シートに記録しました。';
  if (stopped) {
    msg += '\n\n⚠ 実行時間の上限が近づいたため ' + remaining + ' 英文を残して中断しました。' +
      'もう一度同じメニューを実行すると、続きから再開します。';
  }
  if (!silent) SpreadsheetApp.getUi().alert(msg);
  return msg;
}

/** 2桁ゼロ埋め(1→"01"、60→"60"、100→"100") */
function pad2_(n) { return (n < 10 ? '0' : '') + n; }

/** シートを 1行=1英文 として読み取る */
function readSentences_(sheet, tabName) {
  var rows = sheet.getDataRange().getValues();
  var header = rows.shift().map(function (h) { return String(h).trim(); });
  var indexed = indexColumns_(header, tabName);
  var col = indexed.col, maxQ = indexed.maxQ;
  var out = [];
  rows.forEach(function (row, ri) {
    var no = String(row[col.no]).trim();
    if (!no) return; // 空行スキップ
    var questions = [];
    for (var qi = 1; qi <= maxQ; qi++) {
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

/** フォームを1つ生成し、指定フォルダに保存する */
function buildForm_(title, sentences, folder) {
  var form;
  if (TEMPLATE_FORM_ID) {
    // テンプレを複製 → テスト設定(送信直後採点・各問フィードバック表示)を引き継ぐ
    var copy = DriveApp.getFileById(TEMPLATE_FORM_ID).makeCopy(title, folder);
    form = FormApp.openById(copy.getId());
    // テンプレに入っている見本の質問をすべて削除
    var items = form.getItems();
    for (var k = items.length - 1; k >= 0; k--) form.deleteItem(items[k]);
    form.setTitle(title);
    // ※ 複製版では setIsQuiz を呼ばない(テストの表示設定がリセットされるのを防ぐため)
  } else {
    // テンプレ未設定: 通常のテストフォームを新規作成(採点の表示は各フォームで手動設定が必要)
    form = FormApp.create(title);
    form.setIsQuiz(true);
  }
  form.setDescription(FORM_DESCRIPTION);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  sentences.forEach(function (s, si) {
    if (si > 0) form.addPageBreakItem().setTitle('No.' + s.no);
    // 英文のみ表示(訳は答えのヒントになるためフォームには出さない)
    form.addSectionHeaderItem()
      .setTitle('【No.' + s.no + '】 ' + s.en);
    s.questions.forEach(function (q) {
      var item = form.addMultipleChoiceItem();
      item.setTitle(q.title).setRequired(true).setPoints(1);
      item.setChoices(['A', 'B', 'C', 'D'].map(function (L) {
        return item.createChoice(L + '. ' + q.choices[L], L === q.answer);
      }));
      // 正解時: 解説のみ / 不正解時: 「正解: X」+解説(Google側の「正解を表示」設定に関わらず答えが届く)
      var exp = q.explanation || '';
      var correctText = exp || '正解です。';
      var incorrectText = '正解: ' + q.answer + (exp ? '\n\n' + exp : '');
      item.setFeedbackForCorrect(FormApp.createFeedback().setText(correctText).build());
      item.setFeedbackForIncorrect(FormApp.createFeedback().setText(incorrectText).build());
    });
  });

  // 新規作成した場合のみ指定フォルダへ移動(複製版は既にフォルダ内にある)
  if (!TEMPLATE_FORM_ID) {
    var file = DriveApp.getFileById(form.getId());
    try {
      file.moveTo(folder);
    } catch (e) {
      folder.addFile(file);
      DriveApp.getRootFolder().removeFile(file);
    }
  }

  return {
    title: title,
    editUrl: form.getEditUrl(),
    liveUrl: form.getPublishedUrl(),
    numSentences: sentences.length,
    numQuestions: sentences.reduce(function (n, s) { return n + s.questions.length; }, 0),
  };
}

/** 「フォームリンク」シートを取得(なければ作成しヘッダーを付ける) */
function getLinkSheet_(ss) {
  var out = ss.getSheetByName(LINK_SHEET);
  if (!out) out = ss.insertSheet(LINK_SHEET);
  if (out.getLastRow() === 0) {
    out.appendRow(['作成日時', 'タブ', '対象No.', 'タイトル', '英文数', '設問数', '回答用URL', '編集用URL', '保存フォルダ']);
    out.getRange(1, 1, 1, 9).setFontWeight('bold');
  }
  return out;
}

/** 既に作成済みの No. の集合を作る(再開時の重複防止)。"5" や "1〜10" を展開して取り込む */
function doneNoSet_(linkSheet, tabName) {
  var done = {};
  if (linkSheet.getLastRow() < 2) return done;
  var values = linkSheet.getRange(2, 2, linkSheet.getLastRow() - 1, 2).getValues(); // B列(タブ),C列(対象No.)
  values.forEach(function (r) {
    if (String(r[0]).trim() !== tabName) return;
    var t = String(r[1]).trim();
    if (t.indexOf('〜') >= 0) {
      var parts = t.split('〜');
      var a = parseInt(parts[0], 10), b = parseInt(parts[1], 10);
      if (!isNaN(a) && !isNaN(b)) { for (var k = a; k <= b; k++) done[String(k)] = true; }
    } else if (t) {
      done[t] = true;
    }
  });
  return done;
}

/** 生成した1フォームの情報を追記する */
function appendLink_(linkSheet, tabName, target, folder, f) {
  linkSheet.appendRow([new Date(), tabName, target, f.title, f.numSentences, f.numQuestions,
    f.liveUrl, f.editUrl, folder.getUrl()]);
}

/**
 * ヘッダー行の列名から列番号を引く(CSVのヘッダーと同一)。
 * 設問ブロック(問題01〜)は実際に存在する分だけ読み取る。
 * 返り値: { col: 列マップ, maxQ: 検出した最大設問番号 }
 */
function indexColumns_(header, tabName) {
  var col = {};
  ['no', 'en', 'ja'].forEach(function (key, k) {
    var name = ['問題No', '問題', '訳'][k];
    var idx = header.indexOf(name);
    if (idx === -1) throw new Error('タブ「' + tabName + '」のヘッダー行に列「' + name + '」がありません。');
    col[key] = idx;
  });

  var maxQ = 0;
  for (var i = 1; i <= MAX_QUESTIONS; i++) {
    var stemName = '問題0' + i;
    if (header.indexOf(stemName) === -1) break; // 設問文の列が無ければ、それ以降の設問は無いとみなす
    var block = {
      ['q' + i]: '問題0' + i,
      ['ch' + i + 'A']: '問題0' + i + '選択肢A',
      ['ch' + i + 'B']: '問題0' + i + '選択肢B',
      ['ch' + i + 'C']: '問題0' + i + '選択肢C',
      ['ch' + i + 'D']: '問題0' + i + '選択肢D',
      ['a' + i]: '問題0' + i + 'の答え',
      ['e' + i]: '問題0' + i + 'の解説',
    };
    Object.keys(block).forEach(function (key) {
      var idx = header.indexOf(block[key]);
      if (idx === -1) {
        throw new Error('タブ「' + tabName + '」に列「' + block[key] + '」がありません(問題0' + i + 'の列が不完全です)。');
      }
      col[key] = idx;
    });
    maxQ = i;
  }
  if (maxQ === 0) throw new Error('タブ「' + tabName + '」に設問の列(問題01…)が見つかりません。');
  return { col: col, maxQ: maxQ };
}
