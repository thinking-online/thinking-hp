/**
 * 英文解釈 確認テスト — Googleフォーム一括生成スクリプト
 *
 * 使い方:
 * 1. questions シート(spreadsheet-format.md の列構成)を用意する。
 * 2. スプレッドシートの「拡張機能 > Apps Script」にこのファイルを貼り付ける。
 * 3. createFormsFromSheet() を実行(初回は権限承認が必要)。
 * 4. forms シートに生成されたフォームのURL(編集用・回答用)が書き込まれる。
 *
 * 仕様:
 * - クイズモードで作成(自動採点)。
 * - sentence_id ごとにセクション(英文+配布訳の表示)を作り、その設問を続ける。
 * - 各設問は4択・必須。正解と配点を設定し、解説(explanation)を
 *   正解時/不正解時のフィードバックとして紐づける。
 * - QUESTIONS_PER_FORM 件の英文ごとにフォームを分割(既定10文=1フォーム)。
 */

const SHEET_NAME = 'questions';
const OUTPUT_SHEET_NAME = 'forms';
const QUESTIONS_PER_FORM = 10; // 1フォームに入れる英文(sentence_id)の数
const FORM_TITLE_PREFIX = '英文解釈 確認テスト';
const FORM_DESCRIPTION =
  'それぞれの英文について、本当の意味で理解できているかを確認するテストです。' +
  '訳の暗記ではなく、英文そのものを読んで答えてください。';

function createFormsFromSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) throw new Error('シート "' + SHEET_NAME + '" が見つかりません。');

  const rows = sheet.getDataRange().getValues();
  const header = rows.shift();
  const col = indexColumns_(header);

  // sentence_id ごとにグループ化(シートの行順を維持)
  const groups = [];
  const groupIndex = {};
  rows.forEach(function (row) {
    const sid = String(row[col.sentence_id]).trim();
    if (!sid) return; // 空行スキップ
    if (!(sid in groupIndex)) {
      groupIndex[sid] = groups.length;
      groups.push({
        sentenceId: sid,
        sentenceEn: String(row[col.sentence_en]),
        sentenceJa: String(row[col.sentence_ja]),
        questions: [],
      });
    }
    groups[groupIndex[sid]].questions.push(row);
  });
  if (groups.length === 0) throw new Error('questions シートにデータ行がありません。');

  // QUESTIONS_PER_FORM 文ごとにフォームを分割して生成
  const created = [];
  for (let i = 0; i < groups.length; i += QUESTIONS_PER_FORM) {
    const chunk = groups.slice(i, i + QUESTIONS_PER_FORM);
    const first = chunk[0].sentenceId;
    const last = chunk[chunk.length - 1].sentenceId;
    const title =
      FORM_TITLE_PREFIX +
      (groups.length > QUESTIONS_PER_FORM ? '(英文 ' + first + '〜' + last + ')' : '');
    created.push(buildForm_(title, chunk, col));
  }

  writeOutput_(ss, created);
  SpreadsheetApp.getUi().alert(created.length + ' 件のフォームを作成しました。forms シートを確認してください。');
}

function buildForm_(title, groups, col) {
  const form = FormApp.create(title);
  form.setDescription(FORM_DESCRIPTION);
  form.setIsQuiz(true);
  form.setProgressBar(true);
  form.setCollectEmail(false); // 塾の運用に合わせて変更可

  groups.forEach(function (g, gi) {
    // 2文目以降は改ページしてから英文ヘッダーを置く
    if (gi > 0) form.addPageBreakItem().setTitle('英文 ' + g.sentenceId);
    const headerItem = form.addSectionHeaderItem();
    headerItem
      .setTitle('【英文 ' + g.sentenceId + '】 ' + g.sentenceEn)
      .setHelpText('配布訳:' + g.sentenceJa);

    g.questions.forEach(function (row) {
      const item = form.addMultipleChoiceItem();
      const correctLetter = String(row[col.correct]).trim().toUpperCase();
      const choiceTexts = [
        String(row[col.choice_a]),
        String(row[col.choice_b]),
        String(row[col.choice_c]),
        String(row[col.choice_d]),
      ];
      const letters = ['A', 'B', 'C', 'D'];
      if (letters.indexOf(correctLetter) === -1) {
        throw new Error(
          'sentence_id=' + g.sentenceId + ' q_no=' + row[col.q_no] +
          ' の correct が A〜D ではありません: "' + row[col.correct] + '"'
        );
      }

      item
        .setTitle('問' + row[col.q_no] + ' ' + String(row[col.question]))
        .setRequired(true)
        .setPoints(Number(row[col.points]) || 1);

      item.setChoices(
        choiceTexts.map(function (text, idx) {
          return item.createChoice(text, letters[idx] === correctLetter);
        })
      );

      const explanation = String(row[col.explanation] || '');
      if (explanation) {
        const feedback = FormApp.createFeedback().setText(explanation).build();
        item.setFeedbackForCorrect(feedback);
        item.setFeedbackForIncorrect(feedback);
      }
    });
  });

  return {
    title: title,
    editUrl: form.getEditUrl(),
    liveUrl: form.getPublishedUrl(),
    numQuestions: groups.reduce(function (n, g) { return n + g.questions.length; }, 0),
  };
}

function indexColumns_(header) {
  const required = [
    'sentence_id', 'sentence_en', 'sentence_ja', 'q_no', 'tag', 'question',
    'choice_a', 'choice_b', 'choice_c', 'choice_d', 'correct', 'points', 'explanation',
  ];
  const col = {};
  required.forEach(function (name) {
    const idx = header.indexOf(name);
    if (idx === -1) throw new Error('ヘッダー行に列 "' + name + '" がありません。');
    col[name] = idx;
  });
  return col;
}

function writeOutput_(ss, created) {
  let out = ss.getSheetByName(OUTPUT_SHEET_NAME);
  if (!out) out = ss.insertSheet(OUTPUT_SHEET_NAME);
  if (out.getLastRow() === 0) {
    out.appendRow(['作成日時', 'タイトル', '設問数', '編集用URL', '回答用URL']);
  }
  const now = new Date();
  created.forEach(function (f) {
    out.appendRow([now, f.title, f.numQuestions, f.editUrl, f.liveUrl]);
  });
}
