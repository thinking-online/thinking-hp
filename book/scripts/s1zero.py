# -*- coding: utf-8 -*-
"""S1　ゼロから出した生徒の言葉を、50本の項目に落とす。

　python3 scripts/s1zero.py           重なり・突き合わせ・章と力の数を見る
　python3 scripts/s1zero.py --write   現行案.md を新しい50本に書き換える

入力は manuscript/企画書/S1_ゼロから.md。
　「生徒の言葉」
　　→　やっていること
の2行で1本。考え方は docs/38。
"""
import re, sys, json, difflib, os
from collections import Counter

SRC  = "manuscript/企画書/S1_ゼロから.md"
PLAN = "manuscript/企画書/現行案.md"
WORD = "選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力"
BUCKET_CH = {"1": "授業", "2": "集中", "3": "暗記", "4": "演習", "5": "復習",
             "6": "戦略", "7": "戦略", "8": "本番", "9": "モチベ", "10": "モチベ"}

def norm(s): return re.sub(r'[、。「」『』？！\s　・…\-ー]', '', s)

def read_src():
    t = open(SRC, encoding="utf-8").read()
    t = t.split("\n---\n", 1)[1] if "\n---\n" in t else t
    rows, cur, curno = [], None, None
    for line in t.split("\n"):
        h = re.match(r'^## (\d+)[　\s]+(.+?)\s*$', line)
        if h: curno, cur = h.group(1), h.group(2).strip(); continue
        if line.strip().startswith("## "): cur = None; continue
        q = re.match(r'^[\s　]*「(.+?)」?\s*$', line)
        if q and cur and q.group(1).strip():
            rows.append({"q": q.group(1).strip().rstrip("」"), "a": "",
                         "bk": curno, "bkname": cur}); continue
        a = re.match(r'^[\s　]*(?:→|->)[\s　]*(.+?)\s*$', line)
        if a and rows and not rows[-1]["a"]: rows[-1]["a"] = a.group(1).strip()
    return [r for r in rows if r["q"]]

def read_plan():
    t = open(PLAN, encoding="utf-8").read()
    m = re.search(r'^# 7 (\d+)項目$', t, flags=re.M)
    if not m: return [], t, 0, 0
    sec = t[m.end():].split("# 8 ")[0]
    out, cur, last = [], None, None
    for line in sec.split("\n"):
        h = re.match(r'^## (.+?)[\s　]+(\d+)本\s*$', line)
        if h: cur = re.split(r'[\s　]+', h.group(1).strip())[-1]; continue
        it = re.match(r'^(\d{2})　(.+)$', line.rstrip())
        if it and cur:
            w = re.search(WORD, it.group(2))
            out.append({"n": it.group(1), "ch": cur, "w": w.group(0) if w else "",
                        "t": re.sub(r'[\s　]*(★厚く書く|★新規|［\d+p］|' + WORD + r')', '', it.group(2)).strip(),
                        "x": "", "o": ""})
            last = out[-1]; continue
        p = re.match(r'^[\s　]+(×|○)「(.*)」\s*$', line)
        if p and last: last["x" if p.group(1) == "×" else "o"] = p.group(2)
    return out, t, m.start(), m.end()

