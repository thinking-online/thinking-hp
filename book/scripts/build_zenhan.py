# -*- coding: utf-8 -*-
"""表紙から第1章の終わりまでを1本のPDFにする。
book/ で実行 → build/表紙から第1章.pdf

中身　表紙と帯 ／ 目次 ／ 巻頭ページ ／ 序章 ／ 第1章 基本の基本編
"""
import subprocess, sys, os

STEPS = [
    ("表紙と帯",   [sys.executable, "scripts/build_hyoshi.py"],        "build/表紙.pdf"),
    ("目次",       [sys.executable, "scripts/build_toc_pdf.py"],       "build/目次.pdf"),
    ("巻頭と序章", [sys.executable, "scripts/build_jo.py"],            "build/巻頭と序章.pdf"),
    ("第1章",      [sys.executable, "scripts/build_jo.py", "kihon"],   "build/基本の基本編.pdf"),
]

# 本文は先に組み直しておく
subprocess.run([sys.executable, "scripts/assemble.py"], check=True, capture_output=True)

parts = []
for name, cmd, out in STEPS:
    subprocess.run(cmd, check=True, capture_output=True)
    n = subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout
    n = [l.split(":")[1].strip() for l in n.split("\n") if l.startswith("Pages")][0]
    print(f"  {name}　{n}ページ")
    parts.append(out)

OUT = "build/表紙から第1章.pdf"
subprocess.run(["pdfunite"] + parts + [OUT], check=True)
n = subprocess.run(["pdfinfo", OUT], capture_output=True, text=True).stdout
n = [l.split(":")[1].strip() for l in n.split("\n") if l.startswith("Pages")][0]
print(f"→ {OUT}　{n}ページ")
