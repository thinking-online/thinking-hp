# -*- coding: utf-8 -*-
"""大問Ⅲ READING 09 ― ファストファッションと持続可能性。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "ファストファッションと持続可能性 ― 安く速い流行服",
  "genre": "環境／消費 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 420,
  "passage_title": "The Real Price of Cheap Clothes",
  "passage": [
    "In recent years, the clothing industry has learned to move at astonishing speed. New styles that once took months "
    "to reach the shelves now appear in a matter of weeks, sold at prices so low that a shirt can cost less than a sandwich. "
    "Retailers call this model fast fashion, and shoppers around the world have embraced [[u:32]]it[[/u]] with enthusiasm.",

    "The appeal is easy to understand. Fast fashion makes clothing remarkably [[u:33]]affordable[[/u]], putting the latest "
    "looks within reach of people who could never spend a fortune on their wardrobe. Stores refresh their collections "
    "constantly, so customers enjoy endless variety and the pleasure of buying something new whenever they wish. For many "
    "young people, the ability to dress well on a small budget feels like a genuine form of freedom.",

    "Yet this convenience carries a heavy hidden cost. Producing garments so cheaply and quickly demands enormous quantities "
    "of water, energy, and chemicals, and much of the clothing is [[u:34]]discarded[[/u]] after only a few wears. Mountains "
    "of textile waste pile up in landfills, where synthetic fibers may take centuries to break down. Behind the low prices, "
    "too, lie factories where workers are often paid very little for long hours in unsafe conditions.",

    "Observers are sharply divided over what [[u:35]]this pattern[[/u]] means. Defenders insist that fast fashion has "
    "democratized style, giving ordinary consumers choices that were once reserved for the wealthy, while providing jobs in "
    "developing economies. Critics reply that the industry encourages a throwaway culture in which clothes are treated as "
    "disposable, and that its true price is paid by the planet and by the people who sew the garments. Both sides agree that "
    "the volume of clothing produced each year continues to climb.",

    "For businesses and shoppers alike, the trend poses an awkward question. Some argue that only strict government "
    "regulation can curb the waste, forcing companies to recycle materials and reveal how their goods are made. Others "
    "believe that laws alone will accomplish little unless buying habits change, since a market that rewards ever-cheaper "
    "clothing will always find ways to supply it. The most promising efforts combine both, pairing clear rules with a shift "
    "in what customers value.",

    "Whether fast fashion becomes a lasting burden or a manageable one may depend less on any single law than on the "
    "awareness of consumers and the responsibility of the firms that serve them. The industry has taught the world to buy "
    "more for less; it has not yet taught it to weigh the fuller cost of what a cheap garment truly requires.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (have embraced it) refer to?","inline":True,
     "choices":[
       "the fast-fashion model of cheap, quickly changing clothes",
       "a single expensive luxury brand",
       "a new government regulation",
       "a cheaper kind of sandwich"],"answer":"ア",
     "basis":"<span class='en'>Retailers call this model fast fashion, and shoppers … have embraced it</span> の <span class='en'>it</span> は直前の <span class='en'>this model</span>＝<b>ファストファッション</b>。",
     "solve":"代名詞は直前の名詞へ。『それを受け入れた』の『それ』＝安く速く変わる服のモデル。",
     "cut":"『高級ブランド』はファストファッションと対比される側で逆。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“affordable”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["inexpensive","fashionable","durable","exclusive"],"answer":"ア",
     "basis":"<span class='en'>affordable</span>＝「手頃な、安く買える」。直後の <span class='en'>within reach of people who could never spend a fortune</span> と一致。",
     "solve":"大金をかけられない人でも手が届く＝安い。<span class='en'>inexpensive</span> が同義。",
     "cut":"<span class='en'>exclusive</span>（高級で限られた）は手頃さと正反対。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“discarded”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["thrown away","repaired","recycled","stored"],"answer":"ア",
     "basis":"<span class='en'>much of the clothing is discarded after only a few wears</span>＝数回着ただけで<b>捨てられる</b>。次文の <span class='en'>textile waste pile up in landfills</span> が裏づけ。",
     "solve":"埋立地に廃棄物が積み上がる文脈から『捨てる』。<span class='en'>thrown away</span> が同義。",
     "cut":"<span class='en'>recycled</span>（再生利用）はむしろ廃棄の反対で、廃棄物が積み上がる記述と食い違う。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this pattern”</span> in paragraph 4 refer to?","inline":True,
     "choices":[
       "the fast-fashion practice of making and quickly throwing away cheap clothes",
       "a steady decline in clothing prices",
       "a new law requiring recycling",
       "a worldwide shortage of textiles"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this pattern</span> は前段までの<b>安い服を大量に作り短期間で捨てる仕組み</b>を指す。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段の内容を要約して指す。話題は安く速い生産と廃棄。",
     "cut":"『繊維の世界的不足』は本文になく、むしろ大量生産が問題とされている。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 3, which of the following is true?",
     "choices":[
       "Synthetic fibers in landfills may take centuries to break down.",
       "Fast fashion uses very little water and energy.",
       "Most garments are worn for many years before disposal.",
       "Factory workers are typically paid generous wages."],"answer":"ア",
     "basis":"第3段 <span class='en'>synthetic fibers may take centuries to break down</span> に一致。",
     "solve":"設問のキーワード（synthetic fibers / landfills）を第3段で照合。",
     "cut":"『水や電力をほとんど使わない』は <span class='en'>demands enormous quantities of water, energy</span> と矛盾。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a drawback of fast fashion?",
     "choices":[
       "Cheap clothes often cause allergic reactions in customers.",
       "Production demands huge amounts of water and chemicals.",
       "Textile waste piles up in landfills for a very long time.",
       "Factory workers face low pay and unsafe conditions."],"answer":"ア",
     "basis":"『安い服がアレルギーを起こす』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある短所を消し、残る1つが答え。",
     "cut":"大量の水と化学物質・埋立地の廃棄・低賃金と危険な労働は、いずれも第3段に一致するので短所として『述べられている』。"},
    {"no":38,"tag":"理由","stem":"Why do critics object to fast fashion?",
     "choices":[
       "Because it promotes a throwaway culture whose cost falls on the planet and garment workers.",
       "Because it makes clothing too expensive for ordinary people.",
       "Because it reserves fashionable styles only for the wealthy.",
       "Because it sharply reduces the total amount of clothing produced."],"answer":"ア",
     "basis":"第4段 <span class='en'>the industry encourages a throwaway culture … its true price is paid by the planet and by the people who sew the garments</span>。",
     "solve":"<span class='en'>Critics reply that …</span> の直後が批判の中身。",
     "cut":"『服が高くなりすぎる』は手頃さを利点とする第2段と食い違い、批判の論拠でもない。"},
    {"no":39,"tag":"詳細","stem":"According to paragraph 2, what do shoppers gain from fast fashion?",
     "choices":[
       "The latest styles at low prices and constant variety.",
       "Guaranteed high quality that lasts for many years.",
       "Clothing made entirely from recycled materials.",
       "Personal tailoring designed for each customer."],"answer":"ア",
     "basis":"第2段 <span class='en'>the latest looks within reach … endless variety and the pleasure of buying something new</span>。",
     "solve":"設問の主語（shoppers）を第2段で探し、利点を照合する。",
     "cut":"『何年も長持ちする高品質』は数回で捨てられるという第3段の記述と逆。"},
    {"no":40,"tag":"内容真偽","stem":"According to paragraphs 4 and 5, which of the following is true?",
     "choices":[
       "Defenders say fast fashion has made stylish clothing available to ordinary consumers.",
       "Both sides agree that yearly clothing production is falling.",
       "Everyone agrees that strict regulation is unnecessary.",
       "Critics claim the industry has no effect on the environment."],"answer":"ア",
     "basis":"第4段 <span class='en'>Defenders insist that fast fashion has democratized style, giving ordinary consumers choices …</span> に一致。",
     "solve":"賛否それぞれの主張を段で照合。擁護派は『普通の消費者に流行を開いた』と述べる。",
     "cut":"『毎年の生産量が減っている』は <span class='en'>the volume … continues to climb</span> と正反対。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Fast fashion offers affordable variety but brings environmental and human costs, and its future hinges on consumer awareness and corporate responsibility more than on law alone.",
       "Government regulation has already eliminated textile waste around the world.",
       "Fast fashion has proven completely harmless to the environment.",
       "Shoppers everywhere should stop buying any new clothes at once."],"answer":"ア",
     "basis":"手頃さ・多様性（2段）／環境と労働の弊害（3段）／賛否（4段）／規制か意識か（5段）／意識と企業責任次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点と弊害の両論＋留保に沿う1つを残す。",
     "cut":"『規制が既に廃棄物をなくした』『環境に無害と証明された』は言い過ぎ。『新品を一切買うな』は本文にない。"},
  ],
  "structure":
    "<b>序論[1]</b>ファストファッションの登場と流行の高速化 ／ <b>利点[2]</b>手頃さ・多様性・低予算の自由 ／ "
    "<b>弊害[3]</b>水・エネルギー・廃棄物・労働問題 ／ <b>論争[4]</b>擁護（流行の民主化）vs 批判（使い捨て文化） ／ "
    "<b>含意[5]</b>規制か消費者の意識か、両輪が有望 ／ <b>結論[6]</b>是非は意識と企業責任次第（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "近年、衣料産業は驚くべき速さで動くことを身につけた。かつては店頭に並ぶまで数か月かかった新しいスタイルが、"
    "今や数週間で現れ、シャツ1枚がサンドイッチより安いほどの低価格で売られる。小売業者はこの仕組みを"
    "『ファストファッション』と呼び、世界中の買い物客がそれを熱狂的に受け入れてきた。",
    "その魅力は分かりやすい。ファストファッションは衣料を著しく手頃にし、大金を服にかけられない人々にも"
    "最新の装いを手の届くものにする。店は絶えず品ぞろえを一新するので、客は無限の多様性と、"
    "好きなときに新しいものを買う楽しみを味わう。多くの若者にとって、少ない予算でおしゃれをできることは、"
    "本物の自由の一形態のように感じられる。",
    "だがこの便利さには重い隠れた代償が伴う。これほど安く速く衣類を作るには膨大な量の水・エネルギー・化学物質を要し、"
    "衣類の多くはほんの数回着ただけで捨てられる。繊維廃棄物の山が埋立地に積み上がり、そこでは合成繊維が"
    "分解に何世紀もかかりうる。低価格の裏にはまた、労働者がしばしば危険な環境で長時間、ごくわずかな賃金で"
    "働く工場が横たわっている。",
    "この構図が何を意味するかで、識者の見解は鋭く割れている。擁護派は、ファストファッションはスタイルを民主化し、"
    "かつては富裕層のものだった選択肢を普通の消費者に与え、発展途上の経済に雇用をもたらしたと主張する。"
    "批判派は、この産業は服を使い捨てとして扱う『使い捨て文化』を助長し、その真の代償は地球と、"
    "服を縫う人々によって支払われると反論する。両者が一致するのは、毎年生産される衣類の量が増え続けている点だ。",
    "企業にとっても買い物客にとっても、この傾向は厄介な問いを突きつける。厳しい政府規制だけが廃棄を抑えられ、"
    "企業に素材の再生利用と製造方法の開示を強制できると論じる者もいる。他方、買う習慣が変わらない限り法律だけでは"
    "ほとんど成果はない、より安い服を求める市場は常に供給の道を見つけるからだ、と考える者もいる。"
    "最も有望な取り組みは両者を組み合わせ、明確な規則と、客が何を大切にするかの変化とを対にする。",
    "ファストファッションが末永い重荷になるのか、御しうるものになるのかは、単一の法律よりも、"
    "消費者の意識と、彼らに奉仕する企業の責任にかかっているのかもしれない。この産業は世界に『より少なく払って"
    "より多く買う』ことを教えたが、安い一着が本当に要求するものの、より大きな代償を量ることは、まだ教えていない。",
  ],
  "vocab": [
    ("fast fashion","名","安く速く流行を回す衣料モデル"),
    ("affordable","形","手頃な、安く買える"),
    ("wardrobe","名","持ち衣装、衣装だんす"),
    ("discard","動","捨てる、処分する"),
    ("textile waste","名","繊維廃棄物"),
    ("landfill","名","埋立地、ごみ処分場"),
    ("synthetic fiber","名","合成繊維"),
    ("democratize","動","（広く）行き渡らせる、民主化する"),
    ("throwaway culture","名","使い捨て文化"),
    ("disposable","形","使い捨ての"),
    ("curb","動","抑える、抑制する"),
    ("hinge on","句動","〜次第である"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "言い換えは前後の文脈語（<span class='en'>within reach / landfills</span> など）で確定させ、"
    "主旨は利点と弊害の両論併記＋<b>留保</b>を選ぶ。",
}
