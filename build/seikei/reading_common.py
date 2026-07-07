# -*- coding: utf-8 -*-
"""
長文読解系（大問Ⅱ・Ⅲ・Ⅳ）共通レンダラー。
本文（段落番号・下線・空所付き）と設問（多肢選択）と解説をデータ駆動で組む。
"""
import re
import seikei_common as C
from seikei_common import esc, _raw

CIRCLED = {1:"①",2:"②",3:"③",4:"④",5:"⑤",6:"⑥",7:"⑦",8:"⑧",9:"⑨",10:"⑩"}
CHOICE_LABELS = ["ア", "イ", "ウ", "エ", "オ", "カ"]

# 本文マークアップ記法（データ内で使う軽量タグ）:
#   [[u:14]]phrase[[/u]]   下線部（設問番号14）
#   [[b:41]]                空所（番号41）
#   {{word}}               太字強調（本文中のキーワード等）は使わず、素の英文推奨
U_OPEN = re.compile(r"\[\[u:(\d+)\]\]")
U_CLOSE = re.compile(r"\[\[/u\]\]")
BLANK = re.compile(r"\[\[b:(\d+)\]\]")


def markup(text):
    """本文の軽量タグをHTMLへ。"""
    s = esc(text)
    # weasyのescで [[ ]] はそのまま残る
    s = U_OPEN.sub(lambda m: f'<span class="ul">', s)
    s = U_CLOSE.sub('<span class="ulmark">'+"</span></span>", s)  # placeholder, fixed below
    # 上のやり方だと下線番号が消えるので作り直す
    return s


def render_passage(passage, title=None, wordcount=None):
    """passage: list of paragraph strings（軽量タグ入り）。段落番号を付す。"""
    paras = []
    for i, para in enumerate(passage, 1):
        html = _passage_markup(para)
        paras.append(f'<p><span class="pno">[{i}]</span>{html}</p>')
    head = ""
    if title:
        wc = f'<span style="font-weight:400;font-size:8pt;color:var(--gray)">　（約{wordcount} words）</span>' if wordcount else ""
        head = f'<div class="ttl">{esc(title)}{wc}</div>'
    return f'<div class="passage">{head}{"".join(paras)}</div>'


def _passage_markup(text):
    """[[u:N]]...[[/u]] を下線＋上付き番号に、[[b:N]] を空所チップに変換。"""
    # まずエスケープ
    s = esc(text)
    # 下線開始：番号を上付きで下線の頭に付ける
    s = re.sub(r"\[\[u:(\d+)\]\]", lambda m: f'<span class="ul"><span class="ulmark">({m.group(1)})</span>', s)
    s = s.replace("[[/u]]", "</span>")
    # 空所
    s = re.sub(r"\[\[b:(\d+)\]\]", lambda m: f'<span class="blk">（&nbsp;{m.group(1)}&nbsp;）</span>', s)
    return s


def distribute(q):
    """著者が指定した正解を、設問番号から決まる位置へ機械的に移動し、
    正解が常に「ア」に偏らないよう分散させる（決定論的・再ビルドで不変）。
    戻り値: (表示用choicesリスト, 正解ラベル)。"""
    choices = q["choices"]
    n = len(choices)
    ci = CHOICE_LABELS.index(q["answer"]) if q["answer"] in CHOICE_LABELS else 0
    correct = choices[ci]
    rest = [c for i, c in enumerate(choices) if i != ci]
    t = q["no"] % n
    disp, ri = [], 0
    for pos in range(n):
        if pos == t:
            disp.append(correct)
        else:
            disp.append(rest[ri]); ri += 1
    return disp, CHOICE_LABELS[t]


def render_question(q):
    """設問1つ。q: {no,tag,stem,choices,answer,(inline)} 。"""
    label = f'<span class="mk">{esc(q.get("tag",""))}</span>' if q.get("tag") else ""
    stem = f'<div class="qh">{label}問{q["no"]}　{_raw(q["stem"])}</div>'
    cls = "choices inline" if q.get("inline") else "choices"
    disp, _ = distribute(q)
    chs = []
    for i, ch in enumerate(disp):
        lab = CHOICE_LABELS[i]
        chs.append(f'<div class="ch"><span class="lab">{lab}.</span>{_raw(ch)}</div>')
    return f'<div class="q">{stem}<div class="{cls}">{"".join(chs)}</div></div>'


