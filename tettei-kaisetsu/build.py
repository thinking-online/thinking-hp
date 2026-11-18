#!/usr/bin/env python3
"""THINKINGの徹底解説シリーズ  PDF ビルダー

  data/<univ>_<year>.py（BOOK 辞書） → HTML → PDF（WeasyPrint）

使い方:
  python3 build.py sample/sample_dummy.py                 # 見本（ダミー）
  python3 build.py waseda-shogaku_2026                     # 中身置き場の <id>.py を使う
  python3 build.py waseda-shogaku_2026 --out x.pdf --html  # HTML も残す
  python3 build.py waseda-shogaku_2026 --png /path/to/dir  # ページ画像も出す（pdftoppm）

中身（解説・全訳・正解を含む data）はリポジトリに置かない。
このリポジトリは Netlify で publish="." のため、置いた物はすべてサイトに公開される。
中身置き場は --content-dir か環境変数 TETTEI_CONTENT_DIR で指定（既定は DEFAULT_CONTENT_DIR）。
PDF の既定の出力先も <中身置き場>/out/。

ビルド後に必ず検査を行い、1 つでも ERROR があれば終了コード 1 を返す:
  - 必要フォント（Noto Sans/Serif CJK JP, Liberation Serif）が入っているか
  - 本文の全文字がフォントに収録されているか（豆腐・代替フォント落ちの防止）
  - PDF の全フォントが埋め込まれているか、想定外のフォントが混ざっていないか（pdffonts）
  - PDF から抜いた文字に U+FFFD（文字化け）がないか、見出し文字列が読み戻せるか（pdftotext）
  - 禁止語（他社のシリーズ名）が入っていないか
  - 英文の載せすぎ（本文転載）になっていないか（中身の形 v2）：
      引用 1 つは原則 1 文（目安 45 語。超えたら WARN、80 語超は ERROR）
      大問ごとの英語（根拠の文・下線部・選択肢・精読・[[...]]。同じ文の重複は 1 回）が
      本文語数（大問の "body_words"）の約 3 割以内（30% 超で WARN、35% 超で ERROR）
  - 大問の出典（"source"）があるか（無ければ ERROR）
  - 欠け：負の text-indent の中の背景・枠つき inline-block、本文領域からはみ出した背景・枠

本文の記法（data 内の文字列で使える）:
  **太字**   __下線（設問の下線部の引用）__   [[英語の語句・短い引用]]
  根拠の文（evidence）の英文・訳の中の **…** は「決め手の語句」として蛍光ペンで強調される
  【札】 は自動で色付きの太字になる（推定＝金、罠・注意・誤答＝朱、正解・根拠＝緑、ほか＝紺）

見た目（templates/style.css）：Web 版解説と同じ配色（紺＋金・緑・朱）。地は白で、色は
見出しの帯・設問カードの左線・札の文字色・正解の強調・表の見出し行など要所だけに使う。
欠けの防止のため、負の text-indent と、背景・枠つきの inline-block は使わない（check_clipping が検査）。
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSS_PATH = HERE / "templates" / "style.css"
# 中身（data/<univ>_<year>.py）の置き場所。リポジトリの外に置くこと。
DEFAULT_CONTENT_DIR = Path(
    "/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad/content"
)

SERIES_NAME = "THINKINGの徹底解説シリーズ"
COVER_TOP_LINE = "学部別・逆算戦略設計 THINKING"

REQUIRED_FONTS = ["Noto Sans CJK JP", "Noto Serif CJK JP", "Liberation Serif"]
# PDF に出てきてよいフォント名（サブセット接頭辞を除いた名前の一部）
ALLOWED_PDF_FONTS = ["NotoSansCJK", "NotoSerifCJK", "LiberationSerif"]
BANNED_WORDS = ["赤本", "青本", "黒本", "緑本", "教学社", "駿台文庫", "河合出版", "東京書籍"]
# 英語の量（中身の形 v2）。本文は載せず、引用は根拠の文・下線部・選択肢・精読だけ。
QUOTE_WARN_WORDS = 45         # 引用 1 つは原則 1 文。目安 45 語を超えたら WARN
QUOTE_MAX_WORDS = 80          # これを超える引用は段落の転載とみなして ERROR
QUOTE_WARN_SENTENCES = 3      # 引用 1 つに 4 文以上（根拠の文は前後 1 文まで）→ WARN
EN_RATIO_WARN = 0.30          # 大問の英語 ÷ 本文語数（body_words）。約 3 割以内
EN_RATIO_MAX = 0.35           # これを超えたら ERROR（本文の通し掲載に近い）
FALLBACK_MAX_EN_WORDS = 260   # body_words が無い大問の上限（旧来の絶対値。超えたら ERROR）
EN_WORD_RE = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)?")

MARU = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚"


# ---------------------------------------------------------------- 記法
def md(text) -> str:
    """data の文字列 → インライン HTML。リストなら段落の並びにする。"""
    if text is None:
        return ""
    if isinstance(text, (list, tuple)):
        return "".join(f"<p>{md(t)}</p>" for t in text)
    s = html.escape(str(text), quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"__(.+?)__", r"<u>\1</u>", s)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="en">\1</span>', s)
    s = re.sub(r"【([^】]{1,20})】", lambda m: f'<span class="tag {tag_class(m.group(1))}">【{m.group(1)}】</span>', s)
    return s


# 札（【…】）の色。札は inline の色付き太字（inline-block や枠は使わない＝欠けの原因になるため）
TAG_COLORS = [
    (("推定",), "t-gold"),
    (("罠", "注意", "減点", "誤答", "NG", "ダメ"), "t-verm"),
    (("正解", "根拠", "答案例", "訳"), "t-teal"),
]


def tag_class(label: str) -> str:
    for keys, cls in TAG_COLORS:
        if any(k in label for k in keys):
            return cls
    return "t-navy"


def callout(kind: str, label: str, inner: str, extra: str = "") -> str:
    """色付きの囲み（薄い背景＋左の色線）。札はブロックの見出し行として置く。
    kind: navy / gold / teal / verm / blue"""
    lab = f'<div class="co-lbl">{md(label)}</div>' if label else ""
    return f'<div class="co co-{kind} {extra}">{lab}{inner}</div>'


def paras(text) -> str:
    if isinstance(text, (list, tuple)):
        return md(text)
    return f"<p>{md(text)}</p>" if text else ""


def mark_sno(h: str) -> str:
    """全訳の文番号（①②…）を金の太字にする（md 済みの HTML に掛ける）。"""
    return re.sub(f"([{MARU}])", r'<span class="sn">\1</span>', h)


def maru(n: int) -> str:
    return MARU[n - 1] if 1 <= n <= len(MARU) else f"({n})"


def css_str(s) -> str:
    return str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def esc(s) -> str:
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- 部品
def table(head, rows, cls="", col_cls=None) -> str:
    """head: 見出しのリスト / rows: セル（記法文字列）のリストのリスト"""
    col_cls = col_cls or []
    th = "".join(
        f'<th class="{col_cls[i] if i < len(col_cls) else ""}">{md(h)}</th>' for i, h in enumerate(head)
    )
    body = []
    for r in rows:
        tds = "".join(
            f'<td class="{col_cls[i] if i < len(col_cls) else ""}">{md(c)}</td>' for i, c in enumerate(r)
        )
        body.append(f"<tr>{tds}</tr>")
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def masu(chars: int, text: str = "", per_row: int = 20, caption: str = "", example: bool = False) -> str:
    """字数指定の記述用マス目。text を入れると答案例として 1 字 1 マスで埋める。"""
    rows = -(-chars // per_row)
    cells = list(text or "")
    out = [f'<div class="masu-wrap{" example" if example else ""}">']
    if caption:
        out.append(f'<div class="masu-caption">{md(caption)}</div>')
    out.append('<table class="masu"><tbody>')
    for r in range(rows):
        tds = []
        for c in range(per_row):
            i = r * per_row + c
            ch = esc(cells[i]) if i < len(cells) else ""
            cls = ' class="dead"' if i >= chars else ""
            tds.append(f"<td{cls}>{ch}</td>")
        upto = min((r + 1) * per_row, chars)
        tds.append(f'<td class="count">{upto}</td>')
        out.append(f"<tr>{''.join(tds)}</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


MARK_CLASS = {"S": "m-s", "V": "m-v", "O": "m-o", "C": "m-c", "M": "m-m"}


def mark_class(tok: str) -> str:
    """S / V / O / C / M（O1・S′ なども）なら色、それ以外（関係詞・接続詞など）は灰。"""
    t = tok.strip("()（）")
    return MARK_CLASS.get(t[:1], "m-x") if t and len(t) <= 3 else "m-x"


def mark_html(mark: str) -> str:
    """働きの記号を色分け（S＝紺、V＝朱、O・C＝緑、M＝金、その他＝灰）。inline の色付き太字のみ。"""
    out = []
    for tok in str(mark or "").split():
        out.append(f'<span class="mk {mark_class(tok)}">{esc(tok)}</span>')
    return " ".join(out)


def parse_table(lines) -> str:
    """精読の構文の図：1 行 = 英文の区切り / 働き / 訳。level で従属の深さを字下げ。"""
    rows = []
    for ln in lines:
        lv = int(ln.get("level", 0))
        lvc = f" lv{lv}" if lv else ""
        mk = str(ln.get("mark", "")).split()
        role = mark_class(mk[0]) if mk else "m-x"
        rows.append(
            f'<tr class="row-{role}"><td class="en-chunk{lvc}">{md(ln["en"])}</td>'
            f'<td class="mark">{mark_html(ln.get("mark", ""))}</td>'
            f'<td class="ja-chunk{lvc}">{md(ln["ja"])}</td></tr>'
        )
    return (
        '<table class="parse"><thead><tr><th>英文の区切り</th><th class="c">働き</th><th>訳</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )


# ---------------------------------------------------------------- 章
def render_cover(b) -> str:
    fac = b.get("faculty", "")
    return f"""
