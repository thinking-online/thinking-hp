// Intro splash — fades in/out before revealing main page
const Intro = () => {
  const [phase, setPhase] = React.useState("entering"); // entering -> showing -> exiting -> done

  React.useEffect(() => {
    // Block body scroll while intro is up
    document.body.style.overflow = "hidden";

    const t1 = setTimeout(() => setPhase("showing"), 100);
    const t2 = setTimeout(() => setPhase("exiting"), 4200);
    const t3 = setTimeout(() => {
      setPhase("done");
      document.body.style.overflow = "";
      window.scrollTo(0, 0);
    }, 5200);

    return () => {
      clearTimeout(t1); clearTimeout(t2); clearTimeout(t3);
      document.body.style.overflow = "";
    };
  }, []);

  if (phase === "done") return null;

  return (
    <div className={`intro intro-${phase}`}>
      <div className="intro-bg" />
      <div className="intro-grain" />

      <div className="intro-content">
        <div className="intro-line-wrap">
          <span className="intro-line" />
        </div>

        <p className="intro-jp">
          <span className="ch">一</span>
          <span className="ch">切</span>
          <span className="ch">、</span>
          <span className="ch">妥</span>
          <span className="ch">協</span>
          <span className="ch">し</span>
          <span className="ch">な</span>
          <span className="ch">い</span>
          <span className="ch">。</span>
        </p>

        <p className="intro-jp intro-jp-2">
          <span className="ch">私</span>
          <span className="ch">立</span>
          <span className="ch">文</span>
          <span className="ch">系</span>
          <span className="ch">専</span>
          <span className="ch">門</span>
          <span className="ch">塾</span>
          <span className="ch">。</span>
        </p>

        <h1 className="intro-brand">
          <span className="intro-brand-logo" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
              <ellipse cx="32" cy="32" rx="26" ry="11" stroke="currentColor" strokeWidth="1.2" transform="rotate(35 32 32)" opacity="0.9" />
              <ellipse cx="32" cy="32" rx="26" ry="11" stroke="currentColor" strokeWidth="1.2" transform="rotate(-35 32 32)" opacity="0.9" />
              <circle cx="56" cy="22" r="1.4" fill="currentColor" />
              <circle cx="8" cy="42" r="1.4" fill="currentColor" />
              <g stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" fill="none">
                <path d="M32 20.5 C 27.5 18.5, 22 20, 21 24.5 C 18.5 25, 17 27.5, 18 30 C 16.5 32, 17.5 35, 19.5 35.5 C 19 38.5, 22 41, 25 40 C 26 42.5, 30 43, 32 41" />
                <path d="M32 20.5 C 36.5 18.5, 42 20, 43 24.5 C 45.5 25, 47 27.5, 46 30 C 47.5 32, 46.5 35, 44.5 35.5 C 45 38.5, 42 41, 39 40 C 38 42.5, 34 43, 32 41" />
                <path d="M32 20.5 L 32 41" opacity="0.6" />
                <path d="M24 26 C 26 27, 27 29, 26 31" opacity="0.7" />
                <path d="M22 32 C 24 33, 25 34.5, 24 36" opacity="0.7" />
                <path d="M40 26 C 38 27, 37 29, 38 31" opacity="0.7" />
                <path d="M42 32 C 40 33, 39 34.5, 40 36" opacity="0.7" />
              </g>
            </svg>
          </span>
          <span className="intro-brand-mark">THINKING</span>
        </h1>

        <p className="intro-tag">
          <i>Designed for Your Faculty.</i>
        </p>

        <div className="intro-line-wrap bottom">
          <span className="intro-line" />
        </div>
      </div>

      <div className="intro-corner tl" />
      <div className="intro-corner tr" />
      <div className="intro-corner bl" />
      <div className="intro-corner br" />
    </div>
  );
};

window.Intro = Intro;
