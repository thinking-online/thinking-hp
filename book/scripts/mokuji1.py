# -*- coding: utf-8 -*-
# 目次（1行の形）。1項目を1行にして、左に「やらないこと」、右に「かわりにやること」を並べる（2026-11-19 の案A。2026-11-20 に、著者がこの形で最新版を求めた）。
#   python3 -I scripts/mokuji1.py   → manuscript/目次_最新.md に書き出して、画面にも出す
# 言葉の出どころ：
#   07〜40番のうち、頭の2行（v4_data の pair）がある項目は、その言葉を、そのまま使う（目次と、項目の頭が、同じ言葉になる）
#   第1章（01〜06番）、07・08番、第7章（41〜46番）は、頭の2行をまだ短くしていないので、下の KARI の言葉を使う（著者が貼った目次の言葉）
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import v4_data as V
import book_data as K
import author_doc as AD
AUTHOR = AD.heads()   # 著者の手元の原稿の、頭の2行の言葉（2026-11-20 から、これが一番新しい）

MAE = ["10秒だけ、付き合ってください", "はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」", "この本の使い方"]
ATO = ["巻末　%dを、1枚に", "巻末　6つの言葉で、初めての場面を解く", "巻末　保護者の方へ", "巻末　参考文献", "おわりに　笑わなかった人が、1人だけいました"]
CH1_FUDA = "6つの絶対法則"
KARI = {
    "01": ("「みんなやってるから」で選ぶ", "一度、疑ってから選ぶ"),
    "02": ("覚えるために、何度も読む", "閉じて、何も見ずに思い出す"),
    "03": ("スラスラ進むやり方を選ぶ", "「うーん」となるほうを選ぶ"),
    "04": ("やみくもに、全部頑張る", "先に、やらないことを決める"),
    "05": ("まとめて、一気にやる", "分けて、別の日にもう一度やる"),
    "06": ("基礎を固めてから、解く", "早く解いて、早く直す"),
    "07": ("説明できないまま、次へ進む", "キーワード3つで、30秒説明する"),
    "08": ("1ページ目から、丁寧に読む", "先に、全体像をさっとつかむ"),
    "41": ("全部、1人でやろうとする", "途中で見せて、直す所を聞く"),
    "42": ("「全部わかりません」と聞く", "「ここまではわかります」と聞く"),
    "43": ("AIに、答えを聞く", "AIに、ヒントと反論をもらう"),
    "44": ("「AIはズルだ」と、避ける", "分析と問題づくりを、任せる"),
    "45": ("「もったいない」で、決める", "これからの時間で、決める"),
    "46": ("合格を、ゴールにする", "勝ったら、次の勝負を決める"),
}
N_ALL = 6 + len(V.ITEMS)
W = 16   # ×の言葉の幅（全角の字の数。これより短い言葉は、全角の空白で埋める）


def pair(kk):
    """（やらないこと, かわりにやること）。著者の手元の原稿に頭の2行がある項目は、その言葉。なければ、こちらの原稿の頭の2行。それもなければ、仮の言葉。"""
    if kk in AUTHOR:
        return AUTHOR[kk]
    if kk in V.ITEMS and V.ITEMS[kk].get("pair"):
        return V.ITEMS[kk]["pair"]
    return KARI[kk]


def chapters():
    """[(章の番号, 札, 題, [(小見出し, [項目の番号])])]。第1章も入れる。"""
    out = [(1, CH1_FUDA, K.CH1_TITLE, [(None, sorted(K.CH1_MOKUJI))])]
    return out + [(num, fuda, title, groups) for num, fuda, title, sub, groups in V.CHAPTERS]


def line(kk):
    x, o = pair(kk)
    return "%s　%s%s　→　%s" % (kk, x, "　" * max(0, W - len(x)), o)


def text():
    L = ["⚫︎目次"] + MAE + [""]
    for num, fuda, title, groups in chapters():
        L += ["第%d章　" % num, "【%s】%s" % (fuda, title)]
        for name, items in groups:
            if name:
                L.append("■ " + name)
            L += [line(kk) for kk in items]
        L.append("")
    L += [a % N_ALL if "%d" in a else a for a in ATO]
    return "\n".join(L) + "\n"


def main():
    t = text()
    p = os.path.join(ROOT, "manuscript", "目次_最新.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("# 目次（1行の形。%d項目）\n\n`python3 -I scripts/mokuji1.py` で、今の原稿の言葉から作り直す。手で直さない。\n\n```\n%s```\n" % (N_ALL, t))
    print(t)


if __name__ == "__main__":
    main()
