# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 11。
Set A(空所1-7)＝会社訪問後のお礼メール／Set B(空所8-13)＝フリマアプリ売買。
語群には使わない2語が混じる。"""

SET = {
  "theme": "会社訪問後のお礼メール ＆ フリマアプリで売買",
  "scene": "大学の就活ラウンジ／自宅のスマホ画面",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "会社訪問後のお礼メールを先輩に相談する就活生（Yuma と 先輩 Rio）",
      "lines": [
        ("Yuma", "Rio, I finally ( 1 ) up the courage to visit that company yesterday."),
        ("Rio", "Nice work! So, did you send a thank-you email afterward?"),
        ("Yuma", "Not yet. I wasn't sure if it would come ( 2 ) as too formal."),
        ("Rio", "A short one is perfectly fine. Just ( 3 ) them for their time."),
        ("Yuma", "Right. Should I ( 4 ) it to the person who showed me around?"),
        ("Rio", "Yes, definitely. And keep the ( 5 ) polite but natural."),
        ("Yuma", "Got it. What about the ( 6 )? 'Best regards' sounds too stiff to me."),
        ("Rio", "It's actually standard. Don't ( 7 ) it too much."),
      ],
      "bank": [("a","thank"),("b","along"),("c","closing"),("d","worked"),
               ("e","across"),("f","greeting"),("g","tone"),("h","overthink"),("i","address")],
      "answers": {1:"worked",2:"across",3:"thank",4:"address",5:"tone",6:"closing",7:"overthink"},
      "exp": {
        1:{"frame":"副詞 <span class='en'>finally</span> の後、主語 <span class='en'>I</span> に対する<b>動詞（過去形）</b>。<span class='en'>( ) up the courage</span> の形。",
           "logic":"<span class='en'>work up the courage</span>＝「勇気を奮い起こす」。過去形 <span class='en'>worked</span>。",
           "trap":"<span class='en'>courage</span> と結びつく句動詞は <span class='en'>work up</span> のみ。<span class='en'>thank</span>/<span class='en'>address</span> では <span class='en'>up the courage</span> と繋がらない。"},
        2:{"frame":"<span class='en'>would come ( ) as too formal</span>。動詞 <span class='en'>come</span> の後の<b>副詞（不変化詞）</b>。",
           "logic":"<span class='en'>come across as</span>＝「（人・物が）〜という印象を与える」。「堅苦しく<b>見える</b>のでは」。",
           "trap":"ダミー <span class='en'>along</span> を入れた <span class='en'>come along as</span> は非慣用。印象を表す定型は <span class='en'>come across as</span>。"},
        3:{"frame":"命令文 <span class='en'>Just ( ) them for their time</span>。文頭は<b>動詞原形</b>。",
           "logic":"<span class='en'>thank … for one's time</span>＝「時間を割いてくれたことに礼を言う」。お礼メールの定番コロケ。",
           "trap":"<span class='en'>address</span> は宛先を示す動詞で <span class='en'>for their time</span> と噛み合わない。お礼の動詞は <span class='en'>thank</span>。"},
        4:{"frame":"<span class='en'>Should I ( ) it to the person …</span>。助動詞 <span class='en'>should</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>address … to ～</span>＝「（手紙・メールを）〜宛てにする」。「案内してくれた人<b>宛て</b>にすべき？」",
           "trap":"<span class='en'>thank it to</span> は非文（<span class='en'>thank</span> は人を目的語に取る）。<span class='en'>to ～</span> で宛先を示すのは <span class='en'>address</span>。"},
        5:{"frame":"<span class='en'>keep the ( ) polite but natural</span>。冠詞 <span class='en'>the</span> の後は<b>名詞</b>。",
           "logic":"<span class='en'>tone</span>＝「（文章の）調子・語調」。「語調は丁寧かつ自然に保て」。",
           "trap":"ダミー <span class='en'>greeting</span> も名詞だが「冒頭の挨拶」で、文章全体の調子を指す語ではない。"},
        6:{"frame":"<span class='en'>What about the ( )?</span> 冠詞 <span class='en'>the</span> の後の<b>名詞</b>。",
           "logic":"<span class='en'>closing</span>＝「結びの言葉」。<span class='en'>Best regards</span> はメールの<b>締め</b>の表現。",
           "trap":"<span class='en'>greeting</span> は<b>冒頭</b>の挨拶で、<span class='en'>Best regards</span>（末尾）とは逆。締めは <span class='en'>closing</span>。"},
        7:{"frame":"否定命令 <span class='en'>Don't ( ) it too much</span>。<span class='en'>Don't</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>overthink</span>＝「考えすぎる」。「（メールの文面を）考えすぎるな」。",
           "trap":"残る動詞から確定。<span class='en'>thank</span>/<span class='en'>address</span> では <span class='en'>it too much</span> と意味が通らない。"},
      },
      "unused": "<b>along</b>（不変化詞）と <b>greeting</b>（名詞）が残る。"
                "along は空所2で <span class='en'>come along as</span> となり非慣用。"
                "greeting は空所6に形は入るが「冒頭の挨拶」で、締めの <span class='en'>Best regards</span> を指す語にはならない。"
                "使わない2語を先に見抜くと、残りの空所が確定する。",
      "trans": "Yuma「リオ、昨日やっと勇気を出してあの会社を訪問してきたよ」／Rio「よくやったね！ で、後でお礼メールは送った？」／"
               "Yuma「まだなんだ。堅苦しすぎる印象にならないか不安で」／Rio「短いので十分だよ。時間を割いてくれたお礼を言えばいい」／"
               "Yuma「なるほど。案内してくれた人宛てに送るべき？」／Rio「うん、ぜひ。語調は丁寧だけど自然にね」／"
               "Yuma「了解。締めはどうしよう？ 『Best regards』は自分には堅すぎる気がして」／Rio「あれは実は定番だよ。考えすぎないで」",
      "vocab": [
        ("work up the courage","句","勇気を奮い起こす"),
        ("come across as","句動","（人・物が）〜という印象を与える"),
        ("thank … for one's time","句","時間を割いてくれたことに礼を言う"),
        ("address … to ～","動","（手紙・メールを）〜宛てにする"),
        ("tone","名","（文章の）調子、語調"),
        ("closing","名","（手紙・メールの）結びの言葉"),
        ("overthink","動","考えすぎる"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "フリマアプリで不用品を売買する友人2人（Nana と Kota）",
      "lines": [
        ("Nana", "Kota, I'm trying to ( 8 ) some old textbooks on that flea market app."),
        ("Kota", "Good idea. Did anyone ( 9 ) an offer yet?"),
        ("Nana", "One person asked me to ( 10 ) the price by 500 yen."),
        ("Kota", "That's normal. If it's not too low, you should just ( 11 ) it."),
        ("Nana", "True. After that, I just ( 12 ) it out and wait for a rating, right?"),
        ("Kota", "Exactly. Most buyers ( 13 ) a good review if the item arrives quickly."),
      ],
      "bank": [("a","accept"),("b","give"),("c","list"),("d","make"),
               ("e","lower"),("f","ship"),("g","raise"),("h","leave")],
      "answers": {8:"list",9:"make",10:"lower",11:"accept",12:"ship",13:"leave"},
      "exp": {
        8:{"frame":"<span class='en'>trying to ( ) some old textbooks</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>list</span>＝「（フリマ・オークションに）出品する」。「古い教科書を出品しようとしている」。",
           "trap":"<span class='en'>list</span>＝出品する、という語義がポイント。<span class='en'>make</span>/<span class='en'>give</span> では商品を売りに出す意味にならない。"},
        9:{"frame":"<span class='en'>Did anyone ( ) an offer</span>。<span class='en'>Did</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>make an offer</span>＝「（購入の）申し出をする」。定番コロケ。",
           "trap":"ダミー <span class='en'>give</span> の <span class='en'>give an offer</span> は非慣用。オファーは <span class='en'>make</span> と結ぶ。"},
        10:{"frame":"<span class='en'>asked me to ( ) the price</span>。<span class='en'>to</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>lower the price</span>＝「値下げする」。買い手が「500円<b>下げて</b>」と頼んだ。",
            "trap":"ダミー <span class='en'>raise</span> は「値上げ」で意味が逆。文脈は値下げ交渉なので <span class='en'>lower</span>。"},
        11:{"frame":"<span class='en'>should just ( ) it</span>。助動詞 <span class='en'>should</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>accept</span>＝「（申し出を）受け入れる」。「安すぎなければ受けてしまえ」。",
            "trap":"<span class='en'>raise it</span>/<span class='en'>give it</span> では申し出を承諾する意味にならない。承諾は <span class='en'>accept</span>。"},
        12:{"frame":"<span class='en'>I just ( ) it out and wait</span>。主語 <span class='en'>I</span> の<b>現在形（原形同形）</b>＋ <span class='en'>out</span>。",
            "logic":"<span class='en'>ship out</span>＝「発送する」。「発送して評価を待つ」流れ。",
            "trap":"<span class='en'>make out</span>/<span class='en'>give out</span> では「商品を送る」意味にならない。発送は <span class='en'>ship</span>。"},
        13:{"frame":"<span class='en'>Most buyers ( ) a good review</span>。主語の後の<b>現在形動詞</b>。",
            "logic":"<span class='en'>leave a review</span>＝「レビュー（評価）を残す」。アプリ売買の定番コロケ。",
            "trap":"ダミー <span class='en'>give a review</span> は「批評する」寄りで、購入評価には <span class='en'>leave</span> が自然。残る語から確定。"},
      },
      "unused": "<b>give</b> と <b>raise</b>（ともに動詞）が残る。"
                "give は空所9で <span class='en'>give an offer</span> となり非慣用（正しくは <span class='en'>make an offer</span>）。"
                "raise は空所10に形は合うが「値上げ」で、値下げ交渉の文脈と逆になる。"
                "全空所が動詞なので、<b>コロケーション</b>で候補を落とすのが鍵。",
      "trans": "Nana「コウタ、あのフリマアプリに古い教科書を何冊か出品しようとしてるんだ」／Kota「いいね。もう誰か申し出てきた？」／"
               "Nana「一人、500円値下げしてくれって頼んできた」／Kota「よくあることだよ。安すぎないなら、受けちゃえばいい」／"
               "Nana「そうだね。その後は発送して評価を待つだけ、だよね？」／Kota「その通り。商品が早く届けば、たいていの買い手はいい評価を残してくれるよ」",
      "vocab": [
        ("list","動","（フリマ・オークションに）出品する"),
        ("make an offer","句","（購入の）申し出をする"),
        ("lower the price","句","値下げする"),
        ("accept an offer","句","申し出を受け入れる"),
        ("ship out","句動","発送する"),
        ("leave a review","句","レビュー（評価）を残す"),
        ("flea market app","名","フリマアプリ"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>コロケーションと会話定型の品詞判定</b>。"
            "<span class='en'>to</span>／助動詞／命令文の後は原形、冠詞 <span class='en'>the</span> の後は名詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "Set B は全て動詞なので、<span class='en'>make an offer</span>／<span class='en'>lower the price</span>／<span class='en'>leave a review</span> のような<b>定番の結びつき</b>で確定させる。"
            "使わない2語（along・greeting／give・raise）を先に当てにいくと、連鎖ミスが消える。",
}
