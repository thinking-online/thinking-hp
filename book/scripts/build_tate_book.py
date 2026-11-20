# -*- coding: utf-8 -*-
# 本の形のPDFを作る。A5・縦書き・1行40字・1ページ16行（類書と同じ組み方）。表紙から「おわりに」まで。
#   python3 -I scripts/build_tate_book.py max   → build/本の形_マックス版.html と .pdf
#   python3 -I scripts/build_tate_book.py cut   → build/本の形_削った版.html と .pdf
# マックス版：今の文を削らない。改行は最低限（段落にまとめる）。ブロックは、項目の頭・2コマ・3STEP・まとめ。
# 削った版　：07〜45番を「STEPが本文」の形にしたもの（manuscript/本文/v5/）。第1章・前付け・巻末は、マックス版と同じ。
# 文は、1本の長い帯に流して、HTMLの中のスクリプトが16行ごとにページに切る。PDFにするのは scripts/print_tate_book.js。
import html, math, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import assemble_book as Z
import book_data as K
import v4_data as V
import assemble_v4 as B
import v5 as F

ROOT = os.path.dirname(HERE)
MODE = sys.argv[1] if len(sys.argv) > 1 else "max"
NAME = {"max": "本の形_マックス版", "cut": "本の形_削った版", "s35": "本の形_35個の版", "new": "本の形_新しい形", "new35": "本の形_新しい形_35個"}[MODE]
KOMA_ON = "--koma" in sys.argv   # new の時：2コマも入れる
NEW_FORM = MODE in ("new", "new35")   # 新しい形：文字の3STEPと、端的なまとめ
if NEW_FORM and KOMA_ON:
    NAME += "_2コマあり"
if MODE in ("s35", "new35"):   # 35個の版：45個の版のかわりに、scripts/assemble_v6.py のものを使う
    import assemble_v6 as A6
    Z, K, V, B = A6.Z6, A6.K6, A6.V6, A6.B6
N_ALL = getattr(K, "N_ALL", 45)
PART = "07〜%d番" % N_ALL
PARA_MAX = 170
esc = lambda s: html.escape(s, quote=False)

# ---------------------------------------------------------------- 縦書きの字
FW = str.maketrans("0123456789", "０１２３４５６７８９")
FWU = {chr(c): chr(c - 0x41 + 0xFF21) for c in range(0x41, 0x5B)}
FWL = {chr(c): chr(c - 0x61 + 0xFF41) for c in range(0x61, 0x7B)}
SYM = {"%": "％", "+": "＋", "=": "＝", ":": "：", "?": "？", "!": "！", "(": "（", ")": "）", "/": "／", "&": "＆"}
TOK = re.compile(r"https?://[!-~]+|[0-9]+\.[0-9]+|[0-9]+(?:,[0-9]{3})+|[0-9]+|[A-Za-z]+|[%+=:?!()/&]")


def vt(s):
    """縦書き用。2けたの数字と2字の英字は横に並べる。ほかの数字と、短い大文字は全角にする。==…== は網かけ。"""
    s = s.replace("...", "…").replace("==", "\x00")
    def tok(m):
        t = m.group(0)
        if t.startswith("http"):
            return t
        if t.isdigit():
            return "\x01%s\x02" % t if len(t) == 2 else t.translate(FW)
        if "." in t:
            a, b = t.split(".")
            return a.translate(FW) + "・" + b.translate(FW)
        if "," in t:
            return t.replace(",", "，").translate(FW)
        if t.isalpha():
            if len(t) == 1:
                return FWU.get(t) or FWL.get(t) or t
            if len(t) == 2:
                return "\x01%s\x02" % t
            if len(t) <= 4 and t.isupper():
                return "".join(FWU[c] for c in t)
            return t
        return SYM.get(t, t)
    s = esc(TOK.sub(tok, s))
    s = s.replace("\x01", '<span class="tcy">').replace("\x02", "</span>")
    return re.sub("\x00(.+?)\x00", r"<mark>\1</mark>", s).replace("\x00", "")


def cells(s):
    return len(re.sub(r"(?<![0-9])[0-9]{2}(?![0-9])", "0", s.replace("==", "")))


def P(s, cls=""):
    return '<p%s>%s</p>' % ((' class="%s"' % cls) if cls else "", vt(s))


def H(s):
    return "<h3>%s</h3>" % vt(s)


FIX = re.compile(r"^(・|×|○|→|↓|[①-⑨]|[0-9０-９]+[　 .．、])")


