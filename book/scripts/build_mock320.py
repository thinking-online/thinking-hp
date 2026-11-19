# -*- coding: utf-8 -*-
# 「320ページに収める時の構成（案）」の見本を作る。A5・横書きを想定。
#   python3 -I scripts/build_mock320.py   → build/見本_320ページの構成.html
#   node scripts/shot_mock320.js          → build/見本_320ページの構成.png（はみ出しがあれば知らせる）
# 前の見本（build/見本_6ページ.png。12番を、四六判・縦書き・6ページで組んだもの）をもとに、
# 今の形（質問ページ → 本文 → 2コマ → 3STEP → できた基準 → まとめ）と、5章・45項目に合わせた。
# 中身：(1) 全体のページ配分　(2) ふつうの項目＝4ページ（14番で実際に組む）　(3) 柱の項目＝6ページ（07番の割りふり）　(4) 第1章の項目＝12ページ（05番の割りふり）
import html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NAME = "見本_320ページの構成"


def mk(s):
    s = html.escape(s, quote=False)
    return re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)


def P(*ps):
    return "".join("<p>%s</p>" % mk(p) for p in ps)


def ill(label, text, cls=""):
    return '<div class="ill %s"><span>%s</span><div>%s</div></div>' % (cls, label, text)


# ---------------------------------------------------------------- 全体のページ配分（合わせて320）
PLAN = [
    ("前付け", 27, "扉・巻頭の10秒・目次・はじめに・使い方", "c1"),
    ("第1章", 77, "章の扉と導入4 ＋ 6項目×12 ＋ コラム1", "c2"),
    ("第2〜5章の扉と導入", 8, "4章×2", "c3"),
    ("6ページの項目", 60, "10個×6ページ", "c4"),
    ("4ページの項目", 116, "29個×4ページ", "c5"),
    ("コラム", 13, "11本（長い2本は2ページ）", "c6"),
    ("巻末・おわりに", 17, "45を1枚に・6つの言葉・保護者の方へ・参考文献・おわりに", "c7"),
    ("予備", 2, "", "c8"),
]
assert sum(p[1] for p in PLAN) == 320

# ---------------------------------------------------------------- ふつうの項目（14番）。4ページに入る長さにした本文
P1_TOP = '''<div class="qhead">
<div class="no">14</div>
<div class="q1">頭のいい人が絶対やらないこと</div>
<div class="q2">「見つめて覚える」</div>
<div class="q3">じゃあ、何をするの？</div>
</div>''' + ill("イラスト", "教科書を、<br>じっと見つめる子<br>（×の場面）", "illq")
P1_BOTTOM = '''<div class="toi">
<div class="toilab">やってみよう</div>
<div class="toiq">家の玄関に、今、靴は何足、出ていますか？</div>
<div class="toit">思い浮かべて、数えてみてください。</div>
<div class="dots">……</div>
<div class="next">めくる ▶</div>
</div>'''

P2 = (P("数えている間、目は、どこを見ていましたか。この本から目を離して、上か、遠くを見たはずです。目を閉じた人も、いると思います。",
        "人は、何かを思い出そうとする時、目の前のものから、目を離します。目に入ってくるものが、じゃまになるからです。逆に言うと、==教材をじっと見つめている間、頭は、思い出していません。==",
        "歴史のテストが、近づいています。「集中して、じっと見ていれば、頭に入るはず」。教科書を開いて、黙って、見つめます。目は、同じ行の上を、何度もすべっています。20分たって、教科書を閉じます。何が書いてあったか、言おうとしても、出てきません。")
      + "<h3>見つめている間、頭は受け取っているだけです</h3>"
      + P("じっと見るのは、真面目な人ほどやります。静かで、集中しているように見えます。本人も、集中しているつもりです。",
          "でも、やっていることは「入れる」だけです。絶対法則02で書いた通り、点になるのは「思い出して、出す」ほうでした。では、思い出す時、体をどう使えばいいのか。ここが、この項目の話です。使うのは、==目と、口==です。")
      + "<h3>目を閉じると、思い出しやすくなります</h3>"
      + P("イギリスのヨーク大学の研究者たちの実験です。映像を見てもらって、そのあと内容を思い出してもらいます。片方のグループには、目を開けたまま思い出してもらいました。もう片方には、目を閉じて思い出してもらいました。目を閉じたグループのほうが、==見たものも、聞いたものも、正確に思い出せました。==",
          "理由は、単純です。目を開けていると、目の前のものが、ずっと頭に入ってきます。机の上、壁のポスター、窓の外。見るつもりがなくても、頭は、それを全部受け取っています。目を閉じると、それが止まります。そのぶん、頭を、思い出すことに使えます。",
          "教材を見つめたまま「思い出そう」としても、目に答えが入ってきてしまいます。それは、思い出しているのではなく、見ているだけです。"))

