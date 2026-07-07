# -*- coding: utf-8 -*-
"""
成蹊大学 経営学部 英語 完全攻略マニュアル
第3部-Ⅳ 大問Ⅳ「長文空所補充」完全攻略ドリル

大問Ⅳ（解答番号41〜44・4マーク）＝短めの英文2本に、各2空所。
語彙空所（1語）＋文選択空所（1文）を、段落の論理展開で補う。堅実な得点源。
本冊は成蹊型オリジナルの短文2本セットを多数収録し、論理接続で解く型を体に入れる。
"""
import seikei_common as C
import reading_common as R
from seikei_common import esc, _raw

RUNNING = "成蹊大学 経営学部 英語 完全攻略マニュアル【第3部-Ⅳ】大問Ⅳ 長文空所補充ドリル"
OUT = "/home/user/thinking-hp/dist/成蹊大学_経営学部_英語_完全攻略マニュアル_第3部-Ⅳ_大問Ⅳ長文空所補充ドリル.pdf"


# ---------------------------------------------------------------------------
# 大問Ⅳ 専用レンダラー（短文2本セット）
# ---------------------------------------------------------------------------

def _render_text(t):
    paras = "".join(
        f'<p><span class="pno">[{i}]</span>{R._passage_markup(p)}</p>'
        for i, p in enumerate(t["paras"], 1)
    )
    wc = f'<span style="font-weight:400;font-size:8pt;color:var(--gray)">　（約{t["wordcount"]} words）</span>' if t.get("wordcount") else ""
    ttl = f'<div class="ttl">{esc(t.get("label",""))}　{esc(t.get("title",""))}{wc}</div>'
    return f'<div class="passage">{ttl}{paras}</div>'


def render_problem(s, idx):
    head = f"""
<div class="prob-head">
  <div class="id">SET {idx:02d}</div>
  <div class="meta"><span class="ttl">{esc(s['theme'])}</span><span>{esc(s.get('genre',''))}</span></div>
  <div class="limit">{esc(s.get('limit',''))}</div>
</div>
"""
    instr = ('<p class="cv-instr">次の短い英文2本を読み、各空所に入る最も適切なもの（語または文）を選べ。'
             '空所前後の論理接続（逆接・因果・例示・言い換え）を先につかむこと。</p>')
    texts = "".join(_render_text(t) for t in s["texts"])
    qs = "".join(R.render_question(q) for q in s["questions"])
    qhead = '<div class="miniband" style="margin-top:3mm">設問</div>'
    return f'<div class="prob">{head}{instr}{texts}{qhead}{qs}</div>'


def render_answer(s, idx):
    parts = [f'<div class="ans-head"><div class="id">SET {idx:02d}</div>'
             f'<div class="ttl">{esc(s["theme"])}</div></div>']
    parts.append(R.render_answer_key(s))
    parts.append('<div class="miniband">空所別 解説 ― 論理接続で解く</div>')
    for q in s["questions"]:
        _, lab = R.distribute(q)
        parts.append(f'<div class="ex-q"><span class="badge">空所{q["no"]}'
                     f'{" / "+esc(q["tag"]) if q.get("tag") else ""}</span>'
                     f'正解 <span style="color:var(--vermilion)">{esc(lab)}</span></div>')
        body = ['<div class="exp">']
        if q.get("basis"):
            body.append(f'<p><span class="ex-lab">接続</span>{_raw(q["basis"])}</p>')
        if q.get("solve"):
            body.append(f'<p><span class="ex-lab">解法</span>{_raw(q["solve"])}</p>')
        if q.get("cut"):
            body.append(f'<p><span class="ex-lab ng">切り</span>{_raw(q["cut"])}</p>')
        body.append('</div>')
        parts.append("".join(body))
    if s.get("trans"):
        tr = "".join(f'<p><b>{esc(lbl)}</b>　{_raw(t)}</p>' for lbl, t in s["trans"])
        parts.append(f'<div class="trans"><div class="tr-t">全訳</div>{tr}</div>')
    if s.get("vocab"):
        parts.append(R.render_vocab(s["vocab"]))
    if s.get("lesson"):
        parts.append(C.win("このセットで持ち帰る型", _raw(s["lesson"])))
    return '<div class="ans">' + "".join(parts) + "</div>"


