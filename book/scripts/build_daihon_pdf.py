# -*- coding: utf-8 -*-
# 台本（完全版のmd）を、横書きの確認用PDFにする。表紙から「おわりに」まで。
#   python3 -I scripts/build_daihon_pdf.py 45   → build/台本_45個の版_新しい形.pdf
#   python3 -I scripts/build_daihon_pdf.py 35   → build/台本_35個の版_新しい形.pdf
# 先に、台本を作っておく（assemble_v4.py と assemble_book.py、35個の版は v6.py rebuild と assemble_v6.py）。
# 項目の題の下に出す「本の形でのページ数」は、build_tate_book.py new / new35 （--koma つきも）の結果を使う。
# 本文は、本の形と同じように、文をつなげて段落にする（無駄な改行をなくす。170字まで）。
import html, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WHICH = sys.argv[1] if len(sys.argv) > 1 else "45"
CONF = {
    "45": dict(md="manuscript/完全版/完全版_仮.md", name="台本_45個の版_新しい形", n=45, pg="本の形_新しい形", label="45個の版"),
    "35": dict(md="manuscript/35個版/完全版_35個.md", name="台本_35個の版_新しい形", n=35, pg="本の形_新しい形_35個", label="35個の版"),
}[WHICH]
PARA_MAX = 170
FIX = re.compile(r"^(・|×|○|→|↓|[①-⑨]|[0-9０-９]+[　 .．、])")
esc = lambda s: html.escape(s, quote=False)


def inline(s):
    return re.sub(r"==(.+?)==", r"<mark>\1</mark>", esc(s)).replace("==", "")


def pages(suffix=""):
    p = os.path.join(ROOT, "build", CONF["pg"] + suffix + "_ページ数.json")
    if not os.path.exists(p):
        return None, {}
    d = json.load(open(p, encoding="utf-8"))
    return d["total"], {n: pg for part, n, pg, r in d["flows"] if part.startswith("07〜")}


TOTAL, PG = pages()
TOTAL_K, PG_K = pages("_2コマあり")
# 文をつなげる所：項目の本文と導入文、章の導入、はじめに、おわりに、コラム（手紙は別）、この本の使い方
MERGE_SEC = ("本文", "導入文")


def kind(title):
    if re.match(r"^[0-9]{2}　", title):
        return "item"
    if title.startswith("コラム"):
        return "col"
    if title.startswith("■"):
        return "grp"
    if re.match(r"^第[0-9]章", title):
        return "ch"
    return "text"


def body_html(lines, merge_all, k):
    """mdの行を、HTMLにする。## は部分の名前、### は小見出し。``` の中は、そのまま置く。"""
    out, buf, code, sec = [], [], False, None
    def flush():
        if buf:
            out.append("<p>%s</p>" % inline("".join(buf)))
            del buf[:]
    def merge_on():
        return merge_all if sec is None else sec in MERGE_SEC
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            flush()
            out.append("</div>" if code else '<div class="blk">')
            code = not code
            continue
        if code:
            if s:
                out.append("<div>%s</div>" % inline(s))
            continue
        if not s or s == "---":
            if not merge_on():
                flush()
            continue
        m = re.match(r"^(#{2,5}) (.+)$", s)
        if m:
            flush()
            lv, t = len(m.group(1)), m.group(2)
            if lv == 2 and k in ("item",):
                sec = t
                out.append('<div class="sec"><span>%s</span></div>' % esc(t))
            elif lv == 2:
                out.append("<h3>%s</h3>" % inline(t))
            elif lv == 3:
                out.append("<h3>%s</h3>" % inline(t))
            else:
                out.append("<h4>%s</h4>" % inline(t))
            continue
        if s in ("……", "…"):
            flush(); out.append('<p class="c">%s</p>' % s); continue
        if line.startswith("　") or FIX.match(s):
            flush(); out.append('<p class="ind">%s</p>' % inline(s)); continue
        if s.startswith("「") and s.endswith("」"):
            flush(); out.append('<p class="q">%s</p>' % inline(s)); continue
        if not merge_on():
            flush(); out.append("<p>%s</p>" % inline(s)); continue
        if buf and sum(len(x) for x in buf) + len(s) > PARA_MAX:
            flush()
        buf.append(s)
    flush()
    if code:
        out.append("</div>")
    return "\n".join(out)


