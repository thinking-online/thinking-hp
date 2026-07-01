// Blog article — body from data/blog-articles.js (/blog/:slug)
function blogArticleHref(slug) {
  if (typeof window.blogArticleHref === "function") return window.blogArticleHref(slug);
  return "/blog/" + encodeURIComponent(slug);
}

function blogArticleCanonical(slug) {
  if (typeof window.blogArticleCanonical === "function") return window.blogArticleCanonical(slug);
  return "https://thinking-online.com" + blogArticleHref(slug);
}

function blogSlugAliases() {
  return typeof BLOG_SLUG_ALIASES !== "undefined" ? BLOG_SLUG_ALIASES : {};
}

function blogResolveSlug(all) {
  if (!all) return "why-faculty-strategy";
  var aliases = blogSlugAliases();
  if (typeof window.__BLOG_PRESET_SLUG__ === "string" && all[window.__BLOG_PRESET_SLUG__]) {
    return window.__BLOG_PRESET_SLUG__;
  }
  var path = window.location.pathname.replace(/\/+$/, "");
  var pathMatch = path.match(/^\/blog\/([^/]+)$/);
  if (pathMatch) {
    var fromPath = decodeURIComponent(pathMatch[1]);
    if (all[fromPath]) return fromPath;
    if (aliases[fromPath] && all[aliases[fromPath]]) return aliases[fromPath];
  }
  var slugParam = new URLSearchParams(window.location.search).get("slug");
  if (slugParam) {
    if (all[slugParam]) return slugParam;
    if (aliases[slugParam] && all[aliases[slugParam]]) return aliases[slugParam];
  }
  return "why-faculty-strategy";
}

