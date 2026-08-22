#!/usr/bin/env python3
"""THINKING 英文解釈 問題集 — 問題編/解説編を別々のPDF用HTMLで生成。
4冊: 入門(問題/解説) と 基礎(問題/解説)。
"""
import json, html
from pathlib import Path

SP = Path('/tmp/claude-0/-home-user-thinking-hp/5f12d2a1-7df4-5ffd-924b-ed23125eba30/scratchpad')

def esc(s): return html.escape(str(s))

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm; }
* { box-sizing: border-box; }
body { font-family: "IPAGothic", sans-serif; font-size: 10.5pt; line-height: 1.7; color: #1b1b1b; margin: 0; }
.en { font-family: "DejaVu Serif","Times New Roman",serif; }
/* 表紙 */
.cover { height: 245mm; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; page-break-after: always; }
.cover .brand { font-family: "DejaVu Serif",serif; letter-spacing: 6px; font-size: 13pt; color: #b0895e; margin-bottom: 22px; }
.cover h1 { font-size: 30pt; margin: 0 0 10px; letter-spacing: 3px; }
.cover .kind { margin-top: 26px; font-size: 15pt; color: #fff; background: #1b1b1b; padding: 6px 30px; letter-spacing: 6px; }
.cover .meta { margin-top: 40mm; font-size: 10pt; color: #999; line-height: 2; }
.cover .accent { width: 54px; height: 3px; background: #b0895e; margin: 18px auto 0; }
/* 本文 */
.item { margin: 0 0 20px; padding-bottom: 16px; border-bottom: 1px dashed #cfcfcf; }
.item:last-child { border-bottom: none; }
.head { display: flex; align-items: baseline; gap: 10px; margin-bottom: 8px; break-after: avoid; }
.head .no { font-size: 12pt; font-weight: bold; background: #1b1b1b; color: #fff; padding: 1px 11px; letter-spacing: 1px; }
.head .no.ans { background: #b00000; }
.passage { border-left: 4px solid #1b1b1b; padding: 6px 0 6px 12px; margin: 4px 0 6px; font-size: 11.5pt; line-height: 1.9; break-inside: avoid; }
.passage.ans { border-left-color: #b00000; }
.yaku { font-size: 9.6pt; color: #444; margin: 2px 0 12px; line-height: 1.7; }
.yaku .lbl { font-weight: bold; color: #222; }
.q { margin: 0 0 11px; break-inside: avoid; }
.q .qhead { font-weight: bold; margin-bottom: 3px; }
.q .qtag { font-size: 8pt; color: #8a8a8a; font-weight: normal; margin-left: 6px; }
.q .qtext { margin-bottom: 4px; }
ol.choices { list-style: none; padding-left: 1.5em; margin: 3px 0; }
ol.choices li { margin: 2.5px 0; text-indent: -1.5em; padding-left: 1.5em; }
ol.choices .mk { display: inline-block; width: 1.5em; font-weight: bold; }
.correct { background: #fdeaea; }
.ansrow { margin: 5px 0 3px; }
.ansrow .lab { font-weight: bold; font-size: 9.5pt; }
.ansrow .val { font-size: 12.5pt; font-weight: bold; color: #b00000; margin-left: 6px; }
.exp { background: #f6f6f4; border: 1px solid #d8d8d3; padding: 7px 11px; margin: 2px 0 10px; font-size: 9.5pt; line-height: 1.62; break-inside: avoid; }
.exp .lbl { font-weight: bold; color: #222; }
"""

def choices_html(q, correct=None):
    out = ['<ol class="choices">']
    for L in 'abcd':
        cls = ' class="correct"' if correct == L.upper() else ''
        out.append(f'<li{cls}><span class="mk">{L.upper()}.</span>{esc(q[L])}</li>')
    out.append('</ol>')
    return ''.join(out)

def cover(title_main, kind_label, subtitle):
    return f"""<div class="cover">
  <div class="brand">THINKING</div>
  <h1>{esc(title_main)}</h1>
  <div class="accent"></div>
  <div class="kind">{esc(kind_label)}</div>
  <div class="meta">{esc(subtitle)}<br>全問客観式(4択)</div>
</div>"""

def build(entries, kind, title_main, kind_label, subtitle, out_html):
    parts = ['<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">',
             f'<style>{CSS}</style></head><body>']
    parts.append(cover(title_main, kind_label, subtitle))
    for e in entries:
        no, en, ja, qs = e['no'], esc(e['en']), esc(e['ja']), e['questions']
        parts.append('<div class="item">')
        if kind == 'problem':
            parts.append(f'<div class="head"><span class="no">No.{no}</span></div>')
            parts.append(f'<div class="passage en">{en}</div>')
            for i, q in enumerate(qs, 1):
                parts.append('<div class="q">')
                parts.append(f'<div class="qhead">問{i}<span class="qtag">［{esc(q["tag"])}］</span></div>')
                parts.append(f'<div class="qtext">{esc(q["q"])}</div>')
                parts.append(choices_html(q))
                parts.append('</div>')
        else:  # answer
            parts.append(f'<div class="head"><span class="no ans">No.{no}</span></div>')
            parts.append(f'<div class="passage en ans">{en}</div>')
            parts.append(f'<div class="yaku"><span class="lbl">訳:</span> {ja}</div>')
            for i, q in enumerate(qs, 1):
                cor = q['answer'].strip().upper()
                parts.append('<div class="q">')
                parts.append(f'<div class="qhead">問{i}<span class="qtag">［{esc(q["tag"])}］</span></div>')
                parts.append(choices_html(q, correct=cor))
                parts.append(f'<div class="ansrow"><span class="lab">正解</span><span class="val">{cor}</span></div>')
                parts.append(f'<div class="exp"><span class="lbl">解説:</span> {esc(q["explanation"])}</div>')
                parts.append('</div>')
        parts.append('</div>')
    parts.append('</body></html>')
    Path(out_html).write_text(''.join(parts), encoding='utf-8')
    return out_html

nyu = json.load(open(SP / 'nyumon60.json', encoding='utf-8'))
juk = json.load(open(SP / 'kiso70.json', encoding='utf-8'))

jobs = [
    (nyu, 'problem', '入門英文解釈', '問題編', '入門レベル｜No.1–60', SP / 'book_nyumon_q.html'),
    (nyu, 'answer',  '入門英文解釈', '解説編', '入門レベル｜No.1–60', SP / 'book_nyumon_a.html'),
    (juk, 'problem', '基礎英文解釈', '問題編', '基礎レベル｜No.1–70', SP / 'book_kiso_q.html'),
    (juk, 'answer',  '基礎英文解釈', '解説編', '基礎レベル｜No.1–70', SP / 'book_kiso_a.html'),
]
for entries, kind, tm, kl, sub, out in jobs:
    build(entries, kind, tm, kl, sub, out)
    print('wrote', out.name)
