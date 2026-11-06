# -*- coding: utf-8 -*-
"""幹と構成の確定版をPDFに。book/ で実行 → build/幹と構成.pdf"""
import re, html, os, subprocess
NAVY, GRAY, RATE = "#15467E", "#8a8a8a", 520
def esc(s): return html.escape(s, quote=False)

MAP = [("基本の基本","第1章","基本の基本編"), ("戦略","第2章","戦略編"), ("計画","第3章","計画編"),
       ("授業","第4章","授業編"), ("暗記","第5章","暗記編"), ("演習","第6章","演習編"),
       ("復習","第7章","復習編"), ("集中","第8章","集中編"), ("モチベ","第9章","モチベ編"),
       ("本番","終章","本番編")]

gen = open("manuscript/原稿_最新版.md", encoding="utf-8").read()
_p = re.split(r'^## (\d{2})　.+$', gen, flags=re.M)
ZI = {_p[i]: len(re.sub(r'\s','',_p[i+1])) for i in range(1,len(_p),2)}
HEAD = {_p[i]: ("頭のなか" in _p[i+1] or "頭の中" in _p[i+1]) for i in range(1,len(_p),2)}
DONE = {_p[i] for i in range(1,len(_p),2)
        if re.search(r'###?\s*伸びない人', _p[i+1]) and re.search(r'###?\s*頭のいい人', _p[i+1])}
THINK = {"入れる力","つなげる力","出す力","なおす力"}

plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 75項目")[1].split("# 8 1週間")[0]
chs, cur = [], None
for line in sec.split("\n"):
    m = re.match(r'^## (.+?)\s+(\d+)本\s*$', line)
    if m:
        cur = {"k": re.split(r'[\s　]{2,}', m.group(1).strip())[0], "items": []}
        chs.append(cur); continue
    m = re.match(r'^(\d{2})　(.*?)(?:\s+(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力))?\s*$', line.rstrip())
    if m and cur:
        cur["items"].append({"n":m.group(1),"t":m.group(2).replace("★厚く書く","").replace("★新規","").strip(),
                             "w":m.group(3) or "","x":"","o":"","thick":"★厚く書く" in line,"new":"★新規" in line}); continue
    m = re.match(r'^\s+(×|○)「(.+)」\s*$', line)
    if m and cur and cur["items"]:
        cur["items"][-1]["x" if m.group(1)=="×" else "o"] = m.group(2)
by = {c["k"]: c for c in chs}

FP = (11, 9, 11, 12)          # はじめに／序章／第1章／第2章
rows, tot = [], 0
for k, no, name in MAP:
    c = by[k]; n = len(c["items"])
    pg = max(1, round(sum(ZI.get(i["n"],0) for i in c["items"])/RATE)) + 2
    tot += pg; rows.append((no, name, n, pg))
TOTAL = sum(FP) + tot + 28     # 巻末24＋大人の方へ4

VOICE = "  ".join(f'<span class="wn">{w}</span><span class="wk">{k}</span>'
    for w,k in [("選ぶ力","これ、出るの？"),("入れる力","いま、閉じて出せる？"),
                ("つなげる力","これ、前にどこで見た？"),("出す力","それ、テストでもできる？"),
                ("なおす力","どこで、止まった？"),("続ける力","次の1個目は？")])

