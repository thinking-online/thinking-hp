# -*- coding: utf-8 -*-
"""製品版（見本組）のPDFを作る。

台本（build_pdf.py）や読者版（build_tate.py）と違い、これは本そのものの体裁で組む。
　　A5・縦組み・右綴じ。奇数ページが左、偶数ページが右。
　　法則の見開きは、問いが偶数ページ（右）、答えが奇数ページ（左）に来る。
　　足りないときは白ページを入れて、丁合いを合わせる。
　　目次のノンブルは、組んだ結果から拾って入れる。
　　柱とノンブルは、本文を組んだあとに重ね刷りする。

改ページ位置は組んでみないと分からないので、
組む → ページ番号を測る → 白ページと目次を直す → もう一度組む、を繰り返す。
"""
import os, re, sys, subprocess, shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pdf as bp
import build_tate as bt

M = bp.M
OUT = "build/見本組.pdf"
CHROME = "/opt/pw-browsers/chromium"
TITLE = "あの子が、勉強中に絶対にやらないこと"
SUB = "マネするだけで伸びる、あの子の勉強法則45"
AUTHOR = "朝倉 徹大"
PUB = "学研"

CH_TITLE = {
    1: ("考え方", "同じ参考書、同じ3時間。なぜ差がつくのか"),
    2: ("決め方", "何をやらないかを、先に決める"),
    3: ("見つけ方", "「全部わからない」を、1行に絞る"),
    4: ("覚え方", "1つ覚えて、10動かす"),
    5: ("確かめ方", "わかった、を、できる、に変える"),
    6: ("直し方", "間違いを、次の1個に変える"),
    7: ("続け方", "試験の日まで、数を落とさない"),
}
CH_RANGE = bp.CH          # {2:(4,10), ... 7:(39,45)}
ACCENT = {2: "f1", 3: "f2", 4: "f3", 5: "f4", 6: "f5", 7: "f6"}

# ---------------------------------------------------------------- 素材の読み込み

def body_of(path):
    raw = open(os.path.join(M, path), encoding="utf-8").read()
    head, body, _note = bp.strip_meta(raw)
    return head, body

def law_title(n):
    """法則NN の「法則NN」本文（1行）と、力の名前を返す。"""
    raw = open(os.path.join(M, f"法則{n}.md"), encoding="utf-8").read()
    m = re.search(r'^### 法則%d\s*\n\s*\n(.+)$' % n, raw, re.M)
    t = m.group(1).strip() if m else ""
    m2 = re.match(r'^# 法則\d+\s+(\S+)', raw)
    return t, (m2.group(1) if m2 else "")

def yaranai_lines():
    """巻頭のチェックリストから、法則番号ごとの「やらないこと」を拾う。"""
    raw = open(os.path.join(M, "やらない45.md"), encoding="utf-8").read()
    return {int(m.group(1)): m.group(2).strip()
            for m in re.finditer(r'^　\s*(\d+)　□　(.+)$', raw, re.M)}

YARANAI = None


def render_flow(path, accent=""):
    """流し込みの節（前付・章・巻末）。編集用の注記は落とす。"""
    head, body = body_of(path)
    h = bt.md_to_html_v(head + "\n\n" + body, accent)
    # 見出しの直後の改ページは落とす。見出しだけのページができてしまうため
    h = re.sub(r'(<h1>.*?</h1>)\s*<div class="pagebreak"></div>', r'\1', h, flags=re.S)
    return h

def render_law(n, accent):
    """法則1本を、問いページと答えページの2ページに組む。"""
    head, body = body_of(f"法則{n}.md")
    h = bt.md_to_html_v(body, accent)
    h = re.sub(r'<h1>.*?</h1>', '', h, flags=re.S)
    # 隅の図は、作図の指示文ではなく、図が入る場所そのものにする
    # 問いページと答えページで、組みを変える。
    # 問いは大きく余白を取り、答えは情報が多いので詰める。学参ではふつうの作り。
    br = '<div class="pagebreak"></div>'
    if br in h:
        q, a_ = h.split(br, 1)
        h = (f'<div class="qpage">{q}</div>{br}'
             f'<div class="apage">{a_}</div>')
    return h

