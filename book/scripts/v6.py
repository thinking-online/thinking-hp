# -*- coding: utf-8 -*-
# 35個の版（第1章の6個 ＋ 29個）。形は、45個の版と同じ（問い・理由・やり方・つまずく所 → 文字の3STEP → 端的なまとめ）。
#   python3 -I scripts/v6.py rebuild       → 今の45個の版（本文/v4/NN.md）から、29個を作り直す（全部、上書きする）。
#                                            まとめた9個は、まとめ先の本文のあとに、本文/v6/足し/NN.md（まとめる相手のやり方）を足す
# 07番から先の本文は manuscript/本文/v6/NN.md に置く（NN は、35個の版での新しい番号）。
#   python3 -I scripts/v6.py init          → 今の原稿から、最初のファイルを作る（もうあるファイルは、上書きしない）
#   python3 -I scripts/v6.py show 14       → その項目の材料（今のファイル、まとめる相手の本文、行の上限、2コマ・3STEP・まとめ）
#   python3 -I scripts/v6.py check [14 …]  → 行の数、番号、今の原稿にない数字や大学名がないかを調べる
#   python3 -I scripts/v6.py map           → 番号の対応を出す
# ファイルの形：1行目は「# NN」。2行目から先は、今の本文と同じ形（最初の「## 」が問い。あとは「## 小見出し」と文。``` で囲んだ行は、そのまま置く行）。
# 45個の版（v4）の番号 → 35個の版（v6）の番号は、下の NEW の通り。まとめた項目は、まとめ先の番号になる。
import math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_v4 as B
import v4_data as V
import tate_model as M

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "manuscript", "本文", "v6")
W, R = 40, 16
# 章と小見出し。中の番号は、45個の版の番号
GROUPS = [
    (2, [("理解編", ["07", "08", "09", "10", "11"]), ("暗記編", ["12", "14", "15"])]),
    (3, [("問題の解き方", ["16", "17", "18", "19", "20"]), ("復習の仕方", ["21", "22", "24"])]),
    (4, [("計画編", ["25", "27", "29"]), ("集中編", ["30", "33", "34"]), ("モチベ編", ["35", "36", "37", "39"])]),
    (5, [("", ["41", "42", "45"])]),
]
ABSORB = {"13": "15", "23": "18", "26": "25", "28": "27", "31": "30", "32": "29", "38": "35", "40": "41", "43": "42"}   # まとめる項目 → まとめ先
TO_COLUMN = {"44"}                                                  # コラムに回す項目
PILLAR = {"07", "09", "17", "19", "21", "29", "34", "37", "39"}     # 柱の項目（今の長さのまま）

# まとめた項目の、目次に出る言葉（仮。まとめた中身が、目次から見えるようにするため。番号は、35個の版の番号）
OVERRIDE = {
    "14": dict(o="前に覚えたものや、絵・場面に、つなげる"),
    "17": dict(o="なぜ違うかを言う。2周目は、△と×だけ回す"),
    "23": dict(o="先週やった時間を見て、「何を、どこまで」で決める"),
    "24": dict(o="「○○したら、△△する」を1つ決める。ゼロの日は作らない"),
    "26": dict(t="音楽を聴きながら、スマホを横に置いて勉強する", o="無音か、歌詞のない音にする。スマホは、別の部屋に置く"),
    "29": dict(o="合格体験記を、先に自分で書く。「できない」には「まだ」を足す"),
    "33": dict(o="わかった最後の1行を、指で押さえる。途中で見せて、指摘をもらう"),
    "34": dict(o="考えるのは自分。AIには、ヒントと、力のつかない作業を任せる"),
}

KEEP = [k for _, gs in GROUPS for _, ks in gs for k in ks]
NEW = {k: "%02d" % (i + 7) for i, k in enumerate(KEEP)}
NEW.update({a: NEW[h] for a, h in ABSORB.items()})
OLD = {NEW[k]: k for k in KEEP}                                     # 新しい番号 → もとの番号（まとめ先の項目）
HOST = {NEW[h]: a for a, h in ABSORB.items()}                       # 新しい番号 → まとめる相手（もとの番号）


