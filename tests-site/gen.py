#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英単語/熟語テスト 静的ページ生成ツール
各単語帳の *_cloze_all.csv から、問題＋解答を1ページにまとめた印刷対応HTMLを生成する。
URL: /<slug>/1-50/  /<slug>/mix-1-100/  /<slug>/final-1/  と /<slug>/ (索引)
"""
import csv, html, os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "test"  # 出力ベースフォルダ: /test/<slug>/<range>/

BOOKS = {
    "leap":       {"title": "LEAP",            "csv": "leap-test-maker/LEAP_cloze_all.csv",        "label": "見出し語"},
    "tetsubeki":  {"title": "鉄壁",            "csv": "tetsubeki-test-maker/鉄壁_cloze_all.csv",   "label": "見出し"},
    "sistan":     {"title": "システム英単語",  "csv": "sistan-test-maker/sistan_cloze_all.csv",     "label": "見出し語"},
    "target1900": {"title": "ターゲット1900",  "csv": "target1900-test-maker/target1900_cloze_all.csv", "label": "見出し語"},
    "target1000": {"title": "ターゲット英熟語1000", "csv": "target-test-maker/target1000_cloze_all.csv", "label": "熟語"},
    "sokudoku":   {"title": "速読英熟語",      "csv": "sokudoku-test-maker/sokudoku_cloze_all.csv", "label": "熟語"},
}
CIRC = {1: "①", 2: "②", 3: "③", 4: "④"}

CSS = """
:root{--ink:#1a1a1a;--line:#444;--soft:#888;--accent:#0a4d8c}
*{box-sizing:border-box}
html,body{margin:0;padding:0;color:var(--ink);font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",YuGothic,"Noto Sans JP",IPAGothic,Meiryo,sans-serif;line-height:1.6}
.wrap{max-width:820px;margin:0 auto;padding:24px 28px 64px}
.toolbar{position:sticky;top:0;background:#fff;border-bottom:1px solid #eee;padding:10px 0;margin-bottom:18px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.toolbar a,.btn{display:inline-block;border:1px solid var(--accent);color:var(--accent);background:#fff;border-radius:8px;padding:7px 14px;font-size:14px;text-decoration:none;cursor:pointer}
.btn.primary{background:var(--accent);color:#fff}
.toolbar .sp{flex:1}
.head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid var(--ink);padding-bottom:6px}
.head .ttl{font-size:19px;font-weight:700}
.head .name{font-size:14px;color:#333;letter-spacing:1px}
.sub{display:flex;justify-content:space-between;align-items:center;margin:8px 0 4px;font-size:15px;font-weight:700}
.score{font-weight:700;border:1px solid #999;border-radius:6px;padding:3px 12px;font-size:13px}
.inst{font-size:13.5px;color:#333;margin:10px 0 18px;padding:8px 10px;background:#f6f8fa;border-radius:6px}
.q{margin:0 0 16px;padding-bottom:14px;border-bottom:1px dotted #ccc;page-break-inside:avoid}
.q .line{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}
.q .stmt{flex:1}
.q .qn{font-weight:700;margin-right:6px}
.q .ans-label{font-size:11px;color:var(--soft)}
.q .ans-box{width:46px;height:34px;border:1.5px solid #333;border-radius:4px;flex:none;text-align:center}
.choices{display:grid;grid-template-columns:1fr 1fr;gap:2px 26px;margin:7px 0 0 22px;font-size:14.5px}
.choices .c .n{display:inline-block;width:1.4em;color:var(--accent);font-weight:700}
.blank{font-weight:700;letter-spacing:1px}
/* answer section */
.ans-sec{margin-top:8px}
.ans-sec h2{font-size:17px;border-bottom:2px solid var(--ink);padding-bottom:5px;margin:0 0 14px}
.a{margin:0 0 12px;font-size:14px;page-break-inside:avoid}
.a .top{font-weight:700}
.a .top .ok{color:#0a7a3d;margin:0 6px}
.a .top .mean{font-weight:400;color:#333}
.a .en{margin:3px 0 1px;color:#222}
.a .en b{color:#0a7a3d}
.a .ja{color:#555;font-size:13px}
.foot{margin-top:30px;font-size:11px;color:#aaa;text-align:center}
@media print{
  .toolbar{display:none}
  .wrap{max-width:none;padding:0 6mm}
  @page{size:A4;margin:14mm 12mm}
  .ans-sec{page-break-before:always}
  a{color:inherit;text-decoration:none}
}
"""

def esc(s): return html.escape(s, quote=True)

def render_blanked(stmt):
    # 問題文の空所をそのまま (   ) 表示
    return esc(stmt).replace("(     )", '<span class="blank">(&nbsp;&nbsp;&nbsp;&nbsp;)</span>')

def render_filled(stmt, word):
    # 解答用：空所を正解語で埋め、強調
    return esc(stmt).replace("(     )", f"<b>{esc(word)}</b>")

def test_page(book, slug, rng_label, kind_label, rows):
    """rows: list of dict with keys No.,単語/熟語,日本語,問題,選択肢1-4,答え,日本語訳"""
    title = book["title"]
    n = len(rows)
    qs = []
    ans = []
    for i, r in enumerate(rows, 1):
        word = r["word"]; stmt = r["q"]; ansidx = int(r["ans"])
        ch = [r["c1"], r["c2"], r["c3"], r["c4"]]
        choices_html = "".join(
            f'<div class="c"><span class="n">{CIRC[k]}</span>{esc(ch[k-1])}</div>' for k in (1,2,3,4)
        )
        qs.append(f'''<div class="q">
  <div class="line"><div class="stmt"><span class="qn">問{i}</span>{render_blanked(stmt)}</div>
    <div style="text-align:center"><div class="ans-label">解答</div><div class="ans-box"></div></div></div>
  <div class="choices">{choices_html}</div>
</div>''')
        correct = ch[ansidx-1]
        ans.append(f'''<div class="a">
  <div class="top">問{i} <span class="ok">正解 {CIRC[ansidx]} {esc(correct)}</span><span class="mean">― {esc(r["jp"])}</span></div>
  <div class="en">{render_filled(stmt, correct)}</div>
  <div class="ja">{esc(r["tr"])}</div>
</div>''')

    body = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} 単語テスト {esc(rng_label)}</title>
<meta name="robots" content="noindex">
<style>{CSS}</style></head><body>
<div class="wrap">
 <div class="toolbar">
   <a href="../">← {esc(title)}テスト一覧</a>
   <span class="sp"></span>
   <button class="btn primary" onclick="window.print()">印刷 / PDF保存</button>
 </div>
 <div class="head"><div class="ttl">{esc(title)} 単語テスト</div><div class="name">氏名＿＿＿＿＿＿＿＿＿＿</div></div>
 <div class="sub"><div>範囲 {esc(rng_label)}（{esc(kind_label)}）　全{n}問</div><div class="score">得点 ＿＿ / {n}</div></div>
 <div class="inst">次の各英文の空所に入れるのに最も適切なものを ①〜④ から1つ選び，解答欄に番号で答えなさい。</div>
 {''.join(qs)}
 <div class="ans-sec">
   <h2>{esc(title)} 範囲 {esc(rng_label)}　解答</h2>
   {''.join(ans)}
 </div>
 <div class="foot">THINKING 単語テスト ／ thinking-online.com</div>
</div>
</body></html>'''
    out_dir = os.path.join(ROOT, BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)

def load_rows(csv_path):
    rows = []
    with open(os.path.join(ROOT, csv_path), encoding="utf-8") as f:
        rd = csv.reader(f)
        header = next(rd)
        for r in rd:
            if not r or len(r) < 10: continue
            rows.append({"no": int(r[0]), "word": r[1], "jp": r[2], "q": r[3],
                         "c1": r[4], "c2": r[5], "c3": r[6], "c4": r[7], "ans": r[8], "tr": r[9]})
    return rows

def gen_book(slug):
    book = BOOKS[slug]
    rows = load_rows(book["csv"])
    total = len(rows)
    rng = random.Random(hash(slug) & 0xffffffff)
    index_items = {"seq": [], "mix": [], "final": []}

    # Tier1: 連番50語
    seq_idx = 0
    for start in range(0, total, 50):
        chunk = rows[start:start+50]
        seq_idx += 1
        lo, hi = chunk[0]["no"], chunk[-1]["no"]
        s = f"{slug}/{lo}-{hi}"
        test_page(book, s, f"No.{lo}〜{hi}", "連番", chunk)
        index_items["seq"].append((f"{lo}-{hi}", f"No.{lo}〜{hi}", len(chunk)))

    # Tier2: 100語ブロックをシャッフル出題
    for start in range(0, total, 100):
        chunk = rows[start:start+100][:]
        lo, hi = chunk[0]["no"], chunk[-1]["no"]
        shuffled = chunk[:]; rng.shuffle(shuffled)
        s = f"{slug}/mix-{lo}-{hi}"
        test_page(book, s, f"No.{lo}〜{hi}（順不同）", "100語シャッフル", shuffled)
        index_items["mix"].append((f"mix-{lo}-{hi}", f"No.{lo}〜{hi} シャッフル", len(shuffled)))

    # Tier3: 全範囲から50問（3種）
    for v in range(1, 4):
        picks = rng.sample(rows, min(50, total))
        s = f"{slug}/final-{v}"
        test_page(book, s, f"全範囲 総合 第{v}回", "全範囲50問", picks)
        index_items["final"].append((f"final-{v}", f"全範囲 総合テスト 第{v}回", len(picks)))

    write_book_index(slug, book, total, index_items)
    return total, index_items

def write_book_index(slug, book, total, items):
    def links(group):
        return "".join(f'<li><a href="{slug_part}/">{esc(name)}</a> <span class="n">全{cnt}問</span></li>'
                        for slug_part, name, cnt in group) if False else \
               "".join(f'<li><a href="{esc(sp.split("/")[-1] if "/" in sp else sp)}/">{esc(name)}</a> <span class="n">全{cnt}問</span></li>'
                        for sp, name, cnt in group)
    body = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(book["title"])} 単語テスト一覧</title>
<style>{CSS}
.grp{{margin:22px 0}} .grp h2{{font-size:16px;border-left:4px solid var(--accent);padding-left:8px}}
ul{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}}
li{{border:1px solid #e3e3e3;border-radius:8px;padding:10px 12px}}
li a{{font-weight:700;color:var(--accent);text-decoration:none}} li .n{{color:#999;font-size:12px;margin-left:6px}}
</style></head><body><div class="wrap">
<div class="toolbar"><a href="../">← 全テスト</a></div>
<h1 style="font-size:22px">{esc(book["title"])} 単語テスト</h1>
<p style="color:#666;font-size:14px">全{total}{esc(book["label"])}。4択・空所補充。各テストは問題＋解答が1ページに入り、「印刷 / PDF保存」でそのままPDF化できます。</p>
<div class="grp"><h2>① 連番（50語ずつ）</h2><ul>{links(items["seq"])}</ul></div>
<div class="grp"><h2>② 100語シャッフル（定着確認）</h2><ul>{links(items["mix"])}</ul></div>
<div class="grp"><h2>③ 全範囲 総合テスト（50問）</h2><ul>{links(items["final"])}</ul></div>
<div class="foot">THINKING 単語テスト ／ thinking-online.com</div>
</div></body></html>'''
    with open(os.path.join(ROOT, BASE, slug, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)

def write_master_index(done):
    cards = "".join(
        f'<li><a href="{slug}/">{esc(BOOKS[slug]["title"])}</a><span class="n">全{total}・{ntests}テスト</span></li>'
        for slug, (total, ntests) in done.items())
    body = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>THINKING 単語テスト</title><style>{CSS}
ul{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}
li{{border:1px solid #e3e3e3;border-radius:10px;padding:16px}}
li a{{font-weight:700;font-size:18px;color:var(--accent);text-decoration:none}} li .n{{display:block;color:#999;font-size:12px;margin-top:4px}}
</style></head><body><div class="wrap">
<h1 style="font-size:24px">THINKING 単語テスト</h1>
<p style="color:#666;font-size:14px">単語帳ごとに、4択・空所補充テストを「連番50語 → 100語シャッフル → 全範囲総合」の順で用意。各ページの「印刷 / PDF保存」でPDF化できます。</p>
<ul>{cards}</ul>
<div class="foot">THINKING ／ thinking-online.com</div>
</div></body></html>'''
    os.makedirs(os.path.join(ROOT, BASE), exist_ok=True)
    with open(os.path.join(ROOT, BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)

if __name__ == "__main__":
    targets = sys.argv[1:] or list(BOOKS.keys())
    done = {}
    for slug in targets:
        total, items = gen_book(slug)
        ntests = sum(len(v) for v in items.values())
        done[slug] = (total, ntests)
        print(f"{slug}: {total} words -> {ntests} tests")
    write_master_index({s: done[s] for s in BOOKS if s in done})
    print("done")
