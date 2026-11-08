# -*- coding: utf-8 -*-
"""原稿を四六判で組んだときの行数とページ数を、改行の扱い別に出す。
book/ で実行。引数に原稿のパス（省略で序章）。

字数割りではなく行数割りで数える。
改行を1つ入れると、その行の残りは空白になる。そこが字数割りでは見えない。
"""
import re, sys, math, io

SRC = sys.argv[1] if len(sys.argv) > 1 else "manuscript/序章_v7.md"

# 四六判 9.5pt 縦組みの想定を2つ
SET = [("ゆったり組み　40字×15行", 40, 15),
       ("標準組み　　　43字×17行", 43, 17)]

lines = io.open(SRC, encoding="utf-8").read().split("\n")

def width(s):
    """全角を1、半角を0.5で数える"""
    return sum(0.5 if ord(c) < 0x3000 and c.isascii() else 1 for c in s)

def count(cpl, policy):
    """A 改行も空行もすべて生かす（原稿のまま）
       B 段落内だけ流し込む。空行は1行アキとして残す
       C 空行も改行も全部つぶす。節の中は1段落に流し込む（圧縮の下限）"""
    n, i, N = 0, 0, len(lines)
    para = []
    def flush():
        nonlocal n, para
        if not para: return
        if policy == "A":
            for l in para:
                n += max(1, math.ceil(width(l) / cpl))
        else:
            total = sum(width(l) for l in para)
            n += max(1, math.ceil(total / cpl))
        para = []
    while i < N:
        l = lines[i].rstrip()
        if l.startswith("```"):                      # 囲み（図・表）はそのまま
            flush(); i += 1; inner = 0
            while i < N and not lines[i].startswith("```"):
                inner += max(1, math.ceil(width(lines[i].rstrip()) / cpl)); i += 1
            i += 1
            n += inner + 2                            # 囲みの上下アキ
            continue
        if re.match(r'^#{1,3}\s', l):                # 見出しは前アキ＋本体
            flush(); n += 3; i += 1; continue
        if re.match(r'^\s*---\s*$', l):              # 区切り
            flush(); n += 2; i += 1; continue
        if not l.strip():
            if policy == "C":                        # 空行を段落切れにしない
                i += 1; continue
            flush()
            if policy == "A": n += 1                 # 1行アキとして残す
            i += 1; continue
        para.append(l); i += 1
    flush()
    return n

ws = re.compile(r'\s')
zi = len(ws.sub('', "\n".join(lines)))
print(f"{SRC}　{zi:,}字")
print()
for name, cpl, lpp in SET:
    a, b, c = count(cpl, "A"), count(cpl, "B"), count(cpl, "C")
    pa, pb, pc = (math.ceil(x / lpp) for x in (a, b, c))
    print(f"  {name}（1ページ {cpl*lpp}字）")
    print(f"    A 原稿のまま（改行も空行も全部生かす）　{a:4d}行　{pa:3d}ページ")
    print(f"    B 空行は残し、段落内だけ流し込む　　　　{b:4d}行　{pb:3d}ページ")
    print(f"    C 改行も空行も全部つぶす　　　　　　　　{c:4d}行　{pc:3d}ページ")
    print(f"    A は C の {pa/pc:.1f} 倍")
    print()
