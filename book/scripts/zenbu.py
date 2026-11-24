# -*- coding: utf-8 -*-
# 今の原稿を、1つのページにまとめる（著者が、通して確認するためのもの。本を組む道具ではない）
#   python3 -I scripts/zenbu.py 出す先.html
# 中身の出どころ：
#   巻頭〜第5章（01〜35番）　著者の手元の原稿（manuscript/著者の最新原稿/ の一番新しいもの）。27番は「差しかえ」のもの
#   第5章の導入、第6章の導入と36〜40番　こちらの作業用の文（本文/v4/）
#   第7章の導入と41〜45番　下書き（本文/v4/案_第7章_5つ/。本には、まだ入れていない）
#   コラム、おわりに　今、本に入っているもの
import html, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import v4_data as V
import assemble_v4 as B
import book_data as K

def rd(*p):
    return open(os.path.join(ROOT, *p), encoding="utf-8").read()

def md_to_doc(md):
    """作業用の文（## 見出し、``` の表、== の印）を、著者のドキュメントの形にする"""
    out, code = [], False
    for line in md.split("\n"):
        s = line.rstrip()
        if s.strip().startswith("```"):
            code = not code
            if out and out[-1] != "":
                out.append("")
            continue
        s = s.replace("==", "")
        if s.startswith("#"):
            if out and out[-1] != "":
                out.append("")
            out.append("⚫︎" + s.lstrip("# "))
            continue
        if code:
            s = re.sub(r"^　　", "", s)
        out.append(s)
    res = []
    for s in out:
        if s == "" and res and (res[-1] == "" or res[-1].startswith("⚫︎") or res[-1] == "……"):
            continue
        res.append(s)
    while res and res[-1] == "":
        res.pop()
    return "\n".join(res)

def item_v4(no):
    it = V.ITEMS[no]
    x, o = it["pair"]
    ttl, steps, king = B.sheet(no)
    m = it["matome"]
    t = ["%s × 頭のいい人は「%s」をしない。" % (no, x), "→○ 頭のいい人は「%s」をする" % o, "", md_to_doc(rd("manuscript", "本文", "v4", no + ".md")), "", "今日からできる3STEP"]
    for i, st in enumerate(steps, 1):
        t += ["STEP0%d" % i, st[0], ""]
    t += ["「できた」の基準", king, "", "まとめ", m[0], m[2], "迷ったら、自分に聞きます。「%s」" % m[3]]
    return "\n".join(t)

DRAFT = os.path.join("manuscript", "本文", "v4", "案_第7章_5つ")
def item_draft(no):
    lst = rd(DRAFT, "頭の2行と3STEP.md")
    m = re.search(r"## %s　×(.+?)　○(.+?)\n(?:一言：.*\n)?3STEP：(.+?)\n基準：(.+?)\nまとめ：(.+?)\n" % no, lst)
    x, o, steps, king, mat = m.groups()
    s, mm = steps.split("／"), mat.split("／")
    t = ["%s × 頭のいい人は「%s」をしない。" % (no, x), "→○ 頭のいい人は「%s」をする" % o, "", md_to_doc(rd(DRAFT, no + ".md")), "", "今日からできる3STEP"]
    for i, st in enumerate(s, 1):
        t += ["STEP0%d" % i, st, ""]
    t += ["「できた」の基準", king, "", "まとめ", mm[0], mm[1], "迷ったら、自分に聞きます。" + mm[2]]
    return "\n".join(t)

def master():
    f = sorted(glob.glob(os.path.join(ROOT, "manuscript", "著者の最新原稿", "*.txt")))[-1]
    return os.path.basename(f), open(f, encoding="utf-8").read().split("\n")

