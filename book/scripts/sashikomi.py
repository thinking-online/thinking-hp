# -*- coding: utf-8 -*-
# 45個の版に、新しい項目を1つ差しこむ（著者が、目次に新しい項目を足した時に使う）。
#   python3 -I scripts/sashikomi.py 24     → 今の24番から後ろを、1つずつ後ろへ送る（24→25、25→26、…）。24番が空く
# 直す所：本文のファイル名（本文/v4/NN.md、詰める前、直しメモ、NN_足し）、本文の中の「NN番」、
#   「この本の使い方」の索引の番号、scripts の中の番号（v4_data の項目・前の番号との対応、book_data のコラムと一言と参考文献、
#   v4_hooks、柱の項目、35個の版の決まりの中の「45個の版の番号」）、直しメモの一覧と、短い言葉の表の番号。
# 直さない所：章ごとの項目の並び（v4_data.CHAPTERS）。終わったあとに、手で直す。35個の版の番号で書いてある所（そのまま）。
# 終わったら：空いた番号に、新しい項目を足す（v4_data.ITEMS、本文/v4/NN.md、詰める前/NN.md、直しメモ/NN.md）。
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V4 = os.path.join(ROOT, "manuscript", "本文", "v4")
N = sys.argv[1]
assert re.fullmatch(r"[0-9]{2}", N) and int(N) >= 7
sys.path.insert(0, HERE)
import v4_data as V
LAST = max(int(k) for k in V.ITEMS)
LOG = []


def mv(k):
    """番号を、1つ後ろへ（N以上、今の最後の番号まで）。"""
    return "%02d" % (int(k) + 1) if int(N) <= int(k) <= LAST else k


def sub(t, pat):
    def f(m):
        k = m.group("n")
        s, e = m.start("n") - m.start(0), m.end("n") - m.start(0)
        return m.group(0)[:s] + mv(k) + m.group(0)[e:]
    return re.sub(pat, f, t)


def edit(path, fn):
    with open(path, encoding="utf-8") as f:
        t = f.read()
    t2 = fn(t)
    if t2 != t:
        with open(path, "w", encoding="utf-8") as f:
            f.write(t2)
        LOG.append(os.path.relpath(path, ROOT))


def block(t, start, end, fn):
    i = t.index(start)
    j = t.index(end, i)
    return t[:i] + fn(t[i:j]) + t[j:]


# 1) ファイル名（後ろの番号から、順に送る）
for k in range(LAST, int(N) - 1, -1):
    a, b = "%02d" % k, "%02d" % (k + 1)
    for d in ("", "詰める前", "直しメモ"):
        for suf in (".md", "_足し.md"):
            pa, pb = os.path.join(V4, d, a + suf), os.path.join(V4, d, b + suf)
            if os.path.exists(pa):
                assert not os.path.exists(pb), pb
                os.rename(pa, pb)
LOG.append("ファイル名：%s〜%02d番を、1つずつ後ろへ" % (N, LAST))

# 2) 本文の中の「NN番」
REF = r"(?<![0-9])(?P<n>[0-9]{2})(?=番|〜[0-9]{2}番)"   # 「NN番」と、「NN〜MM番」の前の番号
for n in sorted(x for x in os.listdir(V4) if x.endswith(".md")):
    edit(os.path.join(V4, n), lambda t: sub(t, REF))
d6 = os.path.join(ROOT, "manuscript", "本文", "v6", "足し")
for n in sorted(os.listdir(d6)) if os.path.isdir(d6) else []:
    edit(os.path.join(d6, n), lambda t: sub(t, REF))


def sakuin(t):
    out = []
    for l in t.split("\n"):
        m = re.match(r"^(.*?[^0-9　 ])((?:[　 ]+[0-9]{2})+)([　 ]*)$", l)
        if m:
            l = m.group(1) + re.sub(r"[0-9]{2}", lambda x: mv(x.group(0)), m.group(2)) + m.group(3)
        out.append(l)
    return "\n".join(out)


edit(os.path.join(V4, "00_使い方.md"), sakuin)
# 一覧と、短い言葉の表（行の頭の「| NN 」）
ROW = r"(?m)^\| (?P<n>[0-9]{2})(?=[ （])"
edit(os.path.join(V4, "直しメモ", "00_一覧.md"), lambda t: sub(t, ROW))
edit(os.path.join(V4, "しないとするの言葉_案.md"), lambda t: sub(t, ROW))


# 3) scripts
def v4_data(t):
    t = sub(t, r'(?m)^ "(?P<n>[0-9]{2})": dict\(')
    t = sub(t, r'\("file", "(?P<n>[0-9]{2})(?:_足し)?"\)')
    return block(t, "OLD2NEW = {", "}", lambda s: sub(s, r'"[0-9]{2}": "(?P<n>[0-9]{2})"'))


def book_data(t):
    t = sub(t, r'(?m)^    \("(?P<n>[0-9]{2})", "v[0-9]"')
    t = block(t, "HITOKOTO = {", "}", lambda s: sub(s, r'(?m)^    "(?P<n>[0-9]{2})":'))
    t = block(t, "REF_SPECIAL = {", "}", lambda s: sub(s, r': "(?P<n>[0-9]{2})"'))
    return block(t, "CH1_REF = {", "\n}", lambda s: sub(s, r': "(?P<n>[0-9]{2})"'))


def sets(t):
    return re.sub(r"(?m)^(PILLAR = \{)([^}]*)(\})",
                  lambda m: m.group(1) + ", ".join('"%s"' % k for k in sorted(mv(k) for k in re.findall(r"[0-9]{2}", m.group(2)))) + m.group(3), t)


def v6py(t):
    t = sets(t)
    t = block(t, "GROUPS = [", "\n]", lambda s: sub(s, r'"(?P<n>[0-9]{2})"'))
    t = block(t, "ABSORB = {", "}", lambda s: sub(s, r'"(?P<n>[0-9]{2})"'))
    return block(t, "TO_COLUMN = {", "}", lambda s: sub(s, r'"(?P<n>[0-9]{2})"'))


edit(os.path.join(HERE, "v4_data.py"), v4_data)
edit(os.path.join(HERE, "book_data.py"), book_data)
edit(os.path.join(HERE, "v4_hooks.py"), lambda t: sub(t, r'(?m)^"(?P<n>[0-9]{2})": """'))
edit(os.path.join(HERE, "haibun.py"), sets)
edit(os.path.join(HERE, "v6.py"), v6py)
print("%s番を空けた（%s〜%02d番 → 1つずつ後ろへ。最後は %02d番）" % (N, N, LAST, LAST + 1))
for l in LOG:
    print("　" + l)
print("このあと：v4_data.CHAPTERS の並びを直す。%s番に、新しい項目を足す。" % N)
