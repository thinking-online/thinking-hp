# -*- coding: utf-8 -*-
"""大問Ⅳ SET 13 ― 短文2本・空所6（語彙4＋文選択2）。
文1=ブランドと口コミ、文2=森林と炭素吸収。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "ブランドと口コミ ＆ 森林と炭素吸収",
  "genre": "ビジネス／科学・環境 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The Voice of the Crowd", "wordcount": 93,
     "paras": [
        "A company can spend a fortune on advertising, yet the message customers trust most rarely comes from the company itself. "
        "Instead, it comes from other buyers. When a friend praises a product or an online reviewer describes an honest experience, "
        "that recommendation carries [[b:41]] that no paid slogan can match. "
        "Because such opinions feel free of commercial motives, shoppers tend to [[b:42]] them far more than glossy commercials. "
        "[[b:43]] A single viral post can lift an unknown brand overnight, while a wave of angry reviews can sink a famous one just as fast.",
     ]},
    {"label": "文2", "title": "The Lungs of the Planet", "wordcount": 93,
     "paras": [
        "A forest is far more than a collection of trees; it is one of the planet's great engines for cleaning the air. "
        "As they grow, trees [[b:44]] carbon dioxide from the atmosphere and lock the carbon away in their trunks, roots, and the soil beneath them. "
        "In this way a healthy woodland can [[b:45]] the warming effect of gases released by cars and factories. "
        "[[b:46]] When forests are cut down or burned, that stored carbon escapes back into the sky, "
        "and a system that once cooled the climate suddenly begins to heat it.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["credibility","confusion","expense","silence"],"answer":"ア",
     "basis":"<span class='en'>that recommendation carries ( ) that no paid slogan can match</span>。他者の推薦が『帯びるもの』。",
     "solve":"<span class='en'>carry credibility</span>（信頼性を帯びる）。『商業的動機がないから信じられる』という後続と整合し、有料宣伝が及ばないのは<b>信頼性</b>。",
     "cut":"<span class='en'>confusion / expense / silence</span> は『どんな宣伝文句も及ばない』という称賛の文脈に合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["believe","doubt","avoid","forget"],"answer":"ア",
     "basis":"<span class='en'>shoppers tend to ( ) them far more than glossy commercials</span>。them＝商業的動機のない正直な意見。",
     "solve":"『動機がないと感じられる』→華やかなCMより<b>信じる</b>＝<span class='en'>believe</span>。<span class='en'>far more than</span> の比較とも整合。",
     "cut":"<span class='en'>doubt</span>（疑う）は逆向き。<span class='en'>avoid / forget</span> は『CMより〜する』という比較と噛み合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "In the age of social media, this everyday chatter has become a powerful marketing force.",
       "For this reason, traditional advertising has never been more effective than now.",
       "Yet personal opinions almost never influence what people actually buy.",
       "Companies have therefore stopped listening to their customers entirely."],"answer":"ア",
     "basis":"空所前＝買い物客は口コミを広告より信じる。空所後＝<span class='en'>A single viral post can lift ... a wave of angry reviews can sink ...</span>（投稿の影響力の具体例）。",
     "solve":"空所は<b>一般化→具体例</b>の橋渡し。『SNS時代に日常の口コミが強力なマーケティングの力になった』が直後の投稿の威力の例を束ねる。",
     "cut":"『従来型広告がかつてなく有効』『個人の意見はほぼ影響しない』『企業は顧客の声を聞くのをやめた』は本文の主張と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["absorb","produce","ignore","release"],"answer":"ア",
     "basis":"<span class='en'>trees ( ) carbon dioxide from the atmosphere and lock the carbon away</span>。大気『から』炭素をどうするか。",
     "solve":"<span class='en'>absorb ... from the atmosphere</span>（大気から吸収する）。直後の <span class='en'>lock the carbon away</span>（閉じ込める）と整合。",
     "cut":"<span class='en'>produce / release</span>（生み出す・放出する）は『閉じ込める』と逆。<span class='en'>ignore</span> は無意味。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["offset","double","ignore","cause"],"answer":"ア",
     "basis":"<span class='en'>a healthy woodland can ( ) the warming effect of gases released by cars and factories</span>。炭素を吸収する森の働き。",
     "solve":"吸収→温暖化効果を<b>打ち消す</b>＝<span class='en'>offset the warming effect</span>（相殺する）。空気を浄化するという前段と整合。",
     "cut":"<span class='en'>double</span>（倍にする）や <span class='en'>cause</span>（引き起こす）は温暖化を強める方向で逆。<span class='en'>ignore</span> は不整合。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "This natural service, however, lasts only as long as the forest is left standing.",
       "As a result, planting new trees can never affect the climate at all.",
       "Trees, in fact, give off far more carbon than they ever take in.",
       "Fortunately, a burned forest stores even more carbon than before."],"answer":"ア",
     "basis":"空所前＝森が温暖化効果を相殺する（良い働き）。空所後＝<span class='en'>When forests are cut down or burned, that stored carbon escapes ...</span>（伐採・焼失で炭素が逃げ気候を温める逆転）。",
     "solve":"空所は <span class='en'>however</span> で<b>好条件→崩壊</b>を対比する橋渡し。『この働きは森が立っている限りにおいてのみ続く』が直後の伐採の帰結を導く。",
     "cut":"『植林は気候に影響しない』『木は吸収より排出が多い』『燃えた森はより多く蓄える』は、吸収と貯留を説く本文と矛盾。"},
  ],
  "trans": [
    ("文1", "企業は広告に大金を費やせるが、顧客が最も信頼するメッセージが企業自身から来ることはまれだ。むしろそれは他の買い手から来る。"
            "友人が製品を褒めたり、オンラインのレビュアーが正直な体験を語ったりするとき、その推薦はどんな有料の宣伝文句も及ばない"
            "<b>信頼性</b>を帯びる。そうした意見は商業的な動機がないように感じられるため、買い物客は華やかなコマーシャルよりも"
            "それらをはるかに<b>信じ</b>やすい。<b>ソーシャルメディアの時代、この日常のおしゃべりは強力なマーケティングの力になった。</b>"
            "たった一つのバズった投稿が無名のブランドを一夜で押し上げることもあれば、怒りのレビューの波が有名ブランドを同じ速さで沈めることもある。"),
    ("文2", "森は単なる木の集まりをはるかに超えるもので、大気を浄化する地球の偉大なエンジンの一つだ。木は成長するにつれ、大気から"
            "二酸化炭素を<b>吸収し</b>、その炭素を幹や根、そしてその下の土壌に閉じ込める。こうして健全な森林は、自動車や工場から"
            "放出される気体の温暖化効果を<b>相殺する</b>ことができる。<b>しかしこの自然の働きは、森が立ったままである限りにおいてのみ続く。</b>"
            "森が伐採されたり燃やされたりすると、蓄えられた炭素は空へと逃げ戻り、かつて気候を冷やしていた仕組みが突如としてそれを温め始めるのだ。"),
  ],
  "vocab": [
    ("credibility", "名", "信頼性、信憑性"),
    ("viral", "形", "急速に拡散する、バズる"),
    ("glossy", "形", "華やかな、光沢のある"),
    ("word of mouth", "句", "口コミ"),
    ("absorb", "動", "吸収する"),
    ("offset", "動", "相殺する、埋め合わせる"),
    ("atmosphere", "名", "大気"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋論理の向き</b>で決める――"
    "<span class='en'>carry credibility</span>・<span class='en'>absorb ... from</span>・<span class='en'>offset the warming effect</span> の"
    "結び付きと、『動機がない→信じる』『吸収→相殺』の因果を確認する。文選択空所（43・46）は<b>一般化→具体例</b>や"
    "<span class='en'>however</span> による<b>好転→崩壊の対比</b>で一意に決まる。代入して前後を音読し確かめる。",
}