def md_vt(md, merge=True, hook=False):
    """mdを、縦書きの帯に並べる要素にする。## は小見出し（2行ぶん）、### は小さい見出し、``` の中は1行ずつ置く。"""
    out, buf, code, first = [], [], False, True
    def flush():
        if buf:
            out.append(P("".join(buf)))
            del buf[:]
    for line in md.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            flush(); code = not code; continue
        if code:
            if s:
                out.append(P(s, "cd"))
            continue
        if not s or s == "---":
            continue
        m = re.match(r"^(#{2,4}) (.+)$", s)
        if m:
            flush()
            if hook and first:
                out.append(P(m.group(2), "hq"))
            elif len(m.group(1)) == 2:
                out.append(H(m.group(2)))
            else:
                out.append("<h4>%s</h4>" % vt(m.group(2)))
            first = False
            continue
        first = False
        if s in ("……", "…"):
            flush(); out.append(P(s, "c")); continue
        if line.startswith("　") or FIX.match(s):
            flush(); out.append(P(s, "cd")); continue
        if s.startswith("「") and s.endswith("」"):
            flush(); out.append(P(s, "c")); continue
        if not merge:
            out.append(P(s, "c")); continue
        if buf and sum(len(x) for x in buf) + len(s) > PARA_MAX:
            flush()
        buf.append(s)
    flush()
    return "".join(out)


# ---------------------------------------------------------------- ブロック
def head(no, pill, title, sub=None):
    n = len(title)
    size = "t25" if n <= 20 else "t22" if n <= 23 else "t19"
    return ('<div class="blk vhead%s"><div class="vlab">%s<span class="pill">%s</span></div><div class="vttl %s">%s</div>%s</div>'
            % (" vhead4" if sub else "", ('<b class="vno">%s</b>' % no) if no else "", vt(pill), size, vt(title),
               ('<div class="vsub"><b>○</b>　%s</div>' % vt(sub)) if sub else ""))


def ill(text):
    return '<div class="ill"><span>絵</span><div>%s</div></div>' % text


def koma_blk(c):
    return ('<div class="blk vkoma"><div class="k x"><span>伸びない人</span>' + ill("") + '<b>%s</b><i>%s</i></div>'
            '<div class="k o"><span>頭のいい人</span>' + ill("") + '<b>%s</b><i>%s</i></div></div>') % tuple(esc(x.strip()) for x in (c[0][0], c[0][1], c[1][0], c[1][1]))


def sheet_blk(ttl, steps, king):
    notes = any(n for _, _, n in steps)
    st = "".join('<div class="st"><div class="lab">STEP <b>0%d</b></div><div class="do">%s</div><div class="say">「%s」</div>%s</div>'
                 % (i, esc(h), esc(v), ('<div class="nt">※%s</div>' % esc(n)) if n else "") for i, (h, v, n) in enumerate(steps, 1))
    return ('<div class="blk vsheet%s"><div class="sbox"><div class="sttl">頭のいい人の<br>『%s』3STEP</div>%s'
            '<div class="king"><span>「できた」の基準</span><p>%s</p></div></div></div>' % (" wide" if notes else "", esc(ttl), st, esc(king)))


def matome_blk(one, lines):
    """まとめ。linesは (種類, 文)。種類は li（3つ）か dk（そのほか）。行の数に合わせて、幅を決める。"""
    cols = math.ceil(cells(one) / 34) + sum(math.ceil((cells(s) + (1 if k == "li" else 0)) / 37) for k, s in lines)
    width = math.ceil((16 + 25 * cols + 12 + 4) / 26) * 26
    return ('<div class="blk vmatome" style="width:%dpx"><div class="mbox"><p class="mlab">まとめ</p>%s%s</div></div>'
            % (width, P(one, "one"), "".join(P(s, k) for k, s in lines)))


def hito_blk(kk):
    if kk not in K.HITOKOTO:
        return ""
    return '<div class="blk vhito"><div class="hbox"><p class="hlab">王様の一言</p>%s</div></div>' % P("「%s」" % K.HITOKOTO[kk], "h1")


def goal_blk(king, toi):
    return ('<div class="blk vgoal"><div class="gbox"><p class="glab">「できた」の基準</p>' + P(king, "g1")
            + P("迷ったら、自分に聞きます。「%s」" % toi, "g2") + "</div></div>")


# ---------------------------------------------------------------- 流し込みの単位
OUT = []


