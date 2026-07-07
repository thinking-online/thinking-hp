# -*- coding: utf-8 -*-
"""大問Ⅳ SET 15 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=再生可能エネルギーとコスト／文2=チーズと発酵の科学。"""

SET = {
  "theme": "再生可能エネルギーとコスト ＆ チーズと発酵の科学",
  "genre": "科学・ビジネス／文化・科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The Falling Price of Clean Power", "wordcount": 97,
     "paras": [
        "A decade ago, electricity from solar and wind was costly, and critics dismissed it as a luxury "
        "for rich nations. Since then, that argument has largely [[b:41]]. "
        "The cost of solar panels has fallen so sharply that, in many regions, new renewable plants are "
        "now cheaper to build than coal ones. [[b:43]] "
        "The remaining challenge is not price but timing, since the sun sets each evening and the wind sometimes drops. "
        "To keep supply steady, engineers are racing to expand batteries and build smarter [[b:42]] "
        "that can store power and move it to where it is needed.",
     ]},
    {"label": "文2", "title": "The Science Inside a Cheese", "wordcount": 98,
     "paras": [
        "Cheese may look simple, but every wheel is the product of careful [[b:44]]. "
        "Thousands of years ago, people stored fresh milk in bags made from animal stomachs, whose natural "
        "enzymes made the liquid separate into solid curds and watery whey. [[b:46]] "
        "By adding particular bacteria and moulds, and by ageing the curds in cool caves for months, "
        "cheesemakers slowly learned to create hundreds of distinct flavours. "
        "The sharp bite of a blue cheese, for instance, comes from a living mould that would [[b:45]] "
        "most other foods. What looks like simple decay is, in skilled hands, a delicious transformation.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["collapsed","survived","spread","tightened"],"answer":"ア",
     "basis":"直前 <span class='en'>that argument has largely ( )</span>。直後で『太陽光の価格が急落し、再エネの方が石炭より安い』と<b>主張が成り立たなくなった</b>理由が続く。",
     "solve":"『高くて金持ち国の贅沢だ』という主張が、価格急落で崩れた。<span class='en'>the argument has collapsed</span>（崩れ去った）が文脈と一致。",
     "cut":"<span class='en'>survived</span>（生き残った）は続く反証と逆。<span class='en'>spread</span>（広まった）・<span class='en'>tightened</span>（引き締まった）は主張の消長として不自然。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["grids","gardens","habits","songs"],"answer":"ア",
     "basis":"<span class='en'>expand batteries and build smarter ( ) that can store power and move it to where it is needed</span>。電力を蓄え・必要な場所へ送る対象。",
     "solve":"電力を『蓄え、送る』のは送電網。<span class='en'>smarter grids</span>（賢い送電網＝スマートグリッド）が電力・供給の文脈と一致。",
     "cut":"<span class='en'>gardens</span>（庭）・<span class='en'>habits</span>（習慣）・<span class='en'>songs</span>（歌）は電力を蓄え送る主体になりえない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "In short, cost is no longer the main obstacle to clean power.",
       "For this reason, coal still remains the cheapest option worldwide.",
       "Sunlight, however, can never really be turned into electricity.",
       "Only the richest nations can afford such expensive technology."],"answer":"ア",
     "basis":"空所前＝『再エネは石炭より安く建設できる』という価格の話。空所後＝<span class='en'>The remaining challenge is not price but timing</span>（課題は価格ではなくタイミング）。",
     "solve":"空所は<b>価格の議論のまとめ→次の論点</b>への橋渡し。『もはやコストが主な障害ではない』が入り、直後の『課題は価格ではなく…』と一貫する。",
     "cut":"『石炭が最安』は直前と矛盾。『太陽光は電気にならない』は事実と逆。『最富裕国しか手が出ない』は『石炭より安い』と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["fermentation","painting","weather","silence"],"answer":"ア",
     "basis":"<span class='en'>every wheel is the product of careful ( )</span>。直後で酵素・細菌・カビが牛乳を変える過程が具体的に説明される。",
     "solve":"酵素や細菌・カビが牛乳を変える＝<b>発酵</b>。<span class='en'>the product of careful fermentation</span> が続く説明と一致。",
     "cut":"<span class='en'>painting</span>（絵画）・<span class='en'>weather</span>（天気）・<span class='en'>silence</span>（静けさ）は牛乳が固形に変わる過程を表さない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["spoil","protect","sweeten","freeze"],"answer":"ア",
     "basis":"<span class='en'>a living mould that would ( ) most other foods</span>。直後 <span class='en'>What looks like simple decay</span>（腐敗のように見えるもの）と対比。",
     "solve":"青カビは他の食品なら<b>だめにする</b>生きたカビ。<span class='en'>would spoil most other foods</span> が『腐敗のように見えるが実は美味な変化』という対比を成立させる。",
     "cut":"<span class='en'>protect</span>（守る）・<span class='en'>sweeten</span>（甘くする）・<span class='en'>freeze</span>（凍らせる）は <span class='en'>decay</span> との対比を壊す。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "This happy accident was only the beginning of the story.",
       "Unfortunately, the result was always far too poisonous to eat.",
       "Milk, however, can never change its form once it is stored.",
       "Modern factories abandoned these slow methods long ago."],"answer":"ア",
     "basis":"空所前＝『古代人が偶然、胃袋の酵素で牛乳が固形と液体に分離した』。空所後＝『細菌やカビを加え熟成させ数百の味を作った』という<b>人の手による発展</b>。",
     "solve":"空所は<b>偶然の発見→人為的な改良</b>の橋渡し。『この幸運な偶然は始まりにすぎなかった』が入り、直後の技術的発展を導く。",
     "cut":"『いつも有毒だった』はチーズ作りの発展と矛盾。『牛乳は形を変えられない』は分離の描写と矛盾。『現代の工場は捨てた』は続く伝統技術の話とつながらない。"},
  ],
  "trans": [
    ("文1", "10年前、太陽光や風力による電気は高価で、批評家はそれを富裕国のための贅沢だと切り捨てていた。だがそれ以来、"
            "その主張はおおむね<b>崩れ去った</b>。太陽光パネルの費用が急激に下がり、多くの地域では新しい再生可能エネルギーの"
            "発電所の方が石炭発電所より建設費が安くなっている。<b>要するに、もはやコストがクリーンな電力の主な障害ではない。</b>"
            "残る課題は価格ではなくタイミングだ。太陽は毎晩沈み、風はときに止むからである。供給を安定させるため、技術者たちは"
            "蓄電池を増やし、電力を蓄えて必要な場所へ送れる、より賢い<b>送電網</b>を築こうと急いでいる。"),
    ("文2", "チーズは単純に見えるが、その一つ一つは丹念な<b>発酵</b>の産物だ。何千年も前、人々は動物の胃袋で作った袋に新鮮な"
            "牛乳を蓄えており、その天然の酵素が液体を固形のカードと水っぽいホエーに分離させた。<b>この幸運な偶然は、物語の始まりに"
            "すぎなかった。</b>特定の細菌やカビを加え、涼しい洞窟で数か月間カードを熟成させることで、チーズ職人たちは徐々に数百もの"
            "異なる風味を生み出すことを学んだ。たとえばブルーチーズの鋭い味は、他のたいていの食品なら<b>だめにしてしまう</b>"
            "生きたカビから生まれる。腐敗のように見えるものが、熟練の手にかかれば美味な変化になるのだ。"),
  ],
  "vocab": [
    ("dismiss", "動", "切り捨てる、一蹴する"),
    ("renewable", "形", "再生可能な"),
    ("grid", "名", "送電網、電力網"),
    ("fermentation", "名", "発酵"),
    ("enzyme", "名", "酵素"),
    ("spoil", "動", "だめにする、腐らせる"),
    ("decay", "名", "腐敗、腐朽"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（主張の否定→次の論点／偶然の発見→人為的改良）</b>で一意に決まる。"
    "文選択は代入して前後を音読し、話が途切れない1文を選ぶ。",
}
