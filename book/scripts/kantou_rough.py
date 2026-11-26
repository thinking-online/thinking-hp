# -*- coding: utf-8 -*-
# 巻頭ページを「1ページに1つのこと＋絵」の形にする案のラフ（2026-11-26。まだ、本には入れていない）
#   python3 -I scripts/kantou_rough.py 出す先.html [--pdf]
# 文は、著者の今の巻頭ページ（manuscript/著者の最新原稿/）の言葉を、ページごとに切り直したもの。
# 絵は、言葉で書いた指定だけ（わくの中）。見開きは、右のページが先。
import html, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026年11月26日"

# 1ページ：{"plain": 文だけのページか, "tx": [(大きさ b/m/s, 文。／で改行)], "fig": 横組みの図（数字）, "pic": 絵の指定}
P = [
    {"plain": True, "tx": [("b", "10秒だけ、／付き合ってください。")]},
    {"tx": [("m", "次の11個の数字を、／10秒で、覚えてください。")],
     "fig": ["1　4　9　1　6　2　5　3　6　4　9"], "pic": "絵は、なし（数字だけを、大きく）。下に小さく「10秒たったら、めくってください」"},

    {"tx": [("b", "はい、終了。"), ("m", "本を伏せて、言えますか？"), ("s", "……"),
            ("m", "たぶん、6個目か、7個目で、／怪しくなったはずです。"), ("m", "安心してください。／それが、普通です。")],
     "pic": "机に向かう「自分」（読者の分身。真面目に頑張っている子）。頭の上で、数字が、ばらばらに浮いている"},
    {"plain": True, "tx": [("m", "では、1つだけ、教えます。"), ("b", "見方を、変えます。")]},

    {"tx": [("m", "こう、見てください。")],
     "fig": ["1×1　2×2　3×3　4×4　5×5　6×6　7×7", "↓", "1｜4｜9｜16｜25｜36｜49"], "pic": "絵は、なし（図だけ）"},
    {"tx": [("m", "もう一度、見てください。")],
     "fig": ["1　4　9　1　6　2　5　3　6　4　9"],
     "tx2": [("b", "もう、10秒も、／いりませんよね。")], "pic": "さっきと同じ「自分」、同じ机。頭の上の数字が、7つのかたまりに並んでいる"},

    {"tx": [("m", "今、何が、変わったのでしょうか。"), ("m", "記憶力は、同じです。／集中力も、やる気も、／1分前のままです。"),
            ("m", "覚えるための努力は、／むしろ、減りました。"), ("b", "変わったのは、／見方だけです。")],
     "pic": "「自分」が、自分の頭を指さして、おどろいている（人は同じ。変わったのは、頭の上の並びだけ）"},
    {"tx": [("m", "「あの子は、頭がいい。／自分は、頭が悪い……」"), ("m", "「頭がいい」は、たいてい、／生まれつきのこととして、使われます。"),
            ("m", "でも、あなたは、1分前より、／多く、覚えられるようになりました。"), ("m", "生まれつきのものは、／1ミリも、変わっていないのに。")],
     "pic": "となりの席の「あの子」（頭のいい人）が、はじめて出てくる。「自分」が、ちらっと見ている"},

    {"plain": True, "tx": [("b", "〝頭がよくなる〟って、／こういうことです。"), ("m", "「やり方」を知る。それだけで、／同じ時間で、頭に入る量が変わります。")]},
    {"tx": [("m", "でも、多くの人は、／一番肝心な所を、教わりません。"), ("m", "「何度も、復習しなさい」／「計画を、ちゃんと立てなさい」"),
            ("m", "どれも、正しいです。"), ("m", "でも、復習は、どうやるのか。／計画は、どう立てるのか。／そこは、決まっていません。")],
     "pic": "机の「自分」に、まわりから「ちゃんと」「ちゃんと」「ちゃんと」の吹き出し"},

    {"tx": [("m", "クラスで一番点を取るあの子に、／聞いてみてください。"), ("m", "「どうやって、勉強してるの？」"),
            ("m", "「復習を、ちゃんとやってるだけだよ」"), ("b", "その「ちゃんと」の中身は、／わかりますか？")],
     "pic": "「自分」と「あの子」。あの子の頭の上に、考えの吹き出し。中は、白くて、見えない"},
    {"tx": [("b", "見えないんです。"), ("m", "問題を見た瞬間に、何を考えているか。／どこで手を止めて、何を書いていないか。／覚えたあとに、何をして、何をやらないか。"),
            ("m", "全部、頭の中で、起きています。")],
     "pic": "2人が、同じ姿勢で机に向かっている、うしろ姿。外から見ると、同じ"},

    {"tx": [("m", "見えないから、マネできない。／同じように机に向かっているのに、／差が、開いていく。"),
            ("b", "だから、／あなたのせいでは、／ありません。"), ("m", "「結果が出るやり方」が、／見えなかっただけです。")],
     "pic": "うつむいていた「自分」が、顔を上げる"},
    {"tx": [("b", "この本で、全部、／見えるようにします。"), ("m", "頭のいい人が、何をやっているのか。／何を、絶対にやらないのか。／その時、頭の中で、何を考えているのか。"),
            ("m", "45個。1つ残らず、書きます。")],
     "pic": "あの子の吹き出しが、開く。中が、見える。「自分」が、のぞきこんでいる"},

    {"tx": [("b", "書いてあることを、／徹底的に、／パクってください。"), ("m", "センスも、才能も、いりません。")],
     "pic": "「自分」の頭の上に、あの子と同じ吹き出しが出ている"},
    {"plain": True, "tx": [("b", "人は、誰だって、／変われる。"), ("m", "準備は、いいですか。／次は、あなたの番です。")]},
]
# 見開きごとの、ねらい
CAP = ["さそう。約束ではなく、やってもらう", "ここでは、まだ答えを見せない", "めくって、はじめて、見方が出る", "体験を、言葉にする",
       "この本の考えの中心。そして、問題に入る", "「ちゃんと」の中身が、見えない", "読者を責めない。そして、この本が何か", "手渡して、終わる"]

