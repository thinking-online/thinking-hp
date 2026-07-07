# -*- coding: utf-8 -*-
"""大問Ⅲ READING 02 ― Eコマースと実店舗（the high street）の衰退。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "Eコマースと実店舗 ― 高街の衰退",
  "genre": "ビジネス／流通 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 436,
  "passage_title": "The Fading High Street",
  "passage": [
    "In the space of a single generation, the way people shop has been transformed. Where families once walked to a row "
    "of local shops to buy food, clothes, and gifts, many now order the same goods from a screen and wait for a van to "
    "arrive at the door. Retailers call this rise of online selling e-commerce, and shoppers everywhere have embraced "
    "[[u:32]]it[[/u]] with remarkable speed.",

    "The appeal is easy to understand. Online stores are open at every hour, carry a far wider range of products than any "
    "single building could hold, and often sell them at lower prices. Buying is [[u:33]]convenient[[/u]]: a person can "
    "compare dozens of sellers, read the views of past buyers, and place an order in minutes without leaving home. For "
    "those who live far from a town center, or who find travel difficult, this access can be a genuine gain.",

    "Yet the same shift is hollowing out the traditional shopping street, known in Britain as the high street. As sales "
    "move online, familiar stores close, empty windows spread, and the jobs they once provided [[u:34]]vanish[[/u]]. "
    "Something less visible is lost as well: the high street has long been a place where neighbors meet, where a shop owner "
    "knows a customer by name, and where a town keeps a sense of its own life. A district of shuttered fronts can drain the "
    "spirit of a community.",

    "Observers disagree about what [[u:35]]this trend[[/u]] means. Optimists insist that the change is simply progress, "
    "arguing that consumers gain lower prices and that new kinds of work spring up in warehouses and delivery. Critics "
    "reply that the gains flow mainly to a few giant platforms, while the costs fall on small towns that lose both their "
    "shops and their gathering places. Both sides accept one fact: the movement toward online buying shows no sign of "
    "slowing.",

    "For those who run physical stores, the lesson is not to fight the internet but to offer what a screen cannot. Shops "
    "that thrive today tend to sell experience as much as goods, hosting events, giving expert advice, and letting "
    "customers touch and try before they buy. Some use their premises as places to collect online orders, turning the "
    "store into a bridge rather than a rival to the web.",

    "Whether the high street survives may depend less on stopping e-commerce than on rethinking what a shop is for. The "
    "convenience of online buying is here to stay, and no town can wish it away. But a street of shops that offers "
    "welcome, advice, and a shared public space still holds a value that a delivery van cannot carry. The future of "
    "retail may belong not to one model alone, but to those who learn to weave the two together.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (shoppers have embraced it) refer to?","inline":True,
     "choices":["the rise of online selling","a row of local shops","a delivery van","a single generation"],"answer":"ア",
     "basis":"<span class='en'>Retailers call this rise of online selling e-commerce, and shoppers everywhere have embraced it</span> の <span class='en'>it</span> は直前の <b>e-commerce（オンライン販売の台頭）</b>。",
     "solve":"代名詞は直前の名詞へ。『買い物客が受け入れたそれ』＝オンライン販売＝Eコマース。",
     "cut":"<span class='en'>a row of local shops</span> はEコマースと対比される旧来の実店舗で逆。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“convenient”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["handy","costly","unreliable","rare"],"answer":"ア",
     "basis":"<span class='en'>convenient</span>＝「手軽な、便利な」。<span class='en'>place an order in minutes without leaving home</span> と一致。",
     "solve":"家を出ずに数分で注文できる＝手軽。<span class='en'>handy</span> が同義。",
     "cut":"<span class='en'>costly</span>（高くつく）は本文の <span class='en'>lower prices</span> と逆で不適。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“vanish”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["disappear","increase","remain","return"],"answer":"ア",
     "basis":"<span class='en'>familiar stores close … and the jobs they once provided vanish</span>＝店が閉じ、雇用が<b>消える</b>。",
     "solve":"店の閉店に伴い雇用が失われる文脈。<span class='en'>disappear</span> が同義。",
     "cut":"<span class='en'>increase</span>（増える）や <span class='en'>remain</span>（残る）は消失の逆で矛盾。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this trend”</span> in paragraph 4 refer to?","inline":True,
     "choices":["the movement toward online shopping","a fall in warehouse jobs","a rise in local shop owners","a new tax on delivery"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this trend</span>＝これまで述べてきた<b>オンライン購入への移行</b>。段末の <span class='en'>the movement toward online buying</span> と一致。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段までの内容を指す。話題はEコマースへの移行。",
     "cut":"<span class='en'>a fall in warehouse jobs</span> は本文でむしろ倉庫の仕事が生まれると述べており逆。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, which of the following is true about online stores?",
     "choices":[
       "They are open at all hours and often sell goods at lower prices.",
       "They carry fewer products than a single shop building.",
       "They can be used only by people living in town centers.",
       "They require buyers to travel before placing an order."],"answer":"ア",
     "basis":"第2段 <span class='en'>Online stores are open at every hour … and often sell them at lower prices</span> に一致。",
     "solve":"設問のキーワード（open / prices）を第2段前半で照合。",
     "cut":"『扱う商品が少ない』は <span class='en'>a far wider range of products</span> と矛盾。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a loss caused by the decline of the high street?",
     "choices":[
       "House prices in towns fall sharply.",
       "The jobs that local stores once provided disappear.",
       "A place where neighbors meet is lost.",
       "The spirit of a community can be drained."],"answer":"ア",
     "basis":"『住宅価格が急落する』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある損失を消し、残る1つが答え。",
     "cut":"雇用の消失・出会いの場の喪失・地域の活気の枯渇は、いずれも第3段に一致するので損失として『述べられている』。"},
    {"no":38,"tag":"理由","stem":"Why do critics worry about the growth of e-commerce?",
     "choices":[
       "Because the gains flow mainly to a few giant platforms while small towns bear the costs.",
       "Because online prices are always higher than shop prices.",
       "Because warehouses and delivery create no new work at all.",
       "Because consumers refuse to buy goods from a screen."],"answer":"ア",
     "basis":"第4段 <span class='en'>the gains flow mainly to a few giant platforms, while the costs fall on small towns</span>。",
     "solve":"<span class='en'>Critics reply that …</span> の直後が批判の中身。",
     "cut":"『倉庫や配送が全く雇用を生まない』は楽観論の <span class='en'>new kinds of work spring up</span> と食い違い、批判の論拠でもない。"},
    {"no":39,"tag":"詳細","stem":"According to paragraph 5, what do shops that thrive today tend to do?","inline":True,
     "choices":[
       "They sell experience as much as goods, hosting events and giving expert advice.",
       "They lower their prices below those of every online seller.",
       "They stop selling goods and rent their space to warehouses.",
       "They refuse to accept or collect any online orders."],"answer":"ア",
     "basis":"第5段 <span class='en'>Shops that thrive today tend to sell experience as much as goods, hosting events, giving expert advice</span>。",
     "solve":"設問の主語（shops that thrive）を第5段で探す。",
     "cut":"『オンライン注文を一切受けない』は <span class='en'>use their premises as places to collect online orders</span> と逆。"},
    {"no":40,"tag":"内容真偽","stem":"Which of the following is true according to the passage?",
     "choices":[
       "The convenience of online buying is likely to remain, and no town can simply get rid of it.",
       "Physical stores are advised to ignore the internet completely.",
       "The movement toward online buying is quickly slowing down.",
       "A delivery van can provide the same public space as a street of shops."],"answer":"ア",
     "basis":"第6段 <span class='en'>The convenience of online buying is here to stay, and no town can wish it away</span> に一致。",
     "solve":"各選択肢を段の記述と照合。留保しつつ利便性の定着を認める第6段に合う1つを残す。",
     "cut":"『配送車が商店街と同じ公共空間を与える』は <span class='en'>a value that a delivery van cannot carry</span> と矛盾。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "E-commerce brings convenience but hollows out the high street, and coexistence depends on redefining what a shop is for.",
       "Online shopping has completely destroyed every physical store in the world.",
       "The high street can survive only by banning e-commerce outright.",
       "Delivery vans have already solved the problem of community life."],"answer":"ア",
     "basis":"利便性（2段）／実店舗の空洞化（3段）／賛否（4段）／実店舗の再定義（5段）／共存はあり方の見直し次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点と弊害の両論＋留保に沿う1つを残す。",
     "cut":"『全ての実店舗を破壊した』『Eコマース全面禁止でのみ存続』は言い過ぎ。『配送車が地域社会を解決した』は本文と逆。"},
  ],
  "structure":
    "<b>序論[1]</b>Eコマースの台頭と急速な普及 ／ <b>利点[2]</b>24時間・品揃え・低価格・手軽さ ／ "
    "<b>弊害[3]</b>高街の空洞化・雇用喪失・地域の絆の消失 ／ <b>論争[4]</b>楽観論（進歩）vs 批判（利益は巨大企業へ、負担は小都市へ） ／ "
    "<b>経営視点[5]</b>実店舗は体験を売り、Web との橋渡し役へ ／ <b>結論[6]</b>存続は『店とは何か』の再定義次第（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "一世代のうちに、人々の買い物の仕方は一変した。かつて家族は近所の商店の並びまで歩いて食料や衣服や贈り物を買ったが、"
    "今や多くの人が同じ品を画面から注文し、配送車が戸口に着くのを待つ。小売業者はこのオンライン販売の台頭を『Eコマース』と呼び、"
    "世界中の買い物客が驚くべき速さでそれを受け入れてきた。",
    "その魅力は分かりやすい。オンライン店舗はあらゆる時間に開いており、どんな一つの建物にも収まらないほど幅広い品を扱い、"
    "しかも多くの場合それをより安く売る。買い物は手軽だ。数十の売り手を比べ、過去の購入者の評価を読み、"
    "家を出ずに数分で注文できる。町の中心から遠い人や、移動が難しい人にとって、この利用しやすさは真の恩恵となりうる。",
    "だが同じ変化は、伝統的な商店街――英国で『ハイストリート（高街）』と呼ばれる――を空洞化させている。"
    "売上がオンラインへ移るにつれ、なじみの店が閉じ、空き店舗が広がり、そこがかつて生んでいた雇用が消える。"
    "目に見えにくいものも失われる。高街は長らく、隣人が出会い、店主が客を名前で知り、町がそれ自身の暮らしの実感を保つ場だった。"
    "シャッターの下りた通りは、地域の活気を枯らしうる。",
    "この傾向が何を意味するかで、見る者の意見は割れる。楽観論者は、この変化は単なる進歩だと言い張り、"
    "消費者は低価格を得て、倉庫や配送に新しい種類の仕事が生まれると論じる。批判者は、利益は主に一握りの巨大プラットフォームへ流れ、"
    "その負担は店と集いの場の双方を失う小さな町に落ちる、と反論する。両者が認める事実は一つ――"
    "オンライン購入への流れは衰える気配がない、ということだ。",
    "実店舗を営む者にとっての教訓は、ネットと戦うことではなく、画面にできないものを提供することだ。"
    "今日栄える店は、商品と同じくらい体験を売る傾向がある――催しを開き、専門的な助言を与え、買う前に客に触れさせ試させる。"
    "自店の場所をオンライン注文の受け取り場所として使い、店をWebの競争相手ではなく橋渡し役に変える店もある。",
    "高街が生き残るかは、Eコマースを止めることよりも、『店とは何のためにあるか』を見直すことにかかっているのかもしれない。"
    "オンライン購入の利便性は定着しており、どの町もそれを願い消すことはできない。だが、歓迎と助言と共有の公共空間を提供する商店の通りは、"
    "配送車には運べない価値をなお持っている。小売の未来は、一つのモデルだけにではなく、"
    "その二つを織り合わせることを学ぶ者に属するのかもしれない。",
  ],
  "vocab": [
    ("e-commerce","名","電子商取引、オンライン販売"),
    ("embrace","動","受け入れる、取り入れる"),
    ("convenient","形","手軽な、便利な"),
    ("high street","名","（英）目抜き通り、商店街"),
    ("hollow out","句動","空洞化させる"),
    ("vanish","動","消える、消失する"),
    ("shuttered","形","シャッターの下りた、閉店した"),
    ("warehouse","名","倉庫、物流拠点"),
    ("thrive","動","栄える、繁盛する"),
    ("premises","名","店舗、敷地、建物"),
    ("weave","動","織り合わせる、組み合わせる"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点と弊害の両論併記＋<b>留保</b>を選ぶ。",
}
