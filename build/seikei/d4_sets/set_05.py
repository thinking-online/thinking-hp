# -*- coding: utf-8 -*-
"""大問Ⅳ SET 05 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=サブスクリプションと所有／文2=渡り鳥のナビゲーション。"""

SET = {
  "theme": "サブスクリプションと所有 ＆ 渡り鳥はどう道を見つけるか",
  "genre": "ビジネス・社会／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "From Owning to Renting", "wordcount": 94,
     "paras": [
        "A generation ago, people mostly bought the things they used and kept them for years. "
        "Now music, films, software, and even cars increasingly arrive by [[b:41]] instead. "
        "For a monthly fee, you gain access to a vast library, yet you never actually [[b:42]] any of it. "
        "[[b:43]] "
        "Companies like this model because a steady stream of small payments is easier to predict than one large sale. "
        "Customers enjoy the convenience and the low starting price. "
        "Still, those little charges quietly add up, and many people pay for services they have long since stopped using.",
     ]},
    {"label": "文2", "title": "How Birds Find Their Way", "wordcount": 100,
     "paras": [
        "Every autumn, millions of birds set off on journeys of thousands of kilometres, often to places they have never seen. "
        "How they find their way has puzzled scientists for centuries. "
        "Part of the answer lies in the sky: many species [[b:44]] the position of the sun by day and the pattern of stars by night. "
        "[[b:46]] "
        "Remarkably, birds also seem to sense the Earth's magnetic field, using it like an invisible compass built into their bodies. "
        "Young birds inherit a rough sense of direction, but experience gradually [[b:45]] it, teaching them to correct for wind and weather along the route.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["subscription","accident","mistake","tradition"],"answer":"ア",
     "basis":"直前 <span class='en'>music, films, software, and even cars increasingly arrive by ( ) instead</span>。"
             "直前文は『昔は買って何年も持った』という対比。",
     "solve":"『買う』のではなく月ぎめで届く仕組み＝『定額利用（サブスク）』＝<span class='en'>subscription</span>。次文 <span class='en'>a monthly fee</span> が裏づけ。",
     "cut":"『事故』『間違い』『伝統』はいずれも <span class='en'>arrive by ( )</span> の手段として文脈に合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["own","lose","break","sell"],"answer":"ア",
     "basis":"<span class='en'>you gain access to a vast library, yet you never actually ( ) any of it</span>。"
             "<span class='en'>access</span>（利用）と <span class='en'>yet</span> で対比される語。",
     "solve":"『使えるが決して<b>所有</b>しない』の対比。<span class='en'>access</span> の対義は <span class='en'>own</span>。",
     "cut":"『失う』『壊す』『売る』は <span class='en'>gain access ... yet</span> の対比構造（利用 対 所有）に合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "This shift from owning to borrowing suits both sides, at least at first.",
       "As a result, buyers now insist on owning everything outright.",
       "Few businesses have any reason to prefer such an arrangement.",
       "Renting, in the end, always costs far less than buying."],"answer":"ア",
     "basis":"空所前＝『利用できるが所有しない』。空所後＝<span class='en'>Companies like this model ...</span>（企業側）→<span class='en'>Customers enjoy ...</span>（客側）と<b>両者</b>の利点が続く。",
     "solve":"空所は企業と客の双方の話をまとめて導く位置。『所有から借用への移行は、少なくとも最初は双方に都合がよい』が両側の説明に橋渡しする。",
     "cut":"『買い手は所有に固執する』は所有しない流れと逆。『企業が好む理由はない』は直後 <span class='en'>Companies like this model</span> と矛盾。『常に安い』は末尾『料金が積み重なる』と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["track","hide","cause","waste"],"answer":"ア",
     "basis":"<span class='en'>many species ( ) the position of the sun by day and the pattern of stars by night</span>。"
             "直前 <span class='en'>Part of the answer lies in the sky</span>（答えの一部は空にある）。",
     "solve":"太陽や星の位置を手がかりに道を探すのだから『追う・把握する』＝<span class='en'>track</span>。<span class='en'>the position of the sun</span> と好相性。",
     "cut":"『隠す』『引き起こす』『無駄にする』はいずれも <span class='en'>the position of the sun</span> と結びつかない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["sharpens","erases","ignores","weakens"],"answer":"ア",
     "basis":"<span class='en'>Young birds inherit a rough sense of direction, but experience gradually ( ) it</span>。"
             "<span class='en'>a rough sense</span>（大まかな感覚）と <span class='en'>but</span> の逆接。",
     "solve":"『大まか』だった感覚を経験が<b>研ぎ澄ます</b>＝<span class='en'>sharpens</span>。続く <span class='en'>teaching them to correct ...</span>（修正を教える）とも整合。",
     "cut":"『消す』『無視する』『弱める』は、経験で方向感覚が向上するという後続と逆向き。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Yet the sky is often hidden by clouds, so these cues cannot be the whole story.",
       "In fact, no bird has ever been shown to watch the stars.",
       "Because of this, birds simply follow rivers and coastlines home.",
       "This proves that the sun alone guides every migration."],"answer":"ア",
     "basis":"空所前＝『昼は太陽、夜は星を手がかりにする』。空所後＝<span class='en'>Remarkably, birds also seem to sense the Earth's magnetic field ...</span>（<b>also</b> で別の手段を追加）。",
     "solve":"空所は空の手がかりの限界を示す位置。『空は雲に隠れるので、これだけでは全部を説明できない』なら、直後の <span class='en'>also ... magnetic field</span> が『足りない分を補う手段』として自然に続く。",
     "cut":"『星を見る鳥はいない』は直前と矛盾。『川や海岸線をたどる』は磁場の話へつながらない。『太陽だけが導く』は直後の <span class='en'>also</span>（別手段の追加）と矛盾。"},
  ],
  "trans": [
    ("文1", "一世代前、人々は使うものをたいてい買い、何年も手元に置いた。今や音楽、映画、ソフト、さらには車までもが、"
            "代わりに<b>サブスクリプション</b>で届くことが増えている。月ぎめの料金で、膨大なライブラリーにアクセスできるが、"
            "そのどれも実際に<b>所有する</b>ことはない。<b>この所有から借用への移行は、少なくとも最初のうちは双方に都合がよい。</b>"
            "企業がこの仕組みを好むのは、小さな支払いの安定した流れのほうが、一度の大きな販売より予測しやすいからだ。"
            "客は手軽さと安い出だしの価格を喜ぶ。それでも、そうしたわずかな料金は静かに積み重なり、多くの人はとうにやめたサービスに払い続けている。"),
    ("文2", "毎秋、何百万羽もの鳥が数千キロの旅に出る。しばしば見たこともない場所へと。どうやって道を見つけるのかは、"
            "何世紀も科学者を悩ませてきた。答えの一部は空にある。多くの種は昼は太陽の位置を、夜は星の並びを<b>追う</b>のだ。"
            "<b>とはいえ空はしばしば雲に隠れるので、これらの手がかりだけがすべてではありえない。</b>"
            "驚くべきことに、鳥は地球の磁場も感じ取り、体に組み込まれた見えないコンパスのように使っているようだ。"
            "若い鳥は大まかな方向感覚を受け継ぐが、経験がそれを次第に<b>研ぎ澄まし</b>、道中の風や天気に合わせて修正することを教える。"),
  ],
  "vocab": [
    ("subscription", "名", "定額購読、サブスク"),
    ("access", "名／動", "利用（する）、接続"),
    ("predict", "動", "予測する"),
    ("migratory", "形", "渡りをする"),
    ("magnetic field", "名", "磁場"),
    ("inherit", "動", "受け継ぐ"),
    ("puzzle", "動", "悩ませる、当惑させる"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で決める。"
    "<span class='en'>yet</span> や <span class='en'>but</span> の逆接（42・45）は<b>反対語・対比語</b>が答えのサイン。"
    "文選択空所（43・46）は<b>前後の論理（両者の導入／限界→追加手段）</b>で一意に。特に直後の <span class='en'>also</span> は『別の手段の追加』を予告する。",
}