<section class="cover">
  <div class="c-top">{esc(COVER_TOP_LINE)}</div>
  <div class="c-title">
    <div class="c-univ">{esc(b['univ'])}</div>
    {f'<div class="c-faculty">{esc(fac)}</div>' if fac else ''}
    <div class="c-year">{esc(b['year'])}年度&#x3000;{esc(b['subject'])}</div>
  </div>
  <div class="c-band"></div>
  <div class="c-series">{esc(SERIES_NAME)}</div>
  {f'<div class="c-sub">{esc(b["cover_sub"])}</div>' if b.get("cover_sub") else ''}
</section>"""


def toc_entries(b):
    ents = [("overview", "この年度の全体像", [])]
    for i, p in enumerate(b["parts"], 1):
        # 精読（core）は小さく扱う：目次には出さない（本文では設問の前に短く置く）
        trans_label = ("全訳（段落ごとの全訳と「つまり」）" if is_v2_translation(p)
                       else "全訳（原文に忠実な訳・かみくだいた訳）")
        subs = [
            (f"p{i}-identity", "この文章の正体／設問タイプと攻め方"),
            (f"p{i}-map", "英文マップ"),
            (f"p{i}-qs", "設問ごとの解説"),
            (f"p{i}-trans", trans_label),
        ]
        ents.append((f"part{i}", f"大問{p['no']}　{p['title']}", subs))
    ents.append(("summary", "総まとめ", [
        ("sum-answers", "解答一覧"),
        ("sum-review", "失点の型別の復習動線"),
        ("sum-self", "自己採点表"),
    ]))
    return ents


def render_toc(b) -> str:
    items = []
    for anchor, label, subs in toc_entries(b):
        items.append(f'<li class="lv1"><a href="#{anchor}">{md(label)}</a></li>')
        for a2, l2 in subs:
            items.append(f'<li class="lv2"><a href="#{a2}">{md(l2)}</a></li>')
    return f"""