def flow(part, name, hashira, inner, mode="v"):
    cls = "vt" if mode == "v" else "ht"
    OUT.append('<section class="flow" data-part="%s" data-name="%s" data-hashira="%s" data-mode="%s"><div class="measure"><div class="%s">%s</div></div></section>'
               % (part, esc(name), esc(hashira), mode, cls, inner))


def fixed(part, name, hashira, inner, cls=""):
    OUT.append('<div class="page fixed %s" data-part="%s" data-name="%s" data-hashira="%s"><div class="fx">%s</div></div>' % (cls, part, esc(name), esc(hashira), inner))


def split_title(name):
    a, _, b = name.partition("　")
    return (a, b) if b else ("", a)


# ---------------------------------------------------------------- 07〜45番
def item_max(kk):
    it = V.ITEMS[kk]
    ttl, steps, king = B.sheet(kk)
    one, pts, dakara, toi = B.matome(kk)
    lines = [("li", "%s　%s" % ("①②③"[i], p)) for i, p in enumerate(pts)] + [("dk", dakara), ("dk", "迷ったら、自分に聞きます。「%s」" % toi)]
    return (head(kk, "頭のいい人が絶対やらないこと", it["t"]) + md_vt(B.body(kk), hook=True)
            + koma_blk(B.koma(kk)) + sheet_blk(ttl, steps, king) + matome_blk(one, lines) + hito_blk(kk))


def owari_blk(steps, king, one, dakara, toi):
    """新しい終わり方。文字の3STEP（見出し＋3行＋基準）と、端的なまとめ（見出し＋3行）。前に1行ずつ空ける。"""
    st = "".join(P("STEP%02d　%s" % (i, h), "e1") + (P("※" + n, "e3") if n else "") for i, (h, v, n) in enumerate(steps, 1))
    a = '<div class="blk vend">%s%s%s</div>' % (P("今日からできる3STEP", "el"), st, P("「できた」の基準：" + king, "e2"))
    b = '<div class="blk vend"><p class="el">まとめ</p>%s%s%s</div>' % (P(one, "e1"), P(dakara, "e2"), P("迷ったら、自分に聞きます。「%s」" % toi, "e2"))
    return a + b


def item_new(kk):
    """新しい形：項目の頭 → 本文（問い・理由・やり方・つまずく所）→ 文字の3STEP → 端的なまとめ。"""
    it = V.ITEMS[kk]
    ttl, steps, king = B.sheet(kk)
    one, pts, dakara, toi = B.matome(kk)
    return (head(kk, "頭のいい人が絶対やらないこと", it["t"]) + md_vt(B.body(kk), hook=True)
            + (koma_blk(B.koma(kk)) if KOMA_ON else "") + owari_blk(steps, king, one, dakara, toi) + hito_blk(kk))


def item_cut(kk):
    it = V.ITEMS[kk]
    ttl, steps, king = B.sheet(kk)
    toi = B.matome(kk)[3]
    out = [head(kk, "頭のいい人が絶対やらないこと", it["t"], it["o"])]
    def lines_html(lines):
        return "".join(P(s, "cd") if fixed_ else P(s, "c") if (s in ("……", "…") or (s.startswith("「") and s.endswith("」"))) else P(s) for fixed_, s in lines)
    koma_done = kk not in F.PILLAR
    for kind, title, lines in F.parse(kk):
        if kind == "問い":
            out.append(P(lines[0][1], "hq"))
            out.append("".join(P(s, "cd") if f else P(s, "c") if cells(s) <= 20 or (s.startswith("「") and s.endswith("」")) else P(s) for f, s in lines[1:]))
        elif kind.startswith("STEP"):
            if not koma_done:
                out.append(koma_blk(B.koma(kk))); koma_done = True
            i = int(kind[-1])
            h, v, _ = steps[i - 1]
            out.append('<h3 class="sth"><span class="slab">STEP<b>0%d</b></span>%s</h3><p class="ssay">「%s」</p>' % (i, vt(h), vt(v)))
            out.append(lines_html(lines))
        else:
            out.append(H(title) + lines_html(lines))
    out.append(goal_blk(king, toi) + hito_blk(kk))
    return "".join(out)


