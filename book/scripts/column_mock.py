# -*- coding: utf-8 -*-
# コラムのページの見せ方の案（イメージ画像）。2026-11-27、著者「コラムを、最高に表示していけるような感じにしたい。その時のイメージ画像を作ってほしい」
#   python3 -I scripts/column_mock.py 出す先のフォルダ   → column_mock.html と、案ごとのPNG
# 色と書体は、著者が作った巻頭ページ（assets/巻頭_参考イメージ/）に合わせた。王様の絵も、そのPDFから取り出して使う（見本用）。
# 文は、今あるコラムの文（manuscript/本文/）を、そのまま流している。
import base64, html, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PDF = os.path.join(ROOT, "assets", "巻頭_参考イメージ", "巻頭ページ_参考イメージ_20261126.pdf")
NAVY, TINT = "#17467f", "#e9f0f8"
FW = str.maketrans("0123456789", "０１２３４５６７８９")


def kings():
    """巻頭のPDFから、王様の絵を取り出す。{番号: data URI}"""
    d = tempfile.mkdtemp()
    subprocess.check_call(["pdfimages", "-png", PDF, os.path.join(d, "k")])
    out = {}
    for n in (1, 13, 14):
        with open(os.path.join(d, "k-%03d.png" % n), "rb") as f:
            out[n] = "data:image/png;base64," + base64.b64encode(f.read()).decode()
    return out


# 題を2行にする所（見本用。文字は、原稿のまま）
BREAK = {"col_でもだって": "「でも」「だって」のあとに、／一言だけ足す", "col_ch4_1": "「〜しちゃう」じゃない。／自分で、選んでいる"}


def tate(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"(?<!\d)(\d{2})(?!\d)", r'<span class="tcy">\1</span>', t)
    t = re.sub(r"(?<![\d>])(\d)(?![\d<])", lambda m: m.group(1).translate(FW), t)
    return re.sub(r"==(.+?)==", r'<em>\1</em>', t).replace("／", "<br>")


def column(ver, fn):
    """コラムの文を読む。(題, [(種類, 文)])　種類：p＝ふつうの段落、q＝字下げの行（せりふ・箇条）、h＝印（==）だけの行"""
    L = open(os.path.join(ROOT, "manuscript", "本文", ver, fn + ".md"), encoding="utf-8").read().split("\n")
    title = BREAK.get(fn) or re.sub(r"^#\s*コラム[\s　]*", "", L[0]).strip()
    out, key = [], ""
    for s in L[1:]:
        if not s.strip() or s.strip().startswith("```"):
            continue
        m = re.search(r"==(.+?)==", s)
        if m and not key:
            key = m.group(1)
        if s.startswith("　　"):
            t = s.strip()
            out.append(("h" if re.fullmatch(r"==.+==", t) else "q", t))
        else:
            out.append(("p", s.strip()))
    return title, out, key


def body(paras):
    return "".join('<p class="%s">%s</p>' % (k, tate(t)) for k, t in paras)


