// Hero section — full-bleed dark with parallax library bg + serif typography
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
      {/* Background layers — full-bleed studying scene */}
      <div className="hero-bg">
        <div
          className="hero-bg-img hero-bg-img-desktop"
          style={{
            backgroundImage: "url('assets/hero-male-new.png')",
            transform: `translate3d(${mouseX * -4}px, calc(${scrollY * 0.2}px + ${mouseY * -3}px), 0) scale(1.02)`,
          }}
        />
        <div
          className="hero-bg-img hero-bg-img-mobile"
          style={{
            backgroundImage: "url('assets/hero-male-new.png')",
            transform: `translate3d(0, ${scrollY * 0.12}px, 0) scale(1.02)`,
          }}
        />
        <div className="hero-bg-vignette" />
        <div className="hero-bg-grain" />
      </div>

      {/* Hero content */}
      <div className="hero-content">
        <div className="hero-eyebrow">
          <span className="line" />
          <span className="hero-eyebrow-text">Online Faculty-Specific Coaching</span>
          <span className="line" />
        </div>

        <h1 className="hero-title">
          <span className="hero-title-line line-1">
            <span className="nobr">私立文系</span>・<span className="nobr"><em>学部別</em>の、</span>
          </span>
          <span className="hero-title-line line-2">
            <span className="nobr">合格<em>設計</em>塾。</span>
          </span>
        </h1>

        <p className="hero-tag">
          <i>Designed for Your Faculty.</i>
        </p>

        <p className="hero-lead">
          <span className="nobr">「学部別」だから、勝てる。</span><br />
          <span className="nobr">早慶上智ICU・MARCH・関関同立まで、</span><br />
          <span className="nobr">志望学部ごとに異なる出題傾向と対策を、</span>
          <span className="nobr">専属コーチが一対一で設計します。</span>
        </p>

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

        <div className="hero-stats">
          <div className="hero-stat">
            <span className="stat-num">3<i>Y+</i></span>
            <span className="stat-label">Years of Practice</span>
          </div>
          <span className="stat-sep" />
          <div className="hero-stat">
            <span className="stat-num">30<i>+</i></span>
            <span className="stat-label">Student Voices</span>
          </div>
          <span className="stat-sep" />
          <div className="hero-stat">
            <span className="stat-num">1:1</span>
            <span className="stat-label">Faculty Coaching</span>
          </div>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="hero-scroll">
        <span className="hero-scroll-text">Scroll</span>
        <span className="hero-scroll-line" />
      </div>
    </section>
  );
};

window.Hero = Hero;
