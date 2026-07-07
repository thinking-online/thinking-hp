# -*- coding: utf-8 -*-
"""大問Ⅲ READING 08 ― 注意経済とデータ・プライバシー。設問文はすべて英語。
本文タグ: [[u:N]]..[[/u]]=下線部(設問N)。"""

SET = {
  "theme": "注意経済 ― 無料サービスが対価にするもの",
  "genre": "テクノロジー／社会 論説（英問英答）",
  "limit": "目標15分",
  "wordcount": 440,
  "passage_title": "The Price of Free",
  "passage": [
    "Every day, billions of people scroll through feeds, watch videos, and search the web without paying a single coin. "
    "These services feel free, but they are not. In what analysts call the attention economy, the true price is the time "
    "users spend looking at a screen and the personal data they leave behind. Companies gather that attention and sell "
    "[[u:32]]it[[/u]] to advertisers, who pay handsomely to reach the right eyes at the right moment.",

    "For ordinary users, the bargain can seem generous. Powerful tools for messaging, mapping, and learning cost nothing "
    "to install. Because platforms track what people click and watch, they can tailor content to individual tastes, "
    "surfacing news, music, and products that feel remarkably [[u:33]]relevant[[/u]]. A well-tuned feed saves time and can "
    "introduce users to ideas they might never have found on their own. In this sense, the attention economy delivers real "
    "value at no obvious cost, which is exactly why so many people embrace it without a second thought.",

    "Yet the same machinery has a darker side. To personalize so precisely, firms must watch users closely, recording "
    "locations, purchases, and even the pauses over a photograph. This constant [[u:34]]surveillance[[/u]] erodes privacy "
    "in ways few people fully notice. Worse, systems built to hold attention can nudge users toward outrage or endless "
    "scrolling, since content that provokes strong feelings keeps eyes on the screen longer, whatever the cost to well-being.",

    "Observers are divided over how alarming this really is. Defenders argue that data-driven advertising funds the free "
    "tools society now depends on, and that most users happily accept the exchange. Critics reply that few people "
    "understand what they are giving away, and that consent buried in long, unread agreements is hardly consent at all. "
    "Between these camps lies a hard question: can a bargain be fair when one side barely sees the terms?",

    "The stakes reach beyond any single account. When a handful of companies hold detailed records of how millions of "
    "people think and behave, that knowledge becomes a form of power. [[u:35]]It[[/u]] can shape which stories spread, "
    "which products win, and even which opinions come to feel normal. A market built to capture attention may quietly "
    "reshape the public square, rewarding whatever is gripping rather than whatever is true.",

    "None of this means the attention economy is beyond repair. The trade of data for service could be worthwhile if "
    "users could see clearly what they surrender and choose freely whether to accept. Stronger transparency and real "
    "control would not end targeted advertising, but they might turn a hidden bargain into an honest one. Until then, the "
    "cheapest services may prove the most expensive of all.",
  ],
  "instr": "Read the passage and answer the questions in English. 各設問は英語である。最も適切なものを1つ選べ。",
  "questions": [
    {"no":32,"tag":"指示語","stem":"In paragraph 1, what does <span class='en'>“it”</span> (and sell it to advertisers) refer to?","inline":True,
     "choices":[
       "the attention companies gather",
       "a single coin",
       "the web itself",
       "a free video"],"answer":"ア",
     "basis":"<span class='en'>Companies gather that attention and sell it</span> の <span class='en'>it</span> は直前の <span class='en'>that attention</span>。",
     "solve":"代名詞は直前の名詞へ。企業が集めて売るのは集めた<b>注意（アテンション）</b>。",
     "cut":"<span class='en'>a single coin</span> は『対価を払わない』例で、売買対象ではない。"},
    {"no":33,"tag":"言い換え","stem":"The word <span class='en'>“relevant”</span> in paragraph 2 is closest in meaning to","inline":True,
     "choices":[
       "pertinent",
       "boring",
       "random",
       "expensive"],"answer":"ア",
     "basis":"<span class='en'>tailor content to individual tastes ... feel remarkably relevant</span>＝好みに<b>関連した</b>。",
     "solve":"各人の好みに合わせて出す内容＝『的を射た・関係の深い』。<span class='en'>pertinent</span> が同義。",
     "cut":"<span class='en'>random</span>（無作為）はむしろ逆で、好みに合わせる文脈と矛盾。"},
    {"no":34,"tag":"言い換え","stem":"The word <span class='en'>“surveillance”</span> in paragraph 3 is closest in meaning to","inline":True,
     "choices":[
       "monitoring",
       "freedom",
       "payment",
       "advertisement"],"answer":"ア",
     "basis":"<span class='en'>firms must watch users closely ... This constant surveillance</span>＝絶えず<b>監視</b>すること。",
     "solve":"位置・購入・写真での間まで記録する＝常時見張る＝監視。<span class='en'>monitoring</span> が同義。",
     "cut":"<span class='en'>freedom</span>（自由）は監視の逆で、プライバシー侵食の文脈に合わない。"},
    {"no":35,"tag":"指示語","stem":"In paragraph 5, what does <span class='en'>“It”</span> (It can shape which stories spread) refer to?","inline":True,
     "choices":[
       "the detailed knowledge companies hold about people",
       "a single account",
       "the free tools users install",
       "the price of one advertisement"],"answer":"ア",
     "basis":"直前 <span class='en'>that knowledge becomes a form of power. It can shape ...</span>＝企業が握る<b>詳細な知識</b>。",
     "solve":"<span class='en'>It</span> は直前主語の <span class='en'>that knowledge</span>（数百万人の思考・行動の記録）を指す。",
     "cut":"<span class='en'>a single account</span> は『個々の利用者を超える』と否定された小さな単位で逆。"},
    {"no":36,"tag":"内容真偽","stem":"According to paragraph 2, why can platforms tailor content to each user?",
     "choices":[
       "Because they track what people click and watch.",
       "Because users pay a monthly fee for the service.",
       "Because the government supplies their data.",
       "Because they ask each user to write a report."],"answer":"ア",
     "basis":"第2段 <span class='en'>Because platforms track what people click and watch, they can tailor content</span> に一致。",
     "solve":"設問の <span class='en'>tailor content</span> を第2段で照合。クリックや視聴の追跡が根拠。",
     "cut":"『月額料金を払うから』は <span class='en'>cost nothing to install</span> と矛盾する。"},
    {"no":37,"tag":"内容真偽(NOT)","stem":"Which of the following is NOT mentioned as a downside of the attention economy?",
     "choices":[
       "Services secretly delete users personal photographs.",
       "Constant surveillance erodes users privacy.",
       "Systems can nudge users toward endless scrolling.",
       "Consent is often buried in long, unread agreements."],"answer":"ア",
     "basis":"『写真をひそかに削除する』は本文に記述がない。他の3つは第3段・第4段に明記。",
     "solve":"<span class='en'>NOT</span> に印。本文にある弊害を消し、残る1つが答え。",
     "cut":"監視でプライバシー侵食（3段）・延々スクロール（3段）・埋もれた同意（4段）は、いずれも弊害として『述べられている』。"},
    {"no":38,"tag":"内容真偽","stem":"According to paragraph 4, what do defenders of data-driven advertising argue?",
     "choices":[
       "It funds the free tools that society now depends on.",
       "It should be banned by every government at once.",
       "It gives users too little content to enjoy.",
       "It forces companies to charge high install fees."],"answer":"ア",
     "basis":"第4段 <span class='en'>Defenders argue that data-driven advertising funds the free tools society now depends on</span>。",
     "solve":"<span class='en'>Defenders argue that ...</span> の直後が擁護の中身。無料ツールを支える資金源だと主張。",
     "cut":"『全面禁止すべき』は擁護側ではなく、批判側にも本文にない言い過ぎ。"},
    {"no":39,"tag":"理由","stem":"According to paragraph 3, why can such systems keep users scrolling longer?",
     "choices":[
       "Because content that provokes strong feelings holds attention longer.",
       "Because users are charged for every minute they scroll.",
       "Because the systems block all upsetting content.",
       "Because platforms limit how much data they collect."],"answer":"ア",
     "basis":"第3段 <span class='en'>content that provokes strong feelings keeps eyes on the screen longer</span>。",
     "solve":"<span class='en'>since ...</span> が理由の合図。強い感情を煽る内容ほど画面に留めるから。",
     "cut":"『動揺させる内容を全て遮断する』は、怒りへ誘う仕組みという記述と正反対。"},
    {"no":40,"tag":"詳細","stem":"According to paragraph 6, what would make the trade of data for service worthwhile?",
     "choices":[
       "Letting users see what they surrender and choose freely whether to accept.",
       "Ending all forms of advertising on every platform.",
       "Charging users a high price for each service.",
       "Collecting even more personal data than before."],"answer":"ア",
     "basis":"第6段 <span class='en'>could be worthwhile if users could see clearly what they surrender and choose freely whether to accept</span>。",
     "solve":"設問の <span class='en'>worthwhile</span> を最終段で照合。透明性と選択権が条件。",
     "cut":"『広告を全廃する』は <span class='en'>would not end targeted advertising</span> と食い違う。"},
    {"no":41,"tag":"主旨/タイトル","stem":"What is the overall content of the passage?",
     "choices":[
       "Free services are paid for with attention and data, and the bargain is fair only with transparency and real choice.",
       "The attention economy has completely destroyed personal privacy everywhere.",
       "Targeted advertising should be banned because it offers no benefits at all.",
       "Users always understand exactly what data they are giving away."],"answer":"ア",
     "basis":"無料の対価（1段）／利点（2段）／弊害（3段）／賛否（4段）／社会的含意（5段）／透明性と選択という留保（6段）の全体像に一致。",
     "solve":"主旨は言い過ぎ・本文にない要素を切り、両論併記＋<b>留保</b>に沿う1つを残す。",
     "cut":"『プライバシーを完全に破壊した』『利点は皆無』『利用者は常に理解している』はいずれも断定しすぎで本文の留保と矛盾。"},
  ],
  "structure":
    "<b>序論[1]</b>『無料』の正体＝注意とデータが対価（注意経済） ／ <b>利点[2]</b>無料の高機能・好みに合う個別化 ／ "
    "<b>弊害[3]</b>常時監視によるプライバシー侵食・怒りへの誘導 ／ <b>論争[4]</b>擁護（無料を支える）vs 批判（同意なき同意） ／ "
    "<b>含意[5]</b>データの集中は権力になり公共空間を歪める ／ <b>結論[6]</b>透明性と選択権があれば公正な取引になりうる（留保）。"
    "　英問英答では、この段構成が<b>設問の並び順</b>とほぼ対応する。設問→該当段の照合で解ける。",
  "trans": [
    "毎日、何十億もの人々が一枚の硬貨も払わずに、フィードをスクロールし、動画を見て、ウェブを検索している。"
    "こうしたサービスは無料に感じられるが、そうではない。分析家が『注意経済』と呼ぶものにおいて、真の対価は、"
    "利用者が画面を見つめて費やす時間と、彼らが残していく個人データである。企業はその注意を集め、"
    "それを広告主に売る。広告主は、適切な相手に適切な瞬間に届くために大枚をはたく。",
    "普通の利用者にとって、この取引は気前よく見えうる。メッセージ送信、地図、学習のための強力な道具が、"
    "無料で導入できる。プラットフォームは人々が何をクリックし何を見るかを追跡するため、内容を各人の好みに"
    "合わせて調整でき、驚くほど自分に関連すると感じられるニュースや音楽や商品を浮かび上がらせる。"
    "よく調整されたフィードは時間を節約し、自力では決して見つけられなかったであろう発想へ利用者を導きうる。",
    "だが同じ仕組みには暗い側面がある。これほど精密に個別化するために、企業は利用者を綿密に見張り、"
    "位置情報や購入履歴、さらには一枚の写真に見入る間の停止までも記録する。この絶え間ない監視は、"
    "ほとんどの人が十分に気づかない形でプライバシーを蝕む。さらに悪いことに、注意を引き留めるよう作られた"
    "仕組みは、利用者を怒りや果てしないスクロールへと誘いうる。強い感情を煽る内容ほど、"
    "幸福を犠牲にしてでも、目を画面に長く留めるからだ。",
    "これがどれほど憂慮すべきかで、観察者の見解は割れている。擁護派は、データ主導の広告が、"
    "いまや社会が依存する無料の道具を支えており、大半の利用者はこの交換を喜んで受け入れていると論じる。"
    "批判派は、自分が何を手放しているかを理解している人はわずかで、長く読まれない規約に埋もれた同意など、"
    "同意とはとても呼べないと反論する。両陣営の間には難しい問いが横たわる――一方がほとんど条件を見ていない取引は、"
    "公正でありうるのか。",
    "その影響は、一つのアカウントの枠を超えて及ぶ。ひと握りの企業が、数百万人がどう考えどう振る舞うかの"
    "詳細な記録を握るとき、その知識は一種の権力となる。それは、どの物語が広まり、どの商品が勝ち、"
    "さらにはどの意見が普通に感じられるようになるかまで、形づくりうる。注意を捕らえるために作られた市場は、"
    "真実であるものよりも、心をつかむものを報いながら、公共の場を静かに作り変えるかもしれない。",
    "とはいえ、これは注意経済が修復不可能だという意味ではない。データとサービスの取引は、"
    "利用者が自分の手放すものをはっきり見て、受け入れるか否かを自由に選べるなら、価値あるものになりうる。"
    "より強い透明性と真の選択権は、ターゲティング広告を終わらせはしないが、隠れた取引を誠実な取引へと"
    "変えうる。それまでは、最も安いサービスが、結局すべての中で最も高くつくかもしれない。",
  ],
  "vocab": [
    ("attention economy","名","注意経済（注意を資源とする経済）"),
    ("feed","名","（SNS等の）フィード、更新表示"),
    ("tailor","動","（好みに）合わせて調整する"),
    ("relevant","形","関連した、的を射た"),
    ("surveillance","名","監視"),
    ("erode","動","（徐々に）蝕む、損なう"),
    ("nudge","動","そっと促す、誘導する"),
    ("consent","名","同意、承諾"),
    ("targeted advertising","名","ターゲティング広告"),
    ("transparency","名","透明性、情報開示"),
    ("surrender","動","（権利などを）手放す、明け渡す"),
  ],
  "lesson":
    "Ⅲは『設問英文を先に読み、疑問詞とキーワードで<b>指示語／言い換え／真偽／理由／主旨</b>に分類→本文で照合』。"
    "設問の並びは段構成に対応する。<span class='en'>NOT</span> と <span class='en'>overall content</span> の指示に必ず印を。"
    "主旨は両論併記＋<b>留保</b>（透明性と選択権があれば公正）を選ぶ。",
}
