# -*- coding: utf-8 -*-
"""原稿_最新版.md を、読んで詰めるためのPDFにする。
A4横組み・目次つき・項目ごとの字数つき。book/ で実行。"""
import re, html, os, subprocess

NAVY = "#15467E"
SRC  = "manuscript/原稿_最新版.md"

def esc(s): return html.escape(s, quote=False)

def body_html(text):
    out, lines, i, n = [], text.split("\n"), 0, len(text.split("\n"))
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i])); i += 1
            i += 1
            out.append('<pre>' + "\n".join(buf).strip("\n") + '</pre>'); continue
        if re.match(r'^\s*---\s*$', l): i += 1; continue
        m = re.match(r'^###?\s+(.*)$', l)
        if m: out.append(f'<h3>{esc(m.group(1))}</h3>'); i += 1; continue
        if not l.strip(): i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith(("#", "```")) \
              and not re.match(r'^\s*---\s*$', lines[i]):
            buf.append(esc(lines[i].rstrip())); i += 1
        txt = "<br>".join(buf)
        cls = ' class="xo"' if txt.lstrip().startswith(("×", "○")) else ''
        out.append(f'<p{cls}>{txt}</p>')
    return "\n".join(out)

raw = open(SRC, encoding="utf-8").read()
raw = raw.split("---", 1)[1] if raw.startswith("# 原稿") else raw

# 章と項目に割る
chunks = re.split(r'^# (.+)$', raw, flags=re.M)
pre = chunks[0]
secs = [(chunks[i].strip(), chunks[i+1]) for i in range(1, len(chunks), 2)]

def count(s): return len(re.sub(r'\s', '', s))

book, toc, total = [], [], 0
for name, blob in secs:
    parts = re.split(r'^## (\d{2})　(.+)$', blob, flags=re.M)
    items = [(parts[j], parts[j+1].strip(), parts[j+2]) for j in range(1, len(parts), 3)]
    if not items:                                   # 序章
        c = count(blob); total += c
        toc.append(f'<div class="tc"><span class="tn">{esc(name)}</span>'
                   f'<span class="tz">{c:,}字</span></div>')
        book.append(f'<section class="ch"><h1>{esc(name)}</h1>{body_html(blob)}</section>')
        continue
    toc.append(f'<div class="tch">{esc(name)}　<span class="tcn">{len(items)}本</span></div>')
    out = [f'<section class="ch"><h1>{esc(name)}</h1>']
    for num, title, bd in items:
        mw = re.search(r'^(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力)(　★厚く書く)?\s*$',
                       bd, flags=re.M)
        wp = (mw.group(1) + ("　★厚く書く" if mw.group(2) else "")) if mw else ""
        bd2 = re.sub(r'^(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力)(　★厚く書く)?\s*$',
                     '', bd, count=1, flags=re.M)
        mx = re.search(r'^\s*×「(.+?)」\s*$', bd2, flags=re.M)
        mo = re.search(r'^\s*○「(.+?)」\s*$', bd2, flags=re.M)
        bd2 = re.sub(r'^\s*[×○]「.+?」\s*$', '', bd2, count=2, flags=re.M)
        c = count(bd2); total += c
        thin = ' thin' if c < 1200 else (' fat' if c > 2300 else '')
        toc.append(f'<div class="tc"><span class="tnum">{num}</span>'
                   f'<span class="tn">{esc(title)}</span>'
                   f'<span class="tz{thin}">{c:,}</span></div>')
        out.append(f'''<div class="item">
<h2><span class="no">{num}</span>{esc(title)}</h2>
<div class="pair"><div class="l x">×　{esc(mx.group(1)) if mx else ""}</div>
<div class="l o">○　{esc(mo.group(1)) if mo else ""}</div></div>
<div class="meta">{esc(wp)}<span class="cz{thin}">{c:,}字</span></div>
{body_html(bd2)}</div>''')
    out.append('</section>'); book.append("\n".join(out))

