#!/usr/bin/env python3
"""Generate fully static blog article HTML from data/blog-articles.js + blog-meta."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_JS = ROOT / "data" / "blog-articles.js"
META_JS = ROOT / "data" / "blog-meta.js"
PAGES_DIR = ROOT / "blog" / "pages"
SITE = "https://thinking-online.com"
LINE_URL = (
    "https://liff.line.me/1656043253-rkMxPZMQ/landing?"
    "follow=%40499yrupi&lp=0ah1RL&liff_id=1656043253-rkMxPZMQ"
)
DEFAULT_OG = SITE + "/assets/campus-03.png"

# slug -> og image path (relative)
OG_IMAGES = {
    "leap-oboeho-benkyoho": "/leap/assets/hero.png",
}


def quote_js_keys(code: str) -> str:
    """Turn `key:` into `"key":` outside of quoted strings."""
    out: list[str] = []
    i = 0
    n = len(code)
    in_str = False
    quote = ""
    while i < n:
        c = code[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(code[i + 1])
                i += 2
                continue
            if c == quote:
                in_str = False
            i += 1
            continue
        if c in ('"', "'"):
            in_str = True
            quote = c
            out.append(c)
            i += 1
            continue
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:", code[i:])
        if m and (not out or out[-1] in "{,[\n "):
            out.append(f'"{m.group(1)}":')
            i += m.end()
            continue
        out.append(c)
        i += 1
    return "".join(out)


def load_blog_articles() -> dict:
    raw = ARTICLES_JS.read_text(encoding="utf-8")
    start = raw.index("var B = {};") + len("var B = {};")
    end = raw.index("window.BLOG_ARTICLES = B;")
    body = raw[start:end].strip()
    first_article = body.index('B["')
    body = body[first_article:]
    body = "\n".join(line.lstrip() for line in body.splitlines())
    py = (
        "def M(cat, catEn, title, lead, date, readTime, catKey):\n"
        "    return {\n"
        '        "cat": cat, "catEn": catEn, "title": title, "lead": lead,\n'
        '        "date": date, "readTime": readTime,\n'
        '        "author": "朝倉 徹大", "authorRole": "THINKING 代表",\n'
        '        "catKey": catKey,\n'
        "    }\n"
        "B = {}\n"
    )
    py += quote_js_keys(body)
    py = py.replace("true", "True").replace("false", "False")
    ns: dict = {}
    exec(py, ns)  # noqa: S102 — trusted local data file
    return ns["B"]


def load_blog_meta() -> dict:
    raw = META_JS.read_text(encoding="utf-8")
    start = raw.index("window.BLOG_META = {") + len("window.BLOG_META = ")
    depth = 0
    i = start
    while i < len(raw):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                block = raw[start : i + 1]
                break
        i += 1
    else:
        raise ValueError("Could not parse blog-meta.js")
    block = quote_js_keys(block)
    block = re.sub(r"SITE \+ \"([^\"]+)\"", rf'"{SITE}\1"', block)
    block = block.replace("DEFAULT_OG", f'"{DEFAULT_OG}"')
    block = re.sub(r",(\s*[}\]])", r"\1", block)
    return json.loads(block)


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def plain(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").replace("**", "")).strip()


def format_inline(text: str) -> str:
    if not text:
        return ""
    parts: list[str] = []
    last = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)", text):
        if m.start() > last:
            parts.append(esc(text[last : m.start()]))
        if m.group(1) is not None:
            parts.append(f"<em>{esc(m.group(1))}</em>")
        else:
            href = m.group(3)
            label = esc(m.group(2))
            if re.match(r"^https?://", href, re.I):
                parts.append(
                    f'<a href="{esc(href)}" class="article-inline-link" '
                    f'target="_blank" rel="noopener noreferrer">{label}</a>'
                )
            else:
                parts.append(f'<a href="{esc(href)}" class="article-inline-link">{label}</a>')
        last = m.end()
    if last < len(text):
        parts.append(esc(text[last:]))
    return "".join(parts)


def paragraph(txt: str) -> str:
    lines = (txt or "").split("\n")
    inner = "<br />\n      ".join(format_inline(line) for line in lines)
    return f"<p>{inner}</p>"


def render_callout_side(side: dict) -> str:
    items = "".join(f"<li>{esc(it)}</li>" for it in side.get("items", []))
    return (
        f'<div class="callout-side">'
        f'<h4 class="callout-title">{esc(side.get("title", ""))}</h4>'
        f'<ul class="callout-list">{items}</ul>'
        f"</div>"
    )


def render_block(b: dict) -> str:
    t = b.get("t")
    if t == "p":
        return paragraph(b.get("txt", ""))
    if t == "quote":
        return (
            f'<blockquote class="article-quote"><p>{format_inline(b.get("txt", ""))}</p></blockquote>'
        )
    if t == "cite":
        footer = ""
        if b.get("href"):
            footer = (
                f'<footer class="article-cite-footer">'
                f'<span class="article-cite-label">出典：</span>'
                f'<a href="{esc(b["href"])}" target="_blank" rel="noopener noreferrer">'
                f'{esc(b.get("source", ""))}</a></footer>'
            )
        return (
            f'<blockquote class="article-quote article-cite">'
            f'<p>{format_inline(b.get("txt", ""))}</p>{footer}</blockquote>'
        )
    if t == "callout":
        return (
            f'<div class="article-callout">'
            f'{render_callout_side(b["L"])}'
            f'<div class="callout-divider"></div>'
            f'{render_callout_side(b["R"])}'
            f"</div>"
        )
    if t == "ol":
        items = []
        for it in b.get("items", []):
            items.append(
                f"<li><strong>{esc(it.get('lead', ''))}</strong><br />"
                f"{format_inline(it.get('rest', ''))}</li>"
            )
        return f'<ol class="article-list-ordered">{"".join(items)}</ol>'
    if t == "ul":
        items = "".join(f"<li>{format_inline(it)}</li>" for it in b.get("items", []))
        return f'<ul class="article-list">{items}</ul>'
    if t == "summary":
        label = esc(b.get("label") or "この記事の要点")
        items = "".join(f"<li>{format_inline(it)}</li>" for it in b.get("items", []))
        return (
            f'<div class="article-summary" role="note">'
            f'<p class="article-summary-label">{label}</p>'
            f'<ul class="article-summary-list">{items}</ul></div>'
        )
    if t == "h3":
        return f'<h3 class="article-h3">{format_inline(b.get("txt", ""))}</h3>'
    if t == "deflist":
        rows = []
        for it in b.get("items", []):
            rows.append(
                f'<div class="article-deflist-row">'
                f'<dt>{esc(it.get("term", ""))}</dt>'
                f'<dd>{format_inline(it.get("def", ""))}</dd></div>'
            )
        return f'<dl class="article-deflist">{"".join(rows)}</dl>'
    if t == "faq":
        rows = []
        for it in b.get("items", []):
            rows.append(
                f'<div class="article-faq-item">'
                f'<dt class="article-faq-q">{esc(it.get("q", ""))}</dt>'
                f'<dd class="article-faq-a">{format_inline(it.get("a", ""))}</dd></div>'
            )
        return f'<dl class="article-faq">{"".join(rows)}</dl>'
    if t == "linkbox":
        external = b.get("external", True)
        target = ' target="_blank" rel="noopener noreferrer"' if external else ""
        title = ""
        if b.get("title"):
            title = f'<p class="article-linkbox-title">{esc(b["title"])}</p>'
        lead = ""
        if b.get("txt"):
            lead = f'<p class="article-linkbox-lead">{format_inline(b["txt"])}</p>'
        return (
            f'<div class="article-linkbox">{title}{lead}'
            f'<a href="{esc(b.get("href", ""))}" class="article-linkbox-cta"{target}>'
            f'{esc(b.get("label", ""))}'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a></div>'
        )
    return ""


def pick_related(slug: str, cat_key: str, all_articles: dict) -> list[dict]:
    keys = [k for k in all_articles if k != slug]
    same = [k for k in keys if all_articles[k]["meta"]["catKey"] == cat_key]
    rest = [k for k in keys if all_articles[k]["meta"]["catKey"] != cat_key]
    ordered = same + rest
    out = []
    for k in ordered[:3]:
        m = all_articles[k]["meta"]
        out.append({"slug": k, "cat": m["cat"], "title": m["title"], "date": m["date"]})
    return out


def collect_faq(sections: list) -> list[dict]:
    items = []
    for sec in sections or []:
        for b in sec.get("blocks", []):
            if b.get("t") == "faq":
                for it in b.get("items", []):
                    if it.get("q") and it.get("a"):
                        items.append(it)
    return items


def merged_meta(slug: str, article: dict, meta_db: dict) -> dict:
    base = dict(article.get("meta", {}))
    extra = meta_db.get(slug, {})
    base.update(extra)
    return base


def json_ld_article(slug: str, meta: dict, canonical: str, og_image: str) -> str:
    seo_desc = plain(meta.get("seoDescription") or meta.get("lead", ""))[:160]
    date_iso = meta.get("dateISO", "2026-01-01")
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta.get("title", ""),
        "description": seo_desc,
        "image": og_image,
        "datePublished": date_iso,
        "dateModified": date_iso,
        "author": {
            "@type": "Person",
            "name": meta.get("author", "朝倉 徹大"),
            "jobTitle": meta.get("authorRole", "THINKING 代表"),
            "worksFor": {"@type": "Organization", "name": "THINKING", "url": SITE + "/"},
        },
        "publisher": {"@type": "Organization", "name": "THINKING", "url": SITE + "/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "inLanguage": "ja",
    }
    if meta.get("keywords"):
        data["keywords"] = meta["keywords"]
    return json.dumps(data, ensure_ascii=False)


def json_ld_faq(faq_items: list) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": plain(it["q"]),
                "acceptedAnswer": {"@type": "Answer", "text": plain(it["a"])},
            }
            for it in faq_items
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def render_page(slug: str, article: dict, meta_db: dict, all_articles: dict) -> str:
    meta = merged_meta(slug, article, meta_db)
    raw = article["meta"]
    toc = article.get("toc", [])
    sections = article.get("sections", [])
    canonical = f"{SITE}/blog/{slug}"
    og_path = OG_IMAGES.get(slug) or meta.get("ogImage", DEFAULT_OG).replace(SITE, "")
    if not og_path.startswith("/"):
        og_path = "/" + og_path.lstrip("/")
    og_image = SITE + og_path if og_path.startswith("/") else og_path

    seo_title = meta.get("seoTitle") or raw["title"]
    doc_title = f"{seo_title} — THINKING"
    seo_desc = esc(plain(meta.get("seoDescription") or raw.get("lead", ""))[:160])
    share_desc = esc(plain(meta.get("shareDescription") or meta.get("seoDescription") or raw.get("lead", ""))[:120])
    share_preview = plain(meta.get("shareDescription") or meta.get("seoDescription") or raw.get("lead", ""))

    toc_html = []
    for t in toc:
        toc_html.append(
            f'<li><a href="#section-{esc(t["no"])}">'
            f'<span class="toc-no"><i>{esc(t["no"])}</i></span>'
            f'<span class="toc-title">{esc(t["title"])}</span></a></li>'
        )

    sections_html = []
    for sec in sections:
        blocks = "".join(render_block(b) for b in sec.get("blocks", []))
        sections_html.append(
            f'<section id="section-{esc(sec["no"])}">'
            f'<h2 class="article-h2"><span class="article-h2-no"><i>{esc(sec["no"])}</i></span>'
            f'{esc(sec["h2"])}</h2>{blocks}</section>'
        )

    related = pick_related(slug, raw.get("catKey", ""), all_articles)
    related_html = []
    for r in related:
        related_html.append(
            f'<a href="/blog/{esc(r["slug"])}" class="article-related-card">'
            f'<span class="blog-cat">{esc(r["cat"])}</span>'
            f'<h3 class="article-related-title">{esc(r["title"])}</h3>'
            f'<span class="blog-date">{esc(r["date"])}</span></a>'
        )

    faq_items = collect_faq(sections)
    faq_ld = ""
    if faq_items:
        faq_ld = (
            f'\n  <script type="application/ld+json" id="blog-faq-jsonld">'
            f"{json_ld_faq(faq_items)}</script>"
        )

    keywords_tag = ""
    if meta.get("keywords"):
        keywords_tag = f'\n  <meta name="keywords" content="{esc(meta["keywords"])}" />'

    lead_html = format_inline(raw.get("lead", "")).replace("\n", "<br />\n      ")

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(doc_title)}</title>
  <meta name="description" content="{seo_desc}" />{keywords_tag}
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <link rel="canonical" href="{esc(canonical)}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="THINKING" />
  <meta property="og:locale" content="ja_JP" />
  <meta property="og:title" content="{esc(seo_title)}" />
  <meta property="og:description" content="{share_desc}" />
  <meta property="og:url" content="{esc(canonical)}" />
  <meta property="og:image" content="{esc(og_image)}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(seo_title)}" />
  <meta name="twitter:description" content="{share_desc}" />
  <meta name="twitter:image" content="{esc(og_image)}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Noto+Sans+JP:wght@300;400;500;600&family=Noto+Serif+JP:wght@400;500;600;700&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />
  <link rel="stylesheet" href="/styles-site.css" />
  <link rel="stylesheet" href="/styles-line-cta.css" />
  <link rel="stylesheet" href="/styles-founder.css" />
  <link rel="stylesheet" href="/styles-blog.css" />
  <script type="application/ld+json" id="blog-article-jsonld">{json_ld_article(slug, meta, canonical, og_image)}</script>{faq_ld}
</head>
<body>

<header class="site-header scrolled">
  <div class="site-header-inner">
    <a href="/" class="site-logo" aria-label="THINKING トップへ">
      <span class="site-logo-en">THINKING</span>
      <span class="site-logo-jp">学部別・合格設計塾</span>
    </a>
    <nav class="site-nav" aria-label="メイン">
      <ul>
        <li><a href="/blog"><span class="nav-jp">記事一覧</span><span class="nav-en">Journal</span></a></li>
        <li><a href="/price"><span class="nav-jp">料金・入塾</span><span class="nav-en">Pricing</span></a></li>
      </ul>
    </nav>
    <a class="cta site-header-cta" href="{esc(LINE_URL)}" target="_blank" rel="noopener noreferrer">無料相談</a>
  </div>
</header>

<header class="article-header">
  <div class="article-header-inner">
    <a href="/blog" class="article-back">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      <span>記事一覧へ戻る</span>
    </a>
    <div class="article-meta-top">
      <span class="article-cat">{esc(raw["cat"])}</span>
      <span class="blog-dot">·</span>
      <span class="article-cat-en"><i>{esc(raw["catEn"])}</i></span>
    </div>
    <h1 class="article-title">{esc(raw["title"])}</h1>
    <p class="article-lead">{lead_html}</p>
    <div class="article-meta-bottom">
      <div class="article-author">
        <span class="article-author-avatar">T</span>
        <div class="article-author-info">
          <span class="article-author-name">{esc(raw.get("author", "朝倉 徹大"))}</span>
          <span class="article-author-role">{esc(raw.get("authorRole", "THINKING 代表"))}</span>
        </div>
      </div>
      <div class="article-meta-stats">
        <span class="article-date">{esc(raw["date"])}</span>
        <span class="blog-dot">·</span>
        <span class="article-readtime">{esc(raw["readTime"])}</span>
      </div>
    </div>
    <div class="article-share">
      <div class="article-share-head">
        <span class="article-share-label">この記事のリンク</span>
        <a class="article-share-permalink" href="{esc(canonical)}">{esc(canonical)}</a>
      </div>
      <p class="article-share-preview">
        <span class="article-share-preview-label">LINEで送るときの説明文</span>
        {esc(share_preview)}
      </p>
    </div>
  </div>
</header>

<div class="article-hero">
  <div class="article-hero-inner">
    <div class="blog-image-placeholder hero">
      <span class="image-placeholder-mark">{esc(raw["catEn"])}</span>
      <span class="image-placeholder-note">[ Article Hero Image ]</span>
    </div>
  </div>
</div>

<div class="article-layout">
  <div class="article-layout-inner">
    <aside class="article-toc">
      <div class="article-toc-sticky">
        <span class="eyebrow"><i>Contents</i></span>
        <ol class="article-toc-list">
          {"".join(toc_html)}
        </ol>
      </div>
    </aside>

    <article class="article-body">
      {"".join(sections_html)}

      <p class="article-signature">THINKING 代表 — <em>朝倉 徹大</em></p>

      <div class="article-cta">
        <h3 class="article-cta-title">あなた専用の<em>合格設計図</em>を、無料相談で。</h3>
        <p class="article-cta-lead">30〜45分のオンライン面談で、その場でお渡しします。</p>
        <a href="{esc(LINE_URL)}" target="_blank" rel="noopener noreferrer" class="cta cta-large">
          LINEで無料相談
          <svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
  </div>
</div>

<section class="article-related">
  <div class="article-related-inner">
    <div class="founder-section-head">
      <span class="eyebrow"><i>Related Articles</i></span>
      <h2 class="founder-section-title">関連する<em>記事</em>。</h2>
    </div>
    <div class="article-related-grid">
      {"".join(related_html)}
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-brand">
      <span class="site-logo-en">THINKING</span>
      <p class="site-footer-tagline">学部別・合格設計塾</p>
    </div>
    <nav class="site-footer-nav" aria-label="フッター">
      <ul>
        <li><a href="/">トップ</a></li>
        <li><a href="/blog">記事一覧</a></li>
        <li><a href="/price">料金・入塾</a></li>
        <li><a href="/faq">よくある質問</a></li>
      </ul>
    </nav>
    <p class="site-footer-copy">© THINKING</p>
  </div>
</footer>

</body>
</html>
"""


def main() -> None:
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    articles = load_blog_articles()
    meta_db = load_blog_meta()
    for slug in articles:
        html_out = render_page(slug, articles[slug], meta_db, articles)
        out = PAGES_DIR / f"{slug}.html"
        out.write_text(html_out, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
