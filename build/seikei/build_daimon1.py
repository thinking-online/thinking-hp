# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル
第3部-Ⅰ 大問Ⅰ「会話文 Set選択補充」完全攻略ドリル

大問Ⅰ（解答番号1〜13）＝2つの会話に散らばる空所を Set A / Set B の語群から選ぶ。
番号は一度ずつ、各Setに不要選択肢が2つ混じる。本冊はこの形式を忠実に再現した
完全オリジナル問題10セット＋設問1つずつの根拠まで示した解説で構成する。
"""
import re
import seikei_common as C
from seikei_common import esc, _raw

RUNNING = "成蹊大学 経営学部 英語 完全攻略マニュアル【第3部-Ⅰ】大問Ⅰ 会話文Set選択補充ドリル"
OUT = "/home/user/thinking-hp/dist/成蹊大学_経営学部_英語_完全攻略マニュアル_第3部-Ⅰ_大問Ⅰ会話文Set選択補充ドリル.pdf"

BLANK_RE = re.compile(r"\(\s*(\d+)\s*\)")

# ---------------------------------------------------------------------------
# 大問Ⅰ 専用レンダラー
# ---------------------------------------------------------------------------

def blankify(text):
    """会話本文中の ( N ) を空所チップに変換する。"""
    def repl(m):
        return f'<span class="blk">（&nbsp;{m.group(1)}&nbsp;）</span>'
    return BLANK_RE.sub(repl, esc(text))


def render_conv(conv):
    """1つの会話 + その Set語群 をレンダー。"""
    rows = []
    rows.append(f'<div class="wb-h">{esc(conv["title"])} — {esc(conv["setting"])}</div>')
    # 会話本体
    lines_html = []
    for spk, txt in conv["lines"]:
        lines_html.append(
            f'<div class="cv-line"><span class="cv-spk">{esc(spk)}:</span>'
            f'<span class="cv-txt">{blankify(txt)}</span></div>'
        )
    body = "".join(lines_html)
    # 語群
    chips = "".join(
        f'<span class="chip"><b>{esc(lab)}</b>{esc(w)}</span>'
        for lab, w in conv["bank"]
    )
    setname = conv["set"]
    return f"""
<div class="conv-wrap">
  <div class="cv-h">{esc(conv["title"])}<span class="cv-scene">{esc(conv["setting"])}</span></div>
  <div class="cv-body">{body}</div>
  <div class="wordbank">
    <div class="wb-h">語群 Set {esc(setname)}（各語は一度だけ使用。2語は使わない）</div>
    <div class="wb-b"><div class="wb-row">{chips}</div></div>
  </div>
</div>
"""


def render_problem(s, idx):
    head = f"""
<div class="prob-head">
  <div class="id">SET {idx:02d}</div>
  <div class="meta"><span class="ttl">{esc(s['theme'])}</span><span>{esc(s['scene'])}</span></div>
  <div class="limit">{esc(s['limit'])}</div>
</div>
"""
    convs = "".join(render_conv(c) for c in s["convs"])
    instr = ('<p class="cv-instr">次の2つの会話を読み、空所（ 1 ）〜（ 13 ）に入る最も適切な語句を、'
             'それぞれの Set の語群から1つずつ選べ。各語は一度だけ使い、各 Set には使わない語が2語ある。</p>')
    return f'<div class="prob avoid-head">{head}{instr}{convs}</div>'


def render_key_table(s, idx):
    """解答一覧（13マーク）。"""
    cells = []
    for c in s["convs"]:
        for n, w in sorted(c["answers"].items()):
            cells.append((n, w))
    cells.sort()
    # 2段組の表
    ths = "".join(f"<th>{n}</th>" for n, _ in cells)
    tds = "".join(f'<td class="w">{esc(w)}</td>' for _, w in cells)
    return f"""
<table class="keytable">
  <tr><th style="background:var(--gold-deep)">空所</th>{ths}</tr>
  <tr><td style="font-weight:700;color:var(--navy)">解答</td>{tds}</tr>
</table>
"""


def render_answer(s, idx):
    parts = [f"""
<div class="ans-head"><div class="id">SET {idx:02d}</div>
  <div class="ttl">{esc(s['theme'])}</div></div>