# ---------------------------------------------------------------- 第1章の項目
def item1(kk, hashira):
    it = Z.ch1_item(kk)
    door = Z.nonempty(it["章最初のページ"])
    q = Z.nonempty(it["質問ページ"])
    fixed("第1章", kk, hashira, '<div class="d1"><p class="d1a">%s</p><p class="d1b">%s</p>%s</div>'
          % (vt(door[0]), vt(door[1]) if len(door) > 1 else "", "".join('<p class="d1c">%s</p>' % vt(l) for l in door[2:])), "door1")
    ttl, steps, king = Z.ch1_sheet(kk, it)
    ls = Z.nonempty(it["まとめ"])
    li = [l for l in ls[1:] if re.match(r"^(・|[①②③]|[123][　 ])", l)]
    lines = [("li", "%s　%s" % ("①②③④⑤"[i], re.sub(r"^(・|[①②③]|[123][　 ]+)", "", l))) for i, l in enumerate(li)] + [("dk", l) for l in ls[1:] if l not in li]
    c = Z.ch1_koma(it)
    inner = (md_vt(Z.body_md(it["導入文"], 0)) + head(kk, q[0] if q else "頭のいい人が絶対やらないこと", q[1].strip("「」") if len(q) > 1 else Z.ch1_name(kk))
             + md_vt(Z.body_md(it["本文"], 0), hook=True) + (koma_blk(c) if c else "") + sheet_blk(ttl, steps, king) + matome_blk(ls[0], lines) + hito_blk(kk))
    flow("第1章", kk, hashira, inner)


# ---------------------------------------------------------------- 目次
def toc_inner():
    L = [head("", "", "目次")]
    for l in ("10秒だけ、付き合ってください", "はじめに　「お前の勉強法、ぜーんぶ、ズレとる。」", "この本の使い方"):
        L.append(P(l, "t0"))
    def cols(kk):
        return "".join(P("コラム　" + c[0], "tc") for c in Z.columns_after(kk))
    def item(kk, t, o):
        return '<p class="ti"><span class="tcy tn">%s</span>　%s<span class="to">　→　%s</span></p>' % (kk, vt(t), vt(o))
    L.append('<p class="tch">%s</p>' % vt("第1章　%s" % K.CH1_TITLE))
    for kk in sorted(K.CH1_MOKUJI):
        nm, t, x, o = K.CH1_MOKUJI[kk]
        L.append(item(kk, t, o) + cols(kk))
    for num, fuda, title, sub, groups in V.CHAPTERS:
        L.append('<p class="tch">%s</p>' % vt("第%d章　【%s】%s" % (num, fuda, title)))
        for name, items in groups:
            if name:
                L.append(P("■ " + name, "tg"))
            for kk in items:
                L.append(item(kk, V.ITEMS[kk]["t"], V.ITEMS[kk]["o"]) + cols(kk))
    L.append('<p class="tch">%s</p>' % vt("巻末"))
    for l in ("%dを、1枚に" % N_ALL, "6つの言葉で、初めての場面を解く", "保護者の方へ", "参考文献"):
        L.append(P(l, "t0"))
    L.append('<p class="tch">%s</p>' % vt("おわりに　笑わなかった人が、1人だけいました"))
    return "".join(L)


def ref_inner(md):
    """参考文献は、英語が多いので、横書きで流す。1行16px。"""
    out = ['<p class="rt">参考文献</p>']
    for l in md.split("\n")[1:]:
        s = l.strip()
        if s.startswith("```"):
            continue
        out.append('<p class="rl">%s</p>' % esc(s) if s else '<p class="rb"></p>')
    return "".join(out)


