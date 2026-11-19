# -*- coding: utf-8 -*-
# 第2章〜第5章（07〜45番）を、5章・45項目の目次で組む。案・第1版（2026-11-19）。
#   python3 -I scripts/assemble_v4.py           → manuscript/v4/ に書き出す
#   python3 -I scripts/assemble_v4.py --check   → 字数と抜けを調べるだけ
# 形：章の最初にだけ導入文。章の中は、番号のない小見出しで分ける。
#     項目は、質問ページ → 本文 → 2コマ → 3STEP → できた基準 → まとめ。
# もとの材料：
#   目次と、項目ごとの組み立て   scripts/v4_data.py
#   前の本文（v2・v3）          manuscript/本文/v2/NN.md（assemble_v3.body_of で読む）
#   新しく書いた文              manuscript/本文/v4/
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v4_data as V
import v3_data as D
import assemble_v3 as A
import taihi_card_v2 as T
import step_card_v1 as S1

ROOT = os.path.dirname(HERE)
NEW = os.path.join(ROOT, "manuscript", "本文", "v4")
OUT = os.path.join(ROOT, "manuscript", "v4")
n = A.n


def read_new(name):
    with open(os.path.join(NEW, name + ".md"), encoding="utf-8") as f:
        return f.read().strip() + "\n"


def remap(t, where=""):
    """前の番号の「〜番」を、新しい番号に直す。01〜06は、そのまま。"""
    def f(m):
        k = m.group(1)
        if int(k) <= 6:
            return m.group(0)
        if k not in V.OLD2NEW:
            raise SystemExit("%s: 新しい目次にない番号を指している: %s番" % (where, k))
        return V.OLD2NEW[k] + "番"
    return re.sub(r"(?<![0-9])([0-9]{2})番", f, t)


def old_secs(kk, start=None, stop=None, drop=()):
    """前の本文の、見出しstart（含む）から見出しstop（含まない）まで。"""
    secs = re.split(r"(?m)^(?=## )", A.body_of(kk))
    heads = [s.split("\n", 1)[0] for s in secs]
    def idx(key):
        hit = [i for i, h in enumerate(heads) if h.startswith("## ") and key in h]
        if len(hit) != 1:
            raise SystemExit("%s: 見出し「%s」が %d 個" % (kk, key, len(hit)))
        return hit[0]
    a = idx(start) if start else 0
    b = idx(stop) if stop else len(secs)
    keep = [s for s, h in zip(secs[a:b], heads[a:b]) if not any(d in h for d in drop)]
    return "".join(keep).strip() + "\n"


def body(kk):
    it = V.ITEMS[kk]
    parts = it.get("parts") or [("old", it["old"], None, None)]
    out, used = [], set()
    for p in parts:
        if p[0] == "file":
            out.append(read_new(p[1]))
        else:
            t = old_secs(p[1], p[2], p[3], it.get("drop", ()))
            for a, b in it.get("pre", ()):
                used.add(a) if a in t else None
                t = t.replace(a, b)
            t = remap(t, kk)
            for a, b in it.get("fix", ()):
                used.add(a) if a in t else None
                t = t.replace(a, b)
            out.append(t)
    for a, b in list(it.get("pre", ())) + list(it.get("fix", ())):
        if a not in used:
            raise SystemExit("%s: 入れかえる言葉が見つからない: %s" % (kk, a))
    return "\n".join(out).strip() + "\n"


def koma(kk):
    it = V.ITEMS[kk]
    return it.get("koma") or (T.C.get(int(it["old"])) or T.C.get(it["old"]))


def sheet(kk):
    """(題, [(見出し, 声, 補足)], 基準)"""
    it = V.ITEMS[kk]
    if "sheet" in it:
        ttl, steps, king = it["sheet"]
        return ttl, [(h, v, None) for h, v in steps], king
    o = it["old"]
    steps, king = D.SHEET[o]
    notes = getattr(D, "SHEET_NOTE", {})
    return (it.get("ttl") or S1.S[o][0],
            [(remap(h, kk), remap(v, kk), remap(notes[(o, i)], kk) if (o, i) in notes else None)
             for i, (h, v) in enumerate(steps, 1)],
            remap(king, kk))


def matome(kk):
    it = V.ITEMS[kk]
    one, pts, dakara, toi = it.get("matome") or D.MATOME[it["old"]]
    return remap(one, kk), [remap(p, kk) for p in pts], remap(dakara, kk), remap(toi, kk)


