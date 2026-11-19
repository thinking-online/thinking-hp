# -*- coding: utf-8 -*-
# 07〜45番の「STEPが本文」の形（削った版）。文は manuscript/本文/v5/NN.md に置く。
#   python3 -I scripts/v5.py show 14        → その項目の材料（今の本文、STEPの見出しと声、行の上限）を出す
#   python3 -I scripts/v5.py check 14 15    → 形と、行の数を調べる（番号なしなら、ある分を全部）
# ファイルの形（1行＝1段落。空の行は、あってもなくてもいい）：
#   # 14
#   ## 問い                  1行目が、問い（太字になる）。続けて、短い行や、答えの段落
#   ## なぜ｜小見出しの言葉    1〜2個
#   ## STEP01               見出しと声は、3STEPのデータから入る。ここには、説明の段落だけを書く
#   ## STEP02
#   ## STEP03
#   ## ほか｜小見出しの言葉    0〜3個
#   行の頭が全角の空白2つ「　　」の行は、型や×○などの「そのまま置く行」（段落にしない。1行ずつ字下げで置く）
# 項目の頭（番号・×の題・○）、「できた」の基準、自分への問い、2コマ、王様の一言は、データから入る。ファイルには書かない。
import math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v4 as B
import v4_data as V
import v3_data as D
import book_data as K

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "manuscript", "本文", "v5")
W, R = 40, 16
PILLAR = {"07", "09", "17", "19", "21", "29", "34", "37", "39"}     # 6ページの項目（2コマを置く）。ほかは4ページ
HEAD, GOAL, HITO, KOMA, SLACK = 4, 3, 3, 6, 2     # ブロックが使う行と、ゆとり
KINDS = ("問い", "なぜ", "STEP01", "STEP02", "STEP03", "ほか")


def pages(kk):
    return 6 if kk in PILLAR else 4


def cells(s):
    """縦書きで使うます目の数。2けたの数字は、横に並べて1ます。"""
    return len(re.sub(r"(?<![0-9])[0-9]{2}(?![0-9])", "0", s.replace("==", "")))


def parse(kk):
    """[(種類, 小見出し, [行])]。行は (そのまま置く行かどうか, 文)。"""
    with open(os.path.join(DIR, kk + ".md"), encoding="utf-8") as f:
        ls = f.read().split("\n")
    if ls[0].strip() != "# " + kk:
        raise SystemExit("%s: 1行目は「# %s」" % (kk, kk))
    secs = []
    for l in ls[1:]:
        if l.startswith("## "):
            head = l[3:].strip()
            kind, _, title = head.partition("｜")
            if kind not in KINDS:
                raise SystemExit("%s: 見出しの種類がちがう: %s" % (kk, l))
            secs.append((kind, title.strip(), []))
        elif l.strip():
            if not secs:
                raise SystemExit("%s: 見出しの前に文がある: %s" % (kk, l[:20]))
            secs[-1][2].append((l.startswith("　　"), l.strip()))
    return secs


def line_rows(fixed, s):
    return math.ceil((cells(s) + (2 if fixed else 1)) / W)


def rows(kk):
    secs = parse(kk)
    r = HEAD
    for kind, title, lines in secs:
        if kind == "問い":
            r += math.ceil(cells(lines[0][1]) / 37) + sum(line_rows(f, s) for f, s in lines[1:])
        else:
            r += 2 + (1 if kind.startswith("STEP") else 0) + sum(line_rows(f, s) for f, s in lines)
    return r + (KOMA if kk in PILLAR else 0) + GOAL + (HITO if kk in K.HITOKOTO else 0)


def budget(kk):
    return pages(kk) * R - SLACK


def text(kk):
    return "\n".join(s for _, _, lines in parse(kk) for _, s in lines)


