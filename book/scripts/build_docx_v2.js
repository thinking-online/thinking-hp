// 原稿_v2_マーカー.md を、Googleドキュメントで開ける .docx にする。book/ で実行。
//   node scripts/build_docx_v2.js
// 見出し1＝章などの大きな区切り　見出し2＝項目（01〜50）　見出し3＝節　見出し4＝STEP・小見出し
// 飾りは最小限。マーカー（==…==）は黄色の蛍光ペン。ページ区切りは入れない。
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
} = require('docx');

const SRC = process.argv[2] || 'manuscript/原稿_v2_マーカー.md';
const OUT = process.argv[3] || 'build/原稿_v2.docx';
const FONT = 'Noto Sans JP';
const NAVY = '15467E';
const GRAY = '666666';
const F = { ascii: FONT, eastAsia: FONT, hAnsi: FONT, cs: FONT };

let raw = fs.readFileSync(SRC, 'utf8');
if (raw.startsWith('# 原稿')) raw = raw.split('\n---\n').slice(1).join('\n---\n');
const lines = raw.split('\n');

function runs(text, base = {}) {
  // ==…== を蛍光ペンにする
  const out = [];
  const re = /==(.+?)==/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: F, ...base }));
    out.push(new TextRun({ text: m[1], font: F, highlight: 'yellow', ...base }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: F, ...base }));
  if (!out.length) out.push(new TextRun({ text: '', font: F, ...base }));
  return out;
}

const children = [];
children.push(new Paragraph({
  heading: HeadingLevel.TITLE,
  children: [new TextRun({ text: '頭のいい人が絶対にやらないこと', font: F })],
}));
children.push(new Paragraph({
  spacing: { after: 240 },
  children: [new TextRun({ text: '原稿（8章・50本）　朝倉 徹大', font: F, color: GRAY })],
}));

function para(text, opt = {}, runopt = {}) {
  children.push(new Paragraph({ ...opt, children: runs(text, runopt) }));
}

let i = 0;
const N = lines.length;
while (i < N) {
  let l = lines[i].replace(/\s+$/, '');
  // かたまり（``` … ```）：字下げした、ふつうの段落にする
  if (l.startsWith('```')) {
    i++;
    const buf = [];
    while (i < N && !lines[i].startsWith('```')) { buf.push(lines[i].replace(/\s+$/, '')); i++; }
    i++;
    while (buf.length && !buf[0].trim()) buf.shift();
    while (buf.length && !buf[buf.length - 1].trim()) buf.pop();
    buf.forEach((b, k) => {
      const t = b.replace(/^　{1,2}/, '');
      para(t, {
        indent: { left: 480 },
        spacing: { before: k === 0 ? 60 : 0, after: k === buf.length - 1 ? 140 : 0, line: 320 },
      });
    });
    continue;
  }
  if (/^\s*---\s*$/.test(l)) { i++; continue; }
  if (!l.trim()) { i++; continue; }
  const h = l.match(/^(#{1,6})\s+(.*)$/);
  if (h) {
    const lv = h[1].length, t = h[2];
    let heading;
    if (lv === 1) heading = HeadingLevel.HEADING_1;
    else if (lv === 2 && /^\d{2}　/.test(t)) heading = HeadingLevel.HEADING_2;
    else if (lv === 2) heading = HeadingLevel.HEADING_3;
    else heading = HeadingLevel.HEADING_4;
    children.push(new Paragraph({ heading, children: [new TextRun({ text: t.replace(/==/g, ''), font: F })] }));
    i++; continue;
  }
  // ふつうの文。空行までを1かたまりとして、行ごとに段落にする
  const buf = [];
  while (i < N && lines[i].trim() && !lines[i].startsWith('#') && !lines[i].startsWith('```')
         && !/^\s*---\s*$/.test(lines[i])) { buf.push(lines[i].replace(/\s+$/, '')); i++; }
  buf.forEach((b, k) => {
    const lastLine = k === buf.length - 1;
    const sp = { before: 0, after: lastLine ? 140 : 0, line: 340 };
    const t = b.replace(/^　+/, '');
    const indented = /^　{2}/.test(b);
    if (/^〔.+〕$/.test(t)) {                       // 章の副題
      para(t, { spacing: sp }, { color: GRAY });
    } else if (t.startsWith('×「')) {
      para(t, { indent: { left: 480 }, spacing: sp }, { color: GRAY });
    } else if (t.startsWith('○「')) {
      para(t, { indent: { left: 480 }, spacing: sp }, { color: NAVY, bold: true });
    } else if (t.startsWith('「できた」の基準')) {
      para(t, { spacing: { before: 60, after: 140, line: 340 } }, { color: NAVY, bold: true });
    } else if (t.startsWith('もとにある絶対法則') || t.startsWith('絶対法則 ')) {
      para(t, { spacing: sp }, { color: NAVY });
    } else if (t.startsWith('今日やること')) {
      para(t, { spacing: { before: 60, after: 200, line: 340 } }, { bold: true });
    } else if (indented) {
      para(t, { indent: { left: 480 }, spacing: sp });
    } else {
      para(t, { spacing: sp });
    }
  });
}

const hd = (size, before, after, color) => ({
  run: { font: F, size, bold: true, color },
  paragraph: { spacing: { before, after }, keepNext: true },
});
const doc = new Document({
  creator: '朝倉 徹大',
  title: '頭のいい人が絶対にやらないこと　原稿',
  styles: {
    default: {
      document: { run: { font: F, size: 21 }, paragraph: { spacing: { line: 340 } } },
      title: { run: { font: F, size: 40, bold: true, color: NAVY }, paragraph: { spacing: { before: 0, after: 80 } } },
      heading1: hd(32, 600, 200, NAVY),
      heading2: hd(26, 480, 140, '000000'),
      heading3: hd(22, 280, 100, NAVY),
      heading4: hd(21, 200, 60, '000000'),
    },
  },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1247, right: 1247 } } },
    children,
  }],
});
Packer.toBuffer(doc).then((buf) => {
  fs.mkdirSync('build', { recursive: true });
  fs.writeFileSync(OUT, buf);
  console.log('段落', children.length, '→', OUT);
});
