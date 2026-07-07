# -*- coding: utf-8 -*-
"""大問Ⅲ 付録：英語設問 定型フレーズ50 ＆ 主旨問題チェックリスト。"""
import seikei_common as C
from seikei_common import esc


def _phr(title, rows):
    trs = "".join(f'<tr><td class="w">{esc(e)}</td><td>{esc(j)}</td></tr>' for e, j in rows)
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:58mm">英語の設問フレーズ</th>'
            f'<th>意味・何を問うか</th></tr></thead><tbody>{trs}</tbody></table>')


APPENDIX = "".join([
    C.chapter("APPENDIX / 付録",
        "英語設問 定型フレーズ50 ＆ 主旨チェックリスト",
        "英問英答の負荷の正体は『設問英文を読む速度』だ。設問は定型表現の組み合わせでできている。"
        "以下の50フレーズを見た瞬間に『何を問われているか』が分かれば、Ⅲは一気に軽くなる。"),

    C.miniband("A. 英語設問 定型フレーズ50 ― タイプ別"),
    C.p("設問英文は『疑問詞＋定型』でできている。左を見た瞬間に右（問われる情報）が浮かぶまで回せ。"),

    _phr("① 指示語・語句を問う（10）", [
        ("What does “it / this / they” refer to?", "下線の代名詞が指すもの"),
        ("The word “X” refers to …", "X が指す語句"),
        ("What does “this (shift/idea)” mean here?", "this＋名詞が指す前文の内容"),
        ("To what does the underlined part refer?", "下線部の指示対象"),
        ("Which of the following does “such” include?", "such が含む範囲"),
        ("The underlined “one” stands for …", "one が受ける名詞"),
        ("In line X, “them” most likely means …", "them の指示対象"),
        ("What is “the former / the latter”?", "前者・後者の特定"),
        ("The pronoun in paragraph X points to …", "代名詞の指示先"),
        ("What does the author mean by “X”?", "下線表現の含意"),
    ]),
    _phr("② 言い換え・語義を問う（10）", [
        ("The word “X” is closest in meaning to", "X の同義語"),
        ("Which word is closest to “X”?", "X に最も近い語"),
        ("“X” can best be replaced by", "X の置き換え語"),
        ("What does “X” mean in this context?", "文脈上の語義"),
        ("The underlined phrase is similar to", "下線句の同義表現"),
        ("Which best paraphrases the underlined sentence?", "下線文の言い換え"),
        ("“X” here is used to mean", "多義語の文脈語義"),
        ("The expression “X” suggests that …", "表現が示す含意"),
        ("What is the meaning of “X” as used here?", "使われ方に即した意味"),
        ("Choose the synonym of “X”.", "X の同義語選択"),
    ]),
    _phr("③ 内容真偽・一致を問う（12）", [
        ("Which of the following is true?", "本文に合致する1つ"),
        ("Which is NOT true according to the passage?", "本文と矛盾する1つ（NOTに注意）"),
        ("Which is NOT mentioned in the passage?", "本文で触れられていない1つ"),
        ("According to the passage, which is correct?", "本文に照らして正しいもの"),
        ("All of the following are true EXCEPT …", "1つだけ誤り（EXCEPTに注意）"),
        ("Which statement does the author agree with?", "筆者が同意する記述"),
        ("Which is consistent with paragraph X?", "第X段と整合する記述"),
        ("What is stated about X?", "X について本文が述べる内容"),
        ("Choose TWO that are true.", "正しいものを2つ（個数指定）"),
        ("Which best matches the passage?", "本文に最も合う記述"),
        ("According to the author, X is …", "筆者による X の説明"),
        ("Which of these did the writer NOT say?", "筆者が述べていない1つ"),
    ]),
    _phr("④ 理由・詳細を問う（10）", [
        ("Why does the author say “X”?", "その発言の理由"),
        ("Why do critics worry about X?", "批判の論拠"),
        ("What is the reason for X?", "X の理由"),
        ("According to paragraph X, what …?", "第X段の具体情報"),
        ("What advantage / drawback does X have?", "X の利点・短所"),
        ("How does X affect Y?", "X が Y に与える影響"),
        ("What example does the author give?", "筆者が挙げる例"),
        ("What happens when X?", "X のときに起きること"),
        ("What is the purpose of X?", "X の目的"),
        ("What does X allow companies to do?", "X が可能にすること"),
    ]),
    _phr("⑤ 主旨・タイトル・筆者を問う（8）", [
        ("What is the overall content of the passage?", "本文全体の主旨"),
        ("What is the main idea?", "中心的な考え"),
        ("Which is the best title for the passage?", "最も適切なタイトル"),
        ("What is the author’s attitude toward X?", "X への筆者の態度"),
        ("What is the author’s view / opinion?", "筆者の見解"),
        ("What is the passage mainly about?", "本文の主題"),
        ("What conclusion does the author reach?", "筆者の結論"),
        ("What is the tone of the passage?", "文章のトーン"),
    ]),

    C.miniband("B. 主旨（overall content）問題 チェックリスト"),
    C.p("主旨問題は英問英答の山場。次の切り方で誤答を機械的に落とす。"),
    C.checks([
        "<b>too broad</b>（言い過ぎ・一般化しすぎ）を切る。『必ず』『すべて』『唯一』に注意。",
        "<b>too narrow</b>（一部の段落だけ）を切る。主旨は全体を覆う1つ。",
        "<b>本文にない要素</b>を含む選択肢を切る。もっともらしい一般論に飛びつかない。",
        "筆者の<b>結論段の留保・両論併記</b>に沿う1つを残す。",
        "タイトル問題も同じ。本文全体を最もよく表す1つを選ぶ。",
    ]),

    C.miniband("C. 本番 直前チェックリスト（大問Ⅲ）"),
    C.checks([
        "設問英文を先に読み、疑問詞とキーワードで分類したか。",
        "各設問の探す情報（who/what/why/指示語）を決めてから本文に入ったか。",
        "<span class='en'>NOT / EXCEPT / TWO</span> の指示に印をつけたか。",
        "指示語は直前の文へ、言い換えは代入確認をしたか。",
        "真偽は選択肢のキーワードを本文照合し、消去法を使ったか。",
        "主旨は言い過ぎ・部分的・本文外を切り、留保に沿う1つを残したか。",
    ]),

    C.callout("Ⅲ攻略の最終結論",
        C.p("英語で問われる負荷は、設問を<b>定型フレーズとして即読み</b>できれば消える。"
            "『設問先読み→探す情報を決定→本文照合』の順を崩さなければ、9マークは安定して6以上取れる。"
            "Ⅲを『捨てる大問』にせず、この付録のフレーズを回し切って道しるべに変えろ。")),
    C.p('<span class="tiny">学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第3部-Ⅲ。'
        '本巻の長文・設問はすべて完全オリジナルであり、実際の入試問題の転載は含まない。'
        '配点・試験時間・合格最低点は大学公表資料および赤本で最終照合のこと。</span>'),
])
