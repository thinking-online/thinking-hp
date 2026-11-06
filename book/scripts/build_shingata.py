# -*- coding: utf-8 -*-
"""新型の項目をPDFに。図つき。book/ で実行 → build/新型_20番.pdf"""
import re, html, os, subprocess
NAVY, GRAY, LT = "#15467E", "#8a8a8a", "#c9d6e6"
def esc(s): return html.escape(s, quote=False)

# ---------- 図1　10回書くあいだの頭と手
def fig1():
    cols = 10; x0, w, gap = 26, 15, 5.2
    cells = []
    for i in range(cols):
        x = x0 + i*(w+gap)
        lab = f"{i+1}回目" if i==cols-1 else str(i+1)
        cells.append(f'<text x="{x+w/2}" y="13" class="cn">{lab}</text>')
        # 頭
        fill = NAVY if i == 0 else "#fff"
        stroke = NAVY if i == 0 else "#cfcfcf"
        cells.append(f'<rect x="{x}" y="19" width="{w}" height="15" rx="2" fill="{fill}" stroke="{stroke}"/>')
        # 手
        cells.append(f'<rect x="{x}" y="40" width="{w}" height="15" rx="2" fill="{NAVY}" stroke="{NAVY}"/>')
    return f'''<svg viewBox="0 0 236 78" class="fig">
<style>
 .cn{{font:4.6px "Noto Sans CJK JP";fill:{GRAY};text-anchor:middle}}
 .rw{{font:5.2px "Noto Sans CJK JP";fill:#333}}
 .cp{{font:4.8px "Noto Sans CJK JP";fill:{NAVY};font-weight:700}}
 .un{{font:4.4px "Noto Sans CJK JP";fill:{GRAY}}}
</style>
<text x="2" y="30" class="rw">頭</text>
<text x="2" y="51" class="rw">手</text>

{"".join(cells)}
<text x="26" y="68" class="cp">頭が参加しているのは、最初の1回だけ。あとの9回は、手の運動。</text>
</svg>'''

# ---------- 図2　10語1セットの回し方
def fig2():
    words = [("available","・"),("capable",""),("reliable","・・"),("avoid","・"),
             ("provide",""),("require","・・"),("remain",""),("suppose","・"),
             ("tend",""),("afford","")]
    rows=[]
    for i,(w,d) in enumerate(words):
        y = 20 + i*7.4
        hot = len(d) >= 2
        rows.append(f'<text x="8" y="{y}" class="wd{" hot" if hot else ""}">{w}</text>')
        rows.append(f'<text x="58" y="{y}" class="dt">{d}</text>')
    steps=[("1","10語を、上から3秒ずつ見る","30秒"),
           ("2","訳を隠して、上から出していく","30秒"),
           ("3","点がついた語だけ、もう1周","20秒"),
           ("4","点が全部消えたら、次の10語へ","")]
    sv=[]
    for i,(n,t,sec) in enumerate(steps):
        y = 22 + i*18
        sv.append(f'<circle cx="84" cy="{y-2}" r="4.2" fill="{NAVY}"/>')
        sv.append(f'<text x="84" y="{y-0.3}" class="sn">{n}</text>')
        sv.append(f'<text x="93" y="{y}" class="st">{esc(t)}</text>')
        if sec: sv.append(f'<text x="226" y="{y}" class="ss">{sec}</text>')
        if i < 3: sv.append(f'<line x1="84" y1="{y+3}" x2="84" y2="{y+12}" stroke="{LT}" stroke-width="1"/>')
    return f'''<svg viewBox="0 0 232 100" class="fig">
<style>
 .wd{{font:5px "Noto Sans CJK JP";fill:#555}}
 .wd.hot{{fill:{NAVY};font-weight:700}}
 .dt{{font:6px "Noto Sans CJK JP";fill:{NAVY};letter-spacing:.5px}}
 .sn{{font:4.4px "Noto Sans CJK JP";fill:#fff;font-weight:700;text-anchor:middle}}
 .st{{font:5.2px "Noto Sans CJK JP";fill:#222}}
 .ss{{font:4.6px "Noto Sans CJK JP";fill:{GRAY};text-anchor:end}}
 .bx{{font:4.4px "Noto Sans CJK JP";fill:{GRAY}}}
 .cp{{font:4.6px "Noto Sans CJK JP";fill:{NAVY};font-weight:700}}
</style>
<rect x="3" y="9" width="66" height="84" rx="2" fill="#f6f8fb" stroke="{LT}"/>
<text x="8" y="15" class="bx">1セット　10語</text>
{"".join(rows)}
{"".join(sv)}
<text x="8" y="99" class="cp">点が2つついた語だけ、次の日に書いて覚える</text>
</svg>'''