def main():
    rows = read_src()
    plan, ptxt, p0, p1 = read_plan()
    if not rows:
        print("=" * 64)
        print("  %s に、まだ1本も書かれていない。" % SRC)
        print("  まず「生徒の言葉」だけ、思い出せるだけ並べる。50ではなく70を目指す。")
        print("=" * 64); return

    bk = Counter(r["bkname"] for r in rows)
    print("=" * 64)
    print("  出た数　%d本" % len(rows))
    print("=" * 64)
    for k, v in bk.items(): print("  %-28s %2d本" % (k, v))
    noar = [r for r in rows if not r["a"]]
    print()
    if len(rows) < 60:
        print("  ★ まだ %d本。70を目指す。足りないカテゴリに戻る。" % len(rows))
        print()

    # 重なり
    dup = []
    for i, a in enumerate(rows):
        for b in rows[i+1:]:
            key_a, key_b = norm(a["a"] or a["q"]), norm(b["a"] or b["q"])
            if difflib.SequenceMatcher(None, key_a, key_b).ratio() > 0.62:
                dup.append((a, b))
    if dup:
        print("  重なっているかもしれない　%d組" % len(dup))
        print("  （やることが同じなら1本に。違うなら2本のまま）")
        for a, b in dup[:15]:
            print("    ・%s" % (a["a"] or a["q"])[:34])
            print("      %s" % (b["a"] or b["q"])[:34])
        print()

    if noar:
        print("  矢印がまだ　%d本（これが見出しになる。書けないものは本にならない）" % len(noar))
        for r in noar[:10]: print("    「%s" % r["q"][:40])
        print()

    # いまの51本との突き合わせ
    if plan:
        # 見出し・×・○ のどれかに当たれば、同じ項目とみなす
        cands = [(p, [norm(p["t"]), norm(p["x"]), norm(p["o"])]) for p in plan]
        hit, new = {}, []
        for r in rows:
            probes = [norm(r["a"]), norm(r["q"])]
            probes = [x for x in probes if x]
            best, score = None, 0.0
            for p, ks in cands:
                v = max(difflib.SequenceMatcher(None, a, b).ratio()
                        for a in probes for b in ks if b)
                if v > score: best, score = p, v
            if score >= 0.5:
                hit.setdefault(best["n"], []).append(r); r["plan"] = best
            else:
                new.append(r); r["plan"] = None
        KIHON = plan[0]["ch"] if plan else ""
        nomatch = [p for p in plan if p["n"] not in hit and p["ch"] != KIHON]
        kihon_miss = [p for p in plan if p["n"] not in hit and p["ch"] == KIHON]
        print("  いまの%d本との突き合わせ" % len(plan))
        print("    原稿がある　　　%2d本　書き直すだけ" % len(hit))
        print("    ゼロから書く　　%2d本　1本あたり2時間" % len(new))
        print("    出てこなかった　%2d本" % len(nomatch))
        print()
        if new:
            print("  ゼロから書くもの")
            print("  （下の「出てこなかったもの」と見比べる。言い方が違うだけで同じものがある）")
            for r in new[:20]:
                print("    ・%s" % (r["a"] or r["q"])[:46])
            print()
        if kihon_miss:
            print("  基本の基本 %d本は、生徒の言葉から出てこなくて当たり前（場面ではなく原理）。" % len(kihon_miss))
            print("  この8本はゼロから出し直さない。そのまま残す。")
            print()
        if nomatch:
            print("  いまの本にあるが、今回出てこなかったもの")
            print("  （これを言う生徒が、この1年で1人もいなかったか。いたなら戻す）")
            for p in nomatch[:25]: print("    %s  %s" % (p["n"], p["t"]))
            print()
        n = len(new)
        print("  " + ("2日の下書きに収まる。" if n <= 5 else
                      "その章は2日目に回す。" if n <= 12 else
                      "ゼロから書くのが多すぎる。いまの本に寄せるか、締切を1日延ばす。"))
        print()

    ch = Counter(BUCKET_CH.get(r["bk"], "？") for r in rows)
    print("  章の目安（カテゴリから機械で割ったもの。S1-6 で手で直す）")
    for c, v in ch.items():
        mk = "　← 薄い" if v <= 2 else ("　← 多い" if v >= 9 else "")
        print("    %-8s %2d本%s" % (c, v, mk))
    print("=" * 64)
    d = len(rows) - 50
    if d > 0: print("  50本まで、あと %d本 削る。docs/38 の S1-5 の順番で。" % d)
    elif d < 0: print("  50本まで、あと %d本 足りない。S1-1 に戻る。" % -d)
    else: print("  ちょうど50本。--write で現行案に書き込める。")
    print("=" * 64)

    if "--write" not in sys.argv: return
    if not (48 <= len(rows) <= 55):
        print("  48〜55本にしてから --write する。"); return
    bad = [r for r in rows if not r["a"]]
    if bad:
        print("  矢印が %d本 空。見出しが作れないので書き込めない。" % len(bad)); return

    order, o2n = [], {}
    seen = []
    for r in rows:
        r["ch"] = r.get("ch") or BUCKET_CH.get(r["bk"], "その他")
        if r["ch"] not in seen: seen.append(r["ch"])
    num = 0
    L = ["# 7 %d項目" % len(rows), "",
         "ゼロから出し直した版（docs/38）。生徒の言葉から起こしている。",
         "各項目の右肩に力を1つ。［Np］は目標ページ。", ""]
    for c in seen:
        mine = [r for r in rows if r["ch"] == c]
        L += ["## %s　　%d本" % (c, len(mine)), "", "```"]
        for r in mine:
            num += 1; nn = "%02d" % num
            p = r.get("plan")
            if p: o2n[p["n"]] = nn
            w = (p or {}).get("w", "")
            L.append("%s　%s%s　［4p］" % (nn, r["a"], ("　" + w) if w else ""))
            L.append("　　×「%s」" % (p or {}).get("x", ""))
            L.append("　　○「%s」" % (p or {}).get("o", ""))
            L.append("")
        L += ["```", ""]
    open(PLAN, "w", encoding="utf-8").write(ptxt[:p0] + "\n".join(L) + "\n# 8 " + ptxt.split("# 8 ", 1)[1])
    json.dump({"old2new": o2n}, open("manuscript/企画書/番号対応表_S1.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    qs = ["# Q　生徒が実際に言う言葉", "", "S1でゼロから出したものを、そのまま並べた。", ""]
    num = 0
    for c in seen:
        qs += ["## %s" % c, ""]
        for r in [r for r in rows if r["ch"] == c]:
            num += 1; qs.append("%02d　%s" % (num, r["q"]))
        qs.append("")
    open("manuscript/企画書/Q50.md", "w", encoding="utf-8").write("\n".join(qs))
    print("  現行案.md を %d本に書き換えた。Q50.md も生徒の言葉で作り直した。" % len(rows))
    print("  ×／○が空の項目は、埋めないと step.py の S1 が通らない。")

if __name__ == "__main__":
    main()
