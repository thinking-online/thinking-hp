#!/usr/bin/env python3
"""公開用の解説一覧は作らない。

以前このスクリプトは explanation/index.html と sitemap を生成していた。
/explanation を開くと全解説が見えてしまうため、一覧の再生成はしない。
解説 HTML は lesson/ に英語ファイル名で置き、URL はパスそのものにする。
"""

from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX = REPO_ROOT / "explanation" / "index.html"
SITEMAP = REPO_ROOT / "sitemap.xml"


def main() -> None:
    if INDEX.exists():
        INDEX.unlink()
        print("removed explanation/index.html")
    if SITEMAP.exists():
        xml = SITEMAP.read_text(encoding="utf-8")
        pattern = re.compile(r"\n*  <!-- explanation:start -->[\s\S]*?  <!-- explanation:end -->\n*")
        updated, count = pattern.subn("\n", xml)
        if count:
            SITEMAP.write_text(updated, encoding="utf-8")
            print("removed explanation sitemap entries")
    print("lesson catalog is not published")


if __name__ == "__main__":
    main()
