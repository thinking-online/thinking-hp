# -*- coding: utf-8 -*-
"""現時点の内容を1本のPDFにまとめる。本の体裁にはしない。内容確認用。
book/ で実行。出力 build/内容確認.html → chromium で PDF 化。"""
import html, re, io, os, sys

def esc(s):
    return html.escape(s, quote=False)

def md(text):
    """最小限の markdown → HTML。全角スペースのインデントは保つ。"""
    out, lines = [], text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if l.startswith("```"):
            buf = []
            i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(esc(lines[i]))
                i += 1
            i += 1
            out.append('<pre class="blk">' + "\n".join(buf) + "</pre>")
            continue
        if re.match(r'^\s*(---|___)\s*$', l):
            out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            lv = len(m.group(1))
            out.append(f'<h{lv}>{esc(m.group(2))}</h{lv}>'); i += 1; continue
        if l.startswith("|") and i + 1 < n and set(lines[i+1].replace("|","").strip()) <= set("-: "):
            head = [c.strip() for c in l.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            t = "<table><tr>" + "".join(f"<th>{esc(c)}</th>" for c in head) + "</tr>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</table>"); continue
        if not l.strip():
            i += 1; continue
        # 連続する非空行を1つの段落に。行頭の全角スペースはそのまま出す
        buf = []
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4})\s|^\s*---\s*$|^\|', lines[i]) \
              and not lines[i].startswith("```"):
            buf.append(esc(lines[i].rstrip()))
            i += 1
        cls = ' class="ind"' if buf and buf[0].startswith("　") else ""
        out.append(f'<p{cls}>' + "<br>".join(buf) + "</p>")
    return "\n".join(out)

def read(p):
    return io.open(p, encoding="utf-8").read()

def strip_h1(s):
    return re.sub(r'^#\s+.*\n', '', s, count=1)

SECTIONS = []

def add(title, kicker, body, note=None):
    SECTIONS.append((title, kicker, body, note))

# ---------------------------------------------------------------- 中身
add("1　全体構成", "いま決まっている形", """
```
はじめに　　　　　　この本は、10秒で始まります

序章　　　「自分に合った勉強法」を、探すのをやめる
　　　　　やめる4つ　／　かわりにやる1つ

第1章　　 結果 ＝ 戦略 × やり方 × 量
　　　　　覚えるのは、この式だけ

第2章　戦略編　　　　01〜09
第3章　計画編　　　　10〜14
第4章　インプット編　15〜21
第5章　暗記編　　　　22〜28
第6章　演習編　　　　29〜35
第7章　復習編　　　　36〜43
第8章　本番編　　　　44〜46
第9章　継続編　　　　47〜50

終章　　　5教科で、50をどう使うか
巻末　　　50を1枚に／悩み別の引き方／再現性テスト／保護者の方へ／
　　　　　おわりに／参考文献
```

番号は章をまたいで01から50まで通す。章が変わっても切れない。
読者には50本の一本道に見えて、探すときだけ章で引ける。

分量は本文で約11万字、全体で250〜280ページ。四六判。
""")

add("2　冒頭メッセージ", "著者執筆。原文のまま", strip_h1(read("manuscript/冒頭メッセージ.md")).replace("著者執筆。原文のまま保存。\n", ""))
add("3　序章", "やめる。そして、探すのをやめる", strip_h1(read("manuscript/序章_v5.md")))
add("4　第1章", "本質。50項目がノウハウにならないための芯", strip_h1(read("manuscript/第1章_v5.md")))
add("5　目次　50項目", "×と○は、心の声で書く", strip_h1(read("manuscript/企画書/目次_第5版.md")))
add("6　本文サンプル　項目29", "確定した型で書いたもの", strip_h1(read("manuscript/項目29_解説を読んで納得したら.md")))
add("7　本文サンプル　項目11", "型の確定より前に書いたもの。頭のなかの節がまだ入っていない",
    strip_h1(read("manuscript/見本_節_計画.md")))
add("8　項目の型と、3つの問い", "本質と具体をつなぐ部品", strip_h1(read("docs/22_本質と具体をつなぐ設計.md")))

