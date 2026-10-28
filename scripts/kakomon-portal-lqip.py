#!/usr/bin/env python3
"""過去問ポータルの「ぼかしの下絵」を作り直す。

kakomon-portal/img/uni/<名前>-640.webp と img/top-800.webp から、横32pxの小さな画像を作り、
index.html の LQIP:BEGIN 〜 LQIP:END の間（PIC_LQ）に埋め込む。大学の画像を足したら1回実行する。

  python3 scripts/kakomon-portal-lqip.py
"""
import base64, io, json, pathlib, re
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent / "kakomon-portal"


def tiny(path):
    im = Image.open(path).convert("RGB")
    w = 32
    im = im.resize((w, round(w * im.height / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=40, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


lq = {"__top": tiny(ROOT / "img/top-800.webp")}
for p in sorted((ROOT / "img/uni").glob("*-640.webp")):
    lq[p.name[: -len("-640.webp")]] = tiny(p)

html_path = ROOT / "index.html"
html = html_path.read_text(encoding="utf-8")
block = "/* LQIP:BEGIN（scripts/kakomon-portal-lqip.py が書く。手で直さない） */\nvar PIC_LQ = " + json.dumps(lq, indent=0, ensure_ascii=False) + ";\n/* LQIP:END */"
new, n = re.subn(r"/\* LQIP:BEGIN.*?/\* LQIP:END \*/", lambda m: block, html, flags=re.S)
if n != 1:
    raise SystemExit("index.html に LQIP:BEGIN 〜 LQIP:END が見つかりません")
html_path.write_text(new, encoding="utf-8")
print(f"{len(lq)} 枚（{sum(len(v) for v in lq.values()) // 1024} KB）")
