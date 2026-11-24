# -*- coding: utf-8 -*-
# 「体系を見える形にする」案（2026-11-24。著者「どっちもしてみて欲しい」。まだ、本には入れていない）
#   1) 各項目の頭に「もとは：絶対法則02」の札をつける
#   2) 6つの絶対法則と、章のつながりを、1枚の図にする
#   python3 -I scripts/fuda.py 出す先.html [--pdf]
# 対応（どの項目が、どの法則から来ているか）は、下の FUDA。主は1つ。副は、あっても1つ。
import html, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import zenbu as Z

# 法則の番号: (名前, 図に入れる一言。どれも、第1章の「まとめ」にある言葉)
LAW = {
    "01": ("疑う", "自分の当たり前を、一度疑う"),
    "02": ("思い出す", "読んだら、閉じる"),
    "03": ("負荷", "少しきついほうを選ぶ"),
    "04": ("戦略", "始める前に、ゴールを見る"),
    "05": ("分散", "2回目は、別の日にやる"),
    "06": ("速度", "さっさと失敗して、さっさと直す"),
}
# 項目: (主, 副, 理由, 確かさ)　確かさ：◎＝本文で、その法則に戻っている／○＝中身が合う／△＝つながりが弱い（著者に見てもらう）
FUDA = {
    "07": ("02", "03", "説明は、何も見ずに思い出すこと", "◎"),
    "08": ("06", None, "1回目から完璧にしない。先に全体を見て、進む", "◎"),
    "09": ("02", None, "区切るたびに、1分、思い出す", "◎"),
    "10": ("01", None, "「読めた感じ」を疑って、図にできるかで確かめる", "◎"),
    "11": ("03", None, "「これって、つまりは？」と考える時間が、負荷", "△"),
    "12": ("02", "05", "残るのは、書いた回数ではなく、思い出した回数", "◎"),
    "13": ("02", None, "目を閉じて声に出すのは、思い出すこと", "○"),
    "14": ("03", None, "意味を絵にする3秒が、頭を使う時間", "△"),
    "15": ("02", "06", "問題は、いやでも思い出させてくれる。先に解く", "◎"),
    "16": ("02", None, "白紙に再現するのは、何も見ずに思い出すこと", "○"),
    "17": ("06", "04", "まず解いて、「できない」を早く知る", "○"),
    "18": ("01", None, "その○を疑う。当たっただけか、わかっていたのか", "○"),
    "19": ("04", None, "本番と同じ時間で測って、足りないものから、やることを決める", "△"),
    "20": ("03", None, "混ぜると、1問ごとに「何の問題だ？」と考える", "◎"),
    "21": ("03", "06", "きつすぎても、伸びない。止まる時間には、目安がある", "○"),
    "22": ("01", None, "「ケアレスミス」という言い方を疑って、直す場所を見つける", "○"),
    "23": ("04", None, "○はやらない、と決める。△と×だけやる", "○"),
    "24": ("04", None, "わかる所と、わからない所を分けて、やる所を決める", "△"),
    "25": ("04", None, "やらない本を決めて、1冊を取り切る", "◎"),
    "26": ("01", None, "自分の見積もりを疑って、実績で決める", "○"),
    "27": ("04", None, "ゴールは「何ができるか」。時間ではなく、できることで決める", "○"),
    "28": ("06", None, "意志に頼らず、先に仕組みを作る", "○"),
    "29": ("06", "05", "こだわるのは、途中の完璧ではなく、最後に勝つこと", "△"),
    "30": ("02", "05", "すきまの3分で、思い出す回数を増やす", "◎"),
    "31": ("01", None, "「集中できている感じ」を疑って、できた数で確かめる", "◎"),
    "32": ("06", None, "意志に頼らず、触れない仕組みを、先に作る", "○"),
    "33": ("01", None, "「朝型が勝つ」を疑って、自分の記録で確かめる", "○"),
    "34": ("06", None, "先に、1問、解く", "○"),
    "35": ("04", None, "やることと、やらないことを決める", "○"),
    "36": ("04", None, "ゴールから後ろ向きに、途中を書く", "○"),
    "37": ("06", None, "さっさと失敗して、さっさと直す。責めるより、直す", "○"),
    "38": ("04", None, "見るのは、ゴールまでの残りと、今のペース", "○"),
    "39": ("03", None, "「まだできない」は、「うーん」の途中", "△"),
    "40": ("01", None, "「落ち着け」「不安は消すもの」という当たり前を疑う", "△"),
    "41": ("06", None, "知っていればすむことは、すぐ聞いて、先に進む", "△"),
    "42": ("04", "03", "やらなくていい努力は、やらないと決める。本番でやる所は、楽をしない", "◎"),
    "43": ("03", "02", "考えるのは、自分。AIには、足りない所を突いてもらう", "◎"),
    "44": ("04", None, "未来から見て、今のお金と時間の使い方を決める", "○"),
    "45": ("04", None, "合格の先から、今を見る", "◎"),
}
CH = [("第2章", "インプット", 7, 15), ("第3章", "アウトプット", 16, 25), ("第4章", "計画", 26, 30),
      ("第5章", "集中", 31, 35), ("第6章", "モチベ", 36, 40), ("第7章", "アップデート", 41, 45)]

