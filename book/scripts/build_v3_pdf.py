# -*- coding: utf-8 -*-
# 第2章から先（07〜50番）の新しい形を、横書きの読み用PDFにする。
#   python3 -I scripts/build_v3_pdf.py   → build/原稿_07番から50番_横書き.html と .pdf
# 中身は assemble_v3.py と同じ材料から作る。A4・1段。項目ごとにページを改める。
import os, re, sys, html, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v3 as A
import v3_data as D
import mokuji_v5 as M5
import taihi_card_v2 as T
import step_card_v1 as S1

ROOT = os.path.dirname(HERE)
NAME = "原稿_07番から50番_横書き"


def esc(s):
    s = html.escape(s, quote=False)
    return re.sub(r"==(.+?)==", r'<mark>\1</mark>', s)


def body_html(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(esc(lines[i].rstrip())); i += 1
            i += 1
            out.append("<pre>" + "\n".join(buf).strip("\n") + "</pre>"); continue
        if re.match(r"^\s*---\s*$", l) or not l.strip():
            i += 1; continue
        m = re.match(r"^(#{2,4})\s+(.*)$", l)
        if m:
            tag = "h3" if len(m.group(1)) == 2 else "h4"
            out.append("<%s>%s</%s>" % (tag, esc(m.group(2)), tag)); i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "```")) and not re.match(r"^\s*---\s*$", lines[i]):
            buf.append(lines[i].rstrip()); i += 1
        cls = ' class="q"' if buf[0].startswith("　　") else ""
        out.append("<p%s>%s</p>" % (cls, "<br>".join(esc(b.strip() if cls else b) for b in buf)))
    return "\n".join(out)


def item_html(kk):
    k = int(kk)
    bad, good = M5.PAIR[kk] if kk in M5.PAIR else M5.PAIR[k]
    c = T.C.get(k) or T.C.get(kk)
    steps, king = D.SHEET[kk]
    one, pts, dakara, toi = D.MATOME[kk]
    title = S1.S[kk][0]
    st = "".join('<div class="st"><div class="lab">STEP<b>0%d</b></div><div><p class="do">%s</p><p class="say">「%s」</p></div></div>'
                 % (i, esc(h), esc(v)) for i, (h, v) in enumerate(steps, 1))
    return """<section class="item">
<div class="qpage"><div class="no">%s</div><p class="q1">頭のいい人が絶対やらないこと</p><p class="q2">「%s」</p><p class="q3">じゃあ、何をするの？</p></div>
<div class="tag">本文</div>
%s
<div class="tag">頭のいい人と伸びない人の違い</div>
<div class="koma"><div class="k x"><span>伸びない人</span><b>%s</b><i>%s</i></div><div class="k o"><span>頭のいい人</span><b>%s</b><i>%s</i></div></div>
<div class="tag">今日からできる3STEP</div>
<div class="sheet"><p class="sttl">頭のいい人の『%s』3STEP</p>%s<div class="king"><span>「できた」の基準</span><p>%s</p></div></div>
<div class="tag">まとめ</div>
<div class="matome"><p class="one">%s</p><ol>%s</ol><p>%s</p><p>迷ったら、自分に聞きます。「%s」</p></div>
</section>""" % (kk, esc(bad), body_html(A.body_of(kk)), esc(c[0][0]), esc(c[0][1]), esc(c[1][0]), esc(c[1][1]),
                 esc(title), st, esc(king), esc(one), "".join("<li>%s</li>" % esc(p) for p in pts), esc(dakara), esc(toi))


