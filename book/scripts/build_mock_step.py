# -*- coding: utf-8 -*-
# 「STEPを本文にする形（案）」の見本。07〜45番を、320〜340ページに収めるための形。
#   python3 -I scripts/build_mock_step.py                 → build/見本_STEPが本文の形.html
#   node scripts/shot_mock_tate.js 見本_STEPが本文の形     → build/見本_STEPが本文の形.png
# 組み方は、縦書きの見本（scripts/build_mock_tate.py）と同じ：A5・縦書き・1行40字・1ページ16行。いちばん入らない場合で確かめる。
# 形：項目の頭（×の題と○）→ 問い → なぜ（短く）→ STEP01〜03（やり方と、その理由）→ 「できた」の基準と、自分への問い。
#     3STEPのシートと、まとめは、別に置かない（本文のSTEPと同じことを、もう一度書くことになるため）。
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_mock_tate as T
import tate_model as M
ROOT = os.path.dirname(HERE)
NAME = "見本_STEPが本文の形"
W, R = 40, 16
P, H, vt = T.P, T.H, T.vt

HEAD = ('<div class="blk vhead vhead4"><div class="vlab"><b class="vno">14</b><span class="pill">頭のいい人が絶対やらないこと</span></div>'
        '<div class="vttl">黙って、じっと見つめて覚える</div><div class="vsub"><b>○</b>　目を閉じて、声に出す</div></div>')
C2 = "見つめる人は、教材に向かっています。頭のいい人は、教材から顔を上げています。自習室や図書館で、時々天井を見ている人がいますよね。あれは、さぼっているのではありません。思い出しています。"
D2 = "では、思い出す時、体をどう使えばいいのか。使うのは、==目と、口==です。本を閉じる。目を閉じる。声に出す。この3つを、1つの動作にします。"
S1 = "教材を開いたまま「思い出そう」としても、目に答えが入ってきてしまいます。それは、思い出しているのではなく、見ているだけです。だから、最初に、本を閉じます。"
S3 = "声にはもう1つ、いいところがあります。頭の中で言うと、言えたかどうかを、自分でごまかせます。声は、出てこなければ止まります。==ごまかせません。==止まった所が、まだ覚えていない所です。そこだけ見て、また閉じて、もう一度、言います。"


def step(i, head, say):
    return ('<h3 class="sth"><span class="slab">STEP<b>0%d</b></span>%s</h3><p class="ssay">「%s」</p>' % (i, vt(head), vt(say)))


GOAL = ('<div class="blk vgoal"><div class="gbox"><p class="glab">「できた」の基準</p>' + P("目を閉じたまま、止まらずに最後まで言えたらOK！", "g1")
        + P("迷ったら、自分に聞きます。「目を閉じて、言える？」", "g2") + "</div></div>")

NEW = (HEAD + T.HQ + P("思い浮かべて、数えてみてください。", "c") + P("……", "c") + P(T.A)
       + H("なぜ、見つめても覚えられないのか") + P(T.C) + P(C2) + P(D2) + T.KOMA
       + step(1, *T.STEPS[0]) + P(S1)
       + step(2, *T.STEPS[1]) + P(T.E) + P(T.F) + P(T.H1) + P(T.I)
       + step(3, *T.STEPS[2]) + P(S3)
       + H(T.T5) + P(T.L) + GOAL)
N_NEW = T.count("家の玄関に、今、靴は何足、出ていますか？思い浮かべて、数えてみてください。……", T.A, "なぜ、見つめても覚えられないのか", T.C, C2, D2, S1, T.E, T.F, T.H1, T.I, S3, T.T5, T.L,
                "".join(h + v for h, v in T.STEPS))

CSS = T.CSS + """
.vhead4{width:104px}
.vsub{line-height:26px;font-family:"Noto Sans CJK JP",sans-serif;font-size:13px;font-weight:700;text-align:end;color:#16181d}
.vsub b{color:#15467e;font-weight:900}
.vt h3.sth{margin:0 26px 0 0;color:#16181d;position:relative;padding-top:31px}
.slab{position:absolute;top:0;left:2px;writing-mode:horizontal-tb;width:22px;height:24px;background:#15467e;color:#fff;border-radius:4px;font-size:6px;line-height:1.1;text-align:center;font-weight:700;padding-top:3px;letter-spacing:0}
.slab b{display:block;font-size:10.5px;line-height:1.1}
.vt p.ssay{text-indent:2.6em;font-family:"Noto Sans CJK JP",sans-serif;font-size:12.4px;color:#15467e}
.vgoal{width:78px;padding-right:6px}
.gbox{height:100%;background:#e3ecf7;border-radius:8px;padding:12px 5px}
.gbox p{text-indent:0;font-family:"Noto Sans CJK JP",sans-serif}
.gbox .glab{line-height:14px;font-size:9.5px;font-weight:700;color:#15467e}
.gbox .g1{line-height:24px;font-size:13px;font-weight:900}
.gbox .g2{line-height:24px;font-size:12.4px}
"""


def scen(its, F, total, other):
    """項目ごとにいつも使う行がFの時。全部4ページから始めて、削る量が大きい項目から6ページにする。"""
    cap = lambda p: p * R - F
    plan = {k: 4 for k, _, _ in its}
    used = 4 * len(its)
    for g, _, k in sorted(((min(r, cap(6)) - cap(4), r, k) for k, c, r in its if r > cap(4)), reverse=True):
        if used + 2 > total - other:
            break
        plan[k] = 6; used += 2
    cut = sum(max(0, r - cap(plan[k])) * c / r for k, c, r in its)
    return sum(1 for k in plan if plan[k] == 6), cut


