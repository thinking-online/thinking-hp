# -*- coding: utf-8 -*-
"""大問Ⅳ SET 02 ― 短文2本・空所6（語彙4＋文選択2）。
文1=リサイクルと循環経済（社会／経済）、文2=睡眠と学習・記憶（科学）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "循環経済 ＆ 睡眠と記憶",
  "genre": "社会・経済／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Beyond Recycling", "wordcount": 96,
     "paras": [
        "Recycling once seemed like the final answer to our waste problem. "
        "Yet most materials can be reused only a limited number of times before their quality [[b:41]]. "
        "When old bottles are melted down, for instance, the plastic grows weaker and is eventually [[b:42]] away. "
        "A circular economy sets a higher goal: to keep products, parts, and raw materials in use for as long as possible. "
        "[[b:43]] "
        "Rather than buying a new phone every year, we might repair it, upgrade a single part, "
        "or return it so its metals can be turned into something else.",
     ]},
    {"label": "文2", "title": "The Sleeping Student", "wordcount": 103,
     "paras": [
        "Pulling an all-nighter before an exam feels productive, but it often [[b:44]] the very memory it is meant to build. "
        "Sleep is not wasted time; it is when the brain quietly files what we have learned. "
        "During deep sleep, the brain replays the day's lessons and moves them into long-term storage. "
        "Skip that stage, and the new information never becomes [[b:45]]. "
        "[[b:46]] "
        "In one careful study, students who slept after studying recalled far more the next morning "
        "than those who stayed awake all night. "
        "Rest, it turns out, is not the opposite of work; it is a hidden part of learning.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["declines","rises","returns","spreads"],"answer":"ア",
     "basis":"直前 <span class='en'>reused only a limited number of times before their quality ( )</span>。"
             "『限られた回数しか再利用できず、その前に品質が〜する』。次文の <span class='en'>grows weaker</span>（弱くなる）が具体化。",
     "solve":"<span class='en'>quality</span> が主語で、再利用の回数に限界がある文脈＝品質は<b>下がる</b>方向。"
             "<span class='en'>declines</span>（低下する）が一意。",
     "cut":"<span class='en'>rises</span>（上昇）は逆向き。<span class='en'>returns / spreads</span> は品質の変化として不自然。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["thrown","given","put","taken"],"answer":"ア",
     "basis":"<span class='en'>the plastic grows weaker and is eventually ( ) away</span>。弱くなった末の結末。",
     "solve":"<span class='en'>( ) away</span>＝『捨てられる』。<span class='en'>throw away</span>（廃棄する）のコロケーション。"
             "品質低下→最後は廃棄、という論理に一致。",
     "cut":"<span class='en'>given / put / taken</span> は <span class='en'>away</span> と結んでも『廃棄』の意味にならず文脈に合わない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "In everyday life, this changes how we treat the things we already own.",
       "As a result, recycling itself becomes completely unnecessary.",
       "This is why the cheapest goods will always win the market.",
       "So far, no business has been willing to try such ideas."],"answer":"ア",
     "basis":"空所前＝『製品や素材をできるだけ長く使い続ける』という循環経済の<b>一般原則</b>。"
             "空所後＝『新品を買う代わりに修理し、部品を交換し、金属を作り替える』という<b>具体例</b>。",
     "solve":"空所は<b>一般化→具体例</b>の橋渡し。直後の身近な行動の話につなぐ『日常で持ち物の扱い方が変わる』が最適。",
     "cut":"『リサイクルが不要になる』『最安の品が勝つ』は本文の趣旨とずれ、"
           "『どの企業も試していない』は直後の具体例と矛盾する。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["weakens","strengthens","builds","protects"],"answer":"ア",
     "basis":"<span class='en'>feels productive, but it often ( ) the very memory it is meant to build</span>。"
             "逆接 <span class='en'>but</span> が『生産的に感じるが実は逆』を示す。",
     "solve":"『築くはずの記憶を』＋逆接＝記憶を<b>弱める</b>。<span class='en'>weakens</span> が一意。",
     "cut":"<span class='en'>strengthens / builds / protects</span> はいずれも<b>強める</b>方向で、逆接 <span class='en'>but</span> と噛み合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["permanent","useless","visible","cheaper"],"answer":"ア",
     "basis":"直前 <span class='en'>moves them into long-term storage</span>。"
             "その段階を飛ばすと <span class='en'>the new information never becomes ( )</span>。",
     "solve":"深い睡眠で長期記憶に移す→それを省けば情報は<b>定着しない</b>。"
             "<span class='en'>long-term storage</span> と対応して <span class='en'>permanent</span>（永続的）。",
     "cut":"<span class='en'>useless / visible / cheaper</span> は長期記憶への定着という文脈と無関係。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "Researchers have measured this effect in the laboratory.",
       "Fortunately, memory has nothing to do with sleep.",
       "This is why students should study straight through the night.",
       "No experiment has ever supported such a claim."],"answer":"ア",
     "basis":"空所前＝『睡眠を省くと記憶は定着しない』という<b>主張</b>。"
             "空所後＝『ある研究では、勉強後に眠った学生の方がよく覚えていた』という<b>実験の証拠</b>。",
     "solve":"空所は<b>主張→根拠（実験）</b>の橋渡し。直後の研究へつなぐ『研究者がこの効果を実験室で測定した』が最適。",
     "cut":"『記憶は睡眠と無関係』『徹夜で勉強すべき』は主張と逆、"
           "『支持した実験はない』は直後で研究が示される流れと矛盾する。"},
  ],
  "trans": [
    ("文1", "リサイクルはかつて廃棄物問題の最終的な答えのように見えた。だが、ほとんどの素材は品質が<b>低下する</b>前に、"
            "限られた回数しか再利用できない。たとえば古い瓶を溶かすと、プラスチックは弱くなり、やがて<b>捨てられて</b>しまう。"
            "循環経済はより高い目標を掲げる――製品や部品、原材料をできるだけ長く使い続けることだ。"
            "<b>日常生活では、これはすでに持っている物の扱い方を変える。</b>"
            "毎年新しいスマホを買う代わりに、修理したり、部品を一つ交換したり、返却して金属を別の物に作り替えたりできる。"),
    ("文2", "試験前の徹夜は生産的に感じられるが、実際には築くはずの記憶をしばしば<b>弱めて</b>しまう。"
            "睡眠は無駄な時間ではなく、脳が学んだことを静かに整理する時間なのだ。"
            "深い睡眠の間、脳はその日の学習を再生し、長期記憶へと移す。"
            "その段階を飛ばせば、新しい情報は決して<b>永続的</b>にならない。"
            "<b>研究者はこの効果を実験室で測定してきた。</b>"
            "ある入念な研究では、勉強後に眠った学生は、徹夜した学生よりも翌朝はるかに多くを思い出した。"
            "休息は、実は仕事の反対ではなく、学習の隠れた一部なのだ。"),
  ],
  "vocab": [
    ("reuse", "動", "再利用する"),
    ("circular economy", "名", "循環経済"),
    ("raw material", "名", "原材料"),
    ("all-nighter", "名", "徹夜(の勉強)"),
    ("long-term", "形", "長期の"),
    ("permanent", "形", "永続的な、恒久的な"),
    ("recall", "動", "思い出す、想起する"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で決める――"
    "<span class='en'>quality declines / throw away / becomes permanent</span> のように相方の語と論理の矢印を確認する。"
    "文選択空所（43・46）は<b>前後の論理（一般化→具体例／主張→根拠）</b>で一意化し、代入して音読で検証する。",
}
