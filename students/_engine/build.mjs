#!/usr/bin/env node
/**
 * THINKING 個別戦略シート ビルダー
 * ------------------------------------------------------------------
 *   node students/_engine/build.mjs students/<生徒スラッグ>
 *
 *   students/<生徒スラッグ>/data.json  →  index.html （+ strategy-sheet.pdf）
 *
 * data.json のブロック仕様は students/README.md を参照。
 * PDF 化は Chromium ヘッドレスの --print-to-pdf を使用（日本語フォント同梱）。
 */

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..", "..");

/* ---------------- 小さなユーティリティ ---------------- */

const esc = (s = "") =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/** **強調** と 〔小文字注記〕 だけを許すミニマークアップ */
const md = (s = "") =>
  esc(s)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\/\/(.+?)\/\//g, '<span style="color:var(--ink-3)">$1</span>')
    .replace(/\n/g, "<br>");

const num = (n, d = 1) =>
  Number(n).toFixed(d).replace(/\.0+$/, (m) => (d === 0 ? "" : m));

const fmt = (n) => {
  const v = Number(n);
  return Number.isInteger(v) ? String(v) : v.toFixed(1);
};

const level = (pct) => (pct >= 80 ? "hi" : pct >= 60 ? "mid" : "lo");

/* ---------------- ブロックレンダラ ---------------- */