# ---------------------------------------------------------------------------
# 前付け・戦略
# ---------------------------------------------------------------------------
FRONT = "".join([
    '<section style="page-break-before:always"></section>',
    C.h2("はじめに ― 大問Ⅳは「論理接続」で確実に取る得点源"),
    C.p("成蹊 経営の大問Ⅳ（解答番号41〜44・<b>4マーク</b>）は、短めの英文2本に各2空所。"
        "空所には<b>1語（語彙空所）</b>または<b>1文（文選択空所）</b>が入る。"
        "長文ほど時間はかからず、<b>段落の論理展開</b>をつかめば堅実に取れる『取り所』だ。"),
    C.p("鍵は、空所の前後にある<b>接続関係</b>を先に読むこと。逆接（but/however）、因果（so/therefore）、"
        "例示（for example）、言い換え（in other words）――この矢印が見えれば、"
        "語彙空所はコロケーションと文脈で、文選択空所は前後の論理整合で、ほぼ一意に決まる。"),
    C.callout("この巻の到達目標", C.dots([
        "空所前後の<b>接続語・論理の矢印</b>を先に把握してから選ぶ習慣をつける。",
        "語彙空所（コロケ＋文脈）と文選択空所（論理整合）を別の手順で処理できるようにする。",
        "4マークを<b>3以上（75%）</b>安定させ、Ⅳを短時間で取り切る。",
    ])),
    C.p("本巻は完全オリジナルの成蹊型『短文2本』セットを多数収録する。各セットは6空所（語彙4＋文選択2の混成）で、"
        "成蹊Ⅳの形式・難度を再現している。実際の過去問は転載していない。"),
    C.box("この巻の使い方", C.steps([
        "第0章「Ⅳ型の解法」で、語彙空所と文選択空所の手順を分けて覚える。",
        "1セット（短文2本）を<b>目標6分</b>で解く。まず接続語に印をつける。",
        "答え合わせは解説の「接続・解法・切り」を精読。<b>なぜその論理でその答えか</b>を言語化する。",
    ])),
    C.h2("目次"),
    '<div class="toc">',
    '<div class="row"><span class="n">第0章</span><span class="t">Ⅳ型の解法 ― 語彙空所と文選択空所</span><span class="pg">strategy</span></div>',
    '<div class="row"><span class="n">問題編</span><span class="t">成蹊型オリジナル短文2本セット SET 01〜</span><span class="pg">problems</span></div>',
    '<div class="row"><span class="n">解説編</span><span class="t">空所別の論理接続と根拠＋全訳</span><span class="pg">answers</span></div>',
    '<div class="row"><span class="n">付録</span><span class="t">論理マーカー一覧 ／ 文選択空所チェックリスト</span><span class="pg">appendix</span></div>',
    '</div>',
])

