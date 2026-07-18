#!/usr/bin/env python3
"""60文の問題集PDF用HTMLを生成する。
各文: 問題ページ →(改ページ)→ 解答・解説ページ の順で独立配置。
"""
import json, html
from pathlib import Path

BASE = Path('/tmp/claude-0/-home-user-thinking-hp/5f12d2a1-7df4-5ffd-924b-ed23125eba30/scratchpad')
RES = BASE / 'results'
OUT = BASE / 'booklet.html'

def esc(s): return html.escape(str(s))

entries = [json.load(open(RES / f'q{n}.json', encoding='utf-8')) for n in range(1, 61)]

CSS = """
@page { size: A4; margin: 16mm 15mm 18mm; }
* { box-sizing: border-box; }
body { font-family: "IPAGothic", sans-serif; font-size: 10.5pt; line-height: 1.7; color: #1b1b1b; margin: 0; }
.en, .choice-en { font-family: "DejaVu Serif","Times New Roman",serif; }
.cover { text-align: center; padding-top: 70mm; }
.cover h1 { font-size: 26pt; letter-spacing: 2px; margin: 0 0 6px; }
.cover .sub { font-size: 12pt; color: #555; }
.cover .rule { font-size: 10pt; color: #888; margin-top: 40mm; line-height: 1.9; }
.page { break-before: page; }
.sec-head { display: flex; align-items: baseline; gap: 10px; border-bottom: 2.5px solid #1b1b1b; padding-bottom: 5px; margin-bottom: 12px; }
.sec-head .no { font-size: 15pt; font-weight: bold; background: #1b1b1b; color: #fff; padding: 1px 12px; }
.sec-head .kind { font-size: 10pt; color: #666; }
.sec-head .kind.ans { color: #b00000; font-weight: bold; }
.passage { border: 1.2px solid #333; border-left: 6px solid #333; padding: 10px 14px; margin: 8px 0 4px; font-size: 11.5pt; line-height: 1.95; }
.yaku { font-size: 9.5pt; color: #555; padding: 4px 4px 0; margin-bottom: 14px; }
.yaku .lbl { font-weight: bold; color: #333; }
.q { margin: 0 0 14px; break-inside: avoid; }
.q .qhead { font-weight: bold; margin-bottom: 3px; }
.q .qtag { font-size: 8pt; color: #888; font-weight: normal; margin-left: 6px; }
.q .qtext { margin-bottom: 5px; }
ol.choices { list-style: none; padding-left: 1.4em; margin: 3px 0; }
ol.choices li { margin: 2.5px 0; text-indent: -1.4em; padding-left: 1.4em; }
ol.choices .mk { display: inline-block; width: 1.4em; font-weight: bold; }
.ansrow { display: flex; align-items: baseline; gap: 8px; margin: 6px 0 3px; }
.ansrow .lab { font-weight: bold; font-size: 10pt; }
.ansrow .val { font-size: 13pt; font-weight: bold; color: #b00000; }
.correct-choice { background: #fdeaea; }
.exp { background: #f6f6f4; border: 1px solid #ccc; padding: 7px 11px; margin: 2px 0 12px; font-size: 9.7pt; line-height: 1.65; }
.exp .lbl { font-weight: bold; color: #333; }
.answer-block { break-inside: avoid; margin-bottom: 10px; }
.footer-note { text-align:center; font-size: 8.5pt; color: #aaa; margin-top: 6px; }
"""

def render_choices(q, correct=None):
    out = ['<ol class="choices">']
    for L in 'abcd':
        cls = ' class="correct-choice"' if correct == L.upper() else ''
        # detect if choice is mostly English (contains latin + space, few kana) -> use serif
        txt = esc(q[L])
        out.append(f'<li{cls}><span class="mk">{L.upper()}.</span>{txt}</li>')
    out.append('</ol>')
    return '\n'.join(out)

parts = [f'<style>{CSS}</style>']

# cover
parts.append("""
<div class="cover">
  <h1>SMART STUDY ENGLISH</h1>
  <div class="sub">英文解釈 確認問題集 &nbsp;No.1 – 60</div>
  <div class="sub" style="font-size:10pt;margin-top:8px;">全174問・全問客観式(4択)</div>
  <div class="rule">
    ● 訳の暗記ではなく、英文そのものを読んで答える問題です。<br>
    ● 各文は「問題ページ」→「解答・解説ページ」の順に独立して並んでいます。<br>
    ● まず問題を解き、次のページで答え合わせと解説を確認しましょう。
  </div>
</div>
""")

for e in entries:
    no = e['no']; en = esc(e['en']); ja = esc(e['ja']); qs = e['questions']
    # --- problem page ---
    p = [f'<div class="page">']
    p.append(f'<div class="sec-head"><span class="no">No.{no}</span><span class="kind">問題</span></div>')
    p.append(f'<div class="passage en">{en}</div>')
    for i, q in enumerate(qs, 1):
        p.append('<div class="q">')
        p.append(f'<div class="qhead">問{i}<span class="qtag">［{esc(q["tag"])}］</span></div>')
        p.append(f'<div class="qtext">{esc(q["q"])}</div>')
        p.append(render_choices(q))
        p.append('</div>')
    p.append('<div class="footer-note">— 解答・解説は次のページ —</div>')
    p.append('</div>')
    parts.append('\n'.join(p))
    # --- answer page ---
    a = [f'<div class="page">']
    a.append(f'<div class="sec-head"><span class="no">No.{no}</span><span class="kind ans">解答・解説</span></div>')
    a.append(f'<div class="passage en" style="border-left-color:#b00000;">{en}</div>')
    a.append(f'<div class="yaku"><span class="lbl">訳:</span> {ja}</div>')
    for i, q in enumerate(qs, 1):
        cor = q['answer'].strip().upper()
        a.append('<div class="answer-block">')
        a.append(f'<div class="qhead">問{i}<span class="qtag">［{esc(q["tag"])}］</span></div>')
        a.append(render_choices(q, correct=cor))
        a.append(f'<div class="ansrow"><span class="lab">正解</span><span class="val">{cor}</span></div>')
        a.append(f'<div class="exp"><span class="lbl">解説:</span> {esc(q["explanation"])}</div>')
        a.append('</div>')
    a.append('</div>')
    parts.append('\n'.join(a))

OUT.write_text('\n'.join(parts), encoding='utf-8')
print('wrote', OUT, 'entries:', len(entries),
      'questions:', sum(len(e['questions']) for e in entries))
