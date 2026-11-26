# -*- coding: utf-8 -*-
# 今の原稿を、1つのページにまとめる（著者が、通して確認するためのもの。本を組む道具ではない）
#   python3 -I scripts/zenbu.py 出す先.html          → .html と .txt
#   python3 -I scripts/zenbu.py 出す先.html --pdf    → .pdf も（A4。目次にページ番号、しおりつき）
# 中身の出どころ：
#   巻頭〜第5章（01〜35番）　著者の手元の原稿（manuscript/著者の最新原稿/ の一番新しいもの）。27番は「差しかえ」のもの
#   第5章の導入、第6章の導入と36〜40番　こちらの作業用の文（本文/v4/）
#   第7章の導入と41〜45番　下書き（本文/v4/案_第7章_5つ/。本には、まだ入れていない）
#   コラム、おわりに　今、本に入っているもの
import html, os, re, subprocess, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import v4_data as V
import assemble_v4 as B
import book_data as K

def rd(*p):
    return open(os.path.join(ROOT, *p), encoding="utf-8").read()

def md_to_doc(md):
    """作業用の文（## 見出し、``` の表、== の印）を、著者のドキュメントの形にする"""
    out, code = [], False
    for line in md.split("\n"):
        s = line.rstrip()
        if s.strip().startswith("```"):
            code = not code
            if out and out[-1] != "":
                out.append("")
            continue
        s = s.replace("==", "")
        if s.startswith("#"):
            if out and out[-1] != "":
                out.append("")
            out.append("⚫︎" + s.lstrip("# "))
            continue
        if code:
            s = re.sub(r"^　　", "", s)
        out.append(s)
    res = []
    for s in out:
        if s == "" and res and (res[-1] == "" or res[-1].startswith("⚫︎") or res[-1] == "……"):
            continue
        res.append(s)
    while res and res[-1] == "":
        res.pop()
    return "\n".join(res)

def item_v4(no):
    it = V.ITEMS[no]
    x, o = it["pair"]
    ttl, steps, king = B.sheet(no)
    m = it["matome"]
    t = ["%s × 頭のいい人は「%s」をしない。" % (no, x), "→○ 頭のいい人は「%s」をする" % o, "", md_to_doc(rd("manuscript", "本文", "v4", no + ".md")), "", "今日からできる3STEP"]
    for i, st in enumerate(steps, 1):
        t += ["STEP0%d" % i, st[0], ""]
    t += ["「できた」の基準", king, "", "まとめ", m[0], m[2], "迷ったら、自分に聞きます。「%s」" % m[3]]
    return "\n".join(t)

DRAFT = os.path.join("manuscript", "本文", "v4", "案_第7章_5つ")
def item_draft(no):
    lst = rd(DRAFT, "頭の2行と3STEP.md")
    m = re.search(r"## %s　×(.+?)　○(.+?)\n(?:一言：.*\n)?3STEP：(.+?)\n基準：(.+?)\nまとめ：(.+?)\n" % no, lst)
    x, o, steps, king, mat = m.groups()
    s, mm = steps.split("／"), mat.split("／")
    t = ["%s × 頭のいい人は「%s」をしない。" % (no, x), "→○ 頭のいい人は「%s」をする" % o, "", md_to_doc(rd(DRAFT, no + ".md")), "", "今日からできる3STEP"]
    for i, st in enumerate(s, 1):
        t += ["STEP0%d" % i, st, ""]
    t += ["「できた」の基準", king, "", "まとめ", mm[0], mm[1], "迷ったら、自分に聞きます。" + mm[2]]
    return "\n".join(t)

def master():
    f = sorted(glob.glob(os.path.join(ROOT, "manuscript", "著者の最新原稿", "*.txt")))[-1]
    return os.path.basename(f), open(f, encoding="utf-8").read().split("\n")