FW = str.maketrans("0123456789", "０１２３４５６７８９")
def tate(t):
    """縦書き用。2けたの数字は、1文字分に横に並べる。1けたは、全角にする"""
    t = html.escape(t, quote=False)
    t = re.sub(r"(?<!\d)(\d{2})(?!\d)", r'<span class="tcy">\1</span>', t)
    t = re.sub(r"(?<![\d>])(\d)(?![\d<])", lambda m: m.group(1).translate(FW), t)
    return t.replace("／", "<br>")

def tx(lines):
    return '<div class="tx">%s</div>' % "".join('<p class="%s">%s</p>' % (k, tate(t)) for k, t in lines)

def page(i, p):
    e = lambda t: html.escape(t, quote=False)
    h = tx(p["tx"])
    if "fig" in p:
        h += '<div class="fig">%s</div>' % "".join('<div%s>%s</div>' % (' class="w"' if "×" in x else "", e(x)) for x in p["fig"])
    if "tx2" in p:
        h += tx(p["tx2"])
    if p.get("pic") and not p.get("plain"):
        h += '<div class="pic"><b>絵</b>%s</div>' % e(p["pic"])
    return '<div class="pg%s%s"><span class="no">%d</span>%s</div>' % (" plain" if p.get("plain") else "", " hasfig" if "fig" in p else "", i, h)

CSS = """
@page{size:A4 landscape;margin:9mm 12mm 12mm}
*{box-sizing:border-box}
body{margin:0;color:#16181d;font-family:"Noto Sans CJK JP","Hiragino Sans",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.sheet{break-after:page;height:178mm;display:flex;flex-direction:column}
.sheet:last-child{break-after:auto}
.hd{display:flex;justify-content:space-between;align-items:baseline;font-size:9pt;color:#5b606b;margin:0 0 2.5mm}
.hd b{font-size:11pt;color:#0f2f57}.hd i{font-style:normal}
.sp{display:flex;flex-direction:row-reverse;justify-content:center;flex:1;min-height:0}
.pg{position:relative;width:118mm;height:100%;border:.3mm solid #b9c0cc;background:#fff;display:flex;flex-direction:column;align-items:center;padding:10mm 9mm 8mm;overflow:hidden}
.pg+.pg{border-right:none}
.pg.plain{background:#fff6dd;justify-content:center}
.no{position:absolute;bottom:2.5mm;left:4mm;font-size:7.5pt;color:#8a8f99}
.pg:first-child .no{left:auto;right:4mm}
.tx{writing-mode:vertical-rl;height:86mm;flex:none}
.pg.plain .tx{height:112mm}
.pg.hasfig .tx{height:auto;max-height:52mm}
.tx p{margin:0;margin-block-end:.95em}.tx p:last-child{margin-block-end:0}
.tx .b{font-size:17.5pt;font-weight:700;line-height:1.55;letter-spacing:.04em}
.pg.plain .tx .b{font-size:21pt}
.tx .m{font-size:11.5pt;line-height:1.85}
.tx .s{font-size:10pt;color:#5b606b}
.tcy{text-combine-upright:all;-webkit-text-combine:horizontal}
.fig{margin:6mm 0;text-align:center;font-weight:700;font-size:15pt;letter-spacing:.02em;line-height:1.7;flex:none}
.fig div{white-space:nowrap}.fig div.w{font-size:12pt}
.fig div:nth-child(2){font-size:11pt;color:#8a5a00}
.pic{margin-top:auto;width:100%;min-height:44mm;border:.35mm dashed #8a8f99;border-radius:2mm;background:#f5f6f8;padding:3mm 4mm;font-size:8.6pt;line-height:1.65;color:#30343c;display:flex;flex-direction:column;justify-content:center}
.pic b{font-size:7.6pt;color:#8a5a00;margin-bottom:.6mm}
.pg.hasfig .pic{min-height:20mm}
/* 最後のメモ */
.memo{font-size:9.6pt;line-height:1.75}
.memo h1{font-size:15pt;margin:0 0 3mm;color:#0f2f57}
.memo h2{font-size:11pt;color:#0f2f57;margin:4mm 0 1mm}
.memo .g{display:grid;grid-template-columns:1fr 1fr;gap:0 10mm}
.memo ul{margin:0;padding-left:1.3em}.memo li{margin:.5mm 0}
"""

