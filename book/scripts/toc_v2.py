# -*- coding: utf-8 -*-
"""plan_v2.py から、新しい目次（docs/50）を作る。book/ で実行。"""
import sys, io
sys.path.insert(0, 'scripts')
from plan_v2 import CHAPTERS, LAWS
o = []
o.append("# 50　新しい目次（8章・50本）\n")
o.append("章は8つ。章タイトルは、全部「頭のいい人は、〜しない」。項目タイトルは、全部「読者がいま、良いと思ってやっていること」。\nこのファイルは scripts/toc_v2.py が scripts/plan_v2.py から作る。直すときは plan_v2.py を直す。\n")
o.append("---\n")
o.append("# 章タイトル\n")
o.append("```")
for c in CHAPTERS:
    o.append("　%s　%s　　〔%s・%d本〕" % (c[0], c[1], c[2], len(c[3])))
o.append("```\n")
o.append("ふつうは「やったほうがいい」と思われていることを、章タイトルに置いた。答えが、章の中身になっている。\n")
o.append("```")
o.append("　授業を「聞かない」　　　→　聞く時間ではなく、思い出す時間にしている")
o.append("　「覚えよう」としない　　→　覚えるのではなく、思い出す練習をしている")
o.append("　解けた問題を数えない　　→　点になるのは、解けなかった問題のほう")
o.append("　計画を守らない　　　　　→　崩れる前提で作って、直しつづける")
o.append("　集中力に頼らない　　　　→　意志ではなく、環境と区切りで作る")
o.append("　落ち着こうとしない　　　→　気持ちは消さずに、やることを変える")
o.append("　ひとりで頑張らない　　　→　AIと人を、使い倒す")
o.append("```\n")
o.append("---\n")
o.append("# 目次\n")
for c in CHAPTERS:
    o.append("## %s　%s\n" % (c[0], c[1]))
    o.append("```")
    for no, law, title, x, m, src in c[3]:
        tag = ("【%s】" % LAWS[law]) if c[0] == "第1章" else ""
        o.append("%s　%s%s" % (no, tag, title))
        o.append("　　　×「%s」" % x)
        o.append("　　　○「%s」" % m)
    o.append("```\n")
o.append("---\n")
o.append("# 前後につくもの\n")
o.append("```")
o.append("　巻頭　　　　　10秒だけ、付き合ってください（11個の数字）")
o.append("　はじめに　　　「お前の勉強法、ぜーんぶ、ズレとる。」")
o.append("　この本の使い方　悩みから引く")
o.append("　第1章〜第8章　各章の終わりにコラム1〜2本")
o.append("　巻末　　　　　50を1枚に／6つの言葉で初めての場面を解く／保護者の方へ／参考文献")
o.append("　おわりに　　　笑わなかった人が、ひとりだけいました")
o.append("```")
io.open('docs/50_新しい目次_8章.md', 'w', encoding='utf-8').write("\n".join(o) + "\n")
print("docs/50 を更新")
