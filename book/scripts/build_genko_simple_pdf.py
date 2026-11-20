# -*- coding: utf-8 -*-
# 原稿を、そのまま読んで確かめるための、かざりのないPDFにする（横書き・A5・字は大きめ）。表紙から「おわりに」まで。
#   python3 -I scripts/build_genko_simple_pdf.py 45   → build/原稿_45個の版.pdf
#   python3 -I scripts/build_genko_simple_pdf.py 35   → build/原稿_35個の版.pdf
# もとは、台本のmd（manuscript/完全版/完全版_仮.md、manuscript/35個版/完全版_35個.md）。先に、台本を作っておく。
# 台本とちがう所：
#   ・項目は、題 →（×と○）→ 本文 → 今日からできる3STEP → まとめ（→ 王様の一言）だけ。質問ページと、2コマの欄は入れない
#   ・改行は、原稿のまま（文をつなげない）
#   ・色や枠は使わない
import html, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
WHICH = sys.argv[1] if len(sys.argv) > 1 else "45"
CONF = {
    "45": dict(md="manuscript/完全版/完全版_仮.md", name="原稿_45個の版", label="45個の版"),
    "35": dict(md="manuscript/35個版/完全版_35個.md", name="原稿_35個の版", label="35個の版"),
}[WHICH]
if WHICH == "35":
    import assemble_v6 as A6
    ITEMS = A6.V6.ITEMS
else:
    import v4_data as V
    ITEMS = V.ITEMS
SKIP = ("質問ページ", "頭のいい人と伸びない人の違い")   # 台本だけの欄
esc = lambda s: html.escape(s, quote=False)


def inline(s):
    return re.sub(r"==(.+?)==", r"<u>\1</u>", esc(s)).replace("==", "")


def kind(title):
    m = re.match(r"^([0-9]{2})　", title)
    if m:
        return "item" if int(m.group(1)) >= 7 else "item1"
    if title.startswith("コラム"):
        return "col"
    if title.startswith("■"):
        return "grp"
    if re.match(r"^第[0-9]章", title):
        return "ch"
    return "text"


def body_html(lines, k):
    """mdを、そのままの改行でHTMLにする。項目の中の ## は欄の名前（本文は名前を出さない）。### は小見出し。"""
    out, para, code, skip = [], [], False, False
    def flush():
        if para:
            out.append("<p>%s</p>" % "<br>".join(inline(x) for x in para))
            del para[:]
    for line in lines:
        s = line.strip()
        m = re.match(r"^(#{2,5}) (.+)$", s) if not code else None
        if m and len(m.group(1)) == 2 and k in ("item", "item1"):
            flush()
            t = m.group(2)
            skip = t in SKIP
            if not skip and t not in ("本文", "章最初のページ"):
                out.append('<p class="lab">%s</p>' % esc(t))
            continue
        if skip:
            continue
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
            flush(); continue
        if m:
            flush()
            out.append("<h%d>%s</h%d>" % ((3, inline(m.group(2)), 3) if len(m.group(1)) <= 3 else (4, inline(m.group(2)), 4)))
            continue
        if line.startswith("　"):
            flush(); out.append('<p class="ind">%s</p>' % inline(s)); continue
        para.append(s)
    flush()
    if code:
        out.append("</div>")
    return "\n".join(out)


CSS = """
@page { size: A5; margin: 13mm 13mm 15mm; }
* { box-sizing: border-box; }
html { font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif; font-size: 11pt; line-height: 1.95; color: #111; }
body { margin: 0; }
p { margin: 0 0 3.2mm; }
u { text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
section { page-break-before: always; }
section.first { page-break-before: auto; }
h1 { font-size: 15pt; font-weight: 900; line-height: 1.5; margin: 0 0 4mm; padding-bottom: 2.5mm; border-bottom: 1px solid #111; }
.xo { margin: 0 0 6mm; font-size: 10pt; color: #333; line-height: 1.7; }
h3 { font-size: 12pt; font-weight: 900; margin: 8mm 0 3mm; line-height: 1.6; break-after: avoid; }
h4 { font-size: 11pt; font-weight: 900; margin: 6mm 0 2.5mm; break-after: avoid; }
.lab { font-weight: 900; margin: 9mm 0 2.5mm; padding-top: 3mm; border-top: 1px solid #999; break-after: avoid; }
.ind { padding-left: 1.5em; }
.blk { margin: 2mm 0 4.5mm; padding-left: 4mm; border-left: 2px solid #999; break-inside: avoid; }
.blk div { white-space: pre-wrap; }
.grp h1, .ch h1 { border: 0; }
.top { font-size: 9.5pt; color: #333; margin-bottom: 6mm; }
.toc a { color: inherit; text-decoration: none; }
.toc div { font-size: 9.5pt; line-height: 1.8; }
.toc .t0 { font-weight: 900; margin-top: 2.5mm; }
.toc .t2, .toc .t3 { padding-left: 1.5em; }
"""


def main():
    t = open(os.path.join(ROOT, CONF["md"]), encoding="utf-8").read()
    secs = []
    for s in re.split(r"(?m)^(?=# )", t):
        if s.strip().startswith("# "):
            head, _, rest = s.partition("\n")
            secs.append((head[2:].strip(), rest))
    n_item = sum(1 for x, _ in secs if kind(x) in ("item", "item1"))
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>' % (CONF["name"], CSS)]
    toc = ['<section class="first toc"><h1>原稿（%s）</h1><p class="top">2026年11月20日　仮。項目は%d個。項目は「題 → 本文 → 今日からできる3STEP → まとめ」の順です。</p>' % (CONF["label"], n_item)]
    for i, (title, rest) in enumerate(secs):
        cls = {"ch": "t0", "grp": "t0", "item": "t2", "item1": "t2", "col": "t3"}.get(kind(title), "t1")
        toc.append('<div class="%s"><a href="#s%d">%s</a></div>' % (cls, i, esc(title)))
    toc.append("</section>")
    out.append("\n".join(toc))
    for i, (title, rest) in enumerate(secs):
        k = kind(title)
        xo = ""
        if k == "item":
            it = ITEMS[title[:2]]
            xo = '<p class="xo">×　%s<br>○　%s</p>' % (esc(it["x"]), esc(it["o"]))
        out.append('<section class="%s" id="s%d"><h1>%s</h1>%s%s</section>' % (k, i, esc(title), xo, body_html(rest.split("\n"), k)))
    out.append("</body></html>")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", CONF["name"] + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    pp = os.path.join(ROOT, "build", CONF["name"] + ".pdf")
    subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), hp, pp])
    print("PDF：build/%s.pdf　%.1fMB　／　項目 %d個" % (CONF["name"], os.path.getsize(pp) / 1e6, n_item))


if __name__ == "__main__":
    main()
