# -*- coding: utf-8 -*-
"""目次をPDFにする。book/ で実行 → build/目次.pdf"""
import re, html, os, subprocess

NAVY, GRAY = "#15467E", "#8a8a8a"
RATE = 520
def esc(s): return html.escape(s, quote=False)

MAP = [("基本の基本","第1章","基本の基本編"), ("戦略","第2章","戦略編"), ("計画","第3章","計画編"),
       ("授業","第4章","授業編"), ("暗記","第5章","暗記編"), ("演習","第6章","演習編"),
       ("復習","第7章","復習編"), ("集中","第8章","集中編"), ("モチベ","第9章","モチベ編"),
       ("本番","終章","本番編")]

gen = open("manuscript/原稿_最新版.md", encoding="utf-8").read()
_p = re.split(r'^## (\d{2})　.+$', gen, flags=re.M)
ZI = {_p[i]: len(re.sub(r'\s', '', _p[i+1])) for i in range(1, len(_p), 2)}

plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 75項目")[1].split("# 8 1週間")[0]
chs, cur = [], None
for line in sec.split("\n"):
    m = re.match(r'^## (.+?)\s+(\d+)本\s*$', line)
    if m:
        cur = {"old": re.split(r'[\s　]{2,}', m.group(1).strip())[0], "items": []}
        chs.append(cur); continue
    m = re.match(r'^(\d{2})　(.*?)(?:\s+(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力))?\s*$',
                 line.rstrip())
    if m and cur:
        cur["items"].append({"n": m.group(1), "t": m.group(2).replace("★厚く書く","").replace("★新規","").strip(),
                             "x": "", "o": "", "thick": "★厚く書く" in line, "new": "★新規" in line}); continue
    m = re.match(r'^\s+(×|○)「(.+)」\s*$', line)
    if m and cur and cur["items"]:
        cur["items"][-1]["x" if m.group(1)=="×" else "o"] = m.group(2)
by = {c["old"]: c for c in chs}

# 巻頭と序章は会話体で改行が多いため、本文より少ないレートで数える
RATE2 = 420
_ws = re.compile(r'\s')
KAN_ZI = len(_ws.sub('', open("manuscript/巻頭ページ.md", encoding="utf-8").read()))
JO_ZI  = len(_ws.sub('', open("manuscript/序章_v6_完全版.md", encoding="utf-8").read()))
KAN_PG = max(1, round(KAN_ZI / RATE2))
JO_PG  = max(1, round(JO_ZI  / RATE2))
FP = (KAN_PG,)
rows, tot = [], 0
for old, no, name in MAP:
    c = by[old]; n = len(c["items"])
    pg = max(1, round(sum(ZI.get(i["n"],0) for i in c["items"])/RATE)) + 2; tot += pg
    rows.append((no, name, n, pg))
TOTAL = sum(FP) + JO_PG + tot + 28

front = f'''<div class="sheet">
<div class="ttl">やっているのに、伸びない。</div>
<div class="sub">頭のいい人が勉強で、絶対にやらない75のこと　／　朝倉 徹大</div>
<div class="lead">目次　2026年11月6日</div>
<table class="big">
<tr class="hd"><td></td><td></td><td class="c3">項目</td><td class="c4">ページ数</td></tr>
<tr class="fr"><td class="c1">巻頭</td><td class="c2">10秒だけ、付き合ってください</td>
  <td class="c3"></td><td class="c4">{FP[0]}</td></tr>
<tr class="sb"><td></td><td colspan="3">11個の数字　／　正しいのに変われない　／　見えないから　／　偏差値42から早稲田　／　全部書く、隠すところは1つもない</td></tr>
<tr class="fr"><td class="c1">序章</td><td class="c2">「自分に合った勉強法」を、探すのをやめる</td>
  <td class="c3"></td><td class="c4">{JO_PG}</td></tr>
<tr class="sb"><td></td><td colspan="3">それ、誰から教わりましたか　／　人は、やったことのないものを選べない　／　2000人が、全員同じ4つ　／　×やりやすかったか　○出せたか　／　探している間は、やらなくていい</td></tr>
'''
for no, name, n, pg in rows:
    front += (f'<tr class="mr"><td class="c1">{no}</td>'
              f'<td class="c2"><span class="pre">頭のいい人が、絶対にやらないこと</span>'
              f'<span class="hen">{name}</span></td>'
              f'<td class="c3">{n}本</td><td class="c4">{pg}</td></tr>\n')
front += f'''<tr class="fr"><td class="c1">巻末</td>
  <td class="c2">手持ちカード ／ まず、この6つ ／ 悩み別の引き方</td>
  <td class="c3"></td><td class="c4">28</td></tr>
<tr class="sb"><td></td><td colspan="3">5教科で、どう使うか ／ 保護者の方へ ／ おわりに ／ 参考文献</td></tr>
<tr class="tot"><td></td><td colspan="2">合計</td><td class="tv">約 {TOTAL} ページ　四六判</td></tr>
</table>
<div class="note">章の名前が8回くり返される。目次を上から読むだけで、
表紙の約束が8回、目に入る。<br>
ページは実字数から計算（本文は1ページ520字、巻頭と序章は改行が多いので420字。四六判9.5pt縦組み、見出しと×／○の囲みこみ）。<br>
6つの力は目次に出さない。第1章の03〜08で1つずつ、各項目の右肩、章扉、巻末カードの4か所に置く。</div>
</div>'''

