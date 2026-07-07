# -*- coding: utf-8 -*-
"""大問Ⅳ SET 07 ― 短文2本・空所6（語彙4＋文選択2）。
本文タグ: [[b:N]]=空所(設問N)。文1=リモートワークと通勤／文2=カフェインと集中力。"""

SET = {
  "theme": "リモートワークと通勤 ＆ カフェインと集中",
  "genre": "社会／科学 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Working from Home", "wordcount": 100,
     "paras": [
        "For decades, a full office was the normal shape of working life, and long commutes were simply accepted as "
        "part of the deal. The pandemic changed that overnight. When millions began working from home, many found "
        "that the hours once [[b:41]] on crowded trains could be spent with family or on sleep instead. Cities felt "
        "the [[b:42]] almost at once: fewer commuters meant quieter roads, but also half-empty office towers and "
        "struggling shops that had relied on weekday crowds. [[b:43]] Today most firms are settling on a hybrid "
        "pattern, asking staff to come in person only two or three days a week.",
     ]},
    {"label": "文2", "title": "The Limits of Coffee", "wordcount": 101,
     "paras": [
        "Caffeine is the most widely used stimulant on the planet, and most of us meet it first thing in the morning. "
        "It works by blocking the brain chemical that makes us feel sleepy, so a single cup can sharpen [[b:44]] and "
        "lift a tired mood. But the benefit has clear limits. Beyond about two or three cups, extra caffeine rarely "
        "adds focus and instead [[b:45]] restlessness, a racing heart, and broken sleep the following night. [[b:46]] "
        "The key, researchers suggest, is moderation and timing: a modest dose early in the day helps, while a "
        "late-afternoon cup often does more harm than good.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["wasted","gained","hidden","planned"],"answer":"ア",
     "basis":"<span class='en'>the hours once ( ) on crowded trains could be spent with family or on sleep instead</span>。"
             "『満員電車で〜だった時間を、代わりに家族や睡眠に使える』という対比。",
     "solve":"<span class='en'>instead</span> が『無駄→有益』の転換を示す。満員電車で<b>浪費されていた</b>＝<span class='en'>wasted on</span> のコロケ。",
     "cut":"<span class='en'>gained</span>（得た）は <span class='en'>instead</span> の対比と逆。"
           "<span class='en'>hidden / planned</span> は <span class='en'>on crowded trains</span> と噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["impact","comfort","silence","profit"],"answer":"ア",
     "basis":"<span class='en'>Cities felt the ( ) almost at once</span>。コロン以降に『道は静かになったが、"
             "オフィスは半分空き、店は苦戦』と良悪両面の変化が続く。",
     "solve":"<span class='en'>feel the ( )</span> で、直後の良悪混在の変化を束ねるのは<b>影響</b>＝<span class='en'>impact</span>。",
     "cut":"<span class='en'>comfort / silence / profit</span> はいずれも一面的で、続く『苦戦する店』などの負の変化を含められない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "Neither a total return nor permanent home-working satisfied everyone.",
       "As a result, commuting vanished from working life forever.",
       "Employers quickly ordered all their staff back to the desk full time.",
       "Workers soon agreed that the office had lost all of its value."],"answer":"ア",
     "basis":"空所前＝在宅化の利点と、街の負の変化の両面。空所後＝<span class='en'>Today most firms are settling on a hybrid pattern</span>（折衷案）。",
     "solve":"空所は<b>問題→折衷案</b>の橋渡し。『完全復帰も完全在宅もどちらも皆を満足させなかった』が、次の<b>ハイブリッド</b>導入の理由になる。",
     "cut":"『通勤が永遠に消えた』『全員デスクに戻された』は <span class='en'>hybrid</span> と矛盾。"
           "『オフィスは価値を全て失った』も折衷案の導入と噛み合わない。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["attention","appetite","patience","silence"],"answer":"ア",
     "basis":"<span class='en'>a single cup can sharpen ( ) and lift a tired mood</span>。眠気を止める働きの直後で、良い効果を並べる。",
     "solve":"<span class='en'>sharpen ( )</span>＝『〜を鋭くする』。眠気を止めるので研ぎ澄まされるのは<b>注意力</b>＝<span class='en'>attention</span>。",
     "cut":"<span class='en'>appetite</span>（食欲）は <span class='en'>sharpen</span> と結びつくが眠気の話と無関係。"
           "<span class='en'>patience / silence</span> はカフェインの覚醒効果と噛み合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["triggers","cures","prevents","hides"],"answer":"ア",
     "basis":"<span class='en'>extra caffeine rarely adds focus and instead ( ) restlessness, a racing heart, and broken sleep</span>。"
             "『集中を増やさず、代わりに〜』と悪影響を並べる。",
     "solve":"<span class='en'>instead</span> の後は負の結果。落ち着きのなさや動悸を<b>引き起こす</b>＝<span class='en'>triggers</span>。",
     "cut":"<span class='en'>cures / prevents</span>（治す・防ぐ）は悪影響を並べる文脈と逆。"
           "<span class='en'>hides</span>（隠す）も『眠りが妨げられる』結果と矛盾。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "In short, more caffeine is not always better.",
       "For this reason, doctors advise drinking as much of it as possible.",
       "Sleep problems have nothing to do with what we choose to drink.",
       "Caffeine, in truth, has no measurable effect on the brain at all."],"answer":"ア",
     "basis":"空所前＝『量を増やしても集中は増えず、むしろ弊害』。空所後＝<span class='en'>The key ... is moderation and timing</span>（節度と時間帯が鍵）。",
     "solve":"空所は<b>要点のまとめ</b>。『要するに、多ければ良いわけではない』が前文を束ね、次の<b>節度</b>の助言へ自然に繋がる。",
     "cut":"『できるだけ多く飲め』は弊害の説明と逆。『睡眠問題は飲み物と無関係』は <span class='en'>broken sleep</span> と矛盾。"
           "『脳に全く効果なし』は覚醒作用の説明と矛盾。"},
  ],
  "trans": [
    ("文1", "何十年もの間、出社勤務が働き方の当たり前の形であり、長い通勤は取引の一部として当然に受け入れられていた。"
            "パンデミックはそれを一夜にして変えた。何百万もの人が在宅勤務を始めると、多くの人は、かつて満員電車で"
            "<b>浪費されていた</b>時間を、代わりに家族や睡眠に使えると気づいた。都市はその<b>影響</b>をすぐに感じた――"
            "通勤者が減って道は静かになったが、同時にオフィスビルは半分空き、平日の人出に頼っていた店は苦戦した。"
            "<b>完全な出社復帰も、恒久的な在宅勤務も、どちらも皆を満足させはしなかった。</b>今日、多くの企業は"
            "週に二、三日だけ出社を求めるハイブリッド型に落ち着きつつある。"),
    ("文2", "カフェインは地球上で最も広く使われる興奮剤であり、私たちの多くは朝一番にそれと出会う。眠気を感じさせる"
            "脳内物質を遮断することで働き、一杯で<b>注意力</b>を研ぎ澄まし、疲れた気分を持ち上げてくれる。だがその効用には"
            "明確な限界がある。二、三杯を超えると、余分なカフェインは集中をほとんど増やさず、代わりに落ち着きのなさや"
            "動悸、翌夜の途切れた眠りを<b>引き起こす</b>。<b>要するに、カフェインは多ければ良いというものではない。</b>"
            "鍵は節度と時間帯だと研究者は言う――一日の早い時間の控えめな量は役立つが、午後遅くの一杯はしばしば益より害が大きい。"),
  ],
  "vocab": [
    ("commute", "名／動", "通勤（する）"),
    ("hybrid", "形／名", "混合の、ハイブリッド"),
    ("struggling", "形", "苦戦している、あえいでいる"),
    ("stimulant", "名", "興奮剤、刺激物"),
    ("moderation", "名", "節度、適度"),
    ("restlessness", "名", "落ち着きのなさ、そわそわ"),
    ("dose", "名", "（薬などの）一回分の量"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋論理の向き</b>で決まり、"
    "<span class='en'>instead</span> のような対比語は『無駄→有益』『集中→弊害』の切り替えを教えてくれる。"
    "文選択空所（43・46）は<b>問題→折衷案</b>や<b>要点のまとめ</b>の型。代入して前後を音読し、話が途切れない1文を選ぶ。",
}
