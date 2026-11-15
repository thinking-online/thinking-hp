# -*- coding: utf-8 -*-
# 「見開き4つ・8ページで1つ完結」の見本を作る。12番を、四六判・縦書きで組む。
#   python3 -I scripts/build_mock8.py      → build/見本_8ページ_案A.html と 案B.html
#   node scripts/shot_mock8.js             → それぞれ PNG にする（はみ出しも調べる）
# 案A＝1ページ目が大きな二項対立。案B＝1ページ目が「法則」の宣言。2〜8ページ目は同じ。
import io, re, html

NAVY = "#15467E"

def tcy(s):
    return re.sub(r"(?<![0-9A-Za-z])([0-9]{1,2}|[QA])(?![0-9A-Za-z])", r'<span class="tcy">\1</span>', s)

def mk(s):
    s = html.escape(s)
    s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
    return tcy(s)

def P(*lines):
    return "".join(f"<p>{mk(l)}</p>" for l in lines)

def ill(label, desc, cls="ill"):
    return (f'<div class="{cls}"><span class="il">{html.escape(label)}</span>'
            f'<span class="id">{desc}</span></div>')

def count(*chunks):
    t = re.sub(r"<span class=\"i[ld]\">.*?</span>", "", "".join(chunks), flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    return len(re.sub(r"\s", "", html.unescape(t)))

# ================================================================ 1ページ目　案A
p1a = f'''<div class="p1">
<div class="num">12</div><div class="lawtag">絶対法則 ② 思い出す</div>
<div class="duo">
  <div class="panel ok"><div class="head"><span class="m">○</span>頭のいい人</div>
    <div class="big">目を閉じて、<br>声に出す</div>
    {ill("イラスト", "目を閉じて、<br>声に出している子")}</div>
  <div class="panel ng"><div class="head"><span class="m">×</span>伸びない人</div>
    <div class="big">黙って、じっと<br>見つめて覚える</div>
    {ill("イラスト", "教科書を、<br>じっと見つめる子")}</div>
</div></div>'''

# ================================================================ 1ページ目　案B
p1b = f'''<div class="p1b">
<div class="lawno"><span class="lw">法則</span><span class="ln">12</span></div>
<div class="lawtag2">絶対法則 ② 思い出す</div>
<div class="decl">
  <div class="d1">頭のいい人は、</div>
  <div class="d2">「黙って、じっと見つめて覚える」</div>
  <div class="d3">を、やらない。</div>
</div>
<div class="then"><span class="bar"></span>じゃあ、何をする？</div>
<div class="next">◀ 次のページへ</div>
</div>'''

# ================================================================ 2ページ目　Q → 答えの始まり
p2 = ('<div class="v">'
      '<div class="q"><div class="ql">' + tcy("Q") + '</div><div class="qh">こんな時、何が正解？</div>'
      + P("歴史のテスト前。教科書を開いて、黙って、じっと見ています。",
          "20分経って、教科書を閉じました。何が書いてあったか、言おうとしても、出てきません。")
      + '</div>'
      '<div class="a"><div class="al">' + tcy("A") + '</div><div class="ah">目を閉じて、声に出す。</div></div>'
      + P("じっと見るのは、真面目な人ほどやります。静かで、集中しているように見えます。本人も、集中しているつもりです。",
          "でも、やっていることは「入れる」だけです。点になるのは、「思い出して、出す」ほうでした（02番）。",
          "では、思い出す時、体をどう使えばいいのか。使うのは、==目と、口==です。",
          "本を閉じる。目を閉じる。声に出す。これで、1つの動作です。",
          "自習室や図書館で、時々天井を見ている人がいますよね。あれは、さぼっているのではありません。思い出しています。")
      + '</div>')

# ================================================================ 3ページ目　説明
p3 = ('<div class="v"><h3>目を閉じると、思い出しやすくなります</h3>'
      + P("イギリスのヨーク大学の実験です。",
          "映像を見てもらって、そのあと内容を思い出してもらいます。片方のグループには、目を開けたまま思い出してもらいました。もう片方には、目を閉じて思い出してもらいました。",
          "目を閉じたグループのほうが、==見たものも、聞いたものも、正確に思い出せました。==",
          "理由は、単純です。目を開けていると、目の前のものが、ずっと頭に入ってきます。見るつもりがなくても、頭は、それを全部受け取っています。",
          "教材を見つめたまま「思い出そう」としても、目に答えが入ってきてしまいます。それは、思い出しているのではなく、見ているだけです。",
          "だから、思い出す時は、教材から顔を上げます。目を閉じるのが恥ずかしければ、天井を見るのでもかまいません。")
      + '</div>')

# ================================================================ 4ページ目　上にイラスト、下に説明書き
p4 = ('<div class="upper">' + ill("イラスト（図解）", "左：目を開けている時<br>机・ポスター・窓の外が、頭に入ってくる<br><br>右：目を閉じている時<br>入ってくるものが止まり、思い出すことに使える", "ill tall")
      + '</div><div class="lower"><div class="v"><h3>目を閉じると、何が変わるか</h3>'
      + P("目を開けていると、机の上、壁のポスター、窓の外が、ずっと頭に入ってきます。",
          "目を閉じると、それが止まります。そのぶん、頭を、思い出すことに使えます。")
      + '</div></div>')

# ================================================================ 5ページ目　説明
p5 = ('<div class="v"><h3>声に出すと、残りやすくなります</h3>'
      + P("もう1つは、口です。カナダのウォータールー大学の実験です。",
          "単語のリストを覚えてもらいます。半分は、声に出して読む。もう半分は、黙って読む。あとでテストをすると、==声に出した単語のほうが、よく覚えていました。==",
          "声に出すと、口が動き、自分の声が耳から入ります。思い出す手がかりが増えます。",
          "しかも声は、出てこなければ止まります。頭の中で言うのと違って、==ごまかせません。==")
      + '<h3>英単語なら、こうします</h3>'
      + P("見ながら10回書いている間、頭は1回も思い出していません。同じ時間を、こう使います。")
      + '<div class="list">' + "".join(f"<p>{mk(x)}</p>" for x in
            ["① 10個だけ、30秒見る", "② 閉じて、10個を声に出す", "③ 出なかったものにだけ、印をつける", "④ 印のついたものだけ、もう一度"]) + '</div>'
      + P("1回で出たものは、もうやらない。回数は、印が決めてくれます（16番）。")
      + '</div>')

# ================================================================ 6ページ目　やり方を、イラストでページいっぱいに
def srow(n, head, body, desc):
    return (f'<div class="srow"><div class="stx"><div class="sn">STEP {n}</div><div class="sh">{html.escape(head)}</div>'
            f'<div class="sb">{html.escape(body)}</div></div>{ill("イラスト", desc, "ill sill")}</div>')
p6 = ('<div class="hp"><div class="stt">やり方<span>　3つのSTEP</span></div>'
      + srow("01", "読んだら、本を閉じて、顔を上げる", "答えが目に入らないようにする。", "本を閉じて、<br>顔を上げる")
      + srow("02", "目を閉じて、止まるまで声に出す", "声を出せない場所では、口だけ動かす。", "目を閉じて、<br>声に出す")
      + srow("03", "止まったところだけ見て、もう一度言う", "止まった場所が、まだ入っていない場所。", "1か所だけ見て、<br>また閉じる")
      + '<div class="kj"><span>「できた」の基準</span>目を閉じたまま、止まらずに最後まで言えた。次の日にも、言えた。</div></div>')

# ================================================================ 7ページ目　頭の中（上＝頭のいい人、下＝伸びない人）
def mbox(cls, who, lines, desc):
    return (f'<div class="mbox {cls}"><div class="mhead">{html.escape(who)}</div><div class="mbody">'
            f'<div class="mv">{P(*lines)}</div>{ill("イラスト", desc, "ill mill")}</div></div>')
p7 = ('<div class="mind"><div class="mt">頭の中<span>　教科書を読んだあと</span></div>'
      + mbox("ok", "頭のいい人", ["「読んだ。閉じる」", "（目も閉じる）", "「鎌倉幕府ができて、執権が北条氏になって、……そのあと、何だっけ」",
                             "（声が止まる）", "「止まった。そこだけ見よう」", "（1か所だけ見て、また閉じて言う）"], "顔を上げて<br>目を閉じる")
      + mbox("ng", "伸びない人", ["「もう1回、よく見ておこう」", "（じっと見る）", "「うん、見覚えがある。大丈夫」", "（閉じたら、出てこない）"], "教科書を<br>見つめる")
      + '</div>')

# ================================================================ 8ページ目　まとめ
p8 = ('<div class="v"><h3>この場面のまとめ</h3>'
      '<div class="sum">' + P("見つめている間は、入れているだけ。", "目を閉じると、思い出しやすくなる。", "声に出すと、残りやすくなる。ごまかせない。") + '</div>'
      '<h3>これをやると、何が残るか</h3>'
      + P("じっと見ていた20分は、閉じた時に何も出てこなければ、0です。閉じて声に出した5分は、出てきたぶんだけ、確実に残っています。",
          "どこが入っていないかも、声が止まった場所でわかります。")
      + '<div class="todo"><span class="tl">今日やること</span>' + mk("今日読んだページを1つ選び、本と目を閉じて、書いてあったことを3つ声に出す。") + '</div>'
      '<div class="foot">もとにある絶対法則　② 思い出す</div>'
      '</div>')

CSS = """
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"Noto Sans CJK JP",sans-serif; background:#e9e7e2; color:#111; padding:9mm 9mm 10mm; width:545mm; }
.sheet { font-size:15pt; font-weight:700; color:NAVY; margin-bottom:2mm; }
.sub { font-size:10pt; color:#444; margin-bottom:6mm; line-height:1.75; }
.grid { display:grid; grid-template-columns:254mm 254mm; gap:9mm 12mm; }
.cap { font-size:10pt; font-weight:700; color:#333; margin:0 0 2mm 1mm; }
.pages { display:flex; width:254mm; box-shadow:0 2px 10px rgba(0,0,0,.18); }
.page { width:127mm; height:188mm; background:#fff; position:relative; padding:17mm 15mm 16mm 15mm; }
.page.left  { border-right:1px solid #ddd; padding-right:18mm; }
.page.right { padding-left:18mm; }
.pno { position:absolute; bottom:6.5mm; font-size:7.5pt; color:#888; }
.page.left .pno { left:15mm; } .page.right .pno { right:15mm; }
.tag { position:absolute; top:6.5mm; font-size:7.2pt; color:#fff; background:NAVY; padding:.6mm 2.2mm; border-radius:1mm; letter-spacing:.04em; white-space:nowrap; }
.page.left .tag { left:15mm; } .page.right .tag { right:15mm; }

.v { writing-mode:vertical-rl; width:100%; height:100%; font-family:"Noto Serif CJK JP",serif;
     font-size:10pt; line-height:1.82; text-align:justify; }
.v p { text-indent:1em; }
.tcy { text-combine-upright:all; -webkit-text-combine:horizontal; }
mark { background:#fff3a6; color:inherit; }
h3 { font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt; font-weight:700; color:NAVY; line-height:1.4; margin:0 .75em 0 .45em; }
.v > h3:first-child { margin-right:0; }

/* イラストの枠 */
.ill { border:1px dashed #9a9a9a; background:#f5f4ef; font-family:"Noto Sans CJK JP",sans-serif; writing-mode:horizontal-tb;
       display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; position:relative; }
.il { position:absolute; top:1.6mm; left:2mm; font-size:6.5pt; color:#fff; background:#8a8a8a; padding:.3mm 1.6mm; border-radius:1mm; }
.id { font-size:8pt; color:#777; line-height:1.7; }

/* 1ページ目 案A */
.p1 { width:100%; height:100%; display:flex; flex-direction:column; align-items:center; }
.p1 .num { font-size:27pt; font-weight:900; color:NAVY; line-height:1; border-bottom:2.5pt solid NAVY; padding:0 3mm 1.2mm; letter-spacing:.06em; }
.lawtag { font-size:7.5pt; color:NAVY; letter-spacing:.12em; margin-top:2mm; }
.duo { flex:1; display:flex; gap:5mm; width:100%; margin-top:4.5mm; min-height:0; }
.panel { flex:1; border:1.8pt solid; border-radius:2.5mm; display:flex; flex-direction:column; align-items:center; padding-bottom:3mm; overflow:hidden; }
.panel.ng { border-color:#9a9a9a; } .panel.ok { border-color:NAVY; }
.panel .head { width:100%; text-align:center; padding:1.8mm 0 1.6mm; font-size:9pt; font-weight:700; letter-spacing:.12em; }
.panel.ng .head { background:#e6e6e6; color:#666; } .panel.ok .head { background:NAVY; color:#fff; }
.head .m { font-size:16pt; display:block; line-height:1.15; letter-spacing:0; }
.big { flex:1; writing-mode:vertical-rl; font-size:20pt; font-weight:700; line-height:1.55; letter-spacing:.07em; margin:4mm auto 3mm; text-align:center; min-height:0; }
.panel.ng .big { color:#666; } .panel.ok .big { color:#111; }
.panel .ill { width:calc(100% - 6mm); height:47mm; flex:none; }

/* 1ページ目 案B */
.p1b { width:100%; height:100%; position:relative; }
.lawno { position:absolute; top:0; right:0; text-align:center; color:NAVY; line-height:1; }
.lawno .lw { display:block; font-size:8pt; letter-spacing:.3em; padding-left:.3em; margin-bottom:1.2mm; }
.lawno .ln { display:block; font-size:30pt; font-weight:900; border-top:2.5pt solid NAVY; padding-top:1.5mm; }
.lawtag2 { position:absolute; top:26mm; right:1mm; writing-mode:vertical-rl; font-size:7.5pt; color:NAVY; letter-spacing:.12em; }
.decl { position:absolute; top:4mm; right:24mm; height:150mm; writing-mode:vertical-rl; }
.decl .d1 { font-size:15pt; font-weight:700; margin-left:5mm; }
.decl .d2 { font-size:24.5pt; font-weight:900; letter-spacing:.04em; line-height:1.25; }
.decl .d3 { font-size:15pt; font-weight:700; margin-right:5mm; padding-top:84mm; }
.then { position:absolute; left:1mm; bottom:9mm; writing-mode:vertical-rl; font-size:16pt; font-weight:700; color:NAVY; letter-spacing:.06em; }
.then .bar { display:inline-block; width:1.6pt; height:16mm; background:NAVY; margin-bottom:3mm; }
.next { position:absolute; left:0; bottom:0; font-size:7.5pt; color:#888; letter-spacing:.08em; }

/* 2ページ目 */
.q { border:1.4pt solid NAVY; padding:.8em .7em .8em .6em; margin-left:1.1em; }
.q p { text-indent:0; }
.ql, .al { font-family:"Noto Sans CJK JP",sans-serif; font-size:19pt; font-weight:900; color:NAVY; line-height:1.2; }
.qh { font-family:"Noto Sans CJK JP",sans-serif; font-size:11.5pt; font-weight:700; color:NAVY; margin-left:.5em; padding-top:2.4em; line-height:1.3; }
.ql { float:none; }
.q .ql { position:absolute; }
.q { position:relative; }
.a { position:relative; margin-left:.9em; }
.a .al { position:absolute; }
.ah { font-family:"Noto Sans CJK JP",sans-serif; font-size:14pt; font-weight:700; padding-top:2em; line-height:1.3; }

/* 4ページ目 */
.upper { height:57%; } .lower { height:38%; margin-top:5%; }
.ill.tall { width:100%; height:100%; }
.ill.tall .id { font-size:8.5pt; }

/* 5ページ目 */
.list { font-family:"Noto Sans CJK JP",sans-serif; font-size:9.3pt; line-height:1.7; border-right:2pt solid NAVY; padding-right:.7em; margin:0 .5em 0 .7em; }
.list p { text-indent:0; }

/* 6ページ目 */
.hp { writing-mode:horizontal-tb; width:100%; height:100%; display:flex; flex-direction:column; }
.stt { font-size:13pt; font-weight:700; color:NAVY; border-bottom:2pt solid NAVY; padding-bottom:1.2mm; }
.stt span { font-size:8pt; color:#777; font-weight:400; }
.srow { flex:1; display:flex; gap:3.5mm; align-items:stretch; padding:3mm 0; border-bottom:1px solid #dcdcdc; min-height:0; }
.stx { flex:1; display:flex; flex-direction:column; justify-content:center; }
.sn { font-size:8pt; font-weight:900; color:#fff; background:NAVY; align-self:flex-start; padding:.3mm 2.2mm; border-radius:1mm; letter-spacing:.08em; }
.sh { font-size:10.5pt; font-weight:700; line-height:1.45; margin-top:1.8mm; }
.sb { font-size:8.5pt; color:#444; line-height:1.6; margin-top:1.2mm; }
.ill.sill { width:45mm; flex:none; }
.kj { margin-top:3mm; border:1.3pt solid NAVY; color:NAVY; font-size:8.8pt; font-weight:700; line-height:1.6; padding:2mm 2.5mm; }
.kj span { display:block; font-size:7.5pt; letter-spacing:.06em; }

/* 7ページ目 */
.mind { width:100%; height:100%; display:flex; flex-direction:column; gap:3.5mm; }
.mt { font-size:13pt; font-weight:700; color:NAVY; }
.mt span { font-size:8pt; color:#777; font-weight:400; }
.mbox { flex:1; border:1px solid #c4c4c4; display:flex; flex-direction:column; min-height:0; }
.mbox.ok { border:1.5pt solid NAVY; flex:1.25; }
.mhead { font-size:8.5pt; font-weight:700; padding:1mm 2.5mm; background:#ececec; color:#555; letter-spacing:.08em; }
.mbox.ok .mhead { background:NAVY; color:#fff; }
.mbody { flex:1; display:flex; gap:3mm; padding:3mm; min-height:0; }
.mv { flex:1; height:100%; writing-mode:vertical-rl; font-family:"Noto Serif CJK JP",serif; font-size:9.6pt; line-height:1.75; }
.mv p { text-indent:0; }
.ill.mill { width:22mm; flex:none; order:2; }
.ill.mill .id { font-size:7pt; }

/* 8ページ目 */
.sum { font-family:"Noto Sans CJK JP",sans-serif; font-size:10.3pt; font-weight:700; line-height:1.75; margin:0 .9em 0 1.1em; border-right:2pt solid NAVY; padding-right:.8em; }
.sum p { text-indent:0; }
.todo { font-family:"Noto Sans CJK JP",sans-serif; font-size:9.3pt; line-height:1.65; font-weight:700; background:#f1f1ee; padding:.7em .55em; margin:0 .8em 0 1.2em; }
.tl { display:inline-block; margin-bottom:.8em; font-size:8pt; color:NAVY; }
.foot { font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:NAVY; letter-spacing:.12em; padding-top:1em; }
.note { margin-top:8mm; font-size:10pt; line-height:1.9; color:#333; background:#fff; padding:5mm 7mm; }
.note b { color:NAVY; }
""".replace("NAVY", NAVY)

def page(side, no, tag, inner):
    return (f'<div class="page {side}" data-p="{no}"><div class="tag">{no}ページ目　{tag}</div>{inner}'
            f'<div class="pno">{no}</div></div>')

def spread(n, right, left):
    return (f'<div class="spread"><div class="cap">見開き {n}　　右＝{right[0]}ページ目　／　左＝{left[0]}ページ目</div>'
            f'<div class="pages">{page("left", *left)}{page("right", *right)}</div></div>')

body_n = count(p2, p3, p4, p5, p6, p7, p8)

def build(variant):
    p1, t1, name = ((p1a, "ドカンと二項対立", "案A　1ページ目＝大きな二項対立") if variant == "A"
                    else (p1b, "法則の宣言「〜をやらない」", "案B　1ページ目＝法則の宣言"))
    grid = (spread(1, (1, t1, p1), (2, "Q → 答えの始まり", p2))
            + spread(2, (3, "説明", p3), (4, "上にイラスト、下に説明書き", p4))
            + spread(3, (5, "説明", p5), (6, "やり方を、イラストでページいっぱいに", p6))
            + spread(4, (7, "頭の中（上＝頭のいい人、下＝伸びない人）", p7), (8, "まとめ", p8)))
    doc = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本 8ページ {variant}</title><style>{CSS}</style></head><body>
<div class="sheet">見本　1項目を「見開き4つ・8ページ」で完結させた形（12番）　{name}</div>
<div class="sub">四六判・縦書きを想定。縦書きなので、各見開きは右のページが先です。点線の枠は、イラストが入る場所です（6か所＋1ページ目）。<br>
2〜8ページ目の本文は 約{body_n:,}字（今の12番は約2,480字）。案Aと案Bで違うのは、1ページ目だけです。</div>
<div class="grid">{grid}</div>
</body></html>"""
    io.open(f"build/見本_8ページ_案{variant}.html", "w", encoding="utf-8").write(doc)

build("A"); build("B")
print("2〜8ページ目の本文", body_n, "字 ／ ページ別", [count(x) for x in (p2, p3, p4, p5, p6, p7, p8)])
