# -*- coding: utf-8 -*-
"""巻頭ページ＋序章を、読む用のPDFにする。book/ で実行 → build/巻頭と序章.pdf

本文の改行は原稿のまま出す。杉浦さんに見せるときに「どこで改行するか」
まで含めて判断してもらうため、prettify はしない。
"""
import re, html, os, subprocess, sys

NAVY, GRAY = "#15467E", "#8a8a8a"
def esc(s): return html.escape(s, quote=False)

SRCS = [("巻頭ページ", "manuscript/巻頭ページ.md"),
        ("序章",       "manuscript/序章_v6_完全版.md")]
OUT = "巻頭と序章"

ARROW = re.compile(r'[→×○□]')

def render(path, first):
    src = open(path, encoding="utf-8").read()
    # 巻頭ページ.md は先頭にメモがある版があるので、--- が3つ以上あれば本体だけ取る
    out, lines = [], src.split("\n")
    i, n = 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i].rstrip())); i += 1
            i += 1
            body = "\n".join(buf).strip("\n")
            ne = [b for b in buf if b.strip()]
            if any("□" in b for b in ne):            cls = "chk"
            elif any("×" in b for b in ne) and any("○" in b for b in ne): cls = "xo"
            elif any("→" in b for b in ne):          cls = "arw"
            else:                                     cls = "box"
            out.append(f'<pre class="{cls}">{body}</pre>'); continue
        if re.match(r'^\s*---\s*$', l):
            out.append('<div class="beat">◆</div>'); i += 1; continue
        m = re.match(r'^(#{1,3})\s+(.*)$', l)
        if m:
            lv, txt = len(m.group(1)), esc(m.group(2))
            if lv == 1:
                out.append(f'<h1>{txt}</h1>')
            elif lv == 2:
                out.append(f'<h2>{txt}</h2>')
            else:
                out.append(f'<h3>{txt}</h3>')
            i += 1; continue
        if not l.strip(): i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith(("#", "```")) \
              and not re.match(r'^\s*---\s*$', lines[i]):
            buf.append(esc(lines[i].rstrip())); i += 1
        txt = "<br>".join(buf)
        # 1行だけ・短い・「か。」で終わる → 問いかけとして立てる
        bare = buf[0].strip() if len(buf) == 1 else ""
        cls = ' class="q"' if (len(buf) == 1 and bare.endswith(("か。", "か？")) and len(bare) < 42) else ""
        out.append(f'<p{cls}>{txt}</p>')
    return "\n".join(out)

body = []
for k, (name, path) in enumerate(SRCS):
    body.append(f'<div class="sh{"" if k == 0 else " brk"}">')
    body.append(render(path, first=True))
    body.append('</div>')

CSS = f"""
@page{{size:A4;margin:20mm 24mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10.6pt;line-height:2.0;color:#111}}
.sh.brk{{page-break-before:always}}
h1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:16pt;font-weight:700;color:#111;
 letter-spacing:.02em;margin:0 0 9mm;padding-bottom:3.5mm;
 border-bottom:2.5px solid {NAVY};page-break-after:avoid}}
h2{{font-family:"Noto Sans CJK JP",sans-serif;font-size:12pt;font-weight:700;color:{NAVY};
 margin:9mm 0 3.5mm;padding-left:3.5mm;border-left:3px solid {NAVY};
 line-height:1.55;page-break-after:avoid}}
h3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10.5pt;font-weight:700;
 margin:6mm 0 2mm;page-break-after:avoid}}
p{{margin:0 0 3.2mm}}
p.q{{font-family:"Noto Sans CJK JP",sans-serif;font-size:11.5pt;font-weight:700;
 color:{NAVY};margin:5mm 0 5mm}}
.beat{{color:#cfcfcf;font-size:8pt;text-align:center;letter-spacing:.5em;margin:5.5mm 0}}
pre{{white-space:pre-wrap;page-break-inside:avoid;
 font-family:"Noto Serif CJK JP",serif;font-size:10pt;line-height:2.0}}
pre.box{{background:#f7f7f7;border-left:3px solid #d8d8d8;padding:4mm 5mm;margin:3mm 0 4mm}}
pre.arw{{background:#f7f9fc;border-left:3px solid {NAVY};padding:4mm 5mm;margin:3mm 0 4mm;
 font-family:"Noto Sans CJK JP",sans-serif;font-size:9.6pt}}
pre.chk{{background:#fff;border:1px solid #d9d9d9;padding:5mm 5mm;margin:4mm 0 4.5mm;
 font-size:10.4pt;line-height:2.3}}
pre.xo{{background:#fff;border:1.5px solid {NAVY};padding:5.5mm 5mm;margin:4.5mm 0;
 font-family:"Noto Sans CJK JP",sans-serif;font-size:12pt;font-weight:700;color:{NAVY};
 line-height:2.1;letter-spacing:.04em}}
"""
out_html = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
            '<title>巻頭と序章</title>'
            f'<style>{CSS}</style></head><body>' + "\n".join(body) + '</body></html>')
os.makedirs("build", exist_ok=True)
open(f"build/{OUT}.html", "w", encoding="utf-8").write(out_html)
subprocess.run(["/usr/bin/google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer", f"--print-to-pdf=build/{OUT}.pdf",
                "file://" + os.path.abspath(f"build/{OUT}.html")],
               check=True, capture_output=True)
ws = re.compile(r'\s')
for name, path in SRCS:
    z = len(ws.sub('', open(path, encoding="utf-8").read()))
    print(f"{name}　{z:,}字　約{max(1,round(z/420))}ページ")