def renum(t, where=""):
    """45個の版の「NN番」を、35個の版の番号にする。01〜06は、そのまま。"""
    def f(m):
        k = m.group(1)
        if int(k) <= 6:
            return m.group(0)
        if k not in NEW:
            raise SystemExit("%s: 35個の版にない番号を指している: %s番" % (where, k))
        return NEW[k] + "番"
    return re.sub(r"(?<![0-9])([0-9]{2})番", f, t)


HEAD, OWARI = 4, 11   # 項目の頭4行（題と、「かわりに」の行）、終わり11行（文字の3STEP 5行、端的なまとめ 4行、前に1行ずつの空き）


def limit(nn):
    """(ページ, 本文の行の上限)。柱と、まとめた項目は6ページ。ほかは5ページ。"""
    pages = 6 if (OLD[nn] in PILLAR or nn in HOST) else 5
    return pages, pages * R - HEAD - OWARI


def pages_of(r):
    return math.ceil((HEAD + r + OWARI) / R)


# 作り直す時に、言葉を入れかえる所（35個の版の番号 → [(前, 後)]。番号を直す前の文に当てる）
FIX = {"31": [("この本にある45のうち", "この本にある35のうち")]}


def rebuild():
    """今の45個の版から、29個を作り直す。まとめた項目は、足し/NN.md を後ろにつける。"""
    os.makedirs(DIR, exist_ok=True)
    for nn in sorted(OLD):
        t = B.body(OLD[nn]).rstrip() + "\n"
        if nn in HOST:
            with open(os.path.join(DIR, "足し", nn + ".md"), encoding="utf-8") as f:
                t += "\n" + f.read().strip() + "\n"
        for a, b in FIX.get(nn, ()):
            if a not in t:
                raise SystemExit("%s: 入れかえる言葉が見つからない: %s" % (nn, a))
            t = t.replace(a, b)
        with open(path(nn), "w", encoding="utf-8") as f:
            f.write("# %s\n%s" % (nn, renum(t, nn)))
    print("作り直した %d個" % len(OLD))


def path(nn):
    return os.path.join(DIR, nn + ".md")


def body(nn):
    with open(path(nn), encoding="utf-8") as f:
        t = f.read()
    head, rest = t.split("\n", 1)
    if head.strip() != "# " + nn:
        raise SystemExit("%s: 1行目は「# %s」" % (nn, nn))
    return rest.strip() + "\n"


def source(nn):
    """調べる時にくらべる、もとの文（まとめ先と、まとめる相手の本文、3STEP、まとめ）。"""
    ks = [OLD[nn]] + ([HOST[nn]] if nn in HOST else [])
    out = ""
    for k in ks:
        out += B.body(k) + "".join(h + v + (n or "") for h, v, n in B.sheet(k)[1]) + B.sheet(k)[2] + "".join(str(x) for x in B.matome(k))
    return out


def init():
    os.makedirs(DIR, exist_ok=True)
    made = 0
    for nn in sorted(OLD):
        if os.path.exists(path(nn)):
            continue
        with open(path(nn), "w", encoding="utf-8") as f:
            f.write("# %s\n%s" % (nn, renum(B.body(OLD[nn]), nn)))
        made += 1
    print("作ったファイル %d個（全部で %d個）" % (made, len(OLD)))


