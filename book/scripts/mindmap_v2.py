# -*- coding: utf-8 -*-
"""原稿_v2 を、マインドマップの道具に読みこめる形にする。book/ で実行。
　build/マインドマップ_原稿.opml　　多くのマインドマップ・アウトライナーで読める
　build/マインドマップ_原稿.mm　　　FreeMind形式（MindMeister、XMind などで読める）
　build/マインドマップ_原稿.md　　　見出しと箇条書き（Markdownを読める道具用）
　build/マインドマップ_原稿.html　　ブラウザで開いて、たたんだり開いたりして見る用
中身は「構成」だけ。本文は入れない（本文は Googleドキュメント版で直す）。"""
import io, re, html, sys
sys.path.insert(0, "scripts")

SRC = "manuscript/原稿_v2_マーカー.md"
s = io.open(SRC, encoding="utf-8").read().split("\n---\n", 1)[1].replace("==", "")
FIXED = {"頭のなか", "やり方", "これをやると、何が残るか", "この場面のまとめ", "この法則のまとめ", "残るもの", "まとめ"}

def nchar(t):
    t = re.sub(r'^#{1,6}\s*', '', t, flags=re.M)
    return len(re.sub(r'\s', '', t))

def N(text, kids=None, fold=False):
    return {"t": text, "k": kids or [], "fold": fold}

def uni(body):
    u = []
    for m in re.finditer(r'([一-龥ァ-ヶー・]{2,}大学)', body):
        w = m.group(1)
        if w in ("早稲田大学", "名門大学") or w.endswith("の大学"):
            continue
        if w not in u:
            u.append(w)
    if "ミュンヘンの大学" in body:
        u.append("ミュンヘンの大学")
    if not u and re.search(r'実験です|実験があります|研究で|研究があります|確かめられています', body):
        u.append("研究あり（大学名は書いていない）")
    return u

def item_node(no, title, body):
    kids = []
    mx = re.search(r'^　　×「(.+)」\s*$', body, flags=re.M)
    mo = re.search(r'^　　○「(.+)」\s*$', body, flags=re.M)
    if mx: kids.append(N("× " + mx.group(1)))
    if mo: kids.append(N("○ " + mo.group(1)))
    ml = re.search(r'^　　(?:もとにある)?絶対法則[　 ]+(.+?)\s*$', body, flags=re.M)
    if ml: kids.append(N("絶対法則　" + re.sub(r'[　 ]+', ' ', ml.group(1))))
    heads = [h for h in re.findall(r'^## (.+)$', body, flags=re.M) if h not in FIXED]
    if heads: kids.append(N("話の流れ", [N(h) for h in heads], fold=True))
    steps = re.findall(r'^### (STEP 0[123])　(.+)$', body, flags=re.M)
    kj = re.search(r'^　　「できた」の基準　+(.+)$', body, flags=re.M)
    sk = [N("%s　%s" % (a, b)) for a, b in steps]
    if kj: sk.append(N("「できた」の基準　" + kj.group(1)))
    if sk: kids.append(N("やり方", sk))
    mt = re.search(r'^今日やること　*(.+)$', body, flags=re.M)
    if mt: kids.append(N("今日やること　" + mt.group(1)))
    u = uni(body)
    if u: kids.append(N("研究　" + "／".join(u)))
    kids.append(N("（%s字）" % format(nchar(body), ",")))
    return N("%s　%s" % (no, title), kids, fold=True)

