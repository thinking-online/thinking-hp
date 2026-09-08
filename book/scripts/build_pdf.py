# -*- coding: utf-8 -*-
"""原稿の markdown を、本の体裁の HTML に組んで PDF 化するための HTML を作る。
book/ で実行する。出力は build/台本.html と build/企画書.html。
PDF 化は headless chromium の --print-to-pdf で行う。"""
import os, re, html, sys

M = "manuscript"

CH = {2: (4, 10), 3: (11, 17), 4: (18, 24), 5: (25, 31), 6: (32, 38), 7: (39, 45)}
FORCE_OF_CH = {2: "捨てる力", 3: "突き止める力", 4: "つなげる力",
               5: "取り出す力", 6: "さかのぼる力", 7: "回す力"}
CLASS_OF_FORCE = {"捨てる力": "f1", "突き止める力": "f2", "つなげる力": "f3",
                  "取り出す力": "f4", "さかのぼる力": "f5", "回す力": "f6"}

def esc(s):
    return html.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

FIG_RE = re.compile(r'^（(図|完全版|1ヶ月分|図4).*(挿入|再掲|配置した図).*）$')


FROW_RE = re.compile(r'^(.*?)\u3000{5,}(.*)$')

def as_formrow(l):
    """記入欄の行なら (左, 右) を返す。違えば None。"""
    if "→" in l:
        return None
    m = FROW_RE.match(l)
    if not m:
        return None
    left, right = m.group(1), m.group(2)
    if not left.strip():
        return None
    tail = right.replace("\u3000", " ").strip()
    if len(tail) > 10:
        return None
    return left.replace("\u3000", " ").rstrip(), tail

