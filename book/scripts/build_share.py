# -*- coding: utf-8 -*-
# 編集の方に見てもらう「原稿のご確認ページ」を作る。1つの入口のページから、台本・形の候補・タイトル案などへ飛べる。
#   python3 -I scripts/build_share.py   → build/共有ページ/
#     site/      そのままウェブサイトに置ける一式（index.html から始まる。Word・PDF もここに入る）
#     artifact/  同じ入口のページを、Claude の Artifact 用にしたもの（index.html だけ。ほかのページは site/ のものを使う）
# 2026-11-20：入口を、部分ごとに見る形に変えた（巻頭ページ／はじめに／第1章…。できた部分だけ読める）。下の説明は、前の形（main_old）のもの。
# 入っているページ：
#   index.html     入口（台本、形の候補、タイトル案、目次、イラストのラフ案、ご相談したいこと）
#   daihon35.html  台本・35個の版（横書きで通して読む）
#   daihon45.html  台本・45個の版（同じ）
#   book45.html / book35.html   本の形（A5・縦書き）で見る
#   katachi.html   同じ項目を、4つの形で組んだ見本
#   rough.html     イラストのラフ案（2コマの言葉の一覧）
# どのページにも、検索に出ないようにする印（noindex）を入れている。
import html, os, re, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_book as Z
import book_data as K
import v4_data as V
import assemble_v4 as B
import assemble_v6 as A6
import build_book_pdf as BP
import build_v4_pdf as P4
import build_v3_pdf as P3

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "build", "共有ページ")
SITE = os.path.join(OUT, "site")
esc = lambda s: html.escape(s, quote=False)
DATE = "2026年11月20日"
TITLE = K.TITLES[0]
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@500;700&display=swap">'
HEAD = '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive">'
BACK = '<a class="back" href="./" onclick="if(document.referrer&&history.length>1){history.back();return false}">← 一覧にもどる</a>'
# 版ごとの数（本の形のPDFで、実際に流した数。字数は、空白をのぞいた数）
FACTS = {"35": dict(pages=327, chars="約12万字", items=35), "45": dict(pages=390, chars="約13万7千字", items=45), "step": dict(pages=319)}


def write(name, text):
    with open(os.path.join(SITE, name), "w", encoding="utf-8") as f:
        f.write(text)


# ---------------------------------------------------------------- 台本を、横書きで通して読むページ
READ_CSS = P4.CSS + BP.CSS[len(P4.CSS):] + """
/* 画面で読むための上書き */
html{background:#eef0f4;color-scheme:light;font-size:11.4pt}
body{background:#fff;max-width:820px;margin:0 auto;padding:0 max(18px,env(safe-area-inset-left,0px)) 90px;box-shadow:0 0 0 1px #dfe3ea}
@media(min-width:900px){body{padding:0 58px 110px}}
.bar{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #dfe3ea;margin:0 -18px 18px;padding:9px 18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap;font-size:9.5pt}
@media(min-width:900px){.bar{margin:0 -58px 24px;padding:10px 58px}}
.bar .back{color:#15467e;font-weight:700;text-decoration:none}
.bar b{font-weight:700}
.bar select{font:inherit;font-size:9.5pt;padding:3px 6px;border:1px solid #c9ced8;border-radius:6px;background:#fff;color:#16181d;max-width:100%}
.top h1{font-size:19pt;line-height:1.5;font-weight:900;margin:8mm 0 2mm}
.top p{color:#555;font-size:10pt;margin:0 0 2mm}
.sec{scroll-margin-top:56px}
.text,.item,.col,.toc{margin-top:22mm}
.chdoor{margin-top:26mm;padding-top:10mm;border-top:3px solid #15467e}
.grp{margin-top:18mm;padding-top:0;text-align:left;border-left:6px solid #15467e;padding-left:5mm}
.grp p,.grp .g3{text-align:left}
.cover{display:none}
pre{overflow-x:auto}
"""


