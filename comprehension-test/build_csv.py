#!/usr/bin/env python3
"""results/q{n}.json (検証済み) を横持ちCSVに組み上げる。

列: 問題No, 問題, 訳, 問題01, 問題01の答え, 問題01の解説, ... 問題04の解説
問題0X セル = 設問文 + 改行 + "A. .." 〜 "D. .." (セル内改行)
"""
import csv
import json
import sys
from pathlib import Path

BASE = Path('/tmp/claude-0/-home-user-thinking-hp/5f12d2a1-7df4-5ffd-924b-ed23125eba30/scratchpad')
RESULTS = BASE / 'results'
SENTS = json.load(open(BASE / 'sentences60.json'))
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / 'questions-60.csv'
MAXQ = 6
MERGE_EXTRA = (BASE / 'results' / 'extra')  # 追加問題(内容一致・英語言い換え)を末尾に結合

errors = []
rows = []
for s in SENTS:
    n = s['no']
    f = RESULTS / f'q{n}.json'
    if not f.exists():
        errors.append(f'No.{n}: 結果ファイルなし')
        continue
    try:
        data = json.loads(f.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'No.{n}: JSONパース失敗 ({e})')
        continue
    qs = list(data.get('questions', []))
    # 追加問題(内容一致・英語言い換え)を末尾に結合
    ef = MERGE_EXTRA / f'q{n}.json'
    if ef.exists():
        try:
            qs += json.loads(ef.read_text(encoding='utf-8')).get('questions', [])
        except Exception as e:
            errors.append(f'No.{n}: extra JSONパース失敗 ({e})')
    if not (2 <= len(qs) <= MAXQ):
        errors.append(f'No.{n}: 問題数が範囲外 ({len(qs)})')
    row = {'問題No': n, '問題': s['en'], '訳': s['ja']}
    for i, q in enumerate(qs[:MAXQ], 1):
        for k in ('q', 'a', 'b', 'c', 'd', 'answer', 'explanation'):
            if not str(q.get(k, '')).strip():
                errors.append(f'No.{n} 問{i}: フィールド {k} が空')
        if str(q.get('answer', '')).strip().upper() not in ('A', 'B', 'C', 'D'):
            errors.append(f'No.{n} 問{i}: answer が不正 ({q.get("answer")})')
        cell = q['q'].strip() + '\n' + '\n'.join(
            f'{L}. {q[l].strip()}' for L, l in zip('ABCD', 'abcd'))
        row[f'問題0{i}'] = cell
        row[f'問題0{i}の答え'] = str(q['answer']).strip().upper()
        row[f'問題0{i}の解説'] = q['explanation'].strip()
    rows.append(row)

header = ['問題No', '問題', '訳']
for i in range(1, MAXQ + 1):
    header += [f'問題0{i}', f'問題0{i}の答え', f'問題0{i}の解説']

with open(OUT, 'w', newline='', encoding='utf-8-sig') as fp:
    w = csv.DictWriter(fp, fieldnames=header)
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, '') for k in header})

print(f'書き出し: {OUT} ({len(rows)}行)')
qcount = sum(1 for r in rows for i in range(1, MAXQ + 1) if r.get(f'問題0{i}'))
print(f'設問総数: {qcount}')
# 正解記号の分布(偏りチェック)
from collections import Counter
dist = Counter(r[f'問題0{i}の答え'] for r in rows for i in range(1, MAXQ + 1) if r.get(f'問題0{i}の答え'))
print('正解分布:', dict(sorted(dist.items())))
if errors:
    print('\n== 要確認 ==')
    for e in errors:
        print(' -', e)
    sys.exit(1)
print('検証OK: 全行完全')
