# 個別原稿を本の順に束ねて 台本_全文.md を作り直す。book/ で実行する。
import os
m = "manuscript"
order = ["はじめに.md", "やらない45.md", "序章.md", "第1章.md"]
ch = {2:(4,10),3:(11,17),4:(18,24),5:(25,31),6:(32,38),7:(39,45)}
for c in range(2,8):
    order.append(f"第{c}章_扉.md")
    a,b = ch[c]
    order += [f"法則{n}.md" for n in range(a,b+1)]
order += ["まとめ.md","親へ.md","付録.md","おわりに.md"]
out = ["# 「やればやるだけ伸びる」あの子が、勉強中に絶対にやらないこと","",
       "## マネするだけで伸びる、あの子の勉強法則45","","朝倉 徹大","",
       "通し台本。個別ファイルは `manuscript/` にある。このファイルはそれを本の順に束ねたもの。",
       "編集はかならず個別ファイル側で行い、このファイルは `scripts/build_daihon.py` で作り直す。","","---",""]
for f in order:
    out.append(open(os.path.join(m,f)).read().rstrip()); out += ["","---",""]
open("台本_全文.md","w").write("\n".join(out))
print("wrote 台本_全文.md from", len(order), "files")
