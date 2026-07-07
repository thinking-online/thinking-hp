# -*- coding: utf-8 -*-
"""大問Ⅲ READING 04 ― 企業の社会的責任（CSR）。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "企業の社会的責任 ― 評判か、見せかけか",
  "genre": "ビジネス／経営 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 440,
  "passage_title": "Doing Well by Doing Good",
  "passage": [
    "In recent years, companies have been asked to do more than simply make money. Under the banner of corporate "
    "social responsibility, or CSR, firms now promise to protect the environment, treat workers fairly, and give back "
    "to the communities around them. Business leaders present this idea as a modern duty, and many describe the "
    "goodwill [[u:32]]it[[/u]] creates as an asset worth cultivating. Investors, too, increasingly weigh a firms "
    "record on such matters before committing their money.",

    "The clearest benefit is reputation. Customers increasingly prefer brands that appear [[u:33]]conscientious[[/u]], "
    "and talented employees are drawn to workplaces that seem to stand for something beyond profit. A firm known for "
    "fair labor and clean production can charge more, keep staff longer, and weather scandals better than its rivals. "
    "In this way, doing good and doing well often reinforce each other, turning responsibility into a source of "
    "long-term advantage.",

    "Yet the promise can outrun the practice. Some companies invest heavily in advertising their virtue while changing "
    "little about how they actually operate, a habit critics call [[u:34]]greenwashing[[/u]]. A glossy report about "
    "sustainability may hide pollution that continues out of sight, and a cheerful slogan about diversity may mask "
    "unfair pay. When words and deeds diverge, consumers who feel deceived can turn on a brand as quickly as they once "
    "embraced it.",

    "Observers disagree about how seriously to take [[u:35]]this trend[[/u]]. Enthusiasts insist that CSR marks a "
    "genuine shift, pushing business toward an accountability that markets alone would never demand. Skeptics reply "
    "that much of it is mere public relations, a soft mask over the old goal of maximizing returns. Both camps concede, "
    "however, that stakeholders now watch corporate behavior more closely than before, and that empty gestures are "
    "easier than ever to expose.",

    "For managers, this environment demands care. CSR can build trust, but only when its aims are matched by "
    "measurable results and open reporting. Firms that treat responsibility as decoration risk a backlash far worse "
    "than staying silent, since exposed hypocrisy erodes the very trust the program was meant to secure. Trust, once "
    "broken, is slow and costly to rebuild, and no advertising campaign can quickly restore it. The safest "
    "course is to promise less and deliver more.",

    "Whether corporate social responsibility strengthens society or merely polishes an image may depend less on the "
    "pledges companies make than on the honesty and transparency behind them. The language of good citizenship is now "
    "everywhere in business; whether it reflects real change remains, in each case, a question that only conduct, "
    "measured over time, can answer. Champions and critics alike will keep testing every pledge against the record it "
    "leaves behind.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (the goodwill it creates) refer to?","inline":True,
     "choices":[
       "corporate social responsibility",
       "a business scandal",
       "a government tax",
       "a financial loss"],"answer":"ア",
     "basis":"<span class='en'>the goodwill it creates</span> の <span class='en'>it</span> は直前の <span class='en'>this idea</span>＝<b>CSR</b>。",
     "solve":"代名詞は直前の名詞句へ。『それが生む好意（信用）』の『それ』＝企業の社会的責任。",
     "cut":"<span class='en'>a business scandal</span>（不祥事）は好意を生む主体ではなく無関係。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“conscientious”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":[
       "principled",
       "indifferent",
       "wealthy",
       "secretive"],"answer":"ア",
     "basis":"<span class='en'>conscientious</span>＝「良心的で誠実な」。倫理を重んじる姿勢を指す。",
     "solve":"顧客が好むのは<b>道義を守る</b>ブランド。<span class='en'>principled</span>（信念のある）が同義。",
     "cut":"<span class='en'>indifferent</span>（無関心）はむしろ正反対。"},
    {"no":34,"tag":"言い換え","stem":"In paragraph 3, the word <span class='en'>“greenwashing”</span> is closest in meaning to","inline":True,
     "choices":[
       "presenting a false image of responsibility",
       "making honest public disclosures",
       "donating money to charity",
       "obeying strict environmental laws"],"answer":"ア",
     "basis":"第3段 <span class='en'>advertising their virtue while changing little about how they actually operate</span> の言い換え。",
     "solve":"宣伝だけ立派で実態が伴わない行為＝<b>見せかけ</b>。実態を偽る自己宣伝が同義。",
     "cut":"<span class='en'>honest public disclosures</span>（誠実な情報開示）は見せかけと真逆。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this trend”</span> in paragraph 4 refer to?","inline":True,
     "choices":[
       "the rise of corporate social responsibility",
       "a fall in company profits",
       "the decline of advertising",
       "a new environmental tax"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this trend</span>＝前段までに述べた<b>CSRの広まり</b>。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段までの話題を指す。話題は社会的責任の台頭。",
     "cut":"<span class='en'>a fall in company profits</span> は本文で論じられておらず無関係。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, which of the following is true about a firm with a good reputation?",
     "choices":[
       "It can charge more and keep staff longer than its rivals.",
       "It is forced to lower its prices below its rivals.",
       "It loses talented employees who dislike its values.",
       "Its reputation has no effect on customer choice."],"answer":"ア",
     "basis":"第2段 <span class='en'>can charge more, keep staff longer, and weather scandals better than its rivals</span> に一致。",
     "solve":"設問のキーワード（reputation / rivals）を第2段で照合。",
     "cut":"『価格を下げざるを得ない』は<b>より高く売れる</b>という記述と矛盾。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a risk of hollow or dishonest CSR?",
     "choices":[
       "The government imposes heavy fines on companies that mislead the public.",
       "A sustainability report may conceal ongoing pollution.",
       "Deceived consumers can quickly turn against a brand.",
       "Exposed hypocrisy can erode the trust a program sought to build."],"answer":"ア",
     "basis":"『政府が重い罰金を科す』は本文に記述がない。他の3つは第3・5段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある危険を消し、残る1つが答え。",
     "cut":"汚染の隠蔽・消費者の離反・偽善の露呈による信用失墜は、いずれも本文にあるので危険として『述べられている』。"},
    {"no":38,"tag":"理由","stem":"Why do skeptics doubt CSR?",
     "choices":[
       "Because they see much of it as public relations masking the old goal of profit.",
       "Because it forces markets to demand too much accountability.",
       "Because it lowers company profits far too sharply.",
       "Because it bans companies from advertising at all."],"answer":"ア",
     "basis":"第4段 <span class='en'>much of it is mere public relations, a soft mask over the old goal of maximizing returns</span>。",
     "solve":"<span class='en'>Skeptics reply that …</span> の直後が懐疑論の中身。",
     "cut":"『説明責任を市場に強いる』は楽観論側の主張に近く、懐疑論の論拠ではない。"},
    {"no":39,"tag":"詳細","stem":"According to paragraph 5, what is the safest course for managers?","inline":True,
     "choices":[
       "To promise less and deliver more.",
       "To treat responsibility as decoration.",
       "To stay completely silent about their values.",
       "To spend more on advertising than on real results."],"answer":"ア",
     "basis":"第5段末 <span class='en'>The safest course is to promise less and deliver more</span>。",
     "solve":"設問の <span class='en'>safest course</span> を第5段末尾で直接照合。",
     "cut":"『責任を飾りとして扱う』は本文が<b>反発を招く</b>と警告する行為で逆。"},
    {"no":40,"tag":"内容真偽","stem":"According to paragraph 4, on what point do both enthusiasts and skeptics agree?",
     "choices":[
       "Stakeholders now watch corporate behavior more closely than before.",
       "CSR is nothing more than clever public relations.",
       "Markets on their own will demand full accountability.",
       "Empty gestures are impossible for anyone to detect."],"answer":"ア",
     "basis":"第4段 <span class='en'>Both camps concede … that stakeholders now watch corporate behavior more closely</span>。",
     "solve":"<span class='en'>Both camps concede</span> の後が両者の一致点。",
     "cut":"『空虚な身ぶりは誰にも見抜けない』は <span class='en'>easier than ever to expose</span> と正反対。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "CSR can bring reputation and long-term gains but risks empty greenwashing, so its real value rests on honesty and transparency.",
       "CSR has completely replaced the profit motive in modern business.",
       "Advertising alone now guarantees that a company is socially responsible.",
       "Companies should abandon social responsibility and focus only on profit."],"answer":"ア",
     "basis":"評判の利点（2段）／見せかけの危うさ（3段）／賛否（4段）／経営の要点（5段）／誠実さと透明性次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点＋弊害＋留保に沿う1つを残す。",
     "cut":"『利益動機を完全に置き換えた』『広告だけで責任を保証』『責任を捨てよ』はいずれも言い過ぎか本文に反する。"},
  ],
  "structure":
    "<b>序論[1]</b>CSRの登場と『好意（信用）という資産』 ／ <b>利点[2]</b>評判・人材・長期の優位 ／ "
    "<b>弊害[3]</b>グリーンウォッシング（見せかけ） ／ <b>論争[4]</b>熱心派 vs 懐疑派（監視は強まる） ／ "
    "<b>経営視点[5]</b>飾りは反発を招く／約束より実行 ／ <b>結論[6]</b>是非は誠実さと透明性次第（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "近年、企業は単に金もうけをする以上のことを求められている。企業の社会的責任、すなわちCSRの旗印のもと、"
    "企業は今や環境を守り、労働者を公正に扱い、周囲の地域社会に還元することを約束する。経営者はこの考えを"
    "現代の義務として掲げ、多くはそれが生む好意（信用）を、育てる価値のある資産だと語る。",
    "最も明白な利点は評判である。顧客はますます良心的に見えるブランドを好み、有能な人材は利益の先にある"
    "何かを掲げているように見える職場に引き寄せられる。公正な労働と清潔な生産で知られる企業は、より高く売り、"
    "従業員を長くとどめ、不祥事にも競合よりうまく耐えられる。こうして善を行うことと成功することは"
    "しばしば互いを強め合い、責任を長期的な優位の源に変える。",
    "だが約束は実践を追い越しうる。一部の企業は、実際の運営はほとんど変えないまま、自社の美徳を宣伝することに"
    "多額を投じる――批判者がグリーンウォッシングと呼ぶ習性だ。持続可能性についての華やかな報告書が、"
    "見えないところで続く汚染を隠すこともあり、多様性を掲げる明るい標語が不公正な賃金を覆い隠すこともある。"
    "言葉と行いが食い違えば、だまされたと感じた消費者は、かつて受け入れたのと同じ速さでブランドに背を向けうる。",
    "この潮流をどれほど真剣に受け止めるかで、見る者の意見は分かれる。熱心派は、CSRは真の転換を示し、"
    "市場だけでは決して求めない説明責任へと企業を押しやると主張する。懐疑派は、その多くは単なる広報にすぎず、"
    "利益最大化という古い目標を覆う柔らかな仮面だと反論する。だが両陣営とも、利害関係者が今や以前より"
    "企業行動を注意深く見ており、空虚な身ぶりはかつてなく暴かれやすい、という点は認めている。",
    "経営者にとって、この環境は慎重さを要求する。CSRは信頼を築きうるが、それは目標が測定可能な成果と"
    "開かれた報告によって裏づけられているときに限られる。責任を飾りとして扱う企業は、沈黙しているよりも"
    "はるかにひどい反発を招く危険がある。露呈した偽善が、その取り組みが確保しようとしたまさにその信頼を"
    "むしばむからだ。最も安全な道は、約束を減らし、実行を増やすことである。",
    "企業の社会的責任が社会を強くするのか、それとも単に企業イメージを磨くだけなのかは、企業が掲げる誓いよりも、"
    "その背後にある誠実さと透明性にかかっているのかもしれない。良き市民であるという言葉は今やビジネスのいたる"
    "ところにある。それが本当の変化を映しているかどうかは、結局どの場合も、行動だけが答えられる問いである。",
  ],
  "vocab": [
    ("corporate social responsibility","名","企業の社会的責任（CSR）"),
    ("goodwill","名","好意、信用（無形の資産）"),
    ("conscientious","形","良心的な、誠実な"),
    ("reputation","名","評判、名声"),
    ("sustainability","名","持続可能性"),
    ("greenwashing","名","見せかけの環境配慮"),
    ("stakeholder","名","利害関係者"),
    ("accountability","名","説明責任"),
    ("hypocrisy","名","偽善"),
    ("backlash","名","激しい反発"),
    ("transparency","名","透明性、開示"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点と弊害の<b>両面＋留保</b>を選ぶ。",
}
