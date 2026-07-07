# -*- coding: utf-8 -*-
"""大問Ⅱ READING 01（基準サンプル）― サブスクリプション経済。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "サブスクリプション経済 ― 所有から利用へ",
  "genre": "ビジネス／経済 論説",
  "limit": "目標18分",
  "wordcount": 430,
  "passage_title": "The Subscription Shift",
  "passage": [
    "Not long ago, owning things was a mark of success. People bought music on discs, films on tape, and software in boxes. "
    "Today, a growing number of consumers [[u:14]]would rather[[/u]] pay for access than for ownership. From streaming platforms "
    "to meal kits, the subscription model has [[u:15]]sprung up[[/u]] across almost every industry, quietly rewriting how "
    "companies earn their money.",

    "The appeal to businesses is easy to grasp. A single sale brings in cash once; a subscription brings it in month after month. "
    "This steady flow of revenue is far more [[u:16]]predictable[[/u]], which makes planning and investment less risky. Instead of "
    "chasing new buyers every quarter, a firm can concentrate on keeping the customers it already has — and a loyal subscriber, "
    "on average, is worth far more over time than a one-time shopper.",

    "Customers benefit too, at least in theory. Subscriptions lower the upfront cost of trying something new. Rather than "
    "[[u:17]]shelling out[[/u]] a large sum for a product they may dislike, users pay a small monthly fee and can walk away "
    "whenever they choose. For many, the convenience of automatic delivery and constant updates [[u:18]]outweighs[[/u]] the "
    "nagging sense that the payments never really stop.",

    "Yet the model has a darker side. Because canceling takes effort, some companies [[u:19]]bank on[[/u]] customers forgetting "
    "to quit. Services that once felt like bargains can [[u:20]]pile up[[/u]] until a household is paying for a dozen it barely "
    "uses. Critics argue that parts of the industry have learned to profit not from satisfaction but from inertia.",

    "For managers, the central challenge is retention. Signing up a customer [[b:21]] little if that customer disappears within "
    "two months. Firms therefore invest heavily in data, studying when and why users cancel. Had they ignored these warning "
    "signs, many early subscription start-ups [[b:22]] long before they ever turned a profit. The lesson was blunt: growth "
    "without loyalty is a leaking bucket.",

    "The subscription wave shows no sign of slowing. As more of daily life moves online, the line between buying and renting "
    "will keep fading. Whether this shift ultimately serves customers or merely traps them may depend less on the technology "
    "itself than on how honestly companies choose to treat the people who pay them.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>would rather</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["prefer to","refuse to","happen to","tend not to"],"answer":"ア",
     "basis":"<span class='en'>would rather do A than B</span>＝「BよりむしろAしたい」。",
     "solve":"直後の <span class='en'>than</span> と対比構造から『好んで選ぶ』意と判断。",
     "cut":"<span class='en'>refuse to</span>（拒む）は逆。<span class='en'>happen to</span>（たまたま）は文意に合わない。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>sprung up</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["emerged","declined","paused","vanished"],"answer":"ア",
     "basis":"<span class='en'>spring up</span>＝「急に現れる、あちこちで生まれる」。",
     "solve":"<span class='en'>across almost every industry</span>（あらゆる業界に）と結び、拡大・出現の意。",
     "cut":"<span class='en'>declined/vanished</span> は減少・消失で真逆。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>predictable</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["foreseeable","unstable","temporary","costly"],"answer":"ア",
     "basis":"<span class='en'>predictable</span>＝「予測できる」。<span class='en'>foreseeable</span> が同義。",
     "solve":"<span class='en'>makes planning ... less risky</span>（計画のリスクが減る）から『見通せる』意。",
     "cut":"<span class='en'>unstable</span>（不安定）は文脈と矛盾。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>shelling out</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["paying","saving","borrowing","earning"],"answer":"ア",
     "basis":"<span class='en'>shell out</span>＝「（大金を）支払う」。",
     "solve":"<span class='en'>a large sum for a product</span> と結び『支払う』。直後の <span class='en'>pay a small monthly fee</span> との対比も手がかり。",
     "cut":"<span class='en'>saving/earning</span> は出費と逆方向。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>outweighs</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["is greater than","falls short of","depends on","gives way to"],"answer":"ア",
     "basis":"<span class='en'>outweigh</span>＝「〜に勝る、〜を上回る」。",
     "solve":"利便性が『払い続ける不安』に勝る、という天秤の構図。",
     "cut":"<span class='en'>falls short of</span>（及ばない）は逆。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>bank on</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["rely on","give up","warn against","make up for"],"answer":"ア",
     "basis":"<span class='en'>bank on</span>＝「〜を当てにする、頼みにする」。",
     "solve":"『客が解約を忘れることを当てにする』という文脈。",
     "cut":"多義の <span class='en'>bank</span>（銀行・土手）に引かれない。ここは句動詞の『頼る』。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>pile up</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["accumulate","break down","run out","spread out"],"answer":"ア",
     "basis":"<span class='en'>pile up</span>＝「積み上がる、たまる」。",
     "solve":"『使いもしない十数個のサービスに払い続ける』＝契約がたまる。",
     "cut":"<span class='en'>run out</span>（尽きる）は逆。"},
    {"no":21,"tag":"E 語法","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["means","mean","meaning","to mean"],"answer":"ア",
     "basis":"主語は動名詞句 <span class='en'>Signing up a customer</span>＝<b>単数扱い</b>。現在の一般論なので三単現。",
     "solve":"<span class='en'>Signing up a customer means little if ...</span>「客を1人獲得しても…なら意味がない」。",
     "cut":"動名詞主語を複数と誤り <span class='en'>mean</span> を選ばない。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would have folded","will fold","folded","would fold"],"answer":"ア",
     "basis":"文頭 <span class='en'>Had they ignored ...</span> は <span class='en'>If they had ignored</span> の倒置＝<b>仮定法過去完了</b>。帰結節は <span class='en'>would have + 過去分詞</span>。",
     "solve":"「もし兆候を無視していたら、多くの新興企業は利益を出す前に<b>倒れていただろう</b>」。",
     "cut":"<span class='en'>would fold</span>（仮定法過去）は時制が過去完了の条件節と不一致。"},
    {"no":23,"tag":"D 情報整序","stem":"第5段で述べられる企業の対応を、本文の論理に沿って正しい順に並べたものを選べ。"
        "　(あ)解約の時期と理由を分析する　(い)顧客を1人獲得する　(う)データに投資する　(え)顧客維持を経営課題と捉える",
     "choices":["え → い → う → あ","い → あ → う → え","う → あ → い → え","え → あ → う → い"],"answer":"ア",
     "basis":"第5段は『維持が課題(え)→客を得ても離脱すれば無意味(い)→だからデータに投資(う)→いつ・なぜ解約かを研究(あ)』の順。",
     "solve":"<span class='en'>therefore</span> の前後で因果の向きを確定。最初(え)と最後(あ)を先に固定して挟み撃ち。",
     "cut":"『データ投資(う)』は『維持を課題と捉える(え)』より後。順序を逆にした選択肢を切る。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "企業にとって定期収入は一度きりの販売より予測しやすい。",
       "サブスクは新しい商品を試す初期費用を下げる面がある。",
       "筆者は、サブスク業界のすべてが顧客の惰性から利益を得ていると断言している。",
       "日常生活のオンライン化が進むほど、購入と賃借の境界は曖昧になる。"],
     "answer":"ウ",
     "basis":"第4段は <span class='en'>parts of the industry</span>（業界の<b>一部</b>）と限定。『すべて』とは言っていない。",
     "solve":"設問の『合致しない』に印。選択肢のキーワード（すべて/一部）を本文で照合。",
     "cut":"他の3つ（予測しやすい定期収入／初期費用を下げる／購入と賃借の境界が薄れる）は本文に一致。"
           "『業界のすべてが惰性から利益を得ている』という選択肢だけが <span class='en'>parts of the industry</span> の限定を無視した言い過ぎ(too broad)で誤り。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "忠実な購読者は平均すると一度きりの客より長期的な価値が高い。",
       "サブスクでは利用者はいつでも解約できないよう縛られる。",
       "定期収入は企業の投資判断をより危険にする。",
       "筆者はサブスクが必ず顧客の利益になると結論づけている。"],
     "answer":"ア",
     "basis":"第2段 <span class='en'>a loyal subscriber ... is worth far more over time than a one-time shopper</span> と一致。",
     "solve":"本文の該当文を特定して照合。",
     "cut":"『解約できないよう縛られる』は第3段 <span class='en'>walk away whenever they choose</span> と矛盾。"
           "『投資判断をより危険にする』は第2段 <span class='en'>less risky</span> と逆。『必ず顧客の利益になる』は第6段の留保（断定回避）と矛盾。"},
    {"no":26,"tag":"F 指示語","stem":"最終段の <span class='en'>the people who pay them</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["subscribers（購読者）","managers（経営者）","critics（批評家）","start-ups（新興企業）"],"answer":"ア",
     "basis":"<span class='en'>them</span>＝企業(companies)。『企業に支払う人々』＝購読者・顧客。",
     "solve":"指示語は直前の主語を確認。<span class='en'>companies choose to treat the people who pay them</span>。",
     "cut":"経営者は支払う側ではなく受け取る側。"},
    {"no":27,"tag":"C 理由","stem":"企業がデータに多額の投資をするのはなぜか。最も適切なものを選べ。",
     "choices":[
       "顧客がいつ・なぜ解約するかを把握し、顧客維持につなげるため。",
       "新規顧客を毎四半期できるだけ多く集めるため。",
       "競合他社の価格を調査して値下げするため。",
       "商品の生産コストを下げるため。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>studying when and why users cancel</span>＋<span class='en'>the central challenge is retention</span>。",
     "solve":"『therefore invest ... in data』の直前の課題（retention）と結ぶ。",
     "cut":"『新規顧客をできるだけ集める』は第2段で否定される方向（新規追いより維持）。『競合の価格調査』『生産コスト削減』は本文に記述がない。"},
    {"no":28,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "サブスク型は企業と顧客の双方に利点がある一方で惰性による搾取の危うさも抱え、その是非は企業の誠実さ次第である。",
       "サブスク型は技術の進歩によって必ず消費者を幸福にする。",
       "所有はもはや成功の証ではなく、賃借だけが唯一の選択肢になった。",
       "サブスク企業はデータ投資をやめるべきである。"],
     "answer":"ア",
     "basis":"利点（2・3段）／弊害（4段）／維持という課題（5段）／是非は誠実さ次第（6段）という論の全体像に一致。",
     "solve":"主旨は『言い過ぎ・本文にない要素』を切り、筆者の両論併記＋留保に沿う1つを残す。",
     "cut":"『必ず消費者を幸福にする』『賃借だけが唯一の選択肢』は断定しすぎ(too broad)。『データ投資をやめるべき』は本文にない主張。"},
  ],
  "structure":
    "<b>序論[1]</b>所有→利用への転換とサブスクの台頭 ／ <b>本論(企業側)[2]</b>予測可能な定期収入・維持の価値 ／ "
    "<b>本論(顧客側)[3]</b>初期費用減・利便性 ／ <b>反論[4]</b>惰性からの利益という影 ／ "
    "<b>核心[5]</b>retention（維持）こそ課題・データ投資 ／ <b>結論[6]</b>是非は企業の誠実さ次第（留保）。"
    "　――『利点→弊害→課題→留保』の典型的な論説構造。主旨問題はこの<b>留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "少し前まで、物を所有することは成功の証だった。人々は音楽をディスクで、映画をテープで、ソフトを箱で買った。"
    "今日、ますます多くの消費者が、所有ではなく利用にお金を払うことを好む。ストリーミングからミールキットまで、"
    "サブスク型はほぼあらゆる業界に一気に広がり、企業の稼ぎ方を静かに書き換えている。",
    "企業にとっての魅力は分かりやすい。一度の販売は一度きりの現金をもたらすが、サブスクは毎月それをもたらす。"
    "この安定した収入の流れははるかに予測しやすく、計画や投資のリスクを下げる。毎四半期新規客を追う代わりに、"
    "企業は既存客の維持に集中できる――そして忠実な購読者は平均すると、一度きりの客より長期的にずっと価値が高い。",
    "顧客にも、少なくとも理屈の上では利点がある。サブスクは新しい物を試す初期費用を下げる。気に入らないかもしれない"
    "商品に大金を払う代わりに、利用者は少額の月額を払い、いつでもやめられる。多くの人にとって、自動配送と絶えざる"
    "更新の便利さは、支払いが止まらないという漠然とした不安に勝る。",
    "だがこのモデルには暗い面もある。解約には手間がかかるため、一部の企業は客が解約を忘れることを当てにする。"
    "かつてお得に見えたサービスは、ある家庭がほとんど使わない十数個に払い続けるまで積み上がりうる。"
    "批評家は、業界の一部は満足からではなく惰性から利益を得ることを学んだ、と論じる。",
    "経営者にとって中心的な課題は「維持」である。客を1人獲得しても、その客が2か月で消えれば意味がない。"
    "だから企業はデータに多額を投じ、利用者がいつ・なぜ解約するかを研究する。もしこうした兆候を無視していたら、"
    "多くの初期のサブスク新興企業は、利益を出すはるか前に倒れていただろう。教訓は身も蓋もない――"
    "忠誠なき成長は、穴の空いたバケツだ。",
    "サブスクの波が衰える気配はない。日常生活のより多くがオンラインに移るにつれ、購入と賃借の境界は薄れ続けるだろう。"
    "この転換が最終的に顧客に資するのか、それとも顧客を罠にかけるだけなのかは、技術そのものよりも、"
    "企業が支払う人々をどれだけ誠実に扱うかにかかっているのかもしれない。",
  ],
  "vocab": [
    ("would rather","句","むしろ〜したい"),
    ("spring up","句動","急に現れる、あちこちに生まれる"),
    ("revenue","名","収入、歳入"),
    ("predictable","形","予測できる"),
    ("shell out","句動","（大金を）支払う"),
    ("outweigh","動","〜に勝る、〜を上回る"),
    ("bank on","句動","〜を当てにする"),
    ("pile up","句動","積み上がる、たまる"),
    ("inertia","名","惰性、慣性"),
    ("retention","名","（顧客の）維持、保持"),
    ("turn a profit","句","利益を出す"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『利点→弊害→課題→留保』の型。主旨問題は必ず筆者の<b>留保</b>に沿う。",
}
