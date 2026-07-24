#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""30日1000単語暗記法 — スパイラル型 確認スケジュールを生成（CSV＋印刷用PDF用HTML）。
1000語を 50語×20ブロック に分割。
Phase1(Day1-20): 毎日 新規1ブロック(50語) ＋ 復習(1日後/3日後/7日後のブロック)。
Phase2(Day21-30): 全ブロックを総復習(1日2ブロック)＋総合テスト。Day30は全1000の総合。
"""
import csv, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
def esc(s): return html.escape(str(s), quote=True)
def rng(b): return f"{(b-1)*50+1}–{b*50}"   # ブロック番号→No範囲

rows = []  # (day, phase, new, review, test)
# Phase 1
for d in range(1, 21):
    new = rng(d)
    revs = [b for b in (d-1, d-3, d-7) if b >= 1]
    rev = "・".join(rng(b) for b in revs) if revs else "—"
    test = f"確認① {new}" + ("　確認② " + "・".join(rng(b) for b in revs) if revs else "")
    rows.append((d, "INPUT", new, rev, test))
# Phase 2  (総復習: 1日2ブロック)
for i, d in enumerate(range(21, 31)):
    b1, b2 = 2*i+1, 2*i+2
    rev = f"{rng(b1)}・{rng(b2)}"
    if d < 30:
        test = f"シャッフル {rng(b1)}／{rng(b2)}"
        new = "—（総復習）"
    else:
        rev = "全1000語"
        new = "—（仕上げ）"
        test = "総合テスト（全範囲・50問×複数）"
    rows.append((d, "REVIEW", new, rev, test))

# CSV
with open(os.path.join(ROOT, "plan30_schedule.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["日", "フェーズ", "新規(50語)", "復習", "確認テスト"])
    for r in rows: w.writerow(r)

# ---------- PDF用HTML ----------
CSS = """
:root{--navy:#16233f;--navy2:#22345c;--ink:#1c2331;--sub:#5b6373;--gold:#c79a3b;--gold-d:#a97f26;
--line:#e6e2d6;--tint:#faf8f2;--tint2:#f2f5fb;}
*{box-sizing:border-box}
html,body{margin:0;color:var(--ink);font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",YuGothic,"Noto Sans JP",IPAGothic,Meiryo,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.en{font-family:Georgia,serif}
.page{width:210mm;height:297mm;overflow:hidden;padding:14mm 14mm;position:relative;background:#fff}
.page+.page{page-break-before:always}
@page{size:A4;margin:0}
/* cover/method */
.hero{background:linear-gradient(160deg,#16233f,#22345c 60%,#2c4374);color:#fff;border-radius:16px;padding:26px 30px;margin-bottom:16px}
.hero .k{letter-spacing:.42em;font-size:11px;color:var(--gold);font-weight:700}
.hero h1{font-size:34px;margin:8px 0 6px;font-weight:800}
.hero h1 .a{color:#f2d492}
.hero p{font-size:12.5px;color:#dbe1ee;line-height:1.85;margin:6px 0 0;max-width:165mm}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0 6px}
.card{border:1px solid var(--line);border-radius:12px;padding:12px 14px;background:var(--tint)}
.card .n{font-family:Georgia,serif;font-size:22px;font-weight:800;color:var(--navy)}
.card .t{font-size:11px;color:var(--sub);margin-top:2px;font-weight:700}
.card .d{font-size:10.5px;color:var(--sub);margin-top:4px;line-height:1.6}
h2.sec{font-size:15px;color:var(--navy);border-left:5px solid var(--gold);padding-left:9px;margin:14px 0 8px}
.flow{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:6px}
.step{border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.step .s{font-family:Georgia,serif;color:var(--gold-d);font-weight:800;font-size:13px}
.step .h{font-weight:800;font-size:12.5px;margin:2px 0}
.step .b{font-size:10.5px;color:var(--sub);line-height:1.6}
.note{font-size:10.5px;color:var(--sub);line-height:1.7;background:var(--tint2);border-radius:8px;padding:8px 10px;margin-top:6px}
/* table */
.thead{font-size:15px;color:var(--navy);font-weight:800;margin:0 0 8px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid var(--navy);padding-bottom:6px}
.thead .ph{font-size:11px;color:#fff;background:var(--navy);border-radius:14px;padding:3px 12px}
table{width:100%;border-collapse:collapse;font-size:11px}
th{background:var(--navy);color:#fff;font-weight:700;font-size:10.5px;padding:6px 8px;text-align:left}
td{padding:5.5px 8px;border-bottom:1px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:var(--tint)}
.day{font-family:Georgia,serif;font-weight:800;color:var(--navy);white-space:nowrap}
.new{font-family:Georgia,serif;font-weight:700;color:var(--ink)}
.rev{color:var(--sub)}
.tst{color:#0a4d8c;font-size:10.5px}
.chk{width:12px;height:12px;border:1.4px solid #9aa1b0;border-radius:3px;display:inline-block}
.foot{position:absolute;left:14mm;right:14mm;bottom:8mm;display:flex;justify-content:space-between;font-size:10px;color:#b3b8c2;border-top:1px solid var(--line);padding-top:5px}
.foot .b{letter-spacing:.28em;font-weight:700;color:#9aa1b0}
"""

def table_html(sub, title, ph, part):
    trs = ""
    for d, phase, new, rev, test in part:
        trs += (f'<tr><td class="day">Day {d:02d}</td>'
                f'<td class="new en">{esc(new)}</td>'
                f'<td class="rev">{esc(rev)}</td>'
                f'<td class="tst">{esc(test)}</td>'
                f'<td style="text-align:center"><span class="chk"></span></td></tr>')
    return f'''<div class="page">
 <div class="thead"><span>30日1000単語暗記法　{esc(title)}</span><span class="ph">{esc(ph)}</span></div>
 <p style="font-size:11px;color:#5b6373;margin:0 0 8px">{esc(sub)}</p>
 <table><thead><tr><th style="width:64px">日</th><th style="width:88px">新規(50語)</th><th>復習</th><th style="width:210px">確認テスト</th><th style="width:34px">済</th></tr></thead>
 <tbody>{trs}</tbody></table>
 <div class="foot"><span class="b">THINKING</span><span>30日1000単語暗記法 &nbsp;/&nbsp; thinking-online.com</span></div>
</div>'''

cover = f'''<div class="page">
 <div class="hero">
   <div class="k">THINKING · 30-DAY METHOD</div>
   <h1>30日 <span class="a">1000単語</span> 暗記法</h1>
   <p>「1回で覚える」のではなく、<b style="color:#fff">忘れる前に何度も出会う</b>のが暗記のコツ。
   1000語を50語×20ブロックに分け、新しい50語＋過去のブロックを<b style="color:#fff">1日後・3日後・1週間後</b>に
   確認テストで繰り返す“スパイラル方式”。1つの語に自然と4〜5回触れられます。</p>
 </div>
 <div class="cards">
   <div class="card"><div class="n">50語/日</div><div class="t">新規インプット</div><div class="d">Day1–20で毎日1ブロック。20日で全1000語を1周。</div></div>
   <div class="card"><div class="n">×4〜5回</div><div class="t">スパイラル復習</div><div class="d">導入→翌日→3日後→1週間後→総復習。忘却曲線に沿って定着。</div></div>
   <div class="card"><div class="n">毎日テスト</div><div class="t">確認で固める</div><div class="d">読むだけでなく4択テストで“思い出す”。弱点だけ再確認。</div></div>
 </div>
 <h2 class="sec">1日の進め方（15〜25分）</h2>
 <div class="flow">
   <div class="step"><div class="s">STEP 1</div><div class="h">新規50語を確認</div><div class="b">今日のブロックをテスト形式でざっと1周。分からない語に印。</div></div>
   <div class="step"><div class="s">STEP 2</div><div class="h">復習ブロックを確認</div><div class="b">スケジュール表の「復習」欄のブロックをテスト。間隔復習で長期記憶へ。</div></div>
   <div class="step"><div class="s">STEP 3</div><div class="h">間違いだけ再チェック</div><div class="b">×が付いた語だけもう一度。翌日の最初にも軽く見直す。</div></div>
 </div>
 <div class="note">■ 使い方：範囲(例 <b>1–50</b>)は各単語帳の No.。THINKINGの確認テスト <b>/test/&lt;単語帳&gt;/1-50</b> と対応。
 「シャッフル」は <b>/mix-…</b>、「総合テスト」は <b>/final-…</b> を使うと、そのまま印刷/PDFで確認できます。<br>
 ■ Phase1(Day1–20)＝インプット＋間隔復習、Phase2(Day21–30)＝全体の総復習で仕上げ。</div>
 <h2 class="sec">この30日の全体像</h2>
 <div class="note" style="background:#fff;border:1px solid var(--line)">
 <b>Day 1–20</b>　毎日：新規50語 ＋ 復習(前日・3日前・1週間前のブロック) ＋ 確認テスト<br>
 <b>Day 21–29</b>　総復習：1日100語(2ブロック)を回し、シャッフルテストで抜けをチェック<br>
 <b>Day 30</b>　仕上げ：全1000語から総合テスト。8割取れれば完成、弱点はリスト化して継続。</div>
 <div class="foot"><span class="b">THINKING</span><span>30日1000単語暗記法 &nbsp;/&nbsp; thinking-online.com</span></div>
</div>'''

p1 = table_html("Day1–20：毎日あたらしい50語を入れ、過去のブロックを間隔をあけて復習します（数字はNo.範囲）。",
                "スケジュール表 ①", "PHASE 1 ・ INPUT", rows[:20])
p2 = table_html("Day21–30：新規はなし。全20ブロックを総復習し、テストで確実に仕上げます。",
                "スケジュール表 ②", "PHASE 2 ・ REVIEW", rows[20:])

doc = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>30日1000単語暗記法</title><style>{CSS}</style></head><body>{cover}{p1}{p2}</body></html>'''
open(os.path.join(ROOT, "plan30.html"), "w", encoding="utf-8").write(doc)
print("wrote schedule.csv + plan30.html (3 pages)")
