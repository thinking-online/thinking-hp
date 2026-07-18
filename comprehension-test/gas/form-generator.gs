/**
 * 英文解釈 確認テスト — Googleフォーム一括生成スクリプト(横持ちCSV形式対応)
 *
 * 使い方:
 * 1. questions-60.csv をGoogleスプレッドシートにインポートする
 *    (ファイル > インポート > アップロード > 「現在のシートを置き換える」)。
 *    シート名を「questions」にする。
 * 2. スプレッドシートの「拡張機能 > Apps Script」にこのファイルを貼り付ける。
 * 3. createFormsFromSheet() を実行(初回は権限承認が必要)。
 * 4. forms シートに生成されたフォームのURL(編集用・回答用)が書き込まれる。
 *
 * シート形式(1行 = 1英文):
 *   問題No | 問題(英文) | 訳 | 問題01 | 問題01の答え | 問題01の解説 | 問題02 | ... | 問題04の解説
 *   - 「問題0X」セル: 1行目以降が設問文、"A. " "B. " "C. " "D. " で始まる行が選択肢(セル内改行区切り)
 *   - 「問題0Xの答え」セル: A/B/C/D の1文字(後ろに補足があっても先頭1文字を採用)
 *   - 「問題0Xの解説」セル: 解答後に表示するフィードバック文
 *   - 設問が3問しかない英文は「問題04」列を空欄にする(自動でスキップ)
 *
 * 仕様:
 * - クイズモードで作成(自動採点)。設問はすべて必須・4択。
 * - 英文ごとにセクションを作り、英文+配布訳を表示してから設問を並べる。
 * - 解説は正解時/不正解時どちらのフィードバックにも紐づけ。
 * - SENTENCES_PER_FORM 文ごとにフォームを分割(既定10文=1フォーム、60文なら6フォーム)。
 */

const SHEET_NAME = 'questions';
const OUTPUT_SHEET_NAME = 'forms';
const SENTENCES_PER_FORM = 10;
const MAX_QUESTIONS = 6;
const FORM_TITLE_PREFIX = '英文解釈 確認テスト';
const FORM_DESCRIPTION =
  'それぞれの英文について、本当の意味で理解できているかを確認するテストです。' +
  '訳の暗記ではなく、英文そのものを読んで答えてください。';

function createFormsFromSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) throw new Error('シート "' + SHEET_NAME + '" が見つかりません。');

  const rows = sheet.getDataRange().getValues();
  const header = rows.shift().map(String);
  const col = indexColumns_(header);

  // 1行=1英文としてパース
  const sentences = [];
  rows.forEach(function (row, ri) {
    const no = String(row[col.no]).trim();
    if (!no) return; // 空行スキップ
    const questions = [];
    for (let qi = 1; qi <= MAX_QUESTIONS; qi++) {
      const qCell = String(row[col['q' + qi]] || '').trim();
      if (!qCell) continue;
      questions.push(parseQuestionCell_(qCell, String(row[col['a' + qi]] || ''), String(row[col['e' + qi]] || ''), no, qi, ri + 2));
    }
    if (questions.length === 0) {
      throw new Error('行 ' + (ri + 2) + '(問題No ' + no + ')に設問がありません。');
    }
    sentences.push({
      no: no,
      en: String(row[col.en]),
      ja: String(row[col.ja]),
      questions: questions,
    });
  });
  if (sentences.length === 0) throw new Error('questions シートにデータ行がありません。');

  const created = [];
  for (let i = 0; i < sentences.length; i += SENTENCES_PER_FORM) {
    const chunk = sentences.slice(i, i + SENTENCES_PER_FORM);
    const title =
      FORM_TITLE_PREFIX +
      (sentences.length > SENTENCES_PER_FORM
        ? '(英文 ' + chunk[0].no + '〜' + chunk[chunk.length - 1].no + ')'
        : '');
    created.push(buildForm_(title, chunk));
  }

  writeOutput_(ss, created);
  SpreadsheetApp.getUi().alert(created.length + ' 件のフォームを作成しました。forms シートを確認してください。');
}

