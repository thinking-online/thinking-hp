// Voices — horizontal swipe carousel; each card opens its YouTube interview
const Voices = () => {
  const voices = [
    {
      thumb: "assets/thumb-keio-geneki.png",
      headline: "非進学校から、慶應現役合格。",
      result: "慶應義塾大学 現役合格",
      meta: "偏差値60未満 / 逆転合格",
      name: "合格者インタビュー",
      duration: "対談動画",
      url: "https://youtu.be/Xid8x7UUJfE",
    },
    {
      thumb: "assets/thumb-aoyama-geneki.png",
      headline: "E判定・学年ビリから、逆転現役合格。",
      result: "青山学院大学 現役合格",
      meta: "高3の11月まで部活",
      name: "合格者インタビュー",
      duration: "対談動画",
      url: "https://youtu.be/CcwIX4-j2Mo",
    },
    {
      thumb: "assets/thumb-aboshi.png",
      headline: "最下位層から、学年3位。",
      result: "関西学院大学 現役合格",
      meta: "週7部活 / 偏差値62",
      name: "合格者インタビュー",
      duration: "12:48",
      url: "https://youtu.be/8R0aILkSbhc",
    },
    {
      thumb: "assets/thumb-matsuyama.png",
      headline: "高3秋・E判定から親子で号泣。",
      result: "MARCH 全勝",
      meta: "親子インタビュー",
      name: "合格者インタビュー",
      duration: "18:22",
      url: "https://youtu.be/Qp17tvgggOQ",
    },
    {
      thumb: "assets/thumb-march.png",
      headline: "全落ちからの、奇跡のダブル合格。",
      result: "関学・法政・中央 合格",
      meta: "偏差値39 → 全勝",
      name: "合格者インタビュー",
      duration: "15:04",
      url: "https://youtu.be/e5OzmZKSe28",
    },
    {
      thumb: "assets/thumb-toyama.jpg",
      headline: "高校受験失敗から、学年トップへ。",
      result: "偏差値70超え",
      meta: "英語・国語",
      name: "合格者インタビュー",
      duration: "14:11",
      url: "https://youtu.be/HP_5tDBODaY",
    },
    {
      thumb: "assets/thumb-nakamura.png",
      headline: "日本史県内1位、英語48.2から逆転。",
      result: "関西学院大学 合格",
      meta: "苦手克服インタビュー",
      name: "合格者インタビュー",
      duration: "16:35",
      url: "https://youtu.be/NwrlH_tyukA",
    },
  ];

  const trackRef = React.useRef(null);
  const [activeIdx, setActiveIdx] = React.useState(0);
  const [canPrev, setCanPrev] = React.useState(false);
  const [canNext, setCanNext] = React.useState(true);

  // Track scroll position to update active index + button states
  const updateScrollState = React.useCallback(() => {
    const el = trackRef.current;
    if (!el) return;
    const cards = el.querySelectorAll(".voice-card");
    if (!cards.length) return;

    // Find which card is closest to the left edge (snap point)
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

  // Drag-to-scroll for desktop (mouse)
  React.useEffect(() => {
    const el = trackRef.current;
    if (!el) return;
    let isDown = false;
    let startX = 0;
    let scrollStart = 0;
    let moved = false;

    const onDown = (e) => {
      // Only left mouse button, ignore touch (touch uses native scroll)
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
      // Suppress click if dragged
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

        {/* Carousel */}
        <div className="voices-carousel">
          {/* Prev / next buttons (PC only) */}
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
            {voices.map((v, i) => (
              <a
                key={i}
                href={v.url}
                target="_blank"
                rel="noopener noreferrer"
                className={`voice-card ${i === activeIdx ? "active" : ""}`}
              >
                <div className="voice-thumb">
                  <img src={v.thumb} alt={v.headline} className="voice-thumb-img" draggable="false" />
                  <div className="voice-thumb-corners">
                    <span className="corner tl" /><span className="corner tr" />
                    <span className="corner bl" /><span className="corner br" />
                  </div>
                  <div className="voice-thumb-play">
                    <svg viewBox="0 0 56 56" fill="none">
                      <circle cx="28" cy="28" r="27" stroke="currentColor" strokeWidth="1" fill="rgba(10,9,7,0.55)" />
                      <path d="M22 18v20l16-10z" fill="currentColor" />
                    </svg>
                  </div>
                  <span className="voice-duration">{v.duration}</span>
                  <span className="voice-index">
                    <i>{String(i + 1).padStart(2, "0")}</i> / {String(voices.length).padStart(2, "0")}
                  </span>
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
              </a>
            ))}
          </div>
        </div>

        {/* Pagination dots */}
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
