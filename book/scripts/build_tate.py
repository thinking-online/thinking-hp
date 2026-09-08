# -*- coding: utf-8 -*-
"""縦組みの読者版を組む。book/ で実行する。
横組み版（build_pdf.py）は編集用で、docs への参照や「右ページ／左ページ」などの
注記が入っている。こちらは読者が手に取る姿にするため、それらを落とす。
判型はA5（148×210mm）、本文は明朝、見出しはゴシック。"""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pdf as bp

# ---- 縦組み用の追加処理 --------------------------------------------------

def tatechuyoko(s):
    """算用数字を縦中横にする。3桁以上は正立させて縦に積む。"""
    s = re.sub(r'(?<![0-9])([0-9]{3,})(?![0-9])', r'<span class="upr">\1</span>', s)
    s = re.sub(r'(?<![0-9>])([0-9]{1,2})(?![0-9<])', r'<span class="tcy">\1</span>', s)
    return s

_orig_inline = bp.inline
def inline_v(s):
    return tatechuyoko(_orig_inline(s))

# 読者版で落とす見出し（構造の注記であって、本文ではないもの）
DROP_H2 = {"右ページ", "左ページ", "問題ページ", "答えページ",
           "左ページ上", "右ページ下", "左ページ上　この見開きの一行", "45"}
DROP_H3 = {"隅の図", "状況文"}

def md_to_html_v(text, accent=""):
    bp.HR_AS_PAGEBREAK = False
    h = bp.md_to_html(text, accent)
    # ページラベルは改ページだけ残して文字は消す
    h = re.sub(r'<div class="pagelabel(?: newpage)?">(.*?)</div>',
               lambda m: '<div class="pagebreak"></div>' if "左ページ" in m.group(1) else '', h)
    # 隅の図（デザイナー向けの作図指示）と、状況文のラベルを落とす
    h = re.sub(r'<div class="lbl lbl-corner">.*?</div>\s*<p class="cornerfig">.*?</p>', '', h, flags=re.S)
    h = h.replace('<div class="lbl lbl-situ">状況文</div>', '')
    # 章扉の「問題ページ／答えページ」の見出しは、改ページに置き換える
    h = re.sub(r'<h2>問題ページ</h2>', '', h)
    h = re.sub(r'<h2>答えページ</h2>', '<div class="pagebreak"></div>', h)
    h = re.sub(r'<h[23]>(左ページ上|右ページ下|左ページ|右ページ|45)</h[23]>', '', h)
    h = re.sub(r'<h2>[0-9]+ページ目</h2>', '<div class="pagebreak"></div>', h)
    h = re.sub(r'<h2><span class="tcy">[0-9]+</span>ページ目</h2>', '<div class="pagebreak"></div>', h)
    h = re.sub(r'<div class="sep"></div>\s*(?=<div class="pagebreak">)', '', h)
    h = re.sub(r'<div class="sep"></div>\s*(?=<h1)', '', h)
    h = re.sub(r'^\s*<div class="pagebreak"></div>', '', h)
    h = re.sub(r'(?:<div class="pagebreak"></div>\s*)+(?=<div class="pagebreak"></div>)', '', h)
    return h

def render_v(path, accent=""):
    raw = open(os.path.join(bp.M, path), encoding="utf-8").read()
    head, body, _note = bp.strip_meta(raw)      # 注記は読者版では出さない
    return md_to_html_v(head + "\n\n" + body, accent)

