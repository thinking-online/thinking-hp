# -*- coding: utf-8 -*-
"""大問Ⅰ 成蹊型オリジナル演習セット（会話2本×空所13）。
各Setは Set A(空所1-7) と Set B(空所8-13)。語群には使わない2語が混じる。"""

PROBLEMS = []

# ===========================================================================
# SET 01 ― プレゼンの手応え／インターンの締切
# ===========================================================================
PROBLEMS.append({
  "theme": "プレゼンの手応え ＆ インターンの締切",
  "scene": "キャンパスのカフェ／インターン先のオフィス",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "経営学のグループ発表を終えた学生2人（Aoi と Ken）",
      "lines": [
        ("Aoi", "Ken, how did your group's presentation ( 1 ) in the end?"),
        ("Ken", "Honestly, better than I expected. We were ( 2 ) behind schedule last week, so I was worried."),
        ("Aoi", "I remember. You said your slides weren't even finished."),
        ("Ken", "Right. But Mari ( 3 ) up with a way to split the workload, and everything came together."),
        ("Aoi", "That ( 4 ) sense. She's good at organizing people."),
        ("Ken", "Exactly. Professor Sato even said our market analysis was ( 5 )."),
        ("Aoi", "No ( 6 )! You spent two whole weekends on it."),
        ("Ken", "Well, it finally ( 7 ) off. I'm just glad it's over."),
      ],
      "bank": [("a","makes"),("b","eager"),("c","turn out"),("d","wonder"),
               ("e","running"),("f","impressive"),("g","came"),("h","paid"),("i","brought")],
      "answers": {1:"turn out",2:"running",3:"came",4:"makes",5:"impressive",6:"wonder",7:"paid"},
      "exp": {
        1:{"frame":"疑問文 <span class='en'>how did … ( )</span> の空所は<b>動詞（原形）</b>。<span class='en'>did</span> があるので原形が入る。",
           "logic":"「発表は結局どう<b>なった</b>のか」と結果を尋ねる文脈。<span class='en'>turn out</span>＝「結局〜となる／判明する」。",
           "trap":"<span class='en'>came</span> も動詞だが <span class='en'>how did it come?</span> は不自然。結果を問う定型は <span class='en'>turn out</span>。"},
        2:{"frame":"<span class='en'>were ( ) behind schedule</span>。be動詞の後なので <b>-ing 形</b>が枠に合う。",
           "logic":"<span class='en'>run behind schedule</span>＝「予定より遅れている」。過去進行で「遅れていた」。",
           "trap":"<span class='en'>eager</span>（形容詞）は枠には合うが <span class='en'>behind schedule</span> と意味が繋がらない。"},
        3:{"frame":"主語 <span class='en'>Mari</span> ＋（ ）＋ <span class='en'>up with</span>。空所は<b>動詞の過去形</b>。",
           "logic":"<span class='en'>come up with</span>＝「（案を）思いつく」。過去形 <span class='en'>came</span>。",
           "trap":"<span class='en'>brought</span> を入れると <span class='en'>brought up with</span> となり非慣用。<span class='en'>bring up</span>＝「話題に出す」で <span class='en'>with</span> を取らない。"},
        4:{"frame":"<span class='en'>That ( ) sense</span>。主語 <span class='en'>That</span> に対する<b>動詞（三単現）</b>。",
           "logic":"<span class='en'>make sense</span>＝「筋が通る／なるほど」。現在の一般的評価なので <span class='en'>makes</span>。",
           "trap":"<span class='en'>came</span>/<span class='en'>brought</span> では <span class='en'>sense</span> と結び付かない。定型 <span class='en'>make sense</span> を丸ごと覚える。"},
        5:{"frame":"<span class='en'>analysis was ( )</span>。be動詞の後は<b>形容詞</b>。",
           "logic":"教授が褒めた文脈＝プラス評価。<span class='en'>impressive</span>＝「見事な、印象的な」。",
           "trap":"<span class='en'>eager</span>（熱心な）は人には使うが分析物には不自然。主語が<b>物</b>なら <span class='en'>impressive</span>。"},
        6:{"frame":"<span class='en'>No ( )!</span> 単独の感嘆。<b>名詞</b>が入る会話定型。",
           "logic":"<span class='en'>No wonder!</span>＝「どうりで／道理で」。努力を知って納得する反応。",
           "trap":"ここは会話定型表現の枠。品詞が名詞で意味が「納得」になるのは <span class='en'>wonder</span> のみ。"},
        7:{"frame":"<span class='en'>it finally ( ) off</span>。主語 <span class='en'>it</span> の<b>過去形動詞</b>。",
           "logic":"<span class='en'>pay off</span>＝「（努力が）報われる／実を結ぶ」。過去形 <span class='en'>paid</span>。",
           "trap":"残る動詞から機械的に確定できる。<span class='en'>came off</span>（取れる・成功する）は文脈と噛み合わない。"},
      },
      "unused": "<b>eager</b>（熱心な・形容詞）と <b>brought</b>（bring の過去形）が残る。"
                "eager は空所5に形の上では入るが「分析＝物」に対する評価語として不適。"
                "brought は空所3で <span class='en'>brought up with</span> という非慣用形になり脱落する。",
      "trans": "Aoi「ケン、グループ発表、結局どうだった？」／Ken「正直、思ったよりよかった。先週は予定より遅れてて心配だったんだ」／"
               "Aoi「覚えてる。スライドすら終わってないって言ってたよね」／Ken「そう。でもマリが作業分担のやり方を思いついて、全部まとまったんだ」／"
               "Aoi「なるほどね。彼女、人をまとめるの上手いもん」／Ken「まさに。佐藤教授にも市場分析が見事だって言われたよ」／"
               "Aoi「どうりで！週末まるまる2回かけてたもんね」／Ken「うん、やっと報われた。終わってほっとしてる」",
      "vocab": [
        ("turn out","句動","結局〜となる／判明する。<span class='en'>It turned out to be true.</span>"),
        ("run behind schedule","句","予定より遅れている"),
        ("come up with","句動","（案・解決策を）思いつく"),
        ("make sense","句","筋が通る／理解できる"),
        ("impressive","形","印象的な、見事な"),
        ("No wonder!","定型","どうりで／道理で"),
        ("pay off","句動","（努力が）報われる、実を結ぶ"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "インターン先で締切について話す同僚2人（Riku と Nina）",
      "lines": [
        ("Riku", "Hey Nina, do you have a minute? I need to ( 8 ) base with you about the client report."),
        ("Nina", "Sure, go ( 9 ). What's up?"),
        ("Riku", "The deadline got moved up to Friday. I'm worried we won't ( 10 ) up in time."),
        ("Nina", "Don't panic. If we split the sections, we can ( 11 ) it off."),
        ("Riku", "That would help. To be ( 12 ), I've never handled a report this big."),
        ("Nina", "Neither had I at first. Just ( 13 ) to the outline and we'll be fine."),
      ],
      "bank": [("a","ahead"),("b","afraid"),("c","touch"),("d","stick"),
               ("e","reach"),("f","pull"),("g","honest"),("h","catch")],
      "answers": {8:"touch",9:"ahead",10:"catch",11:"pull",12:"honest",13:"stick"},
      "exp": {
        8:{"frame":"<span class='en'>need to ( ) base with you</span>。<span class='en'>to</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>touch base with</span>＝「〜と連絡・意思確認を取る」。ビジネス会話の定番。",
           "trap":"<span class='en'>reach base</span> は非慣用。<span class='en'>touch base</span> を句で覚える。"},
        9:{"frame":"<span class='en'>go ( )</span>。許可を促す会話定型。<b>副詞</b>が入る。",
           "logic":"<span class='en'>Go ahead.</span>＝「どうぞ（話して）」。相手の発言を促す応答。",
           "trap":"ここは応答の定型。副詞で意味が「どうぞ」になるのは <span class='en'>ahead</span> のみ。"},
        10:{"frame":"<span class='en'>won't ( ) up in time</span>。助動詞 <span class='en'>won't</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>catch up</span>＝「（遅れを）取り戻す／間に合う」。締切に「間に合わない」心配。",
            "trap":"<span class='en'>reach up</span> は不自然。<span class='en'>catch up in time</span> のコロケーション。"},
        11:{"frame":"<span class='en'>can ( ) it off</span>。助動詞の後の<b>原形</b>＋ <span class='en'>off</span>。",
            "logic":"<span class='en'>pull off</span>＝「（難しいことを）やってのける」。分担すれば達成できる、の文脈。",
            "trap":"<span class='en'>reach it off</span> は非慣用。目的語 <span class='en'>it</span> を挟む句動詞 <span class='en'>pull … off</span>。"},
        12:{"frame":"<span class='en'>To be ( ),</span> 文頭の前置き。<b>形容詞</b>が入る会話定型。",
            "logic":"<span class='en'>To be honest,</span>＝「正直に言うと」。本音を切り出す前置き。",
            "trap":"<span class='en'>To be afraid</span> は非文。前置きの定型は <span class='en'>To be honest</span>。afraid は <span class='en'>I'm afraid …</span> の形で使う。"},
        13:{"frame":"命令文 <span class='en'>Just ( ) to the outline</span>。文頭は<b>動詞原形</b>。",
            "logic":"<span class='en'>stick to</span>＝「〜を守り続ける／（計画に）忠実にやる」。「筋書き通りにやれば大丈夫」。",
            "trap":"残る動詞から確定。<span class='en'>reach to the outline</span> は意味不明。"},
      },
      "unused": "<b>afraid</b>（形容詞）と <b>reach</b>（動詞）が残る。"
                "afraid は空所12に形は合うが <span class='en'>To be afraid</span> という前置きは存在しない。"
                "reach はどの空所でもコロケーションが成立せず脱落する。「使わない2語」を先に予想できれば残りが確定する。",
      "trans": "Riku「ニナ、ちょっといい？ クライアント向けレポートの件で確認したいんだ」／Nina「いいよ、どうぞ。どうしたの？」／"
               "Riku「締切が金曜に前倒しになってさ。間に合わないんじゃないかと心配で」／Nina「落ち着いて。セクションを分ければ、やり切れるよ」／"
               "Riku「助かる。正直、こんな大きなレポートは初めてなんだ」／Nina「最初は私もそうだったよ。筋書き通りにやれば大丈夫」",
      "vocab": [
        ("touch base with","句動","〜と連絡・意思確認を取る"),
        ("Go ahead.","定型","どうぞ（許可・促し）"),
        ("catch up","句動","遅れを取り戻す／追いつく"),
        ("pull off","句動","（難事を）やってのける"),
        ("To be honest","定型","正直に言うと"),
        ("stick to","句動","〜を守り続ける、（計画に）忠実にやる"),
        ("move up","句動","（日程を）前倒しにする"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞と会話定型の品詞判定</b>。<span class='en'>to</span>／助動詞／命令文の後は原形、"
            "be動詞の後は形容詞・-ing、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "使わない2語（eager・brought／afraid・reach）を先に当てにいくと、連鎖ミスが消える。",
})

# ---------------------------------------------------------------------------
# 追加セット（d1_sets/set_02.py 〜 set_10.py）を順に読み込む
# ---------------------------------------------------------------------------
import importlib, os
_here = os.path.dirname(__file__)
for _n in range(2, 13):
    _mod = f"d1_sets.set_{_n:02d}"
    _path = os.path.join(_here, "d1_sets", f"set_{_n:02d}.py")
    if os.path.exists(_path):
        _m = importlib.import_module(_mod)
        PROBLEMS.append(_m.SET)