def main():
    its = M.items(W)
    body = sum(c for _, c, _ in its)
    forms = [("今の形", "項目の頭／本文／2コマ／3STEPのシート／まとめ", 23),
             ("STEPを本文にする。2コマは全部に残す", "項目の頭／問い／なぜ／STEP01〜03／2コマ／基準と問い", 16),
             ("STEPを本文にする。2コマは、柱の項目と第1章だけ", "項目の頭／問い／なぜ／STEP01〜03／基準と問い", 10)]
    rows = []
    for name, parts, F in forms:
        free = sum(M.pages_for(r, R) if F == 23 else math.ceil((F + r) / R) for _, _, r in its)
        cells = ""
        for tot in (320, 340):
            n6, cut = scen(its, F, tot, T.OTHER)
            cells += "<td class='num'>約%s字（%d%%）</td>" % (format(int(round(cut, -2)), ","), round(100 * cut / body))
        rows.append("<tr%s><td>%s</td><td>%s</td><td class='num'>%d行</td><td class='num'>約%dページ</td>%s</tr>"
                    % (" class='hl'" if F != 23 else "", name, parts, F, round(T.OTHER + free, -1), cells))
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本　STEPを本文にする形</title><style>' + CSS + "</style></head><body>",
           "<h1>見本　STEPを本文にする形（案）</h1>",
           '<p class="lead">07〜45番を、320〜340ページに収めるための形です。組み方は、縦書きの見本と同じ（A5・縦書き・1行40字・1ページ16行）。いちばん入らない場合で、確かめています。</p>',
           '<p class="lead">今の形は、やり方を3回書いています（本文、3STEPのシート、まとめ）。これを1回にします。STEPを、本文の柱にして、理由や実験は、そのSTEPの下に置きます。</p>',
           '<h2><span class="n">1</span>形ごとの、削る量（07〜45番の本文 約%s字から）</h2>' % format(int(round(body, -2)), ","),
           "<table><tr><th>形</th><th>1項目の中身</th><th>いつも使う行</th><th>削らない時の全体</th><th>320ページにする時</th><th>340ページにする時</th></tr>" + "".join(rows) + "</table>",
           '<p class="note" style="margin-top:8px">「いつも使う行」は、本文のほかに、項目ごとに必ず使う行の数です（1ページは16行）。第1章・前付け・巻末（合わせて%dページ）は、どの形でも同じです。<br>'
           '字を少し小さく（1行44字・18行）するか、横書きにすると、下の2つの形は、ほとんど削らずに320ページに入ります。</p>' % T.OTHER,
           '<h2><span class="n">2</span>14番を、この形で組んだ見本（4ページ。2コマあり）</h2>',
           '<p class="note">本文は 約%s字（今の14番は 約%s字）。今の文を、STEPの下に並べかえました。外したのは、場面の描写の1段落と、×○の2行（項目の頭に入れました）。つなぎの文を、3つ足しています。3STEPのシートと、まとめの中身は、本文のSTEPと、最後の箱に入っています。<br>'
           '2コマを置かない項目は、ここがあと6行（約200字ぶん）あきます。</p>' % (format(N_NEW, ","), format(T.N_MAX, ",")),
           T.sps("srcNew", ["項目の頭 ＋ 問い → なぜ", "なぜ ＋ 2コマ → STEP01", "STEP02", "STEP03 ＋ 基準と問い"], ["つかむ → わかる", "やる"], "次の項目（15番）の<br>1ページ目"),
           '<h2><span class="n">3</span>イラストの数（見本の形で数えた場合）</h2>',
           "<table><tr><th>形</th><th>1項目の絵</th><th>全体</th></tr>"
           "<tr><td>前の横書きの見本</td><td>質問ページ1 ＋ 2コマ2 ＋ STEP3 ＝ 6</td><td class='num'>45項目で 270</td></tr>"
           "<tr><td>縦書きの見本（今の形）</td><td>2コマ2</td><td class='num'>45項目で 90</td></tr>"
           "<tr class='hl'><td>この形（2コマは、柱の10項目と第1章だけ）</td><td>2コマ2。ほかの項目は、絵なし</td><td class='num'>16項目で 32</td></tr></table>",
           '<p class="note" style="margin-top:8px">絵のない項目も、項目の頭の「×の題」と「○」で、2つの対比は残ります。王様の絵は、表情を数点だけ作って、使い回す形にできます。</p>',
           '<p class="note" style="margin-top:26px">数え方：14番は、実際に文字を流して、16行ごとにページに切りました。全体の数は、07〜45番の本文を行に直して数えた目安です（<code>scripts/tate_model.py</code>）。並べかえても本文の行は変わらない、として数えています。本の大きさ、字の大きさ、縦か横か、色の数は、まだ決まっていません。</p>',
           '<div class="measure"><div class="vt" id="srcNew">%s</div></div>' % NEW,
           "<script>" + T.JS + "</script></body></html>"]
    with open(os.path.join(ROOT, "build", NAME + ".html"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("14番　この形 %d字（今 %d字）" % (N_NEW, T.N_MAX))


if __name__ == "__main__":
    main()
