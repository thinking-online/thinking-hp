#!/bin/bash
# 使い方: bash testpart.sh N   （N=1..5）  → work/test_N/ に PDF とページ画像、検査結果を出す
set -e
S=/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad/wsc25
N=$1; T=$S/work/test_$N; rm -rf "$T"; mkdir -p "$T/data"
cat > "$T/data/test-part$N.py" <<PY
import sys
sys.path.insert(0, "$S/content/parts")
import importlib
PART = importlib.import_module("part$N").PART
BOOK = {"id": "test-part$N", "univ": "早稲田大学", "faculty": "商学部", "year": 2025, "subject": "英語",
  "cover_color": "#6f1d2b", "cover_sub": "", "footer_note": "",
  "howto": ["テスト"], "overview": {"lead": "テスト", "exam_line": "テスト", "structure_head": ["大問"], "structure_cls": [""],
  "structure": [["$N"]], "time_plan": [], "diff_points": [], "notes": []},
  "parts": [PART],
  "summary": {"lead": "テスト", "total_points": "—", "answer_notes": [], "review_lead": "テスト",
   "miss_types": [{"key": k, "name": k, "lack": k, "action": k} for k in "ABCDE"], "closing": []},
  "sources": [], "copyright": ["テスト"]}
PY
cd /home/user/thinking-hp/tettei-kaisetsu
python3 build.py test-part$N --content-dir "$T" --out "$T/test.pdf" --png "$T/png" 2>&1 | tail -40
