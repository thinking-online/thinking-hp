# -*- coding: utf-8 -*-
"""大問Ⅳ SET 08 ― 短文2本・空所6（語彙4＋文選択2）。
文1=観光と文化財保護（文化）、文2=都市のヒートアイランド（科学／社会）。
本文タグ: [[b:N]]=空所(設問N)。"""

SET = {
  "theme": "観光と文化財保護 ＆ 都市のヒートアイランド",
  "genre": "文化／科学・社会 短文2本",
  "limit": "目標7分",
  "texts": [
    {"label": "文1", "title": "Loving Old Places to Death", "wordcount": 100,
     "paras": [
        "Every year, millions of visitors flock to ancient temples, old castles, and historic city centres. "
        "Tourism brings welcome income, yet it can also [[b:41]] the very sites people come to admire. "
        "Crowds slowly wear down old stone steps, and constant camera flashes fade delicate wall paintings. "
        "[[b:43]] For this reason, some cities now limit daily ticket numbers and charge a small fee for [[b:42]]. "
        "The money is spent on careful repairs and regular cleaning, so that future generations can enjoy the same treasures. "
        "Handled wisely, visitors and heritage need not be enemies.",
     ]},
    {"label": "文2", "title": "Why Cities Stay Hot", "wordcount": 100,
     "paras": [
        "On summer nights, city centres often stay far warmer than the fields and countryside around them. "
        "Concrete and asphalt [[b:44]] heat during the day and release it slowly after dark. "
        "This effect, known as the urban heat island, can raise night-time temperatures by several degrees. "
        "[[b:46]] Trees and parks cool the surrounding air by providing shade and slowly releasing moisture. "
        "For this reason, planners are adding green [[b:45]] to rooftops and streets. "
        "A city with more plants is not only prettier but also healthier and much cheaper to keep cool.",
     ]},
  ],
  "questions": [
    {"no":41,"tag":"語彙空所","stem":"空所(41)に入る最も適切な語を選べ。","inline":True,
     "choices":["damage","protect","measure","invite"],"answer":"ア",
     "basis":"直前 <span class='en'>Tourism brings welcome income, yet it can also ( ) the very sites</span>。"
             "<span class='en'>yet</span>（しかし）で収入という利点と<b>逆向き</b>の内容が来る。",
     "solve":"次文が『石段をすり減らし壁画を色あせさせる』＝害の具体例。ゆえに『（場所を）<b>損なう</b>』＝<span class='en'>damage</span>。",
     "cut":"<span class='en'>protect</span>（守る）は <span class='en'>yet</span> の逆接に合わず正反対。"
            "<span class='en'>measure / invite</span> は目的語 <span class='en'>the very sites</span> と噛み合わない。"},
    {"no":42,"tag":"語彙空所","stem":"空所(42)に入る最も適切な語を選べ。","inline":True,
     "choices":["conservation","advertising","transport","parking"],"answer":"ア",
     "basis":"<span class='en'>charge a small fee for ( )</span>。直後の文が『その資金は修復と清掃に充てられる』と説明。",
     "solve":"料金の使い道が『修復・清掃』＝文化財の<b>保全</b>。<span class='en'>a fee for conservation</span> が文脈と一致。",
     "cut":"<span class='en'>advertising / transport / parking</span> は『修復に使う』という直後の説明と結びつかない。"},
    {"no":43,"tag":"文選択空所","stem":"空所(43)に入る最も適切な文を選べ。",
     "choices":[
       "The result is a slow but real threat to fragile monuments.",
       "Fortunately, such visits leave no mark on the buildings at all.",
       "As a result, tourists gradually lose all interest in old sites.",
       "Most of these famous temples were actually built for tourists."],"answer":"ア",
     "basis":"空所前＝『群衆が石段をすり減らし、フラッシュが壁画を色あせさせる』（被害の描写）。"
             "空所後＝<span class='en'>For this reason, some cities now limit ...</span>（そのための対策）。",
     "solve":"空所は<b>被害→まとめ（脅威）</b>の橋渡し。直後が『だから制限する』なので『もろい記念物への現実の脅威』が接続。",
     "cut":"『跡を残さない』は被害の描写と矛盾。『観光客が興味を失う』は話題がずれ、直後の対策につながらない。"
            "『観光客のために建てられた』は史実として無関係。"},
    {"no":44,"tag":"語彙空所","stem":"空所(44)に入る最も適切な語を選べ。","inline":True,
     "choices":["absorb","reflect","waste","block"],"answer":"ア",
     "basis":"<span class='en'>Concrete and asphalt ( ) heat during the day and release it slowly after dark</span>。"
             "<span class='en'>and release it</span>（後で放出する）と対。",
     "solve":"『日中に取り込み、夜に放出』の流れ。取り込む＝<b>吸収する</b>＝<span class='en'>absorb</span>。",
     "cut":"<span class='en'>reflect</span>（反射）は熱を溜めず放出とつながらず逆。"
            "<span class='en'>waste / block</span> は <span class='en'>release it</span> と論理が合わない。"},
    {"no":45,"tag":"語彙空所","stem":"空所(45)に入る最も適切な語を選べ。","inline":True,
     "choices":["spaces","noise","waste","fees"],"answer":"ア",
     "basis":"<span class='en'>planners are adding green ( ) to rooftops and streets</span>。"
             "前文で『樹木や公園が空気を冷やす』と述べる。",
     "solve":"<span class='en'>green ( )</span>＝<b>緑地</b>＝<span class='en'>green spaces</span>。冷却策としての公園・草木と一致。",
     "cut":"<span class='en'>green noise / green waste / green fees</span> はいずれも意味を成さず、冷却の文脈に合わない。"},
    {"no":46,"tag":"文選択空所","stem":"空所(46)に入る最も適切な文を選べ。",
     "choices":[
       "One simple remedy is to bring more greenery into the city.",
       "Luckily, tall concrete towers help the night air cool down fast.",
       "This is why deserts stay cooler than forests after sunset.",
       "City residents rarely notice any change in temperature."],"answer":"ア",
     "basis":"空所前＝『ヒートアイランドで夜間気温が数度上がる』（問題）。"
             "空所後＝<span class='en'>Trees and parks cool the surrounding air ...</span>（緑による冷却の説明）。",
     "solve":"空所は<b>問題→対策</b>の橋渡し。直後が樹木・公園の効果なので『簡単な対策は都市に緑を増やすこと』が接続。",
     "cut":"『コンクリートの塔が冷やす』は熱を溜める本文と矛盾。『砂漠が森より涼しい』は無関係で誤り。"
            "『住民は気温変化に気づかない』は『数度上がる』と矛盾。"},
  ],
  "trans": [
    ("文1", "毎年、何百万もの観光客が古代の寺院や古城、歴史ある市街地に押し寄せる。観光は歓迎すべき収入をもたらすが、"
            "同時に人々が見に来るまさにその場所を<b>損なう</b>こともある。群衆は古い石段を少しずつすり減らし、"
            "絶え間ないカメラのフラッシュは繊細な壁画を色あせさせる。<b>その結果、もろい記念物への緩やかだが現実の脅威が生じる。</b>"
            "こうした理由から、今では一部の都市が一日の入場券数を制限し、<b>保全</b>のためにわずかな料金を課している。"
            "その資金は入念な修復と定期的な清掃に充てられ、将来の世代が同じ宝を楽しめるようにする。"
            "賢く管理すれば、観光客と文化遺産は敵同士である必要はない。"),
    ("文2", "夏の夜、都心はしばしば周囲の野原や田園よりはるかに暖かいままだ。コンクリートやアスファルトは日中に熱を"
            "<b>吸収し</b>、暗くなった後にゆっくりと放出する。都市のヒートアイランドとして知られるこの現象は、"
            "夜間の気温を数度上昇させることがある。<b>単純な対策の一つは、都市にもっと緑を取り入れることだ。</b>"
            "樹木や公園は日陰を作り、ゆっくりと水分を放出することで周囲の空気を冷やす。こうした理由から、"
            "都市計画者は屋上や街路に緑の<b>空間</b>を加えつつある。より多くの植物のある都市は、美しいだけでなく、"
            "より健康的で、涼しく保つのがずっと安上がりでもある。"),
  ],
  "vocab": [
    ("flock", "動", "群がって集まる"),
    ("heritage", "名", "文化遺産"),
    ("fragile", "形", "もろい、壊れやすい"),
    ("conservation", "名", "保全、保護"),
    ("absorb", "動", "吸収する"),
    ("moisture", "名", "水分、湿気"),
    ("greenery", "名", "緑、草木"),
  ],
  "lesson":
    "Ⅳは『空所を見たら接続を読む』。語彙空所（41・42・44・45）は<b>コロケ＋文脈の向き</b>で、"
    "文選択空所（43・46）は<b>前後の論理（問題→まとめ／問題→対策）</b>で決まる。"
    "<span class='en'>yet</span> や <span class='en'>For this reason</span> などの論理標識を先に押さえ、"
    "代入して前後を音読し、話が途切れない選択肢だけを残す。",
}
