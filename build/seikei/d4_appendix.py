# -*- coding: utf-8 -*-
"""大問Ⅳ 付録：論理マーカー一覧 ＆ 文選択空所チェックリスト。"""
import seikei_common as C
from seikei_common import esc


def _mk(title, rows):
    trs = "".join(f'<tr><td class="w">{esc(e)}</td><td>{esc(j)}</td></tr>' for e, j in rows)
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:60mm">マーカー</th>'
            f'<th>論理の向き・空所への効き方</th></tr></thead><tbody>{trs}</tbody></table>')


APPENDIX = "".join([
    C.chapter("APPENDIX / 付録",
        "論理マーカー一覧 ＆ 文選択空所チェックリスト",
        "空所補充は『論理の矢印』が見えれば一意に決まる。ここでは空所の前後で答えを縛る"
        "接続表現（論理マーカー）を機能別に一覧化した。見た瞬間に矢印の向きが浮かぶまで回せ。"),

    C.miniband("A. 論理マーカー一覧 ― 空所を縛る接続表現"),
    _mk("① 逆接・対比（前と反対が入る）", [
        ("but / however / yet / still", "直前と<b>逆</b>の内容・語。"),
        ("although / though / even though", "譲歩。主節に<b>逆</b>の結論。"),
        ("on the other hand / in contrast", "<b>対比</b>される反対側。"),
        ("nevertheless / nonetheless", "それでもなお、と<b>逆接</b>。"),
        ("while / whereas", "一方で、と<b>対比</b>。"),
        ("despite / in spite of", "〜にもかかわらず（<b>逆</b>）。"),
    ]),
    _mk("② 因果・帰結（前の結果／原因が入る）", [
        ("so / therefore / thus / hence", "前の<b>結果</b>。"),
        ("because / since / as", "前の<b>原因・理由</b>。"),
        ("as a result / consequently", "その<b>結果</b>。"),
        ("that is why …", "だから〜（<b>結果</b>）。"),
        ("due to / owing to / thanks to", "〜のため（<b>原因</b>）。"),
    ]),
    _mk("③ 例示・言い換え・追加（前と同方向）", [
        ("for example / for instance", "前の一般論の<b>具体例</b>。"),
        ("such as / like", "<b>例</b>の列挙。"),
        ("in other words / that is / namely", "前と<b>同義</b>の言い換え。"),
        ("moreover / furthermore / in addition", "前と<b>同方向</b>の追加。"),
        ("also / besides / what is more", "さらに（<b>追加</b>）。"),
        ("in short / to sum up", "前の<b>まとめ</b>。"),
    ]),
    _mk("④ 時間・条件・並列", [
        ("first / then / finally", "<b>順序</b>。整序の手がかり。"),
        ("once / as soon as", "〜するとすぐ（<b>時間</b>）。"),
        ("if / unless / as long as", "<b>条件</b>。"),
        ("meanwhile / at the same time", "その間・同時に。"),
    ]),

    C.miniband("B. 語彙空所（1語）チェックリスト"),
    C.checks([
        "空所前後の<b>コロケーション</b>（動詞＋名詞・形容詞＋名詞・前置詞句）を確認したか。",
        "直近の<b>論理マーカー</b>を見て、入る語の向き（順接／逆接）を決めたか。",
        "多義語・句動詞は<b>文脈で語義</b>を確定したか。",
        "各選択肢を代入し、最も自然に筋が通る1つを選んだか。",
    ]),

    C.miniband("C. 文選択空所（1文）チェックリスト"),
    C.checks([
        "空所は<b>要点・結論</b>か、<b>具体例・補足</b>か、役割を見極めたか。",
        "直前・直後の文と<b>論理（問題→解決／一般→具体／主張→根拠）</b>がつながる1文か。",
        "選択肢の中の<b>代名詞・指示語（they / this / such）</b>が前文と一致するか確認したか。",
        "選択肢を入れて前後を音読し、<b>話が途切れない</b>1文を選んだか。",
        "本文の主張と<b>逆・言い過ぎ</b>の選択肢を切ったか。",
    ]),
    C.warn("文選択で落ちる典型",
        C.p("『それ単体では正しい文』でも、<b>前後とつながらなければ不正解</b>。"
            "文選択空所は『内容の正しさ』ではなく『前後との論理整合』で選ぶ。"
            "直後の文が具体例なら、空所にはそれを束ねる一般化が入る――この対応を最優先で見る。")),

    C.callout("Ⅳ攻略の最終結論",
        C.p("Ⅳは4マークの<b>取り所</b>。空所を見たら、まず論理マーカーに印をつけ、矢印の向きを決める。"
            "語彙空所はコロケ＋向き、文選択空所は前後整合。この2手順で、短時間に3/4以上を確実にする。")),
    C.p('<span class="tiny">学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第3部-Ⅳ。'
        '本巻の英文・設問はすべて完全オリジナルであり、実際の入試問題の転載は含まない。'
        '配点・試験時間・合格最低点は大学公表資料および赤本で最終照合のこと。</span>'),
])
