# -*- coding: utf-8 -*-
# 「同じ14番を、4つの形で組んだ見本」。構成と長さを変えて、並べて比べる。
#   python3 -I scripts/build_mock_patterns.py              → build/見本_4つのパターン.html
#   node scripts/shot_mock_tate.js 見本_4つのパターン       → build/見本_4つのパターン.png
# 組み方は、ほかの縦書きの見本と同じ：A5・縦書き・1行40字・1ページ16行。
# 形1 今の形（削らない）／形2 STEPが本文・絵あり／形3 STEPが本文・絵なし／形4 見開き2ページ
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_mock_tate as T
import build_mock_step as S
import tate_model as M
ROOT = os.path.dirname(HERE)
NAME = "見本_4つのパターン"
W, R = 40, 16
OTHER = 145      # 07〜45番のほかのページ（本の形のPDFで、実際に流した数）
P, H, vt = T.P, T.H, T.vt

# ---------------------------------------------------------------- 形4：見開き2ページ。右のページで「つかむ・わかる」、左のページで「やる」
A4 = "数えている間、目は、この本から離れて、上か、遠くを見たはずです。人は、何かを思い出そうとする時、目の前のものから、目を離します。逆に言うと、==教材をじっと見つめている間、頭は、思い出していません。=="
N4 = "じっと見ている間、やっていることは「入れる」だけです。絶対法則02で書いた通り、点になるのは「思い出して、出す」ほうでした。使うのは、==目と、口==です。"
S41 = "開いたままだと、目に答えが入ってきます。それは、思い出しているのではなく、見ているだけです。"
S42 = "目を閉じると、目の前のものが頭に入ってこなくなり、思い出すことに頭を使えます。声に出すと、口と耳も使うので、残りやすくなります。"
S43 = "声は、出てこなければ止まります。==ごまかせません。==止まった所が、まだ覚えていない所です。"


def step(i, cls=""):
    h, v = T.STEPS[i - 1]
    return '<h3 class="sth %s"><span class="slab">STEP<b>0%d</b></span>%s</h3><p class="ssay">「%s」</p>' % (cls, i, vt(h), vt(v))


SHORT = (S.HEAD + T.HQ + P("思い浮かべて、数えてみてください。……", "c") + P(A4)
         + H("なぜ、見つめても覚えられないのか") + P(N4)
         + step(1, "pb") + P(S41) + step(2) + P(S42) + step(3) + P(S43) + S.GOAL)
N_SHORT = T.count("家の玄関に、今、靴は何足、出ていますか？思い浮かべて、数えてみてください。……", A4, "なぜ、見つめても覚えられないのか", N4, S41, S42, S43,
                  "".join(h + v for h, v in T.STEPS))
NOPIC = S.NEW.replace(T.KOMA, "")
assert NOPIC != S.NEW

# ---------------------------------------------------------------- この形で、07〜45番を全部作った時のページ（目安）
its = M.items(W)
rows_all = [r for _, _, r in its]


def total(fixed, n=39):
    """項目ごとにいつも使う行がfixedの時。削らずに流す。n個にした時は、割合で数える。"""
    pages = sum(math.ceil((fixed + r) / R) for r in rows_all)
    return OTHER + round(pages * n / 39)


PATS = [
    ("1", "今の形（削らない）", "srcMax", T.MAX, T.N_MAX, "2コマ",
     "項目の頭 → 本文 → 2コマ → 3STEPのシート → まとめ",
     "今の文を、1字も削らない。やり方は、本文・3STEP・まとめの3か所に出てくる。",
     ["項目の頭 ＋ 問い → 本文", "本文", "本文", "本文の終わり ＋ 2コマ", "3STEP ＋ 基準 ＋ まとめ"], ["つかむ → わかる", "わかる", "やる"],
     "394ページ", "約360ページ", "約300ページ"),
    ("2", "STEPが本文・絵あり", "srcNew", S.NEW, S.N_NEW, "2コマ",
     "項目の頭（×と○）→ 問い → なぜ → 2コマ → STEP01〜03 → 基準と問いの箱",
     "やり方は、STEPの1か所だけ。理由と実験は、そのSTEPの下に置く。文は、ほぼ今のまま。",
     ["項目の頭 ＋ 問い → なぜ", "なぜ ＋ 2コマ → STEP01", "STEP02", "STEP03 ＋ 基準と問い"], ["つかむ → わかる", "やる"],
     "約%dページ" % round(total(16), -1), "約%dページ" % round(total(16, 34), -1), "約%dページ" % round(total(16, 24), -1)),
    ("3", "STEPが本文・絵なし", "srcNoPic", NOPIC, S.N_NEW, "なし",
     "項目の頭（×と○）→ 問い → なぜ → STEP01〜03 → 基準と問いの箱",
     "形2から、2コマを外したもの。6行あくので、王様の一言か、文をあと約200字入れられる。削った版のPDF（319ページ）は、この形。",
     ["項目の頭 ＋ 問い → なぜ", "なぜ → STEP01 → STEP02", "STEP02 → STEP03", "基準と問い"], ["つかむ → わかる", "やる"],
     "約%dページ" % round(total(10), -1), "約%dページ" % round(total(10, 34), -1), "約%dページ" % round(total(10, 24), -1)),
    ("4", "見開き2ページ", "srcShort", SHORT, N_SHORT, "なし",
     "右ページ：項目の頭 → 問い → なぜ　／　左ページ：STEP01〜03 → 基準と問いの箱",
     "開いた2ページで、1項目が終わる。右で「つかむ・わかる」、左で「やる」。実験の話と、場面の話は、入らない。",
     ["項目の頭 ＋ 問い → なぜ", "STEP01〜03 ＋ 基準と問い"], ["つかむ → やる"],
     "約%dページ" % (OTHER + 78), "約%dページ" % (OTHER + 68), "約%dページ" % (OTHER + 48)),
]

