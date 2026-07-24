#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""夏休み英単語300 — 特典用の単語帳ブックレット(印刷/PDF)を生成する。"""
import csv, html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "idiom200_words.csv")
OUT = os.path.join(ROOT, "booklet.html")

def esc(s): return html.escape(s or "", quote=True)

rows = [r for r in csv.reader(open(SRC)) if r and r[0] != "No."]
# rows: [No, 単語, 意味, 出現冊数]

def stars(n):
    n = int(n)
    if n >= 5: return 3
    if n >= 4: return 2
    return 1

CSS = """
@import url('');
:root{
  --navy:#16233f; --navy2:#22345c; --ink:#1c2331; --sub:#5b6373;
  --gold:#c79a3b; --gold-d:#a97f26; --line:#e6e2d6; --paper:#ffffff;
  --tint:#faf8f2; --chip:#eef1f7;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;color:var(--ink);
  font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",YuGothic,"Noto Sans JP",IPAGothic,Meiryo,sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.en{font-family:"Georgia","Times New Roman",serif}
.page{width:210mm;height:297mm;overflow:hidden;margin:0 auto;padding:13mm 14mm;background:var(--paper);position:relative}
.page + .page{page-break-before:always}

/* ---------- COVER ---------- */
.cover{background:linear-gradient(160deg,#16233f 0%,#22345c 55%,#2c4374 100%);color:#fff;
  min-height:297mm;padding:34mm 22mm;display:flex;flex-direction:column;justify-content:space-between}
.cover .kicker{letter-spacing:.5em;font-size:12px;color:var(--gold);font-weight:700;text-transform:uppercase}
.cover h1{font-size:52px;line-height:1.18;margin:20px 0 10px;font-weight:800;letter-spacing:.02em}
.cover h1 .accent{color:#f2d492}
.cover .lead{font-size:15px;line-height:1.9;color:#dfe4ef;max-width:150mm;margin-top:8px}
.cover .rule{height:2px;width:70px;background:var(--gold);margin:26px 0}
.cover .meta{display:flex;gap:28px;flex-wrap:wrap;margin-top:10px}
.cover .meta .box{border:1px solid rgba(255,255,255,.28);border-radius:12px;padding:14px 20px;min-width:120px}
.cover .meta .num{font-size:30px;font-weight:800;color:#f2d492;font-family:Georgia,serif}
.cover .meta .cap{font-size:11px;color:#c7cede;letter-spacing:.08em;margin-top:2px}
.cover .brand{font-size:13px;letter-spacing:.35em;color:#aeb8cf;font-weight:700}
.cover .note{font-size:11.5px;color:#aab4cc;line-height:1.8}

/* ---------- SECTION ---------- */
.sec-head{display:flex;align-items:baseline;justify-content:space-between;
  border-bottom:2px solid var(--navy);padding-bottom:7px;margin:0 0 12px}
.sec-head .l{display:flex;align-items:baseline;gap:12px}
.sec-head .sn{font-family:Georgia,serif;font-size:13px;font-weight:700;color:#fff;background:var(--navy);
  border-radius:20px;padding:3px 12px;letter-spacing:.06em}
.sec-head .tt{font-size:16px;font-weight:800;color:var(--navy)}
.sec-head .rg{font-family:Georgia,serif;font-size:12px;color:var(--sub)}
.legend{font-size:10.5px;color:var(--sub);margin:-6px 0 12px}
.legend .st{color:var(--gold-d);letter-spacing:1px}

.grid{column-count:2;column-gap:8mm}
.item{break-inside:avoid;display:grid;grid-template-columns:13px 24px 1fr;gap:0 7px;
  padding:3.2px 5px 3.2px 3px;border-bottom:1px solid var(--line);align-items:start}
.item:nth-child(odd){background:var(--tint)}
.chk{width:10px;height:10px;border:1.3px solid #9aa1b0;border-radius:3px;margin-top:3px}
.no{font-family:Georgia,serif;font-size:10px;color:#a7adba;text-align:right;padding-top:2px}
.main{min-width:0}
.wline{display:flex;align-items:baseline;gap:6px;flex-wrap:wrap}
.w{font-family:Georgia,serif;font-size:12.8px;font-weight:700;color:var(--ink);letter-spacing:.01em;line-height:1.25}
.st{font-size:9px;color:var(--gold);letter-spacing:.5px}
.m{font-size:11px;color:var(--sub);line-height:1.35;margin-top:0}

.foot{position:absolute;left:14mm;right:14mm;bottom:7mm;display:flex;justify-content:space-between;
  font-size:10px;color:#b3b8c2;border-top:1px solid var(--line);padding-top:5px}
.foot .b{letter-spacing:.28em;font-weight:700;color:#9aa1b0}
@page{size:A4;margin:0}
"""