def reading(mode):
    """mode: "35" か "45"。版に合わせて、組み立ての材料を入れかえてから、同じ作り方でHTMLにする。"""
    if mode == "35":
        BP.Z, BP.K, BP.V, BP.B = A6.Z6, A6.K6, A6.V6, A6.B6
        P4.B, P4.V = A6.B6, A6.V6
    else:
        BP.Z, BP.K, BP.V, BP.B = Z, K, V, B
        P4.B, P4.V = B, V
    P4.kind = lambda kk: ""     # 「新しく書いた」などの、こちらの作業用の印は出さない
    Zm, Km, Vm, Bm = BP.Z, BP.K, BP.V, BP.B
    n_all = FACTS[mode]["items"]
    parts, nav = [], []
    def add(sid, label, h):
        parts.append('<div class="sec" id="%s">%s</div>' % (sid, h))
        if label:
            nav.append((sid, label))
    for kind, name, md in Zm.sections():
        if kind == "cover":
            continue
        if kind == "toc":
            add("mokuji", "目次", BP.toc_html().replace("<p class=\"line\">45を、1枚に</p>", "<p class=\"line\">%dを、1枚に</p>" % n_all))
        elif kind == "text":
            add("t%d" % len(parts), name.replace("巻末　", "巻末｜"), BP.text_html(md))
        elif kind == "door":
            if name == "第1章":
                intro = P3.body_html(Zm.to_md(Zm.master(Km.CH1_INTRO)))
                h = ('<section class="chdoor"><div class="cno">第1章</div><h1>%s</h1><p class="fld">【%s】　01〜06番</p><div class="intro">%s</div></section>'
                     % (esc(Km.CH1_TITLE), esc(Km.CH1_SUB), intro))
                label = "第1章　" + Km.CH1_TITLE
            else:
                num, fuda, title, sub, groups = [c for c in Vm.CHAPTERS if "第%d章" % c[0] == name][0]
                ks = [kk for _, items in groups for kk in items]
                h = ('<section class="chdoor"><div class="cno">第%d章</div><h1>%s</h1><p class="fld">【%s】　%s〜%s番</p>%s<div class="intro">%s</div></section>'
                     % (num, esc(title), esc(fuda), ks[0], ks[-1], ('<p class="sub">%s</p>' % esc(sub)) if sub else "", P3.body_html(Bm.read_new("ch%d_導入" % num))))
                label = "第%d章　【%s】%s" % (num, fuda, title)
            add("ch" + name[1], label, h)
        elif kind == "group":
            num, fuda, title, sub, groups = [c for c in Vm.CHAPTERS if any(g[0] == name for g in c[4])][0]
            items = [g[1] for g in groups if g[0] == name][0]
            lines = "<br>".join("%s　%s" % (kk, esc(Vm.ITEMS[kk]["t"])) for kk in items)
            add("g%d" % len(parts), "", '<section class="grp"><p class="g1">第%d章　【%s】</p><p class="g2">%s</p><p class="g3">%s</p></section>' % (num, esc(fuda), esc(name), lines))
        elif kind == "item1":
            add("i" + name, "　%s　絶対法則%s　%s" % (name, name, Km.CH1_MOKUJI[name][0]), BP.item1_html(name))
        elif kind == "item":
            add("i" + name, "　%s　%s" % (name, Vm.ITEMS[name]["t"]), P4.item_html(name, BP.hito_html(name)))
        elif kind == "column":
            src = [(s, nm) for k, s, nm in Km.COLUMNS if (Zm.column(s, nm) or ("",))[0] == name][0]
            add("c%d" % len(parts), "", BP.column_html(Zm.column(*src)))
    BP.Z, BP.K, BP.V, BP.B = Z, K, V, B
    P4.B, P4.V = B, V
    f = FACTS[mode]
    opts = "".join('<option value="%s">%s</option>' % (sid, esc(label)) for sid, label in nav)
    return ('<!doctype html><html lang="ja"><head>%s<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>台本　%d個の版</title>%s<style>%s</style></head><body>'
            '<div class="bar">%s<b>台本　%d個の版</b><select id="jump" aria-label="読みたい所へ飛ぶ"><option value="">読みたい所へ飛ぶ</option>%s</select></div>'
            '<div class="top"><h1>%s<span style="font-size:11pt;font-weight:700;color:#555">（仮題）</span></h1><p>%s　／　%s</p>'
            '<p>%d個の版（第1章の6個 ＋ %d個）。%s。A5・縦書きで組むと、%dページの見込みです。黄色の線は、原稿のマーカーの印です。</p></div>'
            '%s<script>document.getElementById("jump").addEventListener("change",function(){if(this.value){document.getElementById(this.value).scrollIntoView();this.value=""}});</script></body></html>'
            % (HEAD, n_all, FONT, READ_CSS, BACK, n_all, opts, esc(TITLE), esc(K.AUTHOR), DATE, n_all, n_all - 6, f["chars"], f["pages"], "\n".join(parts)))


# ---------------------------------------------------------------- 本の形（縦書き）で見るページ
def book(mode):
    arg, name = {"35": ("s35", "本の形_35個の版"), "45": ("max", "本の形_マックス版")}[mode]
    subprocess.check_call([sys.executable, "-I", os.path.join(HERE, "build_tate_book.py"), arg, "--html"])
    t = open(os.path.join(ROOT, "build", name + ".html"), encoding="utf-8").read()
    extra = ('<meta name="robots" content="noindex,nofollow,noarchive"><meta name="viewport" content="width=560">' + FONT + '<style>'
             'html{background:#e8e6e1}body{margin:0 auto !important;padding:46px 0 60px}'
             '.page{margin:0 auto 14px;box-shadow:0 1px 4px rgba(0,0,0,.18)}'
             '.topbar{position:fixed;top:0;left:0;right:0;z-index:9;background:#fff;border-bottom:1px solid #d5d8de;padding:8px 14px;font:700 13px "Noto Sans JP",sans-serif;display:flex;gap:14px;align-items:center}'
             '.topbar a{color:#15467e;text-decoration:none}.topbar span{font-weight:400;color:#555;font-size:12px}'
             '@media print{.topbar{display:none}body{padding:0}.page{margin:0;box-shadow:none}}</style>')
    assert "<title>%s</title>" % name in t
    t = t.replace("<title>%s</title>" % name, "<title>本の形で見る　%s個の版</title>" % mode + extra)
    t = t.replace("<body>", '<body><div class="topbar">%s<span>%s個の版を、A5・縦書きで組んだ形です（全%dページ）。右から左へ読みます。点線の枠は、イラストが入る場所です。</span></div>' % (BACK, mode, FACTS[mode]["pages"]), 1)
    assert "topbar" in t and "noindex" in t
    return t