<h1 id="toc">目次</h1>
<div class="chapter-lead">{md(b['univ'])} {md(b.get('faculty', ''))} {md(b['year'])}年度 {md(b['subject'])}</div>
<div class="toc"><ul>{''.join(items)}</ul></div>
"""


def render_howto(b) -> str:
    """「この本の使い方」。目次の下に置くと目次が 1 ページを超えたときに 2 ページ目がほぼ空白になるので、
    全体像の章の冒頭に置く。"""
    howto = b.get("howto") or [
        "問題冊子を印刷して手元に置いてください。この解説には問題文・英文本文を載せていません。",
        "各大問は「出典 → 正体 → 攻め方 → 英文マップ → 設問 → 全訳」の順です。設問の解説は「手順 → 根拠の文 → 全選択肢の検討」で、正解へのたどり着き方を示します。",
    ]
    return f'<div class="toc-howto">{callout("navy", "【この本の使い方】", paras(howto))}</div>'



def render_overview(b) -> str:
    ov = b["overview"]
    out = [f'<h1 id="overview">この年度の全体像</h1>']
    if ov.get("lead"):
        out.append(f'<div class="chapter-lead">{md(ov["lead"])}</div>')
    out.append(render_howto(b))
    out.append('<h2>大問構成</h2>')
    out.append(f'<div class="hero">{md(ov["exam_line"])}</div>')
    # 見出し・列の書式は data で上書きできる（structure_head / structure_cls）
    out.append(table(ov.get("structure_head", ["大問", "形式・テーマ", "設問", "配点", "目安時間"]),
                     ov["structure"], "structure",
                     ov.get("structure_cls", ["c key", "", "", "c nowrap", "c nowrap"])))
    out.append('<h2>時間配分</h2>')
    out.append(table(["順番", "やること", "時間", "ねらい"], ov["time_plan"], "", ["c key", "", "c nowrap", ""]))
    out.append('<h2>差がつく所</h2>')
    out.append(table(["どこで", "何が起きるか", "対策"], ov["diff_points"], "diff", ["key", "", ""]))
    if ov.get("notes"):
        out.append(callout("gold", "【注記】", paras(ov["notes"]), "small"))
    return "".join(out)


def q_anchor(pi: int, qi: int) -> str:
    """設問の id 属性。大問ごとに設問番号が重なる（設問1 が各大問にある）ので、
    大問の通し番号と大問内の順番から作って文書全体で一意にする。"""
    return f"q-p{pi}-{qi}"


def render_question(q, anchor: str = "") -> str:
    ans = q.get("answer_display", q["answer"])
    id_attr = f' id="{esc(anchor)}"' if anchor else ""
    out = [f'<div class="question"{id_attr}>']
    out.append(
        f'<div class="q-top"><div class="q-head{" long-ans" if len(str(ans)) > 24 else ""}"><span class="q-ans">正解<span class="q-ans-v">{md(ans)}</span></span>'
        f'<span class="q-no">設問{md(q["id"])}</span><span class="q-type">{md(q["type"])}</span></div>'
    )
    out.append('<div class="q-body">')
    if q.get("target"):
        out.append(f'<p class="q-target">{md(q["target"])}</p>')
    out.append("</div></div>")  # q-body と q-top（見出し＋設問の要約を割らない塊）を閉じる
    out.append('<div class="q-body q-rest">')
    if q.get("intent"):
        out.append(callout("navy", "【出題意図】", paras(q["intent"])))
    if q.get("steps"):
        lis = "".join(f"<li>{md(s)}</li>" for s in q["steps"])
        out.append(callout("gold", "【解く人の頭の中の手順】", f'<ol class="steps">{lis}</ol>'))
    if q.get("evidence"):
        out.append(render_evidence(q, ans))
    elif q.get("basis"):
        head = f'<p class="basis-ans">正解 <span class="ok">{md(ans)}</span></p>' if not q.get("chars") else ""
        out.append(callout("teal", "【正解の根拠】", head + paras(q["basis"]), "basis"))
    if q.get("choices"):
        # v2：全選択肢の表。旧の誤答表（wrong）が残っていても出さない（重複させない）
        out.append(render_choices(q["choices"]))
    elif q.get("wrong"):
        rows = [[f'× {w["choice"]}', w["why"], w["lack"]] for w in q["wrong"]]
        # 誤答が語句・文（整序の誤答例など）のときは選択肢の列を折り返せる幅にする（nowrap だと他の列が潰れる）
        long_choice = any(len(str(w["choice"])) > 16 for w in q["wrong"])
        out.append(callout("verm", "【誤答の検討】",
                           table(["選択肢", "ダメな理由", "これを選ぶ人に足りないもの"], rows,
                                 "wrong long-choice" if long_choice else "wrong",
                                 ["choice", "why", "lack"])))
    if q.get("rubric"):
        rows = [[r["element"], r["points"], r["criteria"]] for r in q["rubric"]]
        out.append(callout("gold", "【採点の要素】",
                           table(["要素", "配点", "判定（ここまで書けていれば可／減点）"], rows, "rubric",
                                 ["el", "pt", ""])))
    if q.get("chars"):
        per_row = q.get("per_row", 20)
        inner = "".join(masu(q["chars"], ex["text"], per_row, ex.get("label", ""), True)
                        for ex in q.get("examples", []))
        out.append(callout("teal", "【答案例】", inner, "nobreak"))
        if q.get("blank_masu", True):
            out.append(masu(q["chars"], "", per_row, f"自分の答案（{q['chars']}字以内）"))
    elif q.get("examples"):
        inner = "".join(f'<p>{md(ex.get("label", ""))}　{md(ex["text"])}</p>' for ex in q["examples"])
        out.append(callout("teal", "【答案例】", inner))
    if q.get("ng"):
        out.append(callout("verm", "【減点される書き方】",
                           table(["答案", "どこが足りないか"], [[n["text"], n["why"]] for n in q["ng"]], "ng",
                                 ["", ""])))
    if q.get("note"):
        out.append(callout("verm", "【要注意の罠】", paras(q["note"]), "trap"))
    out.append("</div></div>")
    return "".join(out)


def render_evidence(q, ans) -> str:
    """根拠の文：場所 → 英文｜訳（並べる。**…** は決め手の語句として強調）→ 決め手。"""
    inner = []
    if not q.get("chars"):
        inner.append(f'<p class="basis-ans">正解 <span class="ok">{md(ans)}</span></p>')
    if q.get("basis"):
        inner.append(f'<div class="ev-sum">{paras(q["basis"])}</div>')
    for ev in q["evidence"]:
        blk = ['<div class="ev">']
        if ev.get("loc"):
            blk.append(f'<div class="ev-loc">{md(ev["loc"])}</div>')
        blk.append('<table class="ev-pair"><tbody><tr>'
                   f'<td class="ev-en">{md(ev.get("en", ""))}</td>'
                   f'<td class="ev-ja">{md(ev.get("ja", ""))}</td></tr></tbody></table>')
        if ev.get("point"):
            blk.append(f'<div class="ev-point"><span class="ev-point-lbl">決め手</span>{md(ev["point"])}</div>')
        blk.append("</div>")
        inner.append("".join(blk))
    return callout("teal", "【根拠の文】", "".join(inner), "evidence")


def render_choices(choices) -> str:
    """全選択肢の表：記号（正解＝緑の ○、誤答＝朱の ×）｜英語と訳｜理由（誤答は「選ぶ人の思考」も）。"""
    trs = []
    for c in choices:
        ok = bool(c.get("ok"))
        mark = "○" if ok else "×"
        en = f'<div class="c-en">{md(c.get("en", ""))}</div>' if c.get("en") else ""
        ja = f'<div class="c-ja">{md(c["ja"])}</div>' if c.get("ja") else ""
        why_lbl = "なぜ正解か" if ok else "どこがずれるか"
        why = f'<div class="c-why"><span class="c-lbl">{why_lbl}</span>{md(c.get("why", ""))}</div>'
        who = ""
        if not ok and c.get("who"):
            who = f'<div class="c-who"><span class="c-lbl">選ぶ人の思考</span>{md(c["who"])}</div>'
        trs.append(f'<tr class="{"c-ok" if ok else "c-ng"}"><td class="ck">{mark}&#x2009;{md(c.get("key", ""))}</td>'
                   f'<td class="cen">{en}{ja}</td><td class="cwhy">{why}{who}</td></tr>')
    t = ('<table class="choices"><thead><tr><th class="c">記号</th><th>選択肢と訳</th>'
         '<th>正解・不正解の理由</th></tr></thead><tbody>' + "".join(trs) + "</tbody></table>")
    return callout("navy", "【全選択肢の検討】", t, "choices-co")


def is_v2_translation(p) -> bool:
    tr = p.get("translation") or []
    return bool(tr) and all("full" in x for x in tr)


def para_label(para) -> str:
    v = str(para.get("para", ""))
    return f"第{v}段落" if v.isdigit() else v


def render_translation_v2(p) -> str:
    """全訳（v2）：段落ごとに全訳 → その下に色を変えた「つまり」の囲み。"""
    out = [f'<p class="trans-note">{md(p.get("trans_note") or "段落ごとに、全訳（文頭の①②…は段落内の文番号）と、その段落が「つまりどういうことか」を示します。英文本文は問題冊子で確認してください。訳はTHINKINGのオリジナルです。")}</p>']
    for para in p["translation"]:
        label = para_label(para)
        if para.get("label"):
            label += f'｜{para["label"]}'
        qs = f'<span class="para-qs">{md(para["qs"])}</span>' if para.get("qs") else ""
        out.append('<div class="tp">')
        out.append(f'<div class="tp-head">{md(label)}{qs}</div>')
        out.append(f'<div class="tp-full">{mark_sno(paras(para["full"]))}</div>')
        if para.get("gist"):
            out.append(f'<div class="gist"><div class="gist-lbl">つまり</div>{paras(para["gist"])}</div>')
        out.append("</div>")
    return "".join(out)


def render_translation_legacy(p) -> str:
    """旧：文単位の 2 列（原文に忠実な訳・かみくだいた訳）。v2 の形でない data 用（互換）。"""
    out = [f'<p class="trans-note">{md(p.get("trans_note") or "左＝原文に忠実な訳（構造を写した訳）、右＝かみくだいた訳（言いたいことを日本語の順で言い直した訳）。番号は段落番号と段落内の文番号。英文本文は問題冊子で確認してください。訳はTHINKINGのオリジナルです。")}</p>']
    out.append('<table class="trans"><thead><tr><th class="c">文</th><th class="h-faithful">原文に忠実な訳</th>'
               '<th class="h-plain">かみくだいた訳</th></tr></thead><tbody>')
    for para in p["translation"]:
        label = f'第{para["para"]}段落'
        if para.get("label"):
            label += f'｜{para["label"]}'
        qs = f'<span class="para-qs">{md(para["qs"])}</span>' if para.get("qs") else ""
        out.append(f'<tr class="para-row"><td class="para-head" colspan="3">{md(label)}{qs}</td></tr>')
        for n, st in enumerate(para["sentences"], 1):
            out.append(
                f'<tr><td class="sno">{para["para"]}{maru(n)}</td>'
                f'<td class="faithful">{md(st["faithful"])}</td><td class="plain">{md(st["plain"])}</td></tr>'
            )
    out.append("</tbody></table>")
    return "".join(out)


def render_core(i, p) -> str:
    """精読（構文の図）。v2 では小さく扱う：目次に出さない小さめの見出しで、設問の前に短く置く。"""
    out = []
    # 見出しだけがページ末に取り残されないよう、見出し＋前置き＋最初の構文の図を一塊にする。
    # 各精読ブロックは「小見出し＋構文の図＋凡例」だけを割らない塊にし、訳・解説の囲みは続けて流す
    # （ブロック全体を割らない塊にすると、ページ末に大きな空白ができる）。
    out.append('<div class="nobreak">')
    out.append(f'<h2 id="p{i}-core" class="minor">構文の確認（精読）</h2>')
    if p.get("core_lead"):
        out.append(paras(p["core_lead"]))
    for ci, c in enumerate(p["core"]):
        if ci > 0:
            out.append('<div class="core-block">')
        out.append('<div class="core-head">' if ci == 0 else '<div class="core-head nobreak">')
        out.append(f'<h3 class="core-title">{md(c["title"])}</h3>')
        out.append(parse_table(c["lines"]))
        if c.get("legend"):
            out.append(f'<p class="parse-legend">{md(c["legend"])}</p>')
        out.append("</div>")
        if ci == 0:
            out.append("</div>")  # 章頭の nobreak を閉じる
        out.append(callout("blue", "【訳】", f'<p class="core-trans">{md(c["translation"])}</p>'))
        if c.get("points"):
            out.append(callout("gold", "【ここで止まって考える】", paras(c["points"])))
        if ci > 0:
            out.append("</div>")
    return "".join(out)


def render_part(i, p) -> str:
    out = [f'<h1 id="part{i}"><span class="h1-eyebrow">大問{md(p["no"])}&#x3000;</span>{md(p["title"])}</h1>']
    if p.get("source"):
        out.append(f'<div class="part-source"><span class="src-lbl">出典</span>{md(p["source"])}</div>')
    out.append(f'<div class="chapter-lead">{md(p["lead"])}</div>')

    out.append(f'<h2 id="p{i}-identity">この文章の正体</h2>')
    out.append(f'<div class="identity">{md(p["identity"])}</div>')
    if p.get("identity_note"):
        out.append(paras(p["identity_note"]))

    out.append('<h2>設問タイプと攻め方</h2>')
    out.append(table(["設問", "タイプ", "攻め方"], p["types"], "types", ["key c", "nowrap", ""]))
    if p.get("types_note"):
        out.append(callout("verm", "【要注意の罠】", paras(p["types_note"]), "trap"))

    out.append(f'<h2 id="p{i}-map">英文マップ ― 段落の流れと設問の在りか</h2>')
    if p.get("map_flow"):
        out.append(f'<div class="flow">{md(p["map_flow"])}</div>')
    out.append(table(["段落", "役割", "内容", "設問"], p["map"], "map", ["para", "role", "", "qs"]))
    if p.get("map_note"):
        out.append(callout("navy", "", paras(p["map_note"])))

    if p.get("core"):
        out.append(render_core(i, p))

    out.append(f'<h2 id="p{i}-qs">設問ごとの解説</h2>')
    if p.get("questions_lead"):
        out.append(paras(p["questions_lead"]))
    for qi, q in enumerate(p["questions"], 1):
        out.append(render_question(q, q_anchor(i, qi)))

    out.append(f'<h2 id="p{i}-trans" class="pagebreak">全訳 ― 大問{md(p["no"])}</h2>')
    out.append(render_translation_v2(p) if is_v2_translation(p) else render_translation_legacy(p))
    return "".join(out)


def all_questions(b):
    for p in b["parts"]:
        for q in p["questions"]:
            yield p, q


def render_summary(b) -> str:
    s = b["summary"]
    out = ['<h1 id="summary">総まとめ</h1>']
    out.append(f'<div class="chapter-lead">{md(s.get("lead", "まず自己採点。落とした問題を「型」で分けて、型ごとに復習する。"))}</div>')

    out.append('<h2 id="sum-answers">解答一覧</h2>')
    rows = []
    for p, q in all_questions(b):
        rows.append([f'大問{p["no"]}', q["id"], q.get("answer_display", q["answer"]), q.get("points", "—"),
                     q.get("checked", "未照合")])
    html_t = table(["大問", "設問", "解答", "配点", "照合（資料との一致・不一致・推定の別）"], rows, "answers",
                   ["key nowrap", "c nowrap qid", "ans", "c nowrap", "chk"])
    # 資料と食い違った設問の行を目立たせる
    html_t = re.sub(r'<tr>(<td class="key nowrap">(?:(?!</tr>).)*?不一致)', r'<tr class="mismatch">\1', html_t)
    out.append(html_t)
    out.append('<h3>照合した資料と注記</h3>')
    src_rows = [[x["name"], x["status"], x.get("note", "")] for x in b.get("sources", [])]
    out.append(table(["資料", "扱い", "注記"], src_rows, "", ["key", "nowrap", ""]))
    if s.get("answer_notes"):
        out.append(callout("gold", "【注記】", paras(s["answer_notes"]), "small"))

    out.append('<h2 id="sum-review">失点の型別の復習動線</h2>')
    if s.get("review_lead"):
        out.append(paras(s["review_lead"]))
    # 該当設問は大問ごとに 1 行にまとめ、行の中では折り返してよい（nowrap にしない＝はみ出し防止）
    trs = []
    for t in s["miss_types"]:
        groups = []
        for p in b["parts"]:
            ids = [q["id"] for q in p["questions"] if t["key"] in q.get("miss_types", [])]
            if ids:
                groups.append(f'<div class="hit-grp"><span class="hit-part">{md(p["no"])}</span> '
                              f'{"　".join(md(x) for x in ids)}</div>')
        n = sum(1 for _p, q in all_questions(b) if t["key"] in q.get("miss_types", []))
        hits = "".join(groups) + f'<div class="hit-n">計{n}問</div>' if groups else "—"
        trs.append(f'<tr><td class="key">{md("【" + t["key"] + "】" + t["name"])}</td><td class="hits">{hits}</td>'
                   f'<td>{md(t["lack"])}</td><td>{md(t["action"])}</td></tr>')
    out.append('<table class="review"><thead><tr><th>失点の型</th><th>該当設問（大問別）</th><th>足りないもの</th>'
               '<th>次にやること</th></tr></thead><tbody>' + "".join(trs) + "</tbody></table>")

    # 表は 1 ページに収まらないので nobreak で包まない（包むと前のページ末が大きく空く）。見出しは break-after: avoid
    out.append('<div><h2 id="sum-self">自己採点表</h2>')
    rows = []
    for p, q in all_questions(b):
        rows.append(f'<tr><td class="key nowrap">大問{md(p["no"])}</td><td class="c">{md(q["id"])}</td>'
                    f'<td>{md(q["type"])}</td><td class="c">{md(q.get("points", "—"))}</td>'
                    f'<td class="blank"></td><td class="blank"></td><td class="blank"></td>'
                    f'<td class="blank"></td></tr>')
    total = s.get("total_points", "")
    rows.append(f'<tr class="total"><td colspan="3">合計</td><td class="c">{md(total)}</td>'
                f'<td class="blank"></td><td class="blank"></td><td class="blank"></td><td class="blank"></td></tr>')
    out.append('<table class="selfscore"><thead><tr><th>大問</th><th class="c">設問</th><th>タイプ</th>'
               '<th class="c">配点</th><th class="c">1回目</th><th class="c">2回目</th><th class="c">3回目</th>'
               '<th class="c">失点の型</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")
    if s.get("closing"):
        out.append(paras(s["closing"]))
    if b.get("copyright"):
        out.append(f'<div class="notes muted">{paras(b["copyright"])}</div>')
    return "".join(out)


def render_html(b) -> str:
    css = CSS_PATH.read_text(encoding="utf-8")
    color = b.get("cover_color", "#1f2d3d")
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise SystemExit(f"cover_color は #RRGGBB で指定してください: {color}")
    book_title = f'{b["univ"]} {b.get("faculty", "")} {b["year"]}年度 {b["subject"]}｜{SERIES_NAME}'
    foot = b.get("footer_note", "")
    body = [
        render_cover(b),
        render_toc(b),
        render_overview(b),
    ]
    for i, p in enumerate(b["parts"], 1):
        body.append(render_part(i, p))
    body.append(render_summary(b))
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<title>{esc(book_title)}</title>
<meta name="author" content="THINKING">
<style>{css}
@page {{ @top-left {{ content: "{css_str(book_title)}"; }} @bottom-right {{ content: "{css_str(foot)}"; }} }}
@page cover {{ background: {color}; @top-left {{ content: none; }} @bottom-right {{ content: none; }} }}
</style></head>
<body>{''.join(body)}</body></html>"""


