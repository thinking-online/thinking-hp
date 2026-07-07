# -*- coding: utf-8 -*-
"""大問Ⅳ SET 04 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=キャッシュレス決済と小売／文2=サンゴ礁と海洋温暖化。"""

SET = {
  "theme": "キャッシュレス決済と小さな店 ＆ サンゴ礁と海の温暖化",
  "genre": "ビジネス／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Small Shops Go Cashless", "wordcount": 94,
     "paras": [
        "For small shops, going cashless once seemed like a luxury reserved for large chains. "
        "Today, however, many owners find that accepting cards and phone payments actually [[b:41]] their daily work. "
        "Counting coins, guarding cash after closing time, and making frequent trips to the bank all shrink or even disappear. "
        "[[b:43]] "
        "Customers, meanwhile, tend to spend a little more freely when they do not have to [[b:42]] the exact change in their pockets. "
        "For a tiny store with thin margins, even a small rise in sales can decide whether the business survives another difficult year.",
     ]},
    {"label": "文2", "title": "The Quiet Crisis of Coral", "wordcount": 100,
     "paras": [
        "Coral reefs cover a tiny fraction of the ocean floor, yet they [[b:44]] roughly a quarter of all marine species. "
        "This richness depends on a quiet partnership: tiny algae live inside the coral and feed it through photosynthesis. "
        "When the water grows too warm, however, the coral expels these algae and turns a ghostly white. "
        "[[b:46]] "
        "If cooler conditions return quickly, the reef may recover, but repeated heat waves leave it [[b:45]] and easy prey for disease. "
        "Protecting reefs, therefore, is not only about saving fish; it is about defending coasts and the millions of people who live beside them.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["simplifies","complicates","delays","records"],"answer":"ア",
     "basis":"直前 <span class='en'>accepting cards and phone payments actually ( ) their daily work</span>。"
             "直後で <span class='en'>Counting coins ... all shrink or even disappear</span>（作業が減る・消える）と続く。",
     "solve":"面倒な現金作業が<b>減る</b>のだから、日々の仕事を『簡単にする』＝<span class='en'>simplifies</span>。後続の具体例が理由づけ。",
     "cut":"『複雑にする』は作業が減る描写と逆。『遅らせる』『記録する』は <span class='en'>daily work</span> の変化として文脈に合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語句を選べ。","inline":True,
     "choices":["dig for","give away","carry out","depend on"],"answer":"ア",
     "basis":"<span class='en'>when they do not have to ( ) the exact change in their pockets</span>。"
             "キャッシュレスなら<b>小銭を探す</b>必要がない、という含意。",
     "solve":"<span class='en'>in their pockets</span> と結ぶと『ポケットの中でちょうどの小銭を<b>探す</b>』＝<span class='en'>dig for</span>。",
     "cut":"『与える』『実行する』『頼る』はいずれも <span class='en'>the exact change in their pockets</span> と噛み合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "That frees owners to spend their time on customers rather than on cash.",
       "As a result, most owners soon return to handling only cash.",
       "Still, the machines rarely save any real time at all.",
       "Larger chains, therefore, avoid these payment systems entirely."],"answer":"ア",
     "basis":"空所前＝『現金の作業が減る・消える』（経営者の利点）。空所後＝<span class='en'>Customers, meanwhile ...</span>（<b>一方で</b>客の話へ）。",
     "solve":"空所は経営者側の利点をまとめる位置。『経営者を、現金ではなく客に時間を割けるようにする』が入れば <span class='en'>meanwhile</span> の対比が自然。",
     "cut":"『現金だけに戻る』『時間を節約しない』は利点の流れと逆。『大手はこの決済を避ける』は小さな店の話とずれる。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["support","destroy","ignore","escape"],"answer":"ア",
     "basis":"<span class='en'>they ( ) roughly a quarter of all marine species</span>。"
             "直前は <span class='en'>a tiny fraction ... yet</span>（わずかな面積<b>なのに</b>）という譲歩。",
     "solve":"<span class='en'>yet</span> の逆接から、狭いのに多くの生物を『支える』＝<span class='en'>support</span>。次文の <span class='en'>richness</span> とも整合。",
     "cut":"『破壊する』は生物の豊かさの説明と正反対。『無視する』『逃れる』は主語（サンゴ礁）と目的語が結びつかない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["weakened","stronger","colorful","protected"],"answer":"ア",
     "basis":"<span class='en'>repeated heat waves leave it ( ) and easy prey for disease</span>。"
             "<span class='en'>and easy prey for disease</span>（病気の格好の餌食）と並ぶ状態語。",
     "solve":"『病気の餌食』と等位で並ぶのは<b>弱った</b>状態＝<span class='en'>weakened</span>。繰り返す熱波の悪影響と一致。",
     "cut":"『より強い』『色鮮やかな』『守られた』はいずれも <span class='en'>easy prey for disease</span> と論理が逆。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "This bleaching does not kill the coral at once, but it leaves it starving.",
       "Such warming actually helps the algae grow far faster.",
       "Bright colors are a clear sign that the reef is dying.",
       "Warmer seas, in fact, make reefs stronger over time."],"answer":"ア",
     "basis":"空所前＝『藻を吐き出し白くなる』（白化）。空所後＝<span class='en'>If cooler conditions return quickly, the reef may recover ...</span>（回復もありうる）。",
     "solve":"空所は白化の帰結を述べる位置。『白化はただちに殺さないが飢えさせる』なら、直後の『すぐ冷えれば回復』が自然につながる。",
     "cut":"『温暖化が藻を速く育てる』『明るい色が死の兆候』『暖かい海が礁を強くする』は、白化＝白くなる・弱るという本文と矛盾。"},
  ],
  "trans": [
    ("文1", "小さな店にとって、キャッシュレス化はかつて大手チェーンだけの贅沢に思えた。しかし今日、多くの経営者は、"
            "カードやスマホ決済を受け入れることが実際に日々の仕事を<b>簡単にする</b>と気づいている。硬貨を数え、閉店後に現金を守り、"
            "頻繁に銀行へ足を運ぶ――そうした作業はすべて減るか、消えさえする。<b>それは経営者を、現金ではなく客に時間を割けるようにしてくれる。</b>"
            "一方で客は、ポケットの中でちょうどの小銭を<b>探さ</b>なくてよいと、少し気前よく使う傾向がある。"
            "利益の薄い小さな店では、わずかな売上増でも、次の厳しい一年を生き延びられるかどうかを左右しうる。"),
    ("文2", "サンゴ礁は海底のごくわずかな部分を覆うにすぎないが、全海洋生物のおよそ四分の一を<b>支えている</b>。"
            "この豊かさは静かな協力関係に依存している。小さな藻がサンゴの内部に住み、光合成でサンゴに栄養を与えるのだ。"
            "しかし水温が高くなりすぎると、サンゴはこの藻を吐き出し、幽霊のように白くなる。"
            "<b>この白化はサンゴをただちに殺しはしないが、飢えた状態にする。</b>"
            "すぐに涼しい状態に戻れば礁は回復するかもしれないが、繰り返す熱波はそれを<b>弱らせ</b>、病気の格好の餌食にしてしまう。"
            "だからサンゴ礁を守ることは、魚を救うことだけの話ではない。海岸と、そのそばで暮らす何百万もの人々を守ることなのだ。"),
  ],
  "vocab": [
    ("cashless", "形", "現金を使わない"),
    ("margin", "名", "利ざや、余白"),
    ("algae", "名", "藻類"),
    ("photosynthesis", "名", "光合成"),
    ("expel", "動", "吐き出す、追い出す"),
    ("prey", "名", "獲物、餌食"),
    ("marine", "形", "海洋の"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で決める。"
    "特に <span class='en'>yet</span> の逆接（44）や、等位接続 <span class='en'>and</span> で並ぶ語（45）は<b>周りの語との論理</b>が手がかり。"
    "文選択空所（43・46）は<b>前後の論理（利点のまとめ→対比／原因→結果）</b>で一意に。代入して前後を音読し、話が途切れない1文を選ぶ。",
}