def item_md(kk):
    it = V.ITEMS[kk]
    c = koma(kk)
    ttl, steps, king = sheet(kk)
    one, pts, dakara, toi = matome(kk)
    L = ["# %s　%s" % (kk, it["t"]), "", "## 質問ページ", "",
         "頭のいい人が絶対やらないこと", "「%s」" % it["q"], "じゃあ、何をするの？", "", "## 本文", ""]
    b = body(kk)
    b = re.sub(r"^### ", "#### ", b, flags=re.M)
    b = re.sub(r"^## ", "### ", b, flags=re.M)
    L += [b.rstrip(), "", "## 頭のいい人と伸びない人の違い", "",
          "伸びない人", c[0][0], c[0][1], "", "頭のいい人", c[1][0], c[1][1], "",
          "## 今日からできる3STEP", "", "題：頭のいい人の『%s』3STEP" % ttl, ""]
    for i, (h, v, note) in enumerate(steps, 1):
        L += ["STEP0%d" % i, h, "「%s」" % v]
        if note:
            L.append("※" + note)
        L.append("")
    L += ["## できた基準", "", king, "", "## まとめ", "", one, "", "```"]
    L += ["　　%d　%s" % (i, p) for i, p in enumerate(pts, 1)]
    L += ["```", "", dakara, "迷ったら、自分に聞きます。「%s」" % toi, ""]
    return "\n".join(L)


def chapter_md(ch):
    num, fuda, title, sub, groups = ch
    L = ["# 第%d章　【%s】%s" % (num, fuda, title)]
    if sub:
        L.append(sub)
    L += ["", "## 章の導入文", "", read_new("ch%d_導入" % num).strip(), ""]
    for name, items in groups:
        if name:
            L += ["---", "", "# ■ %s" % name, ""]
        for kk in items:
            L += ["---", "", item_md(kk)]
    return "\n".join(L)


def mokuji_md():
    L = ["# 目次（第2章〜第5章　07〜45番）", ""]
    for num, fuda, title, sub, groups in V.CHAPTERS:
        L += ["## 第%d章　【%s】%s" % (num, fuda, title)]
        if sub:
            L.append(sub)
        L.append("")
        for name, items in groups:
            if name:
                L += ["■ %s" % name, ""]
            for kk in items:
                it = V.ITEMS[kk]
                L += ["%s　%s" % (kk, it["t"]), "　　×　%s" % it["x"], "　　○　%s" % it["o"], ""]
    return "\n".join(L)


def all_items():
    return [kk for ch in V.CHAPTERS for _, items in ch[4] for kk in items]


def check():
    ng = 0
    ks = all_items()
    if ks != ["%02d" % k for k in range(7, 46)]:
        print("項目の並びが、07〜45になっていない"); ng += 1
    for kk in ks:
        ttl, steps, king = sheet(kk)
        if n(ttl) > 6:
            print(kk, "題 %d字: %s" % (n(ttl), ttl)); ng += 1
        for i, (h, v, note) in enumerate(steps, 1):
            if n(h) > 24:
                print(kk, "STEP0%d 見出し %d字: %s" % (i, n(h), h)); ng += 1
            if n(v) > 14:
                print(kk, "STEP0%d 声 %d字: %s" % (i, n(v), v)); ng += 1
        if n(king) > 36:
            print(kk, "基準 %d字: %s" % (n(king), king)); ng += 1
        for big, small in koma(kk):
            if n(big.strip("「」")) > 8 or n(small) > 14:
                print(kk, "2コマ 長い:", big, small); ng += 1
        b = body(kk)
        for w in ("今日やること　", "### STEP", "「できた」の基準", "この場面のまとめ"):
            if w in b:
                print(kk, "本文に残っている:", w); ng += 1
        if "*" in item_md(kk):
            print(kk, "アスタリスクがある"); ng += 1
        for m in re.finditer(r"(?<![0-9])([0-9]{2})番", item_md(kk)):
            if not 1 <= int(m.group(1)) <= 45:
                print(kk, "ない番号:", m.group(0)); ng += 1
            if m.group(1) == kk:
                print(kk, "自分の番号を指している:", item_md(kk)[max(0, m.start() - 20):m.end() + 10].replace("\n", " ")); ng += 1
    return ng


def main():
    ng = check()
    total = 0
    write = "--check" not in sys.argv
    if write:
        os.makedirs(os.path.join(OUT, "貼り付け用"), exist_ok=True)
    whole = []
    for ch in V.CHAPTERS:
        md = chapter_md(ch)
        tx = A.to_paste(md)
        total += n(tx)
        whole.append(tx)
        print("第%d章　%2d項目　%6d字" % (ch[0], sum(len(g[1]) for g in ch[4]), n(tx)))
        if write:
            with open(os.path.join(OUT, "第%d章.md" % ch[0]), "w", encoding="utf-8") as f:
                f.write(md)
            with open(os.path.join(OUT, "貼り付け用", "第%d章.txt" % ch[0]), "w", encoding="utf-8") as f:
                f.write(tx)
    if write:
        with open(os.path.join(OUT, "目次.md"), "w", encoding="utf-8") as f:
            f.write(mokuji_md())
        with open(os.path.join(OUT, "貼り付け用", "第2章から第5章_全部.txt"), "w", encoding="utf-8") as f:
            f.write(A.to_paste(mokuji_md()) + "\n\n" + "\n\n".join(whole))
    for kk in all_items():
        if "--sizes" in sys.argv:
            print(kk, n(body(kk)), V.ITEMS[kk]["t"])
    print("合計 %d字　／　直す所 %d件" % (total, ng))


if __name__ == "__main__":
    main()
