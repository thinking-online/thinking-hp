/**
 * 早稲田 得点調整シミュレーター用データ。
 *
 * 数値の出典は早稲田大学「一般選抜 学部別得点状況」（各年度の入試結果PDF）。
 *   https://www.waseda.jp/inst/admission/undergraduate/result/
 * average = 受験者平均点（素点）、minimum = 合格最低点（成績標準化後）。
 *
 * verified: 公式PDFと1件ずつ照合済みなら true。
 *   false の間はページに「確認中」と表示される。公開前に必ず照合して true にすること。
 *
 * 年度・方式を足すときは rows に1行追加するだけでよい。
 * 科目の max がその方式の配点と一致しない場合（配点換算がある方式）は載せない。
 */
(function (root) {
  "use strict";

  var DATA = {
    // 調整式: 満点の半分 + k ×（素点 − 受験者平均点）
    // 早稲田は式を公表していないため k は推定値。幅を持たせて表示する。
    coefficient: { low: 1.0, mid: 1.25, high: 1.5 },

    faculties: [
      {
        key: "shogaku",
        name: "商学部",
        methods: [
          {
            key: "chireki",
            name: "地歴・公民型",
            rows: [
              {
                year: 2026,
                verified: false,
                minimum: 130.3,
                total: 200,
                required: [
                  { name: "英語", max: 80, average: 33.55 },
                  { name: "国語", max: 60, average: 38.773 }
                ],
                electives: [
                  { name: "日本史", max: 60, average: 33.226 },
                  { name: "世界史", max: 60, average: 36.475 },
                  { name: "政治・経済", max: 60, average: 37.757 }
                ]
              },
              {
                year: 2025,
                verified: false,
                minimum: 129.95,
                total: 200,
                required: [
                  { name: "英語", max: 80, average: 36.688 },
                  { name: "国語", max: 60, average: 35.837 }
                ],
                electives: [
                  { name: "日本史", max: 60, average: 38.163 },
                  { name: "世界史", max: 60, average: 40.207 },
                  { name: "政治・経済", max: 60, average: 34.787 }
                ]
              },
              {
                year: 2024,
                verified: false,
                minimum: 128.7,
                total: 200,
                required: [
                  { name: "英語", max: 80, average: 30.601 },
                  { name: "国語", max: 60, average: 27.449 }
                ],
                electives: [
                  { name: "日本史", max: 60, average: 32.474 },
                  { name: "世界史", max: 60, average: 38.755 },
                  { name: "政治・経済", max: 60, average: 30.381 }
                ]
              }
            ]
          }
        ]
      }
    ]
  };

  if (typeof module !== "undefined" && module.exports) module.exports = DATA;
  else root.WASEDA_SCORE_DATA = DATA;
})(typeof window !== "undefined" ? window : globalThis);
