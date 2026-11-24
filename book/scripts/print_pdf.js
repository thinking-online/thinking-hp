// HTMLを、ページ番号つきのPDFにする。 node scripts/print_pdf.js 入力.html 出力.pdf [下に入れる言葉]
// 3つ目を渡した時は、下の左にその言葉を入れて、見出しからしおりを作る
const { chromium } = require('playwright');
(async () => {
  const [inp, out, label] = process.argv.slice(2);
  const esc = t => t.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const foot = label
    ? `<div style="width:100%;padding:0 20mm;display:flex;justify-content:space-between;font-size:7.5px;color:#888;font-family:'Noto Sans CJK JP',sans-serif"><span>${esc(label)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`
    : '<div style="width:100%;text-align:center;font-size:8px;color:#888;font-family:sans-serif"><span class="pageNumber"></span> / <span class="totalPages"></span></div>';
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + inp, { waitUntil: 'load' });
  await p.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: foot,
    margin: { top: '18mm', bottom: '20mm', left: '20mm', right: '20mm' },
    ...(label ? { outline: true, tagged: true } : {}),
  });
  await b.close();
})();