add("9　残っている宿題", "著者に出してもらうもの／これから決めるもの", """
## 著者からしか出ないもの

```
1　冒頭メッセージの中の二択の問題　　〔ここに二択の問題が入る〕のところ
2　各章1本の厚い項目に入れる、実在の生徒の話（固有名詞・数字・失敗込み）
3　キングコング西野さんの話　　どの話を指しているか不明
4　学研刊行の問題集　　第1章の事例に使う。書名を編集部からもらう
```

## これから決めるもの

```
1　本番編を3本から5本にするか（リアプレイザル、不安の書き出し）
2　暗記編に記憶術を1本入れるか
3　序章の4つの説明をどこまで短くするか
　　同じ4つを類書3冊が書いているため、紙を使いすぎない
```

## 杉浦さんへの報告が必要な点

```
1　章の軸を、6つの力から〜編に変えた
2　番号を01から50まで通しにした
3　総論を2章立てにした（序章でやめる、第1章で式）
4　ご指摘の①→⑥の誤解は、章が工程でなくなったので消えた
5　AIは、計画・暗記・演習の項目に入れる
　　ご指示の3つの用途（計画を立てる／教材を作る／勉強法を編み出す）と一致
6　45項目を50項目にした（本番編の新設ほか）
```

## スケジュール

```
原稿締切　11月30日
発売　　　2月中旬

残り日数　28日のうち、ここまでで序章・第1章・サンプル2本
これから　50項目の本文、終章、巻末、図解ラフ約50点
```
""")

# ---------------------------------------------------------------- 出力
CSS = """
@page { size: A4 portrait; margin: 18mm 20mm 20mm 20mm; }
* { box-sizing: border-box; }
body { font-family: "Hiragino Sans","Noto Sans CJK JP","Yu Gothic",sans-serif;
       font-size: 10pt; line-height: 1.85; color:#111; margin:0; }
.cover { height: 250mm; display:flex; flex-direction:column; justify-content:center; }
.cover .t { font-size: 22pt; font-weight:700; line-height:1.5; }
.cover .s { font-size: 11pt; color:#555; margin-top:14mm; line-height:2.1; }
section { break-before: page; }
section.first { break-before: auto; }
.kicker { font-size: 8.6pt; color:#888; letter-spacing:.04em; margin:0 0 1mm; }
h1 { font-size: 16pt; margin:0 0 7mm; padding-bottom:2.5mm;
     border-bottom:2.5px solid #111; font-weight:700; }
h2 { font-size: 12.2pt; margin:9mm 0 3mm; font-weight:700;
     border-left:4px solid #111; padding-left:3mm; }
h3 { font-size: 10.6pt; margin:6mm 0 2mm; font-weight:700; color:#333; }
h4 { font-size: 10pt; margin:4mm 0 1.5mm; font-weight:700; color:#444; }
p { margin:0 0 3.2mm; }
p.ind { white-space: pre-wrap; }
hr { border:0; border-top:1px solid #ddd; margin:6mm 0; }
pre.blk { font-family:"Hiragino Sans","Noto Sans CJK JP",monospace; font-size:9pt;
      line-height:1.75; background:#f6f6f4; border:1px solid #e3e3df;
      padding:3.5mm 4.5mm; margin:0 0 4mm; white-space:pre-wrap;
      break-inside: avoid-page; }
table { border-collapse:collapse; margin:0 0 4mm; font-size:9pt; width:100%; }
th,td { border:1px solid #ccc; padding:1.6mm 2.6mm; text-align:left; vertical-align:top; }
th { background:#f2f2ef; font-weight:700; }
"""

parts = ['<meta charset="utf-8"><title>内容確認</title><style>%s</style>' % CSS]
parts.append("""<div class="cover">
<div class="t">頭のいい人が勉強で、<br>絶対にやらないこと</div>
<div class="s">内容確認用　全文まとめ<br>
2026年11月3日　朝倉 徹大<br><br>
構成／冒頭メッセージ／序章／第1章／目次50項目／本文サンプル2本／項目の型／宿題</div>
</div>""")

for idx, (title, kicker, body, note) in enumerate(SECTIONS):
    cls = ' class="first"' if False else ''
    parts.append(f'<section{cls}><div class="kicker">{esc(kicker)}</div><h1>{esc(title)}</h1>')
    parts.append(md(body))
    parts.append('</section>')

os.makedirs("build", exist_ok=True)
io.open("build/内容確認.html", "w", encoding="utf-8").write("\n".join(parts))
print("ok build/内容確認.html")
