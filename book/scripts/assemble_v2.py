# -*- coding: utf-8 -*-
"""新構成（8章・50本）の原稿を組み立てる。
土台：旧原稿（manuscript/原稿_最新版_マーカー.md）と、新しく書いた manuscript/本文/v2/*.md
出力：manuscript/原稿_v2_マーカー.md（マーカーあり）／原稿_v2.md（マーカーなし）
book/ で実行。"""
import io, os, re, sys
sys.path.insert(0, "scripts")
from plan_v2 import CHAPTERS, LAWS, OLD2NEW

V2 = "manuscript/本文/v2"
CIRC = "①②③④⑤⑥"
FORCE = r'(?:選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力)'

def rd(p):
    return io.open(p, encoding="utf-8").read()

# ---------- 旧原稿を番号ごとに取り出す ----------
OLD = rd("manuscript/原稿_最新版_マーカー.md")
_p = re.split(r'\n## (\d{2})　(.+?)\n', OLD)
old = {}
for i in range(1, len(_p) - 2, 3):
    body = re.split(r'\n# ', _p[i + 2])[0]
    body = re.sub(r'^　　[×○]「.*」[ \t]*\n', '', body, count=2, flags=re.M)
    body = re.sub(r'^　?(?:' + FORCE + r'(?:　★厚く書く)?|★厚く書く)[ \t]*\n', '', body, count=1, flags=re.M)
    old[_p[i]] = body.strip("\n")

def sec(body, heading):
    """## heading の節をまるごと返す（次の ## の手前まで）"""
    m = re.search(r'^## ' + re.escape(heading) + r'[ \t]*\n.*?(?=^## |\Z)', body, flags=re.M | re.S)
    if not m:
        raise SystemExit("節が見つからない: " + heading)
    return m.group(0).rstrip("\n") + "\n"

def drop(body, heading):
    s = sec(body, heading)
    return body.replace(s, "", 1)

def before(body, heading, text):
    if not text.strip():
        return body
    m = re.search(r'^## ' + re.escape(heading) + r'[ \t]*$', body, flags=re.M)
    if not m:
        raise SystemExit("挿入先が見つからない: " + heading)
    return body[:m.start()] + text.rstrip("\n") + "\n\n" + body[m.start():]

def part(name):
    """v2/_parts/name.md（補強として差し込む短い節）。無ければ飛ばして報告する"""
    p = os.path.join(V2, "_parts", name + ".md")
    if not os.path.exists(p):
        MISSING.append("補強:" + name)
        return ""
    return rd(p).strip("\n") + "\n"

MISS, MISSING, out = [], [], []

# ---------- 項目ごとの加工 ----------
def ops(no, b):
    if no == "09":   # 小テスト ← 模試の見方を補強
        b = before(b, "頭のなか", part("09_模試"))
    if no == "10":   # 宿題 ← 内申という判断軸
        b = before(b, "頭のなか", part("10_内申"))
    if no == "16":   # 混ぜる話は17番に移した
        b = drop(b, "まとめてやるより、混ぜたほうが残ります")
    if no == "21":   # 時間を測る ← 本番と同じ形で（旧06）
        b = before(b, "頭のなか", part("21_本番の形"))
    if no == "24":   # 解き直し ← 止まった場所を探す（旧07）
        b = before(b, "頭のなか", part("24_止まった場所"))
    if no == "30":   # 計画 ← 10分で切る（旧15）
        b = before(b, "頭のなか", part("30_10分で切る"))
    if no == "36":   # スマホ ← 手間を作る
        b = before(b, "頭のなか", part("36_手間"))
    if no == "39":   # 睡眠 ← 仮眠
        b = before(b, "頭のなか", part("39_仮眠"))
    if no == "43":   # 比べる ← 2つの物差し
        b = before(b, "頭のなか", part("43_2つの物差し"))
    if no == "46":   # 本番 ← ルーティン
        b = before(b, "やり方", part("46_ルーティン"))
    return b

