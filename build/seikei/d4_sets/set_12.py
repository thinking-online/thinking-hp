# -*- coding: utf-8 -*-
"""大問Ⅳ SET 12 ― 短文2本・空所6（語彙4＋文選択2）。
文1=宇宙ビジネス（民間ロケット）、文2=チョコレートとカカオ交易。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "宇宙ビジネス（民間ロケット） ＆ チョコレートとカカオ交易",
  "genre": "ビジネス・技術／文化・歴史 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Rockets for Hire", "wordcount": 96,
     "paras": [
        "For decades, sending anything into orbit was the exclusive business of national governments with enormous budgets. "
        "Today, private companies have [[b:41]] that monopoly by building rockets whose boosters can be flown again and again. "
        "Because a single launch once cost a fortune, reusing the same hardware has dramatically [[b:42]] the price of reaching space. "
        "[[b:43]] Small firms can now buy a ride for a tiny satellite, and start-ups that once seemed impossible are suddenly winning serious contracts. "
        "What used to belong to a handful of superpowers has quietly become a crowded and fiercely competitive market.",
     ]},
    {"label": "文2", "title": "From Bitter Cup to Sweet Bar", "wordcount": 99,
     "paras": [
        "Long before it filled shop windows as sweet bars, chocolate was a bitter, spiced drink prized by the peoples of ancient Mesoamerica. "
        "Cacao beans were so precious that they [[b:44]] as money, and could be exchanged for cloth, food, and even labour. "
        "When Spanish traders carried the beans back across the ocean to Europe, cooks there added sugar and warm milk, "
        "and the once-bitter drink was gradually [[b:45]] to suit European tastes. "
        "[[b:46]] Plantations spread across the tropics, and a treat once reserved for kings and priests slowly turned into an everyday pleasure sold on almost every street corner.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["broken","protected","joined","ignored"],"answer":"ア",
     "basis":"直前 <span class='en'>private companies have ( ) that monopoly by building reusable rockets</span>。"
             "政府の独占を『どうした』のか。続く文が価格の急落と新規参入の増加を説明する。",
     "solve":"<span class='en'>break a monopoly</span>（独占を打ち破る）のコロケ。後続の『価格が下がり小企業も参入』＝独占の崩壊なので<span class='en'>broken</span>。",
     "cut":"<span class='en'>protected</span>（守る）や <span class='en'>joined</span>（加わる）は、市場が競争的になった流れと逆。<span class='en'>ignored</span> は意味を成さない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["lowered","raised","fixed","matched"],"answer":"ア",
     "basis":"<span class='en'>reusing the same hardware has dramatically ( ) the price of reaching space</span>。機体の再利用が価格に与えた効果。",
     "solve":"『一度は莫大な費用』→再利用で <span class='en'>dramatically ( ) the price</span>。コストを劇的に<b>下げた</b>＝<span class='en'>lowered</span>。",
     "cut":"<span class='en'>raised</span>（上げる）は逆。<span class='en'>fixed / matched</span> は『価格を劇的に』という副詞と噛み合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "As a result, access to space is no longer limited to the wealthiest nations.",
       "Even so, only governments can still afford to launch anything at all.",
       "The technology, however, has never actually left the drawing board.",
       "Reusable rockets soon turned out to be far too dangerous to fly."],"answer":"ア",
     "basis":"空所前＝再利用で宇宙到達コストが急落。空所後＝<span class='en'>Small firms can now buy a ride ... start-ups ... are winning contracts</span>（小企業や新興企業の具体例）。",
     "solve":"空所は<b>結果の一般化→具体例</b>の橋渡し。コスト低下の帰結『宇宙へのアクセスがもはや最富裕国だけのものではない』が直後の具体例を束ねる。",
     "cut":"『政府しか打ち上げられない』『技術は机上の空論』『再利用ロケットは危険すぎた』は、民間が成功しているという本文と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["served","refused","disappeared","complained"],"answer":"ア",
     "basis":"<span class='en'>Cacao beans were so precious that they ( ) as money</span>。貴重ゆえに『貨幣として』。",
     "solve":"<span class='en'>serve as money</span>（〜の役目を果たす）のコロケ。『布や食料や労働と交換できた』という説明とも整合。",
     "cut":"<span class='en'>refused / disappeared / complained</span> はいずれも主語（豆）と噛み合わず、<span class='en'>as money</span> と結びつかない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["adapted","banned","returned","forgotten"],"answer":"ア",
     "basis":"<span class='en'>the once-bitter drink was gradually ( ) to suit European tastes</span>。砂糖と牛乳を加えた結果。",
     "solve":"<span class='en'>adapt ... to suit</span>（〜に合うよう作り替える）。『ヨーロッパの好みに合わせて』変化した、＝<span class='en'>adapted</span>。",
     "cut":"<span class='en'>banned</span>（禁止）や <span class='en'>returned / forgotten</span> は『好みに合わせた』という順接と逆で、後続の普及の流れとも合わない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Demand grew so quickly that it reshaped farming on the other side of the world.",
       "Yet Europeans never really developed any taste for the drink.",
       "The recipe remained a closely guarded secret for many centuries.",
       "Cacao proved impossible to grow anywhere outside Mesoamerica."],"answer":"ア",
     "basis":"空所前＝ヨーロッパ好みに作り替えられ人気に。空所後＝<span class='en'>Plantations spread across the tropics ... an everyday pleasure</span>（熱帯での農園拡大と大衆化）。",
     "solve":"空所は<b>需要の増大→その帰結</b>の橋渡し。『需要が急伸し世界の反対側の農業を作り替えた』が直後のプランテーション拡大を自然に導く。",
     "cut":"『決して好まれなかった』『秘密のまま』『メソアメリカ以外で栽培不可』は、農園の拡大と大衆化という直後の記述と矛盾。"},
  ],
  "trans": [
    ("文1", "何十年もの間、軌道に何かを送ることは巨額の予算を持つ国家政府だけの独占的な事業だった。今日、民間企業はブースターを"
            "何度も再使用できるロケットを造ることで、その独占を<b>打ち破った</b>。かつて一度の打ち上げが莫大な費用を要したため、"
            "同じ機体を再利用することは宇宙到達の価格を劇的に<b>引き下げた</b>。<b>その結果、宇宙へのアクセスはもはや最も豊かな国だけのものではなくなった。</b>"
            "小さな企業も今や小型衛星の相乗りを買え、かつて不可能に見えた新興企業が突如として本格的な契約を勝ち取っている。"
            "かつて一握りの超大国のものだったものが、静かに混雑した激しい競争市場になったのだ。"),
    ("文2", "甘い板チョコとして店頭に並ぶずっと前、チョコレートは古代メソアメリカの人々に珍重された、苦く香辛料の効いた飲み物だった。"
            "カカオ豆はとても貴重で、貨幣として<b>役立ち</b>、布や食料、さらには労働とも交換できた。スペインの商人が豆を海の向こうの"
            "ヨーロッパへ運ぶと、そこの料理人が砂糖と温めた牛乳を加え、かつて苦かった飲み物は次第にヨーロッパの好みに合うよう<b>作り替えられた</b>。"
            "<b>需要はあまりに急速に伸び、世界の反対側の農業までも作り替えた。</b>プランテーションが熱帯地方に広がり、かつて王や司祭のために"
            "取っておかれた贅沢品は、次第にほとんどどの街角でも売られる日常の楽しみへと変わっていった。"),
  ],
  "vocab": [
    ("monopoly", "名", "独占"),
    ("booster", "名", "（ロケットの）補助推進機、ブースター"),
    ("contract", "名", "契約"),
    ("prize", "動", "高く評価する、珍重する"),
    ("exchange", "動", "交換する"),
    ("adapt", "動", "適応させる、作り替える"),
    ("plantation", "名", "大農園、プランテーション"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋論理の向き</b>で決める――"
    "<span class='en'>break a monopoly</span>・<span class='en'>serve as money</span> のような結び付きと、"
    "『高い→下げた』『苦い→好みに合わせた』の因果を確認する。文選択空所（43・46）は<b>結果の一般化→具体例</b>の橋渡し。"
    "代入して前後を音読し、話が途切れない1文を選ぶ。",
}