# ---------------------------------------------------------------- 形の候補（同じ項目を、4つの形で）
def katachi():
    subprocess.check_call([sys.executable, "-I", os.path.join(HERE, "build_mock_patterns.py")], stdout=subprocess.DEVNULL)
    t = open(os.path.join(ROOT, "build", "見本_4つのパターン.html"), encoding="utf-8").read()
    def rep(a, b):
        nonlocal t
        if a not in t:
            raise SystemExit("形の見本：言葉が見つからない: " + a[:30])
        t = t.replace(a, b)
    rep("<h1>見本　同じ14番を、4つの形で組みました</h1>", "<h1>形の候補　同じ項目を、4つの形で組みました</h1>")
    rep("どれも、実際に文字を流しています。", "もとにしたのは、「黙って、じっと見つめて覚える」の項目です。どれも、実際に文字を流しています。")
    rep("右の3つの列は、07〜45番を全部その形で作った時の、本全体のページ数の目安です（文は削らない。第1章・前付け・巻末の145ページをふくむ）。",
        "右の3つの列は、第2章から先を全部その形で作った時の、本全体のページ数の目安です（文は削らない場合。第1章・前付け・巻末の145ページをふくむ）。")
    rep("形3で、長い項目を少し削って4ページと6ページにそろえたものが、先に送った「削った版」のPDF（45個で319ページ）です。", "形3で、長い項目を少し削って、4ページと6ページにそろえると、45個で319ページになります。")
    rep("削った版のPDF（319ページ）は、この形。", "")
    rep("全体のページ数は、07〜45番の本文を行に直して数えた目安です（<code>scripts/tate_model.py</code>）。形1の45個は、本の形のPDFで実際に流した数です。", "全体のページ数は、本文を行に直して数えた目安です。")
    rep("形4の文は、見本のために短くしたものです（実験の大学名などは、入れていません）。", "形4の文は、見本のために短くしたものです。")
    rep("<th class='c'>14番のページ</th><th class='c'>14番の本文</th>", "<th class='c'>この項目のページ</th><th class='c'>この項目の本文</th>")
    rep("今の14番の文（約1,378字）を、1字も削っていません。", "今の文（約1,378字）を、1字も削っていません。") if "今の14番の文（約1,378字）を、1字も削っていません。" in t else None
    t = t.replace("<title>見本　14番を、4つの形で</title>", "<title>形の候補</title>" + HEAD.replace('<meta charset="utf-8">', "") + '<meta name="viewport" content="width=1180">' + FONT
                  + '<style>.backbar{font:700 13px "Noto Sans JP",sans-serif;margin:0 0 14px}.backbar a{color:#15467e;text-decoration:none}</style>')
    t = t.replace("<body>", '<body><div class="backbar">%s</div>' % BACK, 1)
    assert "backbar" in t and "noindex" in t
    return t


# ---------------------------------------------------------------- イラストのラフ案（2コマの言葉）
PAGE_CSS = """
html{background:#eef0f4;color-scheme:light}
body{margin:0 auto;max-width:900px;background:#fff;padding:0 max(18px,env(safe-area-inset-left,0px)) 80px;font-family:"Noto Sans JP","Noto Sans CJK JP",sans-serif;color:#16181d;font-size:15px;line-height:1.85;box-shadow:0 0 0 1px #dfe3ea}
@media(min-width:900px){body{padding:0 48px 100px}}
.bar{position:sticky;top:0;background:#fff;border-bottom:1px solid #dfe3ea;margin:0 -18px 18px;padding:9px 18px;font-size:13px}
@media(min-width:900px){.bar{margin:0 -48px 22px;padding:10px 48px}}
.back{color:#15467e;font-weight:700;text-decoration:none}
h1{font-size:24px;font-weight:900;line-height:1.5;margin:26px 0 6px}
.lead{color:#444;margin:0 0 6px}
h2{font-size:16px;font-weight:900;color:#15467e;margin:38px 0 10px;padding-top:14px;border-top:3px solid #15467e}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:640px;font-size:13.5px}
th,td{border:1px solid #d5d9e0;padding:7px 10px;text-align:left;vertical-align:top;line-height:1.65}
th{background:#eef1f6;font-weight:700;white-space:nowrap}
td.no{font-weight:900;color:#15467e;white-space:nowrap;font-variant-numeric:tabular-nums}
td b{display:block;font-weight:900}
td span{color:#555;font-size:12.5px}
td.x{background:#f4f5f7}td.o{background:#eaf1fa}
"""


def rough():
    rows = []
    def row(no, title, c):
        return ('<tr><td class="no">%s</td><td>%s</td><td class="x"><b>%s</b><span>%s</span></td><td class="o"><b>%s</b><span>%s</span></td></tr>'
                % (no, esc(title), esc(c[0][0].strip()), esc(c[0][1].strip()), esc(c[1][0].strip()), esc(c[1][1].strip())))
    out = ['<h2>第1章　%s</h2>' % esc(K.CH1_TITLE), '<div class="tw"><table><tr><th>番号</th><th>項目</th><th>伸びない人のコマ</th><th>頭のいい人のコマ</th></tr>']
    for kk in sorted(K.CH1_MOKUJI):
        c = Z.ch1_koma(Z.ch1_item(kk))
        out.append(row(kk, "絶対法則%s　%s" % (kk, K.CH1_MOKUJI[kk][0]), c))
    out.append("</table></div>")
    for num, fuda, title, sub, groups in V.CHAPTERS:
        out.append('<h2>第%d章　【%s】%s</h2>' % (num, esc(fuda), esc(title)))
        out.append('<div class="tw"><table><tr><th>番号</th><th>項目</th><th>伸びない人のコマ</th><th>頭のいい人のコマ</th></tr>')
        for _, items in groups:
            for nn in items:
                out.append(row(nn, V.ITEMS[nn]["t"], B.koma(nn)))
        out.append("</table></div>")
    return ('<!doctype html><html lang="ja"><head>%s<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>イラストのラフ案</title>%s<style>%s</style></head><body>'
            '<div class="bar">%s</div><h1>イラストのラフ案（2コマの言葉）</h1>'
            '<p class="lead">各項目に、「頭のいい人と伸びない人の違い」の2コマを置く想定です。同じ場面で、2人が考えていることを、並べます。</p>'
            '<p class="lead">絵そのものは、まだありません。下の表は、コマに入れる言葉です（大きい言葉と、その下の小さい言葉）。番号は、45個の版のものです。</p>%s</body></html>'
            % (HEAD, FONT, PAGE_CSS, BACK, "\n".join(out)))


