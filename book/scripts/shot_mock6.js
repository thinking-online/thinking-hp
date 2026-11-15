// build/見本_6ページ.html を PNG にする。はみ出しがあれば知らせる。
//   node scripts/shot_mock6.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve('build/見本_6ページ.html'));
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page').forEach((pg) => {
      const pr = pg.getBoundingClientRect();
      pg.querySelectorAll('.v').forEach((el) => {
        const box = el.getBoundingClientRect();
        let minLeft = box.right;
        el.querySelectorAll('*').forEach((e) => {
          const r = e.getBoundingClientRect();
          if (r.width && r.height) minLeft = Math.min(minLeft, r.left);
        });
        res.push(`${pg.dataset.p}:左の余り=${Math.round(minLeft - box.left)}`);
      });
      let maxBottom = 0;
      pg.querySelectorAll('*').forEach((e) => { if (!e.classList.contains('pno')) maxBottom = Math.max(maxBottom, e.getBoundingClientRect().bottom); });
      res.push(`${pg.dataset.p}:下の余り=${Math.round(pr.bottom - maxBottom)}`);
    });
    return res;
  });
  console.log(over.join('  '));       // 左の余りがマイナス、下の余りが60より小さい時は、はみ出している
  await page.screenshot({ path: 'build/見本_6ページ.png', fullPage: true });
  await browser.close();
})();