CSS = """
@page { size: A4; margin: 18mm 20mm 20mm; }
* { box-sizing: border-box; }
html { font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif; font-size: 10.5pt; line-height: 1.9; color: #16181d; }
body { margin: 0; }
h1, h2, h3, h4, p, ol, pre { margin: 0; }
mark { background: linear-gradient(transparent 55%, #ffe37a 55%); color: inherit; }
.cover { page-break-after: always; padding-top: 60mm; }
.cover h1 { font-size: 24pt; line-height: 1.5; font-weight: 900; }
.cover .sub { margin-top: 6mm; color: #555; font-size: 11pt; }
.cover .note { margin-top: 18mm; border-top: 1px solid #c9ced8; padding-top: 6mm; font-size: 10pt; color: #333; }
.cover .note p { margin-bottom: 2mm; }
.toc { page-break-after: always; }
.toc h2 { font-size: 15pt; margin-bottom: 5mm; }
.toc .ch { font-weight: 700; margin-top: 4.5mm; }
.toc .it { display: grid; grid-template-columns: 9mm 1fr; font-size: 9.5pt; line-height: 1.75; color: #333; }
.toc .it b { font-variant-numeric: tabular-nums; color: #15467e; }
.chdoor { page-break-before: always; page-break-after: always; padding-top: 55mm; }
.chdoor .cno { font-size: 13pt; color: #15467e; font-weight: 700; letter-spacing: .08em; }
.chdoor h1 { font-size: 22pt; line-height: 1.5; margin-top: 3mm; font-weight: 900; }
.chdoor .fld { margin-top: 2mm; color: #555; }
.chdoor .intro { margin-top: 14mm; border-top: 1px solid #c9ced8; padding-top: 7mm; }
.chdoor .intro p { margin-bottom: 4mm; }
.item { page-break-before: always; }
.qpage { background: #15467e; color: #fff; border-radius: 4mm; padding: 9mm 10mm 10mm; margin-bottom: 8mm; text-align: center; position: relative; }
.qpage p { text-align: center; margin: 0; }
.qpage .no { text-align: left; font-size: 15pt; font-weight: 900; font-variant-numeric: tabular-nums; opacity: .9; line-height: 1.2; margin: -3mm 0 1mm -3mm; }
.qpage .q1 { font-size: 11pt; letter-spacing: .04em; }
.qpage .q2 { font-size: 20pt; font-weight: 900; line-height: 1.5; margin: 2mm 0 2mm !important; }
.qpage .q3 { font-size: 12pt; font-weight: 700; }
.tag { display: inline-block; font-size: 8.5pt; font-weight: 700; color: #15467e; border: 1px solid #15467e; border-radius: 99px; padding: 0 3.2mm; line-height: 1.7; margin: 7mm 0 3mm; }
.item > .tag:first-of-type { margin-top: 0; }
h3 { font-size: 12pt; font-weight: 900; line-height: 1.6; margin: 7mm 0 2.5mm; padding-left: 3mm; border-left: 1.4mm solid #15467e; break-after: avoid; }
h4 { font-size: 10.5pt; font-weight: 700; margin: 4.5mm 0 1.5mm; break-after: avoid; }
p { margin-bottom: 3mm; text-align: justify; }
p.q { padding-left: 2em; font-weight: 700; }
pre { font-family: inherit; font-size: 9.8pt; line-height: 1.8; white-space: pre-wrap; background: #f1f3f7; border-radius: 2mm; padding: 3mm 4.5mm; margin: 2mm 0 4mm; break-inside: avoid; }
.koma { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; break-inside: avoid; }
.koma .k { border-radius: 3mm; padding: 4mm 5mm 5mm; text-align: center; }
.koma .x { background: #eceef2; }
.koma .o { background: #e3ecf7; border: 1px solid #15467e; }
.koma span { display: block; font-size: 9pt; color: #555; }
.koma b { display: block; font-size: 15pt; font-weight: 900; line-height: 1.6; }
.koma i { display: block; font-style: normal; font-size: 9.5pt; }
.sheet { border: 1px solid #15467e; border-radius: 3mm; padding: 4mm 5mm 5mm; break-inside: avoid; }
.sheet .sttl { font-size: 12.5pt; font-weight: 900; border-bottom: 1.5px solid #15467e; padding-bottom: 1.5mm; margin-bottom: 3mm; text-align: left; }
.st { display: grid; grid-template-columns: 20mm 1fr; gap: 4mm; align-items: start; padding: 2.2mm 0; border-bottom: 1px solid #dfe3ea; }
.st .lab { background: #15467e; color: #fff; border-radius: 99px; text-align: center; font-size: 8pt; font-weight: 700; line-height: 1.5; padding: .6mm 0 .8mm; }
.st .lab b { font-size: 10.5pt; margin-left: 1mm; }
.st .do { font-weight: 700; margin: 0 0 .8mm; text-align: left; }
.st .say { display: inline-block; border: 1px solid #15467e; border-radius: 2.5mm; padding: 0 3mm; font-size: 9.8pt; margin: 0; }
.king { display: grid; grid-template-columns: auto 1fr; gap: 4mm; align-items: center; background: #e3ecf7; border-radius: 2.5mm; padding: 2.5mm 4mm; margin-top: 3.5mm; }
.king span { background: #15467e; color: #fff; border-radius: 99px; font-size: 8.5pt; font-weight: 700; padding: 0 3mm; white-space: nowrap; }
.king p { margin: 0; font-weight: 700; text-align: left; }
.matome { background: #f7f5ee; border-radius: 3mm; padding: 4.5mm 6mm; break-inside: avoid; }
.matome .one { font-size: 12pt; font-weight: 900; line-height: 1.7; }
.matome ol { margin: 2mm 0 3mm 1.6em; padding: 0; }
.matome p { margin-bottom: 1mm; text-align: left; }
"""