const R = {
  h: (b) => `<h3 class="blk">${md(b.text)}</h3>`,

  p: (b) =>
    `<p class="sec-lead"${b.tight ? ' style="margin-bottom:3mm"' : ""}>${md(b.text)}</p>`,

  ul: (b) =>
    `<ul class="bul${b.tight ? " tight" : ""}">${b.items
      .map((i) => `<li>${md(i)}</li>`)
      .join("")}</ul>`,

  ol: (b) =>
    `<ol class="num">${b.items.map((i) => `<li>${md(i)}</li>`).join("")}</ol>`,

  cards: (b) =>
    `<div class="${b.cols === 3 ? "grid3" : b.cols === 4 ? "grid4" : "grid2"}">${b.items
      .map(
        (c) => `<div class="card${c.style ? " is-" + c.style : ""}">
          ${c.kicker ? `<div class="c-kicker">${esc(c.kicker)}</div>` : ""}
          ${c.title ? `<div class="c-title">${md(c.title)}</div>` : ""}
          ${c.body ? `<p class="c-body">${md(c.body)}</p>` : ""}
        </div>`
      )
      .join("")}</div>`,

  steps: (b) =>
    `<div class="steps">${b.items
      .map(
        (s, i) => `<div class="step">
          <div class="step-no">${s.no ?? i + 1}</div>
          <div class="step-txt">
            <div class="step-t">${md(s.title)}</div>
            ${s.desc ? `<div class="step-d">${md(s.desc)}</div>` : ""}
          </div>
        </div>`
      )
      .join("")}</div>`,

  kpis: (b) =>
    `<div class="kpirow${b.items.length === 3 ? " k3" : ""}">${b.items
      .map(
        (k) => `<div class="kpi${k.style ? " " + k.style : ""}">
          <div class="k-l">${esc(k.label)}</div>
          <div class="k-v">${esc(k.value)}${k.unit ? `<small>${esc(k.unit)}</small>` : ""}</div>
          ${k.note ? `<div class="k-n">${esc(k.note)}</div>` : ""}
        </div>`
      )
      .join("")}</div>`,

  callout: (b) =>
    `<div class="callout${b.style === "navy" ? " is-navy" : ""}">
      ${b.title ? `<div class="co-t">${md(b.title)}</div>` : ""}
      <div class="co-b">${md(b.body)}</div>
    </div>`,

  checks: (b) =>
    `<div class="checks">${b.items
      .map((c) => `<div class="check"><span class="box"></span><span>${md(c)}</span></div>`)
      .join("")}</div>`,

  wish: (b) =>
    `<div class="wish">${b.items
      .map(
        (w, i) => `<div class="wish-row">
          <div class="wish-rank">${i + 1}</div>
          <div class="wish-main">
            <div class="wish-univ">${esc(w.univ)}</div>
            <div class="wish-fac">${esc(w.fac)}</div>
          </div>
          ${w.tag ? `<div class="wish-tag"><span class="pill p-${w.tagStyle || "base"}">${esc(w.tag)}</span></div>` : ""}
        </div>`
      )
      .join("")}</div>`,

  /** 模試得点表（合計は自動計算） */
  score: (b) => {
    const rows = b.rows;
    const sum = rows.reduce(
      (a, r) => ({
        conv: a.conv + Number(r.conv),
        convMax: a.convMax + Number(r.convMax),
        target: a.target + Number(r.target ?? r.conv),
      }),
      { conv: 0, convMax: 0, target: 0 }
    );
    const body = rows
      .map((r) => {
        const pct = (Number(r.conv) / Number(r.convMax)) * 100;
        const tpct = (Number(r.target ?? r.conv) / Number(r.convMax)) * 100;
        const lv = level(pct);
        const gap = Number(r.target ?? r.conv) - Number(r.conv);
        return `<tr${r.sub ? ' class="is-sub"' : ""}>
          <td class="s-name"><b>${esc(r.name)}</b>${r.note ? `<span>${esc(r.note)}</span>` : ""}</td>
          <td class="s-num">${fmt(r.conv)}<i>/${fmt(r.convMax)}</i></td>
          <td class="s-bar">
            <div class="track lv-${lv}">
              <div class="fill" style="width:${pct.toFixed(1)}%"></div>
              <div class="tick" style="left:${tpct.toFixed(1)}%"></div>
            </div>
          </td>
          <td class="s-pct lv-${lv}">${pct.toFixed(1)}<i>%</i></td>
          <td class="s-tgt">${fmt(r.target ?? r.conv)}</td>
          <td class="s-gap">${gap > 0 ? "+" + fmt(gap) : gap < 0 ? fmt(gap) : "—"}</td>
        </tr>`;
      })
      .join("");

    const sPct = (sum.conv / sum.convMax) * 100;
    const tPct = (sum.target / sum.convMax) * 100;
    return `<table class="score">
      <thead><tr>
        <th class="t-name">科目</th>
        <th>換算得点</th>
        <th class="t-bar">現在地 ／ ▼ 目標</th>
        <th>得点率</th>
        <th>目標</th>
        <th>必要</th>
      </tr></thead>
      <tbody>${body}
        <tr class="is-sum">
          <td class="s-name"><b>合計</b></td>
          <td class="s-num">${fmt(sum.conv)}<i>/${fmt(sum.convMax)}</i></td>
          <td class="s-bar">
            <div class="track lv-${level(sPct)}">
              <div class="fill" style="width:${sPct.toFixed(1)}%"></div>
              <div class="tick" style="left:${tPct.toFixed(1)}%"></div>
            </div>
          </td>
          <td class="s-pct lv-${level(sPct)}">${sPct.toFixed(1)}<i>%</i></td>
          <td class="s-tgt">${fmt(sum.target)}</td>
          <td class="s-gap">+${fmt(sum.target - sum.conv)}</td>
        </tr>
      </tbody></table>`;
  },

  /** 配点構造の帯グラフ */
  weight: (b) => {
    const total = b.segs.reduce((a, s) => a + Number(s.value), 0);
    return `<div class="weight">
      <div class="weight-bar">${b.segs
        .map((s, i) => {
          const p = (Number(s.value) / total) * 100;
          return `<div class="wseg w${s.cls || i + 1}" style="width:${p.toFixed(2)}%">
            <div class="w-t">${esc(s.label)}</div>
            <div class="w-v">${p.toFixed(1)}%</div>
          </div>`;
        })
        .join("")}</div>
      ${
        b.legend
          ? `<div class="weight-legend">${b.legend
              .map(
                (l, i) =>
                  `<span><i style="background:${l.color}"></i>${md(l.text)}</span>`
              )
              .join("")}</div>`
          : ""
      }
    </div>`;
  },

  table: (b) =>
    `<table class="plain">
      ${b.head ? `<thead><tr>${b.head.map((h, i) => `<th${b.widths?.[i] ? ` style="width:${b.widths[i]}"` : ""}>${esc(h)}</th>`).join("")}</tr></thead>` : ""}
      <tbody>${b.rows
        .map((r) => `<tr>${r.map((c) => `<td>${md(c)}</td>`).join("")}</tr>`)
        .join("")}</tbody>
    </table>`,

  memo: (b) =>
    `<div class="memo">
      ${b.title ? `<div class="mm-t">${esc(b.title)}</div>` : ""}
      ${Array.from({ length: b.lines || 5 }, () => `<div class="mm-line"></div>`).join("")}
    </div>`,

  sign: (b) =>
    `<div class="sign">${b.items
      .map(
        (s) => `<div class="sign-box"><div class="sg-l">${esc(s)}</div><div class="sg-line"></div></div>`
      )
      .join("")}</div>`,

  row: (b) =>
    `<div class="${b.cols === 3 ? "grid3" : "grid2"}"${b.style ? ` style="${b.style}"` : ""}>${b.items
      .map((col) => `<div class="stack-gap">${col.map(render).join("")}</div>`)
      .join("")}</div>`,

  space: (b) => `<div style="height:${b.h || "4mm"}"></div>`,

  /** 残り高さを吸収して、直後のブロックをページ下端に寄せる */
  fill: () => `<div class="pb-fill"></div>`,

  raw: (b) => b.html,
};

