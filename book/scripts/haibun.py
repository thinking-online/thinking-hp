# -*- coding: utf-8 -*-
# 07〜45番の本文を、行で数える（1項目ずつ詰める時の道具）。
#   python3 -I scripts/haibun.py 10      → 10番の、小見出しごとの行、ページ、3STEPとまとめ、気をつける所
#   python3 -I scripts/haibun.py         → 全部の一覧（詰める前と、今）
# 数え方：A5・縦書き・1行40字・1ページ16行。項目の頭4行（題と、「かわりに」の行）＋本文＋終わり11行（文字の3STEP 5行、端的なまとめ 4行、前に1行ずつ空き）。
# 本当のページは、組んで数える：python3 -I scripts/build_tate_book.py new --nopdf
# 目安：柱の項目は6ページ（本文81行まで）、ほかは5ページ（本文65行まで）。
# 配分：問い（約12行）→ 理由（1つ。約10行）→ やり方（本文の半分以上。29行目までに始める）→ つまずく所（1〜2つ）。
import math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v4 as B
import tate_model as M

ROOT = os.path.dirname(HERE)
MAE = os.path.join(ROOT, "manuscript", "本文", "v4", "詰める前")
PILLAR = {"07", "11", "17", "19", "21", "29", "34", "37", "39"}
HEAD, OWARI, KOMA, R, W = 4, 11, 6, 16, 40


def limit(kk):
    return (6 if kk in PILLAR else 5) * R - HEAD - OWARI


def mae(kk):
    with open(os.path.join(MAE, kk + ".md"), encoding="utf-8") as f:
        return f.read()


def n(t):
    return len("".join(t.replace("==", "").split()))


def secs(b):
    """[(始まる行, 行の数, 見出し)]"""
    parts = re.split(r"(?m)^#{2,3} +(.+)$", b)
    out, acc = [], 0
    for i in range(1, len(parts), 2):
        h = parts[i].strip()
        r = int(M.body_rows("## " + h + "\n" + parts[i + 1], W)) + (1 if i > 1 else 0)
        out.append((acc + 1, r, h))
        acc += r
    return out


def pages(r, koma=False):
    return math.ceil((HEAD + r + OWARI + (KOMA if koma else 0)) / R)


def warn(kk, b):
    out, old = [], mae(kk)
    if not b.lstrip().startswith("## "):
        out.append("最初の行が、小見出し（## 問い）になっていない")
    if "*" in b:
        out.append("アスタリスクがある")
    num = lambda t: set(re.findall(r"\d+(?:\.\d+)?", t))
    extra = sorted(num(b) - num(old) - {kk})
    if extra:
        out.append("詰める前にない数字：" + " ".join(extra) + "（見本の中の数字ならよい。研究の数字は足さない）")
    uni = lambda t: set(re.findall(r"[一-龥ァ-ヶー]{2,}大学", t))
    if uni(b) - uni(old):
        out.append("詰める前にない大学名：" + " ".join(sorted(uni(b) - uni(old))))
    for w in ("証明", "必ず", "1位", "出来", "憶え", "科学的に正しい", "しましょう"):
        if b.count(w) > old.count(w):
            out.append("増えた言葉：" + w)
    for m in re.finditer(r"(\d{2})番", b):
        if not ("01" <= m.group(1) <= "45") or m.group(1) == kk:
            out.append("番号がおかしい：" + m.group(0))
    if b.count("==") % 2:
        out.append("==が、対になっていない")
    if b.count("==") > old.count("=="):
        out.append("強調（==）が増えた")
    code = False
    for line in b.split("\n"):
        if line.strip().startswith("```"):
            code = not code
        elif code and len(line.strip()) > W - 2:
            out.append("ブロックの1行が38字をこえる（2行に数える）：" + line.strip()[:16] + "…")
    if code:
        out.append("```が、閉じていない")
    r = int(M.body_rows(b, W))
    if r > limit(kk):
        out.append("本文が目安をこえている：%d行（目安 %d行まで）" % (r, limit(kk)))
    s = secs(b)
    if len(s) < 3:
        out.append("小見出しが少ない（%d個）" % len(s))
    return out


def show(kk):
    b, old = B.body(kk), mae(kk)
    r, r0 = int(M.body_rows(b, W)), int(M.body_rows(old, W))
    it = B.V.ITEMS[kk]
    print("%s番　×「%s」　○ %s　%s" % (kk, it["x"], it["o"], "【柱】" if kk in PILLAR else ""))
    print("詰める前：%d字・%d行・%dページ　→　今：%d字・%d行・%dページ（2コマを入れると%dページ）　目安：本文%d行まで"
          % (n(old), r0, pages(r0), n(b), r, pages(r), pages(r, True), limit(kk)))
    print("小見出し（始まる行／行の数）。2ページ目は、本文の29行目まで")
    for a, rr, h in secs(b):
        print("　%3d行目から　%2d行　%s" % (a, rr, h))
    ttl, steps, king = B.sheet(kk)
    print("3STEP")
    for i, (h, v, note) in enumerate(steps, 1):
        print("　STEP%02d　%s%s" % (i, h, ("　※" + note) if note else ""))
    print("　「できた」の基準：" + king)
    one, pts, dakara, toi = B.matome(kk)
    print("まとめ")
    print("　%s／%s／迷ったら、自分に聞きます。%s" % (one, dakara, toi if toi.startswith("「") else "「%s」" % toi))
    for p in pts:
        print("　（今の3つ）" + p)
    w = warn(kk, b)
    print("気をつける所：" + ("なし" if not w else ""))
    for x in w:
        print("　・" + x)


def table():
    tot0 = tot = 0
    for kk in B.all_items():
        b, old = B.body(kk), mae(kk)
        r, r0 = int(M.body_rows(b, W)), int(M.body_rows(old, W))
        tot0 += pages(r0); tot += pages(r)
        done = "済" if b.strip() != old.strip() else "　"
        w = warn(kk, b) if done == "済" else []
        print("%s %s %s　%4d字 %3d行 %dp　→　%4d字 %3d行 %dp（2コマ %dp）%s"
              % (kk, "柱" if kk in PILLAR else "　", done, n(old), r0, pages(r0), n(b), r, pages(r), pages(r, True),
                 ("　！" + str(len(w))) if w else ""))
    print("07〜45番のページ：詰める前 %d　→　今 %d" % (tot0, tot))


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("-")]
    if a:
        for kk in a:
            show(kk)
    else:
        table()