# ---------------------------------------------------------------- 入口のページ
INDEX_CSS = """
/* 並べ方：上に題。その下に、見るものを順に1列で。台本だけは、2つの版を横に並べる */
:root{--bg:#f3f5f9;--paper:#ffffff;--ink:#15181f;--sub:#566070;--line:#d9dee7;--accent:#15467e;--accent-ink:#ffffff;--tint:#e8eff8;
  --display:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif;--body:"Noto Sans JP","Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#10141b;--paper:#181e28;--ink:#e9edf3;--sub:#a3adbb;--line:#2c3542;--accent:#8ab6ee;--accent-ink:#0f1620;--tint:#1f2a3a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#10141b;--paper:#181e28;--ink:#e9edf3;--sub:#a3adbb;--line:#2c3542;--accent:#8ab6ee;--accent-ink:#0f1620;--tint:#1f2a3a;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15.5px;line-height:1.9;margin:0}
.wrap{max-width:860px;margin:0 auto;padding-block:34px 90px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:30px}
header .eyebrow{font-size:12.5px;font-weight:700;color:var(--accent);letter-spacing:.14em;margin:0}
header h1{font-family:var(--display);font-weight:700;font-size:clamp(25px,5.4vw,36px);line-height:1.45;margin:6px 0 8px;text-wrap:balance}
header h1 small{font-family:var(--body);font-size:13px;font-weight:700;color:var(--sub);margin-left:6px}
header .by{color:var(--sub);font-size:13.5px;margin:0}
header .lead{margin:16px 0 0;max-width:40em}
nav.toc{display:flex;flex-wrap:wrap;gap:8px}
nav.toc a{font-size:13px;font-weight:700;color:var(--accent);text-decoration:none;border:1px solid var(--line);background:var(--paper);border-radius:99px;padding:3px 14px}
nav.toc a:hover,nav.toc a:focus-visible{border-color:var(--accent)}
section{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:22px 24px 24px;min-width:0}
section h2{font-size:18px;font-weight:900;margin:0 0 4px;display:flex;align-items:baseline;gap:10px}
section h2 .n{font-family:var(--display);color:var(--accent);font-size:22px;font-variant-numeric:tabular-nums}
section .note{color:var(--sub);font-size:13.5px;margin:0 0 14px;max-width:44em}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.ver{border:1px solid var(--line);border-radius:12px;padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;min-width:0}
.ver h3{font-size:17px;font-weight:900;margin:0}
.ver .fig{display:flex;gap:18px;flex-wrap:wrap;font-variant-numeric:tabular-nums}
.ver .fig div{font-size:12px;color:var(--sub);line-height:1.5}
.ver .fig b{display:block;font-size:20px;color:var(--ink);font-weight:900}
.ver p{margin:0;font-size:14px}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:6px}
a.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);font-weight:700;font-size:14px;text-decoration:none;border-radius:8px;padding:7px 16px;border:1px solid var(--accent)}
a.btn.sub{background:transparent;color:var(--accent)}
a.btn:focus-visible,nav.toc a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14px;font-variant-numeric:tabular-nums}
th,td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{font-size:12.5px;color:var(--sub);font-weight:700;white-space:nowrap}
td.num{text-align:right;font-weight:900;white-space:nowrap}
ol.titles{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px}
ol.titles li{font-family:var(--display);font-weight:700;font-size:clamp(18px,4vw,22px);line-height:1.6;background:var(--tint);border-radius:10px;padding:10px 16px}
details{border-top:1px solid var(--line)}
details:first-of-type{border-top:0}
summary{cursor:pointer;font-weight:700;padding:10px 0;color:var(--accent)}
.moku{margin:0 0 12px;padding:0;list-style:none}
.moku li{display:grid;grid-template-columns:2.4em 1fr;gap:2px 8px;padding:5px 0;border-bottom:1px dashed var(--line);font-size:14px;line-height:1.7}
.moku li b{color:var(--accent);font-variant-numeric:tabular-nums}
.moku li span{grid-column:2;color:var(--sub);font-size:13px}
.moku .g{display:block;font-weight:700;font-size:12.5px;color:var(--sub);padding:10px 0 2px;border:0}
ul.ask{margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:4px}
ul.ask li{max-width:44em}
footer{color:var(--sub);font-size:12.5px}
"""


def mokuji_html():
    """入口のページの目次。1行の形（scripts/mokuji1.py）の言葉を使う。左が、やらないこと。矢印の先が、かわりにやること。"""
    import mokuji1 as M1
    out = []
    for num, fuda, title, groups in M1.chapters():
        L = []
        ks = [nn for _, items in groups for nn in items]
        for name, items in groups:
            if name:
                L.append('<li class="g">%s</li>' % esc(name))
            L += ["<li><b>%s</b>%s<span>→　%s</span></li>" % (nn, esc(M1.pair(nn)[0]), esc(M1.pair(nn)[1])) for nn in items]
        out.append('<details><summary>第%d章　【%s】%s（%s〜%s番）</summary><ul class="moku">%s</ul></details>' % (num, esc(fuda), esc(title), ks[0], ks[-1], "".join(L)))
    return "".join(out)


def mokuji_page_html():
    """読むページ（巻頭ページ）に入れる目次。本の目次と同じ並びで、1行の形。"""
    import mokuji1 as M1
    L = ['<section class="toc"><h2>目次</h2>'] + ['<p class="line">%s</p>' % esc(l) for l in M1.MAE]
    for num, fuda, title, groups in M1.chapters():
        L.append('<p class="ch">第%d章　【%s】%s</p>' % (num, esc(fuda), esc(title)))
        for name, items in groups:
            if name:
                L.append('<p class="grp2">■ %s</p>' % esc(name))
            L += ['<div class="it"><b>%s</b><span><span class="t">%s</span><br><span class="xo">→　%s</span></span></div>' % (nn, esc(M1.pair(nn)[0]), esc(M1.pair(nn)[1])) for nn in items]
    L += ['<p class="line">%s</p>' % esc(a % M1.N_ALL if "%d" in a else a) for a in M1.ATO]
    return "".join(L) + "</section>"