def render_tobira(c):
    """章扉。1ページ使う扉と、そのあとの問題・答えページ。"""
    tag, title = CH_TITLE[c]
    raw = open(os.path.join(M, f"第{c}章_扉.md"), encoding="utf-8").read()
    tobira, chap_end = bp.split_chapter_end(raw)
    head, body, _ = bp.strip_meta(tobira)
    inner = bt.md_to_html_v(body, ACCENT[c])
    inner = re.sub(r'<h1>.*?</h1>', '', inner, flags=re.S)
    door = (f'<div class="door {ACCENT[c]}">'
            f'<div class="dnum">第{c}章</div>'
            f'<div class="dtag">【{tag}】</div>'
            f'<div class="dttl">{bt.inline_v(title)}</div>'
            f'<div class="dbar"></div></div>')
    end = ""
    if chap_end:
        end = bt.md_to_html_v(chap_end, ACCENT[c])
    return door, inner, end

# ---------------------------------------------------------------- ブロックの組み立て

class Block:
    __slots__ = ("bid", "html", "even", "toc", "level", "run", "numbered")
    def __init__(self, bid, html, even=False, toc=None, level=0, run="", numbered=True):
        self.bid, self.html, self.even = bid, html, even
        self.toc, self.level, self.run, self.numbered = toc, level, run, numbered

def build_blocks():
    B = []
    B.append(Block("cover", '<div class="blankpage"></div>', numbered=False))
    B.append(Block("b1", '<div class="blankpage"></div>', numbered=False))
    B.append(Block("tobira0",
                   f'<div class="htobira"><div class="httl">{TITLE}</div>'
                   f'<div class="hsub">{SUB}</div>'
                   f'<div class="hau">{AUTHOR}</div>'
                   f'<div class="hpub">{PUB}</div></div>', numbered=False))
    B.append(Block("b2", '<div class="blankpage"></div>', numbered=False))
    B.append(Block("toc", "@@TOC@@", numbered=False))

    B.append(Block("yomu", '<div class="front">' + render_flow("読む前に.md") + "</div>",
                   toc=("読む前に　あなたは、サボっていません", 0), run="読む前に"))
    B.append(Block("haji", render_flow("はじめに.md"),
                   toc=("はじめに　毎日5時間やって、伸びない子がいた", 0), run="はじめに"))
    B.append(Block("yara", render_flow("やらない45.md"), even=True,
                   toc=("あの子が、絶対にやらない45のこと", 0), run="やらない45"))
    B.append(Block("jo", render_flow("序章.md"), even=True,
                   toc=("序章　あなたは、何を数えている？", 0), run="序章"))

    tag1, ttl1 = CH_TITLE[1]
    door1 = ('<div class="door f0"><div class="dnum">第1章</div>'
             f'<div class="dtag">【{tag1}】</div>'
             f'<div class="dttl">{bt.inline_v(ttl1)}</div><div class="dbar"></div></div>')
    B.append(Block("ch1door", door1, even=True, numbered=False,
                   toc=(f"第1章【{tag1}】{ttl1}", 0), run=f"第1章　{ttl1}"))
    h1 = render_flow("第1章.md")
    h1 = re.sub(r'<h1>.*?</h1>', '', h1, flags=re.S)
    B.append(Block("ch1", h1, run=f"第1章　{ttl1}"))

    for c in range(2, 8):
        tag, ttl = CH_TITLE[c]
        door, inner, end = render_tobira(c)
        run = f"第{c}章　{ttl}"
        B.append(Block(f"ch{c}door", door, even=True, numbered=False,
                       toc=(f"第{c}章【{tag}】{ttl}", 0), run=run))
        B.append(Block(f"ch{c}q", inner, run=run))
        a, b = CH_RANGE[c]
        for n in range(a, b + 1):
            t, _f = law_title(n)
            B.append(Block(f"law{n}", render_law(n, ACCENT[c]), even=True,
                           toc=(f"{n}　{t}", 1), run=run))
        if end:
            B.append(Block(f"ch{c}end", end, run=run))

    B.append(Block("matome", render_flow("まとめ.md"), even=True,
                   toc=("まとめ　45を1枚にする", 0), run="まとめ"))
    B.append(Block("oya", render_flow("親へ.md"), even=True,
                   toc=("保護者の方へ", 0), run="保護者の方へ"))
    B.append(Block("furoku", render_flow("付録.md"), even=True,
                   toc=("付録　できないノートの作り方", 0), run="付録"))
    B.append(Block("owari", render_flow("おわりに.md"), even=True,
                   toc=("おわりに　1日14時間やって、偏差値42だった", 0), run="おわりに"))
    B.append(Block("okuduke",
                   f'<div class="colophon"><div class="cottl">{TITLE}</div>'
                   f'<div class="cosub">{SUB}</div>'
                   f'<div class="corow">著　者　{AUTHOR}</div>'
                   f'<div class="corow">発行所　{PUB}</div>'
                   f'<div class="conote">これは見本組です。判型・書体・段組・柱とノンブルの位置は、'
                   f'制作側の指定で変わります。図の入る位置だけ、枠で示しています。</div></div>',
                   numbered=False))
    return B

