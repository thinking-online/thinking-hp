# -*- coding: utf-8 -*-
"""大問Ⅲ READING 11 ― キャッシュレス社会。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "キャッシュレス社会 ― 現金なき決済のゆくえ",
  "genre": "社会／経済 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 445,
  "passage_title": "A Society Without Cash",
  "passage": [
    "In many countries, notes and coins are quietly disappearing from daily life. Shoppers tap a card or wave a phone, "
    "and money moves in an instant from one account to another. Governments and banks welcome this trend, and some "
    "observers predict a fully cashless society within a single generation. Supporters admire the ease and speed "
    "[[u:32]]it[[/u]] brings to ordinary shopping.",

    "The main appeal is convenience. A digital payment is [[u:33]]swift[[/u]], requiring neither change nor a trip to the "
    "bank, and it can be made at any hour from almost anywhere. For businesses, electronic records reduce the cost of "
    "counting and guarding cash, and they leave a clear trail that makes tax collection and accounting more transparent. "
    "For governments, that same trail can expose bribery and hidden income that once passed unseen.",

    "Yet the move away from cash carries real dangers. Millions of people have no bank account or smartphone, and a shop "
    "that refuses notes shuts these customers out. Older people and low-income households often depend on cash, so a "
    "cashless system can deepen their [[u:34]]exclusion[[/u]]. Every digital payment also records who bought what, where, "
    "and when, which raises serious questions about privacy. And when a network fails or the power goes down, a purely "
    "electronic system can leave everyone unable to buy even food.",

    "Experts disagree about what [[u:35]]this transformation[[/u]] means for society. Optimists argue that digital money "
    "is safer than cash, harder to steal, and a powerful tool for financial inclusion in poor regions where banks are "
    "scarce but phones are common. Critics reply that it hands enormous power to the firms and states that control the "
    "payment networks, and that a society able to track every transaction may lose an important kind of freedom. Both "
    "sides agree on one point: the change is arriving faster than the rules meant to govern it.",

    "For policymakers, the design of the system matters as much as the technology itself. A network built only for the "
    "young and connected will punish those who are not, while one that guarantees an offline option and protects personal "
    "data can spread the benefits far more widely. The question is not simply whether to go cashless, but how, and for "
    "whose benefit.",

    "For these reasons, many economists urge a gradual path rather than a sudden leap. Keeping cash available as a "
    "backstop, even as digital payment grows, protects the vulnerable and guards against the day the machines fail. "
    "Whether a cashless society sets people free or quietly fences them in may depend less on the speed of the change "
    "than on the care with which it is designed.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (the ease and speed it brings) refer to?","inline":True,
     "choices":[
       "the trend toward a cashless society",
       "a single bank account",
       "a trip to the bank",
       "a paper note"],"answer":"ア",
     "basis":"<span class='en'>the ease and speed it brings</span> の <span class='en'>it</span> は直前で述べた<b>キャッシュレス化の流れ</b>を指す。",
     "solve":"代名詞は直前の話題へ。第1段の主題は現金が消えていく<b>trend</b>。その流れが与える速さと手軽さ。",
     "cut":"<span class='en'>a trip to the bank</span> は第2段で『不要になるもの』として出るだけで、<span class='en'>it</span> の指示対象ではない。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“swift”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["quick","slow","risky","expensive"],"answer":"ア",
     "basis":"<span class='en'>swift</span>＝「素早い」。<span class='en'>in an instant</span>・<span class='en'>at any hour</span> の文脈と一致。",
     "solve":"瞬時に完了し両替も来店も要らない＝速い。<span class='en'>quick</span> が同義。",
     "cut":"<span class='en'>slow</span> は反意で、決済の利点を述べる文脈に合わない。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“exclusion”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["being left out","full participation","a cash reward","a bank loan"],"answer":"ア",
     "basis":"<span class='en'>a shop that refuses notes shuts these customers out</span> を受け、<span class='en'>exclusion</span>＝<b>締め出されること</b>。",
     "solve":"口座もスマホもない人が現金拒否で買えなくなる＝仲間外れ・排除。<span class='en'>being left out</span> が同義。",
     "cut":"<span class='en'>full participation</span>（十分な参加）は反意で逆。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this transformation”</span> in paragraph 4 refer to?","inline":True,
     "choices":[
       "the move away from cash toward digital payment",
       "a sudden rise in bank fees",
       "a new tax law on smartphones",
       "a fall in the use of the internet"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this transformation</span>＝前段までで論じた<b>現金からデジタル決済への移行</b>。",
     "solve":"<span class='en'>this ＋ 名詞</span>は直前までの内容を要約して指す。話題は現金離れ。",
     "cut":"<span class='en'>a rise in bank fees</span> は本文に記述がなく、指示対象になりえない。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, which of the following is true about digital payments?",
     "choices":[
       "They leave records that make tax collection more transparent.",
       "They can be made only during bank opening hours.",
       "They require shoppers to carry small change.",
       "They raise the cost of counting and guarding cash."],"answer":"ア",
     "basis":"第2段 <span class='en'>a clear trail that makes tax collection and accounting more transparent</span> に一致。",
     "solve":"設問のキーワード（tax collection / transparent）を第2段後半で照合。",
     "cut":"『現金の警備費が上がる』は <span class='en'>reduce the cost of counting and guarding cash</span> と逆。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a danger of moving away from cash?",
     "choices":[
       "Digital payments raise the price of everyday goods.",
       "People without a bank account can be shut out of shops.",
       "Records of purchases raise questions about privacy.",
       "A network failure can leave people unable to buy food."],"answer":"ア",
     "basis":"『日用品の値段が上がる』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。第3段の危険（排除・プライバシー・障害）を消し、残る1つが答え。",
     "cut":"口座なしの締め出し・プライバシー・障害での買い物不能は、いずれも第3段に一致するので危険として『述べられている』。"},
    {"no":38,"tag":"内容真偽","stem":"According to paragraph 4, on what point do optimists and critics agree?",
     "choices":[
       "The change is arriving faster than the rules meant to govern it.",
       "Digital money is less safe than cash.",
       "Cash should be banned immediately.",
       "Banks are common in most poor regions."],"answer":"ア",
     "basis":"第4段末 <span class='en'>Both sides agree on one point: the change is arriving faster than the rules meant to govern it</span>。",
     "solve":"<span class='en'>Both sides agree</span> の直後が両者一致点。速度が規則を追い越している点。",
     "cut":"『貧しい地域に銀行は多い』は <span class='en'>banks are scarce</span> と矛盾する。"},
    {"no":39,"tag":"理由","stem":"Why do critics worry about a cashless society?",
     "choices":[
       "Because it gives great power to those who control the payment networks.",
       "Because it makes cash easier to steal.",
       "Because it forces every shop to accept notes.",
       "Because it slows down ordinary shopping."],"answer":"ア",
     "basis":"第4段 <span class='en'>it hands enormous power to the firms and states that control the payment networks</span>。",
     "solve":"<span class='en'>Critics reply that …</span> の直後が批判の中身。決済網を握る側への権力集中と監視。",
     "cut":"『現金が盗まれやすくなる』は楽観論の <span class='en'>safer than cash, harder to steal</span> と食い違い、批判の論拠でもない。"},
    {"no":40,"tag":"詳細","stem":"According to paragraph 4, why do optimists see digital money as useful in poor regions?","inline":True,
     "choices":[
       "Because banks are scarce there but phones are common.",
       "Because those regions have already banned cash.",
       "Because governments there pay people to use apps.",
       "Because notes and coins are printed locally."],"answer":"ア",
     "basis":"第4段 <span class='en'>financial inclusion in poor regions where banks are scarce but phones are common</span>。",
     "solve":"設問の <span class='en'>poor regions</span> を第4段で探し、その直後の理由節を読む。",
     "cut":"『すでに現金を禁止している』は本文に記述がなく、根拠にならない。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Cashless payment brings convenience and transparency but risks excluding people and eroding privacy, so its value depends on careful design.",
       "A cashless society has already made cash useless everywhere in the world.",
       "Digital payment is dangerous and should be stopped in every country.",
       "The only concern about going cashless is the speed of the internet."],"answer":"ア",
     "basis":"利点（2段）／弊害（3段）／賛否（4段）／設計の重要性（5段）／段階的移行という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点と弊害の併記＋<b>設計次第</b>という留保に沿う1つを残す。",
     "cut":"『現金を無用にした』『全面停止すべき』は言い過ぎ。『唯一の懸念は通信速度』は本文の論点をすり替えている。"},
  ],
  "structure":
    "<b>序論[1]</b>現金の消失とキャッシュレス化への期待 ／ <b>利点[2]</b>利便性・低コスト・記録の透明性 ／ "
    "<b>弊害[3]</b>非利用者の排除・プライバシー・システム障害 ／ <b>論争[4]</b>楽観論（安全・金融包摂）vs 批判（権力集中・監視） ／ "
    "<b>含意[5]</b>技術より設計が要（誰のための仕組みか） ／ <b>結論[6]</b>現金を残し段階的に移行（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "多くの国で、紙幣と硬貨が日常から静かに姿を消しつつある。買い物客はカードをかざしスマホを振り、"
    "お金は一瞬で口座から口座へ移る。政府や銀行はこの流れを歓迎し、一世代のうちに完全なキャッシュレス社会が"
    "来ると予測する者もいる。支持者は、それが普段の買い物にもたらす手軽さと速さを称賛する。",
    "最大の魅力は利便性だ。デジタル決済は素早く、両替も銀行への外出も要らず、ほぼどこからでも何時でも行える。"
    "企業にとって電子記録は現金を数え守る費用を減らし、税の徴収や会計をより透明にする明確な記録を残す。"
    "政府にとって、その同じ記録は、かつて見えないまま通り過ぎた賄賂や隠れた所得をあぶり出しうる。",
    "だが現金離れには現実の危険が伴う。何百万もの人は銀行口座もスマホも持たず、紙幣を拒む店はそうした客を締め出す。"
    "高齢者や低所得世帯はしばしば現金に頼るため、キャッシュレス化は彼らの排除を深めうる。"
    "あらゆるデジタル決済は、誰が何をどこでいつ買ったかを記録し、プライバシーに深刻な問いを投げかける。"
    "そして通信網が落ちたり停電したりすれば、純粋に電子的な仕組みは、誰もが食料さえ買えない状態を招きうる。",
    "この移行が社会に何を意味するかで、専門家の見解は割れている。楽観論者は、デジタルマネーは現金より安全で盗みにくく、"
    "銀行が乏しくスマホが普及した貧しい地域では金融包摂の強力な道具だと論じる。批判者は、それは決済網を握る企業や国家に"
    "巨大な権力を与え、あらゆる取引を追跡できる社会は重要な種類の自由を失いうると反論する。"
    "両者が一致するのは一点――変化は、それを律するはずの規則より速く到来している、ということだ。",
    "政策立案者にとって、仕組みの設計は技術そのものと同じくらい重要だ。若者と接続環境のある人だけに作られた網は"
    "そうでない人を罰する一方、オフラインの手段を保証し個人データを守る網は、恩恵をはるかに広く行き渡らせられる。"
    "問いは、キャッシュレスにするか否かではなく、どのように、そして誰のために、なのだ。",
    "こうした理由から、多くの経済学者は急な飛躍ではなく段階的な道を勧める。デジタル決済が伸びてもなお、"
    "現金を後ろ盾として残しておくことは、弱い立場の人を守り、機械が壊れる日に備える。"
    "キャッシュレス社会が人々を自由にするのか、それとも静かに囲い込むのかは、変化の速さよりも、"
    "それがどれだけ丁寧に設計されるかにかかっているのかもしれない。",
  ],
  "vocab": [
    ("cashless","形","現金を使わない、キャッシュレスの"),
    ("digital payment","名","電子決済、デジタル決済"),
    ("transaction","名","取引、決済"),
    ("transparent","形","透明な、明朗な"),
    ("financial inclusion","名","金融包摂（誰もが金融を使える状態）"),
    ("exclusion","名","排除、締め出し"),
    ("privacy","名","私生活、プライバシー"),
    ("backstop","名","後ろ盾、最後の支え"),
    ("vulnerable","形","弱い立場の、被害を受けやすい"),
    ("gradual","形","段階的な、緩やかな"),
    ("govern","動","律する、統治する"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／詳細／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点と弊害の併記＋<b>設計次第という留保</b>を選ぶ。",
}
