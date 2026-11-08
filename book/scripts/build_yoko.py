# -*- coding: utf-8 -*-
"""原稿_最新版_マーカー.md を、本の体裁に近い横組みPDFにする。
A5・1段・柱とノンブルつき。マーカー（==…==）は色の帯で出す。
読み用。実際の本は四六判の縦組み（scripts/build_tatekumi.py）。
book/ で実行。"""
import re, html, os, subprocess

NAVY = "#15467E"
MK   = "#d0dae8"
SRC  = "manuscript/原稿_最新版_マーカー.md"

def esc(s):
    s = html.escape(s, quote=False)
    return re.sub(r'==(.+?)==', r'<span class="mk">\1</span>', s)

def body_html(text):
    out, lines = [], text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i].rstrip())); i += 1
            i += 1
            out.append('<pre>' + "\n".join(buf).strip("\n") + '</pre>'); continue
        if re.match(r'^\s*---\s*$', l): i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m:
            lv = "h3" if len(m.group(1)) <= 2 else "h4"
            out.append(f'<{lv}>{esc(m.group(2))}</{lv}>'); i += 1; continue
        if not l.strip(): i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith(("#", "```")) \
              and not re.match(r'^\s*---\s*$', lines[i]):
            buf.append(lines[i].rstrip()); i += 1
        if not buf: i += 1; continue
        joined = "<br>".join(esc(b) for b in buf)
        first = buf[0].lstrip()
        if first.startswith(("×", "○")):
            out.append(f'<p class="xo">{joined}</p>')
        elif first.startswith(("この場面を見つけた問い", "今日やること")):
            out.append(f'<p class="todo">{joined}</p>')
        elif buf[0].startswith("　　"):
            out.append(f'<p class="q">{joined}</p>')
        else:
            out.append(f'<p>{joined}</p>')
    return "\n".join(out)

raw = open(SRC, encoding="utf-8").read()
raw = raw.split("\n---\n", 1)[1] if raw.startswith("# 原稿") else raw

chunks = re.split(r'^# (.+)$', raw, flags=re.M)
secs = [(chunks[i].strip(), chunks[i+1]) for i in range(1, len(chunks), 2)]

CHNO = {"基本の基本": "第1章", "戦略": "第2章", "計画": "第3章", "授業": "第4章",
        "暗記": "第5章", "演習": "第6章", "復習": "第7章", "集中": "第8章",
        "モチベ": "第9章"}
CHSUB = {"基本の基本": "全部の土台になる8つ", "戦略": "どこをやるかを決める",
         "計画": "いつやるかを決める", "授業": "学校の時間を使い切る",
         "暗記": "覚えたものを、出せるようにする", "演習": "解くときの手を変える",
         "復習": "間違いを、точ点に変える", "集中": "机に向かう時間を守る",
         "モチベ": "続ける形を作る"}
CHSUB["復習"] = "間違いを、点に変える"

book, toc = [], []
WORD = r'(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力)'

