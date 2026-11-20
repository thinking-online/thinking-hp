// build/名前.html（scripts/build_tate_book.py が作る）を、A5のPDFにする。ページ数と、気になる所を知らせる。
//   node scripts/print_tate_book.js 本の形_マックス版
//   --nopdf をつけると、数えるだけ（PDFは作らない）
//   --shot=12,13 をつけると、そのページの画像を build/_本の形_確認/ に出す
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const name = process.argv[2];
  const args = process.argv.slice(3);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 504, height: 714 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve('build/' + name + '.html'));
  await page.waitForFunction(() => document.body.dataset.done === '1', null, { timeout: 600000 });
  const rep = await page.evaluate(() => window.__rep);
  const parts = {};
  rep.flows.forEach((f) => { parts[f.part] = (parts[f.part] || 0) + f.pages; });
  console.log('全部で ' + rep.total + 'ページ');
  Object.keys(parts).forEach((k) => console.log('　' + k + '：' + parts[k] + 'ページ'));
  const items = rep.flows.filter((f) => f.part.startsWith('07〜'));
  const by = {};
  items.forEach((f) => { (by[f.pages] = by[f.pages] || []).push(f.name); });
  Object.keys(by).forEach((k) => console.log('　　07番から先で ' + k + 'ページ：' + by[k].length + '個　' + by[k].join(' ')));
  const others = rep.flows.filter((f) => !f.part.startsWith('07〜') && !f.name.endsWith('（扉）'));
  console.log('　　ほかの流れ：' + others.map((f) => f.name.slice(0, 12) + '=' + f.pages).join('　'));
  rep.warn.forEach((w) => console.log('　！' + w));
  // それぞれの部分が、何ページ目から始まるか
  const starts = await page.evaluate(() => {
    const seen = {}, res = [];
    document.querySelectorAll('.page').forEach((p, i) => {
      const key = p.dataset.name + (p.classList.contains('fixed') ? '（扉）' : '');
      if (!seen[key]) { seen[key] = 1; res.push([key, i + 1]); }
    });
    return res;
  });
  if (args.includes('--index')) console.log('　　始まるページ：' + starts.map((s) => s[1] + ':' + s[0].slice(0, 10)).join('  '));
  fs.writeFileSync('build/' + name + '_ページ数.json', JSON.stringify({ total: rep.total, flows: rep.flows.map((f) => [f.part, f.name, f.pages, f.rows]), starts }));
  const shot = args.find((a) => a.startsWith('--shot='));
  if (shot) {
    fs.mkdirSync('build/_本の形_確認', { recursive: true });
    const pages = await page.$$('.page');
    for (const n of shot.slice(7).split(',').map(Number)) {
      if (pages[n - 1]) await pages[n - 1].screenshot({ path: 'build/_本の形_確認/' + name + '_' + String(n).padStart(3, '0') + '.png' });
    }
  }
  if (!args.includes('--nopdf')) {
    await page.pdf({ path: 'build/' + name + '.pdf', width: '148mm', height: '210mm', scale: 1.1098, printBackground: true });
    console.log('PDF：build/' + name + '.pdf　' + (fs.statSync('build/' + name + '.pdf').size / 1e6).toFixed(1) + 'MB');
  }
  await browser.close();
})();