def fuda_text(no, full=True):
    """札の言葉。例：もとは：絶対法則02 思い出す（＋03 負荷）"""
    m, s = FUDA[no][0], FUDA[no][1]
    t = "もとは：絶対法則%s %s" % (m, LAW[m][0]) if full else "%s %s" % (m, LAW[m][0])
    return t + ("（＋%s %s）" % (s, LAW[s][0]) if s else "")

def heads():
    """今の原稿から、各項目の ×と○ を拾う"""
    out = {}
    for sid, ttl, _, text, note in Z.build_secs():
        L = text.split("\n")
        for i, line in enumerate(L):
            m = re.match(r"\s?(\d\d) × 頭のいい人は「(.+?)」", line)
            if m and m.group(1) not in out:
                o = re.match(r"→○ 頭のいい人は「(.+?)」", L[i + 1].strip())
                out[m.group(1)] = (m.group(2), o.group(1) if o else "")
    return out

CSS = """
@page{size:A4;margin:15mm 16mm 17mm}
*{box-sizing:border-box}html{font-size:10pt}
body{margin:0;color:#16181d;font-family:"Noto Sans CJK JP","Hiragino Sans",sans-serif;line-height:1.75;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@media screen{body{max-width:190mm;margin:0 auto;padding:10mm 16px 20mm}}
h1{font-size:19pt;line-height:1.4;margin:0 0 1mm}
h2{font-size:13.5pt;line-height:1.5;color:#0f2f57;margin:0 0 2mm;padding-bottom:1.2mm;border-bottom:.5mm solid #0f2f57}
h3{font-size:10.6pt;color:#0f2f57;margin:5mm 0 1.5mm}
.lead{color:#5b606b;font-size:9pt;margin:0 0 5mm}
p{margin:0 0 2mm}.pg{break-before:page}
.note{font-size:8.8pt;color:#5b606b}
/* 図 */
.zu{border:.4mm solid #0f2f57;border-radius:3mm;padding:6mm 6mm 5mm;margin:0 auto 4mm;max-width:172mm}
.zu .ttl{font-size:15pt;font-weight:700;text-align:center;line-height:1.4;margin:0 0 .5mm}
.zu .sub{font-size:9.2pt;text-align:center;color:#30343c;margin:0 0 4mm}
.gr{display:grid;grid-template-columns:44mm repeat(6,1fr);border-top:.4mm solid #0f2f57;border-left:.25mm solid #c9ced8}
.gr>div{border-right:.25mm solid #c9ced8;border-bottom:.25mm solid #c9ced8;padding:1.6mm 1mm;min-height:13mm}
.gr .hc{background:#0f2f57;color:#fff;text-align:center;font-size:8.6pt;line-height:1.35;font-weight:700;min-height:0;padding:1.8mm .5mm;border-color:#0f2f57 #3b5680 #0f2f57 #0f2f57}
.gr .hc small{display:block;font-weight:400;font-size:7.2pt;opacity:.9}
.gr .h0{background:#fff;color:#0f2f57;border-right:.4mm solid #0f2f57;font-size:8.2pt;text-align:left;padding-left:2mm}
.gr .law{background:#fff8e6;border-right:.4mm solid #0f2f57;padding:1.6mm 2mm;line-height:1.4}
.gr .law b{display:block;font-size:11pt;color:#0f2f57}.gr .law b i{font-style:normal;font-size:8.4pt;font-weight:700;color:#8a5a00;margin-right:1.4mm}
.gr .law span{font-size:7.4pt;color:#30343c}
.gr .c{display:flex;flex-wrap:wrap;gap:1mm;align-content:center;justify-content:center}
.b{width:6.6mm;height:6.6mm;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:7.8pt;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.b.m{background:#0f2f57;color:#fff}.b.s{background:#fff;color:#0f2f57;border:.35mm dashed #0f2f57}
.leg{display:flex;gap:6mm;justify-content:center;align-items:center;font-size:8.2pt;color:#30343c;margin:3mm 0 0}
.leg span{display:inline-flex;align-items:center;gap:1.4mm}
.yomi{font-size:9.2pt;margin:3.5mm 2mm 0;line-height:1.7}
/* 札 */
.fd{display:inline-block;font-size:8.2pt;line-height:1;font-weight:700;color:#0f2f57;background:#fff;border:.35mm solid #0f2f57;border-radius:5mm;padding:1.3mm 2.6mm 1.4mm;white-space:nowrap}
.fd i{font-style:normal;font-weight:400;color:#5b606b;margin-right:1.2mm}.fd em{font-style:normal;font-weight:400;color:#30343c;margin-left:1.4mm}
.ex{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;margin:0 0 3mm}
.card{border:.3mm solid #c9ced8;border-radius:2mm;padding:3mm 3.2mm;font-size:9pt}
.card .x{font-weight:700;font-size:9.4pt;background:#fff1cf;border-left:1.2mm solid #e2a100;padding:1mm 2mm;margin:0 0 1mm}
.card .o{font-weight:700;padding-left:3.2mm;margin:0 0 2mm}
.card .cap{font-size:8pt;color:#5b606b;margin:2mm 0 0}
.card pre{font:inherit;font-size:8.4pt;white-space:pre-wrap;margin:0;background:#f5f6f8;border-radius:1.5mm;padding:2mm 2.6mm;line-height:1.65}
.mk{columns:2;column-gap:8mm;font-size:8.7pt;line-height:1.5}
.mk .chp{font-weight:700;color:#0f2f57;margin:2.2mm 0 .6mm;break-after:avoid}.mk .chp:first-child{margin-top:0}
.mk .r{display:flex;align-items:baseline;gap:1.5mm;break-inside:avoid;padding:.35mm 0}
.mk .r .n{font-variant-numeric:tabular-nums;font-weight:700;min-width:5mm}.mk .r .t{flex:1}
.mk .r .f{font-size:7.4pt;font-weight:700;color:#0f2f57;border:.3mm solid #0f2f57;border-radius:4mm;padding:.2mm 1.6mm;white-space:nowrap}
/* 表 */
table{border-collapse:collapse;width:100%;font-size:8.3pt;line-height:1.5}
th,td{border:.25mm solid #c9ced8;padding:1mm 1.6mm;vertical-align:top;text-align:left}
table{table-layout:fixed}th:nth-child(1){width:6%}th:nth-child(2){width:39%}th:nth-child(3){width:10.5%}th:nth-child(4){width:10.5%}th:nth-child(6){width:6%}
th{background:#eef1f6;white-space:nowrap}td.n{font-weight:700;white-space:nowrap}td.k{text-align:center;white-space:nowrap}
tr{break-inside:avoid}tr.w td{background:#fff8e6}
.box{border:.3mm solid #e2a100;background:#fffaf0;border-radius:2mm;padding:3mm 4mm;margin:0 0 4mm;font-size:9.2pt}
.box b{color:#8a5a00}.box ul{margin:1mm 0 0;padding-left:1.3em}.box li{margin:.4mm 0}
"""

