# -*- coding: utf-8 -*-
# 著者の手元の原稿（会話に貼ってもらった文を、そのまま保存したもの）を読む。
#   置き場所：manuscript/著者の最新原稿/日付.txt（一番新しい日付のものを使う。中身は、手で直さない）
#   2026-11-20：著者「最新の原稿は以下の通り。原稿確認ページは文字だけになるからね」
#   2026-11-22：第5章（31〜35番）の確定版を、著者が貼った（「よし確定！」）。前の日付の文の、第5章の所だけを、入れかえたもの
#   → ご確認ページは、このファイルの文字を、そのまま出す。目次と、言葉の資料も、ここの頭の2行の言葉に合わせる
#   差しかえ/番号.txt … あとから、著者が、その項目だけを貼り直したもの。あれば、その項目の本文は、こちらを使う
#     そのあと、著者の指示で直した所は、このファイルに入れていく（どこを直したかは、docs/08 に書く）
#     頭の2行は、もとの原稿の形（「27 × 頭のいい人は…」「→○ 頭のいい人は…」）のまま出す。貼り直した文の、題の行と、×○の行は、使わない
#   python3 -I scripts/author_doc.py   → 読み取った形を、画面に出す
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "manuscript", "著者の最新原稿")

MARK = "[⚫●]︎?"
TOP = re.compile(r"^%s(表紙・タイトル|巻頭ページ|目次|はじめに|この本の使い方|第(\d*)章)" % MARK)
ITEM1 = re.compile(r"^(0[1-6])(【絶対法則】(.+?))\s*$")                 # 第1章の項目の頭（01【絶対法則】疑う）
ITEM = re.compile(r"^\s*(\d\d) (× 頭のいい人は「(.*?)」.*?)\s*$")        # 07番から先の項目の頭（1行目）
MARU = re.compile(r"^(→○ 頭のいい人は「(.*?)」.*?)\s*$")                # 　　〃　　　　　　　　　（2行目）
EMPTY = re.compile(r"^\s*× 頭のいい人は「」")                            # まだ書いていない項目の枠
GROUP = re.compile(r"^[◻□]︎?(.+編)\s*$")                           # ◻︎理解編 など
KEYS = {"表紙・タイトル": "title", "巻頭ページ": "kantou", "目次": "mokuji", "はじめに": "hajimeni", "この本の使い方": "tsukaikata"}


def path():
    return os.path.join(DIR, sorted(fn for fn in os.listdir(DIR) if fn.endswith(".txt"))[-1])


def date():
    return os.path.basename(path())[:-4].replace("-", "/")


def parse():
    """[{kind, head, lines}] と、章は {kind:"chapter", num, head, intro, units:[("group", 名前) | ("item", 番号, [頭の行], [本文の行])]}。"""
    with open(path(), encoding="utf-8") as f:
        L = f.read().split("\n")
    secs, cur, last = [], None, 0
    for line in L:
        m = TOP.match(line)
        if m:
            head = re.sub("^" + MARK, "", line).strip()
            if m.group(1).startswith("第"):
                last = int(m.group(2)) if m.group(2) else last + 1
                cur = dict(kind="chapter", num=last, head=head, lines=[])
            else:
                cur = dict(kind=KEYS[m.group(1)], head=head, lines=[])
            secs.append(cur)
        elif cur is not None:
            cur["lines"].append(line)
    for s in secs:
        if s["kind"] != "chapter":
            continue
        s["intro"], s["units"] = [], []
        item = None
        for line in s["lines"]:
            g, a, b = GROUP.match(line), ITEM1.match(line), ITEM.match(line)
            if g:
                s["units"].append(("group", g.group(1)))
                item = None
            elif b and not b.group(3):
                item = ("empty", None, [], [])           # 番号だけ入っていて、言葉がまだの枠（消し忘れ）。中身は、捨てる
            elif a or b:
                m = a or b
                item = ("item", m.group(1), [m.group(2)], [])
                s["units"].append(item)
            elif EMPTY.match(line):
                item = ("empty", None, [], [])           # まだ書いていない枠。中身は、捨てる
            elif item is not None:
                if item[0] == "item" and len(item[2]) == 1 and not item[3] and MARU.match(line):
                    item[2].append(MARU.match(line).group(1))
                else:
                    item[3].append(line)
            else:
                s["intro"].append(line)
        for u in s["units"]:
            if u[0] == "item":
                r = replacement(u[1])
                if r is not None:
                    u[3][:] = r
    return secs


def replacement(no):
    """差しかえ/番号.txt があれば、その本文の行（○の行の、次から）。なければ None。"""
    q = os.path.join(DIR, "差しかえ", no + ".txt")
    if not os.path.exists(q):
        return None
    with open(q, encoding="utf-8") as f:
        L = f.read().split("\n")
    for i, line in enumerate(L[:8]):
        if re.match(r"^○[\s\u3000]*頭のいい人は", line):
            return L[i + 1:]
    return L


def heads():
    """{番号: (やらない言葉, やる言葉)}。07番から先で、頭の2行に言葉が入っている項目だけ。"""
    out = {}
    for s in parse():
        if s["kind"] != "chapter":
            continue
        for u in s["units"]:
            if u[0] == "item" and len(u[2]) == 2:
                x, o = ITEM.match(u[1] + " " + u[2][0]).group(3), MARU.match(u[2][1]).group(2)
                if x and o:
                    out[u[1]] = (x, o)
    return out


def items(s):
    return [u for u in s["units"] if u[0] == "item"]


if __name__ == "__main__":
    print(path())
    for s in parse():
        if s["kind"] == "chapter":
            print("第%d章　%s　｜導入 %d行｜項目 %s" % (s["num"], s["head"], sum(1 for x in s["intro"] if x.strip()), " ".join(u[1] for u in items(s)) or "なし"))
            for u in s["units"]:
                print("   ", u[0], u[1], (" / ".join(u[2]) + "　本文 %d行" % sum(1 for x in u[3] if x.strip())) if u[0] == "item" else "")
        else:
            print(s["kind"], s["head"], "｜%d行" % sum(1 for x in s["lines"] if x.strip()))
    print(heads())
