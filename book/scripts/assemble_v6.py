# -*- coding: utf-8 -*-
# 35個の版（第1章の6個 ＋ 29個）を、表紙から「おわりに」まで組む。仮。
#   python3 -I scripts/assemble_v6.py           → manuscript/35個版/ に書き出す
#   python3 -I scripts/assemble_v6.py --check   → 調べるだけ
#   python3 -I scripts/assemble_v6.py --log     → 番号を直した所を出す
# もとは、45個の版（scripts/assemble_book.py）。そこから、(1) 07番から先を29個にして、番号をつけ直す
# (2) 前付け・第1章・巻末の中の番号と、「45個」「39個」の数を直す (3) コラムと王様の一言の置き場所を直す。
# 07番から先の本文は manuscript/本文/v6/NN.md（番号の対応と、行の調べ方は scripts/v6.py）。
# 本の形のPDFは scripts/build_tate_book.py s35（このファイルの Z6・K6・V6・B6 を、45個の版のかわりに使う）。
import os, re, sys, types
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_book as Z
import book_data as K
import v4_data as V
import assemble_v4 as B
import assemble_v3 as A
import v6 as F

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "manuscript", "35個版")
N_ALL = 6 + len(F.OLD)     # 35
LOG = []


def n2(k):
    """45個の版の番号 → 35個の版の番号。01〜06はそのまま。なくなった項目は None。"""
    return k if int(k) <= 6 else F.NEW.get(k)


def fixnum(t, where, tables=False):
    """文の中の「NN番」を直す。tables=True の時は、表の右はしの番号と「→NN」も直す（使い方の索引、第1章の表、参考文献）。"""
    out = []
    for l in t.split("\n"):
        o = l
        def f(m):
            k2 = n2(m.group(1))
            if k2 is None:
                raise SystemExit("%s: なくなった項目を指している: %s" % (where, l.strip()))
            return k2 + "番"
        l = re.sub(r"(?<![0-9])([0-9]{2})番", f, l)
        l = re.sub(r"([0-9]{2})番(?:と|、|・|や)\1番", r"\1番", l)   # まとめた結果、同じ番号が2つ並んだ所は、1つにする
        if tables:
            arrow = re.search(r"→[　 ]*[0-9]{2}(?=[ 　]|$)", l)
            if arrow:
                def g(m):
                    k2 = n2(m.group(2))
                    if k2 is None:
                        raise SystemExit("%s: なくなった項目を指している: %s" % (where, l.strip()))
                    return "→" + m.group(1) + k2
                l = re.sub(r"→([　 ]*)([0-9]{2})(?=[ 　]|$)", g, l)
            else:
                m = re.match(r"^(.*?[^0-9　 ])((?:[　 ]+[0-9]{2})+)[　 ]*$", l)
                if m and "　" in m.group(2) and not re.search(r"[0-9]$", m.group(1)):
                    seen = []
                    for k in re.findall(r"[0-9]{2}", m.group(2)):
                        k2 = n2(k)
                        if k2 and k2 not in seen:
                            seen.append(k2)
                    if not seen:
                        LOG.append((where, o.strip(), "（行ごと外した）"))
                        continue
                    l = m.group(1) + re.match(r"^[　 ]+", m.group(2)).group(0) + "　".join(sorted(seen))
        if l != o:
            LOG.append((where, o.strip(), l.strip()))
        out.append(l)
    return "\n".join(out)


