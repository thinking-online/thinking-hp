# -*- coding: utf-8 -*-
"""巻頭ページ＋序章を、読む用のPDFにする。book/ で実行 → build/巻頭と序章.pdf

本文の改行は原稿のまま出す。杉浦さんに見せるときに「どこで改行するか」
まで含めて判断してもらうため、prettify はしない。
"""
import re, html, os, subprocess, sys

NAVY, GRAY = "#15467E", "#8a8a8a"
def esc(s): return html.escape(s, quote=False)

import sys
MODE = sys.argv[1] if len(sys.argv) > 1 else ""
if MODE == "kihon":
    SRCS = [("第1章 基本の基本編", "manuscript/本文/新構成/基本の基本8本.md")]
    OUT = "基本の基本編"
elif MODE == "jo":
    SRCS = [("序章", "manuscript/序章_v7.md")]
    OUT = "序章"
else:
    SRCS = [("巻頭ページ", "manuscript/巻頭ページ.md"),
            ("序章",       "manuscript/序章_v7.md")]
    OUT = "巻頭と序章"

ARROW = re.compile(r'[→×○□]')

def render(path, first):
    src = open(path, encoding="utf-8").read()
    if src.lstrip().startswith("# 巻頭ページ"):
        # 見出しと編集メモを落として、本文だけにする
        src = "# 巻頭　10秒だけ、付き合ってください\n" + src.split("---", 1)[1]
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
            elif len(ne) == 1 and ne[0].strip().endswith(("？", "?")): cls = "aik"
            elif any("頭のなか" in b for b in ne):    cls = "atm"
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
                cls = "" if not out else ' class="brk"'
                out.append(f'<h1{cls}>{txt}</h1>')
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
if OUT == "基本の基本編":
    import re as _re
    _src = open(SRCS[0][1], encoding="utf-8").read()
    _its = _re.findall(r'^# (\d{2})　(.+)$', _src, flags=_re.M)
    _li = "\n".join(f'<div class="ti"><span class="tn">{n}</span>{t}</div>' for n, t in _its)
    body.append(f'''<div class="tobira">
  <div class="tno">第1章</div>
  <div class="tpre">頭のいい人が、絶対にやらないこと</div>
  <div class="thn">基本の基本編</div>
  <div class="tct">{len(_its)}本</div>
  <div class="tlist">{_li}</div>
  <div class="tfoot">ここから先の67個は、全部この8個のどれかでできている。</div>
</div>''')

for k, (name, path) in enumerate(SRCS):
    first_sheet = (k == 0 and OUT != "基本の基本編")
    body.append(f'<div class="sh{"" if first_sheet else " brk"}">')
    body.append(render(path, first=True))
    body.append('</div>')

CSS = f"""
@page{{size:A4;margin:20mm 24mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10.6pt;line-height:2.0;color:#111}}
.sh.brk{{page-break-before:always}}
h1.brk{{page-break-before:always;margin-top:0}}
.tobira{{page-break-after:always;padding-top:30mm}}
.tno{{font-family:"Noto Sans CJK JP",sans-serif;font-size:11pt;font-weight:700;
 color:{NAVY};letter-spacing:.3em}}
.tpre{{font-size:12pt;color:#555;margin-top:12mm;letter-spacing:.04em}}
.thn{{font-family:"Noto Sans CJK JP",sans-serif;font-size:26pt;font-weight:700;
 color:{NAVY};margin-top:3mm;letter-spacing:.05em}}
.tct{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;color:{GRAY};
 margin-top:5mm;letter-spacing:.2em;border-bottom:2px solid {NAVY};
 padding-bottom:4mm;display:block}}
.tlist{{margin-top:11mm}}
.ti{{font-size:11pt;line-height:1.6;margin-bottom:4.5mm}}
.tn{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;
 color:{NAVY};margin-right:4mm}}
.tfoot{{margin-top:14mm;border-top:1px dotted #ccc;padding-top:5mm;
 font-size:9pt;color:#777}}
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
pre.aik{{background:#fff;border:2px solid {NAVY};padding:7mm 4mm;margin:6mm 0;
 font-family:"Noto Sans CJK JP",sans-serif;font-size:15pt;font-weight:700;color:{NAVY};
 text-align:center;letter-spacing:.08em;line-height:1.4}}
pre.atm{{background:#fbfbfb;border:1px solid #e2e2e2;border-left:3px solid {NAVY};
 padding:4.5mm 5mm;margin:4mm 0 4.5mm;font-size:10pt;line-height:2.05}}
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
sys.path.insert(0, "scripts")
import pages as _pg
for name, path in SRCS:
    src = open(path, encoding="utf-8").read()
    z = len(ws.sub('', src))
    print(f"{name}　{z:,}字　四六判で {_pg.pages(src)}ページ"
          f"（改行を流し込めば {_pg.pages(src, honor_breaks=False)}ページ）")