CSS = """
@page { size: A4; margin: 18mm 20mm 20mm; }
* { box-sizing: border-box; }
html { font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif; font-size: 10.5pt; line-height: 1.9; color: #16181d; }
body { margin: 0; }
p { margin: 0 0 2.6mm; text-align: justify; }
p.c { text-align: center; color: #666; margin: 1mm 0 3mm; }
p.ind { padding-left: 2em; font-weight: 700; margin: 2.5mm 0 3.5mm; }
p.q { padding-left: 1em; }
mark { background: #d5e4f7; color: inherit; padding: 0 .1em; }
section { page-break-before: always; }
section.cover, section.first { page-break-before: auto; }
h1 { font-size: 17pt; font-weight: 900; line-height: 1.5; margin: 0 0 3mm; padding-bottom: 3mm; border-bottom: 1.5px solid #15467e; }
h1 .no { display: inline-block; background: #15467e; color: #fff; border-radius: 2mm; padding: 0 3mm; margin-right: 3mm; font-size: 14pt; }
.meta { font-size: 8.5pt; color: #666; margin: 0 0 6mm; }
h3 { font-size: 12pt; font-weight: 900; color: #15467e; margin: 7mm 0 2.5mm; line-height: 1.6; break-after: avoid; }
h4 { font-size: 10.5pt; font-weight: 900; margin: 5mm 0 2mm; break-after: avoid; }
.sec { margin: 7mm 0 3mm; border-top: 1px solid #c9d3e0; padding-top: 2mm; break-after: avoid; }
.sec span { display: inline-block; background: #e3ecf7; color: #15467e; font-size: 8.5pt; font-weight: 700; border-radius: 99px; padding: 0 3.5mm; line-height: 1.8; }
.blk { background: #f4f6f9; border-radius: 2.5mm; padding: 3mm 5mm; margin: 2.5mm 0 4mm; font-size: 10pt; line-height: 1.85; break-inside: avoid; }
.blk div { white-space: pre-wrap; }
.grp h1, .ch h1 { border: 0; text-align: center; margin-top: 60mm; font-size: 20pt; }
.grp h1 { font-size: 16pt; color: #15467e; }
.ch .intro { margin-top: 14mm; }
.col { background: #fbf7ee; border-radius: 4mm; padding: 8mm 10mm; }
.col h1 { border-bottom-color: #a4500a; }
.cover h1 { border: 0; font-size: 24pt; margin: 30mm 0 4mm; }
.cover .kari { display: inline-block; border: 1.5px solid #a4500a; color: #a4500a; font-weight: 700; border-radius: 99px; padding: 0 5mm; font-size: 10pt; }
.cover table { border-collapse: collapse; margin: 4mm 0 6mm; font-size: 9.5pt; }
.cover td, .cover th { border: 1px solid #c9d3e0; padding: 1mm 3.5mm; text-align: left; line-height: 1.6; }
.cover th { background: #e3ecf7; }
.cover ul { margin: 2mm 0 6mm; padding-left: 1.4em; }
.cover li { margin: .8mm 0; }
.toc a { color: inherit; text-decoration: none; }
.toc div { font-size: 9.6pt; line-height: 1.75; }
.toc .t0 { font-weight: 900; margin-top: 3mm; color: #15467e; }
.toc .t2 { padding-left: 1.5em; }
.toc .t3 { padding-left: 1.5em; color: #a4500a; font-size: 9pt; }
"""