# 数の直し（どこ, 前, 後）。どれも、45個 → 35個、39個 → 29個
COUNT = [
    ("10秒だけ、付き合ってください", "45個。1つ残らず書きます。", "35個。1つ残らず書きます。"),
    ("はじめに", "の場面ごとの、39個", "の場面ごとの、29個"),
    ("はじめに", "45個、全部こうなっています。", "35個、全部こうなっています。"),
    ("この本の使い方", "第2章から先の39個は", "第2章から先の29個は"),
    ("この本の使い方", "## 45個とも、同じ順番で書いてあります", "## 35個とも、同じ順番で書いてあります"),
    ("この本の使い方", "45個を全部やろうとしなくていいです。", "35個を全部やろうとしなくていいです。"),
    ("02", "特別な方法を、45個も知っているわけ", "特別な方法を、35個も知っているわけ"),
    ("02", "だから、45個を全部は覚えられなくても", "だから、35個を全部は覚えられなくても"),
    ("巻末　保護者の方へ", "この本に書いた45個は", "この本に書いた35個は"),
    ("おわりに", "この本を、明日から45個、全部やろうとしないでください。", "この本を、明日から35個、全部やろうとしないでください。"),
    ("おわりに", "45個のうち、半分以上が当てはまったと思います。", "35個のうち、半分以上が当てはまったと思います。"),
]
USED = set()


def count(where, t):
    for w, a, b in COUNT:
        if w == where:
            if a not in t:
                raise SystemExit("%s: 数を直す言葉が見つからない: %s" % (where, a))
            USED.add((w, a))
            t = t.replace(a, b)
    return t


# ---------------------------------------------------------------- 07番から先（29個）
def _item(nn):
    return V.ITEMS[F.OLD[nn]]


class _B6:
    n = staticmethod(B.n)

    @staticmethod
    def body(nn):
        return F.body(nn)

    @staticmethod
    def koma(nn):
        return B.koma(F.OLD[nn])

    @staticmethod
    def sheet(nn):
        ttl, steps, king = B.sheet(F.OLD[nn])
        r = lambda s: fixnum(s, nn) if s else s
        return ttl, [(r(h), r(v), r(note)) for h, v, note in steps], r(king)

    @staticmethod
    def matome(nn):
        one, pts, dakara, toi = B.matome(F.OLD[nn])
        r = lambda s: fixnum(s, nn)
        return r(one), [r(p) for p in pts], r(dakara), r(toi)

    @staticmethod
    def read_new(name):
        t = fixnum(B.read_new(name), name)
        # 「計画編（25〜29番）」のような、番号の幅は、35個の版の小見出しから入れ直す
        for _, gs in F.GROUPS:
            for g, ks in gs:
                if g:
                    t = re.sub(re.escape(g) + r"（[0-9]{2}〜[0-9]{2}番）", "%s（%s〜%s番）" % (g, F.NEW[ks[0]], F.NEW[ks[-1]]), t)
        return t


B6 = _B6()
V6 = types.SimpleNamespace(
    # pair（項目の頭の、短い「しない／する」）は、45個の版のものを、そのまま使う。まとめた項目で、目次の言葉を変えたものは、そちらを使う
    ITEMS={nn: dict(dict(t=_item(nn)["t"], q=_item(nn)["q"], x=_item(nn)["x"], o=_item(nn)["o"]),
                    **({"pair": _item(nn)["pair"]} if "pair" in _item(nn) and nn not in F.OVERRIDE else {}), **F.OVERRIDE.get(nn, {})) for nn in F.OLD},
    CHAPTERS=[(num, fuda, title, sub, [(name, [F.NEW[k] for k in ks]) for name, ks in dict(F.GROUPS)[num]])
              for num, fuda, title, sub, _ in V.CHAPTERS])

# 王様の一言：残る項目は新しい番号へ。まとめた項目のものは、まとめ先に一言がなければ、そこへ移す
HITOKOTO = {}
for k, v in K.HITOKOTO.items():
    if int(k) <= 6 or k in F.KEEP:
        HITOKOTO[n2(k)] = v
for k, v in K.HITOKOTO.items():
    if k in F.ABSORB and F.NEW[k] not in HITOKOTO:
        HITOKOTO[F.NEW[k]] = v
HITO_OUT = [k for k in K.HITOKOTO if k in F.ABSORB and HITOKOTO.get(F.NEW[k]) != K.HITOKOTO[k]] + [k for k in K.HITOKOTO if k in F.TO_COLUMN]

