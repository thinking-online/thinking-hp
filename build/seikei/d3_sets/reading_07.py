# -*- coding: utf-8 -*-
"""大問Ⅲ READING 07 ― グローバル化と地域文化。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "グローバル化と地域文化 ― 均質化かグローカルか",
  "genre": "文化／社会 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 439,
  "passage_title": "The World and the Local",
  "passage": [
    "In a single afternoon, a shopper in almost any large city can buy the same coffee, wear the same brand of shoes, and "
    "watch the same film as someone thousands of miles away. This blending of national markets into one vast web of trade "
    "is what people mean by globalization, and few forces have reshaped daily life so quickly. Yet [[u:32]]it[[/u]] raises a "
    "difficult question: when the whole world can share everything, what happens to the things that once made each place "
    "unlike any other?",

    "Supporters point first to the gains in efficiency and choice. When goods, money, and ideas cross borders freely, "
    "producers can sell to a larger audience, and prices tend to fall. A farmer in one country can reach kitchens on the "
    "far side of the planet, while shoppers enjoy a range of products that earlier generations could hardly imagine. "
    "Global competition, its defenders argue, rewards the [[u:33]]inventive[[/u]] and pushes everyone to improve.",

    "But the same openness carries a cost. As a handful of powerful brands spread into every market, local shops, foods, "
    "and crafts can struggle to survive. Small producers who cannot match the prices of giant firms may [[u:34]]fold[[/u]], "
    "and a distinctive regional recipe or a traditional skill can quietly vanish. Critics warn of a slow homogenization, in "
    "which the streets of distant cities begin to look, sound, and taste unsettlingly alike.",

    "Scholars are divided over how serious [[u:35]]this danger[[/u]] really is. Pessimists fear that a few dominant cultures "
    "will overwhelm the rest, flattening the worlds rich variety into a single bland sameness. Optimists reply that people "
    "rarely swallow foreign influences whole; instead they borrow, adjust, and mix them with their own traditions, producing "
    "hybrids that are genuinely new. On one point, though, both camps agree: cultures never stay perfectly still, and contact "
    "always changes them.",

    "For businesses and communities alike, the practical lesson is one of balance. Companies that ignore local tastes often "
    "fail, while those that adapt a global product to regional needs tend to thrive; observers call this careful blending "
    "glocalization. A restaurant chain that adjusts its menu to suit local palates, or a festival that welcomes outside "
    "visitors without losing its own character, shows that the world and the local need not be enemies.",

    "Whether globalization narrows human culture or enriches it may therefore depend less on trade itself than on how wisely "
    "societies choose to guide it. Openness can spread comfort and opportunity, but a world that forgets its many voices "
    "would be poorer for the loss. The task ahead is not to halt exchange, but to keep it from erasing the very differences "
    "that make exchange worth having.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (it raises a difficult question) refer to?","inline":True,
     "choices":["globalization","a single afternoon","a brand of shoes","a large city"],"answer":"ア",
     "basis":"<span class='en'>Yet it raises a difficult question</span> の <span class='en'>it</span> は直前で定義された <span class='en'>globalization</span>。",
     "solve":"代名詞は直前の主要名詞へ。第1段の話題＝グローバル化そのものが問いを生む。",
     "cut":"<span class='en'>a single afternoon</span> は買い物の場面設定にすぎず、問いを起こす主体ではない。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“inventive”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["creative","cautious","obedient","wealthy"],"answer":"ア",
     "basis":"<span class='en'>rewards the inventive and pushes everyone to improve</span>＝「<b>創意ある</b>者に報い改善を促す」。",
     "solve":"競争が改善を促す文脈。工夫し新しく作る＝<span class='en'>creative</span> が同義。",
     "cut":"<span class='en'>cautious</span>（慎重な）は発明の意味と無関係。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“fold”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["close down","expand fast","join together","raise prices"],"answer":"ア",
     "basis":"<span class='en'>Small producers who cannot match the prices of giant firms may fold</span>＝値段で勝てず「<b>廃業する</b>」。",
     "solve":"直後に伝統の技が消えるとある。事業の <span class='en'>fold</span>＝倒れる・畳む＝<span class='en'>close down</span>。",
     "cut":"<span class='en'>expand fast</span>（急拡大）は文脈と正反対。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this danger”</span> in paragraph 4 refer to?","inline":True,
     "choices":["the homogenization of local cultures","a rise in global prices","a shortage of new products","the failure of world trade"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this danger</span>＝第3段で述べた<b>均質化</b>（地域文化が似通い消える恐れ）。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段の内容を受ける。直前の話題は均質化の脅威。",
     "cut":"<span class='en'>a rise in global prices</span> は第2段でむしろ下がると述べており逆。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, what do supporters of globalization emphasize?",
     "choices":[
       "Greater efficiency and a wider range of choices.",
       "The protection of every local craft.",
       "A rise in prices caused by competition.",
       "The need to close national borders."],"answer":"ア",
     "basis":"第2段 <span class='en'>Supporters point first to the gains in efficiency and choice</span> に一致。",
     "solve":"設問のキーワード（supporters）を第2段冒頭で照合。効率と選択肢の拡大が要点。",
     "cut":"『地域の工芸をすべて守る』は支持者ではなく批判側の懸念で、第2段の主張ではない。"},
    {"no":37,"tag":"内容真偽","stem":"According to paragraph 4, what do both pessimists and optimists agree on?",
     "choices":[
       "Cultures never stay still and contact always changes them.",
       "A single culture will surely dominate the world.",
       "Foreign influences are always accepted unchanged.",
       "Global trade should be stopped immediately."],"answer":"ア",
     "basis":"第4段末 <span class='en'>both camps agree: cultures never stay perfectly still, and contact always changes them</span>。",
     "solve":"<span class='en'>both camps agree</span> の直後が両者一致の内容。文化は静止せず接触で変わる。",
     "cut":"『単一文化が必ず支配する』は悲観論の予測であって両者の合意点ではない。"},
    {"no":38,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a possible cost of globalization?",
     "choices":[
       "Governments lose the power to collect taxes.",
       "Local shops and crafts can struggle to survive.",
       "A traditional skill can quietly vanish.",
       "Distant cities begin to look and taste alike."],"answer":"ア",
     "basis":"『政府が徴税権を失う』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"<span class='en'>NOT</span> に印。第3段の弊害（地元店の苦境・伝統喪失・均質化）を消し、残る1つが答え。",
     "cut":"地元店の苦境・伝統技能の消失・都市の均質化は、いずれも第3段に一致するので『述べられている』。"},
    {"no":39,"tag":"理由","stem":"Why do optimists believe local cultures can survive contact with foreign influences?",
     "choices":[
       "Because people borrow and adjust influences, mixing them into new hybrids.",
       "Because foreign products are always too expensive to buy.",
       "Because governments ban most imported goods.",
       "Because global brands avoid entering small markets."],"answer":"ア",
     "basis":"第4段 <span class='en'>they borrow, adjust, and mix them with their own traditions, producing hybrids that are genuinely new</span>。",
     "solve":"<span class='en'>Optimists reply that …</span> の直後が楽観論の論拠。取り込み混ぜて新しくする。",
     "cut":"『政府が輸入を禁止する』は本文になく、楽観論の根拠でもない。"},
    {"no":40,"tag":"詳細","stem":"According to paragraph 5, what does the term <span class='en'>“glocalization”</span> describe?",
     "choices":[
       "Adapting a global product to suit regional needs.",
       "Selling the same product everywhere without change.",
       "Rejecting all outside visitors and influences.",
       "Replacing local festivals with global ones."],"answer":"ア",
     "basis":"第5段 <span class='en'>those that adapt a global product to regional needs tend to thrive; observers call this careful blending glocalization</span>。",
     "solve":"設問の語（glocalization）を第5段で探し、直前の定義を確認する。世界的な製品を地域に合わせること。",
     "cut":"『どこでも同じ製品を無変更で売る』は適応と逆で、失敗しがちだと述べられている。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Globalization brings both wider choice and the risk of sameness, so societies must guide it to preserve local differences.",
       "Globalization has already erased every local culture around the world.",
       "Global trade should be halted to protect traditional ways of life.",
       "Local cultures are unaffected by the spread of global brands."],"answer":"ア",
     "basis":"効率と選択肢（2段）／均質化の弊害（3段）／賛否（4段）／グローカルな適応（5段）／導き方次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎと本文にない要素を切り、両論併記＋留保に沿う1つを残す。",
     "cut":"『すべての地域文化を既に消し去った』『貿易を止めるべき』は言い過ぎ。『地域文化は無影響』は第3段と矛盾。"},
  ],
  "structure":
    "<b>序論[1]</b>グローバル化の定義と『固有性はどうなるか』という問い ／ <b>利点[2]</b>効率・選択肢・低価格 ／ "
    "<b>弊害[3]</b>地元産業の苦境・均質化の恐れ ／ <b>論争[4]</b>悲観論 vs 楽観論（雑種文化）・共通の合意点 ／ "
    "<b>含意[5]</b>バランス＝グローカル化 ／ <b>結論[6]</b>導き方次第という留保。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "たった一つの午後で、ほとんどどの大都市の買い物客も、数千マイル離れた誰かと同じコーヒーを買い、"
    "同じブランドの靴を履き、同じ映画を観られる。国ごとの市場が一つの巨大な取引の網へと溶け合うこと――"
    "それが人々の言う『グローバル化』であり、これほど速く日常を作り変えた力はほとんどない。"
    "だがそれは難しい問いを生む。世界中が何もかもを共有できるとき、かつて各地を他のどことも違うものにしていたものは、どうなるのか。",
    "支持者はまず効率と選択肢の拡大を挙げる。財・カネ・アイデアが国境を自由に越えれば、生産者はより多くの相手に売れ、"
    "価格は下がる傾向にある。ある国の農家が地球の裏側の台所に届き、買い物客は前の世代には想像もつかなかった品揃えを楽しむ。"
    "世界的な競争は、擁護者に言わせれば、創意ある者に報い、誰もが改善するよう促す。",
    "だが同じ開放性には代償がある。一握りの強力なブランドがあらゆる市場に広がるにつれ、地元の店・食・工芸は生き残りに苦しみうる。"
    "巨大企業の価格に太刀打ちできない小さな生産者は廃業しかねず、独特の地方料理や伝統の技が静かに消えうる。"
    "批判者は、遠く離れた都市の街並みが、見た目も音も味わいも不気味なほど似通っていく、ゆるやかな均質化を警告する。",
    "この危険がどれほど深刻かで、学者の見解は割れている。悲観論者は、少数の支配的な文化が残りを圧倒し、"
    "世界の豊かな多様性を単一の味気ない同一性へと平板化することを恐れる。楽観論者は、人々が外来の影響を丸ごと呑み込むことはまれで、"
    "むしろ借り、調整し、自らの伝統と混ぜて、本当に新しい雑種を生み出すのだと応じる。だが一点で両陣営は一致する――"
    "文化は完全に静止することはなく、接触は常にそれを変える、ということだ。",
    "企業にとっても地域社会にとっても、実際的な教訓はバランスの一つだ。地元の好みを無視する企業はしばしば失敗し、"
    "世界的な製品を地域の需要に合わせる企業は繁栄しがちだ――観察者はこの丁寧な融合を『グローカル化』と呼ぶ。"
    "地元の味覚に合わせて献立を調整する外食チェーンや、独自の性格を失わずに外来の客を迎える祭りは、"
    "世界と地域が敵同士である必要はないことを示している。",
    "したがって、グローバル化が人間の文化を狭めるのか豊かにするのかは、貿易そのものよりも、"
    "社会がそれをどれほど賢く導くかにかかっているのかもしれない。開放性は快適さと機会を広げうるが、"
    "多くの声を忘れた世界は、その喪失のぶんだけ貧しくなるだろう。これからの課題は交流を止めることではなく、"
    "交流を価値あるものにしているまさにその違いを、交流が消し去らないようにすることだ。",
  ],
  "vocab": [
    ("globalization","名","グローバル化、世界市場の統合"),
    ("efficiency","名","効率"),
    ("inventive","形","創意に富む、独創的な"),
    ("homogenization","名","均質化、同質化"),
    ("distinctive","形","独特の、他と異なる"),
    ("fold","動","（事業が）廃業する、倒れる"),
    ("dominant","形","支配的な、優勢な"),
    ("hybrid","名","雑種、混成物"),
    ("adapt","動","適応させる、合わせる"),
    ("glocalization","名","グローカル化（世界と地域の融合）"),
    ("erase","動","消し去る"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は両論併記＋<b>留保</b>を選ぶ。",
}
