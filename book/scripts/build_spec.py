# -*- coding: utf-8 -*-
"""幹と構成の確定版をPDFに。book/ で実行 → build/制作仕様書.pdf"""
import re, html, os, subprocess
NAVY, GRAY, RATE = "#15467E", "#8a8a8a", 520
def esc(s): return html.escape(s, quote=False)

MAP = [("基本の基本","序章","基本の基本編"), ("戦略","第1章","戦略編"), ("計画","第2章","計画編"),
       ("授業","第3章","授業編"), ("暗記","第4章","暗記編"), ("演習","第5章","演習編"),
       ("復習","第6章","復習編"), ("集中","第7章","集中編"), ("モチベ","第8章","モチベ編"),
       ("本番","終章","本番編")]

gen = open("manuscript/原稿_最新版.md", encoding="utf-8").read()
_p = re.split(r'^## (\d{2})　.+$', gen, flags=re.M)
ZI = {_p[i]: len(re.sub(r'\s','',_p[i+1])) for i in range(1,len(_p),2)}
HEAD = {_p[i]: ("頭のなか" in _p[i+1] or "頭の中" in _p[i+1]) for i in range(1,len(_p),2)}
PAIR = {_p[i] for i in range(1,len(_p),2)
        if re.search(r'^### .*伸びない', _p[i+1], re.M) and re.search(r'^### .*頭のいい', _p[i+1], re.M)}
DONE = {_p[i] for i in range(1,len(_p),2) if "違いは、1か所" in _p[i+1] or "違いは1か所" in _p[i+1]}
THINK = {"入れる力","つなげる力","出す力","なおす力"}

plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 70項目")[1].split("# 8 1週間")[0]
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

FP = (6,)   # 巻頭のみ。序章以下は章として数える
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
<div class="s">頭のいい人が勉強で、絶対にやらない70のこと　／　朝倉 徹大</div>
<div class="lb">制作仕様書　2026年11月6日</div>

<div class="sec">読者</div>
<div class="bd">やっているのに伸びない中高生と、その保護者。社会人は切る。</div>

<div class="sec">約束</div>
<div class="bd">頭のなかは、外から見えない。だから真似できない。それを見える化する。</div>

<div class="sec">幹　70項目を貫く1行</div>
<div class="kan">その場の自分を、信用しない。</div>
<div class="bd sm">70個の×を全部並べると、サボっている人の言葉が1つもない。全部、まじめな人が自分に言っている言葉で、
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
67の場面で、その6つを使う</pre>

<div class="sec">6つの武器</div>
<div class="w6">{VOICE}</div>
<div class="bd sm">選ぶ力＝戦略　／　入れる・つなげる・出す・なおす＝やり方　／　続ける力＝量　　11本 ／ 36本 ／ 20本 ＋ 基本の基本3　＝　70</div>
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

<div class="sec">分岐点の例　試作した5つ</div>
<table class="fk">
<tr><td class="fn">37</td><td class="ft">「ここ、全部わからないです」と言う</td><td class="fw">どこまで？</td></tr>
<tr><td class="fn">20</td><td class="ft">単語を、1語10回ずつ書いて覚える</td><td class="fw">何秒で出た？</td></tr>
<tr><td class="fn">30</td><td class="ft">初めて見る問題を、ゼロから考え続ける</td><td class="fw">全部が初めて？　組み合わせだけ？</td></tr>
<tr><td class="fn">52</td><td class="ft">やる気が出るのを待つ</td><td class="fw">で、1個目は？</td></tr>
<tr><td class="fn">61</td><td class="ft">緊張したときに、落ち着こうとする</td><td class="fw">来てる</td></tr>
</table>