# コラム（どの項目の後に置くか＝35個の版の番号, もと, ファイル）
COLUMNS = [
    ("06", "v2", "col_ch1_1"),                 # ダメなままでいることこそ、ダメだ
    ("09", "v2", "col_ch6_2"),                 # 休憩の質
    ("13", "v2", "col_ch3_2"),                 # 勉強場所（45個の版では14番の後）
    ("22", "v2", "col_ch3_1"),                 # 参考書を選ぶ3つの基準（24番の後）
    ("24", "v4", "col_でもだって"),              # 27番の後
    ("26", "v2", "col_ch4_1"),                 # 「〜しちゃう」（31番の後 → まとめ先の30番の後）
    ("25", "v2", "col_ch6_1"),                 # 空気に流されるな（32番の後 → まとめ先の29番の後）
    ("29", "v4", "col_未来の自分からの手紙"),      # 35番の後
    ("31", "v2", "col_ch2_1"),                 # 周りの5人（40番の後 → 友達と比べる話の後に移した）
    ("32", "v4", "col_冷笑"),                   # 39番の後
    ("33", "v2", "col_ch7_1"),                 # 無駄なプライド（41番の後）
    ("34", "v6", "col_値段"),                   # 新：45個の版の44番を、コラムにしたもの
    ("35", "v4", "col_決断"),                   # 決断する時に自分に聞くこと（44番の後 → 最後の項目の後）
]
K6 = types.SimpleNamespace(**{k: getattr(K, k) for k in dir(K) if not k.startswith("_")})
K6.HITOKOTO, K6.COLUMNS, K6.N_ALL = HITOKOTO, COLUMNS, N_ALL


def column(src, name):
    """(題, 本文)"""
    if src == "v6":
        p = os.path.join(F.DIR, name + ".md")
        if not os.path.exists(p):
            return None
        head, body = open(p, encoding="utf-8").read().strip().split("\n", 1)
        return head[2:].strip().replace("コラム　", "", 1), body.strip()
    title, body = Z.column(src, name)
    return title, fixnum(body, name)


def columns_after(nn):
    return [c for c in (column(s, nm) for k, s, nm in COLUMNS if k == nn) if c]


def ch1_item(kk):
    it = Z.ch1_item(kk)
    return {lab: count(kk, fixnum(t, kk, tables=True)) if lab == "本文" else fixnum(t, kk, tables=True) for lab, t in it.items()}


def hitokoto_md(nn):
    return ["## 王様の一言", "", "「%s」" % HITOKOTO[nn], ""] if nn in HITOKOTO else []


def ch1_item_md(kk):
    it = ch1_item(kk)
    L = ["# %s　絶対法則%s　%s" % (kk, kk, Z.ch1_name(kk)), ""]
    for lab in Z.LABELS:
        L += ["## " + lab, "", Z.body_md(it[lab]) if lab in ("本文", "導入文") else it[lab].strip(), ""]
    return "\n".join(L + hitokoto_md(kk))


def item_md(nn):
    it = V6.ITEMS[nn]
    c = B6.koma(nn)
    ttl, steps, king = B6.sheet(nn)
    one, pts, dakara, toi = B6.matome(nn)
    b = B6.body(nn)
    b = re.sub(r"^### ", "#### ", b, flags=re.M)
    b = re.sub(r"^## ", "### ", b, flags=re.M)
    atama = (["## しないこと、すること", ""] + B.pair_lines(it)) if B.ATAMA == "pair" else ["## 質問ページ", "", "頭のいい人が絶対やらないこと", "「%s」" % it["q"], "じゃあ、何をするの？"]
    L = ["# %s　%s" % (nn, it["t"]), ""] + atama + ["", "## 本文", "",
         b.rstrip(), "", "## 頭のいい人と伸びない人の違い", "", "伸びない人", c[0][0], c[0][1], "", "頭のいい人", c[1][0], c[1][1], ""]
    if B.OWARI == "moji":   # 文字の3STEPと、端的なまとめ（45個の版と同じ形）
        L += ["## 今日からできる3STEP", ""]
        for i, (h, v, note) in enumerate(steps, 1):
            L += ["STEP0%d　%s" % (i, h)] + (["※" + note] if note else [])
        L += ["「できた」の基準：" + king, "", "## まとめ", "", one, dakara, "迷ったら、自分に聞きます。「%s」" % toi, ""]
        return "\n".join(L + hitokoto_md(nn))
    L += ["## 今日からできる3STEP", "", "題：頭のいい人の『%s』3STEP" % ttl, ""]
    for i, (h, v, note) in enumerate(steps, 1):
        L += ["STEP0%d" % i, h, "「%s」" % v] + (["※" + note] if note else []) + [""]
    L += ["## できた基準", "", king, "", "## まとめ", "", one, "", "```"] + ["　　%d　%s" % (i, p) for i, p in enumerate(pts, 1)]
    L += ["```", "", dakara, "迷ったら、自分に聞きます。「%s」" % toi, ""]
    return "\n".join(L + hitokoto_md(nn))


