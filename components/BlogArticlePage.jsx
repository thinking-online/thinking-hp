// Blog article page — long-form essay layout
const BlogArticlePage = () => {
  const meta = {
    cat: "戦略",
    catEn: "Strategy",
    title: "なぜ「学部別」でしか、難関大に受からないのか。",
    lead: "早稲田法学部と慶應経済学部では、「合格に必要な力」がまったく違います。にもかかわらず、多くの予備校は『難関大文系』という大括りで指導を行っています——。",
    date: "2025.04.18",
    readTime: "8 min read",
    author: "朝倉 徹大",
    authorRole: "THINKING. 代表"
  };

  const tableOfContents = [
  { no: "01", title: "「難関大文系」という大雑把な括り" },
  { no: "02", title: "学部ごとに、求められる力は違う" },
  { no: "03", title: "「学部別」がもたらす、3つの効果" },
  { no: "04", title: "では、どう学部別に学習を組み立てるか" },
  { no: "05", title: "おわりに" }];


  const related = [
  { cat: "戦略", title: "偏差値ランキングを見ない、という戦略。", date: "2025.03.14" },
  { cat: "学習法", title: "高3の6月、何をすべきか。残り8ヶ月の最適解。", date: "2025.04.10" },
  { cat: "戦略", title: "模試の判定が悪くても、絶望しなくていい3つの理由。", date: "2025.02.28" }];


  return (
    <>
      {/* Article header */}
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
            <span className="article-cat-en"><i>{meta.catEn}</i></span>
          </div>

          <h1 className="article-title">{meta.title}</h1>

          <p className="article-lead">{meta.lead}</p>

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

      {/* Hero image */}
      <div className="article-hero">
        <div className="article-hero-inner">
          <div className="blog-image-placeholder hero">
            <span className="image-placeholder-mark">{meta.catEn}</span>
            <span className="image-placeholder-note">[ Article Hero Image ]</span>
          </div>
        </div>
      </div>

      {/* Article body */}
      <div className="article-layout">
        <div className="article-layout-inner">
          {/* TOC sidebar */}
          <aside className="article-toc">
            <div className="article-toc-sticky">
              <span className="eyebrow"><i>Contents</i></span>
              <ol className="article-toc-list">
                {tableOfContents.map((t, i) =>
                <li key={i}>
                    <a href={`#section-${t.no}`}>
                      <span className="toc-no"><i>{t.no}</i></span>
                      <span className="toc-title">{t.title}</span>
                    </a>
                  </li>
                )}
              </ol>
            </div>
          </aside>

          {/* Article body */}
          <article className="article-body">
            <section id="section-01">
              <h2 className="article-h2">
                <span className="article-h2-no"><i>01</i></span>
                「難関大文系」という大雑把な括り
              </h2>
              <p>
                予備校のパンフレットを開くと、よく目にする言葉があります。<br />
                「難関大文系コース」「早慶上理対策」「GMARCH突破」——。
              </p>
              <p>
                一見、便利な括りに見えます。実際、私自身も予備校講師時代は、こう括って授業を行っていました。でも、本当にこれでいいのか、という違和感を、ずっと抱えていました。
              </p>
              <p>
                <em>早稲田大学法学部と、慶應義塾大学経済学部</em>。同じ「難関大文系」です。でも、合格に必要な力は、まったく違います。
              </p>
            </section>

            <section id="section-02">
              <h2 className="article-h2">
                <span className="article-h2-no"><i>02</i></span>
                学部ごとに、求められる力は違う
              </h2>
              <p>
                具体例を見てみましょう。
              </p>

              <div className="article-callout">
                <div className="callout-side">
                  <h4 className="callout-title">早稲田大学 法学部</h4>
                  <ul className="callout-list">
                    <li>長文中の論理構造の把握</li>
                    <li>抽象的な議論への耐性</li>
                    <li>記述・小論文での論証力</li>
                  </ul>
                </div>
                <div className="callout-divider" />
                <div className="callout-side">
                  <h4 className="callout-title">慶應義塾大学 経済学部</h4>
                  <ul className="callout-list">
                    <li>数学的・統計的な処理能力</li>
                    <li>図表からの情報抽出</li>
                    <li>英語の即応力（速読）</li>
                  </ul>
                </div>
              </div>

              <p>
                同じ「難関大文系」でも、求められる力はこれだけ違います。法学部志望者に「数学的な処理能力」を磨かせても、経済学部志望者に「論証力」を鍛えさせても、それは合格から遠ざかる道です。
              </p>

              <blockquote className="article-quote">
                <p>
                  全員に同じ授業をすることは、誰のためにもならない。
                </p>
              </blockquote>

              <p>
                これが、私が予備校時代から気づいていた、教育業界の最大の歪みでした。
              </p>
            </section>

            <section id="section-03">
              <h2 className="article-h2">
                <span className="article-h2-no"><i>03</i></span>
                「学部別」がもたらす、3つの効果
              </h2>
              <p>
                では、学部別に学習を組み立てると、何が起きるか。私たちが10年近く実践してきて、はっきりした効果が3つあります。
              </p>

              <ol className="article-list-ordered">
                <li>
                  <strong>学習時間が、3割減る。</strong><br />
                  必要な力にだけ集中するので、無駄な学習が消えます。結果、同じ成果を出すのに必要な時間が、平均で30%減少しました。
                </li>
                <li>
                  <strong>モチベーションが、続く。</strong><br />
                  「いまやっていることが、合格に直結している」という実感が、毎日のやる気を支えます。これが、長丁場の受験では決定的に効いてきます。
                </li>
                <li>
                  <strong>本番で、崩れない。</strong><br />
                  学部固有の問題形式に慣れているので、初見でも動揺しません。これが、当日の点数を確実に押し上げます。
                </li>
              </ol>
            </section>

            <section id="section-04">
              <h2 className="article-h2">
                <span className="article-h2-no"><i>04</i></span>
                では、どう学部別に学習を組み立てるか
              </h2>
              <p>
                THINKING. では、入塾時に必ず、<em>学部別の合格設計図</em>を作成します。これは、志望学部の過去問10年分を分析し、必要な力を分解、現在地から合格までの道のりを月単位で逆算したものです。
              </p>

              <p>
                例えば、早稲田法学部志望なら、12月までに以下のマイルストーンを置きます：
              </p>

              <ul className="article-list">
                <li>6月末：英語長文の論理構造把握ができる（共通テスト過去問で90%）</li>
                <li>9月末：抽象論文の精読で、抽出ノートが書ける</li>
                <li>11月末：小論文で論証構造を組み立てられる（添削評価B以上）</li>
                <li>12月末：過去問演習で、合格点に到達する</li>
              </ul>

              <p>
                このマイルストーンに沿って、毎週の学習計画が決まります。コーチが日々の進捗を見ながら、ズレがあればすぐ軌道修正。これが、私たちの「学部別戦略」の中身です。
              </p>
            </section>

            <section id="section-05">
              <h2 className="article-h2">
                <span className="article-h2-no"><i>05</i></span>
                おわりに
              </h2>
              <p>
                受験勉強は、ただ大量にやればいい、というものではありません。<em>正しい順序で、必要なことだけを、徹底的にやる</em>。これが、最短距離での合格を可能にします。
              </p>
              <p>
                そして、それを設計するためには、学部別の解像度が必要です。「難関大文系」という括りでは、絶対に届かない解像度。私たちは、ここに10年以上、向き合い続けてきました。
              </p>
              <p>
                もし、あなたが今、漠然とした不安の中で勉強しているなら——<br />
                ぜひ一度、無料相談で、あなた専用の合格設計図を見てみてください。
              </p>

              <p className="article-signature">
                THINKING. 代表 — <em>朝倉 徹大</em>
              </p>
            </section>

            {/* Article CTA */}
            <div className="article-cta">
              <h3 className="article-cta-title">
                あなた専用の<em>合格設計図</em>を、無料相談で。
              </h3>
              <p className="article-cta-lead">
                30〜45分のオンライン面談で、その場でお渡しします。
              </p>
              <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta cta-large">
                LINEで無料相談
                <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M5 12h14M13 5l7 7-7 7" />
                </svg>
              </a>
            </div>
          </article>
        </div>
      </div>

      {/* Related articles */}
      <section className="article-related">
        <div className="article-related-inner">
          <div className="founder-section-head">
            <span className="eyebrow"><i>Related Articles</i></span>
            <h2 className="founder-section-title">関連する<em>記事</em>。</h2>
          </div>
          <div className="article-related-grid">
            {related.map((r, i) =>
            <a key={i} href="blog-article.html" className="article-related-card">
                <span className="blog-cat">{r.cat}</span>
                <h3 className="article-related-title">{r.title}</h3>
                <span className="blog-date">{r.date}</span>
              </a>
            )}
          </div>
        </div>
      </section>
    </>);

};

window.BlogArticlePage = BlogArticlePage;