MK = "MK%sZ"

def marker(bid):
    return f'<span class="mk">{MK % bid}</span>'

# ---------------------------------------------------------------- 組む

def assemble(blocks, blanks, pages):
    parts = []
    for b in blocks:
        for _ in range(blanks.get(b.bid, 0)):
            # 白は、それ自体を1ページ分のセクションにする。
            # 直前の改ページと合体して消えてしまうため。
            parts.append('<section class="blk"><div class="blankpage"></div></section>')
        html = b.html
        if html == "@@TOC@@":
            html = make_toc(blocks, pages)
        cls = "blk" + (" first" if b is blocks[0] else "")
        parts.append(f'<section class="{cls}">{marker(b.bid)}{html}</section>')
    return ("<!doctype html><html lang='ja'><head><meta charset='utf-8'>"
            f"<title>{TITLE}</title><style>{CSS}</style></head><body>\n"
            + "\n".join(parts) + "\n</body></html>")

def make_toc(blocks, pages):
    """目次。法則は2段にする。
    上が「あの子がやらないこと」、下が「かわりにやっていること」。
    表紙の約束を、目次で45回くり返すことになる。"""
    rows = ['<div class="toc"><div class="tocttl">目次</div>',
            '<div class="tocnote">上が、あの子が絶対にやらないこと。<br>'
            '下が、かわりにやっていることです。</div>']
    for b in blocks:
        if not b.toc:
            continue
        label, lv = b.toc
        p = pages.get(b.bid)
        num = bt.inline_v(str(p)) if p else "　"
        if lv == 0:
            rows.append(f'<div class="trow"><span class="tl">{bt.inline_v(label)}</span>'
                        f'<span class="td"></span><span class="tp">{num}</span></div>')
            continue
        n = int(b.bid[3:])
        no = bt.inline_v(f"{n:02d}")
        rows.append(f'<div class="trow sub"><span class="tl">'
                    f'<span class="tn">{no}</span>{bt.inline_v(YARANAI.get(n, ""))}</span>'
                    f'<span class="td"></span><span class="tp">{num}</span></div>'
                    f'<div class="tsub">→　{bt.inline_v(label.split("　", 1)[-1])}</div>')
    rows.append("</div>")
    return "".join(rows)

def render(html_path, pdf_path, html):
    open(html_path, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
                    "file://" + os.path.abspath(html_path)],
                   check=True, capture_output=True)

