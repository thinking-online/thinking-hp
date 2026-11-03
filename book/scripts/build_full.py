# -*- coding: utf-8 -*-
"""全原稿を1本のPDFに。book/ で実行。出力 build/全原稿.html"""
import html, re, io, os

def esc(s): return html.escape(s, quote=False)

def md(text):
    out, lines = [], text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i])); i += 1
            i += 1
            out.append('<pre class="blk">' + "\n".join(buf) + "</pre>"); continue
        if re.match(r'^\s*---\s*$', l):
            out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            lv, t = len(m.group(1)), m.group(2)
            if lv == 1:
                out.append(f'<h1 class="pb">{esc(t)}</h1>')
            else:
                out.append(f'<h{lv}>{esc(t)}</h{lv}>')
            i += 1; continue
        if l.startswith("|") and i + 1 < n and set(lines[i+1].replace("|","").strip()) <= set("-: "):
            head = [c.strip() for c in l.strip("|").split("|")]; i += 2; rows = []
            while i < n and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            t = "<table><tr>" + "".join(f"<th>{esc(c)}</th>" for c in head) + "</tr>"
            for r in rows: t += "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</table>"); continue
        if not l.strip(): i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4})\s|^\s*---\s*$|^\|', lines[i]) \
              and not lines[i].startswith("```"):
            buf.append(esc(lines[i].rstrip())); i += 1
        cls = ' class="ind"' if buf and buf[0].startswith("　") else ""
        out.append(f'<p{cls}>' + "<br>".join(buf) + "</p>")
    return "\n".join(out)

def read(p): return io.open(p, encoding="utf-8").read()
def strip_h1(s): return re.sub(r'^#\s+.*\n', '', s, count=1)

FILES = [
    ("目次",            "manuscript/企画書/目次_第5版.md", True),
    ("はじめに",        "manuscript/冒頭メッセージ.md", True),
    (None,              "manuscript/序章_v5.md", False),
    (None,              "manuscript/第1章_v5.md", False),
    (None,              "manuscript/本文/第2章_戦略編.md", False),
    (None,              "manuscript/本文/第3章_計画編.md", False),
    (None,              "manuscript/本文/第4章_インプット編.md", False),
    (None,              "manuscript/本文/第5章_暗記編.md", False),
    (None,              "manuscript/本文/第6章_演習編.md", False),
    (None,              "manuscript/本文/第7章_復習編.md", False),
    (None,              "manuscript/本文/第8章_本番編.md", False),
    (None,              "manuscript/本文/第9章_継続編.md", False),
    (None,              "manuscript/本文/終章_5教科.md", False),
    (None,              "manuscript/本文/巻末.md", False),
]

CSS = """
@page { size: A4 portrait; margin: 18mm 20mm 20mm 20mm; }
body { font-family:"Hiragino Sans","Noto Sans CJK JP","Yu Gothic",sans-serif;
       font-size:10pt; line-height:1.85; color:#111; margin:0; }
.cover { height:248mm; display:flex; flex-direction:column; justify-content:center; }
.cover .t { font-size:23pt; font-weight:700; line-height:1.5; }
.cover .s { font-size:11pt; color:#555; margin-top:14mm; line-height:2.1; }
h1.pb { break-before: page; font-size:16pt; margin:0 0 7mm; padding-bottom:2.5mm;
        border-bottom:2.5px solid #111; font-weight:700; }
h2 { font-size:12.2pt; margin:9mm 0 3mm; font-weight:700;
     border-left:4px solid #111; padding-left:3mm; }
h3 { font-size:10.6pt; margin:6mm 0 2mm; font-weight:700; color:#333; }
h4 { font-size:10pt; margin:4mm 0 1.5mm; font-weight:700; color:#444; }
p { margin:0 0 3.2mm; }
p.ind { white-space:pre-wrap; }
hr { border:0; border-top:1px solid #e0e0e0; margin:6mm 0; }
pre.blk { font-family:"Hiragino Sans","Noto Sans CJK JP",monospace; font-size:9pt;
      line-height:1.75; background:#f6f6f4; border:1px solid #e3e3df;
      padding:3.5mm 4.5mm; margin:0 0 4mm; white-space:pre-wrap; break-inside:avoid-page; }
table { border-collapse:collapse; margin:0 0 4mm; font-size:9pt; width:100%; }
th,td { border:1px solid #ccc; padding:1.6mm 2.6mm; text-align:left; vertical-align:top; }
th { background:#f2f2ef; font-weight:700; }
"""

parts = ['<meta charset="utf-8"><title>全原稿</title><style>%s</style>' % CSS]
parts.append("""<div class="cover">
<div class="t">頭のいい人が勉強で、<br>絶対にやらないこと</div>
<div class="s">全原稿　第1稿<br>2026年11月3日　朝倉 徹大<br><br>
目次／はじめに／序章／第1章／50項目（第2〜9章）／終章／巻末</div></div>""")

total = 0
for title, path, add_title in FILES:
    s = read(path)
    total += len(s)
    if add_title:
        s = strip_h1(s)
        parts.append(f'<h1 class="pb">{esc(title)}</h1>')
        if title == "はじめに":
            s = s.replace("著者執筆。原文のまま保存。\n", "")
    parts.append(md(s))

os.makedirs("build", exist_ok=True)
io.open("build/全原稿.html","w",encoding="utf-8").write("\n".join(parts))
print("総字数", total)