# ---------------------------------------------------------------- 検査
class Report:
    def __init__(self):
        self.errors, self.warns, self.oks = [], [], []

    def err(self, m): self.errors.append(m)
    def warn(self, m): self.warns.append(m)
    def ok(self, m): self.oks.append(m)

    def print(self):
        for m in self.oks:
            print(f"  OK    {m}")
        for m in self.warns:
            print(f"  WARN  {m}")
        for m in self.errors:
            print(f"  ERROR {m}")


def check_fonts_installed(rep: Report):
    if not shutil.which("fc-list"):
        rep.warn("fc-list が無いのでフォントの有無を確認できません")
        return
    fams = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
    for f in REQUIRED_FONTS:
        if f in fams:
            rep.ok(f"フォントあり: {f}")
        else:
            rep.err(f"フォントが見つかりません: {f}（README の「準備」参照：apt-get install fonts-noto-cjk fonts-liberation）")


def _font_cmaps():
    """本文で使う 3 書体の cmap（収録文字集合）を集める。"""
    try:
        from fontTools.ttLib import TTCollection, TTFont
    except ImportError:
        return None
    cov = set()
    for fam in ["Noto Sans CJK JP", "Noto Serif CJK JP", "Noto Sans CJK JP:bold", "Noto Serif CJK JP:bold"]:
        path = subprocess.run(["fc-match", "-f", "%{file}", fam], capture_output=True, text=True).stdout.strip()
        if not path:
            continue
        if path.endswith(".ttc"):
            fonts = TTCollection(path).fonts
            # JP のフェイスを探す（無ければ先頭）
            pick = [f for f in fonts if "JP" in (f["name"].getDebugName(1) or "")] or fonts[:1]
            for f in pick[:1]:
                cov |= set(f.getBestCmap().keys())
        else:
            cov |= set(TTFont(path).getBestCmap().keys())
    return cov


