#!/usr/bin/env python3
"""標準編(70文): results-jukko/q{n}.json を横持ちCSVに組む。
新形式: 問題文・選択肢A/B/C/D・正解・解説をそれぞれ別セルに分ける(フォーム生成の安全化)。
"""
import csv, json, sys
from pathlib import Path

BASE = Path('/tmp/claude-0/-home-user-thinking-hp/5f12d2a1-7df4-5ffd-924b-ed23125eba30/scratchpad')
RES = BASE / 'results-jukko'
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / 'questions-jukko.csv'
N = 70
MAXQ = 6

def qcols(i):
    return [f'問題0{i}', f'問題0{i}選択肢A', f'問題0{i}選択肢B',
            f'問題0{i}選択肢C', f'問題0{i}選択肢D', f'問題0{i}の答え', f'問題0{i}の解説']

header = ['問題No', '問題', '訳']
for i in range(1, MAXQ + 1):
    header += qcols(i)

errors, rows = [], []
for n in range(1, N + 1):
    f = RES / f'q{n}.json'
    if not f.exists():
        errors.append(f'No.{n}: 結果ファイルなし'); continue
    try:
        d = json.loads(f.read_text(encoding='utf-8'))
    except Exception as ex:
        errors.append(f'No.{n}: JSONパース失敗 ({ex})'); continue
    qs = d.get('questions', [])
    if not (2 <= len(qs) <= MAXQ):
        errors.append(f'No.{n}: 問題数が範囲外 ({len(qs)})')
    row = {'問題No': n, '問題': d.get('en', ''), '訳': d.get('ja', '')}
    for i, q in enumerate(qs[:MAXQ], 1):
        for k in ('q', 'a', 'b', 'c', 'd', 'answer', 'explanation'):
            if not str(q.get(k, '')).strip():
                errors.append(f'No.{n} 問{i}: フィールド {k} が空')
        if str(q.get('answer', '')).strip().upper() not in ('A', 'B', 'C', 'D'):
            errors.append(f'No.{n} 問{i}: answer が不正 ({q.get("answer")})')
        c = qcols(i)
        row[c[0]] = q['q'].strip()
        row[c[1]] = q['a'].strip()
        row[c[2]] = q['b'].strip()
        row[c[3]] = q['c'].strip()
        row[c[4]] = q['d'].strip()
        row[c[5]] = str(q['answer']).strip().upper()
        row[c[6]] = q['explanation'].strip()
    rows.append(row)

with open(OUT, 'w', newline='', encoding='utf-8-sig') as fp:
    w = csv.DictWriter(fp, fieldnames=header)
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, '') for k in header})

qcount = sum(1 for r in rows for i in range(1, MAXQ + 1) if r.get(f'問題0{i}'))
from collections import Counter
dist = Counter(r[f'問題0{i}の答え'] for r in rows for i in range(1, MAXQ + 1) if r.get(f'問題0{i}の答え'))
print(f'書き出し: {OUT} ({len(rows)}行, {len(header)}列) / 設問総数: {qcount}')
print('正解分布:', dict(sorted(dist.items())))
if errors:
    print('\n== 要確認 =='); [print(' -', e) for e in errors]; sys.exit(1)
print('検証OK: 全行完全')
