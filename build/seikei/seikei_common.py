# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル — 共通ビルド基盤
学部別合格設計塾THINKING（合同会社ARC）

THINKING標準デザインシステム（navy/gold/落款）とレンダリングヘルパーを提供する。
各巻の build_daimonN.py はこのモジュールを import して単一PDFを吐く。
"""
from html import escape as _esc

GOLD = "#b8954a"

# ---------------------------------------------------------------------------
# 基本ユーティリティ
# ---------------------------------------------------------------------------

def esc(s):
    """None安全なHTMLエスケープ。"""
    if s is None:
        return ""
    return _esc(str(s))


def _raw(s):
    """既にHTMLとして組み立て済みの文字列をそのまま返す（可読性のため）。"""
    return "" if s is None else str(s)


# ---------------------------------------------------------------------------
# デザインシステムCSS
# ---------------------------------------------------------------------------

def build_css(running_title):
    """running_title は @top-left に出る巻タイトル。"""
    return """
:root{
  --navy:#16263f; --navy-deep:#0e1a2e; --navy-soft:#1c3354;
  --gold:#b8954a; --gold-light:#d9c08a; --gold-deep:#9a7a36;
  --vermilion:#c8431f; --ink:#1f2933; --gray:#5b6672;
  --paper:#ffffff; --washi:#f7f4ee; --washi-2:#f1ece1; --line:#d8d2c4; --teal:#1e7a4f;
}

