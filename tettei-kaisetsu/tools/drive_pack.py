#!/usr/bin/env python3
"""作業データをドライブに預けるための分割ツール（ドライブ1回のアップロード上限 約3MB 対策）。

使い方:
  # まとめて分割（フォルダやファイルを複数指定できる）
  python3 drive_pack.py pack  <名前> <出力フォルダ> <対象1> [対象2 ...]
    → <出力フォルダ>/<名前>.part01 … と <名前>.manifest.json ができる。
      これを全部ドライブの同じフォルダに上げる（disableConversionToGoogleType=true）。

  # 復元（ドライブから全部の part と manifest を同じフォルダに落としてから）
  python3 drive_pack.py restore <manifest.json> <展開先>
    → sha256 を照合し、1つでも違えば止まる。

中身（教材データ・訳・過去問）は絶対にリポジトリに入れないこと（main は Netlify で全公開）。
このスクリプト自体はデータを含まないので、リポジトリに置いてよい。
"""
import hashlib, io, json, os, sys, tarfile

PART = 2_500_000  # 余裕をもって 2.5MB
SKIP_DIRS = {"__pycache__", ".git"}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def pack(name, outdir, targets):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for t in targets:
            t = os.path.abspath(t)
            base = os.path.dirname(t)
            def filt(ti):
                return None if any(p in SKIP_DIRS for p in ti.name.split("/")) else ti
            tf.add(t, arcname=os.path.relpath(t, base), filter=filt)
    data = buf.getvalue()
    os.makedirs(outdir, exist_ok=True)
    parts = []
    for i in range(0, len(data), PART):
        chunk = data[i:i + PART]
        fn = f"{name}.part{len(parts) + 1:02d}"
        with open(os.path.join(outdir, fn), "wb") as f:
            f.write(chunk)
        parts.append({"file": fn, "sha256": sha(chunk), "size": len(chunk)})
    man = {"name": name, "total_sha256": sha(data), "total_size": len(data),
           "targets": [os.path.basename(os.path.abspath(t)) for t in targets], "parts": parts}
    mp = os.path.join(outdir, f"{name}.manifest.json")
    with open(mp, "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    print(f"{len(parts)} parts, {len(data):,} bytes → {outdir}")
    for p in parts:
        print(f"  {p['file']}  {p['size']:,}  sha256:{p['sha256']}")
    print(f"  {os.path.basename(mp)}")


def restore(manifest, dest, search_dir=None):
    with open(manifest, encoding="utf-8") as f:
        man = json.load(f)
    d = search_dir or os.path.dirname(os.path.abspath(manifest))
    data = b""
    for p in man["parts"]:
        path = os.path.join(d, p["file"])
        with open(path, "rb") as f:
            chunk = f.read()
        if sha(chunk) != p["sha256"]:
            sys.exit(f"NG: {p['file']} の sha256 が一致しません")
        data += chunk
    if sha(data) != man["total_sha256"]:
        sys.exit("NG: 全体の sha256 が一致しません")
    os.makedirs(dest, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        tf.extractall(dest, filter="data")
    print(f"OK: {man['name']} を {dest} に復元（{', '.join(man['targets'])}）")


if __name__ == "__main__":
    if len(sys.argv) >= 5 and sys.argv[1] == "pack":
        pack(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif len(sys.argv) in (4, 5) and sys.argv[1] == "restore":
        restore(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) == 5 else None)
    else:
        sys.exit(__doc__)
