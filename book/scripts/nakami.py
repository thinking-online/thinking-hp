# -*- coding: utf-8 -*-
"""50本それぞれが、読者に何を渡しているかを数える。

1項目が渡せるものは、4つしかない。
　数字　　実行の基準になる数値（10秒、3問、8割）
　判断　　どういうときにどうするか（方針が立たない→見る／計算で詰まった→粘る）
　動作　　手の動かし方（指を1行目に置く、解答冊子を別の部屋に）
　理由　　なぜ効くか（探していないものは、あとで探せない）

4つそろっていない項目は、読んでも動けない。
book/ で実行。
"""
import re, sys, io
sys.path.insert(0, "scripts")
from pages import pages

SRC = "manuscript/原稿_最新版.md"
PLAN = "manuscript/企画書/現行案.md"

NUM  = re.compile(r'\d+(?:秒|分|問|回|周|個|割|ページ|行|時間|語|点|日|冊|パーセント)')
HAN  = re.compile(r'なら[、。]|ときは|場合は|→|とき　|かどうか|超えたら|以上なら|以下なら|だったら')
DOU  = re.compile(r'^#+\s*(やり方|手順|やること)|^###?\s*[1-9]　')
RIYU = re.compile(r'なぜ|理由は|からです|ためです|ということです|のは、')
KEN  = re.compile(r'大学|実験|調査|研究|パーセント|被験者|報告')

plan = io.open(PLAN, encoding="utf-8").read()
sec = plan.split("# 7 50項目")[1].split("# 8 ")[0]
tgt, cur, chs = {}, None, {}
for line in sec.split("\n"):
    m = re.match(r'^## (.+?)[\s　]+(\d+)本\s*$', line)
    if m: cur = re.split(r'[\s　]+', m.group(1).strip())[-1]; continue
    m = re.match(r'^(\d{2})　(.+)$', line.rstrip())
    if m and cur:
        p = re.search(r'［(\d)p］', m.group(2))
        tgt[m.group(1)] = (int(p.group(1)) if p else 4, cur)

man = io.open(SRC, encoding="utf-8").read()
parts = re.split(r'^## (\d{2})　(.+)$', man, flags=re.M)
rows, cur = [], None
for i in range(1, len(parts), 3):
    n, t, b = parts[i], parts[i+1].strip(), parts[i+2]
    t = re.sub(r'[\s　]*(★厚く書く|★新規|［\d+p］|〔新〕|〔旧稿〕)', '', t).strip()
    if "★未執筆" in b:
        rows.append((n, t, None)); continue
    nums = sorted(set(NUM.findall(b)))
    rows.append((n, t, {
        "数字": nums,
        "判断": len(HAN.findall(b)),
        "動作": len(re.findall(r'^###?\s*[1-9]　', b, flags=re.M)) or (1 if DOU.search(b) else 0),
        "理由": len(RIYU.findall(b)),
        "研究": len(KEN.findall(b)),
        "p":    pages(b),
    }))

print("=" * 78)
print("  50本が渡している情報　　python3 scripts/nakami.py")
print("=" * 78)
print("  番号 項目                               数字 判断 動作 理由 研究  目標  実測")
薄 = []
for n, t, d in rows:
    want, ch = tgt.get(n, (4, "?"))
    if d is None:
        print("  %s  %-32s  ──　まだ書いていない  （目標%dp）" % (n, t[:32], want)); continue
    thin = []
    if len(d["数字"]) < 2: thin.append("数字")
    if d["判断"] < 2:      thin.append("判断")
    if d["動作"] < 2:      thin.append("動作")
    if d["理由"] < 3:      thin.append("理由")
    mark = "  ← " + "・".join(thin) + "が薄い" if thin else ""
    print("  %s  %-32s  %2d  %2d  %2d  %2d  %2d   %dp  %2dp%s"
          % (n, t[:32], len(d["数字"]), d["判断"], d["動作"], d["理由"], d["研究"],
             want, d["p"], mark))
    if thin: 薄.append((n, t, thin, d))
print("=" * 78)
done = [r for r in rows if r[2]]
print("  書けている %d本　／　まだ %d本" % (len(done), len(rows) - len(done)))
print("  4つそろっている %d本　／　どれか薄い %d本" % (len(done) - len(薄), len(薄)))
print()
print("  研究が入っているのは %d本。序章の3つ以外に根拠が要る項目は、ここで足す。"
      % sum(1 for _, _, d in rows if d and d["研究"] >= 2))
print("=" * 78)
if 薄:
    print("  中身を足すべき項目")
    for n, t, thin, d in 薄:
        ex = "　数字の例 " + "／".join(d["数字"][:5]) if d["数字"] else "　数字が1つもない"
        print("    %s %s" % (n, t))
        print("       %sが薄い。%s" % ("・".join(thin), ex))
