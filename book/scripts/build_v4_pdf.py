# -*- coding: utf-8 -*-
# 第2章〜第5章（07〜45番。5章・45項目の目次）を、横書きの読み用PDFにする。
#   python3 -I scripts/build_v4_pdf.py   → build/原稿_07番から45番_横書き.html と .pdf
# 中身は assemble_v4.py と同じ材料から作る。A4・1段。項目ごとにページを改める。
# 見た目（CSS）と、本文をHTMLにする所は、build_v3_pdf.py のものを使う。
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v4 as B
import v4_data as V
import build_v3_pdf as P3

ROOT = os.path.dirname(HERE)
NAME = "原稿_07番から45番_横書き"
esc = P3.esc

CSS = P3.CSS + """
/* 項目の最初の青い箱が、ページのいちばん上にぴったり付くと、前のページの下に細い線がにじむ。少しだけ下げる */
.item { padding-top: 1mm; }
/* 「まとめ」などの札だけが、ページの下に取り残されないようにする */
.tag { display: block; width: fit-content; break-after: avoid; page-break-after: avoid; }
/* まとめと、その下の一言を、同じページに置く */
.mwrap { break-inside: avoid; page-break-inside: avoid; }
.qpage .ttl { font-size: 11.5pt; font-weight: 700; margin: 0 0 4mm !important; padding-bottom: 3mm; border-bottom: 1px solid rgba(255,255,255,.45); text-align: left; }
.grp { page-break-before: always; padding-top: 80mm; text-align: center; }
.grp p { text-align: center; margin: 0; }
.grp .g1 { font-size: 11pt; color: #555; }
.grp .g2 { font-size: 22pt; font-weight: 900; color: #15467e; margin-top: 3mm; }
.grp .g3 { margin-top: 10mm; font-size: 10pt; color: #333; line-height: 2.1; text-align: center; }
.toc .grpname { font-size: 9.5pt; font-weight: 700; color: #15467e; margin: 3mm 0 1mm; }
.toc .it { grid-template-columns: 9mm 1fr; margin-bottom: 1.2mm; }
.toc .it .t { font-weight: 700; color: #16181d; }
.toc .it .xo { color: #444; font-size: 9pt; line-height: 1.6; }
.chdoor .intro h4 { font-size: 12.5pt; font-weight: 900; line-height: 1.6; margin: 0 0 4mm; }
.chdoor { padding-top: 30mm; }
.chdoor .sub { margin-top: 2mm; color: #555; }
.new { display: inline-block; font-size: 8pt; font-weight: 700; color: #a4500a; border: 1px solid #a4500a; border-radius: 99px; padding: 0 2.6mm; line-height: 1.6; margin-left: 2mm; vertical-align: middle; }
.qpage .new { color: #fff; border-color: #fff; }
"""


def kind(kk):
    """新しく書いた項目か、節を足した項目か。読む人が、見る所を選べるようにする。"""
    it = V.ITEMS[kk]
    if it["old"] is None:
        return "新しく書いた"
    if any(p[0] == "file" for p in it.get("parts", ())):
        return "節を足した"
    return ""


def item_html(kk, extra=""):
    it = V.ITEMS[kk]
    c = B.koma(kk)
    ttl, steps, king = B.sheet(kk)
    one, pts, dakara, toi = B.matome(kk)
    tag = kind(kk)
    st = "".join('<div class="st"><div class="lab">STEP<b>0%d</b></div><div><p class="do">%s</p><p class="say">「%s」</p>%s</div></div>'
                 % (i, esc(h), esc(v), ('<p class="nt">※%s</p>' % esc(note)) if note else "")
                 for i, (h, v, note) in enumerate(steps, 1))
    return """<section class="item">
<div class="qpage"><div class="no">%s%s</div><p class="ttl">%s</p><p class="q1">頭のいい人が絶対やらないこと</p><p class="q2">「%s」</p><p class="q3">じゃあ、何をするの？</p></div>
<div class="tag">本文</div>
%s
<div class="tag">頭のいい人と伸びない人の違い</div>
<div class="koma"><div class="k x"><span>伸びない人</span><b>%s</b><i>%s</i></div><div class="k o"><span>頭のいい人</span><b>%s</b><i>%s</i></div></div>
<div class="tag">今日からできる3STEP</div>
<div class="sheet"><p class="sttl">頭のいい人の『%s』3STEP</p>%s<div class="king"><span>「できた」の基準</span><p>%s</p></div></div>
<div class="mwrap"><div class="tag">まとめ</div>
<div class="matome"><p class="one">%s</p><ol>%s</ol><p>%s</p><p>迷ったら、自分に聞きます。「%s」</p></div>
%s</div></section>""" % (kk, ('<span class="new">%s</span>' % tag) if tag else "", esc(it["t"]), esc(it["q"]),
                 P3.body_html(B.body(kk)), esc(c[0][0]), esc(c[0][1]), esc(c[1][0]), esc(c[1][1]),
                 esc(ttl), st, esc(king), esc(one), "".join("<li>%s</li>" % esc(p) for p in pts), esc(dakara), esc(toi), extra)


