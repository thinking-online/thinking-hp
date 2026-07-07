# -*- coding: utf-8 -*-
"""大問Ⅲ READING 05 ― 価格の心理学（behavioral pricing）。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "価格の心理学 ― 見せ方が支払意思を変える",
  "genre": "ビジネス／行動経済学 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 440,
  "passage_title": "The Price We Are Willing to Pay",
  "passage": [
    "A price is more than a number printed on a tag. It is a signal that our minds read, compare, and interpret before we "
    "decide to buy. Researchers in behavioral pricing have found that the very same product can feel cheap or expensive "
    "depending on how [[u:32]]it[[/u]] is presented. What we are willing to pay, in other words, is shaped far less by the "
    "object itself than by the mental frame that surrounds it.",

    "One of the most studied of these effects is anchoring. When shoppers see a high number first, that figure becomes a "
    "reference point, and every later price seems small beside it. A watch marked down from a large original price feels "
    "like a bargain, even when the seller never expected to sell it at the higher figure. The first number quietly [[u:33]]sets[[/u]] "
    "the stage, and the rest of the decision unfolds around it.",

    "A related trick is the decoy. Suppose a shop offers a small coffee and a large one, and few people choose the large. "
    "If the seller adds a medium option priced just below the large, the large suddenly looks generous by comparison, and "
    "sales of it climb. The medium was never meant to sell; it exists only to make its neighbor [[u:34]]appealing[[/u]]. In this "
    "way, sellers can steer demand toward the option they most wish to move.",

    "Companies defend these methods as ordinary and even useful. Prices, they argue, must be communicated somehow, and a "
    "well-designed menu simply helps buyers judge value quickly in a crowded market. Critics see [[u:35]]the matter[[/u]] differently. "
    "To them, engineering the frame around a price is a form of manipulation that exploits predictable weaknesses in human "
    "judgment, nudging people to spend more than they truly intend.",

    "The dispute is not easily settled, because the line between guiding a choice and distorting it is genuinely blurry. A "
    "reference price that reflects real quality informs the buyer and helps a fair decision; one invented purely to mislead "
    "does not, and it quietly turns a helpful signal into a trap. Much depends on whether the perceived value a customer "
    "feels corresponds to anything the product actually delivers, rather than to a clever arrangement of numbers alone.",

    "What seems clear is that pricing is never neutral, and firms cannot pretend otherwise. Every menu and every discount "
    "already guides the eye somehow. Yet the power to shape perception carries a long-term risk. Buyers who later feel "
    "tricked rarely return, and trust, once spent, is hard to earn back. The cleverest pricing may win a single sale, but "
    "the businesses that last are usually those whose numbers a customer can believe.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (how it is presented) refer to?","inline":True,
     "choices":["the same product","the price tag","the mind","the researcher"],"answer":"ア",
     "basis":"<span class='en'>the very same product can feel cheap or expensive depending on how it is presented</span> の <span class='en'>it</span> は直前の <span class='en'>the very same product</span>。",
     "solve":"代名詞は直前の名詞へ。『それがどう見せられるか』の『それ』＝同じ商品。",
     "cut":"<span class='en'>the price tag</span> は第1文の話題だが、この <span class='en'>it</span> が指すのは提示される『商品』の方。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“sets”</span> in paragraph 2 (sets the stage) is closest in meaning to","inline":True,
     "choices":["prepares","cancels","hides","lowers"],"answer":"ア",
     "basis":"<span class='en'>sets the stage</span>＝「お膳立てをする、下地を整える」。最初の数字が後の判断の枠を用意する。",
     "solve":"<span class='en'>set the stage</span> は成句で『準備を整える』。<span class='en'>prepares</span> が同義。",
     "cut":"<span class='en'>cancels</span>（取り消す）は逆で、アンカーは判断を消さず方向づける。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“appealing”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["attractive","expensive","useless","confusing"],"answer":"ア",
     "basis":"<span class='en'>make its neighbor appealing</span>＝隣の選択肢を『魅力的に』見せる。",
     "solve":"おとりは本命を良く見せるためのもの＝魅力的。<span class='en'>attractive</span> が同義。",
     "cut":"<span class='en'>expensive</span>（高価な）は魅力とは別の概念で、本文の狙いと合わない。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“the matter”</span> in paragraph 4 refer to?","inline":True,
     "choices":["the use of framing techniques in pricing","a shortage of coffee sizes","the printing of price tags","a rise in production costs"],"answer":"ア",
     "basis":"第4段の <span class='en'>the matter</span>＝企業が擁護する<b>価格の見せ方（フレーミング）の手法</b>そのもの。批判者はそれを別様に見る。",
     "solve":"<span class='en'>the ＋ 名詞</span>は前の話題を受ける。ここは価格設計の手法をめぐる問題。",
     "cut":"<span class='en'>a shortage of coffee sizes</span> はおとり例の小道具にすぎず、論点ではない。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, how does anchoring affect shoppers?",
     "choices":[
       "A high number seen first makes later prices seem small.",
       "Shoppers ignore the first price they see.",
       "The lowest price always becomes the reference point.",
       "Buyers refuse to purchase discounted items."],"answer":"ア",
     "basis":"第2段 <span class='en'>When shoppers see a high number first ... every later price seems small beside it</span> に一致。",
     "solve":"設問のキーワード（anchoring / first number）を第2段で照合。",
     "cut":"『最初の価格を無視する』は、最初の数字が参照点になるという説明と正反対。"},
    {"no":37,"tag":"詳細","stem":"According to paragraph 3, why does a seller add a medium coffee option?",
     "choices":[
       "To make the large size look more generous and boost its sales.",
       "To sell as many medium coffees as possible.",
       "To lower the price of the small coffee.",
       "To reduce the number of choices for buyers."],"answer":"ア",
     "basis":"第3段 <span class='en'>the large suddenly looks generous by comparison, and sales of it climb</span> / <span class='en'>The medium was never meant to sell</span>。",
     "solve":"おとり（decoy）の目的＝本命を良く見せて売る。中サイズ自体は売る気がない。",
     "cut":"『中サイズをできるだけ多く売るため』は <span class='en'>never meant to sell</span> と矛盾。"},
    {"no":38,"tag":"理由","stem":"Why do critics object to these pricing methods?",
     "choices":[
       "Because they exploit predictable weaknesses in human judgment.",
       "Because they make prices too difficult to communicate.",
       "Because they force companies to lower every price.",
       "Because they always reduce a company's profits."],"answer":"ア",
     "basis":"第4段 <span class='en'>a form of manipulation that exploits predictable weaknesses in human judgment</span>。",
     "solve":"<span class='en'>Critics see the matter differently ... To them</span> の直後が批判の中身。",
     "cut":"『価格の伝達を難しくする』は、むしろ企業が擁護に使う『素早く価値を判断できる』論と食い違う。"},
    {"no":39,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned in the passage?",
     "choices":[
       "A law that bans discounts on watches.",
       "The anchoring effect of a high first number.",
       "The decoy effect created by a medium option.",
       "The long-term risk of losing customer trust."],"answer":"ア",
     "basis":"『割引を禁じる法律』は本文に記述がない。他の3つはそれぞれ第2段・第3段・第6段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある要素を消し、残る1つが答え。",
     "cut":"アンカリング・おとり効果・信頼喪失の長期リスクは、いずれも本文に述べられている。"},
    {"no":40,"tag":"内容真偽","stem":"According to paragraph 5, what makes the difference between guiding a choice and distorting it?",
     "choices":[
       "Whether the perceived value matches what the product actually delivers.",
       "Whether the price is the lowest in the market.",
       "Whether the seller offers many size options.",
       "Whether the buyer has shopped there before."],"answer":"ア",
     "basis":"第5段 <span class='en'>whether the perceived value a customer feels corresponds to anything the product actually delivers</span>。",
     "solve":"『誘導』と『歪曲』を分けるのは、感じる価値が実際の中身と対応するか否か。",
     "cut":"『市場で最も安いか』は本文の判断基準ではなく、価格の高低は論点ではない。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Pricing shapes perceived value and can guide demand, but firms that abuse it risk losing the trust that lasting business depends on.",
       "Companies should always set the lowest possible price to win customers.",
       "Psychological pricing has been proven harmless and fully fair to buyers.",
       "Anchoring and decoys no longer influence how people shop today."],"answer":"ア",
     "basis":"見せ方が支払意思を変える仕組み（1〜3段）／擁護と批判（4段）／境界の曖昧さ（5段）／信頼を損なう長期リスクという留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点と倫理的懸念の併記＋留保に沿う1つを残す。",
     "cut":"『無害で完全に公正と証明された』『最も安い価格にすべき』は言い過ぎで、本文の留保と矛盾。"},
  ],
  "structure":
    "<b>序論[1]</b>価格は数字以上の『信号』、支払意思は心の枠が決める ／ <b>利点[2]</b>アンカリング＝最初の数字が参照点 ／ "
    "<b>利点[3]</b>おとり効果＝本命を魅力的に見せ需要を誘導 ／ <b>論争[4]</b>企業の擁護 vs 批判（操作・弱点の悪用） ／ "
    "<b>含意[5]</b>誘導と歪曲の境界は曖昧＝知覚価値が実体と対応するか ／ <b>結論[6]</b>価格は中立でない、信頼を損なえば長期的に不利（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "価格は値札に印刷された数字以上のものだ。それは私たちの心が読み、比べ、解釈したうえで買うかどうかを決める『信号』である。"
    "行動経済学（行動価格研究）の研究者は、まったく同じ商品でも、どう見せられるかによって安く感じられたり高く感じられたりすることを"
    "見いだした。言い換えれば、私たちがいくら払う気になるかは、商品そのものよりも、それを取り巻く心の枠に大きく左右される。",
    "こうした効果の中でも最もよく研究されているのがアンカリングだ。買い手が最初に大きな数字を目にすると、その数字が参照点となり、"
    "後に続くどの価格もそれと並ぶと小さく見える。大きな元値から値下げされた時計は、売り手がその高い値段で売るつもりなど"
    "なかったとしても、お買い得に感じられる。最初の数字が静かにお膳立てをし、残りの判断はその周りで展開していく。",
    "関連する仕掛けがおとりだ。ある店が小と大のコーヒーを出し、大を選ぶ人がほとんどいないとしよう。売り手が大のすぐ下の値段で"
    "中を加えると、大は比較によって急に太っ腹に見え、その売上が伸びる。中はもともと売るためのものではなく、隣の選択肢を"
    "魅力的に見せるためだけに存在する。こうして売り手は、最も動かしたい選択肢へと需要を導くことができる。",
    "企業はこうした手法を、当たり前でむしろ有益なものだと擁護する。価格は何らかの形で伝えねばならず、よく設計された品目表は"
    "混み合った市場で買い手が価値を素早く判断する助けになるだけだ、と彼らは論じる。批判者はこの問題を違うように見る。"
    "彼らにとって、価格を取り巻く枠を作り込むことは、人間の判断にある予測可能な弱点につけ込み、本当に意図する以上に"
    "使わせるよう仕向ける操作の一形態なのだ。",
    "この論争は簡単には決着しない。選択を導くことと歪めることの境界が本当に曖昧だからだ。実際の品質を反映した参照価格は"
    "買い手に情報を与え、公正な判断を助けるが、もっぱら誤らせるために作り出された参照価格はそうではなく、"
    "役立つはずの信号を静かに罠へと変えてしまう。多くは、客が感じる知覚価値が、巧みな数字の並べ方だけでなく、"
    "商品が実際に提供する何かに対応しているかどうかにかかっている。",
    "はっきりしているのは、価格づけが決して中立ではなく、企業がそうでないふりはできないということだ。どんな品目表も"
    "どんな割引も、すでに何らかの形で目を誘導している。だが知覚を形づくる力は長期的なリスクを伴う。後になってだまされたと"
    "感じる買い手が戻ってくることはまれで、信頼はいったん失えば取り戻しにくい。最も巧妙な価格づけは一度の売上を"
    "勝ち取るかもしれないが、長く続く企業はたいてい、客がその数字を信じられる企業なのだ。",
  ],
  "vocab": [
    ("behavioral pricing","名","行動価格（価格の心理効果の研究）"),
    ("frame","名","枠組み、（判断の）フレーム"),
    ("anchoring","名","アンカリング（最初の数字への係留）"),
    ("reference point","名","参照点、基準"),
    ("bargain","名","お買い得品"),
    ("decoy","名","おとり（選択肢）"),
    ("steer","動","（需要などを）導く、操る"),
    ("manipulation","名","操作、操り"),
    ("exploit","動","（弱点に）つけ込む、利用する"),
    ("perceived value","名","知覚価値（客が感じる価値）"),
    ("neutral","形","中立の、偏りのない"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点と倫理的懸念の併記＋<b>留保</b>を選ぶ。",
}