def stars_html(n):
    k = stars(n)
    return '<span class="st">' + "★"*k + "☆"*(3-k) + "</span>"

def item_html(r):
    no, w, m, cnt = r[0], r[1], r[2], r[3]
    return (f'<div class="item"><div class="chk"></div>'
            f'<div class="no">{esc(no)}</div>'
            f'<div class="main"><div class="wline"><span class="w en">{esc(w)}</span>{stars_html(cnt)}</div>'
            f'<div class="m">{esc(m)}</div></div></div>')

# cover
cover = f'''<div class="page cover">
  <div>
    <div class="kicker">THINKING &nbsp;/&nbsp; Special Bonus</div>
    <h1>この夏の必修<br><span class="accent">英熟語 200</span></h1>
    <div class="rule"></div>
    <div class="lead">ターゲット英熟語1000・速読英熟語・英検（準1級／2級／準2級）——
    主要熟語帳を横断し、<b style="color:#fff">「どの単語帳にも共通して載っている＝入試・英検で必ず問われる」</b>
    最重要の英熟語だけを頻度で厳選しました。単語と合わせて、この200熟語を。</div>
  </div>
  <div>
    <div class="meta">
      <div class="box"><div class="num">200</div><div class="cap"> IDIOMS 厳選</div></div>
      <div class="box"><div class="num">5</div><div class="cap">熟語帳を横断</div></div>
      <div class="box"><div class="num">★★★</div><div class="cap">重要度つき</div></div>
    </div>
  </div>
  <div>
    <div class="note">★の数＝掲載熟語帳の多さ（重要度）。★★★＝5冊すべてに掲載。<br>
    □にチェックしながら、覚えた熟語を消していこう。</div>
    <div style="height:16px"></div>
    <div class="brand">THINKING &nbsp;·&nbsp; thinking-online.com</div>
  </div>
</div>'''

SEC = 50
pages = [cover]
total = len(rows)
for si, start in enumerate(range(0, total, SEC), 1):
    chunk = rows[start:start+SEC]
    lo, hi = chunk[0][0], chunk[-1][0]
    items = "".join(item_html(r) for r in chunk)
    pages.append(f'''<div class="page">
  <div class="sec-head"><div class="l"><span class="sn">SECTION {si:02d}</span>
    <span class="tt">必修英熟語 200</span></div>
    <span class="rg">No.{int(lo):03d} – {int(hi):03d}</span></div>
  <div class="legend">重要度 <span class="st">★★★</span>=5冊掲載 / <span class="st">★★☆</span>=4冊 / <span class="st">★☆☆</span>=3冊　　□にチェックして暗記</div>
  <div class="grid">{items}</div>
  <div class="foot"><span class="b">THINKING</span><span>この夏の必修英熟語200 &nbsp;—&nbsp; {si} / {(total+SEC-1)//SEC}</span></div>
</div>''')

doc = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>この夏の必修 英熟語200</title><style>{CSS}</style></head>
<body>{''.join(pages)}</body></html>'''
open(OUT, "w", encoding="utf-8").write(doc)
print("wrote", OUT, "pages:", len(pages))
