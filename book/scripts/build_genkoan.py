# -*- coding: utf-8 -*-
"""現行案の見本。四六判・縦組み・2色。book/ で実行 → build/現行案_見本.html"""
import os, re

src = open(os.path.join(os.path.dirname(__file__), "build_mock.py")).read()
ns = {}
exec(src.split("def page(")[0], ns)
CSS, NAVY, GRAY = ns["CSS"], ns["NAVY"], ns["GRAY"]

CSS += f"""
/* 表紙 */
.cover {{ position:absolute; inset:0; background:#fff; }}
.cover .inner {{ position:absolute; top:26mm; left:14mm; right:14mm;
  writing-mode:horizontal-tb; font-family:"Noto Serif CJK JP",serif; text-align:center; }}
.cover .main {{ font-size:25pt; font-weight:700; line-height:1.45; letter-spacing:.01em;
  color:#111; }}
.cover .sub {{ font-size:10pt; color:{NAVY}; margin-top:9mm; line-height:1.75;
  font-weight:600; }}
.cover .au {{ position:absolute; bottom:46mm; left:0; right:0; text-align:center;
  writing-mode:horizontal-tb; font-size:9pt; color:#444;
  font-family:"Noto Serif CJK JP",serif; }}
.obi {{ position:absolute; bottom:0; left:0; right:0; height:42mm; background:{NAVY};
  color:#fff; writing-mode:horizontal-tb; font-family:"Noto Sans CJK JP",sans-serif;
  display:flex; flex-direction:column; align-items:center; justify-content:center; }}
.obi .dig {{ font-size:19pt; letter-spacing:.42em; font-weight:300; }}
.obi .q {{ font-size:10.5pt; margin-top:5mm; font-weight:700; letter-spacing:.08em; }}

/* 横組みの箱（問題・表・図） */
.hbox {{ position:absolute; top:20mm; bottom:22mm; left:15mm; right:15mm;
  writing-mode:horizontal-tb; font-family:"Noto Serif CJK JP",serif; }}
.hbox .lbl {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:{GRAY};
  letter-spacing:.14em; border-bottom:1px solid #ddd; padding-bottom:2mm; }}
.hbox .lead {{ font-size:9pt; line-height:2.0; margin-top:7mm; }}
.qbox {{ border:1.5px solid {NAVY}; padding:7mm 6mm; margin-top:7mm; text-align:center; }}
.qbox .ja {{ font-size:11.5pt; font-weight:600; line-height:1.7; }}
.qbox .words {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt; color:{NAVY};
  margin-top:6mm; letter-spacing:.04em; }}
.qbox.flat {{ border:none; background:#eef3f9; }}
.ansbox {{ background:#f6f6f6; padding:5mm; margin-top:6mm; font-size:8.6pt;
  line-height:1.95; }}
.ansbox .en {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt;
  color:{NAVY}; font-weight:700; margin-bottom:3mm; }}
.hbox .note {{ font-size:8.6pt; line-height:1.95; margin-top:6mm; }}
.hbox .punch {{ font-size:11pt; font-weight:700; color:{NAVY}; margin-top:8mm;
  line-height:1.6; text-align:center; }}

/* 6本グリッド */
.grid6 {{ display:grid; grid-template-columns:1fr 1fr; gap:3.2mm; margin-top:6mm;
  direction:rtl; }}
.w {{ border:1px solid #d8d8d8; border-top:2.5px solid {NAVY}; padding:3.6mm 3.2mm;
  direction:ltr; }}
.w .nm {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; font-weight:700;
  color:{NAVY}; }}
.w .kuse {{ font-size:8.4pt; margin-top:2.2mm; line-height:1.5; }}
.w .cnt {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:6.8pt; color:{GRAY};
  margin-top:2.2mm; }}

/* 1週間の表 */
table.wk {{ width:100%; border-collapse:collapse; margin-top:6mm; font-size:7.6pt; }}
table.wk th {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:6.8pt; color:{GRAY};
  font-weight:700; text-align:left; padding:2mm 1.5mm; border-bottom:1.5px solid {NAVY};
  letter-spacing:.06em; }}
table.wk td {{ padding:2.3mm 1.5mm; border-bottom:1px solid #e8e8e8; line-height:1.5;
  vertical-align:top; }}
table.wk td.d {{ font-family:"Noto Sans CJK JP",sans-serif; font-weight:700;
  color:{NAVY}; width:8mm; }}
table.wk tr.off td {{ background:#f7f7f7; color:#999; }}
table.wk td .em {{ color:{NAVY}; font-weight:700; }}

/* 巻末カード */
.card {{ position:absolute; top:30mm; bottom:34mm; left:19mm; right:21mm;
  border:1.5px dashed {NAVY}; writing-mode:horizontal-tb;
  font-family:"Noto Serif CJK JP",serif; padding:7mm 6mm; }}
.card .ct {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8.5pt;
  color:{NAVY}; letter-spacing:.2em; text-align:center; font-weight:700;
  border-bottom:1px solid #cfdcea; padding-bottom:4mm; }}
.card .row {{ display:flex; justify-content:space-between; align-items:baseline;
  margin-top:5.2mm; font-size:8.6pt; }}
.card .row .k {{ font-family:"Noto Sans CJK JP",sans-serif; font-weight:700;
  color:#222; font-size:8.4pt; }}
.card .row .v {{ color:{NAVY}; }}
.card .foot {{ font-size:7.6pt; color:#555; margin-top:7mm; line-height:1.8;
  border-top:1px solid #cfdcea; padding-top:4mm; }}
"""