def index_inner(downloads):
    f35, f45 = FACTS["35"], FACTS["45"]
    dl35 = ('<a class="btn sub" href="files/daihon35.docx">Word</a><a class="btn sub" href="files/daihon35_book.pdf">PDF（本の形）</a>' if downloads else "")
    dl45 = ('<a class="btn sub" href="files/daihon45.docx">Word</a><a class="btn sub" href="files/daihon45_book.pdf">PDF（本の形）</a>' if downloads else "")
    dlnote = "" if downloads else '<p class="note" style="margin:14px 0 0">WordとPDFのファイルは、メールに添えてお送りします。</p>'
    return """<title>原稿のご確認ページ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="robots" content="noindex,nofollow,noarchive">
%s
<style>%s</style>
<div class="wrap">
<header>
<p class="eyebrow">ご確認用</p>
<h1>%s<small>（仮題）</small></h1>
<p class="by">%s　／　%s</p>
<p class="lead">原稿と、構成の案を、このページにまとめました。まずは、書いたものを全部入れた版（45個）をお出しします。ページ数が多いので、「このくらいまで減らしたい」などのご希望があれば、それに向けて調整を進めます。</p>
</header>
<nav class="toc" aria-label="このページの中身"><a href="#daihon">台本</a><a href="#katachi">形の候補</a><a href="#title">タイトル案</a><a href="#mokuji">目次</a><a href="#rough">イラストのラフ案</a><a href="#soudan">ご相談したいこと</a></nav>

<section id="daihon">
<h2><span class="n">1</span>台本（原稿）</h2>
<p class="note">まず全部書いた版が、45個の版です。項目を少なくした場合の例として、35個の版も用意しました。第1章（6つの絶対法則）、はじめに、おわりには、どちらも同じです。</p>
<div class="two">
<div class="ver"><h3>45個の版（全部入り）</h3>
<div class="fig"><div><b>%d個</b>第1章6 ＋ 39</div><div><b>%dページ</b>の見込み</div><div><b>%s</b></div></div>
<p>今ある原稿を、全部入れた版です。1項目は、5〜9ページ。まずは、こちらをご覧ください。</p>
<div class="btns"><a class="btn" href="daihon45.html">台本を読む</a><a class="btn sub" href="book45.html">本の形で見る（縦書き）</a>%s</div></div>
<div class="ver"><h3>35個の版（少なくした場合の例）</h3>
<div class="fig"><div><b>%d個</b>第1章6 ＋ 29</div><div><b>%dページ</b>の見込み</div><div><b>%s</b></div></div>
<p>中身が重なる項目を1つにまとめて、29個にした版です。1項目は5ページが基本で、柱になる9項目だけ、7〜9ページ。</p>
<div class="btns"><a class="btn" href="daihon35.html">台本を読む</a><a class="btn sub" href="book35.html">本の形で見る（縦書き）</a>%s</div></div>
</div>
<p class="note" style="margin:14px 0 0">ページ数は、A5判・縦書き・1行40字・1ページ16行で、実際に文字を流して数えた目安です。イラストは、まだ入っていません。</p>%s
</section>

<section id="katachi">
<h2><span class="n">2</span>形の候補</h2>
<p class="note">項目の数と、1項目の形と長さで、本全体のページ数が変わります。ご希望のページ数に合わせて、調整できます。同じ項目を4つの形で組んだ見本も、用意しました。</p>
<div class="tw"><table>
<tr><th>版</th><th>項目の数</th><th>1項目のページ</th><th>全体</th></tr>
<tr><td>45個・今の形（全部入り）</td><td>45</td><td>5〜9ページ</td><td class="num">%dページ</td></tr>
<tr><td>35個・今の形</td><td>35</td><td>5ページが基本（柱は7〜9）</td><td class="num">%dページ</td></tr>
<tr><td>45個・STEPを本文にする形</td><td>45</td><td>4ページか6ページ</td><td class="num">%dページ</td></tr>
</table></div>
<div class="btns" style="margin-top:14px"><a class="btn" href="katachi.html">4つの形の見本を見る</a></div>
</section>

<section id="title">
<h2><span class="n">3</span>タイトル案</h2>
<p class="note">今、考えている案です。</p>
<ol class="titles">%s</ol>
</section>

<section id="mokuji">
<h2><span class="n">4</span>目次</h2>
<p class="note">45個の版の目次です。左が「頭のいい人が絶対やらないこと」、矢印の先が「かわりにやっていること」です。</p>
%s
</section>

<section id="rough">
<h2><span class="n">5</span>イラストのラフ案</h2>
<p class="note">各項目に置く2コマ（伸びない人／頭のいい人）の、言葉の一覧です。絵そのものは、まだありません。</p>
<div class="btns"><a class="btn" href="rough.html">2コマの言葉の一覧を見る</a></div>
</section>

<section id="soudan">
<h2><span class="n">6</span>ご相談したいこと</h2>
<ul class="ask">
<li>本の大きさ（A5判か、四六判か）</li>
<li>縦書きか、横書きか</li>
<li>総ページ数の目安</li>
<li>色の数（1色、2色、フルカラー）</li>
<li>イラスト（どなたにお願いするか、点数の目安）</li>
<li>特典（本の中に、QRコードやLINEへの案内を入れてよいか）</li>
<li>今後の進め方と、入稿の時期</li>
</ul>
</section>

<footer>このページは、ご確認用にお送りしているものです。</footer>
</div>
""" % (FONT, INDEX_CSS, esc(TITLE), esc(K.AUTHOR), DATE,
       f45["items"], f45["pages"], f45["chars"], dl45, f35["items"], f35["pages"], f35["chars"], dl35, dlnote,
       f45["pages"], f35["pages"], FACTS["step"]["pages"],
       "".join("<li>%s</li>" % esc(t) for t in K.TITLES), mokuji_html())


