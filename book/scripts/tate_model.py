# -*- coding: utf-8 -*-
# 縦書きにした時に、何ページになるかを、行の数で数える（目安）。
#   python3 -I scripts/tate_model.py            → 類書と同じ組み方（1行40字、1ページ16行）
#   python3 -I scripts/tate_model.py 44 18      → 字を少し小さくした時（1行44字、1ページ18行）
#   -v をつけると、項目ごとの数を出す
# 前提：改行は最低限（文をつなげて段落にする）。ブロックは、項目の頭・2コマ・3STEP・まとめの4つだけ。
# 数え方は、見本（scripts/build_mock_tate.py）で実際に組んだ形に合わせてある。
import math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v4 as B

ROOT = os.path.dirname(HERE)
HEAD, KOMA, SHEET, MATOME = 3, 6, 7, 7   # ブロックが使う行（項目の頭／2コマ／3STEPと基準／まとめ）
PARA_MAX = 170                           # 1つの段落にまとめる長さの上限（字）
ILL = 8                                  # 挿絵（［挿絵：…］の行）が使う行。半ページで数える


def body_rows(md, W, merge=True, gap=0.0):
    """本文（## 見出しつきのmd）が、縦書きで何行になるか。小見出しは2行ぶん（最初の問いは1行）。"""
    rows, buf, code, first = 0.0, "", False, True
    def flush():
        nonlocal rows, buf
        if buf:
            rows += math.ceil((len(buf) + 1) / W) + gap
            buf = ""
    for line in md.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            flush(); code = not code; continue
        if code:
            rows += max(1, math.ceil(len(s) / (W - 2))); continue
        if not s or s == "---":
            continue
        if s.startswith("［挿絵"):
            flush(); rows += ILL; first = False; continue
        if s.startswith("#"):
            flush(); rows += 1 if first else 2; first = False; continue
        first = False
        s = s.replace("==", "")
        plain = s.endswith("。") and not s.startswith(("「", "・", "×", "○", "|")) and not line.startswith("　　")
        if merge and plain:
            if buf and len(buf) + len(s) > PARA_MAX:
                flush()
            buf += s
        else:
            flush(); rows += math.ceil(len(s) / W) + gap
    flush()
    return rows


def pages_for(r, R, head=HEAD):
    """本文r行の項目が、何ページになるか。ブロックは、ページをまたがせない。"""
    pos = head + r
    for blk in (KOMA, SHEET, MATOME):
        if pos % R + blk > R:
            pos = math.ceil(pos / R) * R
        pos += blk
    return math.ceil(pos / R)


def cap(pages, R):
    """pagesページの項目に入る本文の行（最後のページに3STEPとまとめ、その前のページの終わりに2コマ）。"""
    return (pages - 1) * R - HEAD - KOMA


def items(W):
    return [(kk, B.n(B.body(kk)), body_rows(B.body(kk), W)) for kk in B.all_items()]


def fit(its, R, budget):
    """項目に使えるページがbudgetの時。全部4ページから始めて、削る量が大きい項目から6ページにする。"""
    plan = {kk: 4 for kk, c, r in its}
    used = 4 * len(its)
    gain = sorted(((min(r, cap(6, R)) - cap(4, R), r, kk) for kk, c, r in its if r > cap(4, R)), reverse=True)
    for g, _, kk in gain:
        if used + 2 > budget:
            break
        plan[kk] = 6; used += 2
    cut = sum(max(0, r - cap(plan[kk], R)) * c / r for kk, c, r in its)
    return plan, used, cut


def sec(md, name):
    m = re.search(r"(?ms)^## %s.*?\n(.*?)(?=^## |\Z)" % re.escape(name), md)
    return m.group(1) if m else ""


def others(W, R):
    """07〜45番のほかの部分のページ（完全版から数える）。"""
    t = open(os.path.join(ROOT, "manuscript", "完全版", "完全版_仮.md"), encoding="utf-8").read()
    out = {"第1章の項目": [], "コラム": [], "章の扉と導入": [], "前付け・巻末": []}
    for s in [x for x in re.split(r"(?m)^(?=# )", t) if x.strip()]:
        h = s.split("\n", 1)[0][2:]
        body = s.split("\n", 1)[1] if "\n" in s else ""
        m = re.match(r"(\d{2})[　 ]", h)
        if m and int(m.group(1)) <= 6:   # 章最初のページに1ページ。導入文と本文は続けて流す
            r = body_rows(sec(s, "導入文"), W) + body_rows(sec(s, "本文"), W)
            out["第1章の項目"].append((h[:2], 1 + pages_for(r, R)))
        elif m or h.startswith("■"):
            continue
        elif h.startswith("コラム"):
            out["コラム"].append((h[4:12], max(1, math.ceil((2 + body_rows(body, W)) / R))))
        elif re.match(r"第[1-5]章", h):
            out["章の扉と導入"].append((h[:3], 1 + math.ceil(body_rows(body, W) / R)))
        else:
            out["前付け・巻末"].append((h[:14], math.ceil((2 + body_rows(body, W, merge=False)) / R)))
    return out


def main():
    nums = [a for a in sys.argv[1:] if a.isdigit()]
    W, R = (int(nums[0]), int(nums[1])) if len(nums) == 2 else (40, 16)
    its = items(W)
    print("組み方：1行%d字、1ページ%d行" % (W, R))
    free = even = base = 0
    cls = {}
    for kk, c, r in its:
        p = pages_for(r, R); e = p + p % 2
        free += p; even += e
        cls.setdefault(p, []).append(kk)
        # 何も変えない時：今の改行（段落のあいだを半行あける）。質問ページ1ページ、2コマ半ページ、3STEP1ページ、まとめ半ページ
        r0 = body_rows(B.body(kk), W, merge=False, gap=0.5)
        base += math.ceil(r0 / R) + 3
        if "-v" in sys.argv:
            print(kk, "%5d字 本文%5.1f行 → %dページ" % (c, r, p))
    print("07〜45番　何も変えない：%dページ／改行とブロックを最低限に（削らない）：%dページ（見開きの頭から始めるなら %d）" % (base, free, even))
    for p in sorted(cls):
        print("　%dページ：%d個　%s" % (p, len(cls[p]), " ".join(cls[p])))
    per = sum(c for _, c, _ in its) / sum(r for _, _, r in its)
    for pg in (4, 6, 8):
        print("　%dページの項目に入る本文：%d行 ≒ 約%d字" % (pg, cap(pg, R), cap(pg, R) * per))
    for budget in (160, 170, 180, 190, 200):
        plan, used, cut = fit(its, R, budget)
        n6 = sorted(k for k in plan if plan[k] == 6)
        print("　項目に%dページ使える時：4ページ×%d個＋6ページ×%d個＝%dページ。削るのは約%d字。6ページ：%s"
              % (budget, len(plan) - len(n6), len(n6), used, cut, " ".join(n6)))
    for k, v in others(W, R).items():
        print("　%s：%s　合わせて %dページ" % (k, " ".join("%s=%d" % x for x in v), sum(x[1] for x in v)))


if __name__ == "__main__":
    main()