detail = ['<div class="sheet2"><div class="dh">目次　項目</div>']
for old, no, name in MAP:
    c = by[old]
    detail.append(f'<div class="ch"><span class="cn">{no}</span>'
                  f'頭のいい人が、絶対にやらないこと　<span class="hen2">{name}</span>'
                  f'<span class="cc">{len(c["items"])}本</span></div>')
    for k_i, it in enumerate(c["items"]):
        if c.get("secs",{}).get(k_i):
            detail.append(f'<div class="sec2">{esc(c["secs"][k_i])}</div>')
        st = '<span class="star">★</span>' if it["thick"] else ''
        detail.append(f'''<div class="it"><div class="t"><span class="n">{it["n"]}</span>
{esc(it["t"])}{st}</div>
<div class="x">×　{esc(it["x"])}</div><div class="o">○　{esc(it["o"])}</div></div>''')
detail.append('<div class="note2">★＝厚く書く項目（4ページ）。ほかは約3ページ。</div></div>')

CSS = f"""
@page {{ size:A4; margin:18mm 20mm; }}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;color:#111;font-size:10pt}}
.sheet{{page-break-after:always}}
.ttl{{font-size:19pt;font-weight:700;letter-spacing:.03em}}
.sub{{font-size:9.5pt;color:#555;margin-top:3mm}}
.lead{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;color:{GRAY};
  margin:9mm 0 4mm;letter-spacing:.2em;border-bottom:2px solid {NAVY};padding-bottom:2.5mm}}
table.big{{width:100%;border-collapse:collapse}}
table.big td{{padding:2.6mm 1mm;vertical-align:baseline}}
.fr td,.mr td{{border-bottom:1px solid #e6e6e6}}
.c1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;
  color:{NAVY};width:17mm;white-space:nowrap}}
.c2{{font-size:10.5pt}}
.c3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8pt;color:{GRAY};
  width:12mm;text-align:right;white-space:nowrap}}
.c4{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;color:#444;
  width:20mm;text-align:right;white-space:nowrap}}
.mr .pre{{color:#666;font-size:9.5pt}}
.mr .hen{{color:{NAVY};font-weight:700;font-size:11pt;margin-left:1.5mm}}
.hd td{{font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:#aaa;
  letter-spacing:.12em;padding:0 1mm 1.5mm;border:none;text-align:right}}
.sb td{{font-size:8.5pt;color:#888;padding:0 1mm 3mm;border:none}}
.tot td{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;
  color:{NAVY};border-top:2px solid {NAVY};padding-top:3.5mm;text-align:right}}
.tot td:nth-child(2){{text-align:left}}
.tot .tv{{white-space:nowrap;width:46mm}}
.note{{font-size:8.5pt;color:#777;line-height:2;margin-top:9mm;
  border-top:1px dotted #ccc;padding-top:4mm}}

.dh{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;color:{GRAY};
  letter-spacing:.2em;border-bottom:2px solid {NAVY};padding-bottom:2.5mm;margin-bottom:6mm}}
.ch{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5pt;color:#555;
  background:#eef3f9;border-left:3px solid {NAVY};padding:3mm 4mm;
  margin:7mm 0 4mm;page-break-after:avoid}}
.ch .cn{{color:{NAVY};font-weight:700;margin-right:3mm}}
.ch .hen2{{color:{NAVY};font-weight:700;font-size:11pt}}
.ch .cc{{float:right;font-size:8pt;color:{GRAY}}}
.sec2{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8pt;color:{NAVY};letter-spacing:.14em;margin:4.5mm 0 2.5mm;padding-left:1mm;border-left:2px solid {NAVY};page-break-after:avoid}}
.it{{margin-bottom:3.6mm;page-break-inside:avoid}}
.it .t{{font-size:10.5pt;line-height:1.55}}
.it .n{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;
  color:{NAVY};margin-right:3mm}}
.it .star{{color:#b8860b;font-size:8pt;margin-left:2mm}}
.it .x{{font-size:9pt;color:#666;margin:.6mm 0 0 9mm}}
.it .o{{font-size:9pt;color:{NAVY};margin-left:9mm}}
.note2{{font-size:8.5pt;color:#777;margin-top:8mm;border-top:1px dotted #ccc;padding-top:4mm}}
"""
out = ('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>目次</title>'
       f'<style>{CSS}</style></head><body>' + front + "\n".join(detail) + '</body></html>')
os.makedirs("build", exist_ok=True)
open("build/目次.html","w",encoding="utf-8").write(out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
  "--no-pdf-header-footer","--print-to-pdf=build/目次.pdf",
  "file://"+os.path.abspath("build/目次.html")], check=True, capture_output=True)
print(f"章 {len(rows)}　項目 {sum(r[2] for r in rows)}　合計 {TOTAL}ページ")
