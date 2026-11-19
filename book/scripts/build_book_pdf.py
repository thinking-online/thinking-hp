# -*- coding: utf-8 -*-
# 完全版（仮）を、横書きの読み用PDFにする。表紙から「おわりに」まで。
#   python3 -I scripts/build_book_pdf.py   → build/完全版_仮_表紙から最後まで.html と .pdf
# 中身は assemble_book.py と同じ材料から作る。見た目は build_v4_pdf.py のものを使う。
import os, re, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_book as Z
import book_data as K
import v4_data as V
import assemble_v4 as B
import build_v4_pdf as P4
import build_v3_pdf as P3

ROOT = os.path.dirname(HERE)
NAME = "完全版_仮_表紙から最後まで"
esc = P3.esc

CSS = P4.CSS + """
.cover .kari { display: inline-block; border: 1.5px solid #a4500a; color: #a4500a; font-weight: 700; border-radius: 99px; padding: 0 5mm; font-size: 10pt; margin-bottom: 8mm; }
.cover .alt { margin-top: 6mm; color: #555; font-size: 10pt; line-height: 1.9; }
.cover .au { margin-top: 10mm; font-size: 12pt; font-weight: 700; }
.text { page-break-before: always; }
.text > h1, .col > h1 { font-size: 17pt; font-weight: 900; line-height: 1.5; margin-bottom: 7mm; padding-bottom: 3mm; border-bottom: 1.5px solid #15467e; }
.toc .line { font-size: 9.8pt; margin: 1mm 0; }
.toc .colm { font-size: 9pt; color: #a4500a; margin: 0 0 1.2mm 9mm; }
.col { page-break-before: always; background: #fbf7ee; border-radius: 4mm; padding: 9mm 10mm 8mm; }
.col .ctag { display: inline-block; background: #a4500a; color: #fff; font-size: 8.5pt; font-weight: 700; border-radius: 99px; padding: 0 3.5mm; line-height: 1.7; margin-bottom: 3mm; }
.col > h1 { border-bottom-color: #a4500a; }
.hito { margin-top: 7mm; border: 1.5px solid #16181d; border-radius: 4mm; padding: 4mm 6mm 5mm; break-inside: avoid; position: relative; }
.hito span { display: inline-block; background: #16181d; color: #fff; font-size: 8.5pt; font-weight: 700; border-radius: 99px; padding: 0 3.5mm; line-height: 1.7; }
.hito p { margin: 2.5mm 0 0; font-size: 13pt; font-weight: 900; line-height: 1.7; text-align: left; }
.hito i { display: block; font-style: normal; font-size: 8.5pt; color: #555; text-align: right; margin-top: 1mm; }
.d1 { border: 1.5px solid #15467e; border-radius: 4mm; padding: 6mm 7mm 7mm; margin-bottom: 6mm; text-align: center; }
.item > .qpage { margin-top: 2mm; }
.d1 p { text-align: center; margin: 0; line-height: 1.8; }
.d1 .dno { color: #15467e; font-weight: 900; font-size: 15pt; line-height: 1.3; text-align: left; margin: -2mm 0 1mm -2mm; }
.d1 .big { font-size: 15pt; font-weight: 900; }
.matome .raw { margin-bottom: 1mm; }
"""


def text_html(md):
    md = md.strip()
    head, body = md.split("\n", 1) if md.startswith("# ") else ("", md)
    return '<section class="text"><h1>%s</h1>\n%s</section>' % (esc(head[2:].strip()), P3.body_html(body))


def hito_html(kk):
    if kk not in K.HITOKOTO:
        return ""
    return '<div class="hito"><span>王様の一言</span><p>「%s」</p><i>受験の王様</i></div>' % esc(K.HITOKOTO[kk])


def column_html(c):
    return '<section class="col"><div class="ctag">コラム</div><h1>%s</h1>\n%s</section>' % (esc(c[0]), P3.body_html(c[1]))