def main():
    parts = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>原稿 07番から50番（新しい形）</title><style>' + CSS + "</style></head><body>"]
    total = sum(A.n(A.to_paste(A.chapter_md(ch))) for ch in D.CHAPTERS)
    parts.append('<section class="cover"><h1>原稿　第2章〜第8章<br>07番から50番（新しい形）</h1>'
                 '<p class="sub">2026年11月17日　読み用・横書き　約%s字</p>'
                 '<div class="note"><p>章の最初にだけ、導入文があります。</p>'
                 '<p>項目は、どれも同じ順番です：質問ページ → 本文 → 頭のいい人と伸びない人の違い → 今日からできる3STEP → できた基準 → まとめ。</p>'
                 '<p>本文は、今の原稿のままです。質問ページ、3STEPのシート、まとめは、新しく書いた案です。</p>'
                 '<p>黄色の線は、原稿のマーカーの印です。</p></div></section>' % format(total, ","))
    toc = ['<section class="toc"><h2>目次</h2>']
    for num, title, field, a, b in D.CHAPTERS:
        toc.append('<p class="ch">第%d章　【%s】%s</p>' % (num, esc(field), esc(title)))
        for k in range(a, b + 1):
            kk = "%02d" % k
            bad, good = M5.PAIR[kk] if kk in M5.PAIR else M5.PAIR[k]
            toc.append('<div class="it"><b>%s</b><span>×　%s　→　○　%s</span></div>' % (kk, esc(bad), esc(good)))
    toc.append("</section>")
    parts.append("\n".join(toc))
    for num, title, field, a, b in D.CHAPTERS:
        intro = "".join("<p>%s</p>" % esc(p.replace("\n", "")) for p in A.read("ch%d_扉.md" % num).strip().split("\n\n"))
        parts.append('<section class="chdoor"><div class="cno">第%d章</div><h1>%s</h1><p class="fld">【%s】　%02d〜%02d番</p>'
                     '<div class="intro">%s</div></section>' % (num, esc(title), esc(field), a, b, intro))
        for k in range(a, b + 1):
            parts.append(item_html("%02d" % k))
    parts.append("</body></html>")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", NAME + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    js = os.path.join(HERE, "print_pdf.js")
    subprocess.check_call(["node", js, hp, os.path.join(ROOT, "build", NAME + ".pdf")])


if __name__ == "__main__":
    main()
