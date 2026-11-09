# -*- coding: utf-8 -*-
"""いまの原稿を、著者案の5ステップ（新テンプレ）に組み替える。

　Q　生徒の言葉　→　頭のいい人が絶対にやらないこと　→　なぜ、それだと伸びないのか
　→　じゃあ、どうすればいいのか　→　まとめ

もとの ## 見出しは ### に落として、5つのどれかに振り分ける。
中身は足さない。置き場所を変えるだけ。比較用。
出力 manuscript/原稿_新テンプレ.md
"""
import re, sys

SRC = "manuscript/原稿_最新版_マーカー.md"
Q50 = "manuscript/企画書/Q50.md"
OUT = "manuscript/原稿_新テンプレ.md"

H = {k: (v or "") for k, v in
     [l.split("＝", 1) if "＝" in l else (l, "") for l in []]}   # 決定.md は未確定なので既定値を使う
HEADS = ["Q", "頭のいい人が、絶対にやらないこと", "なぜ、それだと伸びないのか",
         "じゃあ、どうすればいいのか", "まとめ"]
try:
    t = open("manuscript/企画書/決定.md", encoding="utf-8").read()
    for i in range(1, 6):
        m = re.search(r'^[ \t　]*見出し%d[ \t　]*[=＝][ \t　]*(.+)$' % i, t, flags=re.M)
        if m and m.group(1).strip(): HEADS[i-1] = m.group(1).strip()
except OSError:
    pass

qs = dict(re.findall(r'^(\d{2})　(\S.*)$', open(Q50, encoding="utf-8").read(), flags=re.M))

DOU  = re.compile(r'頭のなか|やり方|手順|やりすぎ|注意|気をつける|ときは|場合|コツ|聞いてもらう|書き方')
MATO = re.compile(r'これをやると|何が残るか|残るもの|この場面のまとめ|まとめ|最後に|AIにやらせるなら')

def split_sections(body):
    """[(見出し or None, 本文), ...] 見出しなしの冒頭は None"""
    parts = re.split(r'^(##+ .+)$', body, flags=re.M)
    out = [(None, parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i], parts[i+1]))
    return out

def convert(num, title, body, x, o, w):
    secs = split_sections(body)
    naze, dou, mato = [], [], []
    phase = "naze"
    for h, txt in secs:
        if h is None:
            naze.append(("", txt)); continue
        name = re.sub(r'^#+\s*', '', h)
        if MATO.search(name): phase = "mato"
        elif DOU.search(name) and phase != "mato": phase = "dou"
        lv = "####" if h.startswith("###") else "###"
        {"naze": naze, "dou": dou, "mato": mato}[phase].append((f"{lv} {name}", txt))
    def emit(xs):
        return "\n".join((h + "\n" + t if h else t) for h, t in xs).strip()
    q = qs.get(num, "")
    L = [f'## {HEADS[0]}「{q}」', "",
         f'## {HEADS[1]}', "",
         f'　　=={title}。==', "", "これだけは、やりません。", "",
         "```", f'　　×　{x}', f'　　○　{o}', "```", ""]
    if naze: L += [f'## {HEADS[2]}', "", emit(naze), ""]
    if dou:  L += [f'## {HEADS[3]}', "", emit(dou), ""]
    if mato: L += [f'## {HEADS[4]}', "", emit(mato), ""]
    return "\n".join(L)

raw = open(SRC, encoding="utf-8").read()
chunks = re.split(r'^(# .+)$', raw, flags=re.M)
out = [chunks[0]]
W = r'選ぶ力|入れる力|つなげる力|出す力|なおす力|続ける力'
for i in range(1, len(chunks), 2):
    head, blob = chunks[i], chunks[i+1]
    items = re.split(r'^## (\d{2})　(.+)$', blob, flags=re.M)
    if len(items) == 1:
        out += [head, blob]; continue
    buf = [head, items[0]]
    for j in range(1, len(items), 3):
        num, title, body = items[j], items[j+1].strip(), items[j+2]
        title = re.sub(r'[\s　]*(★厚く書く|★新規|［\d+p］|〔新〕|〔旧稿〕)', '', title).strip()
        mx = re.search(r'^\s*×「(.*?)」\s*$', body, flags=re.M)
        mo = re.search(r'^\s*○「(.*?)」\s*$', body, flags=re.M)
        mw = re.search(r'^(' + W + r')(　★厚く書く)?\s*$', body, flags=re.M)
        b = re.sub(r'^\s*[×○]「.*?」\s*$', '', body, count=2, flags=re.M)
        b = re.sub(r'^(' + W + r')(　★厚く書く)?\s*$', '', b, count=1, flags=re.M)
        b = re.sub(r'^\s*---\s*$', '', b, flags=re.M).strip()
        if "★未執筆" in b:
            buf += [f'## {num}　{title}', "", (mw.group(0) if mw else ""), "",
                    f'## {HEADS[0]}「{qs.get(num,"")}」', "", "★未執筆", "", "---", ""]
            continue
        buf += [f'## {num}　{title}', "", (mw.group(0) if mw else ""), "",
                convert(num, title, b, mx.group(1) if mx else "", mo.group(1) if mo else "",
                        mw.group(1) if mw else ""), "", "---", ""]
    out.append("\n".join(buf))
open(OUT, "w", encoding="utf-8").write("\n".join(out))
n = len(re.findall(r'^## \d{2}　', open(OUT, encoding="utf-8").read(), flags=re.M))
print(f"新テンプレに組み替えた　{n}項目　→ {OUT}")