def visible_text(html_src: str) -> str:
    t = re.sub(r"<style.*?</style>", "", html_src, flags=re.S)
    t = re.sub(r"<title.*?</title>", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return html.unescape(t)


def check_glyphs(html_src: str, rep: Report):
    cov = _font_cmaps()
    if cov is None:
        rep.warn("fontTools が無いので収録文字の検査を省略")
        return
    text = visible_text(html_src)
    missing = sorted({ch for ch in text if not ch.isspace() and ord(ch) not in cov})
    if missing:
        desc = ", ".join(f"{c}(U+{ord(c):04X} {unicodedata.name(c, '?')})" for c in missing[:20])
        rep.err(f"Noto CJK JP に無い文字が {len(missing)} 種: {desc}")
    else:
        rep.ok(f"本文 {len(set(text))} 種の文字はすべて Noto CJK JP に収録")


def check_banned_and_english(b, html_src: str, rep: Report):
    text = visible_text(html_src)
    hit = [w for w in BANNED_WORDS if w in text]
    if hit:
        rep.err(f"禁止語が入っています: {'、'.join(hit)}")
    else:
        rep.ok("禁止語（他社シリーズ名など）なし")
    for p in b["parts"]:
        check_part_english(p, rep)
        if not str(p.get("source") or "").strip():
            rep.err(f"大問{p['no']}: 出典（source）がありません。大問の冒頭に 1 行で出す")
        if len(p.get("core") or []) > 3:
            rep.warn(f"大問{p['no']}: 構文の図（core）が {len(p['core'])} 個。v2 では構造が決め手の設問に限って 0〜3 個")


def _strings(obj):
    """data の中の文字列をすべて取り出す（dict・list を辿る）。"""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _strings(v)


def _plain(s: str) -> str:
    return re.sub(r"\*\*|__|\[\[|\]\]", "", str(s))


def en_words(s: str) -> int:
    return len(EN_WORD_RE.findall(_plain(s)))


def part_quotes(p):
    """大問に載せている英語の引用を (種類, 英文) で集める。
    根拠の文・選択肢・精読（構文の図 1 つ＝1 文）・下線部 __...__・[[...]]（英語を含むものだけ）。"""
    qs = []
    for q in p.get("questions", []):
        for ev in q.get("evidence", []) or []:
            qs.append((f"設問{q['id']} 根拠の文", ev.get("en", "")))
        for c in q.get("choices", []) or []:
            qs.append((f"設問{q['id']} 選択肢{c.get('key', '')}", c.get("en", "")))
    for c in p.get("core", []) or []:
        qs.append(("精読", " ".join(ln.get("en", "") for ln in c.get("lines", []))))
    for s in _strings(p):
        for m in re.findall(r"__(.+?)__", s):
            qs.append(("下線部", m))
        for m in re.findall(r"\[\[(.+?)\]\]", s):
            qs.append(("引用", m))
    return [(k, t) for k, t in qs if en_words(t) > 0]


def check_part_english(p, rep: Report):
    """v2 の英語量の検査。引用 1 つは原則 1 文（目安 45 語）。大問の英語の合計（同じ文の重複は 1 回）が
    本文語数（body_words）の約 3 割以内。"""
    no = p["no"]
    quotes = part_quotes(p)
    # 1 引用ごと
    for kind, t in quotes:
        w = en_words(t)
        head = _plain(t)[:50]
        if w > QUOTE_MAX_WORDS:
            rep.err(f"大問{no} {kind}: 引用が {w} 語（{QUOTE_MAX_WORDS} 語超＝段落の転載）: {head}…")
        elif w > QUOTE_WARN_WORDS:
            rep.warn(f"大問{no} {kind}: 引用が {w} 語（原則 1 文・目安 {QUOTE_WARN_WORDS} 語まで）: {head}…")
        n_sent = len(re.findall(r"[.!?](?:[\"'”’)]*)(?:\s|$)", _plain(t).strip()))
        if n_sent > QUOTE_WARN_SENTENCES:
            rep.warn(f"大問{no} {kind}: 引用に {n_sent} 文（原則 1 文、必要なら前後 1 文まで）: {head}…")
    # 合計（同じ文・その一部の重複は 1 回だけ数える）
    # 選択肢は設問（大学の作成部分）で本文ではないので、本文の何割を載せたかの計算には入れない
    norm = sorted({" ".join(x.lower() for x in EN_WORD_RE.findall(_plain(t))) for _k, t in quotes
                   if "選択肢" not in _k},
                  key=len, reverse=True)
    kept = []
    for n in norm:
        if not any(f" {n} " in f" {k} " for k in kept):
            kept.append(n)
    total = sum(len(k.split()) for k in kept)
    body = p.get("body_words")
    if not body:
        rep.warn(f"大問{no}: body_words（本文の概算語数）がありません。英語の割合を検査できない"
                 f"（代わりに絶対上限 {FALLBACK_MAX_EN_WORDS} 語で検査）")
        if total > FALLBACK_MAX_EN_WORDS:
            rep.err(f"大問{no}: 英語が {total} 語（上限 {FALLBACK_MAX_EN_WORDS}）。本文の転載になっていないか確認")
        else:
            rep.ok(f"大問{no}: 載せている英語 {total} 語（重複除く。上限 {FALLBACK_MAX_EN_WORDS}）")
        return
    ratio = total / float(body)
    msg = f"大問{no}: 載せている英語 {total} 語／本文 約{body} 語＝{ratio:.0%}（約 {EN_RATIO_WARN:.0%} 以内）"
    if ratio > EN_RATIO_MAX:
        rep.err(msg + f"。{EN_RATIO_MAX:.0%} 超は本文の通し掲載に近い。引用を減らす")
    elif ratio > EN_RATIO_WARN:
        rep.warn(msg + "。引用を見直す")
    else:
        rep.ok(msg)


def check_answers(b, rep: Report):
    """記述の答案例が字数内か、正解・照合欄が空でないか。"""
    for p in b["parts"]:
        for q in p["questions"]:
            tag = f"大問{p['no']} 設問{q['id']}"
            if not q.get("answer"):
                rep.err(f"{tag}: answer が空")
            if not q.get("checked"):
                rep.warn(f"{tag}: 照合欄（checked）が空。照合していないなら「未照合」と書く")
            ch = q.get("choices") or []
            if ch:
                oks = [str(c.get("key", "")) for c in ch if c.get("ok")]
                if not oks:
                    rep.err(f"{tag}: choices に正解（ok: True）がありません")
                elif not all(k and k in str(q.get("answer", "")) for k in oks):
                    rep.warn(f"{tag}: choices の正解 {'・'.join(oks)} と answer「{q.get('answer')}」が食い違っていないか確認")
                for c in ch:
                    if not c.get("why"):
                        rep.warn(f"{tag} 選択肢{c.get('key', '')}: why（理由）が空")
                    if not c.get("ok") and not c.get("who"):
                        rep.warn(f"{tag} 選択肢{c.get('key', '')}: 誤答の who（選ぶ人の思考）が空")
                    if c.get("en") and not c.get("ja"):
                        rep.warn(f"{tag} 選択肢{c.get('key', '')}: 訳（ja）が空")
            for ev in q.get("evidence") or []:
                if not ev.get("ja") or not ev.get("point"):
                    rep.warn(f"{tag}: 根拠の文（{ev.get('loc', '?')}）の訳 ja か決め手 point が空")
            for ex in q.get("examples", []):
                if q.get("chars") and len(ex["text"]) > q["chars"]:
                    rep.err(f"{tag}: 答案例が {len(ex['text'])} 字（指定 {q['chars']} 字）")


def check_clipping(doc, rep: Report):
    """欠けの検査（レイアウト後の箱を調べる）。
    1) inline-block / inline-table が、負の text-indent を持つ親の中にある → ERROR（欠ける原因）
    2) 背景・枠のある箱が本文領域の左右からはみ出している → ERROR（印刷で切れる・欠ける）
    表紙（@page cover）は全面塗りなので対象外。"""
    from weasyprint.formatting_structure import boxes as B

    def visible(box):
        st = box.style
        bg = st["background_color"]
        has_bg = bg is not None and getattr(bg, "alpha", 0) > 0
        has_border = any(getattr(box, f"border_{s}_width", 0) > 0 for s in ("top", "right", "bottom", "left"))
        return has_bg or has_border

    def indent_neg(box):
        ti = box.style["text_indent"]
        v = getattr(ti, "value", ti)
        try:
            return float(v) < 0
        except (TypeError, ValueError):
            return False

    problems = []
    for pno, page in enumerate(doc.pages, 1):
        pb = page._page_box
        if pb.page_type.name == "cover":
            continue
        left = pb.margin_left + pb.padding_left + pb.border_left_width
        right = pb.margin_width() - pb.margin_right - pb.padding_right - pb.border_right_width
        right = left + pb.width

        def walk(box, neg_parent=False):
            if isinstance(box, (B.InlineBlockBox, B.InlineFlexBox if hasattr(B, "InlineFlexBox") else B.InlineBlockBox)) \
                    and neg_parent and visible(box):
                problems.append(f"p.{pno}: 負の text-indent の中に背景・枠つき inline-block（欠ける）")
            if visible(box) and not isinstance(box, (B.PageBox, B.MarginBox)):
                x0 = box.position_x + box.margin_left
                x1 = x0 + box.border_width()
                if x0 < left - 1 or x1 > right + 1:
                    cls = (box.element.get("class") if box.element is not None else "") or ""
                    problems.append(f"p.{pno}: 背景・枠つきの箱が本文領域からはみ出し"
                                    f"（<{box.element_tag} class=\"{cls}\"> {x0:.0f}–{x1:.0f}px／領域 {left:.0f}–{right:.0f}px）")
            neg = neg_parent or (isinstance(box, B.BlockContainerBox) and indent_neg(box))
            for ch in getattr(box, "children", []) or []:
                walk(ch, neg)

        for ch in pb.children:
            walk(ch)
    if problems:
        for m in sorted(set(problems))[:15]:
            rep.err(m)
    else:
        rep.ok("欠けの検査：負の text-indent 内の inline-block なし、はみ出した背景・枠なし")


def check_pdf(pdf: Path, b, rep: Report):
    if shutil.which("pdffonts"):
        out = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout.splitlines()[2:]
        names = []
        for line in out:
            cols = line.split()
            if not cols:
                continue
            name = cols[0]
            # 列: name type [encoding...] emb sub uni object ID — 後ろから数える
            emb, sub, uni = cols[-5], cols[-4], cols[-3]
            names.append(name)
            if emb != "yes":
                rep.err(f"埋め込まれていないフォント: {name}")
            if uni != "yes":
                rep.warn(f"ToUnicode が無いフォント（コピペ・検索で化ける）: {name}")
            base = name.split("+", 1)[-1].replace("-", "")
            if not any(a in base for a in ALLOWED_PDF_FONTS):
                rep.err(f"想定外のフォントに落ちています（代替フォント）: {name}")
        rep.ok(f"PDF のフォント {len(names)} 本: " + ", ".join(sorted({n.split('+', 1)[-1] for n in names})))
    else:
        rep.warn("pdffonts が無いので埋め込み検査を省略（poppler-utils を入れてください）")

    if shutil.which("pdftotext"):
        txt = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True).stdout
        flat = re.sub(r"\s+", "", txt)
        if "�" in txt:
            rep.err("PDF から抜いた文字に U+FFFD（文字化け）があります")
        must = [b["univ"], SERIES_NAME, "この年度の全体像", "設問ごとの解説", "全訳", "自己採点表"]
        must += [re.sub(r"\s+", "", re.sub(r"[*_\[\]]", "", p["identity"]))[:12] for p in b["parts"]]
        lost = [m for m in must if re.sub(r"\s+", "", m) not in flat]
        if lost:
            rep.err("PDF から読み戻せない文字列: " + " / ".join(lost))
        else:
            rep.ok(f"PDF の文字を読み戻せた（{len(must)} 箇所照合、U+FFFD なし）")
        pages = txt.count("\f")
        rep.ok(f"ページ数 {pages}")
    else:
        rep.warn("pdftotext が無いので読み戻し検査を省略")


