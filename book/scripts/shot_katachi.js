// build/タイトルの型_2案.html を PNG（確認用）と PDF（送る用）にする。
//   node scripts/shot_katachi.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const src = 'file://' + path.resolve('build/タイトルの型_2案.html');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1200 }, deviceScaleFactor: 2, colorScheme: 'light' });
  await page.goto(src);
  await page.evaluate(() => document.fonts.ready);
  const wide = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  console.log('横スクロール（PC幅）', wide);
  await page.screenshot({ path: 'build/タイトルの型_2案.png', fullPage: true });
  await page.pdf({ path: 'build/タイトルの型_2案.pdf', format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '11mm', right: '11mm' } });
  // スマホ幅と暗い色も1枚ずつ（確認用）
  const sp = await browser.newPage({ viewport: { width: 400, height: 900 }, deviceScaleFactor: 1, colorScheme: 'dark' });
  await sp.goto(src);
  await sp.evaluate(() => document.fonts.ready);
  console.log('横スクロール（スマホ幅）', await sp.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth));
  await sp.screenshot({ path: 'build/_chk_katachi_sp.png', clip: { x: 0, y: 0, width: 400, height: 2300 } });
  await browser.close();
})();