# ================================================================ 2026-11-20：部分ごとに見る形（著者の指示）
# 入口のページに、本の順番で、部分を並べる（巻頭ページ／はじめに／第1章…／コラム候補／最後に）。
# できた部分だけ、クリックで読める。まだの部分は、「準備中」と出す。更新したら、UPDATES に1行足して、READY に足す。
PARTS = [  # (記号, 題, 中身の説明)
    ("kantou", "巻頭ページ", "はじめにの前まで（巻頭ページ、目次）"),
    ("hajimeni", "はじめに", "はじめに、この本の使い方"),
    ("ch1", "第1章", ""), ("ch2", "第2章", ""), ("ch3", "第3章", ""), ("ch4", "第4章", ""), ("ch5", "第5章", ""), ("ch6", "第6章", ""), ("ch7", "第7章", ""),
    ("column", "コラム候補", "章の間に入れるコラム"),
    ("owari", "おわりに", "おわりに、巻末のページ"),
]
READY = {"kantou": "2026/11/20", "hajimeni": "2026/11/20", "ch1": "2026/11/20", "ch2": "2026/11/20", "ch3": "2026/11/20", "ch4": "2026/11/20"}   # 読める部分 → いつの時点か
UPDATES = [("2026/11/20", "巻頭ページ、はじめに、第1章〜第4章と、書名・項目の言葉の案のページを掲載しました。")]
# あわせて見てもらう資料（記号, 題, 説明, 作るスクリプト, できるファイル）。3つとも、今の項目の数に合わせて作り直す
SHIRYO = [
    ("shomei", "書名の方向性　3案", "表紙の見本と、その書名にした時の中身を、3つの方向で比べます", "build_title3.py", "書名の方向性_3案.html"),
    ("kotoba", "やらない言葉の3パターン", "項目それぞれに、「やらない言葉」の案を3つずつ並べています", "build_sanpattern.py", "やらない言葉_3パターン.html"),
    ("kata", "項目タイトルの型　2案", "1ページ目と目次での見え方を、2つの型で比べます", "build_katachi.py", "タイトルの型_2案.html"),
]


def shiryo_pages():
    """3つの資料を作り直して、ご確認ページの中のページにする（一覧にもどる、の行を足す）。"""
    for key, ttl, ds, script, out in SHIRYO:
        subprocess.check_call([sys.executable, "-I", os.path.join(HERE, script)], cwd=ROOT, stdout=subprocess.DEVNULL)
        with open(os.path.join(ROOT, "build", out), encoding="utf-8") as f:
            doc = f.read()
        back = '<p style="margin:0 0 18px;font-size:14px;font-weight:700"><a href="./" style="color:var(--accent);text-decoration:none" onclick="if(document.referrer&&history.length>1){history.back();return false}">← 一覧にもどる</a></p>'
        assert doc.count('<div class="wrap">') == 1, out
        doc = doc.replace('<div class="wrap">', '<div class="wrap">' + back)
        write(key + ".html", '<!doctype html><html lang="ja"><head>%s<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
              '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style></head><body>%s</body></html>' % (HEAD, doc))   # 新しいものを、下に足していく
PART_CSS = """
.qpage{text-align:left}
.qpage .pr{font-size:14.5pt;font-weight:900;line-height:1.75;text-align:left;margin:0 !important}
.qpage .px{opacity:.82}
figure.fig{margin:8mm 0;padding:0;text-align:center}
figure.fig img{max-width:100%;height:auto;border:1px solid #dfe3ea;border-radius:8px}
figure.fig figcaption{font-size:9pt;color:#555;margin-top:2mm}
.pintro{margin:6mm 0 0;padding:5mm 6mm;background:#f5f7fa;border-radius:8px}
.pintro h4{margin-top:0}
.st{grid-template-columns:20mm 1fr}
.toc .grp2{font-size:9.5pt;font-weight:700;color:#555;margin:3mm 0 1mm}
"""


def body_fig(md, kk):
    """本文をHTMLに。挿絵の印（［挿絵：説明（assets/figures/…）］）は、絵にする。絵のファイルは site/fig/ に写す。"""
    figs = []
    def f(m):
        src = os.path.join(ROOT, m.group(2))
        if not os.path.exists(src):
            return m.group(0)
        os.makedirs(os.path.join(SITE, "fig"), exist_ok=True)
        name = "%s_%d%s" % (kk, len(figs) + 1, os.path.splitext(src)[1])
        shutil.copyfile(src, os.path.join(SITE, "fig", name))
        figs.append('<figure class="fig"><img src="fig/%s" alt="%s"><figcaption>挿絵（ラフ）：%s</figcaption></figure>' % (name, esc(m.group(1)), esc(m.group(1))))
        return "FIGFIGFIG%d" % (len(figs) - 1)
    md = re.sub(r"(?m)^［挿絵：(.+?)（(assets/figures/[^）]+)）］$", f, md)
    h = P3.body_html(md)
    for n, fig in enumerate(figs):
        h = h.replace("<p>FIGFIGFIG%d</p>" % n, fig)
    return h


def item_now(kk):
    """今の項目の形（頭の2行 → 本文 → 2コマのラフ → 3STEP → まとめ）。"""
    it = V.ITEMS[kk]
    x, o = B.pair_lines(it)
    c = B.koma(kk)
    ttl, steps, king = B.sheet(kk)
    one, pts, dakara, toi = B.matome(kk)
    st = "".join('<div class="st"><div class="lab">STEP<b>0%d</b></div><div><p class="do">%s</p></div></div>' % (n, esc(h)) for n, (h, v, note) in enumerate(steps, 1))
    return """<section class="item">
<div class="qpage"><div class="no">%s</div><p class="ttl">%s</p><p class="pr px">%s</p><p class="pr po">%s</p></div>
%s
<div class="tag">イラストのラフ案（2コマ）</div>
<div class="koma"><div class="k x"><span>伸びない人</span><b>%s</b><i>%s</i></div><div class="k o"><span>頭のいい人</span><b>%s</b><i>%s</i></div></div>
<div class="tag">今日からできる3STEP</div>
<div class="sheet">%s<div class="king"><span>「できた」の基準</span><p>%s</p></div></div>
<div class="mwrap"><div class="tag">まとめ</div>
<div class="matome"><p class="one">%s</p><p>%s</p><p>迷ったら、自分に聞きます。「%s」</p></div>
%s</div></section>""" % (kk, esc(it["t"]), esc(x), esc(o), body_fig(B.body(kk), kk),
                 esc(c[0][0]), esc(c[0][1]), esc(c[1][0]), esc(c[1][1]), st, esc(king), esc(one), esc(dakara), esc(toi), BP.hito_html(kk))


