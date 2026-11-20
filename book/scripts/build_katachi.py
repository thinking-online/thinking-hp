# -*- coding: utf-8 -*-
# 項目タイトルの「型」を2つ並べて比べるページを作る（編集者に見せる用）。
#   python3 -I scripts/build_katachi.py   → build/タイトルの型_2案.html
#   node scripts/shot_katachi.js          → PNG と PDF
# 型1＝頭のいい人が絶対にやらない「◯◯」　型2＝頭のいい人は「◯◯」をやらない
# 入れる言葉（WORDS）は仮のもの。著者が決めたら、ここを直す。
import io, html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import words46 as W46
# 2026-11-20：今の46項目に合わせた。入れる言葉は scripts/words46.py（今の原稿の「しない」の言葉）
WORDS = W46.YARANAI
MARU = W46.MARU
ITEMS = W46.ITEMS      # no -> (章の番号, 章の札, ×, ○)
N = W46.N
E = html.escape

def ksize(w):
    n = len(w)
    return 17 if n <= 5 else 13 if n <= 7 else 10.5 if n <= 9 else 8.6

def page(kind, no, w):
    k = ksize(w)
    kw = f'<div class="kw" style="font-size:{k}cqw">「{E(w)}」</div>'
    if kind == 1:
        body = f'<div class="decl"><div class="lead">頭のいい人が絶対にやらない</div>{kw}</div>'
    else:
        pad = max(0, (len(w) + 2) * k * 1.0 - 7 * 6.2 - 2)
        body = (f'<div class="decl"><div class="lead l2">頭のいい人は、</div>{kw}'
                f'<div class="tail" style="padding-top:{pad:.1f}cqw">を、しない。</div></div>')
    return (f'<div class="pg"><div class="no"><span>法則</span><b>{no}</b></div>{body}'
            f'<div class="then"><i></i>じゃあ、何をする？</div></div>')

SAMPLES = [("02", "名詞がそのまま入る言葉"), ("07", "「する」と続けにくい言葉"), ("22", "動きの言葉を入れる場合")]

def sample_row(kind):
    cells = "".join(f'<figure>{page(kind, no, WORDS[no])}<figcaption>{E(cap)}</figcaption></figure>' for no, cap in SAMPLES)
    return f'<div class="row">{cells}</div>'

def toc(kind):
    out = []
    if kind == 1:
        out.append('<div class="tochead">頭のいい人が絶対にやらない</div>')
    for no in ["07", "08", "09", "10"]:
        _, _, x, o = ITEMS[no]
        w = E(WORDS[no])
        line = f'「{w}」' if kind == 1 else f'<span class="fx">頭のいい人は</span>「{w}」<span class="fx">をしない</span>'
        out.append(f'<div class="ti"><div class="tl"><b>{no}</b><span>{line}</span></div>'
                   f'<div class="tx">×　{E(x)}</div><div class="to">○　{E(o)}</div></div>')
    return "".join(out)

def table():
    rows, cur = [], None
    for no in sorted(WORDS):
        ch_no, ch_sub, _, _ = ITEMS[no]
        if ch_no != cur:
            cur = ch_no
            rows.append(f'<div class="chrow">{E(ch_no)}　{E(ch_sub)}</div>')
        w = E(WORDS[no])
        rows.append(f'<div class="r"><div class="n">{no}</div>'
                    f'<div class="c c1"><span class="fx">頭のいい人が絶対にやらない</span><b>「{w}」</b></div>'
                    f'<div class="c c2"><span class="fx">頭のいい人は</span><b>「{w}」</b><span class="fx">をしない</span><br><span class="fx">頭のいい人は</span><b>「{E(MARU[no])}」</b><span class="fx">をする</span></div></div>')
    return "".join(rows)