def pg(inner, hashira="", nombre="", cls="area"):
    h = f'<div class="hashira">{hashira}</div>' if hashira else ''
    n = f'<div class="nombre">{nombre}</div>' if nombre else ''
    return f'<div class="page">{h}<div class="{cls}">{inner}</div>{n}</div>'

def raw(inner):
    return f'<div class="page">{inner}</div>'

P = []

# 1 表紙＋帯
P.append(raw(f'''<div class="cover">
  <div class="inner">
    <div class="main">やっているのに、<br>伸びない。</div>
    <div class="sub">頭のいい人が勉強で、<br>絶対にやらない62のこと</div>
  </div>
  <div class="au">朝倉 徹大</div>
  <div class="obi">
    <div class="dig">1 4 9 1 6 2 5 3 6 4 9</div>
    <div class="q">10秒で、覚えきれますか</div>
  </div>
</div>'''))

# 2 序章 1問
P.append(raw(f'''<div class="hbox">
  <div class="lbl">序章　頭のいい人が持っている、6つの武器</div>
  <div class="lead">さっき、数字で1回やりました。今度は、勉強でやります。<br>
  鉛筆を持ってください。3分で終わります。</div>
  <div class="qbox">
    <div class="ja">彼は私に、その本を読むように言いました。</div>
    <div class="words">( me ／ the ／ he ／ read ／ to ／ told ／ book )</div>
  </div>
  <div class="note">30秒。<br><br>できましたか。できた人は、横に○をつけてください。</div>
  <div class="ansbox">
    <div class="en">He told me to read the book.</div>
    told me to 〜 で「私に〜するように言った」。<br>
    tell のうしろは「だれに」「何を」の順。<br>
    「〜するように」は、to のあとに動詞をそのまま置く。
  </div>
  <div class="punch">「なるほど」と思いましたか。<br>ここが、勉強でいちばん危ないところです。</div>
</div><div class="nombre">28</div>'''))

# 3 序章 2回目
P.append(raw(f'''<div class="hbox">
  <div class="lbl">もう1問。さっきと同じ問題</div>
  <div class="lead">本を閉じてください。<br><br>
  閉じたまま、もう一度、同じ文を英語にしてください。<br>
  今度は、語のならびはありません。日本語だけです。</div>
  <div class="qbox flat"><div class="ja">彼は私に、その本を読むように言いました。</div></div>
  <div class="note">書けましたか。<br><br>
  1回目はできて、2回目で止まった人。<br>
  to が抜けた人。said を使った人。read を reading にした人。<br><br>
  <span style="color:{NAVY};font-weight:700">その人が、この本の読者です。</span><br><br>
  あなたの頭は、1分前と何も変わっていません。<br>
  変わったのは、選ぶ語が目の前にあるかないか。それだけです。</div>
  <div class="punch">そして、テストは2回目のほうです。</div>
</div><div class="nombre">30</div>'''))