def build_secs():
    """2026-11-26 から：著者の手元の原稿が、巻頭から第7章（45番）まで全部入った形になったので、そこまでは、原稿のまま出す。
    コラムと、おわりには、原稿にまだないので、今、本に入っているものを足す。"""
    name, L = master()
    idx = lambda pat: next(i for i in range(len(L)) if re.match(pat, L[i]))
    secs = []   # (id, 目次に出す名前, 段, 本文, 注)
    cut = [("kantou", "表紙・巻頭ページ", r"⚫︎表紙"), ("hajimeni", "はじめに", r"⚫︎はじめに"), ("tsukaikata", "この本の使い方", r"⚫︎この本の使い方"),
           ("ch1", "第1章　6つの絶対法則（01〜06番）", r"⚫︎第1章"), ("ch2", "第2章【インプット】（07〜15番）", r"⚫︎第2章"), ("ch3", "第3章【アウトプット】（16〜25番）", r"⚫︎第3章"),
           ("ch4", "第4章【計画】（26〜30番）", r"⚫︎第4章"), ("ch5", "第5章【集中】（31〜35番）", r"⚫︎第5章"), ("ch6", "第6章【モチベ】（36〜40番）", r"⚫︎第6章"),
           ("ch7", "第7章【アップデート】（41〜45番）", r"⚫︎第7章")]
    pos = [idx(p) for _, _, p in cut] + [len(L)]
    for (sid, ttl, _), a, b in zip(cut, pos[:-1], pos[1:]):
        secs.append((sid, ttl, 0, "\n".join(L[a:b]).strip("\n"), "著者の手元の原稿（%s）のまま" % name))
    col = []
    for after, ver, fn in K.COLUMNS:
        col += [md_to_doc(rd("manuscript", "本文", ver, fn + ".md")), "（置き場：%s番のあと。前の並びの番号）" % after, "", ""]
    secs.append(("column", "コラム（12本）", 0, "\n".join(col).strip("\n"), "今、本に入っているもの。原稿が45項目になったあとの置き場は、まだ決めていない"))
    secs.append(("owarini", "おわりに", 0, md_to_doc(rd("manuscript", "本文", "v2", "91_おわりに.md")), "11月15日の下書きのまま。まだ、今の本に合わせていない"))
    return secs

HEAD = lambda sid, line: re.match(r"\s?(\d\d)(\s*× 頭のいい人は「.+」|【絶対法則】)", line) or (sid == "column" and re.match(r"⚫︎コラム　(.+)", line))
def label(t):
    if t.startswith("⚫︎コラム"):
        return t.replace("⚫︎コラム　", "")
    return re.sub(r"^(\d\d)\s*× 頭のいい人は「(.+?)」.*$", r"\1　\2", t)

def main(dst, pdf=False):
    secs = build_secs()

    def anchors(sid, text):
        """本文の中の項目の頭（NN × … / NN【絶対法則】）に、目次から飛べる印をつける"""
        out, toc = [], []
        for line in text.split("\n"):
            m = HEAD(sid, line)
            e = html.escape(line, quote=False)
            if m:
                aid = "%s-%s" % (sid, m.group(1) if sid != "column" else str(len(toc) + 1))
                if aid not in [a for a, _ in toc]:
                    toc.append((aid, line.strip()))
                    e = '<span id="%s" class="it">%s</span>' % (aid, e)
            elif line.startswith("⚫︎"):
                e = '<span class="hd">%s</span>' % e
            out.append(e)
        return "\n".join(out), toc

    nav, body, n = [], [], 0
    for sid, ttl, _, text, note in secs:
        h, toc = anchors(sid, text)
        n += len(re.sub(r"\s", "", text))
        nav.append('<li><a href="#%s">%s</a>%s</li>' % (sid, html.escape(ttl), ("<ul>" + "".join('<li><a href="#%s">%s</a></li>' % (a, html.escape(label(t))) for a, t in toc) + "</ul>") if toc else ""))
        body.append('<section id="%s"><h2>%s</h2><p class="note">%s</p><div class="tx">%s</div><p class="up"><a href="#top">↑ 目次へ</a></p></section>' % (sid, html.escape(ttl), html.escape(note), h))
    page = """<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>今の原稿（通し）</title>
<style>
:root{--bg:#f6f5f1;--pa:#fff;--fg:#1c1d21;--mu:#666b76;--li:#dcdfe6;--ac:#15467e;--hd:#0f2f57;--it:#fff3d6}
@media(prefers-color-scheme:dark){:root{--bg:#15171b;--pa:#1d2026;--fg:#e8e9ec;--mu:#9aa0ab;--li:#33373f;--ac:#8fb8ee;--hd:#b9d3f5;--it:#3a321c;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.95 "Hiragino Sans","Noto Sans JP","Yu Gothic",sans-serif}
main{max-width:780px;margin:0 auto;padding:24px max(16px,env(safe-area-inset-left,0px)) 80px}
h1{font-size:24px;line-height:1.5;margin:8px 0 4px}h2{font-size:20px;line-height:1.5;margin:0 0 4px;color:var(--hd)}
.lead{color:var(--mu);font-size:14px;margin:0 0 18px}
nav{background:var(--pa);border:1px solid var(--li);border-radius:10px;padding:14px 18px;margin:0 0 28px}
nav>ul{margin:0;padding-left:1.2em}nav ul ul{font-size:14px;color:var(--mu);columns:2;column-gap:24px;padding-left:1.1em;margin:2px 0 8px}
@media(max-width:560px){nav ul ul{columns:1}}
a{color:var(--ac);text-decoration:none}a:hover{text-decoration:underline}
section{background:var(--pa);border:1px solid var(--li);border-radius:10px;padding:22px 22px 10px;margin:0 0 26px;scroll-margin-top:10px}
.note{color:var(--mu);font-size:13px;margin:0 0 14px;padding-bottom:10px;border-bottom:1px solid var(--li)}
.tx{white-space:pre-wrap;word-break:break-word;overflow-wrap:anywhere}
.hd{font-weight:700;color:var(--hd)}.it{font-weight:700;background:var(--it);padding:2px 4px;border-radius:4px;scroll-margin-top:12px}
.up{text-align:right;font-size:13px;margin:14px 0 6px}
</style></head><body><main id="top">
<h1>今の原稿（通し）</h1>
<p class="lead">%s 時点。全部で 約%s字（空白をのぞく）。各部分の上に、どこから持ってきた文かを書いてあります。</p>
<nav><ul>%s</ul></nav>
%s
</main></body></html>""" % (DATE, "{:,}".format(n), "".join(nav), "\n".join(body))
    open(dst, "w", encoding="utf-8").write(page)
    txt = "\n\n\n".join("＝＝＝＝＝ %s ＝＝＝＝＝\n（%s）\n\n%s" % (ttl, note, text) for _, ttl, _, text, note in secs)
    open(os.path.splitext(dst)[0] + ".txt", "w", encoding="utf-8").write(txt + "\n")
    print("出した：", dst, "／ 字数", n, "／ 部分", len(secs))
    for sid, ttl, _, text, note in secs:
        print("　", ttl, len(re.sub(r"\s", "", text)), "字")

    if pdf:
        make_pdf(secs, os.path.splitext(dst)[0] + ".pdf", n)