secs = re.split(r'^# (.+)$', s, flags=re.M)
root = N("頭のいい人が絶対にやらないこと　原稿（8章・50本）")
front = N("前付")
back = N("巻末・おわりに")
cur_ch = None
for i in range(1, len(secs), 2):
    name, blob = secs[i].strip(), secs[i + 1]
    parts = re.split(r'^## (\d{2})　(.+)$', blob, flags=re.M)
    if len(parts) > 1:                                   # 章
        sub = re.search(r'^〔(.+?)〕', parts[0], flags=re.M)
        ch = N("%s　〔%s・%d本・%s字〕" % (name, sub.group(1) if sub else "", (len(parts) - 1) // 3, format(nchar(blob), ",")))
        for j in range(1, len(parts), 3):
            ch["k"].append(item_node(parts[j], parts[j + 1].strip(), parts[j + 2]))
        root["k"].append(ch); cur_ch = ch
        continue
    heads = re.findall(r'^## (.+)$', blob, flags=re.M)
    node = N("%s　（%s字）" % (name, format(nchar(blob), ",")), [N(h) for h in heads], fold=True)
    if name.startswith("コラム") or name.startswith("絶対法則は、ここまで"):
        (cur_ch or root)["k"].append(node)
    elif name.startswith(("巻末", "おわりに")):
        back["k"].append(node)
    else:
        front["k"].append(node)
root["k"].insert(0, front)
root["k"].append(back)

# 最後の調整リスト（決まっていないこと）
root["k"].append(N("最後の調整リスト", [
    N("章タイトルの差し替え（案は出してある。まだ反映していない）", [
        N("第1章　勉強の「当たり前」をやらない"),
        N("第2章　授業も宿題も「こなさ」ない"),
        N("第3章　「覚えよう」としない（いまのまま）"),
        N("第4章　「できた」を信じない"),
        N("第5章　「明日の自分」に期待しない"),
        N("第6章　自分の「意志」をあてにしない"),
        N("第7章　不安の言うとおりに動かない"),
        N("第8章　丸投げも、抱えこみもしない"),
    ], fold=True),
    N("事実の確認", [
        N("勉強時間　13時間以上か、14時間か"),
        N("教え始めた時期　大学1年で独立か、大学2年からか"),
        N("はじめにの恩師と、おわりにの恩師は、同じ人か"),
    ], fold=True),
    N("著者が書くもの", [
        N("実話10本"),
        N("コラム10本を、自分の言葉で上書き"),
        N("コラム「勉強の時給は○○円？」"),
        N("コラム　高校時代の話"),
        N("終章の5教科を入れるかどうか"),
    ], fold=True),
    N("研究の最終確認（大学名と言い方）", [N("docs/48 と docs/51 に一覧"), N("36番「戻るのに23分」の言い方")], fold=True),
    N("長さ　四六判で約350ページ。目標は280ページ"),
    N("本のタイトル・帯"),
]))

def count(n):
    return 1 + sum(count(k) for k in n["k"])

# ---- Markdown ----
def md(n, d=0, out=None):
    out = [] if out is None else out
    if d < 3:
        out.append("#" * (d + 1) + " " + n["t"]); out.append("")
    else:
        out.append("  " * (d - 3) + "- " + n["t"])
    for k in n["k"]:
        md(k, d + 1, out)
    if d == 2: out.append("")
    return out
io.open("build/マインドマップ_原稿.md", "w", encoding="utf-8").write("\n".join(md(root)) + "\n")

# ---- OPML ----
def opml(n, d=1):
    a = html.escape(n["t"], quote=True)
    pad = "  " * d
    if not n["k"]:
        return ['%s<outline text="%s"/>' % (pad, a)]
    o = ['%s<outline text="%s">' % (pad, a)]
    for k in n["k"]:
        o += opml(k, d + 1)
    o.append('%s</outline>' % pad)
    return o
io.open("build/マインドマップ_原稿.opml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<opml version="2.0">\n<head><title>%s</title></head>\n<body>\n%s\n</body>\n</opml>\n'
    % (html.escape(root["t"]), "\n".join(opml(root))))

# ---- FreeMind .mm ----
def mm(n, d=1):
    a = html.escape(n["t"], quote=True)
    pad = "  " * d
    f = ' FOLDED="true"' if (n["fold"] and n["k"]) else ""
    if not n["k"]:
        return ['%s<node TEXT="%s"/>' % (pad, a)]
    o = ['%s<node TEXT="%s"%s>' % (pad, a, f)]
    for k in n["k"]:
        o += mm(k, d + 1)
    o.append('%s</node>' % pad)
    return o
io.open("build/マインドマップ_原稿.mm", "w", encoding="utf-8").write(
    '<map version="1.0.1">\n%s\n</map>\n' % "\n".join(mm(root)))

# ---- HTML（たたんで見る用。外のファイルは読みこまない） ----
def ht(n, d=0):
    t = html.escape(n["t"])
    cls = "x" if n["t"].startswith("× ") else "o" if n["t"].startswith("○ ") else \
          "kj" if n["t"].startswith("「できた」の基準") else "st" if n["t"].startswith("STEP") else ""
    if not n["k"]:
        return '<div class="leaf %s">%s</div>' % (cls, t)
    op = "" if (n["fold"] or d >= 2) else " open"
    return '<details%s><summary class="d%d">%s</summary><div class="kids">%s</div></details>' % (
        op, min(d, 3), t, "".join(ht(k, d + 1) for k in n["k"]))
CSS = """
body{font-family:"Hiragino Sans","Noto Sans JP","Yu Gothic",sans-serif;font-size:14px;line-height:1.75;color:#111;
  max-width:980px;margin:24px auto;padding:0 16px;background:#fff}
h1{font-size:18px;color:#15467E;margin:0 0 4px} p.n{color:#666;font-size:12px;margin:0 0 14px}
button{font:inherit;font-size:12px;margin:0 6px 14px 0;padding:3px 10px;border:1px solid #15467E;background:#fff;color:#15467E;border-radius:3px;cursor:pointer}
details{margin:1px 0} summary{cursor:pointer;padding:2px 4px;border-radius:3px} summary:hover{background:#f1f4f8}
.kids{margin-left:20px;border-left:1px solid #d9dee6;padding-left:10px}
.d0{font-weight:700;font-size:16px;color:#15467E} .d1{font-weight:700;color:#15467E;margin-top:6px} .d2{font-weight:700}
.leaf{padding:1px 4px 1px 18px} .x{color:#666} .o{color:#15467E;font-weight:700} .st{font-weight:600}
.kj{color:#15467E;font-weight:700;background:#eef2f7;border-radius:3px}
"""
JS = """
function all(o){document.querySelectorAll('details').forEach(function(d){d.open=o});}
function lv(n){document.querySelectorAll('details').forEach(function(d){
  var k=0,p=d.parentElement;while(p){if(p.tagName==='DETAILS')k++;p=p.parentElement;}d.open=(k<n);});}
"""
page = ('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>原稿の構成</title><style>%s</style></head><body><h1>原稿の構成</h1>'
        '<p class="n">章 → 項目 → ×／○・話の流れ・STEP・基準。クリックで開閉。本文は入っていません。</p>'
        '<button onclick="lv(1)">章まで</button><button onclick="lv(2)">項目まで</button>'
        '<button onclick="lv(3)">項目の中まで</button><button onclick="all(true)">全部開く</button>'
        '%s<script>%s</script></body></html>') % (CSS, ht(root), JS)
io.open("build/マインドマップ_原稿.html", "w", encoding="utf-8").write(page)
print("ノード", count(root), "→ build/マインドマップ_原稿.{opml,mm,md,html}")
