# -*- coding: utf-8 -*-
"""分岐点の試作をPDFに。book/ で実行 → build/分岐点_試作5本.pdf"""
import re, html, os, subprocess
NAVY, GRAY = "#15467E", "#8a8a8a"
def esc(s): return html.escape(s, quote=False)
src = open("manuscript/分岐点/試作5本.md", encoding="utf-8").read()

out, lines = [], src.split("\n"); i, n = 0, len(lines)
while i < n:
    l = lines[i].rstrip()
    if l.startswith("```"):
        buf=[]; i+=1
        while i<n and not lines[i].startswith("```"): buf.append(esc(lines[i])); i+=1
        i+=1
        body="\n".join(buf).strip("\n")
        ne = [b for b in buf if b.strip()]
        cls = "fork" if (len(ne)==1 and "「" not in ne[0]) else "mono"
        out.append(f'<pre class="{cls}">{body}</pre>'); continue
    if re.match(r'^\s*---\s*$', l): out.append('<hr>'); i+=1; continue
    m = re.match(r'^(#{1,3})\s+(.*)$', l)
    if m:
        lv=len(m.group(1)); txt=esc(m.group(2))
        if lv==1: out.append(f'<h1>{txt}</h1>')
        elif lv==2: out.append(f'<h2>{txt}</h2>')
        else:
            c = "ng" if "伸びない" in txt else ("ok" if "頭のいい" in txt else "")
            out.append(f'<h3 class="{c}">{txt}</h3>')
        i+=1; continue
    if not l.strip(): i+=1; continue
    buf=[]
    while i<n and lines[i].strip() and not lines[i].startswith(("#","```")) \
          and not re.match(r'^\s*---\s*$',lines[i]):
        buf.append(esc(lines[i].rstrip())); i+=1
    out.append('<p>'+"<br>".join(buf)+'</p>')

CSS=f"""
@page{{size:A4;margin:19mm 22mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10.3pt;line-height:1.9;color:#111}}
h1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:14pt;font-weight:700;color:#111;
 margin:11mm 0 4mm;padding-bottom:3mm;border-bottom:2px solid {NAVY};page-break-after:avoid}}
h1:first-of-type{{margin-top:0}}
h2{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{GRAY};
 letter-spacing:.18em;margin:7mm 0 3mm;page-break-after:avoid}}
h3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;
 margin:5.5mm 0 2mm;page-break-after:avoid}}
h3.ng{{color:#8a8a8a}} h3.ok{{color:{NAVY}}}
p{{margin:0 0 2mm}}
hr{{border:none;border-top:1px dotted #ccc;margin:5mm 0}}
pre.mono{{font-family:"Noto Serif CJK JP",serif;font-size:9.6pt;line-height:2.0;
 background:#f7f7f7;border-left:3px solid #d8d8d8;padding:3.5mm 5mm;margin:2mm 0 3mm;
 white-space:pre-wrap;page-break-inside:avoid}}
h3.ok + pre.mono{{background:#eef3f9;border-left-color:{NAVY}}}
pre.fork{{font-family:"Noto Sans CJK JP",sans-serif;font-size:13pt;font-weight:700;
 color:{NAVY};text-align:center;background:#fff;border:1.5px solid {NAVY};
 padding:5.5mm 4mm;margin:4mm 0;white-space:pre-wrap;letter-spacing:.06em;
 page-break-inside:avoid}}
"""
html_out=('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>分岐点</title>'
 f'<style>{CSS}</style></head><body>'+"\n".join(out)+'</body></html>')
os.makedirs("build",exist_ok=True)
open("build/分岐点_試作5本.html","w",encoding="utf-8").write(html_out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
 "--no-pdf-header-footer","--print-to-pdf=build/分岐点_試作5本.pdf",
 "file://"+os.path.abspath("build/分岐点_試作5本.html")],check=True,capture_output=True)
print("ok")