"""]
    parts.append(render_key_table(s, idx))
    # 会話ごとの解説
    for c in s["convs"]:
        parts.append(f'<div class="miniband">{esc(c["title"])}（Set {esc(c["set"])}）— 空所別の根拠</div>')
        for n in sorted(c["answers"].keys()):
            e = c["exp"][n]
            row = [f'<div class="ex-q"><span class="badge">空所 {n}</span>正解 '
                   f'<span style="color:var(--vermilion)">{esc(c["answers"][n])}</span></div>']
            row.append(f'<div class="exp">')
            row.append(f'<p><span class="ex-lab">枠</span>{_raw(e["frame"])}</p>')
            row.append(f'<p><span class="ex-lab">論理</span>{_raw(e["logic"])}</p>')
            if e.get("trap"):
                row.append(f'<p><span class="ex-lab ng">切り</span>{_raw(e["trap"])}</p>')
            row.append('</div>')
            parts.append("".join(row))
        # 不要選択肢
        if c.get("unused"):
            parts.append(C.warn("使わない2語（ここで炙り出す）", _raw(c["unused"])))
        # 全訳
        if c.get("trans"):
            parts.append(f'<div class="trans"><div class="tr-t">全訳 — {esc(c["title"])}</div>{_raw(c["trans"])}</div>')
        # 語彙
        if c.get("vocab"):
            parts.append(render_vocab(c["vocab"]))
    if s.get("lesson"):
        parts.append(C.callout("このセットで持ち帰る型", _raw(s["lesson"])))
    return '<div class="ans">' + "".join(parts) + "</div>"


def render_vocab(rows):
    trs = "".join(
        f'<tr><td class="w">{esc(w)}</td><td class="p">{esc(pos)}</td><td>{_raw(mean)}</td></tr>'
        for w, pos, mean in rows
    )
    return f"""
<table class="vocab"><thead><tr><th style="width:32mm">語句</th><th style="width:14mm">品詞</th><th>意味・使い方</th></tr></thead>
<tbody>{trs}</tbody></table>
"""


# ---------------------------------------------------------------------------
# 追加CSS（大問Ⅰ固有）
# ---------------------------------------------------------------------------
EXTRA_CSS = """
.conv-wrap{ margin:3mm 0 4mm; }
.cv-h{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:10pt; color:var(--navy);
       border-bottom:1.2pt solid var(--gold); padding-bottom:1mm; margin:3mm 0 2mm; }
.cv-h .cv-scene{ font-weight:400; font-size:8.4pt; color:var(--gray); margin-left:3mm; }
.cv-body{ border:0.6pt solid var(--line); background:#fffdf8; padding:3.5mm 4.5mm; }
.cv-line{ font-family:"Noto Serif CJK JP","Times New Roman",serif; font-size:9.7pt; line-height:1.9;
       padding:.6mm 0 .6mm 15mm; text-indent:-15mm; }
.cv-spk{ font-family:"Noto Sans CJK JP"; font-weight:700; color:var(--navy-soft); font-size:8.8pt;
       display:inline-block; min-width:13mm; }
.cv-txt{ }
.cv-instr{ font-family:"Noto Sans CJK JP"; font-size:8.8pt; color:var(--ink); background:var(--washi);
       border-left:3pt solid var(--navy); padding:2mm 3.5mm; margin:2mm 0 3mm; line-height:1.7; }
.ex-lab{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8pt; color:#fff; background:var(--navy-soft);
       border-radius:1mm; padding:0 1.6mm; margin-right:2mm; }
.ex-lab.ng{ background:var(--vermilion); }
.exp p{ margin:.8mm 0; }
.avoid-head .prob-head{ page-break-after:avoid; }
"""

# ---------------------------------------------------------------------------
# データ（PROBLEMS）は別ファイルから読み込む
# ---------------------------------------------------------------------------
from daimon1_data import PROBLEMS, FRONT, STRATEGY, APPENDIX


def build():
    css = C.build_css(RUNNING) + EXTRA_CSS
    body = []
    # 表紙
    body.append(C.cover("第 3 部 - Ⅰ / 大問Ⅰ", "会話文 Set選択補充 攻略ドリル", RUNNING, badge="会話文"))
    # 前付け
    body.append(FRONT)
    # 戦略章
    body.append(STRATEGY)
    # 問題編
    body.append(C.chapter("PROBLEMS / 問題編",
        "成蹊型 会話文Set補充 — オリジナル演習 12セット",
        "ここからは実戦だ。各セットは会話2本・空所13・語群Set A/Bで、成蹊大問Ⅰの形式を忠実に再現している。"
        "目標時間内に、品詞仕分け→確信空所の固定→不要2語の炙り出し、の手順で解け。解答解説は後半にまとめてある。"))
    for i, s in enumerate(PROBLEMS, 1):
        body.append(render_problem(s, i))
    # 解答解説編
    body.append(C.chapter("ANSWERS / 解答解説編",
        "全13空所 × 12セット — 根拠と切り方の完全解剖",
        "空所ごとに「文法枠・会話論理・誤答の切り方」を分解する。単なる正誤ではなく、"
        "本番で同じ判断を再現するための手順に落とし込め。使わない2語の理由まで詰めて、消去法を体で覚える。"))
    for i, s in enumerate(PROBLEMS, 1):
        body.append(render_answer(s, i))
    # 付録
    body.append(APPENDIX)

    html = C.document(css, body)
    C.write_pdf(html, OUT)
    print("built:", OUT)


if __name__ == "__main__":
    build()