@page{
  size:A4; margin:19mm 15mm 16mm 15mm;
  @bottom-center{content:counter(page); font-family:"Noto Sans CJK JP"; font-size:8.5pt; color:#8a8273;}
  @top-left{content:"__RUNNING__"; font-family:"Noto Sans CJK JP"; font-size:7.4pt; color:#a89f8c; letter-spacing:.03em;}
  @top-right{content:"学部別合格設計塾THINKING"; font-family:"Noto Serif CJK JP"; font-size:7.3pt; letter-spacing:.12em; color:var(--gold);}
}
@page cover{ margin:0; @bottom-center{content:none;} @top-left{content:none;} @top-right{content:none;} }
@page chapter{ @top-left{content:none;} }

*{ box-sizing:border-box; }
html{ -weasy-hyphens:none; }
body{
  font-family:"Noto Serif CJK JP", serif;
  font-size:10pt; line-height:1.85; color:var(--ink);
  margin:0; padding:0;
}
p{ margin:0 0 .55em; text-align:justify; }
.sans{ font-family:"Noto Sans CJK JP", sans-serif; }
.serif{ font-family:"Noto Serif CJK JP", serif; }
.en{ font-family:"Noto Serif CJK JP", "Times New Roman", serif; }
b, strong{ font-weight:700; }
.nav{ color:var(--navy); }
.gld{ color:var(--gold-deep); }
.ver{ color:var(--vermilion); }
.tl{ color:var(--teal); }
.small{ font-size:8.6pt; color:var(--gray); line-height:1.7; }
.tiny{ font-size:7.8pt; color:var(--gray); line-height:1.65; }

/* ---------- 表紙 ---------- */
.cover{
  page:cover; position:relative; width:210mm; height:297mm; overflow:hidden;
  background:linear-gradient(150deg, var(--navy-deep) 0%, var(--navy) 55%, var(--navy-soft) 100%);
  color:#f4efe4;
}
.cover .frame{
  position:absolute; top:13mm; left:13mm; right:13mm; bottom:13mm;
  border:0.6pt solid rgba(217,192,138,.42);
}
.cover .frame::after{
  content:""; position:absolute; top:3mm; left:3mm; right:3mm; bottom:3mm;
  border:0.4pt solid rgba(217,192,138,.22);
}
.cover .kicker{
  position:absolute; top:30mm; left:0; right:0; text-align:center;
  font-family:"Noto Sans CJK JP"; letter-spacing:.55em; font-size:9.5pt;
  color:var(--gold-light); text-indent:.55em;
}
.cover .kicker2{
  position:absolute; top:37mm; left:0; right:0; text-align:center;
  font-family:"Noto Serif CJK JP"; letter-spacing:.16em; font-size:8pt;
  color:rgba(244,239,228,.66);
}
.cover .badge{
  position:absolute; top:24mm; right:20mm; width:26mm; height:38mm;
  border:0.8pt solid var(--gold-light); color:var(--gold-light);
  writing-mode:vertical-rl; text-orientation:upright;
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:12pt; letter-spacing:.28em;
  display:flex; align-items:center; justify-content:center;
  background:rgba(14,26,46,.35);
}
.cover .univ{
  position:absolute; top:96mm; left:0; right:0; text-align:center;
  font-family:"Noto Serif CJK JP"; font-weight:900; color:#fbf7ee;
  font-size:42pt; letter-spacing:.10em; line-height:1.12;
}
.cover .fac{
  position:absolute; top:138mm; left:0; right:0; text-align:center;
  font-family:"Noto Serif CJK JP"; font-weight:900; color:var(--gold-light);
  font-size:23pt; letter-spacing:.30em; text-indent:.30em;
}
.cover .rule{
  position:absolute; left:50%; transform:translateX(-50%); width:74mm; height:0;
  border-top:1.4pt solid var(--gold);
}
.cover .rule.r1{ top:130mm; }
.cover .rule.r2{ top:154mm; }
.cover .maintitle{
  position:absolute; top:166mm; left:0; right:0; text-align:center;
  font-family:"Noto Serif CJK JP"; font-weight:700; color:#f4efe4;
  font-size:15pt; letter-spacing:.14em;
}
.cover .volband{
  position:absolute; top:186mm; left:32mm; right:32mm; text-align:center;
  padding:5mm 0; border-top:0.5pt solid rgba(217,192,138,.5);
  border-bottom:0.5pt solid rgba(217,192,138,.5);
}
.cover .volno{
  font-family:"Noto Sans CJK JP"; letter-spacing:.4em; font-size:10pt;
  color:var(--gold-light); text-indent:.4em;
}
.cover .voltitle{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:18pt;
  color:#fbf7ee; letter-spacing:.10em; margin-top:2.5mm;
}
.cover .tagline{
  position:absolute; top:224mm; left:0; right:0; text-align:center;
  font-family:"Noto Serif CJK JP"; font-size:12pt; color:var(--gold-light);
  letter-spacing:.14em;
}
.cover .lockup{
  position:absolute; bottom:20mm; left:0; right:0; text-align:center;
}
.cover .lockup .brand{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:13pt;
  color:#f4efe4; letter-spacing:.16em;
}
.cover .lockup .sub{
  font-family:"Noto Sans CJK JP"; font-size:7.6pt; letter-spacing:.35em;
  color:rgba(217,192,138,.85); margin-top:2mm; text-indent:.35em;
}

/* ---------- 章扉 ---------- */
.chapter{ page:chapter; page-break-before:always; padding-top:6mm; }
.chapter .band{
  background:linear-gradient(120deg, var(--navy) 0%, var(--navy-soft) 100%);
  color:#f4efe4; padding:11mm 12mm 10mm; position:relative;
  border-left:3.5pt solid var(--gold);
}
.chapter .cno{
  font-family:"Noto Sans CJK JP"; letter-spacing:.42em; font-size:9pt;
  color:var(--gold-light); text-indent:.42em;
}
.chapter .ctitle{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:20pt;
  letter-spacing:.06em; margin-top:3mm; line-height:1.3;
}
.chapter .clead{
  font-family:"Noto Serif CJK JP"; font-size:10pt; line-height:1.85;
  margin-top:5mm; color:#e7e0d2; max-width:150mm;
}
.chapter .goldbar{ height:2pt; background:var(--gold); width:38mm; margin:6mm 0 0; }

/* ---------- セクション見出し ---------- */
.h2{
  font-family:"Noto Sans CJK JP"; font-weight:700; font-size:13pt; color:var(--navy);
  border-left:4pt solid var(--gold); padding:1mm 0 1mm 3.5mm; margin:8mm 0 3.5mm;
  page-break-after:avoid;
}
.h3{
  font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10.8pt; color:var(--navy-soft);
  margin:5.5mm 0 2.2mm; page-break-after:avoid;
  border-bottom:0.5pt solid var(--line); padding-bottom:1mm;
}
.lead{ font-size:10pt; color:var(--ink); margin-bottom:3mm; }

/* ---------- 汎用ボックス ---------- */
.box{ border:0.7pt solid var(--line); border-radius:1.5mm; padding:4mm 4.5mm; margin:3.5mm 0;
      background:var(--washi); page-break-inside:avoid; }
.box .bx-t{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt; color:var(--navy);
      margin-bottom:2mm; letter-spacing:.02em; }
.box.plain{ background:var(--paper); }

.callout{ border-left:3.5pt solid var(--gold); background:var(--washi-2);
      padding:3.5mm 4.5mm; margin:3.5mm 0; page-break-inside:avoid; }
.callout .co-t{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt;
      color:var(--gold-deep); margin-bottom:1.5mm; }

.warn{ border-left:3.5pt solid var(--vermilion); background:#fbeee9;
      padding:3.5mm 4.5mm; margin:3.5mm 0; page-break-inside:avoid; }
.warn .wn-t{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt;
      color:var(--vermilion); margin-bottom:1.5mm; }

.win{ border-left:3.5pt solid var(--teal); background:#eaf5ef;
      padding:3.5mm 4.5mm; margin:3.5mm 0; page-break-inside:avoid; }
.win .wi-t{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt;
      color:var(--teal); margin-bottom:1.5mm; }

/* ---------- 表 ---------- */
table.t{ width:100%; border-collapse:collapse; margin:3mm 0; font-size:9pt;
      page-break-inside:avoid; }
table.t thead th{ background:var(--navy); color:#f4efe4; font-family:"Noto Sans CJK JP";
      font-weight:600; font-size:8.8pt; padding:2.4mm 2.6mm; text-align:left;
      border:0.5pt solid var(--navy-soft); }
table.t tbody td{ padding:2.2mm 2.6mm; border:0.5pt solid var(--line); vertical-align:top;
      line-height:1.6; }
table.t tbody tr:nth-child(odd) td{ background:var(--washi); }
table.t tbody tr:nth-child(even) td{ background:var(--paper); }
table.t td.c{ text-align:center; }
table.t td.num{ font-family:"Noto Sans CJK JP"; text-align:center; white-space:nowrap; }

/* ---------- チェックリスト ---------- */
ul.ck{ list-style:none; margin:2.5mm 0; padding:0; }
ul.ck li{ font-family:"Noto Sans CJK JP"; font-size:9.4pt; line-height:1.75;
      padding:1mm 0 1mm 7mm; text-indent:-7mm; }
ul.ck li::before{ content:"□"; color:var(--gold-deep); margin-right:2.5mm; font-size:10pt; }

ul.dot{ margin:2mm 0 2mm 5mm; padding:0; }
ul.dot li{ margin:.6mm 0; line-height:1.75; }

ol.step{ margin:2mm 0 2mm 6mm; padding:0; counter-reset:st; list-style:none; }
ol.step li{ position:relative; padding:1mm 0 1mm 8mm; text-indent:0; line-height:1.7;
      counter-increment:st; }
ol.step li::before{ content:counter(st); position:absolute; left:0; top:1mm;
      width:5mm; height:5mm; background:var(--navy); color:#fff;
      font-family:"Noto Sans CJK JP"; font-size:8pt; font-weight:700;
      display:inline-flex; align-items:center; justify-content:center; border-radius:50%; }

/* ---------- 演習: 問題編 ---------- */
.prob{ page-break-inside:auto; margin:0 0 4mm; }
.prob-head{
  display:flex; align-items:stretch; margin:7mm 0 3mm; page-break-after:avoid;
  border:0.8pt solid var(--navy); border-radius:1.5mm; overflow:hidden;
}
.prob-head .id{
  background:var(--navy); color:#f4efe4; font-family:"Noto Sans CJK JP"; font-weight:700;
  font-size:11pt; padding:2.6mm 4mm; display:flex; align-items:center; letter-spacing:.04em;
  white-space:nowrap;
}
.prob-head .meta{
  flex:1; padding:2mm 4mm; background:var(--washi); font-family:"Noto Sans CJK JP";
  font-size:8.5pt; color:var(--gray); display:flex; flex-direction:column; justify-content:center;
}
.prob-head .meta .ttl{ font-weight:700; color:var(--navy); font-size:9.6pt; margin-bottom:.5mm; }
.prob-head .limit{
  background:var(--gold); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:700;
  font-size:8.6pt; padding:0 4mm; display:flex; align-items:center; white-space:nowrap;
}

.passage{
  border:0.6pt solid var(--line); background:#fffdf8; padding:4mm 5mm; margin:3mm 0;
  font-family:"Noto Serif CJK JP", "Times New Roman", serif; font-size:9.7pt; line-height:1.95;
  color:#22303f;
}
.passage p{ text-align:left; margin:0 0 .6em; }
.passage .pno{ font-family:"Noto Sans CJK JP"; font-size:7.6pt; color:var(--gold-deep);
      font-weight:700; margin-right:1.5mm; }
.passage .blk{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy);
      background:var(--washi-2); border:0.5pt solid var(--gold-light); border-radius:1mm;
      padding:0 1.6mm; margin:0 .4mm; white-space:nowrap; }
.passage .ul{ border-bottom:1.2pt solid var(--vermilion); padding-bottom:.3pt;
      font-style:normal; }
.passage .ulmark{ font-family:"Noto Sans CJK JP"; font-size:7pt; color:var(--vermilion);
      font-weight:700; vertical-align:super; }
.passage .ttl{ text-align:center; font-weight:700; font-size:10.4pt; margin-bottom:2.5mm;
      color:var(--navy); }

/* 語群（Set A / Set B） */
.wordbank{ border:0.7pt solid var(--navy-soft); border-radius:1.5mm; margin:3mm 0;
      overflow:hidden; page-break-inside:avoid; }
.wordbank .wb-h{ background:var(--navy-soft); color:#f4efe4; font-family:"Noto Sans CJK JP";
      font-weight:700; font-size:9pt; padding:1.6mm 4mm; letter-spacing:.05em; }
.wordbank .wb-b{ padding:3mm 4mm; background:var(--washi); }
.wordbank .wb-row{ display:flex; flex-wrap:wrap; gap:2mm 3mm; }
.wordbank .chip{ font-family:"Noto Sans CJK JP", "Times New Roman", serif; font-size:9pt;
      border:0.5pt solid var(--line); background:#fff; border-radius:1mm; padding:1mm 2.6mm;
      white-space:nowrap; }
.wordbank .chip b{ color:var(--gold-deep); font-family:"Noto Sans CJK JP"; margin-right:1mm; }

/* 設問 */
.q{ margin:2.4mm 0; padding-left:0; page-break-inside:avoid; }
.q .qh{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt; color:var(--navy);
      margin-bottom:1mm; }
.q .qh .mk{ display:inline-block; background:var(--navy); color:#fff; font-size:7.8pt;
      border-radius:1mm; padding:0 2mm; margin-right:2mm; vertical-align:.5pt; }
.choices{ margin:.5mm 0 0; }
.choices .ch{ font-family:"Noto Serif CJK JP", "Times New Roman", serif; font-size:9.4pt;
      line-height:1.6; padding:.4mm 0 .4mm 7mm; text-indent:-7mm; }
.choices .ch .lab{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--gold-deep);
      margin-right:2mm; }