def problems(nn):
    out = []
    b = body(nn)
    if not b.startswith("## "):
        out.append("最初は、問いの見出し（## ）")
    if "*" in b:
        out.append("アスタリスクがある")
    for m in re.finditer(r"(?<![0-9])([0-9]{2})番", b):
        if not 1 <= int(m.group(1)) <= 35:
            out.append("ない番号: " + m.group(0))
        if m.group(1) == nn:
            out.append("自分の番号を指している: …%s…" % b[max(0, m.start() - 18):m.end() + 8].replace("\n", " "))
    src = source(nn)
    num = lambda t: set(re.findall(r"[0-9]+(?:\.[0-9]+)?", re.sub(r"[0-9]{2}番", "", t)))
    extra = sorted(num(b) - num(src) - {str(6 + len(OLD))})   # 「この本にある35のうち」の35は、数を直したもの
    if extra:
        out.append("今の原稿にない数字: " + " ".join(extra))
    uni = sorted(set(re.findall(r"[ァ-ヶー一-龥]+大学", b)) - set(re.findall(r"[ァ-ヶー一-龥]+大学", src)))
    if uni:
        out.append("今の原稿にない大学名: " + " ".join(uni))
    for w in ("証明", "必ず", "1位", "絶対に"):
        if w in b and w not in src:
            out.append("今の原稿にない強い言葉: " + w)
    pages, cap = limit(nn)
    r = M.body_rows(b, W)
    if cap and r > cap:
        out.append("行が多い：%d行（上限%d行）。あと%d行、削る" % (r, cap, r - cap))
    return out


def show(nn):
    k = OLD[nn]
    it = V.ITEMS[k]
    pages, cap = limit(nn)
    b = body(nn)
    print("==== %s番（45個の版では %s番）　%s" % (nn, k, it["t"]))
    print("×：%s　／　○：%s" % (it["x"], it["o"]))
    print("今のファイル：%d字、%d行　／　目標：%s" % (B.n(b), M.body_rows(b, W), ("%dページ（本文は%d行まで）" % (pages, cap)) if cap else "柱なので、今の長さのまま"))
    ttl, steps, king = B.sheet(k)
    for i, (h, v, note) in enumerate(steps, 1):
        print("STEP0%d　%s　／声「%s」%s" % (i, renum(h), renum(v), ("　／※" + renum(note)) if note else ""))
    one, pts, dakara, toi = B.matome(k)
    print("基準：%s　／　まとめ：%s／%s／%s　／　問い：%s" % (king, one, "・".join(pts), dakara, toi))
    c = B.koma(k)
    print("2コマ：×「%s」%s　／　○「%s」%s" % (c[0][0], c[0][1], c[1][0], c[1][1]))
    print("---- 今のファイル（%s）" % os.path.relpath(path(nn), ROOT))
    print(b)
    if nn in HOST:
        a = HOST[nn]
        ia = V.ITEMS[a]
        print("==== まとめる相手：45個の版の %s番　%s" % (a, ia["t"]))
        print("×：%s　／　○：%s" % (ia["x"], ia["o"]))
        for i, (h, v, note) in enumerate(B.sheet(a)[1], 1):
            print("STEP0%d　%s　／声「%s」" % (i, h, v))
        print("---- 相手の本文（番号は、35個の版に直してある。自分を指す番号は、外すこと）")
        print(renum(B.body(a), a))


def main():
    cmd, ks = sys.argv[1], sys.argv[2:]
    if cmd == "init":
        return init()
    if cmd == "rebuild":
        return rebuild()
    if cmd == "map":
        for nn in sorted(OLD):
            print("%s ← %s%s　%s" % (nn, OLD[nn], ("＋" + HOST[nn]) if nn in HOST else "", V.ITEMS[OLD[nn]]["t"]))
        return
    if cmd == "show":
        for nn in ks:
            show(nn)
        return
    ks = ks or sorted(OLD)
    ng = 0
    for nn in ks:
        ps = problems(nn)
        ng += len(ps)
        pages, cap = limit(nn)
        r = M.body_rows(body(nn), W)
        print("%s（%s%s）　%d行／%s　→ %dページ　%d字　%s" % (nn, OLD[nn], ("＋" + HOST[nn]) if nn in HOST else "", r, ("上限%d行" % cap) if cap else "上限なし",
                                              pages_of(r), B.n(body(nn)), "OK" if not ps else ""))
        for p in ps:
            print("　　× " + p)
    print("調べた %d個／直す所 %d件" % (len(ks), ng))


if __name__ == "__main__":
    main()
