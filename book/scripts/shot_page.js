// build/<名前>.html を PNG と PDF にする。スマホ幅・暗い色の確認用の画像も出す。
//   node scripts/shot_page.js 言葉の3つ比較_50
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const name = process.argv[2];
  const src = 'file://' + path.resolve(`build/${name}.html`);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1200 }, deviceScaleFactor: 2, colorScheme: 'light' });
  await page.goto(src);
  await page.evaluate(() => document.fonts.ready);
  console.log('横スクロール（PC幅）', await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth));
  await page.screenshot({ path: `build/${name}.png`, fullPage: true });
  await page.pdf({ path: `build/${name}.pdf`, format: 'A4', printBackground: true, margin: { top: '11mm', bottom: '11mm', left: '10mm', right: '10mm' } });
  const chk = await browser.newPage({ viewport: { width: 1100, height: 1000 }, deviceScaleFactor: 1, colorScheme: 'light' });
  await chk.goto(src); await chk.evaluate(() => document.fonts.ready);
  await chk.screenshot({ path: 'build/_chk_pc.png', fullPage: true, clip: { x: 0, y: 0, width: 1100, height: 1500 } });
  await chk.close();
  const sp = await browser.newPage({ viewport: { width: 400, height: 900 }, deviceScaleFactor: 1, colorScheme: 'dark' });
  await sp.goto(src); await sp.evaluate(() => document.fonts.ready);
  console.log('横スクロール（スマホ幅）', await sp.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth));
  await sp.screenshot({ path: 'build/_chk_sp.png', fullPage: true, clip: { x: 0, y: 0, width: 400, height: 1500 } });
  await browser.close();
})();