P3 = ("<h3>声に出すと、残りやすくなります</h3>"
      + P("もう1つは、口です。カナダのウォータールー大学の研究者たちの実験です。単語のリストを覚えてもらいます。半分の単語は、声に出して読む。もう半分は、黙って読む。あとでテストをすると、==声に出した単語のほうが、よく覚えていました。==",
          "声に出すと、口が動きます。自分の声が、耳から入ってきます。黙って読む時は目だけですが、声に出すと、目と口と耳を使います。思い出す時の手がかりが、増えるんです。",
          "そして、声にはもう1つ、いいところがあります。頭の中で言うと、言えたかどうかを、自分でごまかせます。声は、出てこなければ止まります。==ごまかせません。==")
      + "<h3>2つを、1つの動作にします</h3>"
      + '<pre>×　教材を開いたまま、黙って、見つめる\n○　教材を閉じて、目も閉じて、声に出す</pre>'
      + P("本を閉じる。目を閉じる。声に出す。これで、1つの動作です。",
          "見つめる人は、教材に向かっています。頭のいい人は、教材から顔を上げています。自習室や図書館で、時々天井を見ている人がいますよね。あれは、さぼっているのではありません。思い出しています。")
      + "<h3>声を出せない場所では</h3>"
      + P("電車の中や、図書館では、声が出せません。その時は、口だけ動かします。家に帰ったら、声に出します。家で黙って勉強するのは、もったいないです。"))
KOMA = '''<div class="koma">
<div class="k x"><span>伸びない人</span>''' + ill("絵", "じっと見つめる", "illk") + '''<b>見つめて覚える</b><i>じーっと見れば、入るはず</i></div>
<div class="k o"><span>頭のいい人</span>''' + ill("絵", "目を閉じて、声に出す", "illk") + '''<b>声に出して覚える</b><i>目を閉じて、言える？</i></div>
</div>'''

STEPS = [("覚えたい所を読んだら、本を閉じて、顔を上げる", "見つめない。閉じる", "本を閉じて、<br>顔を上げる"),
         ("目を閉じて、書いてあったことを声に出す", "光合成は、葉で……えーと", "目を閉じて、<br>声に出す"),
         ("声が止まった所だけ見て、もう一度、言う", "ここで止まった。もう1回", "1か所だけ見て、<br>また閉じる")]
P4 = ('<div class="sheet"><div class="sttl">頭のいい人の『暗記のしかた』3STEP</div>'
      + "".join('<div class="st"><div class="stl"><div class="lab">STEP <b>0%d</b></div><div class="do">%s</div><div class="say">「%s」</div></div>%s</div>'
                % (i, mk(h), mk(v), ill("絵", t, "ills")) for i, (h, v, t) in enumerate(STEPS, 1))
      + '<div class="king"><span>「できた」の基準</span><p>目を閉じたまま、止まらずに最後まで言えたらOK！</p></div></div>'
      + '<div class="matome"><div class="mlab">まとめ</div><p class="one">見つめている間は、入れているだけ。</p>'
        '<ol><li>じっと見ても、思い出す回数は0のまま</li><li>目を閉じると、思い出しやすくなる</li><li>声に出すと、残りやすくなる</li></ol>'
        '<p>だから、見つめない。閉じて、声に出す。</p><p>迷ったら、自分に聞きます。「目を閉じて、言える？」</p></div>'
      + '<div class="hito"><span>王様の一言</span><p>（入れる項目だけ。まとめの下の、空いた所に置く）</p></div>')


def count(h):
    return len(re.sub(r"\s", "", re.sub(r"<[^>]+>", "", h)))


def page(no, label, inner, cls=""):
    return ('<div class="page %s"><div class="chip">%s</div><div class="body">%s</div><div class="folio">%s</div></div>'
            % (cls, label, inner, no))


