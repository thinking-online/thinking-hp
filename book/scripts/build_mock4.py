# -*- coding: utf-8 -*-
# 「見開き4ページで1つ完結」の見本を作る。12番を約1,400字にして、四六判・縦組みで組む。
#   python3 -I scripts/build_mock4.py   → build/見本_4ページ完結_12番.html
#   そのあと node scripts/shot_mock4.js で PNG と PDF にする
import io, re, html

NAVY = "#15467E"

def tcy(s):
    # 1〜2けたの数字を、縦中横にする
    return re.sub(r"(?<![0-9A-Za-z])([0-9]{1,2})(?![0-9A-Za-z])", r'<span class="tcy">\1</span>', s)

def mk(s):
    s = html.escape(s)
    s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
    return tcy(s)

def P(*lines):
    return "".join(f"<p>{mk(l)}</p>" for l in lines)

def count(*chunks):
    t = re.sub(r"<[^>]+>", "", "".join(chunks))
    return len(re.sub(r"\s", "", html.unescape(t)))

# ---------------------------------------------------------------- 1ページ目
p1_text = (
    '<div class="law">絶対法則 ② 思い出す</div>'
    f'<h2><span class="no">{tcy("12")}</span>黙って、じっと見つめて覚える</h2>'
    '<div class="pair"><div class="x"><span class="s">×</span>集中して見ていれば、頭に入る</div>'
    '<div class="o"><span class="s">○</span>目を閉じて、声に出す</div></div>'
    + P("歴史のテスト前。教科書を開いて、黙って、じっと見ています。",
        "10分経ちました。ページは、めくっていません。目は、同じ行の上を何度もすべっています。")
    + '<p class="q">「集中して見ていれば、頭に入るはず」</p>'
    + P("20分経って、教科書を閉じます。何が書いてあったか、言おうとしても、出てきません。",
        "真面目な人ほど、これをやります。")
)
p1_fig = ('<div class="fig"><div class="figl">イラスト ①　場面</div>'
          '<div class="figd">教科書をじっと見つめる中学生。<br>時計は20分進んでいる。ページはそのまま。<br>'
          '頭の上に「入ってるはず……」</div></div>')

# ---------------------------------------------------------------- 2ページ目
p2 = (
    "<h3>見つめている間、頭は受け取っているだけです</h3>"
    + P("点になるのは、「思い出して、出す」ほうでした（02番）。では、思い出す時、体をどう使えばいいのか。使うのは、==目と、口==です。")
    + "<h3>目を閉じると、思い出しやすくなります</h3>"
    + P("イギリスのヨーク大学の実験です。映像を見てもらったあと、内容を思い出してもらいます。目を開けたままのグループと、目を閉じたグループ。==目を閉じたほうが、正確に思い出せました。==",
        "目を開けていると、机の上や壁のポスターが、ずっと頭に入ってきます。目を閉じると、それが止まります。そのぶん、頭を、思い出すことに使えます。")
    + "<h3>声に出すと、残りやすくなります</h3>"
    + P("カナダのウォータールー大学の実験です。単語を、声に出して読むものと、黙って読むものに分けます。==声に出した単語のほうが、よく覚えていました。==",
        "声に出すと、口が動いて、自分の声が耳から入ります。目だけでなく、口と耳も使うので、思い出す時の手がかりが増えます。",
        "しかも声は、出てこなければ止まります。頭の中で言うのと違って、==ごまかせません。==")
)

# ---------------------------------------------------------------- 3ページ目
p3_text = (
    "<h3>頭の中</h3>"
    '<div class="box ng"><div class="bl">教科書を読んだあと、伸びない人</div>'
    + P("「もう1回、よく見ておこう」", "（じっと見る）", "「うん、見覚えがある。大丈夫」", "（閉じたら、出てこない）")
    + "</div>"
    '<div class="box ok"><div class="bl">同じ時、頭のいい人</div>'
    + P("「読んだ。閉じる」", "（目も閉じる）", "「鎌倉幕府ができて、執権が北条氏になって、……そのあと、何だっけ」",
        "（声が止まる）", "「止まった。そこだけ見よう」", "（1か所だけ見て、また閉じて、声に出す）")
    + "</div>"
)
p3_fig = ('<div class="dia"><div class="figl">イラスト ②　図解</div>'
          '<div class="row"><div class="b x2">×　開いたまま、黙って、見つめる</div><div class="ar">→</div>'
          '<div class="r">入った「気がする」だけ</div></div>'
          '<div class="row"><div class="b o2">○　閉じて、目も閉じて、声に出す</div><div class="ar">→</div>'
          '<div class="r"><b>出せるかどうかが、わかる</b></div></div></div>')