.choices.inline{ display:flex; flex-wrap:wrap; gap:1mm 6mm; }
.choices.inline .ch{ padding-left:0; text-indent:0; }

/* ---------- 解答解説編 ---------- */
.ans{ page-break-inside:auto; margin:0 0 3mm; }
.ans-head{ display:flex; align-items:center; gap:3mm; margin:6mm 0 2.5mm;
      border-bottom:1.4pt solid var(--gold); padding-bottom:1.5mm; page-break-after:avoid; }
.ans-head .id{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:11pt; color:var(--navy);
      background:var(--washi-2); border:0.6pt solid var(--gold-light); border-radius:1mm;
      padding:.6mm 3mm; }
.ans-head .ttl{ font-family:"Noto Serif CJK JP"; font-weight:700; font-size:11pt; color:var(--navy); }

.keytable{ width:100%; border-collapse:collapse; margin:2.5mm 0; font-family:"Noto Sans CJK JP";
      font-size:9pt; page-break-inside:avoid; }
.keytable th{ background:var(--navy); color:#fff; padding:1.8mm 2mm; border:0.5pt solid var(--navy-soft);
      font-weight:600; font-size:8.4pt; }
.keytable td{ padding:1.8mm 2mm; border:0.5pt solid var(--line); text-align:center; }
.keytable td.ans{ font-weight:700; color:var(--vermilion); }
.keytable td.w{ font-family:"Times New Roman", serif; }

