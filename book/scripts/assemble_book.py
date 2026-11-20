# -*- coding: utf-8 -*-
# 完全版（仮）を組む。表紙から「おわりに」まで。案・第1版（2026-11-19）。
#   python3 -I scripts/assemble_book.py           → manuscript/完全版/ に書き出す
#   python3 -I scripts/assemble_book.py --check   → 調べるだけ
# もとの材料：
#   前付け・第1章の01〜04番   著者のマスター（book_data.MASTER）の言葉のまま。直した所は book_data.FIXES に全部書いてある
#   05番・06番               manuscript/著者原稿/ の確定版
#   07〜45番                 scripts/assemble_v4.py（v4_data.py）
#   コラム・王様の一言        book_data.COLUMNS・HITOKOTO
#   巻末・おわりに            manuscript/本文/v2/90_巻末.md・91_おわりに.md（番号と数を直す）
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import book_data as K
import v4_data as V
import assemble_v4 as B
import assemble_v3 as A

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "manuscript", "完全版")
n = A.n
LABELS = ["章最初のページ", "導入文", "質問ページ", "本文", "頭のいい人と伸びない人の違い", "今日からできる3STEP", "まとめ"]
USED_FIX = set()
LOG = []   # 番号を直した所（確かめるために出す）


def rd(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


_MASTER = None
def master(rng):
    global _MASTER
    if _MASTER is None:
        _MASTER = rd(K.MASTER).split("\n")
    return "\n".join(_MASTER[rng[0] - 1:rng[1]])


def fix(where, t):
    for w, a, b, _ in K.FIXES:
        if w == where:
            if a not in t:
                raise SystemExit("%s: 直す言葉が見つからない: %s" % (where, a.strip()))
            USED_FIX.add((w, a))
            t = t.replace(a, b)
    return t


def newnum(k, where):
    """前の番号 → 新しい番号。01〜06はそのまま。"""
    if int(k) <= 6:
        return k
    sp = K.CH1_REF.get(where, {})
    if k in sp:
        return sp[k]
    if k not in V.OLD2NEW:
        raise SystemExit("%s: 新しい目次にない番号: %s" % (where, k))
    return V.OLD2NEW[k]


def remap(t, where):
    """本文の中の「〜番」と、表の右はしの番号を、新しい番号に直す。"""
    out = []
    for l in t.split("\n"):
        o = l
        l = re.sub(r"(?<![0-9])([0-9]{2})番", lambda m: newnum(m.group(1), where) + "番", l)
        l = re.sub(r"→([0-9]{2})(?=[ 　]|$)", lambda m: "→" + newnum(m.group(1), where), l)
        m = re.match(r"^(.*?[^0-9　 ])((?:[　 ]+(?:→[　 ]*)?[0-9]{2})+)[　 ]*$", l)
        if m and re.search(r"[　]|→", m.group(2)) and not re.search(r"[0-9]$", m.group(1)):
            nums, seen = [], []
            for k in re.findall(r"[0-9]{2}", m.group(2)):
                k2 = newnum(k, where)
                if k2 not in seen:
                    seen.append(k2)
            lead = re.match(r"^[　 ]+(→[　 ]*)?", m.group(2)).group(0)
            l = m.group(1) + lead + "　".join(seen)
        if l != o and (where, o.strip(), l.strip()) not in LOG:
            LOG.append((where, o.strip(), l.strip()))
        out.append(l)
    return "\n".join(out)


def to_md(t):
    """著者の貼り付けの形（⚫︎、■）を、こちらの形（##、###）にする。"""
    out = []
    for l in t.split("\n"):
        s = l.strip()
        if s.startswith("⚫︎"):
            out += ["", "## " + s[2:].strip(), ""]
        elif s.startswith("■"):
            out += ["", "### " + s[1:].strip(), ""]
        elif re.match(r"^【[^】]+】.+", s):
            out += ["", "## " + s, ""]
        else:
            out.append(l.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


# ---------- 第1章 ----------

def ch1_lines(kk):
    if kk in K.CH1_MASTER:
        t = fix(kk, master(K.CH1_MASTER[kk]) + "\n")
        return t.split("\n")
    t = rd(K.CH1_KAKUTEI[kk])
    t = t[t.index("## 章最初のページ"):]
    i = t.find("\n---\n\n組む時の注意")
    if i < 0:
        raise SystemExit(kk + ": 確定版の「組む時の注意」が見つからない")
    out = ["%s【絶対法則】" % kk]
    for l in t[:i].split("\n"):
        if l.startswith("## "):
            name = l[3:].strip()
            out.append(name if name in LABELS else "⚫︎" + name)
        else:
            out.append(l)
    return out


def ch1_item(kk):
    """項目を、ラベルごとに分ける。{ラベル: 文}"""
    lines = ch1_lines(kk)
    parts = {l: [] for l in LABELS}
    cur = "章最初のページ"
    for l in lines[1:]:
        s = l.strip()
        s2 = s[1:-1] if s.startswith("【") and s.endswith("】") else s
        if s2 in LABELS:
            cur = s2
            continue
        parts[cur].append(l)
    for (k, lab), fill in K.CH1_FILL.items():
        if k == kk:
            if "".join(parts[lab]).strip():
                raise SystemExit("%s %s: 空いていない" % (kk, lab))
            parts[lab] = list(fill)
    res = {}
    for lab in LABELS:
        t = "\n".join(parts[lab]).strip("\n")
        res[lab] = remap(t, kk)
    if kk in K.CH1_TOI:
        if "自分に聞きます" in res["まとめ"]:
            raise SystemExit(kk + ": まとめに、もう問いがある")
        res["まとめ"] = res["まとめ"].rstrip() + "\n迷ったら、自分に聞きます。「%s」" % K.CH1_TOI[kk]
    return res


def nonempty(t):
    return [l.strip() for l in t.split("\n") if l.strip() and l.strip() != "```"]


def ch1_koma(it):
    ls = nonempty(it["頭のいい人と伸びない人の違い"])
    if len(ls) != 6 or ls[0] != "伸びない人" or ls[3] != "頭のいい人":
        return None
    return ((ls[1], ls[2]), (ls[4], ls[5]))


def ch1_sheet(kk, it):
    """(題, [(見出し, 声, 補足)], 基準)。読み取れない時は None。見出しが2行に分かれていても、1行にする。"""
    ls = nonempty(it["今日からできる3STEP"])
    ttl, blocks, king, cur = None, [], None, None
    i = 0
    while i < len(ls):
        l = ls[i]
        if re.match(r"^STEP0[123]$", l):
            cur = []; blocks.append(cur)
        elif l == "できた基準":
            king = " ".join(ls[i + 1:]).strip(); break
        elif cur is None:
            m = re.search(r"『(.+?)』", l)
            if m:
                ttl = m.group(1)
            elif not l.startswith("※"):
                return None
        else:
            cur.append(l)
        i += 1
    steps = []
    for b in blocks:
        voice = [l for l in b if l.startswith("「") and l.endswith("」")]
        note = [l[1:] for l in b if l.startswith("※")]
        head = [l for l in b if l not in voice and not l.startswith("※")]
        if len(voice) != 1 or not head:
            return None
        steps.append(("".join(head), voice[0][1:-1], note[0] if note else None))
    if len(steps) != 3 or not king:
        return None
    if not ttl:
        import step_card_v2 as S2
        ttl = S2.S[kk][0]
    return ttl, steps, king


def ch1_name(kk):
    return K.CH1_MOKUJI[kk][0]


def body_md(t, up=1):
    """⚫︎・■を見出しにする。up=1 なら、項目の中に置く深さ（###、####）にする。"""
    md = to_md(t)
    if up:
        md = re.sub(r"^### ", "#### ", md, flags=re.M)
        md = re.sub(r"^## ", "### ", md, flags=re.M)
    return md.strip()


def hitokoto_md(kk):
    return ["## 王様の一言", "", "「%s」" % K.HITOKOTO[kk], ""] if kk in K.HITOKOTO else []


def ch1_item_md(kk):
    it = ch1_item(kk)
    L = ["# %s　絶対法則%s　%s" % (kk, kk, ch1_name(kk)), ""]
    for lab in LABELS:
        L += ["## " + lab, ""]
        if lab == "本文" or lab == "導入文":
            L.append(body_md(it[lab]))
        else:
            L.append(it[lab].strip())
        L.append("")
    L += hitokoto_md(kk)
    return "\n".join(L)


# ---------- コラム ----------

def column(src, name):
    """(題, 本文)"""
    t = rd("manuscript/本文/%s/%s.md" % (src, name)).strip()
    head, body = t.split("\n", 1)
    if not head.startswith("# コラム"):
        raise SystemExit(name + ": コラムの題がない")
    body = body.strip()
    if src == "v2":
        body = B.remap(body, name)
    return head[2:].strip().replace("コラム　", "", 1), body


def columns_after(kk):
    return [column(s, nm) for k, s, nm in K.COLUMNS if k == kk]


def column_md(c):
    return "\n".join(["# コラム　%s" % c[0], "", c[1], ""])


# ---------- 07〜45番 ----------

def item_md(kk):
    md = B.item_md(kk)
    return md.rstrip() + "\n\n" + "\n".join(hitokoto_md(kk)) if kk in K.HITOKOTO else md


# ---------- 巻末 ----------

def kanmatsu():
    """90_巻末.md を、節ごとに分ける。{題: 本文}"""
    t = rd("manuscript/本文/v2/90_巻末.md")
    secs = re.split(r"(?m)^(?=# 巻末　)", t)
    return {s.split("\n", 1)[0][2:].replace("巻末", "", 1).strip(): s.split("\n", 1)[1].strip() for s in secs if s.startswith("# 巻末")}


def ichiran_md():
    L = ["45個を、1枚にまとめました。左が、頭のいい人が絶対やらないこと。右が、かわりにやっていることです。", ""]
    L += ["第1章　%s" % K.CH1_TITLE, "", "```"]
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L.append("　%s　×　%s　→　○　%s" % (kk, t, o))
    L += ["```", ""]
    for num, fuda, title, sub, groups in V.CHAPTERS:
        L += ["第%d章　【%s】%s" % (num, fuda, title), "", "```"]
        for _, items in groups:
            for kk in items:
                it = V.ITEMS[kk]
                L.append("　%s　×　%s　→　○　%s" % (kk, it["t"], it["o"]))
        L += ["```", ""]
    return "\n".join(L)


def sankou_md(t):
    """参考文献の、項目の番号を直す。使う項目がなくなった研究は、外す。"""
    blocks = re.split(r"\n\s*\n", t)
    out = []
    for b in blocks:
        ls = b.split("\n")
        m = re.match(r"^(.*?)((?:　[0-9]{2})+)\s*$", ls[-1])
        if not m or ls[0].startswith(("本文では", "```")) and len(ls) == 1:
            out.append(b); continue
        seen = []
        for k in re.findall(r"[0-9]{2}", m.group(2)):
            k2 = k if int(k) <= 6 else K.REF_SPECIAL[k] if k in K.REF_SPECIAL else V.OLD2NEW[k]
            if k2 and k2 not in seen:
                seen.append(k2)
        if not seen:
            LOG.append(("参考文献", "外した：" + ls[0].strip(), "")); continue
        ls[-1] = m.group(1) + "".join("　" + k for k in sorted(seen))
        nb = "\n".join(ls)
        if nb != b:
            LOG.append(("参考文献", b.split("\n")[0].strip() + m.group(2), "".join("　" + k for k in sorted(seen))))
        out.append(nb)
    return "\n\n".join(out)


# ---------- 全体 ----------

def mokuji_md():
    L = ["10秒だけ、付き合ってください", "はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」", "この本の使い方", "",
         "第1章　%s" % K.CH1_TITLE, "　　　　【%s】" % K.CH1_SUB, ""]
    def cols(kk):
        return ["　コラム　%s" % c[0] for c in columns_after(kk)] + ([""] if columns_after(kk) else [])
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L += ["　%s　%s　［%s］" % (kk, t, nm), "　　　×　%s" % x, "　　　○　%s" % o, ""] + cols(kk)
    for num, fuda, title, sub, groups in V.CHAPTERS:
        L += ["第%d章　【%s】%s" % (num, fuda, title)] + (["　　　　%s" % sub] if sub else []) + [""]
        for name, items in groups:
            if name:
                L += ["　■ %s" % name, ""]
            for kk in items:
                it = V.ITEMS[kk]
                L += ["　%s　%s" % (kk, it["t"]), "　　　×　%s" % it["x"], "　　　○　%s" % it["o"], ""] + cols(kk)
    L += ["巻末　45を、1枚に", "巻末　6つの言葉で、初めての場面を解く", "巻末　保護者の方へ", "巻末　参考文献",
          "おわりに　笑わなかった人が、1人だけいました"]
    return "\n".join(L)


def sections():
    """本の頭から順に、(種類, 名前, md) を返す。"""
    S = []
    S.append(("cover", "表紙", "\n".join(["# 表紙（題は、まだ決まっていない）", "", "題の案", ""] + ["　　" + t for t in K.TITLES] + ["", "著者　" + K.AUTHOR, ""])))
    S.append(("text", "10秒だけ、付き合ってください", "# 10秒だけ、付き合ってください\n\n" + to_md(fix("巻頭", master(K.KANTOU)))))
    S.append(("toc", "目次", "# 目次\n\n```\n" + mokuji_md() + "\n```\n"))
    S.append(("text", "はじめに", "# はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」\n\n" + to_md(fix("はじめに", master(K.HAJIMENI)))))
    S.append(("text", "この本の使い方", "# この本の使い方\n\n" + rd("manuscript/本文/v4/00_使い方.md")))
    S.append(("door", "第1章", "\n".join(["# 第1章　%s" % K.CH1_TITLE, "【%s】" % K.CH1_SUB, "", "## 章の導入文", "", to_md(master(K.CH1_INTRO))])))
    for kk in sorted(K.CH1_MOKUJI):
        S.append(("item1", kk, ch1_item_md(kk)))
        for c in columns_after(kk):
            S.append(("column", c[0], column_md(c)))
    for ch in V.CHAPTERS:
        num, fuda, title, sub, groups = ch
        L = ["# 第%d章　【%s】%s" % (num, fuda, title)] + ([sub] if sub else []) + ["", "## 章の導入文", "", B.read_new("ch%d_導入" % num).strip(), ""]
        S.append(("door", "第%d章" % num, "\n".join(L)))
        for name, items in groups:
            if name:
                pi = B.part_intro(num, name)
                S.append(("group", name, "# ■ %s\n" % name + ("\n## 編の導入文\n\n%s\n" % pi if pi else "")))
            for kk in items:
                S.append(("item", kk, item_md(kk)))
                for c in columns_after(kk):
                    S.append(("column", c[0], column_md(c)))
    km = kanmatsu()
    S.append(("text", "巻末　45を、1枚に", "# 巻末　45を、1枚に\n\n" + ichiran_md()))
    S.append(("text", "巻末　6つの言葉で、初めての場面を解く", "# 巻末　6つの言葉で、初めての場面を解く\n\n" + fix("6つの言葉", km["6つの言葉で、初めての場面を解く"])))
    S.append(("text", "巻末　保護者の方へ", "# 巻末　保護者の方へ\n\n" + fix("保護者の方へ", km["保護者の方へ"])))
    S.append(("text", "巻末　参考文献", "# 巻末　参考文献\n\n" + sankou_md(km["参考文献"])))
    ow = rd("manuscript/本文/v2/91_おわりに.md").strip()
    S.append(("text", "おわりに", fix("おわりに", ow)))
    return S


def check(S):
    ng = 0
    for w, a, b, _ in K.FIXES:
        if (w, a) not in USED_FIX:
            print("使われなかった直し:", w, a.strip()); ng += 1
    for kk in sorted(K.CH1_MOKUJI):
        it = ch1_item(kk)
        for lab in LABELS:
            if not it[lab].strip():
                print(kk, "空いている:", lab); ng += 1
        if not ch1_koma(it):
            print(kk, "2コマが読み取れない"); ng += 1
        if not ch1_sheet(kk, it):
            print(kk, "3STEPが読み取れない"); ng += 1
    for k in K.HITOKOTO:
        if not (k in K.CH1_MOKUJI or k in V.ITEMS):
            print("一言の置き場所がない:", k); ng += 1
    for kind, name, md in S:
        if "*" in md:
            print(name, "アスタリスクがある"); ng += 1
        for m in re.finditer(r"(?<![0-9])([0-9]{2})番", md):
            if not 1 <= int(m.group(1)) <= 45:
                print(name, "ない番号:", md[max(0, m.start() - 15):m.end() + 5].replace("\n", " ")); ng += 1
        for w in ("50個", "44個", "第8章", "合格法則", "今日やること"):
            if w in md and kind != "item":
                i = md.index(w)
                print(name, "前の形の言葉:", md[max(0, i - 20):i + 20].replace("\n", " ")); ng += 1
    return ng


def main():
    S = sections()
    ng = check(S)
    if "--log" in sys.argv:
        for w, a, b in LOG:
            print("[%s] %s  ⇒  %s" % (w, a, b))
    tot = {}
    for kind, name, md in S:
        tot[kind] = tot.get(kind, 0) + n(A.to_paste(md))
    if "--check" not in sys.argv:
        os.makedirs(os.path.join(OUT, "貼り付け用"), exist_ok=True)
        whole = "\n\n---\n\n".join(md.strip() for _, _, md in S) + "\n"
        with open(os.path.join(OUT, "完全版_仮.md"), "w", encoding="utf-8") as f:
            f.write(whole)
        with open(os.path.join(OUT, "貼り付け用", "完全版_仮.txt"), "w", encoding="utf-8") as f:
            f.write("\n\n\n".join(A.to_paste(md).strip() for _, _, md in S) + "\n")
    names = {"cover": "表紙", "text": "前付け・巻末・おわりに", "toc": "目次", "door": "章の扉と導入", "item1": "第1章の6項目",
             "item": "07〜45番", "column": "コラム", "group": "小見出し"}
    for k, v in tot.items():
        print("%-12s %7d字" % (names[k], v))
    print("合計 %d字　／　コラム %d本　／　王様の一言 %d個　／　直す所 %d件" % (sum(tot.values()), len(K.COLUMNS), len(K.HITOKOTO), ng))


if __name__ == "__main__":
    main()
