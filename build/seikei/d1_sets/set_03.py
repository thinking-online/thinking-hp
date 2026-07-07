# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 03（会話2本×空所13）。
Set A(空所1-7) と Set B(空所8-13)。語群には使わない2語が混じる。"""

SET = {
  "theme": "短期海外語学研修の相談 ＆ カフェのシフト交代",
  "scene": "大学の国際交流課前／カフェのバックヤード",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "短期語学研修について経験者の友人に相談する学生（Mio と Sota）",
      "lines": [
        ("Mio", "Sota, do you have a sec? I've been ( 1 ) about applying for the summer language program in Vancouver."),
        ("Sota", "Oh nice. I did that exact one two years ago. What do you want to know?"),
        ("Mio", "First, is it really ( 2 ) the money? The tuition looks pretty high to me."),
        ("Sota", "Honestly, yes. And here's the best part: the credits ( 3 ) toward your degree."),
        ("Mio", "Wait, really? That would ( 4 ) a huge difference for my graduation plan."),
        ("Sota", "It does. But you should ( 5 ) up soon; the spots fill up fast every year."),
        ("Mio", "Got it. There's no ( 6 ) in putting it off, then."),
        ("Sota", "Exactly. And it's a great chance to ( 7 ) up on your French before you fly out."),
      ],
      "bank": [("a","sign"),("b","worth"),("c","afford"),("d","count"),
               ("e","point"),("f","wondering"),("g","make"),("h","reason"),("i","brush")],
      "answers": {1:"wondering",2:"worth",3:"count",4:"make",5:"sign",6:"point",7:"brush"},
      "exp": {
        1:{"frame":"<span class='en'>I've been ( ) about …</span>。<span class='en'>have been</span> の後なので<b>-ing 形</b>が枠に合う。",
           "logic":"<span class='en'>wonder about</span>＝「〜について思案する／気になっている」。現在完了進行で「ずっと考えていた」。",
           "trap":"<span class='en'>afford</span>（動詞）は <span class='en'>-ing</span> 形ではないうえ <span class='en'>afford about</span> という形も存在しない。枠でまず脱落する。"},
        2:{"frame":"<span class='en'>is it really ( ) the money</span>。be動詞の後で名詞句 <span class='en'>the money</span> を従える<b>形容詞</b>。",
           "logic":"<span class='en'>be worth the money</span>＝「金額に見合う価値がある」。<span class='en'>worth</span> は直後に名詞を取る特殊な形容詞。",
           "trap":"<span class='en'>reason</span>（名詞）は <span class='en'>is it reason the money</span> と非文になる。<span class='en'>worth ＋名詞</span> の型を覚える。"},
        3:{"frame":"主語 <span class='en'>the credits</span>（複数）＋（ ）＋ <span class='en'>toward</span>。<b>現在形の動詞</b>で複数主語に対応。",
           "logic":"<span class='en'>count toward</span>＝「〜に算入される／〜の一部として数えられる」。単位が学位に「カウントされる」。",
           "trap":"<span class='en'>make toward</span> は非慣用。<span class='en'>toward</span> と結ぶ動詞は <span class='en'>count</span>。三単現の <span class='en'>-s</span> が付かないのは主語が複数だから。"},
        4:{"frame":"<span class='en'>That would ( ) a huge difference</span>。助動詞 <span class='en'>would</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>make a difference</span>＝「大きく影響する／効いてくる」。単位が認められれば計画が変わる、の文脈。",
           "trap":"<span class='en'>count a difference</span> とは言わない。<span class='en'>difference</span> と結ぶ定型動詞は <span class='en'>make</span>。"},
        5:{"frame":"<span class='en'>you should ( ) up soon</span>。助動詞 <span class='en'>should</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>sign up</span>＝「（申し込みの）登録をする」。定員が埋まる前に「申し込むべき」。",
           "trap":"直後の <span class='en'>the spots fill up fast</span> の <span class='en'>fill</span> に引きずられない。主語が <span class='en'>you</span> なら申込動作の <span class='en'>sign up</span>。"},
        6:{"frame":"<span class='en'>There's no ( ) in putting …</span>。<span class='en'>no ＋（ ）＋ in doing</span> の枠は<b>名詞</b>。",
           "logic":"<span class='en'>There's no point in doing</span>＝「〜しても意味がない／無駄だ」。先延ばしする理由がない、の文脈。",
           "trap":"<span class='en'>reason</span> も名詞だが <span class='en'>no reason in doing</span> は非慣用（正しくは <span class='en'>no reason to do</span>）。<span class='en'>in ＋動名詞</span> を取れるのは <span class='en'>point</span>。"},
        7:{"frame":"<span class='en'>a great chance to ( ) up on …</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>brush up on</span>＝「（語学などを）学び直す・磨き直す」。渡航前にフランス語を復習する好機。",
           "trap":"残る動詞から確定できる。<span class='en'>sign up on</span> は <span class='en'>on</span> を取らず意味も合わない。<span class='en'>brush up on ＋技能</span> のコロケーション。"},
      },
      "unused": "<b>afford</b>（〜する余裕がある・動詞）と <b>reason</b>（理由・名詞）が残る。"
                "afford は空所4や5の動詞枠に形は入るが <span class='en'>afford a difference</span>／<span class='en'>afford up</span> とコロケーションが成立しない。"
                "reason は空所6で <span class='en'>no reason in doing</span> という非慣用形になり脱落する（正用は <span class='en'>no reason to do</span>）。",
      "trans": "Mio「ソウタ、ちょっといい？ バンクーバーの夏の語学プログラムに申し込もうか、ずっと考えてて」／"
               "Sota「いいね。俺、2年前にまさにそれ行ったよ。何が知りたい？」／"
               "Mio「まず、本当に費用に見合う？ 授業料がけっこう高そうで」／"
               "Sota「正直、見合うよ。しかも一番いいのは、単位が学位にちゃんとカウントされること」／"
               "Mio「え、ほんと？ それなら卒業計画に大きく効いてくるな」／"
               "Sota「そうなんだ。でも早めに申し込んだほうがいい。毎年すぐ定員が埋まるから」／"
               "Mio「了解。じゃあ先延ばしする意味はないね」／"
               "Sota「まさに。それに渡航前にフランス語をやり直すいい機会だよ」",
      "vocab": [
        ("wonder about","句動","〜について思案する、気になる"),
        ("worth","形","（直後に名詞を取り）〜の価値がある"),
        ("count toward","句動","〜に算入される、一部として数えられる"),
        ("make a difference","句","大きく影響する、効いてくる"),
        ("sign up","句動","（申込・登録を）する"),
        ("no point in doing","句","〜しても意味がない、無駄だ"),
        ("brush up on","句動","（語学・技能を）学び直す、磨き直す"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "カフェのバイトで急にシフト交代を頼む同僚2人（Haru と Leo）",
      "lines": [
        ("Haru", "Leo, could you do me a ( 8 )? I need someone to cover my Saturday shift."),
        ("Leo", "This Saturday? Let me ( 9 ) my schedule real quick."),
        ("Haru", "Something came ( 10 ) at home; my cousin's wedding got moved to that day."),
        ("Leo", "Ah, congrats to them. Yeah, I can ( 11 ) in for you, no problem."),
        ("Haru", "You're a lifesaver. I'll ( 12 ) you one, I promise."),
        ("Leo", "No ( 13 ). Just take one of my Tuesday shifts sometime and we're even."),
      ],
      "bank": [("a","owe"),("b","hand"),("c","up"),("d","favor"),
               ("e","trade"),("f","check"),("g","worries"),("h","fill")],
      "answers": {8:"favor",9:"check",10:"up",11:"fill",12:"owe",13:"worries"},
      "exp": {
        8:{"frame":"<span class='en'>do me a ( )</span>。冠詞 <span class='en'>a</span> の後なので<b>名詞</b>。",
           "logic":"<span class='en'>do someone a favor</span>＝「〜に頼み事を聞いてもらう／親切にする」。依頼を切り出す会話定型。",
           "trap":"<span class='en'>hand</span> も名詞だが <span class='en'>do me a hand</span> は非慣用。手助けの意なら <span class='en'>give me a hand</span> と動詞が変わる。<span class='en'>do me a favor</span> を丸ごと覚える。"},
        9:{"frame":"<span class='en'>Let me ( ) my schedule</span>。<span class='en'>Let me ＋</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>check my schedule</span>＝「予定を確認する」。交代できるか確かめる自然な応答。",
           "trap":"<span class='en'>trade my schedule</span> は不自然（交換するのは shift であって schedule ではない）。予定を「確認」する動詞は <span class='en'>check</span>。"},
        10:{"frame":"<span class='en'>Something came ( )</span>。動詞 <span class='en'>came</span> と結ぶ<b>副詞（不変化詞）</b>。",
            "logic":"<span class='en'>Something came up</span>＝「（急に）用事ができた」。予定変更の理由を切り出す定番表現。",
            "trap":"ここは句動詞の不変化詞の枠。<span class='en'>came</span> と結んで「用事ができた」となるのは <span class='en'>up</span> のみ。"},
        11:{"frame":"<span class='en'>I can ( ) in for you</span>。助動詞 <span class='en'>can</span> の後は<b>原形</b>＋ <span class='en'>in</span>。",
            "logic":"<span class='en'>fill in for someone</span>＝「〜の代わりを務める」。シフトを代わる、の中心表現。",
            "trap":"<span class='en'>trade in for</span> は「下取りに出す」で意味が全く違う。人の代役は <span class='en'>fill in for</span>。"},
        12:{"frame":"<span class='en'>I'll ( ) you one</span>。<span class='en'>will</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>I'll owe you one.</span>＝「借りができたね／恩に着るよ」。お礼として使う会話定型。",
            "trap":"<span class='en'>trade you one</span> では「1つ交換する」となり感謝の意にならない。恩義を表すのは <span class='en'>owe you one</span>。"},
        13:{"frame":"<span class='en'>No ( ).</span> 単独で応じる会話定型。<b>名詞</b>が入る。",
            "logic":"<span class='en'>No worries.</span>＝「気にしないで／どういたしまして」。お礼への軽い返し。",
            "trap":"残る名詞から確定できる。<span class='en'>No hand</span> という応答は存在しない。快諾の定型は <span class='en'>No worries</span>。"},
      },
      "unused": "<b>hand</b>（手・名詞）と <b>trade</b>（交換する・動詞）が残る。"
                "hand は空所8や13の名詞枠に形は合うが <span class='en'>do me a hand</span>／<span class='en'>No hand</span> という言い方は存在しない。"
                "trade は空所9・11・12の動詞枠に形は入るが、schedule・in for・you one のいずれとも意味・コロケーションが噛み合わず脱落する。",
      "trans": "Haru「レオ、ちょっとお願いしていい？ 土曜のシフトを誰かに代わってほしくて」／"
               "Leo「今週の土曜？ ちょっと予定を確認させて」／"
               "Haru「実家で急に用事ができちゃって。いとこの結婚式がその日に動いたんだ」／"
               "Leo「へえ、おめでとう。うん、代わりに入れるよ、問題ない」／"
               "Haru「助かる、命の恩人だよ。この借りは必ず返すから」／"
               "Leo「気にしないで。いつか俺の火曜のシフトを1回代わってくれたら、それでチャラ」",
      "vocab": [
        ("do someone a favor","句","〜に頼み事を聞いてもらう、親切にする"),
        ("check one's schedule","句","予定を確認する"),
        ("come up","句動","（急に）用事・問題が持ち上がる"),
        ("fill in for","句動","〜の代わりを務める、代役をする"),
        ("owe someone one","句","〜に借りができる、恩に着る"),
        ("No worries.","定型","気にしないで／どういたしまして"),
        ("cover a shift","句","シフトを代わって入る"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞・会話定型のコロケーション判定</b>。<span class='en'>to</span>／助動詞／<span class='en'>Let me</span> の後は原形、"
            "be動詞や冠詞 <span class='en'>a</span> の後は形容詞・名詞、と<b>枠で候補を半分に落として</b>から、"
            "<span class='en'>count toward</span>・<span class='en'>fill in for</span> のように結びつく前置詞・名詞で最終決定する。"
            "使わない2語（afford・reason／hand・trade）を先に見抜くと、連鎖ミスが防げる。",
}
