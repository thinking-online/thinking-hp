# -*- coding: utf-8 -*-
"""大問Ⅱ READING 07 ― 人工知能と雇用の未来。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "人工知能と雇用の未来 ― 脅威か好機か",
  "genre": "科学技術／社会 論説",
  "limit": "目標18分",
  "wordcount": 490,
  "passage_title": "Machines That Learn to Work",
  "passage": [
    "A generation ago, the office computer was little more than a faster typewriter. Today, artificial intelligence can draft "
    "reports, sort job applications, and answer customer questions without human help. Machines that once merely followed orders "
    "now [[u:14]]do away with[[/u]] whole categories of routine labour, and the change is spreading through factories, banks, and "
    "hospitals alike. What began as a tool for a handful of specialists has quietly become a force that reshapes the very nature "
    "of work — and few industries expect to be left untouched.",

    "The economic case for automation is hard to ignore. Software never tires, rarely errs, and works around the clock. When "
    "algorithms [[u:15]]take over[[/u]] the most [[u:16]]tedious[[/u]] parts of a job — copying figures, scanning documents, "
    "tracking shipments — output rises while costs fall. Firms that adopt these systems early can serve more customers with "
    "fewer staff, and the savings they make often flow into lower prices or fresh investment.",

    "Supporters insist that workers gain as well. By handing dull duties to machines, companies can [[u:17]]free up[[/u]] their "
    "employees for tasks that demand judgement, empathy, or imagination — the very things software still does poorly. History "
    "offers some comfort here: earlier waves of mechanisation destroyed particular jobs yet created others that nobody had "
    "foreseen, from software design to logistics management. Seen in this light, AI looks less like a replacement for people "
    "than like a demanding new partner.",

    "Yet the optimists may be moving too fast. Unlike past machines, which mainly replaced muscle, today's systems increasingly "
    "rival the mind, threatening clerks, translators, and even junior lawyers. Much is [[u:18]]at stake[[/u]]: when automation "
    "strikes a workplace, its gains tend to gather at the top, while displaced workers struggle to find equally secure jobs. "
    "Economists warn that the technology could [[u:19]]widen[[/u]] the gap between those who own the machines and those who once "
    "competed with them.",

    "This is why reskilling has become the heart of the debate. Teaching a laid-off cashier to write code [[b:21]] little if the "
    "training is too short or too shallow to lead anywhere real. Governments and firms therefore face a hard question about who "
    "should pay for lifelong learning. Had earlier industrial societies left workers to [[u:20]]keep pace with[[/u]] change "
    "entirely on their own, the disruption [[b:22]] far greater than it eventually turned out to be. Technology alone, in short, "
    "decides nothing.",

    "Whether AI proves a threat or an opportunity, then, may hinge less on the technology itself than on the human choices that "
    "surround it. Well-designed schools, fair tax rules, and generous retraining programmes can turn automation into shared "
    "progress; neglect and short-term thinking can just as easily turn it into a fresh source of resentment. The machines are "
    "not writing our future for us. We still are — provided we decide, in good time, how to share the wealth they help to produce.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>do away with</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["eliminate","rely on","take up","hand over"],"answer":"ア",
     "basis":"<span class='en'>do away with</span>＝「〜を廃止する、なくす」。<span class='en'>eliminate</span> が同義。",
     "solve":"目的語 <span class='en'>whole categories of routine labour</span>（定型労働のまるごとの分野）と結び『消し去る』意。",
     "cut":"<span class='en'>rely on</span>（頼る）・<span class='en'>take up</span>（始める）は逆または無関係。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>take over</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["assume control of","give up","fall behind","break down"],"answer":"ア",
     "basis":"<span class='en'>take over</span>＝「〜を引き継ぐ、支配する」。",
     "solve":"『アルゴリズムが最も退屈な作業を<b>肩代わりする</b>』文脈。直後の <span class='en'>output rises</span> とも整合。",
     "cut":"<span class='en'>give up</span>（放棄する）は逆。<span class='en'>break down</span>（故障する）は文意に合わない。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>tedious</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["monotonous","challenging","rewarding","urgent"],"answer":"ア",
     "basis":"<span class='en'>tedious</span>＝「退屈な、単調な」。<span class='en'>monotonous</span> が同義。",
     "solve":"具体例 <span class='en'>copying figures, scanning documents</span>（数字の書き写し・書類の読み取り）が単調作業を示す。",
     "cut":"<span class='en'>rewarding</span>（やりがいのある）・<span class='en'>challenging</span>（骨の折れる）は方向違い。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>free up</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["make available","tie down","lay off","hand over"],"answer":"ア",
     "basis":"<span class='en'>free up</span>＝「（人・時間など）を解放して使えるようにする」。",
     "solve":"『退屈な仕事を機械に任せ、従業員を判断力の要る仕事に<b>振り向ける</b>』文脈。",
     "cut":"<span class='en'>lay off</span>（解雇する）は本文の趣旨（人を別の仕事へ）と別物。<span class='en'>tie down</span>（縛りつける）は逆。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>at stake</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["at risk","under control","for sale","on display"],"answer":"ア",
     "basis":"<span class='en'>at stake</span>＝「危険にさらされて、賭けられて」。<span class='en'>at risk</span> が同義。",
     "solve":"直後のコロン以下『格差の拡大・不安定な職』という危うい内容が『多くが<b>かかっている</b>』意を裏づける。",
     "cut":"<span class='en'>under control</span>（制御下）は文意と矛盾。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>widen</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["enlarge","narrow","close","cross"],"answer":"ア",
     "basis":"<span class='en'>widen the gap</span>＝「格差を広げる」。<span class='en'>enlarge</span> が近い。",
     "solve":"『機械を所有する者と機械と競わされた者の<b>格差を拡大</b>しうる』という警告。",
     "cut":"<span class='en'>narrow</span>（狭める）・<span class='en'>close</span>（縮める）は真逆。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>keep pace with</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["keep up with","fall short of","catch sight of","do without"],"answer":"ア",
     "basis":"<span class='en'>keep pace with</span>＝「〜に遅れずついていく」。<span class='en'>keep up with</span> が同義。",
     "solve":"『労働者を自力で変化に<b>ついていかせる</b>』文脈。",
     "cut":"<span class='en'>fall short of</span>（及ばない）・<span class='en'>do without</span>（なしで済ます）は意味がずれる。"},
    {"no":21,"tag":"E 語法","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["means","mean","meaning","to mean"],"answer":"ア",
     "basis":"主語は動名詞句 <span class='en'>Teaching a laid-off cashier to write code</span>＝<b>単数扱い</b>。現在の一般論で三単現。",
     "solve":"<span class='en'>Teaching ... means little if the training is too short</span>「〜を教えても、研修が短すぎれば<b>ほとんど意味がない</b>」。",
     "cut":"動名詞主語を複数と誤り <span class='en'>mean</span> を選ばない。<span class='en'>meaning/to mean</span> では述語動詞にならない。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would have been","will be","had been","would be"],"answer":"ア",
     "basis":"文頭 <span class='en'>Had earlier industrial societies left ...</span> は <span class='en'>If they had left</span> の倒置＝<b>仮定法過去完了</b>。帰結節は <span class='en'>would have + 過去分詞</span>。",
     "solve":"「もし過去の産業社会が労働者を自力任せにしていたら、混乱は実際よりはるかに大きかった<b>だろう</b>」。",
     "cut":"<span class='en'>would be</span>（仮定法過去）は時制が過去完了の条件節と不一致。<span class='en'>will be</span> は仮定法でない。"},
    {"no":23,"tag":"D 情報整序","stem":"第4段が描く自動化の影響を、本文の論理に沿って正しい順に並べたものを選べ。"
        "　(あ)離職した労働者が同等に安定した職を探して苦労する　(い)自動化が職場を襲う　(う)利益は上層に集まりやすい　(え)所有者と労働者の格差が広がりうる",
     "choices":["い → う → あ → え","え → い → う → あ","い → あ → う → え","う → い → あ → え"],"answer":"ア",
     "basis":"第4段は『自動化が襲う(い)→利益は上に集まる(う)→離職者は職探しに苦労(あ)→格差が広がりうる(え)』の順。",
     "solve":"<span class='en'>when automation strikes ... while displaced workers struggle</span> の因果と、最後の <span class='en'>widen the gap</span> で末尾(え)を固定して挟み撃ち。",
     "cut":"『格差が広がる(え)』は結論的な帰結なので先頭に置けない。冒頭を(え)や(う)にした並びを切る。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "今日のAIは主に筋力を代替し、頭脳労働にはほとんど及ばない。",
       "過去の機械化は特定の職を消す一方、誰も予期しなかった新しい職も生んだ。",
       "自動化を早く導入した企業は、より少ない人員で多くの顧客に対応できる。",
       "AIが脅威か好機かは技術そのものより人間の選択にかかっているかもしれない。"],
     "answer":"ア",
     "basis":"第4段 <span class='en'>Unlike past machines, which mainly replaced muscle, today's systems increasingly rival the mind</span>（今日の系は<b>頭脳</b>に迫る）と正反対。",
     "solve":"設問の『合致しない』に印。『筋力／頭脳』の対比を本文で照合すると、この選択肢だけが逆。",
     "cut":"他の3つ（機械化が新職を生む／早期導入で少人数対応／是非は人間の選択次第）はいずれも本文に一致。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "再教育は、研修が短すぎたり浅すぎたりすると効果が乏しい。",
       "ソフトウェアは判断力や共感を要する仕事を人間より得意とする。",
       "自動化による利益は労働者全体に均等に配分される傾向がある。",
       "筆者はAIが必ず社会全体の進歩をもたらすと結論づけている。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>the training is too short or too shallow to lead anywhere real</span> と一致。",
     "solve":"『再教育の質』に触れた文を特定して照合。",
     "cut":"『ソフトが判断・共感を得意』は第3段 <span class='en'>the very things software still does poorly</span> と矛盾。"
           "『利益が均等配分』は第4段 <span class='en'>gains tend to gather at the top</span> と逆。『必ず進歩をもたらす』は第6段の留保と矛盾。"},
    {"no":26,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "早期に自動化を導入した企業が生む節約は、値下げや新規投資に回ることがある。",
       "AIの普及によって、どの業界も影響を免れると筆者は述べている。",
       "過去の機械は主に人間の頭脳を代替してきた。",
       "再教育の費用を誰が負担すべきかは既に明確に決着している。"],
     "answer":"ア",
     "basis":"第2段 <span class='en'>the savings they make often flow into lower prices or fresh investment</span> と一致。",
     "solve":"『節約の使い道』に言及した文を照合。",
     "cut":"『どの業界も影響を免れる』は第1段 <span class='en'>few industries expect to be left untouched</span> と逆。"
           "『過去の機械が頭脳を代替』は第4段と矛盾。『費用負担が決着済み』は第5段 <span class='en'>a hard question about who should pay</span> と矛盾。"},
    {"no":27,"tag":"F 指示語","stem":"第4段末の <span class='en'>those who once competed with them</span> の <span class='en'>them</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["the machines（機械）","the owners（所有者）","the economists（経済学者）","the lawyers（弁護士）"],"answer":"ア",
     "basis":"<span class='en'>those who own the machines and those who once competed with them</span>＝『機械を<b>所有する者</b>と、かつて<b>機械</b>と競った者』。<span class='en'>them</span>＝機械。",
     "solve":"直前の名詞 <span class='en'>the machines</span> を確認。労働者は『機械と競った側』だから <span class='en'>them</span> は機械。",
     "cut":"所有者を指すと『所有者と競った者』となり、対比（所有者 vs 競わされた側）が崩れる。"},
    {"no":28,"tag":"C 理由","stem":"再教育（reskilling）が議論の中心になったのはなぜか。最も適切なものを選べ。",
     "choices":[
       "自動化で職を失う人が新しい仕事へ移るには、十分な質と長さの学び直しが要るから。",
       "ソフトウェアが判断や共感を要する仕事まで完全に代替してしまったから。",
       "企業が新規顧客をできるだけ多く集める必要に迫られているから。",
       "過去の機械化が新しい職を一切生まなかったから。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>reskilling has become the heart of the debate</span>＋<span class='en'>too short or too shallow to lead anywhere real</span>。自動化(第4段)で職を失う人の移行に十分な学び直しが要る。",
     "solve":"『reskilling が中心になった理由』を、直前の第4段（職の喪失・格差）と第5段（研修の質）で結ぶ。",
     "cut":"『ソフトが完全代替』は第3段 <span class='en'>does poorly</span> と矛盾。『新規顧客集め』『新職を一切生まなかった』は本文に根拠がない、または第3段と逆。"},
    {"no":29,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "AIは生産性を高める好機と職の喪失・格差という脅威を併せ持ち、その帰結は技術より再教育や制度設計など人間の選択にかかっている。",
       "AIは技術の進歩によって必ず社会全体を豊かにし、格差の心配は無用である。",
       "自動化は労働者から職を奪うだけの脅威であり、導入は止めるべきである。",
       "過去の機械化と同様、AIも新しい職を自動的に生むので何の対策も要らない。"],
     "answer":"ア",
     "basis":"好機（2・3段）／脅威（4段）／再教育という核心（5段）／是非は人間の選択次第（6段）という論全体に一致。",
     "solve":"主旨は『言い過ぎ・本文にない要素』を切り、筆者の両論併記＋留保に沿う1つを残す。",
     "cut":"『必ず豊かにする』『奪うだけ・導入を止めるべき』『何の対策も要らない』はいずれも一方に振れた断定(too broad)で、第6段の留保と合わない。"},
  ],
  "structure":
    "<b>序論[1]</b>AIが定型労働を代替し働き方を変える ／ <b>本論(経済)[2]</b>不眠不休・低コストで生産性向上 ／ "
    "<b>本論(労働者)[3]</b>退屈な仕事を機械へ、人は判断・共感の仕事へ ／ <b>反論[4]</b>頭脳労働まで脅かし格差を広げる影 ／ "
    "<b>核心[5]</b>reskilling（学び直し）こそ争点・費用負担の問い ／ <b>結論[6]</b>是非は技術より人間の選択次第（留保）。"
    "　――『好機→脅威→核心→留保』の典型的な論説構造。主旨問題はこの<b>留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "一世代前、オフィスのコンピュータは速いタイプライター程度のものでしかなかった。今日、人工知能は報告書を書き、"
    "求職書類を仕分けし、顧客の質問に人手を介さず答えられる。かつて命令に従うだけだった機械は、いまや定型労働の"
    "まるごとの分野を消し去り、その変化は工場、銀行、病院にひとしく広がっている。ひと握りの専門家の道具として"
    "始まったものは、静かに仕事の本質そのものを作り変える力となった――そして影響を免れると考える業界はほとんどない。",
    "自動化の経済的な理屈は無視しがたい。ソフトウェアは疲れず、めったに誤らず、二十四時間働く。アルゴリズムが"
    "最も退屈な作業――数字の書き写し、書類の読み取り、荷物の追跡――を肩代わりすると、生産量は上がり費用は下がる。"
    "こうした仕組みを早く導入した企業は、より少ない人員でより多くの顧客に対応でき、生み出した節約はしばしば"
    "値下げや新たな投資へと流れ込む。",
    "支持者は、労働者も同様に得をすると主張する。退屈な務めを機械に渡すことで、企業は従業員を、判断力や共感、"
    "想像力を要する仕事――ソフトウェアがいまだ苦手とするまさにその領域――に振り向けられる。歴史はいくらかの慰めを"
    "与える。以前の機械化の波は特定の職を壊した一方、ソフト設計から物流管理まで、誰も予期しなかった別の職を生んだ。"
    "この見方に立てば、AIは人の代替というより、手のかかる新しい相棒に見える。",
    "だが楽観論者は先を急ぎすぎているのかもしれない。主に筋力を代替した過去の機械と違い、今日の系はますます頭脳に"
    "迫り、事務員、翻訳者、さらには若手の弁護士までも脅かす。かかっているものは大きい。自動化が職場を襲うと、その"
    "利益は上層に集まりやすく、一方で職を失った労働者は同等に安定した職を見つけるのに苦労する。経済学者は、この技術が"
    "機械を所有する者と、かつて機械と競わされた者との格差を広げかねないと警告する。",
    "だからこそ再教育（学び直し）が議論の核心になった。解雇されたレジ係にコードの書き方を教えても、研修が短すぎたり"
    "浅すぎたりして先につながらなければ、ほとんど意味がない。政府と企業はそれゆえ、生涯学習の費用を誰が負担すべきかという"
    "難しい問いに直面する。もし過去の産業社会が労働者を自力だけで変化についていかせていたら、混乱は実際に起きた以上に"
    "はるかに大きかっただろう。要するに、技術だけでは何も決まらないのだ。",
    "したがって、AIが脅威となるか好機となるかは、技術そのものよりも、それを取り巻く人間の選択にかかっているのかも"
    "しれない。よく設計された学校、公正な税制、手厚い再訓練の制度は、自動化を分かち合える進歩へと変えうる。放置と"
    "近視眼的な思考は、それをたやすく新たな不満の源へと変えてしまう。機械が私たちの未来を書いているのではない。"
    "書いているのは今なお私たちだ――彼らが生み出す富をどう分かち合うかを、時を逃さず決めさえすれば。",
  ],
  "vocab": [
    ("do away with","句動","〜を廃止する、なくす"),
    ("take over","句動","〜を引き継ぐ、肩代わりする"),
    ("tedious","形","退屈な、単調な"),
    ("free up","句動","（人・時間）を解放して使えるようにする"),
    ("at stake","句","危険にさらされて、賭けられて"),
    ("displaced","形","（職などを）追われた"),
    ("widen the gap","句","格差を広げる"),
    ("reskilling","名","学び直し、再教育"),
    ("keep pace with","句","〜に遅れずについていく"),
    ("lifelong learning","句","生涯学習"),
    ("hinge on","句動","〜次第である、〜にかかっている"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『好機→脅威→核心→留保』の型。主旨問題は必ず筆者の<b>留保</b>"
    "（技術より人間の選択・制度設計次第）に沿う選択肢を選ぶ。",
}
