# -*- coding: utf-8 -*-
# 50項目を「やらない／パクる／口ぐせ」の3つの言い方で並べる比較ページを作る。
#   python3 -I scripts/build_hikaku3.py        → build/言葉の3つ比較_50.html
#   node scripts/shot_page.js 言葉の3つ比較_50   → PNG と PDF
# 言葉は scripts/words_v2.py（PAKURU, KUCHI）と scripts/build_katachi.py（WORDS）にある。まだ仮。
import io, html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_v2 as plan
from words_v2 import PAKURU, KUCHI, IN_BOOK
from build_katachi import WORDS as YARANAI

E = html.escape

def row(no):
    star = '<span class="star" title="本文にある口ぐせ">★</span>' if no in IN_BOOK else ''
    return (f'<div class="r"><div class="n">{no}</div>'
            f'<div class="c x"><span class="lb">やらない</span><span class="w"><i>×</i>{E(YARANAI[no])}</span></div>'
            f'<div class="c o"><span class="lb">パクる</span><span class="w"><i>○</i>{E(PAKURU[no])}</span></div>'
            f'<div class="c s"><span class="lb">口ぐせ</span><span class="bub">{E(KUCHI[no])}</span>{star}</div></div>')

rows = []
for ch_no, ch_title, ch_sub, items in plan.CHAPTERS:
    rows.append(f'<div class="ch"><span>{E(ch_no)}</span>{E(ch_sub)}</div>')
    rows += [row(no) for no, *_ in items]

CSS = """
/* 配置の考え方：1項目＝1行。左から × やらない／○ パクる／口ぐせ。列ごとに色と形を変えて、行を横に読むだけで比べられるようにする */
:root {
  --bg:#f3f5f8; --surface:#ffffff; --fg:#151a22; --muted:#5d6878; --line:#d9dee6; --band:#e7ecf3;
  --no:#15467e; --x:#59626f; --x-soft:#e9ecf0; --o:#15467e; --o-soft:#e2ebf7; --say:#0b6b5b; --say-soft:#dff2ed; --star:#b4530a;
  --sans:"Noto Sans JP","Noto Sans CJK JP","Hiragino Sans","Yu Gothic",sans-serif;
  --serif:"Noto Serif JP","Noto Serif CJK JP","Hiragino Mincho ProN","Yu Mincho",serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#2f3946; --band:#232c38;
  --no:#8db8ee; --x:#a9b3c0; --x-soft:#2a323d; --o:#9cc4f5; --o-soft:#1f3350; --say:#7fd6c3; --say-soft:#143a34; --star:#f0a65a; color-scheme:dark } }
:root[data-theme="dark"] {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#2f3946; --band:#232c38;
  --no:#8db8ee; --x:#a9b3c0; --x-soft:#2a323d; --o:#9cc4f5; --o-soft:#1f3350; --say:#7fd6c3; --say-soft:#143a34; --star:#f0a65a; color-scheme:dark }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.7; margin:0; }
body::before { content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top, 0px); z-index:10; background:var(--bg); }
.wrap { max-width:1080px; margin:0 auto; padding-block:26px 56px;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family:var(--serif); font-weight:900; font-size:clamp(24px,4.2vw,34px); line-height:1.35; margin:0 0 6px; text-wrap:balance; }
.lede { color:var(--muted); margin:0 0 18px; max-width:44em; }

/* 3つの言い方の見本（02番） */
.ex { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:12px; margin-bottom:26px; }
.exc { background:var(--surface); border:1px solid var(--line); padding:14px 16px 16px; min-width:0; }
.exc .k { font-size:12px; font-weight:700; letter-spacing:.12em; }
.exc .f { font-size:13px; color:var(--muted); margin-top:6px; line-height:1.5; }
.exc .v { font-family:var(--serif); font-weight:900; font-size:clamp(22px,3.4vw,28px); line-height:1.4; margin-top:2px; }
.exc.x .k, .exc.x .v { color:var(--x); } .exc.o .k, .exc.o .v { color:var(--o); } .exc.s .k, .exc.s .v { color:var(--say); }
.exc.x { border-top:4px solid var(--x); } .exc.o { border-top:4px solid var(--o); } .exc.s { border-top:4px solid var(--say); }

.tbl { background:var(--surface); border:1px solid var(--line); }
.th, .r { display:grid; grid-template-columns:52px minmax(0,1fr) minmax(0,1fr) minmax(0,1.25fr); gap:0 16px; align-items:center; padding:0 16px; }
.th { position:sticky; top:env(safe-area-inset-top, 0px); z-index:5; background:var(--surface); border-bottom:2px solid var(--fg); padding-block:9px; font-size:13px; font-weight:700; }
.th .hx { color:var(--x); } .th .ho { color:var(--o); } .th .hs { color:var(--say); }
.th small { display:block; font-weight:400; font-size:11.5px; color:var(--muted); line-height:1.4; }
.ch { background:var(--band); color:var(--fg); font-size:13px; font-weight:700; padding:6px 16px; letter-spacing:.04em; border-top:1px solid var(--line); }
.ch span { color:var(--no); margin-right:12px; }
.r { border-top:1px solid var(--line); padding-block:9px; }
.n { font-family:var(--serif); font-weight:900; font-size:20px; color:var(--no); font-variant-numeric:tabular-nums; line-height:1; }
.c { min-width:0; }
.lb { display:none; }
.w { font-size:17px; font-weight:700; line-height:1.45; display:inline-block; }
.w i { font-style:normal; display:inline-block; width:1.5em; font-weight:900; }
.x .w { color:var(--x); } .o .w { color:var(--o); }
.bub { display:inline-block; position:relative; background:var(--say-soft); color:var(--say); font-size:16px; font-weight:700; line-height:1.45;
       padding:5px 13px; border-radius:15px; margin-left:7px; }
.bub::before { content:""; position:absolute; left:-6px; top:50%; margin-top:-5px; border:5px solid transparent; border-left:0; border-right:7px solid var(--say-soft); }
.star { color:var(--star); font-size:12px; margin-left:6px; }
.foot { margin-top:14px; color:var(--muted); font-size:13px; }

@media (max-width:700px) {
  .th { display:none; }
  .r { grid-template-columns:40px minmax(0,1fr); gap:5px 10px; align-items:start; padding-block:11px; }
  .n { grid-row:1 / span 3; font-size:19px; padding-top:3px; }
  .c { grid-column:2; display:flex; align-items:baseline; gap:8px; flex-wrap:nowrap; }
  .c .w, .c .bub { min-width:0; } .star { flex:none; margin-left:0; }
  .lb { display:inline-block; flex:none; width:4.2em; font-size:11px; font-weight:700; letter-spacing:.04em; }
  .x .lb { color:var(--x); } .o .lb { color:var(--o); } .s .lb { color:var(--say); }
  .w { font-size:16px; } .w i { display:none; } .bub { font-size:15px; margin-left:4px; }
}
@media print {
  body { font-size:11px; } .wrap { max-width:none; padding-block:0; }
  .th { position:static; } .r, .exc { break-inside:avoid; } .ch { break-after:avoid; }
  .w { font-size:13px; } .bub { font-size:12.5px; } .n { font-size:15px; } .r { padding-block:5px; }
}
"""