# ---------------------------------------------------------------- 全体
def build():
    chap, grp = "", ""
    for kind, name, md in Z.sections():
        body = md.split("\n", 1)[1] if "\n" in md else ""
        if kind == "cover":
            fixed("前付け", "扉", "", '<div class="cv"><p class="cv1">%s</p><p class="cv2">%s</p><p class="cv3">（題は、まだ決まっていない）</p></div>' % (vt(K.TITLES[0]), vt(K.AUTHOR)), "cover")
        elif kind == "toc":
            flow("前付け", "目次", "目次", toc_inner())
        elif kind == "text":
            part = "巻末・おわりに" if name.startswith(("巻末", "おわりに")) else "前付け"
            if name == "巻末　参考文献":
                flow(part, name, "参考文献", ref_inner(md), "h")
                continue
            full = md.split("\n", 1)[0][2:].strip()
            a, b = split_title(full)
            merge = name in ("この本の使い方", "巻末　6つの言葉で、初めての場面を解く", "巻末　保護者の方へ")
            flow(part, name, b if a in ("巻末", "") else a, head("", a, b) + md_vt(body, merge=merge))
        elif kind == "door":
            if name == "第1章":
                title, fuda, sub, intro = K.CH1_TITLE, K.CH1_SUB, "", md_vt(Z.to_md(Z.master(K.CH1_INTRO)), hook=True)
                part = "第1章"
            else:
                ch = [c for c in V.CHAPTERS if "第%d章" % c[0] == name][0]
                title, fuda, sub, intro = ch[2], ch[1], ch[3], md_vt(B.read_new("ch%d_導入" % ch[0]), hook=True)
                part = "章の扉と導入"
            chap, grp = "%s　【%s】" % (name, fuda), ""
            fixed(part, name, "", '<div class="dr"><p class="dr1">%s</p><p class="dr2">%s</p><p class="dr3">%s</p>%s</div>'
                  % (vt(name), vt(title), vt("【%s】" % fuda), ('<p class="dr4">%s</p>' % vt(sub)) if sub else ""), "door")
            flow(part, name + "の導入", chap, intro)
        elif kind == "group":
            grp = name
        elif kind == "item1":
            item1(name, chap)
        elif kind == "item":
            cut = MODE == "cut" and os.path.exists(os.path.join(F.DIR, name + ".md"))   # まだ書いていない項目は、マックス版の形で入れる
            flow(PART, name, chap + ("｜" + grp if grp else ""), item_cut(name) if cut else item_new(name) if NEW_FORM else item_max(name))
        elif kind == "column":
            src = [(s, nm) for k, s, nm in K.COLUMNS if (Z.column(s, nm) or ("",))[0] == name][0]
            title, text = Z.column(*src)
            part = "第1章" if chap.startswith("第1章") else "コラム"
            flow(part, "コラム " + title, "コラム", head("", "コラム", title) + md_vt(text, merge="手紙" not in src[1]))


