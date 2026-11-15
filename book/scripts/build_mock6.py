# -*- coding: utf-8 -*-
# 「見開き3つ・6ページで1つ完結」の見本を作る。12番を、四六判・縦書きで組む。
#   python3 -I scripts/build_mock6.py   → build/見本_6ページ.html
#   node scripts/shot_mock6.js          → build/見本_6ページ.png
# 見開き1＝つかむ（宣言 → Q → A）／見開き2＝わかる（説明 → 図と説明書き）／見開き3＝やる（やり方 → 頭の中とまとめ）
import io, html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_mock8 as m          # 部品（P, ill, page, CSS など）を使う

P, ill, mk, tcy, count = m.P, m.ill, m.mk, m.tcy, m.count

# ---------------------------------------------------------------- 1　法則の宣言 ＋ ×の場面のイラスト
p1 = f'''<div class="p1b">
<div class="lawno"><span class="lw">法則</span><span class="ln">12</span></div>
<div class="lawtag2">絶対法則 ② 思い出す</div>
<div class="decl">
  <div class="d1">頭のいい人は、</div>
  <div class="d2">「黙って、じっと見つめて覚える」</div>
  <div class="d3">を、やらない。</div>
</div>
{ill("イラスト", "教科書を、<br>じっと見つめる子<br>（×の場面）", "ill p1ill")}
<div class="then then6"><span class="bar"></span>じゃあ、何をする？</div>
<div class="next">◀ 次のページへ</div>
</div>'''

# ---------------------------------------------------------------- 2　Q → A → 本文の始まり（8ページ版と同じ）
p2 = m.p2

# ---------------------------------------------------------------- 3　説明（実験2つ）
p3 = ('<div class="v"><h3>目を閉じると、思い出しやすくなります</h3>'
      + P("イギリスのヨーク大学の実験です。映像を見てもらったあと、内容を思い出してもらいます。目を開けたままのグループと、目を閉じたグループ。==目を閉じたほうが、正確に思い出せました。==",
          "目を開けていると、机の上や壁のポスターが、ずっと頭に入ってきます。目を閉じると、それが止まります。そのぶん、頭を、思い出すことに使えます。")
      + '<h3>声に出すと、残りやすくなります</h3>'
      + P("カナダのウォータールー大学の実験です。単語を、声に出して読むものと、黙って読むものに分けます。==声に出した単語のほうが、よく覚えていました。==",
          "声に出すと、口が動き、自分の声が耳から入ります。思い出す手がかりが増えます。",
          "しかも声は、出てこなければ止まります。頭の中で言うのと違って、==ごまかせません。==")
      + '</div>')

# ---------------------------------------------------------------- 4　上に図、下に説明書き
p4 = ('<div class="upper">'
      + ill("イラスト（図解）", "×　開いたまま、黙って、見つめる<br>→ 答えが、目に入り続ける<br><br>○　閉じて、目も閉じて、声に出す<br>→ 出てこないところで、声が止まる", "ill tall")
      + '</div><div class="lower"><div class="v"><h3>図の説明</h3>'
      + P("見つめている間は、答えが目に入り続けます。閉じて声に出すと、入っていないところで、声が止まります。")
      + '<h3>英単語なら</h3>'
      + '<div class="list">' + "".join(f"<p>{mk(x)}</p>" for x in
            ["① 10個だけ、30秒見る", "② 閉じて、声に出す", "③ 出ないものに、印", "④ 印だけ、もう一度"]) + '</div>'
      + '</div></div>')

# ---------------------------------------------------------------- 5　やり方（8ページ版の6ページ目と同じ）
p5 = m.p6

# ---------------------------------------------------------------- 6　頭の中（上＝頭のいい人、下＝伸びない人）＋ まとめ ＋ 今日やること
def hbox(cls, who, lines):
    rows = "".join(f'<div class="{"act" if l.startswith("（") else "say"}">{html.escape(l)}</div>' for l in lines)
    return f'<div class="hb {cls}"><div class="hh">{html.escape(who)}</div><div class="hr">{rows}</div></div>'