doc = f"""<title>50項目の言葉くらべ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<style>{CSS}</style>
<div class="wrap">
<h1>50項目の言葉くらべ</h1>
<p class="lede">1つの項目を、3つの言い方で横に並べました。左から「やらないこと」「パクること」「その時の口ぐせ」。どの言葉も、まだ仮のものです。</p>

<div class="ex">
  <div class="exc x"><div class="k">× やらない</div><div class="f">頭のいい人が絶対にやらない</div><div class="v">「{E(YARANAI["02"])}」</div></div>
  <div class="exc o"><div class="k">○ パクる</div><div class="f">パクったら頭がよくなった</div><div class="v">「{E(PAKURU["02"])}」</div></div>
  <div class="exc s"><div class="k">口ぐせ</div><div class="f">その時、頭の中で言う一言</div><div class="v">「{E(KUCHI["02"])}」</div></div>
</div>

<div class="tbl">
  <div class="th"><div></div><div class="hx">× やらない<small>頭のいい人が絶対にやらない「　」</small></div>
    <div class="ho">○ パクる<small>パクったら頭がよくなった「　」</small></div>
    <div class="hs">口ぐせ<small>その時、頭の中で言う一言</small></div></div>
  {"".join(rows)}
</div>
<p class="foot">★は、本文の「頭の中」に、もう出てくる口ぐせ（{len(IN_BOOK)}本）。『頭のいい人が絶対にやらないこと』（仮）　言葉の検討用</p>
</div>
"""
io.open("build/言葉の3つ比較_50.html", "w", encoding="utf-8").write(doc)
print("ok", len(rows), "行")