def part_bodies():
    """部分ごとの中身。{記号: (ページの題, [(id, 飛ぶ先の名前, html)])}"""
    P4.kind = lambda kk: ""
    BP.hito_html = lambda kk: ""     # 王様の一言は、いったん出さない（2026-11-20、著者の指示）。第1章の項目にも効く
    n_all = 6 + len(V.ITEMS)
    out = {k: [] for k, _, _ in PARTS}
    names = {}
    cur = None
    for kind, name, md in Z.sections():
        if kind == "cover":
            continue
        if kind == "toc":
            out["kantou"].append(("mokuji", "目次", mokuji_page_html()))
        elif kind == "text":
            key = "kantou" if name.startswith("10秒") else "hajimeni" if name in ("はじめに", "この本の使い方") else "owari"
            out[key].append(("t%d" % len(out[key]), name.replace("巻末　", "巻末｜"), BP.text_html(md)))
        elif kind == "door":
            cur = "ch" + name[1]
            if name == "第1章":
                intro = P3.body_html(Z.to_md(Z.master(K.CH1_INTRO)))
                h = ('<section class="chdoor"><div class="cno">第1章</div><h1>%s</h1><p class="fld">【%s】　01〜06番</p><div class="intro">%s</div></section>' % (esc(K.CH1_TITLE), esc(K.CH1_SUB), intro))
                names[cur] = ("第1章　" + K.CH1_TITLE, "01〜06番　6つの絶対法則")
            else:
                num, fuda, title, sub, groups = [c for c in V.CHAPTERS if "第%d章" % c[0] == name][0]
                ks = [kk for _, items in groups for kk in items]
                h = ('<section class="chdoor"><div class="cno">第%d章</div><h1>%s</h1><p class="fld">【%s】　%s〜%s番</p>%s<div class="intro">%s</div></section>'
                     % (num, esc(title), esc(fuda), ks[0], ks[-1], ('<p class="sub">%s</p>' % esc(sub)) if sub else "", P3.body_html(B.read_new("ch%d_導入" % num))))
                gs = "・".join(g for g, _ in groups if g)
                names[cur] = ("第%d章　【%s】%s" % (num, fuda, title), "%s〜%s番%s" % (ks[0], ks[-1], ("　" + gs) if gs else ""))
            out[cur].append(("door", "章の導入", h))
        elif kind == "group":
            num, fuda, title, sub, groups = [c for c in V.CHAPTERS if any(g[0] == name for g in c[4])][0]
            items = [g[1] for g in groups if g[0] == name][0]
            lines = "<br>".join("%s　%s" % (kk, esc(V.ITEMS[kk]["t"])) for kk in items)
            pi = B.part_intro(num, name)
            out[cur].append(("g%d" % len(out[cur]), "■ " + name,
                             '<section class="grp"><p class="g1">第%d章　【%s】</p><p class="g2">%s</p><p class="g3">%s</p></section>%s'
                             % (num, esc(fuda), esc(name), lines, ('<div class="pintro">%s</div>' % P3.body_html(pi)) if pi else "")))
        elif kind == "item1":
            out[cur].append(("i" + name, "　%s　絶対法則%s　%s" % (name, name, K.CH1_MOKUJI[name][0]), BP.item1_html(name)))
        elif kind == "item":
            out[cur].append(("i" + name, "　%s　%s" % (name, V.ITEMS[name]["t"]), item_now(name)))
        elif kind == "column":
            src = [(s, nm) for k, s, nm in K.COLUMNS if (Z.column(s, nm) or ("",))[0] == name][0]
            out["column"].append(("c%d" % len(out["column"]), name, BP.column_html(Z.column(*src))))
    return out, names


def part_page(key, title, secs):
    opts = "".join('<option value="%s">%s</option>' % (sid, esc(label)) for sid, label, _ in secs)
    body = "\n".join('<div class="sec" id="%s">%s</div>' % (sid, h) for sid, _, h in secs)
    return ('<!doctype html><html lang="ja"><head>%s<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>%s</title>%s<style>%s%s</style></head><body>'
            '<div class="bar">%s<b>%s</b><select id="jump" aria-label="読みたい所へ飛ぶ"><option value="">読みたい所へ飛ぶ</option>%s</select></div>'
            '<div class="top"><p>%s<span style="font-weight:700">（仮題）</span>　／　%s　／　%s 時点</p>'
            '<p>黄色の線は、原稿のマーカーの印です。「イラストのラフ案（2コマ）」は、絵にする前の、言葉の案です。</p></div>'
            '%s<script>document.getElementById("jump").addEventListener("change",function(){if(this.value){document.getElementById(this.value).scrollIntoView();this.value=""}});</script></body></html>'
            % (HEAD, esc(title), FONT, READ_CSS, PART_CSS, BACK, esc(title), opts, esc(TITLE), esc(K.AUTHOR), READY[key], body))


