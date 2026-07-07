# -*- coding: utf-8 -*-
"""大問Ⅳ SET 09 ― 短文2本・空所6（語彙4＋文選択2）。
文1=クラウドファンディング（ビジネス）、文2=紅茶の歴史と交易（文化／歴史）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "クラウドファンディング ＆ 紅茶の歴史と交易",
  "genre": "ビジネス／文化・歴史 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Funded by the Crowd", "wordcount": 100,
     "paras": [
        "Not long ago, a new company needed a bank or a wealthy investor to get started. "
        "Crowdfunding has changed that. Through a website, a founder can [[b:41]] small amounts of money "
        "from thousands of ordinary people at once. In return, these backers are often promised an early product or a special reward. "
        "[[b:43]] If enough people believe in the idea, the project reaches its target and production begins. "
        "If not, the money is returned and nothing is [[b:42]]. "
        "For many small startups, the crowd has become both a first customer and a first source of funding.",
     ]},
    {"label": "文2", "title": "The Long Road of Tea", "wordcount": 100,
     "paras": [
        "For centuries, tea was grown almost only in China. Merchants carried the dried leaves along dusty roads "
        "and later by sea, and the drink slowly [[b:44]] across Asia and beyond. "
        "By the 1700s, tea had reached Europe, where it quickly became a fashionable and costly luxury. "
        "[[b:46]] Ships raced home from distant ports, and whole fortunes were built on the trade. "
        "To break China's [[b:45]] on supply, the British later planted tea in India. "
        "Today the humble cup on your table carries a long history of travel, money, and power.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["raise","borrow","waste","hide"],"answer":"ア",
     "basis":"<span class='en'>a founder can ( ) small amounts of money from thousands of ordinary people</span>。"
             "多数の人から資金を集める仕組みの説明。",
     "solve":"<span class='en'>( ) money from people</span>＝『資金を<b>集める</b>』＝<span class='en'>raise money</span> のコロケ。",
     "cut":"<span class='en'>borrow</span> は返済を含意するが本文の返礼は貸借ではない。"
            "<span class='en'>waste / hide</span> は資金調達の文脈と正反対・無関係。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["lost","saved","earned","counted"],"answer":"ア",
     "basis":"<span class='en'>If not, the money is returned and nothing is ( )</span>。"
             "目標未達なら『お金は返される』が前提。",
     "solve":"返金されるのだから、出資者は何も<b>失わ</b>ない＝<span class='en'>nothing is lost</span>。",
     "cut":"<span class='en'>saved / earned / counted</span> は『返金＝損失なし』という論理と噛み合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "Most campaigns set a clear goal and a fixed deadline.",
       "Banks still control almost every step of the whole process.",
       "Such rewards are usually worth more than the product itself.",
       "Investors alone decide whether the project will succeed."],"answer":"ア",
     "basis":"空所前＝『支援者は製品や返礼を約束される』。"
             "空所後＝<span class='en'>If enough people believe ..., the project reaches its target</span>。",
     "solve":"直後の <span class='en'>reaches its target</span> と呼応。ゆえに『目標と締め切りを設ける』が橋渡しになる。",
     "cut":"『銀行が全工程を握る』『投資家だけが成否を決める』は群衆による資金調達という趣旨と矛盾。"
            "『返礼は製品より価値がある』は話題がずれ、直後の目標達成の話につながらない。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["spread","vanished","froze","fell"],"answer":"ア",
     "basis":"<span class='en'>the drink slowly ( ) across Asia and beyond</span>。"
             "商人が茶葉を各地へ運んだ結果。",
     "solve":"<span class='en'>( ) across ... and beyond</span>＝『各地へ<b>広がった</b>』＝<span class='en'>spread</span>。",
     "cut":"<span class='en'>vanished</span>（消えた）は普及の流れと逆。"
            "<span class='en'>froze / fell</span> は <span class='en'>across Asia</span> と結びつかない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["monopoly","promise","shortage","habit"],"answer":"ア",
     "basis":"<span class='en'>To break China's ( ) on supply, the British later planted tea in India</span>。"
             "供給を握る中国の状態を『打ち破る』ための行動。",
     "solve":"<span class='en'>break a monopoly on supply</span>＝『供給の<b>独占</b>を崩す』。インドでの栽培はその手段。",
     "cut":"<span class='en'>promise / shortage / habit</span> は <span class='en'>break ... on supply</span> の目的語として成立しない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Demand grew so fast that the tea trade became hugely profitable.",
       "Few Europeans could stand the bitter taste of the leaves.",
       "As a result, tea was soon forgotten across the West.",
       "China happily shared its growing methods with everyone."],"answer":"ア",
     "basis":"空所前＝『茶は流行の高価なぜいたく品になった』。"
             "空所後＝<span class='en'>Ships raced home ..., and whole fortunes were built on the trade</span>。",
     "solve":"『ぜいたく品→高需要→儲かる交易→船が競い財産が築かれる』の流れ。『需要が急伸し交易が非常に儲かった』が接続。",
     "cut":"『苦い味に耐えられない』は流行品という記述と矛盾。『すぐ忘れられた』は財産が築かれた記述と矛盾。"
            "『中国が栽培法を共有した』は後の『独占を崩す』と矛盾する。"},
  ],
  "trans": [
    ("文1", "少し前まで、新しい会社を始めるには銀行か裕福な投資家が必要だった。クラウドファンディングがそれを変えた。"
            "ウェブサイトを通じて、創業者は一度に何千もの普通の人々から少額のお金を<b>集める</b>ことができる。"
            "見返りとして、こうした支援者はしばしば初期の製品や特別な返礼を約束される。"
            "<b>たいていの企画は明確な目標と定められた締め切りを設ける。</b>十分な人がそのアイデアを信じれば、"
            "企画は目標に達し、生産が始まる。そうでなければ、お金は返され、何も<b>失われ</b>ない。"
            "多くの小さな新興企業にとって、群衆は最初の顧客であると同時に最初の資金源にもなっている。"),
    ("文2", "何世紀もの間、茶はほぼ中国でのみ栽培されていた。商人たちは乾いた茶葉を埃っぽい道沿いに、"
            "後には海路で運び、その飲み物は少しずつアジア全域とその先へと<b>広がった</b>。"
            "1700年代までに茶はヨーロッパに達し、そこでたちまち流行の高価なぜいたく品となった。"
            "<b>需要が急速に高まり、紅茶の交易は非常に儲かるものとなった。</b>船は遠い港から先を競って帰り、"
            "莫大な財産がこの交易の上に築かれた。供給に対する中国の<b>独占</b>を打ち破るため、"
            "イギリスは後にインドで茶を栽培した。今日、あなたの食卓の慎ましいカップは、旅と金と権力の長い歴史を運んでいる。"),
  ],
  "vocab": [
    ("investor", "名", "投資家"),
    ("founder", "名", "創業者"),
    ("backer", "名", "支援者、出資者"),
    ("deadline", "名", "締め切り、期限"),
    ("luxury", "名", "ぜいたく品"),
    ("monopoly", "名", "独占"),
    ("fortune", "名", "財産、大金"),
  ],
  "lesson":
    "語彙空所（41・42・44・45）は<b>動詞と目的語のコロケ</b>（<span class='en'>raise money / break a monopoly</span>）と"
    "文脈の向きで、文選択空所（43・46）は<b>直後の語との呼応</b>で決まる。"
    "43は次文の <span class='en'>reaches its target</span>、46は次文の <span class='en'>Ships raced ... fortunes</span> が決め手。"
    "候補を代入し、話が途切れないかを自己検証する。",
}