CSS = """
/* 配置の考え方：上から「2つの型」→「1ページ目」→「目次」→「50本の一覧」。同じ言葉を同じ並びで見せて、型だけを比べる */
:root {
  --bg:#f3f5f8; --surface:#ffffff; --fg:#151a22; --muted:#5d6878; --line:#d5dbe4;
  --accent:#15467e; --accent-soft:#e4ecf6; --warn:#b4530a; --warn-soft:#fbeedd;
  --paper:#ffffff; --paper-ink:#14171c; --paper-accent:#15467e; --paper-muted:#7c8794;
  --sans:"Noto Sans JP","Noto Sans CJK JP","Hiragino Sans","Yu Gothic",sans-serif;
  --serif:"Noto Serif JP","Noto Serif CJK JP","Hiragino Mincho ProN","Yu Mincho",serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#12161c; --surface:#1b212a; --fg:#e8ecf2; --muted:#9aa6b6; --line:#333d4a;
  --accent:#8db8ee; --accent-soft:#22324a; --warn:#f0a65a; --warn-soft:#3a2a18;
  --paper:#eceef2; --paper-ink:#14171c; --paper-accent:#15467e; --paper-muted:#6d7886; color-scheme:dark } }
:root[data-theme="dark"] {
  --bg:#12161c; --surface:#1b212a; --fg:#e8ecf2; --muted:#9aa6b6; --line:#333d4a;
  --accent:#8db8ee; --accent-soft:#22324a; --warn:#f0a65a; --warn-soft:#3a2a18;
  --paper:#eceef2; --paper-ink:#14171c; --paper-accent:#15467e; --paper-muted:#6d7886; color-scheme:dark }
* { box-sizing:border-box; }
body { background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.8; margin:0; }
.wrap { max-width:1040px; margin:0 auto; padding-block:28px 56px;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family:var(--serif); font-weight:900; font-size:clamp(24px,4.2vw,34px); line-height:1.35; margin:0 0 8px; text-wrap:balance; }
.lede { color:var(--muted); margin:0 0 22px; max-width:44em; }
h2 { font-family:var(--serif); font-weight:700; font-size:20px; line-height:1.5; margin:44px 0 6px; padding-top:18px; border-top:1px solid var(--line); text-wrap:balance; }
.h2sub { color:var(--muted); margin:0 0 16px; font-size:14px; max-width:46em; }
.types { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; }
.type { background:var(--surface); border:1px solid var(--line); padding:16px 18px; min-width:0; }
.badge { display:inline-block; font-size:12px; font-weight:700; letter-spacing:.14em; color:var(--surface); background:var(--accent); padding:1px 10px; }
.type .frame { font-family:var(--serif); font-weight:700; font-size:clamp(17px,2.6vw,21px); line-height:1.6; margin:8px 0 4px; }
.type .frame em { font-style:normal; color:var(--accent); }
.type p { margin:0; color:var(--muted); font-size:14px; }

.pair { display:grid; gap:22px; }
.block { min-width:0; }
.blockhead { display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; margin-bottom:8px; }
.blockhead .nm { font-family:var(--serif); font-weight:700; font-size:16px; }
.rowwrap { overflow-x:auto; padding-bottom:6px; }
.row { display:grid; grid-template-columns:repeat(3, minmax(172px, 1fr)); gap:14px; min-width:560px; }
figure { margin:0; min-width:0; }
figcaption { font-size:12.5px; color:var(--muted); margin-top:6px; line-height:1.5; }

/* 本の1ページ目（四六判 127×188mm）。大きさは cqw（ページの幅の％）で決める */
.pg { aspect-ratio:127/188; max-width:100%; container-type:inline-size; position:relative; background:var(--paper); color:var(--paper-ink);
      border:1px solid var(--line); overflow:hidden; font-family:var(--sans); }
.pg .no { position:absolute; top:9cqw; right:9cqw; text-align:center; color:var(--paper-accent); line-height:1; }
.pg .no span { display:block; font-size:3.4cqw; letter-spacing:.3em; padding-left:.3em; margin-bottom:1.2cqw; }
.pg .no b { display:block; font-size:12cqw; font-weight:900; border-top:.9cqw solid var(--paper-accent); padding-top:1.4cqw; }
.pg .decl { position:absolute; top:12cqw; right:27cqw; height:128cqw; writing-mode:vertical-rl; }
.pg .lead { font-size:5.5cqw; font-weight:700; letter-spacing:.06em; margin-left:3cqw; color:var(--paper-ink); }
.pg .lead.l2 { font-size:6.2cqw; }
.pg .kw { font-weight:900; line-height:1.2; letter-spacing:.03em; }
.pg .tail { font-size:6.2cqw; font-weight:700; margin-right:3cqw; }
.pg .then { position:absolute; left:9cqw; bottom:10cqw; writing-mode:vertical-rl; font-size:6cqw; font-weight:700; color:var(--paper-accent); letter-spacing:.06em; }
.pg .then i { display:inline-block; width:.6cqw; height:12cqw; background:var(--paper-accent); margin-bottom:2.4cqw; }

.cols { display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:16px; }
.toc { background:var(--surface); border:1px solid var(--line); padding:14px 16px 16px; min-width:0; }
.tochead { font-family:var(--serif); font-weight:700; color:var(--accent); font-size:15px; margin:6px 0 2px; }
.ti { padding:8px 0; border-top:1px solid var(--line); }
.ti:first-of-type { border-top:0; }
.tl { display:flex; gap:10px; align-items:baseline; font-weight:700; font-size:15px; line-height:1.6; }
.tl b { color:var(--accent); font-size:13px; font-variant-numeric:tabular-nums; flex:none; }
.fx { color:var(--muted); font-weight:400; }
.tx, .to { font-size:12.5px; line-height:1.65; padding-left:27px; }
.tx { color:var(--muted); } .to { color:var(--accent); }

.legend { font-size:13.5px; color:var(--muted); margin:0 0 10px; }
.rough { display:inline-block; margin-left:8px; font-size:11px; font-weight:700; color:var(--warn); background:var(--warn-soft); padding:0 6px; line-height:1.6; }
.list { background:var(--surface); border:1px solid var(--line); }
.listhead, .r { display:grid; grid-template-columns:44px minmax(0,1fr) minmax(0,1fr); gap:0 14px; padding:7px 14px; align-items:baseline; }
.listhead { font-size:12.5px; font-weight:700; color:var(--accent); border-bottom:2px solid var(--accent); }
.r { border-top:1px solid var(--line); font-size:14px; line-height:1.65; }
.r .n { color:var(--accent); font-weight:700; font-variant-numeric:tabular-nums; }
.r .c b { font-weight:700; }
.chrow { padding:6px 14px; background:var(--accent-soft); color:var(--accent); font-size:12.5px; font-weight:700; letter-spacing:.06em; border-top:1px solid var(--line); }
.pts { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; }
.pt { border-left:3px solid var(--accent); padding:2px 0 2px 14px; min-width:0; }
.pt b { display:block; font-size:15px; }
.pt span { color:var(--muted); font-size:14px; }
.foot { margin-top:36px; color:var(--muted); font-size:12.5px; }
@media (max-width:640px) {
  .listhead { display:none; }
  .r { grid-template-columns:36px minmax(0,1fr); }
  .r .c2 { grid-column:2; }
  .r .c1::before { content:"型1　"; color:var(--accent); font-size:11px; font-weight:700; }
  .r .c2::before { content:"型2　"; color:var(--accent); font-size:11px; font-weight:700; }
}
@media print {
  body { font-size:11.5px; } .wrap { max-width:none; padding-block:0; }
  h2 { break-after:avoid; } .block, .toc, .type, .ti { break-inside:avoid; } .r { break-inside:avoid; }
  .row { min-width:0; } .rowwrap { overflow:visible; }
}
"""

