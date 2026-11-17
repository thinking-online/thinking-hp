// HTMLを、ページ番号つきのPDFにする。 node scripts/print_pdf.js 入力.html 出力.pdf
const { chromium } = require('playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + inp, { waitUntil: 'load' });
  await p.pdf({
    path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-size:8px;color:#888;font-family:sans-serif"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '18mm', bottom: '20mm', left: '20mm', right: '20mm' },
  });
  await b.close();
})();