def matome_html(t):
    ls = Z.nonempty(t)
    out = ['<p class="one">%s</p>' % esc(ls[0])]
    items = [l for l in ls[1:] if re.match(r"^(・|[①②③]|[123][　 ])", l)]
    rest = [l for l in ls[1:] if l not in items]
    if items:
        out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % esc(re.sub(r"^(・|[①②③]|[123][　 ]+)", "", l)) for l in items))
    out += ['<p class="raw">%s</p>' % esc(l) for l in rest]
    return '<div class="matome">%s</div>' % "".join(out)


def item1_html(kk):
    it = Z.ch1_item(kk)
    door = Z.nonempty(it["章最初のページ"])
    q = Z.nonempty(it["質問ページ"])
    c = Z.ch1_koma(it)
    ttl, steps, king = Z.ch1_sheet(kk, it)
    st = "".join('<div class="st"><div class="lab">STEP<b>0%d</b></div><div><p class="do">%s</p><p class="say">「%s」</p>%s</div></div>'
                 % (i, esc(h), esc(v), ('<p class="nt">※%s</p>' % esc(note)) if note else "")
                 for i, (h, v, note) in enumerate(steps, 1))
    dh = "".join('<p%s>%s</p>' % (' class="big"' if i == len(door) - 1 or len(door) <= 2 and i == 1 else "", esc(l)) for i, l in enumerate(door))
    qq = q[1] if len(q) >= 2 else ""
    return """<section class="item">
<div class="tag">章最初のページ</div>
<div class="d1"><p class="dno">%s</p>%s</div>
<div class="tag">導入文</div>
%s
<div class="tag">質問ページ</div>
<div class="qpage"><p class="q1">%s</p><p class="q2">%s</p><p class="q3">%s</p></div>
<div class="tag">本文</div>
%s
<div class="tag">頭のいい人と伸びない人の違い</div>
<div class="koma"><div class="k x"><span>伸びない人</span><b>%s</b><i>%s</i></div><div class="k o"><span>頭のいい人</span><b>%s</b><i>%s</i></div></div>
<div class="tag">今日からできる3STEP</div>
<div class="sheet"><p class="sttl">頭のいい人の『%s』3STEP</p>%s<div class="king"><span>「できた」の基準</span><p>%s</p></div></div>
<div class="mwrap"><div class="tag">まとめ</div>
%s
%s</div></section>""" % (kk, dh, P3.body_html(Z.body_md(it["導入文"], 0)),
                   esc(q[0]) if q else "", esc(qq), esc(q[2]) if len(q) > 2 else "",
                   P3.body_html(Z.body_md(it["本文"], 0)),
                   esc(c[0][0]), esc(c[0][1]), esc(c[1][0]), esc(c[1][1]), esc(ttl), st, esc(king),
                   matome_html(it["まとめ"]), hito_html(kk))


def toc_html():
    L = ['<section class="toc"><h2>目次</h2>']
    for l in ("10秒だけ、付き合ってください", "はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」", "この本の使い方"):
        L.append('<p class="line">%s</p>' % esc(l))
    def cols(kk):
        return "".join('<p class="colm">コラム　%s</p>' % esc(c[0]) for c in Z.columns_after(kk))
    L.append('<p class="ch">第1章　%s　【%s】</p>' % (esc(K.CH1_TITLE), esc(K.CH1_SUB)))
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L.append('<div class="it"><b>%s</b><span><span class="t">%s　［%s］</span><br><span class="xo">×　%s<br>○　%s</span></span></div>%s'
                 % (kk, esc(t), esc(nm), esc(x), esc(o), cols(kk)))
    for num, fuda, title, sub, groups in V.CHAPTERS:
        L.append('<p class="ch">第%d章　【%s】%s</p>' % (num, esc(fuda), esc(title)))
        for name, items in groups:
            if name:
                L.append('<p class="grpname">■ %s</p>' % esc(name))
            for kk in items:
                it = V.ITEMS[kk]
                L.append('<div class="it"><b>%s</b><span><span class="t">%s</span><br><span class="xo">×　%s<br>○　%s</span></span></div>%s'
                         % (kk, esc(it["t"]), esc(it["x"]), esc(it["o"]), cols(kk)))
    L.append('<p class="ch">巻末</p>')
    for l in ("45を、1枚に", "6つの言葉で、初めての場面を解く", "保護者の方へ", "参考文献"):
        L.append('<p class="line">%s</p>' % esc(l))
    L.append('<p class="ch">おわりに　笑わなかった人が、1人だけいました</p></section>')
    return "\n".join(L)