for name, blob in secs:
    parts = re.split(r'^## (\d{2})　(.+)$', blob, flags=re.M)
    items = [(parts[j], parts[j+1].strip(), parts[j+2]) for j in range(1, len(parts), 3)]
    if not items:                                        # 巻頭・序章
        short = name.split("　")[0]
        mx = re.search(r'^\s*×「(.+?)」\s*$', blob, flags=re.M)
        mo = re.search(r'^\s*○「(.+?)」\s*$', blob, flags=re.M)
        pair = ""
        if mx and mo:
            blob = re.sub(r'^\s*[×○]「.+?」\s*$', '', blob, count=2, flags=re.M)
            pair = (f'<div class="pair"><div class="l x"><span class="s">×</span>'
                    f'{esc(mx.group(1))}</div><div class="l o"><span class="s">○</span>'
                    f'{esc(mo.group(1))}</div></div>')
        toc.append(f'<div class="tch">{esc(name)}</div>')
        book.append(f'<section class="ch" data-run="{esc(short)}">'
                    f'<div class="runner">{esc(short)}</div>'
                    f'<h1 class="front">{esc(name)}</h1>{pair}{body_html(blob)}</section>')
        continue
    key = name.split("　")[0]
    no  = CHNO.get(key, "終章")
    sub = CHSUB.get(key, "本番で、取りこぼさない")
    run = f'{no}　{key}'
    toc.append(f'<div class="tch">{no}　{key}　<span class="tcn">{len(items)}本</span></div>')
    out = [f'<section class="chdoor"><div class="dno">{no}</div>'
           f'<div class="dname">{esc(key)}</div><div class="dsub">{esc(sub)}</div></section>',
           f'<section class="ch" data-run="{esc(run)}"><div class="runner">{esc(run)}</div>']
    for num, title, bd in items:
        title = re.sub(r'\s*★(厚く書く|新規)\s*$', '', title)
        mw = re.search(r'^' + WORD + r'(　★厚く書く)?\s*$', bd, flags=re.M)
        wp = mw.group(1) if mw else ""
        bd2 = re.sub(r'^' + WORD + r'(　★厚く書く)?\s*$', '', bd, count=1, flags=re.M)
        mx = re.search(r'^\s*×「(.+?)」\s*$', bd2, flags=re.M)
        mo = re.search(r'^\s*○「(.+?)」\s*$', bd2, flags=re.M)
        bd2 = re.sub(r'^\s*[×○]「.+?」\s*$', '', bd2, count=2, flags=re.M)
        toc.append(f'<div class="tc"><span class="tnum">{num}</span>'
                   f'<span class="tn">{esc(title)}</span></div>')
        out.append(f'''<div class="item">
<h2><span class="no">{num}</span>{esc(title)}</h2>
<div class="pair"><div class="l x"><span class="s">×</span>{esc(mx.group(1)) if mx else ""}</div>
<div class="l o"><span class="s">○</span>{esc(mo.group(1)) if mo else ""}</div></div>
<div class="meta">{esc(wp)}</div>
{body_html(bd2)}</div>''')
    out.append('</section>')
    book.append("\n".join(out))

# 巻末・おわりに
for path, nm in [("manuscript/本文/巻末.md", "巻末"), ("manuscript/おわりに.md", "おわりに")]:
    t = open(path, encoding="utf-8").read()
    t = re.sub(r'^#\s+(.+)$', r'', t, count=1, flags=re.M)
    t = re.sub(r'^\*\*(.+?)\*\*$', r'\1', t, flags=re.M).replace("**", "")
    head = open(path, encoding="utf-8").read().split("\n")[0].lstrip("# ").strip()
    book.append(f'<section class="ch" data-run="{esc(nm)}"><div class="runner">{esc(nm)}</div>'
                f'<h1 class="front">{esc(head)}</h1>{body_html(t)}</section>')
    toc.append(f'<div class="tch">{esc(head)}</div>')

