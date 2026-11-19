// build/見本_縦書きの構成.html を PNG にする。行のずれや、はみ出しがあれば知らせる。
//   node scripts/shot_mock_tate.js              → 見本_縦書きの構成
//   node scripts/shot_mock_tate.js 名前          → build/名前.html を PNG にする
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const name = process.argv[2] || '見本_縦書きの構成';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1180, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(`build/${name}.html`));
  await page.waitForFunction(() => document.body.dataset.done === '1');
  const rep = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.sps').forEach((b) => {
      res.push(`${b.dataset.src}: 全部で ${b.dataset.total / 26}行 → ${b.dataset.pages}ページ（最後のページの空き ${b.dataset.pages * 16 - b.dataset.total / 26}行）`);
      const src = document.getElementById(b.dataset.src);
      [...src.children].forEach((el) => {
        const w = el.getBoundingClientRect().width + parseFloat(getComputedStyle(el).marginRight);
        if (Math.abs(w / 26 - Math.round(w / 26)) > 0.02) res.push('　行の幅がずれている: ' + el.className + ' ' + w + 'px ' + el.textContent.slice(0, 12));
        if (el.scrollHeight > 529) res.push('　下にはみ出し: ' + el.className + ' ' + el.scrollHeight);
      });
      src.querySelectorAll('.sbox,.vkoma .k,.mbox,.gbox').forEach((el) => {
        if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) res.push('　ブロックの中がはみ出し: ' + el.className + ' ' + el.scrollWidth + 'x' + el.scrollHeight + ' / ' + el.clientWidth + 'x' + el.clientHeight);
      });
    });
    res.push('横にはみ出し: ' + (document.documentElement.scrollWidth > document.documentElement.clientWidth));
    return res;
  });
  rep.forEach((l) => console.log(l));
  await page.screenshot({ path: `build/${name}.png`, fullPage: true });
  await browser.close();
})();