CROWN = '<svg class="crown" viewBox="0 0 40 30" aria-hidden="true"><path d="M5 25 L3 9 L13 17 L20 5 L27 17 L37 9 L35 25 Z"/><circle cx="3" cy="7" r="3"/><circle cx="20" cy="3.5" r="3"/><circle cx="37" cy="7" r="3"/></svg>'

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#d9dde4;font-family:"Noto Sans CJK JP",sans-serif;color:#16181d}
.sheet{width:1180px;padding:34px 40px 40px;background:#d9dde4}
.cap{display:flex;align-items:baseline;gap:16px;margin:0 0 6px}
.cap b{font-size:25px;color:%(navy)s}.cap span{font-size:15px;font-weight:700}
.sub{font-size:13.5px;line-height:1.75;color:#30343c;margin:0 0 18px;max-width:1040px}
.sp{display:flex;flex-direction:row-reverse;justify-content:center;filter:drop-shadow(0 8px 18px rgba(20,30,50,.22))}
.pg{position:relative;width:508px;height:752px;background:#fff;overflow:hidden}
.pg+.pg{box-shadow:inset -14px 0 18px -14px rgba(0,0,0,.18)}
.pg:first-child{box-shadow:inset 14px 0 18px -14px rgba(0,0,0,.18)}
.no{position:absolute;bottom:20px;font-size:10px;color:%(navy)s;font-weight:700}
.no.l{left:26px}.no.r{right:26px}
.tcy{text-combine-upright:all}
.crown{width:1.5em;height:1.1em;fill:currentColor;vertical-align:-.1em}
/* ふつうのページ（となりに置いて、ちがいを見せる） */
.plain .bars{position:absolute;inset:64px 50px 70px;display:flex;flex-direction:row-reverse;gap:14.5px}
.plain .bars i{display:block;width:11px;border-radius:2px;background:#e6e8ec}
.plain .tag{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);background:#fff;border:1px solid #c9ced8;border-radius:99px;padding:5px 16px;font-size:12px;color:#5b606b;white-space:nowrap}
/* コラムの本文（縦書き・2段組） */
.tx{position:absolute;writing-mode:vertical-rl;column-count:2;column-fill:balance;font-family:"Noto Serif CJK JP","IPAexMincho",serif;font-size:12.6px;line-height:1.86;text-align:justify}
.tx p{margin:0;margin-block-end:.42em;break-inside:avoid-column}
.tx p.q{font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;color:%(navy)s;padding-inline-start:1em;font-size:12.2px;margin-block-end:.1em;text-align:start}
.tx p.q+p.p,.tx p.h+p.p{margin-block-start:.4em}
.tx p.h{font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;color:%(navy)s;font-size:14px;padding-inline-start:1em;margin-block:.5em .6em}
.tx em{font-style:normal;font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;color:%(navy)s;background:linear-gradient(to left,transparent 0 6%%,rgba(23,70,127,.15) 6%% 94%%,transparent 94%%)}
.ttl{position:absolute;writing-mode:vertical-rl;font-weight:700;color:%(navy)s;letter-spacing:.05em;line-height:1.45}
.pill{display:inline-flex;align-items:center;gap:7px;font-size:10.5px;font-weight:700;letter-spacing:.2em;border-radius:99px;padding:5px 15px 5px 13px;white-space:nowrap}
.pill b{font-size:15px;letter-spacing:.04em}
.kc{position:absolute;border-radius:50%%;background:#fff;overflow:hidden;display:flex;align-items:center;justify-content:center}
.kc img{width:86%%;height:86%%;object-fit:contain}
/* 案A */
.a{background:%(tint)s}
.a .head{position:absolute;top:30px;left:44px;right:44px;height:26px;display:flex;justify-content:center;align-items:center}
.a .head::before{content:"";position:absolute;left:0;right:0;top:50%%;border-top:1.5px solid %(navy)s;opacity:.35}
.a .pill{position:relative;background:%(navy)s;color:#fff}
.a .ttl{top:84px;right:40px;height:480px;font-size:25px}
.a .tx{top:84px;left:46px;width:328px;height:480px;column-gap:26px}
.a .say{position:absolute;left:36px;right:36px;bottom:46px;height:100px;background:#fff;border-radius:16px;padding:17px 16px 12px 124px}
.a .say::before{content:"";position:absolute;left:112px;top:42px;border:9px solid transparent;border-right-color:#fff;transform:translateX(-100%%)}
.a .say small{display:block;font-size:10.5px;font-weight:700;color:%(navy)s;letter-spacing:.14em;margin:0 0 5px}
.a .say p{margin:0;font-size:13.2px;line-height:1.65;font-weight:700;color:#16181d;white-space:nowrap}
.a .kc{left:24px;bottom:38px;width:116px;height:116px;border:3px solid %(navy)s}
/* 案B */
.b .band{position:absolute;top:0;bottom:0;right:0;width:74px;background:%(navy)s;color:#fff}
.b .band .lab{position:absolute;top:30px;left:0;right:0;text-align:center;font-size:9.5px;font-weight:700;letter-spacing:.22em;line-height:1.5}
.b .band .lab .crown{display:block;margin:0 auto 5px;width:22px;height:17px}
.b .band .lab b{display:block;font-size:25px;letter-spacing:.02em;line-height:1.15;margin-top:2px}
.b .ttl{top:128px;right:9px;height:470px;font-size:19.5px;color:#fff;line-height:1.45}
.b .tx{top:64px;left:44px;width:356px;height:500px;column-gap:30px;column-rule:1px solid rgba(23,70,127,.3)}
.b .foot{position:absolute;left:44px;right:104px;bottom:52px;height:92px;border-top:1.5px solid %(navy)s;padding:15px 0 0 108px}
.b .foot small{display:block;font-size:10.5px;font-weight:700;color:%(navy)s;letter-spacing:.14em;margin:0 0 4px}
.b .foot p{margin:0;font-size:13.6px;line-height:1.65;font-weight:700}
.b .kc{left:44px;bottom:46px;width:94px;height:94px;border:2.5px solid %(navy)s}
/* 案C */
.c1{background:%(navy)s;color:#fff}
.c1 .pill{position:absolute;top:34px;left:50%%;transform:translateX(-50%%);border:1.5px solid rgba(255,255,255,.75);color:#fff}
.c1 .big{position:absolute;top:92px;left:0;right:0;height:450px;display:flex;justify-content:center}
.c1 .big div{writing-mode:vertical-rl;font-weight:700;font-size:41px;line-height:1.55;letter-spacing:.05em;white-space:nowrap}
.c1 .name{position:absolute;right:34px;top:96px;writing-mode:vertical-rl;font-size:13px;font-weight:700;letter-spacing:.12em;color:#bcd3ef}
.c1 .kc{left:50%%;transform:translateX(-50%%);bottom:52px;width:150px;height:150px}
.c2{background:%(tint)s}
.c2 .tx{top:60px;left:50px;width:408px;height:618px;column-gap:30px;font-size:12.8px}
"""


def plain(no, side):
    bars = "".join('<i style="height:%d%%"></i>' % h for h in (100, 100, 62, 0, 100, 100, 100, 38, 0, 100, 100, 84, 0, 100, 100, 100, 55))
    return '<div class="pg plain"><div class="bars">%s</div><span class="tag">ふつうのページ（本文）</span><span class="no %s">%d</span></div>' % (bars, side, no)


def build(K):
    e = lambda t: html.escape(t, quote=False)
    ta, pa, ka = column("v4", "col_でもだって")
    tb, pb, kb = column("v2", "col_ch4_1")
    tc, pc, kc = column("v4", "col_冷笑")
    def say(k):
        """王様の一言。2つの文なら、間で改行。1つの長い文なら、最後の「、」で改行（言葉の途中で、切れないように）"""
        if k.count("。") >= 2:
            return e(k).replace("。", "。<br>", 1)
        i = k.rfind("、")
        return e(k[:i + 1]) + "<br>" + e(k[i + 1:]) if len(k) > 18 and i > 0 else e(k)
    pill = lambda n: '<span class="pill">%sCOLUMN<b>%s</b></span>' % (CROWN, n)
    A = """<div class="sheet" id="a"><div class="cap"><b>案A</b><span>うす青の全面　＋　王様の一言</span></div>
<p class="sub">ページ全体を、巻頭ページと同じうす青にします。本を閉じたままでも、小口（ページの端）の色で、コラムの場所がわかります。本文は2段にして、ふつうのページと、読む調子を変えます。一番大事な一文は、下で、王様がもう一度言います。1ページで収まります。</p>
<div class="sp">%s<div class="pg a"><div class="head">%s</div><div class="ttl">%s</div><div class="tx">%s</div>
<div class="say"><small>王様の一言</small><p>%s</p></div><div class="kc"><img src="%s" alt=""></div><span class="no l">%d</span></div></div></div>""" % (
        plain(121, "r"), pill("05"), tate(ta), body(pa), say(ka), K[1], 122)
    B = """<div class="sheet" id="b"><div class="cap"><b>案B</b><span>白地　＋　紺の帯</span></div>
<p class="sub">ページは白のまま、外側に、紺の帯を1本通します。帯に、番号と題を入れます。色を使う面が小さいので、きりっと見えます。帯は小口まで届くので、こちらも、閉じたままで場所がわかります。本文は2段で、間に細い線を入れます。1ページで収まります。</p>
<div class="sp"><div class="pg b"><div class="band"><div class="lab">%sCOLUMN<b>06</b></div></div><div class="ttl">%s</div><div class="tx">%s</div>
<div class="foot"><small>王様の一言</small><p>%s</p></div><div class="kc"><img src="%s" alt=""></div><span class="no l">%d</span></div>%s</div></div>""" % (
        CROWN, tate(tb), body(pb), say(kb), K[14], 141, plain(142, "l").replace("ふつうのページ（本文）", "ふつうのページ（次の項目）"))
    big = tate(kc).replace("、", "、<br>", 1)
    C = """<div class="sheet" id="c"><div class="cap"><b>案C</b><span>見開き　＋　紺のページに、大きな一言</span></div>
<p class="sub">2ページ使います。右のページは、紺の全面に、一番大事な一文だけを、大きく置きます。巻頭ページの「文だけのページ」と、同じ作りです。左のページで、本文を読みます。一番伝えたいコラム（「冷笑に、負けるな」など、2〜3本）だけを、この形にする使い方が合います。</p>
<div class="sp"><div class="pg c1">%s<div class="name">%s</div><div class="big"><div>%s</div></div><div class="kc"><img src="%s" alt=""></div><span class="no r" style="color:#bcd3ef">%d</span></div>
<div class="pg c2"><div class="tx">%s</div><span class="no l">%d</span></div></div></div>""" % (
        pill("09"), tate(tc), big, K[13], 220, body(pc), 221)
    return '<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>コラムのページの案</title><style>%s</style></head><body>%s%s%s</body></html>' % (
        CSS % dict(navy=NAVY, tint=TINT), A, B, C)


SHOT = """
const { chromium } = require('playwright');
(async () => {
  const [f, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1180, height: 1000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + f); await p.waitForTimeout(600);
  for (const id of ['a', 'b', 'c']) {
    const el = await p.$('#' + id);
    const over = await el.evaluate(n => [...n.querySelectorAll('.tx')].map(t => [t.scrollWidth, t.clientWidth, t.scrollHeight, t.clientHeight]));
    console.log(id, JSON.stringify(over));
    await el.screenshot({ path: out + '/コラムの案_' + id.toUpperCase() + '.png' });
  }
  await b.close();
})();
"""

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, "column_mock.html")
    open(p, "w", encoding="utf-8").write(build(kings()))
    js = os.path.join(out, "_shot.js")
    open(js, "w", encoding="utf-8").write(SHOT)
    subprocess.check_call(["node", js, p, out])
    os.remove(js)
    print("出した：", out)