p1 = f'''<div class="sh">
<div class="t" style="font-size:17pt">やっているのに、伸びない。</div>
<div class="s">頭のいい人が勉強で、絶対にやらない75のこと　／　朝倉 徹大</div>
<div class="lb">幹　2026年11月6日　確定版</div>

<div class="sec">読者</div>
<div class="bd">やっているのに伸びない中高生と、その保護者。社会人は切る。</div>

<div class="sec">約束</div>
<div class="bd">頭のなかは、外から見えない。だから真似できない。それを見える化する。</div>

<div class="sec">幹　62項目を貫く1行</div>
<div class="kan">その場の自分を、信用しない。</div>
<div class="bd sm">62個の×を全部並べると、サボっている人の言葉が1つもない。全部、まじめな人が自分に言っている言葉で、
その場では正しく聞こえる。そして全部、確かめていない。<br>
「わかった」も「大事そう」も「やる気がない」も、確かめていない その場の感覚。6つの武器は、それを確かめる6つの方法。</div>

<div class="sec">論理</div>
<pre class="logic">穴の空いたバケツ　→　もっと注ぐな、穴をふさげ
　　　↓
順番がある　　　　①やめる　　②知る　　③量
　　　↓
結果 ＝ 戦略 × やり方 × 量　　かけ算だから、1つが0なら0
　　　　<span class="n">戦略＝①やめるの、やめる対象を決めること</span>
　　　↓
「やり方」は1語だと手が出ない　→　4つに割る　→　6つの武器
　　　↓
62の場面で、その6つを使う</pre>

<div class="sec">6つの武器</div>
<div class="w6">{VOICE}</div>
<div class="bd sm">選ぶ力＝戦略　／　入れる・つなげる・出す・なおす＝やり方　／　続ける力＝量　　11本 ／ 33本 ／ 18本 ＝ 62</div>
</div>

<div class="sh">
<div class="lb">どこまで書くか</div>
<div class="sec">深さ</div>
<table class="lv">
<tr><td class="l">レベル1</td><td class="ln">原則</td><td class="le">アクティブリコールが効く</td><td class="lw">科学の本</td></tr>
<tr><td class="l">レベル2</td><td class="ln">行動</td><td class="le">寝る前に復習しろ</td><td class="lw">多くの勉強法本</td></tr>
<tr><td class="l">レベル3</td><td class="ln">手順</td><td class="le">教科書を閉じて、白紙に3つ書く</td><td class="lw">いい勉強法本</td></tr>
<tr class="hit"><td class="l">レベル4</td><td class="ln">頭の動かし方</td><td class="le">白紙を見て何も出ないとき、何を先に探すか</td><td class="lw">この本</td></tr>
</table>
<div class="bd sm">調べた類書5冊は、2か3で止まっていた。3まで行く本はある。4はない。</div>

<div class="sec">分岐点　この本の必殺技</div>
<pre class="logic">1　同じ場面で、2つの頭の中を並べる　　　伸びない人　／　頭のいい人
2　時間を入れる　　　　　　　　　　　　 3秒　／　40秒
3　<span class="em">分岐点の1語を取り出す</span>　　　　　　読者が持ち帰るのは、ここだけ</pre>
<div class="bd sm">2つの思考を並べるだけなら類書もやる。どこで枝分かれしたかを1語に絞るのは見たことがない。
テスト2週間前の夜に思い出せるのは、手順ではなく1語。</div>

<div class="sec">試作した5つ</div>
<table class="fk">
<tr><td class="fn">37</td><td class="ft">「ここ、全部わからないです」と言う</td><td class="fw">どこまで？</td></tr>
<tr><td class="fn">20</td><td class="ft">単語を、1語10回ずつ書いて覚える</td><td class="fw">何秒で出た？</td></tr>
<tr><td class="fn">30</td><td class="ft">初めて見る問題を、ゼロから考え続ける</td><td class="fw">全部が初めて？　組み合わせだけ？</td></tr>
<tr><td class="fn">52</td><td class="ft">やる気が出るのを待つ</td><td class="fw">で、1個目は？</td></tr>
<tr><td class="fn">61</td><td class="ft">緊張したときに、落ち着こうとする</td><td class="fw">来てる</td></tr>
</table>

<div class="sec">形式</div>
<div class="bd">全項目 ×／○ の二項対立。1項目3ページ。右肩に武器タグ1つ。<br>
全項目に「頭のなか」を1節。<span class="chk">現在 54／62</span><br>
頭を動かす項目に、分岐点を1語。<span class="chk">現在 1／約40</span></div>

<div class="sec">物理</div>
<div class="bd">四六判　2色刷り　約{TOTAL}ページ　1,700円台<span class="chk">　←　価格は学研に確認</span></div>
</div>'''

trs = "".join(f'<tr class="mr"><td class="c1">{no}</td>'
   f'<td class="c2"><span class="pre">頭のいい人が、絶対にやらないこと</span>'
   f'<span class="hen">{name}</span></td><td class="c3">{n}本</td><td class="c4">{pg}</td></tr>'
   for no,name,n,pg in rows)
