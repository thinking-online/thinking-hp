# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル
第3部-Ⅲ 大問Ⅲ「長文読解（英問英答）」完全攻略ドリル

大問Ⅲ（解答番号32〜40・9マーク）＝ビジネス論説に、設問文がすべて英語の問いが付く。
指示語の特定・下線部言い換え・内容真偽・overall content（主旨）まで、英語で問われる
負荷が成蹊Ⅲの山場。本冊は成蹊型オリジナル長文8本＋英問英答の全設問解説で構成する。
"""
import seikei_common as C
import reading_common as R
from seikei_common import esc

RUNNING = "成蹊大学 経営学部 英語 完全攻略マニュアル【第3部-Ⅲ】大問Ⅲ 英問英答 長文読解ドリル"
OUT = "/home/user/thinking-hp/dist/成蹊大学_経営学部_英語_完全攻略マニュアル_第3部-Ⅲ_大問Ⅲ英問英答長文読解ドリル.pdf"

FRONT = "".join([
    '<section style="page-break-before:always"></section>',
    C.h2("はじめに ― 大問Ⅲは「英語で問われる」負荷を捌く"),
    C.p("成蹊 経営の大問Ⅲ（解答番号32〜40・<b>9マーク</b>）は、ビジネス論説に"
        "<b>設問文がすべて英語</b>で付く読解問題である。問われるのは指示語の特定、下線部の言い換え、"
        "内容真偽（true / NOT true）、そして <span class='en'>overall content</span>（主旨）の選択。"
        "設問まで英語で読む分の負荷が、成蹊Ⅲの山場になる。"),
    C.p("だが裏を返せば、Ⅲは<b>設問英文の読み方さえ手順化すれば</b>安定して稼げる。"
        "設問を先に読み、<b>何を探すか（who / what / why / 指示語）</b>を確定してから本文に戻る。"
        "この一手で、英語の設問は『負荷』から『道しるべ』に変わる。"),
    C.callout("この巻の到達目標", C.dots([
        "英語の設問文を<b>疑問詞・キーワードで即座に分類</b>し、探す情報を先に決められるようにする。",
        "指示語・言い換え・真偽・主旨の4タイプを、英語設問のまま解法手順に乗せる。",
        "<span class='en'>true / NOT true</span> と <span class='en'>2つ選ぶ</span> の指示を読み飛ばす事故を根絶する。",
        "9マーク中<b>6マーク以上</b>を安定させ、Ⅲを『捨てる大問』にしない。",
    ])),
    C.p("本巻は完全オリジナルの成蹊型長文<b>8本</b>と、英語設問の全問について"
        "「設問の読み解き・根拠となる本文箇所・誤答の切り方」を示した解説で構成する。実際の過去問は転載していない。"),
    C.box("この巻の使い方", C.steps([
        "第0章「英問英答の読み方」で、設問英文の分類と手順を頭に入れる。",
        "1本を<b>目標15分</b>で通す。設問英文を先読みし、探す情報を決めてから本文へ。",
        "答え合わせでは、設問英文を<b>自分で和訳</b>し直し、何を問われていたかを言語化する。",
        "全訳と語彙で、本文・設問双方の読めなかった原因を特定する。",
    ])),
    C.h2("目次"),
    '<div class="toc">',
    '<div class="row"><span class="n">第0章</span><span class="t">英問英答の読み方 ― 設問英文の分類と手順</span><span class="pg">strategy</span></div>',
    '<div class="row"><span class="n">問題編</span><span class="t">成蹊型オリジナル英問英答長文 READING 01〜11</span><span class="pg">problems</span></div>',
    '<div class="row"><span class="n">解説編</span><span class="t">英語設問の読み解き＋根拠・切り方＋全訳</span><span class="pg">answers</span></div>',
    '<div class="row"><span class="n">付録</span><span class="t">英語設問 定型フレーズ50 ／ 主旨問題チェックリスト</span><span class="pg">appendix</span></div>',
    '</div>',
])

STRATEGY = "".join([
    C.chapter("CHAPTER 0 / 読み方の設計",
        "英問英答の読み方 ― 設問英文を「道しるべ」に変える",
        "設問が英語だと身構える受験生は多い。だが設問英文は本文の要点を先に教えてくれる地図でもある。"
        "疑問詞とキーワードで設問を分類し、探すものを決めてから本文へ――この順序がⅢを安定させる。"),

    C.miniband("0-1 大問Ⅲの構成 ― 9マークの内訳"),
    C.p("成蹊Ⅲは9マーク。設問はすべて英語。問われるタイプは大きく4つに分かれる。"
        "<span class='en'>問7 のように『2つ選ぶ』（2マーク）</span>が混じることもあるので、個数指定に注意する。"),
    C.table(
        ["タイプ", "英語設問の典型", "処理方針"],
        [
            ["指示語", "What does <span class='en'>“it / this / they”</span> refer to?", "直前の文へ戻り、代入して意味が通る名詞を選ぶ。"],
            ["言い換え", "What does the underlined word mean? / is closest to", "語彙知識＋文脈で同義語を確定。"],
            ["内容真偽", "Which is true / NOT true according to the passage?", "選択肢のキーワードを本文照合。<b>NOTに印</b>。"],
            ["理由・詳細", "Why does the author say …? / According to …, what …", "該当段落を特定して根拠を1文で押さえる。"],
            ["主旨", "What is the <span class='en'>overall content</span> / best title?", "言い過ぎ・本文にない要素を切り、筆者の主張に沿う1つ。"],
        ],
        [None, None, None]),

    C.miniband("0-2 手順 ― 設問英文を先に読む"),
    C.box("Ⅲの標準手順（毎回この順）", C.steps([
        "設問英文を<b>先に</b>ざっと読み、各設問を『指示語／言い換え／真偽／理由／主旨』に<b>タグ付け</b>する。",
        "各設問の<b>疑問詞とキーワード</b>に下線（who/what/why/when と固有名詞）。何を探すかを確定。",
        "本文を頭から読み、設問のキーワードに当たったら<b>その場で該当設問を処理</b>する。",
        "真偽・主旨は本文読了後にまとめて。<b>NOT / 2つ選ぶ</b>の指示を最後にもう一度確認。",
    ])),
    C.win("設問先読みが効く理由",
        C.p("英語設問は本文の<b>キーワードを先に提示</b>してくれる。先に読んでおけば、"
            "本文のどこを精読すべきかが分かり、拾い読みで足りる箇所と区別できる。"
            "9マークを15分で取り切るには、この『地図を先に見る』動きが要になる。")),

    C.miniband("0-3 指示語・言い換えタイプの解法"),
    C.box("指示語（refer to）", C.dots([
        "代名詞（<span class='en'>it / this / they / such</span>）は<b>直前の文</b>に答えがある。",
        "候補の名詞を空所に<b>代入</b>して、意味が自然に通るものを選ぶ。",
        "<span class='en'>this / that ＋ 抽象名詞</span>は前文全体の内容を指すこともある。",
    ])),
    C.box("言い換え（closest in meaning）", C.dots([
        "まず自分の語彙知識で同義語を想起（付録の定型フレーズ・第2部の同義語テーブル）。",
        "多義語・句動詞は文脈で語義を確定してから選ぶ。",
        "下線部を選択肢で置換して、文が成立するか確認する。",
    ])),

    C.miniband("0-4 真偽・主旨タイプの解法"),
    C.box("真偽（true / NOT true）", C.dots([
        "設問の <span class='en'>NOT</span> に必ず印。<b>NOT true＝本文と矛盾する1つ</b>を選ぶ。",
        "各選択肢のキーワードを本文で照合。書いていない≠矛盾に注意。",
        "3つが本文で確認できれば残りが答え。消去法を明示的に。",
    ])),
    C.box("主旨（overall content / best title）", C.dots([
        "<b>言い過ぎ（too broad / too narrow）</b>と<b>本文にない要素</b>を切る。",
        "筆者の主張（多くは結論段の留保・両論併記）に沿う1つを残す。",
        "一部の段落だけを述べた選択肢（too narrow）は主旨にならない。",
    ])),
    C.callout("この章の結論",
        C.p("Ⅲは『設問英文を先に読み、探すものを決めてから本文へ』。"
            "英語で問われる負荷は、設問を<b>疑問詞とキーワードで分類</b>すれば道しるべに変わる。"
            "次ページからは実戦だ。設問→本文→照合、の順で手を動かせ。")),
])

import importlib, os
PROBLEMS = []
_here = os.path.dirname(__file__)
for _n in range(1, 12):
    _path = os.path.join(_here, "d3_sets", f"reading_{_n:02d}.py")
    if os.path.exists(_path):
        _m = importlib.import_module(f"d3_sets.reading_{_n:02d}")
        PROBLEMS.append(_m.SET)

try:
    from d3_appendix import APPENDIX
except Exception:
    APPENDIX = ""


def build():
    css = C.build_css(RUNNING) + R.READING_EXTRA_CSS
    body = []
    body.append(C.cover("第 3 部 - Ⅲ / 大問Ⅲ", "英問英答 長文読解 攻略ドリル", RUNNING, badge="英問英答"))
    body.append(FRONT)
    body.append(STRATEGY)
    body.append(C.chapter("PROBLEMS / 問題編",
        "成蹊型 英問英答長文 ― オリジナル演習 READING 01〜11",
        "設問はすべて英語だ。まず設問英文を先読みして『指示語／言い換え／真偽／理由／主旨』にタグを振り、"
        "探す情報を決めてから本文を読め。目標は1本15分・6/9マーク以上。解答解説は後半にまとめてある。"))
    kind = "Read the passage and answer the questions. 各設問文は英語である。指示に従い最も適切なものを1つ選べ（指定がある場合は2つ選べ）。"
    for i, s in enumerate(PROBLEMS, 1):
        body.append(R.render_problem_block(s, i, kind))
    body.append(C.chapter("ANSWERS / 解答解説編",
        "全設問 × 11長文 ― 英語設問の読み解きと根拠",
        "英語の設問文を和訳し直し、何を問われているかを明示してから根拠を示す。設問を『道しるべ』として"
        "使う感覚を、解説を通して体に入れろ。全訳と語彙で本文・設問双方の穴を埋める。"))
    for i, s in enumerate(PROBLEMS, 1):
        body.append(R.render_answer_block(s, i))
    body.append(APPENDIX)
    html = C.document(css, body)
    C.write_pdf(html, OUT)
    print("built:", OUT, "sets:", len(PROBLEMS))


if __name__ == "__main__":
    build()