# ---------------------------------------------------------------- 4ページ目
def step(n, head, body):
    return f'<div class="step"><div class="sh"><span class="sn">STEP {tcy(n)}</span>{mk(head)}</div>{P(body)}</div>'
p4 = (
    "<h3>やり方</h3>"
    + step("01", "読んだら、本を閉じて、顔を上げる", "答えが目に入らないようにします。本を見つめたまま「思い出そう」としても、それは見ているだけです。")
    + step("02", "目を閉じて、止まるまで声に出す", "天井を見るのでもいいです。声を出せない場所では、口だけ動かします。")
    + step("03", "止まったところだけ見て、もう一度言う", "声が止まった場所が、まだ入っていない場所です。")
    + '<div class="kijun"><span class="kl">「できた」の基準</span>' + mk("目を閉じたまま、止まらずに最後まで言えた。次の日にも、言えた。") + "</div>"
    + "<h3>この場面のまとめ</h3>"
    + P("じっと見ていた20分は、閉じた時に何も出てこなければ、0です。閉じて声に出した5分は、出てきたぶんだけ、確実に残ります。",
        "見つめている間は、入れているだけ。閉じて、目も閉じて、声に出す。")
    + '<div class="todo"><span class="tl">今日やること</span>' + mk("今日読んだページを1つ選び、本と目を閉じて、書いてあったことを3つ声に出す。") + "</div>"
)

n1, n2, n3, n4 = count(p1_text), count(p2), count(p3_text), count(p4)
total = n1 + n2 + n3 + n4

CSS = f"""
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:"Noto Sans CJK JP",sans-serif; background:#e9e7e2; color:#111; padding:10mm 10mm 12mm; width:286mm; }}
.sheet {{ font-size:13pt; font-weight:700; color:{NAVY}; margin-bottom:2mm; }}
.sub {{ font-size:9pt; color:#555; margin-bottom:7mm; line-height:1.7; }}
.cap {{ font-size:9.5pt; font-weight:700; color:#333; margin:0 0 2.5mm 1mm; }}
.spread {{ margin-bottom:9mm; }}
.pages {{ display:flex; width:254mm; box-shadow:0 2px 10px rgba(0,0,0,.18); }}
.page {{ width:127mm; height:188mm; background:#fff; position:relative; padding:17mm 15mm 17mm 15mm; }}
.page.left  {{ border-right:1px solid #ddd; padding-right:18mm; }}
.page.right {{ padding-left:18mm; }}
.pno {{ position:absolute; bottom:7mm; font-size:7.5pt; color:#888; }}
.page.left .pno {{ left:15mm; }} .page.right .pno {{ right:15mm; }}
.tag {{ position:absolute; top:6.5mm; font-size:7pt; color:#fff; background:{NAVY}; padding:.6mm 2.2mm; border-radius:1mm; letter-spacing:.05em; }}
.page.left .tag {{ left:15mm; }} .page.right .tag {{ right:15mm; }}

.v {{ writing-mode:vertical-rl; width:100%; height:100%; font-family:"Noto Serif CJK JP",serif;
     font-size:10pt; line-height:1.82; text-align:justify; overflow:visible; }}
.v p {{ text-indent:1em; }}
.v p.q {{ text-indent:0; padding-top:2em; margin:0 .35em; }}
.tcy {{ text-combine-upright:all; -webkit-text-combine:horizontal; }}
mark {{ background:#fff3a6; color:inherit; }}
.law {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:7.5pt; color:{NAVY}; letter-spacing:.12em; margin-left:1.2em; }}
h2 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:15pt; font-weight:700; line-height:1.35; margin-left:.9em; letter-spacing:.03em; }}
h2 .no {{ color:{NAVY}; font-size:17pt; margin-bottom:.45em; display:inline-block; }}
.pair {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; line-height:1.6; border-right:2.2pt solid {NAVY};
        padding:.2em .8em .2em .2em; margin-left:1.3em; }}
.pair .x {{ color:#888; }} .pair .o {{ color:{NAVY}; font-weight:700; }}
.pair .s {{ display:inline-block; margin-bottom:.5em; }}
h3 {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:10.5pt; font-weight:700; color:{NAVY}; line-height:1.4;
      margin:0 .75em 0 .45em; }}
.v > h3:first-child {{ margin-right:0; }}

.upper {{ height:60.5%; }}
.lower {{ height:34.5%; margin-top:6.5%; }}
.fig, .dia {{ writing-mode:horizontal-tb; width:100%; height:100%; border:1px dashed #9a9a9a; background:#f5f4ef;
      font-family:"Noto Sans CJK JP",sans-serif; display:flex; flex-direction:column; align-items:center; justify-content:center;
      text-align:center; position:relative; }}
.figl {{ position:absolute; top:2mm; left:2.5mm; font-size:7pt; color:#fff; background:#8a8a8a; padding:.4mm 2mm; border-radius:1mm; }}
.figd {{ font-size:8.5pt; color:#666; line-height:1.9; }}
.dia {{ padding:6.5mm 3mm 1.5mm; gap:2.2mm; background:#fff; border:1px solid #cfcfcf; }}
.dia .row {{ display:flex; align-items:center; width:100%; font-size:8pt; }}
.dia .b {{ flex:none; width:47mm; padding:1.6mm 2mm; border-radius:1.2mm; text-align:left; white-space:nowrap; }}
.dia .x2 {{ background:#efefef; color:#666; }}
.dia .o2 {{ background:{NAVY}; color:#fff; font-weight:700; }}
.dia .ar {{ flex:none; width:5mm; color:#888; text-align:center; }}
.dia .r {{ flex:1; text-align:left; line-height:1.4; white-space:nowrap; font-size:7.6pt; }}

.box {{ border:1px solid #c9c9c9; padding:.7em .55em; margin:0 .5em; font-size:9.5pt; line-height:1.72; }}
.box p {{ text-indent:0; }}
.box.ok {{ border:1.4pt solid {NAVY}; }}
.bl {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:8pt; font-weight:700; margin-left:.5em; color:#666; }}
.box.ok .bl {{ color:{NAVY}; }}

.step {{ margin-left:.55em; }}
.sh {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9.5pt; font-weight:700; line-height:1.5; }}
.sn {{ color:{NAVY}; font-size:8pt; letter-spacing:.08em; display:inline-block; margin-bottom:.7em; }}
.step p {{ text-indent:0; padding-top:1em; font-size:9.5pt; line-height:1.72; }}
.kijun {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt; line-height:1.6; color:{NAVY}; font-weight:700;
         border:1.2pt solid {NAVY}; padding:.6em .5em; margin:0 .9em 0 .9em; }}
.kl {{ display:inline-block; margin-bottom:.8em; font-size:8pt; }}
.todo {{ font-family:"Noto Sans CJK JP",sans-serif; font-size:9pt; line-height:1.6; font-weight:700; background:#f1f1ee;
        padding:.6em .5em; margin-right:.7em; }}
.tl {{ display:inline-block; margin-bottom:.8em; font-size:8pt; color:{NAVY}; }}
.note {{ font-size:9pt; line-height:1.85; color:#333; background:#fff; padding:5mm 6mm; width:254mm; }}
.note b {{ color:{NAVY}; }}
"""

