# -*- coding: utf-8 -*-
"""いまの原稿を、四六判の縦組みで実際に組む。book/ で実行。

　python3 scripts/build_tatekumi.py jo      → build/縦組み_序章.pdf
　python3 scripts/build_tatekumi.py kihon   → build/縦組み_第1章.pdf
　python3 scripts/build_tatekumi.py kan     → build/縦組み_巻頭.pdf

判型　四六判 127×188mm
本文　9.5pt 明朝　行間1.75　天地18mm　左右15mm
　　　→ 1行45字　1ページ16行くらい

pages.py の計算（43字×17行）が実際と合っているかの検算にもなる。
"""
import re, html, os, sys, subprocess

NAVY, GRAY = "#15467E", "#8a8a8a"
MODE = sys.argv[1] if len(sys.argv) > 1 else "jo"
PRESET = {"jo":    ("序章",   "manuscript/序章_v10.md"),
          "kihon": ("第1章",  "manuscript/本文/新構成/基本の基本8本.md"),
          "kan":   ("巻頭",   "manuscript/巻頭ページ.md"),
          "zen":   ("原稿",   "manuscript/原稿_最新版.md")}
if MODE in PRESET:
    SRC = PRESET[MODE]
else:                                  # ファイルを直接渡してもいい
    SRC = (os.path.splitext(os.path.basename(MODE))[0], MODE)
OUT = f"縦組み_{SRC[0]}"

def esc(s): return html.escape(s, quote=False)

def tcy(s):
    """算用数字　1〜2桁は縦中横　3桁以上は正立させて縦に積む"""
    s = re.sub(r'(?<![0-9])([0-9]{3,})(?![0-9])', r'<span class="upr">\1</span>', s)
    s = re.sub(r'(?<![0-9>])([0-9]{1,2})(?![0-9<])', r'<span class="tcy">\1</span>', s)
    return s

src = open(SRC[1], encoding="utf-8").read()
if src.lstrip().startswith("# 巻頭ページ"):
    src = "# 巻頭　10秒だけ、付き合ってください\n" + src.split("---", 1)[1]

out, lines, i = [], src.split("\n"), 0
N = len(lines)
while i < N:
    l = lines[i].rstrip()
    if l.startswith("```"):
        buf = []; i += 1
        while i < N and not lines[i].startswith("```"):
            buf.append(tcy(esc(lines[i].rstrip()))); i += 1
        i += 1
        out.append('<div class="box">' + "<br>".join(buf) + '</div>'); continue
    if re.match(r'^\s*---\s*$', l):
        out.append('<div class="beat">＊</div>'); i += 1; continue
    m = re.match(r'^(#{1,3})\s+(.*)$', l)
    if m:
        lv, t = len(m.group(1)), tcy(esc(m.group(2)))
        out.append(f'<h{lv}>{t}</h{lv}>'); i += 1; continue
    if not l.strip(): i += 1; continue
    buf = []
    while i < N and lines[i].strip() and not lines[i].startswith(("#", "```")) \
          and not re.match(r'^\s*---\s*$', lines[i]):
        buf.append(tcy(esc(lines[i].rstrip()))); i += 1
    cls = ' class="ind"' if buf[0].startswith("　") else ""
    out.append(f'<p{cls}>' + "<br>".join(buf) + '</p>')

hashira = SRC[0]
CSS = f"""
@page {{ size:127mm 188mm; margin:18mm 15mm;
  @bottom-center {{ content:counter(page);
    font-family:"Noto Serif CJK JP",serif; font-size:8pt; color:#555 }}
  @top-center {{ content:"{hashira}";
    font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt;
    color:#aaa; letter-spacing:.2em }} }}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{height:100%}}
body{{height:152mm;              /* 188mm − 天地18mm×2。行の長さはこの高さで決まる */
 writing-mode:vertical-rl;text-orientation:mixed;
 font-family:"Noto Serif CJK JP",serif;font-size:9.5pt;line-height:1.75;
 color:#111;text-align:justify;
 font-feature-settings:"palt" 0}}
p{{text-indent:1em;margin:0}}
p.ind{{text-indent:0}}
p + p{{margin-top:0}}
h1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:14pt;font-weight:700;
 line-height:1.5;margin:0 0 3em 0;letter-spacing:.05em;break-after:avoid}}
h2{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10.5pt;font-weight:700;
 color:{NAVY};line-height:1.5;margin:1.6em 0 .9em 0;break-after:avoid}}
h3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;
 line-height:1.5;margin:1.2em 0 .7em 0;break-after:avoid}}
.box{{border-right:1px solid #ccc;border-left:1px solid #ccc;
 padding:.7em .2em;margin:1em 0;font-size:9pt;line-height:1.95;
 break-inside:avoid}}
.beat{{color:#bbb;font-size:7.5pt;margin:.9em 0;text-align:center;
 letter-spacing:.4em}}
.tcy{{text-combine-upright:all;-webkit-text-combine:horizontal}}
.upr{{text-orientation:upright;letter-spacing:-.05em}}
"""
html_out = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
            f'<title>{OUT}</title><style>{CSS}</style></head><body>'
            + "\n".join(out) + '</body></html>')
os.makedirs("build", exist_ok=True)
open(f"build/{OUT}.html", "w", encoding="utf-8").write(html_out)
subprocess.run(["/usr/bin/google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer", f"--print-to-pdf=build/{OUT}.pdf",
                "file://" + os.path.abspath(f"build/{OUT}.html")],
               check=True, capture_output=True)
n = subprocess.run(["pdfinfo", f"build/{OUT}.pdf"], capture_output=True, text=True).stdout
n = [l.split(":")[1].strip() for l in n.split("\n") if l.startswith("Pages")][0]
sys.path.insert(0, "scripts"); import pages
print(f"{SRC[0]}　実際に縦組みで組むと {n}ページ"
      f"（pages.py の計算では {pages.pages(open(SRC[1], encoding='utf-8').read())}ページ）")
