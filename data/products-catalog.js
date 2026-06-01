/**
 * 問題集（完全攻略マニュアル）カタログ — 私立文系の志望学部のみ
 * status: "available" | "wip"  （wip = 2027年度版 作成中の枠）
 */
(function (global) {
  function wipFaculty(facultyJa) {
    return {
      id: facultyJa,
      facultyJa: facultyJa,
      status: "wip",
      tags: ["2027年度版", "作成中"],
      lead:
        "私立文系の志望学部向けに、過去問を徹底分析した完全攻略マニュアル（2027年度版）を制作中です。公開まで今しばらくお待ちください。",
    };
  }

  function wipList(names) {
    return names.map(wipFaculty);
  }

  /** 私立文系入試の対象学部のみ（理・工・医・歯・薬・農・建築・スポーツ科学等は除外） */
  var STD_LIBERAL_ARTS = [
    "法学部",
    "商学部",
    "政治経済学部",
    "文学部",
    "経済学部",
    "社会学部",
    "国際学部",
    "人間科学部",
    "総合政策学部",
  ];

  var CATALOG = {
    groups: [
      { id: "waseda-keio", labelJa: "早慶", labelEn: "Waseda & Keio", universityIds: ["waseda", "keio"] },
      { id: "gmarch", labelJa: "G MARCH", labelEn: "G-MARCH", universityIds: ["meiji", "aoyama", "gakushuin", "chuo", "hosei"] },
      {
        id: "kankan",
        labelJa: "関関同立",
        labelEn: "Kansai Big Four",
        universityIds: ["kandai", "kangaku", "doshisha", "ritsumeikan"],
      },
      {
        id: "ssei",
        labelJa: "成成明学獨國武",
        labelEn: "Sei-sei-mei-gaku-doku-koku-bu",
        universityIds: ["seikei", "seijo", "meijigakuin", "dokkyo", "kokugakuin", "musashi"],
      },
      { id: "nitto", labelJa: "日東駒専", labelEn: "Nitto-koma-sen", universityIds: ["nihon", "toyo", "komazawa", "senshu"] },
      {
        id: "sankin",
        labelJa: "産近甲龍",
        labelEn: "Sankin-ko-ryu",
        universityIds: ["kyosan", "kindai", "konan", "ryukoku"],
      },
    ],
    universities: {
      waseda: {
        id: "waseda",
        name: "早稲田大学",
        searchKeys: "早稲田 waseda ワセダ わせだ",
        manuals: wipList([
          "政治経済学部",
          "法学部",
          "文化構想学部",
          "文学部",
          "教育学部",
          "商学部",
          "社会科学部",
          "人間科学部",
          "国際教養学部",
        ]),
      },
      keio: {
        id: "keio",
        name: "慶應義塾大学",
        searchKeys: "慶應 keio ケイオウ けいおう",
        manuals: wipList([
          "文学部",
          "経済学部",
          "法学部",
          "商学部",
          "総合政策学部",
          "環境情報学部",
        ]),
      },
      meiji: {
        id: "meiji",
        name: "明治大学",
        searchKeys: "明治 meiji メイジ めいじ gmarch g march",
        manuals: wipList([
          "法学部",
          "商学部",
          "政治経済学部",
          "文学部",
          "経営学部",
          "情報コミュニケーション学部",
          "国際日本学部",
        ]),
      },
      aoyama: {
        id: "aoyama",
        name: "青山学院大学",
        searchKeys: "青山 aoyama アオヤマ あおやま gmarch g march",
        manuals: wipList([
          "文学部",
          "教育人間科学部",
          "法学部",
          "経済学部",
          "経営学部",
          "国際政治経済学部",
          "総合文化政策学部",
          "社会情報学部",
          "地球社会共生学部",
        ]),
      },
      chuo: {
        id: "chuo",
        name: "中央大学",
        searchKeys: "中央 chuo チュウオウ gmarch g march",
        manuals: wipList([
          "法学部",
          "経済学部",
          "商学部",
          "総合政策学部",
          "国際情報学部",
          "文学部",
        ]),
      },
      hosei: {
        id: "hosei",
        name: "法政大学",
        searchKeys: "法政 hosei ホウセイ gmarch g march",
        manuals: wipList([
          "法学部",
          "文学部",
          "経営学部",
          "国際文化学部",
          "人間環境学部",
          "キャリアデザイン学部",
          "経済学部",
          "社会学部",
          "現代福祉学部",
        ]),
      },
      kandai: {
        id: "kandai",
        name: "関西大学",
        searchKeys: "関大 関西大学 kandai",
        manuals: wipList(STD_LIBERAL_ARTS),
      },
      kangaku: {
        id: "kangaku",
        name: "関西学院大学",
        searchKeys: "関学 kangaku カンガク 関西学院",
        manuals: [
          {
            id: "kangaku-21-english",
            facultyJa: "2/1試験（英語）",
            status: "available",
            href: "/product-kangaku-english",
            img: "assets/kangaku-hero.png",
            tags: ["2027年度最新版", "販売中"],
            price: "¥19,800",
            priceLabel: "〜（早期割）",
            lead:
              "関学の英語専門。関西学院大学2/1試験向け。大問別問題集90題・頻出180語・模試付き。過去5年を大問別に分析。",
          },
        ].concat(
          wipList([
            "神学部",
            "文学部",
            "社会学部",
            "法学部",
            "経済学部",
            "商学部",
            "人間福祉学部",
            "国際学部",
            "教育学部",
            "総合政策学部",
          ])
        ),
      },
      doshisha: {
        id: "doshisha",
        name: "同志社大学",
        searchKeys: "同志社 doshisha ドウシシャ",
        manuals: wipList(STD_LIBERAL_ARTS),
      },
      ritsumeikan: {
        id: "ritsumeikan",
        name: "立命館大学",
        searchKeys: "立命館 ritsumeikan リツメイカン",
        manuals: wipList(STD_LIBERAL_ARTS),
      },
      seikei: {
        id: "seikei",
        name: "成蹊大学",
        searchKeys: "成蹊 seikei セイケイ",
        manuals: wipList(["経済学部", "経営学部", "法学部", "文学部"]),
      },
      seijo: {
        id: "seijo",
        name: "成城大学",
        searchKeys: "成城 seijo セイジョウ",
        manuals: wipList(["経済学部", "法学部", "文学部"]),
      },
      meijigakuin: {
        id: "meijigakuin",
        name: "明治学院大学",
        searchKeys: "明学 meijigakuin メイジガクイン",
        manuals: wipList(["文学部", "経済学部", "社会学部", "法学部", "国際学部", "心理学部"]),
      },
      gakushuin: {
        id: "gakushuin",
        name: "学習院大学",
        searchKeys: "学習院 gakushuin ガクシュウイン gmarch g march",
        manuals: wipList(["法学部", "政治経済学部", "文学部", "国際教育学部"]),
      },
      dokkyo: {
        id: "dokkyo",
        name: "獨協大学",
        searchKeys: "獨協 dokkyo ドッキョウ",
        manuals: wipList(["法学部", "経済学部", "外国語学部", "国際教養学部"]),
      },
      kokugakuin: {
        id: "kokugakuin",
        name: "國學院大學",
        searchKeys: "國學院 kokugakuin コクガクイン",
        manuals: wipList(["文学部", "神道文化学部", "法学部", "経済学部"]),
      },
      musashi: {
        id: "musashi",
        name: "武蔵大学",
        searchKeys: "武蔵 musashi ムサシ",
        manuals: wipList(["人間情報学部", "教育学部", "法学部", "経済学部"]),
      },
      nihon: {
        id: "nihon",
        name: "日本大学",
        searchKeys: "日大 nihon ニホン 日本大学",
        manuals: wipList([
          "法学部",
          "文理学部",
          "経済学部",
          "商学部",
          "芸術学部",
          "国際関係学部",
          "危機管理学部",
        ]),
      },
      toyo: {
        id: "toyo",
        name: "東洋大学",
        searchKeys: "東洋 toyo トウヨウ",
        manuals: wipList([
          "文学部",
          "経済学部",
          "経営学部",
          "法学部",
          "社会学部",
          "国際学部",
          "国際観光学部",
          "福祉社会デザイン学部",
          "総合情報学部",
        ]),
      },
      komazawa: {
        id: "komazawa",
        name: "駒澤大学",
        searchKeys: "駒澤 komazawa コマザワ",
        manuals: wipList(["仏教学部", "文学部", "経済学部", "法学部", "経営学部"]),
      },
      senshu: {
        id: "senshu",
        name: "専修大学",
        searchKeys: "専修 senshu センシュウ",
        manuals: wipList(["法学部", "経済学部", "文学部", "商学部", "ネットワーク情報学部", "人間科学部"]),
      },
      kyosan: {
        id: "kyosan",
        name: "京都産業大学",
        searchKeys: "京産 kyosan キョウサン 京都産業",
        manuals: wipList(["経済学部", "法学部", "外国語学部", "文化学部"]),
      },
      kindai: {
        id: "kindai",
        name: "近畿大学",
        searchKeys: "近大 kindai キンダイ 近畿大学",
        manuals: wipList([
          "法学部",
          "経済学部",
          "経営学部",
          "文学部",
          "商学部",
          "総合社会学部",
        ]),
      },
      konan: {
        id: "konan",
        name: "甲南大学",
        searchKeys: "甲南 konan コウナン",
        manuals: wipList(["文学部", "経済学部", "法学部", "経営学部"]),
      },
      ryukoku: {
        id: "ryukoku",
        name: "龍谷大学",
        searchKeys: "龍谷 ryukoku リュウコク",
        manuals: wipList(["文学部", "経済学部", "経営学部", "法学部", "政策学部", "国際文化学部"]),
      },
    },
  };

  global.PRODUCTS_MANUAL_CATALOG = CATALOG;
})(typeof window !== "undefined" ? window : this);
