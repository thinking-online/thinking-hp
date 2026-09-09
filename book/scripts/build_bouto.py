# -*- coding: utf-8 -*-
"""冒頭の新案だけを組む。縦組みと横組みの両方を出す。読んで判断するための1本。"""
import os, re, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pdf as bp
import build_tate as bt

CHROME = "/opt/pw-browsers/chromium"
SRC = "冒頭_新案.md"
SRC2 = "実演6本.md"


def force_break(h):
    """（ここでページを送る）を、本物の改ページに変える。ここだけは絶対に送る。"""
    h = re.sub(r'<p[^>]*>（ここでページを送る）</p>',
               '<div class="pagebreak"></div>', h)
    h = re.sub(r'<div class="sep"></div>\s*(?=<div class="pagebreak">)', '', h)
    h = re.sub(r'<div class="pagebreak"></div>\s*<div class="sep"></div>',
               '<div class="pagebreak"></div>', h)
    # 見出しの直後の区切り線は、注記を外した名残なので消す
    h = re.sub(r'(</h1>)\s*<div class="sep"></div>', r'\1', h)
    return h


def topdf(html_path, pdf_path):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
                    "file://" + os.path.abspath(html_path)],
                   check=True, capture_output=True)


def tate():
    """縦組み。本の見本組と同じ体裁。"""
    bp.HR_AS_PAGEBREAK = False
    bp.inline = bt.inline_v
    css = open("scripts/book.css", encoding="utf-8").read()
    raw = open(os.path.join(bp.M, SRC), encoding="utf-8").read()
    head, body, _ = bp.strip_meta(raw)
    h = bt.md_to_html_v(head + "\n\n" + body)
    h = re.sub(r'(<h1>.*?</h1>)\s*<div class="pagebreak"></div>', r'\1', h, flags=re.S)
    h = force_break(h)
    doc = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
           f"<title>冒頭 新案 縦組み</title><style>{css}</style></head><body>"
           f'<div class="front">{h}</div></body></html>')
    open("build/冒頭_新案_縦.html", "w", encoding="utf-8").write(doc)
    topdf("build/冒頭_新案_縦.html", "build/冒頭_新案_縦.pdf")
    return "build/冒頭_新案_縦.pdf"


def yoko():
    """横組み。読み合わせ用。ページ区切りは残す。"""
    bp.HR_AS_PAGEBREAK = False
    bp.inline = bt._orig_inline
    raw = open(os.path.join(bp.M, SRC), encoding="utf-8").read()
    head, body, _ = bp.strip_meta(raw)
    h = bp.md_to_html(head + "\n\n" + body)
    # 「Nページ目」の見出しは、改ページと小さな見出しに置き換える
    h = re.sub(r'<h2>(\d+)ページ目</h2>',
               r'<div class="pnum">\1ページ目</div>', h)
    h = re.sub(r'<div class="sep"></div>\s*(?=<div class="pnum">)', '', h)
    h = force_break(h)
    css = bp.CSS + """
@page { size: A5; margin: 16mm 15mm 15mm 15mm; }
body { font-family: "IPAPGothic","IPAGothic",sans-serif; font-size: 10.4pt; line-height: 1.95; }
p { margin: 0 0 1.15em 0; }
h1 { font-size: 15pt; margin: 0 0 1.6em 0; padding-bottom: .5em;
     border-bottom: 2px solid #1a1a1a; page-break-after: avoid; }
.pnum { font-size: 7.6pt; letter-spacing: .22em; color: #a8a8a8; margin: 0 0 1.1em 0;
        page-break-before: always; page-break-after: avoid; }
.pnum:first-of-type { page-break-before: avoid; }
.indent { white-space: pre-wrap; font-size: 11pt; letter-spacing: .12em;
          margin: .4em 0 1.3em 0; }
.sep { border: 0; border-top: 1px solid #ececec; margin: 1.4em 0; height: 0; }
"""
    doc = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
           f"<title>冒頭 新案 横組み</title><style>{css}</style></head><body>"
           f'<div class="front">{h}</div></body></html>')
    open("build/冒頭_新案_横.html", "w", encoding="utf-8").write(doc)
    topdf("build/冒頭_新案_横.html", "build/冒頭_新案_横.pdf")
    return "build/冒頭_新案_横.pdf"


def yoko2():
    """実演6本を、横組みで。各実演の問いと答えは必ず別ページにする。"""
    bp.HR_AS_PAGEBREAK = True
    bp.inline = bt._orig_inline
    raw = open(os.path.join(bp.M, SRC2), encoding="utf-8").read()
    head, body, _ = bp.strip_meta(raw)
    h = bp.md_to_html(head + "\n\n" + body)
    css = bp.CSS + """
@page { size: A5; margin: 16mm 15mm 15mm 15mm; }
body { font-family: "IPAPGothic","IPAGothic",sans-serif; font-size: 10.2pt; line-height: 1.95; }
p { margin: 0 0 1.15em 0; }
h1 { font-size: 15pt; margin: 0 0 1.6em 0; padding-bottom: .5em;
     border-bottom: 2px solid #1a1a1a; page-break-after: avoid; }
h2 { font-size: 9pt; letter-spacing: .18em; color: #8a8a8a; font-weight: 400;
     margin: 0 0 1.6em 0; padding-bottom: .4em; border-bottom: 1px solid #e4e4e4;
     page-break-after: avoid; }
.indent { white-space: pre-wrap; font-size: 10.6pt; letter-spacing: .06em;
          margin: .5em 0 1.4em 0; line-height: 2.0; }
"""
    doc = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
           f"<title>実演6本</title><style>{css}</style></head><body>"
           f'<div class="front">{h}</div></body></html>')
    open("build/実演6本.html", "w", encoding="utf-8").write(doc)
    topdf("build/実演6本.html", "build/実演6本.pdf")
    return "build/実演6本.pdf"


if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    print(yoko())
    print(tate())
    print(yoko2())
