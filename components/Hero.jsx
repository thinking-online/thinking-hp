// Hero — overlay stage (copy + bounded photo panel, not forced full-bleed)
const Hero = () => {
  const features = [
    {
      no: "01",
      en: "Faculty-Specific",
      jp: "学部別",
      title: "学部ごとに、戦略が違う。",
      desc: "早慶上智ICU・MARCH・関関同立。出題傾向は学部ごとに別物。",
      href: "#why",
      icon: (
        <svg viewBox="0 0 32 32" fill="none">
          <path d="M6 8h20M6 14h20M6 20h12M6 26h8" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
          <circle cx="24" cy="22" r="4" stroke="currentColor" strokeWidth="1.4" />
          <path d="M27 25l3 3" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
        </svg>
      ),
    },
    {
      no: "02",
      en: "1:1 Coach",
      jp: "専属コーチ",
      title: "ひとりに、ひとり。",
      desc: "受験を終えた現役早慶生コーチが、合格まで完全伴走する。",
      href: "#capacity",
      icon: (
        <svg viewBox="0 0 32 32" fill="none">
          <circle cx="11" cy="12" r="4" stroke="currentColor" strokeWidth="1.4" />
          <circle cx="22" cy="12" r="4" stroke="currentColor" strokeWidth="1.4" />
          <path d="M4 26c0-3.5 3-6 7-6s7 2.5 7 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
          <path d="M16 26c1-2.5 3-4 6-4s5 1.5 6 4" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
        </svg>
      ),
    },
    {
      no: "03",
      en: "Data-Driven",
      jp: "徹底数値管理",
      title: "毎日、数字で追う。",
      desc: "学習量・正答率・偏差値を毎日トラッキング。感覚で語らない。",
      href: "#method",
      icon: (
        <svg viewBox="0 0 32 32" fill="none">
          <path d="M5 26V6M5 26h22" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
          <path d="M9 22l5-7 4 4 7-10" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" />
          <circle cx="9" cy="22" r="1.5" fill="currentColor" />
          <circle cx="14" cy="15" r="1.5" fill="currentColor" />
          <circle cx="18" cy="19" r="1.5" fill="currentColor" />
          <circle cx="25" cy="9" r="1.5" fill="currentColor" />
        </svg>
      ),
    },
  ];

  return (
    <section className="hero" id="top">
      <div className="hero-shell">
        <figure className="hero-visual">
          <img
            className="hero-visual-img"
            src="assets/hero-sse-mobile-student.png"
            alt="勉強に集中する女子学生"
            width="576"
            height="1024"
            fetchPriority="high"
          />
          <div className="hero-visual-scrim hero-visual-scrim-edge" aria-hidden="true" />
          <div className="hero-visual-scrim hero-visual-scrim-bottom" aria-hidden="true" />
        </figure>

        <div className="hero-content">
          <div className="hero-content-main">
            <div className="hero-eyebrow">
              <span className="line" />
              <span className="hero-eyebrow-text">Online Faculty-Specific Coaching</span>
              <span className="line" />
            </div>

            <div className="hero-concept">
              <h1 className="hero-concept-headline">
                <span className="hcl"><span className="hl">学部別</span>に設計された、</span>
                <span className="hcl"><span className="hl">最短ルート</span>の、</span>
                <span className="hcl"><span className="hl">逆算合格設計</span>。</span>
              </h1>

              <p className="hero-concept-tag">
                <i>Designed for Your Faculty.</i>
              </p>

              <p className="hero-concept-sub">
                早慶上智ICU・MARCH・関関同立まで、<br />
                学部ごとに異なる出題傾向を、<br />
                専属コーチが一対一で攻略します。
              </p>
            </div>

            <div className="hero-ctas">
              <a href={window.THINKING_LINE_LIFF_URL} target="_blank" rel="noopener noreferrer" className="cta">
                <span>LINEで無料相談</span>
                <svg className="arrow" viewBox="0 0 16 16" fill="none">
                  <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
                </svg>
              </a>
              <a href="#voices" className="cta-ghost">
                <span>合格者の声を見る</span>
                <span className="dot">↓</span>
              </a>
            </div>
          </div>

          <div className="hero-features">
            {features.map((f) => (
              <a key={f.no} href={f.href} className="hero-feature-card">
                <div className="hf-top">
                  <div className="hf-no">{f.no}</div>
                  <div className="hf-icon">{f.icon}</div>
                </div>
                <div className="hf-en">{f.en}</div>
                <div className="hf-jp">{f.jp}</div>
                <div className="hf-title">{f.title}</div>
                <div className="hf-desc">{f.desc}</div>
                <div className="hf-arrow">
                  <svg viewBox="0 0 16 16" fill="none">
                    <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
                  </svg>
                </div>
              </a>
            ))}
          </div>
        </div>
      </div>

      <div className="hero-scroll">
        <span className="hero-scroll-text">Scroll</span>
        <span className="hero-scroll-line" />
      </div>
    </section>
  );
};

window.Hero = Hero;
