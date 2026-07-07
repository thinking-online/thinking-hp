# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット SET 06。
Set A(空所1-7) と Set B(空所8-13)。語群には使わない2語が混じる。"""

SET = {
  "theme": "一人暮らしの部屋探し ＆ オンライン授業の接続トラブル",
  "scene": "部屋探しの相談／オンライン会議の画面越し",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "初めての一人暮らしに向けて部屋探しを相談する2人（Riku と Emma）",
      "lines": [
        ("Riku", "I'm finally looking for a place of my own. Do you know how I should ( 1 ) about finding a good apartment?"),
        ("Emma", "Well, the first thing is to set a budget. How much rent can you ( 2 ) each month?"),
        ("Riku", "Around 70,000 yen, I think. But the deposit is what really worries me."),
        ("Emma", "Right, most places ask for a deposit ( 3 ) advance. Have you decided on the area?"),
        ("Riku", "I'd like somewhere within walking ( 4 ) of the station."),
        ("Emma", "That makes sense. Just keep in mind that rent tends to go ( 5 ) the closer you get to the station."),
        ("Riku", "True. Should I ( 6 ) a look at the room before signing anything?"),
        ("Emma", "Definitely. Never sign a contract without ( 7 ) the place a visit first."),
      ],
      "bank": [("a","distance"),("b","spend"),("c","go"),("d","up"),
               ("e","paying"),("f","afford"),("g","range"),("h","in"),("i","take")],
      "answers": {1:"go",2:"afford",3:"in",4:"distance",5:"up",6:"take",7:"paying"},
      "exp": {
        1:{"frame":"疑問詞節 <span class='en'>how I should ( )</span>。助動詞 <span class='en'>should</span> の後なので<b>動詞原形</b>。",
           "logic":"<span class='en'>go about ~ing</span>＝「〜に取りかかる／どう進めるか」。「どうやって部屋探しを進めるべきか」。",
           "trap":"<span class='en'>spend</span> も動詞だが <span class='en'>spend about</span> は非慣用。「取りかかる」は <span class='en'>go about</span>。"},
        2:{"frame":"<span class='en'>can you ( ) each month</span>。<span class='en'>can</span> の後は<b>原形</b>で、<span class='en'>rent</span> を目的語に取る他動詞。",
           "logic":"<span class='en'>afford</span>＝「（金銭的に）〜を払える余裕がある」。「毎月いくらの家賃を払えるか」。",
           "trap":"<span class='en'>spend</span> は <span class='en'>spend money on rent</span> のように <span class='en'>on</span> が要る。<span class='en'>spend rent</span> とは言えない。"},
        3:{"frame":"<span class='en'>a deposit ( ) advance</span>。名詞 <span class='en'>advance</span> と結び付く<b>前置詞</b>。",
           "logic":"<span class='en'>in advance</span>＝「前もって、事前に」。敷金を「前もって」払う、の文脈。",
           "trap":"語群の中で前置詞はこれだけ。<span class='en'>in advance</span> を句のまま覚えるのが最短。"},
        4:{"frame":"<span class='en'>within walking ( )</span>。<span class='en'>walking</span> が前から修飾する<b>名詞</b>が入る。",
           "logic":"<span class='en'>within walking distance of ~</span>＝「〜から徒歩圏内で」。駅まで歩ける距離。",
           "trap":"<span class='en'>range</span> も名詞だが <span class='en'>walking range</span> は非慣用。定番は <span class='en'>walking distance</span>。"},
        5:{"frame":"<span class='en'>rent tends to go ( )</span>。動詞 <span class='en'>go</span> と組む<b>副詞</b>。",
           "logic":"<span class='en'>go up</span>＝「（値段が）上がる」。駅に近いほど家賃は上がる。",
           "trap":"方向を表す副詞はこれだけ。価格上昇は <span class='en'>go up</span> で表す。"},
        6:{"frame":"<span class='en'>Should I ( ) a look</span>。助動詞 <span class='en'>should</span> の後の<b>原形</b>。",
           "logic":"<span class='en'>take a look at ~</span>＝「〜を（ちょっと）見てみる」。契約前に部屋を内見する。",
           "trap":"<span class='en'>spend a look</span> とは言わない。「見てみる」は <span class='en'>take a look</span>。"},
        7:{"frame":"前置詞 <span class='en'>without</span> の後は<b>動名詞（-ing）</b>。",
           "logic":"<span class='en'>pay ~ a visit</span>＝「〜を訪れる」。「内見せずに契約するな」。",
           "trap":"残る語から確定できる。<span class='en'>a visit</span> と結ぶ動詞は <span class='en'>pay</span> で、<span class='en'>pay a visit</span> が定型。"},
      },
      "unused": "<b>spend</b>（動詞）と <b>range</b>（名詞）が残る。"
                "spend は空所2に形は合うが <span class='en'>spend on rent</span> のように <span class='en'>on</span> が要り、<span class='en'>afford</span> に負ける。"
                "range は空所4で <span class='en'>walking range</span> という非慣用形になり脱落する。使わない2語を先に見抜けば残りが決まる。",
      "trans": "Riku「やっと自分の部屋を探し始めるんだ。いい物件の探し方って、どう進めればいいか分かる？」／Emma「まずは予算を決めることね。毎月いくらの家賃を払える？」／"
               "Riku「7万円くらいかな。でも敷金が一番心配で」／Emma「そうね、たいていの物件は敷金を前払いで求めるから。エリアはもう決めた？」／"
               "Riku「駅から徒歩圏内のところがいいな」／Emma「なるほど。ただ、駅に近いほど家賃は上がりがちだと覚えておいてね」／"
               "Riku「確かに。契約する前に部屋を見ておくべきかな？」／Emma「絶対にね。内見せずに契約しちゃだめだよ」",
      "vocab": [
        ("go about","句動","（物事に）取りかかる、どう進めるか"),
        ("afford","動","（金銭的に）〜を払える余裕がある"),
        ("in advance","句","前もって、事前に"),
        ("within walking distance","句","徒歩圏内で"),
        ("go up","句動","（値段が）上がる"),
        ("take a look","句","（ちょっと）見てみる"),
        ("pay ~ a visit","句","〜を訪れる、訪問する"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "オンライン会議の接続トラブルに対応する2人（Mai と Jun）",
      "lines": [
        ("Mai", "Jun, can you hear me? Your voice keeps ( 8 ) out."),
        ("Jun", "Sorry, my connection is unstable. Let me ( 9 ) back in."),
        ("Mai", "Okay. While you do that, I'll ( 10 ) my screen so everyone can see the slides."),
        ("Jun", "Thanks. I'm ( 11 ) now. Is the audio any better?"),
        ("Mai", "Much clearer. By the way, could you ( 12 ) yourself when you're not talking? There's some background noise."),
        ("Jun", "Oh, sorry. I forgot I was unmuted. Anyway, let's ( 13 ) on with the meeting."),
      ],
      "bank": [("a","share"),("b","away"),("c","log"),("d","move"),
               ("e","cutting"),("f","back"),("g","close"),("h","mute")],
      "answers": {8:"cutting",9:"log",10:"share",11:"back",12:"mute",13:"move"},
      "exp": {
        8:{"frame":"<span class='en'>keeps ( ) out</span>。動詞 <span class='en'>keep</span> の後は<b>動名詞（-ing）</b>。",
           "logic":"<span class='en'>cut out</span>＝「（音声・接続が）途切れる」。声が途切れ続けている。",
           "trap":"<span class='en'>close</span> は <span class='en'>close out</span>＝「締め切る」で音声には使わない。途切れるは <span class='en'>cut out</span>。"},
        9:{"frame":"<span class='en'>Let me ( ) back in</span>。<span class='en'>let me</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>log back in</span>＝「（一度出て）再ログインする」。接続が不安定なので入り直す。",
           "trap":"<span class='en'>close back in</span> は意味をなさない。再入室は <span class='en'>log ... in</span>。"},
        10:{"frame":"<span class='en'>I'll ( ) my screen</span>。<span class='en'>will</span> の後の<b>原形</b>で、<span class='en'>screen</span> を目的語に取る。",
            "logic":"<span class='en'>share one's screen</span>＝「画面を共有する」。スライドを皆に見せる。",
            "trap":"<span class='en'>close my screen</span> は「画面を閉じる」で、皆に見せる文脈と逆。共有は <span class='en'>share</span>。"},
        11:{"frame":"<span class='en'>I'm ( ) now</span>。be動詞の後の<b>副詞（補語）</b>。",
            "logic":"<span class='en'>be back</span>＝「戻ってきた」。再接続して戻った状態。",
            "trap":"<span class='en'>away</span> も副詞だが <span class='en'>I'm away</span> は「席を外している」で逆の意味。戻ったは <span class='en'>back</span>。"},
        12:{"frame":"<span class='en'>could you ( ) yourself</span>。<span class='en'>could you</span> の後は<b>動詞原形</b>で、再帰目的語を取る。",
            "logic":"<span class='en'>mute oneself</span>＝「（自分の）マイクをミュートする」。雑音が入るので消音を依頼。",
            "trap":"再帰目的語 <span class='en'>yourself</span> と結んで意味が通る動詞は <span class='en'>mute</span> のみ。"},
        13:{"frame":"勧誘の <span class='en'>let's ( ) on with</span>。<span class='en'>let's</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>move on with ~</span>＝「〜を先に進める」。会議を進行する。",
            "trap":"残る動詞から確定できる。<span class='en'>move on</span>（先へ進む）は会議進行の定番表現。"},
      },
      "unused": "<b>away</b>（副詞）と <b>close</b>（動詞）が残る。"
                "away は空所11に形は合うが <span class='en'>I'm away</span>＝「離席中」で「戻った」と逆になる。"
                "close は空所10で <span class='en'>close my screen</span> となり「共有して見せる」文脈に合わず脱落する。使わない2語を先に読めば残りが確定する。",
      "trans": "Mai「ジュン、聞こえる？ 声が途切れ続けてるんだけど」／Jun「ごめん、接続が不安定で。入り直すね」／"
               "Mai「オッケー。その間に画面を共有して、みんながスライドを見られるようにするね」／Jun「ありがとう。戻ったよ。音声はよくなった？」／"
               "Mai「ずっとクリアになった。ところで、話してないときはミュートしてもらえる？ 雑音が少し入ってて」／Jun「あ、ごめん。ミュート解除したままだった。とにかく、会議を進めよう」",
      "vocab": [
        ("cut out","句動","（音声・接続が）途切れる"),
        ("log in","句動","ログインする（log back in＝入り直す）"),
        ("share one's screen","句","画面を共有する"),
        ("be back","句","戻ってきた"),
        ("mute","動","〜をミュートする、消音する"),
        ("move on with","句動","〜を先に進める、進行する"),
        ("background noise","名","背景雑音"),
      ],
    },
  ],
  "lesson": "本セットも<b>句動詞と会話定型を品詞の枠で絞る</b>のが核。"
            "<span class='en'>should</span>／<span class='en'>let me</span>／<span class='en'>let's</span>／<span class='en'>can・could you</span> の後は原形、"
            "<span class='en'>keep</span>／<span class='en'>without</span> の後は -ing、be動詞の後は副詞・形容詞、と<b>枠で半分に落として</b>から意味で決める。"
            "使わない2語（spend・range／away・close）を先に当てにいくと、連鎖ミスが消える。",
}