def figure():
    c = ['<div class="h0 hc">土台（第1章）<small>6つの絶対法則</small></div>']
    for ch, nm, a, b in CH:
        c.append('<div class="hc">%s<small>%s</small><small>%02d〜%02d</small></div>' % (ch, nm, a, b))
    for k in sorted(LAW):
        c.append('<div class="law"><b><i>%s</i>%s</b><span>%s</span></div>' % (k, LAW[k][0], LAW[k][1]))
        for ch, nm, a, b in CH:
            bs = []
            for no in ["%02d" % n for n in range(a, b + 1)]:
                if FUDA[no][0] == k:
                    bs.append('<span class="b m">%s</span>' % no)
                elif FUDA[no][1] == k:
                    bs.append('<span class="b s">%s</span>' % no)
            c.append('<div class="c">%s</div>' % "".join(bs))
    return """<div class="zu"><p class="ttl">全部、6つから、できています</p>
<p class="sub">07番から先の39個は、どれも、第1章の「6つの絶対法則」の、どれかを使っています。</p>
<div class="gr">%s</div>
<div class="leg"><span><span class="b m">07</span>その法則が、一番のもと</span><span><span class="b s">07</span>その法則も、使っている</span></div>
<p class="yomi">横に見ると、1つの法則が、どの場面で使われているかが、わかります。項目の頭にある札（もとは：絶対法則02）は、この図の、行のことです。やり方を忘れたら、札の番号の法則に、戻ってください。</p></div>""" % "".join(c)

def pill(no):
    m, s = FUDA[no][0], FUDA[no][1]
    return '<span class="fd"><i>もとは</i>絶対法則%s　%s%s</span>' % (m, LAW[m][0], "<em>＋%s %s</em>" % (s, LAW[s][0]) if s else "")

