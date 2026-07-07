# -*- coding: utf-8 -*-
"""大問Ⅳ SET 01（基準サンプル）― 短文2本・空所6（語彙4＋文選択2）。
本試験のⅣは短文2本×各2空所だが、本ドリルでは演習量を増やすため各文3空所（語彙2＋文選択1）とする。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "習慣化の科学 ＆ コーヒーハウスの起源",
  "genre": "社会／文化・歴史 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Why Small Steps Win", "wordcount": 100,
     "paras": [
        "Many people give up on a new habit within a few weeks. The problem is rarely willpower; it is poor [[b:41]]. "
        "When a goal feels too big, the brain treats it as a threat and [[b:42]]. [[b:43]] "
        "By shrinking the first action until it seems almost trivial — one page, one push-up, one line of code — "
        "we remove the friction that keeps us from starting at all.",
     ]},
    {"label": "文2", "title": "The First Coffee Houses", "wordcount": 98,
     "paras": [
        "In the seventeenth century, coffee houses [[b:44]] across London at remarkable speed. "
        "For the price of a single cup, anyone could sit for hours, read the latest news, and [[b:45]] about trade. "
        "[[b:46]] Merchants closed deals at these tables, writers traded ideas, and more than one newspaper "
        "was born in the noise and smoke of a crowded coffee room.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["planning","weather","luck","height"],"answer":"ア",
     "basis":"直前 <span class='en'>The problem is rarely willpower; it is poor ( )</span>。"
             "『問題は意志力ではなく、貧弱な〜だ』と対比。続く文が『目標が大きすぎると脳が抵抗する』＝<b>設計の失敗</b>を説明。",
     "solve":"<span class='en'>poor ( )</span> のコロケーションと、後続の原因説明から『計画・設計』＝<span class='en'>planning</span>。",
     "cut":"<span class='en'>weather / luck / height</span> は文脈と無関係。意志力と対比されるのは<b>計画性</b>。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["resists","cooperates","vanishes","improves"],"answer":"ア",
     "basis":"<span class='en'>the brain treats it as a threat and ( )</span>。脅威とみなした脳の反応。",
     "solve":"『脅威とみなす』の順接。脳は<b>抵抗する</b>＝<span class='en'>resists</span>。次文の <span class='en'>friction</span>（摩擦）とも整合。",
     "cut":"<span class='en'>cooperates</span>（協力する）は脅威への反応として逆。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "The solution is to make that first step smaller.",
       "This is why natural talent matters more than effort.",
       "Most people simply lack the willpower to change.",
       "Large goals are always better than small ones."],"answer":"ア",
     "basis":"空所前＝『大きな目標に脳が抵抗する』（問題）。空所後＝<span class='en'>By shrinking the first action ...</span>（最初の一歩を小さくする方法）。",
     "solve":"空所は<b>問題→解決</b>の橋渡し。直後が『縮める』方法なので『解決策は最初の一歩を小さくすること』が接続。",
     "cut":"『才能が努力に勝る』『意志力が足りない』は本文の主張（設計の問題）と逆。『大きな目標が常に良い』は直後と矛盾。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語句を選べ。","inline":True,
     "choices":["sprang up","died out","broke down","gave in"],"answer":"ア",
     "basis":"<span class='en'>coffee houses ( ) across London at remarkable speed</span>。『目覚ましい速さでロンドン中に』＝急増。",
     "solve":"<span class='en'>spring up</span>＝『あちこちに急に現れる』。<span class='en'>across ... at remarkable speed</span> と一致。",
     "cut":"<span class='en'>died out</span>（消滅）は逆。<span class='en'>broke down / gave in</span> は主語と噛み合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["argue","remain","sleep","hide"],"answer":"ア",
     "basis":"<span class='en'>sit for hours, read the latest news, and ( ) about trade</span>。動詞の並列。",
     "solve":"<span class='en'>( ) about trade</span>＝『商売について<b>議論する</b>』。<span class='en'>argue about</span> のコロケ。",
     "cut":"<span class='en'>remain / sleep / hide</span> は <span class='en'>about trade</span> と結びつかない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "They quickly became the hubs of commerce and conversation.",
       "They were soon banned for being far too quiet.",
       "Few ordinary people could ever afford to enter them.",
       "Coffee was seen as a luxury with no social value."],"answer":"ア",
     "basis":"空所前＝『誰でも座って新聞を読み商売を論じられた』。空所後＝商人が取引をまとめ作家がアイデアを交換した具体例。",
     "solve":"空所は<b>一般化（要点）→具体例</b>の橋渡し。直後の具体例を束ねる『商業と会話の中心地になった』が最適。",
     "cut":"『静かすぎて禁止』は騒がしい描写と矛盾。『庶民は入れない』は『誰でも座れた』と矛盾。『社会的価値なし』は趣旨と逆。"},
  ],
  "trans": [
    ("文1", "多くの人は新しい習慣を数週間でやめてしまう。問題は意志力ではなく、たいてい貧弱な<b>計画</b>にある。"
            "目標が大きすぎると感じると、脳はそれを脅威とみなし<b>抵抗する</b>。<b>解決策は、その最初の一歩を小さくすることだ。</b>"
            "最初の行動を――1ページ、腕立て1回、コード1行と――ほとんど取るに足らないほどに縮めれば、始めるのを妨げる摩擦が消える。"),
    ("文2", "17世紀、コーヒーハウスは目覚ましい速さでロンドン中に<b>次々と現れた</b>。一杯の値段で、誰もが何時間も座り、"
            "最新のニュースを読み、商売について<b>議論</b>できた。<b>それらはたちまち商業と会話の中心地になった。</b>"
            "商人はこの席で取引をまとめ、作家はアイデアを交換し、混雑した店の騒音と煙の中で新聞さえ生まれた。"),
  ],
  "vocab": [
    ("willpower", "名", "意志力"),
    ("friction", "名", "摩擦、抵抗"),
    ("trivial", "形", "取るに足らない"),
    ("spring up", "句動", "急に現れる、次々と生じる"),
    ("remarkable", "形", "目覚ましい、注目に値する"),
    ("hub", "名", "中心地、拠点"),
    ("commerce", "名", "商業"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（問題→解決／一般化→具体例）</b>で一意に決まる。"
    "文選択は代入して前後を音読し、話が途切れない1文を選ぶ。",
}