p2 = f'''<div class="sh">
<div class="lb">構成</div>
<table class="big">
<tr class="fr"><td class="c1">はじめに</td><td class="c2">この本は、10秒で始まります</td><td class="c3"></td><td class="c4">{FP[0]}</td></tr>
<tr class="sb"><td></td><td colspan="3">11個の数字　／　ちゃんと勉強してるの？　／　あの子はなぜ　／　バケツ　／　①やめる②知る③量　／　頭のなかは映らない</td></tr>
<tr class="fr"><td class="c1">序章</td><td class="c2">「自分に合った勉強法」を、探すのをやめる</td><td class="c3"></td><td class="c4">{FP[1]}</td></tr>
<tr class="sb"><td></td><td colspan="3">やめる4つ　／　人は経験したことがないものを選べない　／　探している間は、やらなくていい</td></tr>
<tr class="fr"><td class="c1">第1章</td><td class="c2">結果 ＝ 戦略 × やり方 × 量</td><td class="c3"></td><td class="c4">{FP[2]}</td></tr>
<tr class="sb"><td></td><td colspan="3">1つが0なら0　／　類書が埋めているのはまん中の1列だけ　／　勝ち切れ　／　あなたは、どこが0ですか</td></tr>
<tr class="fr"><td class="c1">第2章</td><td class="c2">頭のいい人が<span class="hen">持っている</span>、6つの武器</td><td class="c3">6つ</td><td class="c4">{FP[3]}</td></tr>
<tr class="sb"><td></td><td colspan="3">式を分解しただけ　／　1問につき、だいたい2つ　／　まず、この6つ</td></tr>
{trs}
<tr class="fr"><td class="c1">巻末</td><td class="c2">手持ちカード ／ まず、この6つ ／ 悩み別の引き方 ／ 5教科で、どう使うか</td><td class="c3"></td><td class="c4">24</td></tr>
<tr class="fr"><td class="c1"></td><td class="c2">保護者の方へ ／ 大人の方へ（資格と仕事に、6つをどう使うか） ／ おわりに</td><td class="c3"></td><td class="c4">4</td></tr>
<tr class="tot"><td></td><td colspan="2">合計</td><td class="tv">約 {TOTAL} ページ　四六判</td></tr>
</table>
<div class="nt">「頭のいい人が、絶対にやらないこと」が目次に9回出る。表紙の約束が、目次を上から読むだけで9回入る。<br>
ページは1ページ520字で計算。</div>
</div>'''

det = ['<div class="sh2"><div class="lb">62項目</div>']
for k, no, name in MAP:
    c = by[k]
    det.append(f'<div class="ch"><span class="cn">{no}</span>頭のいい人が、絶対にやらないこと　'
               f'<span class="hen2">{name}</span><span class="cc">{len(c["items"])}本</span></div>')
    for it in c["items"]:
        st = '<span class="star">★</span>' if it["thick"] else ''
        hd = '' if HEAD.get(it["n"], True) else '<span class="warn">頭のなか 未</span>'
        if it["n"] in DONE: hd += '<span class="done">分岐点 済</span>'
        elif it["w"] in THINK: hd += '<span class="need">分岐点 要</span>'
        det.append(f'<div class="it"><div class="t"><span class="n">{it["n"]}</span>{esc(it["t"])}{st}'
                   f'<span class="wg">{it["w"]}</span>{hd}</div>'
                   f'<div class="x">×　{esc(it["x"])}</div><div class="o">○　{esc(it["o"])}</div></div>')
det.append('<div class="nt">★＝厚く書く項目。<span class="warn">頭のなか 未</span>＝約束の節がまだない項目。'
 '<span class="need">分岐点 要</span>＝入れる・つなげる・出す・なおす の33本。'
 'ここに選ぶ力と続ける力から頭を動かすものを足して、計40本前後になる。'
 '物理と段取りの項目（スマホを別の部屋に置く、寝る時間を削らない等）には分岐点がないので入れない。</div></div>')

