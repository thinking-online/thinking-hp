# -*- coding: utf-8 -*-
"""大問Ⅰ 付録：会話定型表現100 ／ 品詞仕分け・直前チェックリスト。"""
import seikei_common as C
from seikei_common import esc


def _phrase_table(title, rows):
    trs = "".join(
        f'<tr><td class="w">{esc(e)}</td><td>{esc(j)}</td></tr>' for e, j in rows
    )
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:52mm">表現</th>'
            f'<th>会話での使いどころ・訳</th></tr></thead><tbody>{trs}</tbody></table>')


APPENDIX = "".join([
    C.chapter("APPENDIX / 付録",
        "会話定型表現100 ＆ 仕分けチェックリスト",
        "大問Ⅰの語群に繰り返し現れる「会話の潤滑油」を機能別に100個。選択肢を見た瞬間に"
        "『これは同意の相づち』『これは断りの前置き』と品詞・機能でタグ付けできるよう、繰り返し目を通せ。"),

    C.miniband("A. 会話定型表現100 ― 機能別"),
    C.p("以下は成蹊型の会話文で狙われやすい機能表現。左の英語を隠して意味を言えるか、"
        "意味から英語を復元できるか、両方向で回せ。"),

    _phrase_table("① 同意・共感・相づち（10）", [
        ("I know, right?", "だよね／わかる（強い共感）"),
        ("Exactly.", "まさに／その通り"),
        ("Tell me about it.", "ほんとにね（同感の皮肉混じり）"),
        ("That makes sense.", "なるほど、筋が通る"),
        ("No wonder.", "どうりで／道理で"),
        ("Fair enough.", "まあ、それもそうだね／納得"),
        ("I couldn't agree more.", "大賛成だ"),
        ("Good point.", "いい指摘だね"),
        ("Same here.", "こっちも同じ"),
        ("That's true.", "確かに"),
    ]),
    _phrase_table("② 依頼・許可・応答（10）", [
        ("Would you mind -ing?", "〜してもらえますか（丁寧な依頼）"),
        ("Do you mind if I …?", "〜してもいいですか"),
        ("Go ahead.", "どうぞ（許可）"),
        ("Feel free to …", "遠慮なく〜して"),
        ("Be my guest.", "どうぞご自由に"),
        ("Sure, no problem.", "もちろん、問題ないよ"),
        ("I'd appreciate it if …", "〜してもらえると助かる"),
        ("Could you do me a favor?", "お願いがあるんだけど"),
        ("I'd rather you didn't.", "できればやめてほしい"),
        ("By all means.", "ぜひどうぞ"),
    ]),
    _phrase_table("③ 緩衝・遠回し・本音の前置き（10）", [
        ("To be honest, …", "正直に言うと"),
        ("I'm afraid …", "残念ながら／申し訳ないが"),
        ("Sort of. / Kind of.", "まあね／どちらかというと"),
        ("Not really.", "そうでもない"),
        ("If you ask me, …", "私に言わせれば"),
        ("I hate to say it, but …", "言いにくいんだけど"),
        ("No offense, but …", "悪く取らないでほしいけど"),
        ("The thing is, …", "実はね／問題は"),
        ("It's just that …", "ただね、〜なんだ"),
        ("I guess so.", "たぶんそうだね（消極的同意）"),
    ]),
    _phrase_table("④ 提案・勧誘・助言（10）", [
        ("Why don't we …?", "〜しない？（提案）"),
        ("How about -ing?", "〜するのはどう？"),
        ("We might as well …", "どうせなら〜した方がいい"),
        ("You'd better …", "〜した方がいい（強め）"),
        ("If I were you, I'd …", "私なら〜する"),
        ("It wouldn't hurt to …", "〜して損はない"),
        ("Let's just …", "とりあえず〜しよう"),
        ("You could always …", "いざとなれば〜もできる"),
        ("Shall we …?", "〜しましょうか"),
        ("What if we …?", "〜してみたらどう？"),
    ]),
    _phrase_table("⑤ つなぎ・話題転換（10）", [
        ("By the way, …", "ところで"),
        ("Anyway, …", "とにかく／それはそうと"),
        ("Speaking of which, …", "その話で言えば"),
        ("That reminds me, …", "それで思い出した"),
        ("On second thought, …", "考え直したんだけど"),
        ("Come to think of it, …", "そういえば"),
        ("As I was saying, …", "さっきの続きだけど"),
        ("Long story short, …", "手短に言うと"),
        ("Either way, …", "どちらにしても"),
        ("For what it's worth, …", "参考までに言うと"),
    ]),
    _phrase_table("⑥ 驚き・反応・感情（10）", [
        ("You're kidding!", "冗談でしょ！"),
        ("No way!", "まさか／ありえない"),
        ("That's a relief.", "よかった、ほっとした"),
        ("What a pain.", "面倒だな"),
        ("It's about time.", "やっとか／遅すぎるくらいだ"),
        ("That's the last thing I need.", "それだけは勘弁"),
        ("I can't believe it.", "信じられない"),
        ("Lucky you.", "いいなあ／うらやましい"),
        ("That's too bad.", "それは残念"),
        ("Better late than never.", "遅くてもやらないよりまし"),
    ]),
    _phrase_table("⑦ ビジネス・キャンパス頻出（20）", [
        ("run behind schedule", "予定より遅れている"),
        ("catch up on", "（遅れ）を取り戻す／情報を仕入れる"),
        ("touch base with", "〜と連絡を取り合う"),
        ("follow up on", "〜の後追いをする"),
        ("get back to you", "後で返事する"),
        ("fill in for", "〜の代わりを務める"),
        ("call it a day", "今日はここまでにする"),
        ("come up with", "（案などを）思いつく"),
        ("work out", "うまくいく／解決する"),
        ("turn out", "結局〜となる／判明する"),
        ("sign up for", "〜に申し込む／登録する"),
        ("drop by / drop in", "立ち寄る"),
        ("run into", "偶然出会う／（問題に）ぶつかる"),
        ("look into", "〜を調べる"),
        ("pull off", "（難事を）やってのける"),
        ("put off", "延期する"),
        ("bring up", "（話題を）持ち出す"),
        ("stick to", "〜を守り続ける／固執する"),
        ("keep up with", "〜に遅れずついていく"),
        ("wrap up", "（会議・仕事を）まとめて終える"),
    ]),
    _phrase_table("⑧ 断り・保留・条件（10）", [
        ("I'll pass this time.", "今回は遠慮しておく"),
        ("Maybe some other time.", "また別の機会に"),
        ("Let me think about it.", "考えさせて"),
        ("I'm tied up right now.", "今は手が離せない"),
        ("It depends.", "場合による"),
        ("I'll see what I can do.", "できるだけやってみる"),
        ("No promises, though.", "約束はできないけど"),
        ("Count me in.", "参加する／乗った"),
        ("Count me out.", "私は抜けるよ"),
        ("It's up to you.", "君に任せる"),
    ]),

    C.miniband("B. 品詞仕分け 早見チェックリスト"),
    C.p("選択肢を見た瞬間、次の順で機械的に仕分ける。"),
    C.checks([
        "冠詞・所有格・形容詞の直後の空所 → <b>名詞</b>を探す。",
        "他動詞・前置詞の直後 → <b>名詞／動名詞</b>。",
        "to の直後 → <b>動詞原形</b>。be動詞の直後 → <b>形容詞／-ing／-ed</b>。",
        "主語と目的語に挟まれた空所 → <b>動詞</b>。時制・数の一致も確認。",
        "文頭・応答の単独空所 → <b>会話定型表現（機能語）</b>を疑う。",
        "句動詞は<b>自動詞型か他動詞型か</b>（後ろに目的語があるか）で絞る。",
    ]),

    C.miniband("C. 本番 直前チェックリスト（大問Ⅰ）"),
    C.checks([
        "解く前に語群へ品詞タグを振ったか。",
        "確信空所から先に埋め、語群から線で消したか。",
        "各Setの「使わない2語」を最後に特定したか。",
        "1つの語を2か所に使っていないか（重複チェック）。",
        "会話の話者交代・因果・逆接の流れと矛盾していないか。",
        "マーク欄と解答番号（1〜13）がずれていないか。",
    ]),
    C.callout("最後に一言",
        C.p("大問Ⅰで作った得点とリズムが、長文（Ⅱ・Ⅲ）の集中力を決める。"
            "ここは<b>知識で秒殺する枠</b>だ。迷ったら飛ばし、確信から埋め、最後に2語で挟み撃つ。"
            "――それだけを、当日は淡々とやればいい。")),
    C.p('<span class="tiny">学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第3部-Ⅰ。'
        '本巻の演習はすべて完全オリジナルであり、実際の入試問題の転載は含まない。'
        '配点・試験時間・合格最低点は大学公表資料および赤本で最終照合のこと。</span>'),
])
