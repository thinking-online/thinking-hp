# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 07。
会話2本×空所13。Set A(空所1-7) と Set B(空所8-13)。語群には使わない2語が混じる。"""

SET = {
  "theme": "インターン最終面接の報告 ＆ ゼミ論文の進捗相談",
  "scene": "大学のラウンジ／研究室（指導教員の部屋）",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "インターンの最終面接を終えた学生2人（Sota と Hina）",
      "lines": [
        ("Hina", "Sota, you look worn out. How did the final interview ( 1 )?"),
        ("Sota", "Pretty well, actually. I managed to ( 2 ) most of their questions calmly."),
        ("Hina", "That's great. Were you nervous when they put you ( 3 ) the spot?"),
        ("Sota", "A little. But I'd ( 4 ) up on the company beforehand, so I felt prepared."),
        ("Hina", "Smart. Did you get to ask them anything yourself?"),
        ("Sota", "Yes. When they asked if I had questions, I ( 5 ) up a few about their overseas projects."),
        ("Hina", "Nice. Interviewers love it when you show real ( 6 )."),
        ("Sota", "I hope so. Now I just have to ( 7 ) for the results."),
        ("Hina", "Fingers crossed! I'm sure you stood out."),
      ],
      "bank": [("a","brought"),("b","into"),("c","wait"),("d","handle"),
               ("e","raised"),("f","on"),("g","interest"),("h","go"),("i","brushed")],
      "answers": {1:"go",2:"handle",3:"on",4:"brushed",5:"brought",6:"interest",7:"wait"},
      "exp": {
        1:{"frame":"疑問文 <span class='en'>How did the interview ( )?</span>。<span class='en'>did</span> があるので空所は<b>動詞（原形）</b>。",
           "logic":"「面接はどう<b>進んだ</b>のか」を尋ねる文脈。<span class='en'>How did it go?</span>＝「どうだった？」の会話定番。",
           "trap":"<span class='en'>raised</span> は過去形なので <span class='en'>did</span> の後には置けない。原形で「進む」の意を持つのは <span class='en'>go</span>。"},
        2:{"frame":"<span class='en'>manage to ( )</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>handle questions</span>＝「質問をうまくさばく」。落ち着いて対処した、という流れ。",
           "trap":"<span class='en'>raised</span>（過去形）は <span class='en'>to</span> の後に不可。「質問に対処する」のコロケーションは <span class='en'>handle</span>。"},
        3:{"frame":"<span class='en'>put you ( ) the spot</span>。名詞句 <span class='en'>the spot</span> の前なので<b>前置詞</b>。",
           "logic":"<span class='en'>put ... on the spot</span>＝「その場で返答を迫る／困らせる」。緊張した場面。",
           "trap":"<span class='en'>into</span> は <span class='en'>put ... into the spot</span> という慣用がなく脱落。定型は <span class='en'>on the spot</span>。"},
        4:{"frame":"<span class='en'>I'd ( ) up on …</span>。<span class='en'>had</span> の後なので<b>過去分詞</b>。",
           "logic":"<span class='en'>brush up on</span>＝「（知識を）復習する、磨き直す」。事前に会社を調べておいた文脈。",
           "trap":"原形 <span class='en'>go</span> や名詞 <span class='en'>interest</span> は形が合わない。過去分詞で <span class='en'>up on</span> を取るのは <span class='en'>brushed</span>。"},
        5:{"frame":"<span class='en'>I ( ) up a few …</span>。主語 <span class='en'>I</span> に対する<b>過去形動詞</b>。",
           "logic":"<span class='en'>bring up</span>＝「（質問・話題を）持ち出す」。逆質問をした場面。過去形 <span class='en'>brought</span>。",
           "trap":"<span class='en'>raised</span> を入れると <span class='en'>raised up</span> となり非慣用。<span class='en'>up</span> を伴って自然なのは <span class='en'>brought</span>。"},
        6:{"frame":"<span class='en'>show real ( )</span>。形容詞 <span class='en'>real</span> に修飾されるので<b>名詞</b>。",
           "logic":"<span class='en'>show interest</span>＝「関心を示す」。面接官が好む態度、という評価。",
           "trap":"動詞群は名詞枠に入らない。<span class='en'>real</span>（本当の）が付く名詞は <span class='en'>interest</span> のみ。"},
        7:{"frame":"<span class='en'>have to ( ) for …</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>wait for the results</span>＝「結果を待つ」。合否待ちの定番表現。",
           "trap":"残る原形動詞から確定できる。<span class='en'>go for</span> や <span class='en'>handle for</span> では意味が繋がらない。"},
      },
      "unused": "<b>raised</b>（raise の過去形・動詞）と <b>into</b>（前置詞）が残る。"
                "raised は空所5に形は近いが <span class='en'>raised up</span> が非慣用で脱落する。"
                "into は空所3で <span class='en'>put ... into the spot</span> が成立せず落ちる。使わない2語を先に外すと残りが決まる。",
      "trans": "Hina「ソウタ、疲れてるね。最終面接はどうだった？」／Sota「実はけっこう良かったよ。質問のほとんどを落ち着いてさばけたんだ」／"
               "Hina「すごい。その場で返答を迫られたとき緊張しなかった？」／Sota「少しね。でも事前に会社のことを調べておいたから、準備万端だった」／"
               "Hina「賢いね。自分から何か質問できた？」／Sota「うん。質問はあるかと聞かれたとき、海外プロジェクトについていくつか持ち出したよ」／"
               "Hina「いいね。面接官は本当の関心を見せてくれると嬉しいものだよ」／Sota「だといいな。あとは結果を待つだけだ」／"
               "Hina「幸運を祈ってる！ きっと目立ってたよ」",
      "vocab": [
        ("go","動","（物事が）進む・運ぶ。<span class='en'>How did it go?</span>＝どうだった？"),
        ("handle","動","（質問・問題を）うまくさばく、対処する"),
        ("put ... on the spot","句","〜をその場で困らせる、返答を迫る"),
        ("brush up on","句動","（知識を）復習する、磨き直す"),
        ("bring up","句動","（話題・質問を）持ち出す"),
        ("show interest","句","関心を示す"),
        ("wait for","句","〜を待つ（結果待ちの定番）"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "ゼミ論文の進捗を指導教員に相談する学生（Yui と 先生）",
      "lines": [
        ("Yui", "Excuse me, Professor. Could I ( 8 ) over the progress of my seminar paper with you?"),
        ("先生", "Of course, Yui. Have a seat. How is it coming ( 9 )?"),
        ("Yui", "The first two chapters are done, but I'm ( 10 ) behind on the literature review."),
        ("先生", "I see. Have you narrowed ( 11 ) your topic yet?"),
        ("Yui", "Almost. Actually, would it be possible to ( 12 ) the deadline by a week?"),
        ("先生", "Given your progress, I can ( 13 ) an extension. Just send me a revised outline."),
      ],
      "bank": [("a","down"),("b","extend"),("c","forward"),("d","talk"),
               ("e","grant"),("f","along"),("g","make"),("h","falling")],
      "answers": {8:"talk",9:"along",10:"falling",11:"down",12:"extend",13:"grant"},
      "exp": {
        8:{"frame":"<span class='en'>Could I ( ) over …</span>。助動詞 <span class='en'>Could</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>talk over</span>＝「〜をじっくり相談する」。<span class='en'>with you</span> と結んで「先生と話し合う」。",
           "trap":"<span class='en'>make over</span> は「改造する」で相談の意にならず脱落。相談は <span class='en'>talk over</span>。"},
        9:{"frame":"<span class='en'>How is it coming ( )?</span>。<span class='en'>come</span> に続く<b>副詞</b>。",
           "logic":"<span class='en'>come along</span>＝「はかどる、進展する」。論文の進み具合を問う定番。",
           "trap":"<span class='en'>forward</span> では <span class='en'>come forward</span>＝「名乗り出る」となり意味が別。進捗は <span class='en'>along</span>。"},
        10:{"frame":"<span class='en'>I'm ( ) behind …</span>。be動詞の後なので<b>-ing 形</b>。",
            "logic":"<span class='en'>fall behind</span>＝「（作業が）遅れる」。文献レビューが遅れている、という状況。",
            "trap":"原形・過去形は be動詞の後に置けない。<span class='en'>behind</span> と結ぶ進行形は <span class='en'>falling</span>。"},
        11:{"frame":"<span class='en'>narrowed ( ) your topic</span>。動詞に続く<b>副詞</b>。",
            "logic":"<span class='en'>narrow down</span>＝「（テーマ・範囲を）絞り込む」。研究テーマを限定したか尋ねる。",
            "trap":"<span class='en'>forward</span> では <span class='en'>narrow forward</span> という句がない。絞り込みは <span class='en'>down</span>。"},
        12:{"frame":"<span class='en'>possible to ( ) the deadline</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>extend the deadline</span>＝「締切を延長する」。<span class='en'>by a week</span>＝「1週間」。",
            "trap":"<span class='en'>make the deadline</span> は「間に合う」の意で <span class='en'>by a week</span> と噛み合わない。延長は <span class='en'>extend</span>。"},
        13:{"frame":"<span class='en'>I can ( ) an extension</span>。助動詞 <span class='en'>can</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>grant an extension</span>＝「延長を認める」。教員が許可を出す文脈。",
            "trap":"<span class='en'>make an extension</span> は非慣用。「認める・与える」の意で <span class='en'>extension</span> を取るのは <span class='en'>grant</span>。"},
      },
      "unused": "<b>make</b>（動詞）と <b>forward</b>（副詞）が残る。"
                "make は空所13で <span class='en'>make an extension</span> が非慣用、空所12でも <span class='en'>make the deadline</span> が「延長」と噛み合わず落ちる。"
                "forward は <span class='en'>come forward</span>／<span class='en'>narrow forward</span> が文脈に合わず脱落する。",
      "trans": "Yui「失礼します、先生。ゼミ論文の進み具合について相談してもいいですか？」／先生「もちろん、ユイ。座って。どんな感じ？」／"
               "Yui「最初の2章は終わったんですが、文献レビューが遅れていて」／先生「なるほど。テーマはもう絞り込めた？」／"
               "Yui「ほぼ。実は、締切を1週間延ばしていただくことは可能でしょうか？」／"
               "先生「君の進み具合なら延長を認めるよ。修正した章立て（アウトライン）を送っておいて」",
      "vocab": [
        ("talk over","句動","〜についてじっくり相談する"),
        ("come along","句動","（物事が）はかどる、進展する"),
        ("fall behind","句動","（予定・作業が）遅れる"),
        ("narrow down","句動","（範囲・テーマを）絞り込む"),
        ("extend","動","（期限を）延長する"),
        ("grant an extension","句","延長を認める"),
        ("literature review","名","文献レビュー、先行研究のまとめ"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞と会話定型の品詞判定</b>。<span class='en'>to</span>／助動詞／命令文の後は原形、"
            "be動詞の後は形容詞・-ing、名詞句の前は前置詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "使わない2語（raised・into／make・forward）を先に当てにいくと、面接・論文相談のビジネス／アカデミック定型でも連鎖ミスが消える。",
}