STRATEGY = "".join([
    C.chapter("CHAPTER 0 / 解法の型",
        "Ⅳ型の解法 ― 論理接続で空所を一意に決める",
        "空所補充は『なんとなく合いそう』で選ぶと落とす。前後の接続関係という客観的な手がかりを先に読めば、"
        "答えは一つに絞れる。語彙空所と文選択空所で手順を分けるのがコツだ。"),
    C.miniband("0-1 まず接続語に印 ― 論理の矢印を可視化する"),
    C.p("空所を見たら、<b>まず前後の接続語</b>に印をつける。論理の向きが分かれば候補は半減する。"),
    C.table(
        ["論理", "マーカー", "空所への効き方"],
        [
            ["逆接", "but / however / yet / although", "前と<b>反対</b>の内容・語が入る。"],
            ["因果", "so / therefore / thus / because", "前の<b>結果・原因</b>が入る。"],
            ["例示", "for example / such as", "前の一般論の<b>具体例</b>が入る。"],
            ["言い換え", "in other words / that is", "前と<b>同義</b>の内容が入る。"],
            ["追加", "moreover / in addition / also", "前と<b>同方向</b>の内容が入る。"],
        ],
        [None, None, None]),
    C.miniband("0-2 語彙空所（1語）の手順"),
    C.box("語彙空所", C.dots([
        "空所前後の<b>コロケーション</b>（動詞＋名詞、形容詞＋名詞）を確認。",
        "接続語が示す<b>論理の向き</b>（逆接なら反対語）に合う語を選ぶ。",
        "各選択肢を入れて読み、話の筋が最も自然に通る1つを残す。",
    ])),
    C.miniband("0-3 文選択空所（1文）の手順"),
    C.box("文選択空所", C.dots([
        "空所の<b>直前・直後</b>の文と論理がつながる1文を選ぶ（代名詞・指示語の一致も確認）。",
        "空所が<b>段落の要点・結論</b>か、<b>具体例・補足</b>かを見極める。",
        "選択肢を入れて前後を音読し、話の流れが途切れないものを選ぶ。",
    ])),
    C.warn("Ⅳで落ちる典型",
        C.p("①接続語を見ずに『意味が近い』だけで選ぶ　②文選択空所で代名詞の一致を確認しない　"
            "③1語空所に気を取られ、より確実な文選択空所を落とす。"
            "対策：空所を見たら必ず接続語→論理の向き→代入確認、の順を踏む。")),
    C.callout("この章の結論",
        C.p("Ⅳは短く確実な<b>取り所</b>。前後の接続関係という客観的手がかりで、"
            "語彙空所も文選択空所も一意に決まる。次ページからは実戦だ。"
            "空所を見たら、まず接続語に印。")),
])

import importlib, os
PROBLEMS = []
_here = os.path.dirname(__file__)
for _n in range(1, 25):
    _path = os.path.join(_here, "d4_sets", f"set_{_n:02d}.py")
    if os.path.exists(_path):
        _m = importlib.import_module(f"d4_sets.set_{_n:02d}")
        PROBLEMS.append(_m.SET)

try:
    from d4_appendix import APPENDIX
except Exception:
    APPENDIX = ""


def build():
    css = C.build_css(RUNNING) + R.READING_EXTRA_CSS
    body = []
    body.append(C.cover("第 3 部 - Ⅳ / 大問Ⅳ", "長文空所補充 攻略ドリル", RUNNING, badge="空所補充"))
    body.append(FRONT)
    body.append(STRATEGY)
    body.append(C.chapter("PROBLEMS / 問題編",
        "成蹊型 短文2本 空所補充 ― オリジナル演習",
        "各セットは短い英文2本・空所6（語彙4＋文選択2）で、成蹊Ⅳの形式を再現している。"
        "空所を見たらまず接続語に印をつけ、論理の矢印で候補を絞れ。目標は1セット6分・3/4マーク以上。"))
    for i, s in enumerate(PROBLEMS, 1):
        body.append(render_problem(s, i))
    body.append(C.chapter("ANSWERS / 解答解説編",
        "全空所 × 全セット ― 論理接続の完全解剖",
        "空所ごとに『前後の接続関係・解法・誤答の切り方』を分解する。語彙空所はコロケと論理、"
        "文選択空所は前後整合。なぜその論理でその答えかを、本文の接続語で押さえろ。"))
    for i, s in enumerate(PROBLEMS, 1):
        body.append(render_answer(s, i))
    body.append(APPENDIX)
    html = C.document(css, body)
    C.write_pdf(html, OUT)
    print("built:", OUT, "sets:", len(PROBLEMS))


if __name__ == "__main__":
    build()
