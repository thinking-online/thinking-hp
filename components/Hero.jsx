// Hero — concept-first (Polaris-style) for both desktop & mobile
//   Desktop: editorial split (concept-text left ~58%, full-bleed photo right ~42%)
//            3 feature cards in a horizontal row at the bottom of the hero.
//   Mobile:  vertical stack (concept → photo → CTAs → 3 feature cards).
const Hero = () => {
  const [scrollY, setScrollY] = React.useState(0);
  const [mouseX, setMouseX] = React.useState(0);
  const [mouseY, setMouseY] = React.useState(0);

  React.useEffect(() => {
    const onScroll = () => setScrollY(window.scrollY);
    const onMouse = (e) => {
      setMouseX((e.clientX / window.innerWidth - 0.5) * 2);
      setMouseY((e.clientY / window.innerHeight - 0.5) * 2);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("mousemove", onMouse);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("mousemove", onMouse);
    };
  }, []);

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
      {/* Mobile-only first view */}
      <div className="hero-mobile-firstview">
        <div className="hero-mobile-bg-wrap">
          <img
            className="hero-mobile-bg-image"
            src="assets/hero-sse-mobile-student.png"
            alt="勉強に集中する女子学生"
          />
        </div>
        <div className="hero-mobile-overlay hero-mobile-overlay-left" />
        <div className="hero-mobile-overlay hero-mobile-overlay-top" />
        <div className="hero-mobile-overlay hero-mobile-overlay-bottom" />

        <div className="hero-mobile-copy-panel" aria-label="志望学部から逆算する">
          <span>志望学部から、</span>
          <span>逆算する。</span>
        </div>

        <p className="hero-mobile-subcopy">
          早慶上智ICU・MARCH・関関同立まで、<br />
          <span>学部ごと</span>に異なる出題傾向を、<br />
          専属コーチが<span>一対一</span>で攻略します。
        </p>
      </div>

      {/* Desktop full-bleed photo (right half) */}
      <div className="hero-bg hero-bg-desktop-only">
        <div
          className="hero-bg-img hero-bg-img-desktop"
          style={{
            backgroundImage: "url('assets/hero-sse-mobile-student.png')",
            transform: `translate3d(${mouseX * -4}px, calc(${scrollY * 0.2}px + ${mouseY * -3}px), 0) scale(1.02)`,
          }}
        />
        <div className="hero-bg-vignette" />
        <div className="hero-bg-grain" />
      </div>

      {/* Hero content */}
      <div className="hero-content">
        <div className="hero-content-main">
          <div className="hero-eyebrow">
            <span className="line" />
            <span className="hero-eyebrow-text">Online Faculty-Specific Coaching</span>
            <span className="line" />
          </div>

          {/* Concept block — shown on both desktop & mobile */}
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
            <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta">
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

        {/* Feature cards — shown on both, layout differs */}
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

      {/* Scroll indicator — desktop only (see styles-hero-why.css) */}
      <div className="hero-scroll">
        <span className="hero-scroll-text">Scroll</span>
        <span className="hero-scroll-line" />
      </div>
    </section>
  );
};

window.Hero = Hero;