def md_to_html(text, accent=""):
    """最低限のmarkdown変換。原稿内の改行は意味があるので <br> で保つ。"""
    lines = text.split("\n")
    out = []
    i = 0
    last_h3 = ""
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        # 水平線 = 区切り
        if re.fullmatch(r'-{3,}', line.strip()):
            if out and not out[-1].startswith('<div class="pagebreak"'):
                out.append('<div class="pagebreak"></div>')
            i += 1
            continue
        # 見出し
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            level, txt = len(m.group(1)), m.group(2).strip()
            if level == 2 and txt in ("右ページ", "左ページ"):
                cls = "pagelabel" + (" newpage" if txt == "左ページ" else "")
                label = "右ページ　問い" if txt == "右ページ" else "左ページ　答え"
                out.append(f'<div class="{cls}">{esc(label)}</div>')
                last_h3 = ""
                i += 1
                continue
            if level == 3:
                last_h3 = txt
                key = re.sub(r'\d+$', '', txt)
                LBL = {"Q": "q", "HINT": "hint", "法則": "law", "結論": "concl",
                       "状況文": "situ", "伸びない人の答え": "bad", "伸びる人の答え": "good",
                       "他の場面で": "other", "隅の図": "corner", "分かれ道": "vs"}
                if key in LBL:
                    out.append(f'<div class="lbl lbl-{LBL[key]}">{esc(txt)}</div>')
                    i += 1
                    continue
                out.append(f'<h3>{inline(txt)}</h3>')
                i += 1
                continue
            disp = re.sub(r'\s+\d+ページ$', '', txt) if level == 1 else txt
            out.append(f'<h{level}>{inline(disp)}</h{level}>')
            last_h3 = ""
            i += 1
            continue
        # 表
        if line.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            body = []
            head_cells = None
            for r_i, r in enumerate(rows):
                cells = [c.strip() for c in r.strip("|").split("|")]
                if all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    continue
                if head_cells is None:
                    head_cells = cells
                tag = "th" if r_i == 0 else "td"
                body.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            tcls = ""
            if head_cells and len(head_cells) == 3 and head_cells[1] == "伸びない人" and head_cells[2] == "伸びる人":
                tcls = f' class="vs {accent}"'
            out.append(f'<table{tcls}>' + "".join(body) + '</table>')
            continue
        # 箇条書き
        if re.match(r'^\s*-\s+', line):
            items = []
            while i < n and re.match(r'^\s*-\s+', lines[i]):
                items.append("<li>" + inline(re.sub(r'^\s*-\s+', '', lines[i].rstrip())) + "</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        # 段落（空行までをひとかたまり、改行は <br>）
        buf = []
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4}\s|\||\s*-\s|-{3,}$)', lines[i]):
            buf.append(lines[i].rstrip(" \t\r\n"))
            i += 1
        if not buf:
            i += 1
            continue
        joined = buf
        # 図のプレースホルダ
        if len(joined) == 1 and FIG_RE.match(joined[0].strip()):
            out.append(f'<div class="figbox">{inline(joined[0].strip())}</div>')
            continue
        # 全角スペース始まりの行が主体なら、字下げの塊として整形
        rows = [as_formrow(l) for l in joined]
        if rows and all(r is not None for r in rows):
            body = "".join(
                f'<div class="frow"><span class="fl">{inline(a)}</span>'
                f'<span class="fd"></span><span class="fu">{inline(b)}</span></div>'
                for a, b in rows)
            out.append(f'<div class="frows">{body}</div>')
            continue
        if all(l.startswith("　") for l in joined):
            out.append('<div class="indent">' + "<br>".join(inline(l) for l in joined) + "</div>")
            continue
        cls = ""
        if last_h3 == "Q":
            cls = ' class="qtext"'
        elif last_h3 == "HINT":
            cls = ' class="hintbox"'
        elif last_h3.startswith("法則") and re.fullmatch(r'法則\d+', last_h3):
            cls = f' class="lawbox {accent}"'
        elif last_h3 == "結論":
            cls = ' class="conclbox"'
        elif last_h3 == "状況文":
            cls = ' class="situ"'
        elif last_h3 == "隅の図":
            cls = ' class="cornerfig"'
        elif last_h3 in ("伸びない人の答え", "伸びる人の答え"):
            cls = ' class="ans"'
        elif len(joined) <= 2 and all(re.match(r'^(捨てる力|突き止める力|つなげる力|取り出す力|さかのぼる力|回す力)\s|^場面タグ', l) for l in joined):
            cls = ' class="rubric"'
        out.append(f'<p{cls}>' + "<br>".join(inline(l) for l in joined) + "</p>")
    doc = "\n".join(out)
    # 改ページの直後がさらに改ページ／章見出しなら、白ページになるので落とす
    doc = re.sub(r'(?:<div class="pagebreak"></div>\s*)+(?=<div class="pagebreak"></div>)', '', doc)
    doc = re.sub(r'<div class="pagebreak"></div>\s*(?=<h1)', '', doc)
    doc = re.sub(r'<div class="pagebreak"></div>\s*$', '', doc)
    return doc