/**
 * 「問題0X」セルを設問文+選択肢A〜Dに分解し、答え・解説と合わせて検証する。
 * 期待形式: 設問文(複数行可)のあとに "A. " 〜 "D. " で始まる行が各1つ。
 */
function parseQuestionCell_(qCell, answerCell, explanation, no, qi, rowNum) {
  const lines = qCell.split('\n');
  const questionLines = [];
  const choices = { A: null, B: null, C: null, D: null };
  let seenChoice = false;
  lines.forEach(function (line) {
    const m = line.match(/^([A-D])[.．]\s*(.*)$/);
    if (m) {
      seenChoice = true;
      choices[m[1]] = (choices[m[1]] ? choices[m[1]] + '\n' : '') + m[2];
    } else if (!seenChoice) {
      questionLines.push(line);
    } else if (line.trim()) {
      // 選択肢の折り返し行(前の選択肢の続き)
      const lastLetter = ['D', 'C', 'B', 'A'].find(function (L) { return choices[L] !== null; });
      choices[lastLetter] += '\n' + line;
    }
  });

  const missing = ['A', 'B', 'C', 'D'].filter(function (L) { return !choices[L]; });
  if (missing.length) {
    throw new Error('行 ' + rowNum + ' 問題0' + qi + ': 選択肢 ' + missing.join(',') + ' が見つかりません。セル内で "A. " 形式の行になっているか確認してください。');
  }
  const answer = String(answerCell).trim().charAt(0).toUpperCase();
  if (['A', 'B', 'C', 'D'].indexOf(answer) === -1) {
    throw new Error('行 ' + rowNum + ' 問題0' + qi + 'の答えが A〜D ではありません: "' + answerCell + '"');
  }
  return {
    title: '【英文' + no + '-問' + qi + '】 ' + questionLines.join('\n').trim(),
    choices: choices,
    answer: answer,
    explanation: String(explanation).trim(),
  };
}

function buildForm_(title, sentences) {
  const form = FormApp.create(title);
  form.setDescription(FORM_DESCRIPTION);
  form.setIsQuiz(true);
  form.setProgressBar(true);
  form.setCollectEmail(false); // 運用に合わせて変更可
  form.setShuffleQuestions(false);

  sentences.forEach(function (s, si) {
    if (si > 0) form.addPageBreakItem().setTitle('英文 ' + s.no);
    form.addSectionHeaderItem()
      .setTitle('【英文 ' + s.no + '】 ' + s.en)
      .setHelpText('配布訳:' + s.ja);

    s.questions.forEach(function (q) {
      const item = form.addMultipleChoiceItem();
      item.setTitle(q.title).setRequired(true).setPoints(1);
      item.setChoices(
        ['A', 'B', 'C', 'D'].map(function (L) {
          return item.createChoice(L + '. ' + q.choices[L], L === q.answer);
        })
      );
      if (q.explanation) {
        const fb = FormApp.createFeedback().setText(q.explanation).build();
        item.setFeedbackForCorrect(fb);
        item.setFeedbackForIncorrect(fb);
      }
    });
  });

  return {
    title: title,
    editUrl: form.getEditUrl(),
    liveUrl: form.getPublishedUrl(),
    numQuestions: sentences.reduce(function (n, s) { return n + s.questions.length; }, 0),
  };
}

function indexColumns_(header) {
  // 列名は日本語ヘッダーに一致させる(questions-60.csv のヘッダーと同一)
  const map = {
    no: '問題No',
    en: '問題',
    ja: '訳',
  };
  for (let i = 1; i <= MAX_QUESTIONS; i++) {
    map['q' + i] = '問題0' + i;
    map['a' + i] = '問題0' + i + 'の答え';
    map['e' + i] = '問題0' + i + 'の解説';
  }
  const col = {};
  Object.keys(map).forEach(function (key) {
    const idx = header.indexOf(map[key]);
    if (idx === -1) throw new Error('ヘッダー行に列 "' + map[key] + '" がありません。CSVを1行目ごとインポートしたか確認してください。');
    col[key] = idx;
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
