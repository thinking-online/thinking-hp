# -*- coding: utf-8 -*-
"""大問Ⅳ SET 10 ― 短文2本・空所6（語彙4＋文選択2）。
文1=フードロスと食品廃棄（社会）／文2=火山と気候（科学）。
本文タグ: [[b:N]]=空所(設問N)。各文3空所（語彙2＋文選択1）。"""

SET = {
  "theme": "フードロスと食品廃棄 ＆ 火山と気候",
  "genre": "社会／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "The Cost of Wasted Food", "wordcount": 101,
     "paras": [
        "Roughly a third of all food grown for people is never eaten. "
        "The causes range from strict cosmetic standards in stores to plain forgetfulness at home. "
        "Some crops [[b:41]] in the field before harvest, and huge amounts are thrown away later in shops and homes. "
        "The loss is not only moral but environmental, because the water, land, and energy [[b:42]] to grow that food "
        "are wasted along with it. [[b:43]] "
        "Simple habits — planning meals, storing food properly, and trusting our senses instead of printed dates — "
        "could cut household waste sharply and ease pressure on a strained global food supply.",
     ]},
    {"label": "文2", "title": "When Volcanoes Cool the Earth", "wordcount": 96,
     "paras": [
        "Large volcanic eruptions do more than reshape the land; they can cool the entire planet. "
        "When a volcano [[b:44]] huge clouds of ash and sulphur gas high into the atmosphere, "
        "tiny droplets form and spread around the globe. "
        "These droplets reflect sunlight back into space, so surface temperatures [[b:45]] for months or even years. "
        "[[b:46]] "
        "After the eruption of Tambora in 1815, Europe and North America suffered a year without a summer: "
        "crops failed, snow fell in June, and hunger spread. "
        "Such events remind us that a single mountain can rewrite a season of human history.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["rot","travel","appear","double"],"answer":"ア",
     "basis":"<span class='en'>Some crops ( ) in the field before harvest</span>。"
             "文全体は『食料が食べられずに失われる』話で、直後も <span class='en'>thrown away</span>（捨てられる）と続く。",
     "solve":"『収穫前に畑で』＋損失の文脈から、作物が<b>だめになる＝腐る</b>＝<span class='en'>rot</span>。",
     "cut":"<span class='en'>travel / appear / double</span>（移動する・現れる・倍増する）は<b>損失</b>の流れと噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["needed","refused","saved","sold"],"answer":"ア",
     "basis":"<span class='en'>the water, land, and energy ( ) to grow that food are wasted along with it</span>。"
             "『その食料を育てるのに〜資源も一緒に無駄になる』。",
     "solve":"<span class='en'>( ) to grow that food</span>＝『育てるのに<b>必要な</b>』＝<span class='en'>needed</span>。後半の <span class='en'>wasted</span> と論理が通る。",
     "cut":"<span class='en'>refused / saved / sold</span>（拒まれた・節約された・売られた）だと『無駄になる』と繋がらない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "Yet much of this waste is surprisingly easy to prevent.",
       "As a result, growing far more food is the only answer.",
       "Fortunately, food has never been cheaper to produce.",
       "For this reason, printed dates should always be obeyed."],"answer":"ア",
     "basis":"空所前＝『資源まで無駄になる』という問題提起。空所後＝<span class='en'>Simple habits ... could cut household waste sharply</span>（簡単な習慣で廃棄を大きく減らせる）。",
     "solve":"空所は<b>問題→解決</b>の橋渡し。直後が防止策なので『だが多くは驚くほど防ぎやすい』が接続する。",
     "cut":"『もっと作るしかない』は防止策と逆。『安く作れる』は無関係。『表示日を常に守れ』は直後の『自分の感覚を信じよ』と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["hurls","buries","absorbs","swallows"],"answer":"ア",
     "basis":"<span class='en'>a volcano ( ) huge clouds of ash and sulphur gas high into the atmosphere</span>。"
             "『大量の灰と硫黄ガスを大気の高くへ』。",
     "solve":"<span class='en'>( ) ... high into the atmosphere</span>＝上方へ<b>噴き上げる</b>＝<span class='en'>hurls</span>。次文の <span class='en'>form and spread</span> とも整合。",
     "cut":"<span class='en'>buries / absorbs / swallows</span>（埋める・吸収する・飲み込む）は方向が逆で『高くへ』と矛盾。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["drop","rise","spread","return"],"answer":"ア",
     "basis":"<span class='en'>These droplets reflect sunlight back into space, so surface temperatures ( )</span>。"
             "『小滴が日光を宇宙へ反射するので、地表の気温が〜』。",
     "solve":"<span class='en'>reflect sunlight ... so</span> の因果から、気温は<b>下がる</b>＝<span class='en'>drop</span>。冒頭 <span class='en'>cool the entire planet</span> と一致。",
     "cut":"<span class='en'>rise</span>（上がる）は寒冷化と逆。<span class='en'>spread / return</span> は主語の気温と結びつかない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "History records several dramatic cases of this cooling.",
       "Fortunately, no eruption has ever changed the weather.",
       "In warmer regions, volcanoes have the opposite effect.",
       "Most of this ash settles harmlessly within a single day."],"answer":"ア",
     "basis":"空所前＝『気温が数か月〜数年下がる』という一般的な仕組み。空所後＝<span class='en'>After the eruption of Tambora in 1815 ...</span> という具体的な歴史例。",
     "solve":"空所は<b>一般化→具体例</b>の橋渡し。直後が過去の事例なので『歴史はこの寒冷化の劇的な例をいくつも記録している』が最適。",
     "cut":"『噴火が天候を変えた例はない』は直後の事例と矛盾。『暖地では逆の効果』は無関係。『灰は一日で無害に沈む』は数年続く記述と矛盾。"},
  ],
  "trans": [
    ("文1", "人間のために育てられる食料のおよそ3分の1は食べられることがない。原因は、店の厳しい見た目の基準から、"
            "家庭での単なる忘れっぽさまで多岐にわたる。作物の一部は収穫前に畑で<b>腐り</b>、さらに大量が後で店や家庭で捨てられる。"
            "この損失は道徳的であるだけでなく環境的でもある。というのも、その食料を育てるのに<b>必要な</b>水・土地・エネルギーも"
            "一緒に無駄になるからだ。<b>だが、この廃棄の多くは驚くほど防ぎやすい。</b>"
            "献立を計画し、食品を適切に保存し、印字された日付ではなく自分の感覚を信じるといった簡単な習慣が、"
            "家庭の廃棄を大きく減らし、逼迫した世界の食料供給への圧力を和らげうる。"),
    ("文2", "大規模な火山噴火は土地の形を変えるだけでなく、地球全体を冷やしうる。火山が大量の灰と硫黄ガスを大気の高くへ"
            "<b>噴き上げる</b>と、微小な小滴ができて地球全体に広がる。これらの小滴が日光を宇宙へ反射するので、地表の気温は"
            "数か月、時には数年にわたって<b>下がる</b>。<b>歴史はこの寒冷化の劇的な例をいくつも記録している。</b>"
            "1815年のタンボラ噴火の後、ヨーロッパと北米は夏のない一年に見舞われた。作物は不作となり、6月に雪が降り、"
            "飢えが広がった。こうした出来事は、一つの山が人類の歴史の一季節を書き換えうることを思い出させてくれる。"),
  ],
  "vocab": [
    ("rot", "動", "腐る、だめになる"),
    ("harvest", "名", "収穫（期）"),
    ("strained", "形", "逼迫した、張り詰めた"),
    ("eruption", "名", "噴火、爆発"),
    ("sulphur", "名", "硫黄"),
    ("droplet", "名", "小滴、微小な粒"),
    ("reflect", "動", "反射する、映す"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（問題→解決／一般化→具体例）</b>で一意に決まる。"
    "文選択は代入して前後を音読し、話が途切れない1文を選ぶ。",
}