<div class="sec">形式</div>
<div class="bd">全項目 ×／○ の二項対立。1項目3ページ。右肩に武器タグ1つ。<br>
全項目に「頭のなか」を、伸びない人と頭のいい人の対で。<span class="chk">現在 54／70</span><br>
頭を動かす項目に、分岐点を1語。<span class="chk">現在 7／36</span></div>

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
<tr class="fr"><td class="c1">巻頭</td><td class="c2">10秒だけ、付き合ってください</td><td class="c3"></td><td class="c4">6</td></tr>
<tr class="sb"><td></td><td colspan="3">11個の数字　／　正しいのに変われない　／　見えないから　／　偏差値42から早稲田　／　全部書く</td></tr>
{trs}
<tr class="fr"><td class="c1">巻末</td><td class="c2">手持ちカード ／ まず、この6つ ／ 悩み別の引き方 ／ 5教科で、どう使うか</td><td class="c3"></td><td class="c4">24</td></tr>
<tr class="fr"><td class="c1"></td><td class="c2">保護者の方へ ／ 大人の方へ（資格と仕事に、6つをどう使うか） ／ おわりに</td><td class="c3"></td><td class="c4">4</td></tr>
<tr class="tot"><td></td><td colspan="2">合計</td><td class="tv">約 {TOTAL} ページ　四六判</td></tr>
</table>
<div class="nt">「頭のいい人が、絶対にやらないこと」が目次に10回出る。表紙の約束が、目次を上から読むだけで10回入る。<br>
ページは1ページ520字で計算。</div>
</div>'''


pk = '''<div class="sh">
<div class="lb">1項目の型　7つの拍</div>
<table class="lv">
<tr><td class="l">1</td><td class="ln">問い</td><td class="le">1行。読者が頭の中で答える。場面は書かない</td></tr>
<tr><td class="l">2</td><td class="ln">やらないこと</td><td class="le">行動　→　その結末</td></tr>
<tr><td class="l">3</td><td class="ln">やっていること</td><td class="le">行動　→　その結末</td></tr>
<tr><td class="l">4</td><td class="ln">説明</td><td class="le">責めない　＋　何が起きているか　＋　図1</td></tr>
<tr><td class="l">5</td><td class="ln">頭のなか</td><td class="le">伸びない人／頭のいい人。時間を入れる</td></tr>
<tr class="hit"><td class="l">6</td><td class="ln">分岐点</td><td class="le">1語。読者が持ち帰るのはこれだけ</td></tr>
<tr><td class="l">7</td><td class="ln">やり方</td><td class="le">図2　＋　手順　＋　注意　＋　残るもの</td></tr>
</table>
<div class="bd sm">1-3 守りから降ろす ／ 4-6 理解を持ち帰れる1語に変える ／ 7 1語を明日の手の動きに変える。<br>
3で終わると概念の本。7から始めると手順書。4〜6を挟むから再現できる。</div>

<div class="sec">2と3の書き方</div>
<pre class="logic">頭のいい人が、絶対にやらないこと
　　1語を、10回書く　　　　　　　→　書いた回数で、覚えたと判断する

頭のいい人が、やっていること
　　1語を、3秒見て、隠して、出す　→　出た速さで、覚えたと判断する</pre>
<div class="bd sm">章タイトルと同じ言葉を使う。両側とも 行動＋結末。生徒の声は5に置く。</div>

<div class="sec">分量</div>
<div class="bd">標準 約1,650字＝3ページ　／　厚く書く7本 約2,200字＝4ページ　／　図は1本に1〜2点<br><span class="chk">基本の基本3　選ぶ11　入れる8　つなげる6　出す12　なおす10　続ける20　＝　70</span></div>

<div class="sec">図の4型</div>
<table class="lv">
<tr><td class="l">対比図</td><td class="le" colspan="2">伸びない人と頭のいい人の動きを並べる。10回書くあいだの頭と手、など</td></tr>
<tr><td class="l">手順図</td><td class="le" colspan="2">やり方のステップ。10語1セットの回し方、など</td></tr>
<tr><td class="l">時間図</td><td class="le" colspan="2">時間がどこに消えているか。75分と12分、など</td></tr>
<tr><td class="l">構造図</td><td class="le" colspan="2">頭の中のつながり方。1本ずつの線と、束ねた線、など</td></tr>
</table>
<div class="bd sm">4型に絞る。70本でもバラけず、同じ本に見える。SVGで作り、2色刷りの版下にそのまま出せる。</div>
</div>

<div class="sh">
<div class="lb">文体の決まり</div>
<div class="sec">守る</div>
<div class="bd">話し言葉。1文を短く。先生の声ではなく、隣の席の人の声。<br>
読者を責めない。62本すべて、頑張っている人の型。<br>
伸びない人の選択には、必ずまともな理由を1つ持たせる。<br>
説明より問い。説明したくなったら、問いに変えられないか考える。<br>
答えは1つの行動。意識・姿勢・心がけで終わらせない。<br>
結論は数に帰着させる。数が増えるか、減るか。<br>
場面は中学生と高校生。社会人は書かない。</div>

<div class="sec">使わない</div>
<div class="bd">アスタリスクによる太字・強調。<br>
理解力・暗記力・計画力など、既視感のある能力名。<br>
才能・根性・やる気・時間の量を、成績の原因として書かない。<br>
「復習が大事」のような順接の常識。逆説か、常識の言い換えにする。<br>
「〜しましょう」の連発。言い切りで書く。<br>
ビジネス書の言葉（有限、仕組み、条件をそろえる など）。<br>
研究の名前と専門用語。「〜と言われています」で逃げない。</div>

