# -*- coding: utf-8 -*-
"""大問Ⅱ READING 08 ― 老舗企業とイノベーションのジレンマ。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "老舗企業とイノベーションのジレンマ ― 成功が生む失敗",
  "genre": "ビジネス／経営 論説",
  "limit": "目標18分",
  "wordcount": 473,
  "passage_title": "The Innovator's Dilemma",
  "passage": [
    "For decades, a handful of giant companies seemed unbeatable. They had loyal customers, deep pockets, and "
    "factories that ran like clockwork. The bigger and more admired such a company grew, the safer its future "
    "appeared to be. Yet history is full of firms that [[u:14]]fell behind[[/u]] almost overnight, overtaken by "
    "smaller rivals nobody had feared. This puzzle — why hard-won success can quietly breed failure — is what "
    "scholars call the innovator's dilemma.",

    "The root of the problem is not laziness but discipline. A well-run firm listens closely to its most valuable "
    "customers and pours resources into the products those customers already prize. Managers naturally "
    "[[u:15]]allocate[[/u]] money to projects with clear, near-term returns, and they [[u:16]]shy away from[[/u]] "
    "risky bets that promise almost nothing today. Rewards, budgets, and promotions all reinforce the same "
    "caution. By every ordinary measure, this looks like sound, responsible management — and for a while it truly is.",

    "Concentration has genuine strengths, and it would be foolish to deny them. A company that focuses on what it "
    "does best can cut costs, refine quality, and defend its lead against imitators. Sharpening a single edge "
    "often [[u:17]]yields[[/u]] steadier profits than scattering scarce effort across a dozen uncertain ideas. "
    "Investors, too, reward firms that tell a simple, focused story. Focus, in short, is not a weakness but a "
    "discipline that has made countless businesses rich.",

    "But the very same focus can harden into a trap. Disruptive technologies usually arrive looking crude, cheap, "
    "and unprofitable — hardly worth a great company's attention. Because they serve tiny, marginal markets at "
    "first, established firms [[u:18]]dismiss[[/u]] them as toys and hand them to the low end without a fight. By "
    "the time the newcomer improves enough to threaten the core business, the leader has [[u:19]]squandered[[/u]] "
    "its head start, and catching up proves far harder than it ever looked from a distance.",

    "The way out, many argue, is self-disruption: attacking your own business before an outsider does. This "
    "demands that a firm sometimes [[b:21]] the very products that made it famous, funding a rival team inside its "
    "own walls and letting it compete freely. Such courage is rare. Had most incumbents been willing to "
    "cannibalize their own profits early, they [[b:22]] the very disruption they later suffered. Instead, the fear "
    "of hurting this year's earnings [[u:20]]blinds[[/u]] them to next decade's threat.",

    "None of this means that focus is a mistake or that firms should chase every shiny novelty. Abandoning a "
    "proven strength is genuinely dangerous, and many predicted disruptions never materialize at all. The hard "
    "truth is that leaders must hold two ideas at once: defend the core that pays today's bills, yet keep the "
    "nerve to let part of it go tomorrow. Whether an established company survives the next wave may depend less on "
    "how much it already knows than on how bravely it is willing to unlearn.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>fell behind</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["lost ground","pulled ahead","stood firm","broke even"],"answer":"ア",
     "basis":"<span class='en'>fall behind</span>＝「遅れをとる、後れる」。<span class='en'>lose ground</span>（地歩を失う）が同義。",
     "solve":"直後の <span class='en'>overtaken by smaller rivals</span>（小さな競合に追い抜かれた）から『遅れをとる』と判断。",
     "cut":"<span class='en'>pulled ahead</span>（先んじる）・<span class='en'>stood firm</span>（踏みとどまる）は逆方向。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>allocate</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["distribute","withhold","borrow","waste"],"answer":"ア",
     "basis":"<span class='en'>allocate</span>＝「（資源・資金を）割り当てる、配分する」。<span class='en'>distribute</span> が近い。",
     "solve":"<span class='en'>allocate money to projects</span>（案件に資金を回す）という文脈。",
     "cut":"<span class='en'>withhold</span>（出し惜しむ）は逆。<span class='en'>waste</span>（浪費する）は否定的含意が過剰。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>shy away from</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["avoid","rush into","insist on","account for"],"answer":"ア",
     "basis":"<span class='en'>shy away from</span>＝「〜を避ける、尻込みする」。<span class='en'>avoid</span> が同義。",
     "solve":"<span class='en'>risky bets that promise almost nothing today</span>（今日ほぼ見返りのない賭け）を『避ける』流れ。",
     "cut":"<span class='en'>rush into</span>（飛び込む）は真逆。<span class='en'>insist on</span>（固執する）も文意に合わない。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>yields</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["produces","consumes","delays","hides"],"answer":"ア",
     "basis":"<span class='en'>yield</span>（他動詞）＝「（利益などを）生む、もたらす」。<span class='en'>produce</span> が同義。",
     "solve":"<span class='en'>yields steadier profits</span>（より安定した利益を生む）から『生み出す』意。",
     "cut":"<span class='en'>yield</span> には『屈する・譲る』の自動詞用法もあるが、ここは目的語 <span class='en'>profits</span> をとる他動詞。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>dismiss</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["brush off","take up","hold onto","look into"],"answer":"ア",
     "basis":"<span class='en'>dismiss</span>＝「（取るに足らぬものとして）退ける、軽視する」。<span class='en'>brush off</span> が近い。",
     "solve":"<span class='en'>dismiss them as toys</span>（おもちゃとして退ける）から『まともに取り合わない』意。",
     "cut":"<span class='en'>take up</span>（取り上げる）・<span class='en'>look into</span>（調べる）は逆に関心を向ける動き。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>squandered</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["wasted","secured","doubled","regained"],"answer":"ア",
     "basis":"<span class='en'>squander</span>＝「無駄にする、浪費する」。<span class='en'>waste</span> が同義。",
     "solve":"<span class='en'>squandered its head start</span>（先行の利を無駄にした）＝せっかくの優位を失う。",
     "cut":"<span class='en'>secured</span>（確保した）・<span class='en'>regained</span>（取り戻した）は逆方向。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>blinds ... to</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["keeps them from seeing","opens their eyes to","warns them about","points them toward"],"answer":"ア",
     "basis":"<span class='en'>blind A to B</span>＝「AにBが見えなくさせる」。『気づけなくする』意。",
     "solve":"<span class='en'>the fear ... blinds them to next decade's threat</span>「恐れが将来の脅威を見えなくする」。",
     "cut":"<span class='en'>opens their eyes to</span>（気づかせる）・<span class='en'>warns them about</span>（警告する）は逆。"},
    {"no":21,"tag":"E 語法/仮定法現在","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["abandon","abandons","abandoned","to abandon"],"answer":"ア",
     "basis":"<span class='en'>demand that ...</span> の <span class='en'>that</span> 節は<b>仮定法現在</b>で<b>原形</b>（should 省略）。主語が三人称単数でも <span class='en'>s</span> は付かない。",
     "solve":"<span class='en'>This demands that a firm sometimes abandon the very products ...</span>「企業が…を捨てることを求める」。",
     "cut":"三単現に引かれた <span class='en'>abandons</span> は不可。<span class='en'>to abandon</span> は節の動詞になれない。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would have avoided","will avoid","avoided","would avoid"],"answer":"ア",
     "basis":"文頭 <span class='en'>Had most incumbents been ...</span> は <span class='en'>If most incumbents had been</span> の倒置＝<b>仮定法過去完了</b>。帰結節は <span class='en'>would have + 過去分詞</span>。",
     "solve":"「もし早期に自らの利益を食い潰す覚悟があったなら、後に被った破壊を<b>避けられていただろう</b>」。",
     "cut":"<span class='en'>would avoid</span>（仮定法過去）は過去完了の条件節と時制が不一致。"},
    {"no":23,"tag":"D 情報整序","stem":"第4段で述べられる破壊的技術と老舗企業の展開を、本文の論理に沿って正しい順に並べたものを選べ。"
        "　(あ)老舗企業がそれをおもちゃとして退ける　(い)破壊的技術が粗削りで安価な姿で現れる　"
        "(う)新参者が中核事業を脅かすまで改良される　(え)先行企業が先行の利を無駄にする",
     "choices":["い → あ → う → え","あ → い → え → う","う → え → い → あ","い → う → あ → え"],"answer":"ア",
     "basis":"第4段は『技術が粗削りで現れる(い)→老舗が退ける(あ)→新参者が脅威になるまで改良(う)→先行企業が優位を失う(え)』の順。",
     "solve":"<span class='en'>By the time the newcomer improves ...</span> の前後で時間関係を確定し、最初(い)と最後(え)を固定して挟み撃ち。",
     "cut":"『退ける(あ)』は『改良され脅威になる(う)』より前。順序を逆にした選択肢を切る。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "老舗企業が新技術に乗り遅れる主な原因は、経営者の怠慢である。",
       "選択と集中は、模倣者に対する優位を守るのに役立つ。",
       "破壊的技術は当初、粗削りで安価に見えることが多い。",
       "経営者は明確で短期的な利益が見込める案件に資金を回しがちである。"],
     "answer":"ア",
     "basis":"第2段 <span class='en'>The root of the problem is not laziness but discipline</span>（原因は怠惰ではなく規律）と矛盾。",
     "solve":"設問の『合致しない』に印。原因を『怠慢』とする選択肢は本文の <span class='en'>not laziness but discipline</span> に真っ向から反する。",
     "cut":"他の3つ（優位の防衛／粗削りで安価／短期利益への配分）はそれぞれ第3・4・2段に一致。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "破壊的技術は当初、小さく限られた市場しか相手にしないことが多い。",
       "筆者は、企業はあらゆる新規事業に飛びつくべきだと述べている。",
       "選択と集中は経営上の明確な誤りである。",
       "老舗企業は常に破壊的技術をいち早く取り入れてきた。"],
     "answer":"ア",
     "basis":"第4段 <span class='en'>they serve tiny, marginal markets at first</span> と一致。",
     "solve":"本文の該当文を特定して照合。",
     "cut":"『あらゆる新規事業に飛びつくべき』は第6段 <span class='en'>should chase every shiny novelty</span> の否定と矛盾。"
           "『選択と集中は明確な誤り』は第3段の <span class='en'>genuine strengths</span> と逆。『常にいち早く取り入れてきた』は本文の主張と正反対。"},
    {"no":26,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "自己破壊とは、外部の競合より先に自社の事業を攻めることを指す。",
       "予想された破壊は必ず現実になる。",
       "焦点を絞ることは投資家から嫌われる。",
       "既存の強みを捨てることには全く危険がない。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>self-disruption: attacking your own business before an outsider does</span> と一致。",
     "solve":"用語の定義文（コロンの直後）を照合する。",
     "cut":"『破壊は必ず現実になる』は第6段 <span class='en'>many predicted disruptions never materialize</span> と矛盾。"
           "『投資家に嫌われる』は第3段 <span class='en'>Investors ... reward firms that tell a ... focused story</span> と逆。『全く危険がない』は第6段 <span class='en'>genuinely dangerous</span> と矛盾。"},
    {"no":27,"tag":"F 指示語","stem":"第4段の <span class='en'>established firms dismiss them as toys</span> の <span class='en'>them</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["disruptive technologies（破壊的技術）","established firms（老舗企業）","loyal customers（忠実な顧客）","core businesses（中核事業）"],"answer":"ア",
     "basis":"直前の主語は <span class='en'>Disruptive technologies</span>。『老舗企業がそれらをおもちゃとして退ける』の『それら』＝破壊的技術。",
     "solve":"指示語は直前の複数名詞を確認。<span class='en'>Because they serve tiny ... markets, established firms dismiss them</span> の <span class='en'>they</span>／<span class='en'>them</span> は同一物。",
     "cut":"<span class='en'>established firms</span> は『退ける』側であって退けられる対象ではない。"},
    {"no":28,"tag":"C 理由","stem":"本文によれば、多くの老舗企業が自己破壊（外部より先に自らの事業を攻めること）に踏み切れないのはなぜか。最も適切なものを選べ。",
     "choices":[
       "今年の収益が損なわれることを恐れるから。",
       "破壊的技術が高価すぎて手が出せないから。",
       "顧客が新技術を全く求めていないから。",
       "政府の規制によって新規事業が禁じられているから。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>the fear of hurting this year's earnings blinds them to next decade's threat</span>。",
     "solve":"『自己破壊は勇気が要る（<span class='en'>Such courage is rare</span>）』の理由を、直後の <span class='en'>fear of hurting this year's earnings</span> と結ぶ。",
     "cut":"『技術が高価すぎる』は本文と逆（破壊的技術は <span class='en'>cheap</span>）。『顧客が全く求めない』『政府の規制』は本文に記述がない。"},
    {"no":29,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "選択と集中は強みである一方で破壊的技術を見落とす罠にもなり、企業には中核を守りつつ強みを手放す勇気（自己破壊）が要る。ただし焦点そのものが誤りなのではない。",
       "焦点を絞る経営は誤りであり、企業はあらゆる新技術に投資すべきである。",
       "破壊的技術は取るに足らず、老舗企業がそれを恐れる必要はない。",
       "企業の存続は、その企業が保有する知識の量だけで決まる。"],
     "answer":"ア",
     "basis":"強み（3段）／罠（4段）／自己破壊という核心（5段）／焦点は誤りではないという留保（6段）という論の全体像に一致。",
     "solve":"主旨は『言い過ぎ・本文にない要素』を切り、筆者の両論併記＋留保に沿う1つを残す。",
     "cut":"『焦点を絞る経営は誤り』『あらゆる新技術に投資すべき』は断定しすぎ(too broad)で第6段の留保と矛盾。"
           "『破壊的技術を恐れる必要はない』は第4段の警告と逆。『知識の量だけで決まる』は第6段 <span class='en'>less on how much it knows than on how bravely it is willing to unlearn</span> と矛盾。"},
  ],
  "structure":
    "<b>序論[1]</b>強大な老舗が突然崩れる謎＝innovator's dilemma ／ <b>本論(原因)[2]</b>怠惰ではなく規律・短期利益への最適化 ／ "
    "<b>本論(選択と集中)[3]</b>焦点の強み（コスト・品質・優位の防衛） ／ <b>反論[4]</b>その焦点が破壊的技術を見落とす罠になる ／ "
    "<b>核心[5]</b>self-disruption（自己破壊）＝外部より先に自らを攻める勇気 ／ <b>結論[6]</b>焦点自体は誤りでない・中核防衛と自己破壊の両立という留保。"
    "　――『強み→罠→核心→留保』の典型構造。主旨問題はこの<b>両論併記＋留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "何十年もの間、一握りの巨大企業は無敵に見えた。忠実な顧客、潤沢な資金、そして時計仕掛けのように動く工場を"
    "持っていた。そうした企業が大きく称賛されるほど、その将来はいっそう安泰に見えた。だが歴史には、誰も恐れて"
    "いなかった小さな競合に追い抜かれ、ほとんど一夜にして遅れをとった企業があふれている。なぜ苦労して得た成功が"
    "静かに失敗を生むのか――この謎を学者たちは「イノベーターのジレンマ」と呼ぶ。",
    "問題の根は怠惰ではなく規律にある。よく運営された企業は最も価値ある顧客の声に丁寧に耳を傾け、その顧客が"
    "すでに重んじる製品に資源を注ぐ。経営者は当然、明確で短期的な見返りのある案件に資金を割り当て、今日ほとんど"
    "見返りのない危険な賭けからは尻込みする。報酬も予算も昇進も、同じ慎重さを強化する。あらゆる通常の尺度で見れば、"
    "これは健全で責任ある経営に見える――そして実際、しばらくの間はまさにそうなのだ。",
    "選択と集中には確かな強みがあり、それを否定するのは愚かだろう。最も得意なことに焦点を絞る企業は、コストを"
    "下げ、品質を磨き、模倣者に対して優位を守れる。一つの刃を研ぐことは、乏しい労力を十指に余る不確かなアイデアに"
    "ばらまくよりも、しばしば安定した利益を生む。投資家もまた、単純で焦点の定まった物語を語る企業を評価する。"
    "要するに焦点は弱みではなく、無数の企業を富ませてきた規律なのだ。",
    "だが、まさにその焦点が罠へと硬化しうる。破壊的技術はたいてい、粗削りで安価で儲からない姿で現れる――"
    "大企業がわざわざ注意を払う価値などなさそうに見える。当初は小さく取るに足らない市場しか相手にしないため、"
    "老舗企業はそれをおもちゃとして退け、抵抗もせず低価格帯を明け渡す。新参者が中核事業を脅かすほどに改良された"
    "頃には、先行企業は先行の利を無駄にしており、追いつくのは遠目に見えたよりもはるかに難しいと分かる。",
    "多くが説くその出口は「自己破壊」――外部の者が攻めてくる前に、自らの事業を攻めることだ。これは企業に、"
    "自社を有名にしたまさにその製品を時に捨て、自社内に競合チームを設けて自由に競わせることを求める。そんな勇気は"
    "まれだ。もし大半の既存企業が早期に自らの利益を食い潰す覚悟を持っていたなら、後に被ったまさにその破壊を"
    "避けられていただろう。だが実際には、今年の収益を損なう恐れが、次の十年の脅威を見えなくしてしまう。",
    "これは焦点を絞ることが誤りだとか、企業があらゆる目新しいものを追うべきだという意味ではない。実証済みの強みを"
    "捨てるのは本当に危険であり、予想された破壊の多くはまったく現実にならない。厳しい真実は、経営者が二つの考えを"
    "同時に抱かねばならないということだ――今日の勘定を払う中核を守りつつ、明日にはその一部を手放す胆力を保つ。"
    "老舗企業が次の波を生き延びられるかは、すでにどれだけ知っているかよりも、どれだけ勇敢に学びほぐそうとするかに"
    "かかっているのかもしれない。",
  ],
  "vocab": [
    ("fall behind","句動","遅れをとる、後れる"),
    ("breed","動","（結果を）生む、引き起こす"),
    ("allocate","動","割り当てる、配分する"),
    ("shy away from","句動","〜を避ける、尻込みする"),
    ("yield","動","（利益などを）生む、もたらす"),
    ("dismiss","動","退ける、軽視する"),
    ("disruptive","形","破壊的な、既存秩序を覆す"),
    ("squander","動","無駄にする、浪費する"),
    ("incumbent","名","既存企業、現職者"),
    ("cannibalize","動","（自社製品が）自社の売上を食う"),
    ("materialize","動","（予想などが）現実になる"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は時間・因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『強み→罠→核心(自己破壊)→留保』の型。<span class='en'>demand that</span>＋原形（仮定法現在）と、"
    "<span class='en'>Had S 過去分詞 ...</span>（仮定法過去完了の倒置）は頻出。主旨問題は必ず筆者の<b>留保</b>に沿う。",
}