function blogMergedMeta(slug, article) {
  if (!article) return null;
  var base = article.meta;
  var extra = typeof BLOG_META !== "undefined" && BLOG_META[slug] ? BLOG_META[slug] : {};
  return Object.assign({}, base, extra);
}
function blogFormatInline(text, keyPrefix) {
  if (!text) return text;
  const pfx = keyPrefix || "em";
  const re = /\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)/g;
  if (!re.test(text)) return text;
  re.lastIndex = 0;
  const nodes = [];
  let last = 0;
  let m;
  let i = 0;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) {
      nodes.push(<span key={`${pfx}-${i++}`}>{text.slice(last, m.index)}</span>);
    }
    if (m[1] != null) {
      nodes.push(<em key={`${pfx}-${i++}`}>{m[1]}</em>);
    } else {
      const isExternal = /^https?:\/\//i.test(m[3]);
      nodes.push(
        <a
          key={`${pfx}-${i++}`}
          href={m[3]}
          className="article-inline-link"
          target={isExternal ? "_blank" : undefined}
          rel={isExternal ? "noopener noreferrer" : undefined}
        >
          {m[2]}
        </a>
      );
    }
    last = m.index + m[0].length;
  }
  if (last < text.length) {
    nodes.push(<span key={`${pfx}-${i++}`}>{text.slice(last)}</span>);
  }
  return nodes;
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
  if (b.t === "cite") {
    return (
      <blockquote className="article-quote article-cite">
        <p>{blogFormatInline(b.txt, "cite")}</p>
        {b.href ? (
          <footer className="article-cite-footer">
            <span className="article-cite-label">出典：</span>
            <a href={b.href} target="_blank" rel="noopener noreferrer">
              {b.source}
            </a>
          </footer>
        ) : null}
      </blockquote>
    );
  }
  if (b.t === "linkbox") {
    const external = b.external !== false;
    return (
      <div className="article-linkbox">
        {b.title ? <p className="article-linkbox-title">{b.title}</p> : null}
        {b.txt ? <p className="article-linkbox-lead">{blogFormatInline(b.txt, "lb")}</p> : null}
        <a
          href={b.href}
          className="article-linkbox-cta"
          target={external ? "_blank" : undefined}
          rel={external ? "noopener noreferrer" : undefined}
        >
          {b.label}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
            <path d="M5 12h14M13 5l7 7-7 7" />
          </svg>
        </a>
      </div>
    );
  }
  if (b.t === "summary") {
    return (
      <div className="article-summary" role="note" aria-label="この記事の要点">
        <p className="article-summary-label">{b.label || "この記事の要点"}</p>
        <ul className="article-summary-list">
          {b.items.map((it, j) => (
            <li key={j}>{blogFormatInline(it, `sum-${j}`)}</li>
          ))}
        </ul>
      </div>
    );
  }
  if (b.t === "h3") {
    return <h3 className="article-h3">{blogFormatInline(b.txt, "h3")}</h3>;
  }
  if (b.t === "deflist") {
    return (
      <dl className="article-deflist">
        {b.items.map((it, j) => (
          <div key={j} className="article-deflist-row">
            <dt>{it.term}</dt>
            <dd>{blogFormatInline(it.def, `def-${j}`)}</dd>
          </div>
        ))}
      </dl>
    );
  }
  if (b.t === "faq") {
    return (
      <dl className="article-faq">
        {b.items.map((it, j) => (
          <div key={j} className="article-faq-item">
            <dt className="article-faq-q">{it.q}</dt>
            <dd className="article-faq-a">{blogFormatInline(it.a, `faq-${j}`)}</dd>
          </div>
        ))}
      </dl>
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

function blogEnsureMeta(name, content) {
  if (!content) return;
  let el = document.querySelector(`meta[name="${name}"]`);
  if (!el) {
    el = document.createElement("meta");
    el.setAttribute("name", name);
    document.head.appendChild(el);
  }
  el.setAttribute("content", content);
}

function blogEnsureProp(property, content) {
  if (!content) return;
  let el = document.querySelector(`meta[property="${property}"]`);
  if (!el) {
    el = document.createElement("meta");
    el.setAttribute("property", property);
    document.head.appendChild(el);
  }
  el.setAttribute("content", content);
}

function blogEnsureCanonical(href) {
  if (!href) return;
  let el = document.querySelector('link[rel="canonical"]');
  if (!el) {
    el = document.createElement("link");
    el.setAttribute("rel", "canonical");
    document.head.appendChild(el);
  }
  el.setAttribute("href", href);
}

function blogEnsureJsonLd(id, data) {
  if (!data) return;
  let el = document.getElementById(id);
  if (!el) {
    el = document.createElement("script");
    el.type = "application/ld+json";
    el.id = id;
    document.head.appendChild(el);
  }
  el.textContent = JSON.stringify(data);
}

function blogCollectFaq(sections) {
  const items = [];
  (sections || []).forEach((sec) => {
    (sec.blocks || []).forEach((b) => {
      if (b.t === "faq") {
        (b.items || []).forEach((it) => {
          if (it.q && it.a) items.push(it);
        });
      }
    });
  });
  return items;
}

function blogApplyArticleHead(slug, article) {
  if (!article) return;
  const meta = blogMergedMeta(slug, article);
  const plain = (s) => (s || "").replace(/\*\*/g, "").replace(/\n/g, " ").trim();
  const seoDesc = plain(meta.seoDescription || meta.lead).slice(0, 160);
  const shareDesc = plain(meta.shareDescription || meta.seoDescription || meta.lead).slice(0, 120);
  const title = meta.seoTitle || meta.title;
  const canonical = blogArticleCanonical(slug);
  const dateISO = meta.dateISO || "2026-01-01";
  const ogImage = meta.ogImage || "https://thinking-online.com/assets/campus-03.png";

  document.title = `${title} — THINKING`;
  blogEnsureMeta("description", seoDesc);
  if (meta.keywords) blogEnsureMeta("keywords", meta.keywords);
  blogEnsureProp("og:type", "article");
  blogEnsureProp("og:title", title);
  blogEnsureProp("og:description", shareDesc);
  blogEnsureProp("og:url", canonical);
  blogEnsureProp("og:image", ogImage);
  blogEnsureProp("og:site_name", "THINKING");
  blogEnsureProp("og:locale", "ja_JP");
  blogEnsureMeta("twitter:card", "summary_large_image");
  blogEnsureMeta("twitter:title", title);
  blogEnsureMeta("twitter:description", shareDesc);
  blogEnsureMeta("twitter:image", ogImage);
  blogEnsureCanonical(canonical);

  blogEnsureJsonLd("blog-article-jsonld", {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: meta.title,
    description: seoDesc,
    image: ogImage,
    datePublished: dateISO,
    dateModified: dateISO,
    author: {
      "@type": "Person",
      name: meta.author,
      jobTitle: meta.authorRole,
      worksFor: { "@type": "Organization", name: "THINKING", url: "https://thinking-online.com/" },
    },
    publisher: {
      "@type": "Organization",
      name: "THINKING",
      url: "https://thinking-online.com/",
    },
    mainEntityOfPage: { "@type": "WebPage", "@id": canonical },
    inLanguage: "ja",
    keywords: meta.keywords || undefined,
  });

  const faqItems = blogCollectFaq(article.sections);
  if (faqItems.length) {
    blogEnsureJsonLd("blog-faq-jsonld", {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      mainEntity: faqItems.map((it) => ({
        "@type": "Question",
        name: plain(it.q),
        acceptedAnswer: { "@type": "Answer", text: plain(it.a) },
      })),
    });
  }
}

const ArticleShareBar = ({ slug, shareDescription }) => {
  const [copied, setCopied] = React.useState(false);
  const url = blogArticleCanonical(slug);

  const onCopy = () => {
    const done = () => {
      setCopied(true);
      window.setTimeout(() => setCopied(false), 2000);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(done).catch(() => {});
    }
  };

  return (
    <div className="article-share">
      <div className="article-share-head">
        <span className="article-share-label">この記事のリンク</span>
        <a href={blogArticleHref(slug)} className="article-share-permalink">
          {blogArticleHref(slug)}
        </a>
      </div>
      {shareDescription ? (
        <p className="article-share-preview">
          <span className="article-share-preview-label">LINEで送るときの説明文</span>
          {shareDescription}
        </p>
      ) : null}
      <button type="button" className="article-share-copy" onClick={onCopy}>
        {copied ? "コピーしました" : "リンクをコピー"}
      </button>
    </div>
  );
};

const BlogArticlePage = () => {
  const all = typeof BLOG_ARTICLES !== "undefined" ? BLOG_ARTICLES : null;
  const slug = blogResolveSlug(all);
  const article = all && all[slug] ? all[slug] : null;

  React.useEffect(() => {
    blogApplyArticleHead(slug, article);
  }, [slug, article]);

  React.useEffect(() => {
    if (!slug || !article) return;
    const pretty = blogArticleHref(slug);
    const path = window.location.pathname.replace(/\/+$/, "");
    if (path !== pretty && path.indexOf("/blog/") !== 0) {
      window.history.replaceState(null, "", pretty);
    }
  }, [slug, article]);

  if (!article) {
    return (
      <section className="blog-section">
        <div className="blog-section-inner">
          <p>記事を読み込めませんでした。記事一覧へ戻り、もう一度お試しください。</p>
          <a href="/blog" className="article-back">
            <span>記事一覧へ戻る</span>
          </a>
        </div>
      </section>
    );
  }

  const { meta: rawMeta, toc, sections } = article;
  const meta = blogMergedMeta(slug, article);
  const related = all ? blogPickRelated(slug, rawMeta.catKey, all) : [];
  const shareDesc = (meta.shareDescription || meta.seoDescription || meta.lead || "")
    .replace(/\*\*/g, "")
    .replace(/\n/g, " ")
    .trim();

  return (
    <>
      <header className="article-header">
        <div className="article-header-inner">
          <a href="/blog" className="article-back">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M19 12H5M12 19l-7-7 7-7" />
            </svg>
            <span>記事一覧へ戻る</span>
          </a>

          <div className="article-meta-top">
            <span className="article-cat">{rawMeta.cat}</span>
            <span className="blog-dot">·</span>
            <span className="article-cat-en">
              <i>{rawMeta.catEn}</i>
            </span>
          </div>

          <h1 className="article-title">{rawMeta.title}</h1>

          <p className="article-lead">{blogParagraph(rawMeta.lead)}</p>

          <div className="article-meta-bottom">
            <div className="article-author">
              <span className="article-author-avatar">T</span>
              <div className="article-author-info">
                <span className="article-author-name">{rawMeta.author}</span>
                <span className="article-author-role">{rawMeta.authorRole}</span>
              </div>
            </div>
            <div className="article-meta-stats">
              <span className="article-date">{rawMeta.date}</span>
              <span className="blog-dot">·</span>
              <span className="article-readtime">{rawMeta.readTime}</span>
            </div>
          </div>

          <ArticleShareBar slug={slug} shareDescription={shareDesc} />
        </div>
      </header>

      <div className="article-hero">
        <div className="article-hero-inner">
          <div className="blog-image-placeholder hero">
            <span className="image-placeholder-mark">{rawMeta.catEn}</span>
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
                href={window.THINKING_LINE_LIFF_URL}
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
              <a key={i} href={blogArticleHref(r.slug)} className="article-related-card">
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