def main():
    S = Z.sections()
    total = sum(Z.n(Z.A.to_paste(md)) for _, _, md in S)
    parts = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>完全版（仮）</title><style>' + CSS + "</style></head><body>"]
    for kind, name, md in S:
        if kind == "cover":
            parts.append('<section class="cover"><div class="kari">完全版（仮）　2026年11月19日</div><h1>%s</h1>'
                         '<p class="alt">題の、ほかの案<br>%s</p><p class="au">%s</p>'
                         '<div class="note"><p>表紙から「おわりに」まで、通して読める形にした仮の原稿です。約%s字。</p>'
                         '<p>前付けと01〜04番は、著者のマスター（11月18日）の言葉のままです。05番と06番は、確定版を入れています。</p>'
                         '<p>コラムは12本（うち4本は、今回、仮に書いたもの）。「王様の一言」は17個。どちらも、著者の候補から選んで、仮に置いています。</p>'
                         '<p>題は、まだ決まっていません。黄色の線は、原稿のマーカーの印です。</p></div></section>'
                         % (esc(K.TITLES[0]), "<br>".join(esc(t) for t in K.TITLES[1:]), esc(K.AUTHOR), format(total, ",")))
        elif kind == "toc":
            parts.append(toc_html())
        elif kind == "text":
            parts.append(text_html(md))
        elif kind == "door":
            if name == "第1章":
                intro = P3.body_html(Z.to_md(Z.master(K.CH1_INTRO)))
                parts.append('<section class="chdoor"><div class="cno">第1章</div><h1>%s</h1><p class="fld">【%s】　01〜06番</p>'
                             '<div class="intro">%s</div></section>' % (esc(K.CH1_TITLE), esc(K.CH1_SUB), intro))
            else:
                ch = [c for c in V.CHAPTERS if "第%d章" % c[0] == name][0]
                num, fuda, title, sub, groups = ch
                ks = [kk for _, items in groups for kk in items]
                intro = P3.body_html(B.read_new("ch%d_導入" % num))
                parts.append('<section class="chdoor"><div class="cno">第%d章</div><h1>%s</h1><p class="fld">【%s】　%s〜%s番</p>%s'
                             '<div class="intro">%s</div></section>'
                             % (num, esc(title), esc(fuda), ks[0], ks[-1], ('<p class="sub">%s</p>' % esc(sub)) if sub else "", intro))
        elif kind == "group":
            ch = [c for c in V.CHAPTERS if any(g[0] == name for g in c[4])][0]
            items = [g[1] for g in ch[4] if g[0] == name][0]
            lines = "<br>".join("%s　%s" % (kk, esc(V.ITEMS[kk]["t"])) for kk in items)
            parts.append('<section class="grp"><p class="g1">第%d章　【%s】</p><p class="g2">%s</p><p class="g3">%s</p></section>'
                         % (ch[0], esc(ch[1]), esc(name), lines))
        elif kind == "item1":
            parts.append(item1_html(name))
        elif kind == "item":
            parts.append(P4.item_html(name, hito_html(name)))
        elif kind == "column":
            parts.append(column_html(Z.column(*[(s, nm) for k, s, nm in K.COLUMNS if Z.column(s, nm)[0] == name][0])))
    parts.append("</body></html>")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", NAME + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), hp, os.path.join(ROOT, "build", NAME + ".pdf")])


if __name__ == "__main__":
    main()
