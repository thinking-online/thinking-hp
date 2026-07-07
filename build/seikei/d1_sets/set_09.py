# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 09。
Set A(空所1-7)＝合同企業説明会の回り方相談／Set B(空所8-13)＝レストラン予約変更の電話。
語群には使わない2語が混じる。"""

SET = {
  "theme": "合同企業説明会の回り方 ＆ レストラン予約の変更",
  "scene": "就活イベント会場／レストランへの電話",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "合同企業説明会でブースの回り方を相談する就活生2人（Daiki と Saki）",
      "lines": [
        ("Daiki", "Saki, this job fair is bigger than I expected. Before we split up, let's ( 1 ) out how to get around."),
        ("Saki", "Good idea. First, let's ( 2 ) our priorities. Which industries do you want most?"),
        ("Daiki", "The trading companies, mainly. But their info sessions always ( 3 ) up fast."),
        ("Saki", "Then let's divide the booths. You take those, and I'll ( 4 ) out the IT firms."),
        ("Daiki", "Sounds efficient. By the way, did you ( 5 ) up for the two o'clock seminar?"),
        ("Saki", "Not yet. I want to do more industry ( 6 ) before I decide where to apply."),
        ("Daiki", "Makes sense. Oh, I heard some companies let you ( 7 ) in your entry sheet right at the booth."),
      ],
      "bank": [("a","check"),("b","research"),("c","book"),("d","look"),
               ("e","hand"),("f","set"),("g","study"),("h","figure"),("i","sign")],
      "answers": {1:"figure",2:"set",3:"book",4:"check",5:"sign",6:"research",7:"hand"},
      "exp": {
        1:{"frame":"<span class='en'>let's ( 1 ) out how to get around</span>。<span class='en'>let's</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>figure out</span>＝「（やり方を）考え出す・把握する」。広い会場の回り方を考える文脈。",
           "trap":"<span class='en'>check out</span>（下見する）は空所4で必要。<span class='en'>look out</span> は「気をつけろ」で回り方を考える意味にならない。"},
        2:{"frame":"<span class='en'>( 2 ) our priorities</span>。目的語 <span class='en'>priorities</span> を取る<b>動詞原形</b>。",
           "logic":"<span class='en'>set priorities</span>＝「優先順位を決める」。どの業界を優先するか決める文脈。",
           "trap":"「優先順位を決める」は <span class='en'>set</span> と結ぶ定番コロケ。<span class='en'>check our priorities</span> は非慣用。"},
        3:{"frame":"<span class='en'>info sessions always ( 3 ) up fast</span>。頻度副詞 <span class='en'>always</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>book up</span>＝「予約で埋まる・満席になる」。人気の説明会はすぐ枠が埋まる。",
           "trap":"<span class='en'>sign up</span>（申し込む）は<b>人</b>が主語。ここは説明会（枠）が主語なので <span class='en'>book up</span>。"},
        4:{"frame":"<span class='en'>I'll ( 4 ) out the IT firms</span>。<span class='en'>I'll</span> の後は<b>原形</b>＋ <span class='en'>out</span>。",
           "logic":"<span class='en'>check out</span>＝「（実際に見て）調べる・下見する」。IT企業のブースを見て回る。",
           "trap":"<span class='en'>look out</span> は「注意する」で、目的語を調べる意味にならない。<span class='en'>look</span> はダミー。"},
        5:{"frame":"<span class='en'>did you ( 5 ) up for the seminar</span>。<span class='en'>did</span> があるので<b>原形</b>。",
           "logic":"<span class='en'>sign up for</span>＝「〜に申し込む・登録する」。セミナーへの参加登録の話。",
           "trap":"<span class='en'>book up for</span> は非慣用。「（イベントに）申し込む」は <span class='en'>sign up for</span>。"},
        6:{"frame":"<span class='en'>do more industry ( 6 )</span>。<span class='en'>do more</span> の後、冠詞なしで置ける<b>不可算名詞</b>。",
           "logic":"<span class='en'>industry research</span>／<span class='en'>do research</span>＝「業界研究をする」。応募先を決める前の準備。",
           "trap":"<span class='en'>study</span> は可算寄りで <span class='en'>do study</span> は非文。「調査・研究をする」は <span class='en'>do research</span>。<span class='en'>study</span> はダミー。"},
        7:{"frame":"<span class='en'>let you ( 7 ) in your entry sheet</span>。使役 <span class='en'>let ＋ 人 ＋ 原形</span>。",
           "logic":"<span class='en'>hand in</span>＝「提出する」。ブースでエントリーシートを出せる、の意味。",
           "trap":"残る動詞から確定。<span class='en'>hand in</span>＝submit。<span class='en'>check in</span> では「受付する」で提出の意味にならない。"},
      },
      "unused": "<b>look</b>（動詞）と <b>study</b>（名詞/動詞）が残る。"
                "look は空所4に形は合うが <span class='en'>look out</span>＝「注意する」で「下見する」にならない。"
                "study は空所6に品詞は近いが <span class='en'>do study</span> が非文で <span class='en'>research</span> に負ける。"
                "「使わない2語」を先に予想できれば残りが確定する。",
      "trans": "Daiki「サキ、この合同説明会、思ったより大きいね。手分けする前に、どう回るか考えよう」／"
               "Saki「いいね。まず優先順位を決めよう。どの業界が一番いい？」／"
               "Daiki「主に商社かな。でもあそこの説明会っていつもすぐ埋まるんだよね」／"
               "Saki「じゃあブースを分担しよう。あなたはそっち、私はIT企業を見てくる」／"
               "Daiki「効率いいね。ところで、2時のセミナーは申し込んだ？」／"
               "Saki「まだ。どこに応募するか決める前に、もう少し業界研究したくて」／"
               "Daiki「なるほど。そういえば、ブースでその場でエントリーシートを出せる会社もあるらしいよ」",
      "vocab": [
        ("figure out","句動","（やり方を）考え出す・理解する"),
        ("set priorities","句","優先順位を決める"),
        ("book up","句動","予約で埋まる・満席になる"),
        ("check out","句動","（見て）調べる・下見する"),
        ("sign up for","句動","〜に申し込む・登録する"),
        ("industry research","句","業界研究"),
        ("hand in","句動","提出する"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "レストランの予約を電話で変更する客と店員（Customer と Staff）",
      "lines": [
        ("Staff", "Thank you for calling Bella Cucina. How can I ( 8 ) you today?"),
        ("Customer", "Hi. I need to ( 9 ) a few changes to my booking for tomorrow night."),
        ("Staff", "Certainly. Could you tell me the name on the reservation?"),
        ("Customer", "Of course. It's ( 10 ) the name Tanaka."),
        ("Customer", "First, could you ( 11 ) the time from seven to eight?"),
        ("Customer", "And please ( 12 ) two more people to the booking — we'll be six now."),
        ("Staff", "Got it. So, let me ( 13 ) everything: a table for six at eight tomorrow evening."),
      ],
      "bank": [("a","on"),("b","help"),("c","confirm"),("d","make"),
               ("e","under"),("f","do"),("g","move"),("h","add")],
      "answers": {8:"help",9:"make",10:"under",11:"move",12:"add",13:"confirm"},
      "exp": {
        8:{"frame":"<span class='en'>How can I ( 8 ) you?</span> 助動詞 <span class='en'>can</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>How can I help you?</span>＝「ご用件を伺います」。電話・接客の第一声の定型。",
           "trap":"接客の第一声はこの定型。<span class='en'>make you</span> 等では意味をなさない。"},
        9:{"frame":"<span class='en'>need to ( 9 ) a few changes</span>。<span class='en'>to</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>make changes</span>＝「変更を加える」。予約内容を変えたい、の意味。",
           "trap":"<span class='en'>do changes</span> は非慣用。「変更する」は <span class='en'>make changes</span>。<span class='en'>do</span> はダミー。"},
        10:{"frame":"<span class='en'>It's ( 10 ) the name Tanaka</span>。名詞句 <span class='en'>the name</span> の前は<b>前置詞</b>。",
            "logic":"<span class='en'>under the name</span>＝「〜の名前で（予約されて）」。予約名義を答える定型。",
            "trap":"<span class='en'>on the name</span> は不自然。「〜名義で」は <span class='en'>under the name</span>。<span class='en'>on</span> はダミー。"},
        11:{"frame":"<span class='en'>could you ( 11 ) the time from seven to eight</span>。<span class='en'>could you</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>move</span>＝「（時刻を）ずらす・変更する」。<span class='en'>from A to B</span> で時間帯を移す。",
            "trap":"<span class='en'>add the time</span> は意味不明。時刻の移動は <span class='en'>move</span>。"},
        12:{"frame":"<span class='en'>please ( 12 ) two more people to the booking</span>。命令文の頭は<b>原形</b>。",
            "logic":"<span class='en'>add ... to ...</span>＝「〜に…を加える」。人数を4名から6名へ増やす。",
            "trap":"<span class='en'>move ... to</span> では「人を移動させる」意味になり増員にならない。「加える」は <span class='en'>add</span>。"},
        13:{"frame":"<span class='en'>let me ( 13 ) everything</span>。<span class='en'>let me</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>confirm</span>＝「確認する」。最後に予約内容を復唱して確かめる場面。",
            "trap":"残る動詞から確定。復唱して確かめるのは <span class='en'>confirm</span>。<span class='en'>help everything</span> は非文。"},
      },
      "unused": "<b>do</b>（動詞）と <b>on</b>（前置詞）が残る。"
                "do は空所9で <span class='en'>do changes</span> となり非慣用（正しくは <span class='en'>make changes</span>）。"
                "on は空所10で <span class='en'>on the name</span> となり不自然（正しくは <span class='en'>under the name</span>）。"
                "コロケーションで2語を先に外せば残りが決まる。",
      "trans": "Staff「お電話ありがとうございます、ベラ・クチーナです。本日はどのようなご用件でしょうか」／"
               "Customer「もしもし。明日の夜の予約を少し変更したいのですが」／"
               "Staff「かしこまりました。ご予約のお名前を伺えますか」／"
               "Customer「はい、田中の名前で取っています」／"
               "Customer「まず、時間を7時から8時にずらせますか」／"
               "Customer「それと、予約に2名追加してください。6名になります」／"
               "Staff「承知しました。では確認いたします。明日の夜8時に6名様のお席ですね」",
      "vocab": [
        ("How can I help you?","定型","ご用件を伺います（電話・接客）"),
        ("make changes","句","変更する・変更を加える"),
        ("under the name","句","〜の名前で（予約されて）"),
        ("move","動","（予定・時刻を）ずらす・変更する"),
        ("add ... to ...","句","〜に…を加える"),
        ("confirm","動","確認する"),
        ("booking","名","予約（＝reservation）"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>コロケーションと句動詞の品詞判定</b>。<span class='en'>let's</span>／<span class='en'>to</span>／助動詞／命令文の後は原形、"
            "名詞句の前は前置詞、というふうに<b>枠で候補を絞って</b>から意味で決める。"
            "<span class='en'>set priorities・make changes・add … to・under the name</span> のような定型結合と、"
            "<span class='en'>figure out・check out・sign up・book up・hand in</span> の句動詞を丸ごと覚え、"
            "使わない2語（look・study／do・on）を先に当てにいくと連鎖ミスが消える。",
}
