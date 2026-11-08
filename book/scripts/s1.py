# -*- coding: utf-8 -*-
"""S1　50本の中身を確定する。採点シートを読んで、仕分けと長さを出す。

　python3 scripts/s1.py            採点の結果を見る
　python3 scripts/s1.py --write    現行案.md を50本に書き換える

採点は manuscript/企画書/S1_採点.md。1本につき2つの数字だけ。
　頻度　直近で見た生徒10人のうち何人がやっているか　0〜10
　効き　やめたら何点動くか　　　　　　　　　　　　 0 / 5 / 10
考え方は docs/37_S1の進め方.md。
"""
import re, sys, json, os

SHEET = "manuscript/企画書/S1_採点.md"
PLAN  = "manuscript/企画書/現行案.md"
WORD  = "選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力"

# 残すか外すか
def nokosu(f, k):
    if k == 0:            return False, "外す候補　効きが0"
    if f <= 3 and k == 5: return False, "外す候補　頻度も効きも小さい"
    return True, ""

# 長さは、残したものの中での順位で決める。
# 全部を4ページにすると、読み終わりが平らになる。数は先に決めておく。
WARI = [(6, 9), (4, 29), (2, 12)]      # (ページ, 本数)

def waritsuke(keep):
    """頻度×効き の高い順に、6ページ→4ページ→2ページで配る"""
    rank = sorted(keep, key=lambda r: (-(r["f"] * r["k"]), -r["k"], -r["f"], r["n"] or "zz"))
    i = 0
    for pg, cnt in WARI:
        n = cnt if pg != 4 else max(0, len(rank) - WARI[0][1] - WARI[2][1])
        for r in rank[i:i+n]:
            r["p"] = pg
            r["why"] = {6: "厚く書く　上位", 4: "標準", 2: "短く言い切る"}[pg]
        i += n
    for r in rank[i:]:
        r["p"], r["why"] = 4, "標準"

def read_sheet():
    t = open(SHEET, encoding="utf-8").read()
    rows, cur, adding = [], None, False
    for line in t.split("\n"):
        h = re.match(r'^## (.+?)\s*$', line)
        if h:
            if "足すもの" in h.group(1): adding = True; cur = None
            else: cur, adding = h.group(1).strip(), False
            continue
        c = re.match(r'^[\s　]+章[\s　]+(\S+)\s*$', line)
        if c and rows and rows[-1]["add"]: rows[-1]["ch"] = c.group(1); continue
        q = re.match(r'^[\s　]+力[\s　]+(\S+)\s*$', line)
        if q and rows and rows[-1]["add"]: rows[-1]["w"] = q.group(1); continue
        xo = re.match(r'^[\s　]+(×|○)「(.*)」\s*$', line)
        if xo and rows and rows[-1]["add"]:
            rows[-1]["x" if xo.group(1) == "×" else "o"] = xo.group(2); continue
        m = re.match(r'^([×x]?)[\s　]*(\d{2}|＋|\+)[\s　]+(\S+)[\s　]+(\S+)[\s　]+(.*)$', line.rstrip())
        if not m: continue
        if cur is None and not adding: continue      # 書き方の例を拾わない
        cut, n, f, k, ttl = m.groups()
        rows.append({"cut": bool(cut), "n": None if n in ("＋", "+") else n,
                     "f": f, "k": k, "t": ttl.strip(), "ch": cur, "add": n in ("＋", "+")})
    return rows, t

def plan_src():
    t = open(PLAN, encoding="utf-8").read()
    m = re.search(r'^# 7 (\d+)項目$', t, flags=re.M)
    sec = t[m.end():].split("# 8 ")[0]
    d, cur = {}, None
    for line in sec.split("\n"):
        h = re.match(r'^## (.+?)[\s　]+(\d+)本\s*$', line)
        if h: cur = re.split(r'[\s　]+', h.group(1).strip())[-1]; continue
        it = re.match(r'^(\d{2})　(.+)$', line.rstrip())
        if it and cur:
            w = re.search(WORD, it.group(2))
            d[it.group(1)] = {"ch": cur, "w": w.group(0) if w else "",
                              "thick": "★厚く書く" in line, "new": "★新規" in line,
                              "t": re.sub(r'[\s　]*(★厚く書く|★新規|' + WORD + r')', '', it.group(2)).strip(),
                              "x": "", "o": "", "note": ""}
            last = it.group(1); continue
        p = re.match(r'^[\s　]+(×|○)「(.+)」\s*$', line)
        if p and d: d[last]["x" if p.group(1) == "×" else "o"] = p.group(2)
        nt = re.match(r'^[\s　]+（(.+)）\s*$', line)
        if nt and d: d[last]["note"] = nt.group(1)
    return d, t, m.start(), m.end()

