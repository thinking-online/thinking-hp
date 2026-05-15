/**
 * 合格者インタビュー — 旧 Interview NN の動画・サムネを引き継ぎつつ No.01–10 を再構成
 */
(function (global) {
  const OLD = {
    1: {
      id: "8R0aILkSbhc",
      thumb: "assets/thumb-aboshi.png",
      tag: "現役合格 / 高3春から",
      quote:
        "条文を覚えるのではなく、論理を読む。学部別の戦略があるから、毎日の勉強に迷いがなくなった。",
      story:
        "高3の春、模試の判定はDだった。法学部志望と決めた瞬間から、コーチは「論理構成」と「要約力」だけに焦点を絞ってくれた。日々のSlack報告と週次面談で、自分の弱点が可視化されていった。",
    },
    2: {
      id: "Qp17tvgggOQ",
      thumb: "assets/thumb-matsuyama.png",
      tag: "親子インタビュー / 現役合格",
      quote:
        "高3の秋、E判定から親子で号泣した。それでも設計を崩さなければ、MARCH全勝は現実になる。",
      story:
        "判定が落ち込むたびに、志望学部ごとの優先順位を組み直してくれた。親子で振り返りながら、最後まで走り切れた。",
    },
    3: {
      id: "e5OzmZKSe28",
      thumb: "assets/thumb-march.png",
      tag: "偏差値39 → 複数合格",
      quote: "全落ちからでも、学部別に正しく逆算すれば、複数校合格は狙える。",
      story:
        "一度は全落ちしたが、出願校ごとに必要な力だけに絞り直した。関学・法政・中央と、道が開けていった。",
    },
    4: {
      id: "HP_5tDBODaY",
      thumb: "assets/thumb-toyama.jpg",
      tag: "週7部活 / 偏差値62",
      quote: "最下位層からでも、正しい順序で積み上げれば、学年の上位に食い込める。",
      story:
        "部活と両立しながら、志望学部の出題傾向に合わせて演習量を調整。関西学院大学への現役合格を掴んだ。",
    },
    5: {
      id: "NwrlH_tyukA",
      thumb: "assets/thumb-nakamura.png",
      tag: "英語特化 / 推薦も併願",
      quote: "推薦と一般、両方の戦略を最後まで諦めずに走らせてくれた。一人では絶対に無理だった。",
      story:
        "学校推薦と一般、両方狙うのは無謀と言われた。でもコーチは「両立できる時間配分」を緻密に組んでくれた。結果、第一志望に推薦合格できた。",
    },
    6: {
      id: "Rseh2QY53xQ",
      tag: "国語論理 / 偏差値+18",
      quote: "国語の論理構造を初めてちゃんと理解できた。読み方が変わると、現代文の点数は本当に安定する。",
      story:
        "現代文は「センス」と諦めかけていた。でもコーチに「論理を追う技術」を教わってから、得点が安定した。最後の模試では偏差値が18上がっていた。",
    },
    7: {
      id: "6vRUDEt9aFc",
      tag: "学部別戦略 / 個別最適",
      quote: "学部別の戦略は、こんなに違うのかと衝撃を受けた。同じ大学でも、学部によって全く違う対策が必要だった。",
      story:
        "「同じ大学なら対策は同じ」と思っていた自分が恥ずかしい。学部別の出題傾向を分析してもらい、その学部の問題だけに最適化した。",
    },
    8: {
      id: "bcYQYTCSs8o",
      tag: "添削の質 / 24h質問対応",
      quote: "添削の質が違う。返却が早く、改善点が明確。Slackでいつでも質問できる安心感が、最後まで支えてくれた。",
      story:
        "夜中に詰まった時も、翌朝にはコーチからの返信が届いていた。一人じゃない、という感覚が、最後の追い込み期に何より大きかった。",
    },
    9: {
      id: "Xid8x7UUJfE",
      thumb: "assets/thumb-sokei-zensho.png",
      tag: "偏差値60未満 / 非進学校",
      quote: "偏差値60未満の環境からでも、学部別で正しく逆算すれば、合格は狙えると証明できた。",
      story:
        "学校内では上位ではなかったが、志望学部の出題傾向に絞って学習を再設計。対談では、迷っていた時期から合格までの道筋を振り返っている。",
    },
    10: {
      id: "CcwIX4-j2Mo",
      thumb: "assets/thumb-aoyama-geneki.png",
      tag: "E判定 / 学年ビリ / 高3秋まで部活",
      quote: "E判定と学年ビリからでも、最後まで設計を崩さなければ逆転できる。",
      story:
        "高3の11月まで部活を続けながら、限られた時間で学習優先順位を徹底。対談では、逆転合格までの具体的な行動と心境の変化を話している。",
    },
  };

  function fromOld(no, school, year, extra) {
    const o = OLD[no];
    return {
      id: o.id,
      thumb: o.thumb,
      tag: o.tag,
      quote: o.quote,
      story: o.story,
      school,
      year: year || "現役合格",
      ...extra,
    };
  }

  const HEADLINES = {
    "01": "早慶に、現役全勝。",
    "02": "E判定・学年ビリから、逆転現役合格。",
    "03": "早稲田文学部を、現役で掴む。",
    "04": "高3秋・E判定から、MARCH全勝。",
    "05": "最下位層から、関学現役合格。",
    "06": "推薦と一般、両方の戦略で立教へ。",
    "07": "国語論理で、明治学院大学へ。",
    "08": "学部別戦略で、明治大学へ。",
    "09": "複数校に、同時合格。",
    "10": "非進学校から、関学現役合格。",
  };

  const VOICE_INTERVIEWS = [
    {
      no: "01",
      name: "合格者インタビュー01",
      en: "Interview 01",
      headline: HEADLINES["01"],
      ...fromOld(9, "早稲田・慶應全勝"),
    },
    {
      no: "02",
      name: "合格者インタビュー02",
      en: "Interview 02",
      headline: HEADLINES["02"],
      ...fromOld(10, "青山学院大学"),
    },
    {
      no: "03",
      name: "合格者インタビュー03",
      en: "Interview 03",
      school: "早稲田文学部",
      year: "現役合格",
      headline: HEADLINES["03"],
      pending: true,
      tag: "準備中",
      quote: "公開準備中のインタビューです。",
      story: "早稲田文学部合格の対談動画は、近日公開予定です。",
    },
    {
      no: "04",
      name: "合格者インタビュー04",
      en: "Interview 04",
      headline: HEADLINES["04"],
      ...fromOld(3, "MARCH全勝"),
    },
    {
      no: "05",
      name: "合格者インタビュー05",
      en: "Interview 05",
      headline: HEADLINES["05"],
      ...fromOld(4, "関西学院大学"),
    },
    {
      no: "06",
      name: "合格者インタビュー06",
      en: "Interview 06",
      headline: HEADLINES["06"],
      ...fromOld(5, "立教大学"),
    },
    {
      no: "07",
      name: "合格者インタビュー07",
      en: "Interview 07",
      headline: HEADLINES["07"],
      ...fromOld(6, "明治学院大学"),
    },
    {
      no: "08",
      name: "合格者インタビュー08",
      en: "Interview 08",
      headline: HEADLINES["08"],
      ...fromOld(7, "明治大学"),
    },
    {
      no: "09",
      name: "合格者インタビュー09",
      en: "Interview 09",
      headline: HEADLINES["09"],
      ...fromOld(8, "中央・法政・関西学院"),
    },
    {
      no: "10",
      name: "合格者インタビュー10",
      en: "Interview 10",
      headline: HEADLINES["10"],
      ...fromOld(9, "関西学院大学"),
    },
  ];

  global.VOICE_INTERVIEWS = VOICE_INTERVIEWS;
})(typeof window !== "undefined" ? window : global);
