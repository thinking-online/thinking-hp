# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 12。
会話1(空所1-7)＝学生起業・ビジネスコンテスト、会話2(空所8-13)＝カフェで注文・待ち合わせ。
語群には使わない2語が混じる。"""

SET = {
  "theme": "学生起業のアイデア相談 ＆ カフェで待ち合わせ",
  "scene": "大学の自習スペース／街角のカフェ",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "ビジネスコンテストの応募を相談する学生2人（Sho と Mei）",
      "lines": [
        ("Sho", "Mei, the application deadline for the business contest is ( 1 ) up. Have you got an idea yet?"),
        ("Mei", "Yeah. I want to ( 2 ) an app that helps students find part-time jobs near campus."),
        ("Sho", "That sounds useful. But how will you ( 3 ) the money to build a prototype?"),
        ("Mei", "That's the tough part. I might ( 4 ) for a small startup grant the university offers."),
        ("Sho", "Smart. Have you talked to any students to check the customer ( 5 )?"),
        ("Mei", "Not yet. I think I should ( 6 ) out a short survey first."),
        ("Sho", "Definitely. If you can show real demand, the judges will take you ( 7 )."),
      ],
      "bank": [("a","apply"),("b","highly"),("c","coming"),("d","needs"),
               ("e","collect"),("f","raise"),("g","seriously"),("h","carry"),("i","develop")],
      "answers": {1:"coming",2:"develop",3:"raise",4:"apply",5:"needs",6:"carry",7:"seriously"},
      "exp": {
        1:{"frame":"<span class='en'>is ( ) up</span>。be動詞の後なので<b>-ing 形</b>が枠に合う。bank中 -ing 形は <span class='en'>coming</span> のみ。",
           "logic":"<span class='en'>be coming up</span>＝「（締切・日程が）近づいている」。応募締切が迫る文脈。",
           "trap":"他の候補は原形・副詞・名詞で -ing 枠に入らない。<b>枠だけで確定</b>できる空所。"},
        2:{"frame":"<span class='en'>want to ( ) an app</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>develop an app</span>＝「アプリを開発する」。ものを作り上げる意の動詞。",
           "trap":"<span class='en'>collect</span> も原形だが <span class='en'>collect an app</span> は非文。開発の文脈は <span class='en'>develop</span>。"},
        3:{"frame":"<span class='en'>how will you ( ) the money</span>。助動詞 <span class='en'>will</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>raise money</span>＝「資金を集める」。試作品を作る資金調達の話。",
           "trap":"<span class='en'>collect the money</span> は「（貸した金などを）回収する」で、資金調達の意にならない。調達は <span class='en'>raise</span>。"},
        4:{"frame":"<span class='en'>might ( ) for a grant</span>。助動詞 <span class='en'>might</span> の後は<b>原形</b>、直後に <span class='en'>for</span>。",
           "logic":"<span class='en'>apply for</span>＝「〜に応募・申請する」。助成金に申請する文脈。",
           "trap":"<span class='en'>collect for</span> は非慣用。<span class='en'>apply for</span> を句で覚える。"},
        5:{"frame":"<span class='en'>the customer ( )</span>。冠詞＋<span class='en'>customer</span> に続くのは<b>名詞</b>（複合名詞）。",
           "logic":"<span class='en'>customer needs</span>＝「顧客のニーズ」。需要を確かめる文脈。",
           "trap":"動詞 <span class='en'>raise</span>/<span class='en'>collect</span> では名詞句を作れない。ここは<b>名詞</b> <span class='en'>needs</span>。"},
        6:{"frame":"<span class='en'>should ( ) out a survey</span>。<span class='en'>should</span> の後は<b>原形</b>＋ <span class='en'>out</span>。",
           "logic":"<span class='en'>carry out</span>＝「（調査などを）実施する」。まず調査をやる、の流れ。",
           "trap":"<span class='en'>collect out</span> は非慣用。調査を「実施する」の定型は <span class='en'>carry out</span>。"},
        7:{"frame":"<span class='en'>take you ( )</span>。動詞＋目的語の後は<b>副詞</b>。",
           "logic":"<span class='en'>take ~ seriously</span>＝「〜を真剣に受け止める」。審査員が本気で相手にする。",
           "trap":"<span class='en'>highly</span> も副詞だが <span class='en'>take you highly</span> は非慣用。高く評価は <span class='en'>think highly of</span>。真剣の意は <span class='en'>seriously</span>。"},
      },
      "unused": "<b>collect</b>（集める・動詞）と <b>highly</b>（副詞）が残る。"
                "collect は空所3や6に形は合うが、資金調達＝raise、調査実施＝carry out の定型に負ける。"
                "collect the money は「回収する」の意で文脈に合わない。highly は空所7で <span class='en'>take you highly</span> が非慣用となり脱落する。",
      "trans": "Sho「メイ、ビジネスコンテストの応募締切が近づいてるよ。もうアイデアは決まった？」／"
               "Mei「うん。キャンパス近くのバイトを学生が見つけられるアプリを作りたいの」／"
               "Sho「便利そうだね。でも試作品を作る資金はどうやって集めるの？」／"
               "Mei「そこが難しいところ。大学が出してる小口の起業助成金に応募しようかな」／"
               "Sho「賢いね。顧客のニーズを確かめるのに、誰か学生と話してみた？」／"
               "Mei「まだ。まずは短いアンケートを実施すべきだと思う」／"
               "Sho「絶対そうだよ。実需を示せれば、審査員も君を真剣に受け止めてくれる」",
      "vocab": [
        ("be coming up","句","（締切・日程が）近づいている"),
        ("develop","動","（アプリ・製品を）開発する"),
        ("raise money","句","資金を集める、資金調達する"),
        ("apply for","句動","〜に応募する／申請する"),
        ("customer needs","句","顧客のニーズ"),
        ("carry out","句動","（調査・計画を）実施する"),
        ("take ~ seriously","句","〜を真剣に受け止める"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "カフェで待ち合わせをした友人2人（friend A と B）",
      "lines": [
        ("A", "Sorry to ( 8 ) you waiting! My train was delayed for ages."),
        ("B", "No ( 9 ) at all. I grabbed us a table by the window."),
        ("A", "Perfect spot. Have you ( 10 ) yet?"),
        ("B", "Not yet, I was waiting for you. Shall we ( 11 ) a look at the menu?"),
        ("A", "Sure. I think I'll ( 12 ) for the iced coffee and a bagel."),
        ("B", "Good choice. And lunch is ( 13 ) me today — you paid last time, remember?"),
      ],
      "bank": [("a","on"),("b","make"),("c","keep"),("d","go"),
               ("e","problem"),("f","for"),("g","ordered"),("h","take")],
      "answers": {8:"keep",9:"problem",10:"ordered",11:"take",12:"go",13:"on"},
      "exp": {
        8:{"frame":"<span class='en'>Sorry to ( ) you waiting</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>keep ~ waiting</span>＝「〜を待たせる」。遅刻の詫びの定番。",
           "trap":"<span class='en'>make</span> だと <span class='en'>make you waiting</span> となり非文（make は <span class='en'>make you wait</span>）。待たせるは <span class='en'>keep ~ waiting</span>。"},
        9:{"frame":"<span class='en'>No ( ) at all</span>。<span class='en'>No</span> の後は<b>名詞</b>の会話定型。",
           "logic":"<span class='en'>No problem.</span>＝「問題ないよ／気にしないで」。詫びへの応答。",
           "trap":"bank中で名詞になり「気にしないで」の意になるのは <span class='en'>problem</span> のみ。"},
        10:{"frame":"<span class='en'>Have you ( ) yet?</span> <span class='en'>have</span> の後は<b>過去分詞</b>。",
            "logic":"<span class='en'>order</span>＝「注文する」。現在完了で「もう注文した？」。",
            "trap":"<span class='en'>make</span> の過去分詞 <span class='en'>made</span> は綴りが異なりbankに無い。カフェで注文の文脈は <span class='en'>ordered</span>。"},
        11:{"frame":"<span class='en'>Shall we ( ) a look</span>。<span class='en'>Shall we</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>take a look</span>＝「ちょっと見る」。メニューを見よう、の誘い。",
            "trap":"<span class='en'>make a look</span> は非慣用。「見る」は <span class='en'>take</span>（または have）<span class='en'>a look</span>。"},
        12:{"frame":"<span class='en'>I'll ( ) for the iced coffee</span>。<span class='en'>will</span> の後は<b>原形</b>＋ <span class='en'>for</span>。",
            "logic":"<span class='en'>go for</span>＝「〜を選ぶ／〜にする」。注文を決める言い方。",
            "trap":"<span class='en'>make for</span> は「〜へ向かう」で「選ぶ」の意にならない。注文を決めるは <span class='en'>go for</span>。"},
        13:{"frame":"<span class='en'>lunch is ( ) me</span>。be動詞の後、支払いの主体を示す<b>前置詞</b>。",
            "logic":"<span class='en'>It's on me.</span>＝「私のおごり」。今回は自分が払う、の意。",
            "trap":"<span class='en'>for</span> を入れた <span class='en'>it's for me</span> は「私のためのもの」で「おごる」の意にならない。おごりは <span class='en'>on me</span>。"},
      },
      "unused": "<b>make</b>（動詞）と <b>for</b>（前置詞）が残る。"
                "make は空所8/11に形は合うが、<span class='en'>make you waiting</span>・<span class='en'>make a look</span> はいずれも非慣用。"
                "for は空所13で <span class='en'>it's for me</span> が「おごり」の意にならず脱落する。使わない2語を先に見抜けば残りが決まる。",
      "trans": "A「待たせてごめん！電車がすごく遅れちゃって」／"
               "B「全然問題ないよ。窓際に席を取っておいたから」／"
               "A「いい場所だね。もう注文した？」／"
               "B「まだだよ、あなたを待ってたの。メニュー見ようか？」／"
               "A「うん。私はアイスコーヒーとベーグルにしようかな」／"
               "B「いいね。それに今日のランチは私のおごり——前回あなたが払ってくれたでしょ？」",
      "vocab": [
        ("keep ~ waiting","句","〜を待たせる"),
        ("No problem.","定型","問題ないよ／気にしないで"),
        ("order","動","注文する"),
        ("take a look","句","ちょっと見る"),
        ("go for","句動","〜を選ぶ／〜にする"),
        ("It's on me.","定型","私のおごりだよ"),
        ("grab a table","句","席を確保する"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞・会話定型の品詞判定</b>。<span class='en'>to</span>／助動詞／<span class='en'>Shall we</span> の後は原形、"
            "be動詞の後は形容詞・-ing、冠詞＋名詞に続くのは名詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "資金調達＝raise・調査実施＝carry out・おごり＝on me のように<b>コロケーションを丸ごと</b>覚え、"
            "使わない2語（collect・highly／make・for）を先に当てにいくと連鎖ミスが消える。",
}
