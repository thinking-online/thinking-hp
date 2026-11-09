# -*- coding: utf-8 -*-
"""下書き2日の工程が、いまどこまで終わっているかを出す。book/ で実行。

docs/36_下書き2日の工程.md の S1〜S18 を、ファイルの中身を見て判定する。
自己申告のチェックは受け付けない。通らないステップより先は表示しない。
"""
import re, os, glob, subprocess, sys

def rd(p):
    try: return open(p, encoding="utf-8").read()
    except OSError: return None

PLAN = "manuscript/企画書/現行案.md"
KETU = "manuscript/企画書/決定.md"
Q50  = "manuscript/企画書/Q50.md"
JIT  = "manuscript/企画書/実話10.md"

CH = [("第1章", "基本の基本"), ("第2章", "戦略"), ("第3章", "計画"), ("第4章", "授業・学校"),
      ("第5章", "暗記"), ("第6章", "演習"), ("第7章", "復習・基準"), ("第8章", "集中・環境"),
      ("第9章", "不安とモチベ"), ("終章", "本番")]

def plan_items():
    """現行案から項目を読む。[(番号, 見出し行, 本文ブロック, 章), ...]"""
    t = rd(PLAN)
    if not t: return [], None
    m = re.search(r'^# 7 (\d+)項目$', t, flags=re.M)
    if not m: return [], None
    sec = t[m.end():].split("# 8 ")[0]
    out, cur = [], None
    for line in sec.split("\n"):
        h = re.match(r'^## (.+?)[\s　]+(\d+)本\s*$', line)
        if h:
            cur = re.split(r'[\s　]+', h.group(1).strip())[-1]; continue
        it = re.match(r'^(\d{2})　(.+)$', line.rstrip())
        if it and cur:
            out.append({"n": it.group(1), "line": line.rstrip(), "ch": cur, "x": "", "o": ""})
            continue
        p = re.match(r'^[\s　]+(×|○)「(.+)」\s*$', line)
        if p and out:
            out[-1]["x" if p.group(1) == "×" else "o"] = p.group(2)
    return out, int(m.group(1))

H = r'[ \t　]*'          # 横の空白だけ。改行はまたがせない

def ketu(key):
    t = rd(KETU)
    if not t: return None
    m = re.search(r'^' + H + re.escape(key) + H + r'[=＝]' + H + r'(.*)$', t, flags=re.M)
    if not m: return None
    v = m.group(1).strip().strip("　")
    return v or None

WORD = "選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力"

# ---------------- 各ステップの判定 ----------------

def s1():
    items, n = plan_items()
    if n is None: return False, "現行案.md に「# 7 NN項目」が無い"
    if n != 50 or len(items) != 50:
        return False, f"見出しは「# 7 {n}項目」、実際の項目は {len(items)}本。どちらも50にする"
    bad = [i["n"] for i in items if not (i["x"] and i["o"])]
    if bad: return False, "×／○ が足りない：" + " ".join(bad)
    # 01と02は、力を渡す前の項目なので付けない
    bad = [i["n"] for i in items if i["n"] not in ("01", "02") and not re.search(WORD, i["line"])]
    if bad: return False, "力が付いていない：" + " ".join(bad)
    return True, "50本。×／○と力、すべてあり"

def s2():
    a, b = ketu("テンプレ"), ketu("基本の基本8本")
    if not a: return False, f"{KETU} に「テンプレ　＝　A」の行が無い"
    if a.upper() not in ("A", "B", "C"): return False, f"テンプレの値が {a}。A/B/C のどれかにする"
    if not b: return False, f"{KETU} に「基本の基本8本　＝　…」の行が無い"
    return True, f"テンプレ {a.upper()}　／　基本の基本8本 {b}"

def s3():
    items, _ = plan_items()
    if not items: return False, "S1 が先"
    bad = [i["n"] for i in items if not re.search(r'［\d+p］', i["line"])]
    if bad: return False, f"目標ページが無い {len(bad)}本：" + " ".join(bad[:12]) + (" …" if len(bad) > 12 else "")
    from collections import Counter
    c = Counter(re.search(r'［(\d+)p］', i["line"]).group(1) for i in items)
    return True, "　".join(f"{k}ページ {v}本" for k, v in sorted(c.items(), key=lambda x: int(x[0])))

def s4():
    miss = [k for k in ("見出し1", "見出し2", "見出し3", "見出し4", "見出し5") if not ketu(k)]
    if miss: return False, f"{KETU} に足りない：" + " ".join(miss)
    return True, "　→　".join(ketu(f"見出し{i}") for i in range(1, 6))

def s5():
    t = rd(Q50)
    if t is None: return False, f"{Q50} が無い"
    if "〔" in t: return False, "〔　〕が残っている"
    nm = len(re.findall(r'^[ \t　]*▲', t, flags=re.M))
    if nm: return False, f"▲ が {nm}本 残っている。下書きのまま。1行ずつ自分の言葉に直して ▲ を消す"
    qs = dict(re.findall(r'^(\d{2})[\s　]+(\S.*)$', t, flags=re.M))
    items, _ = plan_items()
    need = [i["n"] for i in items] or [f"{k:02d}" for k in range(1, 51)]
    miss = [n for n in need if n not in qs]
    if miss: return False, f"Qが無い {len(miss)}本：" + " ".join(miss[:12]) + (" …" if len(miss) > 12 else "")
    return True, f"{len(qs)}本ぶんのQ"