# ---------- PDF（A4。1回目で各項目のページを調べ、2回目で目次に入れる） ----------
LABELS = ("今日からできる3STEP", "「できた」の基準", "できた基準", "まとめ", "STEP01", "STEP02", "STEP03", "導入文", "章最初のページ")
PDF_CSS = """
@page{size:A4;margin:17mm 20mm 19mm}
*{box-sizing:border-box}html{font-size:10.6pt}
body{margin:0;color:#16181d;font-family:"Noto Sans CJK JP","Hiragino Sans",sans-serif;line-height:1.86;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1{font-size:22pt;line-height:1.4;margin:0 0 2mm}
.lead{color:#5b606b;font-size:9.4pt;margin:0 0 6mm}
table.src{border-collapse:collapse;width:100%;font-size:9.2pt;line-height:1.6;margin:0 0 4mm}
table.src td{border-top:.3mm solid #d9dce3;padding:1.6mm 2mm;vertical-align:top}table.src tr:last-child td{border-bottom:.3mm solid #d9dce3}
table.src td:first-child{white-space:nowrap;font-weight:700;color:#0f2f57}
.toc{break-before:page}.toc h2{margin-bottom:3mm}
.toc a{display:flex;align-items:baseline;gap:2mm;color:inherit;text-decoration:none;line-height:1.5;break-inside:avoid}
.toc a i{flex:1;border-bottom:.25mm dotted #9aa0ab;transform:translateY(-1mm)}
.toc a b{font-weight:400;font-variant-numeric:tabular-nums;min-width:8mm;text-align:right}
.toc .s{font-weight:700;color:#0f2f57;margin-top:2.6mm;font-size:10.4pt}.toc .i{padding-left:6mm;font-size:9.3pt;color:#30343c}
section{break-before:page}
h2{font-size:15pt;line-height:1.45;color:#0f2f57;margin:0 0 1mm;padding-bottom:1.5mm;border-bottom:.5mm solid #0f2f57}
.note{color:#5b606b;font-size:8.8pt;margin:0 0 5mm}
h3{font-size:12.4pt;line-height:1.55;margin:0;padding:1.8mm 2.6mm;background:#fff1cf;border-left:1.4mm solid #e2a100;break-before:page;break-after:avoid}
.col{break-inside:avoid;margin-top:7mm}.col h3{break-before:auto}.end{break-inside:avoid}
.maru{font-weight:700;padding:1mm 2.6mm 0 4mm;margin:0 0 1mm;break-after:avoid}
h4{font-size:10.9pt;line-height:1.6;color:#0f2f57;margin:1.2mm 0 0;break-after:avoid}
p{margin:0;white-space:pre-wrap;overflow-wrap:anywhere;orphans:2;widows:2}
.sp{height:.95em}.lb{font-weight:700;color:#8a5a00;font-size:9.6pt;break-after:avoid}
.oki{color:#5b606b;font-size:8.8pt}
.mk{position:absolute;font-size:1px;line-height:1;color:#fff}
"""

