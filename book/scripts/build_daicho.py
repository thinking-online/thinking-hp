# -*- coding: utf-8 -*-
"""62項目の中身を1枚ずつ見える化。book/ で実行 → build/コンテンツ台帳.pdf"""
import re, html, os, subprocess, json
NAVY, GRAY = "#15467E", "#8a8a8a"
def esc(s): return html.escape(s, quote=False)

MAP=[("戦略","第3章","戦略編"),("計画","第4章","計画編"),("授業","第5章","授業編"),
     ("暗記","第6章","暗記編"),("演習","第7章","演習編"),("復習","第8章","復習編"),
     ("集中","第9章","集中編"),("モチベ","第10章","モチベ編"),("本番","終章","本番編")]
SRC=json.load(open("/tmp/claude-0/-home-user-thinking-hp/f9344ade-049a-53cf-a8a8-bafe881b2958/scratchpad/src.json"))
LAB={"未執筆_前半.md":"新","未執筆_後半.md":"新","09_1日の計画をtodoリストで立てて終わる.md":"新",
 "DaiGo由来5本.md":"D",
 "14_部活.md":"追","24_なぜそうなる.md":"追","59_時間を記録して満足する.md":"感",
 "60_他人と比べて落ち込む.md":"感","61_できないで終わらせる.md":"感"}
SLB={"新":"僕が今回書いた","追":"必要と判断して追加","感":"感想データから",
 "D":"DaiGo読解から追加","既":"著者の既存原稿"}

gen=open("manuscript/原稿_最新版.md",encoding="utf-8").read()
P=re.split(r'^## (\d{2})　(.+)$', gen, flags=re.M)
D={}
for i in range(1,len(P),3):
    n,ti,b=P[i],P[i+1].strip(),P[i+2]
    hs=[h.strip() for h in re.findall(r'^### (.+)$', b, re.M)]
    steps=[h for h in hs if re.match(r'^[0-9１-９]', h)]
    pair=any("伸びない" in h for h in hs) and any("頭のいい" in h for h in hs)
    fork="違いは、1か所" in b or "違いは1か所" in b
    nums=sorted(set(re.findall(r'\d+(?:\.\d+)?(?:秒|分|回|語|問|個|時間|ページ|日|週間|点|%|割|本|冊|枚)', b)),
                key=lambda s:(len(s),s))
    m=re.search(r'^### これをやると、何が残るか\s*\n+(.+?)(?=\n### |\n## |\Z)', b, re.S|re.M) \
      or re.search(r'^## これをやると、何が残るか\s*\n+(.+?)(?=\n## |\Z)', b, re.S|re.M)
    rest=""
    if m:
        for ln in m.group(1).split("\n"):
            ln=ln.strip().strip("`")
            if ln and not ln.startswith("#"): rest=ln; break
    m2=re.search(r'今日やること\s*(.+?)(?=\n\n|\Z)', b, re.S)
    today=" ".join(m2.group(1).split())[:60] if m2 else ""
    D[n]={"t":ti,"steps":steps,"pair":pair,"fork":fork,"nums":nums,
          "rest":rest[:70],"today":today,"z":len(re.sub(r'\s','',b))}

plan=open("manuscript/企画書/現行案.md",encoding="utf-8").read()
sec=plan.split("# 7 70項目")[1].split("# 8 1週間")[0]
chs,cur=[],None
for line in sec.split("\n"):
    m=re.match(r'^## (.+?)\s+(\d+)本\s*$',line)
    if m: cur={"k":re.split(r'[\s　]{2,}',m.group(1).strip())[0],"items":[]}; chs.append(cur); continue
    m=re.match(r'^(\d{2})　(.*?)(?:\s+(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力))?\s*$',line.rstrip())
    if m and cur: cur["items"].append({"n":m.group(1),"w":m.group(3) or "","x":"","o":"",
        "thick":"★厚く書く" in line,"new":"★新規" in line}); continue
    m=re.match(r'^\s+(×|○)「(.+)」\s*$',line)
    if m and cur and cur["items"]: cur["items"][-1]["x" if m.group(1)=="×" else "o"]=m.group(2)
by={c["k"]:c for c in chs}

cards=['<div class="lb">コンテンツ台帳　70項目の中身</div>',
 '<div class="leg">各項目の　番号・タイトル・武器・出どころ・字数　／　×と○　／　やり方の手順　／'
 '　使っている数字　／　残るもの。<span class="bp">対</span>＝頭のなかが対で入っている　'
 '<span class="bf">分</span>＝分岐点の1語を抜き出している　''<span class="bn">新</span>＝DaiGo本の読解を踏まえて今回追加</div>']