def page_map(pdf_path, blocks):
    txt = subprocess.run(["pdftotext", pdf_path, "-"], check=True,
                         capture_output=True).stdout.decode("utf-8", "replace")
    pages = txt.split("\f")[:-1]
    flat = ["".join(p.split()) for p in pages]
    found = {}
    for b in blocks:
        m = "".join((MK % b.bid).split())
        for i, f in enumerate(flat, 1):
            if m in f or m[::-1] in f:
                found[b.bid] = i
                break
    return found, len(pages)

def solve(blocks, rounds=6):
    """組んで、各ブロックが何ページ使うかを測り、白ページの入れどころを決める。

    白を1枚入れると、そのあとのページ番号が全部1つずれる。
    だから位置を直接いじらず、まず各ブロックの厚み（ページ数）を測って、
    先頭から順に積み上げて配置を決める。厚みが動かなくなったら終わり。
    """
    blanks, pages, lens, total = {}, {}, None, 0
    for _ in range(rounds):
        html = assemble(blocks, blanks, pages)
        render("build/見本組.html", "build/_work.pdf", html)
        found, total = page_map("build/_work.pdf", blocks)
        if len(found) != len(blocks):
            miss = [b.bid for b in blocks if b.bid not in found]
            raise SystemExit("目印が見つからないブロック: " + ", ".join(miss))
        order = [found[b.bid] for b in blocks] + [total + 1]
        newlens = {b.bid: order[i + 1] - order[i] - blanks.get(blocks[i + 1].bid, 0)
                   for i, b in enumerate(blocks) if i + 1 < len(blocks)}
        newlens[blocks[-1].bid] = total + 1 - order[-2]
        # 積み上げて、偶数ページ始まりにするための白を決める
        nb, np_, cur = {}, {}, 1
        for b in blocks:
            if b.even and cur % 2:
                nb[b.bid] = 1
                cur += 1
            np_[b.bid] = cur
            cur += newlens[b.bid]
        if newlens == lens and nb == blanks:
            return nb, np_, cur - 1
        lens, blanks, pages = newlens, nb, np_
    return blanks, pages, total

# ---------------------------------------------------------------- 柱とノンブル

def cover_pdf():
    """カバー（表1）。天地左右いっぱいに組むので、余白ゼロの別ファイルで作る。"""
    html = ("<!doctype html><html lang='ja'><head><meta charset='utf-8'><style>"
            "@page{size:148mm 210mm;margin:0;}"
            "body{margin:0;font-family:'Noto Sans CJK JP',sans-serif;}"
            ".cv{box-sizing:border-box;width:148mm;height:210mm;background:#14161a;"
            "color:#f2f0ea;padding:36mm 16mm 20mm 16mm;}"
            ".t{font-size:21.5pt;font-weight:700;line-height:1.55;}"
            ".s{font-size:10.5pt;color:#b9b4a6;margin-top:2.4em;line-height:1.85;}"
            ".o{margin-top:26mm;font-size:9.6pt;line-height:2.1;color:#14161a;"
            "background:#d9d3c4;padding:7mm 6mm;}"
            ".a{margin-top:15mm;font-size:12pt;letter-spacing:.14em;}"
            ".p{position:absolute;bottom:18mm;left:16mm;font-size:9pt;"
            "letter-spacing:.2em;color:#8d887c;}"
            "</style></head><body><div class='cv'>"
            f"<div class='t'>{TITLE.replace('、', '、<br>')}</div>"
            f"<div class='s'>{SUB}</div>"
            "<div class='o'>やっているのに、伸びない。<br>"
            "あの子は、やればやるだけ伸びる。<br>"
            "違いは、昨日、何個できるようになったか。</div>"
            f"<div class='a'>{AUTHOR}</div>"
            f"<div class='p'>{PUB}</div>"
            "</div></body></html>")
    render("build/_cover.html", "build/_cover.pdf", html)
    return "build/_cover.pdf"