def fix_refs(b, no):
    def rep(m):
        o = m.group(1)
        if o in OLD2NEW:
            return OLD2NEW[o] + "番"
        MISS.append((no, m.group(0)))
        return m.group(0)
    return re.sub(r'(?<!\d)(\d{2})番', rep, b)

def tail(b, law, is_law):
    b = re.sub(r'^今日やること(?=[^\s　])', '今日やること　', b, flags=re.M)
    b = re.sub(r'^　*この場面を見つけた問い.*\n?', '', b, flags=re.M)
    if is_law:
        return b
    tag = "　　もとにある絶対法則　　%s %s" % (CIRC[law - 1], LAWS[law])
    m = list(re.finditer(r'^今日やること', b, flags=re.M))
    if m:
        i = m[-1].start()
        return b[:i].rstrip("\n") + "\n\n" + tag + "\n\n" + b[i:]
    return b.rstrip("\n") + "\n\n" + tag + "\n"

out.append("# 原稿　新構成（8章・50本）\n\n組み立て：scripts/assemble_v2.py\n\n---\n")
for f, head in [("00_巻頭", None), ("00_はじめに", None), ("00_使い方", None)]:
    p = os.path.join(V2, f + ".md")
    if os.path.exists(p):
        out.append(rd(p).strip("\n") + "\n\n---\n")
    else:
        MISSING.append(f)

n_old = n_new = 0
for ci, (cno, ctitle, csub, items) in enumerate(CHAPTERS, 1):
    out.append("# %s　%s\n" % (cno, ctitle))
    out.append("〔%s〕\n" % csub)
    p = os.path.join(V2, "ch%d_扉.md" % ci)
    if os.path.exists(p):
        out.append(rd(p).strip("\n") + "\n")
    else:
        MISSING.append("ch%d_扉" % ci)
    for no, law, title, x, o, src in items:
        if src[0] == "old":
            b = fix_refs(old[src[1]], no); n_old += 1
        else:
            p = os.path.join(V2, no + ".md")
            if os.path.exists(p):
                b = rd(p).strip("\n"); n_new += 1
            else:
                b = "★未執筆"; MISSING.append(no)
        b = ops(no, b)
        b = tail(b, law, cno == "第1章")
        head = "## %s　%s" % (no, title)
        lawline = ("　　絶対法則 %s　%s\n\n" % (CIRC[law - 1], LAWS[law])) if cno == "第1章" else ""
        out.append("%s\n\n%s　　×「%s」\n　　○「%s」\n\n%s\n\n---\n" % (head, lawline, x, o, b))
    p = os.path.join(V2, "ch%d_結び.md" % ci)
    if os.path.exists(p):
        out.append(rd(p).strip("\n") + "\n\n---\n")
    for f in sorted(os.listdir(V2)):
        if f.startswith("col_ch%d_" % ci):
            out.append(rd(os.path.join(V2, f)).strip("\n") + "\n\n---\n")

for f in ["90_巻末", "91_おわりに"]:
    p = os.path.join(V2, f + ".md")
    if os.path.exists(p):
        out.append(rd(p).strip("\n") + "\n\n---\n")
    else:
        MISSING.append(f)

txt = "\n".join(out)
txt = re.sub(r'\n{3,}', '\n\n', txt)
io.open("manuscript/原稿_v2_マーカー.md", "w", encoding="utf-8").write(txt)
io.open("manuscript/原稿_v2.md", "w", encoding="utf-8").write(txt.replace("==", ""))

body = re.sub(r'^#{1,6}\s*', '', txt, flags=re.M).replace("==", "")
print("旧稿を土台 %d本 ／ 新しく書いた %d本 ／ 文字数 %s" % (n_old, n_new, format(len(re.sub(r'\s', '', body)), ",")))
print("まだ無いもの:", " ".join(MISSING) if MISSING else "なし")
if MISS:
    print("行き先のない番号参照:", MISS)