.exp{ margin:2mm 0 3mm; }
.exp .ex-q{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.8pt; color:var(--navy);
      background:var(--washi); border-left:3pt solid var(--navy); padding:1.4mm 3mm; margin:3mm 0 1.5mm;
      page-break-after:avoid; }
.exp .ex-q .badge{ font-family:"Noto Sans CJK JP"; font-size:7.6pt; background:var(--gold);
      color:#fff; border-radius:1mm; padding:0 2mm; margin-right:2mm; }
.exp .ex-a{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--teal); font-size:9.4pt;
      margin:1mm 0; }
.exp .ex-a .x{ color:var(--vermilion); }
.exp p{ font-size:9.5pt; line-height:1.8; }
.exp .why{ margin:1.5mm 0; }
.exp .why .row{ font-size:9.1pt; line-height:1.7; padding:.6mm 0 .6mm 6mm; text-indent:-6mm; }
.exp .why .row .lab{ font-family:"Noto Sans CJK JP"; font-weight:700; margin-right:1.5mm; }
.exp .why .row.ok .lab{ color:var(--teal); }
.exp .why .row.ng .lab{ color:var(--vermilion); }
.trans{ background:var(--washi-2); border:0.5pt solid var(--line); border-radius:1mm;
      padding:2.5mm 3.5mm; margin:2.5mm 0; font-size:9pt; line-height:1.75; }
