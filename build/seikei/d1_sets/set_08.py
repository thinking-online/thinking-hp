# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 08。
Set A(空所1-7)＝学園祭の模擬店の売上振り返り、Set B(空所8-13)＝週末旅行の計画。
語群には使わない2語が混じる。"""

SET = {
  "theme": "学園祭の模擬店の売上振り返り ＆ 週末旅行の計画",
  "scene": "学園祭の実行委員テント／友人宅のリビング",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "学園祭のたこ焼き模擬店を運営した実行委員2人（Kai と Nozomi）",
      "lines": [
        ("Nozomi", "Kai, our stall was packed all day! Did we ( 1 ) a good profit in the end?"),
        ("Kai", "We did. Our total ( 2 ) came to about 80,000 yen."),
        ("Nozomi", "Amazing. Though the ( 3 ) got really long around lunchtime, didn't it?"),
        ("Kai", "It did. We almost ( 4 ) out of octopus by one o'clock."),
        ("Nozomi", "Good thing we ( 5 ) up on extra ingredients that morning."),
        ("Kai", "Exactly. Even after all the expenses, we still had a ( 6 ) profit."),
        ("Nozomi", "No wonder ― we had a steady ( 7 ) of customers all afternoon."),
      ],
      "bank": [("a","stocked"),("b","crowd"),("c","sales"),("d","healthy"),
               ("e","ran"),("f","went"),("g","line"),("h","stream"),("i","make")],
      "answers": {1:"make",2:"sales",3:"line",4:"ran",5:"stocked",6:"healthy",7:"stream"},
      "exp": {
        1:{"frame":"疑問文 <span class='en'>Did we ( ) a good profit</span>。<span class='en'>did</span> があるので空所は<b>動詞の原形</b>。",
           "logic":"<span class='en'>make a profit</span>＝「利益を上げる」。模擬店が儲かったかを尋ねる文脈。",
           "trap":"他候補 <span class='en'>ran</span>／<span class='en'>went</span>／<span class='en'>stocked</span> は過去形で <span class='en'>did</span> の後に置けない。原形は <span class='en'>make</span> だけ。"},
        2:{"frame":"<span class='en'>Our total ( ) came to about 80,000 yen</span>。<span class='en'>came</span> の主語になる<b>名詞</b>。",
           "logic":"<span class='en'>sales</span>＝「売上（高）」。金額（円）に結びつく語。<span class='en'>total sales</span>＝「総売上」。",
           "trap":"<span class='en'>crowd</span>（人だかり）も名詞だが金額 <span class='en'>80,000 yen</span> と噛み合わない。お金の話なら <span class='en'>sales</span>。"},
        3:{"frame":"<span class='en'>the ( ) got really long</span>。<span class='en'>the</span> の後で <span class='en'>got long</span> の主語になる<b>名詞</b>。",
           "logic":"<span class='en'>line</span>＝「行列」。<span class='en'>the line got long</span>＝「行列が長くなった」。",
           "trap":"<span class='en'>crowd</span> は「人だかり」で <span class='en'>got big</span> とは言えても <span class='en'>got long</span> は不自然。長くなるのは <span class='en'>line</span>。"},
        4:{"frame":"<span class='en'>we almost ( ) out of octopus</span>。過去の文なので<b>動詞の過去形</b>。",
           "logic":"<span class='en'>run out of</span>＝「〜を切らす／品切れになる」。過去形 <span class='en'>ran</span>。",
           "trap":"<span class='en'>went</span> も過去形だが <span class='en'>went out of octopus</span> は非慣用。品切れは <span class='en'>run out of</span>。"},
        5:{"frame":"<span class='en'>we ( ) up on extra ingredients</span>。過去の出来事で<b>動詞の過去形</b>＋ <span class='en'>up on</span>。",
           "logic":"<span class='en'>stock up on</span>＝「〜を買いだめする／仕入れておく」。過去形 <span class='en'>stocked</span>。",
           "trap":"<span class='en'>ran up on</span>／<span class='en'>went up on</span> は成立しない。仕入れの句動詞は <span class='en'>stock up on</span>。"},
        6:{"frame":"<span class='en'>we still had a ( ) profit</span>。冠詞 <span class='en'>a</span> と名詞 <span class='en'>profit</span> の間は<b>形容詞</b>。",
           "logic":"<span class='en'>a healthy profit</span>＝「かなりの／しっかりした利益」。<span class='en'>healthy</span> は「額が十分な」の意味。",
           "trap":"空所に入る形容詞は語群中 <span class='en'>healthy</span> のみ。<span class='en'>profit</span> と結ぶ定番のプラス評価語。"},
        7:{"frame":"<span class='en'>a steady ( ) of customers</span>。<span class='en'>a steady … of</span> に挟まれる<b>名詞</b>。",
           "logic":"<span class='en'>a steady stream of customers</span>＝「途切れない客の流れ」。<span class='en'>stream</span>＝「流れ」。",
           "trap":"<span class='en'>crowd</span> は <span class='en'>a steady … of</span> の型に乗らない。「絶え間ない流れ」は <span class='en'>stream</span> が定番。"},
      },
      "unused": "<b>crowd</b>（人だかり・名詞）と <b>went</b>（go の過去形）が残る。"
                "crowd は空所2・3・7に形は入るが、金額・<span class='en'>got long</span>・<span class='en'>steady … of</span> のいずれとも結びつかない。"
                "went は空所4・5で <span class='en'>went out of</span>／<span class='en'>went up on</span> という非慣用形になり脱落する。",
      "trans": "Nozomi「カイ、うちの店、一日中大にぎわいだったね！ 結局、利益はちゃんと出たの？」／Kai「出たよ。総売上で8万円くらいになった」／"
               "Nozomi「すごい。でもお昼どきは行列がかなり長くなってたよね？」／Kai「なったね。1時にはタコがほとんど品切れになりかけたよ」／"
               "Nozomi「朝のうちに材料を多めに仕入れておいてよかった」／Kai「ほんと。経費を全部差し引いても、まだしっかり利益が残ったよ」／"
               "Nozomi「どうりで――午後はずっと途切れなくお客さんが来てたもんね」",
      "vocab": [
        ("make a profit","句","利益を上げる"),
        ("sales","名","売上（高）"),
        ("line","名","行列。<span class='en'>wait in line</span>＝列に並ぶ"),
        ("run out of","句動","〜を切らす、品切れになる"),
        ("stock up on","句動","〜を買いだめする、仕入れておく"),
        ("a healthy profit","句","かなりの利益、しっかりした利益"),
        ("a steady stream of","句","途切れない〜の流れ"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "週末の小旅行を計画する友人2人（Aki と Yu）",
      "lines": [
        ("Aki", "Yu, have you ( 8 ) the hotel for this weekend yet?"),
        ("Yu", "Not yet. I was ( 9 ) to do it tonight. Prices go up if we wait."),
        ("Aki", "Good idea. So, should we ( 10 ) the train, or would driving be faster?"),
        ("Yu", "Let's go by train. Finding parking near the inn is always a real ( 11 )."),
        ("Aki", "True. Oh, and don't ( 12 ) to pack a raincoat."),
        ("Yu", "Right. The weather's been so ( 13 ) lately that I'll bring one just in case."),
      ],
      "bank": [("a","forget"),("b","booked"),("c","steady"),("d","take"),
               ("e","hassle"),("f","ordered"),("g","about"),("h","changeable")],
      "answers": {8:"booked",9:"about",10:"take",11:"hassle",12:"forget",13:"changeable"},
      "exp": {
        8:{"frame":"<span class='en'>have you ( ) the hotel yet</span>。<span class='en'>have</span> の後は<b>過去分詞</b>。",
           "logic":"<span class='en'>book</span>＝「予約する」。<span class='en'>book a hotel</span>＝「ホテルを予約する」。過去分詞 <span class='en'>booked</span>。",
           "trap":"<span class='en'>ordered</span> も過去分詞だが <span class='en'>order a hotel</span> は不自然。宿の予約は <span class='en'>book</span>、<span class='en'>order</span> は料理や品物に使う。"},
        9:{"frame":"<span class='en'>I was ( ) to do it tonight</span>。<span class='en'>was</span> と <span class='en'>to do</span> の間に入る語。",
           "logic":"<span class='en'>be about to do</span>＝「まさに〜しようとしている」。「今夜やるつもりだった」。",
           "trap":"語群でこの型 <span class='en'>was ( ) to do</span> に収まるのは <span class='en'>about</span> のみ。<span class='en'>about to</span> を句で覚える。"},
        10:{"frame":"<span class='en'>should we ( ) the train</span>。助動詞 <span class='en'>should</span> の後は<b>動詞の原形</b>。",
            "logic":"<span class='en'>take the train</span>＝「電車で行く／電車に乗る」。交通手段の <span class='en'>take</span>。",
            "trap":"<span class='en'>booked</span>／<span class='en'>ordered</span> は過去分詞で助動詞の後に置けない。原形は <span class='en'>take</span>。"},
        11:{"frame":"<span class='en'>is always a real ( )</span>。冠詞 <span class='en'>a</span> ＋ <span class='en'>real</span> の後は<b>名詞</b>。",
            "logic":"<span class='en'>a real hassle</span>＝「本当に面倒なこと」。駐車場探しの手間を指す。",
            "trap":"名詞で「面倒」を表せるのは <span class='en'>hassle</span>。<span class='en'>steady</span> は形容詞で <span class='en'>a real steady</span> とは言えない。"},
        12:{"frame":"<span class='en'>don't ( ) to pack a raincoat</span>。否定の命令文で<b>動詞の原形</b>。",
            "logic":"<span class='en'>don't forget to do</span>＝「忘れずに〜する」。「レインコートを忘れずに詰めて」。",
            "trap":"<span class='en'>ordered</span>／<span class='en'>booked</span> は形が合わず意味も通らない。原形で意味が通るのは <span class='en'>forget</span>。"},
        13:{"frame":"<span class='en'>The weather's been so ( ) lately</span>。<span class='en'>so</span> の後は<b>形容詞</b>。",
            "logic":"<span class='en'>changeable</span>＝「変わりやすい」。<span class='en'>so changeable that I'll bring one just in case</span>＝「変わりやすいので念のため持っていく」。",
            "trap":"<span class='en'>steady</span>（安定した）は反対の意味。「念のため持っていく」理由になるのは「変わりやすい」＝ <span class='en'>changeable</span>。"},
      },
      "unused": "<b>ordered</b>（order の過去分詞）と <b>steady</b>（安定した・形容詞）が残る。"
                "ordered は空所8で <span class='en'>order a hotel</span> という非慣用の組み合わせになり脱落。"
                "steady は空所13に形は合うが「変わりやすいから念のため」という文脈と正反対で不適。使わない2語を先に外せば残りが決まる。",
      "trans": "Aki「ユウ、今週末のホテルもう予約した？」／Yu「まだ。今夜やろうとしてたとこ。待つと値段が上がるからね」／"
               "Aki「いいね。で、電車で行く？ それとも車のほうが速いかな」／Yu「電車にしよう。宿の近くは駐車場探しがいつも本当に面倒なんだ」／"
               "Aki「たしかに。あ、レインコートを忘れずに詰めてね」／Yu「了解。最近すごく天気が変わりやすいから、念のため持っていくよ」",
      "vocab": [
        ("book","動","予約する。<span class='en'>book a room</span>＝部屋を予約する"),
        ("be about to do","句","まさに〜しようとしている"),
        ("take the train","句","電車で行く、電車に乗る"),
        ("hassle","名","面倒、手間。<span class='en'>a real hassle</span>＝実に厄介なこと"),
        ("don't forget to do","句","忘れずに〜する"),
        ("changeable","形","変わりやすい（天気など）"),
        ("just in case","句","念のため"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>枠（品詞）で候補を半分に落とす</b>こと。<span class='en'>did</span>・助動詞・命令文・<span class='en'>to</span> の後は原形、"
            "<span class='en'>have</span> の後は過去分詞、<span class='en'>a … 名詞</span>の間や <span class='en'>so</span> の後は形容詞、と機械的に絞る。"
            "そのうえで <span class='en'>make a profit</span>／<span class='en'>run out of</span>／<span class='en'>stock up on</span>／<span class='en'>be about to</span> などの"
            "<b>コロケーションと句動詞</b>で最終決定する。使わない2語（crowd・went／ordered・steady）を先に当てにいくと連鎖ミスが防げる。",
}