function render(block) {
  const fn = R[block.t];
  if (!fn) throw new Error(`未知のブロック種別: ${block.t}`);
  return fn(block);
}

/* ---------------- ページ組み立て ---------------- */

function coverPage(d) {
  const c = d.cover;
  return `<section class="page cover">
    <div class="cover-frame"></div>
    <div class="cover-inner">
      <div class="cover-brand">
        <div class="cb-en">THINK<i>I</i>NG</div>
        <div class="cb-jp">シンキング</div>
      </div>
      <div class="cover-eyebrow">${esc(c.eyebrow)}</div>
      <h1 class="cover-title">${md(c.title)}<em>${esc(c.subtitle)}</em></h1>
      <p class="cover-sub">${md(c.lead)}</p>
      <div class="cover-name">
        <div class="cn-label">生徒</div>
        <div class="cn-value">${esc(d.meta.student)}</div>
        <div class="cn-meta">${esc(d.meta.grade)}／${esc(d.meta.course)}</div>
      </div>
      <div class="cover-contents">
        <div class="cc-label">CONTENTS</div>
        ${d.pages
          .map(
            (p) =>
              `<div class="cc-item"><span class="cc-no">${esc(p.sec?.no ?? "")}</span><span>${esc(p.sec?.title ?? p.runner ?? "")}</span></div>`
          )
          .join("")}
      </div>
      <div class="cover-kpis">${c.kpis
        .map(
          (k) => `<div class="cover-kpi${k.style ? " " + k.style : ""}">
            <div class="k-label">${esc(k.label)}</div>
            <div class="k-value">${esc(k.value)}${k.unit ? `<small>${esc(k.unit)}</small>` : ""}</div>
            <div class="k-note">${esc(k.note || "")}</div>
          </div>`
        )
        .join("")}</div>
      <div class="cover-foot">
        <span>${esc(d.meta.date)} 作成／${esc(d.meta.advisor)}</span>
        <span>CONFIDENTIAL — ${esc(d.meta.student)} 様専用</span>
      </div>
    </div>
  </section>`;
}

function contentPage(p, i, total) {
  return `<section class="page">
    <div class="runner">
      <span class="r-left">THINK<span style="color:var(--gold)">I</span>NG</span>
      <span class="r-right">${esc(p.runner || "個別戦略シート")}</span>
    </div>
    <div class="page-body">
      ${
        p.sec
          ? `<div class="sec">
              <div class="sec-no">${esc(p.sec.no)}</div>
              <div class="sec-txt">
                <h2 class="sec-title">${md(p.sec.title)}</h2>
                ${p.sec.en ? `<div class="sec-en">${esc(p.sec.en)}</div>` : ""}
              </div>
            </div>`
          : ""
      }
      ${(p.blocks || []).map(render).join("\n")}
    </div>
    <div class="page-foot">
      <span>${esc(p.foot || "")}</span>
      <span class="pf-rule"></span>
      <span class="pf-no">${String(i).padStart(2, "0")}</span>
    </div>
  </section>`;
}