CSS = S.CSS + """
.sps{display:flex;flex-wrap:wrap;gap:4px 18px;align-items:flex-start}
.sp{margin:6px 0 10px}
.sphead{font-size:11px;margin-bottom:5px;gap:8px}
.tagc{font-size:10px;padding:0 10px}
.pages{zoom:.51}
.pat{background:#fff;border-radius:10px;padding:14px 18px 6px;margin:18px 0 26px;box-shadow:0 1px 4px rgba(0,0,0,.12)}
.ph{margin:0 0 6px;font-size:17px;font-weight:900;display:flex;align-items:center;gap:12px}
.ph .n{background:#15467e;color:#fff;border-radius:6px;padding:1px 12px;font-size:14px}
.ph small{font-size:12.5px;font-weight:700;color:#a4500a}
.pat .d{font-size:12.5px;line-height:1.8;color:#333;margin:0}
.pat .d b{color:#15467e}
.pat .pages{box-shadow:0 0 0 2px #e8e6e1}
td.c,th.c{text-align:center;white-space:nowrap}
.vt.tight h3{margin-right:0}
"""

JS = T.JS.replace("    else if (el.tagName === 'H3') { if (end % PW === 0) push = COL; }",
                  "    else if (el.classList.contains('pb')) { if (start % PW) push = PW - (start % PW); }\n"
                  "    else if (el.tagName === 'H3') { if (end % PW === 0) push = COL; }")
assert JS != T.JS


def main():
    rows = "".join("<tr><td class='c'><b>%s</b></td><td>%s</td><td class='c' data-p='%s'></td><td class='c'>約%s字</td><td class='c'>%s</td><td class='c'>%s</td><td class='c'>%s</td><td class='c'>%s</td></tr>"
                   % (no, name, src, format(n, ","), pic, a, b, c) for no, name, src, strip, n, pic, parts, memo, labels, tags, a, b, c in PATS)
    out = ['<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>見本　14番を、4つの形で</title><style>' + CSS + "</style></head><body>",
           "<h1>見本　同じ14番を、4つの形で組みました</h1>",
           '<p class="lead">A5・縦書き・1行40字・1ページ16行（類書と同じ組み方）。どれも、実際に文字を流しています。点線の枠は、イラストが入る場所です。</p>',
           '<p class="lead">右の3つの列は、07〜45番を全部その形で作った時の、本全体のページ数の目安です（文は削らない。第1章・前付け・巻末の145ページをふくむ）。</p>',
           "<table><tr><th class='c'>形</th><th>名前</th><th class='c'>14番のページ</th><th class='c'>14番の本文</th><th class='c'>絵</th><th class='c'>全体：45個</th><th class='c'>全体：40個</th><th class='c'>全体：30個</th></tr>" + rows + "</table>",
           '<p class="note" style="margin-top:8px">形3で、長い項目を少し削って4ページと6ページにそろえたものが、先に送った「削った版」のPDF（45個で319ページ）です。'
           '形4は、ページが大きくあくので、あいた分を、柱の項目（6ページ）や、絵に回せます（柱9個を6ページ、ほか30個を見開きにすると、全体は約260ページ）。</p>']
    for no, name, src, strip, n, pic, parts, memo, labels, tags, a, b, c in PATS:
        out.append('<div class="pat"><div class="ph"><span class="n">形%s</span>%s<small data-p2="%s"></small></div><p class="d"><b>並び</b>　%s</p><p class="d">%s</p>%s</div>'
                   % (no, name, src, parts, memo, T.sps(src, labels, tags, "次の項目の<br>1ページ目")))
    out.append('<p class="note">数え方：14番は、実際に文字を流して、16行ごとにページに切りました。全体のページ数は、07〜45番の本文を行に直して数えた目安です（<code>scripts/tate_model.py</code>）。形1の45個は、本の形のPDFで実際に流した数です。'
               '形4の文は、見本のために短くしたものです（実験の大学名などは、入れていません）。本の大きさ、字の大きさ、縦か横かは、まだ決まっていません。</p>')
    out.append('<div class="measure">%s</div>' % "".join('<div class="vt%s" id="%s">%s</div>' % (" tight" if src == "srcShort" else "", src, strip) for _, _, src, strip, *_ in PATS))
    out.append("<script>" + JS + """
document.fonts.ready.then(() => { document.querySelectorAll('.sps').forEach((b) => {
  document.querySelectorAll('[data-p="' + b.dataset.src + '"]').forEach((e) => { e.textContent = b.dataset.pages + 'ページ'; });
  document.querySelectorAll('[data-p2="' + b.dataset.src + '"]').forEach((e) => { e.textContent = b.dataset.pages + 'ページ'; });
}); });
</script></body></html>""")
    with open(os.path.join(ROOT, "build", NAME + ".html"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("14番の本文　形1 %d字／形2・3 %d字／形4 %d字" % (T.N_MAX, S.N_NEW, N_SHORT))
    for no, name, *_rest in PATS:
        print("形%s %s　全体：%s／%s／%s" % (no, name, _rest[-3], _rest[-2], _rest[-1]))


if __name__ == "__main__":
    main()