CSS = """
@page { size: A5; margin: 13mm 14mm 11mm 14mm; }
@page :first { margin: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "IPAPGothic","IPAGothic",sans-serif; font-size: 9.1pt; line-height: 1.72;
       color: #1c1c1c; margin: 0; }
p { margin: 0 0 0.72em 0; }
code { font-size: 0.9em; color: #666; background: #f2f2f2; padding: 0 .25em; border-radius: 2px; }
hr.rule { border: 0; border-top: 1px solid #ddd; margin: 1.6em 0; }
h1 { font-size: 15.5pt; line-height: 1.45; margin: 0 0 .95em 0; padding-bottom: .5em;
     border-bottom: 2px solid #1c1c1c; page-break-before: always; page-break-after: avoid; }
h2 { font-size: 12.5pt; margin: 2.0em 0 .8em 0; page-break-after: avoid; }
h3 { font-size: 10.4pt; margin: 1.5em 0 .5em 0; color: #444; page-break-after: avoid; }
h4 { font-size: 9.8pt; margin: 1.2em 0 .4em 0; color: #555; page-break-after: avoid; }
ul { margin: 0 0 1em 0; padding-left: 1.2em; }
li { margin-bottom: .35em; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: 1em 0; }
th, td { border: 1px solid #ccc; padding: .38em .5em; text-align: left; vertical-align: top; }
th { background: #f4f4f4; }
.indent { margin: 0 0 1em 0; white-space: pre-wrap; font-size: 9.2pt; line-height: 1.85; }
.vs { font-size: 8.2pt; margin: .28em 0 .85em 0; }
.vs th, .vs td { padding: .3em .5em; line-height: 1.45; }
.vs th:first-child, .vs td:first-child { width: 21%; font-size: 7.8pt; color: #8a8a8a;
                                          background: #fafafa; white-space: nowrap; }
.vs th:nth-child(2), .vs td:nth-child(2) { width: 39.5%; color: #5a5a5a; }
.vs th:nth-child(3), .vs td:nth-child(3) { width: 39.5%; }
.vs th { background: #f2f2f2; color: #444; font-size: 8pt; }
.vs th:nth-child(3) { color: #1c1c1c; }
.vs td:nth-child(3) { background: #f4f4f4; }
.vs.f1 td:nth-child(3), .vs.f1 th:nth-child(3) { background: #eef4fb; }
.vs.f2 td:nth-child(3), .vs.f2 th:nth-child(3) { background: #eef6f1; }
.vs.f3 td:nth-child(3), .vs.f3 th:nth-child(3) { background: #faf4e6; }
.vs.f4 td:nth-child(3), .vs.f4 th:nth-child(3) { background: #fdf0f5; }
.vs.f5 td:nth-child(3), .vs.f5 th:nth-child(3) { background: #fbeeec; }
.vs.f6 td:nth-child(3), .vs.f6 th:nth-child(3) { background: #f5eefa; }
.frows { margin: .6em 0 1.2em 0; }
.frow { display: flex; align-items: baseline; gap: .5em; padding: .42em 0; }
.frow .fl { white-space: nowrap; }
.frow .fd { flex: 1 1 auto; border-bottom: 1px solid #cfcfcf; height: .85em; }
.frow .fu { white-space: nowrap; color: #777; font-size: 8.6pt; }
.figbox { border: 1px dashed #b0b0b0; color: #777; text-align: center; padding: 1.5em .8em;
          margin: 1.1em 0; font-size: 8.6pt; border-radius: 3px; background: #fafafa; }
.pagelabel { font-size: 7.3pt; letter-spacing: .18em; color: #8a8a8a; border-bottom: 1px solid #e2e2e2;
             padding-bottom: .35em; margin: 0 0 1.1em 0; page-break-after: avoid; }
.newpage { page-break-before: always; }
.pagebreak { page-break-before: always; height: 0; }
h1 + .meta + .pagebreak, h1 + .pagebreak { page-break-before: avoid; }
.lbl { font-size: 7.3pt; letter-spacing: .16em; color: #9a9a9a; margin: .72em 0 .22em 0; page-break-after: avoid; }
.qtext { font-size: 12.5pt; line-height: 1.55; margin: 0 0 1em 0; }
.situ { margin: 0 0 1.1em 0; }
.hintbox { background: #f6f6f2; border-left: 3px solid #c9c2a6; padding: .6em .85em; margin: 0 0 .9em 0; font-size: 8.9pt; }
.lawbox { font-size: 11pt; line-height: 1.45; padding: .5em .85em; margin: .1em 0 .75em 0;
          border-left: 4px solid #1c1c1c; background: #f7f7f7; }
.lbl-bad, .lbl-good { color: #6a6a6a; }
.lbl-good { border-left: 3px solid #1c1c1c; padding-left: .5em; margin-left: -.65em; }
.ans { margin: 0 0 .6em 0; }
.cornerfig { font-size: 7.8pt; color: #8a8a8a; line-height: 1.75; border-top: 1px dotted #dcdcdc;
             padding-top: .55em; margin: 0; }
.rubric { font-size: 8pt; color: #8a8a8a; letter-spacing: .04em; line-height: 1.7; margin: 0 0 1.3em 0; }
.conclbox { border-top: 1px solid #ddd; padding-top: .55em; margin: 0 0 .8em 0; }
.lawbox.f1 { border-left-color: #2f6fb0; } .lawbox.f2 { border-left-color: #2e8b57; }
.lawbox.f3 { border-left-color: #a8791b; } .lawbox.f4 { border-left-color: #cc3d78; }
.lawbox.f5 { border-left-color: #c0392b; } .lawbox.f6 { border-left-color: #7b3fa0; }
/* 扉 */
.cover { height: 210mm; width: 148mm; box-sizing: border-box; padding: 42mm 20mm 20mm 20mm;
         page-break-after: always; }
.cover .kicker { font-size: 9pt; color: #777; letter-spacing: .1em; }
.cover .t { font-size: 18.5pt; line-height: 1.6; margin: 1.2em 0 .6em 0; }
.cover .s { font-size: 12pt; color: #333; margin-bottom: 3.5em; }
.cover .obi { font-size: 9.4pt; line-height: 1.9; border-top: 1px solid #ccc; border-bottom: 1px solid #ccc;
              padding: 1em 0; margin-bottom: 3em; }
.cover .au { font-size: 11pt; }
.cover .note { font-size: 8pt; color: #999; margin-top: 3.5em; line-height: 1.8; }
/* 目次 */
.toc { page-break-after: always; }
.toc h1 { page-break-before: avoid; }
.toc .row { display: flex; justify-content: space-between; font-size: 9.4pt; padding: .28em 0;
            border-bottom: 1px dotted #e0e0e0; }
.toc .row .r { color: #999; font-size: 8.6pt; }
.toc .grp { margin-top: 1.4em; font-size: 8pt; letter-spacing: .16em; color: #9a9a9a; }
/* 中扉 */
.part { page-break-before: always; padding-top: 55mm; page-break-after: always; }
.part .num { font-size: 8.4pt; letter-spacing: .22em; color: #999; }
.part .ttl { font-size: 18pt; line-height: 1.55; margin-top: .8em; }
.part .bar { width: 34mm; height: 3px; background: #1c1c1c; margin-top: 1.6em; }
.part.f1 .bar { background: #2f6fb0; } .part.f2 .bar { background: #2e8b57; }
.part.f3 .bar { background: #a8791b; } .part.f4 .bar { background: #cc3d78; }
.part.f5 .bar { background: #c0392b; } .part.f6 .bar { background: #7b3fa0; }
.meta { font-size: 8pt; color: #a0a0a0; border: 1px solid #eee; background: #fbfbfb;
        padding: .5em .7em; margin: 0 0 1.1em 0; line-height: 1.7; }
"""