MEMO = """<div class="sheet memo"><h1>この案の考え方</h1><div class="g"><div>
<h2>類書から、もらうもの（見せ方）</h2><ul>
<li>1ページに、1つのこと。文は、1ページ100字くらいまで</li>
<li>大事な1行だけ、大きくする</li>
<li>同じ人物が、最初から最後まで出てくる。1つの絵の世界で、通す</li>
<li>文だけのページで始めて、文だけのページで終わる</li>
<li>最初のほうに、読者が自分で答える問いを置く</li></ul>
<h2>もらわないもの</h2><ul>
<li>「誰でも、必ず」「99％」のような約束（この本は、言い切らない）</li>
<li>「ラクして受かる」（この本は、頑張っているのに、やり方がズレている人の本）</li>
<li>頑張っている人を、からかう言い方（この本は、読者を責めない）</li>
<li>山登りのたとえ、人物の見た目、言い回し（まねに、なるため）</li></ul>
</div><div>
<h2>この本だけの、絵の世界</h2><ul>
<li>人物は2人。「自分」（読者の分身。真面目に頑張っている子）と、「あの子」（頭のいい人）</li>
<li>しるしは、頭の上の「考えの吹き出し」。あの子の吹き出しは、最初、中が見えない。この本が、それを開ける</li>
<li>この2人は、45項目の2コマ（×と○）にも、そのまま出る。○のコマは、あの子の頭の中の声。つまり、本文は、あの子の吹き出しを、45回、開けている</li></ul>
<h2>今の巻頭から、動かすもの（著者が決める）</h2><ul>
<li>「1日後、1週間後、1か月後」の計算と、「人に説明するつもりで」の話 → 長いので、はじめに へ</li>
<li>生徒の実績の箇条書き → はじめに に、もっとくわしいものが、もうある。巻頭からは、外す</li>
<li>「さっきの数字で、もう証明されています」→ 「証明」を使わないため、外した</li>
<li>「50個」→ 45個</li></ul>
<h2>作る時に、守ること</h2><ul>
<li>数字（2ページ）、「言えますか？」（3ページ）、見方の図（5ページ）を、同じ見開きに入れない。先に答えが見えると、体験にならない</li>
<li>ページ数は16。12に縮めるなら、8ページと10ページを、はじめに へ動かす</li></ul>
</div></div></div>"""

def build():
    sheets = []
    for s in range(0, len(P), 2):
        n = s // 2
        sheets.append('<div class="sheet"><div class="hd"><b>見開き%d（%d〜%dページ）</b><i>%s</i><span>右のページから、読みます　／　巻頭ページの案　%s</span></div><div class="sp">%s%s</div></div>'
                      % (n + 1, s + 1, s + 2, CAP[n], DATE, page(s + 1, P[s]), page(s + 2, P[s + 1])))
    return '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive"><title>巻頭ページの案（ラフ）%s</title><style>%s</style></head><body>%s%s</body></html>' % (DATE, CSS, "".join(sheets), MEMO)

def count():
    """ページごとの字数（空白と、改行の印をのぞく）"""
    out = []
    for p in P:
        t = "".join(x for _, x in p["tx"] + p.get("tx2", []))
        out.append(len(re.sub(r"[／\s]", "", t)))
    return out

if __name__ == "__main__":
    dst = sys.argv[1]
    open(dst, "w", encoding="utf-8").write(build())
    c = count()
    print("出した：", dst, "／", len(P), "ページ ／ 文の字数", sum(c), "（1ページ", min(c), "〜", max(c), "字）")
    if "--pdf" in sys.argv[2:]:
        out = os.path.splitext(dst)[0] + ".pdf"
        subprocess.check_call(["node", os.path.join(HERE, "print_pdf.js"), dst, out])
        print("PDF：", out)
