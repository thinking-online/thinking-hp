# -*- coding: utf-8 -*-
"""四六判で組んだときのページ数を、行数で数える。

字数割り（520字/ページ）はやめた。改行を1つ入れるとその行の残りが空白になるが、
字数ではそれが見えない。実測すると最大2倍ずれる。

想定　四六判 9.5pt 縦組み　43字×17行（1ページ 731字が上限）

空行の扱い
　マークダウンの空行は段落の区切りなので、1行アキにはしない（字下げで切る）。
　段落の中の改行は、著者が意図して入れているので生かす。
　これが honor_breaks=True。組み方を変えて流し込む場合は False。
"""
import re, math

CPL, LPP = 43, 17          # 1行の字数 / 1ページの行数

def _w(s):
    return sum(0.5 if (ord(c) < 0x3000 and c.isascii()) else 1 for c in s)

def count_lines(text, cpl=CPL, honor_breaks=True):
    lines = text.split("\n")
    n, i, N = 0, 0, len(lines)
    para = []

    def flush():
        nonlocal n, para
        if not para: return
        if honor_breaks:
            for l in para:
                n += max(1, math.ceil(_w(l) / cpl))
        else:
            n += max(1, math.ceil(sum(_w(l) for l in para) / cpl))
        para.clear()

    while i < N:
        l = lines[i].rstrip()
        if l.startswith("```"):                       # 囲み。上下に1行ずつアキ
            flush(); i += 1; inner = 0
            while i < N and not lines[i].startswith("```"):
                inner += max(1, math.ceil(_w(lines[i].rstrip()) / cpl)); i += 1
            i += 1; n += inner + 2; continue
        if re.match(r'^#{1,6}\s', l):                 # 見出し。前アキ＋本体＋後アキ
            flush(); n += 3; i += 1; continue
        if re.match(r'^\s*---\s*$', l):               # 区切り
            flush(); n += 2; i += 1; continue
        if not l.strip():                             # 空行は段落の区切り
            flush(); i += 1; continue
        para.append(l); i += 1
    flush()
    return n

def pages(text, honor_breaks=True, lpp=LPP):
    return max(1, math.ceil(count_lines(text, honor_breaks=honor_breaks) / lpp))

def report(text, label=""):
    a = count_lines(text, honor_breaks=True)
    b = count_lines(text, honor_breaks=False)
    return (f"{label}　改行を生かす {math.ceil(a/LPP)}ページ　"
            f"／　流し込む {math.ceil(b/LPP)}ページ")
