# -*- coding: utf-8 -*-
"""原稿とビルダーの食い違いを機械で見つける。book/ で実行。

これまで3回、同じ種類の事故が起きた。
  1 ビルダーが古い序章ファイルを指したまま残っていた
  2 巻頭の冒頭134字が、split のミスで原稿から落ちていた
  3 本文が「巻頭で言いました」と書いているのに、巻頭に入っていなかった
どれも、人が読んで気づくまで分からなかった。ここで止める。
"""
import re, os, sys, glob

LIVE = ["assemble.py", "build_toc.py", "build_toc_pdf.py", "build_spec.py",
        "build_genko_pdf.py", "build_daicho.py", "build_jo.py",
        "build_hyoshi.py", "build_zenhan.py", "check.py"]
ACTIVE = ["manuscript/巻頭ページ.md", "manuscript/序章_v11.md",
          "manuscript/本文/新構成/基本の基本8本.md"]

ng = []
def bad(cat, msg): ng.append(f"[{cat}] {msg}")

# 1 稼働中のビルダーが、存在しない原稿を指していないか
for f in LIVE:
    p = os.path.join("scripts", f)
    if not os.path.exists(p): continue
    for m in re.finditer(r'"(manuscript/[^"]+\.md)"', open(p, encoding="utf-8").read()):
        if "*" in m.group(1) or "{" in m.group(1): continue   # glob と f-string は実パスではない
        if not os.path.exists(m.group(1)):
            bad("パス", f"{f} が存在しない原稿を指している　{m.group(1)}")

# 2 アスタリスクによる強調（著者指定で禁止）
for f in ACTIVE:
    n = open(f, encoding="utf-8").read().count("**")
    if n: bad("文体", f"{f} にアスタリスク強調が {n//2} か所")

# 3 巻頭の1行目が、組み上がった原稿に入っているか
gen = open("manuscript/原稿_最新版.md", encoding="utf-8").read()
for probe in ["いきなりですが、", "10秒で、次の11個の数字を覚えきってください。",
              "では、どれを捨てますか？"]:
    if probe not in gen:
        bad("欠落", f"巻頭の「{probe}」が原稿_最新版.md にない")

# 3b マーカーの印が、組み上がった原稿に漏れていないか（置換の壊れを検出）
for probe, why in [("==", "マーカーの印 == が本文に残っている"),
                   ("\\1", "置換が壊れて \\1 という文字列が本文に入っている")]:
    if probe in gen:
        n = gen.count(probe)
        bad("置換", f"原稿_最新版.md に {why}（{n}か所）")

# 4 「N番」の参照先が実在するか
plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 75項目")[1].split("# 8 1週間")[0]
nums = {m.group(1) for m in re.finditer(r'^(\d{2})　', sec, flags=re.M)}
for f in ACTIVE:
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for m in re.finditer(r'(\d{1,2})番', line):
            n = m.group(1).zfill(2)
            if n not in nums:
                bad("参照", f"{f}:{i} 存在しない項目を指している　{m.group(1)}番")

# 5 「巻頭で」「序章で」と書いた主張の、相手がいるか（目視すべき箇所を出すだけ）
kan = open("manuscript/巻頭ページ.md", encoding="utf-8").read()
jo = open("manuscript/序章_v11.md", encoding="utf-8").read()
warn = []
for f in ACTIVE:
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if re.search(r'(巻頭|序章)(で|に|の|は).{0,24}(ました|あります|入ります|思い出|書いた|言った)', line):
            warn.append(f"  {f}:{i}  {line.strip()}")

print("=" * 56)
if ng:
    print(f"NG {len(ng)} 件")
    for x in ng: print(" ", x)
else:
    print("OK　パス・文体・欠落・参照番号、すべて通過")
if warn:
    print(f"\n要目視　巻頭／序章への参照 {len(warn)} か所（相手がいるか人が確かめる）")
    for x in warn: print(x)
print("=" * 56)
sys.exit(1 if ng else 0)