CSS = """
@page{size:148mm 210mm;margin:0}
*{box-sizing:border-box}
html{font-family:"Noto Sans CJK JP","Noto Sans JP",sans-serif;color:#16181d;background:#fff}
body{margin:0;width:504px;position:relative}
.page{width:504px;height:714px;position:relative;background:#fff;overflow:hidden;break-after:page;page-break-after:always}
.win{position:absolute;top:96px;left:44px;width:416px;height:528px;overflow:hidden}
.folio{position:absolute;top:52px;font-size:11px;color:#444;font-family:"Noto Serif CJK JP",serif}
.hashira{position:absolute;top:54px;font-size:8.5px;color:#888;white-space:nowrap}
.page.even .folio{right:44px}.page.even .hashira{right:76px}
.page.odd .folio{left:44px}.page.odd .hashira{left:76px}
.measure{position:absolute;left:-30000px;top:0}
/* 縦書きの帯。1行は幅26px、40字で高さ528px */
.vt{writing-mode:vertical-rl;height:528px;font-family:"Noto Serif CJK JP","Noto Serif JP",serif;font-size:13.2px;line-height:26px;text-align:justify;line-break:strict;color:#16181d}
.vt p{margin:0;text-indent:1em}
.vt p.c,.vt p.hq{text-indent:0}
.vt p.hq{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:14px;color:#15467e}
.vt h3{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:13.6px;line-height:26px;color:#15467e;margin:0 26px 0 0}
.vt h4{font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;font-size:13px;line-height:26px;margin:0;color:#16181d}
.vt p.cd{text-indent:0;padding-top:2em;font-family:"Noto Sans CJK JP",sans-serif;font-size:12.4px;text-align:start}
.vt mark{background:#d5e4f7;color:inherit}
.tcy{text-combine-upright:all}
.spacer{height:528px}
.blk{height:528px}
/* 項目の頭 */
.vhead{width:78px;padding-left:12px}
.vhead4{width:104px}
.vlab{line-height:24px;height:100%;font-family:"Noto Sans CJK JP",sans-serif;font-size:10.5px;font-weight:700;color:#15467e}
.vno{display:inline-block;writing-mode:horizontal-tb;width:24px;height:24px;line-height:24px;text-align:center;background:#15467e;color:#fff;font-size:13px;border-radius:4px;margin-bottom:8px}
.pill{background:#e3ecf7;border-radius:12px;padding:8px 5px}
.pill:empty{display:none}
.vttl{line-height:42px;font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;color:#15467e;letter-spacing:.02em}
.t25{font-size:25px}.t22{font-size:21.5px}.t19{font-size:18.5px}
.vsub{line-height:26px;font-family:"Noto Sans CJK JP",sans-serif;font-size:13px;font-weight:700;text-align:end;color:#16181d}
.vsub b{color:#15467e;font-weight:900}
/* 新しい終わり方（文字の3STEPと、端的なまとめ。前に1行空ける） */
.vend{margin-right:26px}
.vend p{text-indent:0;font-family:"Noto Sans CJK JP",sans-serif;font-size:12.8px}
.vend .el{font-weight:900;font-size:13.6px;color:#15467e}
.vend .e1{font-weight:700}
.vend .e3{font-size:11.6px;padding-top:6em}
/* 絵の枠 */
.ill{border:1.5px dashed #9aa0a8;background:#fff;border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;color:#666;font-size:10px;line-height:1.6}
.ill span{position:absolute;top:4px;left:5px;background:#7a7f87;color:#fff;font-size:8.5px;border-radius:3px;padding:0 6px;line-height:1.6}
/* 2コマ（6行ぶん） */
.vkoma{writing-mode:horizontal-tb;width:156px;padding:0 8px;display:flex;flex-direction:column;gap:8px;font-family:"Noto Sans CJK JP",sans-serif;line-height:1.5;text-align:center}
.vkoma .k{flex:1;border-radius:8px;padding:6px 4px 8px;text-align:center;display:flex;flex-direction:column}
.vkoma .x{background:#eceef2}.vkoma .o{background:#e3ecf7;border:1px solid #15467e}
.vkoma span{font-size:9.5px;color:#555}
.vkoma .ill{flex:1;margin:4px 2px 6px}
.vkoma b{display:block;font-size:14px;font-weight:900}
.vkoma i{display:block;font-style:normal;font-size:9px;white-space:nowrap}
/* 3STEPと基準（7行ぶん。補足がある時は8行ぶん） */
.vsheet{writing-mode:horizontal-tb;width:182px;padding:0 6px;font-family:"Noto Sans CJK JP",sans-serif;text-align:left}
.vsheet.wide{width:208px}
.sbox{height:100%;border:1.5px solid #15467e;border-radius:8px;padding:10px 10px 10px;display:flex;flex-direction:column;justify-content:space-between}
.sttl{font-size:12.5px;font-weight:900;line-height:1.5;border-bottom:2px solid #15467e;padding-bottom:5px}
.st{border-bottom:1px solid #dfe3ea;padding-bottom:8px}
.lab{display:inline-block;background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 10px;line-height:1.7}
.lab b{font-size:11px}
.do{font-size:11.5px;font-weight:700;line-height:1.6;margin:5px 0 5px}
.say{display:inline-block;border:1px solid #15467e;border-radius:8px;padding:1px 6px;font-size:9.5px;line-height:1.7;letter-spacing:-.02em}
.nt{font-size:8.5px;line-height:1.5;color:#444;margin-top:4px}
.king{background:#e3ecf7;border-radius:6px;padding:8px 9px}
.king span{display:inline-block;background:#15467e;color:#fff;border-radius:99px;font-size:9px;font-weight:700;padding:0 9px;line-height:1.8}
.king p{margin:4px 0 0;font-size:11px;font-weight:700;line-height:1.6;text-indent:0}
/* まとめ */
.vmatome{padding-right:4px}
.mbox{height:100%;background:#f1f4f9;border-radius:8px;padding:14px 6px;line-height:25px}
.mbox p{text-indent:0;line-height:25px}
.mbox .mlab{line-height:16px;font-family:"Noto Sans CJK JP",sans-serif;font-size:9.5px;font-weight:700;color:#15467e}
.mbox .one{font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:14px}
.mbox .li{text-indent:1em}
/* 王様の一言（2行ぶん。3STEP・まとめと同じページに入るように、細くした） */
.vhito{width:52px;padding-right:5px}
.hbox{height:100%;border:1.5px solid #16181d;border-radius:8px;padding:12px 3px}
.hbox p{text-indent:0;font-family:"Noto Sans CJK JP",sans-serif}
.hbox .hlab{line-height:13px;font-size:9px;font-weight:700}
.hbox .h1{line-height:25px;font-size:13.4px;font-weight:900}
/* 「できた」の基準と、自分への問い（3行ぶん） */
.vgoal{width:78px;padding-right:6px}
.gbox{height:100%;background:#e3ecf7;border-radius:8px;padding:12px 5px}
.gbox p{text-indent:0;font-family:"Noto Sans CJK JP",sans-serif}
.gbox .glab{line-height:14px;font-size:9.5px;font-weight:700;color:#15467e}
.gbox .g1{line-height:24px;font-size:12.6px;font-weight:900}
.gbox .g2{line-height:24px;font-size:12px}
/* STEPの見出し */
.vt h3.sth{color:#16181d;position:relative;padding-top:31px}
.slab{position:absolute;top:0;left:2px;writing-mode:horizontal-tb;width:22px;height:24px;background:#15467e;color:#fff;border-radius:4px;font-size:6px;line-height:1.1;text-align:center;font-weight:700;padding-top:3px;letter-spacing:0}
.slab b{display:block;font-size:10.5px;line-height:1.1}
.vt p.ssay{text-indent:2.6em;font-family:"Noto Sans CJK JP",sans-serif;font-size:12.4px;color:#15467e}
/* 目次 */
.vt p.t0{text-indent:0;font-size:12.6px}
.vt p.tch{text-indent:0;margin-right:26px;font-family:"Noto Sans CJK JP",sans-serif;font-weight:900;font-size:13.4px;color:#15467e}
.vt p.tg{text-indent:1em;font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;font-size:11.5px;color:#555}
.vt p.ti{text-indent:0;padding-top:1em;font-size:12.6px;text-align:start}
.vt p.ti .tn{font-family:"Noto Sans CJK JP",sans-serif;font-weight:700;color:#15467e}
.vt p.ti .to{font-size:10.8px;color:#444}
.vt p.tc{text-indent:0;padding-top:3em;font-size:11px;color:#a4500a}
/* 決まった形のページ */
.fx{position:absolute;top:96px;left:44px;width:416px;height:528px;writing-mode:vertical-rl;font-family:"Noto Sans CJK JP",sans-serif;display:flex;flex-direction:column;justify-content:center}
.fx p{margin:0}
.cv1{font-size:30px;font-weight:900;line-height:54px;color:#15467e}
.cv2{font-size:15px;font-weight:700;line-height:60px;text-align:end}
.cv3{font-size:10px;color:#888;line-height:30px;text-align:end}
.dr1{font-size:15px;font-weight:700;color:#15467e;line-height:44px;letter-spacing:.2em;padding-top:24px}
.dr2{font-size:23px;font-weight:900;line-height:50px;padding-top:24px}
.dr3{font-size:13px;color:#555;line-height:40px;padding-top:24px}
.dr4{font-size:12px;color:#555;line-height:26px;padding-top:24px}
.d1{padding-top:60px}
.d1a{font-size:14px;font-weight:700;color:#15467e;line-height:40px;letter-spacing:.2em}
.d1b{font-size:54px;font-weight:900;line-height:90px;color:#15467e}
.d1c{font-size:15px;font-weight:700;line-height:34px;padding-top:3em}
/* 参考文献（横書き） */
.ht{width:416px;font-family:"Noto Sans CJK JP",sans-serif;font-size:9.2px;line-height:16px;color:#16181d}
.ht p{margin:0;word-break:break-all}
.ht .rt{font-size:15px;font-weight:900;color:#15467e;line-height:32px;margin-bottom:16px}
.ht .rb{height:16px}
"""

