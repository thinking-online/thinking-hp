# -*- coding: utf-8 -*-
"""大問Ⅲ READING 03 ― シェアリング・エコノミー。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "シェアリング・エコノミー ― 遊休資産を共有する",
  "genre": "ビジネス／社会 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 428,
  "passage_title": "Sharing What We Already Own",
  "passage": [
    "In recent years, a new way of doing business has spread across cities worldwide. Instead of buying goods and "
    "services from large companies, people increasingly rent spare rooms, borrow cars, and hire skills directly from "
    "one another through digital platforms. Supporters call this the sharing economy, and they celebrate the value "
    "[[u:32]]it[[/u]] creates from things that would otherwise sit unused.",

    "The core idea is simple: many valuable assets are used only part of the time. A spare bedroom, a parked car, or a "
    "power drill may stay [[u:33]]idle[[/u]] for most of its life. By connecting owners with strangers who need these "
    "things for a short while, the platforms turn wasted capacity into income for one side and a cheaper option for the "
    "other. Owners earn a little from what they already own, and users pay less than they would to a traditional firm.",

    "Yet these benefits arrive with real costs. Because ordinary people, not licensed businesses, provide the service, "
    "regulators struggle to guarantee safety and quality. A guest may enter a home that meets no hotel standard, and a "
    "rider may sit in a car that faces no professional inspection. Established industries, from hotels to taxi firms, "
    "also complain that platforms compete unfairly while [[u:34]]sidestepping[[/u]] the rules that bind them.",

    "Opinions about [[u:35]]this tension[[/u]] are sharply divided. Enthusiasts argue that the sharing economy lowers "
    "prices, spreads earnings more widely, and makes fuller use of the resources a society already has. Skeptics reply "
    "that it erodes hard-won protections for workers and consumers, and that much of the promised sharing is really just "
    "a market dressed in friendly language. Both camps concede one thing: the model keeps growing, and older laws were "
    "not designed for it.",

    "For the platforms themselves, the central challenge is trust. Strangers will not hand over their homes or climb "
    "into private cars unless they feel reasonably safe. To bridge this gap, the leading services rely on rating "
    "systems, verified identities, and insurance that covers accidents and damage. A single bad review can cost a host "
    "future guests, so most participants have a strong reason to behave well. These tools do not remove every risk, but "
    "they make cooperation between strangers feel ordinary rather than reckless.",

    "Whether the sharing economy matures into a lasting institution or fades as a passing fashion may depend less on the "
    "technology than on whether such trust can be sustained. The platforms have shown that idle assets can be turned "
    "into shared value; they have not yet proven that the confidence holding the system together will survive its own "
    "rapid growth.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (the value it creates) refer to?","inline":True,
     "choices":[
       "the sharing economy",
       "a large company",
       "a spare room",
       "a traditional firm"],"answer":"ア",
     "basis":"<span class='en'>they celebrate the value it creates</span> の <span class='en'>it</span> は直前の <span class='en'>the sharing economy</span>。",
     "solve":"代名詞は直前の名詞へ。『それが生み出す価値』の『それ』＝シェアリング・エコノミー。",
     "cut":"<span class='en'>a large company</span> は本文でシェアと<b>対比</b>される旧来の買い先で逆。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“idle”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":[
       "unused",
       "broken",
       "expensive",
       "shared"],"answer":"ア",
     "basis":"<span class='en'>may stay idle for most of its life</span>＝「その大半を<b>使われずに</b>過ごす」。",
     "solve":"直後の <span class='en'>wasted capacity</span>（無駄になった能力）と対応。<span class='en'>unused</span> が同義。",
     "cut":"<span class='en'>broken</span>（壊れた）は『使われていない』とは別で、故障の記述はない。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“sidestepping”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":[
       "avoiding",
       "obeying",
       "writing",
       "enforcing"],"answer":"ア",
     "basis":"<span class='en'>sidestepping the rules that bind them</span>＝「自分たちを縛る規則を<b>回避する</b>」。",
     "solve":"既存産業が『不当な競争だ』と不満を述べる文脈。規則を『すり抜ける』＝<span class='en'>avoiding</span>。",
     "cut":"<span class='en'>obeying</span>（従う）は正反対で、不公平だという非難と矛盾する。"},
    {"no":35,"tag":"指示語","stem":"What does <span class='en'>“this tension”</span> in paragraph 4 refer to?","inline":True,
     "choices":[
       "the conflict between the benefits of the sharing economy and its costs to safety and existing industries",
       "a disagreement among hotel guests about room prices",
       "a sudden rise in the number of car accidents",
       "a shortage of spare rooms in large cities"],"answer":"ア",
     "basis":"第4段冒頭 <span class='en'>this tension</span>＝第2段の<b>利点</b>と第3段の<b>弊害</b>（安全・既存産業との摩擦）の対立。",
     "solve":"<span class='en'>this ＋ 名詞</span>は前段までの内容を指す。利点と弊害のせめぎ合いを受ける。",
     "cut":"<span class='en'>hotel guests</span> の値段争いや事故の急増は本文に記述がなく、話題の焦点でもない。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, which of the following is true about the sharing economy?",
     "choices":[
       "The platforms turn idle assets into income for owners and cheaper options for users.",
       "The platforms build brand-new assets and sell them to large companies.",
       "The platforms guarantee that every asset is used every day.",
       "The platforms replace owners with licensed professional firms."],"answer":"ア",
     "basis":"第2段 <span class='en'>the platforms turn wasted capacity into income for one side and a cheaper option for the other</span> に一致。",
     "solve":"設問のキーワード（income / cheaper）を第2段後半で照合。",
     "cut":"『新品の資産を作って大企業に売る』は、<b>既にある遊休資産</b>を活用するという趣旨と食い違う。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a problem of the sharing economy?",
     "choices":[
       "Platforms charge owners a large yearly membership fee.",
       "Regulators find it hard to guarantee safety and quality.",
       "Established industries complain about unfair competition.",
       "Some homes meet no hotel safety standard."],"answer":"ア",
     "basis":"『多額の年会費を課す』は本文に記述がない。他の3つは第3段に明記。",
     "solve":"設問の <span class='en'>NOT</span> に印。本文にある問題点を消し、残る1つが答え。",
     "cut":"安全保証の困難・不公平な競争への不満・ホテル基準に満たない住居は、いずれも第3段に一致するので『述べられている』。"},
    {"no":38,"tag":"内容真偽","stem":"According to paragraph 4, what do both enthusiasts and skeptics agree on?",
     "choices":[
       "The model keeps growing, and older laws were not designed for it.",
       "The sharing economy will soon disappear entirely.",
       "The sharing economy fully protects workers and consumers.",
       "Prices in the sharing economy are always higher than in traditional firms."],"answer":"ア",
     "basis":"第4段末 <span class='en'>Both camps concede one thing: the model keeps growing, and older laws were not designed for it</span> に一致。",
     "solve":"<span class='en'>Both camps concede</span> の直後が両者の一致点。",
     "cut":"『すぐ消える』『労働者を完全に守る』は片方の主張を誇張したもので、<b>共通の合意</b>ではない。"},
    {"no":39,"tag":"理由","stem":"Why do skeptics criticize the sharing economy?",
     "choices":[
       "Because it erodes hard-won protections for workers and consumers.",
       "Because it makes established industries too powerful.",
       "Because it forces owners to buy expensive new assets.",
       "Because it raises prices for ordinary users."],"answer":"ア",
     "basis":"第4段 <span class='en'>Skeptics reply that it erodes hard-won protections for workers and consumers</span>。",
     "solve":"<span class='en'>Skeptics reply that …</span> の直後が批判の中身。",
     "cut":"『価格を上げる』は、むしろ <span class='en'>lowers prices</span> と述べる利点の記述と逆で、批判の論拠でもない。"},
    {"no":40,"tag":"詳細","stem":"According to paragraph 5, how do the leading platforms try to build trust?",
     "choices":[
       "By using rating systems, verified identities, and insurance.",
       "By hiring licensed inspectors for every home and car.",
       "By removing every possible risk for their users.",
       "By banning strangers from using their services."],"answer":"ア",
     "basis":"第5段 <span class='en'>the leading services rely on rating systems, verified identities, and insurance</span>。",
     "solve":"設問の主語（platforms）と目的（trust）を第5段で照合。",
     "cut":"『あらゆるリスクを取り除く』は <span class='en'>do not remove every risk</span> と明確に矛盾する。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "The sharing economy turns idle assets into shared value, but its future depends on whether trust between strangers can be sustained.",
       "The sharing economy has already replaced hotels and taxis around the world.",
       "The sharing economy is certain to fail because strangers can never trust one another.",
       "The sharing economy succeeds only when governments own all the platforms."],"answer":"ア",
     "basis":"遊休資産の活用（2段）／規制・安全の弊害（3段）／賛否（4段）／信頼の仕組み（5段）／信頼が続くか次第という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、利点＋弊害＋<b>信頼次第という留保</b>に沿う1つを残す。",
     "cut":"『既にホテルとタクシーを置き換えた』『必ず失敗する』は言い過ぎ。『政府が全所有すべき』は本文にない。"},
  ],
  "structure":
    "<b>序論[1]</b>シェアリング・エコノミーの登場と『遊休資産からの価値』 ／ <b>利点[2]</b>使われない資産を収入と割安な選択肢に ／ "
    "<b>弊害[3]</b>安全・品質の保証困難・既存産業との摩擦 ／ <b>論争[4]</b>賛成論 vs 懐疑論（保護の空洞化） ／ "
    "<b>含意[5]</b>普及の鍵は信頼（評価・本人確認・保険） ／ <b>結論[6]</b>存続は信頼が続くか次第（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "近年、新しいビジネスのやり方が世界中の都市に広がった。大企業から商品やサービスを買う代わりに、"
    "人々はますます、デジタル・プラットフォームを通じて、空き部屋を貸し、車を借り、技能を互いに直接雇い合っている。"
    "支持者はこれを『シェアリング・エコノミー』と呼び、放っておけば使われないままの物から生み出される価値を称賛する。",
    "核心となる考えは単純だ。多くの価値ある資産は、時間の一部しか使われていない。空き寝室も、駐車中の車も、"
    "電動ドリルも、その大半を使われないまま過ごしうる。これらを短時間必要とする見知らぬ人と所有者を結びつけることで、"
    "プラットフォームは無駄になった能力を、一方には収入に、他方には割安な選択肢に変える。"
    "所有者は自分が既に持つ物から少し稼ぎ、利用者は従来の企業に払うより安く済む。",
    "だが、この利点には現実の代償が伴う。免許を持つ事業者ではなく一般の人々がサービスを提供するため、"
    "規制当局は安全と品質を保証するのに苦労する。宿泊客はホテル基準を満たさない住居に入るかもしれず、"
    "乗客は専門の点検を受けていない車に乗るかもしれない。ホテルからタクシー会社まで既存産業も、"
    "プラットフォームが自分たちを縛る規則をすり抜けながら不当に競争していると不満を述べる。",
    "この緊張をめぐって意見は鋭く割れている。熱心な支持者は、シェアリング・エコノミーは価格を下げ、"
    "稼ぎをより広く行き渡らせ、社会が既に持つ資源をより十分に使うと論じる。懐疑派は、"
    "それは労働者と消費者のために勝ち取られた保護を空洞化させ、約束された『共有』の多くは"
    "親しみやすい言葉で装った市場にすぎないと反論する。両陣営が認める点が一つある――"
    "このモデルは拡大を続けており、古い法律はそれを想定して作られていない、ということだ。",
    "プラットフォーム自身にとって、中心的な課題は信頼だ。見知らぬ人は、"
    "そこそこ安全だと感じられなければ、自分の家を明け渡したり他人の車に乗り込んだりしない。"
    "この隔たりを埋めるため、主要なサービスは評価システム、本人確認、事故や損害を補償する保険に頼る。"
    "一つの悪い評価が主催者から今後の客を奪いうるので、参加者の多くには行儀よく振る舞う強い理由がある。"
    "これらの仕組みはあらゆるリスクを取り除きはしないが、見知らぬ者同士の協力を無謀ではなく当たり前に感じさせる。",
    "シェアリング・エコノミーが永続する制度へと成熟するのか、それとも一過性の流行として消えるのかは、"
    "技術そのものよりも、こうした信頼が保たれ続けるかどうかにかかっているのかもしれない。"
    "プラットフォームは遊休資産が共有された価値に変えられることを示した。だが、"
    "その仕組みを支える信頼が、自らの急成長を生き延びられるかは、まだ証明していない。",
  ],
  "vocab": [
    ("sharing economy","名","共有型経済、シェアリング・エコノミー"),
    ("asset","名","資産、財産"),
    ("idle","形","使われていない、遊んでいる"),
    ("capacity","名","能力、収容力"),
    ("licensed","形","免許を持つ、認可された"),
    ("regulator","名","規制当局、規制する人"),
    ("sidestep","動","（規則などを）回避する、かわす"),
    ("tension","名","緊張、対立"),
    ("erode","動","（徐々に）むしばむ、損なう"),
    ("verified","形","確認済みの、認証された"),
    ("sustain","動","持続させる、維持する"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は利点・弊害の両論に<b>留保</b>（信頼次第）を加えた1つを選ぶ。",
}
