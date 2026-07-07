# -*- coding: utf-8 -*-
"""大問Ⅱ READING 04 ― 行動経済学とナッジ。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "行動経済学とナッジ ― 初期設定が選択を動かす",
  "genre": "経済／心理 論説",
  "limit": "目標18分",
  "wordcount": 480,
  "passage_title": "The Quiet Power of the Nudge",
  "passage": [
    "Classical economics long assumed that people [[u:14]]weigh up[[/u]] every option calmly and pick whatever serves them "
    "best. The assumption was tidy and convenient, but it rarely matched how ordinary shoppers, savers, and voters actually "
    "behave. Human beings are busy, distracted, and easily swayed by the way a choice is [[u:15]]laid out[[/u]] in front of "
    "them. Behavioral economics, the field that studies these quirks, argues that the arrangement of options—what scholars "
    "call choice architecture—can guide a decision as powerfully as the options themselves.",

    "Consider the humble default. When starting a new job, many workers never [[u:16]]get around to[[/u]] selecting a "
    "pension plan. If the paperwork enrols them automatically unless they say no, saving rates climb; if it asks them to "
    "sign up on their own, most drift away with nothing put aside. The same inertia explains why nations that register "
    "citizens as organ donors by default report far higher donation rates. A small change to the starting point "
    "[[u:17]]tips the scales[[/u]], yet no one loses the freedom to choose otherwise.",

    "These gentle prompts are known as nudges. A cafeteria that sets fruit at eye level and tucks sweets onto a low shelf "
    "steers diners toward healthier meals. A reminder noting that most neighbours have already paid their taxes on time "
    "quietly raises compliance. Because a nudge changes behaviour without banning anything or altering prices, governments "
    "and firms have embraced it as a cheap tool. Small design choices, repeated across millions of people, can add up to "
    "strikingly large social effects.",

    "Critics, however, are uneasy. A nudge works precisely because people do not notice it, and a technique that slips past "
    "conscious thought sits [[u:18]]at odds with[[/u]] the ideal of free, informed choice. If a designer can make us save "
    "more, the same lever could push us toward a pricier phone or a needless insurance policy. Who, the critics ask, "
    "decides what counts as our own good, and what stops a well-meaning nudge from sliding into quiet manipulation?",

    "The answer, many economists reply, [[b:21]] on transparency. A nudge that citizens can see, understand, and refuse "
    "does not steal their autonomy; it simply makes the wiser path easier to take. People stay free to [[u:19]]opt out[[/u]], "
    "and the reasoning behind the design is open to scrutiny. Had early programmes hidden their methods, public trust "
    "[[b:22]] and the whole approach might have collapsed. Openness, then, is not a mere courtesy but the very thing that "
    "separates a nudge from a trick.",

    "Whether nudging deserves praise or suspicion may depend less on the tool than on the hand that wields it. Used openly, "
    "it can help people [[u:20]]follow through on[[/u]] the very goals they already hold. Hidden away, the same technique "
    "becomes one more way for the powerful to bend the choices of the many. Perhaps the honest nudge is simply the one "
    "that, once noticed, its target would still gladly accept. That, at least, is the standard its defenders hope the "
    "field can meet.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・理由・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>weigh up</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["evaluate carefully","give up on","laugh at","hand over"],"answer":"ア",
     "basis":"<span class='en'>weigh up</span>＝「（各選択肢を）比較検討する、よく吟味する」。",
     "solve":"直後の <span class='en'>every option ... and pick whatever serves them best</span>（選択肢を比べて最善を選ぶ）から『吟味する』意。",
     "cut":"<span class='en'>give up on</span>（見限る）・<span class='en'>hand over</span>（手渡す）は文意に合わない。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>laid out</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["presented","hidden","destroyed","delayed"],"answer":"ア",
     "basis":"<span class='en'>lay out</span>＝「並べる、提示する」。ここは選択肢の『見せ方』。",
     "solve":"<span class='en'>the way a choice is laid out in front of them</span>（選択が目の前にどう提示されるか）から『提示される』。",
     "cut":"<span class='en'>hidden</span>（隠される）は逆方向。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>get around to</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["find the time to","refuse to","manage to avoid","forget how to"],"answer":"ア",
     "basis":"<span class='en'>get around to doing</span>＝「（後回しにしていたことに）ようやく着手する、時間をつくってする」。",
     "solve":"<span class='en'>never get around to selecting a pension plan</span>（年金選びに手をつけないまま）＝先延ばしの惰性。",
     "cut":"<span class='en'>refuse to</span>（拒む）は意図的拒否で、ここは単なる先送り。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>tips the scales</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["decisively influences the outcome","keeps everything balanced","measures the exact weight","removes all the risk"],"answer":"ア",
     "basis":"<span class='en'>tip the scales</span>＝「形勢を左右する、決め手となる」。天秤を傾ける比喩。",
     "solve":"<span class='en'>A small change to the starting point tips the scales</span>（初期設定の小さな変更が結果を左右）から『決定的に動かす』。",
     "cut":"<span class='en'>keeps everything balanced</span>（釣り合いを保つ）は真逆の比喩解釈。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>at odds with</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["in conflict with","in favour of","identical to","dependent on"],"answer":"ア",
     "basis":"<span class='en'>at odds with</span>＝「〜と対立して、相容れずに」。",
     "solve":"<span class='en'>slips past conscious thought sits at odds with ... free, informed choice</span>（意識を通らない手法は自由な選択の理想と相容れない）。",
     "cut":"<span class='en'>in favour of</span>（賛成して）は逆。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>opt out</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["choose to decline","join in eagerly","pay in advance","speak up loudly"],"answer":"ア",
     "basis":"<span class='en'>opt out</span>＝「参加しないことを選ぶ、抜ける、拒否する」。",
     "solve":"<span class='en'>People stay free to opt out</span>（人々は抜ける自由を保つ）＝提示された道を選ばない自由。",
     "cut":"<span class='en'>join in eagerly</span>（進んで参加）は <span class='en'>opt in</span> 側で逆。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>follow through on</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["carry out","give up on","object to","cover up"],"answer":"ア",
     "basis":"<span class='en'>follow through on</span>＝「（計画・目標を）最後までやり遂げる、実行に移す」。",
     "solve":"<span class='en'>help people follow through on the very goals they already hold</span>（本人が既に抱く目標を実行させる）。",
     "cut":"<span class='en'>give up on</span>（あきらめる）は逆。"},
    {"no":21,"tag":"E 語法","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["hinges","hinge","hinging","to hinge"],"answer":"ア",
     "basis":"主語は <span class='en'>The answer</span>＝<b>単数</b>。挿入句 <span class='en'>, many economists reply,</span> に惑わされない。現在の一般論なので三単現 <span class='en'>hinges</span>。",
     "solve":"<span class='en'>The answer ... hinges on transparency</span>「その答えは透明性にかかっている」。<span class='en'>hinge on</span>＝〜次第である。",
     "cut":"挿入句の複数名詞 <span class='en'>economists</span> につられて <span class='en'>hinge</span> を選ばない。主語は <span class='en'>The answer</span>。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would have evaporated","will evaporate","evaporated","would evaporate"],"answer":"ア",
     "basis":"文頭 <span class='en'>Had early programmes hidden ...</span> は <span class='en'>If early programmes had hidden</span> の倒置＝<b>仮定法過去完了</b>。帰結節は <span class='en'>would have + 過去分詞</span>。",
     "solve":"「もし初期のプログラムが手法を隠していたら、社会の信頼は<b>消え失せていただろう</b>」。後続 <span class='en'>might have collapsed</span> とも時制が一致。",
     "cut":"<span class='en'>would evaporate</span>（仮定法過去）は条件節の過去完了と不一致。"},
    {"no":23,"tag":"D 情報整序","stem":"第2段で説明される『初期設定（デフォルト）』の仕組みを、本文の論理に沿って正しい順に並べたものを選べ。"
        "　(あ)会社の書類が本人を自動的に加入させる　(い)労働者が新しい仕事を始める　(う)多くの人は年金プランを選ぶ手間をとらない　(え)貯蓄率が上がる",
     "choices":["い → う → あ → え","あ → い → う → え","う → い → あ → え","い → あ → え → う"],"answer":"ア",
     "basis":"第2段は『新しい仕事を始め(い)→年金選びを後回しにする(う)→書類が自動で加入させる(あ)→貯蓄率が上がる(え)』の因果順。",
     "solve":"<span class='en'>never get around to selecting</span>（後回し）が前提、<span class='en'>enrols them automatically ... saving rates climb</span>（自動加入→貯蓄増）が結果。最初(い)と最後(え)を固定して挟み撃ち。",
     "cut":"『自動加入(あ)』は『選ぶ手間をとらない(う)』の後に来る。順序を前に置く選択肢を切る。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "ナッジは商品の価格を変えたり選択肢を禁止したりすることで人々の行動を変える。",
       "初期設定で市民を臓器提供者として登録する国は、提供率がはるかに高い。",
       "自動加入方式にすると、労働者の貯蓄率は上がる傾向がある。",
       "批評家は、善意のナッジが操作へと滑り込む危険を懸念している。"],
     "answer":"ア",
     "basis":"第3段 <span class='en'>changes behaviour without banning anything or altering prices</span>（禁止も価格変更もせずに行動を変える）と矛盾。",
     "solve":"設問の『合致しない』に印。選択肢の手段（価格変更・禁止 vs 提示の工夫）を本文で照合。",
     "cut":"他の3つ（臓器提供の初期設定／自動加入で貯蓄増／操作への懸念）は第2・4段に一致。"
           "『価格を変えたり禁止したりして行動を変える』だけがナッジの定義（禁止も価格変更もしない）に反し誤り。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "市民に見え、理解でき、拒否できるナッジは自律を奪わず、賢明な道を選びやすくするだけだ。",
       "行動経済学は、人は常に合理的に自分にとって最善を選ぶと結論づけた。",
       "オプトイン方式のほうがオプトアウト方式より貯蓄率が高い。",
       "政府はナッジを高価で導入の難しい手段だとみなしている。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>A nudge that citizens can see, understand, and refuse does not steal their autonomy; it simply makes the wiser path easier to take</span> と一致。",
     "solve":"本文の該当文を特定して照合。",
     "cut":"『人は常に合理的に最善を選ぶ』は第1段 <span class='en'>rarely matched how ... actually behave</span> と矛盾。"
           "『オプトインの方が貯蓄率が高い』は第2段（自動加入=オプトアウト方式で貯蓄増）と逆。『高価』は第3段 <span class='en'>a cheap tool</span> と矛盾。"},
    {"no":26,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "初期設定を少し変えるだけで、選ぶ自由を奪わずに結果を大きく左右できる。",
       "ナッジが機能するのは、人々がそれにはっきり気づくからである。",
       "透明性はナッジにとって単なる礼儀にすぎない。",
       "初期のプログラムは手法を隠したことでかえって成功した。"],
     "answer":"ア",
     "basis":"第2段 <span class='en'>A small change to the starting point tips the scales, yet no one loses the freedom to choose otherwise</span> と一致。",
     "solve":"『自由を奪わず結果を左右』という核心をそのまま述べた選択肢を残す。",
     "cut":"『はっきり気づくから機能する』は第4段 <span class='en'>works precisely because people do not notice it</span> と逆。"
           "『単なる礼儀』は第5段 <span class='en'>not a mere courtesy but the very thing that separates a nudge from a trick</span> と矛盾。『手法を隠して成功』は第5段の仮定法（隠せば信頼は消えた）と矛盾。"},
    {"no":27,"tag":"F 指示語","stem":"最終段の <span class='en'>its target</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["the person being nudged（ナッジを受ける人）","the designer（設計者）","the government（政府）","the goal（目標）"],"answer":"ア",
     "basis":"<span class='en'>its</span>＝<span class='en'>the honest nudge</span>。『そのナッジの標的』＝ナッジを向けられる当人。",
     "solve":"<span class='en'>the honest nudge is ... the one that, once noticed, its target would still gladly accept</span>（気づいてもなお当人が喜んで受け入れる）。受け入れる主体＝人。",
     "cut":"設計者や政府はナッジを『仕掛ける側』で、受け入れる標的ではない。"},
    {"no":28,"tag":"C 理由","stem":"批評家がナッジに不安を覚えるのはなぜか。最も適切なものを選べ。",
     "choices":[
       "ナッジが意識的な思考を通らずに働き、自由で十分な情報に基づく選択という理想と相容れないから。",
       "ナッジの導入に多額の費用と高度な技術がかかるから。",
       "ナッジが必ず商品の価格を引き上げてしまうから。",
       "ナッジが多くの国で法律により禁止されているから。"],
     "answer":"ア",
     "basis":"第4段 <span class='en'>works precisely because people do not notice it</span>＋<span class='en'>sits at odds with the ideal of free, informed choice</span>。",
     "solve":"『however, are uneasy』の直後に続く理由（気づかれずに働く＝自由な選択と衝突）と結ぶ。",
     "cut":"『多額の費用』は第3段 <span class='en'>a cheap tool</span> と矛盾。『価格を引き上げる』『法律で禁止』は本文に記述がない。"},
    {"no":29,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "ナッジは貯蓄や健康を助けうるが操作や自律侵害の懸念も伴い、その是非は透明に使われるか否かにかかっている。",
       "行動経済学は、人が常に合理的に最善を選ぶことを証明した。",
       "ナッジは危険な操作の手段にすぎず、直ちに禁止すべきである。",
       "初期設定さえ工夫すれば、あらゆる社会問題は確実に解決できる。"],
     "answer":"ア",
     "basis":"利点（2・3段）／懸念（4段）／透明性という核心（5段）／是非は使い手次第という留保（6段）の全体像に一致。",
     "solve":"主旨は『言い過ぎ・本文にない要素』を切り、筆者の両論併記＋透明性の留保に沿う1つを残す。",
     "cut":"『常に合理的』は第1段と矛盾。『直ちに禁止すべき』『あらゆる問題を確実に解決』は断定しすぎ(too broad)で本文の留保と合わない。"},
  ],
  "structure":
    "<b>序論[1]</b>人は必ずしも合理的でなく、選択は提示（choice architecture）に左右される ／ "
    "<b>本論(初期設定)[2]</b>デフォルトが貯蓄・臓器提供を動かす（自由は奪わない） ／ "
    "<b>本論(応用)[3]</b>ナッジは安価で社会的効果大 ／ <b>反論[4]</b>意識を通らず自律・操作の懸念 ／ "
    "<b>核心[5]</b>透明性こそがナッジと策略を分ける ／ <b>結論[6]</b>是非は使い手の誠実さ次第（留保）。"
    "　――『利点→懸念→核心→留保』の典型構造。主旨問題はこの<b>留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "古典派経済学は長らく、人は各選択肢を冷静に比較し、自分に最も役立つものを選ぶと想定してきた。"
    "この想定は整然として便利だったが、普通の買い物客・貯蓄者・有権者が実際にどう振る舞うかとはほとんど一致しなかった。"
    "人間は忙しく、気を散らし、選択が目の前にどう提示されるかに簡単に左右される。こうした癖を研究する行動経済学は、"
    "選択肢の並べ方――学者が「選択の設計（choice architecture）」と呼ぶもの――が、選択肢そのものと同じくらい強く決定を導きうると論じる。",
    "ささやかな初期設定を考えてみよう。新しい仕事を始めるとき、多くの労働者は年金プランを選ぶことになかなか手をつけない。"
    "もし書類が、拒否しない限り自動的に加入させる仕組みなら貯蓄率は上がる。自分で申し込む方式なら、多くは何も積み立てないまま流されていく。"
    "同じ惰性は、初期設定で市民を臓器提供者として登録する国の提供率がはるかに高い理由も説明する。"
    "出発点をわずかに変えるだけで形勢は動く。それでいて、別の選択をする自由は誰からも失われない。",
    "こうした穏やかな後押しは「ナッジ」と呼ばれる。果物を目の高さに置き、菓子を低い棚に押し込む食堂は、"
    "客をより健康的な食事へと導く。「近所の大半はもう期限内に納税を済ませた」と告げる通知は、静かに納税率を高める。"
    "ナッジは何かを禁止したり価格を変えたりせずに行動を変えるため、政府も企業も安価な手段としてこれを取り入れてきた。"
    "小さな設計の選択も、何百万人にわたって繰り返されれば、驚くほど大きな社会的効果へと積み上がりうる。",
    "しかし批評家は落ち着かない。ナッジは人々がそれに気づかないからこそ機能するのであり、意識的な思考をすり抜ける手法は、"
    "自由で十分な情報に基づく選択という理想と相容れない。設計者が私たちにもっと貯蓄させられるなら、同じ梃子は、"
    "より高価なスマホや不要な保険へと私たちを押しやることもできる。何が私たち自身の利益に当たるのかを誰が決めるのか、"
    "そして善意のナッジが密かな操作へ滑り込むのを何が止めるのか、と批評家は問う。",
    "その答えは、と多くの経済学者は応じる――透明性にかかっている。市民が見て、理解し、拒否できるナッジは自律を奪わない。"
    "ただ、より賢明な道を選びやすくするだけだ。人々は抜ける自由を保ち、設計の背後にある理由は検証に開かれている。"
    "もし初期のプログラムが手法を隠していたら、社会の信頼は消え失せ、この手法全体が崩れ去っていたかもしれない。"
    "つまり開かれていることは単なる礼儀ではなく、ナッジを策略から分かつまさにその要なのだ。",
    "ナッジが称賛に値するか疑いに値するかは、道具そのものよりも、それを振るう手にかかっているのかもしれない。"
    "開かれた形で使えば、ナッジは人々が既に抱く当の目標を最後までやり遂げる助けになる。隠されて使えば、"
    "同じ手法は、力ある者が多数の選択をねじ曲げるもう一つの手立てになる。おそらく誠実なナッジとは、"
    "いったん気づいてもなお、その標的が喜んで受け入れるようなものだ。少なくともそれが、擁護者たちがこの分野に望む基準である。",
  ],
  "vocab": [
    ("weigh up","句動","比較検討する、吟味する"),
    ("lay out","句動","並べる、提示する"),
    ("get around to","句動","（後回しにしていたことに）ようやく手をつける"),
    ("choice architecture","名","選択の設計（提示の仕方）"),
    ("default","名","初期設定、既定"),
    ("inertia","名","惰性、慣性"),
    ("nudge","名／動","そっと後押しする仕掛け、ナッジ"),
    ("at odds with","句","〜と相容れない、対立して"),
    ("opt out","句動","（参加せず）抜ける、拒否する"),
    ("hinge on","句動","〜次第である、〜にかかっている"),
    ("follow through on","句動","最後までやり遂げる、実行する"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『利点→懸念→核心→留保』の型。語法(21)は挿入句に惑わされず<b>真の主語</b>で数を、"
    "(22)は倒置 <span class='en'>Had S p.p.</span> を仮定法過去完了と見抜く。主旨は必ず筆者の<b>透明性という留保</b>に沿う。",
}