# 4 序章 命名（縦組み）
P.append(pg(f'''<div class="opener">
  <div class="ttl">いま、2つのことが起きました</div></div>
<p class="noind">解説を読んで「なるほど」と思った。<br>閉じたら、出てこなかった。</p>
<div class="sp"></div>
<p>入れたつもりで、入っていなかった。出したつもりで、出していなかった。</p>
<div class="xo">
  <p class="noind"><span class="o">入れる力</span>　入れるだけでは、入らない</p>
  <p class="noind">　　　　　→　入れたら、すぐ出す</p>
  <p class="noind">　　　　　「いま、閉じて出せる？」</p>
  <div class="sp"></div>
  <p class="noind"><span class="o">出す力</span>　　テストと違う練習は、練習じゃない</p>
  <p class="noind">　　　　　→　テストと同じ形で、やる</p>
  <p class="noind">　　　　　「それ、テストでもできる？」</p>
</div>
<p>この2つが、この本でいちばん使う武器です。
62項目のうち18が、この2つで片づきます。</p>
<div class="sp"></div>
<p>そして、この2つは、やることが同じです。閉じること。</p>
<div class="sp"></div>
<p>「わかった」は、閉じるまでは、ただの感想です。</p>''', "序章", "32"))

# 5 手持ち6本
W = [("選ぶ力","「これ、出るの？」","11項目"),
     ("入れる力","「いま、閉じて出せる？」","8項目"),
     ("つなげる力","「これ、前にどこで見た？」","5項目"),
     ("出す力","「それ、テストでもできる？」","10項目"),
     ("なおす力","「どこで、止まった？」","10項目"),
     ("続ける力","「次の1個目は？」","18項目")]
cells = "".join(f'<div class="w"><div class="nm">{n}</div>'
                f'<div class="kuse">{k}</div><div class="cnt">{c}</div></div>'
                for n,k,c in W)
P.append(raw(f'''<div class="hbox">
  <div class="lbl">手持ち、6本</div>
  <div class="grid6">{cells}</div>
  <div class="note">順番はありません。1番から6番まで通す必要も、ありません。<br><br>
  さっきの1問で使ったのは、入れる力と出す力の2つだけです。<br>
  あとの4つは、出番が来たときに抜きます。</div>
  <div class="punch">1問につき、だいたい2つ。それだけです。</div>
  <div class="note" style="text-align:center;color:{GRAY};font-size:8pt">
  迷ったら、入れる力と出す力。つまり、閉じること。</div>
</div><div class="nombre">44</div>'''))

# 6 1週間
rows = [("月","単語20　閉じて出す","英語ワーク p42-45",0),
        ("火","単語20　閉じて出す","数学　間違えた6問を、原因で3つにまとめる",0),
        ("水","単語20　閉じて出す","――",1),
        ("木","単語20　閉じて出す","理科　光の単元を、何も見ないで書き出す",0),
        ("金","単語20　閉じて出す","社会　江戸の流れを、教科書を閉じて口で言う",0),
        ("土","――","9:00-9:30 ワーク2周目 ×だけ ／ 9:40-10:10 英語 長文1本 時間を測る ／ 10:20-10:50 数学 ×をもう1回",0),
        ("日","――","9:00-9:30　1週間の×を、原因で3つにまとめる",0)]
trs = "".join(f'<tr class="{"off" if o else ""}"><td class="d">{d}</td>'
              f'<td style="width:30mm">{a}</td><td>{b}</td></tr>' for d,a,b,o in rows)
