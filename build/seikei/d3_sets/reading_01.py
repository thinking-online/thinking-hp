# -*- coding: utf-8 -*-
"""大問Ⅲ READING 01（基準サンプル）― ギグ・エコノミー。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "ギグ・エコノミー ― オンデマンドで働く",
  "genre": "ビジネス／労働 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 430,
  "passage_title": "Working on Demand",
  "passage": [
    "Over the past decade, a new kind of labor market has taken shape. Instead of holding a single, steady position, "
    "millions of people now earn a living through short, on-demand tasks arranged by apps: driving passengers, delivering "
    "meals, or writing code for a day. Supporters call this the gig economy, and they praise the freedom [[u:32]]it[[/u]] offers.",

    "The main attraction is control over ones own time. A gig worker can be highly [[u:33]]flexible[[/u]], logging on when it "
    "suits them and logging off when it does not. For students, parents, and people with other commitments, this arrangement "
    "can turn idle hours into income. Platforms, for their part, gain a vast workforce they can expand or shrink at a moments "
    "notice, without the fixed costs of full-time staff.",

    "Yet the freedom comes at a price. Because gig workers are usually treated as independent contractors rather than "
    "employees, they receive no paid leave, no health insurance, and no [[u:34]]cushion[[/u]] against slow weeks. Their income "
    "rises and falls with demand, and a sudden change in an apps rules can cut their earnings overnight. What looks like "
    "independence can feel, in practice, like insecurity.",

    "Economists are divided over what [[u:35]]this shift[[/u]] means for the wider economy. Optimists argue that gig work lowers "
    "unemployment and lets the market match labor to demand with new efficiency. Critics counter that it simply moves risk from "
    "companies onto individuals, hollowing out the stable, protected jobs on which the middle class was built. Both sides agree "
    "on one point: the trend is growing, and the old rules were not written for it.",

    "For managers, the gig model is a powerful but delicate tool. It offers speed and savings, but a workforce that feels "
    "disposable is rarely loyal or careful. The firms that succeed with gig labor tend to be those that treat their contractors "
    "fairly, offering clear terms and a measure of stability even without a formal contract.",

    "Whether the gig economy ends up empowering workers or exposing them may depend less on the technology itself than on the "
    "rules societies choose to write around it. The apps have changed how work is arranged; they have not settled the older "
    "question of what a fair days work is worth.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (the freedom it offers) refer to?","inline":True,
     "choices":["the gig economy","a steady position","an app","a single task"],"answer":"ア",
     "basis":"<span class='en'>they praise the freedom it offers</span> の <span class='en'>it</span> は直前の <span class='en'>the gig economy</span>。",
     "solve":"代名詞は直前の名詞へ。『それが与える自由』の『それ』＝ギグ・エコノミー。",
     "cut":"<span class='en'>a steady position</span> はギグと対比される旧来の働き方で逆。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“flexible”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":["adaptable","fragile","reluctant","permanent"],"answer":"ア",
     "basis":"<span class='en'>flexible</span>＝「融通の利く、柔軟な」。<span class='en'>logging on when it suits them</span> と一致。",
     "solve":"自分の都合で入切できる＝融通が利く。<span class='en'>adaptable</span> が同義。",
     "cut":"<span class='en'>permanent</span>（恒久的）は柔軟性と無関係。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“cushion”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":["buffer","reward","schedule","contract"],"answer":"ア",
     "basis":"<span class='en'>no cushion against slow weeks</span>＝「暇な週に対する<b>緩衝材</b>」。",
     "solve":"収入が減る週を和らげるもの＝備え・緩衝。<span class='en'>buffer</span> が同義。",
     "cut":"<span class='en'>reward</span>（報酬）は緩衝の意味ではない。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this shift”</span> in paragraph 4 refer to?","inline":True,
     "choices":["the move toward gig work","a rise in unemployment","a change in app design","a new tax rule"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this shift</span>＝これまで述べてきた<b>ギグ労働への移行</b>。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段までの内容を指す。話題はギグ労働への転換。",
     "cut":"<span class='en'>a rise in unemployment</span> は本文でむしろ下がると論じられており逆。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 3, which of the following is true about gig workers?",
     "choices":[
       "They usually receive no paid leave or health insurance.",
       "They are legally treated as full-time employees.",
       "Their income stays the same regardless of demand.",
       "They are guaranteed a fixed wage by the apps."],"answer":"ア",
     "basis":"第3段 <span class='en'>they receive no paid leave, no health insurance</span> に一致。",
     "solve":"設問のキーワード（paid leave / insurance）を第3段で照合。",
     "cut":"『正社員として扱われる』は <span class='en'>independent contractors rather than employees</span> と矛盾。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a drawback of gig work?",
     "choices":[
       "Workers may be required to relocate for their jobs.",
       "Workers receive no health insurance.",
       "Income can fall when demand drops.",
       "A change in an app’s rules can cut earnings suddenly."],"answer":"ア",
     "basis":"『転居を求められる』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある短所を消し、残る1つが答え。",
     "cut":"保険なし・需要で収入減・ルール変更で減収は、いずれも第3段に一致するので短所として『述べられている』。"},
    {"no":38,"tag":"理由","stem":"Why do critics worry about the gig economy?",
     "choices":[
       "Because it shifts risk from companies onto individuals.",
       "Because it makes companies pay too much tax.",
       "Because it raises unemployment across the market.",
       "Because it forces platforms to hire full-time staff."],"answer":"ア",
     "basis":"第4段 <span class='en'>it simply moves risk from companies onto individuals</span>。",
     "solve":"<span class='en'>Critics counter that …</span> の直後が批判の中身。",
     "cut":"『失業を増やす』は楽観論が下がると述べる点と食い違い、批判の論拠でもない。"},
    {"no":39,"tag":"詳細","stem":"According to paragraph 2, what advantage do platforms gain?",
     "choices":[
       "A workforce they can expand or shrink quickly without fixed costs.",
       "A group of permanent employees with full benefits.",
       "Guaranteed profits regardless of demand.",
       "Complete control over national labor laws."],"answer":"ア",
     "basis":"第2段 <span class='en'>a vast workforce they can expand or shrink at a moment's notice, without the fixed costs</span>。",
     "solve":"設問の主語（platforms）を第2段後半で探す。",
     "cut":"『正社員を福利厚生付きで抱える』は固定費を避ける記述と逆。"},
    {"no":40,"tag":"筆者の見解","stem":"Which of the following best describes the author’s view in the passage?",
     "choices":[
       "The impact of gig work depends largely on the rules societies create around it.",
       "Gig work is certain to empower every worker.",
       "The gig economy should be banned outright.",
       "Technology alone has already solved the problem of fair pay."],"answer":"ア",
     "basis":"最終段 <span class='en'>may depend less on the technology itself than on the rules societies choose to write around it</span>。",
     "solve":"筆者は両論を示したうえで『ルール次第』と留保する。",
     "cut":"『必ず労働者を力づける』『全面禁止すべき』『技術が既に解決』はいずれも断定しすぎで本文の留保と矛盾。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "The gig economy brings both freedom and insecurity, and its ultimate value hinges on the rules built around it.",
       "The gig economy has completely replaced traditional employment worldwide.",
       "Apps have finally determined what a fair day’s work is worth.",
       "Managers should avoid using gig labor under any circumstances."],"answer":"ア",
     "basis":"自由（2段）／不安定さ（3段）／賛否（4段）／経営の要点（5段）／ルール次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、両論併記＋留保に沿う1つを残す。",
     "cut":"『伝統的雇用を完全に置き換えた』『公正な賃金を決めた』は言い過ぎ。『一切使うな』は本文にない。"},
  ],
  "structure":
    "<b>序論[1]</b>ギグ・エコノミーの登場と『自由』 ／ <b>利点[2]</b>時間の裁量・プラットフォームの柔軟性 ／ "
    "<b>弊害[3]</b>保障なし・収入の不安定 ／ <b>論争[4]</b>楽観論 vs 批判（リスクの個人転嫁） ／ "
    "<b>経営視点[5]</b>公正な扱いが成否を分ける ／ <b>結論[6]</b>是非はルール次第（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "この10年で、新しい種類の労働市場が形づくられた。単一の安定した職に就く代わりに、"
    "今や何百万もの人々が、アプリで手配される短いオンデマンドの仕事――乗客を運ぶ、食事を配達する、"
    "1日だけコードを書く――で生計を立てている。支持者はこれを『ギグ・エコノミー』と呼び、それが与える自由を称賛する。",
    "最大の魅力は自分の時間を自分で管理できることだ。ギグワーカーは非常に柔軟に、都合のよいときにログインし、"
    "都合が悪ければログオフできる。学生や親、他に用事のある人にとって、この仕組みは空き時間を収入に変えうる。"
    "プラットフォーム側も、正社員の固定費なしに、瞬時に拡大・縮小できる巨大な労働力を得る。",
    "だが自由には代償がある。ギグワーカーは通常、従業員ではなく独立請負人として扱われるため、"
    "有給休暇も健康保険も、暇な週に対する緩衝材もない。収入は需要とともに上下し、"
    "アプリの規則の突然の変更が一夜で稼ぎを削りうる。独立に見えるものが、実際には不安定に感じられうる。",
    "この移行が経済全体に何を意味するかで、経済学者の見解は割れている。楽観論者は、ギグ労働が失業を減らし、"
    "労働と需要を新たな効率で結びつけると論じる。批判者は、それは単にリスクを企業から個人へ移し、"
    "中間層を支えてきた安定した保障付きの職を空洞化させるだけだと反論する。両者が一致するのは一点――"
    "この傾向は拡大しており、古い規則はそれを想定して書かれていない、ということだ。",
    "経営者にとって、ギグ・モデルは強力だが繊細な道具だ。速さと節約をもたらすが、"
    "使い捨てにされると感じる労働力が忠実で丁寧であることはまれだ。ギグ労働で成功する企業は、"
    "正式な契約がなくとも、明確な条件と一定の安定を提供し、請負人を公正に扱う傾向がある。",
    "ギグ・エコノミーが最終的に労働者を力づけるのか、それとも危険にさらすのかは、技術そのものよりも、"
    "社会がその周りにどんな規則を書くかにかかっているのかもしれない。アプリは仕事の手配の仕方を変えたが、"
    "『公正な1日の労働の価値とは何か』という古い問いには、まだ答えを出していない。",
  ],
  "vocab": [
    ("gig economy","名","単発の仕事で成り立つ労働形態"),
    ("on-demand","形","要求に応じた、随時の"),
    ("flexible","形","融通の利く、柔軟な"),
    ("independent contractor","名","独立請負人（非従業員）"),
    ("cushion","名","緩衝材、備え"),
    ("insecurity","名","不安定さ"),
    ("shift","名","（構造の）移行、転換"),
    ("hollow out","句動","空洞化させる"),
    ("disposable","形","使い捨ての"),
    ("empower","動","力を与える"),
    ("hinge on","句動","〜次第である"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は両論併記＋<b>留保</b>を選ぶ。",
}
