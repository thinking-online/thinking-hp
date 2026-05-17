/**
 * 合格者インタビュー No.01–10（動画URL・サムネイル対応表）
 */
(function (global) {
  const VOICE_INTERVIEWS = [
    {
      no: "01",
      name: "合格者インタビュー01",
      en: "Interview 01",
      school: "早稲田・慶應全勝",
      year: "現役合格",
      id: "Xid8x7UUJfE",
      thumb: "assets/thumb-interview-01.png",
      headline: "早慶に、現役全勝。",
      tag: "偏差値60未満 / 非進学校",
      quote: "偏差値60未満の環境からでも、学部別で正しく逆算すれば、合格は狙えると証明できた。",
      story:
        "学校内では上位ではなかったが、志望学部の出題傾向に絞って学習を再設計。対談では、迷っていた時期から合格までの道筋を振り返っている。",
    },
    {
      no: "02",
      name: "合格者インタビュー02",
      en: "Interview 02",
      school: "青山学院大学",
      year: "現役合格",
      id: "CcwIX4-j2Mo",
      thumb: "assets/thumb-interview-02.png",
      headline: "E判定・学年ビリから、逆転現役合格。",
      tag: "E判定 / 学年ビリ / 高3秋まで部活",
      quote: "E判定と学年ビリからでも、最後まで設計を崩さなければ逆転できる。",
      story:
        "高3の11月まで部活を続けながら、限られた時間で学習優先順位を徹底。対談では、逆転合格までの具体的な行動と心境の変化を話している。",
    },
    {
      no: "03",
      name: "合格者インタビュー03",
      en: "Interview 03",
      school: "早稲田文学部",
      year: "現役合格",
      id: "Rj-lETyecvw",
      thumb: "assets/thumb-interview-03.png",
      headline: "早稲田文学部を、現役で掴む。",
      tag: "E判定 / 早稲田文学部",
      quote: "E判定からでも、学部別に正しく逆算すれば、早稲田文学部は狙える。",
      story:
        "高3の夏、過去問の正答率は30%未満だった。文学部志望に絞って学習を再設計し、現役で早稲田大学文学部に合格した。",
    },
    {
      no: "04",
      name: "合格者インタビュー04",
      en: "Interview 04",
      school: "MARCH全勝",
      year: "現役合格",
      id: "8R0aILkSbhc",
      thumb: "assets/thumb-interview-04.png",
      headline: "高3秋・E判定から、MARCH全勝。",
      tag: "親子インタビュー / 現役合格",
      quote: "高3の秋、E判定から親子で号泣した。それでも設計を崩さなければ、MARCH全勝は現実になる。",
      story:
        "判定が落ち込むたびに、志望学部ごとの優先順位を組み直してくれた。親子で振り返りながら、最後まで走り切れた。",
    },
    {
      no: "05",
      name: "合格者インタビュー05",
      en: "Interview 05",
      school: "関西学院大学",
      year: "現役合格",
      id: "Qp17tvgggOQ",
      thumb: "assets/thumb-interview-05.png",
      headline: "最下位層から、関学現役合格。",
      tag: "週7部活 / 偏差値62",
      quote: "最下位層からでも、正しい順序で積み上げれば、学年の上位に食い込める。",
      story:
        "部活と両立しながら、志望学部の出題傾向に合わせて演習量を調整。関西学院大学への現役合格を掴んだ。",
    },
    {
      no: "06",
      name: "合格者インタビュー06",
      en: "Interview 06",
      school: "立教大学",
      year: "現役合格",
      id: "e5OzmZKSe28",
      thumb: "assets/thumb-interview-06.png",
      headline: "ブラック部活から、立教現役合格。",
      tag: "偏差値45→65 / テニス部",
      quote: "部活で忙しくても、合格設計を崩さなければ、立教への現役合格は現実になる。",
      story:
        "週6〜7の部活と学習の両立は無理だと言われたが、コーチが時間配分を組み直してくれた。偏差値が上がり、第一志望に現役合格できた。",
    },
    {
      no: "07",
      name: "合格者インタビュー07",
      en: "Interview 07",
      school: "明治学院大学",
      year: "現役合格",
      id: "HP_5tDBODaY",
      thumb: "assets/thumb-interview-07.png",
      headline: "バイトしながら、明治学院へ。",
      tag: "指定校推薦 / 面接対策",
      quote: "バイトと部活の合間でも、面接対策を徹底すれば、指定校推薦は勝てる。",
      story:
        "限られた時間の中で、志望学部に必要な力だけに絞った。面接の型を一緒に作り、明治学院大学に現役合格した。",
    },
    {
      no: "08",
      name: "合格者インタビュー08",
      en: "Interview 08",
      school: "明治大学",
      year: "現役合格",
      id: "NwrlH_tyukA",
      thumb: "assets/thumb-interview-08.png",
      headline: "定期テスト以外「勉強」ゼロから、明治文学部へ。",
      tag: "MARCH全勝 / 文学部",
      quote: "勉強時間が少なくても、学部別に正しく設計すれば、明治大学文学部は狙える。",
      story:
        "定期テスト以外はほとんど勉強していなかったが、志望学部の出題傾向に合わせて演習を再設計。現役で明治大学文学部に合格した。",
    },
    {
      no: "09",
      name: "合格者インタビュー09",
      en: "Interview 09",
      school: "中央・法政・関西学院",
      year: "合格",
      id: "Rseh2QY53xQ",
      thumb: "assets/thumb-interview-09.png",
      headline: "全落ちから、複数校合格。",
      tag: "偏差値39 → 複数合格",
      quote: "全落ちからでも、学部別に正しく逆算すれば、複数校合格は狙える。",
      story:
        "一度は全落ちしたが、出願校ごとに必要な力だけに絞り直した。関学・法政・中央と、道が開けていった。",
    },
    {
      no: "10",
      name: "合格者インタビュー10",
      en: "Interview 10",
      school: "関西学院大学",
      year: "現役合格",
      id: "6vRUDEt9aFc",
      thumb: "assets/thumb-interview-10.png",
      headline: "英語48.2から、関学現役合格。",
      tag: "日本史県内1位 / 苦手克服",
      quote: "苦手な英語を克服すれば、関関同立への現役合格は十分に現実になる。",
      story:
        "英語の偏差値が伸び悩んでいた時期もあったが、志望校に必要な科目だけに絞って学習を再設計。日本史で県内1位を取り、関西学院大学に現役合格した。",
    },
  ];

  global.VOICE_INTERVIEWS = VOICE_INTERVIEWS;
})(typeof window !== "undefined" ? window : global);