def ghost(text):
    return '<div class="page ghost"><div class="gtext">%s</div></div>' % text


def spread(tag, title, left, right):
    return ('<div class="sp"><div class="sphead"><span class="tagc">%s</span>%s</div><div class="pages">%s%s</div></div>'
            % (tag, title, left, right))


# ---------------------------------------------------------------- 小さい図（割りふりだけを見せる）
def thumb(no, blocks, cls=""):
    """blocks: [(高さの割合, 種類, 言葉)]。種類：t=本文 q=質問 i=絵 s=シート m=まとめ d=章のページ g=前後の項目"""
    inner = "".join('<div class="b b%s" style="flex:%s">%s</div>' % (k, f, w) for f, k, w in blocks)
    return '<div class="th %s"><div class="thin">%s</div><div class="thno">%s</div></div>' % (cls, inner, no)


def thumbs(pairs):
    return '<div class="throw">' + "".join('<div class="thsp">%s%s</div>' % (a, b) for a, b in pairs) + "</div>"


G = lambda w: thumb("", [(1, "g", w)], "tg")

PILLAR = thumbs([
    (G("前の項目の<br>最後のページ"), thumb("1", [(5, "q", "質問ページ<br>「わかったつもりで次へ」"), (4, "i", "問い<br>ファスナーは、<br>どうやって閉まる？")])),
    (thumb("2", [(1, "t", "問いの答え"), (3, "t", "「わかった」の3つの段"), (2, "t", "ファインマンの話")]),
     thumb("3", [(3, "t", "教えるつもりで<br>入れるだけで、変わる<br>（実験）"), (3, "t", "KW言語化勉強法<br>型と、やること3つ")])),
    (thumb("4", [(3, "t", "光合成でやってみる"), (2, "t", "力が2つ、つく"), (2, "t", "声に出す。<br>止まったら、そこだけ")]),
     thumb("5", [(2, "t", "いきなり全部はやらない"), (2, "t", "相手がいなくても。AI"), (2, "t", "型は、復習の道具"), (3, "i", "2コマ")])),
    (thumb("6", [(6, "s", "3STEP<br>できた基準"), (3, "m", "まとめ"), (1, "m", "王様の一言")]), G("次の項目の<br>1ページ目")),
])

CH1 = thumbs([
    (G("前の項目の<br>最後のページ"), thumb("1", [(1, "d", "章最初のページ<br>絶対法則05　分散<br>まとめてやらない。<br>分けて、繰り返す")])),
    (thumb("2", [(1, "t", "導入文<br>「一夜漬けは、<br>やめなさい」")]), thumb("3", [(6, "q", "質問ページ<br>「まとめて一気にやる」"), (4, "i", "絵")])),
    (thumb("4", [(4, "i", "問い<br>腹筋300回"), (3, "t", "前の日に覚えたこと")]), thumb("5", [(3, "t", "7×8と九九"), (4, "t", "【研究結果】<br>同じ2回でも、間をあけると")])),
    (thumb("6", [(3, "t", "まとめてやると、<br>すぐあとには効く"), (3, "t", "同じ3時間を、<br>3日に分ける")]), thumb("7", [(1, "t", "テストの範囲は、<br>授業の日に決まっている")])),
    (thumb("8", [(1, "t", "2回目は、<br>何日あければいいか")]), thumb("9", [(3, "t", "1日の中では？"), (2, "t", "決めることは1つ")])),
    (thumb("10", [(1, "i", "2コマ<br>（1ページ使う）")]), thumb("11", [(1, "s", "3STEP<br>できた基準")])),
    (thumb("12", [(5, "m", "まとめ"), (2, "m", "王様の一言"), (3, "g", "（余白）")]), G("次の項目、<br>またはコラム")),
])

