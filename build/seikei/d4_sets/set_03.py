# -*- coding: utf-8 -*-
"""大問Ⅳ SET 03 ― 短文2本・空所6（語彙4＋文選択2）。
文1=電気自動車の普及（技術／ビジネス）、文2=ミツバチと農業（科学）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "電気自動車の普及 ＆ ミツバチと農業",
  "genre": "技術・ビジネス／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The End of Range Anxiety", "wordcount": 102,
     "paras": [
        "For years, drivers hesitated to buy electric cars, and the reason was almost always the same: "
        "they were afraid of running out of power far from home. "
        "This worry, often called range anxiety, kept many buyers [[b:41]] to petrol. "
        "Two things are now changing their minds. "
        "Batteries have grown cheaper and can travel much farther on a single charge, "
        "and fast chargers are [[b:42]] along major highways. "
        "[[b:43]] "
        "A trip that once required careful planning can now be made with a short stop for coffee while the car refills. "
        "As the network grows, the old fear is quietly fading.",
     ]},
    {"label": "文2", "title": "The Insects on Our Plates", "wordcount": 102,
     "paras": [
        "We rarely thank the insects that make our meals possible, yet without them many fields would fall silent. "
        "Bees carry pollen from flower to flower, allowing plants to produce the fruits and seeds we eat. "
        "About a third of the food on our plates [[b:44]] on this quiet service. "
        "In recent years, however, bee populations have [[b:45]] sharply, "
        "hit by disease, pesticides, and the loss of wild flowers. "
        "[[b:46]] "
        "Some farmers now rent hives by the truckload and plant strips of flowers at the edges of their fields. "
        "Protecting bees, they have learned, is not charity; it is good business.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["loyal","similar","close","equal"],"answer":"ア",
     "basis":"直前 <span class='en'>This worry ... kept many buyers ( ) to petrol</span>。"
             "電池切れの不安が、買い手をガソリン車に『とどめた』という文脈。",
     "solve":"<span class='en'>( ) to petrol</span>＝『ガソリンから離れない』。<span class='en'>loyal to</span>（〜に忠実な・離れない）のコロケーション。"
             "不安が買い替えを妨げる論理に一致。",
     "cut":"<span class='en'>similar / close / equal to</span> は『比較・近さ・等しさ』で、"
           "『ガソリンに固執し続ける』という意味にはならない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["multiplying","disappearing","closing","failing"],"answer":"ア",
     "basis":"<span class='en'>Two things are now changing their minds</span> の2つ目。"
             "<span class='en'>fast chargers are ( ) along major highways</span>。買い手の考えを変える<b>良い変化</b>。",
     "solve":"電池が安く遠くまで走れるようになった、に並ぶ好材料＝急速充電器が<b>増えている</b>。"
             "<span class='en'>multiplying</span>（急増する）が一意。",
     "cut":"<span class='en'>disappearing / closing / failing</span> はいずれも減少・不調で、"
           "『考えを変える良い変化』という文脈と逆になる。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "Together, these advances make long journeys far less stressful.",
       "Even so, charging remains impossible outside big cities.",
       "This is why sales of electric cars keep falling.",
       "Petrol engines have therefore become the cleaner choice."],"answer":"ア",
     "basis":"空所前＝『電池が安く遠くまで走れ、充電器も増えている』という2つの<b>進歩（原因）</b>。"
             "空所後＝『かつて綿密な計画が要った旅も、コーヒー休憩の間に充電して行ける』という<b>結果</b>。",
     "solve":"空所は<b>原因→結果</b>の橋渡し。二つの進歩を束ねて『これらの進歩が長旅の負担を大きく減らす』が最適。",
     "cut":"『都市の外では充電不可』は充電器増加と矛盾、『販売が減り続ける』は考えが変わる流れと逆、"
           "『ガソリン車の方が環境に良い』は文脈と無関係。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["depends","arrives","spends","insists"],"answer":"ア",
     "basis":"<span class='en'>About a third of the food on our plates ( ) on this quiet service</span>。"
             "直前でミツバチの受粉が食料生産を支えると述べている。",
     "solve":"<span class='en'>( ) on this service</span>＝『この働きに<b>依存している</b>』。<span class='en'>depend on</span> のコロケーション。",
     "cut":"<span class='en'>arrives / spends / insists</span> は <span class='en'>on</span> と結んでも"
           "『〜に頼る』の意味にならず、主語 <span class='en'>a third of the food</span> と噛み合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["fallen","grown","survived","spread"],"answer":"ア",
     "basis":"逆接 <span class='en'>however</span> と、直後の <span class='en'>hit by disease, pesticides, and the loss of wild flowers</span>（打撃の列挙）。"
             "<span class='en'>bee populations have ( ) sharply</span>。",
     "solve":"病気・農薬・花の喪失に打たれた結果＝個体数は<b>激減した</b>。"
             "<span class='en'>fallen sharply</span>（急減する）が一意。",
     "cut":"<span class='en'>grown</span>（増加）は逆向き。<span class='en'>survived / spread</span> は"
           "<span class='en'>sharply</span> や打撃の列挙と噛み合わない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Faced with this threat, growers are starting to act.",
       "Luckily, farmers have never needed bees at all.",
       "As a result, food prices have finally collapsed.",
       "The decline, however, has brought no consequences."],"answer":"ア",
     "basis":"空所前＝『病気や農薬でミツバチが激減している』という<b>問題</b>。"
             "空所後＝『農家は巣箱を大量に借り、畑の縁に花を植える』という<b>対策</b>。",
     "solve":"空所は<b>問題→対応</b>の橋渡し。直後の具体的な行動につなぐ『この脅威に直面し、生産者は動き始めている』が最適。",
     "cut":"『農家はミツバチを必要としてこなかった』は本文と逆、"
           "『食料価格が暴落した』は無関係、『減少に影響はない』は直後の対策と矛盾する。"},
  ],
  "trans": [
    ("文1", "何年もの間、運転手は電気自動車を買うのをためらってきた。理由はほぼいつも同じで、"
            "家から遠く離れた場所で電池が切れるのを恐れていたのだ。"
            "しばしば航続距離への不安と呼ばれるこの心配が、多くの買い手をガソリン車に<b>固執させて</b>いた。"
            "いま二つのことが彼らの考えを変えつつある。電池は安くなり、一度の充電でずっと遠くまで走れるようになった。"
            "そして急速充電器が主要な幹線道路沿いに<b>急増している</b>。"
            "<b>これらの進歩が相まって、長距離の移動の負担を大きく減らしている。</b>"
            "かつては綿密な計画を要した旅も、いまや車が充電する間にコーヒーを飲む短い休憩だけで行える。"
            "ネットワークが広がるにつれ、古い不安は静かに薄れつつある。"),
    ("文2", "私たちは食事を可能にしてくれる昆虫にめったに感謝しないが、彼らがいなければ多くの畑は静まり返ってしまうだろう。"
            "ミツバチは花から花へと花粉を運び、植物が私たちの食べる果実や種子を実らせるのを助ける。"
            "私たちの皿の食べ物のおよそ三分の一は、この静かな働きに<b>依存している</b>。"
            "しかし近年、ミツバチの個体数は急激に<b>減少し</b>、病気や農薬、野生の花の喪失に打撃を受けてきた。"
            "<b>この脅威に直面し、生産者は動き始めている。</b>"
            "今では、巣箱をトラック単位で借り、畑の縁に花の帯を植える農家もいる。"
            "ミツバチを守ることは慈善ではなく、良い商売なのだと彼らは学んだのだ。"),
  ],
  "vocab": [
    ("range anxiety", "名", "航続距離への不安"),
    ("charger", "名", "充電器"),
    ("highway", "名", "幹線道路、高速道路"),
    ("pollen", "名", "花粉"),
    ("pollination", "名", "受粉"),
    ("pesticide", "名", "殺虫剤、農薬"),
    ("hive", "名", "(ミツバチの)巣箱"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で決める――"
    "<span class='en'>loyal to / multiply / depend on / fall sharply</span> のように相方の前置詞や副詞と論理の矢印を確認する。"
    "文選択空所（43・46）は<b>前後の論理（原因→結果／問題→対応）</b>で一意化し、代入して音読で検証する。",
}
