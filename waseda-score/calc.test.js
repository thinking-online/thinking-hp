// 検算: node waseda-score/calc.test.js
const assert = require("assert");
const { model, evaluate, required, borderline, fitLine } = require("./calc.js");
const DATA = require("./data.js");

const near = (a, b, eps = 1e-6) => assert.ok(Math.abs(a - b) < eps, `${a} != ${b}`);
const k = { low: 1, mid: 1.25, high: 1.5 };
const subject = { name: "英語", max: 80, average: 30 };
const entries = raws => raws.map(raw => ({ subject, raw }));

// --- 推定モデル ---
let m = model(subject, k);
assert.strictEqual(m.source, "estimated");
near(m.mid(30), 40); near(m.low(30), 40); near(m.high(30), 40);   // 平均点 → 満点の半分、幅ゼロ
near(m.mid(40), 52.5); near(m.low(40), 50); near(m.high(40), 55); // 平均より上: 係数が小さいほど低い
near(m.low(20), 25); near(m.high(20), 30);                        // 平均より下: 係数が大きいほど低い
near(m.high(80), 80); near(m.low(0), 0);                          // 0〜満点に収まる

// --- 実測モデル ---
const measured = { name: "英語", max: 80, average: 30, fit: { a: 5, b: 1.1, rmse: 1.5, n: 6 } };
m = model(measured, k);
assert.strictEqual(m.source, "measured");
near(m.mid(40), 49); near(m.low(40), 46); near(m.high(40), 52);   // 幅は残差の2倍
near(model({ ...measured, fit: { a: 5, b: 1.1, rmse: 0, n: 2 } }, k).low(40), 48); // 最低でも1点

// --- 合計と判定 ---
let r = evaluate(entries([30, 30, 30]), { minimum: 120 }, k);
near(r.mid, 120); near(r.low, 120); near(r.high, 120);
assert.strictEqual(r.verdict, "above");
r = evaluate(entries([20, 20, 20]), { minimum: 120 }, k);
near(r.high, 90); near(r.low, 75); near(r.mid, 82.5);
assert.strictEqual(r.verdict, "below");
r = evaluate(entries([40, 40, 40]), { minimum: 160 }, k);
near(r.low, 150); near(r.high, 165);
assert.strictEqual(r.verdict, "border");

// --- 必要点: 他の2科目が平均（40+40）で最低点130 → 残り1科目は調整後50が必要 ---
let need = required(entries([30, 30, 0]), 2, { minimum: 130 }, k);
near(need.mid, 38);   // 40 + 1.25(x-30) = 50
near(need.safe, 40);  // 低めの線（係数1.0）: 40 + (x-30) = 50
// 求めた点を入れるとちょうど最低点
near(evaluate(entries([30, 30, need.mid]), { minimum: 130 }, k).mid, 130);
// 満点でも届かない
assert.strictEqual(required(entries([0, 0, 0]), 2, { minimum: 130 }, k).mid, null);
// 中心では届くが、余裕を見ると届かない
need = required(entries([30, 30, 0]), 2, { minimum: 150 }, k);
near(need.mid, 54); assert.ok(need.safe > need.mid);

// --- 年度の目安: 3科目とも平均+8点（得点率+10%）で 120 + 3×10 = 150 ---
let b = borderline([subject, subject, subject], { minimum: 150 }, k);
near(b.mid, 114); near(b.safe, 120); near(b.easy, 110);
assert.ok(b.easy < b.mid && b.mid < b.safe);

// --- 直線の当てはめ ---
let f = fitLine([{ raw: 20, adjusted: 27 }, { raw: 40, adjusted: 49 }], 80);
near(f.b, 1.1); near(f.a, 5); near(f.rmse, 0); assert.strictEqual(f.n, 2);
f = fitLine([{ raw: 20, adjusted: 27.5 }, { raw: 30, adjusted: 37.5 }, { raw: 40, adjusted: 49.5 }, { raw: 50, adjusted: 59.5 }], 80);
near(f.b, 1.08); assert.ok(f.rmse > 0 && f.rmse < 1);
assert.strictEqual(fitLine([{ raw: 20, adjusted: 27 }], 80), null);                               // 1組では決まらない
assert.strictEqual(fitLine([{ raw: 20, adjusted: 27 }, { raw: 20, adjusted: 28 }], 80), null);    // 素点が同じ
assert.strictEqual(fitLine([{ raw: 20, adjusted: 27 }, { raw: 79, adjusted: 80 }], 80), null);    // 満点張り付きは除外

// --- データの整合 ---
for (const faculty of DATA.faculties) for (const method of faculty.methods) for (const row of method.rows) {
  const label = `${faculty.name} ${method.name} ${row.year}`;
  for (const elective of row.electives.length ? row.electives : [null]) {
    const subjects = row.required.concat(elective ? [elective] : []);
    assert.strictEqual(subjects.reduce((s, x) => s + x.max, 0), row.total, label);
    subjects.forEach(x => assert.ok(x.average > 0 && x.average < x.max, label + x.name));
    const line = borderline(subjects, row, DATA.coefficient);
    assert.ok(line.mid > row.total * 0.4 && line.mid < row.total * 0.9, label + " 目安 " + line.mid);
  }
  assert.ok(row.minimum > 0 && row.minimum < row.total, label);
}

console.log("ok");