def mokuji_md():
    L = ["10秒だけ、付き合ってください", "はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」", "この本の使い方", "",
         "第1章　%s" % K.CH1_TITLE, "　　　　【%s】" % K.CH1_SUB, ""]
    def cols(nn):
        cs = columns_after(nn)
        return ["　コラム　%s" % c[0] for c in cs] + ([""] if cs else [])
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L += ["　%s　%s　［%s］" % (kk, t, nm), "　　　×　%s" % x, "　　　○　%s" % o, ""] + cols(kk)
    for num, fuda, title, sub, groups in V6.CHAPTERS:
        L += ["第%d章　【%s】%s" % (num, fuda, title)] + (["　　　　%s" % sub] if sub else []) + [""]
        for name, items in groups:
            if name:
                L += ["　■ %s" % name, ""]
            for nn in items:
                it = V6.ITEMS[nn]
                L += ["　%s　%s" % (nn, it["t"]), "　　　×　%s" % it["x"], "　　　○　%s" % it["o"], ""] + cols(nn)
    return "\n".join(L + ["巻末　%dを、1枚に" % N_ALL, "巻末　6つの言葉で、初めての場面を解く", "巻末　保護者の方へ", "巻末　参考文献",
                          "おわりに　笑わなかった人が、1人だけいました"])


def ichiran_md():
    L = ["%d個を、1枚にまとめました。左が、頭のいい人が絶対やらないこと。右が、かわりにやっていることです。" % N_ALL, "",
         "第1章　%s" % K.CH1_TITLE, "", "```"]
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L.append("　%s　×　%s　→　○　%s" % (kk, t, o))
    L += ["```", ""]
    for num, fuda, title, sub, groups in V6.CHAPTERS:
        L += ["第%d章　【%s】%s" % (num, fuda, title), "", "```"]
        L += ["　%s　×　%s　→　○　%s" % (nn, V6.ITEMS[nn]["t"], V6.ITEMS[nn]["o"]) for _, items in groups for nn in items]
        L += ["```", ""]
    return "\n".join(L)


def sections():
    """本の頭から順に、(種類, 名前, md)。45個の版と同じ並び。"""
    base = {name: md for kind, name, md in Z.sections() if kind in ("cover", "text")}
    S = [("cover", "表紙", base["表紙"])]
    def text(name, tables=False, new_name=None):
        md = count(name, fixnum(base[name], name, tables))
        S.append(("text", new_name or name, md))
    text("10秒だけ、付き合ってください")
    S.append(("toc", "目次", "# 目次\n\n```\n" + mokuji_md() + "\n```\n"))
    text("はじめに")
    text("この本の使い方", tables=True)
    S.append(("door", "第1章", "\n".join(["# 第1章　%s" % K.CH1_TITLE, "【%s】" % K.CH1_SUB, "", "## 章の導入文", "", Z.to_md(Z.master(K.CH1_INTRO))])))
    def cols(nn):
        for c in columns_after(nn):
            S.append(("column", c[0], "\n".join(["# コラム　%s" % c[0], "", c[1], ""])))
    for kk in sorted(K.CH1_MOKUJI):
        S.append(("item1", kk, ch1_item_md(kk)))
        cols(kk)
    for num, fuda, title, sub, groups in V6.CHAPTERS:
        L = ["# 第%d章　【%s】%s" % (num, fuda, title)] + ([sub] if sub else []) + ["", "## 章の導入文", "", B6.read_new("ch%d_導入" % num).strip(), ""]
        S.append(("door", "第%d章" % num, "\n".join(L)))
        for name, items in groups:
            if name:
                S.append(("group", name, "# ■ %s\n" % name))
            for nn in items:
                S.append(("item", nn, item_md(nn)))
                cols(nn)
    S.append(("text", "巻末　%dを、1枚に" % N_ALL, "# 巻末　%dを、1枚に\n\n" % N_ALL + ichiran_md()))
    text("巻末　6つの言葉で、初めての場面を解く")
    text("巻末　保護者の方へ")
    text("巻末　参考文献", tables=True)
    text("おわりに")
    return S


