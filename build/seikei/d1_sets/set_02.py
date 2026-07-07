# -*- coding: utf-8 -*-
SET = {
  "theme": "OB訪問で就活相談 ＆ サークル新歓の準備",
  "scene": "大学のラウンジ／サークルの部室",
  "limit": "目標9分",
  "convs": [
    {
      "set": "A", "title": "Conversation 1",
      "setting": "経営学部の学生 Kaito が先輩 Yui に就活（OB訪問・エントリーシート）の相談をする場面",
      "lines": [
        ("Kaito", "Yui, thanks for making time for me. Could I ( 1 ) your brain about job hunting?"),
        ("Yui", "Of course. Have you ( 2 ) down which industries you're aiming for?"),
        ("Kaito", "Sort of. I've researched a few firms, but I'm not sure I'm on the right ( 3 )."),
        ("Yui", "You're doing fine. The key is to make your entry sheet ( 4 ) out from the rest."),
        ("Kaito", "That's the hard part. Writing about my own strengths doesn't ( 5 ) naturally to me."),
        ("Yui", "It gets easier. Just be ( 6 ) about what you actually did—vague answers never impress interviewers."),
        ("Kaito", "Got it. And I'll ( 7 ) up on each company before the interview, too."),
        ("Yui", "Perfect. Do that and you'll be ahead of most applicants."),
      ],
      "bank": [("a","stand"),("b","brush"),("c","pick"),("d","specific"),
               ("e","narrowed"),("f","come"),("g","eager"),("h","track"),("i","read")],
      "answers": {1:"pick",2:"narrowed",3:"track",4:"stand",5:"come",6:"specific",7:"read"},
      "exp": {
        1:{"frame":"<span class='en'>Could I ( ) your brain</span>。助動詞 <span class='en'>Could</span> ＋主語の後なので空所は<b>動詞（原形）</b>。",
           "logic":"<span class='en'>pick someone's brain</span>＝「〜の知恵を借りる／教えを請う」。相談を切り出す会話定型。",
           "trap":"<span class='en'>read</span> も原形だが <span class='en'>read your brain</span> は非慣用。知恵を借りる定型は <span class='en'>pick your brain</span>。"},
        2:{"frame":"<span class='en'>Have you ( ) down …</span>。現在完了 <span class='en'>have + 過去分詞</span>の枠。",
           "logic":"<span class='en'>narrow down</span>＝「（候補を）絞り込む」。志望業界を絞ったか尋ねる文脈。",
           "trap":"他の動詞では <span class='en'>down</span> と結び付かない。過去分詞形で <span class='en'>narrowed</span> のみが枠に合う。"},
        3:{"frame":"<span class='en'>on the right ( )</span>。前置詞句 <span class='en'>on the right …</span> の後は<b>名詞</b>。",
           "logic":"<span class='en'>on the right track</span>＝「正しい方向に進んで」。方向性が合っているか不安、の流れ。",
           "trap":"空所に動詞を入れる形にはならない。名詞で「順調・方向」を表すのは <span class='en'>track</span>。"},
        4:{"frame":"<span class='en'>make your entry sheet ( ) out</span>。使役 <span class='en'>make + O + 原形</span>の枠。",
           "logic":"<span class='en'>stand out</span>＝「目立つ／際立つ」。応募書類を他と差別化する、の文脈。",
           "trap":"<span class='en'>come out</span>（現れる・出版される）では書類を「目立たせる」意味にならない。<span class='en'>stand out</span>。"},
        5:{"frame":"<span class='en'>doesn't ( ) naturally</span>。助動詞 <span class='en'>does</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>come naturally (to …)</span>＝「（〜にとって）自然にできる」。自己PRが苦手、の流れ。",
           "trap":"<span class='en'>stand naturally</span> は意味を成さない。<span class='en'>come naturally</span> をひとまとまりで覚える。"},
        6:{"frame":"<span class='en'>be ( ) about …</span>。be動詞の後は<b>形容詞</b>。",
           "logic":"<span class='en'>be specific about</span>＝「〜について具体的に述べる」。直後の「曖昧な答えは響かない」と対比。",
           "trap":"<span class='en'>eager</span>（熱心な）は形容詞で枠には合うが、「曖昧さ」と対比されるのは <b>具体性</b>＝<span class='en'>specific</span>。"},
        7:{"frame":"<span class='en'>I'll ( ) up on …</span>。助動詞 <span class='en'>will</span> の後は<b>原形</b>。",
           "logic":"<span class='en'>read up on</span>＝「〜について（新たに）詳しく調べる」。面接前に各社を下調べする、の文脈。",
           "trap":"<span class='en'>brush up on</span> は「学び直す・復習する」で既習の内容に使う。初めて調べる会社には <span class='en'>read up on</span>。"},
      },
      "unused": "<b>brush</b>（動詞）と <b>eager</b>（形容詞）が残る。"
                "brush は空所7に <span class='en'>brush up on</span> として一見入るが、初めて調べる会社に対しては「復習する」の brush は不適で、「新たに調べる」read が正しい。"
                "eager は空所6に形の上では入るが、「曖昧な答え」と対比されるのは <b>具体性</b>を表す specific であり、熱心さの eager では意味がつながらない。",
      "trans": "Kaito「ユイ先輩、時間を作ってくれてありがとうございます。就活のことで知恵を借りてもいいですか？」／"
               "Yui「もちろん。どの業界を狙うか、もう絞り込んだ？」／"
               "Kaito「一応。何社か調べたんですけど、方向性が合っているか自信がなくて」／"
               "Yui「大丈夫、順調よ。大事なのはエントリーシートを他の人より目立たせること」／"
               "Kaito「そこが難しくて。自分の強みを書くのって、自然にはできないんです」／"
               "Yui「だんだん慣れるわ。自分が実際に何をしたかを具体的に書くこと。曖昧な答えは面接官に響かないから」／"
               "Kaito「分かりました。それに面接前には各社をしっかり下調べします」／"
               "Yui「完璧。それができれば、たいていの応募者より一歩リードよ」",
      "vocab": [
        ("pick someone's brain","定型","〜の知恵を借りる、教えを請う"),
        ("narrow down","句動","（候補を）絞り込む"),
        ("on the right track","定型","正しい方向に進んで、順調で"),
        ("stand out","句動","目立つ、際立つ"),
        ("come naturally","句","（人にとって）自然にできる"),
        ("be specific about","句","〜について具体的に述べる"),
        ("read up on","句動","〜について（新たに）詳しく調べる"),
      ],
    },
    {
      "set": "B", "title": "Conversation 2",
      "setting": "サークルの新歓イベント（新入生歓迎会）の準備を相談する2人（Sora と Rin）",
      "lines": [
        ("Sora", "Rin, we should ( 8 ) down and plan the welcome party. New members join next week."),
        ("Rin", "Good idea. First, what's our ( 9 ) for food and decorations?"),
        ("Sora", "About twenty thousand yen. We'll have to ( 10 ) costs down where we can."),
        ("Rin", "Then let's ( 11 ) up the work. I can design the flyers if you book the room."),
        ("Sora", "Sounds fair. Should we ( 12 ) out flyers on campus or just post online?"),
        ("Rin", "Let's do both to be ( 13 ). The more people we reach, the better."),
      ],
      "bank": [("a","hand"),("b","cut"),("c","budget"),("d","sit"),
               ("e","share"),("f","safe"),("g","keep"),("h","split")],
      "answers": {8:"sit",9:"budget",10:"keep",11:"split",12:"hand",13:"safe"},
      "exp": {
        8:{"frame":"<span class='en'>should ( ) down and plan</span>。助動詞 <span class='en'>should</span> の後は<b>動詞原形</b>。",
           "logic":"<span class='en'>sit down (and …)</span>＝「腰を据えて（じっくり）〜する」。準備に取りかかろう、の切り出し。",
           "trap":"<span class='en'>split down</span> などは非慣用。<span class='en'>down</span> と組んで「じっくり取り組む」は <span class='en'>sit down</span>。"},
        9:{"frame":"<span class='en'>what's our ( ) for …</span>。所有格 <span class='en'>our</span> の後は<b>名詞</b>。",
           "logic":"<span class='en'>budget</span>＝「予算」。食事や装飾にいくら使えるかを尋ねる文脈。",
           "trap":"空所は名詞の枠。動詞では <span class='en'>our ( )</span> の形に収まらない。金額の話題は <span class='en'>budget</span>。"},
        10:{"frame":"<span class='en'>have to ( ) costs down</span>。<span class='en'>have to</span> の後は<b>原形</b>。",
            "logic":"<span class='en'>keep costs down</span>＝「費用を（低く）抑える」。予算内に収める、の流れ。",
            "trap":"<span class='en'>cut</span> は <span class='en'>cut costs</span> なら自然だが <span class='en'>cut costs down</span> は語順が非慣用。<span class='en'>( ) costs down</span> の枠に合うのは <span class='en'>keep</span>。"},
        11:{"frame":"<span class='en'>let's ( ) up the work</span>。<span class='en'>let's</span> の後は<b>動詞原形</b>。",
            "logic":"<span class='en'>split up the work</span>＝「作業を分担する」。役割を分けよう、の提案。",
            "trap":"<span class='en'>share</span> は <span class='en'>share the work</span> なら成立するが <span class='en'>share up</span> は非慣用。<span class='en'>up</span> を取って分担を表すのは <span class='en'>split</span>。"},
        12:{"frame":"<span class='en'>Should we ( ) out flyers</span>。助動詞 <span class='en'>Should</span> ＋主語の後は<b>原形</b>。",
            "logic":"<span class='en'>hand out</span>＝「（チラシなどを）配る」。学内で配布するか投稿だけにするか、の相談。",
            "trap":"<span class='en'>keep out</span>（締め出す）では「配る」意味にならない。<span class='en'>hand out flyers</span> のコロケーション。"},
        13:{"frame":"<span class='en'>to be ( )</span>。<span class='en'>to be</span> の後は<b>形容詞</b>の会話定型。",
            "logic":"<span class='en'>to be safe</span>＝「念のため／万全を期して」。両方やっておこう、の文脈。",
            "trap":"残る形容詞から確定。両方の告知手段を使う理由づけとして「念のため」に合うのは <span class='en'>safe</span>。"},
      },
      "unused": "<b>cut</b>（動詞）と <b>share</b>（動詞）が残る。"
                "cut は空所10に一見入るが <span class='en'>cut costs down</span> という語順が非慣用で、<span class='en'>keep costs down</span> が正しい。"
                "share は空所11に <span class='en'>share the work</span> なら合うが、直後に <span class='en'>up</span> があり <span class='en'>share up</span> は成立しないため脱落する。「使わない2語」を先に見抜けば残りが確定する。",
      "trans": "Sora「リン、腰を据えて新歓の計画を立てようよ。来週には新入生が入ってくるし」／"
               "Rin「いいね。まず、食事と装飾の予算はいくら？」／"
               "Sora「2万円くらい。できるところは費用を抑えないとね」／"
               "Rin「じゃあ作業を分担しよう。あなたが部屋を予約してくれるなら、私はチラシを作るよ」／"
               "Sora「公平だね。チラシは学内で配る？ それともオンラインに投稿するだけにする？」／"
               "Rin「念のため両方やろう。届く人数は多いほどいいから」",
      "vocab": [
        ("sit down","句動","腰を据えてじっくり取り組む"),
        ("budget","名","予算"),
        ("keep costs down","句","費用を（低く）抑える"),
        ("split up","句動","（作業などを）分担する、分ける"),
        ("hand out","句動","（チラシなどを）配る"),
        ("to be safe","定型","念のため、万全を期して"),
        ("the more …, the better","構文","〜が多いほど良い"),
      ],
    },
  ],
  "lesson": "本セットの核は<b>句動詞・会話定型と品詞・語順の判定</b>。<span class='en'>Could / should / will</span> や <span class='en'>let's</span>・<span class='en'>have to</span> の後は原形、"
            "be動詞・<span class='en'>to be</span> の後は形容詞、所有格や <span class='en'>on the right …</span> の後は名詞、というふうに<b>枠で候補を半分に落とし</b>てから意味で決める。"
            "紛らわしい語（brush と read／cut と keep／share と split）は<b>付く前置詞（副詞）とコロケーション</b>で切り分ける。"
            "使わない2語（eager・brush／cut・share）を先に予想できれば、連鎖ミスが消える。",
}