CSS = f"""
@page{{size:A4;margin:17mm 20mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Noto Serif CJK JP",serif;font-size:10pt;color:#111}}
.sh,.sh2{{page-break-after:always}}
.sh2{{page-break-after:auto}}
.t{{font-size:19pt;font-weight:700}}
.s{{font-size:9.5pt;color:#555;margin-top:3mm}}
.lb{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;color:{GRAY};letter-spacing:.2em;
 margin:6mm 0 4mm;border-bottom:2px solid {NAVY};padding-bottom:2.5mm}}
.sec{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{NAVY};
 margin:4.4mm 0 1.6mm;letter-spacing:.1em}}
.bd{{font-size:10pt;line-height:1.8}}
.bd.sm{{font-size:8.5pt;color:#666;margin-top:2.5mm}}
.chk{{color:#b8860b;font-size:8.5pt}}
pre.logic{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.6pt;line-height:1.75;
 background:#eef3f9;border-left:3px solid {NAVY};padding:3.2mm 5mm;white-space:pre-wrap}}
pre.logic .n{{color:{GRAY};font-size:8pt}}
.w6{{display:grid;grid-template-columns:1fr 1fr;gap:1mm 5mm;margin-top:1mm}}
.wn{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{NAVY};
 display:inline-block;width:20mm}}
.wk{{font-size:9pt}}
table.big{{width:100%;border-collapse:collapse}}
table.big td{{padding:2.4mm 1mm;vertical-align:baseline}}
.fr td,.mr td{{border-bottom:1px solid #e6e6e6}}
.c1{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{NAVY};width:19mm;white-space:nowrap}}
.c2{{font-size:10pt}}
.c3{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8pt;color:{GRAY};width:12mm;text-align:right;white-space:nowrap}}
.c4{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;color:#444;width:18mm;text-align:right;white-space:nowrap}}
.mr .pre{{color:#666;font-size:9.5pt}}
.mr .hen,.hen{{color:{NAVY};font-weight:700;font-size:10.5pt;margin-left:1.5mm}}
.sb td{{font-size:8.3pt;color:#888;padding:0 1mm 3mm;border:none}}
.tot td{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;color:{NAVY};
 border-top:2px solid {NAVY};padding-top:3.5mm;text-align:right}}
.tot td:nth-child(2){{text-align:left}} .tot .tv{{white-space:nowrap;width:46mm}}
.nt{{font-size:8.3pt;color:#777;line-height:1.95;margin-top:7mm;border-top:1px dotted #ccc;padding-top:3.5mm}}
.ch{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5pt;color:#555;background:#eef3f9;
 border-left:3px solid {NAVY};padding:2.6mm 4mm;margin:6mm 0 3.5mm;page-break-after:avoid}}
.ch .cn{{color:{NAVY};font-weight:700;margin-right:3mm}}
.ch .hen2{{color:{NAVY};font-weight:700;font-size:11pt}}
.ch .cc{{float:right;font-size:8pt;color:{GRAY}}}
.it{{margin-bottom:3.2mm;page-break-inside:avoid}}
.it .t{{font-size:10.3pt;line-height:1.5}}
.it .n{{font-family:"Noto Sans CJK JP",sans-serif;font-size:9pt;font-weight:700;color:{NAVY};margin-right:3mm}}
.it .star{{color:#b8860b;font-size:8pt;margin-left:1.5mm}}
.it .wg{{font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:{GRAY};margin-left:3mm}}
""
.it .x{{font-size:8.8pt;color:#666;margin:.5mm 0 0 9mm}}
.it .o{{font-size:8.8pt;color:{NAVY};margin-left:9mm}}
.kan{{font-family:"Noto Sans CJK JP",sans-serif;font-size:15pt;font-weight:700;color:{NAVY};
 text-align:center;border:1.5px solid {NAVY};padding:5mm;margin:1mm 0 3mm;letter-spacing:.08em}}
pre.logic .em{{color:{NAVY};font-weight:700}}
table.lv{{width:100%;border-collapse:collapse;margin-bottom:2.5mm}}
table.lv td{{padding:2.3mm 1mm;border-bottom:1px solid #e8e8e8;font-size:9.3pt;vertical-align:baseline}}
table.lv .l{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8pt;color:{GRAY};width:16mm;white-space:nowrap}}
table.lv .ln{{font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;width:26mm;white-space:nowrap}}
table.lv .le{{font-size:9.3pt}}
table.lv .lw{{font-size:8pt;color:{GRAY};text-align:right;width:30mm;white-space:nowrap}}
table.lv tr.hit td{{background:#eef3f9;border-bottom:2px solid {NAVY}}}
table.lv tr.hit .ln,table.lv tr.hit .lw{{color:{NAVY};font-weight:700}}
table.fk{{width:100%;border-collapse:collapse}}
table.fk td{{padding:2.2mm 1mm;border-bottom:1px solid #e8e8e8;vertical-align:baseline}}
table.fk .fn{{font-family:"Noto Sans CJK JP",sans-serif;font-size:8.5pt;font-weight:700;color:{NAVY};width:9mm}}
table.fk .ft{{font-size:9.5pt}}
table.fk .fw{{font-family:"Noto Sans CJK JP",sans-serif;font-size:10pt;font-weight:700;
 color:{NAVY};text-align:right;white-space:nowrap}}
.it .warn{{font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:#c0392b;margin-left:2mm}}
.it .need{{font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:#b8860b;margin-left:2mm}}
.it .done{{font-family:"Noto Sans CJK JP",sans-serif;font-size:7pt;color:#1a7f37;margin-left:2mm}}
.nt .warn{{color:#c0392b}} .nt .need{{color:#b8860b}}
"""
out=('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>幹と構成</title>'
     f'<style>{CSS}</style></head><body>'+p1+p2+"\n".join(det)+'</body></html>')
os.makedirs("build",exist_ok=True)
open("build/幹と構成.html","w",encoding="utf-8").write(out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
 "--no-pdf-header-footer","--print-to-pdf=build/幹と構成.pdf",
 "file://"+os.path.abspath("build/幹と構成.html")],check=True,capture_output=True)
print(f"章 {len(rows)}　項目 {sum(r[2] for r in rows)}　{TOTAL}ページ　"
      f"頭のなか未 {sum(1 for v in HEAD.values() if not v)}本")