function buildHtml(d, css) {
  const pages = [coverPage(d), ...d.pages.map((p, i) => contentPage(p, i + 1, d.pages.length))];
  return `<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(d.meta.student)}｜${esc(d.meta.title)}｜THINKING</title>
<meta name="robots" content="noindex,nofollow,noarchive">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700&family=Shippori+Mincho+B1:wght@600;700&family=Cormorant+Garamond:wght@500;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<style>
${css}
</style>
</head>
<body>
${pages.join("\n")}
<script>
/* ?only=N でそのページだけ表示（レイアウト検証用） */
(function(){
  var m = /[?&]only=(\\d+)/.exec(location.search);
  if(!m) return;
  var n = parseInt(m[1],10);
  document.querySelectorAll('.page').forEach(function(el,i){
    if(i !== n) el.style.display='none';
  });
  document.body.style.padding='0';
  var sh = /[?&]shift=(\d+)/.exec(location.search);
  if(sh) document.querySelectorAll('.page')[n].style.marginTop = '-' + sh[1] + 'px';
})();

/* ?qa=1 で各ページのはみ出し量を出力（--dump-dom で回収する） */
(function(){
  if(!/[?&]qa=1/.test(location.search)) return;
  var out = [];
  document.querySelectorAll('.page').forEach(function(el,i){
    var b = el.querySelector('.page-body');
    var over = b ? Math.round(b.scrollHeight - b.clientHeight) : 0;
    var slack = b ? Math.round(b.clientHeight - (b.lastElementChild ? b.lastElementChild.getBoundingClientRect().bottom - b.getBoundingClientRect().top : 0)) : 0;
    out.push('PAGE ' + String(i).padStart(2,'0') + '  h=' + el.offsetHeight + 'px  bodyH=' + (b?b.clientHeight:0) + 'px  overflow=' + over + 'px  slack=' + slack + 'px');
  });
  document.querySelectorAll('.page').forEach(function(el){ el.style.display='none'; });
  var pre = document.createElement('pre');
  pre.id = 'qa-report';
  pre.style.cssText = 'font:16px/1.7 monospace;color:#111;background:#fff;padding:24px;margin:0;white-space:pre;';
  pre.textContent = out.join(String.fromCharCode(10));
  document.body.style.padding = '0';
  document.body.appendChild(pre);
})();
</script>
</body>
</html>`;
}

/* ---------------- PDF 出力 ---------------- */

const CHROME_CANDIDATES = [
  "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
  process.env.CHROME_PATH,
  "/usr/bin/chromium",
  "/usr/bin/google-chrome",
].filter(Boolean);

function findChrome() {
  for (const c of CHROME_CANDIDATES) if (fs.existsSync(c)) return c;
  return null;
}

function toPdf(htmlPath, pdfPath) {
  const chrome = findChrome();
  if (!chrome) {
    console.warn("! Chromium が見つからないため PDF 生成をスキップしました");
    return false;
  }
  execFileSync(
    chrome,
    [
      "--headless=new",
      "--disable-gpu",
      "--no-sandbox",
      "--hide-scrollbars",
      "--force-color-profile=srgb",
      "--font-render-hinting=none",
      "--run-all-compositor-stages-before-draw",
      // フォントはローカル（~/.fonts）に導入済みなので外部通信は遮断して決定的に描画する
      "--host-resolver-rules=MAP * ~NOTFOUND",
      "--disable-background-networking",
      "--disable-component-update",
      "--disable-default-apps",
      "--no-first-run",
      "--no-default-browser-check",
      "--virtual-time-budget=15000",
      "--no-pdf-header-footer",
      `--print-to-pdf=${pdfPath}`,
      `file://${htmlPath}`,
    ],
    { stdio: ["ignore", "ignore", "pipe"] }
  );
  return true;
}

/* ---------------- メイン ---------------- */

const dir = process.argv[2];
if (!dir) {
  console.error("使い方: node students/_engine/build.mjs students/<生徒スラッグ>");
  process.exit(1);
}
const absDir = path.resolve(ROOT, dir);
const data = JSON.parse(fs.readFileSync(path.join(absDir, "data.json"), "utf8"));
const css = fs.readFileSync(path.join(__dirname, "sheet.css"), "utf8");

const html = buildHtml(data, css);
const htmlPath = path.join(absDir, "index.html");
fs.writeFileSync(htmlPath, html, "utf8");
console.log(`✓ HTML  ${path.relative(ROOT, htmlPath)}  (${data.pages.length + 1} ページ)`);

if (!process.argv.includes("--no-pdf")) {
  const pdfPath = path.join(absDir, data.meta.pdfName || "strategy-sheet.pdf");
  if (toPdf(htmlPath, pdfPath)) {
    const kb = (fs.statSync(pdfPath).size / 1024).toFixed(0);
    console.log(`✓ PDF   ${path.relative(ROOT, pdfPath)}  (${kb} KB)`);
  }
}
