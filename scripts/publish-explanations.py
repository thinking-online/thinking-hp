#!/usr/bin/env python3
"""explanation/ 内の HTML から公開リンク一覧と sitemap を更新する。

Netlify の build command から実行する。HTML を追加するたびに
netlify.toml を書き換えなくてよい。

  explanation/foo.html       → https://thinking-online.com/explanation/foo
  explanation/bar/baz.html   → https://thinking-online.com/explanation/bar/baz

index.html はこのスクリプトが上書きする（解説ファイルに使わない）。
"""

from __future__ import annotations

import html
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPLANATION_DIR = REPO_ROOT / "explanation"
SITEMAP_PATH = REPO_ROOT / "sitemap.xml"
SITE_ORIGIN = "https://thinking-online.com"
TITLE_RE = re.compile(r"<title[^>]*>([\s\S]*?)</title>", re.IGNORECASE)


def walk_pages(directory: Path) -> list[dict]:
    pages: list[dict] = []
    if not directory.is_dir():
        return pages
    for path in directory.rglob("*.html"):
        rel_parts = path.relative_to(directory).parts
        if any(part.startswith(".") or part.startswith("_") or part == "source" for part in rel_parts):
            continue
        if path.name == "index.html":
            continue
        slug = "/".join(rel_parts)[: -len(".html")]
        raw = path.read_text(encoding="utf-8")
        match = TITLE_RE.search(raw)
        title = re.sub(r"\s+", " ", match.group(1)).strip() if match else ""
        title = html.unescape(title) or slug
        lastmod = datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()
        pages.append({"slug": slug, "title": title, "lastmod": lastmod})
    pages.sort(key=lambda page: page["slug"])
    return pages


def public_path(slug: str) -> str:
    return "/explanation/" + "/".join(quote(part) for part in slug.split("/"))


def render_index(pages: list[dict]) -> str:
    if pages:
        items = []
        for page in pages:
            href = public_path(page["slug"])
            absolute = SITE_ORIGIN + href
            items.append(
                "    <article class=\"item\">\n"
                f"      <h2>{html.escape(page['title'])}</h2>\n"
                f"      <p class=\"file\">{html.escape(page['slug'])}.html</p>\n"
                "      <div class=\"linkrow\">\n"
                f"        <a href=\"{html.escape(href)}\">{html.escape(absolute)}</a>\n"
                f"        <button type=\"button\" data-copy=\"{html.escape(absolute)}\">リンクをコピー</button>\n"
                "      </div>\n"
                "    </article>"
            )
        listing = "\n".join(items)
    else:
        listing = (
            "    <p class=\"empty\">まだ解説ファイルがありません。"
            "<code>explanation/</code> に HTML を置いて公開すると、ここにリンクが出ます。</p>"
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow">
<title>解説リンク一覧｜THINKING</title>
<meta name="description" content="explanation フォルダに追加した解説 HTML の公開リンク一覧です。">
<link rel="canonical" href="{SITE_ORIGIN}/explanation">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
:root{{--bg:#f7f3ed;--paper:#fdfaf4;--ink:#2c2520;--ink2:#6b6155;--line:#e7ddce;--accent:#e85a1a;}}
body{{font-family:"Hiragino Sans","Noto Sans JP",sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;}}
.wrap{{max-width:760px;margin:0 auto;padding:32px 18px 80px;}}
header{{margin-bottom:22px;}}
.kicker{{font-size:12px;letter-spacing:.08em;color:var(--ink2);}}
h1{{font-size:26px;line-height:1.35;margin:6px 0 10px;}}
.lead{{font-size:14px;color:var(--ink2);}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.92em;}}
.list{{display:flex;flex-direction:column;gap:12px;margin-top:22px;}}
.item{{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:16px 16px 14px;}}
.item h2{{font-size:16px;line-height:1.5;font-weight:700;}}
.file{{margin-top:4px;font-size:12px;color:var(--ink2);}}
.linkrow{{display:flex;gap:8px;align-items:center;margin-top:10px;}}
.linkrow a{{flex:1;min-width:0;font-size:13px;color:var(--accent);word-break:break-all;}}
button{{flex:none;border:0;background:var(--ink);color:#fff;border-radius:999px;padding:8px 12px;font-size:12px;cursor:pointer;}}
button.done{{background:#3b8a5a;}}
.empty{{background:var(--paper);border:1px dashed var(--line);border-radius:14px;padding:16px;font-size:14px;color:var(--ink2);}}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="kicker">THINKING</div>
    <h1>解説リンク一覧</h1>
    <p class="lead"><code>explanation/</code> に置いた HTML が、拡張子なしの公開 URL になります。保護者通信や英語読解特訓からは、ここにあるリンクを使ってください。ファイル名は <code>index.html</code> 以外にしてください。</p>
  </header>
  <div class="list">
{listing}
  </div>
</div>
<script>
document.querySelectorAll("[data-copy]").forEach((button) => {{
  button.addEventListener("click", async () => {{
    const url = button.getAttribute("data-copy");
    try {{
      await navigator.clipboard.writeText(url);
    }} catch (err) {{
      const input = document.createElement("input");
      input.value = url;
      document.body.appendChild(input);
      input.select();
      document.execCommand("copy");
      input.remove();
    }}
    const prev = button.textContent;
    button.textContent = "コピーしました";
    button.classList.add("done");
    setTimeout(() => {{
      button.textContent = prev;
      button.classList.remove("done");
    }}, 1600);
  }});
}});
</script>
</body>
</html>
"""


def render_sitemap_block(pages: list[dict]) -> str:
    today = date.today().isoformat()
    urls = [{"loc": f"{SITE_ORIGIN}/explanation", "lastmod": today}]
    urls.extend(
        {"loc": SITE_ORIGIN + public_path(page["slug"]), "lastmod": page["lastmod"]}
        for page in pages
    )
    body = "\n\n".join(
        "  <url>\n"
        f"    <loc>{html.escape(url['loc'])}</loc>\n"
        f"    <lastmod>{url['lastmod']}</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n"
        "    <priority>0.6</priority>\n"
        "  </url>"
        for url in urls
    )
    return f"  <!-- explanation:start -->\n{body}\n  <!-- explanation:end -->"


def update_sitemap(pages: list[dict]) -> None:
    block = render_sitemap_block(pages)
    xml = SITEMAP_PATH.read_text(encoding="utf-8")
    pattern = re.compile(r"  <!-- explanation:start -->[\s\S]*?  <!-- explanation:end -->")
    if pattern.search(xml):
        xml = pattern.sub(block, xml)
    else:
        xml = xml.replace("</urlset>", f"{block}\n\n</urlset>")
    SITEMAP_PATH.write_text(xml, encoding="utf-8")


def main() -> None:
    pages = walk_pages(EXPLANATION_DIR)
    EXPLANATION_DIR.mkdir(parents=True, exist_ok=True)
    (EXPLANATION_DIR / "index.html").write_text(render_index(pages), encoding="utf-8")
    update_sitemap(pages)
    print(f"explanation: {len(pages)} page(s)")


if __name__ == "__main__":
    main()
