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
  - 英文の載せすぎ（本文転載）になっていないか（大問ごとの英語語数の上限）

本文の記法（data 内の文字列で使える）:
  **太字**   __下線（設問の下線部の引用）__   [[英語の語句・短い引用]]
  【札】 は自動で太字になる（札は【】文字だけ。色付きの箱は使わない）
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
MAX_EN_WORDS_PER_PART = 260   # 大問 1 つあたりの英語語数の上限（精読の構文図＋引用）
MAX_EN_WORDS_PER_QUOTE = 30   # [[...]] 1 つあたりの上限

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
        subs = [
            (f"p{i}-identity", "この文章の正体／設問タイプと攻め方"),
            (f"p{i}-map", "英文マップ"),
            (f"p{i}-core", "心臓部の精読"),
            (f"p{i}-qs", "設問ごとの解説"),
            (f"p{i}-trans", "全訳（原文に忠実な訳・かみくだいた訳）"),
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
    howto = b.get("howto") or [
        "問題冊子を印刷して手元に置いてください。この解説には問題文・英文本文を載せていません。",
        "各大問は「正体 → 攻め方 → 英文マップ → 精読 → 設問 → 全訳」の順です。まず自力で解き、設問の解説から読み始めても構いません。",
    ]
    return f"""
<h1 id="toc">目次</h1>
<div class="chapter-lead">{md(b['univ'])} {md(b.get('faculty', ''))} {md(b['year'])}年度 {md(b['subject'])}</div>
<div class="toc"><ul>{''.join(items)}</ul></div>
<div class="toc-howto">{callout("navy", "【この本の使い方】", paras(howto))}</div>
"""


def render_overview(b) -> str:
    ov = b["overview"]
    out = [f'<h1 id="overview">この年度の全体像</h1>']
    if ov.get("lead"):
        out.append(f'<div class="chapter-lead">{md(ov["lead"])}</div>')
    out.append('<h2>大問構成</h2>')
    out.append(f'<div class="hero">{md(ov["exam_line"])}</div>')
    out.append(table(["大問", "形式・テーマ", "設問", "配点", "目安時間"],
                     ov["structure"], "", ["c key", "", "", "c nowrap", "c nowrap"]))
    out.append('<h2>時間配分</h2>')
    out.append(table(["順番", "やること", "時間", "ねらい"], ov["time_plan"], "", ["c key", "", "c nowrap", ""]))
    out.append('<h2>差がつく所</h2>')
    out.append(table(["どこで", "何が起きるか", "対策"], ov["diff_points"], "", ["key", "", ""]))
    if ov.get("notes"):
        out.append(callout("gold", "【注記】", paras(ov["notes"]), "small"))
    return "".join(out)


def render_question(q) -> str:
    ans = q.get("answer_display", q["answer"])
    out = [f'<div class="question" id="q-{esc(q["id"])}">']
    out.append(
        f'<div class="q-head"><span class="q-ans">正解<span class="q-ans-v">{md(ans)}</span></span>'
        f'<span class="q-no">設問{md(q["id"])}</span><span class="q-type">{md(q["type"])}</span></div>'
    )
    out.append('<div class="q-body">')
    if q.get("target"):
        out.append(f'<p class="q-target">{md(q["target"])}</p>')
    if q.get("intent"):
        out.append(callout("navy", "【出題意図】", paras(q["intent"])))
    if q.get("steps"):
        lis = "".join(f"<li>{md(s)}</li>" for s in q["steps"])
        out.append(callout("gold", "【解く人の頭の中の手順】", f'<ol class="steps">{lis}</ol>'))
    if q.get("basis"):
        head = f'<p class="basis-ans">正解 <span class="ok">{md(ans)}</span></p>' if not q.get("chars") else ""
        out.append(callout("teal", "【正解の根拠】", head + paras(q["basis"]), "basis"))
    if q.get("wrong"):
        rows = [[f'× {w["choice"]}', w["why"], w["lack"]] for w in q["wrong"]]
        out.append(callout("verm", "【誤答の検討】",
                           table(["選択肢", "ダメな理由", "これを選ぶ人に足りないもの"], rows, "wrong",
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


def render_part(i, p) -> str:
    out = [f'<h1 id="part{i}"><span class="h1-eyebrow">大問{md(p["no"])}</span>{md(p["title"])}</h1>']
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

    # 見出しだけがページ末に取り残されないよう、見出し＋前置き＋最初の精読を一塊にする
    out.append('<div class="nobreak">')
    out.append(f'<h2 id="p{i}-core">心臓部の精読</h2>')
    if p.get("core_lead"):
        out.append(paras(p["core_lead"]))
    for ci, c in enumerate(p["core"]):
        out.append('<div class="core-block">' if ci == 0 else '<div class="core-block nobreak">')
        out.append(f'<h3 class="core-title">{md(c["title"])}</h3>')
        out.append(parse_table(c["lines"]))
        if c.get("legend"):
            out.append(f'<p class="parse-legend">{md(c["legend"])}</p>')
        out.append(callout("blue", "【訳】", f'<p class="core-trans">{md(c["translation"])}</p>'))
        if c.get("points"):
            out.append(callout("gold", "【ここで止まって考える】", paras(c["points"])))
        out.append("</div>")
        if ci == 0:
            out.append("</div>")

    out.append(f'<h2 id="p{i}-qs">設問ごとの解説</h2>')
    if p.get("questions_lead"):
        out.append(paras(p["questions_lead"]))
    for q in p["questions"]:
        out.append(render_question(q))

    out.append(f'<h2 id="p{i}-trans" class="pagebreak">全訳 ― 大問{md(p["no"])}</h2>')
    out.append(f'<p class="trans-note">{md(p.get("trans_note") or "左＝原文に忠実な訳（構造を写した訳）、右＝かみくだいた訳（言いたいことを日本語の順で言い直した訳）。番号は段落番号と段落内の文番号。英文本文は問題冊子で確認してください。訳はTHINKINGのオリジナルです。")}</p>')
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
                   ["key nowrap", "c nowrap", "ans", "c nowrap", "chk"])
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
    rows = []
    for t in s["miss_types"]:
        hits = [f'{p["no"]}-{q["id"]}' for p, q in all_questions(b) if t["key"] in q.get("miss_types", [])]
        rows.append([f'【{t["key"]}】{t["name"]}', "・".join(hits) or "—", t["lack"], t["action"]])
    out.append(table(["失点の型", "該当設問", "足りないもの", "次にやること"], rows, "review", ["key", "nowrap hits", "", ""]))

    out.append('<div class="nobreak"><h2 id="sum-self">自己採点表</h2>')
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
    # 英文の量：構文図の英文＋ [[...]] 引用の語数を大問ごとに数える
    for p in b["parts"]:
        src = repr(p)
        quotes = re.findall(r"\[\[(.+?)\]\]", src)
        chunks = [ln["en"] for c in p.get("core", []) for ln in c["lines"]]
        words = sum(len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", x)) for x in quotes + chunks)
        long_q = [q for q in quotes if len(q.split()) > MAX_EN_WORDS_PER_QUOTE]
        if long_q:
            rep.err(f"大問{p['no']}: {MAX_EN_WORDS_PER_QUOTE}語を超える引用があります（本文の転載になる）: {long_q[0][:60]}…")
        if words > MAX_EN_WORDS_PER_PART:
            rep.err(f"大問{p['no']}: 英語が {words} 語（上限 {MAX_EN_WORDS_PER_PART}）。本文の転載になっていないか確認")
        else:
            rep.ok(f"大問{p['no']}: 載せている英語 {words} 語（上限 {MAX_EN_WORDS_PER_PART}）")


def check_answers(b, rep: Report):
    """記述の答案例が字数内か、正解・照合欄が空でないか。"""
    for p in b["parts"]:
        for q in p["questions"]:
            tag = f"大問{p['no']} 設問{q['id']}"
            if not q.get("answer"):
                rep.err(f"{tag}: answer が空")
            if not q.get("checked"):
                rep.warn(f"{tag}: 照合欄（checked）が空。照合していないなら「未照合」と書く")
            for ex in q.get("examples", []):
                if q.get("chars") and len(ex["text"]) > q["chars"]:
                    rep.err(f"{tag}: 答案例が {len(ex['text'])} 字（指定 {q['chars']} 字）")


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
        must = [b["univ"], SERIES_NAME, "この年度の全体像", "設問ごとの解説", "原文に忠実な訳", "自己採点表"]
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
    HTML(string=src, base_url=str(HERE)).write_pdf(str(out))
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