<div class="sec">数字</div>
<div class="bd">再現できるかは、数字で決まる。<br>
「短い間隔で」ではなく「10語」。「速く出す」ではなく「0.5秒」。<br>
20番には数字が18個入っている。これを基準にする。</div>
</div>'''


pt = f'''<div class="pg">
<div class="lb">ここから</div>
<div class="sec">僕がやること</div>
<table class="lv">
<tr><td class="l">1</td><td class="ln">分岐点</td><td class="le">残り29本。頭のなかが対で入っているので、1語を抜くだけ</td><td class="lw">済 7本</td></tr>
<tr><td class="l">2</td><td class="ln">頭のなか</td><td class="le">13本。09 12 14 15 18 22 27 50 51 52 53 65 66</td><td class="lw">対なし 13本</td></tr>
<tr><td class="l">3</td><td class="ln">型の移植</td><td class="le">70本を、場面から問いに書き換える</td><td class="lw">済 1本</td></tr>
<tr><td class="l">4</td><td class="ln">図</td><td class="le">4型で、70本に1〜2点ずつ</td><td class="lw">済 2点</td></tr>
<tr><td class="l">5</td><td class="ln">おわりに</td><td class="le">14時間の話から、そのあとの話へ</td><td class="lw"></td></tr>
</table>

<div class="sec">著者にしかできないこと</div>
<table class="lv">
<tr><td class="l">A</td><td class="ln">実話　7か所</td><td class="le">厚く書く項目に、300〜500字</td><td class="lw">docs/27</td></tr>
<tr><td class="l">B</td><td class="ln">実話　14か所</td><td class="le">断定の根拠が経験しかない場所に1〜2行</td><td class="lw">docs/27</td></tr>
<tr><td class="l">C</td><td class="ln">1週間の数字</td><td class="le">週6部活・帰宅8時の中2が、実際に何時に何を何分</td><td class="lw">09番</td></tr>
<tr><td class="l">D</td><td class="ln">西野さんの話</td><td class="le">サイトが読めないので内容を1段落</td><td class="lw">第1章</td></tr>
<tr><td class="l">E</td><td class="ln">数字の確認</td><td class="le">0.5秒／2秒／10語／点2つ　ほか</td><td class="lw">20番</td></tr>
</table>

<div class="sec">杉浦さんに聞くこと</div>
<div class="bd">{TOTAL}ページで、いくらになりますか。　／　初版部数の想定。　／　表紙の数字は70でいいか。</div>

<div class="sec">進行</div>
<pre class="logic">11/7-11/10　 暗記編10本（23-32）を新型で。1章ぶんで手触りを確定させる
11/11-11/13　本文の相互参照85か所を直す。多くが旧番号のまま
11/14-11/22　残り60本を新型に移植。分岐点29本と図を入れる
11/23-11/25　著者の実話21か所を差し込む
11/26-11/27　序章・第1章・第2章の仕上げ、おわりに書き直し
11/28　　　　巻末
11/29　　　　通し読み。数字と言葉の統一
<div class="bd sm">既存本文は約111,000字あり、新しく書くのは約8,000字（分岐点29本）。残りは移植と加筆。</div>
</div>'''

det = ['<div class="sh2"><div class="lb">62項目</div>']
for k, no, name in MAP:
    c = by[k]
    det.append(f'<div class="ch"><span class="cn">{no}</span>頭のいい人が、絶対にやらないこと　'
               f'<span class="hen2">{name}</span><span class="cc">{len(c["items"])}本</span></div>')
    for it in c["items"]:
        st = '<span class="star">★</span>' if it["thick"] else ''
        hd = '' if it["n"] in PAIR else '<span class="warn">頭のなか 対なし</span>'
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
.pg{{page-break-before:always}}
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
table.lv .l{{font-family:"Noto Sans CJK JP",sans-serif}}
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
out=('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>制作仕様書</title>'
     f'<style>{CSS}</style></head><body>'+p1+p2+pk+"\n".join(det)+pt+'</body></html>')
os.makedirs("build",exist_ok=True)
open("build/制作仕様書.html","w",encoding="utf-8").write(out)
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
 "--no-pdf-header-footer","--print-to-pdf=build/制作仕様書.pdf",
 "file://"+os.path.abspath("build/制作仕様書.html")],check=True,capture_output=True)
print(f"章 {len(rows)}　項目 {sum(r[2] for r in rows)}　{TOTAL}ページ　"
      f"頭のなか未 {sum(1 for v in HEAD.values() if not v)}本")
