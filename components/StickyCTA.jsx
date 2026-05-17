// Sticky LINE CTA — pinned to bottom-right across all scroll
const StickyCTA = () => {
  const [open, setOpen] = React.useState(true);
  const [hidden, setHidden] = React.useState(false);
  const [visible, setVisible] = React.useState(false);

  // Show after intro completes (~5s), or immediately if intro was skipped
  React.useEffect(() => {
    let seen = false;
    try {
      seen = window.localStorage.getItem("thinking-intro-seen") === "1";
    } catch {
      seen = false;
    }
    const delay = seen ? 0 : 5400;
    const t = setTimeout(() => setVisible(true), delay);
    return () => clearTimeout(t);
  }, []);

  // Auto-collapse when reaching the final CTA so it doesn't overlap
  React.useEffect(() => {
    const onScroll = () => {
      const finalCTA = document.querySelector(".line-cta-section, .final-cta-section");
      if (!finalCTA) return;
      const r = finalCTA.getBoundingClientRect();
      // hide when final CTA enters the viewport
      setHidden(r.top < window.innerHeight * 0.85);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  if (!visible) return null;

  return (
    <div className={`sticky-cta ${open ? "open" : "closed"} ${hidden ? "out" : ""}`}>
      {open && (
        <button
          type="button"
          className="sticky-cta-close"
          onClick={() => setOpen(false)}
          aria-label="閉じる"
        >
          ×
        </button>
      )}

      {open ? (
        <a
          className="sticky-cta-card"
          href={window.THINKING_LINE_LIFF_URL}
          target="_blank"
          rel="noopener noreferrer"
        >
          <div className="sticky-cta-icon" aria-hidden="true">
            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
              <path
                fill="currentColor"
                d="M16 3C8.27 3 2 7.96 2 14.07c0 3.66 2.31 6.9 5.86 8.92c-.26.97-.95 3.55-1.09 4.1c-.17.69.25.68.53.49c.22-.15 3.5-2.38 4.92-3.34c1.22.18 2.5.27 3.78.27c7.73 0 14-4.96 14-11.07S23.73 3 16 3z"
              />
              <text
                x="16"
                y="17.5"
                textAnchor="middle"
                fontFamily="Helvetica, Arial, sans-serif"
                fontSize="6.5"
                fontWeight="700"
                fill="#0a0907"
                letterSpacing="0.05em"
              >
                LINE
              </text>
            </svg>
          </div>
          <div className="sticky-cta-text">
            <span className="sticky-cta-eyebrow">
              <span className="dot" />
              <span>受付中 — 月<span className="sticky-cta-num">10</span>名限定</span>
            </span>
            <span className="sticky-cta-title">
              私立文系の<em>個別戦略相談会</em>
            </span>
            <span className="sticky-cta-sub">
              公式LINE追加 <span className="arrow">→</span>{" "}
              <span className="sticky-cta-num">60</span>分・無料
            </span>
          </div>
          <div className="sticky-cta-shine" />
        </a>
      ) : (
        <button
          type="button"
          className="sticky-cta-mini"
          onClick={() => setOpen(true)}
          aria-label="個別戦略相談会"
        >
          <div className="sticky-cta-icon" aria-hidden="true">
            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
              <path
                fill="currentColor"
                d="M16 3C8.27 3 2 7.96 2 14.07c0 3.66 2.31 6.9 5.86 8.92c-.26.97-.95 3.55-1.09 4.1c-.17.69.25.68.53.49c.22-.15 3.5-2.38 4.92-3.34c1.22.18 2.5.27 3.78.27c7.73 0 14-4.96 14-11.07S23.73 3 16 3z"
              />
              <text
                x="16"
                y="17.5"
                textAnchor="middle"
                fontFamily="Helvetica, Arial, sans-serif"
                fontSize="6.5"
                fontWeight="700"
                fill="#0a0907"
                letterSpacing="0.05em"
              >
                LINE
              </text>
            </svg>
          </div>
          <span className="sticky-cta-mini-pulse" />
        </button>
      )}
    </div>
  );
};

window.StickyCTA = StickyCTA;