def render_problem_block(pset, idx, kind_label):
    """1つの読解セット（本文＋設問群）の問題編。"""
    head = f"""
<div class="prob-head">
  <div class="id">READING {idx:02d}</div>
  <div class="meta"><span class="ttl">{esc(pset['theme'])}</span><span>{esc(pset.get('genre',''))}</span></div>
  <div class="limit">{esc(pset.get('limit',''))}</div>
</div>
"""
    instr = f'<p class="cv-instr">{_raw(pset.get("instr", kind_label))}</p>'
    passage = render_passage(pset["passage"], pset.get("passage_title"), pset.get("wordcount"))
    qs = "".join(render_question(q) for q in pset["questions"])
    qhead = '<div class="miniband" style="margin-top:4mm">設問</div>'
    return f'<div class="prob">{head}{instr}{passage}{qhead}{qs}</div>'


def render_answer_key(pset):
    cells = [(q["no"], distribute(q)[1]) for q in pset["questions"]]
    ths = "".join(f"<th>{n}</th>" for n, _ in cells)
    tds = "".join(f'<td class="ans">{esc(a)}</td>' for _, a in cells)
    return (f'<table class="keytable"><tr><th style="background:var(--gold-deep)">問</th>{ths}</tr>'
            f'<tr><td style="font-weight:700;color:var(--navy)">解答</td>{tds}</tr></table>')


def render_answer_block(pset, idx):
    parts = [f'<div class="ans-head"><div class="id">READING {idx:02d}</div>'
             f'<div class="ttl">{esc(pset["theme"])}</div></div>']
    parts.append(render_answer_key(pset))
    # 構造図解
    if pset.get("structure"):
        parts.append(C.callout("パラグラフ構造図解", _raw(pset["structure"])))
    # 各設問解説
    parts.append('<div class="miniband">設問別 解説 ― 根拠と切り方</div>')
    for q in pset["questions"]:
        _, lab = distribute(q)
        head = (f'<div class="ex-q"><span class="badge">問{q["no"]}'
                f'{" / "+esc(q["tag"]) if q.get("tag") else ""}</span>'
                f'正解 <span style="color:var(--vermilion)">{esc(lab)}</span></div>')
        parts.append(head)
        body = ['<div class="exp">']
        if q.get("basis"):
            body.append(f'<p><span class="ex-lab">根拠</span>{_raw(q["basis"])}</p>')
        if q.get("solve"):
            body.append(f'<p><span class="ex-lab">解法</span>{_raw(q["solve"])}</p>')
        if q.get("cut"):
            body.append(f'<p><span class="ex-lab ng">切り</span>{_raw(q["cut"])}</p>')
        body.append('</div>')
        parts.append("".join(body))
    # 全訳
    if pset.get("trans"):
        tr = "".join(f'<p><span class="pno">[{i}]</span>{_raw(t)}</p>'
                     for i, t in enumerate(pset["trans"], 1))
        parts.append(f'<div class="trans"><div class="tr-t">全訳</div>{tr}</div>')
    # 語彙
    if pset.get("vocab"):
        parts.append(render_vocab(pset["vocab"]))
    if pset.get("lesson"):
        parts.append(C.win("このセットで持ち帰る型", _raw(pset["lesson"])))
    return '<div class="ans">' + "".join(parts) + "</div>"


def render_vocab(rows):
    trs = "".join(
        f'<tr><td class="w">{esc(w)}</td><td class="p">{esc(pos)}</td><td>{_raw(mean)}</td></tr>'
        for w, pos, mean in rows
    )
    return (f'<table class="vocab"><thead><tr><th style="width:34mm">語句</th>'
            f'<th style="width:13mm">品詞</th><th>意味</th></tr></thead><tbody>{trs}</tbody></table>')


READING_EXTRA_CSS = """
.passage .ttl{ border-bottom:0.6pt solid var(--line); padding-bottom:1.5mm; }
.cv-instr{ font-family:"Noto Sans CJK JP"; font-size:8.8pt; color:var(--ink); background:var(--washi);
       border-left:3pt solid var(--navy); padding:2mm 3.5mm; margin:2mm 0 3mm; line-height:1.7; }
.ex-lab{ font-family:"Noto Sans CJK JP"; font-weight:700; font-size:8pt; color:#fff; background:var(--navy-soft);
       border-radius:1mm; padding:0 1.6mm; margin-right:2mm; white-space:nowrap; }
.ex-lab.ng{ background:var(--vermilion); }
.exp p{ margin:.8mm 0; }
.trans .pno{ color:var(--gold-deep); font-weight:700; }
"""
