// 検算: node waseda-score/calc.test.js
const assert = require("assert");
const { adjust, evaluate } = require("./calc.js");
const DATA = require("./data.js");

const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} != ${b}`);
const subject = { name: "英語", max: 80, average: 30 };

// 平均点ちょうどなら、係数によらず満点の半分
[1, 1.25, 1.5].forEach(k => near(adjust(subject, 30, k), 40));
// 平均+10点、係数1.25 → 40 + 12.5
near(adjust(subject, 40, 1.25), 52.5);
// 0〜満点に収まる
near(adjust(subject, 80, 1.5), 80);
near(adjust(subject, 0, 1.5), 0);

const row = { minimum: 120 };
const k = { low: 1, mid: 1.25, high: 1.5 };
const entries = raws => raws.map(raw => ({ subject, raw }));

// 全科目平均 → 合計は満点の半分で、幅はゼロ
let r = evaluate(entries([30, 30, 30]), row, k);
near(r.mid, 120); near(r.low, 120); near(r.high, 120);
assert.strictEqual(r.verdict, "above");

// 平均より下 → 係数が大きいほど下がるので low は k=1.5 側
r = evaluate(entries([20, 20, 20]), row, k);
near(r.high, 90); near(r.low, 75); near(r.mid, 82.5);
assert.strictEqual(r.verdict, "below");

// 幅が最低点をまたぐ
r = evaluate(entries([40, 40, 40]), { minimum: 160 }, k);
near(r.low, 150); near(r.high, 165);
assert.strictEqual(r.verdict, "border");

// データの整合: 配点の合計が満点と一致し、平均点が配点内にある
for (const faculty of DATA.faculties) for (const method of faculty.methods) for (const row of method.rows) {
  const label = `${faculty.name} ${method.name} ${row.year}`;
  for (const elective of row.electives.length ? row.electives : [null]) {
    const subjects = row.required.concat(elective ? [elective] : []);
    assert.strictEqual(subjects.reduce((s, x) => s + x.max, 0), row.total, label);
    subjects.forEach(x => assert.ok(x.average > 0 && x.average < x.max, label + x.name));
  }
  assert.ok(row.minimum > 0 && row.minimum < row.total, label);
}

console.log("ok");
