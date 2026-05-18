/* SSE LP — floating LINE CTA (homepage-style) */
function StickyLineCTA() {
  const [open, setOpen] = React.useState(true);
  const [hidden, setHidden] = React.useState(false);
  const lineUrl = window.THINKING_LINE_LIFF_URL || "#";

  React.useEffect(() => {
    const onScroll = () => {
      const finalCTA = document.querySelector("#cta, .price-section");
      if (!finalCTA) return;
      const r = finalCTA.getBoundingClientRect();
      setHidden(r.top < window.innerHeight * 0.85);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div className={`sse-sticky-line ${open ? "open" : "closed"} ${hidden ? "out" : ""}`}>
      {open && (
        <button
          type="button"
          className="sse-sticky-line-close"
          onClick={() => setOpen(false)}
          aria-label="閉じる"
        >
          ×
        </button>
      )}

      {open ? (
        <a
          className="sse-sticky-line-card"
          href={lineUrl}
          target="_blank"
          rel="noopener noreferrer"
        >
          <div className="sse-sticky-line-icon" aria-hidden="true">
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
                fill="#0a1530"
                letterSpacing="0.05em"
              >
                LINE
              </text>
            </svg>
          </div>
          <div className="sse-sticky-line-text">
            <span className="sse-sticky-line-eyebrow">
              <span className="dot" />
              <span>受付中 — 先着30名</span>
            </span>
            <span className="sse-sticky-line-title">
              SSE 45日間<em>個別相談</em>
            </span>
            <span className="sse-sticky-line-sub">
              公式LINE追加 <span className="arrow">→</span> 無料面談
            </span>
          </div>
          <span className="sse-sticky-line-shine" aria-hidden="true" />
        </a>
      ) : (
        <button
          type="button"
          className="sse-sticky-line-mini"
          onClick={() => setOpen(true)}
          aria-label="LINEで個別相談する"
        >
          <span className="sse-sticky-line-icon" aria-hidden="true">
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
                fill="#0a1530"
                letterSpacing="0.05em"
              >
                LINE
              </text>
            </svg>
          </span>
          <span className="sse-sticky-line-mini-pulse" aria-hidden="true" />
        </button>
      )}
    </div>
  );
}

window.StickyLineCTA = StickyLineCTA;