LIST_CSS = """
.parts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.parts li{display:grid;grid-template-columns:1fr auto;gap:4px 16px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line);min-width:0}
.parts li:first-child{padding-top:4px}
.parts li:last-child{border-bottom:0;padding-bottom:2px}
.parts .nm{font-weight:900;font-size:16.5px;line-height:1.6;min-width:0}
.parts .ds{grid-column:1;color:var(--sub);font-size:13px;line-height:1.6}
.parts .dt{font-size:12px;color:var(--sub);font-variant-numeric:tabular-nums;white-space:nowrap}
.parts .act{grid-column:2;grid-row:1 / span 2;display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.parts .wait{font-size:13px;font-weight:700;color:var(--sub);border:1px dashed var(--line);border-radius:8px;padding:6px 14px;white-space:nowrap}
.parts li.off .nm{color:var(--sub)}
.log{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.log li{display:grid;grid-template-columns:6.4em 1fr;gap:10px;font-size:14px}
.log b{font-variant-numeric:tabular-nums;color:var(--accent)}
"""


def index_now(names):
    rows = []
    for key, ttl, ds in PARTS:
        name, sub = names.get(key, (ttl, ds))
        if key in READY:
            rows.append('<li><span class="nm">%s</span><span class="ds">%s</span><span class="act"><a class="btn" href="%s.html">読む</a><span class="dt">%s 時点</span></span></li>'
                        % (esc(name), esc(sub), key, READY[key]))
        else:
            rows.append('<li class="off"><span class="nm">%s</span><span class="ds">%s</span><span class="act"><span class="wait">準備中</span></span></li>' % (esc(name), esc(sub)))
    log = "".join("<li><b>%s</b><span>%s</span></li>" % (d, esc(s)) for d, s in UPDATES)
    return """<title>原稿のご確認ページ</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="robots" content="noindex,nofollow,noarchive">
%s
<style>%s%s</style>
<div class="wrap">
<header>
<p class="eyebrow">ご確認用</p>
<h1>%s<small>（仮題）</small></h1>
<p class="by">%s　／　%s 時点</p>
<p class="lead">原稿を、できた所から、このページに置いていきます。今は、巻頭ページから第4章までを、お読みいただけます。第5章から先と、コラム、おわりには、仕上げている途中です。11月中に、誤字の確認まで含めて、全体を仕上げます。</p>
</header>

<section id="genko">
<h2>原稿</h2>
<p class="note">本の順番に並べています。「読む」を押すと、その部分が開きます。各項目には、イラストのラフ案（2コマの言葉）も入れています。</p>
<ul class="parts">%s</ul>
</section>

<section id="shiryo">
<h2>書名と、項目の言葉の案</h2>
<p class="note">書名の方向と、項目に入れる言葉を比べるためのページです。今の項目の数（%d）に合わせています。言葉は、どれも仮のものです。</p>
<ul class="parts">%s</ul>
</section>

<section id="kiroku">
<h2>更新の記録</h2>
<p class="note">更新したら、ここに足していきます。</p>
<ul class="log">%s</ul>
</section>

<section id="mokuji">
<h2>目次（今の案）</h2>
<p class="note">左が「頭のいい人が絶対やらないこと」、矢印の先が「かわりにやっていること」です。</p>
%s
</section>

<footer>このページは、ご確認用にお送りしているものです。</footer>
</div>
""" % (FONT, INDEX_CSS, LIST_CSS, esc(TITLE), esc(K.AUTHOR), max(READY.values()), "".join(rows), 6 + len(V.ITEMS),
       "".join('<li><span class="nm">%s</span><span class="ds">%s</span><span class="act"><a class="btn" href="%s.html">見る</a></span></li>' % (esc(a), esc(b), k) for k, a, b, _, _ in SHIRYO),
       log, mokuji_html())


def main():
    """部分ごとに見る形で作る（2026-11-20）。前の形（45個・35個の2つの版を並べる入口）は、main_old()。"""
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    os.makedirs(os.path.join(OUT, "artifact"), exist_ok=True)
    bodies, names = part_bodies()
    for key, ttl, ds in PARTS:
        if key in READY:
            write(key + ".html", part_page(key, names.get(key, (ttl, ds))[0], bodies[key]))
    shiryo_pages()
    inner = index_now(names)
    write("index.html", '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + inner + "</body></html>")
    with open(os.path.join(OUT, "artifact", "index.html"), "w", encoding="utf-8") as f:
        f.write(inner)
    for root, _, fs in os.walk(OUT):
        for fn in sorted(fs):
            q = os.path.join(root, fn)
            print("%8.1fKB  %s" % (os.path.getsize(q) / 1024, os.path.relpath(q, OUT)))


def main_old():

    os.makedirs(os.path.join(SITE, "files"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "artifact"), exist_ok=True)
    write("daihon35.html", reading("35"))
    write("daihon45.html", reading("45"))
    write("book45.html", book("45"))
    write("book35.html", book("35"))
    write("katachi.html", katachi())
    write("rough.html", rough())
    write("index.html", '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
          + index_inner(True) + "</body></html>")
    with open(os.path.join(OUT, "artifact", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_inner(False))
    # Word と PDF（ウェブサイトに置く時だけ使う）
    for mode, md, pdf in (("35", "manuscript/35個版/完全版_35個.md", "build/本の形_35個の版.pdf"), ("45", "manuscript/完全版/完全版_仮.md", "build/本の形_マックス版.pdf")):
        subprocess.check_call(["pandoc", os.path.join(ROOT, md), "-f", "markdown+mark+hard_line_breaks-yaml_metadata_block", "-o", os.path.join(SITE, "files", "daihon%s.docx" % mode)])
        shutil.copyfile(os.path.join(ROOT, pdf), os.path.join(SITE, "files", "daihon%s_book.pdf" % mode))
    for root, _, fs in os.walk(OUT):
        for fn in sorted(fs):
            p = os.path.join(root, fn)
            print("%8.1fKB  %s" % (os.path.getsize(p) / 1024, os.path.relpath(p, OUT)))


if __name__ == "__main__":
    main()