# ---------------------------------------------------------------- main
def load_book(path: Path):
    spec = importlib.util.spec_from_file_location("book_data", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BOOK


def main():
    ap = argparse.ArgumentParser(description="THINKINGの徹底解説シリーズ PDF ビルド")
    ap.add_argument("data", help="<univ>_<year>（中身置き場の .py）または data ファイルのパス")
    ap.add_argument("--content-dir", help="中身置き場（既定: $TETTEI_CONTENT_DIR か DEFAULT_CONTENT_DIR）")
    ap.add_argument("--out", help="出力 PDF（既定: <中身置き場>/out/<id>.pdf）")
    ap.add_argument("--html", action="store_true", help="中間 HTML も PDF の隣に残す")
    ap.add_argument("--png", help="ページ画像（PNG, 70dpi）を出すディレクトリ")
    args = ap.parse_args()

    content_dir = Path(args.content_dir or os.environ.get("TETTEI_CONTENT_DIR") or DEFAULT_CONTENT_DIR).resolve()
    data_path = Path(args.data)
    if not data_path.exists():
        data_path = content_dir / "data" / f"{args.data.removesuffix('.py')}.py"
    data_path = data_path.resolve()
    if not data_path.exists():
        raise SystemExit(f"data が見つかりません: {data_path}")
    repo_root = HERE.parent
    b = load_book(data_path)
    if data_path.is_relative_to(repo_root) and not b.get("dummy"):
        raise SystemExit(
            "中身の data がリポジトリ内にあります（Netlify で公開されてしまう）。"
            f"\n  {data_path}\n  中身置き場（{content_dir}/data/）へ移してください。"
        )
    out = Path(args.out).resolve() if args.out else content_dir / "out" / f"{data_path.stem}.pdf"
    if out.is_relative_to(repo_root):
        print(f"WARN 出力先がリポジトリ内です（.gitignore で除外されますが、手動デプロイでは公開されうる）: {out}")
    out.parent.mkdir(parents=True, exist_ok=True)

    rep = Report()
    check_fonts_installed(rep)
    if rep.errors:
        rep.print()
        sys.exit(1)

    src = render_html(b)
    if args.html:
        out.with_suffix(".html").write_text(src, encoding="utf-8")
    check_glyphs(src, rep)
    check_banned_and_english(b, src, rep)
    check_answers(b, rep)

    import logging
    from weasyprint import HTML
    logging.getLogger("weasyprint").setLevel(logging.ERROR)
    doc = HTML(string=src, base_url=str(HERE)).render()
    check_clipping(doc, rep)
    doc.write_pdf(str(out))
    print(f"PDF: {out}")

    check_pdf(out, b, rep)
    if args.png:
        d = Path(args.png)
        d.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftoppm", "-r", "70", "-png", str(out), str(d / "page")], check=True)
        print(f"PNG: {d}/page-*.png")
    rep.print()
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
