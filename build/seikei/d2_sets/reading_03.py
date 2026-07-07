# -*- coding: utf-8 -*-
"""大問Ⅱ READING 03 ― リモートワークと生産性・組織文化。
本文タグ: [[u:N]]...[[/u]]=下線部(設問N), [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "リモートワークと組織文化 ― 効率と信頼のあいだ",
  "genre": "ビジネス／社会 論説",
  "limit": "目標18分",
  "wordcount": 500,
  "passage_title": "The Trust Behind the Screen",
  "passage": [
    "A decade ago, working from home was a rare privilege granted to a lucky few. When offices emptied almost "
    "overnight during the pandemic, millions of employees suddenly [[u:14]]took to[[/u]] remote work, and many "
    "discovered they liked it. Freed from long commutes and constant interruptions, they found they could "
    "[[u:15]]carve out[[/u]] quiet hours for focused tasks. What began as an emergency measure has since hardened "
    "into a permanent feature of working life.",

    "The case for remote work is, on the surface, persuasive. Studies suggest that people who work from home often "
    "finish routine tasks faster, precisely because no one drops by their desk to chat. For the company, the savings "
    "are [[u:16]]substantial[[/u]]: less office space, lower overheads, and access to talent far beyond the local "
    "area. Early surveys seemed to confirm the optimism, with output holding steady or even climbing in the first "
    "year. Workers, meanwhile, gain control over their own schedules, which many prize more highly than a pay rise.",

    "Autonomy, however, cuts both ways. Given the freedom to choose when and where they work, most employees rise to "
    "the occasion and [[u:17]]live up to[[/u]] the trust placed in them. Trusted employees, research repeatedly "
    "shows, tend to guard that trust jealously. A parent can attend a school event at noon and finish a report at "
    "night. Such flexibility, its supporters insist, treats adults as adults rather than as workers to be watched "
    "and timed.",

    "Yet something is lost when the office falls silent. The casual chat by the coffee machine, the overheard remark "
    "that sparks an idea — these chance encounters rarely [[u:18]]crop up[[/u]] on a scheduled video call. A quick "
    "question that would take seconds in person becomes an email, a delay, a missed connection. Newcomers, in "
    "particular, struggle to absorb the unwritten rules of a team when they never sit among their colleagues. Over "
    "time, a scattered workforce can [[u:19]]drift apart[[/u]], its members loyal to their own convenience rather "
    "than to any shared purpose.",

    "The heart of the matter, then, is not location but trust. [[b:21]] employees closely through monitoring "
    "software rarely produces the results managers hope for; it breeds resentment instead. Had firms grasped this "
    "sooner, they [[b:22]] far less on tracking keystrokes and far more on setting clear goals. What truly "
    "[[u:20]]holds a team together[[/u]] is a shared belief that each member will deliver, whether seen or unseen.",

    "None of this means the office must return in full. Some tasks demand the friction of being in one room; others "
    "thrive in solitude. The best arrangement is likely a hybrid one, blending days together with days apart. But "
    "the deeper lesson is that no policy, however clever, can substitute for trust. Whether remote work strengthens "
    "an organization or slowly erodes it may depend less on where people sit than on whether their leaders are "
    "willing to loosen their grip and believe in those they cannot see.",
  ],
  "instr": "次の英文を読み、設問（下線部言い換え・語法・情報整序・内容真偽/一致・指示語・主旨）に答えよ。",
  "questions": [
    {"no":14,"tag":"B 言い換え","stem":"下線部(14) <span class='en'>took to</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["embraced","abandoned","postponed","questioned"],"answer":"ア",
     "basis":"<span class='en'>take to A</span>＝「Aを好きになる、Aになじむ」。<span class='en'>embrace</span>（進んで受け入れる）が同義。",
     "solve":"直後の <span class='en'>and many discovered they liked it</span>（気に入った）が言い換えの手がかり。",
     "cut":"<span class='en'>abandoned</span>（見捨てた）は真逆。<span class='en'>postponed</span>（延期した）は文意に合わない。"},
    {"no":15,"tag":"B 言い換え","stem":"下線部(15) <span class='en'>carve out</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["set aside","use up","give away","cut short"],"answer":"ア",
     "basis":"<span class='en'>carve out time</span>＝「（努力して）時間を作り出す・確保する」。<span class='en'>set aside</span>（取り分ける）が近い。",
     "solve":"<span class='en'>quiet hours for focused tasks</span>（集中作業のための静かな時間）を『確保する』文脈。",
     "cut":"<span class='en'>use up</span>（使い果たす）は逆方向。<span class='en'>cut short</span>（短く切り上げる）も不適。"},
    {"no":16,"tag":"B 言い換え","stem":"下線部(16) <span class='en'>substantial</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["considerable","negligible","temporary","uncertain"],"answer":"ア",
     "basis":"<span class='en'>substantial</span>＝「かなりの、相当な」。<span class='en'>considerable</span> が同義。",
     "solve":"直後のコロン以下 <span class='en'>less office space, lower overheads ...</span> が『大きな削減』を具体化。",
     "cut":"<span class='en'>negligible</span>（取るに足らない）は真逆。<span class='en'>temporary</span>（一時的）は量ではなく期間の語で不適。"},
    {"no":17,"tag":"B 言い換え","stem":"下線部(17) <span class='en'>live up to</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["fulfill","fall short of","take away","give up"],"answer":"ア",
     "basis":"<span class='en'>live up to A</span>＝「A（期待・信頼）に応える」。<span class='en'>fulfill</span>（満たす）が近い。",
     "solve":"<span class='en'>the trust placed in them</span>（寄せられた信頼）に『応える』という肯定文脈。",
     "cut":"<span class='en'>fall short of</span>（及ばない）は逆。<span class='en'>give up</span>（あきらめる）も不適。"},
    {"no":18,"tag":"B 言い換え","stem":"下線部(18) <span class='en'>crop up</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["arise","fade away","break down","carry on"],"answer":"ア",
     "basis":"<span class='en'>crop up</span>＝「（偶然に）生じる、持ち上がる」。<span class='en'>arise</span> が同義。",
     "solve":"<span class='en'>chance encounters rarely crop up on a video call</span>（偶発的な出会いはビデオ会議では起きにくい）。",
     "cut":"<span class='en'>fade away</span>（消えていく）は逆。<span class='en'>break down</span>（故障する）も文意に合わない。"},
    {"no":19,"tag":"B 言い換え","stem":"下線部(19) <span class='en'>drift apart</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["grow distant","come together","settle down","speed up"],"answer":"ア",
     "basis":"<span class='en'>drift apart</span>＝「次第に疎遠になる・ばらばらになる」。<span class='en'>grow distant</span> が近い。",
     "solve":"<span class='en'>a scattered workforce</span>（散り散りの従業員）が『共通の目的より各自の都合に忠実になる』流れ。",
     "cut":"<span class='en'>come together</span>（まとまる）は真逆。<span class='en'>settle down</span>（落ち着く）も不適。"},
    {"no":20,"tag":"B 言い換え","stem":"下線部(20) <span class='en'>holds a team together</span> の意味に最も近いものを選べ。","inline":True,
     "choices":["unites a team","divides a team","replaces a team","monitors a team"],"answer":"ア",
     "basis":"<span class='en'>hold ... together</span>＝「〜をまとめる・結束させる」。<span class='en'>unite</span>（団結させる）が同義。",
     "solve":"直後の <span class='en'>a shared belief that each member will deliver</span>（各自がやり遂げるという共有された信念）が結束の核。",
     "cut":"<span class='en'>divides</span>（分断する）は逆。<span class='en'>monitors</span>（監視する）は本文が否定する方向。"},
    {"no":21,"tag":"E 語法","stem":"空所(21)に入る最も適切な語形を選べ。","inline":True,
     "choices":["Watching","Watched","Watch","To be watched"],"answer":"ア",
     "basis":"文の主語が必要で、動名詞 <span class='en'>Watching employees closely ...</span>＝<b>単数扱い</b>。述語動詞 <span class='en'>produces</span>（三単現）と一致する。",
     "solve":"<span class='en'>Watching employees closely ... rarely produces the results</span>「社員を細かく見張っても望む成果はまず出ない」。",
     "cut":"<span class='en'>Watch</span>（命令形）や過去分詞 <span class='en'>Watched</span> は主語になれない。受動の <span class='en'>To be watched</span> は『見張られること』で意味が逆。"},
    {"no":22,"tag":"E 語法/仮定法","stem":"空所(22)に入る最も適切な語句を選べ。","inline":True,
     "choices":["would have relied","will rely","relied","would rely"],"answer":"ア",
     "basis":"文頭 <span class='en'>Had firms grasped this sooner</span> は <span class='en'>If firms had grasped</span> の倒置＝<b>仮定法過去完了</b>。帰結節は <span class='en'>would have + 過去分詞</span>。",
     "solve":"「もし企業が早く気づいていたら、打鍵の追跡に頼ることははるかに<b>少なかっただろう</b>」。<span class='en'>rely on</span> の目的語が <span class='en'>on tracking keystrokes</span>。",
     "cut":"<span class='en'>would rely</span>（仮定法過去）は過去完了の条件節と時制が不一致。<span class='en'>will rely / relied</span> は仮定法の帰結形になっていない。"},
    {"no":23,"tag":"D 情報整序","stem":"第5段で述べられる論理を、本文に沿って正しい順に並べたものを選べ。"
        "　(あ)明確な目標を設定する　(い)監視ソフトで社員を細かく見張る　(う)社員の反感を生む　(え)問題の核心は信頼だと気づく",
     "choices":["え → い → う → あ","い → う → あ → え","え → あ → い → う","い → え → う → あ"],"answer":"ア",
     "basis":"第5段は『核心は場所でなく信頼(え)→社員を監視する(い)→望む成果でなく反感を生む(う)→（気づいていれば）明確な目標設定に注力していた(あ)』の順。",
     "solve":"<span class='en'>not location but trust</span> を起点(え)に固定し、<span class='en'>breeds resentment</span>(う)が監視(い)の結果である因果を確定して挟み撃ち。",
     "cut":"『明確な目標設定(あ)』は仮定法 <span class='en'>Had firms grasped ...</span> の帰結として最後に来る。監視(い)を最初に置く順は核心提示(え)の後という論理に反する。"},
    {"no":24,"tag":"C 内容不一致","stem":"本文の内容と<b>合致しないもの</b>を選べ。",
     "choices":[
       "筆者は、在宅勤務が必ず生産性を高めると断言している。",
       "在宅勤務は通勤や絶え間ない中断から人を解放し、集中の時間を作れる面がある。",
       "監視ソフトで社員を細かく見張っても、管理職が望む成果はまず出ない。",
       "新人は同僚と席を並べないと、チームの暗黙のルールを吸収しにくい。"],
     "answer":"ア",
     "basis":"第2段は <span class='en'>Studies suggest</span>・<span class='en'>seemed to</span> と<b>控えめな表現</b>で述べ、第6段では是非を信頼次第と留保する。『必ず高める』とは断言していない。",
     "solve":"設問の『合致しない』に印。断定語（必ず）を本文の控えめな表現・留保と照合して切る。",
     "cut":"他の3つ（通勤からの解放と集中時間＝第1段／監視は成果を生まない＝第5段／新人は暗黙のルールを吸収しにくい＝第4段）はいずれも本文に一致。"
           "『必ず生産性を高める』だけが本文の慎重な書きぶりを無視した言い過ぎ(too broad)で誤り。"},
    {"no":25,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "自律を与えられた多くの社員は、寄せられた信頼に応えようとする。",
       "偶発的な雑談はビデオ会議でも頻繁に生じる。",
       "企業にとって在宅勤務のコスト削減効果はわずかである。",
       "筆者はオフィスへの完全復帰を明確に主張している。"],
     "answer":"ア",
     "basis":"第3段 <span class='en'>most employees rise to the occasion and live up to the trust placed in them</span> と一致。",
     "solve":"本文の該当文を特定して照合する。",
     "cut":"『雑談がビデオ会議でも頻繁に生じる』は第4段 <span class='en'>rarely crop up on a scheduled video call</span> と矛盾。"
           "『コスト削減はわずか』は第2段 <span class='en'>substantial</span> と逆。『完全復帰を主張』は第6段 <span class='en'>None of this means the office must return in full</span> と真逆。"},
    {"no":26,"tag":"C 内容一致","stem":"本文の内容と<b>一致するもの</b>を選べ。",
     "choices":[
       "最適な働き方はおそらく、出社と在宅を組み合わせたハイブリッド型である。",
       "監視ソフトは社員の信頼を高め、生産性を押し上げる。",
       "在宅勤務の是非は、技術そのものの性能だけで決まる。",
       "新人は在宅勤務の方が、チームの暗黙のルールを学びやすい。"],
     "answer":"ア",
     "basis":"第6段 <span class='en'>The best arrangement is likely a hybrid one, blending days together with days apart</span> と一致。",
     "solve":"最終段の結論部を照合。<span class='en'>hybrid</span>（混合型）が最適解として挙げられる。",
     "cut":"『監視ソフトが信頼を高める』は第5段 <span class='en'>it breeds resentment</span> と矛盾。"
           "『技術の性能だけで決まる』は第6段 <span class='en'>depend less on ... than on whether their leaders are willing to ... believe</span>（信頼次第）と逆。『新人は在宅の方が学びやすい』は第4段と矛盾。"},
    {"no":27,"tag":"F 指示語","stem":"最終段の <span class='en'>those they cannot see</span> が指すものとして最も適切なものを選べ。","inline":True,
     "choices":["employees（社員）","leaders（管理職）","policies（方針）","offices（オフィス）"],"answer":"ア",
     "basis":"<span class='en'>they</span>＝<span class='en'>their leaders</span>（管理職）。『管理職が見ることのできない人々』＝離れて働く社員。",
     "solve":"指示語は直前の主語を確認。<span class='en'>leaders are willing to ... believe in those they cannot see</span>。",
     "cut":"<span class='en'>leaders</span> は『見る側』であって『見られない人々』ではない。方針やオフィスは『信じる』対象として不自然。"},
    {"no":28,"tag":"C 理由","stem":"監視ソフトで社員を見張っても管理職の望む成果が出にくいのはなぜか。最も適切なものを選べ。",
     "choices":[
       "社員の反感を生むから。",
       "通信費が大きくかさむから。",
       "多くの国で法律により禁じられているから。",
       "新人の数が急に増えるから。"],
     "answer":"ア",
     "basis":"第5段 <span class='en'>rarely produces the results managers hope for; it breeds resentment instead</span>。",
     "solve":"セミコロン以下 <span class='en'>it breeds resentment instead</span> が『成果が出ない』理由を直接説明。",
     "cut":"『通信費』『法律で禁止』『新人が増える』はいずれも本文に記述がない。"},
    {"no":29,"tag":"F 主旨/タイトル","stem":"本文全体の主旨として最も適切なものを選べ。",
     "choices":[
       "在宅勤務は効率と自由をもたらす一方で偶発的な対話や帰属意識を失わせ、最適解は制度そのものより信頼の設計にある。",
       "在宅勤務は生産性を必ず高めるので、あらゆる企業が全面的に導入すべきである。",
       "オフィスはもはや時代遅れであり、完全に廃止すべきである。",
       "社員を監視ソフトで厳しく管理することこそが、組織成功の鍵である。"],
     "answer":"ア",
     "basis":"利点（1〜3段）／偶発的対話と帰属意識の喪失という弊害（4段）／核心は信頼(5段)／制度より信頼次第という留保(6段)の全体像に一致。",
     "solve":"主旨は『言い過ぎ・本文にない主張』を切り、筆者の両論併記＋留保に沿う1つを残す。",
     "cut":"『必ず高めるので全面導入』『オフィスを完全廃止』は断定しすぎ(too broad)。『監視こそ成功の鍵』は第5段の主張と真逆。"},
  ],
  "structure":
    "<b>序論[1]</b>在宅勤務の常態化 ／ <b>本論(効率)[2]</b>速さ・コスト削減・裁量という利点 ／ "
    "<b>本論(自律)[3]</b>信頼に応える社員・柔軟性 ／ <b>反論[4]</b>偶発的対話と帰属意識の喪失 ／ "
    "<b>核心[5]</b>問題は場所でなく信頼／監視は反感を生む ／ <b>結論[6]</b>最適解はハイブリッド、是非は信頼次第（留保）。"
    "　――『利点→弊害→核心→留保』の典型的な論説構造。主旨問題はこの<b>留保</b>を捉えた選択肢を選ぶ。",
  "trans": [
    "十年前、在宅勤務は幸運な少数に与えられる稀な特権だった。パンデミックの間にオフィスがほぼ一夜にして空になると、"
    "何百万もの従業員が突然リモートワークになじみ、多くがそれを気に入った。長い通勤や絶え間ない中断から解放され、"
    "彼らは集中作業のための静かな時間を確保できることに気づいた。緊急措置として始まったものは、その後、"
    "働き方の恒久的な特徴として定着した。",
    "在宅勤務を支持する論拠は、一見すると説得力がある。研究によれば、在宅で働く人はしばしば定型業務をより速く終える。"
    "まさに誰も雑談しに机へ立ち寄らないからだ。企業にとって、削減効果は相当に大きい――オフィス面積は減り、"
    "諸経費は下がり、地元をはるかに超えた人材にも手が届く。初期の調査は楽観を裏づけるように見え、"
    "最初の一年は生産量が横ばい、あるいは上昇さえした。一方で労働者は自らの予定を握れるようになり、"
    "多くはそれを昇給以上に高く評価する。",
    "だが自律は諸刃の剣でもある。いつどこで働くかを選ぶ自由を与えられると、多くの社員は期待に応え、"
    "寄せられた信頼に応えようとする。信頼された社員は、研究が繰り返し示すように、その信頼を大切に守ろうとする傾向がある。"
    "親は正午に学校行事に出て、夜に報告書を仕上げられる。こうした柔軟性は、支持者に言わせれば、"
    "大人を監視され時間を計られる労働者としてではなく、大人として扱うものだ。",
    "しかしオフィスが静まり返ると、失われるものもある。コーヒーメーカーのそばの何気ない雑談、"
    "ふと耳にした一言がアイデアを生む――こうした偶然の出会いは、予定されたビデオ会議ではめったに生じない。"
    "対面なら数秒で済む簡単な質問が、メールになり、遅れになり、途切れたつながりになる。"
    "とりわけ新人は、同僚のあいだに座ることが一度もないと、チームの暗黙のルールを吸収するのに苦労する。"
    "時間が経つと、散り散りになった従業員はばらばらになりかねず、その一人ひとりは共通の目的よりも自分の都合に忠実になる。",
    "では問題の核心は、場所ではなく信頼である。監視ソフトで社員を細かく見張っても、管理職が望む成果はまず出ない。"
    "かえって反感を生むだけだ。もし企業がこれに早く気づいていたら、打鍵の追跡にはるかに頼らず、"
    "明確な目標を設定することにこそはるかに力を注いでいただろう。チームを本当にまとめるのは、"
    "見られていようといまいと各自がやり遂げるという、共有された信念である。",
    "とはいえ、これはオフィスが完全に復活しなければならないという意味ではない。ある業務は同じ部屋にいるという摩擦を必要とし、"
    "別の業務は孤独の中でこそ栄える。最適な形はおそらく、出社の日と離れて働く日を組み合わせたハイブリッド型だろう。"
    "だがより深い教訓は、どれほど巧妙な制度も信頼の代わりにはならないということだ。"
    "リモートワークが組織を強くするのか、それとも静かに蝕むのかは、人がどこに座るかよりも、"
    "指導者が手綱を緩め、見えない相手を信じる気があるかどうかにかかっているのかもしれない。",
  ],
  "vocab": [
    ("take to","句動","〜を好きになる、なじむ"),
    ("carve out","句動","（時間などを）作り出す、確保する"),
    ("substantial","形","かなりの、相当な"),
    ("overheads","名","諸経費、間接費"),
    ("live up to","句","（期待・信頼）に応える"),
    ("crop up","句動","（偶然）生じる、持ち上がる"),
    ("drift apart","句動","次第に疎遠になる、ばらばらになる"),
    ("breed","動","（感情などを）生む、育む"),
    ("keystroke","名","打鍵、キー入力"),
    ("hold together","句動","〜をまとめる、結束させる"),
    ("loosen one's grip","句","手綱を緩める、支配を弱める"),
  ],
  "lesson":
    "Ⅱ型は『言い換え7問を語彙で秒殺→語法(E)は主語と時制/仮定法で判定→整序(D)は因果語で挟み撃ち→真偽(C)は"
    "<b>言い過ぎ(too broad)</b>を切る』。本文は『利点→弊害→核心→留保』の型。主旨問題は必ず筆者の<b>留保</b>"
    "（制度より信頼次第）に沿う選択肢を選ぶ。",
}
