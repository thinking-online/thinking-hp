# -*- coding: utf-8 -*-
"""大問Ⅳ SET 14 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=図書館の役割の変化／文2=光害と生態系。"""

SET = {
  "theme": "図書館の役割の変化 ＆ 光害と生態系",
  "genre": "文化・社会／科学・環境 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The Changing Library", "wordcount": 95,
     "paras": [
        "For centuries, a library was mainly a quiet place to store and borrow printed books. "
        "Over the last few decades, however, its role has [[b:41]] dramatically. "
        "Many public libraries now offer free internet, quiet study rooms, maker spaces with 3D printers, "
        "and even classes for job seekers. [[b:43]] "
        "Rather than simply lending books, they help people who lack a computer at home to [[b:42]] "
        "the digital world with confidence. In poorer neighbourhoods especially, the library has become "
        "a rare public space where anyone can gather, learn, and connect without paying a single coin.",
     ]},
    {"label": "文2", "title": "When the Night Grows Too Bright", "wordcount": 95,
     "paras": [
        "At night, artificial light now brightens much of the planet, and for many wild species this glow "
        "is far from harmless. Sea turtles offer a striking [[b:44]]. "
        "Newly hatched turtles instinctively crawl toward the brightest horizon, which for millions of years "
        "was the moonlit sea. [[b:46]] "
        "Today the bright lights of hotels and busy roads draw them inland, where many die of exhaustion or traffic. "
        "Migrating birds, too, grow confused by illuminated towers and [[b:45]] far off their natural routes. "
        "Dimming needless lights at night, scientists argue, would cost very little yet save countless lives.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["expanded","shrunk","expired","frozen"],"answer":"ア",
     "basis":"直前 <span class='en'>its role has ( ) dramatically</span>。直後で無料ネット・学習室・工作室・講座と<b>新しい役割が次々に列挙</b>される。",
     "solve":"『役割が劇的に〜した』＋直後の役割拡大の列挙から、<span class='en'>expanded</span>（広がった）が一致。",
     "cut":"<span class='en'>shrunk</span>（縮んだ）は役割の増加と逆。<span class='en'>expired</span>（期限切れ）・<span class='en'>frozen</span>（凍った）は主語 <span class='en'>role</span> と噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["navigate","ignore","escape","forget"],"answer":"ア",
     "basis":"<span class='en'>help people who lack a computer ... to ( ) the digital world with confidence</span>。家にPCがない人を<b>助ける</b>文脈。",
     "solve":"<span class='en'>( ) the digital world</span>＝『デジタル世界を<b>うまく渡り歩く</b>』。<span class='en'>navigate</span> のコロケ、<span class='en'>with confidence</span> とも整合。",
     "cut":"<span class='en'>ignore</span>（無視）・<span class='en'>escape</span>（逃げる）・<span class='en'>forget</span>（忘れる）は『助ける』趣旨と逆向き。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "In other words, the library has quietly become a community centre.",
       "As a result, fewer people than ever now walk through its doors.",
       "Books, however, remain the only real purpose it has ever served.",
       "Most of these new services are offered only to paying members."],"answer":"ア",
     "basis":"空所前＝ネット・学習室・工作室・講座という<b>多彩なサービスの列挙</b>。空所後＝『本を貸すだけでなく人々を助ける』という説明。",
     "solve":"空所は<b>列挙→まとめ（一般化）</b>の橋渡し。列挙を束ねる『図書館は地域の中心地になった』が自然につながる。",
     "cut":"『来館者が減った』は役割拡大の趣旨と逆。『本だけが目的』は列挙と矛盾。『有料会員限定』は <span class='en'>without paying a single coin</span> と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["example","silence","holiday","distance"],"answer":"ア",
     "basis":"<span class='en'>Sea turtles offer a striking ( )</span>。直後でウミガメが光に惑わされる具体的な話が続く。",
     "solve":"<span class='en'>a striking ( )</span>＝『際立った<b>例</b>』。<span class='en'>a striking example</span> のコロケで、直後の具体例を予告する。",
     "cut":"<span class='en'>silence</span>（静けさ）・<span class='en'>holiday</span>（休日）・<span class='en'>distance</span>（距離）は続く具体例を導く語として成立しない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["stray","gather","freeze","rest"],"answer":"ア",
     "basis":"<span class='en'>birds ... grow confused by illuminated towers and ( ) far off their natural routes</span>。光の塔に惑わされた鳥の動き。",
     "solve":"<span class='en'>( ) far off their natural routes</span>＝『本来の経路から大きく<b>それる</b>』。<span class='en'>stray far off</span> のコロケで『混乱』と整合。",
     "cut":"<span class='en'>gather</span>（集まる）・<span class='en'>freeze</span>（凍る）・<span class='en'>rest</span>（休む）は <span class='en'>far off their routes</span> と結びつかない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "For millions of years, this simple cue guided them safely to the water.",
       "Sadly, hatchlings have never been able to sense any light at all.",
       "The moon, however, has grown far too dim for turtles to notice.",
       "Most young turtles simply wait on the beach until the next sunrise."],"answer":"ア",
     "basis":"空所前＝『稚ガメは最も明るい地平＝かつては月明かりの海へ本能的に進む』。空所後＝<span class='en'>Today the bright lights ...</span>（今日はホテルや道路の光が内陸へ誘う）。",
     "solve":"空所は<b>昔（安全）→今（危険）</b>の対比の軸。『長い間この手がかりが海へ安全に導いた』が入り、直後の <span class='en'>Today</span> が対比を完成させる。",
     "cut":"『光を感じられない』は本能的に明るい方へ進む描写と矛盾。『月が暗すぎる』は事実と逆。『浜で夜明けを待つ』は『地平へ這う』描写と矛盾。"},
  ],
  "trans": [
    ("文1", "何世紀もの間、図書館は主に印刷された本を保管し貸し出す静かな場所だった。だがここ数十年で、その役割は劇的に"
            "<b>広がった</b>。今や多くの公共図書館は、無料のインターネット、静かな学習室、3Dプリンター付きの工作スペース、"
            "さらには求職者向けの講座まで提供している。<b>言い換えれば、図書館は静かに地域の中心地となったのだ。</b>"
            "単に本を貸すのではなく、家にコンピューターがない人々がデジタル世界を自信をもって<b>渡り歩く</b>手助けをしている。"
            "とりわけ貧しい地区では、図書館は誰もが一銭も払わずに集い、学び、つながれる数少ない公共空間になっている。"),
    ("文2", "夜、人工の光は今や地球の多くを明るく照らしており、多くの野生生物にとってこの光は決して無害ではない。"
            "ウミガメは際立った<b>例</b>を示す。孵化したばかりの稚ガメは本能的に最も明るい地平へ這い進むが、それは何百万年もの間、"
            "月明かりに照らされた海だった。<b>何百万年もの間、この単純な手がかりが彼らを安全に海へと導いてきた。</b>"
            "今日ではホテルや交通量の多い道路の明るい光が彼らを内陸へ誘い、多くが疲労や車にはねられて死ぬ。渡り鳥もまた、"
            "照らされた塔に惑わされ、本来の経路から大きく<b>それて</b>しまう。夜の不要な光を落とせば、費用はごくわずかでも"
            "無数の命を救えるはずだ、と科学者は主張する。"),
  ],
  "vocab": [
    ("maker space", "名", "工作・ものづくりの共用空間"),
    ("navigate", "動", "うまく進む、渡り歩く"),
    ("hatch", "動", "孵化する"),
    ("horizon", "名", "地平線、水平線"),
    ("stray", "動", "それる、はぐれる"),
    ("illuminated", "形", "照らされた、明るく照明された"),
    ("exhaustion", "名", "疲労困憊"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（列挙→まとめ／昔→今の対比）</b>で一意に決まる。"
    "文選択は代入して前後を音読し、話が途切れない1文を選ぶ。",
}
