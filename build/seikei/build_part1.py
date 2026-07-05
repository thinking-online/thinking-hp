# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル 第1部
「出題傾向の徹底分析と合格戦略」
学部別合格設計塾THINKING（合同会社ARC）

一次資料: 2025年度 成蹊 一般選抜「外国語(英語)」問題冊子（18p・全問マーク・解答1〜50・大問5題）
出力: kakomon/seikei-u/manual-p1.pdf
"""
import os
from html import escape as esc
from weasyprint import HTML

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "kakomon", "seikei-u", "manual-p1.pdf")
VOL_TITLE = "第1部 出題傾向の徹底分析と合格戦略"

# =============================================================================
# デザインシステム（THINKING標準）
# =============================================================================
CSS = """
:root{
  --navy:#16263f; --navy-deep:#0e1a2e; --navy-soft:#1c3354;
  --gold:#b8954a; --gold-light:#d9c08a; --gold-deep:#9a7a36;
  --vermilion:#c8431f; --ink:#1f2933; --gray:#5b6672;
  --paper:#ffffff; --washi:#f7f4ee; --washi-2:#f1ece1; --line:#d8d2c4; --teal:#1e7a4f;
}
@page{
  size:A4; margin:19mm 15mm 16mm 15mm;
  @bottom-center{content:counter(page); font-family:"Noto Sans CJK JP"; font-size:8.5pt; color:#8a8273;}
  @top-left{content:"成蹊大学 経営学部 英語 完全攻略マニュアル【第1部】出題傾向の徹底分析と合格戦略"; font-family:"Noto Sans CJK JP"; font-size:7.4pt; color:#a89f8c; letter-spacing:.03em;}
  @top-right{content:"学部別合格設計塾THINKING"; font-family:"Noto Serif CJK JP"; font-size:7.3pt; letter-spacing:.12em; color:#b8954a;}
}
@page cover{ margin:0; @bottom-center{content:none;} @top-left{content:none;} @top-right{content:none;} }

*{ box-sizing:border-box; }
html{ -weasy-hyphens:none; }
body{
  font-family:"Noto Serif CJK JP", serif; font-size:10pt; line-height:1.85;
  color:var(--ink); margin:0; padding:0;
}
p{ margin:0 0 .7em; text-align:justify; }
strong{ font-weight:700; }
.sans{ font-family:"Noto Sans CJK JP", sans-serif; }
.small{ font-size:8.6pt; color:var(--gray); line-height:1.7; }

/* ---------- 表紙 ---------- */
.cover{
  page:cover; position:relative; width:210mm; height:297mm; overflow:hidden;
  background:linear-gradient(150deg, var(--navy-deep) 0%, var(--navy) 55%, var(--navy-soft) 100%);
  color:#fff;
}
.cover .frame{ position:absolute; inset:12mm; border:0.6pt solid rgba(217,192,138,.38); }
.cover .frame2{ position:absolute; inset:13.4mm; border:0.4pt solid rgba(217,192,138,.20); }
.cover .brandtop{
  position:absolute; top:20mm; left:0; right:0; text-align:center;
  font-family:"Noto Sans CJK JP"; font-size:9.5pt; letter-spacing:.42em; color:var(--gold-light);
  text-indent:.42em;
}
.cover .seal{
  position:absolute; top:20mm; right:20mm; writing-mode:vertical-rl;
  border:1pt solid var(--gold-light); color:var(--gold-light);
  font-family:"Noto Serif CJK JP"; font-weight:700; font-size:12pt; letter-spacing:.34em;
  padding:7mm 3.2mm; line-height:1; background:rgba(14,26,46,.28);
}
.cover .center{ position:absolute; top:104mm; left:20mm; right:20mm; }
.cover .kicker{
  font-family:"Noto Sans CJK JP"; font-size:11pt; letter-spacing:.30em; color:var(--gold-light);
  margin-bottom:7mm; text-indent:.30em;
}
.cover h1{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:41pt; line-height:1.24;
  margin:0; letter-spacing:.02em;
}
.cover h1 .dept{ font-size:25pt; font-weight:700; color:var(--gold-light); }
.cover .rule{ height:2.4pt; width:64mm; background:var(--gold); margin:8mm 0 7mm; }
.cover .subject{ font-family:"Noto Sans CJK JP"; font-size:15pt; letter-spacing:.20em; color:#eef2f7; }
.cover .voltag{
  display:inline-block; margin-top:9mm; border:0.8pt solid var(--gold-light);
  padding:2.4mm 6mm; font-family:"Noto Sans CJK JP"; font-size:11.5pt; letter-spacing:.14em;
  color:var(--gold-light);
}
.cover .subtitle{ margin-top:6mm; font-size:12.5pt; color:#d7dee7; letter-spacing:.06em; }
.cover .lock{
  position:absolute; bottom:20mm; left:20mm; right:20mm; text-align:center;
}
.cover .lock .mark{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:16pt; letter-spacing:.10em; color:#fff;
}
.cover .lock .arc{
  font-family:"Noto Sans CJK JP"; font-size:8.4pt; letter-spacing:.30em; color:var(--gold-light); margin-top:3mm;
}
.cover .philo{
  position:absolute; bottom:36mm; left:20mm; right:20mm; text-align:center;
  font-family:"Noto Serif CJK JP"; font-size:11pt; color:#cfd7e1; letter-spacing:.10em;
}

/* ---------- 章扉 ---------- */
.chapter-open{ break-before:page; margin:0 0 7mm; }
.chapter-open .band{
  background:var(--navy); color:#fff; padding:6.5mm 7mm 6mm; position:relative;
  border-left:3pt solid var(--gold);
}
.chapter-open .cno{
  font-family:"Noto Sans CJK JP"; font-size:9pt; letter-spacing:.34em; color:var(--gold-light);
}
.chapter-open .ctitle{
  font-family:"Noto Serif CJK JP"; font-weight:900; font-size:19pt; margin-top:2.5mm; line-height:1.3;
}
.chapter-open .clead{ font-size:9.4pt; color:var(--gray); margin-top:4mm; line-height:1.8; }

/* ---------- 見出し ---------- */
h2.sec{
  font-family:"Noto Sans CJK JP"; font-weight:700; font-size:13pt; color:var(--navy);
  margin:8mm 0 3.5mm; padding-bottom:1.8mm; border-bottom:1.6pt solid var(--gold);
  break-after:avoid;
}
h3.sub{
  font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10.6pt; color:var(--navy-soft);
  margin:6mm 0 2.5mm; padding-left:3mm; border-left:3pt solid var(--gold-light);
  break-after:avoid;
}
.lead{ font-size:10pt; color:#333; margin-bottom:4mm; }

/* ---------- 表 ---------- */
table{ width:100%; border-collapse:collapse; margin:3mm 0 5mm; font-size:8.9pt; }
table.data th{
  background:var(--navy); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:500;
  padding:2.4mm 2.6mm; text-align:left; border:0.4pt solid var(--navy-soft); letter-spacing:.02em;
}
table.data td{
  padding:2.2mm 2.6mm; border:0.4pt solid var(--line); vertical-align:top; line-height:1.6;
}
table.data tr:nth-child(even) td{ background:var(--washi); }
table.data td.c{ text-align:center; }
table.data .em{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy); }
.tblnote{ font-size:8pt; color:var(--gray); margin:-3mm 0 5mm; }

/* ---------- 枠 ---------- */
.box{ padding:4mm 5mm; margin:4mm 0; border-radius:1.2mm; break-inside:avoid; }
.box .bt{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.6pt; margin-bottom:2mm; letter-spacing:.04em; }
.box p{ font-size:9.2pt; line-height:1.75; }
.box.warn{ background:#fbf1ee; border:0.5pt solid #e6bcae; border-left:3pt solid var(--vermilion); }
.box.warn .bt{ color:var(--vermilion); }
.box.ok{ background:#eef6f1; border:0.5pt solid #b7d9c6; border-left:3pt solid var(--teal); }
.box.ok .bt{ color:var(--teal); }
.box.gold{ background:var(--washi); border:0.5pt solid var(--gold-light); border-left:3pt solid var(--gold); }
.box.gold .bt{ color:var(--gold-deep); }
.box.navy{ background:var(--washi-2); border:0.5pt solid var(--line); border-left:3pt solid var(--navy); }
.box.navy .bt{ color:var(--navy); }

/* ---------- タイプカード ---------- */
.tcard{ break-inside:avoid; margin:4.5mm 0; border:0.5pt solid var(--line); border-radius:1.4mm; overflow:hidden; }
.tcard .hd{
  display:flex; align-items:center; gap:3mm; background:var(--navy); color:#fff; padding:2.6mm 4mm;
}
.tcard .badge{
  font-family:"Noto Sans CJK JP"; font-weight:900; font-size:11pt; color:var(--navy);
  background:var(--gold-light); border-radius:1mm; padding:.6mm 2.4mm; letter-spacing:.02em;
}
.tcard .tname{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10.4pt; letter-spacing:.02em; }
.tcard .where{ margin-left:auto; font-family:"Noto Sans CJK JP"; font-size:8pt; color:var(--gold-light); }
.tcard .bd{ padding:3.2mm 4mm 3.6mm; background:#fff; }
.tcard .bd p{ font-size:9.1pt; margin:0 0 1.6mm; }
.tcard .howto{ margin:2mm 0 0; }
.tcard .howto .lbl{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8.6pt; color:var(--gold-deep); letter-spacing:.06em; }
ol.steps{ margin:1.4mm 0 0; padding-left:5.4mm; }
ol.steps li{ font-size:9pt; line-height:1.62; margin-bottom:1mm; }

/* ---------- チェックリスト ---------- */
ul.check{ list-style:none; margin:2.5mm 0; padding:0; }
ul.check li{
  font-family:"Noto Sans CJK JP"; font-size:9.2pt; line-height:1.7; padding-left:6mm; position:relative;
  margin-bottom:1.6mm;
}
ul.check li::before{ content:"\\2610"; position:absolute; left:0; color:var(--gold-deep); font-size:10.5pt; }

/* ---------- タイムテーブル ---------- */
.tl{ margin:3mm 0 5mm; }
.tl .row{ display:flex; align-items:stretch; break-inside:avoid; margin-bottom:1.4mm; }
.tl .t{
  flex:0 0 20mm; background:var(--navy); color:#fff; font-family:"Noto Sans CJK JP"; font-weight:700;
  font-size:8.8pt; display:flex; align-items:center; justify-content:center; border-radius:1mm 0 0 1mm;
}
.tl .bar{
  flex:1; background:var(--washi); border:0.5pt solid var(--line); border-left:none;
  border-radius:0 1mm 1mm 0; padding:2mm 3.5mm;
}
.tl .bar .nm{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:9.2pt; color:var(--navy); }
.tl .bar .ds{ font-size:8.5pt; color:var(--gray); line-height:1.55; }

/* ---------- ロードマップ ---------- */
.phase{ break-inside:avoid; border:0.5pt solid var(--line); border-top:3pt solid var(--gold); margin:3.5mm 0; padding:3.4mm 4.4mm; background:#fff; }
.phase .ph{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10pt; color:var(--navy); }
.phase .pw{ font-family:"Noto Sans CJK JP"; font-size:8.2pt; color:var(--gold-deep); letter-spacing:.08em; }
.phase ul{ margin:2mm 0 0; padding-left:5mm; }
.phase li{ font-size:9pt; line-height:1.66; margin-bottom:.8mm; }

/* ---------- ミニ・KPI ---------- */
.kpis{ display:flex; gap:3mm; margin:4mm 0 5mm; }
.kpi{ flex:1; border:0.5pt solid var(--line); border-radius:1.4mm; padding:3mm 3mm 3.4mm; text-align:center; background:var(--washi); break-inside:avoid; }
.kpi .n{ font-family:"Noto Sans CJK JP"; font-weight:900; font-size:20pt; color:var(--navy); line-height:1; }
.kpi .n .u{ font-size:10pt; font-weight:700; color:var(--gold-deep); }
.kpi .l{ font-family:"Noto Sans CJK JP"; font-size:8pt; color:var(--gray); margin-top:2mm; letter-spacing:.02em; }

.divider-note{ font-size:8pt; color:var(--gray); border-top:0.4pt solid var(--line); padding-top:2mm; margin-top:6mm; }
.mark-legend{ font-size:8.2pt; color:var(--gray); margin:2mm 0 4mm; }
.mark-legend b{ color:var(--navy); font-family:"Noto Sans CJK JP"; }
.tag{ display:inline-block; font-family:"Noto Sans CJK JP"; font-size:7.6pt; padding:.3mm 1.8mm; border-radius:.8mm; letter-spacing:.04em; }
.tag.ok{ background:#e4f0e9; color:var(--teal); border:0.4pt solid #b7d9c6; }
.tag.chk{ background:#f3ece0; color:var(--gold-deep); border:0.4pt solid var(--gold-light); }
"""

# =============================================================================
# 表紙
# =============================================================================
def cover():
    return """
<section class="cover">
  <div class="frame"></div><div class="frame2"></div>
  <div class="brandtop">学部別合格設計塾 THINKING</div>
  <div class="seal">完全攻略</div>
  <div class="center">
    <div class="kicker">大学別・学部別 英語入試 徹底分析</div>
    <h1>成蹊大学<br><span class="dept">経営学部</span></h1>
    <div class="rule"></div>
    <div class="subject">英語 完全攻略マニュアル</div>
    <div class="voltag">第 1 部</div>
    <div class="subtitle">出題傾向の徹底分析と合格戦略</div>
  </div>
  <div class="philo">受験は、根性じゃなく、設計。</div>
  <div class="lock">
    <div class="mark">学部別合格設計塾 THINKING</div>
    <div class="arc">GOUDOU KAISHA ARC &nbsp;/&nbsp; JUKENNO OUSAMA</div>
  </div>
</section>
"""

# =============================================================================
# 巻頭：本書の使い方 / 全体像
# =============================================================================
def intro():
    return """
<section>
  <div class="chapter-open" style="break-before:auto;">
    <div class="band">
      <div class="cno">はじめに &nbsp;/&nbsp; HOW TO USE</div>
      <div class="ctitle">この1冊で、成蹊経営の英語を「地図」にする</div>
      <div class="clead">第1部は、演習に入る前の設計図である。敵の輪郭（大問構成・設問タイプ・時間・配点）を先に固め、どこで何点をどう取るかを決めてから走り出すための巻だ。</div>
    </div>
  </div>

  <p class="lead">成蹊大学 経営学部の英語は、<strong>全問マークセンス方式・大問5題・解答50マーク</strong>で構成される（2025年度実物にて確認）。記述も和訳も英作文もない。だからこそ勝負は「書く力」ではなく、<strong>読む速度・語彙の即応・設問タイプごとの処理手順</strong>にある。ここを設計できるかどうかで、同じ実力でも得点は10点以上動く。</p>

  <div class="kpis">
    <div class="kpi"><div class="n">5<span class="u">題</span></div><div class="l">大問数（Ⅰ〜Ⅴ）</div></div>
    <div class="kpi"><div class="n">50<span class="u">マーク</span></div><div class="l">解答番号 1〜50</div></div>
    <div class="kpi"><div class="n">60<span class="u">分</span></div><div class="l">試験時間 <span class="tag chk">要照合</span></div></div>
    <div class="kpi"><div class="n">0<span class="u">問</span></div><div class="l">記述・英作文</div></div>
  </div>

  <div class="box gold">
    <div class="bt">本マニュアル・シリーズの全体像</div>
    <p><strong>第1部</strong>（本書）出題傾向分析と合格戦略／<strong>第2部</strong>語彙・語法・テーマ対策大全／<strong>第3部</strong>大問タイプ別攻略ドリル（成蹊型オリジナル問題）／<strong>第4部</strong>直前対策・完全模試。第1部で「設計」を、第2〜4部で「実装」を行う。</p>
  </div>

  <div class="mark-legend">
    本書の事実表記ルール — <b>確定</b>＝2025年度の実物問題で直接確認した構造。
    <span class="tag chk">要照合</span>＝配点・試験時間・合格最低点など、大学公式の入試要項／赤本で最終確認すべき数値。
    THINKINGは「出題事実の断定」には必ず根拠を持つ。曖昧な数値は照合欄として空けてある。
  </div>

  <div class="box warn">
    <div class="bt">著作権について（本シリーズの姿勢）</div>
    <p>本シリーズは実際の過去問の英文・設問・選択肢を一切転載しない。分析は大問構成・設問タイプ・語数感などのメタ情報に徹し、演習（第3部以降）はすべて成蹊の形式・難度・語数を再現した<strong>完全オリジナル問題</strong>で構成する。過去問そのものは必ず市販の赤本・大学公表資料で入手し、本書と併用してほしい。</p>
  </div>
</section>
"""

# =============================================================================
# 第1章：試験の骨格・出題マップ
# =============================================================================
def chapter1():
    rows = [
        ("Ⅰ", "会話文・空所補充", "Set A / Set B から不要選択肢込みで選ぶ語句補充。会話2本。", "1〜13", "13"),
        ("Ⅱ", "長文読解（総合）", "ビジネス/経済系の中〜長文。下線部言い換え・理由・整序・語形・内容一致まで1題に凝縮。", "14〜31", "18"),
        ("Ⅲ", "長文読解（英問英答）", "ビジネス論説。設問文がすべて英語。指示語・言い換え・真偽・主旨。", "32〜40", "9"),
        ("Ⅳ", "長文空所補充", "短めの英文2本。各2空所を語彙＋文脈で補充。", "41〜44", "4"),
        ("Ⅴ", "短文空所補充", "英文2本。各3空所。語法・イディオム・準動詞・時制のピンポイント。", "45〜50", "6"),
    ]
    tr = "".join(
        f'<tr><td class="c em">{esc(a)}</td><td class="em">{esc(b)}</td><td>{esc(c)}</td>'
        f'<td class="c">{esc(d)}</td><td class="c">{esc(e)}</td></tr>'
        for a, b, c, d, e in rows
    )

    map_years = ["2025", "2024", "2023", "2022", "2021"]
    map_rows = ""
    for y in map_years:
        if y == "2025":
            cells = "".join(f'<td class="c">{esc(x)}</td>' for x in
                             ["会話補充", "長文(経済)", "長文(英問英答)", "長文空所×2", "短文空所×2"])
            map_rows += f'<tr><td class="c em">2025<br><span class="tag ok">確定</span></td>{cells}</tr>'
        else:
            cells = "".join('<td class="c" style="color:#b9b1a0;">照合欄</td>' for _ in range(5))
            map_rows += f'<tr><td class="c em">{y}</td>{cells}</tr>'

    return f"""
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 1</div>
      <div class="ctitle">試験の骨格 ― 5大問・50マークの全体地図</div>
      <div class="clead">まず「どんな問題が・どの順で・何マーク」出るかを頭に入れる。ここが曖昧なままだと、時間配分も得点設計も机上の空論になる。</div>
    </div>
  </div>

  <h2 class="sec">1-1 大問マップ（2025年度・確定）</h2>
  <p class="lead">2025年度の実物冊子（18ページ・全問マーク）で確認した構成。長文2題（Ⅱ・Ⅲ）で全50マーク中<strong>27マーク</strong>を占め、ここが得点と時間の主戦場になる。</p>
  <table class="data">
    <tr><th style="width:8%">大問</th><th style="width:24%">タイプ</th><th>内容の骨子</th><th style="width:13%" class="c">解答番号</th><th style="width:10%" class="c">マーク</th></tr>
    {tr}
  </table>
  <p class="tblnote">※ マーク数は解答番号ベース。Ⅲの問7は2マーク（2つ選ぶ）を含む。配点（1マークあたりの点数）は大学非公表のため、本書では「マーク数の重み」で戦略を組む。</p>

  <div class="box navy">
    <div class="bt">この配分から読める戦略の芯</div>
    <p>Ⅱ＋Ⅲの長文で<strong>過半（27/50）</strong>。ここを落とすと合格ラインに届かない。一方でⅣ（4）＋Ⅴ（6）の空所補充<strong>10マーク</strong>は語法・語彙の知識で短時間・高確率に取れる「取り所」。長文で粘る時間を作るために、まずⅣ・ⅤとⅠを速く確実に処理する設計が効く。</p>
  </div>

  <h2 class="sec">1-2 出題マップ（年度×大問／照合テンプレ）</h2>
  <p class="lead">確定しているのは2025年度のみ。過年度は<strong>赤本で自分の手で埋める</strong>ことで、傾向の「安定度」を体感できる。埋めながら「毎年出る型」と「揺れる型」を色分けせよ。</p>
  <table class="data">
    <tr><th style="width:14%" class="c">年度</th><th class="c">大問Ⅰ</th><th class="c">大問Ⅱ</th><th class="c">大問Ⅲ</th><th class="c">大問Ⅳ</th><th class="c">大問Ⅴ</th></tr>
    {map_rows}
  </table>
  <p class="tblnote">※ 「照合欄」は赤本で確認して記入する欄。方式（A方式）・実施日程により英語問題が共通か学部個別かは大学要項で要確認。年度で大問数が増減する可能性もあるため、鵜呑みにせず現物で照合すること。</p>

  <div class="box gold">
    <div class="bt">照合チェック（大学公式・赤本で埋める）</div>
    <p><span class="sans">□</span> A方式 英語の試験時間（本書は60分と想定・要確認）　<span class="sans">□</span> 英語の満点・他教科との配点比　<span class="sans">□</span> 経営学部の英語が共通問題か個別問題か　<span class="sans">□</span> 合格最低点／得点率の目安　<span class="sans">□</span> E方式の英語配点（英語重視型）</p>
  </div>

  <h2 class="sec">1-3 設問タイプ×大問 早見マトリクス</h2>
  <p class="lead">第2章で扱う設問タイプA〜Gが、どの大問に現れるかの対応表（●＝2025年度で出題を確認）。1つの型が複数の大問にまたがること、大問Ⅱが最も多くの型を含む「総合問題」であることが一目で分かる。</p>
  <table class="data">
    <tr><th style="width:34%">設問タイプ</th><th class="c">Ⅰ 会話</th><th class="c">Ⅱ 総合長文</th><th class="c">Ⅲ 英問英答</th><th class="c">Ⅳ 長文空所</th><th class="c">Ⅴ 短文空所</th></tr>
    <tr><td class="em">A 会話Set選択補充</td><td class="c">●</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c"></td></tr>
    <tr><td class="em">B 下線部言い換え</td><td class="c"></td><td class="c">●</td><td class="c">●</td><td class="c"></td><td class="c"></td></tr>
    <tr><td class="em">C 内容真偽・不一致</td><td class="c"></td><td class="c">●</td><td class="c">●</td><td class="c"></td><td class="c"></td></tr>
    <tr><td class="em">D 情報整序・時系列</td><td class="c"></td><td class="c">●</td><td class="c"></td><td class="c"></td><td class="c"></td></tr>
    <tr><td class="em">E 語法・文法融合</td><td class="c"></td><td class="c">●</td><td class="c"></td><td class="c"></td><td class="c">●</td></tr>
    <tr><td class="em">F 英問英答・主旨把握</td><td class="c"></td><td class="c"></td><td class="c">●</td><td class="c"></td><td class="c"></td></tr>
    <tr><td class="em">G 空所補充（語彙＋文選択）</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c">●</td><td class="c"></td></tr>
  </table>
  <p class="tblnote">※ Ⅰ・Ⅴも広義の空所補充だが、解法が固有のため独立の型（A・E）として扱う。●は2025年度実物で確認した出題。過年度で型の出入りがあれば赤本照合時に加筆する。</p>

  <div class="box navy">
    <div class="bt">マトリクスの読み方</div>
    <p>横に広い型（B・C・E）は<strong>複数大問で回収できる</strong>＝対策の費用対効果が高い。とくにB（言い換え＝語彙）とC（真偽＝設問精読）は、伸ばせばⅡ・Ⅲ両方に効く。第2部・第3部はこの高レバレッジ順に鍛える設計になっている。</p>
  </div>
</section>
"""

# =============================================================================
# 第2章：設問タイプ分類（タイプA〜G）
# =============================================================================
def type_card(badge, name, where, desc, steps):
    st = "".join(f"<li>{esc(s)}</li>" for s in steps)
    return f"""
  <div class="tcard">
    <div class="hd"><span class="badge">{esc(badge)}</span><span class="tname">{esc(name)}</span><span class="where">{esc(where)}</span></div>
    <div class="bd">
      <p>{desc}</p>
      <div class="howto"><span class="lbl">解法手順</span>
        <ol class="steps">{st}</ol>
      </div>
    </div>
  </div>
"""

def chapter2():
    cards = ""
    cards += type_card("A", "会話文 Set選択補充", "大問Ⅰ",
        "2つの会話に散らばる空所を、<strong>Set A / Set B の語群</strong>から選ぶ。番号は一度ずつ、各Setに不要選択肢が2つ混じる。単語・短語句レベルの語彙＋会話の流れ＋コロケーションで解く。",
        ["先に選択肢群に品詞タグを振る（名詞/動詞/形容詞を仕分け）。",
         "空所の前後の文法枠（be動詞の後→形容詞/-ing、他動詞の後→名詞 等）で候補を絞る。",
         "会話の論理（賛否・因果・言い換え）で意味を確定。確実なものから埋め、不要選択肢2つを最後に炙り出す。",
         "1つのミスが玉突きで連鎖するため、確信度の高い空所を軸に固定する。"])
    cards += type_card("B", "下線部 言い換え（同義語）", "大問Ⅱ 問1ほか",
        "下線部の語句と<strong>最も意味が近い1語/句</strong>を選ぶ。2025ではspectacular→wonderful、struck on→came up with、massive→huge、sprung up→emerged、acquired→obtained など7問集中。<strong>純粋な語彙力が即得点</strong>になる典型。",
        ["まず文脈を見ずに自分の語彙知識で同義語を想起（第2部の同義語テーブルが直結）。",
         "多義語・句動詞は文脈で語義を確定（struckは『殴る』ではなく『思いつく』）。",
         "選択肢に紛らわしい類義語がある場合、下線部を選択肢で置換して文が成立するか確認。",
         "ここは考え込まず即断即決。時間貯金の最大の源泉。"])
    cards += type_card("C", "内容真偽・不一致（NOT型）", "大問Ⅱ 問3 / Ⅲ 問3〜6",
        "「本文に合致<strong>しない</strong>もの」「trueでないもの」を選ぶ。設問の否定語（not / しない）を見落とすと全滅する要注意タイプ。",
        ["設問文の『合致しない/NOT』に必ず印をつける（読み違い事故の最多発地帯）。",
         "各選択肢のキーワードを本文で逐一照合。書いていない=不一致とは限らず、本文と矛盾する記述を探す。",
         "3つが本文で確認できたら、残りが答え。消去法を明示的に使う。"])
    cards += type_card("D", "情報整序・時系列並べ替え", "大問Ⅱ 問4・問6",
        "川の上流→下流の順、出来事A〜Dの時系列など、本文の情報を<strong>並べ替える</strong>。段落単位の事実関係を正確に追えるかを問う。",
        ["該当箇所を本文から抜き、年号・順序を示す語（until, during, shortly thereafter, once）に印。",
         "選択肢の並びを1つずつ本文と突き合わせ、最初と最後を先に確定して挟み撃ち。",
         "地名・固有名詞は図に矢印で書き出すと誤読が激減する。"])
    cards += type_card("E", "語法・文法融合", "大問Ⅱ 問5 / 大問Ⅴ",
        "読解の中に埋め込まれた文法。2025ではlay/lie/leadの<strong>活用形</strong>判別、Ⅴではat ease・分詞・仮定/時制（were）・準動詞（原形）。語彙問題の顔をした文法問題。",
        ["自動詞lie(lay-lain)と他動詞lay(laid-laid)など、紛らわしいペアは第2部の一覧で潰しておく。",
         "空所の直前直後だけでなく主語・時制・仮定法の有無まで見て決定。",
         "Ⅴは短文なので全訳せず、狙われている文法ポイントを一撃で判定して即マーク。"])
    cards += type_card("F", "英問英答・主旨把握", "大問Ⅲ",
        "設問文が<strong>すべて英語</strong>。指示語の特定、下線部の言い換え、内容真偽、そして『overall content（主旨）』の選択まで。英語で問われる分の負荷が成蹊Ⅲの山場。",
        ["設問英文を先に読み、何を探すか（who/what/why/指示語）を確定してから本文に戻る。",
         "指示語問題は直前文へ。true/NOT trueは選択肢のキーワード照合。",
         "主旨問題は『言い過ぎ（too broad/narrow）』『本文にない要素』を切る。筆者の主張（SFは未来予測でなく前提の問い直し）に沿う1つを残す。"])
    cards += type_card("G", "空所補充（語彙＋文選択）", "大問Ⅳ",
        "短め英文の空所に、<strong>1語（quit/value等）</strong>または<strong>1文（There is no magical fix 等）</strong>を補う。段落の論理展開をつかめば取れる、堅実な得点源。",
        ["空所前後の接続関係（逆接but/因果so/例示）を先に把握。",
         "語彙空所はコロケーションと文脈、文選択空所は前後との論理整合で判断。",
         "各選択肢を入れて読み、話の筋が最も自然に通る1つを選ぶ。"])

    return f"""
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 2</div>
      <div class="ctitle">設問タイプ分類 ― A〜Gの型と解法手順</div>
      <div class="clead">成蹊経営の英語は、見た目は5大問だが、中身は7つの設問タイプに分解できる。型ごとに手順を決めておけば、本番は「考える」前に「作業」で処理できる。</div>
    </div>
  </div>

  <p class="lead">以下の7タイプは、2025年度実物から抽出した成蹊経営の設問の全体像である。第3部のオリジナル演習は、この型に対応する形で作られる。まずは「自分がどの型で失点しやすいか」を意識しながら読め。</p>

  {cards}

  <div class="box ok">
    <div class="bt">型で戦うと何が変わるか</div>
    <p>同じ問題でも、型を意識しない受験生は毎回ゼロから考える。型を持つ受験生は「これはB＝即断」「これはC＝否定語に印」と<strong>手が先に動く</strong>。60分・50マークの試験では、この差がそのまま得点差になる。</p>
  </div>

  <h2 class="sec">2-2 頻出テーマの地図 ― 何を読み慣れておくか</h2>
  <p class="lead">成蹊経営の長文は、経営学部らしく<strong>ビジネス/経済の硬派な論説</strong>が核にある。2025年度も、観光開発を題材にした経営戦略（垂直統合）と、意思決定論としてのSF論（HBR）が並んだ。背景知識があるほど読解は速くなる。テーマを象限で押さえておけ。</p>
  <table class="data">
    <tr><th style="width:20%">象限</th><th style="width:30%">2025での該当</th><th>語彙・読解の性格</th></tr>
    <tr><td class="em">ビジネス／経済</td><td>Ⅱ 観光開発と垂直統合（経営戦略テキスト）／Ⅲ 経営者とSF（HBR）</td><td>抽象度が高く論理展開が命。因果・対比の接続語と経営語彙で読み進める。得点の主戦場。</td></tr>
    <tr><td class="em">社会／教育</td><td>Ⅳ(1) 音楽教育と継続（NYT）</td><td>主張＋根拠の型。筆者の結論を掴めば空所も見える。</td></tr>
    <tr><td class="em">文化／歴史</td><td>Ⅳ(2) 英国の芝生史</td><td>時系列と因果。背景が身近でなくても構造で読む。</td></tr>
    <tr><td class="em">科学／心理</td><td>Ⅴ(1) アニマルセラピー／Ⅴ(2) 鳥肌の科学</td><td>平易な説明文。語法・時制の正確さで確実に取る短文枠。</td></tr>
  </table>
  <p class="tblnote">※ テーマは年度で変わるが、「ビジネス/経済の硬派長文＋社会・科学の平易文」という硬軟の組み合わせは傾向として押さえる価値がある。過年度のテーマは赤本で確認し、頻出象限を自分で更新せよ。</p>

  <h3 class="sub">語彙の水準 ― 「言い換え」が示す難度帯</h3>
  <p>大問Ⅱの下線部言い換え（タイプB）は、成蹊が要求する語彙水準の指標になる。2025では、句動詞や多義語を<strong>文脈に応じた同義語</strong>に置き換える力が問われた（例：ある動詞句が「思いつく」の意で使われ、come up with が同義になる／massive＝huge／sprung up＝emerged といった水準）。単語帳の第一義暗記だけでは足りず、<strong>類義語のネットワークと句動詞の語義</strong>まで踏み込む必要がある。ここは第2部の同義語テーブルで体系的に固める。</p>

  <div class="box gold">
    <div class="bt">テーマ地図の使い方</div>
    <p>ビジネス/経済の長文に苦手意識があるなら、日頃から経営・経済の平易な英文記事に触れて<strong>背景スキーマ</strong>を作っておく。内容を知っている話題は、同じ語彙力でも段違いに速く正確に読める。これも「設計」の一部だ。</p>
  </div>
</section>
"""

# =============================================================================
# 第3章：時間配分戦略
# =============================================================================
def chapter3():
    tl = [
        ("0-3分", "全体スキャン", "冊子をめくり大問構成と長文の量を確認。解く順序を決める（下記の推奨は Ⅴ→Ⅳ→Ⅰ→Ⅱ→Ⅲ）。"),
        ("3-9分", "大問Ⅴ（6）", "短文空所。語法・イディオムを即決。1問1分弱。ここで頭を英語モードに温める。"),
        ("9-15分", "大問Ⅳ（4）", "短め長文の空所補充。論理接続を見て確実に。"),
        ("15-24分", "大問Ⅰ（13）", "会話文Set補充。品詞仕分け→確信空所から固定。不要選択肢2つを最後に確認。"),
        ("24-42分", "大問Ⅱ（18）", "本命の総合長文。下線部言い換え7問を先に回収し、整序・真偽・語形へ。"),
        ("42-57分", "大問Ⅲ（9）", "英問英答。設問英文を先読み→本文照合→主旨は最後。"),
        ("57-60分", "見直し・マーク確認", "マークずれ・空欄・Set重複・NOT見落としを総点検。"),
    ]
    rows = "".join(
        f'<div class="row"><div class="t">{esc(t)}</div><div class="bar"><span class="nm">{esc(n)}</span>'
        f'<span class="ds"> ― {esc(d)}</span></div></div>'
        for t, n, d in tl
    )
    return f"""
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 3</div>
      <div class="ctitle">時間配分戦略 ― 60分を「取り所」から設計する</div>
      <div class="clead">長文から解き始めて時間を溶かすのが最大の敗因。短く確実な大問で得点と勢いを先に確保し、長文に「粘れる時間」を残す。</div>
    </div>
  </div>

  <p class="lead">下は<strong>試験時間60分</strong>（<span class="tag chk">要照合</span>）を前提とした推奨タイムテーブル。順序は「速く確実に取れる大問（Ⅴ・Ⅳ・Ⅰ）を先、時間を食う長文（Ⅱ・Ⅲ）を後」に組む。実際の時間が異なる場合は、各ブロックを比例配分すれば同じ設計が使える。</p>

  <div class="tl">{rows}</div>

  <div class="box warn">
    <div class="bt">やってはいけない時間の使い方</div>
    <p>①冊子順（Ⅰ→…→Ⅴ）に律儀に解き、Ⅱの長文で時間を溶かしてⅤの語法6マークを落とす。②下線部言い換えで悩みすぎる（Bは即断が原則）。③マーク確認の3分を確保せず、ずれに気づかず全滅。<strong>順序と締め切りを先に決めておけば、この3つは起きない。</strong></p>
  </div>

  <div class="box ok">
    <div class="bt">「取り所」を先に取る意味</div>
    <p>Ⅴ（6）＋Ⅳ（4）＋Ⅰ（13）で<strong>23マーク</strong>。この前半23マークを高精度で取り切れば、残り37分を長文27マークに集中投下できる。前半でリズムと得点を作ることが、後半の読解の質を上げる。</p>
  </div>
</section>
"""

# =============================================================================
# 第4章：失敗パターン TOP3
# =============================================================================
def chapter4():
    return """
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 4</div>
      <div class="ctitle">落ちる受験生の失敗パターン TOP3</div>
      <div class="clead">実力不足で落ちるのではない。多くは「設計の欠如」で、取れたはずの点を自分で捨てて落ちる。先回りして潰す。</div>
    </div>
  </div>

  <div class="box warn">
    <div class="bt">失敗①　冊子の順番どおりに解いて、長文で時間切れ</div>
    <p>Ⅰから律儀に解き、Ⅱの経済長文で読み込みすぎる。気づけば残り10分でⅢの英問英答とⅤの語法が手つかず ― これが最頻の落ち方。<strong>対策：</strong>解く順序を『Ⅴ→Ⅳ→Ⅰ→Ⅱ→Ⅲ』に固定し、各大問に締め切り時刻を割り当てる（第3章）。短く確実な大問を先に回収する。</p>
  </div>

  <div class="box warn">
    <div class="bt">失敗②　語彙不足を「読解力」でごまかそうとする</div>
    <p>Ⅱの下線部言い換え7問（14〜20）は語彙を知っていれば即答、知らなければ文脈から推測に何十秒もかかる。ここで消耗すると長文本体を読む時間が消える。<strong>対策：</strong>第2部の頻出テーマ語彙・同義語テーブルを先に固める。言い換え問題は『知識で秒殺する枠』と割り切る。</p>
  </div>

  <div class="box warn">
    <div class="bt">失敗③　設問の指示（NOT・2つ選ぶ・英語の問い）を読み飛ばす</div>
    <p>『合致しないもの』を合致するもので選ぶ、『2つ選ぶ』を1つで止める（Ⅱ問11・Ⅲ問7）、英問英答の設問英文を誤読する ― どれも実力と無関係な取りこぼし。<strong>対策：</strong>設問文の否定語・個数指定・疑問詞に必ず印をつける習慣を、演習段階から徹底する。</p>
  </div>

  <div class="box ok">
    <div class="bt">3つに共通する処方箋</div>
    <p>失敗はすべて『本番で初めて考える』ことから生まれる。順序・締め切り・設問の読み方を<strong>演習のうちに手順化</strong>しておけば、本番は作業として処理できる。これが「根性ではなく設計」の具体である。</p>
  </div>
</section>
"""

# =============================================================================
# 第5章：合格点設計
# =============================================================================
def chapter5():
    # 得点設計テーブル（マーク数ベースの目標設計。配点非公表のためマーク正答率で設計）
    rows = [
        ("Ⅴ 短文空所", "6", "5", "83%", "語法・イディオムの知識で満点近くを狙う最優先の得点源。"),
        ("Ⅳ 長文空所", "4", "3", "75%", "論理接続で堅実に。落としても1つまで。"),
        ("Ⅰ 会話補充", "13", "10", "77%", "確信空所を固め、連鎖ミスを防ぐ。3ミス以内。"),
        ("Ⅱ 総合長文", "18", "12", "67%", "言い換え7問を先取り。整序・真偽で稼ぐ。"),
        ("Ⅲ 英問英答", "9", "5", "56%", "設問英文の負荷が高い。主旨と真偽を確実に。"),
    ]
    tot_m, tot_g = 50, 35
    tr = "".join(
        f'<tr><td class="em">{esc(a)}</td><td class="c">{esc(b)}</td><td class="c em">{esc(c)}</td>'
        f'<td class="c">{esc(d)}</td><td>{esc(e)}</td></tr>'
        for a, b, c, d, e in rows
    )
    return f"""
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 5</div>
      <div class="ctitle">合格点設計 ― 目標得点率を大問別に分解する</div>
      <div class="clead">「英語で何割取るか」を決め、それを大問別の正答数に落とし込む。ぼんやり全部を頑張るのではなく、どこで取り・どこは捨てるかを数字で決める。</div>
    </div>
  </div>

  <p class="lead">成蹊の配点（1マークあたりの点数）は非公表のため、本書では<strong>マーク正答率</strong>で設計する。合格ラインは方式・年度で動くが、私大英語の一つの目安として<strong>7割（50マーク中35マーク）</strong>を第一目標に置く。以下はその内訳例だ。</p>

  <table class="data">
    <tr><th style="width:22%">大問</th><th style="width:10%" class="c">マーク</th><th style="width:14%" class="c">目標正答</th><th style="width:12%" class="c">正答率</th><th>取り方の方針</th></tr>
    {tr}
    <tr style="background:var(--washi-2);"><td class="em">合計</td><td class="c em">{tot_m}</td><td class="c em">{tot_g}</td><td class="c em">70%</td><td class="em">前半（Ⅴ・Ⅳ・Ⅰ）で18/23、長文で17/27。</td></tr>
  </table>
  <p class="tblnote">※ 目標正答は「7割ライン到達」の一例。実際の合格最低点・得点率は大学公表資料／赤本で確認し、下の照合欄で自分の目標に置き換えること。</p>

  <div class="box gold">
    <div class="bt">合格点 逆算シート（照合して自分の数字に）</div>
    <p><span class="sans">□</span> 志望方式（A方式／E方式）＝ ______　<span class="sans">□</span> 英語の満点 ＝ ______ 点<br>
    <span class="sans">□</span> 合格最低点（赤本）＝ ______ 点　→　<span class="sans">□</span> 英語の目標得点率 ＝ ______ ％<br>
    <span class="sans">□</span> それを50マークに換算 ＝ 目標正答 ______ マーク　→　大問別に配分し直す</p>
  </div>

  <div class="box navy">
    <div class="bt">「捨てる勇気」も設計のうち</div>
    <p>Ⅲの英問英答は負荷が高い。ここを満点狙いで粘るより、<strong>Ⅴ・Ⅳ・Ⅰ・Ⅱで確実に積む</strong>方が総得点は伸びる。全問正解を狙わず、7割の最短ルートを引く。これが設計思想である。</p>
  </div>
</section>
"""

# =============================================================================
# 第6章：学習ロードマップ
# =============================================================================
def chapter6():
    phases = [
        ("第1期：土台（〜夏前）", "BUILD THE BASE", [
            "単語・熟語：第2部の頻出テーマ語彙（ビジネス/経済/社会/科学）を回す。同義語テーブルで『言い換え耐性』を作る。",
            "文法：lie/lay・時制・仮定法・準動詞など、Ⅴ・Ⅱ問5で狙われる分野を一巡。",
            "1日20分の速読で、英文を『戻り読みせず』処理する型を作る。",
        ]),
        ("第2期：型の習得（夏〜秋）", "MASTER THE PATTERNS", [
            "第3部のタイプ別ドリルで、設問タイプA〜Gごとの解法手順を体に入れる。",
            "下線部言い換え・英問英答を『秒殺枠／精読枠』に仕分けする感覚を養う。",
            "大問単位で時間を計り、締め切り厳守で解く訓練を始める。",
        ]),
        ("第3期：通し演習（秋〜冬）", "RUN FULL SETS", [
            "第4部の完全模試を本番と同一時間で通す。解く順序（Ⅴ→Ⅳ→Ⅰ→Ⅱ→Ⅲ）を固定して検証。",
            "赤本で過年度を解き、出題マップの照合欄を埋めて傾向の安定度を確認。",
            "毎回、失点を『知識不足／時間切れ／設問読み違い』の3つに分類して記録する。",
        ]),
        ("第4期：直前（1月〜本番）", "FINAL TUNING", [
            "新しい問題集に手を広げず、既習の語彙・同義語・文法の穴だけを埋める。",
            "直前チェックリスト（第2部）で頻出語法を最終確認。",
            "本番の時間配分・見直し手順を紙1枚に書き、当日それだけを見る。",
        ]),
    ]
    pr = ""
    for title, wave, items in phases:
        lis = "".join(f"<li>{esc(x)}</li>" for x in items)
        pr += f'<div class="phase"><span class="ph">{esc(title)}</span> <span class="pw">{esc(wave)}</span><ul>{lis}</ul></div>'

    return f"""
<section>
  <div class="chapter-open">
    <div class="band">
      <div class="cno">CHAPTER 6</div>
      <div class="ctitle">3本柱の学習ロードマップ ― 現在期から直前まで</div>
      <div class="clead">語彙・型・通し演習の3本柱を、時期で積み上げる。今どの期にいて、次に何を積むかを、この地図で常に確認する。</div>
    </div>
  </div>

  <p class="lead">柱は3つ ― <strong>①語彙/文法の土台</strong>、<strong>②設問タイプ別の型</strong>、<strong>③本番想定の通し演習</strong>。この順に厚くしていくのが最短経路だ。時期区分は目安。自分の現在地から始めればよい。</p>

  {pr}

  <div class="box ok">
    <div class="bt">迷ったら戻る一文</div>
    <p>量をこなすことが目的化したら立ち止まれ。<strong>成蹊経営の英語で7割を取るために、いま自分に足りない1つは何か。</strong>語彙か、型か、時間管理か。それを1つ潰すのが今日の勉強だ。</p>
  </div>

  <h2 class="sec">第1部 総まとめ ― 設計チェックリスト</h2>
  <ul class="check">
    <li>大問構成（Ⅰ会話／Ⅱ総合長文／Ⅲ英問英答／Ⅳ長文空所／Ⅴ短文空所・全50マーク）を暗記した</li>
    <li>設問タイプA〜Gと、それぞれの解法手順を言える</li>
    <li>解く順序（Ⅴ→Ⅳ→Ⅰ→Ⅱ→Ⅲ）と各大問の締め切り時刻を決めた</li>
    <li>失敗パターンTOP3（順番どおり／語彙ごまかし／設問読み飛ばし）を回避する手を持っている</li>
    <li>目標得点率を決め、大問別の目標正答マーク数に分解した</li>
    <li>赤本で出題マップの照合欄と合格点逆算シートを埋めた</li>
    <li>自分が今どの学習期にいて、次に積む1本柱がどれか分かっている</li>
  </ul>

  <div class="box gold">
    <div class="bt">次巻へ ― 第2部 語彙・語法・テーマ対策大全</div>
    <p>本書で引いた設計図を、次は「実装」に移す。第2部では、成蹊経営の頻出テーマ（ビジネス/経済/社会/科学）別語彙、Ⅱの下線部言い換えに直結する同義語テーブル、Ⅴ・Ⅱ問5の語法・文法の頻出ランキングを、実戦で使える形で揃える。設計ができたら、次は弾を込める番だ。</p>
  </div>

  <div class="divider-note">
    学部別合格設計塾THINKING（合同会社ARC）／成蹊大学 経営学部 英語 完全攻略マニュアル 第1部。
    本書の分析は2025年度一般選抜「外国語(英語)」の構造に基づく。配点・試験時間・合格最低点は大学公表の入試要項および赤本で最終照合のこと。実際の過去問英文・設問・選択肢は転載していない。
  </div>
</section>
"""

# =============================================================================
# 組み立て
# =============================================================================
def build():
    html = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<style>{CSS}</style></head><body>
{cover()}
{intro()}
{chapter1()}
{chapter2()}
{chapter3()}
{chapter4()}
{chapter5()}
{chapter6()}
</body></html>"""
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    HTML(string=html).write_pdf(os.path.abspath(OUT))
    print("WROTE", os.path.abspath(OUT))

if __name__ == "__main__":
    build()
