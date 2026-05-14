// Blog article — body from data/blog-articles.js (?slug=…)
function blogFormatInline(text, keyPrefix) {
  if (!text || text.indexOf("**") === -1) return text;
  const parts = text.split(/\*\*(.+?)\*\*/g);
  const pfx = keyPrefix || "em";
  return parts.map((part, i) => {
    if (i % 2 === 1) return <em key={`${pfx}-${i}`}>{part}</em>;
    if (!part) return null;
    return <span key={`${pfx}-${i}`}>{part}</span>;
  });
}

function blogParagraph(txt) {
  const lines = (txt || "").split("\n");
  return lines.map((line, li) => (
    <React.Fragment key={li}>
      {li > 0 ? <br /> : null}
      {blogFormatInline(line, `p${li}`)}
    </React.Fragment>
  ));
}

function BlogArticleBlock({ b }) {
  if (b.t === "p") {
    return <p>{blogParagraph(b.txt)}</p>;
  }
  if (b.t === "quote") {
    return (
      <blockquote className="article-quote">
        <p>{blogFormatInline(b.txt, "quote")}</p>
      </blockquote>
    );
  }
  if (b.t === "callout") {
    return (
      <div className="article-callout">
        <div className="callout-side">
          <h4 className="callout-title">{b.L.title}</h4>
          <ul className="callout-list">
            {b.L.items.map((it, j) => (
              <li key={j}>{it}</li>
            ))}
          </ul>
        </div>
        <div className="callout-divider" />
        <div className="callout-side">
          <h4 className="callout-title">{b.R.title}</h4>
          <ul className="callout-list">
            {b.R.items.map((it, j) => (
              <li key={j}>{it}</li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
  if (b.t === "ol") {
    return (
      <ol className="article-list-ordered">
        {b.items.map((it, j) => (
          <li key={j}>
            <strong>{it.lead}</strong>
            <br />
            {blogFormatInline(it.rest, `oli-${j}`)}
          </li>
        ))}
      </ol>
    );
  }
  if (b.t === "ul") {
    return (
      <ul className="article-list">
        {b.items.map((it, j) => (
          <li key={j}>{blogFormatInline(it, `uli-${j}`)}</li>
        ))}
      </ul>
    );
  }
  return null;
}

function blogPickRelated(slug, catKey, all) {
  const keys = Object.keys(all).filter((k) => k !== slug);
  const same = keys.filter((k) => all[k].meta.catKey === catKey);
  const rest = keys.filter((k) => all[k].meta.catKey !== catKey);
  const ordered = [...same, ...rest];
  return ordered.slice(0, 3).map((k) => ({
    slug: k,
    cat: all[k].meta.cat,
    title: all[k].meta.title,
    date: all[k].meta.date,
  }));
}

const BlogArticlePage = () => {
  const all = typeof BLOG_ARTICLES !== "undefined" ? BLOG_ARTICLES : null;
  const slugParam = new URLSearchParams(window.location.search).get("slug");
  const slug =
    slugParam && all && all[slugParam]
      ? slugParam
      : "why-faculty-strategy";
  const article = all && all[slug] ? all[slug] : null;

  React.useEffect(() => {
    if (!article) return;
    document.title = `${article.meta.title} — THINKING`;
    const desc = article.meta.lead.replace(/\*\*/g, "").replace(/\n/g, " ");
    const m = document.querySelector('meta[name="description"]');
    if (m) m.setAttribute("content", desc.slice(0, 200));
  }, [slug, article]);

  if (!article) {
    return (
      <section className="blog-section">
        <div className="blog-section-inner">
          <p>記事を読み込めませんでした。記事一覧へ戻り、もう一度お試しください。</p>
          <a href="blog.html" className="article-back">
            <span>記事一覧へ戻る</span>
          </a>
        </div>
      </section>
    );
  }

  const { meta, toc, sections } = article;
  const related = all ? blogPickRelated(slug, meta.catKey, all) : [];

  return (
    <>
      <header className="article-header">
        <div className="article-header-inner">
          <a href="blog.html" className="article-back">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M19 12H5M12 19l-7-7 7-7" />
            </svg>
            <span>記事一覧へ戻る</span>
          </a>

          <div className="article-meta-top">
            <span className="article-cat">{meta.cat}</span>
            <span className="blog-dot">·</span>
            <span className="article-cat-en">
              <i>{meta.catEn}</i>
            </span>
          </div>

          <h1 className="article-title">{meta.title}</h1>

          <p className="article-lead">{blogParagraph(meta.lead)}</p>

          <div className="article-meta-bottom">
            <div className="article-author">
              <span className="article-author-avatar">T</span>
              <div className="article-author-info">
                <span className="article-author-name">{meta.author}</span>
                <span className="article-author-role">{meta.authorRole}</span>
              </div>
            </div>
            <div className="article-meta-stats">
              <span className="article-date">{meta.date}</span>
              <span className="blog-dot">·</span>
              <span className="article-readtime">{meta.readTime}</span>
            </div>
          </div>
        </div>
      </header>

      <div className="article-hero">
        <div className="article-hero-inner">
          <div className="blog-image-placeholder hero">
            <span className="image-placeholder-mark">{meta.catEn}</span>
            <span className="image-placeholder-note">[ Article Hero Image ]</span>
          </div>
        </div>
      </div>

      <div className="article-layout">
        <div className="article-layout-inner">
          <aside className="article-toc">
            <div className="article-toc-sticky">
              <span className="eyebrow">
                <i>Contents</i>
              </span>
              <ol className="article-toc-list">
                {toc.map((t, i) => (
                  <li key={i}>
                    <a href={`#section-${t.no}`}>
                      <span className="toc-no">
                        <i>{t.no}</i>
                      </span>
                      <span className="toc-title">{t.title}</span>
                    </a>
                  </li>
                ))}
              </ol>
            </div>
          </aside>

          <article className="article-body">
            {sections.map((sec) => (
              <section key={sec.no} id={`section-${sec.no}`}>
                <h2 className="article-h2">
                  <span className="article-h2-no">
                    <i>{sec.no}</i>
                  </span>
                  {sec.h2}
                </h2>
                {sec.blocks.map((b, bi) => (
                  <BlogArticleBlock key={bi} b={b} />
                ))}
              </section>
            ))}

            <p className="article-signature">
              THINKING 代表 — <em>朝倉 徹大</em>
            </p>

            <div className="article-cta">
              <h3 className="article-cta-title">
                あなた専用の<em>合格設計図</em>を、無料相談で。
              </h3>
              <p className="article-cta-lead">30〜45分のオンライン面談で、その場でお渡しします。</p>
              <a
                href="https://line.me/R/ti/p/@thinking"
                target="_blank"
                rel="noopener noreferrer"
                className="cta cta-large"
              >
                LINEで無料相談
                <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M5 12h14M13 5l7 7-7 7" />
                </svg>
              </a>
            </div>
          </article>
        </div>
      </div>

      <section className="article-related">
        <div className="article-related-inner">
          <div className="founder-section-head">
            <span className="eyebrow">
              <i>Related Articles</i>
            </span>
            <h2 className="founder-section-title">
              関連する<em>記事</em>。
            </h2>
          </div>
          <div className="article-related-grid">
            {related.map((r, i) => (
              <a key={i} href={`blog-article.html?slug=${encodeURIComponent(r.slug)}`} className="article-related-card">
                <span className="blog-cat">{r.cat}</span>
                <h3 className="article-related-title">{r.title}</h3>
                <span className="blog-date">{r.date}</span>
              </a>
            ))}
          </div>
        </div>
      </section>
    </>
  );
};

window.BlogArticlePage = BlogArticlePage;
