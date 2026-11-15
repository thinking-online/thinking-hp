// build/見本_8ページ_案A.html・案B.html を PNG にする。はみ出しがあれば知らせる。
//   node scripts/shot_mock8.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  for (const v of ['A', 'B']) {
    const page = await browser.newPage({ viewport: { width: 2100, height: 1700 }, deviceScaleFactor: 2 });
    await page.goto('file://' + path.resolve(`build/見本_8ページ_案${v}.html`));
    await page.evaluate(() => document.fonts.ready);
    const over = await page.evaluate(() => {
      const res = [];
      document.querySelectorAll('.page').forEach((pg) => {
        const pr = pg.getBoundingClientRect();
        // 縦書きのかたまり：左にはみ出していないか
        pg.querySelectorAll('.v, .mv, .big, .decl').forEach((el) => {
          const box = el.getBoundingClientRect();
          let minLeft = Infinity;
          el.querySelectorAll('*').forEach((e) => {
            const r = e.getBoundingClientRect();
            if (r.width && r.height) minLeft = Math.min(minLeft, r.left);
          });
          if (minLeft === Infinity) minLeft = box.left;
          const limit = el.classList.contains('v') || el.classList.contains('mv') ? box.left : pr.left + 20;
          const room = Math.round(minLeft - limit);
          res.push(`${pg.dataset.p}:${el.className.split(' ')[0]}=${room}`);
        });
        // ページの下にはみ出していないか
        let maxBottom = 0;
        pg.querySelectorAll('*').forEach((e) => { if (!e.classList.contains('pno')) maxBottom = Math.max(maxBottom, e.getBoundingClientRect().bottom); });
        const b = Math.round(pr.bottom - maxBottom);
        if (b < 20) res.push(`${pg.dataset.p}:下=${b}`);
      });
      return res;
    });
    console.log('案' + v, over.join('  '));   // 数字がマイナスなら、はみ出している
    await page.screenshot({ path: `build/見本_8ページ_案${v}.png`, fullPage: true });
    // 確かめる用に、見開きごとの小さい画像も出す
    const page1 = await browser.newPage({ viewport: { width: 2100, height: 1700 }, deviceScaleFactor: 1 });
    await page1.goto('file://' + path.resolve(`build/見本_8ページ_案${v}.html`));
    await page1.evaluate(() => document.fonts.ready);
    const sp = await page1.$$('.spread');
    for (let i = 0; i < sp.length; i++) await sp[i].screenshot({ path: `build/_chk_${v}${i + 1}.png` });
    await page1.close();
    await page.close();
  }
  await browser.close();
})();