def page(H):
    e = lambda t: html.escape(t, quote=False)
    ex = []
    for no in ("12", "28"):
        x, o = H[no]
        ex.append('<div class="card"><p class="x">%s × 頭のいい人は「%s」をしない。</p><p class="o">→○ 頭のいい人は「%s」をする</p>%s<p class="cap">%s</p></div>'
                  % (no, e(x), e(o), pill(no), e(FUDA[no][2])))
    doc = '<div class="card"><pre>%s</pre><p class="cap">ドキュメントの原稿では、頭の2行の下に、1行で入れる</p></div>' % e(
        "12 × 頭のいい人は「%s」をしない。\n→○ 頭のいい人は「%s」をする\n%s" % (H["12"][0], H["12"][1], fuda_text("12")))
    mk = []
    for ch, nm, a, b in CH:
        mk.append('<p class="chp">%s【%s】</p>' % (ch, nm))
        for no in ["%02d" % n for n in range(a, b + 1)]:
            mk.append('<div class="r"><span class="n">%s</span><span class="t">%s</span><span class="f">%s</span></div>' % (no, e(H[no][0]), fuda_text(no, False).replace("（", " ").replace("）", "")))
    rows = []
    for no in sorted(FUDA):
        m, s, why, k = FUDA[no]
        rows.append('<tr%s><td class="n">%s</td><td>×%s　→　○%s</td><td class="n">%s %s</td><td class="n">%s</td><td>%s</td><td class="k">%s</td></tr>'
                    % (' class="w"' if k == "△" else "", no, e(H[no][0]), e(H[no][1]), m, LAW[m][0], ("%s %s" % (s, LAW[s][0])) if s else "", e(why), k))
    cnt = {k: sum(1 for v in FUDA.values() if v[0] == k) for k in LAW}
    sub = {k: [n for n in sorted(FUDA) if FUDA[n][1] == k] for k in LAW}
    weak = [n for n in sorted(FUDA) if FUDA[n][3] == "△"]
    return """<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="viewport" content="width=device-width,initial-scale=1"><title>体系を見える形にする案 %s</title><style>%s</style></head><body>
<h1>体系を見える形にする案</h1>
<p class="lead">%s。まだ、本には入れていません。1ページ目が図、2ページ目が札、3ページ目からが、対応の表です。</p>
<h2>1　1枚の図（6つの絶対法則と、章のつながり）</h2>
%s
<p class="note">置く場所の案：第1章の終わり（「6つの絶対法則が、そろいました」のあと）。図の中の文は、仮です。本の色が1色でも読めるように、色ではなく、ぬりつぶしと点線で分けています。本は縦書きで幅がせまいので、置く時は、見開き（2ページ）を使う形になります。</p>

<h2 class="pg">2　札（各項目の頭に、小さくつける）</h2>
<h3>項目の頭での見え方</h3>
<div class="ex">%s%s</div>
<h3>目次での見え方（番号の右に、法則の番号と名前）</h3>
<div class="mk">%s</div>

<h2 class="pg">3　対応の表（どの項目が、どの法則から来ているか）</h2>
<div class="box"><b>やってみて、わかったこと</b><ul>
<li>主の数：%s</li>
<li>絶対法則05「分散」を、一番のもとにする項目が、ありません。副で使っているのは、%s番だけです。図では、05の行が、点線の丸だけになります。</li>
<li>つながりが弱い項目が、%d個あります（%s番。表の、色のついた行）。札をつけるなら、ここは、見てほしい所です。無理につけず、札なしにする手もあります。</li>
</ul></div>
<table><tr><th>番号</th><th>項目</th><th>主</th><th>副</th><th>なぜ、その法則か</th><th>確かさ</th></tr>%s</table>
<p class="note" style="margin-top:2mm">確かさ　◎：本文の中で、その法則に戻っている　○：中身が合う　△：つながりが弱い</p>
</body></html>""" % (Z.DATE, CSS, Z.DATE, figure(), "".join(ex), doc, "".join(mk),
                     "、".join("%s %s＝%d個" % (k, LAW[k][0], cnt[k]) for k in sorted(LAW)),
                     "・".join(sub["05"]), len(weak), "・".join(weak), "".join(rows))

def main(dst, pdf=False):
    H = heads()
    miss = [n for n in FUDA if n not in H]
    assert not miss and len(FUDA) == 39, ("原稿に見つからない番号", miss)
    open(dst, "w", encoding="utf-8").write(page(H))
    print("出した：", dst)
    if pdf:
        out = os.path.splitext(dst)[0] + ".pdf"
        subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), dst, out, "体系を見える形にする案　" + Z.DATE])
        n = subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout
        print("PDF：", out, "／", re.search(r"Pages:\s+(\d+)", n).group(1), "ページ")

if __name__ == "__main__":
    main(sys.argv[1], "--pdf" in sys.argv[2:])
