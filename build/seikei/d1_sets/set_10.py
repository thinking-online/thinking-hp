# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 10。
Set A(空所1-7)＝卒論テーマの相談／Set B(空所8-13)＝ノートPC故障のサポート電話。"""

SET = {
  "theme": "卒論テーマの相談 ＆ ノートPC故障のサポート電話",
  "scene": "大学の研究室／自宅からのカスタマーサポート電話",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "卒業論文のテーマを相談する学生 Yuto と Mori 教授",
      "lines": [
        ("Yuto", "Professor Mori, do you have a minute? I'd like to ( 1 ) your brain about my graduation thesis."),
        ("Mori", "Of course. Have you decided what to ( 2 ) on yet?"),
        ("Yuto", "Not really. My topic still feels too broad, so I need to ( 3 ) it down."),
        ("Mori", "That's normal at this stage. What ( 4 ) your interest in this area in the first place?"),
        ("Yuto", "I want to look at how small firms adopt AI, but I'm not sure there's enough ( 5 ) research on it."),
        ("Mori", "There's more than you think. First, you should ( 6 ) out a thorough literature review."),
        ("Yuto", "Right. And after that, maybe I could ( 7 ) a survey to gather original data."),
        ("Mori", "Exactly. Do that, and your thesis will stand on solid ground."),
      ],
      "bank": [("a","focus"),("b","former"),("c","pick"),("d","carry"),
               ("e","sparked"),("f","conduct"),("g","prior"),("h","bring"),("i","narrow")],
      "answers": {1:"pick",2:"focus",3:"narrow",4:"sparked",5:"prior",6:"carry",7:"conduct"},
      "exp": {
        1:{"frame":"<span class='en'>I'd like to ( ) your brain</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>pick someone's brain</span>＝「〜の知恵を借りる／意見を聞く」。相談を切り出す定番表現。",
           "trap":"<span class='en'>bring</span> も原形だが <span class='en'>bring your brain</span> は非慣用。知恵を借りるは <span class='en'>pick</span>。"},
        2:{"frame":"<span class='en'>what to ( ) on</span>。<span class='en'>to</span> の後は<b>動詞原形</b>で後ろに <span class='en'>on</span>。",
           "logic":"<span class='en'>focus on</span>＝「〜に焦点を絞る」。何をテーマの中心に据えるかを問う文脈。",
           "trap":"直後に <span class='en'>on</span> を取り「絞る」意味になる動詞は <span class='en'>focus</span> のみ。"},
        3:{"frame":"<span class='en'>need to ( ) it down</span>。<span class='en'>to</span> の後は<b>原形</b>、目的語 <span class='en'>it</span> を挟む句動詞。",
           "logic":"<span class='en'>narrow down</span>＝「（範囲を）絞り込む」。「too broad（広すぎる）」を受けた自然な流れ。",
           "trap":"<span class='en'>bring it down</span>（下げる・倒す）では研究テーマの話に合わない。範囲は <span class='en'>narrow down</span>。"},
        4:{"frame":"<span class='en'>What ( ) your interest</span>。主語 <span class='en'>What</span> に対する<b>過去形動詞</b>。",
           "logic":"<span class='en'>spark one's interest</span>＝「（人の）興味をかき立てる」。きっかけを尋ねる文脈。",
           "trap":"<span class='en'>brought</span> なら形は合うが、ここに残るのは原形 <span class='en'>bring</span>。「興味に火をつける」定番は <span class='en'>spark</span>。"},
        5:{"frame":"<span class='en'>enough ( ) research</span>。名詞 <span class='en'>research</span> を修飾する<b>形容詞</b>。",
           "logic":"<span class='en'>prior research</span>＝「先行研究」。アカデミックの定型コロケーション。",
           "trap":"<span class='en'>former</span>（前者の・かつての）は形容詞だが <span class='en'>former research</span> は非慣用。先行研究は <span class='en'>prior</span>。"},
        6:{"frame":"<span class='en'>you should ( ) out</span>。助動詞 <span class='en'>should</span> の後は<b>原形</b>＋ <span class='en'>out</span>。",
           "logic":"<span class='en'>carry out</span>＝「（調査などを）実施する」。<span class='en'>literature review</span> と結ぶ標準表現。",
           "trap":"<span class='en'>bring out</span>（引き出す・出版する）は <span class='en'>literature review</span> と噛み合わない。実施は <span class='en'>carry out</span>。"},
        7:{"frame":"<span class='en'>I could ( ) a survey</span>。助動詞 <span class='en'>could</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>conduct a survey</span>＝「アンケート調査を行う」。<span class='en'>original data</span> 収集の文脈に合致。",
           "trap":"残る動詞から確定できる。<span class='en'>survey</span> と結ぶ堅い動詞は <span class='en'>conduct</span>。"},
      },
      "unused": "<b>former</b>（形容詞）と <b>bring</b>（動詞原形）が残る。"
                "former は空所5に形は合うが <span class='en'>former research</span> は非慣用で、先行研究は <span class='en'>prior research</span>。"
                "bring はどの空所でも <span class='en'>pick / narrow / carry out</span> のコロケーションに勝てず脱落する。",
      "trans": "Yuto「モリ先生、少しお時間ありますか。卒論について知恵をお借りしたくて」／Mori「もちろん。何に焦点を絞るかは決まった？」／"
               "Yuto「まだです。テーマがまだ広すぎるので、絞り込む必要があって」／Mori「この段階では普通のことだよ。そもそも何がこの分野への興味をかき立てたの？」／"
               "Yuto「小さな企業がどうAIを導入するかを見たいんですが、先行研究が十分にあるか不安で」／Mori「思ったよりあるよ。まずは徹底した文献レビューを実施すべきだね」／"
               "Yuto「なるほど。その後で、独自データを集めるためにアンケート調査を行うのもありですね」／Mori「その通り。そうすれば、論文はしっかりした土台に立つよ」",
      "vocab": [
        ("pick someone's brain","句","〜の知恵を借りる、意見を聞く"),
        ("focus on","句動","〜に焦点を絞る"),
        ("narrow down","句動","（範囲を）絞り込む"),
        ("spark one's interest","句","（人の）興味をかき立てる"),
        ("prior research","句","先行研究"),
        ("carry out","句動","（調査などを）実施する"),
        ("conduct a survey","句","アンケート調査を行う"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "ノートPCの故障をサポートに電話する客 Emma と担当 Agent",
      "lines": [
        ("Agent", "Thank you for calling TechCare. What seems to be the problem?"),
        ("Emma", "My new laptop keeps ( 8 ) down on its own, even with a full battery."),
        ("Agent", "That's not normal. Is the device still ( 9 ) warranty?"),
        ("Emma", "I think so. I bought it about six months ago."),
        ("Agent", "Good. Then the repair should be ( 10 ) at no cost to you."),
        ("Emma", "That's a relief. But I'm a bit worried about my files."),
        ("Agent", "Before you send it in, please ( 11 ) up your data, just in case."),
        ("Emma", "Okay. And how do I get it to you?"),
        ("Agent", "Just ( 12 ) it in to our service center, and we'll take a look."),
        ("Emma", "Got it. And if it can't be fixed, would I get a ( 13 )?"),
        ("Agent", "Yes. If the fault is confirmed, we'll send you a brand-new unit."),
      ],
      "bank": [("a","send"),("b","under"),("c","receipt"),("d","shutting"),
               ("e","back"),("f","beyond"),("g","covered"),("h","replacement")],
      "answers": {8:"shutting",9:"under",10:"covered",11:"back",12:"send",13:"replacement"},
      "exp": {
        8:{"frame":"<span class='en'>keeps ( ) down</span>。<span class='en'>keep</span> の後は<b>-ing 形</b>＋ <span class='en'>down</span>。",
           "logic":"<span class='en'>shut down</span>＝「電源が切れる／停止する」。<span class='en'>keep -ing</span> で「勝手に切れ続ける」症状。",
           "trap":"<span class='en'>send</span> は原形で <span class='en'>keep</span> の後には来ない。電源が落ちるは <span class='en'>shut down</span>。"},
        9:{"frame":"<span class='en'>still ( ) warranty</span>。名詞 <span class='en'>warranty</span> の前は<b>前置詞</b>。",
           "logic":"<span class='en'>under warranty</span>＝「保証期間内で」。まだ保証が有効かを確認する定型。",
           "trap":"<span class='en'>beyond</span> も前置詞だが <span class='en'>beyond warranty</span> は「保証期間外」で意味が逆。<span class='en'>still</span> と合うのは <span class='en'>under</span>。"},
        10:{"frame":"<span class='en'>should be ( )</span>。be動詞の後は<b>過去分詞（形容詞的）</b>。",
            "logic":"<span class='en'>be covered</span>＝「（費用が）補償される」。<span class='en'>at no cost</span> と結ぶ自然な流れ。",
            "trap":"<span class='en'>send</span>/<span class='en'>back</span> を入れても <span class='en'>be covered at no cost</span> の意味にならない。補償は <span class='en'>covered</span>。"},
        11:{"frame":"<span class='en'>please ( ) up your data</span>。命令の <span class='en'>please</span> の後は<b>原形</b>＋ <span class='en'>up</span>。",
            "logic":"<span class='en'>back up</span>＝「（データを）バックアップする」。修理に出す前の定番の注意。",
            "trap":"<span class='en'>send up</span> は <span class='en'>data</span> と結ばない。データ保全は <span class='en'>back up</span>。"},
        12:{"frame":"命令文 <span class='en'>Just ( ) it in</span>。文頭は<b>動詞原形</b>、目的語を挟む句動詞。",
            "logic":"<span class='en'>send in</span>＝「（修理などに）送る」。<span class='en'>service center</span> へ送付する文脈。",
            "trap":"<span class='en'>back it in</span> は非慣用。「送り込む」は <span class='en'>send … in</span>。"},
        13:{"frame":"<span class='en'>get a ( )</span>。冠詞 <span class='en'>a</span> の後は<b>名詞</b>。",
            "logic":"<span class='en'>replacement</span>＝「交換品／代替品」。修理不能なら代替品をもらえるか、の文脈。",
            "trap":"<span class='en'>receipt</span>（領収書）も名詞だが「直せない場合に受け取る物」ではない。代替品は <span class='en'>replacement</span>。"},
      },
      "unused": "<b>receipt</b>（名詞）と <b>beyond</b>（前置詞）が残る。"
                "receipt は空所13に形は合うが「修理不能時に受け取る物」は交換品＝<span class='en'>replacement</span> で、領収書は文脈外。"
                "beyond は空所9に形は合うが <span class='en'>beyond warranty</span> は「保証期間外」で意味が逆になり脱落する。",
      "trans": "Agent「TechCareサポートです。どのような問題でしょうか」／Emma「新しいノートPCが、バッテリー満タンでも勝手に電源が切れ続けるんです」／"
               "Agent「それは正常ではありませんね。その機器はまだ保証期間内ですか」／Emma「たぶん。半年ほど前に買いました」／"
               "Agent「よかった。では修理はお客様負担なしで補償されるはずです」／Emma「安心しました。でもファイルが少し心配で」／"
               "Agent「送っていただく前に、念のためデータをバックアップしてください」／Emma「わかりました。どうやってお渡しすれば？」／"
               "Agent「サービスセンターに送っていただくだけです。こちらで確認します」／Emma「了解です。もし直せなければ、交換品はもらえますか」／"
               "Agent「はい。不具合が確認されれば、新品をお送りします」",
      "vocab": [
        ("shut down","句動","（電源が）切れる、停止する"),
        ("under warranty","句","保証期間内で"),
        ("be covered","句","（費用が）補償される"),
        ("back up","句動","（データを）バックアップする"),
        ("send in","句動","（修理などに）送る、送付する"),
        ("replacement","名","交換品、代替品"),
        ("fault","名","故障、不具合"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞と定型コロケーションの品詞判定</b>。<span class='en'>to</span>／助動詞／命令文の後は原形、"
            "<span class='en'>keep</span> の後は -ing、be動詞の後は過去分詞・形容詞、名詞の前は形容詞・前置詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "使わない2語（former・bring／receipt・beyond）を先に当てにいくと、連鎖ミスが消える。",
}