def s6():
    t = rd(JIT)
    if t is None: return False, f"{JIT} が無い"
    if "〔" in t: return False, "〔　〕が残っている"
    secs = re.split(r'^## (.+)$', t, flags=re.M)
    done, empty = 0, []
    for i in range(1, len(secs), 2):
        name, body = secs[i].strip(), secs[i+1]
        got = all(re.search(r'^' + H + k + H + r'(\S.+)$', body, flags=re.M)
                  for k in ("いつ", "誰", "何があった"))
        if got: done += 1
        else: empty.append(name)
    if done < 10:
        return False, f"埋まっているのは {done}件。空：" + " ／ ".join(empty[:5]) + (" …" if len(empty) > 5 else "")
    return True, f"{done}件"

def bodies():
    """本文を項目ごとに読む。{番号: 本文} （番号は現行案の番号に題名で突き合わせ）"""
    t = rd("manuscript/原稿_最新版.md")
    if not t: return {}
    p = re.split(r'^## (\d{2})　(.+)$', t, flags=re.M)
    return {p[i]: p[i+2] for i in range(1, len(p), 3)}

def chapter_step(label, key):
    def f():
        items, _ = plan_items()
        mine = [i for i in items if i["ch"] == key]
        if not mine: return False, f"現行案に「{key}」の章が無い（S1が先）"
        heads = [ketu(f"見出し{k}") for k in range(1, 6)]
        if not all(heads): return False, "S4 が先（見出しが決まっていない）"
        tmpl = (ketu("テンプレ") or "").upper()
        if tmpl not in ("A", "B", "C"): return False, "S2 が先"
        bd = bodies()
        qs = dict(re.findall(r'^(\d{2})[ \t　]+(\S.*)$', rd(Q50) or "", flags=re.M))
        if not qs: return False, "S5 が先（Qが1本も確定していない）"
        ng = []
        for i in mine:
            b = bd.get(i["n"])
            if b is None: ng.append(f'{i["n"]} 本文なし'); continue
            if "★未執筆" in b: ng.append(f'{i["n"]} 未執筆'); continue
            q = qs.get(i["n"], "")
            core = re.sub(r'[、。「」『』？！\s　]', '', q)[:14]
            if core and core not in re.sub(r'[、。「」『』\s　]', '', b):
                ng.append(f'{i["n"]} Qが本文に無い'); continue
            if tmpl == "A":
                lack = [h for h in heads[1:] if h not in b]
                if lack: ng.append(f'{i["n"]} 見出し不足（{lack[0]}）'); continue
            m = re.search(r'［(\d+)p］', i["line"])
            if m:
                sys.path.insert(0, "scripts")
                from pages import pages
                got, want = pages(b), int(m.group(1))
                if abs(got - want) > 1: ng.append(f'{i["n"]} {got}ページ（目標{want}）')
        return (False, f"{len(ng)}本：" + " ／ ".join(ng[:6]) + (" …" if len(ng) > 6 else "")) if ng \
               else (True, f"{len(mine)}本すべて通過")
    return f

def s17():
    r = subprocess.run([sys.executable, "scripts/check.py"], capture_output=True, text=True)
    ok = "すべて通過" in r.stdout
    return ok, "check.py 通過" if ok else "check.py が通らない。実行して中身を見る"

def s18():
    src = "manuscript/原稿_最新版.md"
    if not os.path.exists(src): return False, "原稿_最新版.md が無い"
    t = os.path.getmtime(src)
    old = [p for p in ("build/原稿_横組み.pdf", "build/縦組み_原稿.pdf")
           if not os.path.exists(p) or os.path.getmtime(p) < t]
    if old: return False, "原稿より古い：" + " ".join(os.path.basename(p) for p in old)
    return True, "2つとも最新"

STEPS = [("S1", "50本の中身を確定する", "著者", s1),
         ("S2", "テンプレを確定する", "著者", s2),
         ("S3", "長さを50本に割る", "著者", s3),
         ("S4", "固定見出しの文言を確定する", "著者", s4),
         ("S5", "Qを50本ぶん書く", "著者", s5),
         ("S6", "実話を10個えらぶ", "著者", s6)] + \
        [(f"S{7+k}", f"{lb}　{ky}　を書く", "こちら", chapter_step(lb, ky))
         for k, (lb, ky) in enumerate(CH)] + \
        [("S17", "通す", "こちら", s17),
         ("S18", "PDFを出す", "こちら", s18)]

def main():
    print("=" * 62)
    print("  下書き2日の工程　　docs/36_下書き2日の工程.md")
    print("=" * 62)
    blocked = None
    for sid, name, who, fn in STEPS:
        if blocked:
            print(f"  　  {sid}  {name}")
            continue
        try: ok, msg = fn()
        except Exception as e: ok, msg = False, f"判定できない：{e}"
        if ok:
            print(f"  ✓   {sid}  {name}")
            print(f"  　        {msg}")
        else:
            print(f"  →   {sid}  {name}　［{who}］")
            print(f"  　        {msg}")
            blocked = sid
    print("=" * 62)
    if blocked:
        print(f"  いまやるのは {blocked}。これが終わるまで、先に進まない。")
    else:
        print("  全部終わり。下書きが通った。")
    print("=" * 62)

if __name__ == "__main__":
    main()
