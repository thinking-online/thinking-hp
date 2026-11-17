# -*- coding: utf-8 -*-
# 第2章から先（07〜50番）を、新しい形で組む。案・第1版（2026-11-17）。
#   python3 -I scripts/assemble_v3.py           → manuscript/v3/ に書き出す
#   python3 -I scripts/assemble_v3.py --check   → 字数と抜けを調べるだけ
# 形（著者の指示）：章の最初にだけ導入文。項目は、質問ページ → 本文 → 2コマ → 3STEP → できた基準 → まとめ。
# もとの材料：
#   章の導入文      manuscript/本文/v2/chN_扉.md
#   質問ページの言葉 scripts/mokuji_v5.py の PAIR（×のほう）
#   本文            manuscript/本文/v2/NN.md（最後の「この場面のまとめ」は外す。「やり方」は①②③にして残す）
#   2コマ           scripts/taihi_card_v2.py の C
#   3STEP・まとめ    scripts/v3_data.py の SHEET・MATOME。シートの題は scripts/step_card_v1.py の題
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v3_data as D
import mokuji_v5 as M5
import taihi_card_v2 as T
import step_card_v1 as S1

ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "manuscript", "本文", "v2")
OUT = os.path.join(ROOT, "manuscript", "v3")
MARU = {"01": "①", "02": "②", "03": "③"}


def n(s):
    return len(re.sub(r"\s", "", s))


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()


def body_of(kk):
    """本文。最後のまとめを外し、「やり方」のSTEPを①②③にし、基準の行を外す。"""
    t = read(kk + ".md")
    m = re.search(r"^## (この場面のまとめ|この法則のまとめ)\s*$", t, re.M)
    if not m:
        raise SystemExit(kk + ": まとめの見出しが見つからない")
    t = t[: m.start()]
    hook = getattr(D, "HOOK", {}).get(kk)
    if hook:  # 書き出し（最初の見出しの前）を、「こんな時、どうする？」の形に入れかえる
        h = re.search(r"^## ", t, re.M)
        t = hook.strip() + "\n\n" + t[h.start():]
    # 「頭の中」「やり方」「これをやると、何が残るか」の節は、外す（2コマ・3STEP・まとめに一本化。著者の指示）
    secs = re.split(r"(?m)^(?=## )", t)
    t = "".join(s for s in secs if not re.match(r"## (頭の中|やり方|これをやると、何が残るか)\s*\n", s))
    t = re.sub(r"(\n---\s*)+\s*$", "\n", t.rstrip() + "\n")
    return t.strip() + "\n"


def item_md(kk):
    k = int(kk)
    bad, good = M5.PAIR[kk] if kk in M5.PAIR else M5.PAIR[k]
    c = T.C.get(k) or T.C.get(kk)
    steps, king = D.SHEET[kk]
    one, pts, dakara, toi = D.MATOME[kk]
    title = S1.S[kk][0]
    L = []
    L.append("# %s　%s" % (kk, bad))
    L.append("")
    L.append("## 質問ページ")
    L.append("")
    L.append("頭のいい人が絶対やらないこと")
    L.append("「%s」" % bad)
    L.append("じゃあ、何をするの？")
    L.append("")
    L.append("## 本文")
    L.append("")
    b = body_of(kk)
    b = re.sub(r"^### ", "#### ", b, flags=re.M)
    b = re.sub(r"^## ", "### ", b, flags=re.M)
    L.append(b.rstrip())
    L.append("")
    L.append("## 頭のいい人と伸びない人の違い")
    L.append("")
    L += ["伸びない人", c[0][0], c[0][1], "", "頭のいい人", c[1][0], c[1][1], ""]
    L.append("## 今日からできる3STEP")
    L.append("")
    L.append("題：頭のいい人の『%s』3STEP" % title)
    L.append("")
    for i, (h, v) in enumerate(steps, 1):
        L += ["STEP0%d" % i, h, "「%s」" % v]
        note = getattr(D, "SHEET_NOTE", {}).get((kk, i))
        if note:
            L.append("※" + note)
        L.append("")
    L.append("## できた基準")
    L.append("")
    L.append(king)
    L.append("")
    L.append("## まとめ")
    L.append("")
    L.append(one)
    L.append("")
    L.append("```")
    for i, p in enumerate(pts, 1):
        L.append("　　%d　%s" % (i, p))
    L.append("```")
    L.append("")
    L.append(dakara)
    L.append("迷ったら、自分に聞きます。「%s」" % toi)
    L.append("")
    return "\n".join(L)


