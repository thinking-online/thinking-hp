# -*- coding: utf-8 -*-
"""大問Ⅱ 付録：下線部言い換え 頻出同義語テーブル ＆ 真偽/整序/語法チェックリスト。"""
import seikei_common as C
from seikei_common import esc


def _syn(title, rows):
    trs = "".join(
        f'<tr><td class="w">{esc(w)}</td><td>{esc(mean)}</td><td class="p">{esc(syn)}</td></tr>'
        for w, mean, syn in rows)
    return (f'<div class="h3">{esc(title)}</div>'
            f'<table class="vocab"><thead><tr><th style="width:33mm">下線に出る語</th>'
            f'<th style="width:40mm">意味</th><th>言い換え（選択肢に出る同義語）</th></tr></thead>'
            f'<tbody>{trs}</tbody></table>')


APPENDIX = "".join([
    C.chapter("APPENDIX / 付録",
        "下線部言い換え 同義語テーブル ＆ 攻略チェックリスト",
        "大問Ⅱの最大の塊は下線部言い換え（タイプB）。ここは知識で秒殺する枠だ。"
        "頻出の『下線に出る語 ⇄ 選択肢に出る同義語』を機能別に集めた。左を隠して同義語を、"
        "右を隠して原義を――両方向で回し、語彙を『言い換え耐性』のある形で固めろ。"),

    C.miniband("A. 言い換え頻出 同義語テーブル（タイプB 直結）"),
    C.p("成蹊Ⅱの下線部言い換えは、<b>句動詞・多義語・抽象語</b>を文脈に応じた同義語に置換する力を問う。"
        "単語帳の第一義暗記だけでは足りない。以下のネットワークを丸ごと覚える。"),

    _syn("① 句動詞（最頻・最重要）", [
        ("come up with", "（案を）思いつく", "devise / conceive / think of"),
        ("bank on", "当てにする", "rely on / count on / depend on"),
        ("pile up", "積み上がる", "accumulate / build up / mount"),
        ("shell out", "（大金を）払う", "pay / spend / disburse"),
        ("spring up", "急に現れる", "emerge / arise / appear"),
        ("carry out", "実行する", "conduct / perform / execute"),
        ("do away with", "廃止する", "abolish / eliminate / get rid of"),
        ("take over", "引き継ぐ・乗っ取る", "assume / seize / take control of"),
        ("free up", "解放する・空ける", "release / liberate / make available"),
        ("keep pace with", "遅れずついていく", "keep up with / match / stay level with"),
        ("crowd out", "締め出す", "displace / push out / squeeze out"),
        ("rein in", "抑制する", "curb / restrain / check"),
        ("live up to", "（期待に）応える", "meet / fulfill / satisfy"),
        ("crop up", "ふいに生じる", "arise / occur / emerge"),
        ("shy away from", "尻込みする", "avoid / recoil from / hesitate over"),
    ]),
    _syn("② 動詞（多義・抽象）", [
        ("outweigh", "〜に勝る", "surpass / exceed / be greater than"),
        ("hinge on", "〜次第である", "depend on / rest on / turn on"),
        ("command", "（価格・敬意を）得る", "attract / earn / obtain"),
        ("yield", "生む・産出する", "produce / generate / bring about"),
        ("dismiss", "退ける・一蹴する", "reject / brush aside / disregard"),
        ("squander", "浪費する", "waste / fritter away / misspend"),
        ("soar", "急上昇する", "surge / rocket / climb sharply"),
        ("cement", "固める・強固にする", "strengthen / consolidate / reinforce"),
        ("blind (to)", "見えなくする", "prevent from seeing / obscure"),
        ("weigh up", "比較検討する", "assess / evaluate / consider"),
    ]),
    _syn("③ 形容詞・副詞", [
        ("predictable", "予測できる", "foreseeable / expected / reliable"),
        ("substantial", "かなりの", "considerable / significant / sizable"),
        ("tedious", "退屈な・単調な", "boring / monotonous / dull"),
        ("impressive", "見事な", "remarkable / striking / notable"),
        ("at odds with", "〜と食い違って", "in conflict with / inconsistent with"),
        ("at stake", "危機に瀕して", "at risk / in jeopardy / on the line"),
        ("massive", "巨大な", "huge / enormous / vast"),
        ("spectacular", "目覚ましい", "wonderful / stunning / dramatic"),
    ]),
    _syn("④ 名詞・抽象概念", [
        ("revenue", "収入・歳入", "income / earnings / proceeds"),
        ("inertia", "惰性", "sluggishness / passivity / momentum"),
        ("retention", "維持・保持", "keeping / holding on to"),
        ("bargain", "お買い得", "good deal / good value"),
        ("dilemma", "板挟み", "predicament / quandary"),
        ("incentive", "誘因・動機", "motivation / spur / inducement"),
        ("drawback", "難点・短所", "disadvantage / downside / shortcoming"),
        ("surge", "急増", "sharp rise / upswing / spike"),
    ]),

    C.callout("言い換えは『秒殺枠』― 迷ったら飛ばす",
        C.p("下線部言い換えは、知っていれば1問数秒。知らない語に出会っても推測に何十秒もかけるな。"
            "印をつけて飛ばし、本文読了後に文脈から当てにいく。"
            "『知っていれば即答、知らなければ後回し』の線引きが、Ⅱで長文を読む時間を生む。")),

    C.miniband("B. 内容真偽・一致（タイプC）切り方チェックリスト"),
    C.checks([
        "設問文の<b>『合致しない／NOT』に印</b>をつけたか（読み違い事故の最多発地帯）。",
        "各選択肢の<b>キーワード</b>を本文で照合したか（印象で選ばない）。",
        "『すべて／必ず／唯一』などの<b>言い過ぎ(too broad)</b>を疑ったか。",
        "『本文に書いていない＝不一致とは限らない』。本文と<b>矛盾する</b>記述を探したか。",
        "3つが本文で確認できたら残りが答え。<b>消去法</b>を明示的に使ったか。",
    ]),
    C.warn("Cで落ちる典型",
        C.p("①『合致しないもの』を合致するもので選ぶ　②本文にない魅力的な一般論に飛びつく　"
            "③一語の言い換え（例：<span class='en'>parts of ＝ 一部</span> を <span class='en'>all</span> と読む）を見落とす。"
            "どれも実力と無関係な取りこぼし。設問の否定語と数量詞に必ず印を。")),

    C.miniband("C. 情報整序（D）・語法融合（E）チェックリスト"),
    C.box("D 情報整序", C.dots([
        "順序を示す語（<span class='en'>until / during / once / shortly after / then</span>）に印。",
        "選択肢の<b>最初と最後を先に確定</b>して挟み撃ち。",
        "因果（<span class='en'>therefore / because / so</span>）の向きで前後関係を固定する。",
    ])),
    C.box("E 語法・語形", C.dots([
        "空所の<b>主語</b>を確認（動名詞・不定詞主語は<b>単数</b>扱い→三単現）。",
        "<span class='en'>Had S 過去分詞 …</span> の倒置は<b>仮定法過去完了</b>→帰結は <span class='en'>would have + 過去分詞</span>。",
        "<span class='en'>demand / suggest / insist that S (should) 原形</span> の仮定法現在。",
        "自動詞 <span class='en'>lie-lay-lain</span>／他動詞 <span class='en'>lay-laid-laid</span> の混同に注意。",
    ])),

    C.miniband("D. ビジネス/経済テーマ語彙 ミニ（背景スキーマ用）"),
    C.p("Ⅱの長文はビジネス/経済が核。背景知識があるほど読解は速い。頻出概念を最終確認せよ。"),
    C.table(
        ["概念", "英語", "意味"],
        [
            ["ネットワーク効果", "network effects", "利用者が増えるほど価値が高まる現象"],
            ["垂直統合", "vertical integration", "調達〜販売を自社で一体化する戦略"],
            ["先行者利益", "first-mover advantage", "最初に参入した者が得る優位"],
            ["規模の経済", "economies of scale", "生産量増で単価が下がること"],
            ["顧客維持", "customer retention", "既存客をつなぎ留めること"],
            ["破壊的技術", "disruptive technology", "既存市場を塗り替える新技術"],
            ["需要管理", "demand management", "需要の量やタイミングを調整すること"],
            ["ブランド価値", "brand equity", "ブランドが生む付加的価値"],
        ],
        [None, None, None]),

    C.callout("Ⅱ攻略の最終結論",
        C.p("Ⅱは『言い換えを語彙で秒殺→語法は主語と時制で判定→整序は因果で挟み撃ち→真偽は言い過ぎを切る』。"
            "処理を分ければ18マークは<b>稼ぎ頭</b>に変わる。この付録の同義語テーブルを回し切って、"
            "本番の下線部言い換えを『考える問題』から『思い出す作業』にせよ。")),
    C.p('<span class="tiny">学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第3部-Ⅱ。'
        '本巻の長文・設問はすべて完全オリジナルであり、実際の入試問題の転載は含まない。'
        '配点・試験時間・合格最低点は大学公表資料および赤本で最終照合のこと。</span>'),
])