CSS = f"""
@page {{ size: A4; margin: 20mm 24mm 18mm; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:"Noto Serif CJK JP",serif; font-size:10.5pt; line-height:1.95;
  color:#111; }}
.cover {{ text-align:center; padding-top:70mm; page-break-after:always; }}
.cover .t {{ font-size:22pt; font-weight:700; letter-spacing:.04em; }}
.cover .s {{ font-size:11pt; color:#555; margin-top:10mm; line-height:2.1; }}
.cover .n {{ font-size:9pt; color:#888; margin-top:24mm; line-height:2; }}

.toc {{ page-break-after:always; }}
.toc h1 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:13pt; color:{NAVY};
  border-bottom:2px solid {NAVY}; padding-bottom:3mm; margin-bottom:7mm; }}
.tch {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt; font-weight:700;
  color:{NAVY}; margin:6mm 0 2mm; }}
.tch .tcn {{ font-size:8pt; color:#999; font-weight:400; }}
.tc {{ display:flex; align-items:baseline; font-size:9pt; line-height:1.9;
  border-bottom:1px dotted #e0e0e0; }}
.tc .tnum {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8pt; color:{NAVY};
  font-weight:700; width:9mm; flex:none; }}
.tc .tn {{ flex:1; }}
.tc .tz {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8pt; color:#999;
  flex:none; }}
.tz.thin, .cz.thin {{ color:#c0392b; font-weight:700; }}
.tz.fat,  .cz.fat  {{ color:#b8860b; font-weight:700; }}
.tcleg {{ font-size:8pt; color:#888; margin-top:6mm; line-height:1.9; }}

.ch {{ page-break-before:always; }}
.ch h1 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:15pt; color:{NAVY};
  border-bottom:2px solid {NAVY}; padding-bottom:3mm; margin-bottom:9mm;
  letter-spacing:.06em; }}
.item {{ margin-bottom:13mm; }}
h2 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:12.5pt; font-weight:700;
  margin:10mm 0 4mm; page-break-after:avoid; line-height:1.5; }}
h2 .no {{ color:{NAVY}; margin-right:4mm; font-size:14pt; }}
h3 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt; font-weight:700;
  color:{NAVY}; margin:7mm 0 2.5mm; page-break-after:avoid; }}
.pair {{ background:#eef3f9; border-left:3px solid {NAVY}; padding:3.5mm 5mm;
  margin:0 0 2.5mm; page-break-inside:avoid; }}
.pair .l {{ font-size:10pt; line-height:1.85; }}
.pair .x {{ color:#555; }}
.pair .o {{ color:{NAVY}; font-weight:600; }}
.meta {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8pt; color:#999;
  margin-bottom:5mm; display:flex; justify-content:space-between; }}
p {{ margin:0 0 1.5mm; text-indent:0; }}
p.xo {{ background:#f7f7f7; padding:2.5mm 4mm; margin:3mm 0; }}
pre {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt; line-height:1.85;
  background:#f7f7f7; border-left:2px solid #d6d6d6; padding:3.5mm 5mm;
  margin:3.5mm 0; white-space:pre-wrap; page-break-inside:avoid; }}
"""

nitem = sum(len(re.findall(r'^## \d{2}　', b, flags=re.M)) for _, b in secs)
cover = f'''<div class="cover">
<div class="t">やっているのに、伸びない。</div>
<div class="s">頭のいい人が勉強で、絶対にやらない62のこと<br>朝倉 徹大</div>
<div class="n">原稿　最新版　2026年11月4日<br>
序章＋8章　{nitem}項目　約{total:,}字<br>
内容を詰めるための読み用。本の体裁ではない。</div></div>'''
tochtml = ('<div class="toc"><h1>目次と字数</h1>' + "\n".join(toc) +
  '<div class="tcleg">数字は本文の字数。目標は1本1,850字。<br>'
  '<span style="color:#c0392b;font-weight:700">赤</span>＝1,200字未満。足す。　'
  '<span style="color:#b8860b;font-weight:700">黄</span>＝2,300字超。削るか、厚く書く6本に入れる。</div></div>')

html_out = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
            f'<title>原稿 最新版</title><style>{CSS}</style></head><body>'
            + cover + tochtml + "\n".join(book) + '</body></html>')
os.makedirs("build", exist_ok=True)
open("build/原稿_最新版.html", "w", encoding="utf-8").write(html_out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
  "--no-pdf-header-footer","--print-to-pdf=build/原稿_最新版.pdf",
  "file://"+os.path.abspath("build/原稿_最新版.html")], check=True, capture_output=True)
print(f"項目 {nitem}　本文 {total:,}字")