def page(side, no, tag, inner):
    return (f'<div class="page {side}" data-p="{no}"><div class="tag">{tag}</div>{inner}'
            f'<div class="pno">{no}</div></div>')

doc = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本 4ページ完結</title><style>{CSS}</style></head><body>
<div class="sheet">見本　1項目を「見開き2つ・4ページ」で完結させた形（12番）</div>
<div class="sub">四六判・縦書きを想定（1ページ 43字×15行）。縦書きなので、右のページが先です。本文 約{total:,}字（今の12番は約2,480字）＋イラスト2点。</div>

<div class="spread"><div class="cap">見開き 1　　右＝1ページ目　／　左＝2ページ目</div><div class="pages">
{page("left", 2, f"2ページ目　なぜ　約{n2}字", f'<div class="v">{p2}</div>')}
{page("right", 1, f"1ページ目　タイトル・場面　約{n1}字＋イラスト", f'<div class="upper"><div class="v">{p1_text}</div></div><div class="lower">{p1_fig}</div>')}
</div></div>

<div class="spread"><div class="cap">見開き 2　　右＝3ページ目　／　左＝4ページ目</div><div class="pages">
{page("left", 4, f"4ページ目　やり方・まとめ　約{n4}字", f'<div class="v">{p4}</div>')}
{page("right", 3, f"3ページ目　頭の中　約{n3}字＋図解", f'<div class="upper" style="height:71%"><div class="v">{p3_text}</div></div><div class="lower" style="height:23%;margin-top:6%">{p3_fig}</div>')}
</div></div>

<div class="note"><b>この形にするために、12番から外したもの</b><br>
・英単語の覚え方（4つの手順）と、「書くかどうか」の表　→　章の終わりのコラム（1〜2ページ）に移す。巻頭で聞いた「英単語は、どう思い出して、どう出すのか」の答えなので、消さずに場所を変える。<br>
・「声を出せない場所では」「2つを、1つの動作にします」「これをやると、何が残るか」の3つの節　→　大事な1文だけを、STEPと「頭の中」に入れた。<br>
・実験の説明　→　2つとも残したが、それぞれ半分の長さにした。</div>
</body></html>"""
io.open("build/見本_4ページ完結_12番.html", "w", encoding="utf-8").write(doc)
print("字数", n1, n2, n3, n4, "計", total)
