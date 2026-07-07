# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 05。
Set A(空所1-7) と Set B(空所8-13)。語群には使わない2語が混じる。"""

SET = {
  "theme": "イベントの予算会議 ＆ ジム通いの継続",
  "scene": "学生団体の実行委員会室／大学近くのカフェ",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "学園祭の予算について打ち合わせる実行委員2人（Taku と Nao）",
      "lines": [
        ("Taku", "Nao, before the meeting starts, can we go ( 1 ) the festival budget one more time?"),
        ("Nao", "Sure. The good news is that this year we should ( 2 ) even, since income and costs are almost equal."),
        ("Taku", "That's a relief. Last year the committee ended up in the ( 3 ) by about fifty thousand yen."),
        ("Nao", "I remember. This time the sponsor's donation really made a ( 4 )."),
        ("Taku", "Speaking of the sponsor, did they agree to ( 5 ) the cost of the main stage?"),
        ("Nao", "Yes, they'll pay for half of it. Still, the budget is pretty ( 6 ), so we can't afford any waste."),
        ("Taku", "Agreed. If we keep an eye on the small expenses, everything should ( 7 ) up nicely."),
      ],
      "bank": [("a","tight"),("b","spend"),("c","over"),("d","red"),
               ("e","loose"),("f","break"),("g","difference"),("h","cover"),("i","add")],
      "answers": {1:"over",2:"break",3:"red",4:"difference",5:"cover",6:"tight",7:"add"},
      "exp": {
        1:{"frame":"<span class='en'>can we go ( ) the budget</span>。動詞 <span class='en'>go</span> の後で目的語 <span class='en'>the budget</span> を取る枠なので<b>前置詞・副詞</b>。",
           "logic":"<span class='en'>go over</span>＝「〜を見直す／検討する」。「予算をもう一度<b>確認</b>しよう」の文脈。",
           "trap":"動詞 <span class='en'>spend</span>/<span class='en'>cover</span> は <span class='en'>go</span> の直後には並ばない。ここは <span class='en'>go over</span> の副詞枠。"},
        2:{"frame":"<span class='en'>should ( ) even</span>。助動詞 <span class='en'>should</span> の後は<b>動詞の原形</b>。",
           "logic":"<span class='en'>break even</span>＝「収支トントンになる」。収入と費用がほぼ等しいという説明と一致。",
           "trap":"<span class='en'>spend even</span>/<span class='en'>cover even</span> は非慣用。<span class='en'>break even</span> を句で覚える。"},
        3:{"frame":"<span class='en'>in the ( )</span>。前置詞 <span class='en'>in the</span> の後なので<b>名詞</b>が入る。",
           "logic":"<span class='en'>in the red</span>＝「赤字で」。前年は5万円<b>赤字</b>だった、という否定的な文脈。",
           "trap":"色を使った定型。黒字は <span class='en'>in the black</span>。ここは損失なので <span class='en'>red</span>。"},
        4:{"frame":"<span class='en'>made a ( )</span>。冠詞 <span class='en'>a</span> の後は<b>名詞</b>。",
           "logic":"<span class='en'>make a difference</span>＝「効果を生む／状況を変える」。寄付が収支を好転させた。",
           "trap":"<span class='en'>a</span> の後に来られる名詞は語群で <span class='en'>difference</span> のみ。<span class='en'>red</span> はすでに空所3で使う。"},
        5:{"frame":"<span class='en'>agree to ( ) the cost</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>cover the cost</span>＝「費用を負担する」。スポンサーがステージ代を持つか、の話。",
           "trap":"<span class='en'>spend the cost</span> は誤コロケ。金を <span class='en'>spend</span> はするが、費用は <span class='en'>cover</span> する。"},
        6:{"frame":"<span class='en'>the budget is pretty ( )</span>。be動詞＋副詞 <span class='en'>pretty</span> の後は<b>形容詞</b>。",
           "logic":"<span class='en'>a tight budget</span>＝「余裕のない予算」。無駄が許されないという後半と噛み合う。",
           "trap":"<span class='en'>loose</span>（緩い）も形容詞だが「無駄が許されない」文脈と逆。予算がきつい＝ <span class='en'>tight</span>。"},
        7:{"frame":"<span class='en'>should ( ) up</span>。助動詞の後の<b>原形</b>＋副詞 <span class='en'>up</span>。",
           "logic":"<span class='en'>add up</span>＝「計算が合う／つじつまが合う」。小さな出費を抑えれば数字は合う、の意。",
           "trap":"残る動詞から確定できる。<span class='en'>spend up</span> は文脈に合わず、<span class='en'>add up</span> が収支の定型。"},
      },
      "unused": "<b>spend</b>（動詞）と <b>loose</b>（形容詞・緩い）が残る。"
                "spend は空所5に形は合うが <span class='en'>spend the cost</span> という誤コロケになり脱落する。"
                "loose は空所6に形の上では入るが「無駄が許されない」という文脈と意味が逆になる。",
      "trans": "Taku「ナオ、会議が始まる前に、学園祭の予算をもう一度確認しておかない？」／Nao「いいよ。いい知らせは、収入と費用がほぼ同じだから、今年は収支トントンになりそうってこと」／"
               "Taku「よかった。去年は委員会が5万円くらい赤字で終わったからね」／Nao「覚えてる。今回はスポンサーの寄付がすごく効いたよ」／"
               "Taku「スポンサーといえば、メインステージの費用を負担してくれることになった？」／Nao「うん、半分は出してくれる。それでも予算はかなりきついから、無駄は許されないね」／"
               "Taku「同感。細かい出費に気をつければ、数字はきれいに合うはずだよ」",
      "vocab": [
        ("go over","句動","〜を見直す、検討する"),
        ("break even","句","収支トントンになる"),
        ("in the red","句","赤字で（黒字は in the black）"),
        ("make a difference","句","効果を生む、状況を変える"),
        ("cover the cost","句","費用を負担する"),
        ("tight","形","（予算などが）余裕のない、きつい"),
        ("add up","句動","計算が合う、つじつまが合う"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "ジム通いと運動習慣について話す友人2人（Emi と Ken）",
      "lines": [
        ("Emi", "Ken, I heard you finally joined a gym. How's it ( 8 ) along?"),
        ("Ken", "Better than I thought. I work out three times a week and feel much more ( 9 ) already."),
        ("Emi", "Nice. I always ( 10 ) up after a few days. I'm the classic three-day type."),
        ("Ken", "The trick is to ( 11 ) a realistic goal instead of pushing too hard at the start."),
        ("Emi", "That's probably my mistake. I aim too high and burn out."),
        ("Ken", "Exactly. Just ( 12 ) with it for a month, and it turns into a habit."),
        ("Emi", "Good point. I really want to get back into ( 13 ) before the summer."),
      ],
      "bank": [("a","set"),("b","lazy"),("c","coming"),("d","give"),
               ("e","keep"),("f","energetic"),("g","stick"),("h","shape")],
      "answers": {8:"coming",9:"energetic",10:"give",11:"set",12:"stick",13:"shape"},
      "exp": {
        8:{"frame":"<span class='en'>How's it ( ) along?</span> <span class='en'>is</span> の後なので<b>-ing 形</b>。",
           "logic":"<span class='en'>come along</span>＝「（物事が）進む、はかどる」。「ジム通いの調子はどう？」の定番表現。",
           "trap":"<span class='en'>give</span>/<span class='en'>set</span> の -ing はここにないし、<span class='en'>keeping along</span> は非慣用。進捗を問う定型は <span class='en'>come along</span>。"},
        9:{"frame":"<span class='en'>feel much more ( )</span>。<span class='en'>more</span> の後は<b>形容詞</b>。",
           "logic":"<span class='en'>energetic</span>＝「活力のある」。運動して「元気になった」というプラス評価。",
           "trap":"<span class='en'>lazy</span>（怠惰な）も形容詞だが、運動を続けた結果としては意味が逆。"},
        10:{"frame":"<span class='en'>I always ( ) up</span>。主語＋副詞 <span class='en'>always</span> の後は<b>動詞（現在形）</b>。",
            "logic":"<span class='en'>give up</span>＝「あきらめる、やめる」。「三日坊主タイプ」という自己紹介と一致。",
            "trap":"<span class='en'>keep up</span>（維持する）も形は合うが、直後の「三日坊主」と正反対。挫折の意味は <span class='en'>give up</span>。"},
        11:{"frame":"<span class='en'>The trick is to ( ) a goal</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>set a goal</span>＝「目標を立てる」。現実的な目標設定がコツ、という助言。",
            "trap":"目標は <span class='en'>set</span> するのが定型。<span class='en'>keep a goal</span> は「目標を持ち続ける」で文脈と微妙にずれる。"},
        12:{"frame":"命令文 <span class='en'>Just ( ) with it</span>。文頭は<b>動詞原形</b>。",
            "logic":"<span class='en'>stick with</span>＝「〜を続ける、やり通す」。1か月続ければ習慣になる、の意。",
            "trap":"<span class='en'>keep with it</span> は非慣用（<span class='en'>keep at it</span> なら可）。<span class='en'>stick with</span> を句で覚える。"},
        13:{"frame":"<span class='en'>get back into ( )</span>。前置詞 <span class='en'>into</span> の後は<b>名詞</b>。",
            "logic":"<span class='en'>get into shape</span>＝「体を鍛える、健康な体になる」。夏までに体を作りたい、の意。",
            "trap":"残る名詞から確定できる。<span class='en'>into lazy</span> は品詞が合わず、体調の定型は <span class='en'>get into shape</span>。"},
      },
      "unused": "<b>keep</b>（動詞）と <b>lazy</b>（形容詞・怠惰な）が残る。"
                "keep は空所10や12に形は合うが、<span class='en'>keep up</span> は「維持する」で三日坊主の文脈と逆、<span class='en'>keep with it</span> は非慣用で脱落する。"
                "lazy は空所9に形は合うが「運動して元気になった」という意味と逆になる。",
      "trans": "Emi「ケン、ついにジムに入ったんだって？ 調子はどう？」／Ken「思ったより順調だよ。週3回運動してて、もうずいぶん元気になった気がする」／"
               "Emi「いいね。私はいつも数日でやめちゃう。典型的な三日坊主なの」／Ken「コツは、最初から無理をせず現実的な目標を立てることだよ」／"
               "Emi「たぶんそれが私の失敗ね。目標を高くしすぎて燃え尽きちゃう」／Ken「まさに。とにかく1か月続けてみて、そうすれば習慣になるから」／"
               "Emi「なるほど。夏までにちゃんと体を作りたいな」",
      "vocab": [
        ("come along","句動","（物事が）進む、はかどる"),
        ("work out","句動","運動する、トレーニングする"),
        ("energetic","形","活力のある、元気な"),
        ("give up","句動","あきらめる、やめる"),
        ("set a goal","句","目標を立てる"),
        ("stick with","句動","〜を続ける、やり通す"),
        ("get into shape","句","体を鍛える、健康な体になる"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>ビジネス・健康の定型コロケーションと品詞判定</b>。<span class='en'>to</span>／助動詞／命令文の後は原形、"
            "<span class='en'>in the</span>／<span class='en'>into</span>／冠詞の後は名詞、be動詞・<span class='en'>more</span> の後は形容詞、と<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "使わない2語（spend・loose／keep・lazy）を先に当てにいくと、連鎖ミスが消える。",
}
