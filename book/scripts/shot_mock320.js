// build/見本_320ページの構成.html を PNG にする。ページから文字がはみ出していたら知らせる。
//   node scripts/shot_mock320.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const name = '見本_320ページの構成';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1180, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(`build/${name}.html`));
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page .body').forEach((b, i) => {
      const top = b.getBoundingClientRect().top;
      let bottom = top;
      b.querySelectorAll(':scope > *').forEach((e) => { bottom = Math.max(bottom, e.getBoundingClientRect().bottom); });
      const used = Math.round(bottom - top);
      res.push(`本文の枠${i + 1}: 枠 ${b.clientHeight}px、中身 ${used}px、${used > b.clientHeight ? 'はみ出し ' + (used - b.clientHeight) : '残り ' + (b.clientHeight - used)}px`);
    });
    document.querySelectorAll('.b').forEach((b) => { if (b.scrollHeight > b.clientHeight + 1) res.push('小さい図の言葉がはみ出し: ' + b.textContent.slice(0, 14)); });
    res.push('横にはみ出し: ' + (document.documentElement.scrollWidth > document.documentElement.clientWidth));
    return res;
  });
  over.forEach((l) => console.log(l));
  await page.screenshot({ path: `build/${name}.png`, fullPage: true });
  await browser.close();
})();
