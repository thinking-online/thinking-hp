# -*- coding: utf-8 -*-
"""はじめに＋序章＋第1章＋第2章 を1本のPDFに。book/ で実行 → build/前半.pdf"""
import re, html, os, subprocess

NAVY, GRAY, RATE = "#15467E", "#8a8a8a", 520
def esc(s): return html.escape(s, quote=False)

PARTS = [("はじめに", "この本は、10秒で始まります", "manuscript/冒頭メッセージ.md"),
         ("序章", "「自分に合った勉強法」を、探すのをやめる", "manuscript/序章_v5.md"),
         ("第1章", "結果 ＝ 戦略 × やり方 × 量", "manuscript/第1章_v5.md"),
         ("第2章", "頭のいい人が持っている、6つの武器", "manuscript/第2章_6つの武器.md")]

def body(text):
    out, lines = [], text.split("\n"); i, n = 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i])); i += 1
            i += 1
            out.append('<pre>' + "\n".join(buf).strip("\n") + '</pre>'); continue
        if re.match(r'^\s*---\s*$', l): i += 1; continue
        m = re.match(r'^#\s+(.*)$', l)
        if m: i += 1; continue                      # 章タイトルは外で出す
        m = re.match(r'^(##|###)\s+(.*)$', l)
        if m:
            t = 'h3' if m.group(1) == "##" else 'h4'
            out.append(f'<{t}>{esc(m.group(2))}</{t}>'); i += 1; continue
        if not l.strip(): i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith(("#", "```")) \
              and not re.match(r'^\s*---\s*$', lines[i]):
            buf.append(esc(lines[i].rstrip())); i += 1
        out.append('<p>' + "<br>".join(buf) + '</p>')
    return "\n".join(out)

secs, rows, tot = [], [], 0
for no, ttl, path in PARTS:
    raw = open(path, encoding="utf-8").read()
    raw = re.sub(r'^著者執筆。原文のまま保存。\s*$', '', raw, flags=re.M)
    z = len(re.sub(r'\s', '', raw)); pg = max(1, round(z/RATE)); tot += pg
    rows.append((no, ttl, z, pg))
    secs.append(f'<section class="ch"><div class="cno">{no}</div>'
                f'<h1>{esc(ttl)}</h1>{body(raw)}</section>')

trs = "".join(f'<tr><td class="a">{no}</td><td class="b">{esc(t)}</td>'
              f'<td class="c">{z:,}字</td><td class="d">約{pg}p</td></tr>'
              for no, t, z, pg in rows)

CSS = f"""
@page{{size:A4;margin:20mm 24mm 18mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10.5pt;line-height:1.95;color:#111}}
.cv{{page-break-after:always;padding-top:28mm}}
.cv .t{{font-size:20pt;font-weight:700}}
.cv .s{{font-size:10pt;color:#555;margin-top:4mm}}
.cv .lb{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;color:{GRAY};
 letter-spacing:.2em;margin:13mm 0 4mm;border-bottom:2px solid {NAVY};padding-bottom:2.5mm}}
table{{width:100%;border-collapse:collapse}}
td{{padding:3.4mm 1mm;border-bottom:1px solid #e6e6e6;vertical-align:baseline}}
td.a{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;
 color:{NAVY};width:19mm;white-space:nowrap}}
td.b{{font-size:10.5pt}}
td.c,td.d{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;color:#777;
 text-align:right;white-space:nowrap;width:17mm}}
.cv .nt{{font-size:8.5pt;color:#777;line-height:2;margin-top:10mm;
 border-top:1px dotted #ccc;padding-top:4mm}}

.ch{{page-break-before:always}}
.cno{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;
 color:{NAVY};letter-spacing:.2em}}
h1{{font-size:16pt;font-weight:700;margin:2mm 0 9mm;padding-bottom:3.5mm;
 border-bottom:2px solid {NAVY};line-height:1.5}}
h3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:11.5pt;font-weight:700;
 color:{NAVY};margin:9mm 0 3mm;page-break-after:avoid;line-height:1.5}}
h4{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;
 color:#444;margin:6mm 0 2mm;page-break-after:avoid}}
p{{margin:0 0 2mm}}
pre{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5pt;line-height:1.9;
 background:#eef3f9;border-left:3px solid {NAVY};padding:4mm 5mm;margin:4mm 0;
 white-space:pre-wrap;page-break-inside:avoid}}
"""
cv = f'''<div class="cv"><div class="t">やっているのに、伸びない。</div>
<div class="s">頭のいい人が勉強で、絶対にやらない62のこと　／　朝倉 徹大</div>
<div class="lb">前半　はじめに ・ 序章 ・ 第1章 ・ 第2章</div>
<table>{trs}</table>
<div class="nt">はじめにで「頭のなかを見える化します」と約束して、第2章で6つの武器として回収する。<br>
第1章の3つの問いのうち、1つ目（これ、出るのか）と2つ目（いま、閉じて出せるか）は、
そのまま選ぶ力と入れる力の口ぐせになる。第2章はまん中を4つに割るだけで、新しく覚えるものはない。<br>
ページは1ページ520字で計算。図と囲みが多い第2章は、実際にはこれより増えて約12ページ。</div></div>'''

out = ('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>前半</title>'
       f'<style>{CSS}</style></head><body>' + cv + "\n".join(secs) + '</body></html>')
os.makedirs("build", exist_ok=True)
open("build/前半.html", "w", encoding="utf-8").write(out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
  "--no-pdf-header-footer","--print-to-pdf=build/前半.pdf",
  "file://"+os.path.abspath("build/前半.html")], check=True, capture_output=True)
print("　".join(f"{n} {z:,}字" for n,_,z,_ in rows), f"／ 合計 {sum(r[2] for r in rows):,}字")