def problems(kk):
    out = []
    secs = parse(kk)
    kinds = [k for k, _, _ in secs]
    if kinds[0] != "問い":
        out.append("最初は「## 問い」")
    if [k for k in kinds if k.startswith("STEP")] != ["STEP01", "STEP02", "STEP03"]:
        out.append("STEP01〜03が、順番に1個ずつない")
    if "なぜ" not in kinds:
        out.append("「## なぜ｜」がない")
    for kind, title, lines in secs:
        if kind in ("なぜ", "ほか") and not title:
            out.append("%s の小見出しがない" % kind)
        if kind in ("なぜ", "ほか") and cells(title) > 26:
            out.append("小見出しが長い（26字まで）: " + title)
        if not lines:
            out.append("%s が空" % kind)
        for fixed, s in lines:
            if not fixed and cells(s) > 200:
                out.append("段落が長い（%d字。200字まで）: %s" % (cells(s), s[:16]))
    t = text(kk)
    old = B.body(kk) + "".join(h + v + (n or "") for h, v, n in B.sheet(kk)[1]) + "".join(str(x) for x in B.matome(kk)) + B.sheet(kk)[2]
    if "*" in t:
        out.append("アスタリスクがある")
    for w in ("証明", "必ず", "1位", "絶対に"):
        if w in t and w not in old:
            out.append("今の原稿にない強い言葉: " + w)
    for m in re.finditer(r"(?<![0-9])([0-9]{2})番", t):
        if not 1 <= int(m.group(1)) <= 45 or m.group(1) == kk:
            out.append("番号がおかしい: " + m.group(0))
    new_num = sorted(set(re.findall(r"[0-9]+(?:\.[0-9]+)?", t)) - set(re.findall(r"[0-9]+(?:\.[0-9]+)?", old)) - {"3"})
    if new_num:
        out.append("今の原稿にない数字: " + " ".join(new_num))
    new_uni = sorted(set(re.findall(r"[ァ-ヶー一-龥]+大学", t)) - set(re.findall(r"[ァ-ヶー一-龥]+大学", old)))
    if new_uni:
        out.append("今の原稿にない大学名: " + " ".join(new_uni))
    r, b = rows(kk), budget(kk)
    if r > b:
        out.append("行が多い：%d行（上限%d行）。あと%d行、削る" % (r, b, r - b))
    return out


def show(kk):
    it = V.ITEMS[kk]
    ttl, steps, king = B.sheet(kk)
    one, pts, dakara, toi = B.matome(kk)
    fix = HEAD + GOAL + (KOMA if kk in PILLAR else 0) + (HITO if kk in K.HITOKOTO else 0) + 2 * 4 + 3
    print("==== %s　%s" % (kk, it["t"]))
    print("○：%s　／　%dページ　／　行の上限 %d行（うち、項目の頭・箱・見出し4つ・声3つで %d行。文に使えるのは 約%d行）"
          % (it["o"], pages(kk), budget(kk), fix, budget(kk) - fix))
    print("今の本文：%d字、縦書きで 約%d行" % (B.n(B.body(kk)), __import__("tate_model").body_rows(B.body(kk), W)))
    for i, (h, v, note) in enumerate(steps, 1):
        print("STEP0%d　%s　／声「%s」%s" % (i, h, v, ("　／※" + note) if note else ""))
    print("「できた」の基準：%s" % king)
    print("自分への問い：%s" % toi)
    print("今のまとめ：%s／%s／%s" % (one, "・".join(pts), dakara))
    print("---- 今の本文")
    print(B.body(kk))


def main():
    cmd, ks = sys.argv[1], sys.argv[2:]
    if cmd == "show":
        for kk in ks:
            show(kk)
        return
    ks = ks or sorted(f[:2] for f in os.listdir(DIR) if re.match(r"^[0-9]{2}\.md$", f))
    ng = 0
    for kk in ks:
        ps = problems(kk)
        ng += len(ps)
        print("%s　%dページ　%d行／上限%d行　%d字（今 %d字）　%s" % (kk, pages(kk), rows(kk), budget(kk), B.n(text(kk)), B.n(B.body(kk)), "OK" if not ps else ""))
        for p in ps:
            print("　　× " + p)
    print("調べた %d個／直す所 %d件" % (len(ks), ng))


if __name__ == "__main__":
    main()
