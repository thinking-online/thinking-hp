# -*- coding: utf-8 -*-
"""大問Ⅳ SET 11 ― 短文2本・空所6（語彙4＋文選択2）。
文1=Eスポーツの産業化（ビジネス／文化）／文2=睡眠不足と経済損失（社会／科学）。
本文タグ: [[b:N]]=空所(設問N)。各文3空所（語彙2＋文選択1）。"""

SET = {
  "theme": "Eスポーツの産業化 ＆ 睡眠不足と経済損失",
  "genre": "ビジネス・文化／社会・科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Gaming Grows Up", "wordcount": 91,
     "paras": [
        "Competitive video gaming, once a hobby played alone in bedrooms, has grown into a serious global industry. "
        "Millions of fans now [[b:41]] tournaments online and fill huge arenas to watch their favourite teams. "
        "The best players sign contracts as valuable as those of traditional athletes, and money pours in through "
        "sponsorship from major brands, ticket sales, and broadcasting rights. "
        "[[b:42]] the sums involved, the sport still struggles for respect from older generations. [[b:43]] "
        "For millions of young people, however, a skilled gamer is every bit as admirable as a champion runner.",
     ]},
    {"label": "文2", "title": "The Price of Lost Sleep", "wordcount": 92,
     "paras": [
        "Sleep is often treated as wasted time, something to cut when work piles up. "
        "Yet a tired brain [[b:44]] slowly: attention drifts, memory weakens, and simple mistakes multiply. "
        "The danger is that none of this feels serious at the individual level. "
        "Across a whole nation, these small failures [[b:45]] into an enormous cost. "
        "Studies estimate that lost productivity, accidents, and health problems drain billions from major economies every year. "
        "[[b:46]] "
        "The lesson for both workers and companies is clear: protecting sleep is not laziness but a sound investment "
        "in performance and safety.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["follow","ignore","ban","host"],"answer":"ア",
     "basis":"<span class='en'>Millions of fans now ( ) tournaments online and fill huge arenas</span>。"
             "『何百万というファンが〜し、大会場を埋める』。",
     "solve":"熱心なファンの行動＋<span class='en'>online</span> から、大会を<b>追いかける＝観戦し追う</b>＝<span class='en'>follow</span>。",
     "cut":"<span class='en'>ignore</span>（無視する）はファンの態度と逆。<span class='en'>ban / host</span>（禁止・主催）は主語のファンと噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語句を選べ。","inline":True,
     "choices":["Despite","Because of","Instead of","Thanks to"],"answer":"ア",
     "basis":"<span class='en'>( ) the sums involved, the sport still struggles for respect</span>。"
             "『関わる金額〜、それでも尊敬を得るのに苦労する』と、大金と評価の低さが対立。",
     "solve":"前後が<b>逆接</b>（大金あり ⇔ 尊敬されず）なので<span class='en'>Despite</span>（〜にもかかわらず）。",
     "cut":"<span class='en'>Because of / Thanks to</span>（〜のおかげで）は順接で矛盾。<span class='en'>Instead of</span>（〜の代わりに）も論理が合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "Critics still ask whether sitting at a screen can really count as sport.",
       "Clearly, the industry has already won over every possible audience.",
       "As a result, major sponsors have begun to abandon the games.",
       "Most professionals retire wealthy before the age of twenty."],"answer":"ア",
     "basis":"空所前＝『それでも年配世代からの尊敬を得にくい』。空所後＝<span class='en'>For millions of young people, however, ...</span>（だが若者にとっては称賛に値する）。",
     "solve":"空所は年配世代の懐疑を具体化し、直後の <span class='en'>however</span> で若者と対比させる。『画面に座るのが本当にスポーツかと批判者は問う』が接続。",
     "cut":"『あらゆる観客を既に獲得』は苦労の記述と矛盾。『スポンサーが撤退』は資金が流入する記述と矛盾。『20歳前に富んで引退』は話の流れから逸れる。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["functions","recovers","celebrates","expands"],"answer":"ア",
     "basis":"<span class='en'>a tired brain ( ) slowly: attention drifts, memory weakens, and simple mistakes multiply</span>。"
             "コロン以下は能力低下の列挙。",
     "solve":"『疲れた脳は〜遅く<b>働く</b>』＝<span class='en'>functions</span>。直後の『注意が散り、記憶が弱る』と整合。",
     "cut":"<span class='en'>recovers</span>（回復する）は改善方向で、続く低下の列挙と逆。<span class='en'>celebrates / expands</span> は文意に合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["snowball","settle","fade","split"],"answer":"ア",
     "basis":"<span class='en'>Across a whole nation, these small failures ( ) into an enormous cost</span>。"
             "『国全体では、この小さな失敗が巨大な損失に〜』。",
     "solve":"小さな失敗が積み重なって膨らむ流れから、<span class='en'>snowball into</span>（雪だるま式に<b>膨れ上がる</b>）。次文の <span class='en'>billions</span> とも整合。",
     "cut":"<span class='en'>settle / fade / split</span>（収まる・薄れる・分裂する）は増大の向きと逆、または文脈に合わない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "In other words, a sleepless society quietly pays a huge bill.",
       "Even so, most experts say that sleep has no economic value.",
       "Luckily, machines now handle every dangerous night shift.",
       "By contrast, well-rested workers cause the most accidents."],"answer":"ア",
     "basis":"空所前＝『失われた生産性・事故・健康問題が毎年数十億を奪う』という数字。空所後＝<span class='en'>The lesson ... is clear</span>（教訓は明確だ）とまとめへ入る。",
     "solve":"空所は<b>データ→要約</b>の橋渡し。『言い換えれば、眠らない社会は静かに巨額の請求を払っている』が数字を束ね、直後の結論に繋がる。",
     "cut":"『睡眠に経済的価値はない』は数字と矛盾。『機械が夜勤を担う』は無関係。『休んだ労働者が最も事故を起こす』は論理が逆。"},
  ],
  "trans": [
    ("文1", "かつては寝室で一人遊ぶ趣味だった競技型ビデオゲームは、いまや本格的な世界産業へと成長した。"
            "何百万というファンがオンラインで大会を<b>追いかけ</b>、巨大な会場を埋めてお気に入りのチームを観戦する。"
            "トップ選手は従来のアスリートに劣らぬ価値の契約を結び、大手ブランドの協賛、チケット収入、放映権を通じて資金が流れ込む。"
            "<b>関わる金額にもかかわらず</b>、この競技は年配世代からの尊敬を得るのにいまだ苦労している。"
            "<b>画面の前に座ることが本当にスポーツと言えるのかと、批判する人はなお問う。</b>"
            "だが何百万もの若者にとって、熟練したゲーマーは優勝ランナーに勝るとも劣らず称賛に値するのだ。"),
    ("文2", "睡眠はしばしば無駄な時間とみなされ、仕事が積み上がると削られるものとされる。だが疲れた脳は<b>働く</b>のが遅くなる。"
            "注意が散り、記憶が弱り、単純なミスが増える。厄介なのは、個人の水準ではどれも深刻に感じられないことだ。"
            "国全体で見れば、こうした小さな失敗が巨大な損失へと<b>雪だるま式に膨れ上がる</b>。"
            "失われた生産性、事故、健康問題が主要国の経済から毎年数十億を奪う、と研究は見積もっている。"
            "<b>言い換えれば、眠らない社会は静かに巨額の請求を払っているのだ。</b>"
            "労働者にとっても企業にとっても教訓は明確だ。睡眠を守ることは怠惰ではなく、成果と安全への健全な投資なのである。"),
  ],
  "vocab": [
    ("sponsorship", "名", "協賛、スポンサー契約"),
    ("arena", "名", "競技場、アリーナ"),
    ("admirable", "形", "称賛に値する、立派な"),
    ("multiply", "動", "増える、増加する"),
    ("productivity", "名", "生産性"),
    ("snowball", "動", "雪だるま式に増える"),
    ("sound", "形", "健全な、堅実な"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（逆接での対比／データ→要約）</b>で一意に決まる。"
    "特に <span class='en'>Despite</span> のような逆接語は、前後が対立しているかを必ず代入確認する。",
}
