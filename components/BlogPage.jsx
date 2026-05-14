// Blog index page — list of articles
const BlogPage = () => {
  const featured = {
    slug: "why-faculty-strategy",
    cat: "戦略",
    catEn: "Strategy",
    title: "なぜ「学部別」でしか、難関大に受からないのか。",
    lead: "早稲田法学部と慶應経済学部では、「合格に必要な力」がまったく違います。にもかかわらず、多くの予備校は『難関大文系』という大括りで指導を行っています——。",
    date: "2025.04.18",
    readTime: "8 min read",
    author: "朝倉 徹大",
  };

  const articles = [
    {
      slug: "june-strategy",
      cat: "学習法",
      catEn: "Method",
      title: "高3の6月、何をすべきか。残り8ヶ月の最適解。",
      lead: "受験の天王山は夏ではなく、6月。理由を、3つの観点から解説します。",
      date: "2025.04.10",
      readTime: "6 min",
    },
    {
      slug: "essay-correction",
      cat: "添削",
      catEn: "Essay",
      title: "添削の「赤」が多い答案ほど、伸びる理由。",
      lead: "赤入れの量と、合格率には、相関があります。私たちが重視する添削哲学について。",
      date: "2025.04.03",
      readTime: "5 min",
    },
    {
      slug: "parent-relationship",
      cat: "家族",
      catEn: "Family",
      title: "親が「がんばれ」と言わないほうが、伸びる話。",
      lead: "保護者面談で必ずお伝えしている、家族のあり方について。",
      date: "2025.03.28",
      readTime: "7 min",
    },
    {
      slug: "memorize-vs-think",
      cat: "学習法",
      catEn: "Method",
      title: "「暗記」と「思考」の境界線は、どこにあるのか。",
      lead: "暗記が悪なのではない。考えずに暗記することが、悪なのです。",
      date: "2025.03.21",
      readTime: "9 min",
    },
    {
      slug: "ranking-trap",
      cat: "戦略",
      catEn: "Strategy",
      title: "偏差値ランキングを見ない、という戦略。",
      lead: "偏差値は、入試の難易度を測る尺度のひとつに過ぎません。学部別に、本当に重要な指標は——。",
      date: "2025.03.14",
      readTime: "8 min",
    },
    {
      slug: "self-driven",
      cat: "コーチング",
      catEn: "Coaching",
      title: "「自走できる受験生」が、なぜ最後に勝つのか。",
      lead: "コーチがいないと勉強できない受験生は、本番で必ず崩れます。",
      date: "2025.03.07",
      readTime: "6 min",
    },
    {
      slug: "mock-exam",
      cat: "戦略",
      catEn: "Strategy",
      title: "模試の判定が悪くても、絶望しなくていい3つの理由。",
      lead: "E判定からの逆転合格が、毎年起こる理由を分析します。",
      date: "2025.02.28",
      readTime: "7 min",
    },
    {
      slug: "winter-mental",
      cat: "メンタル",
      catEn: "Mental",
      title: "本番1ヶ月前、メンタルが崩れた時の対処法。",
      lead: "冬期に必ず訪れる「壁」と、その乗り越え方。",
      date: "2025.02.21",
      readTime: "8 min",
    },
    {
      slug: "interview-prep",
      cat: "総合型",
      catEn: "AO",
      title: "総合型選抜の面接で、合否を分ける一言。",
      lead: "面接練習を200回以上見てきた経験から、決定的な違いを語ります。",
      date: "2025.02.14",
      readTime: "5 min",
    },
  ];

  const categories = [
    { key: "all", label: "すべて", count: 10 },
    { key: "strategy", label: "戦略", count: 3 },
    { key: "method", label: "学習法", count: 2 },
    { key: "essay", label: "添削", count: 1 },
    { key: "coaching", label: "コーチング", count: 1 },
    { key: "mental", label: "メンタル", count: 1 },
    { key: "family", label: "家族", count: 1 },
    { key: "ao", label: "総合型", count: 1 },
  ];

  const [activeCat, setActiveCat] = React.useState("all");

  return (
    <>
      <PageHeader
        en="Journal"
        eyebrow="ジャーナル"
        jp={<>受験指導の<em>現場</em>から、<br />考えてきたこと。</>}
        lead="代表 朝倉 徹大が、毎週執筆しているコラム。受験戦略、学習法、メンタル、家族のあり方まで、現場の知見をお届けします。"
        bgImage="assets/campus-03.png"
      />

      <section className="blog-section">
        <div className="blog-section-inner">
          {/* Featured article */}
          <article className="blog-featured">
            <a href={`blog-article.html?slug=${encodeURIComponent(featured.slug)}`} className="blog-featured-link">
              <div className="blog-featured-image">
                <div className="blog-image-placeholder featured">
                  <span className="image-placeholder-mark">{featured.catEn}</span>
                  <span className="image-placeholder-note">[ Featured Article Image ]</span>
                </div>
              </div>
              <div className="blog-featured-body">
                <div className="blog-featured-meta">
                  <span className="blog-featured-tag"><i>Featured</i></span>
                  <span className="blog-cat">{featured.cat}</span>
                </div>
                <h2 className="blog-featured-title">{featured.title}</h2>
                <p className="blog-featured-lead">{featured.lead}</p>
                <div className="blog-featured-foot">
                  <span className="blog-author">{featured.author}</span>
                  <span className="blog-dot">·</span>
                  <span className="blog-date">{featured.date}</span>
                  <span className="blog-dot">·</span>
                  <span className="blog-readtime">{featured.readTime}</span>
                  <span className="blog-arrow">
                    続きを読む
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                      <path d="M5 12h14M13 5l7 7-7 7" />
                    </svg>
                  </span>
                </div>
              </div>
            </a>
          </article>

          {/* Category filter */}
          <div className="blog-filter">
            <span className="blog-filter-label"><i>Filter by</i></span>
            <div className="blog-filter-tabs">
              {categories.map((c) => (
                <button
                  key={c.key}
                  className={`blog-filter-tab ${activeCat === c.key ? "active" : ""}`}
                  onClick={() => setActiveCat(c.key)}
                >
                  {c.label}
                  <span className="blog-filter-count">{c.count}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Article grid */}
          <div className="blog-grid">
            {articles.map((a, i) => (
              <article key={i} className="blog-card">
                <a href={`blog-article.html?slug=${encodeURIComponent(a.slug)}`} className="blog-card-link">
                  <div className="blog-card-image">
                    <div className="blog-image-placeholder">
                      <span className="image-placeholder-mark small">{a.catEn}</span>
                    </div>
                  </div>
                  <div className="blog-card-body">
                    <div className="blog-card-meta">
                      <span className="blog-cat">{a.cat}</span>
                      <span className="blog-date">{a.date}</span>
                    </div>
                    <h3 className="blog-card-title">{a.title}</h3>
                    <p className="blog-card-lead">{a.lead}</p>
                    <div className="blog-card-foot">
                      <span className="blog-readtime">{a.readTime}</span>
                      <span className="blog-arrow-small">→</span>
                    </div>
                  </div>
                </a>
              </article>
            ))}
          </div>

          {/* Load more */}
          <div className="blog-loadmore">
            <button className="cta-ghost cta-large">
              さらに記事を読む
              <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <path d="M12 5v14M5 12l7 7 7-7" />
              </svg>
            </button>
          </div>
        </div>
      </section>
    </>
  );
};

window.BlogPage = BlogPage;
