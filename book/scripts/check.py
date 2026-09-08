# -*- coding: utf-8 -*-
"""台本の自己点検。book/ で実行する。全項目 OK になるまで直す。"""
import re, glob, sys, os
M = "manuscript"
CH = {2:(4,10),3:(11,17),4:(18,24),5:(25,31),6:(32,38),7:(39,45)}
ng = []
def bad(cat, msg): ng.append((cat, msg))

laws = {}
s1 = open(f"{M}/第1章.md", encoding="utf-8").read()
for n in (1,2,3):
    m = re.search(r'## 法則%d\b(.*?)(?=\n---\n|\Z)' % n, s1, re.S)
    laws[n] = m.group(1)
for n in range(4,46):
    laws[n] = open(f"{M}/法則{n}.md", encoding="utf-8").read()
allmd = {p: open(p, encoding="utf-8").read() for p in glob.glob(f"{M}/**/*.md", recursive=True)}
body = {p:t for p,t in allmd.items() if "企画書" not in p and "README" not in p}

# 1 構造
for n,t in laws.items():
    for k in ["Q","HINT","分かれ道","伸びない人の答え","伸びる人の答え","他の場面で","結論","隅の図"]:
        if k not in t: bad("構造", f"法則{n} に「{k}」がない")
    for r in ["すること","数えているもの","図の上では","試験の日に"]:
        if f"| {r} |" not in t: bad("構造", f"法則{n} の分かれ道に「{r}」の行がない")

# 2 通貨（結論が「1行消える／1行増える」に着地しているか）
CUR = re.compile(r'行|消す|消え|消し|できるようになった')
for n,t in laws.items():
    m = re.search(r'#+ 結論\n\n(.*?)\n', t, re.S)
    if not m: bad("通貨", f"法則{n} の結論が取れない"); continue
    if not CUR.search(m.group(1)): bad("通貨", f"法則{n} の結論が通貨に着地していない: {m.group(1)[:36]}")

# 3 文体の禁止
for p,t in body.items():
    if "**" in t: bad("文体", f"{p} にアスタリスク強調")
    for w in ["しましょう"]:
        if w in t: bad("文体", f"{p} に「{w}」")
for p,t in body.items():
    for w in ["社会人","上司","会社員"]:
        if w in t: bad("読者", f"{p} に「{w}」（社会人の場面は書かない）")

# 4 法則文の語彙（中学生が意味を知らない語）
HARD = ["工程","逆算","帰着","粒度","反証","対象非依存","前提で"]
for n,t in laws.items():
    m = re.search(r'#+ 法則%d\n\n(.*?)\n' % n, t, re.S)
    if m:
        for w in HARD:
            if w in m.group(1): bad("語彙", f"法則{n} の法則文に「{w}」")

# 5 主語（見開きの中に「あの子」が残っていないか）
for n in range(4,46):
    if "あの子" in laws[n]: bad("主語", f"法則{n} に「あの子」が残っている")

# 6 Qの重複
qs = {}
for n,t in laws.items():
    m = re.search(r'#+ Q\n\n(.*?)\n', t, re.S)
    if m:
        q = m.group(1).strip()
        if q in qs: bad("重複", f"法則{n} と法則{qs[q]} のQが同一: {q}")
        qs[q] = n

# 7 道具の呼び名の統一（できないノート）
for p,t in body.items():
    if re.search(r'できないリスト', t): bad("用語", f"{p} に「できないリスト」（「できないノート」に統一）")

# 8 学年比（各章 中4 高3）
for c,(a,b) in CH.items():
    j = sum(1 for n in range(a,b+1) if re.search(r'中学[123]年生', laws[n]))
    k = sum(1 for n in range(a,b+1) if re.search(r'高校[123]年生', laws[n]))
    if (j,k) != (4,3): bad("学年", f"第{c}章 中{j}／高{k}（4対3にする）")

# 9 目次（docs/03）と本文のQが一致しているか
d3 = open("docs/03_目次_45法則.md", encoding="utf-8").read()
for n in range(4,46):
    q = re.search(r'#+ Q\n\n(.*?)\n', laws[n], re.S).group(1).strip()
    row = re.search(r'\| %d \| (.*?) \|' % n, d3)
    if row and row.group(1).strip() != q:
        bad("目次", f"法則{n} のQが docs/03 と違う\n      本文: {q}\n      docs: {row.group(1).strip()}")

# 10 定義整合（「わかった」を「できる」と書いていないか）
for n,t in laws.items():
    if re.search(r'わかった(から|ので)、?できる', t): bad("定義", f"法則{n} でわかった＝できると書いている")

# 11 章扉に札と力の説明と写真指定
for c in range(2,8):
    t = open(f"{M}/第{c}章_扉.md", encoding="utf-8").read()
    for k in ["【", "## この章の力", "扉の写真", "章末ページ　この章の一行", "5教科で使うと"]:
        if k not in t: bad("章扉", f"第{c}章の扉に「{k}」がない")

