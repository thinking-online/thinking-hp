# -*- coding: utf-8 -*-
# step_card_v1.py の一覧を、著者のSTEPの形（色つきの札・吹き出し・王様の箱）で1ページにする。
# 出力：build/STEPの一覧_50.html（公開用。<html> などは書かない）
import io, html
H = html.escape
CSS = """
/* 並べ方：著者のSTEPの紙を、1列のカードにして50枚並べる。題は黄色のマーカー、札は3色、声は吹き出し、最後に王様の箱 */
:root {
  --bg:#f5f6f8; --surface:#ffffff; --ink:#1b2130; --muted:#5a6475; --line:#d8dde6;
  --step1:#c5312a; --step2:#6a2421; --step3:#23465f; --on-step:#ffffff;
  --marker:#ffe37a; --king:#eceff3; --chip:#e6ebf2; --chip-ink:#3b4658;
  --f-display:"Zen Maru Gothic","Hiragino Maru Gothic ProN","Yu Gothic",sans-serif;
  --f-body:"Noto Sans JP","Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#13161b; --surface:#1b1f26; --ink:#e8ebf0; --muted:#9aa4b3; --line:#313846;
  --step1:#d9544c; --step2:#9c4743; --step3:#4b82a8; --on-step:#ffffff;
  --marker:#5f5110; --king:#232832; --chip:#2a303b; --chip-ink:#c5cedb; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg:#13161b; --surface:#1b1f26; --ink:#e8ebf0; --muted:#9aa4b3; --line:#313846;
  --step1:#d9544c; --step2:#9c4743; --step3:#4b82a8; --on-step:#ffffff;
  --marker:#5f5110; --king:#232832; --chip:#2a303b; --chip-ink:#c5cedb; color-scheme: dark }
body { background:var(--bg); color:var(--ink); font-family:var(--f-body); font-size:15px; line-height:1.7; }
.wrap { max-width:760px; margin:0 auto; padding-block:28px 56px;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family:var(--f-display); font-weight:900; font-size:clamp(24px, 6vw, 34px); line-height:1.3; margin:0 0 10px; text-wrap:balance; }
.lede { color:var(--muted); margin:0 0 18px; max-width:38em; }
.legend { display:flex; flex-wrap:wrap; gap:8px 14px; margin:0 0 14px; padding:0; list-style:none; font-size:13.5px; }
.legend li { display:flex; align-items:center; gap:8px; min-width:0; }
.legend .tag { padding:2px 10px; font-size:12px; }
nav.chs { display:flex; flex-wrap:wrap; gap:6px; margin:0 0 26px; }
nav.chs a { color:var(--ink); text-decoration:none; border:1px solid var(--line); background:var(--surface); border-radius:999px; padding:3px 12px; font-size:13px; }
nav.chs a:hover, nav.chs a:focus-visible { border-color:var(--step3); outline:none; }
h2 { font-family:var(--f-display); font-weight:900; font-size:19px; margin:34px 0 12px; display:flex; flex-wrap:wrap; gap:4px 12px; align-items:baseline; }
h2 small { font-family:var(--f-body); font-weight:400; font-size:13px; color:var(--muted); }
.cards { display:grid; gap:16px; }
.card { background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:18px 18px 16px; min-width:0; }
.card header { display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 10px; margin-bottom:14px; }
.no { font-family:var(--f-display); font-weight:900; font-size:15px; color:var(--muted); font-variant-numeric:tabular-nums; }
.ttl { font-family:var(--f-display); font-weight:900; font-size:19px; line-height:1.45; margin:0;
  background:linear-gradient(transparent 58%, var(--marker) 58%); padding:0 4px; }
.chip { font-size:11.5px; background:var(--chip); color:var(--chip-ink); border-radius:999px; padding:1px 9px; }
ol.steps { list-style:none; margin:0; padding:0; display:grid; gap:12px; }
ol.steps li { display:grid; grid-template-columns:78px minmax(0,1fr); gap:12px; align-items:start; }
.tag { color:var(--on-step); border-radius:9px; text-align:center; font-family:var(--f-display); font-weight:900; line-height:1.25; padding:7px 4px 8px; }
.tag b { display:block; font-size:10.5px; letter-spacing:.08em; font-weight:700; opacity:.92; }
.tag span { display:block; font-size:15px; }
.s1 { background:var(--step1); } .s2 { background:var(--step2); } .s3 { background:var(--step3); }
.do { font-weight:700; font-size:15.5px; line-height:1.55; margin:1px 0 6px; }
.say { position:relative; display:inline-block; max-width:100%; font-family:var(--f-display); font-weight:700; font-size:14px; line-height:1.5;
  border:1.5px solid var(--line); border-radius:11px; padding:4px 12px; margin-left:8px; background:var(--bg); }
.say::before { content:""; position:absolute; left:-7px; top:11px; width:10px; height:10px; background:var(--bg);
  border-left:1.5px solid var(--line); border-bottom:1.5px solid var(--line); transform:rotate(45deg); }
.king { display:grid; grid-template-columns:auto minmax(0,1fr); gap:12px; align-items:center; margin-top:14px; background:var(--king); border-radius:11px; padding:10px 14px; }
.king i { font-style:normal; font-family:var(--f-display); font-weight:900; font-size:12px; border:1.5px solid var(--ink); border-radius:999px; padding:1px 10px; white-space:nowrap; }
.king p { margin:0; font-family:var(--f-display); font-weight:700; font-size:15px; line-height:1.55; }
.foot { color:var(--muted); font-size:13px; margin-top:34px; }
@media (max-width:460px) { ol.steps li { grid-template-columns:64px minmax(0,1fr); gap:10px; } .tag span { font-size:13.5px; } .card { padding:16px 14px 14px; } }
"""
def build(S, REDO, ROLE, CH):
    out = ['<title>今日からできる3STEP 一覧</title>', '<meta name="claude:viewport-fit-sides" content="cover">',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Zen+Maru+Gothic:wght@700;900&display=swap">',
           '<style>' + CSS + '</style>', '<div class="wrap">',
           '<h1>今日からできる3STEP　50項目の一覧</h1>',
           '<p class="lede">50項目とも、同じ形です。見出しが「やること」、吹き出しが「その時の声」、一番下が王様の「ここまでできたらOK」。言葉はどれも案です。</p>',
           '<ul class="legend">'
           '<li><span class="tag s1">STEP 1 やめる</span>×ができなくなる、最初の動作</li>'
           '<li><span class="tag s2">STEP 2 やる</span>かわりにやること</li>'
           '<li><span class="tag s3">STEP 3 もう一度</span>いつ、何を、もう一度やるか</li>'
           '<li><span class="chip">作り直し</span>3つの役目に合わせて、今回作り直した15項目</li></ul>',
           '<nav class="chs" aria-label="章">' + "".join(f'<a href="#ch{i+1}">{H(c[0])}</a>' for i, c in enumerate(CH)) + '</nav>']
    for i, (cno, tag, a, b) in enumerate(CH):
        out.append(f'<section id="ch{i+1}"><h2>{H(cno)}<small>{H(tag)}</small></h2><div class="cards">')
        for k in range(a, b + 1):
            n = "%02d" % k
            t, steps, king = S[n]
            chip = '<span class="chip">作り直し</span>' if n in REDO else ''
            li = "".join(f'<li><div class="tag s{j+1}"><b>STEP {j+1}</b><span>{H(ROLE[j])}</span></div>'
                         f'<div><p class="do">{H(h)}</p><span class="say">「{H(v)}」</span></div></li>' for j, (h, v) in enumerate(steps))
            out.append(f'<article class="card"><header><span class="no">{n}</span><h3 class="ttl">頭のいい人の、{H(t)}</h3>{chip}</header>'
                       f'<ol class="steps">{li}</ol><div class="king"><i>王様</i><p>{H(king)}</p></div></article>')
        out.append('</div></section>')
    out.append('<p class="foot">原稿の検討用。もとは、今の原稿の各項目の「やり方」です。</p></div>')
    io.open("build/STEPの一覧_50.html", "w", encoding="utf-8").write("\n".join(out))
    print("ok", len(S))


