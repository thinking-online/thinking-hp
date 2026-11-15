# -*- coding: utf-8 -*-
# 表紙を「サムネ」として比べる。同じ表紙を、大・中・小の3つの大きさで並べて、小さくした時に何が読めるかを見る。
#   python3 -I scripts/build_thumb.py          → build/表紙のサムネテスト.html
#   node scripts/shot_page.js 表紙のサムネテスト   → PNG と PDF
# 表紙のデザインは、言葉の置き方を比べるための仮のもの。
import io, html

H = html.escape
HOOK = "早慶合格・学年1位・試験一発合格！"
AU = "朝倉 徹大（受験の王様）"
OBI = '<span class="obi"><b>偏差値42→70</b><small>勉強時間は、1分も増やしません。</small></span>'

def cv(cls, inner, obi=OBI):
    return f'<span class="cv {cls}">{inner}<span class="au">{H(AU)}</span>{obi}</span>'

DESIGNS = [
 ("A", "前回の並べ方", "3行がほぼ同じ大きさ",
  cv("a", f'<span class="hook">{H(HOOK)}</span><span class="t"><span class="l1">頭のいい人が</span><span class="l2">絶対やらない</span><span class="l3">勉強法</span>'
          '<span class="st">パクるだけで伸びる、50の法則</span></span>',
     '<span class="obi long"><b>勉強時間は、<br>1分も増やしません。</b></span>'),
  "勉強法"),
 ("B", "大きい言葉を7字にしぼる", "「やらない勉強法」だけを最大に",
  cv("b", '<span class="pre">頭のいい人が絶対</span><span class="big"><span class="r">やらない</span><span>勉強法</span></span>'
          '<span class="st">パクるだけで伸びる、50の法則</span>'),
  "やらない勉強法"),
 ("C", "Bに、×の記号を足す", "字より先に、形が目に入る",
  cv("c", '<span class="x"></span><span class="pre">頭のいい人が絶対</span><span class="big"><span class="r">やらない</span><span>勉強法</span></span>'),
  "×と、やらない勉強法"),
 ("D", "Cを、黄色と黒にする", "棚でも、スマホの一覧でも、色で先に見つかる",
  cv("c d", '<span class="x"></span><span class="pre">頭のいい人が絶対</span><span class="big"><span class="r">やらない</span><span>勉強法</span></span>'),
  "×と、やらない勉強法"),
 ("E", "パクる系で、数字を最大に", "②の方向を、サムネ向きに組んだ場合",
  cv("e", '<span class="pre">パクったら頭が良くなった</span><span class="num">50</span><span class="big2">の勉強法</span>'),
  "50"),
 ("F", "二項対立を、上下で割る", "③の方向を、サムネ向きに組んだ場合",
  cv("f", '<span class="up">頭がいい人</span><span class="to">と</span><span class="dn">伸びない人</span>'),
  "頭がいい人／伸びない人"),
]
SIZES = [("l", "本を手に取った時"), ("m", "ネット書店の一覧くらい"), ("s", "スマホの検索結果くらい")]

head = "".join(f'<div class="hc"><b>{k}</b><span>{H(name)}</span><small>{H(note)}</small></div>' for k, name, note, _, _ in DESIGNS)
rows = ""
for sc, label in SIZES:
    cells = "".join(f'<div class="cell {sc}">{c}</div>' for _, _, _, c, _ in DESIGNS)
    rows += f'<div class="rl">{H(label)}</div><div class="row">{cells}</div>'
survive = "".join(f'<div class="sv"><b>{k}</b><span>{H(s)}</span></div>' for k, _, _, _, s in DESIGNS)