for k,no,name in MAP:
    c=by[k]
    cards.append(f'<div class="ch"><span class="cn">{no}</span>{name}'
                 f'<span class="cc">{len(c["items"])}本</span></div>')
    for it in c["items"]:
        d=D[it["n"]]; sl=LAB.get(SRC.get(it["n"],""),"既")
        badge=('<span class="bp">対</span>' if d["pair"] else '<span class="bx">対なし</span>')
        if it.get("new"): badge='<span class="bn">新</span>'+badge
        if d["fork"]: badge+='<span class="bf">分</span>'
        st = "　".join(re.sub(r'^[0-9１-９]+[　 ]*','',s) for s in d["steps"][:4]) or "―"
        nm = "　".join(d["nums"][:9]) or "―"
        cards.append(f'''<div class="it">
<div class="hd"><span class="n">{it["n"]}</span><span class="tt">{esc(d["t"])}</span>
{'<span class="star">★</span>' if it["thick"] else ''}{badge}
<span class="meta">{it["w"]}　／　{SLB[sl]}　／　{d["z"]:,}字</span></div>
<div class="xo"><span class="x">×　{esc(it["x"])}</span><span class="o">○　{esc(it["o"])}</span></div>
<table class="dt"><tr><td class="k">やり方</td><td>{esc(st)}</td></tr>
<tr><td class="k">数字</td><td class="nm">{esc(nm)}</td></tr>
<tr><td class="k">残るもの</td><td>{esc(d["rest"]) or "―"}</td></tr></table></div>''')

CSS=f"""
@page{{size:A4;margin:15mm 16mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:8.6pt;color:#111;line-height:1.7}}
.lb{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;color:{GRAY};letter-spacing:.2em;
 border-bottom:2px solid {NAVY};padding-bottom:2.5mm;margin-bottom:3mm}}
.leg{{font-size:7.6pt;color:#777;margin-bottom:5mm;line-height:1.8}}
.ch{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;color:{NAVY};
 background:#eef3f9;border-left:3px solid {NAVY};padding:2.2mm 4mm;margin:5mm 0 3mm;
 page-break-after:avoid}}
.ch .cn{{margin-right:3mm}} .ch .cc{{float:right;font-size:7.5pt;color:{GRAY};font-weight:400}}
.it{{border-bottom:1px solid #e8e8e8;padding:2.4mm 0;page-break-inside:avoid}}
.hd{{line-height:1.5}}
.hd .n{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{NAVY};
 margin-right:2.5mm}}
.hd .tt{{font-size:9.6pt;font-weight:600}}
.hd .star{{color:#b8860b;font-size:7.5pt;margin-left:2mm}}
.hd .meta{{float:right;font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:{GRAY}}}
.bp,.bf,.bx{{font-family:"Noto Sans CJK JP",sans-serif;font-size:6.6pt;padding:.3mm 1.4mm;
 border-radius:1.5mm;margin-left:2mm;vertical-align:1px}}
.bp{{background:#e7f1e9;color:#1a7f37}} .bf{{background:#fdf2dc;color:#8a6500}}
.bx{{background:#fbe9e7;color:#c0392b}}
.bn{{background:#e8e4f3;color:#5b3fa8;font-family:"Noto Sans CJK JP",sans-serif;font-size:6.6pt;padding:.3mm 1.4mm;border-radius:1.5mm;margin-left:2mm;vertical-align:1px}}
.xo{{margin:1.2mm 0 1.6mm 8mm;font-size:8.2pt}}
.xo .x{{color:#777;margin-right:6mm}} .xo .o{{color:{NAVY}}}
table.dt{{margin-left:8mm;border-collapse:collapse;width:calc(100% - 8mm)}}
table.dt td{{padding:.5mm 0;font-size:7.8pt;vertical-align:top;line-height:1.65}}
table.dt .k{{font-family:"Noto Sans CJK JP",sans-serif;color:{GRAY};width:16mm;white-space:nowrap}}
table.dt .nm{{font-family:"Noto Sans CJK JP",sans-serif;color:{NAVY}}}
"""
out=('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>コンテンツ台帳</title>'
 f'<style>{CSS}</style></head><body>'+"\n".join(cards)+'</body></html>')
os.makedirs("build",exist_ok=True)
open("build/コンテンツ台帳.html","w",encoding="utf-8").write(out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
 "--no-pdf-header-footer","--print-to-pdf=build/コンテンツ台帳.pdf",
 "file://"+os.path.abspath("build/コンテンツ台帳.html")],check=True,capture_output=True)
print("対",sum(1 for d in D.values() if d["pair"]),"／分岐点",sum(1 for d in D.values() if d["fork"]))