def main():
    rows, raw = read_sheet()
    src, ptxt, p0, p1 = plan_src()

    un = [r for r in rows if not r["add"] and (r["f"] == "_" or r["k"] == "_")]
    if un:
        print("=" * 60)
        print("  まだ採点していないのが %d本。頻度を埋めるところから。" % len(un))
        print("=" * 60)
        for r in un[:60]:
            print("   %s　_　%s　%s" % (r["n"], r["k"], r["t"]))
        print("=" * 60)
        print("  チャットで「01 7」のように番号と頻度を並べてもいい。")
        return

    rows = [r for r in rows if not (r["add"] and (r["f"] == "_" or r["k"] == "_" or not r["t"]))]
    noch = [r["t"] for r in rows if r["add"] and not r["ch"]]
    if noch:
        print("  足すものに章が書いてない：" + " ／ ".join(noch))
        print("  その行の下に「　　章　暗記」のように足す。")
        return
    for r in rows:
        r["f"], r["k"] = int(r["f"]), int(r["k"])
        r["ok"], r["why"] = nokosu(r["f"], r["k"])
        r["p"] = None

    keep = [r for r in rows if r["ok"] and not r["cut"]]
    cand = [r for r in rows if not r["ok"] and not r["cut"]]
    cut  = [r for r in rows if r["cut"]]
    waritsuke(keep)

    print("=" * 66)
    print("  S1　採点の結果")
    print("=" * 66)
    grid = {}
    for r in rows:
        if r["cut"]: continue
        fb = "7〜10" if r["f"] >= 7 else ("4〜6" if r["f"] >= 4 else "0〜3")
        grid.setdefault((fb, r["k"]), []).append(r["n"] or "＋")
    for fb in ("7〜10", "4〜6", "0〜3"):
        for k in (10, 5, 0):
            v = grid.get((fb, k), [])
            if not v: continue
            print("  頻度%-6s 効き%-3d %2d本   %s" % (fb, k, len(v), " ".join(v)))
    print()

    if cand:
        print("  外す候補　%d本" % len(cand))
        for r in sorted(cand, key=lambda r: (r["k"], r["f"])):
            print("    %s  頻度%2d 効き%2d  %s　　%s" % (r["n"] or "＋", r["f"], r["k"], r["t"], r["why"]))
        print()
    if cut:
        print("  外すと決めたもの　%d本" % len(cut))
        for r in cut: print("    %s  %s" % (r["n"] or "＋", r["t"]))
        print()

    from collections import Counter
    pc = Counter(r["p"] for r in keep)
    print("  残る　%d本　　%s" % (len(keep),
          "　".join("%dページ %d本" % (k, v) for k, v in sorted(pc.items()))))
    itempg = sum(r["p"] for r in keep)
    print("  本文 %dページ　＋　前付6・巻頭10・序章19・章扉10・巻末14・おわりに7・奥付2 ＝ 約%dページ"
          % (itempg, itempg + 68))
    print()

    ch = Counter(r["ch"] for r in keep)
    print("  章ごと")
    for c, v in ch.items():
        mark = "　← 薄い。寄せるか足す" if v <= 2 else ("　← 多い。割るか移す" if v >= 9 else "")
        print("    %-12s %d本%s" % (c, v, mark))
    print()

    d = len(keep) - 50
    print("=" * 66)
    if d == 0:
        print("  ちょうど50本。--write で現行案に書き込める。")
    elif d > 0:
        print("  50本まで、あと %d本 外す。外す候補の上から。" % d)
    else:
        print("  50本まで、あと %d本 足りない。S1-c（足すもの）に戻る。" % -d)
        print("  数合わせで弱い項目を戻さないこと。")
    print("=" * 66)

    if "--write" not in sys.argv: return
    if d != 0:
        print("  50本ちょうどになってから --write する。"); return

    order, o2n, num = [], {}, 0
    seen = []
    for r in keep:
        if r["ch"] not in seen: seen.append(r["ch"])
    for c in seen:
        for r in [r for r in keep if r["ch"] == c]:
            num += 1
            r["new"] = "%02d" % num
            if r["n"]: o2n[r["n"]] = r["new"]
            order.append(r)

    L = ["# 7 50項目", "",
         "序章は番号をつけない。各項目の右肩に力を1つ。",
         "基本の基本編の01と02は、力を渡す前なので付けない。", "",
         "75本から24本を畳んで51本、S1でさらに整理して50本。",
         "［Np］は目標ページ（S3）。頻度と効きの採点から出している。",
         "採点は manuscript/企画書/S1_採点.md、考え方は docs/37。", ""]
    for c in seen:
        mine = [r for r in order if r["ch"] == c]
        L += ["## %s　　%d本" % (c, len(mine)), "", "```"]
        for r in mine:
            s = src.get(r["n"]) or {"x": r.get("x", ""), "o": r.get("o", ""),
                                    "w": r.get("w", ""), "new": True, "note": ""}
            tag = "　★厚く書く" if r["p"] == 6 else ("　★新規" if s.get("new") else "")
            w = s.get("w", "")
            L.append("%s　%s%s%s　［%dp］" % (r["new"], r["t"], tag, ("　" + w) if w else "", r["p"]))
            L.append("　　×「%s」" % s.get("x", ""))
            L.append("　　○「%s」" % s.get("o", ""))
            if s.get("note"): L.append("　　（%s）" % s["note"])
            L.append("")
        L += ["```", ""]
    new = "\n".join(L)
    out = ptxt[:p0] + new + ptxt[p1:].split("\n", 1)[1].split("# 8 ", 1)[0].rstrip() + "\n\n"
    out = ptxt[:p0] + new + "\n# 8 " + ptxt.split("# 8 ", 1)[1]
    open(PLAN, "w", encoding="utf-8").write(out)
    json.dump({"old2new": o2n, "cut": [r["n"] for r in rows if r["n"] and r["n"] not in o2n]},
              open("manuscript/企画書/番号対応表_S1.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("  現行案.md を50本に書き換えた。番号対応表_S1.json を出した。")
    moved = {o: n for o, n in o2n.items() if o != n}
    print("  番号が変わったもの %d本" % len(moved))
    import glob
    hits = []
    for f in glob.glob("manuscript/本文/**/*.md", recursive=True) + ["manuscript/序章_v12.md"]:
        if "吸収済み" in f: continue
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            for m in re.finditer(r'(\d{1,2})番', line):
                hits.append((f, i, m.group(1), line.strip()[:50]))
    if hits:
        print("  本文の N番 参照　%d か所。直しはこちらでやる。" % len(hits))
        for f, i, n, s in hits[:12]:
            print("    %s:%s  %s番  %s" % (os.path.basename(f), i, n, s))

if __name__ == "__main__":
    main()