def read(p):
    return open(os.path.join(M, p), encoding="utf-8").read()

def strip_meta(text):
    """ファイル冒頭の、著者・編集向けの注記ブロックを .meta として切り出す。"""
    lines = text.split("\n")
    # 1行目は # 見出し
    head = lines[0]
    rest = lines[1:]
    j = 0
    while j < len(rest) and not rest[j].strip():
        j += 1
    note = []
    while j < len(rest) and rest[j].strip() and not rest[j].startswith(("#", "---", "|", "-")):
        note.append(rest[j].strip())
        j += 1
    if note and any(k in "".join(note) for k in ("docs/", "仮です", "サンプル原稿", "紙面", "著者の物語", "形式")):
        return head, "\n".join(rest[j:]), "<br>".join(esc(x) for x in note)
    return head, "\n".join(rest), ""

def render_file(path, accent=""):
    raw = read(path)
    head, body, note = strip_meta(raw)
    h = md_to_html(head + "\n\n" + body, accent)
    if note:
        # h1 の直後に meta を差し込む
        h = re.sub(r'(</h1>)', r'\1\n<div class="meta">' + note + '</div>', h, count=1)
    return h


def build_daihon(outpath):
    parts = []
    parts.append(f"""<div class="cover">
<div class="kicker">商業出版　通し台本　（2026年9月8日時点）</div>
<div class="t">「やればやるだけ伸びる」あの子が、<br>勉強中に絶対にやらないこと</div>
<div class="s">マネするだけで伸びる、あの子の勉強法則45</div>
<div class="obi">やっているのに、伸びない。そのあなたへ。<br>
秘密は、才能でも時間でもなく、数え方にある。</div>
<div class="au">朝倉 徹大</div>
<div class="note">この PDF は編集用のプレビューです。実際の紙面は見開き2ページ組で、<br>
右ページに問い、めくった左ページに答えが入ります。<br>
ここでは読み味を確かめるため、問いと答えを別ページに割っています。<br>
図は仕様のみ。角丸の枠は、図が入る位置を示しています。</div>
</div>""")

    # 目次
    toc = ['<div class="toc"><h1>目次</h1>']
    toc.append('<div class="grp">前付</div>')
    for t in ["はじめに", "序章　あなたは、何を数えている？"]:
        toc.append(f'<div class="row"><span>{esc(t)}</span></div>')
    toc.append('<div class="grp">本文</div>')
    ch_titles = {
        1: "第1章　あの子の頭のなかでは、何が起きているのか",
        2: "第2章　あの子には「捨てる力」がある",
        3: "第3章　あの子には「突き止める力」がある",
        4: "第4章　あの子には「つなげる力」がある",
        5: "第5章　あの子には「取り出す力」がある",
        6: "第6章　あの子には「さかのぼる力」がある",
        7: "第7章　あの子には「回す力」がある",
    }
    laws = {}
    for c in range(2, 8):
        a, b = CH[c]
        for nnum in range(a, b + 1):
            first = read(f"法則{nnum}.md").split("\n")[0]
            laws[nnum] = first.replace("# ", "")
    toc.append(f'<div class="row"><span>{esc(ch_titles[1])}</span><span class="r">法則1〜3</span></div>')
    for c in range(2, 8):
        a, b = CH[c]
        toc.append(f'<div class="row"><span>{esc(ch_titles[c])}</span><span class="r">法則{a}〜{b}</span></div>')
    toc.append('<div class="grp">後付</div>')
    for t in ["まとめ　45の法則を、そのままパクる", "この本を読んだ子の、親へ", "付録",
              "おわりに　偏差値42の僕も、時間を数えていた"]:
        toc.append(f'<div class="row"><span>{esc(t)}</span></div>')
    toc.append("</div>")
    parts.append("\n".join(toc))

    parts.append(render_file("はじめに.md"))
    parts.append(render_file("序章.md"))
    parts.append(f'<div class="part"><div class="num">第 1 章</div><div class="ttl">あの子の頭のなかでは、<br>何が起きているのか</div><div class="bar"></div></div>')
    parts.append(render_file("第1章.md"))
    for c in range(2, 8):
        force = FORCE_OF_CH[c]
        cls = CLASS_OF_FORCE[force]
        parts.append(f'<div class="part {cls}"><div class="num">第 {c} 章</div>'
                     f'<div class="ttl">あの子には<br>「{force}」がある</div><div class="bar"></div></div>')
        parts.append(render_file(f"第{c}章_扉.md", cls))
        a, b = CH[c]
        for nnum in range(a, b + 1):
            parts.append(render_file(f"法則{nnum}.md", cls))
    for f in ["まとめ.md", "親へ.md", "付録.md", "おわりに.md"]:
        parts.append(render_file(f))

    doc = f"<!doctype html><html lang='ja'><head><meta charset='utf-8'><title>台本</title><style>{CSS}</style></head><body>\n" \
          + "\n".join(parts) + "\n</body></html>"
    open(outpath, "w", encoding="utf-8").write(doc)
    return outpath


def build_kikakusho(outpath):
    body = open(os.path.join(M, "企画書", "企画書.md"), encoding="utf-8").read()
    send = open(os.path.join(M, "企画書", "送付文.md"), encoding="utf-8").read()
    cover = """<div class="cover">
<div class="kicker">企画書　2026年9月　学研　杉浦さん宛</div>
<div class="t">「やればやるだけ伸びる」あの子が、<br>勉強中に絶対にやらないこと</div>
<div class="s">マネするだけで伸びる、あの子の勉強法則45</div>
<div class="au">朝倉 徹大（受験の王様）</div>
<div class="note">合同会社ARC代表／学部別合格設計塾THINKING運営</div>
</div>"""
    doc = f"<!doctype html><html lang='ja'><head><meta charset='utf-8'><title>企画書</title><style>{CSS}</style></head><body>\n" \
          + cover + md_to_html(body) + md_to_html(send) + "\n</body></html>"
    open(outpath, "w", encoding="utf-8").write(doc)
    return outpath

if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    print(build_daihon("build/台本.html"))
    print(build_kikakusho("build/企画書.html"))
