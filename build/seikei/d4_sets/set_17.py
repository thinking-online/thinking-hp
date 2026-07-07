# -*- coding: utf-8 -*-
"""大問Ⅳ SET 17 ― 短文2本・空所6（語彙4＋文選択2）。
文1=顧客ロイヤルティとポイント制度（ビジネス）／文2=パンと発酵の歴史（文化・歴史）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "顧客ロイヤルティとポイント制度 ＆ パンと発酵の歴史",
  "genre": "ビジネス／文化・歴史 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The Points Behind Loyalty", "wordcount": 98,
     "paras": [
        "Retailers have long searched for ways to keep shoppers coming back. "
        "One of the most popular tools is the loyalty programme, which rewards repeat buyers with points "
        "that can later be [[b:41]] for discounts or gifts. The logic is simple: a customer who has collected points "
        "feels a small [[b:42]] to return to the same shop rather than a rival. [[b:43]] "
        "A well-designed scheme also gathers valuable data, telling the company exactly what each member likes to buy. "
        "Yet if the rewards feel cheap or the rules grow confusing, the same programme can quietly push loyal customers away.",
     ]},
    {"label": "文2", "title": "How Bread Learned to Rise", "wordcount": 102,
     "paras": [
        "Bread is one of the oldest prepared foods, yet for thousands of years it was flat and hard. "
        "The great change came when bakers discovered [[b:44]]. Wild yeast, floating in the air or living on grain, "
        "feeds on the sugars in dough and gives off tiny bubbles of gas. "
        "Trapped inside the sticky mixture, these bubbles make the loaf rise and turn [[b:45]]. [[b:46]] "
        "Ancient Egyptian bakers were probably the first to master it, leaving behind ovens and paintings that show rows of rising loaves. "
        "From that accidental discovery grew a craft that still shapes kitchens around the world today.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["redeemed","refused","forgotten","doubled"],"answer":"ア",
     "basis":"直前 <span class='en'>points that can later be ( ) for discounts or gifts</span>。"
             "『後で割引や景品と〜できるポイント』。",
     "solve":"<span class='en'>( ) points for ...</span> のコロケーション。ポイントを景品と<b>交換する</b>＝<span class='en'>redeem</span>。",
     "cut":"<span class='en'>refused</span>（拒否）・<span class='en'>forgotten</span>（忘れる）はポイント制度の利点と逆。"
            "<span class='en'>doubled</span>（倍にする）は <span class='en'>for discounts or gifts</span> と噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["incentive","refund","warning","delay"],"answer":"ア",
     "basis":"<span class='en'>a customer who has collected points feels a small ( ) to return to the same shop rather than a rival</span>。"
             "ポイントを貯めた客が感じるもの。",
     "solve":"<span class='en'>a small ( ) to return</span>＝『戻ろうという小さな<b>動機</b>』＝<span class='en'>incentive</span>。<span class='en'>incentive to do</span> のコロケ。",
     "cut":"<span class='en'>refund</span>（払い戻し）・<span class='en'>warning</span>（警告）・<span class='en'>delay</span>（遅延）は『戻る動機』という文脈に合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "In this way an ordinary purchase becomes the start of a lasting habit.",
       "For that reason most shops have now abandoned such rewards.",
       "Points, however, are worth nothing to the average shopper.",
       "Rival stores are usually unable to copy the idea at all."],"answer":"ア",
     "basis":"空所前＝『ポイントが同じ店へ戻る動機になる』。空所後＝<span class='en'>A well-designed scheme also gathers valuable data ...</span>（データも集める、という第二の利点）。",
     "solve":"直後の <span class='en'>also</span> が『もう一つの利点』を示す合図。空所には第一の効果のまとめ『ありふれた買い物が習慣の始まりになる』が入り、そこに『データも集める』が加わる。",
     "cut":"『店が報酬をやめた』は人気という前提と逆。『ポイントは無価値』も本文と逆。『競合は真似できない』は根拠がなく <span class='en'>also</span> の流れに合わない。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["fermentation","refrigeration","printing","gravity"],"answer":"ア",
     "basis":"<span class='en'>The great change came when bakers discovered ( )</span>。直後で『野生の酵母が糖を食べ気泡を出す』と説明。",
     "solve":"酵母が糖を分解しガスを出す働き＝<b>発酵</b>＝<span class='en'>fermentation</span>。次文の <span class='en'>yeast / bubbles of gas</span> が定義になっている。",
     "cut":"<span class='en'>refrigeration</span>（冷蔵）・<span class='en'>printing</span>（印刷）・<span class='en'>gravity</span>（重力）は酵母の説明とつながらない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["light","heavy","sour","cold"],"answer":"ア",
     "basis":"<span class='en'>these bubbles make the loaf rise and turn ( )</span>。気泡が『パンを膨らませ〜にする』。冒頭は <span class='en'>flat and hard</span>（平たく硬い）。",
     "solve":"<span class='en'>rise</span>（膨らむ）と並ぶ変化。気泡で空気を含み<b>軽く</b>なる＝<span class='en'>light</span>。冒頭の <span class='en'>hard</span> との対比。",
     "cut":"<span class='en'>heavy</span>（重い）・<span class='en'>cold</span>（冷たい）は <span class='en'>rise</span> と逆や無関係。<span class='en'>sour</span>（酸っぱい）は食感の話でずれる。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "No one had planned this process; it was surely found by accident.",
       "Because of this, bread quickly became a food only for the rich.",
       "Modern bakers have since replaced yeast with cheaper chemicals.",
       "Such loaves were, in fact, even harder than the older ones."],"answer":"ア",
     "basis":"空所前＝『気泡がパンを膨らませ軽くする』。空所後＝<span class='en'>Ancient Egyptian bakers were probably the first to master it ...</span>。"
             "末尾は <span class='en'>that accidental discovery</span>（その偶然の発見）。",
     "solve":"末尾の <span class='en'>accidental</span> と、直後の <span class='en'>master it</span>（それを使いこなす）を橋渡しする文が必要。"
             "『誰も計画せず、偶然見つかった』を入れると <span class='en'>it</span> がこの過程を受ける。",
     "cut":"『金持ちだけの食べ物』は話題がそれる。『安い化学物質に置換』は末尾の craft（受け継がれた技術）と逆。"
            "『前より硬かった』は『膨らんで軽くなる』と矛盾。"},
  ],
  "trans": [
    ("文1", "小売業者は長らく、買い物客に再び来てもらう方法を探し続けてきた。最も人気のある手段の一つがロイヤルティ・プログラムで、"
            "これは常連客に、後で割引や景品と<b>交換できる</b>ポイントを与えて報いる。理屈は単純だ。ポイントを貯めた客は、"
            "競合ではなく同じ店に戻ろうという小さな<b>動機</b>を感じる。<b>こうして、ありふれた買い物が長く続く習慣の始まりになる。</b>"
            "よく設計された仕組みは貴重なデータも集め、各会員が何を買うのが好きかを会社に正確に教えてくれる。だが、報酬が安っぽく感じられたり"
            "規則が複雑になったりすれば、同じプログラムが忠実な客を静かに遠ざけることもある。"),
    ("文2", "パンは最も古い調理食品の一つだが、何千年もの間、平たく硬いものだった。大きな変化は、パン職人が<b>発酵</b>を発見したときに訪れた。"
            "空気中を漂い、あるいは穀物に住む野生の酵母は、生地の中の糖を食べ、小さな気泡のガスを出す。粘り気のある生地の中に閉じ込められた"
            "これらの気泡が、パンを膨らませ<b>軽く</b>する。<b>この過程を計画した者は誰もおらず、それはきっと偶然に見つかったのだ。</b>"
            "古代エジプトのパン職人がおそらく最初にそれを使いこなし、膨らむパンが並ぶ様子を示す窯や絵画を残した。その偶然の発見から、"
            "今日なお世界中の台所を形づくる技術が育ったのだ。"),
  ],
  "vocab": [
    ("loyalty programme", "名", "ロイヤルティ制度、会員特典制度"),
    ("redeem", "動", "(ポイントを)交換する、換金する"),
    ("incentive", "名", "動機、誘因"),
    ("rival", "名", "競合相手"),
    ("yeast", "名", "酵母、イースト"),
    ("fermentation", "名", "発酵"),
    ("loaf", "名", "(パンの)一塊"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（効果のまとめ→追加／過程→その由来）</b>で一意に決まる。"
    "文選択は <span class='en'>also</span> や指示語 <span class='en'>it / this</span> が正しく受かるかを代入して確かめる。",
}
