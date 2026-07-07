# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル
第3部-Ⅴ 大問Ⅴ「短文空所補充」完全攻略ドリル

大問Ⅴ（解答番号45〜50・6マーク）＝短い英文の空所に、語法・イディオム・準動詞・時制を
ピンポイントで補う。語彙問題の顔をした文法問題。全訳せず狙われた文法点を一撃で判定する。
本冊は文法分野別に成蹊型オリジナル短文問題を多数収録し、一撃判定の型を体に入れる。
"""
import re
import seikei_common as C
from seikei_common import esc, _raw

RUNNING = "成蹊大学 経営学部 英語 完全攻略マニュアル【第3部-Ⅴ】大問Ⅴ 短文空所補充ドリル"
OUT = "/home/user/thinking-hp/dist/成蹊大学_経営学部_英語_完全攻略マニュアル_第3部-Ⅴ_大問Ⅴ短文空所補充ドリル.pdf"

BLANK = re.compile(r"\(\s*\)")
CHOICE_LABELS = ["ア", "イ", "ウ", "エ"]


def blankify(text):
    return BLANK.sub('<span class="blk">（&nbsp;&nbsp;&nbsp;）</span>', esc(text))


def _distribute(item):
    """正解(choices[0])を no に応じた位置へ分散。"""
    choices = item["choices"]
    n = len(choices)
    t = item["no"] % n
    correct = choices[0]
    rest = choices[1:]
    disp, ri = [], 0
    for pos in range(n):
        if pos == t:
            disp.append(correct)
        else:
            disp.append(rest[ri]); ri += 1
    return disp, CHOICE_LABELS[t]


def render_item_problem(item):
    disp, _ = _distribute(item)
    chs = "".join(
        f'<span class="d5ch"><span class="d5lab">{CHOICE_LABELS[i]}.</span>{esc(c)}</span>'
        for i, c in enumerate(disp))
    return (f'<div class="d5item"><div class="d5q">'
            f'<span class="d5no">{item["no"]}.</span>{blankify(item["sentence"])}</div>'
            f'<div class="d5choices">{chs}</div></div>')


def render_section_problems(sec, show_head=True):
    head = (f'<div class="miniband">{esc(sec["cat"])}　<span style="font-weight:400;font-size:8.5pt">'
            f'{esc(sec.get("desc",""))}</span></div>') if show_head else ""
    items = "".join(render_item_problem(it) for it in sec["items"])
    return f'<div class="d5sec">{head}{items}</div>'


def render_item_answer(item):
    disp, lab = _distribute(item)
    parts = [f'<div class="d5aitem"><div class="d5ahead">'
             f'<span class="d5ano">{item["no"]}</span>'
             f'<span class="d5correct">正解 {lab}</span>'
             f'<span class="d5point">{_raw(item.get("point",""))}</span></div>']
    parts.append('<div class="d5exp">')
    if item.get("exp"):
        parts.append(f'<p><span class="ex-lab">根拠</span>{_raw(item["exp"])}</p>')
    if item.get("cut"):
        parts.append(f'<p><span class="ex-lab ng">切り</span>{_raw(item["cut"])}</p>')
    if item.get("trans"):
        parts.append(f'<p class="d5tr"><span class="ex-lab" style="background:var(--gold-deep)">訳</span>{_raw(item["trans"])}</p>')
    parts.append('</div></div>')
    return "".join(parts)


def render_section_answers(sec):
    head = f'<div class="miniband">{esc(sec["cat"])} ― 解説</div>'
    items = "".join(render_item_answer(it) for it in sec["items"])
    return f'<div class="d5sec">{head}{items}</div>'


EXTRA_CSS = """
.d5sec{ margin:0 0 2mm; }
.d5item{ padding:1.4mm 0; border-bottom:0.4pt dotted var(--line); page-break-inside:avoid; }
.d5q{ font-family:"Noto Serif CJK JP","Times New Roman",serif; font-size:9.7pt; line-height:1.7; }
.d5no{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--gold-deep); margin-right:2mm; }
.d5choices{ display:flex; flex-wrap:wrap; gap:1mm 6mm; margin:1mm 0 0 6mm; }
.d5ch{ font-family:"Times New Roman",serif; font-size:9.3pt; white-space:nowrap; }
.d5lab{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy-soft); margin-right:1.5mm; }
.d5aitem{ padding:1.6mm 0; border-bottom:0.4pt solid var(--line); page-break-inside:avoid; }
.d5ahead{ display:flex; align-items:center; gap:3mm; }
.d5ano{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt; color:#fff; background:var(--navy);
        border-radius:1mm; padding:.2mm 2.4mm; }
