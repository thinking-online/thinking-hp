// build/見本_4ページ完結_12番.html を PNG と PDF にする。はみ出しがあれば知らせる。
//   node scripts/shot_mock4.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const src = path.resolve('build/見本_4ページ完結_12番.html');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + src);
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => [...document.querySelectorAll('.page')].map((pg) => {
    const out = [];
    pg.querySelectorAll('.v').forEach((v) => {
      const box = v.parentElement.getBoundingClientRect();
      let minLeft = Infinity, maxBottom = -Infinity;
      v.querySelectorAll('*').forEach((e) => {
        const r = e.getBoundingClientRect();
        if (r.width && r.height) { minLeft = Math.min(minLeft, r.left); maxBottom = Math.max(maxBottom, r.bottom); }
      });
      out.push({ left: Math.round(minLeft - box.left), bottom: Math.round(box.bottom - maxBottom) });
    });
    return { p: pg.dataset.p, out };
  }));
  // left が マイナスなら、左にはみ出している（縦書きは左へ進む）。数字は、残りの余白（px）
  console.log(JSON.stringify(over));
  await page.screenshot({ path: 'build/見本_4ページ完結_12番.png', fullPage: true });
  const body = await page.evaluate(() => ({ w: document.body.scrollWidth, h: document.body.scrollHeight }));
  await page.pdf({ path: 'build/見本_4ページ完結_12番.pdf', width: body.w + 'px', height: body.h + 'px', printBackground: true });
  await browser.close();
})();