p6 = ('<div class="hp6"><div class="mt">頭の中<span>　教科書を読んだあと</span></div>'
      + hbox("ok", "頭のいい人", ["「読んだ。閉じる」", "（目も閉じる）", "「鎌倉幕府ができて、執権が北条氏になって、……そのあと、何だっけ」",
                             "（声が止まる）", "「止まった。そこだけ見よう」", "（1か所だけ見て、また閉じて言う）"])
      + hbox("ng", "伸びない人", ["「もう1回、よく見ておこう」", "（じっと見る）", "「うん、見覚えがある。大丈夫」", "（閉じたら、出てこない）"])
      + '<div class="sm"><div class="smh">この場面のまとめ</div>'
        '<div class="sml">見つめている間は、入れているだけ。</div>'
        '<div class="sml">目を閉じると、思い出しやすくなる。</div>'
        '<div class="sml">声に出すと、残りやすくなる。ごまかせない。</div></div>'
      + '<div class="td"><span>今日やること</span>今日読んだページを1つ選び、本と目を閉じて、書いてあったことを3つ声に出す。</div>'
      + '<div class="ft">もとにある絶対法則　② 思い出す</div></div>')

CSS6 = """
body { width:286mm; }
.grid { display:block; }
.spread { margin-bottom:9mm; }
.job { display:inline-block; background:NAVY; color:#fff; font-size:8.5pt; padding:.5mm 3mm; border-radius:1mm; margin-right:3mm; letter-spacing:.1em; }
.ill.p1ill { position:absolute; left:0; top:12mm; width:35mm; height:58mm; }
.ill.p1ill .id { font-size:7.5pt; }
.then6 { left:13mm; bottom:9mm; }
.lower .list { margin:0 .4em 0 .5em; }
.hp6 { writing-mode:horizontal-tb; width:100%; height:100%; display:flex; flex-direction:column; font-family:"Noto Sans CJK JP",sans-serif; }
.hp6 .mt { margin-bottom:2.5mm; }
.hb { border:1px solid #c4c4c4; margin-bottom:3mm; }
.hb.ok { border:1.5pt solid NAVY; }
.hh { font-size:8.5pt; font-weight:700; padding:.9mm 2.5mm; background:#ececec; color:#555; letter-spacing:.08em; }
.hb.ok .hh { background:NAVY; color:#fff; }
.hr { padding:2mm 3mm 2.2mm; font-family:"Noto Serif CJK JP",serif; }
.say { font-size:9.2pt; line-height:1.6; }
.act { font-size:8pt; line-height:1.6; color:#777; padding-left:1em; }
.sm { border-left:2.2pt solid NAVY; padding:.5mm 0 .5mm 3mm; margin:1.5mm 0 3mm; }
.smh { font-size:9pt; font-weight:700; color:NAVY; margin-bottom:1mm; }
.sml { font-size:9.6pt; font-weight:700; line-height:1.65; }
.td { background:#f1f1ee; font-size:9pt; font-weight:700; line-height:1.6; padding:2mm 2.8mm; }
.td span { display:block; font-size:7.5pt; color:NAVY; letter-spacing:.06em; }
.ft { margin-top:auto; font-size:7.5pt; color:NAVY; letter-spacing:.12em; }
""".replace("NAVY", m.NAVY)

def spread(n, job, right, left):
    return (f'<div class="spread"><div class="cap"><span class="job">{job}</span>見開き {n}　　右＝{right[0]}ページ目　／　左＝{left[0]}ページ目</div>'
            f'<div class="pages">{m.page("left", *left)}{m.page("right", *right)}</div></div>')

parts = [count(p2), count(p3), count(p4), count(p5), count(p6)]
total = sum(parts)
doc = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本 6ページ</title><style>{m.CSS}{CSS6}</style></head><body>
<div class="sheet">見本　1項目を「見開き3つ・6ページ」で完結させた形（12番）</div>
<div class="sub">四六判・縦書きを想定。各見開きは右のページが先です。点線の枠は、イラストが入る場所です。<br>
見開きごとに役目を1つにしました（つかむ → わかる → やる）。2〜6ページ目の本文は 約{total:,}字（今の12番は約2,480字）。</div>
<div class="grid">
{spread(1, "つかむ", (1, "法則の宣言 ＋ ×の場面のイラスト", p1), (2, "Q → 答えの始まり", p2))}
{spread(2, "わかる", (3, "説明（理由と実験）", p3), (4, "上に図、下に説明書き", p4))}
{spread(3, "やる", (5, "やり方を、イラストでページいっぱいに", p5), (6, "頭の中（上下）＋ まとめ ＋ 今日やること", p6))}
</div></body></html>"""
io.open("build/見本_6ページ.html", "w", encoding="utf-8").write(doc)
print("2〜6ページ目の本文", total, "字 ／ ページ別", parts)
