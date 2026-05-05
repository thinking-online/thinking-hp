// Media — press / TV appearances
const Media = () => {
  const items = [
    {
      thumb: "assets/media-r25-1.png",
      pub: "新R25",
      kind: "WEB INTERVIEW",
      title: "ドS管理で、逆転合格へ。完全\"子\"別、人生を変えるオンライン塾。",
      meta: "塾代表インタビュー",
      url: "https://r25.jp/companies/all-day-thinking/interview/1026804627472908290",
      featured: true,
    },
    {
      thumb: "assets/media-r25-2.png",
      pub: "新R25",
      kind: "WEB INTERVIEW",
      title: "偏差値42→70早稲田大卒。最強の\"脳内インストール\"英語学習法。",
      meta: "英語指導インタビュー",
      url: "https://r25.jp/companies/all-day-thinking/interview/970960432984489985",
    },
    {
      thumb: "assets/media-tv.png",
      pub: "Powered by TV",
      kind: "TV BROADCAST",
      title: "「元気ジャパン」放送回 — 受験指導の現場として出演。",
      meta: "テレビ番組出演",
      url: "https://powered-by-tv.com/2023/08/12/powernews11/",
    },
  ];

  const [feature, ...rest] = items;

  return (
    <section className="section media-section" id="media">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Press · As featured in</i></span>
          <h2 className="section-title">
            メディア掲載 / <em>取材実績</em>
          </h2>
          <p className="section-lead">
            新R25・テレビ番組をはじめとする各メディアにて、<br />
            塾の指導理念・代表インタビューが取り上げられています。
          </p>
          <div className="ornament"><span className="ornament-mark" /></div>
        </div>

        {/* Press logos strip */}
        <div className="media-logos reveal">
          <span className="media-logo-item">新R25</span>
          <span className="media-logo-sep" />
          <span className="media-logo-item">Powered by TV</span>
          <span className="media-logo-sep" />
          <span className="media-logo-item">YouTube</span>
          <span className="media-logo-sep" />
          <span className="media-logo-item">SNS総フォロワー 5万人超</span>
        </div>

        {/* Featured */}
        <a href={feature.url} target="_blank" rel="noopener noreferrer" className="media-feature reveal">
          <div className="media-feature-thumb">
            <img src={feature.thumb} alt={feature.title} />
            <div className="voice-feature-corners">
              <span className="corner tl" /><span className="corner tr" />
              <span className="corner bl" /><span className="corner br" />
            </div>
            <span className="media-pub-badge">
              <span className="media-pub-badge-tick" />
              {feature.pub}
            </span>
          </div>
          <div className="media-feature-meta">
            <span className="voice-feature-tag">{feature.kind}</span>
            <h3 className="voice-feature-title">{feature.title}</h3>
            <div className="media-feature-row">
              <span className="media-feature-meta-text">{feature.meta}</span>
              <span className="media-link">
                記事を読む
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                  <path d="M3 11L11 3M11 3H5M11 3V9" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round" />
                </svg>
              </span>
            </div>
          </div>
        </a>

        {/* Grid */}
        <div className="media-grid">
          {rest.map((m, i) => (
            <a key={i} href={m.url} target="_blank" rel="noopener noreferrer" className={`media-card reveal delay-${(i % 3) + 1}`}>
              <div className="media-card-thumb">
                <img src={m.thumb} alt={m.title} />
                <div className="voice-thumb-corners">
                  <span className="corner tl" /><span className="corner tr" />
                  <span className="corner bl" /><span className="corner br" />
                </div>
                <span className="media-pub-badge">
                  <span className="media-pub-badge-tick" />
                  {m.pub}
                </span>
              </div>
              <div className="media-card-info">
                <span className="media-kind">{m.kind}</span>
                <h4 className="media-card-title">{m.title}</h4>
                <div className="media-card-foot">
                  <span className="media-card-meta-text">{m.meta}</span>
                  <span className="media-link">
                    記事へ
                    <svg width="12" height="12" viewBox="0 0 14 14" fill="none">
                      <path d="M3 11L11 3M11 3H5M11 3V9" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round" />
                    </svg>
                  </span>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
};

window.Media = Media;
