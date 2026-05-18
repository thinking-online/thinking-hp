// Hero — mobile first view (vertical copy) + desktop cinematic (horizontal copy)
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

      {/* Desktop full-bleed photo */}
      <div className="hero-bg hero-bg-desktop-only">
        <div
          className="hero-bg-img hero-bg-img-desktop"
          style={{
            backgroundImage: "url('assets/hero-desktop-student.png')",
            transform: `translate3d(${mouseX * -4}px, calc(${scrollY * 0.2}px + ${mouseY * -3}px), 0) scale(1.02)`,
          }}
        />
        <div className="hero-bg-vignette" />
        <div className="hero-bg-grain" />
      </div>

      {/* Desktop hero content */}
      <div className="hero-content">
        <div className="hero-content-main">
          <div className="hero-eyebrow">
            <span className="line" />
            <span className="hero-eyebrow-text">Online Faculty-Specific Coaching</span>
            <span className="line" />
          </div>

          <div className="hero-concept">
            <h1 className="hero-concept-headline" aria-label="志望学部から逆算する">
              志望学部から、<em>逆算する。</em>
            </h1>

            <p className="hero-concept-sub">
              早慶上智ICU・MARCH・関関同立まで、
              <span className="hero-accent">学部ごと</span>に異なる出題傾向を、
              専属コーチが<span className="hero-accent">一対一</span>で攻略します。
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
      </div>

      <div className="hero-scroll">
        <span className="hero-scroll-text">Scroll</span>
        <span className="hero-scroll-line" />
      </div>
    </section>
  );
};

window.Hero = Hero;
