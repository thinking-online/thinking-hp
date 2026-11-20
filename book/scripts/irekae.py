# -*- coding: utf-8 -*-
# 45個の版の、2つの項目の番号を入れかえる（著者が、項目の順番を変えた時に使う）。
#   python3 -I scripts/irekae.py 09 11     → 09番と11番を入れかえる
# 直す所：本文のファイル名（本文/v4/NN.md、詰める前、直しメモ、NN_足し、35個の版の 本文/v6/足し）、本文の中の「NN番」、
#   「この本の使い方」の索引の番号、scripts の中の番号（v4_data の項目・前の番号との対応、book_data のコラムと一言、
#   v4_hooks、柱の項目、35個の版の決まり）。
# 直さない所：docs の記録、詰める前の文の中身、直しメモの中身（前の番号のまま残る）。
# 終わったら、assemble_v4.py、assemble_book.py、v6.py rebuild、assemble_v6.py を走らせて、「直す所 0件」を確かめる。
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V4 = os.path.join(ROOT, "manuscript", "本文", "v4")
A, B = sys.argv[1], sys.argv[2]
assert re.fullmatch(r"[0-9]{2}", A) and re.fullmatch(r"[0-9]{2}", B) and A != B and int(A) >= 7 and int(B) >= 7
sys.path.insert(0, HERE)
import v6 as F
A6, B6 = F.NEW.get(A), F.NEW.get(B)   # 35個の版での番号（入れかえる前に調べておく）
LOG = []


def sw(k, a=A, b=B):
    return b if k == a else a if k == b else k


def sub(t, pat, a=A, b=B):
    """pat の中の (?P<n>…) が a か b の時、入れかえる。"""
    def f(m):
        k = m.group("n")
        if k not in (a, b):
            return m.group(0)
        s, e = m.start("n") - m.start(0), m.end("n") - m.start(0)
        return m.group(0)[:s] + sw(k, a, b) + m.group(0)[e:]
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
    """start から end までの部分だけ、fn で直す。"""
    i = t.index(start)
    j = t.index(end, i)
    return t[:i] + fn(t[i:j]) + t[j:]


# 1) ファイル名
for d in ("", "詰める前", "直しメモ"):
    for suf in (".md", "_足し.md"):
        pa, pb = os.path.join(V4, d, A + suf), os.path.join(V4, d, B + suf)
        tmp = pa + ".tmp"
        ea, eb = os.path.exists(pa), os.path.exists(pb)
        if ea:
            os.rename(pa, tmp)
        if eb:
            os.rename(pb, pa)
        if ea:
            os.rename(tmp, pb)
        if ea or eb:
            LOG.append("ファイル名：%s/%s%s ⇔ %s%s" % (d or "v4", A, suf, B, suf))

# 2) 本文の中の「NN番」
REF = r"(?<![0-9])(?P<n>[0-9]{2})番"
names = [n for n in os.listdir(V4) if n.endswith(".md")]
for n in sorted(names):
    edit(os.path.join(V4, n), lambda t: sub(t, REF))
d6 = os.path.join(ROOT, "manuscript", "本文", "v6", "足し")
# 35個の版の、足しの文（35個の版の番号で置いてある）。まとめ先の項目が動いたら、ファイル名も入れかえる
if A6 and B6 and A6 != B6:
    pa, pb = os.path.join(d6, A6 + ".md"), os.path.join(d6, B6 + ".md")
    ea, eb = os.path.exists(pa), os.path.exists(pb)
    if ea:
        os.rename(pa, pa + ".tmp")
    if eb:
        os.rename(pb, pa)
    if ea:
        os.rename(pa + ".tmp", pb)
    if ea or eb:
        LOG.append("ファイル名：v6/足し/%s.md ⇔ %s.md" % (A6, B6))
for n in sorted(os.listdir(d6)) if os.path.isdir(d6) else []:
    edit(os.path.join(d6, n), lambda t: sub(t, REF))


# 「この本の使い方」の索引：行の終わりに並んでいる番号
def sakuin(t):
    out = []
    for l in t.split("\n"):
        m = re.match(r"^(.*?[^0-9　 ])((?:[　 ]+[0-9]{2})+)([　 ]*)$", l)
        if m:
            l = m.group(1) + re.sub(r"[0-9]{2}", lambda x: sw(x.group(0)), m.group(2)) + m.group(3)
        out.append(l)
    return "\n".join(out)


edit(os.path.join(V4, "00_使い方.md"), sakuin)

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
    return re.sub(r"(?m)^(PILLAR = \{)([^}]*)(\})", lambda m: m.group(1) + ", ".join('"%s"' % k for k in sorted(sw(k) for k in re.findall(r"[0-9]{2}", m.group(2)))) + m.group(3), t)


def v6py(t):
    t = sets(t)
    t = block(t, "ABSORB = {", "}", lambda s: sub(s, r'"(?P<n>[0-9]{2})"'))
    t = block(t, "TO_COLUMN = {", "}", lambda s: sub(s, r'"(?P<n>[0-9]{2})"'))
    if A6 and B6 and A6 != B6:   # 35個の版の番号で書いてある所（目次の言葉、言葉の入れかえ）
        t = block(t, "OVERRIDE = {", "\n}", lambda s: sub(s, r'(?m)^    "(?P<n>[0-9]{2})":', A6, B6))
        t = block(t, "FIX = {", "}", lambda s: sub(s, r'"(?P<n>[0-9]{2})":', A6, B6))
    return t


def a6py(t):
    if A6 and B6 and A6 != B6:   # コラムの置き場所（35個の版の番号）
        t = sub(t, r'(?m)^    \("(?P<n>[0-9]{2})", "v[0-9]"', A6, B6)
    return t


edit(os.path.join(HERE, "v4_data.py"), v4_data)
edit(os.path.join(HERE, "book_data.py"), book_data)
edit(os.path.join(HERE, "v4_hooks.py"), lambda t: sub(t, r'(?m)^"(?P<n>[0-9]{2})": """'))
edit(os.path.join(HERE, "haibun.py"), sets)
edit(os.path.join(HERE, "v6.py"), v6py)
edit(os.path.join(HERE, "assemble_v6.py"), a6py)
print("%s番 ⇔ %s番（35個の版では %s ⇔ %s）" % (A, B, A6, B6))
for l in LOG:
    print("　" + l)
