// Voices — horizontal swipe carousel; each card opens its YouTube interview
const Voices = () => {
  const voices = window.VOICE_INTERVIEWS.map((v) => ({
    thumb: v.thumb,
    headline: v.headline,
    result: `${v.school}${v.year ? ` ${v.year}` : ""}`,
    meta: v.tag,
    name: v.name,
    duration: v.pending ? "準備中" : "対談動画",
    url: v.pending ? null : `https://youtu.be/${v.id}`,
    pending: v.pending,
    no: v.no,
  }));

  const trackRef = React.useRef(null);
  const [activeIdx, setActiveIdx] = React.useState(0);
  const [canPrev, setCanPrev] = React.useState(false);
  const [canNext, setCanNext] = React.useState(true);

  const updateScrollState = React.useCallback(() => {
    const el = trackRef.current;
    if (!el) return;
    const cards = el.querySelectorAll(".voice-card");
    if (!cards.length) return;

    const trackLeft = el.scrollLeft;
    let nearestIdx = 0;
    let nearestDist = Infinity;
    cards.forEach((card, i) => {
      const dist = Math.abs(card.offsetLeft - trackLeft);
      if (dist < nearestDist) {
        nearestDist = dist;
        nearestIdx = i;
      }
    });
    setActiveIdx(nearestIdx);
    setCanPrev(el.scrollLeft > 4);
    setCanNext(el.scrollLeft < el.scrollWidth - el.clientWidth - 4);
  }, []);

  React.useEffect(() => {
    const el = trackRef.current;
    if (!el) return;
    updateScrollState();
    el.addEventListener("scroll", updateScrollState, { passive: true });
    window.addEventListener("resize", updateScrollState);
    return () => {
      el.removeEventListener("scroll", updateScrollState);
      window.removeEventListener("resize", updateScrollState);
    };
  }, [updateScrollState]);

  const scrollToCard = (idx) => {
    const el = trackRef.current;
    if (!el) return;
    const card = el.querySelectorAll(".voice-card")[idx];
    if (!card) return;
    el.scrollTo({ left: card.offsetLeft, behavior: "smooth" });
  };

  const scrollByDir = (dir) => {
    const next = Math.max(0, Math.min(voices.length - 1, activeIdx + dir));
    scrollToCard(next);
  };

  React.useEffect(() => {
    const el = trackRef.current;
    if (!el) return;
    let isDown = false;
    let startX = 0;
    let scrollStart = 0;
    let moved = false;

    const onDown = (e) => {
      if (e.pointerType !== "mouse") return;
      isDown = true;
      moved = false;
      startX = e.pageX;
      scrollStart = el.scrollLeft;
      el.classList.add("dragging");
    };
    const onMove = (e) => {
      if (!isDown) return;
      const dx = e.pageX - startX;
      if (Math.abs(dx) > 12) moved = true;
      el.scrollLeft = scrollStart - dx;
    };
    const onUp = () => {
      if (!isDown) return;
      isDown = false;
      el.classList.remove("dragging");
      if (moved) {
        const blockClick = (e) => {
          e.preventDefault();
          e.stopPropagation();
          window.removeEventListener("click", blockClick, true);
        };
        window.addEventListener("click", blockClick, true);
      }
    };

    el.addEventListener("pointerdown", onDown);
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
    window.addEventListener("pointercancel", onUp);
    return () => {
      el.removeEventListener("pointerdown", onDown);
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      window.removeEventListener("pointercancel", onUp);
    };
  }, []);

  const renderCard = (v, i) => {
    const cardClass = `voice-card ${i === activeIdx ? "active" : ""} ${v.pending ? "is-pending" : ""}`;
    const thumbInner = (
      <>
        <div className="voice-thumb">
          {v.thumb ? (
            <img src={v.thumb} alt={v.headline} className="voice-thumb-img" draggable="false" />
          ) : (
            <div className="voice-thumb-placeholder" aria-hidden="true" />
          )}
          <div className="voice-thumb-corners">
            <span className="corner tl" /><span className="corner tr" />
            <span className="corner bl" /><span className="corner br" />
          </div>
        </div>
        <div className="voice-info">
          <h4 className="voice-headline">{v.headline}</h4>
          <div className="voice-result-row">
            <span className="voice-result">{v.result}</span>
          </div>
          <div className="voice-meta-row">
            <span className="voice-meta-text">{v.meta}</span>
            <span className="voice-name">— {v.name}</span>
          </div>
        </div>
      </>
    );

    if (v.pending) {
      return (
        <div key={v.no} className={cardClass} aria-label={`${v.name}は準備中です`}>
          {thumbInner}
        </div>
      );
    }

    return (
      <a
        key={v.no}
        href={v.url}
        target="_blank"
        rel="noopener noreferrer"
        className={cardClass}
      >
        {thumbInner}
      </a>
    );
  };

  return (
    <section className="section voices-section" id="voices">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Voices · 対談アーカイブ</i></span>
          <h2 className="section-title">
            合格者たちの、<em>本当の言葉</em>。
          </h2>
          <p className="section-lead">
            数字や偏差値の前に、ひとりの人生がある。<br />
            実際に合格を掴んだ受講生たちの、フルレングスの対談動画。
          </p>
          <div className="ornament"><span className="ornament-mark" /></div>
        </div>

        <div className="voices-carousel">
          <button
            type="button"
            className={`voice-arrow voice-arrow-prev ${canPrev ? "" : "disabled"}`}
            onClick={() => scrollByDir(-1)}
            aria-label="前へ"
          >
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M15 6l-6 6 6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
            </svg>
          </button>
          <button
            type="button"
            className={`voice-arrow voice-arrow-next ${canNext ? "" : "disabled"}`}
            onClick={() => scrollByDir(1)}
            aria-label="次へ"
          >
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M9 6l6 6-6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
            </svg>
          </button>

          <div className="voices-track" ref={trackRef}>
            {voices.map((v, i) => renderCard(v, i))}
          </div>
        </div>

        <div className="voices-pagination">
          {voices.map((_, i) => (
            <button
              key={i}
              type="button"
              className={`voice-dot ${i === activeIdx ? "active" : ""}`}
              onClick={() => scrollToCard(i)}
              aria-label={`${i + 1}番目`}
            />
          ))}
        </div>

        <div className="voices-hint">
          <span className="voices-hint-arrow">←</span>
          <span>swipe</span>
          <span className="voices-hint-arrow">→</span>
        </div>

        <div className="voices-cta">
          <a
            href="https://youtube.com/playlist?list=PLe1Lus8pQKOSWIKGd1VlF3q12vdsXAxm3"
            target="_blank"
            rel="noopener noreferrer"
            className="voices-cta-btn"
          >
            <span className="voices-cta-label">
              <i>Watch All</i>
              <span>すべての対談動画を見る（再生リスト）</span>
            </span>
            <span className="voices-cta-arrow">
              <svg viewBox="0 0 24 24" fill="none">
                <path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </span>
          </a>
          <span className="voices-cta-meta">YouTube · THINKING 対談アーカイブ</span>
        </div>
      </div>
    </section>
  );
};

window.Voices = Voices;
