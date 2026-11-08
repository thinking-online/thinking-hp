# -*- coding: utf-8 -*-
"""原稿を、本にする前提の組み方に寄せる。book/ で実行。

やること
　節（見出し・区切り・囲みで区切られた範囲）の中で、
　細かく割れた段落を1つの段落につなぐ。

つながないもの
　1　全角スペースで始まる行　　著者が意図して下げている（×／○、引用、強調）
　2　1行だけで、24字以内の段落　決め所。独立させる
　3　「か。」「か？」で終わる1行　読者への問いかけ
　4　囲みの中　　　　　　　　　 そのまま
　5　見出し・区切り　　　　　　 そのまま

使い方
　python3 scripts/shimeru.py --dry  差分の行数だけ見る
　python3 scripts/shimeru.py        実際に書き換える
"""
import re, sys, io, glob, os
sys.path.insert(0, "scripts")
import pages

KEEP_MAX = 12                       # この字数以内の1行段落は立てたまま

def is_standalone(para):
    """この段落は、独立させたままにするか"""
    if len(para) != 1:
        return False
    l = para[0]
    if l.startswith("　"):                       # 全角スペース始まり
        return True
    bare = l.strip().strip("　")
    if bare.endswith(("か。", "か？", "か", "？")):  # 問いかけ
        return True
    if len(bare) <= KEEP_MAX:                    # 短い決め所
        return True
    return False

def shimeru(text):
    lines = text.split("\n")
    out, i, N = [], 0, len(lines)
    buf = []            # いまの節にたまっている段落のリスト
    para = []

    def close_para():
        nonlocal para
        if para: buf.append(para); para = []

    def flush_section():
        """たまった段落を、つなげるものはつなげて出す"""
        nonlocal buf
        close_para()
        run = []
        for p in buf:
            if is_standalone(p):
                if run: out.append("".join(run)); out.append(""); run = []
                out.append(p[0]); out.append("")
            else:
                run.extend(x.strip() for x in p)
        if run: out.append("".join(run)); out.append("")
        buf = []

    while i < N:
        l = lines[i].rstrip()
        if l.startswith("```"):
            flush_section(); out.append(l); i += 1
            while i < N and not lines[i].startswith("```"):
                out.append(lines[i].rstrip()); i += 1
            if i < N: out.append(lines[i].rstrip()); i += 1
            out.append(""); continue
        if re.match(r'^#{1,6}\s', l) or re.match(r'^\s*---\s*$', l):
            flush_section(); out.append(l); out.append(""); i += 1; continue
        if not l.strip():
            close_para(); i += 1; continue
        para.append(l); i += 1
    flush_section()

    s = "\n".join(out)
    s = re.sub(r'\n{3,}', '\n\n', s).strip() + "\n"
    return s

# 巻頭ページは著者が自分で書いた文章なので、自動処理の対象から外す。
# あそこのリズムは書店での勝負そのものなので、機械で触らない。
def main():
    TARGETS = (sorted(glob.glob("manuscript/本文/*.md"))
               + sorted(glob.glob("manuscript/本文/新構成/*.md")))

    dry = "--dry" in sys.argv
    tot_a = tot_b = 0
    print(f"{'ファイル':44} {'前':>6} {'後':>6} {'差':>6}")
    for f in TARGETS:
        src = io.open(f, encoding="utf-8").read()
        dst = shimeru(src)
        a, b = pages.count_lines(src), pages.count_lines(dst)
        tot_a += a; tot_b += b
        if a != b:
            print(f"{os.path.basename(f):44} {a:6,} {b:6,} {b-a:6,}")
        if not dry:
            io.open(f, "w", encoding="utf-8").write(dst)
    print(f"{'合計':44} {tot_a:6,} {tot_b:6,} {tot_b-tot_a:6,}")
    print(f"ページ（17行組み）　{-(-tot_a//17)} → {-(-tot_b//17)}")


if __name__ == "__main__":
    main()