CSS = """
*{box-sizing:border-box}
html{font-family:"Noto Sans CJK JP","Noto Sans JP",sans-serif;color:#16181d;background:#e8e6e1}
body{margin:0;padding:34px 40px 60px;width:1180px}
h1{font-size:24px;font-weight:900;color:#15467e;margin:0 0 10px}
.lead{font-size:13px;line-height:1.9;margin:0 0 4px;color:#333}
h2{font-size:17px;font-weight:900;margin:44px 0 6px;display:flex;align-items:center;gap:12px}
h2 .n{background:#15467e;color:#fff;border-radius:6px;padding:1px 12px;font-size:14px}
.note{font-size:12.5px;line-height:1.9;color:#333;margin:0 0 14px}
mark{background:linear-gradient(transparent 55%,#ffe37a 55%);color:inherit}
/* 全体の配分 */
.bar{display:flex;height:64px;border-radius:8px;overflow:hidden;margin:12px 0 8px;background:#fff}
.bar div{display:flex;flex-direction:column;justify-content:center;align-items:center;font-size:11px;line-height:1.35;color:#fff;font-weight:700;white-space:nowrap;overflow:hidden}
.bar b{font-size:16px}
.c1{background:#7a8594}.c2{background:#15467e}.c3{background:#5d7fa8}.c4{background:#a4500a}.c5{background:#d08a3c}.c6{background:#6b8f5a}.c7{background:#7a8594}.c8{background:#b9bec7}
.leg{display:grid;grid-template-columns:repeat(4,1fr);gap:6px 18px;font-size:12px;line-height:1.6;margin-bottom:10px}
.leg i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:6px;vertical-align:-1px}
.leg b{font-weight:900}
.leg span{color:#555}
table{border-collapse:collapse;background:#fff;font-size:12.5px;margin-top:6px}
th,td{border:1px solid #cfd4dc;padding:6px 12px;text-align:left;line-height:1.6}
th{background:#eef1f6;font-weight:700}
td.num{text-align:right;font-weight:700}
/* 見開き */
.sp{margin:16px 0 26px}
.sphead{font-size:13.5px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;gap:12px}
.tagc{background:#15467e;color:#fff;border-radius:99px;padding:1px 14px;font-size:12px}
.pages{display:flex;gap:0;background:#fff;width:1006px;box-shadow:0 1px 4px rgba(0,0,0,.15)}
.page{width:503px;height:714px;position:relative;padding:46px 44px 40px;border-right:1px solid #e3e3e3}
.page:last-child{border-right:0}
.chip{position:absolute;top:14px;left:44px;background:#15467e;color:#fff;font-size:10.5px;border-radius:4px;padding:1px 10px;line-height:1.7}
.folio{position:absolute;bottom:12px;left:0;right:0;text-align:center;font-size:10px;color:#888}
.body{height:628px;overflow:hidden;font-size:11px;line-height:1.75}
.body p{margin:0 0 7px;text-align:justify}
.body h3{font-size:12.5px;font-weight:900;margin:12px 0 5px;padding-left:8px;border-left:4px solid #15467e;line-height:1.5}
.body pre{font-family:inherit;font-size:10.5px;line-height:1.8;background:#f1f3f7;border-radius:5px;padding:7px 12px;margin:5px 0 8px;white-space:pre-wrap}
.ghost{background:#f3f2ef;display:flex;align-items:center;justify-content:center}
.gtext{font-size:13px;color:#888;text-align:center;line-height:1.9}
.ill{border:1.5px dashed #9aa0a8;background:#f0efeb;border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;color:#666;font-size:10.5px;line-height:1.6}
.ill span{position:absolute;top:5px;left:6px;background:#7a7f87;color:#fff;font-size:8.5px;border-radius:3px;padding:0 6px;line-height:1.6}
/* 1ページ目 */
.qhead{background:#15467e;color:#fff;border-radius:12px;padding:16px 20px 18px;text-align:center}
.qhead .no{text-align:left;font-size:22px;font-weight:900;line-height:1}
.qhead .q1{font-size:11.5px;margin-top:2px}
.qhead .q2{font-size:25px;font-weight:900;line-height:1.5;margin:4px 0}
.qhead .q3{font-size:13px;font-weight:700}
.illq{height:236px;margin:14px 0 18px}
.toi{border:2px solid #15467e;border-radius:10px;padding:20px 20px 14px;position:relative}
.toilab{position:absolute;top:-10px;left:16px;background:#fff;color:#15467e;font-size:10.5px;font-weight:700;padding:0 8px}
.toiq{font-size:18px;font-weight:900;line-height:1.6}
.toit{font-size:11.5px;margin-top:4px}
.dots{font-size:18px;margin-top:16px;letter-spacing:.2em}
.next{text-align:right;font-size:10.5px;color:#15467e;font-weight:700}
/* 2コマ */
.koma{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.koma .k{border-radius:8px;padding:8px 10px 10px;text-align:center}
.koma .x{background:#eceef2}.koma .o{background:#e3ecf7;border:1px solid #15467e}
.koma span{font-size:9.5px;color:#555}
.koma b{display:block;font-size:14px;font-weight:900;line-height:1.5;margin-top:5px}
.koma i{display:block;font-style:normal;font-size:10px}
.illk{height:70px;margin-top:4px;background:#fff}
/* 3STEP */
.sheet{border:1.5px solid #15467e;border-radius:8px;padding:10px 14px 12px}
.sttl{font-size:13.5px;font-weight:900;border-bottom:2px solid #15467e;padding-bottom:4px;margin-bottom:4px}
.st{display:grid;grid-template-columns:1fr 112px;gap:12px;align-items:center;padding:7px 0;border-bottom:1px solid #dfe3ea}
.lab{display:inline-block;background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 10px;line-height:1.7}
.lab b{font-size:11px}
.do{font-size:12px;font-weight:700;line-height:1.55;margin:4px 0 3px}
.say{display:inline-block;border:1px solid #15467e;border-radius:8px;padding:0 9px;font-size:10.5px;line-height:1.8}
.ills{height:66px}
.king{display:flex;gap:10px;align-items:center;background:#e3ecf7;border-radius:6px;padding:7px 10px;margin-top:9px}
.king span{background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 9px;white-space:nowrap;line-height:1.8}
.king p{margin:0;font-size:11.5px;font-weight:700;line-height:1.5}
.matome{background:#f7f5ee;border-radius:8px;padding:10px 16px 8px;margin-top:10px}
.mlab{font-size:9.5px;font-weight:700;color:#15467e}
.matome .one{font-size:13px;font-weight:900;margin:2px 0 3px}
.matome ol{margin:0 0 4px 1.5em;padding:0;font-size:11px;line-height:1.75}
.matome p{margin:0 0 1px;font-size:11px}
.hito{border:1.5px dashed #9aa0a8;border-radius:8px;padding:6px 12px;margin-top:9px}
.hito span{background:#16181d;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 9px;line-height:1.8}
.hito p{margin:3px 0 0;font-size:10px;color:#666}
/* 小さい図 */
.throw{display:flex;gap:14px;flex-wrap:wrap}
.thsp{display:flex;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.th{width:124px;height:176px;position:relative;padding:8px 8px 16px;border-right:1px solid #e3e3e3}
.thsp .th:last-child{border-right:0}
.thin{display:flex;flex-direction:column;gap:4px;height:100%}
.thno{position:absolute;bottom:2px;left:0;right:0;text-align:center;font-size:9px;color:#888}
.b{border-radius:4px;font-size:9.5px;line-height:1.45;display:flex;align-items:center;justify-content:center;text-align:center;padding:2px 4px;overflow:hidden}
.bt{background:#eef1f6;color:#333}
.bq{background:#15467e;color:#fff;font-weight:700}
.bi{border:1.5px dashed #9aa0a8;background:#f0efeb;color:#555}
.bs{border:1.5px solid #15467e;color:#15467e;font-weight:700}
.bm{background:#f7f5ee;color:#333}
.bd{background:#fff;border:1.5px solid #15467e;color:#15467e;font-weight:700}
.bg{background:#f3f2ef;color:#999}
.tg{background:#f3f2ef}
"""