CSS = f"""
@page {{ size: 148mm 210mm; margin: 20mm 18mm 16mm;
  @bottom-center {{ content: counter(page); font-family:"Noto Sans CJK JP",sans-serif;
    font-size:8pt; color:#999; }} }}
@page :first {{ @bottom-center {{ content: ""; }} }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:"Noto Serif CJK JP",serif; font-size:9.5pt; line-height:1.95;
  color:#111; text-align:justify; }}

.cover {{ text-align:center; padding-top:52mm; page-break-after:always; }}
.cover .t  {{ font-size:21pt; font-weight:700; letter-spacing:.03em; line-height:1.6; }}
.cover .s  {{ font-size:10.5pt; color:#333; margin-top:11mm; line-height:2.1; }}
.cover .a  {{ font-size:12pt; margin-top:16mm; letter-spacing:.2em; }}
.cover .n  {{ font-size:8pt; color:#999; margin-top:26mm; line-height:1.9; }}

.toc {{ page-break-after:always; }}
.toc h1 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:13pt; color:{NAVY};
  letter-spacing:.3em; margin-bottom:8mm; }}
.tch {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; font-weight:700;
  color:{NAVY}; margin:5mm 0 1.5mm; }}
.tch .tcn {{ font-size:7.5pt; color:#aaa; font-weight:400; }}
.tc {{ display:flex; align-items:baseline; font-size:8.5pt; line-height:1.85; }}
.tc .tnum {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:{NAVY};
  font-weight:700; width:7mm; flex:none; }}
.tc .tn {{ flex:1; }}

.chdoor {{ page-break-before:always; page-break-after:always; padding-top:66mm;
  text-align:center; }}
.chdoor .dno {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt;
  letter-spacing:.4em; color:{NAVY}; }}
.chdoor .dname {{ font-size:24pt; font-weight:700; margin-top:6mm; letter-spacing:.08em; }}
.chdoor .dsub {{ font-size:9.5pt; color:#666; margin-top:7mm; }}

.ch {{ page-break-before:always; }}
.runner {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:#b0b0b0;
  text-align:right; letter-spacing:.1em; margin-bottom:7mm; }}
h1.front {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:16pt; color:{NAVY};
  margin-bottom:9mm; line-height:1.5; letter-spacing:.04em; }}
h2 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:12pt; font-weight:700;
  margin:0 0 4mm; page-break-after:avoid; line-height:1.55; }}
h2 .no {{ color:{NAVY}; margin-right:3.5mm; font-size:14pt; }}
h3 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10pt; font-weight:700;
  color:{NAVY}; margin:7mm 0 2.5mm; page-break-after:avoid; line-height:1.6; }}
h4 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; font-weight:700;
  margin:5mm 0 1.5mm; page-break-after:avoid; }}
.item {{ page-break-before:always; }}
.ch > .item:first-of-type {{ page-break-before:avoid; }}
.pair {{ border-left:3px solid {NAVY}; padding:3mm 0 3mm 5mm; margin:0 0 3mm;
  page-break-inside:avoid; }}
.pair .l {{ font-size:9.5pt; line-height:1.8; }}
.pair .l .s {{ font-family:"Noto Sans CJK JP",sans-serif; display:inline-block;
  width:5mm; }}
.pair .x {{ color:#666; }}
.pair .o {{ color:{NAVY}; font-weight:600; }}
.meta {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:#aaa;
  margin-bottom:6mm; letter-spacing:.08em; }}
p {{ margin:0 0 2mm; }}
p + p {{ text-indent:1em; }}
p.q {{ margin:3.5mm 0; }}
p.xo {{ border-left:2px solid #d6d6d6; padding:2mm 4mm; margin:3.5mm 0;
  font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt; }}
p.todo {{ background:#f5f7fa; padding:3mm 4mm; margin:4mm 0 0;
  font-family:"Noto Sans CJK JP",sans-serif; font-size:8.5pt; line-height:1.9;
  page-break-inside:avoid; }}
pre {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8.5pt; line-height:1.85;
  background:#f7f7f7; padding:3mm 4mm; margin:3.5mm 0; white-space:pre-wrap;
  page-break-inside:avoid; }}
.mk {{ background:{MK}; padding:0 .15em; }}
"""

nitem = sum(len(re.findall(r'^## \d{2}　', b, flags=re.M)) for _, b in secs)
cover = f'''<div class="cover">
<div class="t">やっているのに、伸びない。</div>
<div class="s">頭のいい人が勉強で、絶対にやらない{nitem}のこと</div>
<div class="a">朝倉 徹大</div>
<div class="n">原稿　横組み読み用　{nitem}項目<br>
実際の本は四六判の縦組みになる</div></div>'''
tochtml = '<div class="toc"><h1>目次</h1>' + "\n".join(toc) + '</div>'

html_out = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
            f'<title>やっているのに、伸びない。</title><style>{CSS}</style></head><body>'
            + cover + tochtml + "\n".join(book) + '</body></html>')
os.makedirs("build", exist_ok=True)
open("build/原稿_横組み.html", "w", encoding="utf-8").write(html_out)
subprocess.run(["/usr/bin/google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
  "--no-pdf-header-footer", "--print-to-pdf=build/原稿_横組み.pdf",
  "file://" + os.path.abspath("build/原稿_横組み.html")], check=True, capture_output=True)
print(f"項目 {nitem}　→ build/原稿_横組み.pdf")
