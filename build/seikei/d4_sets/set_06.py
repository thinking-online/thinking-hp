# -*- coding: utf-8 -*-
"""大問Ⅳ SET 06 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=ジャストインタイムと在庫管理／文2=マイクロプラスチック。"""

SET = {
  "theme": "ジャストインタイム ＆ マイクロプラスチック",
  "genre": "ビジネス／科学・環境 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Just in Time", "wordcount": 101,
     "paras": [
        "Toyota made a simple idea famous: hold almost no spare stock. Under a just-in-time system, parts arrive at "
        "the factory exactly when workers need them, rather than weeks in advance. This approach sharply [[b:41]] the "
        "cost of storing goods and frees the cash that would otherwise sit idle on shelves. Yet the same efficiency "
        "makes the supply chain [[b:42]]. [[b:43]] When one supplier fails or a border closes, the line can stop "
        "within hours, because no buffer of extra parts is waiting to fill the gap. Managers must balance the savings "
        "of lean stock against the risk of shortage.",
     ]},
    {"label": "文2", "title": "The Plastic in the Sea", "wordcount": 102,
     "paras": [
        "Microplastics are tiny fragments, smaller than a grain of rice, that form when larger plastic items slowly "
        "break apart in sunlight and waves. Rivers carry them to the sea, where currents [[b:44]] them across every "
        "ocean. Fish and shellfish easily mistake these bright particles for food. Because larger animals then eat the "
        "smaller ones, the plastic steadily [[b:45]] up the food chain until it reaches the plates of people who love "
        "seafood. [[b:46]] Scientists are still measuring the effects on human health, yet many argue that the wisest "
        "response is to cut plastic waste at its source rather than clean the seas afterward.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["reduces","raises","ignores","delays"],"answer":"ア",
     "basis":"<span class='en'>This approach sharply ( ) the cost of storing goods and frees the cash ...</span>。"
             "『保管コストを〜し、寝ていた現金を解放する』と、コスト削減の効果を並べている。",
     "solve":"<span class='en'>frees the cash</span>（資金を解放）と等位で並ぶので、コストは<b>下がる</b>方向。"
             "<span class='en'>reduces the cost</span> のコロケが自然。",
     "cut":"<span class='en'>raises</span>（上げる）はコスト削減の文脈と逆。"
           "<span class='en'>ignores / delays</span> は <span class='en'>the cost</span> と噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["fragile","cheaper","larger","faster"],"answer":"ア",
     "basis":"<span class='en'>Yet the same efficiency makes the supply chain ( )</span>。"
             "<span class='en'>Yet</span> で利点から欠点へ転換し、直後に『供給者が一つ倒れると数時間で止まる』と弱さを説明。",
     "solve":"逆接＋『すぐ止まる』理由から、鎖は<b>脆い</b>＝<span class='en'>fragile</span>。",
     "cut":"<span class='en'>cheaper / faster</span> は利点であり <span class='en'>Yet</span> の転換に合わない。"
           "<span class='en'>larger</span> は後続の脆弱性の説明と無関係。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "A single disruption anywhere along the chain can bring production to a sudden halt.",
       "Extra stock is always the safest way to run a modern factory.",
       "Customers almost never notice when a delivery arrives late.",
       "Storing goods for many years is by far the cheapest option."],"answer":"ア",
     "basis":"空所前＝『供給網は脆い』（一般的な弱さ）。空所後＝<span class='en'>When one supplier fails ..., the line can stop within hours</span>（具体例）。",
     "solve":"空所は<b>一般化→具体例</b>の橋渡し。『鎖のどこか一箇所の混乱が生産を突然止めうる』が脆さを言い換え、次の具体例へ繋がる。",
     "cut":"『予備在庫が常に最も安全』『長年の保管が最も安い』はジャストインタイムの趣旨と逆。"
           "『客は遅配に気づかない』は『数時間で止まる』危機感と噛み合わない。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["spread","trap","absorb","melt"],"answer":"ア",
     "basis":"<span class='en'>currents ( ) them across every ocean</span>。海流が主語で <span class='en'>across every ocean</span> が続く。",
     "solve":"<span class='en'>spread ... across ...</span>＝『〜中に広げる』のコロケ。海流が破片を各地へ運び広げる。",
     "cut":"<span class='en'>trap</span>（閉じ込める）は <span class='en'>across every ocean</span> と逆。"
           "<span class='en'>absorb / melt</span> は海流が破片に対して行う動作として不自然。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["climbs","falls","stops","returns"],"answer":"ア",
     "basis":"<span class='en'>the plastic steadily ( ) up the food chain until it reaches the plates of people</span>。"
             "『大きな動物が小さな動物を食べる』ため、上へ移る流れ。",
     "solve":"<span class='en'>( ) up the food chain</span> は『食物連鎖を<b>上っていく</b>』＝<span class='en'>climbs up</span>。"
             "最後に人の皿へ届く方向と一致。",
     "cut":"<span class='en'>falls</span>（落ちる）は <span class='en'>up</span> や『人へ届く』と矛盾。"
           "<span class='en'>stops / returns</span> も上昇の流れに合わない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "In this way, the waste we throw away can return to our own tables.",
       "Fortunately, plastic breaks down completely once it enters the sea.",
       "Most fish are able to remove these particles without any harm.",
       "Cleaning the open ocean has already solved almost all of the problem."],"answer":"ア",
     "basis":"空所前＝『プラスチックは食物連鎖を上り人の皿へ届く』。空所後＝<span class='en'>Scientists are still measuring the effects on human health</span>（人への影響）。",
     "solve":"空所は<b>要点のまとめ</b>。『こうして捨てた廃棄物が自分の食卓に戻りうる』が前文を束ね、人体影響の話へ自然に接続。",
     "cut":"『海に入れば完全に分解』『魚が無害に除去』は本文の警告と逆。『外洋の清掃で解決済み』は最後の『源で減らすべき』と矛盾。"},
  ],
  "trans": [
    ("文1", "トヨタはある単純な考えを有名にした――予備の在庫をほとんど持たない、というものだ。ジャストインタイム方式では、"
            "部品は数週間前ではなく、作業員が必要とするまさにその時に工場へ届く。この方式は品物の保管費用を大きく<b>減らし</b>、"
            "さもなければ棚で遊んでいたはずの資金を解放する。だが同じ効率が供給網を<b>脆く</b>する。"
            "<b>鎖のどこか一箇所の混乱が、生産を突然止めてしまうことがある。</b>供給者が一社倒れたり国境が閉じたりすると、"
            "隙間を埋める予備部品の緩衝がないため、生産ラインは数時間で止まりうる。経営者は無駄のない在庫の節約と、"
            "品切れの危険とを天秤にかけねばならない。"),
    ("文2", "マイクロプラスチックは米粒より小さな断片で、大きなプラスチック製品が日光と波の中でゆっくり砕けてできる。"
            "河川がそれらを海へ運び、海流が全ての海へと<b>広げる</b>。魚や貝はこの色鮮やかな粒を食べ物と容易に取り違える。"
            "大きな動物が小さな動物を食べるため、プラスチックは着実に食物連鎖を<b>上っていき</b>、ついには海産物を好む人々の皿に達する。"
            "<b>こうして、私たちが捨てた廃棄物が自分たちの食卓へ戻ってきうるのだ。</b>科学者は人の健康への影響をなお測定中だが、"
            "最も賢明な対応は、後から海を掃除するのではなく発生源でプラスチック廃棄物を減らすことだと多くが主張する。"),
  ],
  "vocab": [
    ("spare", "形", "予備の、余分の"),
    ("idle", "形", "遊んでいる、使われていない"),
    ("buffer", "名", "緩衝、予備の蓄え"),
    ("lean", "形", "無駄のない、贅肉のない"),
    ("fragment", "名", "断片、かけら"),
    ("current", "名", "海流、流れ"),
    ("source", "名", "源、発生源"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋論理の向き</b>で、"
    "<span class='en'>Yet</span> のような転換語や <span class='en'>up / across</span> といった前置詞が決め手になる。"
    "文選択空所（43・46）は<b>一般化→具体例</b>や<b>要点のまとめ</b>の型で、代入して前後を音読し話が途切れない1文を選ぶ。",
}