.d5correct{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--vermilion); font-size:9.4pt; }
.d5point{ font-family:"Noto Sans CJK JP"; font-size:8.4pt; color:var(--gold-deep); }
.d5exp{ margin:1mm 0 0 2mm; }
.d5exp p{ font-size:9.1pt; line-height:1.65; margin:.5mm 0; }
.d5tr{ color:var(--gray); }
.ex-lab{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:7.6pt; color:#fff; background:var(--navy-soft);
       border-radius:1mm; padding:0 1.6mm; margin-right:2mm; white-space:nowrap; }
.ex-lab.ng{ background:var(--vermilion); }
.cv-instr{ font-family:"Noto Sans CJK JP"; font-size:8.8pt; color:var(--ink); background:var(--washi);
       border-left:3pt solid var(--navy); padding:2mm 3.5mm; margin:2mm 0 3mm; line-height:1.7; }
"""

FRONT = "".join([
    '<section style="page-break-before:always"></section>',
    C.h2("はじめに ― 大問Ⅴは「語彙の顔をした文法」を一撃で仕留める"),
    C.p("成蹊 経営の大問Ⅴ（解答番号45〜50・<b>6マーク</b>）は、短い英文の空所に語を補う形式。"
        "だが中身は<b>語法・イディオム・準動詞・時制・仮定法</b>のピンポイント――"
        "『語彙問題の顔をした文法問題』だ。短文なので<b>全訳は不要</b>。"
        "狙われている文法ポイントを一撃で見抜いて即マークする、これが満点への最短路だ。"),
    C.p("Ⅴは短く確実な<b>最優先の得点源</b>。時間配分でも先に解く（推奨順序 Ⅴ→Ⅳ→Ⅰ→Ⅱ→Ⅲ）。"
        "ここで頭を英語モードに温め、語法・イディオムの知識で<b>満点近く</b>を狙う。"),
    C.callout("この巻の到達目標", C.dots([
        "空所を見た瞬間に<b>狙われている文法分野</b>（時制／仮定法／準動詞／語法／イディオム）を判定できる。",
        "紛らわしいペア（<span class='en'>lie/lay, rise/raise</span> 等）や句動詞・前置詞を確実に処理する。",
        "6マーク中<b>5以上（83%）</b>を安定させ、Ⅴを満点近い得点源にする。",
    ])),
    C.p("本巻は成蹊型オリジナルの短文空所問題を<b>分野別に多数</b>収録し、全問に"
        "『狙われた文法点・根拠・誤答の切り方・訳』を付す。実際の過去問は転載していない。"),
    C.box("この巻の使い方", C.steps([
        "第0章「Ⅴ型の解法」で、分野判定の手順を頭に入れる。",
        "分野別に解き、間違えた問題の<b>文法点</b>を記録する（時制か・準動詞か・語法か）。",
        "答え合わせは解説の『根拠・切り』を音読し、狙われるポイントを言語化する。",
        "巻末の『語法・イディオム最終チェック』で、頻出の型を総ざらいする。",
    ])),
    C.h2("目次"),
    '<div class="toc">',
    '<div class="row"><span class="n">第0章</span><span class="t">Ⅴ型の解法 ― 分野判定の一撃メソッド</span><span class="pg">strategy</span></div>',
    '<div class="row"><span class="n">問題編</span><span class="t">分野別 成蹊型オリジナル短文問題</span><span class="pg">problems</span></div>',
    '<div class="row"><span class="n">解説編</span><span class="t">全問の狙い・根拠・切り方・訳</span><span class="pg">answers</span></div>',
    '<div class="row"><span class="n">付録</span><span class="t">語法・イディオム最終チェック ／ 紛らわしいペア一覧</span><span class="pg">appendix</span></div>',
    '</div>',
])

STRATEGY = "".join([
    C.chapter("CHAPTER 0 / 解法の型",
        "Ⅴ型の解法 ― 分野を見抜いて一撃で判定する",
        "短文空所は『全部読んで意味を取る』のではなく、『狙われた文法点を見抜く』ゲームだ。"
        "空所の周りの手がかり（主語・時制語・to/-ing・前置詞）から分野を特定し、一撃で決める。"),
    C.miniband("0-1 まず分野を判定する ― 空所周りの手がかり"),
    C.p("空所を見たら、周りの<b>手がかり語</b>から狙われている分野を特定する。分野が分かれば、選択肢の切り方は決まっている。"),
    C.table(
        ["手がかり", "疑うべき分野", "一撃の判定"],
        [
            ["<span class='en'>if / were / had + 過去分詞</span>", "仮定法", "条件節の形→帰結節の助動詞を合わせる。"],
            ["<span class='en'>to / 前置詞 + 空所</span>", "準動詞", "to＋原形／前置詞＋動名詞を判定。"],
            ["時を表す語（<span class='en'>since, by, ago</span>）", "時制・相", "since→完了、by＋未来→未来完了。"],
            ["紛らわしい動詞ペア", "自動詞/他動詞", "<span class='en'>lie/lay, rise/raise</span> を活用で判別。"],
            ["空所後の前置詞・副詞", "イディオム・句動詞", "コロケーションで確定。"],
            ["<span class='en'>than / as / the 比較級</span>", "比較", "比較級・最上級・原級の形を合わせる。"],
        ],
        [None, None, None]),
    C.miniband("0-2 一撃メソッド ― 全訳しない"),
    C.box("Ⅴの3ステップ", C.steps([
        "空所の<b>直前直後</b>と、文全体の<b>時制・主語・接続</b>だけを見る（全訳しない）。",
        "手がかりから<b>狙われた分野を特定</b>し、その分野の判定ルールを当てる。",
        "選択肢を<b>形</b>で絞る（時制・態・活用）。意味は最後の確認に使う。",
    ])),
    C.warn("Ⅴで落ちる典型",
        C.p("①短文なのに全訳して時間を溶かす　②<span class='en'>lie（自動詞）と lay（他動詞）</span>の活用を混同する　"
            "③仮定法の帰結節の助動詞を落とす。対策：分野を先に特定し、形で切る。意味は最後。")),
    C.callout("この章の結論",
        C.p("Ⅴは<b>知識で満点近くを狙う最優先の得点源</b>。空所を見たら分野を判定し、形で一撃。"
            "次ページからは分野別の実戦だ。狙われたポイントを見抜く目を作れ。")),
])

import importlib, os
SECTIONS = []
_here = os.path.dirname(__file__)
for _n in range(1, 23):
    _path = os.path.join(_here, "d5_sets", f"cat_{_n:02d}.py")
    if os.path.exists(_path):
        _m = importlib.import_module(f"d5_sets.cat_{_n:02d}")
        SECTIONS.append(_m.SECTION)

try:
    from d5_appendix import APPENDIX
except Exception:
    APPENDIX = ""


def _renumber():
    n = 1
    for sec in SECTIONS:
        for it in sec["items"]:
            it["no"] = n
            n += 1
    return n - 1


def build():
    total = _renumber()
    css = C.build_css(RUNNING) + EXTRA_CSS
    body = []
    body.append(C.cover("第 3 部 - Ⅴ / 大問Ⅴ", "短文空所補充 攻略ドリル", RUNNING, badge="短文空所"))
    body.append(FRONT)
    body.append(STRATEGY)
    body.append(C.chapter("PROBLEMS / 問題編",
        f"成蹊型 短文空所補充 ― 分野別オリジナル演習（全{total}問）",
        "語法・イディオム・準動詞・時制・仮定法を分野別に集めた。空所を見たら全訳せず、"
        "狙われた文法点を一撃で判定して即マーク。まず分野を見抜く目を、この演習で作れ。"))
    for sec in SECTIONS:
        body.append(render_section_problems(sec))
    body.append(C.chapter("ANSWERS / 解答解説編",
        f"全{total}問 ― 狙い・根拠・切り方・訳の完全解剖",
        "1問ごとに『狙われた文法点・正解の根拠・誤答の切り方・訳』を示す。"
        "分野ごとの判定ルールを、解説を通して手順として体に入れろ。"))
    for sec in SECTIONS:
        body.append(render_section_answers(sec))
    body.append(APPENDIX)
    html = C.document(css, body)
    C.write_pdf(html, OUT)
    print("built:", OUT, "sections:", len(SECTIONS), "items:", total)


if __name__ == "__main__":
    build()
