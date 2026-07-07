# -*- coding: utf-8 -*-
"""大問Ⅴ 付録：語法・イディオム最終チェック ＆ 紛らわしいペア一覧。"""
import seikei_common as C
from seikei_common import esc


def _pair(title, rows):
    trs = "".join(f'<tr><td class="w">{esc(a)}</td><td class="w">{esc(b)}</td><td>{esc(note)}</td></tr>'
                  for a, b, note in rows)
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:30mm">A</th><th style="width:30mm">B</th>'
            f'<th>区別のポイント</th></tr></thead><tbody>{trs}</tbody></table>')


def _idiom(title, rows):
    trs = "".join(f'<tr><td class="w">{esc(e)}</td><td>{esc(j)}</td></tr>' for e, j in rows)
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:48mm">表現</th>'
            f'<th>意味</th></tr></thead><tbody>{trs}</tbody></table>')


APPENDIX = "".join([
    C.chapter("APPENDIX / 付録",
        "語法・イディオム最終チェック ＆ 紛らわしいペア一覧",
        "Ⅴで狙われるのは『知っていれば一撃、知らなければ手が出ない』ピンポイント。"
        "ここでは頻出の紛らわしいペアと必修イディオムを一覧化した。直前に高速で回し、"
        "空所を見た瞬間に分野と正解が浮かぶ状態を作れ。"),

    C.miniband("A. 紛らわしい動詞・語法ペア"),
    _pair("① 自動詞 / 他動詞（活用も要暗記）", [
        ("lie（横たわる）", "lay（横たえる）", "自 lie-lay-lain-lying／他 lay-laid-laid-laying。目的語の有無で判別。"),
        ("rise（上がる）", "raise（上げる）", "自 rise-rose-risen／他 raise-raised-raised。"),
        ("sit（座る）", "seat（座らせる）", "他 seat は <span class='en'>be seated</span> の形が多い。"),
        ("fall（落ちる）", "fell（倒す）", "他 fell（木を切り倒す）は規則変化。"),
        ("arise（生じる）", "arouse（呼び起こす）", "arise は自動詞、arouse は他動詞。"),
    ]),
    _pair("② 意味が紛らわしい動詞", [
        ("borrow（借りる）", "lend（貸す）", "方向が逆。borrow from / lend to。"),
        ("remind（思い出させる）", "remember（思い出す）", "remind 人 of 物。"),
        ("suit（似合う・都合が合う）", "fit（サイズが合う）", "suit は色・都合、fit はサイズ。"),
        ("affect（影響する・動詞）", "effect（影響・名詞）", "affect は動詞、effect は名詞が基本。"),
        ("adopt（採用する）", "adapt（適応させる）", "adopt a plan／adapt to change。"),
    ]),
    _pair("③ 紛らわしい形容詞・副詞", [
        ("hard（熱心に）", "hardly（ほとんど〜ない）", "hardly は準否定。"),
        ("late（遅く）", "lately（最近）", "lately＝recently。"),
        ("high（高く）", "highly（大いに）", "highly＝very much。"),
        ("near（近くに）", "nearly（ほとんど）", "nearly＝almost。"),
        ("most（最も）", "almost（ほとんど）", "almost は副詞で動詞・形容詞を修飾。"),
    ]),

    C.miniband("B. 必修イディオム・句動詞（Ⅴ頻出）"),
    _idiom("① at / in / on を含む句", [
        ("at ease", "くつろいで、安心して"),
        ("at stake", "危機に瀕して"),
        ("at odds with", "〜と食い違って"),
        ("in charge of", "〜を担当して"),
        ("in terms of", "〜の点で"),
        ("in the long run", "長い目で見れば"),
        ("on behalf of", "〜を代表して"),
        ("on the verge of", "〜の寸前で"),
    ]),
    _idiom("② 動詞を含む句動詞", [
        ("account for", "〜を説明する／占める"),
        ("carry out", "実行する"),
        ("come up with", "思いつく"),
        ("cope with", "うまく対処する"),
        ("get rid of", "取り除く"),
        ("look into", "調査する"),
        ("make up for", "埋め合わせる"),
        ("put up with", "我慢する"),
        ("run out of", "使い果たす"),
        ("take advantage of", "利用する"),
    ]),
    _idiom("③ 準動詞・仮定を含む定型", [
        ("cannot help -ing", "〜せずにはいられない"),
        ("be used to -ing", "〜に慣れている"),
        ("would rather A than B", "BよりむしろAしたい"),
        ("It is time S 過去形", "もう〜する時間だ（仮定法）"),
        ("If it were not for …", "〜がなければ（現在）"),
        ("If it had not been for …", "〜がなかったら（過去）"),
        ("no sooner … than", "〜するやいなや"),
        ("so as to / in order to", "〜するために"),
    ]),

    C.miniband("C. 一撃判定 最終チェックリスト（大問Ⅴ）"),
    C.checks([
        "空所を見て、まず<b>狙われた分野</b>（時制／仮定法／準動詞／語法／イディオム／比較）を判定したか。",
        "<span class='en'>if / were / had+過去分詞</span> を見たら<b>仮定法</b>を疑い、帰結節の助動詞を合わせたか。",
        "<span class='en'>to / 前置詞</span> の後は<b>準動詞</b>（原形／動名詞）を判定したか。",
        "紛らわしい動詞ペア（<span class='en'>lie/lay, rise/raise</span>）は<b>目的語の有無と活用</b>で切ったか。",
        "空所後の前置詞・副詞から<b>イディオム・句動詞</b>をコロケで確定したか。",
        "短文なので<b>全訳せず</b>、形で切って意味は最後に確認したか。",
    ]),
    C.callout("Ⅴ攻略の最終結論",
        C.p("Ⅴは<b>知識で満点近くを狙う最優先の得点源</b>。分野を見抜き、形で一撃。"
            "この付録のペアとイディオムを直前に高速で回せば、6マークは5以上で安定する。"
            "前半（Ⅴ・Ⅳ・Ⅰ）で得点とリズムを作り、長文（Ⅱ・Ⅲ）に時間を残せ。")),
    C.p('<span class="tiny">学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第3部-Ⅴ。'
        '本巻の英文・設問はすべて完全オリジナルであり、実際の入試問題の転載は含まない。'
        '配点・試験時間・合格最低点は大学公表資料および赤本で最終照合のこと。</span>'),
])