.trans .tr-t{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8.6pt; color:var(--gold-deep);
      margin-bottom:1mm; }

.vocab{ width:100%; border-collapse:collapse; margin:2.5mm 0; font-size:8.8pt;
      page-break-inside:auto; }
.vocab th{ background:var(--navy-soft); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:600;
      font-size:8.2pt; padding:1.6mm 2mm; text-align:left; }
.vocab td{ padding:1.4mm 2mm; border-bottom:0.5pt solid var(--line); vertical-align:top; line-height:1.55; }
.vocab td.w{ font-family:"Times New Roman", serif; font-weight:600; white-space:nowrap; color:var(--navy); }
.vocab td.p{ font-family:"Noto Sans CJK JP"; color:var(--gray); font-size:8pt; white-space:nowrap; }
.vocab tr:nth-child(even) td{ background:var(--washi); }

/* ---------- 目次・帯 ---------- */
.divider{ text-align:center; margin:4mm 0; color:var(--gold); letter-spacing:1.2em; font-size:8pt; }
.pagebreak{ page-break-before:always; }
.avoid{ page-break-inside:avoid; }

.toc{ margin:4mm 0; }
.toc .row{ display:flex; align-items:baseline; font-family:"Noto Sans CJK JP"; font-size:9.6pt;
      padding:1.6mm 0; border-bottom:0.5pt dotted var(--line); }
.toc .row .n{ color:var(--gold-deep); font-weight:700; width:12mm; }
.toc .row .t{ flex:1; color:var(--navy); }
.toc .row .pg{ color:var(--gray); font-size:8.6pt; }

.hero-sub{ font-family:"Noto Sans CJK JP"; color:var(--gray); font-size:9pt; margin:-1mm 0 4mm; }

.miniband{ background:var(--navy); color:#f4efe4; font-family:"Noto Sans CJK JP"; font-weight:700;
      font-size:10pt; letter-spacing:.06em; padding:2.2mm 4mm; margin:6mm 0 3mm; border-left:3.5pt solid var(--gold);
      page-break-after:avoid; }