def build2(S, CH, NOTE, SRC, over):
    """最新版（step_card_v2.py）。札は STEP 01・02・03 だけ。題は『』、下は「できた」の基準。"""
    css2 = CSS + """
.tag span { font-size:17px; font-variant-numeric:tabular-nums; }
.note { display:block; color:var(--muted); font-size:12.5px; line-height:1.6; margin-top:6px; }
.chip.warn { background:var(--marker); color:var(--ink); }
.king i { letter-spacing:.02em; }
.keys { margin:0 0 14px; padding:0; list-style:none; font-size:13.5px; color:var(--muted); display:grid; gap:2px; }
.keys b { color:var(--ink); font-weight:700; }
"""
    out = ['<title>今日からできる3STEP 一覧</title>', '<meta name="claude:viewport-fit-sides" content="cover">',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Zen+Maru+Gothic:wght@700;900&display=swap">',
           '<style>' + css2 + '</style>', '<div class="wrap">',
           '<h1>今日からできる3STEP　50項目の一覧</h1>',
           '<p class="lede">2026年11月17日の最新版です。50項目とも、同じ形で並べています。</p>',
           '<ul class="keys">'
           '<li><b>太い字</b>：やること</li>'
           '<li><b>吹き出し</b>：その時の声</li>'
           '<li><b>「できた」の基準</b>：ここまでできたらOK、の線</li>'
           '<li><span class="chip">著者の言葉</span> 01〜03番は、著者の原稿の言葉のままです　'
           '<span class="chip warn">枠より長い</span> ひな形の枠（見出し24字、声14字）を超える行がある項目です</li></ul>',
           '<nav class="chs" aria-label="章">' + "".join(f'<a href="#ch{i+1}">{H(c[0])}</a>' for i, c in enumerate(CH)) + '</nav>']
    for i, (cno, tag, a, b) in enumerate(CH):
        out.append(f'<section id="ch{i+1}"><h2>{H(cno)}<small>{H(tag)}</small></h2><div class="cards">')
        for k in range(a, b + 1):
            kk = "%02d" % k
            t, steps, king = S[kk]
            chips = ('<span class="chip">著者の言葉</span>' if kk in SRC else '') + ('<span class="chip warn">枠より長い</span>' if over(kk) else '')
            li = ""
            for j, (h, v) in enumerate(steps):
                note = f'<small class="note">※{H(NOTE[(kk, j+1)])}</small>' if (kk, j + 1) in NOTE else ''
                li += (f'<li><div class="tag s{j+1}"><b>STEP</b><span>0{j+1}</span></div>'
                       f'<div><p class="do">{H(h)}</p><span class="say">「{H(v)}」</span>{note}</div></li>')
            out.append(f'<article class="card"><header><span class="no">{kk}</span><h3 class="ttl">頭のいい人の『{H(t)}』3STEP</h3>{chips}</header>'
                       f'<ol class="steps">{li}</ol><div class="king"><i>「できた」の基準</i><p>{H(king)}</p></div></article>')
        out.append('</div></section>')
    out.append('<p class="foot">原稿の検討用。01〜03番は著者の原稿、04〜06番は確定版、07〜50番は本文の「やり方」の3つを短くしたものです。</p></div>')
    io.open("build/STEPの一覧_50.html", "w", encoding="utf-8").write("\n".join(out))
    print("ok", len(S))