JS = r"""
const COL = 26, R = 16, PW = COL * R, PH = 528;
const rep = { flows: [], warn: [] };
function layoutV(src, name) {
  for (const el of [...src.children]) {
    const e = src.getBoundingClientRect().right, b = el.getBoundingClientRect();
    const start = Math.round(e - b.right), end = Math.round(e - b.left);
    const idx = (start % PW) / COL;
    let push = 0;
    if (el.classList.contains('blk')) {
      const straddle = (x) => { const r0 = src.getBoundingClientRect().right, q = x.getBoundingClientRect(); return Math.floor(Math.round(r0 - q.right) / PW) !== Math.floor((Math.round(r0 - q.left) - 1) / PW); };
      if (straddle(el)) {
        // 2コマは、ページをまたぐ時、うしろの段落のあとへ送ってみる（見出しと、その最初の段落のあいだには置かない）
        let moved = false;
        if (el.classList.contains('vkoma')) {
          const home = el.nextElementSibling;
          let s = home;
          for (let t = 0; t < 10 && s; t++) {
            const nx = s.nextElementSibling;
            const okAfter = s.tagName === 'P' && !s.classList.contains('ssay') && !s.classList.contains('hq') && nx && !nx.classList.contains('blk');
            if (okAfter) { src.insertBefore(el, nx); if (!straddle(el)) { moved = true; break; } }
            s = nx;
          }
          if (!moved) src.insertBefore(el, home);
        }
        if (!moved) { const e2 = src.getBoundingClientRect().right, b2 = el.getBoundingClientRect(), st2 = Math.round(e2 - b2.right); push = (Math.floor(st2 / PW) + 1) * PW - st2; }
      }
    }
    else if (el.tagName === 'H3' || el.tagName === 'H4') {
      const keep = el.classList.contains('sth') ? 2 : 1;
      if (el.tagName === 'H3' && idx === 1) el.style.marginRight = '0';
      else if (idx >= R - keep) push = (R - idx) * COL;
    }
    if (push) { const sp = document.createElement('div'); sp.className = 'spacer'; sp.style.width = push + 'px'; src.insertBefore(sp, el); }
  }
  for (const el of [...src.querySelectorAll(':scope > .blk')]) {
    const r0 = src.getBoundingClientRect().right, q = el.getBoundingClientRect(), st0 = Math.round(r0 - q.right), en0 = Math.round(r0 - q.left);
    if (Math.floor(st0 / PW) !== Math.floor((en0 - 1) / PW)) { const sp = document.createElement('div'); sp.className = 'spacer'; sp.style.width = ((Math.floor(st0 / PW) + 1) * PW - st0) + 'px'; src.insertBefore(sp, el); }
  }
  for (const el of [...src.children]) {
    const st = getComputedStyle(el), w = el.getBoundingClientRect().width + parseFloat(st.marginRight) + parseFloat(st.marginLeft);
    if (Math.abs(w / COL - Math.round(w / COL)) > 0.03) rep.warn.push(name + ' 行の幅がずれている: ' + (el.className || el.tagName) + ' ' + w.toFixed(1) + 'px ' + el.textContent.slice(0, 14));
    if (el.scrollHeight > PH + 1) rep.warn.push(name + ' 下にはみ出し: ' + (el.className || el.tagName) + ' ' + el.textContent.slice(0, 14));
  }
  src.querySelectorAll('.sbox,.vkoma .k,.mbox,.gbox,.hbox,.vhead').forEach((el) => {
    if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) rep.warn.push(name + ' ブロックの中がはみ出し: ' + el.className + ' ' + el.scrollWidth + 'x' + el.scrollHeight + ' / ' + el.clientWidth + 'x' + el.clientHeight + ' ' + el.textContent.slice(0, 12));
  });
  return Math.round(src.getBoundingClientRect().width);
}
function page(sec) {
  const p = document.createElement('div');
  p.className = 'page';
  for (const k of ['part', 'name', 'hashira']) p.dataset[k] = sec.dataset[k];
  p.innerHTML = '<div class="win"></div>';
  return p;
}
function buildFlow(sec) {
  const v = sec.dataset.mode === 'v';
  const src = sec.querySelector(v ? '.vt' : '.ht');
  const total = v ? layoutV(src, sec.dataset.name) : Math.round(src.getBoundingClientRect().height);
  const n = Math.max(1, Math.ceil(total / (v ? PW : PH)));
  const frag = document.createDocumentFragment();
  for (let k = 0; k < n; k++) {
    const p = page(sec), c = src.cloneNode(true);
    c.style.cssText = v ? 'position:absolute;top:0;width:' + total + 'px;right:' + (-k * PW) + 'px' : 'position:absolute;left:0;top:' + (-k * PH) + 'px';
    p.querySelector('.win').appendChild(c);
    frag.appendChild(p);
  }
  rep.flows.push({ part: sec.dataset.part, name: sec.dataset.name, pages: n, rows: v ? total / COL : 0 });
  sec.replaceWith(frag);
}
document.fonts.ready.then(() => {
  document.querySelectorAll('.page.fixed').forEach((p) => rep.flows.push({ part: p.dataset.part, name: p.dataset.name + '（扉）', pages: 1, rows: 0 }));
  document.querySelectorAll('section.flow').forEach(buildFlow);
  document.querySelectorAll('.page').forEach((p, i) => {
    const n = i + 1;
    p.classList.add(n % 2 ? 'odd' : 'even');
    if (!p.classList.contains('fixed')) p.insertAdjacentHTML('beforeend', '<div class="folio">' + n + '</div><div class="hashira">' + (p.dataset.hashira || '') + '</div>');
  });
  rep.total = document.querySelectorAll('.page').length;
  window.__rep = rep;
  document.body.dataset.done = '1';
});
"""


def main():
    build()
    doc = ('<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s<script>%s</script></body></html>'
           % (NAME, CSS, "\n".join(OUT), JS))
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    hp = os.path.join(ROOT, "build", NAME + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(doc)
    if "--html" not in sys.argv:
        subprocess.check_call(["node", os.path.join(HERE, "print_tate_book.js"), NAME] + [a for a in sys.argv[2:] if a.startswith("--")])


if __name__ == "__main__":
    main()
