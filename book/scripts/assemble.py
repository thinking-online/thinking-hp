# -*- coding: utf-8 -*-
"""現行案の62項目順に、既存本文を並べ直して1本の原稿にする。
出力 manuscript/原稿_最新版.md  未執筆は印をつけて残す。"""
import re, glob, difflib, os

def norm(s):
    return re.sub(r'[、。「」？\s　・]', '', s)

# ---- 1 現行案から62項目を読む
plan = open("manuscript/企画書/現行案.md", encoding="utf-8").read()
sec = plan.split("# 7 75項目")[1].split("# 8 1週間")[0]
chapters, cur = [], None
for line in sec.split("\n"):
    m = re.match(r'^## (.+?)\s+(\d+)本\s*$', line)
    if m:
        name = re.split(r'[\s　]{2,}', m.group(1).strip())[0]
        cur = {"name": name, "items": []}
        chapters.append(cur); continue
    m = re.match(r'^(\d{2})　(.*?)(?:\s+(選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力))?\s*$',
                 line.rstrip())
    if m and cur is not None:
        t = m.group(2).replace("★厚く書く","").replace("★新規","").strip()
        cur["items"].append({"n": m.group(1), "t": t,
                             "w": m.group(3) or "", "thick": "★厚く書く" in line, "new": "★新規" in line,
                             "x": "", "o": ""})
        continue
    m = re.match(r'^\s+(×|○)「(.+)」\s*$', line)
    if m and cur and cur["items"]:
        cur["items"][-1]["x" if m.group(1) == "×" else "o"] = m.group(2)

# ---- 2 既存本文を全部読む
bodies = {}
for f in (sorted(glob.glob("manuscript/本文/*.md"))
          + sorted(glob.glob("manuscript/本文/新規/*.md"))
          + sorted(glob.glob("manuscript/本文/新構成/*.md"))):
    txt = open(f, encoding="utf-8").read()
    parts = re.split(r'^# (\d{2})　(.+)$', txt, flags=re.M)
    for i in range(1, len(parts), 3):
        title, body = parts[i+1].strip(), parts[i+2]
        body = re.sub(r'^\s*　　[×○]「.*?」\s*$', '', body, flags=re.M)
        body = body.split("---", 1)[-1].strip() if body.lstrip().startswith("---") \
               else re.sub(r'^\s*---\s*$', '', body, count=1, flags=re.M).strip()
        bodies[norm(title)] = {"src": os.path.basename(f), "title": title, "body": body}

# ---- 3 照合
keys = list(bodies)
out, miss, used = [], [], set()
for ch in chapters:
    for it in ch["items"]:
        k = norm(it["t"])
        hit = k if k in bodies else None
        if not hit:
            c = difflib.get_close_matches(k, keys, n=1, cutoff=0.72)
            hit = c[0] if c else None
        if hit and hit not in used:
            it["body"] = bodies[hit]["body"]; it["src"] = bodies[hit]["src"]
            used.add(hit)
        else:
            it["body"] = None; miss.append(f'{it["n"]}　{it["t"]}')

# ---- 4 出力
L = ["# 原稿　最新版", "", "現行案の62項目順に、既存本文を並べ直したもの。",
     "章と番号は新構成。本文は既存のまま（文体・長さの調整はこれから）。", "",
     "未執筆の項目は「★未執筆」と書いてある。", "", "---", ""]
kan=open("manuscript/巻頭ページ.md",encoding="utf-8").read()
# 1つ目の --- までが見出しと編集メモ。そこから後ろが本文。
# split("---",2)[2] だと「いきなりですが」で始まる冒頭が丸ごと落ちる
L.append("# 巻頭　10秒だけ、付き合ってください\n\n"+kan.split("---",1)[1].strip())
L += ["", "---", ""]
jo=re.sub(r"==(.+?)==", r"\1", open("manuscript/序章_v11.md",encoding="utf-8").read())
L.append(jo.strip())
L += ["", "---", ""]
for ch in chapters:
    L += [f'# {ch["name"]}', ""]
    for it in ch["items"]:
        L += [f'## {it["n"]}　{it["t"]}', "",
              f'　　×「{it["x"]}」', f'　　○「{it["o"]}」', "",
              f'{it["w"]}' + ("　★厚く書く" if it["thick"] else ""), ""]
        if it["body"]:
            L += [it["body"], ""]
        else:
            L += ["★未執筆", ""]
        L += ["---", ""]
os.makedirs("manuscript", exist_ok=True)
open("manuscript/原稿_最新版.md", "w", encoding="utf-8").write("\n".join(L))

tot = sum(len(c["items"]) for c in chapters)
w = sum(len(re.sub(r'\s', '', i["body"] or "")) for c in chapters for i in c["items"])
print(f"項目 {tot}　本文あり {tot-len(miss)}　未執筆 {len(miss)}　本文字数 {w:,}")
print("未執筆：")
for m in miss: print("  ", m)