P.append(raw(f'''<div class="hbox">
  <div class="lbl">第1章　09　1日の計画を、to doリストで立てて終わる</div>
  <div class="lead" style="margin-top:5mm">週6で部活。帰宅8時。定期テストまで2週間。中2。</div>
  <table class="wk"><tr><th></th><th>朝 7:00</th><th>夜 20:30-21:00</th></tr>{trs}</table>
  <div class="note">平日は1日30分です。2時間ではありません。<br>
  週6で部活がある人に2時間は書けません。書いたところで、守れないので、
  計画としての意味がありません。<br><br>
  <span class="em" style="color:{NAVY};font-weight:700">水曜が空いています。</span>
  試合前の練習が長引いて、帰宅が9時半でした。何もできませんでした。<br><br>
  それでも、この計画は崩れていません。崩れる日を、最初から1日入れてあるからです。<br><br>
  そして水曜も、朝の単語20はやりました。</div>
</div><div class="nombre">62</div>'''))

# 7 項目09 本文（縦組み）
P.append(pg(f'''<div class="opener">
  <div class="tag" style="margin-block-end:3mm">続ける力　「次の1個目は？」</div>
  <div class="num">09</div>
  <div class="ttl">1日の計画を、<br>to doリストで立てて終わる</div></div>
<div class="xo">
  <p class="noind"><span class="x">×「今日やることは、この4つ」</span></p>
  <p class="noind"><span class="o">○「10時までに単語30個。量と締切を、セットにする」</span></p>
</div>
<h2>こんなとき</h2>
<p>ノートの隅に、こう書いてある。「英語ワーク」「数学 復習」「単語」「理科 プリント」。</p>
<p>夜11時。4つのうち、1つ半しか終わっていない。</p>
<h2>あなたのせいではありません</h2>
<p>このリストに、間違いは1つもありません。やるべきことは、その4つです。</p>
''', "第1章　計画", "60"))

# 8 項目09 続き
P.append(pg(f'''<p class="noind">問題は、この4つのどれにも、終わりが書いていないことです。</p>
<p>「英語ワーク」は、いつ終わるのか。1ページでも英語ワークです。
20ページでも英語ワークです。終わりが書いていないものは、終わりません。</p>
<h2>何が起きているか</h2>
<p>to doリストは、やることの名前の一覧です。計画は、量と時間の約束です。</p>
<p>名前の一覧を書いて、計画を立てた気になる。ここが「やった気」です。</p>
<div class="minds">
  <div class="mind ng"><div class="cap">書いたもの</div>
    <p>やることの名前</p></div>
  <div class="mind ok"><div class="cap">書いていないもの</div>
    <p>どれだけやるか<br>いつまでにやるか</p></div>
</div>
<h2>やり方</h2>
<p>名前のうしろに、量と締切をつける。それだけです。</p>
<div class="xo">
  <p class="noind"><span class="x">×　英語ワーク</span></p>
  <div class="sp"></div>
  <p class="noind"><span class="o">○　英語ワーク p42-45　　20:30-21:00</span></p>
</div>
''', "第1章　計画", "61"))

# 9 巻末カード
P.append(raw(f'''<div class="card">
  <div class="ct">手 持 ち　6 本</div>
  <div class="row"><span class="k">選ぶ力</span><span class="v">「これ、出るの？」</span></div>
  <div class="row"><span class="k">入れる力</span><span class="v">「いま、閉じて出せる？」</span></div>
  <div class="row"><span class="k">つなげる力</span><span class="v">「これ、前にどこで見た？」</span></div>
  <div class="row"><span class="k">出す力</span><span class="v">「それ、テストでもできる？」</span></div>
  <div class="row"><span class="k">なおす力</span><span class="v">「どこで、止まった？」</span></div>
  <div class="row"><span class="k">続ける力</span><span class="v">「次の1個目は？」</span></div>
  <div class="foot">迷ったら、入れる力と出す力。<br>この2つは同じ動作です。閉じること。</div>
</div><div class="nombre">266</div>'''))

html = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
        f'<title>現行案 見本</title><style>{CSS}</style></head><body>'
        + "".join(P) + '</body></html>')
os.makedirs("build", exist_ok=True)
open("build/現行案_見本.html","w",encoding="utf-8").write(html)
import subprocess
subprocess.run(["/usr/bin/google-chrome","--headless","--disable-gpu","--no-sandbox",
  "--no-pdf-header-footer","--print-to-pdf=build/現行案_見本.pdf",
  "file://"+os.path.abspath("build/現行案_見本.html")],check=True,capture_output=True)
print("pages", len(P))
