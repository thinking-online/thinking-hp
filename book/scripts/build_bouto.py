# -*- coding: utf-8 -*-
"""冒頭の新案だけを、本と同じ縦組みで組む。読んで判断するための1本。"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pdf as bp
import build_tate as bt

CHROME = "/opt/pw-browsers/chromium"

def main():
    bp.HR_AS_PAGEBREAK = False
    bp.inline = bt.inline_v
    css = open("scripts/book.css", encoding="utf-8").read()
    raw = open(os.path.join(bp.M, "冒頭_新案.md"), encoding="utf-8").read()
    head, body, _ = bp.strip_meta(raw)
    h = bt.md_to_html_v(head + "\n\n" + body)
    import re
    h = re.sub(r'(<h1>.*?</h1>)\s*<div class="pagebreak"></div>', r'\1', h, flags=re.S)
    doc = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
           f"<title>冒頭 新案</title><style>{css}</style></head><body>"
           f'<div class="front">{h}</div></body></html>')
    open("build/冒頭_新案.html", "w", encoding="utf-8").write(doc)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=build/冒頭_新案.pdf",
                    "file://" + os.path.abspath("build/冒頭_新案.html")],
                   check=True, capture_output=True)
    print("build/冒頭_新案.pdf")

if __name__ == "__main__":
    main()