def main():
    n2, n3 = count(P2), count(P3)
    total = sum(p[1] for p in PLAN)
    bar = "".join('<div class="%s" style="flex:%d"><b>%d</b>%s</div>' % (c, n, n, name if n >= 13 else "") for name, n, d, c in PLAN)
    leg = "".join('<div><i class="%s"></i><b>%s　%dページ</b><br><span>%s</span></div>' % (c, name, n, d) for name, n, d, c in PLAN)
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本　320ページに収める時の構成</title><style>' + CSS + "</style></head><body>",
           "<h1>見本　320ページに収める時の構成（案）</h1>",
           '<p class="lead">A5・横書きを想定。点線の枠は、イラストが入る場所です。前の見本（12番を6ページで組んだもの）をもとに、今の形（質問ページ → 本文 → 2コマ → 3STEP → できた基準 → まとめ）に合わせました。</p>',
           '<p class="lead">やることは3つです。(1) 1文ごとの改行を、2〜4文の段落にまとめる。(2) 質問ページと問いを1ページに、3STEP・できた基準・まとめを1ページに入れる。(3) 項目を、長さで、4ページと6ページに分ける。</p>',
           '<h2><span class="n">1</span>全体のページ配分（合わせて%dページ）</h2>' % total,
           '<div class="bar">%s</div><div class="leg">%s</div>' % (bar, leg),
           "<table><tr><th>項目の種類</th><th>数</th><th>1項目のページ</th><th>本文に入る字数</th><th>今の原稿</th></tr>"
           "<tr><td>第1章の項目（6つの絶対法則）</td><td class='num'>6</td><td class='num'>12</td><td>約5,000字まで</td><td>平均 約4,400字。そのまま入る</td></tr>"
           "<tr><td>6ページの項目（型や考え方を、最初から説明する）</td><td class='num'>10</td><td class='num'>6</td><td>約3,200字まで</td><td>今、2,000字をこえる10個（07 09 17 19 21 25 29 34 37 39）。そのまま入る</td></tr>"
           "<tr><td>4ページの項目</td><td class='num'>29</td><td class='num'>4</td><td>約1,450字まで</td><td>11個は、そのまま入る。18個は、1項目あたり50〜450字（平均 約230字）削る</td></tr></table>",
           '<p class="note" style="margin-top:8px">削る量は、合わせて約4,000字（07〜45番の本文 約69,500字の、約6%）。どの項目を6ページにするかは、著者が決める。</p>',
           '<h2><span class="n">2</span>4ページの項目（14番で、実際に組んだ見本）</h2>',
           '<p class="note">項目は、いつも右のページから始めます。右に「質問ページと、問い」。めくると、答えと本文。もう1回めくると、左に「3STEPとまとめ」、右に次の項目。問いの答えは、必ず、めくった先に来ます。<br>'
           '2〜3ページ目には、今の14番の本文を、段落にまとめて、そのまま入れました（合わせて約%d字。2ページ目 %d字、3ページ目 %d字と2コマ。削ったのは、3ページ目の1文だけ）。</p>' % (n2 + n3, n2, n3),
           spread("つかむ", "見開き1　　右＝1ページ目", ghost("前の項目（13番）の<br>4ページ目<br>3STEP・まとめ"), page("1", "1ページ目　質問ページ ＋ 問い", P1_TOP + P1_BOTTOM)),
           spread("わかる", "見開き2　　左＝2ページ目　／　右＝3ページ目", page("2", "2ページ目　問いの答え → 本文", P2), page("3", "3ページ目　本文の続き ＋ 2コマ", P3 + KOMA)),
           spread("やる", "見開き3　　左＝4ページ目", page("4", "4ページ目　3STEP ＋ できた基準 ＋ まとめ", P4), ghost("次の項目（15番）の<br>1ページ目<br>質問ページ ＋ 問い")),
           '<h2><span class="n">3</span>6ページの項目（07番「人に教えるつもり」の割りふり）</h2>',
           '<p class="note">始まり方と終わり方は、4ページの項目と同じ。間の本文が、2ページ増えます。今の07番（約2,600字）が、そのまま入ります。</p>',
           PILLAR,
           '<h2><span class="n">4</span>第1章の項目 ＝ 12ページ（05番「分散」の割りふり）</h2>',
           '<p class="note">章最初のページ、導入文、質問ページに、1ページずつ使います。2コマと3STEPも、1ページずつ。第1章だけは、ゆったり組みます。</p>',
           CH1,
           '<p class="note" style="margin-top:26px">数え方：4ページの項目は、実際に文字を入れて、入る量を確かめました（A5、字の大きさ 約9ポイント、1行37字、1ページ32行）。6ページの項目と第1章は、割りふりの図です（文字は入れていません）。字を大きくしたり、本を小さく（四六判に）したりすると、入る量は1〜2割減ります。本の大きさ、字の大きさ、イラストの数は、まだ決まっていないので、ページ数は目安です。</p>',
           "</body></html>"]
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    with open(os.path.join(ROOT, "build", NAME + ".html"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("2ページ目 %d字／3ページ目 %d字／合わせて %d字" % (n2, n3, n2 + n3))


if __name__ == "__main__":
    main()