# 12 結論の言い回しが単調でないか（同じ書き出しが連続しすぎ）
heads = []
for n in sorted(laws):
    m = re.search(r'#+ 結論\n\n(.{0,6})', laws[n], re.S)
    heads.append(m.group(1) if m else "")
same = sum(1 for h in heads if h.startswith("同じ"))
if same > 42: bad("文体", f"結論の書き出し「同じ」が {same}/45。少し崩す")


# ---- ここから、立場別の点検 ----

# 13 マーケター　表紙の約束の回収
d0 = open("docs/00_決定事項サマリー.md", encoding="utf-8").read()
if "やらない45" not in "".join(body.keys()) + " " + " ".join(str(k) for k in body):
    pass
yaranai = open(f"{M}/やらない45.md", encoding="utf-8").read()
if len(re.findall(r'　\s*\d+　□', yaranai)) != 45:
    bad("販売", "巻頭の「やらない45」が45行ちょうどでない")
matome = open(f"{M}/まとめ.md", encoding="utf-8").read()
if "45の分かれ道" not in matome: bad("販売", "まとめに「45の分かれ道」がない（表紙の約束の3回目の回収）")
hajime = open(f"{M}/はじめに.md", encoding="utf-8").read()
if "1分も増やしません" not in hajime: bad("販売", "帯の「勉強時間は、1分も増やしません」が本文で回収されていない")
oya = open(f"{M}/親へ.md", encoding="utf-8").read()
if "何時間やったの" not in oya: bad("販売", "帯裏の保護者への一行が、親向け章で回収されていない")

# 14 中学生読者　1見開きの分量と、答えが行動になっているか
for n,t in laws.items():
    left = t.split("伸びない人の答え",1)[-1]
    if len(left) > 1200: bad("分量", f"法則{n} の左ページが {len(left)}字（1200字を超えると1ページに入らない）")
    m = re.search(r'#+ 伸びる人の答え\n\n(.*?)\n\n', t, re.S)
    if m and re.search(r'(意識|姿勢|心がけ|気持ち)(する|を持つ|を変える)', m.group(1)):
        bad("行動", f"法則{n} の伸びる人の答えが行動になっていない")

# 15 保護者　判定材料と声かけ
for k in ["うちの子は、何型か", "かける一言", "この本の渡し方"]:
    if k not in oya: bad("保護者", f"親向け章に「{k}」がない")
if oya.count("かける一言") < 7: bad("保護者", "7つの型それぞれに「かける一言」が要る")

# 16 編集者　未確定の明示と docs 整合
d8 = open("docs/08_未確定事項と提案.md", encoding="utf-8").read()
for k in ["7つの型の名前", "章扉の6問"]:
    if k not in d8: bad("編集", f"docs/08 に「{k}」の未確定が残っていない")
for c in range(2,8):
    t = open(f"{M}/第{c}章_扉.md", encoding="utf-8").read()
    if "作り話" not in t: bad("編集", f"第{c}章の扉に、作り話である旨の注記がない")

# 17 図の言葉　隅の図は図の語だけで書く
FIG = ["箱","矢印","漏斗","判定","点線","線","カウンター","知らない","知っている","わかっている","できる","×"]
for n in range(4,46):
    m = re.search(r'### 隅の図\n\n(.*?)(?:\n\n|\Z)', laws[n], re.S)
    if m and not any(w in m.group(1) for w in FIG):
        bad("図", f"法則{n} の隅の図が図の言葉になっていない")

# 18 ノートが本文で機能しているか
if "できないノート" not in s1: bad("道具", "第1章に「できないノート」の説明がない")
fu = open(f"{M}/付録.md", encoding="utf-8").read()
if "できないノート" not in fu: bad("道具", "付録に「できないノート」がない")
if "最初の1週間" not in fu: bad("道具", "付録に「最初の1週間」がない")

# 19 第1章の分量
if len(s1) > 11000: bad("分量", f"第1章が {len(s1)}字（1万字を超えると読者が脱落する）")

# 20 場面タグと科目の広がり
for c,(a,b) in CH.items():
    subj = set()
    for n in range(a,b+1):
        for w in ["英語","数学","理科","社会","国語","古文"]:
            if w in laws[n]: subj.add(w)
    if len(subj) < 3: bad("科目", f"第{c}章に出てくる科目が {len(subj)}種類（3種類以上にする）")

print(f"検査項目 20 / 不合格 {len(ng)} 件")
cat = {}
for c,m in ng: cat.setdefault(c, []).append(m)
for c in cat:
    print(f"\n[{c}] {len(cat[c])}件")
    for m in cat[c][:12]: print("  -", m)
    if len(cat[c]) > 12: print(f"  ... 他 {len(cat[c])-12} 件")
sys.exit(1 if ng else 0)