CSS = """
@page { size: A5; margin: 17mm 15mm 15mm 15mm; }
@page :first { margin: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact;
       writing-mode: vertical-rl; text-orientation: mixed; }
body { font-family: "Noto Serif CJK JP","IPA明朝",serif; font-size: 9.5pt; line-height: 1.7;
       color: #1a1a1a; margin: 0; }
p { margin: 0 0 .8em 0; text-indent: 0; }
.tcy { text-combine-upright: all; }
.upr { text-orientation: upright; letter-spacing: -.05em; }
code { font-size: .9em; color: #666; }
hr.rule { border: 0; border-right: 1px solid #ddd; margin: 0 1.4em; }
h1 { font-family: "Noto Sans CJK JP",sans-serif; font-size: 13pt; font-weight: 700;
     line-height: 1.5; margin: 0 0 1.8em 0; padding-right: .7em;
     border-right: 3px solid #1a1a1a; page-break-before: always; page-break-after: avoid; }
h2 { font-family: "Noto Sans CJK JP",sans-serif; font-size: 11pt; font-weight: 700;
     margin: 2.2em 0 1.1em 0; page-break-after: avoid; }
h3 { font-family: "Noto Sans CJK JP",sans-serif; font-size: 9.8pt; font-weight: 700;
     margin: 1.7em 0 .7em 0; page-break-after: avoid; }
h4 { font-family: "Noto Sans CJK JP",sans-serif; font-size: 9.4pt; margin: 1.4em 0 .6em 0; }
ul { margin: 0 0 1em 0; padding: 0 1.1em 0 0; }
li { margin-bottom: .4em; }
.pagebreak { page-break-before: always; width: 0; }
.sep { height: 0; margin: 0 1.2em 0 0; border-right: 1px solid #e6e6e6; }
/* 小見出しラベル */
.lbl { font-family: "Noto Sans CJK JP",sans-serif; font-size: 7.6pt; color: #8a8a8a;
       margin: .95em 0 .3em 0; letter-spacing: .08em; page-break-after: avoid;
       text-orientation: upright; }
.lbl-good { border-right: 2px solid #1a1a1a; padding-right: .45em; margin-right: -.6em; }
.qtext { font-family: "Noto Sans CJK JP",sans-serif; font-size: 12.5pt; font-weight: 700;
         line-height: 1.55; margin: 0 0 1.4em 0; }
.hintbox { background: #f5f4ef; border-right: 3px solid #c9c2a6; padding: .6em .6em .6em 0;
           margin: 0 0 1em 0; font-size: 8.6pt; }
.lawbox { font-family: "Noto Sans CJK JP",sans-serif; font-size: 10.8pt; font-weight: 700;
          line-height: 1.45; padding: .6em .6em .6em 0; margin: .15em 0 .85em 0;
          border-right: 4px solid #1a1a1a; background: #f6f6f6; }
.lawbox.f1 { border-right-color: #2f6fb0; } .lawbox.f2 { border-right-color: #2e8b57; }
.lawbox.f3 { border-right-color: #a8791b; } .lawbox.f4 { border-right-color: #cc3d78; }
.lawbox.f5 { border-right-color: #c0392b; } .lawbox.f6 { border-right-color: #7b3fa0; }
.conclbox { border-right: 1px solid #ddd; padding-right: .65em; margin: 0 0 .8em 0; }
.rubric { font-family: "Noto Sans CJK JP",sans-serif; font-size: 7.6pt; color: #8a8a8a;
          line-height: 1.65; margin: 0 0 1.2em 0; }
.ans { margin: 0 0 .8em 0; }
.indent { margin: 0 0 1em 0; white-space: pre-wrap; font-size: 9pt; }
.figbox { border: 1px dashed #b5b5b5; color: #777; padding: .9em 1.4em; margin: 1.2em 0;
          font-size: 8.4pt; background: #fafafa; text-align: center; }
/* 分かれ道は縦の表にする（右の列から左へ読む。日本語の本の作法） */
table { border-collapse: collapse; font-size: 8pt; margin: .3em 0 1.4em 0; line-height: 1.6; }
th, td { border: 1px solid #ccc; padding: .45em .35em; vertical-align: top; text-align: start; }
th { background: #f2f2f2; font-family: "Noto Sans CJK JP",sans-serif; font-weight: 700; }
.vs { font-size: 7.6pt; float: inline-start; margin: 0 0 .9em 1.1em; clear: both; }
.vs th, .vs td { height: 40mm; }
.vs tr:first-child th { background: #f2f2f2; color: #8a8a8a; font-size: 7.6pt; }
.vs tr:first-child th:nth-child(2), .vs tr:first-child th:nth-child(3) { color: #333; font-size: 8pt; }
.vs td:first-child, .vs th:first-child { background: #fafafa; color: #8a8a8a; font-size: 6.8pt; height: 17mm; }
.vs td:nth-child(3) { background: #f4f4f4; }
.vs.f1 td:nth-child(3), .vs.f1 th:nth-child(3) { background: #eef4fb; }
.vs.f2 td:nth-child(3), .vs.f2 th:nth-child(3) { background: #eef6f1; }
.vs.f3 td:nth-child(3), .vs.f3 th:nth-child(3) { background: #faf4e6; }
.vs.f4 td:nth-child(3), .vs.f4 th:nth-child(3) { background: #fdf0f5; }
.vs.f5 td:nth-child(3), .vs.f5 th:nth-child(3) { background: #fbeeec; }
.vs.f6 td:nth-child(3), .vs.f6 th:nth-child(3) { background: #f5eefa; }
.cklist { margin: 0 0 1.2em 0; }
.ck { display: flex; align-items: flex-start; gap: .45em; padding: .17em 0; font-size: 8.2pt; }
.ck .n { width: 1.6em; text-align: right; color: #9a9a9a; font-size: 7.4pt; padding-top: .15em; }
.ck .box { width: .8em; height: .8em; border: 1px solid #9a9a9a; flex: none; margin-top: .3em; }
.ck .t { flex: 1; line-height: 1.5; }
.frows { writing-mode: horizontal-tb; width: 70mm; margin: 0 0 1.3em 0; }
.frow { display: flex; align-items: baseline; gap: .5em; padding: .45em 0; font-size: 8.6pt; }
.frow .fl { white-space: nowrap; }
.frow .fd { flex: 1; border-bottom: 1px solid #cfcfcf; height: .85em; }
.frow .fu { white-space: nowrap; color: #777; font-size: 8pt; }
/* 扉 */
.cover { writing-mode: horizontal-tb; box-sizing: border-box;
         padding: 46mm 20mm 24mm 20mm; page-break-after: always;
         font-family: "Noto Serif CJK JP",serif; }
.cover .kicker { font-size: 8pt; color: #888; letter-spacing: .1em; }
.cover .t { font-size: 17pt; line-height: 1.6; margin: 1.3em 0 .7em 0; font-weight: 700; }
.cover .s { font-size: 10.5pt; color: #333; margin-bottom: 4em; }
.cover .obi { font-size: 8.8pt; line-height: 1.95; border-top: 1px solid #ccc;
              border-bottom: 1px solid #ccc; padding: 1em 0; margin-bottom: 3em; }
.cover .au { font-size: 10.5pt; }
.cover .note { font-size: 7.6pt; color: #999; margin-top: 3em; line-height: 1.8; }
.part { page-break-before: always; page-break-after: always; padding-right: 30mm; }
.part .num { font-family: "Noto Sans CJK JP",sans-serif; font-size: 8pt;
             letter-spacing: .2em; color: #999; }
.part .ttl { font-family: "Noto Sans CJK JP",sans-serif; font-size: 16pt; font-weight: 700;
             line-height: 1.6; margin-right: .9em; }
.part .bar { width: 3px; height: 34mm; background: #1a1a1a; margin-right: 1.6em; }
.part.f1 .bar { background: #2f6fb0; } .part.f2 .bar { background: #2e8b57; }
.part.f3 .bar { background: #a8791b; } .part.f4 .bar { background: #cc3d78; }
.part.f5 .bar { background: #c0392b; } .part.f6 .bar { background: #7b3fa0; }
.toc { page-break-after: always; }
.toc h1 { page-break-before: avoid; }
.toc .row { font-size: 9pt; padding: .45em 0; border-right: 1px dotted #e0e0e0; }
.toc .grp { font-family: "Noto Sans CJK JP",sans-serif; font-size: 7.6pt;
            letter-spacing: .16em; color: #9a9a9a; margin-right: 1.2em; }
"""