CSS = """
/* 配置の考え方：横に6つの表紙、縦に3つの大きさ。下の段ほど小さい。いちばん下の段で読めるものが、サムネで伝わる言葉 */
:root {
  --bg:#f3f5f8; --surface:#ffffff; --fg:#151a22; --muted:#5d6878; --line:#d5dbe4; --accent:#15467e; --on-accent:#fff;
  --paper:#ffffff; --ink:#111316; --red:#d6261c; --yellow:#ffd60a; --navy:#15467e; --soft:#e4e7ec; --gray:#69737f;
  --sans:"Noto Sans JP","Noto Sans CJK JP","Hiragino Sans","Yu Gothic",sans-serif;
  --serif:"Noto Serif JP","Noto Serif CJK JP","Hiragino Mincho ProN","Yu Mincho",serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#323c49; --accent:#8db8ee; --on-accent:#0f1620;
  --paper:#f2f3f5; --ink:#111316; --red:#d6261c; --yellow:#ffd60a; --navy:#15467e; --soft:#d6dae1; --gray:#5d6773; color-scheme:dark } }
:root[data-theme="dark"] {
  --bg:#12161c; --surface:#1a2029; --fg:#e8ecf2; --muted:#9aa6b6; --line:#323c49; --accent:#8db8ee; --on-accent:#0f1620;
  --paper:#f2f3f5; --ink:#111316; --red:#d6261c; --yellow:#ffd60a; --navy:#15467e; --soft:#d6dae1; --gray:#5d6773; color-scheme:dark }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.75; margin:0; }
.wrap { max-width:1120px; margin:0 auto; padding-block:26px 56px;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family:var(--serif); font-weight:900; font-size:clamp(24px,4.2vw,34px); line-height:1.35; margin:0 0 6px; text-wrap:balance; }
.lede { color:var(--muted); margin:0 0 4px; max-width:46em; }
.scroll { overflow-x:auto; padding-bottom:8px; margin-top:20px; }
.board { min-width:1040px; }
.heads, .row { display:grid; grid-template-columns:repeat(6, minmax(0,1fr)); gap:14px; }
.hc { min-width:0; border-top:3px solid var(--accent); padding-top:6px; }
.hc b { font-family:var(--serif); font-size:22px; color:var(--accent); line-height:1; margin-right:8px; }
.hc span { font-weight:700; font-size:13.5px; line-height:1.45; }
.hc small { display:block; color:var(--muted); font-size:12px; line-height:1.5; margin-top:2px; }
.rl { font-size:12.5px; font-weight:700; color:var(--muted); letter-spacing:.08em; margin:22px 0 8px; padding-top:10px; border-top:1px solid var(--line); }
.cell { min-width:0; display:flex; align-items:flex-start; }
.cell.l .cv { width:100%; } .cell.m .cv { width:96px; } .cell.s .cv { width:52px; }

/* 表紙（四六判）。大きさは cqw（表紙の幅の％）で決めるので、小さくしても同じ比率で縮む */
.cv { display:block; aspect-ratio:127/188; container-type:inline-size; position:relative; background:var(--paper); color:var(--ink); border:1px solid var(--line);
      overflow:hidden; line-height:1.15; font-weight:900; flex:none; }
.cv .au { position:absolute; left:0; right:0; bottom:27cqw; text-align:center; font-size:4.2cqw; font-weight:700; letter-spacing:.08em; }
.cv .obi { position:absolute; left:0; right:0; bottom:0; height:24cqw; background:var(--ink); color:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.cv .obi b { font-size:13cqw; letter-spacing:.01em; line-height:1.1; }
.cv .obi small { font-size:4.2cqw; font-weight:700; margin-top:1.4cqw; }
.cv .obi.long b { font-size:8cqw; line-height:1.4; }
.cv .st { display:block; font-size:5.2cqw; font-weight:700; white-space:nowrap; }
.cv .pre { position:absolute; left:8cqw; right:8cqw; font-size:8.6cqw; letter-spacing:.02em; white-space:nowrap; }
/* A */
.a .hook { position:absolute; top:0; left:0; right:0; background:var(--navy); color:#fff; font-size:5.2cqw; font-weight:700; text-align:center; padding:3cqw 1cqw; }
.a .t { position:absolute; left:8cqw; right:8cqw; top:19cqw; bottom:34cqw; display:flex; flex-direction:column; justify-content:center; }
.a .l1 { font-size:12.4cqw; } .a .l2 { font-size:13.2cqw; color:var(--navy); margin-top:3cqw; border-bottom:1.2cqw solid var(--navy); padding-bottom:1.5cqw; align-self:flex-start; }
.a .l3 { font-size:24cqw; margin-top:2.4cqw; } .a .st { margin-top:4cqw; } .a .au { bottom:27cqw; }
/* B */
.b .pre { top:11cqw; }
.b .big { position:absolute; left:7cqw; right:7cqw; top:25cqw; display:flex; flex-direction:column; }
.b .big span { font-size:28.5cqw; letter-spacing:-.01em; white-space:nowrap; }
.b .big .r { font-size:21.4cqw; color:var(--red); margin-bottom:3cqw; }
.b .st { position:absolute; left:8cqw; top:99cqw; }
/* C・D */
.c .x { position:absolute; left:50%; top:26cqw; width:0; height:0; }
.c .x::before, .c .x::after { content:""; position:absolute; left:-33cqw; top:-5cqw; width:66cqw; height:10cqw; background:var(--red); border-radius:1cqw; }
.c .x::before { transform:rotate(45deg); } .c .x::after { transform:rotate(-45deg); }
.c .pre { top:54cqw; }
.c .big { position:absolute; left:7cqw; right:7cqw; top:66cqw; display:flex; flex-direction:column; }
.c .big span { font-size:24cqw; white-space:nowrap; letter-spacing:-.01em; }
.c .big .r { font-size:21.4cqw; color:var(--red); margin-bottom:1.6cqw; }
.c .au { display:none; }
.c.d { background:var(--yellow); }
.c.d .big .r { color:var(--ink); }
/* E */
.e .pre { top:11cqw; font-size:6.9cqw; }
.e .num { position:absolute; left:6cqw; top:20cqw; font-size:62cqw; color:var(--red); line-height:1; letter-spacing:-.04em; }
.e .big2 { position:absolute; left:8cqw; top:84cqw; font-size:20.5cqw; white-space:nowrap; }
/* F */
.f .up, .f .dn { position:absolute; left:0; right:0; height:55cqw; display:flex; align-items:center; justify-content:center; font-size:15.4cqw; }
.f .up { top:0; background:var(--ink); color:#fff; } .f .dn { top:55cqw; background:var(--soft); color:var(--gray); }
.f .to { position:absolute; left:50%; top:55cqw; width:13cqw; height:13cqw; margin:-6.5cqw 0 0 -6.5cqw; border-radius:50%; background:var(--paper); border:1cqw solid var(--ink);
         font-size:7cqw; display:flex; align-items:center; justify-content:center; z-index:1; }
.f .au { bottom:27cqw; }

h2 { font-family:var(--serif); font-size:19px; margin:34px 0 4px; padding-top:16px; border-top:1px solid var(--line); }
.h2sub { color:var(--muted); font-size:14px; margin:0 0 12px; }
.svs { display:grid; grid-template-columns:repeat(auto-fit, minmax(160px,1fr)); gap:10px; }
.sv { background:var(--surface); border:1px solid var(--line); padding:9px 12px; min-width:0; }
.sv b { font-family:var(--serif); color:var(--accent); font-size:18px; margin-right:8px; }
.sv span { font-weight:700; font-size:14px; }
.foot { margin-top:26px; color:var(--muted); font-size:12.5px; }
@media print { body { font-size:11px; } .wrap { max-width:none; padding-block:0; } .scroll { overflow:visible; } .board { min-width:0; } .cell.m .cv { width:26mm; } .cell.s .cv { width:14mm; } }
"""

doc = f"""<title>表紙のサムネテスト</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<style>{CSS}</style>
<div class="wrap">
<h1>表紙のサムネテスト</h1>
<p class="lede">表紙は、一覧の中で1秒で選ばれるサムネです。同じ表紙を3つの大きさに縮めて、小さくした時に何が読めるかを比べました。</p>
<p class="lede">書名は6つのうちA〜Dが同じ（頭のいい人が絶対やらない勉強法）で、言葉の置き方だけを変えています。デザインは仮のものです。</p>
<div class="scroll"><div class="board">
  <div class="heads">{head}</div>
  {rows}
</div></div>

<h2>いちばん小さい段で、読めるもの</h2>
<p class="h2sub">ここで読める言葉だけが、サムネで伝わります。</p>
<div class="svs">{survive}</div>
<p class="foot">表紙の検討用。帯の「偏差値42→70」は、著者の経歴（現役の時は偏差値42、10ヶ月で全教科70超）からの仮の言葉です。</p>
</div>
"""
io.open("build/表紙のサムネテスト.html", "w", encoding="utf-8").write(doc)
print("ok")
