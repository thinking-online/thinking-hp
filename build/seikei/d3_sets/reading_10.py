# -*- coding: utf-8 -*-
"""大問Ⅲ READING 10 ― 遠隔医療（テレメディシン）。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "遠隔医療 ― 画面越しの診察",
  "genre": "医療／テクノロジー 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 443,
  "passage_title": "The Doctor on the Screen",
  "passage": [
    "Not long ago, seeing a doctor meant sitting in a crowded waiting room, sometimes for hours. Today a growing number "
    "of patients meet their physicians through a phone or a laptop instead. This practice, known as telemedicine, lets "
    "people describe their symptoms, receive advice, and even obtain prescriptions without leaving home. Supporters believe "
    "[[u:32]]it[[/u]] could reshape how ordinary healthcare is delivered.",

    "The clearest benefit is access. In rural areas, the nearest clinic may be a long and costly journey away, and "
    "specialists can be even harder to reach. A video call erases that distance in seconds. Telemedicine is also "
    "[[u:33]]convenient[[/u]] for busy people, who no longer need to take a whole day off work for a short consultation. "
    "For minor complaints and routine follow-ups, a brief online visit is often all that is required, and it "
    "spares the patient the cost and fatigue of travel as well.",

    "Yet a screen cannot capture everything. A skilled doctor gathers information not only from words but from a "
    "handshake, a patient walk across the room, or a faint change in color. Such [[u:34]]subtle[[/u]] clues are easily lost "
    "over a camera, and a physical examination is simply impossible from a distance. There is a real danger that a serious "
    "condition could be missed when the doctor cannot touch, tap, or listen directly.",

    "Access itself is uneven, too. The very people who might gain most from remote care are often the ones least able to "
    "use it. Older patients and poorer households may lack a fast connection, a suitable device, or the confidence to "
    "operate one. In this way telemedicine risks widening the digital divide it was meant to close, offering the greatest "
    "convenience to those who already enjoy good access to care.",

    "Doctors and policymakers are therefore [[u:35]]divided[[/u]] over how far the technology should go. Enthusiasts imagine "
    "a future in which most first visits happen online, freeing clinics for the cases that truly need them. Skeptics reply "
    "that medicine rests on trust, and that trust is built through presence — the reassurance of a face in the same room. "
    "Both sides agree on one point: convenience must never be confused with quality of care, and the choice of "
    "method should always follow the needs of the patient rather than the ease of the system.",

    "Telemedicine, then, is neither a cure-all nor a passing trend. It clearly extends care to people who were once left "
    "out, yet it cannot replace the human contact on which good diagnosis often depends. The wiser goal may be balance: "
    "using screens for what they do well, while keeping the clinic door open for the moments when only a physical presence "
    "will do.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (it could reshape) refer to?","inline":True,
     "choices":["telemedicine","a crowded waiting room","a prescription","a laptop"],"answer":"ア",
     "basis":"<span class='en'>Supporters believe it could reshape …</span> の <span class='en'>it</span> は直前の話題 <span class='en'>telemedicine</span>。",
     "solve":"代名詞は直前の主題へ。『それが医療の届け方を作り変えうる』の『それ』＝遠隔医療。",
     "cut":"<span class='en'>a crowded waiting room</span> は遠隔医療と対比される旧来の光景で逆。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“convenient”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["handy","expensive","dangerous","permanent"],"answer":"ア",
     "basis":"<span class='en'>convenient for busy people, who no longer need to take a whole day off</span>＝「手間がかからず<b>便利</b>」。",
     "solve":"丸一日休まずに済む＝好都合。<span class='en'>handy</span> が同義。",
     "cut":"<span class='en'>expensive</span>（高価）は便利さとは無関係で逆の含み。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“subtle”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["slight","obvious","loud","frequent"],"answer":"ア",
     "basis":"<span class='en'>a faint change in color … Such subtle clues are easily lost</span>＝「<b>かすかな</b>手がかり」。",
     "solve":"直前の <span class='en'>faint</span>（かすかな）と同方向。<span class='en'>slight</span> が同義。",
     "cut":"<span class='en'>obvious</span>（明白な）は反対で、カメラ越しに失われるという文脈に合わない。"},
    {"no":35,"tag":"言い換え","stem":"The word <span class='en'>“divided”</span> in paragraph 5 is closest in meaning to","inline":True,
     "choices":["in disagreement","in agreement","separated by distance","cut in half"],"answer":"ア",
     "basis":"<span class='en'>divided over how far the technology should go</span> の後に賛否両論が続く＝「意見が<b>割れている</b>」。",
     "solve":"直後に <span class='en'>Enthusiasts … Skeptics reply …</span> と対立が示される。<span class='en'>in disagreement</span> が同義。",
     "cut":"<span class='en'>in agreement</span>（合意）は対立の文脈と正反対。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, why is telemedicine especially useful in rural areas?",
     "choices":[
       "The nearest clinic can be a long and costly journey away.",
       "Rural patients dislike meeting doctors face to face.",
       "Country clinics have the newest medical equipment.",
       "Specialists prefer to live far from cities."],"answer":"ア",
     "basis":"第2段 <span class='en'>the nearest clinic may be a long and costly journey away … A video call erases that distance</span> に一致。",
     "solve":"設問語（rural）を第2段前半で照合し、距離の問題を解消する点を選ぶ。",
     "cut":"『対面が嫌い』は本文になく、遠隔が便利な理由は距離であって好みではない。"},
    {"no":37,"tag":"内容真偽","stem":"According to paragraph 3, what is a limitation of telemedicine?",
     "choices":[
       "A physical examination is impossible from a distance.",
       "Doctors can gather too much information from a camera.",
       "Video calls make patients look healthier than they are.",
       "Online visits always take longer than office visits."],"answer":"ア",
     "basis":"第3段 <span class='en'>a physical examination is simply impossible from a distance</span> に一致。",
     "solve":"『画面が捉えきれないもの』を述べる第3段で限界を探す。",
     "cut":"『カメラから情報を得すぎる』は、微妙な手がかりが<b>失われる</b>という記述と矛盾する。"},
    {"no":38,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a reason some patients cannot use telemedicine well?",
     "choices":[
       "They live too close to a hospital to qualify.",
       "They may lack a fast internet connection.",
       "They may not own a suitable device.",
       "They may lack the confidence to operate one."],"answer":"ア",
     "basis":"『病院に近すぎて対象外』は本文に記述がない。他の3つは第4段に明記。",
     "solve":"<span class='en'>NOT</span> に印。第4段の <span class='en'>a fast connection, a suitable device, or the confidence</span> を消し、残る1つが答え。",
     "cut":"回線が遅い・端末がない・操作に自信がないは、いずれも第4段に一致するので理由として『述べられている』。"},
    {"no":39,"tag":"詳細","stem":"According to paragraph 4, what problem might telemedicine make worse?",
     "choices":[
       "The digital divide between richer and poorer patients.",
       "The shortage of doctors in large cities.",
       "The cost of building new rural clinics.",
       "The length of hospital waiting rooms."],"answer":"ア",
     "basis":"第4段 <span class='en'>risks widening the digital divide it was meant to close</span>。",
     "solve":"設問語（make worse）を第4段の <span class='en'>widening</span> と結びつける。",
     "cut":"『都市の医師不足』は本文にない別の問題で、第4段の論点はデジタル格差。"},
    {"no":40,"tag":"理由","stem":"Why do skeptics doubt a future built mostly on online visits?",
     "choices":[
       "Because medicine rests on trust, which is built through presence.",
       "Because online visits are more expensive than office visits.",
       "Because clinics would have too few patients to survive.",
       "Because doctors dislike using new technology."],"answer":"ア",
     "basis":"第5段 <span class='en'>medicine rests on trust, and that trust is built through presence</span>。",
     "solve":"<span class='en'>Skeptics reply that …</span> の直後が懐疑論の中身。",
     "cut":"『費用が高い』は懐疑論の論拠として述べられておらず、主眼は信頼と対面。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Telemedicine widens access to care but cannot replace human contact, so a balance of online and in-person care is wiser.",
       "Telemedicine has already replaced the traditional clinic everywhere.",
       "Telemedicine should be banned because a screen misses subtle clues.",
       "Telemedicine benefits poorer and older patients more than anyone else."],"answer":"ア",
     "basis":"アクセス拡大（2段）／限界（3段）／格差（4段）／賛否（5段）／均衡という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点と弊害の両面＋<b>均衡</b>の留保に沿う1つを残す。",
     "cut":"『病院を完全に置き換えた』『全面禁止すべき』は言い過ぎ。『貧しい高齢者に最も恩恵』は第4段の記述と逆。"},
  ],
  "structure":
    "<b>序論[1]</b>遠隔医療の登場と『医療の届け方を変えうる』 ／ <b>利点[2]</b>アクセス拡大・多忙な人への利便 ／ "
    "<b>弊害[3]</b>画面では掴めない微妙な情報・触診の不可 ／ <b>弊害[4]</b>デジタル格差の拡大 ／ "
    "<b>論争[5]</b>推進派 vs 懐疑派（信頼は対面から） ／ <b>結論[6]</b>対面と遠隔の均衡が鍵（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "少し前まで、医者にかかるとは混み合った待合室に、ときに何時間も座ることを意味した。今日では、"
    "ますます多くの患者が代わりに電話やノートパソコンを通じて医師と会う。テレメディシン（遠隔医療）として知られるこの方法は、"
    "人々が家を出ずに症状を伝え、助言を受け、処方さえ得ることを可能にする。支持者は、それが日常的な医療の届け方を"
    "作り変えうると考えている。",
    "最も明白な利点はアクセスだ。地方では、最寄りの診療所まで長く費用のかかる移動が必要なこともあり、"
    "専門医にはさらに会いにくい。ビデオ通話はその距離を数秒で消し去る。テレメディシンは多忙な人にとっても便利で、"
    "短い診察のために丸一日仕事を休む必要がもうない。軽い不調や定期的な経過観察には、短いオンライン受診で足りることが多く、移動の費用や疲労を患者に負わせずに済む。",
    "だが画面はすべてを捉えられるわけではない。熟練した医師は言葉だけでなく、握手や、患者が部屋を横切る歩き方、"
    "あるいはかすかな顔色の変化からも情報を集める。そうした微妙な手がかりはカメラ越しに容易に失われ、"
    "身体診察は遠隔からはそもそも不可能だ。医師が直接触れ、叩き、聴くことができないとき、"
    "重篤な状態が見逃されうるという現実的な危険がある。",
    "アクセスそのものも一様ではない。遠隔医療から最も恩恵を受けうる当の人々が、しばしばそれを最も使えない人々でもある。"
    "高齢の患者や貧しい世帯は、速い回線や適した端末、あるいはそれを操作する自信を欠いているかもしれない。"
    "こうしてテレメディシンは、本来埋めるはずだったデジタル格差をむしろ広げ、"
    "すでに良い医療アクセスを享受している人々に最大の利便を与える恐れがある。",
    "それゆえ医師や政策立案者は、この技術をどこまで進めるべきかで意見が割れている。"
    "熱心な推進派は、初診の大半がオンラインで行われ、本当に必要な症例のために診療所を空ける未来を思い描く。"
    "懐疑派は、医療は信頼の上に成り立ち、その信頼は存在――同じ部屋にある顔がもたらす安心――を通じて築かれると反論する。"
    "両者が一致するのは一点――利便を医療の質と決して混同してはならず、方法の選択は制度の都合ではなく"
    "常に患者の必要に従うべきだ、という点だ。",
    "つまりテレメディシンは万能薬でも一時の流行でもない。それはかつて取り残された人々に医療を明らかに広げるが、"
    "良い診断がしばしば依拠する人と人との接触に取って代わることはできない。より賢明な目標は均衡かもしれない――"
    "画面が得意なことには画面を使い、身体的な存在だけが役立つ瞬間のためには診療所の扉を開けておくことだ。",
  ],
  "vocab": [
    ("telemedicine","名","遠隔医療、オンライン診療"),
    ("physician","名","医師"),
    ("prescription","名","処方（箋）"),
    ("consultation","名","診察、相談"),
    ("convenient","形","便利な、好都合な"),
    ("subtle","形","かすかな、微妙な"),
    ("physical examination","名","身体診察、触診"),
    ("digital divide","名","デジタル格差"),
    ("skeptic","名","懐疑派、懐疑論者"),
    ("presence","名","（その場にいる）存在、臨在"),
    ("cure-all","名","万能薬"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点と弊害の両面併記＋<b>均衡（留保）</b>を選ぶ。",
}