def build(outpath):
    bp.inline = inline_v            # 数字の縦中横を有効にする
    P = []
    P.append("""<div class="cover">
<div class="kicker">縦組み　読者版　（2026年9月8日時点）</div>
<div class="t">あの子が、<br>勉強中に絶対にやらないこと</div>
<div class="s">マネするだけで伸びる、あの子の勉強法則45</div>
<div class="obi">やっているのに、伸びない。<br>あの子は、やればやるだけ伸びる。<br>違いは、昨日、何個できるようになったか。<br>勉強時間は、1分も増やしません。</div>
<div class="au">朝倉 徹大</div>
<div class="note">A5・縦組み。編集用の注記は外してあります。<br>
表は日本語の本の通例に従って横組みで置いています。図は入る位置のみ。<br>
柱とノンブルは、実際の紙面ではデザイン側で入ります。</div>
</div>""")

    ch_titles = {1:"【考え方】同じ参考書、同じ3時間。なぜ差がつくのか",
                 2:"【決め方】何をやらないかを、先に決める", 3:"【見つけ方】「全部わからない」を、1行に絞る",
                 4:"【覚え方】1つ覚えて、10動かす", 5:"【確かめ方】わかった、を、できる、に変える",
                 6:"【直し方】間違いを、次の1個に変える", 7:"【続け方】試験の日まで、数を落とさない"}
    toc = ['<div class="toc"><h1>目次</h1>', '<div class="grp">前付</div>']
    for t in ["はじめに　毎日5時間やって、伸びない子がいた", "あの子が、絶対にやらない45のこと", "序章　あなたは、何を数えている？"]:
        toc.append(f'<div class="row">{inline_v(t)}</div>')
    toc.append('<div class="grp">本文</div>')
    for c in range(1, 8):
        toc.append(f'<div class="row">第{c}章　{inline_v(ch_titles[c])}</div>')
    toc.append('<div class="grp">後付</div>')
    for t in ["まとめ　45の法則を、そのままパクる", "この本を読んだ子の、親へ", "付録　できないノート／最初の1週間",
              "おわりに　偏差値42の僕も、時間を数えていた"]:
        toc.append(f'<div class="row">{inline_v(t)}</div>')
    toc.append("</div>")
    P.append("\n".join(toc))

    P.append(render_v("はじめに.md"))
    h = render_v("やらない45.md")
    h = re.sub(r'(<h3>第1章</h3>)(.*?)(?=<div class="pagebreak">|$)',
               lambda m: '<div class="cols2">' + m.group(1) + m.group(2) + '</div>', h, flags=re.S)
    P.append(h)
    P.append(render_v("序章.md"))
    P.append(f'<div class="part"><div class="num">第 1 章</div>'
             f'<div class="ttl">あの子の頭のなかでは、<br>何が起きているのか</div><div class="bar"></div></div>')
    P.append(render_v("第1章.md"))
    for c in range(2, 8):
        force = bp.FORCE_OF_CH[c]; cls = bp.CLASS_OF_FORCE[force]
        P.append(f'<div class="part {cls}"><div class="num">第 {c} 章</div>'
                 f'<div class="ttl">あの子には<br>「{force}」がある</div><div class="bar"></div></div>')
        raw = open(os.path.join(bp.M, f"第{c}章_扉.md"), encoding="utf-8").read()
        tobira, chap_end = bp.split_chapter_end(raw)
        head, body, _ = bp.strip_meta(tobira)
        P.append(md_to_html_v(head + "\n\n" + body, cls))
        a, b = bp.CH[c]
        for n in range(a, b + 1):
            P.append(render_v(f"法則{n}.md", cls))
        if chap_end:
            P.append('<div class="pagebreak"></div>' + md_to_html_v(chap_end, cls))
    for f in ["まとめ.md", "親へ.md", "付録.md", "おわりに.md"]:
        P.append(render_v(f))

    doc = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
           f"<title>台本 縦組み</title><style>{CSS}</style></head><body>\n"
           + "\n".join(P) + "\n</body></html>")
    open(outpath, "w", encoding="utf-8").write(doc)
    return outpath

if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    print(build("build/台本_縦組み.html"))