def cover(secs):
    n_item = sum(1 for t, _ in secs if kind(t) == "item")
    L = ['<section class="cover"><div class="kari">台本（仮）　2026年11月20日　確認用・横書き</div>',
         "<h1>%s（新しい形）</h1>" % CONF["label"],
         "<p>項目は、全部で%d個（第1章の6個 ＋ %d個）。</p>" % (n_item, n_item - 6)]
    if TOTAL:
        L.append("<table><tr><th>本の形にした時（A5・縦書き・1行40字・16行）</th><th>全体</th></tr>"
                 "<tr><td>2コマなし</td><td>%dページ</td></tr>%s</table>"
                 % (TOTAL, ("<tr><td>2コマあり</td><td>%dページ</td></tr>" % TOTAL_K) if TOTAL_K else ""))
    L.append("<p>07番から先の項目は、どれも、次の順番で書いてあります。</p><ul>"
             "<li>問い（その場で試せる問い）</li><li>理由（1つ）</li><li>やり方（本文の半分以上。実際の教科で、1回やって見せる）</li>"
             "<li>つまずく所（1〜2つ）</li><li>今日からできる3STEP（文字）と、「できた」の基準</li><li>まとめ（一言 → だから → 自分への問い）</li></ul>")
    L.append("<p>この確認用PDFは、横書きです。本文は、本の形と同じように、文をつなげて段落にしてあります（無駄な改行をなくす）。"
             "「頭のいい人と伸びない人の違い」は、2コマの絵にする想定の欄です（本に入れるかは、まだ決めていません）。"
             "項目の題の下に、本の形にした時のページ数を書いてあります。</p>")
    if WHICH == "35":
        sys.path.insert(0, HERE)
        import v6 as F
        import v4_data as V
        rows = "".join("<tr><td>%s</td><td>%s%s</td><td>%s</td></tr>" % (nn, F.OLD[nn], ("＋" + F.HOST[nn]) if nn in F.HOST else "", esc(V.ITEMS[F.OLD[nn]]["t"]))
                       for nn in sorted(F.OLD) if nn in F.HOST)
        L.append("<p>45個の版から、9個をまとめ、1個（値段だけで決める）をコラムにしました。まとめた項目は、次の9個です。"
                 "まとめた相手の「やり方」を、本文の最後の節に足しています。3STEPとまとめは、まとめ先の項目のものです。</p>"
                 "<table><tr><th>35個の版の番号</th><th>45個の版の番号</th><th>題（まとめ先）</th></tr>%s</table>" % rows)
    L.append("</section>")
    return "\n".join(L)


def main():
    t = open(os.path.join(ROOT, CONF["md"]), encoding="utf-8").read()
    secs = []
    for s in re.split(r"(?m)^(?=# )", t):
        if not s.strip().startswith("# "):
            continue
        head, _, rest = s.partition("\n")
        secs.append((head[2:].strip(), rest))
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>' % (CONF["name"], CSS)]
    out.append(cover(secs))
    toc = ['<section class="toc"><h1>この台本の中身</h1>']
    for i, (title, rest) in enumerate(secs):
        k = kind(title)
        cls = {"ch": "t0", "grp": "t0", "item": "t2", "col": "t3"}.get(k, "t1")
        toc.append('<div class="%s"><a href="#s%d">%s</a></div>' % (cls, i, esc(title)))
    toc.append("</section>")
    out.append("\n".join(toc))
    for i, (title, rest) in enumerate(secs):
        k = kind(title)
        lines = rest.split("\n")
        if k == "item":
            no, _, name = title.partition("　")
            meta = ""
            if no in PG:
                meta = '<p class="meta">本の形で %dページ%s</p>' % (PG[no], ("（2コマを入れると %dページ）" % PG_K[no]) if no in PG_K else "")
            out.append('<section class="item" id="s%d"><h1><span class="no">%s</span>%s</h1>%s%s</section>'
                       % (i, no, esc(name), meta, body_html(lines, False, k)))
        elif k == "grp":
            out.append('<section class="grp" id="s%d"><h1>%s</h1>%s</section>' % (i, esc(title), body_html(lines, False, k)))
        elif k == "ch":
            out.append('<section class="ch" id="s%d"><h1>%s</h1><div class="intro">%s</div></section>' % (i, esc(title), body_html(lines, True, k)))
        elif k == "col":
            out.append('<section class="col" id="s%d"><h1>%s</h1>%s</section>' % (i, esc(title), body_html(lines, "手紙" not in title, k)))
        else:
            merge = title.startswith(("はじめに", "おわりに", "この本の使い方"))
            out.append('<section class="text" id="s%d"><h1>%s</h1>%s</section>' % (i, esc(title), body_html(lines, merge, k)))
    out.append("</body></html>")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", CONF["name"] + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    pp = os.path.join(ROOT, "build", CONF["name"] + ".pdf")
    subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), hp, pp])
    print("PDF：build/%s.pdf　%.1fMB　／　項目 %d個" % (CONF["name"], os.path.getsize(pp) / 1e6, sum(1 for t_, _ in secs if kind(t_) == "item")))


if __name__ == "__main__":
    main()