def chapter_md(ch):
    num, title, field, a, b = ch
    L = ["# 第%d章　【%s】%s" % (num, field, title), "", "## 章の導入文", "", read("ch%d_扉.md" % num).strip(), ""]
    for k in range(a, b + 1):
        L += ["---", "", item_md("%02d" % k)]
    return "\n".join(L)


def to_paste(md):
    """著者のGoogleドキュメントに貼る形（【】、⚫︎、■。マーカーと囲みの記号は外す）。"""
    out = []
    for l in md.split("\n"):
        if l.strip() == "```" or l.strip() == "---":
            continue
        l = l.replace("==", "")
        if l.startswith("#### "):
            out.append("■" + l[5:])
        elif l.startswith("### "):
            out.append("⚫︎" + l[4:])
        elif l.startswith("## "):
            out.append("【" + l[3:] + "】")
        elif l.startswith("# "):
            out.append(l[2:])
        else:
            out.append(l)
    s = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", s).strip() + "\n"


def check():
    ng = 0
    for ch in D.CHAPTERS:
        for k in range(ch[3], ch[4] + 1):
            kk = "%02d" % k
            for key, d in (("SHEET", D.SHEET), ("MATOME", D.MATOME)):
                if kk not in d:
                    print(kk, key, "がない"); ng += 1
            steps, king = D.SHEET[kk]
            for i, (h, v) in enumerate(steps, 1):
                if n(h) > 24:
                    print(kk, "STEP0%d 見出し %d字: %s" % (i, n(h), h)); ng += 1
                if n(v) > 14:
                    print(kk, "STEP0%d 声 %d字: %s" % (i, n(v), v)); ng += 1
            if n(king) > 36:
                print(kk, "基準 %d字: %s" % (n(king), king)); ng += 1
            c = T.C.get(k) or T.C.get(kk)
            for big, small in c:
                if n(big.strip("「」")) > 8 or n(small) > 14:
                    print(kk, "2コマ 長い:", big, small); ng += 1
            b = body_of(kk)
            for w in ("今日やること　", "### STEP", "「できた」の基準"):
                if w in b:
                    print(kk, "本文に残っている:", w); ng += 1
            if re.search(r"(?m)^## (頭の中|やり方|これをやると、何が残るか)\s*$", b):
                print(kk, "本文に、外すはずの節が残っている"); ng += 1
            if "*" in b:
                print(kk, "アスタリスクがある"); ng += 1
    return ng


def main():
    ng = check()
    total = 0
    rows = []
    for ch in D.CHAPTERS:
        md = chapter_md(ch)
        total += n(to_paste(md))
        rows.append((ch[0], ch[4] - ch[3] + 1, n(to_paste(md))))
        if "--check" not in sys.argv:
            os.makedirs(os.path.join(OUT, "貼り付け用"), exist_ok=True)
            with open(os.path.join(OUT, "第%d章.md" % ch[0]), "w", encoding="utf-8") as f:
                f.write(md)
            with open(os.path.join(OUT, "貼り付け用", "第%d章.txt" % ch[0]), "w", encoding="utf-8") as f:
                f.write(to_paste(md))
    for r in rows:
        print("第%d章　%2d項目　%6d字" % r)
    print("合計 %d字　／　直す所 %d件" % (total, ng))


if __name__ == "__main__":
    main()