def main(dst):
    name, L = master()
    idx = lambda pat, a=0: next(i for i in range(a, len(L)) if re.match(pat, L[i]))
    secs = []   # (id, 目次に出す名前, 段, 本文, 注)
    cut = [("kantou", "表紙・巻頭ページ", r"⚫︎表紙"), ("hajimeni", "はじめに", r"⚫︎はじめに"), ("tsukaikata", "この本の使い方", r"⚫︎この本の使い方"),
           ("ch1", "第1章　6つの絶対法則（01〜06番）", r"⚫︎第1章"), ("ch2", "第2章【インプット】（07〜15番）", r"⚫︎第2章"), ("ch3", "第3章【アウトプット】（16〜25番）", r"⚫︎第3章"),
           ("ch4", "第4章【計画】（26〜30番）", r"⚫︎第4章"), ("ch5", "第5章【集中】（31〜35番）", r"⚫︎第5章"), ("end", "", r"⚫︎第6章")]
    pos = [idx(p) for _, _, p in cut]
    for (sid, ttl, _), a, b in zip(cut[:-1], pos[:-1], pos[1:]):
        body = L[a:b]
        note = "著者の手元の原稿（%s）のまま" % name
        if sid == "ch4":   # 27番は、差しかえの文を使う
            i27 = next(i for i, s in enumerate(body) if s.startswith("27 ×")); i28 = next(i for i, s in enumerate(body) if s.startswith("28 ×"))
            r27 = rd("manuscript", "著者の最新原稿", "差しかえ", "27.txt").rstrip("\n")
            r27 = re.sub(r"\A27　.*\n\n×　(.+)\n○　(.+?)。?\n", lambda m: "27 × %s\n→○ %s\n" % (m.group(1), m.group(2)), r27)   # 頭の2行を、ほかの項目と同じ形に
            body = body[:i27] + r27.split("\n") + ["", ""] + body[i28:]
            note += "。27番は、差しかえの文"
        if sid == "ch5":   # 導入は、作業用の文。空のひな形は、外す
            i31 = next(i for i, s in enumerate(body) if s.startswith("31 ×"))
            body = [body[0], ""] + md_to_doc(rd("manuscript", "本文", "v4", "ch5_導入.md")).split("\n") + ["", ""] + body[i31:]
            j = next((i for i, s in enumerate(body) if s.startswith("35 × 頭のいい人は「」")), None)
            if j is not None:
                del body[j:j + 3]
            note += "。導入は、こちらの作業用の文"
        secs.append((sid, ttl, 0, "\n".join(body).strip("\n"), note))
    ch6 = ["⚫︎第6章【モチベ】頭のいい人は、「気持ち」で止まらない（題は仮）", "", md_to_doc(rd("manuscript", "本文", "v4", "ch6_導入.md")), ""]
    for no in ["36", "37", "38", "39", "40"]:
        ch6 += ["", item_v4(no), ""]
    secs.append(("ch6", "第6章【モチベ】（36〜40番）", 0, "\n".join(ch6).strip("\n"), "こちらの作業用の文（著者と1つずつ詰めたもの）"))
    ch7 = ["⚫︎第7章【アップデート】頭のいい人は、（題は、まだ）", "", md_to_doc(rd(DRAFT, "ch7_導入.md")), ""]
    for no in ["41", "42", "43", "44", "45"]:
        ch7 += ["", item_draft(no), ""]
    secs.append(("ch7", "第7章【アップデート】（41〜45番）", 0, "\n".join(ch7).strip("\n"), "下書き。本には、まだ入れていない（本の中は、前の41〜46番のまま）"))
    col = []
    for after, ver, fn in K.COLUMNS:
        col += [md_to_doc(rd("manuscript", "本文", ver, fn + ".md")).replace("⚫︎コラム", "⚫︎コラム", 1), "（置き場：%s番のあと）" % after, "", ""]
    secs.append(("column", "コラム（12本）", 0, "\n".join(col).strip("\n"), "今、本に入っているもの。第7章を5つにしたあとの置き場は、まだ決めていない"))
    secs.append(("owarini", "おわりに", 0, md_to_doc(rd("manuscript", "本文", "v2", "91_おわりに.md")), "11月15日の下書きのまま。まだ、今の本に合わせていない"))

    def anchors(sid, text):
        """本文の中の項目の頭（NN × … / NN【絶対法則】）に、目次から飛べる印をつける"""
        out, toc = [], []
        for line in text.split("\n"):
            m = re.match(r"\s?(\d\d)( × 頭のいい人は「.+」|【絶対法則】)", line) or (sid == "column" and re.match(r"⚫︎コラム　(.+)", line))
            e = html.escape(line, quote=False)
            if m:
                aid = "%s-%s" % (sid, m.group(1) if sid != "column" else str(len(toc) + 1))
                if aid not in [a for a, _ in toc]:
                    toc.append((aid, line.strip()))
                    e = '<span id="%s" class="it">%s</span>' % (aid, e)
            elif line.startswith("⚫︎"):
                e = '<span class="hd">%s</span>' % e
            out.append(e)
        return "\n".join(out), toc

    def label(t):
        if t.startswith("⚫︎コラム"):
            return t.replace("⚫︎コラム　", "")
        return re.sub(r"^(\d\d) × 頭のいい人は「(.+?)」.*$", r"\1　\2", t)
    nav, body, n = [], [], 0
    for sid, ttl, _, text, note in secs:
        h, toc = anchors(sid, text)
        n += len(re.sub(r"\s", "", text))
        nav.append('<li><a href="#%s">%s</a>%s</li>' % (sid, html.escape(ttl), ("<ul>" + "".join('<li><a href="#%s">%s</a></li>' % (a, html.escape(label(t))) for a, t in toc) + "</ul>") if toc else ""))
        body.append('<section id="%s"><h2>%s</h2><p class="note">%s</p><div class="tx">%s</div><p class="up"><a href="#top">↑ 目次へ</a></p></section>' % (sid, html.escape(ttl), html.escape(note), h))
    page = """<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>今の原稿（通し）</title>
<style>
:root{--bg:#f6f5f1;--pa:#fff;--fg:#1c1d21;--mu:#666b76;--li:#dcdfe6;--ac:#15467e;--hd:#0f2f57;--it:#fff3d6}
@media(prefers-color-scheme:dark){:root{--bg:#15171b;--pa:#1d2026;--fg:#e8e9ec;--mu:#9aa0ab;--li:#33373f;--ac:#8fb8ee;--hd:#b9d3f5;--it:#3a321c;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.95 "Hiragino Sans","Noto Sans JP","Yu Gothic",sans-serif}
main{max-width:780px;margin:0 auto;padding:24px max(16px,env(safe-area-inset-left,0px)) 80px}
h1{font-size:24px;line-height:1.5;margin:8px 0 4px}h2{font-size:20px;line-height:1.5;margin:0 0 4px;color:var(--hd)}
.lead{color:var(--mu);font-size:14px;margin:0 0 18px}
nav{background:var(--pa);border:1px solid var(--li);border-radius:10px;padding:14px 18px;margin:0 0 28px}
nav>ul{margin:0;padding-left:1.2em}nav ul ul{font-size:14px;color:var(--mu);columns:2;column-gap:24px;padding-left:1.1em;margin:2px 0 8px}
@media(max-width:560px){nav ul ul{columns:1}}
a{color:var(--ac);text-decoration:none}a:hover{text-decoration:underline}
section{background:var(--pa);border:1px solid var(--li);border-radius:10px;padding:22px 22px 10px;margin:0 0 26px;scroll-margin-top:10px}
.note{color:var(--mu);font-size:13px;margin:0 0 14px;padding-bottom:10px;border-bottom:1px solid var(--li)}
.tx{white-space:pre-wrap;word-break:break-word;overflow-wrap:anywhere}
.hd{font-weight:700;color:var(--hd)}.it{font-weight:700;background:var(--it);padding:2px 4px;border-radius:4px;scroll-margin-top:12px}
.up{text-align:right;font-size:13px;margin:14px 0 6px}
</style></head><body><main id="top">
<h1>今の原稿（通し）</h1>
<p class="lead">%s 時点。全部で 約%s字（空白をのぞく）。各部分の上に、どこから持ってきた文かを書いてあります。</p>
<nav><ul>%s</ul></nav>
%s
</main></body></html>""" % (DATE, "{:,}".format(n), "".join(nav), "\n".join(body))
    open(dst, "w", encoding="utf-8").write(page)
    txt = "\n\n\n".join("＝＝＝＝＝ %s ＝＝＝＝＝\n（%s）\n\n%s" % (ttl, note, text) for _, ttl, _, text, note in secs)
    open(os.path.splitext(dst)[0] + ".txt", "w", encoding="utf-8").write(txt + "\n")
    print("出した：", dst, "／ 字数", n, "／ 部分", len(secs))
    for sid, ttl, _, text, note in secs:
        print("　", ttl, len(re.sub(r"\s", "", text)), "字")

DATE = "2026年11月24日"
if __name__ == "__main__":
    main(sys.argv[1])