def main():
    parts = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>原稿 07番から45番（5章・45項目）</title><style>'
             + CSS + "</style></head><body>"]
    total = sum(B.n(B.A.to_paste(B.chapter_md(ch))) for ch in V.CHAPTERS)
    parts.append('<section class="cover"><h1>原稿　第2章〜第5章<br>07番から45番（5章・45項目の目次）</h1>'
                 '<p class="sub">2026年11月19日　読み用・横書き　約%s字</p>'
                 '<div class="note"><p>章の最初にだけ、導入文があります。章の中は、番号のない小見出し（理解編など）で分けています。</p>'
                 '<p>項目は、どれも同じ順番です：質問ページ → 本文 → 頭のいい人と伸びない人の違い → 今日からできる3STEP → できた基準 → まとめ。</p>'
                 '<p>番号の横の印：「新しく書いた」は、今回、最初から書いた項目（11個）。「節を足した」は、前の原稿に節を足した項目（6個）。印のない22個は、前の原稿を、番号だけ直して使っています。</p>'
                 '<p>新しく書いた項目の、×と○、質問ページ、2コマ、3STEP、まとめは、仮の言葉です。</p>'
                 '<p>黄色の線は、原稿のマーカーの印です。</p></div></section>' % format(total, ","))
    toc = ['<section class="toc"><h2>目次</h2>']
    for num, fuda, title, sub, groups in V.CHAPTERS:
        toc.append('<p class="ch">第%d章　【%s】%s</p>' % (num, esc(fuda), esc(title)))
        for name, items in groups:
            if name:
                toc.append('<p class="grpname">■ %s</p>' % esc(name))
            for kk in items:
                it = V.ITEMS[kk]
                tag = kind(kk)
                toc.append('<div class="it"><b>%s</b><span><span class="t">%s</span>%s<br><span class="xo">×　%s<br>○　%s</span></span></div>'
                           % (kk, esc(it["t"]), ('<span class="new">%s</span>' % tag) if tag else "", esc(it["x"]), esc(it["o"])))
    toc.append("</section>")
    parts.append("\n".join(toc))
    for num, fuda, title, sub, groups in V.CHAPTERS:
        ks = [kk for _, items in groups for kk in items]
        intro = P3.body_html(B.read_new("ch%d_導入" % num))
        parts.append('<section class="chdoor"><div class="cno">第%d章</div><h1>%s</h1><p class="fld">【%s】　%s〜%s番</p>%s'
                     '<div class="intro">%s</div></section>'
                     % (num, esc(title), esc(fuda), ks[0], ks[-1], ('<p class="sub">%s</p>' % esc(sub)) if sub else "", intro))
        for name, items in groups:
            if name:
                lines = "<br>".join("%s　%s" % (kk, esc(V.ITEMS[kk]["t"])) for kk in items)
                parts.append('<section class="grp"><p class="g1">第%d章　【%s】</p><p class="g2">%s</p><p class="g3">%s</p></section>'
                             % (num, esc(fuda), esc(name), lines))
            for kk in items:
                parts.append(item_html(kk))
    parts.append("</body></html>")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", NAME + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), hp, os.path.join(ROOT, "build", NAME + ".pdf")])


if __name__ == "__main__":
    main()
