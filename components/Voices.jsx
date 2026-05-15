// Voices — horizontal swipe carousel; each card opens its YouTube interview
const Voices = () => {
  const voices = React.useMemo(
    () =>
      window.VOICE_INTERVIEWS.map((v) => ({
        thumb: v.thumb,
        headline: v.headline,
        result: `${v.school}${v.year ? ` ${v.year}` : ""}`,
        meta: v.tag,
        name: v.name,
        duration: v.pending ? "準備中" : "対談動画",
        url: v.pending ? null : `https://youtu.be/${v.id}`,
        pending: v.pending,
        no: v.no,
      })),
    []
  );

  const count = voices.length;
  const loopedVoices = React.useMemo(() => {
    if (!count) return [];
    const wrap = (v, key) => ({ ...v, _key: key });
    return [
      wrap(voices[count - 1], "clone-start"),
      ...voices.map((v, i) => wrap(v, `item-${i}`)),
      wrap(voices[0], "clone-end"),
    ];
  }, [voices, count]);

  const trackRef = React.useRef(null);
  const jumpingRef = React.useRef(false);
  const [activeDomIdx, setActiveDomIdx] = React.useState(1);
  const [isDesktop, setIsDesktop] = React.useState(() =>
    typeof window !== "undefined" && window.matchMedia("(min-width: 769px)").matches
  );

  const realIdxFromDom = (domIdx) => {
    if (domIdx <= 0) return count - 1;
    if (domIdx >= count + 1) return 0;
    return domIdx - 1;
  };

  const activeIdx = realIdxFromDom(activeDomIdx);

  React.useEffect(() => {
    const mq = window.matchMedia("(min-width: 769px)");
    const onChange = () => setIsDesktop(mq.matches);
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, []);

  const scrollToDom = React.useCallback((domIdx, smooth = true) => {
    const el = trackRef.current;
    if (!el || !count) return;
    const card = el.querySelectorAll(".voice-card")[domIdx];
    if (!card) return;
    el.scrollTo({ left: card.offsetLeft, behavior: smooth ? "smooth" : "auto" });
  }, [count]);

  const scrollToReal = React.useCallback(
    (realIdx, smooth = true) => {
      scrollToDom(realIdx + 1, smooth);
    },
    [scrollToDom]
  );

  const getNearestDomIdx = React.useCallback(() => {
    const el = trackRef.current;
    if (!el) return 1;
    const cards = el.querySelectorAll(".voice-card");
    if (!cards.length) return 1;

    const trackLeft = el.scrollLeft;
    let nearestIdx = 1;
    let nearestDist = Infinity;
    cards.forEach((card, i) => {
      const dist = Math.abs(card.offsetLeft - trackLeft);
      if (dist < nearestDist) {
        nearestDist = dist;
        nearestIdx = i;
      }
    });
    return nearestIdx;
  }, []);

  const repositionIfOnClone = React.useCallback(() => {
    const el = trackRef.current;
    if (!el || !count || jumpingRef.current) return;

    const domIdx = getNearestDomIdx();
    if (domIdx !== 0 && domIdx !== count + 1) return;

    jumpingRef.current = true;
    const targetDom = domIdx === 0 ? count : 1;
    el.style.scrollBehavior = "auto";
    scrollToDom(targetDom, false);
    el.style.scrollBehavior = "";
    setActiveDomIdx(targetDom);
    requestAnimationFrame(() => {
      jumpingRef.current = false;
    });
  }, [count, getNearestDomIdx, scrollToDom]);

  const updateScrollState = React.useCallback(() => {
    if (jumpingRef.current || !count) return;

    const domIdx = getNearestDomIdx();
    setActiveDomIdx(domIdx);

    if (domIdx === 0 || domIdx === count + 1) {
      requestAnimationFrame(repositionIfOnClone);
    }
  }, [count, getNearestDomIdx, repositionIfOnClone]);

  React.useEffect(() => {
    if (!count) return;
    scrollToDom(1, false);
    setActiveDomIdx(1);
  }, [count, scrollToDom]);

  React.useEffect(() => {
    const el = trackRef.current;
    if (!el) return;
    updateScrollState();
    el.addEventListener("scroll", updateScrollState, { passive: true });
    el.addEventListener("scrollend", repositionIfOnClone);
    window.addEventListener("resize", updateScrollState);
    return () => {
      el.removeEventListener("scroll", updateScrollState);
      el.removeEventListener("scrollend", repositionIfOnClone);
      window.removeEventListener("resize", updateScrollState);
    };
  }, [updateScrollState, repositionIfOnClone]);

  const scrollByDir = (dir) => {
    if (!count) return;
    // 端からループするときはクローン経由で「つながった」方向へ進む
    if (dir === 1 && activeDomIdx === count) {
      scrollToDom(count + 1, true);
      return;
    }
    if (dir === -1 && activeDomIdx === 1) {
      scrollToDom(0, true);
      return;
    }
    const nextReal = (activeIdx + dir + count) % count;
    scrollToReal(nextReal, true);
  };

  const PlayIcon = () => (
    <span className="voice-thumb-play" aria-hidden="true">
      <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="32" cy="32" r="30" fill="rgba(10, 9, 7, 0.55)" stroke="currentColor" strokeWidth="1.2" />
        <path d="M26 20v24l18-12-18-12z" fill="currentColor" />
      </svg>
    </span>
  );

  const WatchButton = ({ url, name }) => (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className="voice-watch-btn"
      aria-label={`${name}の対談動画をYouTubeで開く`}
    >
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M8 5v14l11-7z" />
      </svg>
      対談動画を見る
    </a>
  );

  const renderCard = (v, domIdx) => {
    const cardClass = `voice-card ${domIdx === activeDomIdx ? "active" : ""} ${v.pending ? "is-pending" : ""}`;
    const thumbInner = (
      <>
        <div className="voice-thumb">
          {v.thumb ? (
            <img src={v.thumb} alt={v.headline} className="voice-thumb-img" draggable="false" />
          ) : (
            <div className="voice-thumb-placeholder" aria-hidden="true" />
          )}
          <span className="voice-index"><i>No. {v.no}</i></span>
          <span className="voice-duration">{v.duration}</span>
          {!v.pending && <PlayIcon />}
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
        <div key={v._key} className={cardClass} aria-label={`${v.name}は準備中です`} data-dom-idx={domIdx}>
          {thumbInner}
        </div>
      );
    }

    if (isDesktop) {
      return (
        <div key={v._key} className={`${cardClass} voice-card--desktop`} data-dom-idx={domIdx}>
          {thumbInner}
          <WatchButton url={v.url} name={v.name} />
        </div>
      );
    }

    return (
      <a
        key={v._key}
        href={v.url}
        target="_blank"
        rel="noopener noreferrer"
        className={cardClass}
        data-dom-idx={domIdx}
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
            className="voice-arrow voice-arrow-prev"
            onClick={() => scrollByDir(-1)}
            aria-label="前へ"
          >
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M15 6l-6 6 6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
            </svg>
          </button>
          <button
            type="button"
            className="voice-arrow voice-arrow-next"
            onClick={() => scrollByDir(1)}
            aria-label="次へ"
          >
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M9 6l6 6-6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
            </svg>
          </button>

          <div
            className={`voices-track${isDesktop ? " voices-track--desktop" : ""}`}
            ref={trackRef}
          >
            {loopedVoices.map((v, i) => renderCard(v, i))}
          </div>
        </div>

        <div className="voices-pagination">
          {voices.map((_, i) => (
            <button
              key={i}
              type="button"
              className={`voice-dot ${i === activeIdx ? "active" : ""}`}
              onClick={() => scrollToReal(i, true)}
              aria-label={`${i + 1}番目`}
            />
          ))}
        </div>

        <div className="voices-hint">
          <span className="voices-hint-arrow">←</span>
          <span>{isDesktop ? "矢印で切り替え" : "swipe"}</span>
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
