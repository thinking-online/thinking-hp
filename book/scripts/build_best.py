# -*- coding: utf-8 -*-
# こちらの見立て（3つの方向を、置き場所で分けて全部使う案）を、1枚にまとめる。
#   python3 -I scripts/build_best.py     → build/書名のまとめ案.html
#   node scripts/shot_page.js 書名のまとめ案 → PNG と PDF
import io, html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_title3 as t3
from words_v2 import PAKURU, KUCHI
from build_katachi import WORDS as YARANAI
import plan_v2 as plan

XO = {no: (x, o) for _, _, _, items in plan.CHAPTERS for no, _, _, x, o, _ in items}
H = html.escape

cover = ('<span class="cv best"><span class="hook">早慶合格・学年1位・試験一発合格！</span>'
         '<span class="ttl t1"><span class="a">頭のいい人が</span><span class="b">絶対やらない</span><span class="c">勉強法</span>'
         '<span class="st">パクるだけで伸びる、50の法則</span></span>'
         '<span class="au">朝倉 徹大（受験の王様）</span>'
         '<span class="obi">勉強時間は、<br>1分も増やしません。</span></span>')

def page1(no):
    return t3.page_yaranai(no).replace("頭のいい人が絶対にやらない", "頭のいい人が絶対やらない")

toc = "".join(
    f'<div class="ti"><div class="tl"><b>{no}</b><span>「{H(YARANAI[no])}」</span></div>'
    f'<div class="tx">×　{H(XO[no][0])}</div><div class="to">○　{H(XO[no][1])}</div></div>' for no in ["02", "05", "13"])

furoku = "".join(
    f'<div class="fr"><b>{no}</b><span class="fx">{H(YARANAI[no])}</span><i>→</i><span class="fo">{H(PAKURU[no])}</span>'
    f'<span class="fk">{H(KUCHI[no])}</span></div>' for no in ["02", "05", "13", "40"])

CSS = t3.CSS + """
.best .ttl { top:19cqw; bottom:42cqw; }
.best .t1 .a { font-size:12.4cqw; } .best .t1 .b { font-size:13.2cqw; } .best .t1 .c { font-size:24cqw; margin-top:2.4cqw; }
.best .st { font-size:5.5cqw; font-weight:700; margin-top:4cqw; letter-spacing:.02em; color:var(--paper-ink); white-space:nowrap; }
.best .au { bottom:33.5cqw; }
.best .obi { position:absolute; left:0; right:0; bottom:0; height:30cqw; background:var(--paper-ink); color:#fff; font-weight:900; font-size:8.4cqw; line-height:1.45;
             display:flex; align-items:center; justify-content:center; text-align:center; }
.lay { display:grid; grid-template-columns:minmax(0,330px) minmax(0,1fr); gap:28px; align-items:start; }
.side { display:grid; gap:20px; min-width:0; }
.blk { min-width:0; }
.blk h3 { font-size:15px; margin:0 0 2px; display:flex; gap:8px; align-items:baseline; flex-wrap:wrap; }
.blk h3 em { font-style:normal; font-size:12px; color:var(--on-accent); background:var(--accent); padding:0 8px; letter-spacing:.06em; }
.blk p { margin:0 0 8px; color:var(--muted); font-size:13.5px; }
.p3 { display:grid; grid-template-columns:repeat(3, minmax(0,150px)); gap:10px; }
.tocb, .fb { background:var(--surface); border:1px solid var(--line); padding:4px 14px; }
.ti { padding:7px 0; } .ti + .ti { border-top:1px solid var(--line); }
.ti .tl { padding:0; font-weight:700; color:var(--fg); font-size:15px; }
.tx, .to { font-size:12.5px; line-height:1.6; padding-left:27px; } .tx { color:var(--muted); } .to { color:var(--accent); }
.fr { display:grid; grid-template-columns:28px minmax(0,1fr) 18px minmax(0,1fr) minmax(0,1.3fr); gap:0 8px; align-items:baseline; padding:7px 0; font-size:13.5px; }
.fr + .fr { border-top:1px solid var(--line); }
.fr b { color:var(--accent); font-variant-numeric:tabular-nums; } .fx { color:var(--muted); } .fr i { font-style:normal; color:var(--muted); }
.fo { font-weight:700; color:var(--accent); } .fk { color:var(--paper-say); background:var(--paper-say-soft); padding:1px 10px; border-radius:12px; font-weight:700; font-size:12.5px; justify-self:start; }
@media (max-width:760px) { .lay { grid-template-columns:minmax(0,1fr); } .lay > figure { max-width:300px; }
  .fr { grid-template-columns:28px minmax(0,1fr); } .fr i { display:none; } .fo, .fk { grid-column:2; } }
"""

doc = f"""<title>書名のまとめ案</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<style>{CSS}</style>
<div class="wrap">
<h1>3つを、置き場所で分ける</h1>
<p class="lede">やらない系は書名に。パクる系はサブタイトルと帯と付録に。二項対立は目次と本文の形に。</p>
<div class="lay" style="margin-top:22px">
  <figure>{cover}<figcaption>表紙の見本（デザインは仮）</figcaption></figure>
  <div class="side">
    <div class="blk"><h3><em>① やらない</em>書名と、各項目の1ページ目</h3><p>書名と同じ言い方が、50回くり返される。</p>
      <div class="p3">{"".join(f'<span class="pc">{page1(n)}</span>' for n in ["02", "15", "39"])}</div></div>
    <div class="blk"><h3><em>③ 二項対立</em>目次と本文</h3><p>目次は、言葉の下に×と○の2行。本文も、伸びない人と頭のいい人の対で進む。</p>
      <div class="tocb">{toc}</div></div>
    <div class="blk"><h3><em>② パクる</em>サブタイトル・帯・巻末の付録</h3><p>付録「パクったら頭がよくなった勉強法則50」。やらない → パクる ＋ 口ぐせ。</p>
      <div class="fb">{furoku}</div></div>
  </div>
</div>
<p class="foot">書名の検討用。言葉はどれも仮のものです。</p>
</div>
"""
io.open("build/書名のまとめ案.html", "w", encoding="utf-8").write(doc)
print("ok")