src = open("manuscript/分岐点/新型_20番.md", encoding="utf-8").read()
FIG = {"〔図1〕": fig1(), "〔図2〕": fig2()}

out, lines = [], src.split("\n"); i, n = 0, len(lines)
while i < n:
    l = lines[i].rstrip()
    if l.strip() in FIG: out.append(FIG[l.strip()]); i += 1; continue
    if l.startswith("```"):
        buf=[]; i+=1
        while i<n and not lines[i].startswith("```"): buf.append(esc(lines[i])); i+=1
        i+=1
        body="\n".join(buf).strip("\n"); ne=[b for b in buf if b.strip()]
        if len(ne)==1 and "「" not in ne[0]: cls="fork"
        elif "頭のいい人が" in body: cls="pair"
        elif any("「" in b for b in ne): cls="mono"
        else: cls="plain"
        out.append(f'<pre class="{cls}">{body}</pre>'); continue
    if re.match(r'^\s*---\s*$', l): out.append('<hr>'); i+=1; continue
    m = re.match(r'^(#{1,3})\s+(.*)$', l)
    if m:
        lv=len(m.group(1)); txt=esc(m.group(2))
        if lv==1: out.append(f'<h1>{txt}</h1>')
        elif lv==2: out.append(f'<h2>{txt}</h2>')
        else:
            c="ng" if "伸びない" in txt else ("ok" if "頭のいい" in txt else "")
            out.append(f'<h3 class="{c}">{txt}</h3>')
        i+=1; continue
    if not l.strip(): i+=1; continue
    buf=[]
    while i<n and lines[i].strip() and not lines[i].startswith(("#","```")) \
          and lines[i].strip() not in FIG and not re.match(r'^\s*---\s*$',lines[i]):
        buf.append(esc(lines[i].rstrip())); i+=1
    t="<br>".join(buf)
    bare=t.strip()
    cls=' class="q"' if (len(buf)==1 and bare.endswith("か。") and len(bare)<42) else ''
    out.append(f'<p{cls}>{t}</p>')

CSS=f"""
@page{{size:A4;margin:19mm 22mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10.3pt;line-height:1.9;color:#111}}
h1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:14pt;font-weight:700;
 margin:10mm 0 4mm;padding-bottom:3mm;border-bottom:2px solid {NAVY};page-break-after:avoid}}
h1:first-of-type{{margin-top:0}}
h2{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{GRAY};
 letter-spacing:.18em;margin:7mm 0 3mm;page-break-after:avoid}}
h3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5pt;font-weight:700;
 margin:5mm 0 1.5mm;page-break-after:avoid}}
h3.ng{{color:{GRAY}}} h3.ok{{color:{NAVY}}}
p{{margin:0 0 2mm}}
p.q{{font-family:"Noto Sans CJK JP",sans-serif;font-size:13pt;font-weight:700;color:#111;
 text-align:center;margin:6mm 0;letter-spacing:.03em}}
hr{{border:none;border-top:1px dotted #ccc;margin:5mm 0}}
pre.plain{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9.4pt;line-height:1.95;
 background:#f7f7f7;border-left:3px solid #d8d8d8;padding:3.5mm 5mm;margin:3mm 0;
 white-space:pre-wrap;page-break-inside:avoid}}
pre.pair{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;line-height:2.0;
 border:1.5px solid {NAVY};padding:5mm 6mm;margin:4mm 0;white-space:pre-wrap;
 page-break-inside:avoid;background:#fff}}
pre.mono{{font-family:"Noto Serif CJK JP",serif;font-size:9.6pt;line-height:2.0;
 background:#f7f7f7;border-left:3px solid #d8d8d8;padding:3.5mm 5mm;margin:2mm 0 3mm;
 white-space:pre-wrap;page-break-inside:avoid}}
h3.ok + pre.mono{{background:#eef3f9;border-left-color:{NAVY}}}
pre.fork{{font-family:"Noto Sans CJK JP",sans-serif;font-size:13pt;font-weight:700;
 color:{NAVY};text-align:center;border:1.5px solid {NAVY};padding:5.5mm 4mm;margin:4mm 0;
 white-space:pre-wrap;letter-spacing:.06em;page-break-inside:avoid}}
svg.fig{{display:block;width:100%;margin:5mm 0;page-break-inside:avoid}}
"""
html_out=('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>新型20番</title>'
 f'<style>{CSS}</style></head><body>'+"\n".join(out)+'</body></html>')
os.makedirs("build",exist_ok=True)
open("build/新型_20番.html","w",encoding="utf-8").write(html_out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
 "--no-pdf-header-footer","--print-to-pdf=build/新型_20番.pdf",
 "file://"+os.path.abspath("build/新型_20番.html")],check=True,capture_output=True)
print("ok")