def pdf_html(secs, n, pages=None):
    """pages がない時（1回目）は、ページを調べるための印を、見出しに入れる"""
    mark = pages is None
    mk = lambda aid: '<span class="mk">@@%s@@</span>' % aid if mark else ""
    pg = lambda aid: "000" if mark else str(pages[aid])
    toc, body = [], []
    for sid, ttl, _, text, note in secs:
        toc.append('<a class="s" href="#%s"><span>%s</span><i></i><b>%s</b></a>' % (sid, html.escape(ttl), pg(sid)))
        out, seen, blank, opened = [], set(), True, []   # opened：開いたままの囲み（コラム1本、項目の最後のまとめ）
        def close(*kinds):
            while opened and opened[-1] in kinds:
                opened.pop()
                while out and out[-1] == '<div class="sp"></div>':   # 囲みの最後の空きは、外に出す
                    out.pop()
                out.append("</div>")
                out.append('<div class="sp"></div>')
        for line in text.split("\n"):
            if not line.strip():
                if not blank:
                    out.append('<div class="sp"></div>')
                blank = True
                continue
            blank = False
            e = html.escape(line, quote=False)
            m = HEAD(sid, line)
            aid = m and "%s-%s" % (sid, m.group(1) if sid != "column" else str(len(seen) + 1))
            if m and (sid == "column" or aid not in seen):
                seen.add(aid)
                close("end", "col")
                toc.append('<a class="i" href="#%s"><span>%s</span><i></i><b>%s</b></a>' % (aid, html.escape(label(line.strip())), pg(aid)))
                if sid == "column":   # コラムは短いので、1本ごとにページを変えない。1本が、ページをまたがないようにする
                    out.append('<div class="col">'); opened.append("col")
                out.append('<h3 id="%s">%s%s</h3>' % (aid, mk(aid), e.strip() if sid != "column" else e[2:]))
            elif line.startswith("→○"):
                out.append('<p class="maru">%s</p>' % e)
            elif line.startswith("⚫︎"):
                close("end")
                out.append("<h4>%s</h4>" % e)
            elif line.strip() == "今日からできる3STEP":   # 3STEPからまとめまでを、1ページの中に置く
                close("end")
                out.append('<div class="end">'); opened.append("end")
                out.append('<p class="lb">%s</p>' % e)
            elif line.strip() in LABELS:
                out.append('<p class="lb">%s</p>' % e)
            elif line.startswith("（置き場："):
                out.append('<p class="oki">%s</p>' % e)
            else:
                out.append("<p>%s</p>" % e)
        close("end", "col")
        body.append('<section><h2 id="%s">%s%s</h2><p class="note">%s</p>%s</section>' % (sid, mk(sid), html.escape(ttl), html.escape(note), "".join(out)))
    src = "".join("<tr><td>%s</td><td>%s</td></tr>" % (html.escape(ttl), html.escape(note)) for _, ttl, _, _, note in secs)
    return """<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>今の原稿（通し）%s</title><style>%s</style></head><body>
<h1>今の原稿（通し）</h1>
<p class="lead">%s 時点。全部で 約%s字（空白をのぞく）。下の表は、各部分の文の出どころです。</p>
<table class="src">%s</table>
<div class="toc"><h2>目次</h2>%s</div>
%s
</body></html>""" % (DATE, PDF_CSS, DATE, "{:,}".format(n), src, "".join(toc), "".join(body))

def make_pdf(secs, dst, n):
    tmp = os.path.splitext(dst)[0] + "_印刷用.html"
    js = os.path.join(HERE, "print_pdf.js")
    foot = "今の原稿（通し）　" + DATE
    def run(pages):
        open(tmp, "w", encoding="utf-8").write(pdf_html(secs, n, pages))
        subprocess.check_call(["node", js, tmp, dst, foot])
        return subprocess.run(["pdftotext", dst, "-"], check=True, capture_output=True, text=True).stdout.split("\f")
    pp = run(None)
    pages = {}
    for i, t in enumerate(pp, 1):
        for aid in re.findall(r"@@([a-z0-9]+(?:-\d+)?)@@", t):
            pages.setdefault(aid, i)
    total = len(pp) - 1
    pp2 = run(pages)
    os.remove(tmp)
    assert len(pp2) - 1 == total, "1回目と2回目で、ページ数が違う（%d → %d）" % (total, len(pp2) - 1)
    assert "@@" not in "".join(pp2), "印が残っている"
    print("PDF：", dst, "／", total, "ページ ／ 目次に入れた見出し", len(pages))

DATE = "2026年11月26日"
if __name__ == "__main__":
    main(sys.argv[1], "--pdf" in sys.argv[2:])