def stamp(pdf_path, blocks, blanks, found, total, out):
    import pypdf
    # ページごとの柱を決める
    order = []
    for b in blocks:
        order.append((found.get(b.bid, 10**9), b))
    order.sort(key=lambda x: x[0])
    run_of, num_of = {}, {}
    for idx, (p, b) in enumerate(order):
        end = order[idx + 1][0] - 1 if idx + 1 < len(order) else total
        for q in range(p, end + 1):
            run_of[q] = b.run
            num_of[q] = b.numbered
    # 白ページには入れない
    txt = subprocess.run(["pdftotext", pdf_path, "-"], check=True,
                         capture_output=True).stdout.decode("utf-8", "replace")
    strip = lambda t: re.sub(r'[A-Za-z0-9]', '', t)
    empty = {i for i, p in enumerate(txt.split("\f")[:-1], 1) if not strip(p).strip()}

    cells = []
    for q in range(1, total + 1):
        if q in empty or not num_of.get(q, False):
            cells.append('<div class="op"></div>')
            continue
        side = "r" if q % 2 == 0 else "l"
        run = run_of.get(q, "") if q % 2 == 0 else TITLE
        cells.append(f'<div class="op"><div class="foot {side}">'
                     f'<span class="pn">{q}</span>'
                     f'<span class="hd">{bp.esc(run)}</span></div></div>')
    ohtml = ("<!doctype html><html><head><meta charset='utf-8'><style>"
             "@page{size:148mm 210mm;margin:0;}"
             "body{margin:0;font-family:'Noto Sans CJK JP',sans-serif;}"
             ".op{width:148mm;height:210mm;position:relative;page-break-after:always;}"
             ".foot{position:absolute;bottom:11mm;font-size:7.4pt;color:#8c8c8c;"
             "display:flex;gap:1.4em;align-items:baseline;}"
             ".foot.r{right:17mm;flex-direction:row-reverse;}"
             ".foot.l{left:17mm;}"
             ".pn{font-size:8.6pt;color:#4a4a4a;letter-spacing:.04em;}"
             ".hd{white-space:nowrap;}"
             "</style></head><body>" + "".join(cells) + "</body></html>")
    render("build/_overlay.html", "build/_overlay.pdf", ohtml)

    base = pypdf.PdfReader(pdf_path)
    over = pypdf.PdfReader("build/_overlay.pdf")
    cov = pypdf.PdfReader(cover_pdf())
    w = pypdf.PdfWriter()
    for i, pg in enumerate(base.pages):
        if i == 0:
            pg.merge_page(cov.pages[0])
        if i < len(over.pages):
            pg.merge_page(over.pages[i])
        w.add_page(pg)
    with open(out, "wb") as fh:
        w.write(fh)

CSS = ""   # 下で差し込む

def main():
    global CSS
    CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "book.css"), encoding="utf-8").read()
    os.makedirs("build", exist_ok=True)
    bp.HR_AS_PAGEBREAK = False
    bp.inline = bt.inline_v
    global YARANAI
    YARANAI = yaranai_lines()
    blocks = build_blocks()
    blanks, pages, total = solve(blocks)
    real, rtotal = page_map("build/_work.pdf", blocks)
    stamp("build/_work.pdf", blocks, blanks, real, rtotal, OUT)
    print(f"{OUT}　{rtotal}ページ")
    odd = [b.bid for b in blocks if b.even and real.get(b.bid, 1) % 2]
    print("　偶数ページに置けなかったもの:", odd or "なし")
    mism = [b.bid for b in blocks if real.get(b.bid) != pages.get(b.bid)]
    print("　目次のノンブルがずれたもの:", mism or "なし")
    ids = [b.bid for b in blocks]
    starts = [real[i] for i in ids] + [rtotal + 1]
    span = {ids[i]: starts[i + 1] - starts[i] for i in range(len(ids))}
    spill = [(k, v) for k, v in span.items() if k.startswith("law") and v != 2]
    print("　2ページに収まらない法則:", spill or "なし")
    door = [(k, v) for k, v in span.items() if k.endswith("door") and v != 1]
    print("　1ページに収まらない章扉:", door or "なし")
    if odd or spill or door or mism:
        raise SystemExit("見本組が組み上がっていない。上の行を直すこと。")
    return real, rtotal

if __name__ == "__main__":
    main()
