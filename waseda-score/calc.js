/**
 * 早稲田 得点調整シミュレーターの計算部分（画面に依存しない）。
 * node からも読めるので `node waseda-score/calc.test.js` で検算できる。
 *
 * 科目ごとに2通りの換算がある。
 *   実測: subject.fit = { a, b, rmse, n } があるとき。 調整後 = a + b × 素点
 *         （成績開示と自己採点の組から /waseda-score/calibrate/ で求めた値）
 *   推定: fit がないとき。 調整後 = 満点の半分 + k ×（素点 − 受験者平均点）
 * どちらも「低め・中心・高め」の3本の線を持ち、結果は幅つきで出す。
 */
(function (root) {
  "use strict";

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  /** 科目の換算モデル。low/mid/high は素点 → 調整後得点の関数（単調増加）。 */
  function model(subject, coefficient) {
    var max = subject.max;
    if (subject.fit) {
      var f = subject.fit;
      // 実測でも自己採点の誤差が残るので、残差の2倍（最低1点）を幅にする
      var margin = Math.max(2 * (f.rmse || 0), 1);
      return {
        source: "measured",
        n: f.n,
        mid: function (raw) { return clamp(f.a + f.b * raw, 0, max); },
        low: function (raw) { return clamp(f.a + f.b * raw - margin, 0, max); },
        high: function (raw) { return clamp(f.a + f.b * raw + margin, 0, max); }
      };
    }
    var line = function (k) {
      return function (raw) { return clamp(max / 2 + k * (raw - subject.average), 0, max); };
    };
    var a = line(coefficient.low), m = line(coefficient.mid), b = line(coefficient.high);
    return {
      source: "estimated",
      n: 0,
      mid: m,
      low: function (raw) { return Math.min(a(raw), b(raw)); },
      high: function (raw) { return Math.max(a(raw), b(raw)); }
    };
  }

  /** 単調増加の fn について fn(x) >= target となる最小の x。届かなければ null。 */
  function solve(fn, target, lo, hi) {
    if (fn(hi) < target - 1e-9) return null;
    if (fn(lo) >= target) return lo;
    for (var i = 0; i < 60; i++) {
      var mid = (lo + hi) / 2;
      if (fn(mid) >= target) hi = mid; else lo = mid;
    }
    return hi;
  }

  /**
   * entries: [{ subject, raw }]（全科目入力済み）
   * 合計は科目ごとの低め同士・高め同士を足す（科目間で係数は独立と見る）。
   */
  function evaluate(entries, row, coefficient) {
    var subjects = entries.map(function (entry) {
      var m = model(entry.subject, coefficient);
      return {
        name: entry.subject.name,
        max: entry.subject.max,
        average: entry.subject.average,
        raw: entry.raw,
        source: m.source,
        n: m.n,
        mid: m.mid(entry.raw),
        low: m.low(entry.raw),
        high: m.high(entry.raw)
      };
    });
    var sum = function (key) { return subjects.reduce(function (s, x) { return s + x[key]; }, 0); };
    var low = sum("low"), mid = sum("mid"), high = sum("high");
    return {
      subjects: subjects,
      rawTotal: sum("raw"),
      mid: mid,
      low: low,
      high: high,
      minimum: row.minimum,
      diff: mid - row.minimum,
      verdict: low >= row.minimum ? "above" : high < row.minimum ? "below" : "border"
    };
  }

  /**
   * index 番目の科目だけを動かしたとき、合格最低点に届くのに必要な素点。
   * mid: 中心の線で届く点 / safe: 低めの線でも届く点。満点でも届かなければ null。
   * entries の index 番目の raw は使わない（未入力でもよい）。
   */
  function required(entries, index, row, coefficient) {
    var models = entries.map(function (e) { return model(e.subject, coefficient); });
    var need = function (key) {
      var others = entries.reduce(function (s, e, i) {
        return i === index ? s : s + models[i][key](e.raw);
      }, 0);
      return solve(function (x) { return others + models[index][key](x); }, row.minimum, 0, entries[index].subject.max);
    };
    return { mid: need("mid"), safe: need("low") };
  }

  /**
   * その年度の「素点合計の目安」。全科目を受験者平均点から同じ得点率だけ
   * 上乗せしたとき、合格最低点に届く素点の合計。
   */
  function borderline(subjects, row, coefficient) {
    var models = subjects.map(function (s) { return model(s, coefficient); });
    var rawAt = function (s, t) { return Math.min(s.max, s.average + t * s.max); };
    var total = function (key) {
      var t = solve(function (t) {
        return subjects.reduce(function (sum, s, i) { return sum + models[i][key](rawAt(s, t)); }, 0);
      }, row.minimum, 0, 1);
      return t == null ? null : subjects.reduce(function (sum, s) { return sum + rawAt(s, t); }, 0);
    };
    // 低めの線で届かせるには多く必要（safe）、高めの線なら少なくて済む（easy）
    return { mid: total("mid"), safe: total("low"), easy: total("high") };
  }

  /**
   * 成績開示との照合: pairs = [{ raw, adjusted }] に直線 adjusted = a + b × raw を当てる。
   * 0点・満点に張り付いた組は直線から外れるので除く。2組未満・素点が全部同じなら null。
   */
  function fitLine(pairs, max) {
    var pts = pairs.filter(function (p) {
      return Number.isFinite(p.raw) && Number.isFinite(p.adjusted) && p.adjusted > 0 && p.adjusted < max;
    });
    var n = pts.length;
    if (n < 2) return null;
    var mx = pts.reduce(function (s, p) { return s + p.raw; }, 0) / n;
    var my = pts.reduce(function (s, p) { return s + p.adjusted; }, 0) / n;
    var sxx = pts.reduce(function (s, p) { return s + (p.raw - mx) * (p.raw - mx); }, 0);
    if (sxx < 1e-9) return null;
    var sxy = pts.reduce(function (s, p) { return s + (p.raw - mx) * (p.adjusted - my); }, 0);
    var b = sxy / sxx, a = my - b * mx;
    var sse = pts.reduce(function (s, p) { var e = p.adjusted - (a + b * p.raw); return s + e * e; }, 0);
    return { a: a, b: b, rmse: n > 2 ? Math.sqrt(sse / (n - 2)) : 0, n: n };
  }

  var api = { model: model, evaluate: evaluate, required: required, borderline: borderline, fitLine: fitLine };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.WasedaScoreCalc = api;
})(typeof window !== "undefined" ? window : globalThis);