""".replace("__RUNNING__", running_title)


# ---------------------------------------------------------------------------
# 表紙
# ---------------------------------------------------------------------------

def cover(vol_no, vol_title, running_sub, badge="完全攻略"):
    return f"""
<section class="cover">
  <div class="frame"></div>
  <div class="kicker">大学別・学部別 英語入試 徹底分析</div>
  <div class="kicker2">FACULTY-SPECIFIC ADMISSIONS DESIGN &nbsp;/&nbsp; THINKING</div>
  <div class="badge">{esc(badge)}</div>
  <div class="rule r1"></div>
  <div class="univ">成蹊大学</div>
  <div class="rule r2"></div>
  <div class="fac">経営学部</div>
  <div class="maintitle">英語 完全攻略マニュアル</div>
  <div class="volband">
    <div class="volno">{esc(vol_no)}</div>
    <div class="voltitle">{esc(vol_title)}</div>
  </div>
  <div class="tagline">受験は、根性じゃなく、設計。</div>
  <div class="lockup">
    <div class="brand">学部別合格設計塾 THINKING</div>
    <div class="sub">GOUDOU KAISHA ARC &nbsp;/&nbsp; JUKENNO OUSAMA</div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# 章扉
# ---------------------------------------------------------------------------

def chapter(cno, title, lead):
    return f"""
<section class="chapter">
  <div class="band">
    <div class="cno">{esc(cno)}</div>
    <div class="ctitle">{_raw(title)}</div>
    <div class="clead">{_raw(lead)}</div>
    <div class="goldbar"></div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# 汎用パーツ
# ---------------------------------------------------------------------------

def h2(t):
    return f'<div class="h2">{_raw(t)}</div>'

def h3(t):
    return f'<div class="h3">{_raw(t)}</div>'

def miniband(t):
    return f'<div class="miniband">{_raw(t)}</div>'

def p(t):
    return f'<p>{_raw(t)}</p>'

def lead(t):
    return f'<p class="lead">{_raw(t)}</p>'

def box(title, body_html):
    t = f'<div class="bx-t">{_raw(title)}</div>' if title else ""
    return f'<div class="box">{t}{_raw(body_html)}</div>'

def callout(title, body_html):
    t = f'<div class="co-t">{_raw(title)}</div>' if title else ""
    return f'<div class="callout">{t}{_raw(body_html)}</div>'

def warn(title, body_html):
    t = f'<div class="wn-t">{_raw(title)}</div>' if title else ""
    return f'<div class="warn">{t}{_raw(body_html)}</div>'

def win(title, body_html):
    t = f'<div class="wi-t">{_raw(title)}</div>' if title else ""
    return f'<div class="win">{t}{_raw(body_html)}</div>'

def steps(items):
    lis = "".join(f"<li>{_raw(x)}</li>" for x in items)
    return f'<ol class="step">{lis}</ol>'

def dots(items):
    lis = "".join(f"<li>{_raw(x)}</li>" for x in items)
    return f'<ul class="dot">{lis}</ul>'

def checks(items):
    lis = "".join(f"<li>{_raw(x)}</li>" for x in items)
    return f'<ul class="ck">{lis}</ul>'

def table(headers, rows, aligns=None):
    """headers: list[str]; rows: list[list[str]]; aligns: list[str|None] ('c'/'num'/None)."""
    ths = "".join(f"<th>{_raw(h)}</th>" for h in headers)
    trs = []
    for r in rows:
        tds = []
        for i, cell in enumerate(r):
            cls = ""
            if aligns and i < len(aligns) and aligns[i]:
                cls = f' class="{aligns[i]}"'
            tds.append(f"<td{cls}>{_raw(cell)}</td>")
        trs.append("<tr>" + "".join(tds) + "</tr>")
    return f'<table class="t"><thead><tr>{ths}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


# ---------------------------------------------------------------------------
# HTMLドキュメント組み立て
# ---------------------------------------------------------------------------

def document(css, body_sections):
    body = "\n".join(body_sections)
    return f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="utf-8"><style>{css}</style></head>
<body>
{body}
</body></html>"""


def write_pdf(html_str, out_path):
    from weasyprint import HTML
    HTML(string=html_str).write_pdf(out_path)
    return out_path
