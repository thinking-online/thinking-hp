# -*- coding: utf-8 -*-
"""大問Ⅱ READING 02 ― プラットフォーム・ビジネスとネットワーク効果。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "プラットフォーム経済 ― 所有ではなく「つながり」が生む価値",
  "genre": "ビジネス／経済 論説",
  "limit": "目標18分",
  "wordcount": 500,
  "passage_title": "The Power of Connection",
  "passage": [
    "A generation ago, the largest firms were those that owned the most — factories, fleets, and vast stores of goods. "
    "Today some of the world most valuable companies own remarkably little. A ride-hailing giant owns no cars; a booking "
    "site owns no hotels. Their power [[u:14]]hinges on[[/u]] something far less tangible: the ability to connect one group "
    "of people with another. The platform — a business that creates value by linking buyers and sellers — has "
    "[[u:15]]taken off[[/u]] so quickly that it now shapes much of the digital economy.",

    "What makes a platform powerful is a mechanism economists call the network effect. Each additional user makes the "
    "service more useful to everyone else: a marketplace with more sellers [[u:16]]draws in[[/u]] more buyers, whose "
    "presence in turn attracts still more sellers. Value therefore does not merely add up as the platform grows; it "
    "compounds. This self-reinforcing loop explains why a single app can come to dominate an entire market in only a few "
    "years, long before slower rivals understand what has happened.",

    "For users, the benefits are real. A large platform gathers scattered supply and demand into one place, so that a "
    "driver finds a passenger and a passenger finds a driver within minutes. Buyers [[u:17]]reap[[/u]] the convenience of "
    "endless choice and instant comparison, while small sellers gain access to a global audience they could never have "
    "reached on their own. In principle, everyone on both sides of the market comes out ahead.",

    "Yet the very force that makes platforms useful can turn against the public. Because scale breeds scale, markets "
    "shaped by network effects tend toward winner-take-all outcomes, in which one firm [[u:18]]crowds out[[/u]] almost all "
    "of its rivals. Once a platform dominates, it can raise fees, bury competitors in search results, and dictate terms to "
    "the very users who depend on it. What began as a simple tool for connection can [[u:19]]cement[[/u]] a position of "
    "extraordinary and durable power.",

    "For regulators, this concentration poses a genuine dilemma. What ultimately ties users to a dominant platform "
    "[[b:21]] not any single feature but the crowd already gathered there, a crowd that rivals cannot easily copy. To "
    "break up such a firm might destroy the very convenience that attracted people in the first place. Some economists "
    "insist that earlier action was needed: had watchdogs intervened while these markets were still young, a handful of "
    "today giants [[b:22]] far less unassailable now. Faced with this puzzle, authorities increasingly try to "
    "[[u:20]]curb[[/u]] specific abuses rather than dismantle the companies themselves.",

    "In the end, the platform economy rests on a fragile foundation: trust. Users hand over their attention, their data, "
    "and often their livelihoods to firms whose interests may not match their own. Whether these networks continue to "
    "serve the public or quietly exploit their dominance will depend less on the elegance of the technology than on "
    "whether society can keep the largest platforms honest. Connection, it turns out, is a source of value only so long as "
    "it is not abused.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・理由・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>hinges on</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["depends on","recovers from","gives up on","stands for"],"answer":"ア",
     "basis":"<span class='en'>hinge on</span>＝「〜次第である、〜にかかっている」。",
     "solve":"直後の <span class='en'>the ability to connect ...</span>（つなぐ力）が力の源泉だという文脈から『〜にかかっている』。",
     "cut":"<span class='en'>recovers from</span>（回復する）・<span class='en'>gives up on</span>（見限る）は文意に合わない。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>taken off</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["grown rapidly","slowed down","broken apart","fallen behind"],"answer":"ア",
     "basis":"<span class='en'>take off</span>＝「急成長する、一気に普及する」。",
     "solve":"<span class='en'>so quickly that it now shapes much of the digital economy</span> と結び、急拡大の意。",
     "cut":"<span class='en'>slowed down</span>（減速）・<span class='en'>fallen behind</span>（遅れる）は真逆。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>draws in</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["attracts","repels","confuses","replaces"],"answer":"ア",
     "basis":"<span class='en'>draw in</span>＝「引き寄せる、呼び込む」。",
     "solve":"『売り手が増えれば買い手を呼び込み、その買い手がさらに売り手を引き寄せる』という循環から。",
     "cut":"<span class='en'>repels</span>（はねつける）は逆方向。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>reap</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["gain","lose","doubt","delay"],"answer":"ア",
     "basis":"<span class='en'>reap</span>＝「（利益・恩恵を）得る、刈り取る」。",
     "solve":"<span class='en'>reap the convenience of endless choice</span>（豊富な選択肢の利便性を得る）の目的語から『得る』。",
     "cut":"<span class='en'>lose</span>（失う）は逆。<span class='en'>doubt/delay</span> は文意に無関係。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>crowds out</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["shuts out","makes room for","teams up with","waits for"],"answer":"ア",
     "basis":"<span class='en'>crowd out</span>＝「締め出す、押しのける」。",
     "solve":"<span class='en'>winner-take-all</span>（勝者総取り）で『1社がほぼすべての競合を締め出す』文脈。",
     "cut":"<span class='en'>makes room for</span>（場所を空ける）・<span class='en'>teams up with</span>（提携する）は逆または無関係。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>cement</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["solidify","undermine","abandon","conceal"],"answer":"ア",
     "basis":"動詞 <span class='en'>cement</span>＝「（地位などを）固める、確固たるものにする」。",
     "solve":"<span class='en'>a position of extraordinary and durable power</span> を『固める』の意。",
     "cut":"<span class='en'>undermine</span>（弱める）は逆。名詞の『セメント』に引かれず動詞用法で判断。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>curb</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["restrain","encourage","ignore","measure"],"answer":"ア",
     "basis":"動詞 <span class='en'>curb</span>＝「抑制する、食い止める」。",
     "solve":"<span class='en'>curb specific abuses rather than dismantle the companies</span>（企業解体でなく特定の弊害を抑える）から。",
     "cut":"<span class='en'>encourage</span>（助長）は逆。<span class='en'>ignore</span>（無視）では規制の意図に反する。"},
    {"no":21,"tag":"E 語法","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["is","are","being","to be"],"answer":"ア",
     "basis":"主語は名詞節 <span class='en'>What ultimately ties users to a dominant platform</span>＝<b>単数扱い</b>。<span class='en'>What</span> 節は三単現。",
     "solve":"<span class='en'>What ... is not any single feature but the crowd</span>「利用者を縛るのは単一の機能ではなく、すでに集まった群衆だ」。<span class='en'>not A but B</span> の構文。",
     "cut":"<span class='en'>What</span> 節主語を複数と誤り <span class='en'>are</span> を選ばない。<span class='en'>being/to be</span> では定形動詞が無く文が成立しない。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would be","would have been","will be","were"],"answer":"ア",
     "basis":"文頭 <span class='en'>had watchdogs intervened ...</span> は <span class='en'>if watchdogs had intervened</span> の倒置＝過去の条件。ただし帰結節末に <span class='en'>now</span> があり<b>現在の結果</b>を述べる<b>混合仮定法</b>。よって帰結は <span class='en'>would + 動詞原形</span>。",
     "solve":"「もし監視当局が早く介入していたら、今日の巨大企業のいくつかは<b>今ほど盤石ではなかっただろう</b>」。過去の仮定→現在の帰結。",
     "cut":"<span class='en'>would have been</span> は帰結も過去の場合で、<span class='en'>now</span> と時制が矛盾。<span class='en'>will be</span> は仮定法にならない。"},
    {"no":23,"tag":"D 情報整序","stem":"第2段で説明される『ネットワーク効果』の循環を、本文の論理に沿って正しい順に並べたものを選べ。"
        "　(あ)売り手が増えると買い手が集まる　(い)集まった買い手がさらに売り手を引き寄せる　(う)価値が足し算でなく相乗的に増える　(え)1つのアプリが市場全体を支配する",
     "choices":["あ → い → う → え","い → あ → え → う","う → あ → い → え","え → い → あ → う"],"answer":"ア",
     "basis":"第2段は『売り手増→買い手増(あ)→その買い手がさらに売り手を引き寄せ(い)→価値が相乗的に増え(う)→1つのアプリが市場を支配(え)』の順。",
     "solve":"<span class='en'>in turn</span> と <span class='en'>compounds</span>、結論の <span class='en'>dominate an entire market</span> で因果の向きを確定。最初(あ)と最後(え)を固定して挟み撃ち。",
     "cut":"『相乗的に増える(う)』や『市場支配(え)』を循環の前に置く並びは因果が逆で誤り。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "筆者は、規制当局はためらわず支配的企業を解体すべきだと断言している。",
       "配車大手が車を、予約サイトがホテルを所有しないように、価値の源泉は所有物より「つながり」にある。",
       "ネットワーク効果では利用者が増えるほどサービスの有用性が高まる。",
       "小さな売り手も、単独では届かない世界規模の顧客に接近できる。"],
     "answer":"ア",
     "basis":"第5段は解体すると利便性まで壊しかねないという<b>ジレンマ</b>を述べ、当局は <span class='en'>curb specific abuses rather than dismantle</span>（解体でなく弊害の抑制）へ向かうとする。『ためらわず解体すべきと断言』は本文と逆。",
     "solve":"設問の『合致しない』に印。断定的な選択肢を本文の留保・ジレンマと照合。",
     "cut":"他の3つ（つながりが価値／利用者増で有用性増／小売り手の世界市場接近）はいずれも本文に一致。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "ネットワーク効果により、価値は単なる足し算でなく相乗的に増える。",
       "プラットフォームは規模が大きくなるほど競争が激しく分散する傾向がある。",
       "支配的企業になっても手数料や取引条件を一方的に決めることはできない。",
       "利用者にとってプラットフォームの利点は理屈の上だけで実際には存在しない。"],
     "answer":"ア",
     "basis":"第2段 <span class='en'>Value ... does not merely add up ...; it compounds</span> と一致。",
     "solve":"本文の該当文を特定して照合。",
     "cut":"『規模が大きいほど分散』は第4段 <span class='en'>winner-take-all</span> と逆。『条件を一方的に決められない』は <span class='en'>dictate terms</span> と矛盾。『利点は実際には存在しない』は第3段 <span class='en'>the benefits are real</span> と矛盾。"},
    {"no":26,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "支配的な地位が続くかどうかは、社会が巨大企業を誠実に保てるかにかかっている。",
       "プラットフォーム経済は所有する資産の量によって支えられている。",
       "早期に介入していても、巨大企業の力は今と全く変わらなかっただろう。",
       "利用者はデータや注意を企業に渡さずにサービスを利用できる。"],
     "answer":"ア",
     "basis":"第6段 <span class='en'>will depend ... on whether society can keep the largest platforms honest</span> と一致。",
     "solve":"最終段の留保（trust・honest）を述べた選択肢を選ぶ。",
     "cut":"『所有資産の量で支えられる』は第1段（所有はわずか）と逆。『早期介入でも力は変わらない』は第5段の混合仮定法（今ほど盤石でなかっただろう）と矛盾。『データを渡さず利用できる』は第6段 <span class='en'>hand over their attention, their data</span> と矛盾。"},
    {"no":27,"tag":"F 指示語","stem":"第4段の <span class='en'>the very users who depend on it</span> における <span class='en'>it</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["the dominant platform（支配的なプラットフォーム）","the fee（手数料）","the rival（競合他社）","the regulator（規制当局）"],"answer":"ア",
     "basis":"第4段 <span class='en'>Once a platform dominates, it can raise fees ... and dictate terms to the very users who depend on it</span>。<span class='en'>it</span>＝支配的プラットフォーム。",
     "solve":"直前の主語 <span class='en'>a platform</span>（＝<span class='en'>it</span>）を確認。利用者が『依存する』対象＝そのプラットフォーム。",
     "cut":"<span class='en'>fee</span> は動作の目的語であって利用者が依存する対象ではない。"},
    {"no":28,"tag":"C 理由","stem":"支配的なプラットフォームを解体しても解決にならないと論じられるのはなぜか。最も適切なものを選べ。",
     "choices":[
       "利用者を引きつけていた「集まった群衆」という利便性そのものを壊してしまうから。",
       "解体には巨額の費用がかかり規制当局が負担できないから。",
       "競合他社が支配的企業をすぐに買収してしまうから。",
       "利用者が新しい機能を求めて自然に別の企業へ移るから。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>To break up such a firm might destroy the very convenience that attracted people in the first place</span>＋『価値の源泉は <span class='en'>the crowd already gathered there</span>』。",
     "solve":"『解体＝利便性の破壊』というジレンマの因果を直接結ぶ。",
     "cut":"『費用負担』『競合の買収』『機能目当ての移動』はいずれも本文に記述がない。"},
    {"no":29,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "プラットフォームはつながりによって双方に価値を生む一方、勝者総取りの弊害を抱え、その是非は社会が巨大企業を誠実に保てるかにかかっている。",
       "ネットワーク効果は技術の力によって必ず消費者を豊かにする。",
       "所有はもはや無意味であり、企業は資産を一切持つべきではない。",
       "規制当局は支配的プラットフォームを直ちにすべて解体すべきである。"],
     "answer":"ア",
     "basis":"利点（2・3段）／勝者総取りの弊害（4段）／解体のジレンマ（5段）／是非は誠実さ・信頼次第（6段）という論の全体像に一致。",
     "solve":"主旨は『言い過ぎ・本文にない要素』を切り、筆者の両論併記＋留保に沿う1つを残す。",
     "cut":"『必ず消費者を豊かにする』『資産を一切持つべきでない』は断定しすぎ(too broad)。『直ちにすべて解体すべき』は第5段のジレンマ（解体は利便性を壊す）と矛盾。"},
  ],
  "structure":
    "<b>序論[1]</b>所有から「つながり」へ・プラットフォームの台頭 ／ <b>本論(仕組み)[2]</b>ネットワーク効果と価値の相乗 ／ "
    "<b>本論(利点)[3]</b>需給集約・双方に恩恵 ／ <b>反論[4]</b>勝者総取りと支配の弊害 ／ "
    "<b>核心[5]</b>解体のジレンマと規制の方向（留保の伏線） ／ <b>結論[6]</b>是非は信頼＝誠実さ次第（留保）。"
    "　――『利点→弊害→ジレンマ→留保』の典型的な論説構造。主旨問題はこの<b>留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "一世代前、最大の企業とは最も多くを所有する企業だった――工場、車両、そして膨大な在庫を。今日、世界で最も価値ある"
    "企業のいくつかは、驚くほど何も所有していない。配車の巨人は車を持たず、予約サイトはホテルを持たない。その力は、"
    "はるかに形のないものにかかっている――ある集団と別の集団を結びつける能力だ。買い手と売り手をつなぐことで価値を生む"
    "事業であるプラットフォームは、あまりに急速に普及し、今やデジタル経済の多くを形づくっている。",
    "プラットフォームを強力にするのは、経済学者が「ネットワーク効果」と呼ぶ仕組みだ。利用者が1人増えるたびに、"
    "サービスは他の全員にとってより有用になる。売り手の多い市場はより多くの買い手を呼び込み、その買い手の存在が今度は"
    "さらに多くの売り手を引き寄せる。ゆえに価値は、プラットフォームの成長に伴って単に足し算されるのではなく、相乗的に"
    "増える。この自己強化のループが、たった1つのアプリがわずか数年で市場全体を支配しうる理由を説明する――出遅れた"
    "競合が何が起きたのかを理解するはるか前に。",
    "利用者にとって、利点は現実のものだ。大きなプラットフォームは散在する供給と需要を一か所に集め、運転手は数分で"
    "乗客を、乗客は数分で運転手を見つける。買い手は豊富な選択肢と即座の比較という利便性を得て、小さな売り手は"
    "単独では決して届かなかった世界規模の顧客に接近できる。原理上、市場の両側の誰もが得をする。",
    "だが、プラットフォームを有用にするまさにその力が、公共の利益に牙をむくことがある。規模が規模を生むため、"
    "ネットワーク効果に形づくられた市場は勝者総取りの結果へ傾き、そこでは1社がほぼすべての競合を締め出す。"
    "いったんプラットフォームが支配すれば、手数料を上げ、競合を検索結果に埋もれさせ、依存する当の利用者に条件を"
    "押しつけることができる。単なるつながりの道具として始まったものが、並外れて持続的な力の地位を固めうるのだ。",
    "規制当局にとって、この集中は真のジレンマを突きつける。利用者を支配的プラットフォームに最終的につなぎ止めるのは、"
    "単一の機能ではなく、すでにそこに集まった群衆であり、その群衆は競合が容易に模倣できない。そうした企業を解体すれば、"
    "人々を最初に引きつけた利便性そのものを壊しかねない。一部の経済学者は、より早い対応が必要だったと主張する――"
    "もし監視当局がこれらの市場がまだ若いうちに介入していたら、今日の巨大企業のいくつかは今ほど盤石ではなかっただろう。"
    "この難題に直面し、当局は企業そのものを解体するより、特定の弊害を抑える方向へと次第に傾いている。",
    "結局のところ、プラットフォーム経済は脆い土台の上に立っている――信頼だ。利用者は自らの注意、データ、そしてしばしば"
    "生計までも、利害が自分と一致しないかもしれない企業に委ねる。これらのネットワークが公共に資し続けるのか、それとも"
    "支配的地位を静かに悪用するのかは、技術の巧みさよりも、社会が最大のプラットフォームを誠実に保てるかにかかっている。"
    "つながりとは、結局のところ、悪用されない限りにおいてのみ価値の源泉なのだ。",
  ],
  "vocab": [
    ("hinge on","句動","〜次第である、〜にかかっている"),
    ("take off","句動","急成長する、一気に普及する"),
    ("network effect","名","ネットワーク効果"),
    ("draw in","句動","引き寄せる、呼び込む"),
    ("compound","動","相乗的に増える、複利的に膨らむ"),
    ("reap","動","（利益・恩恵を）得る、刈り取る"),
    ("winner-take-all","形","勝者総取りの"),
    ("crowd out","句動","締め出す、押しのける"),
    ("cement","動","（地位を）固める、確固たるものにする"),
    ("curb","動","抑制する、食い止める"),
    ("unassailable","形","難攻不落の、揺るがない"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『利点→弊害→ジレンマ→留保』の型。とくに<b>混合仮定法</b>"
    "（過去の条件＋<span class='en'>now</span> の現在帰結）は <span class='en'>would+原形</span> を選ぶ。主旨は必ず筆者の<b>留保</b>に沿う。",
}
