# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 04（会話2本×空所13）。
Set A(空所1-7)＝ゼミの新商品ブレスト、Set B(空所8-13)＝図書館でグループ学習の予定調整。"""

SET = {
  "theme": "新商品アイデアのブレスト ＆ 図書館でグループ学習の予定調整",
  "scene": "経営学部のゼミ室／大学図書館のラーニングコモンズ",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "ゼミで新商品・新サービスのアイデアを出し合う学生2人（Ren と Aya）",
      "lines": [
        ("Aya", "Ren, how's the brainstorming ( 1 )? Any ideas for the new-product project?"),
        ("Ren", "A couple. My favorite is a subscription box that could really ( 2 ) out in a crowded market."),
        ("Aya", "Nice. Who are we ( 3 ) this at, though? We need a clear target ( 4 )."),
        ("Ren", "Young professionals ― money but no time. Convenience would be our main selling ( 5 )."),
        ("Aya", "And costs? Fresh items add ( 6 ) fast."),
        ("Ren", "True, but if we buy in bulk and keep things lean, I think it's worth a ( 7 )."),
      ],
      "bank": [("a","aiming"),("b","deal"),("c","stand"),("d","up"),
               ("e","market"),("f","break"),("g","going"),("h","shot"),("i","point")],
      "answers": {1:"going",2:"stand",3:"aiming",4:"market",5:"point",6:"up",7:"shot"},
      "exp": {
        1:{"frame":"<span class='en'>how's the brainstorming ( )</span>。be動詞 <span class='en'>is</span> の後なので<b>-ing 形</b>が枠に合う。",
           "logic":"<span class='en'>How's … going?</span>＝「〜の進み具合はどう？」。進捗を尋ねる会話定型。",
           "trap":"もう一つの-ing候補 <span class='en'>aiming</span> は「〜を狙う」で、主語 <span class='en'>brainstorming</span> と意味が繋がらない。"},
        2:{"frame":"<span class='en'>could really ( ) out</span>。助動詞 <span class='en'>could</span> ＋副詞 <span class='en'>really</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>stand out</span>＝「目立つ／差別化される」。混雑した市場で際立つ、の文脈。",
           "trap":"<span class='en'>break</span>（原形）も入り <span class='en'>break out</span> になるが、これは「勃発する・脱出する」で差別化の意味にならない。差別化は <span class='en'>stand out</span>。"},
        3:{"frame":"<span class='en'>Who are we ( ) this at</span>。be動詞 <span class='en'>are</span> の後 → <b>-ing 形</b>。",
           "logic":"<span class='en'>aim … at</span>＝「〜を（ターゲットに）狙う」。狙う客層を尋ねる。",
           "trap":"<span class='en'>going</span> も-ingだが <span class='en'>aim at</span> のように「対象を狙う」意味は表せない。"},
        4:{"frame":"<span class='en'>clear target ( )</span>。修飾語 <span class='en'>target</span> の後 → <b>名詞</b>。",
           "logic":"<span class='en'>target market</span>＝「ターゲット市場／狙う客層」。ビジネス頻出コロケ。",
           "trap":"<span class='en'>deal</span> も名詞だが <span class='en'>target deal</span> は非慣用。狙う客層は <span class='en'>target market</span>。"},
        5:{"frame":"<span class='en'>main selling ( )</span>。修飾語 <span class='en'>selling</span> の後 → <b>名詞</b>。",
           "logic":"<span class='en'>selling point</span>＝「セールスポイント／売り」。便利さが売り、の文脈。",
           "trap":"<span class='en'>deal</span> は <span class='en'>selling deal</span> で非慣用。売りは <span class='en'>selling point</span>。"},
        6:{"frame":"<span class='en'>add ( ) fast</span>。動詞 <span class='en'>add</span> と副詞 <span class='en'>fast</span> の間 → 句動詞の<b>不変化詞（副詞）</b>。",
           "logic":"<span class='en'>add up</span>＝「（費用などが）積み重なる／かさむ」。コストが増える心配。",
           "trap":"名詞ではなく副詞の枠。<span class='en'>add up</span> で「かさむ」。"},
        7:{"frame":"<span class='en'>worth a ( )</span>。<span class='en'>worth a</span> ＋（ ）の会話定型 → <b>名詞</b>。",
           "logic":"<span class='en'>worth a shot</span>＝「やってみる価値がある」。提案を後押しする言い回し。",
           "trap":"<span class='en'>deal</span> は <span class='en'>worth a deal</span> で非慣用。「試す価値」は <span class='en'>worth a shot</span>（≒worth a try）。"},
      },
      "unused": "<b>deal</b>（名詞）と <b>break</b>（動詞）が残る。"
                "deal は空所4・5・7の名詞枠に形は合うが <span class='en'>target deal</span>／<span class='en'>selling deal</span>／<span class='en'>worth a deal</span> はいずれも非慣用で脱落する。"
                "break は空所2の原形枠に入り <span class='en'>break out</span> という句動詞にはなるが「差別化する」意味にならず（正は <span class='en'>stand out</span>）落ちる。",
      "trans": "Aya「レン、ブレスト進んでる？ 新商品プロジェクトのアイデアある？」／Ren「いくつかね。イチ押しは、混雑した市場でも際立てるサブスクボックス」／"
               "Aya「いいね。でも誰を狙うの？ 明確なターゲット市場が要るよ」／Ren「若手社会人かな。お金はあるけど時間がない。便利さが一番の売りになる」／"
               "Aya「コストは？ 生鮮品はすぐかさむよ」／Ren「確かに。でもまとめ買いして無駄をなくせば、試す価値はあると思う」",
      "vocab": [
        ("stand out","句動","目立つ、際立つ／差別化される"),
        ("aim at","句動","〜を狙う、対象とする"),
        ("target market","名/句","ターゲット市場、狙う客層"),
        ("selling point","名/句","セールスポイント、売り"),
        ("add up","句動","（費用などが）積み重なる、かさむ"),
        ("buy in bulk","句","まとめ買いする"),
        ("worth a shot","定型","やってみる価値がある"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "図書館でグループ学習の予定を調整する学生2人（Yuna と Sho）",
      "lines": [
        ("Yuna", "Sho, we still need to ( 8 ) up a time for the group project. Are you free this week?"),
        ("Sho", "Let me check. Thursday afternoon ( 9 ) for me ― anything after three."),
        ("Yuna", "Same here. We should book a study room in ( 10 ), though. They go quickly."),
        ("Sho", "Good ( 11 ). Actually, those rooms fill up fast, so I'll reserve one tonight."),
        ("Yuna", "Perfect. Let's ( 12 ) up the reading so nobody gets overloaded. I'll take chapters one to three."),
        ("Sho", "Sounds fair. I'll ( 13 ) care of the rest and put the slides together."),
      ],
      "bank": [("a","works"),("b","set"),("c","time"),("d","advance"),
               ("e","take"),("f","call"),("g","sort"),("h","split")],
      "answers": {8:"set",9:"works",10:"advance",11:"call",12:"split",13:"take"},
      "exp": {
        8:{"frame":"<span class='en'>need to ( ) up a time</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>set up a time</span>＝「（会う）時間を段取る／設定する」。日程を決める文脈。",
           "trap":"<span class='en'>sort</span>（原形）も枠には合うが <span class='en'>sort up</span> は非慣用（<span class='en'>sort out</span> ならある）。段取るは <span class='en'>set up</span>。"},
        9:{"frame":"<span class='en'>Thursday afternoon ( ) for me</span>。単数主語の後 → <b>三単現の動詞</b>。",
           "logic":"<span class='en'>work for me</span>＝「私は都合がいい」。日程調整の定番表現。",
           "trap":"名詞 <span class='en'>time</span> ではなく動詞の枠。「都合がいい」は <span class='en'>works for me</span>。"},
        10:{"frame":"<span class='en'>book a study room in ( )</span>。前置詞 <span class='en'>in</span> の後 → <b>名詞</b>。",
            "logic":"<span class='en'>in advance</span>＝「前もって／事前に」。早めに予約する、の文脈。",
            "trap":"<span class='en'>in time</span> も名詞句だが「間に合って」の意味で「事前に」ではない。事前は <span class='en'>in advance</span>。"},
        11:{"frame":"<span class='en'>Good ( ).</span> 単独の相づち。<span class='en'>Good</span> ＋<b>名詞</b>の会話定型。",
            "logic":"<span class='en'>Good call.</span>＝「いい判断だね」。相手の提案への同意。",
            "trap":"<span class='en'>Good time</span> は「楽しい時間」で同意の相づちにならない。判断への賛同は <span class='en'>Good call</span>。"},
        12:{"frame":"<span class='en'>Let's ( ) up the reading</span>。<span class='en'>Let's</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>split up</span>＝「分担する／分ける」。読む範囲を分ける。",
            "trap":"<span class='en'>sort</span>（原形）も形は合うが <span class='en'>sort up</span> は非慣用。分担は <span class='en'>split up</span>。"},
        13:{"frame":"<span class='en'>I'll ( ) care of the rest</span>。助動詞 <span class='en'>will</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>take care of</span>＝「〜を引き受ける／担当する」。残りは自分が担当、の文脈。",
            "trap":"残る動詞から確定できる。<span class='en'>take care of</span> を句で丸ごと覚える。"},
      },
      "unused": "<b>time</b>（名詞）と <b>sort</b>（動詞）が残る。"
                "time は空所10・11の名詞枠に入るが <span class='en'>in time</span>（間に合って）／<span class='en'>Good time</span>（楽しい時間）となり、文脈の「事前に・同意」を表せない。"
                "sort は空所8・12の原形枠に形は合うが <span class='en'>sort up</span> という句動詞が存在せず（<span class='en'>sort out</span> はある）脱落する。「使わない2語」を先に予想すれば残りが確定する。",
      "trans": "Yuna「ショウ、グループ課題で会う時間をまだ決めなきゃ。今週空いてる？」／Sho「確認するね。木曜午後なら都合いいよ、3時以降なら何でも」／"
               "Yuna「私も同じ。でも自習室は事前に予約しよう、すぐ埋まるから」／Sho「いい判断。実際あの部屋はすぐ埋まるから、今夜1つ予約しとくよ」／"
               "Yuna「完璧。読む範囲を分担しよう、誰も抱え込まないように。私は1〜3章やる」／Sho「フェアだね。残りは僕が引き受けて、スライドをまとめるよ」",
      "vocab": [
        ("set up a time","句","会う時間を段取る／設定する"),
        ("work for someone","句","〜にとって都合がいい"),
        ("in advance","句","前もって、事前に"),
        ("Good call.","定型","いい判断だね"),
        ("split up","句動","分担する、分ける"),
        ("take care of","句動","〜を引き受ける、担当する"),
        ("fill up","句動","いっぱいになる、埋まる"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>ビジネス語彙と句動詞・会話定型の品詞判定</b>。"
            "<span class='en'>to</span>／助動詞／<span class='en'>Let's</span> の後は原形、be動詞の後は-ing、"
            "前置詞や <span class='en'>worth a</span>／<span class='en'>Good</span> の後は名詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "使わない2語（deal・break／time・sort）を先に当てにいくと連鎖ミスが消える。"
            "<span class='en'>stand out</span>・<span class='en'>aim at</span>・<span class='en'>add up</span> などの句動詞と "
            "<span class='en'>target market</span>・<span class='en'>selling point</span> のコロケを固めるのが得点源。",
}