doc = f"""<title>項目タイトルの型くらべ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<style>{CSS}</style>
<div class="wrap">
<h1>項目タイトルの型　2案</h1>
<p class="lede">{N}項目それぞれの1ページ目と目次に出す言い方を、どちらの型にするかを比べるためのページです。同じ言葉を、同じ並びで、2つの型に入れました。今の原稿は、型2で書いています。</p>

<div class="types">
  <div class="type"><span class="badge">型1</span><div class="frame">頭のいい人が絶対にやらない<em>「◯◯」</em></div>
    <p>名詞で終わる形。書名『頭のいい人が絶対にやらないこと』の「こと」が、項目ごとに入れかわります。</p></div>
  <div class="type"><span class="badge">型2</span><div class="frame">頭のいい人は<em>「◯◯」</em>をしない</div>
    <p>文で言い切る形。今の原稿は、この形です。すぐ下に、「頭のいい人は「△△」をする」の行が続きます。</p></div>
</div>

<h2>1ページ目の見え方</h2>
<p class="h2sub">各項目の最初のページ（四六判・縦書き）に、大きく置いた場合。言葉の種類がちがう3つで並べました。</p>
<div class="pair">
  <div class="block"><div class="blockhead"><span class="badge">型1</span><span class="nm">頭のいい人が絶対にやらない「◯◯」</span></div><div class="rowwrap">{sample_row(1)}</div></div>
  <div class="block"><div class="blockhead"><span class="badge">型2</span><span class="nm">頭のいい人は「◯◯」をしない</span></div><div class="rowwrap">{sample_row(2)}</div></div>
</div>

<h2>目次での見え方</h2>
<p class="h2sub">第2章の4項目を、×と○の2行つきで並べた場合。</p>
<div class="cols">
  <div class="toc"><span class="badge">型1</span>{toc(1)}</div>
  <div class="toc"><span class="badge">型2</span>{toc(2)}</div>
</div>

<h2>{N}項目を、2つの型で読む</h2>
<p class="legend">型2の2行目（「〜をする」）は、今の原稿に入っている言葉です。第1章、07・08番、第7章の言葉は、まだ仮のものです。</p>
<div class="list"><div class="listhead"><div></div><div>型1</div><div>型2</div></div>{table()}</div>

<h2>比べる時の見どころ</h2>
<div class="pts">
  <div class="pt"><b>言葉のつながり</b><span>型1は、名詞でもセリフでも入る。型2は、動きの言葉（「〜する」）がそのまま入り、「する」の行と対になる。</span></div>
  <div class="pt"><b>書名との関係</b><span>型1は、書名と同じ形のくり返しになる。型2は、文で言い切るぶん、1つ1つが強く聞こえる。</span></div>
  <div class="pt"><b>目次の読みやすさ</b><span>型1は、見出しを1回出せば、あとは言葉だけを並べられる。型2は、「しない → する」を1行で並べられる（今の目次は、この形）。</span></div>
</div>
<p class="foot">『頭のいい人が絶対にやらないこと』（仮）　項目タイトルの検討用</p>
</div>
"""
io.open("build/タイトルの型_2案.html", "w", encoding="utf-8").write(doc)
print("ok", N, "項目")
