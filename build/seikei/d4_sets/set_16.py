# -*- coding: utf-8 -*-
"""大問Ⅳ SET 16 ― 短文2本・空所6（語彙4＋文選択2）。
文1=ダイバーシティと組織（ビジネス）／文2=渡り鮭と川の生態（科学）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "ダイバーシティと組織 ＆ 渡り鮭と川の生態",
  "genre": "ビジネス／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Why Different Minds Matter", "wordcount": 93,
     "paras": [
        "Companies increasingly recognise that a diverse workforce is not merely a matter of fairness. "
        "When people from different backgrounds gather in one team, they bring a wider range of [[b:41]], "
        "and this variety often sparks fresh ideas. A group whose members all think alike tends to [[b:42]] "
        "the same familiar solutions and overlook hidden risks. [[b:43]] "
        "Managers who value only harmony may silence the very voices that could warn them of a mistake. "
        "In short, difference, when handled well, becomes a quiet engine of innovation rather than a source of endless conflict.",
     ]},
    {"label": "文2", "title": "The Long Swim Home", "wordcount": 99,
     "paras": [
        "Each autumn, salmon leave the ocean and swim back to the very streams where they were born. "
        "The journey is exhausting: they battle strong currents, leap up waterfalls, and stop eating altogether. "
        "Most die soon after they [[b:44]], but their bodies are far from wasted. "
        "As the carcasses decay, they release nitrogen and other nutrients that [[b:45]] the whole river. [[b:46]] "
        "Bears and eagles drag the fish into the forest, where the remains feed the soil and help giant trees grow. "
        "In this way a single fish links the distant sea to the roots of an inland woodland.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["perspectives","silences","apologies","machines"],"answer":"ア",
     "basis":"直前 <span class='en'>they bring a wider range of ( ), and this variety often sparks fresh ideas</span>。"
             "『幅広い〜をもたらし、その多様性が新鮮なアイデアを生む』。",
     "solve":"<span class='en'>a wider range of ( )</span> と <span class='en'>this variety</span> が同じものを指す。"
             "異なる背景の人が持ち寄るのは<b>視点</b>＝<span class='en'>perspectives</span>。",
     "cut":"<span class='en'>silences</span>（沈黙）は多様性の逆。<span class='en'>apologies / machines</span> は文脈と無関係。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["recycle","invent","question","abandon"],"answer":"ア",
     "basis":"<span class='en'>A group whose members all think alike tends to ( ) the same familiar solutions and overlook hidden risks</span>。"
             "『皆が同じように考える集団』の行動。",
     "solve":"<span class='en'>the same familiar solutions</span>（同じ使い慣れた解決策）と結ぶ動詞。同質な集団は既存策を<b>使い回す</b>＝<span class='en'>recycle</span>。",
     "cut":"<span class='en'>invent</span>（新しく生む）・<span class='en'>question</span>（疑う）・<span class='en'>abandon</span>（捨てる）は『同じ策を繰り返す』流れと逆。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "A little friction between viewpoints, therefore, can be surprisingly productive.",
       "Such teams therefore make decisions far more quickly than others.",
       "This proves that agreement is always the goal of good teamwork.",
       "Hiring for fairness alone rarely affects a company profits."],"answer":"ア",
     "basis":"空所前＝『同質な集団は同じ策を繰り返しリスクを見落とす』（問題）。"
             "空所後＝<span class='en'>Managers who value only harmony may silence the very voices ...</span>（調和重視が警告の声を封じる）。",
     "solve":"空所は<b>問題→含意</b>の橋渡し。見落としの害を受け、『視点の摩擦はむしろ生産的』が入れば、直後の『調和ばかりだと声を封じる』に自然につながる。",
     "cut":"『決定が速い』は速度の話でずれる。『合意こそ常に目標』は本文の主張（摩擦の価値）と逆。『採用は利益に影響しない』は話題がそれる。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["spawn","recover","escape","hatch"],"answer":"ア",
     "basis":"<span class='en'>Most die soon after they ( ), but their bodies are far from wasted</span>。"
             "生まれた川に戻った鮭が『〜した直後に死ぬ』。",
     "solve":"川へ戻る目的は繁殖。産卵＝<span class='en'>spawn</span>すると力尽きて死ぬ、という生態と一致。",
     "cut":"<span class='en'>recover</span>（回復）・<span class='en'>escape</span>（逃げる）は直後 <span class='en'>die</span> と矛盾。"
            "<span class='en'>hatch</span>（孵化する）は卵の側の動作。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["enrich","pollute","drain","freeze"],"answer":"ア",
     "basis":"<span class='en'>they release nitrogen and other nutrients that ( ) the whole river</span>。死骸が窒素などの栄養分を放出。",
     "solve":"<span class='en'>nutrients that ( ) the whole river</span>。栄養分は川を<b>豊かにする</b>＝<span class='en'>enrich</span>。",
     "cut":"<span class='en'>pollute</span>（汚染）は栄養分の恵みという文脈と逆。<span class='en'>drain</span>（枯渇させる）・<span class='en'>freeze</span>（凍らせる）も不整合。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Yet the benefits do not stop at the water edge.",
       "As a result, the river slowly loses all its living things.",
       "For this reason, no animal will touch the dying fish.",
       "The salmon, however, never actually reach their birthplace."],"answer":"ア",
     "basis":"空所前＝『栄養分が川全体を豊かにする』。空所後＝<span class='en'>Bears and eagles drag the fish into the forest ...</span>（熊や鷲が魚を森へ運び土を養う）。",
     "solve":"空所は<b>川の中→陸へ</b>の橋渡し。『恩恵は水際で止まらない』を入れると、直後の『森へ運ばれ土を養う』へ話が広がる。",
     "cut":"『川が生き物を失う』『どの動物も触れない』は直後の描写（熊や鷲が運ぶ）と矛盾。『生まれた場所に決して届かない』は冒頭の帰還と矛盾。"},
  ],
  "trans": [
    ("文1", "企業はますます、多様な労働力が単なる公平さの問題ではないと認識している。異なる背景を持つ人々が一つのチームに集まると、"
            "彼らはより広い範囲の<b>視点</b>をもたらし、この多様性がしばしば新鮮なアイデアを生む。全員が同じように考える集団は、"
            "同じ使い慣れた解決策を<b>使い回し</b>がちで、隠れたリスクを見落とす。<b>それゆえ、視点どうしのわずかな摩擦は、驚くほど生産的でありうる。</b>"
            "調和ばかりを重んじる管理者は、失敗を警告してくれるかもしれないまさにその声を封じてしまう。要するに、うまく扱えば、"
            "違いは終わりのない対立の源ではなく、静かなイノベーションの原動力になるのだ。"),
    ("文2", "毎秋、鮭は海を離れ、自分が生まれたまさにその川へと泳いで戻る。その旅は過酷だ。強い流れと戦い、滝を跳び上がり、"
            "食べることを完全にやめる。ほとんどは<b>産卵する</b>とまもなく死ぬが、その体は決して無駄にならない。死骸が腐敗するにつれ、"
            "窒素やその他の栄養分を放出し、それが川全体を<b>豊かにする</b>。<b>だが、その恩恵は水際で止まらない。</b>熊や鷲が魚を森へ引きずり込み、"
            "そこで残骸が土を養い、巨大な木々の成長を助ける。こうして一匹の魚が、遠い海を内陸の森の根とつなぐのだ。"),
  ],
  "vocab": [
    ("diverse", "形", "多様な"),
    ("perspective", "名", "視点、観点"),
    ("overlook", "動", "見落とす"),
    ("friction", "名", "摩擦、対立"),
    ("spawn", "動", "産卵する"),
    ("carcass", "名", "死骸"),
    ("nutrient", "名", "栄養分"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（問題→含意／内側→外側への拡張）</b>で一意に決まる。"
    "文選択は代入して前後を音読し、指示語（<span class='en'>it / this</span>）が正しく受かる1文を選ぶ。",
}