# 本の形のPDF（scripts/build_tate_book.py）が、45個の版の Z のかわりに使うもの
Z6 = types.SimpleNamespace(sections=sections, ch1_item=ch1_item, ch1_sheet=Z.ch1_sheet, ch1_koma=Z.ch1_koma, body_md=Z.body_md, ch1_name=Z.ch1_name,
                           columns_after=columns_after, column=column, nonempty=Z.nonempty, to_md=Z.to_md, master=Z.master, LABELS=Z.LABELS)


def check(S):
    ng = 0
    for w, a, b in COUNT:
        if (w, a) not in USED:
            print("使われなかった数の直し:", w, a); ng += 1
    for kind, name, md in S:
        if "*" in md:
            print(name, "アスタリスクがある"); ng += 1
        for m in re.finditer(r"(?<![0-9])([0-9]{2})番", md):
            if not 1 <= int(m.group(1)) <= N_ALL:
                print(name, "ない番号:", md[max(0, m.start() - 15):m.end() + 5].replace("\n", " ")); ng += 1
            if kind == "item" and m.group(1) == name:
                print(name, "自分の番号を指している:", md[max(0, m.start() - 15):m.end() + 5].replace("\n", " ")); ng += 1
        for w in ("45個", "39個", "50個", "45のうち", "45を、1枚"):
            if w in md:
                i = md.index(w)
                print(name, "前の数が残っている:", md[max(0, i - 20):i + 20].replace("\n", " ")); ng += 1
    for nn in sorted(F.OLD):
        ng += len(F.problems(nn))
    if not column("v6", "col_値段"):
        print("コラム（値段）のファイルが、まだない"); ng += 1
    return ng


def main():
    S = sections()
    ng = check(S)
    if "--log" in sys.argv:
        for w, a, b in LOG:
            print("[%s] %s  ⇒  %s" % (w, a, b))
    tot = {}
    for kind, name, md in S:
        tot[kind] = tot.get(kind, 0) + A.n(A.to_paste(md))
    if "--check" not in sys.argv:
        os.makedirs(os.path.join(OUT, "貼り付け用"), exist_ok=True)
        with open(os.path.join(OUT, "完全版_35個.md"), "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(md.strip() for _, _, md in S) + "\n")
        with open(os.path.join(OUT, "貼り付け用", "完全版_35個.txt"), "w", encoding="utf-8") as f:
            f.write("\n\n\n".join(A.to_paste(md).strip() for _, _, md in S) + "\n")
    names = {"cover": "表紙", "text": "前付け・巻末・おわりに", "toc": "目次", "door": "章の扉と導入", "item1": "第1章の6項目",
             "item": "07〜%d番" % N_ALL, "column": "コラム", "group": "小見出し"}
    for k, v in tot.items():
        print("%-12s %7d字" % (names[k], v))
    print("合計 %d字　／　項目 %d個　／　コラム %d本　／　王様の一言 %d個（外したもの：%s）　／　直す所 %d件"
          % (sum(tot.values()), N_ALL, sum(1 for k, _, _ in S if k == "column"), len(HITOKOTO), " ".join(HITO_OUT) or "なし", ng))


if __name__ == "__main__":
    main()
