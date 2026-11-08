# -*- coding: utf-8 -*-
"""現行案.md の62項目から、目次を組む。出力 manuscript/企画書/目次_最新.md"""
import re

MAP = [("基本の基本","第1章","基本の基本編"), ("戦略","第2章","戦略編"), ("計画","第3章","計画編"),
       ("授業","第4章","授業編"), ("暗記","第5章","暗記編"), ("演習","第6章","演習編"),
       ("復習","第7章","復習編"), ("集中","第8章","集中編"), ("モチベ","第9章","モチベ編"),
       ("本番","終章","本番編")]

# 実字数（原稿_最新版.md から）
RATE = 520   # 四六判9.5pt縦組み。見出し・×○囲み・余白こみの実効字数
gen = open("manuscript/原稿_最新版.md", encoding="utf-8").read()
_p = re.split(r'^## (\d{2})　.+$', gen, flags=re.M)
ZI = {_p[i]: len(re.sub(r'\s', '', _p[i+1])) for i in range(1, len(_p), 2)}
def pz(ns): return max(1, round(sum(ZI.get(n, 0) for n in ns) / RATE))

plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 75項目")[1].split("# 8 1週間")[0]
chs, cur = [], None
for line in sec.split("\n"):
    m = re.match(r'^## (.+?)\s+(\d+)本\s*$', line)
    if m:
        cur = {"old": re.split(r'[\s　]{2,}', m.group(1).strip())[0], "items": []}
        chs.append(cur); continue
    m = re.match(r'^(\d{2})　(.*?)(?:\s+(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力))?\s*$',
                 line.rstrip())
    if m and cur:
        cur["items"].append({"n": m.group(1),
                             "t": m.group(2).replace("★厚く書く","").replace("★新規","").strip(),
                             "w": m.group(3) or "", "x": "", "o": "",
                             "thick": "★厚く書く" in line, "new": "★新規" in line}); continue
    m = re.match(r'^\s+(×|○)「(.+)」\s*$', line)
    if m and cur and cur["items"]:
        cur["items"][-1]["x" if m.group(1)=="×" else "o"] = m.group(2)

by = {c["old"]: c for c in chs}
L = ["# 目次　最新版", "",
     "2026年11月4日。コピーを戻した版。", "",
     "序章は 序章_v11、第1章は「基本の基本編」8本。",
     "第2章以降は「頭のいい人が、絶対にやらないこと　○○編」。", "",
     "---", "",
     "# 大枠", "", "```",
     "巻頭　　　10秒だけ、付き合ってください　　　　　　　　　　　　　6ページ",
     "　　11個の数字 ／ 正しいのに変われない ／ 見えないから",
     "　　偏差値42から早稲田 ／ 全部書く、隠すところは1つもない",
     "",
     "序章　　やり方を疑わずに、量を増やすのをやめる",
     "　　それ、誰から教わりましたか ／ 人は、やったことのないものを選べない",
     "　　2000人が、全員同じ4つ ／ ×やりやすかったか　○出せたか",
     "　　探している間は、やらなくていい",
     ""]
tot = 0
for old, no, name in MAP:
    c = by[old]; n = len(c["items"])
    pg = pz([i["n"] for i in c["items"]]) + 2; tot += pg
    head = f"{no}　　　" if no=="終章" else f"{no}　　"
    L.append(f"{head}頭のいい人が、絶対にやらないこと　{name}　"
             f"{'　'*(4-len(name))}{n:>2}本　{pg:>3}ページ")
L += ["", "巻末　　　手持ちカード ／ まず、この6つ ／ 悩み別の引き方　 24ページ",
      "　　　　　5教科で、どう使うか ／ 保護者の方へ ／ おわりに", "",
      f"　　　　　　　　　　　　　　　　　　合計　約{6+9+tot+28}ページ　四六判", "```", "",
      f"（1ページ{RATE}字で計算。四六判9.5pt縦組み、見出しと×／○の囲みこみ）", "",
      "章の名前が8回くり返される。目次を上から読むだけで、",
      "「頭のいい人が、絶対にやらないこと」が8回、目に入る。", "",
      "---", "", "# 目次（本に載せる形）", ""]
for old, no, name in MAP:
    c = by[old]
    L += [f"## {no}　頭のいい人が、絶対にやらないこと　{name}", "", "```"]
    for it in c["items"]:
        mark = "　★" if it["thick"] else ""
        L += [f'{it["n"]}　{it["t"]}{mark}',
              f'　　×「{it["x"]}」', f'　　○「{it["o"]}」', ""]
    L += ["```", ""]
L += ["★は厚く書く項目（4ページ）。ほかは3.3ページ。", "",
      "---", "", "# 武器は、どこに出るか", "", "```",
      "序章03　　　　 6つをまとめて渡す（やり方を6つに分ける）",
      "各項目の右肩　　1つずつ。62項目で62回",
      "章扉　　　　　　その章でよく使う武器を2つ",
      "巻末カード　　　6行。切り取って筆箱に入る",
      "```", "",
      "目次には武器を出さない。出すと1行が2段になって、読みにくくなる。", ""]
open("manuscript/企画書/目次_最新.md","w",encoding="utf-8").write("\n".join(L))
print("章", len(MAP), "項目", sum(len(by[o]['items']) for o,_,_ in MAP))
