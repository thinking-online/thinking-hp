/**
 * 早稲田 得点調整シミュレーターの計算部分（画面に依存しない）。
 * node からも読めるので `node waseda-score/calc.test.js` で検算できる。
 */
(function (root) {
  "use strict";

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  /** 1科目の調整後得点。0〜満点に収める。 */
  function adjust(subject, raw, k) {
    return clamp(subject.max / 2 + k * (raw - subject.average), 0, subject.max);
  }

  /**
   * entries: [{ subject: {name,max,average}, raw: number }]
   * 係数 low / mid / high の3通りで合計を出し、合格最低点との関係を判定する。
   */
  function evaluate(entries, row, coefficient) {
    var ks = [coefficient.low, coefficient.mid, coefficient.high];
    var subjects = entries.map(function (entry) {
      var values = ks.map(function (k) { return adjust(entry.subject, entry.raw, k); });
      return {
        name: entry.subject.name,
        max: entry.subject.max,
        average: entry.subject.average,
        raw: entry.raw,
        mid: values[1],
        low: Math.min.apply(null, values),
        high: Math.max.apply(null, values)
      };
    });
    var totals = ks.map(function (k) {
      return entries.reduce(function (sum, entry) {
        return sum + adjust(entry.subject, entry.raw, k);
      }, 0);
    });
    var low = Math.min.apply(null, totals);
    var high = Math.max.apply(null, totals);
    var verdict = low >= row.minimum ? "above" : high < row.minimum ? "below" : "border";
    return {
      subjects: subjects,
      rawTotal: entries.reduce(function (sum, entry) { return sum + entry.raw; }, 0),
      mid: totals[1],
      low: low,
      high: high,
      minimum: row.minimum,
      diff: totals[1] - row.minimum,
      verdict: verdict
    };
  }

  var api = { adjust: adjust, evaluate: evaluate };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.WasedaScoreCalc = api;
})(typeof window !== "undefined" ? window : globalThis);
