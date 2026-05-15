// Voice page — testimonials with YouTube interview videos + atmospheric backdrop
const VoicePage = () => {
  const interviews = window.VOICE_INTERVIEWS;

  const PLAYLIST_URL =
    "https://youtube.com/playlist?list=PLe1Lus8pQKOSWIKGd1VlF3q12vdsXAxm3";

  const [activeIdx, setActiveIdx] = React.useState(0);
  const active = interviews[activeIdx];
  const videoUrl = active.id ? `https://youtu.be/${active.id}` : null;
  const thumbImage = active.thumb
    ? `url('${active.thumb}')`
    : active.id
      ? `url('https://i.ytimg.com/vi/${active.id}/hqdefault.jpg')`
      : null;
  const thumbStyle = thumbImage
    ? {
        backgroundImage: thumbImage,
        backgroundSize: "cover",
        backgroundPosition: "center",
      }
    : { background: "var(--bg-2)" };

  return (
    <>
      <section className="voice-hero">
        <div className="voice-hero-bg" />
        <div className="voice-hero-veil" />
        <div className="voice-hero-grain" />

        <div className="voice-hero-inner">
          <div className="voice-hero-eyebrow">
            <span className="line" />
            <span><i>Voices / The Words of Our Graduates</i></span>
            <span className="line" />
          </div>
          <span className="voice-hero-tag">合格者の声</span>
          <h1 className="voice-hero-title">
            <span className="voice-hero-title-l1">憧れの大学を、</span>
            <span className="voice-hero-title-l2"><em>母校</em>に変えた生徒たち。</span>
          </h1>
          <p className="voice-hero-lead">
            模試の朝、参考書を閉じた夜、誰にも言えなかった不安。<br />
            THINKINGを選んだ卒業生たちの、本当の言葉を聞いてください。
          </p>
        </div>
        <div className="voice-hero-scroll" aria-hidden="true">
          <span>Scroll</span>
          <span className="voice-hero-scroll-line" />
        </div>
      </section>

      <section className="voice-featured">
        <div className="voice-featured-inner">
          <div className="voice-section-head">
            <span className="eyebrow"><i>{`Long-form Interview · ${interviews.length} Talks`}</i></span>
            <h2 className="voice-section-title">
              対談動画で、<em>合格までの道のり</em>を。
            </h2>
            <p className="voice-section-lead">
              代表と卒業生の対談。<br />
              入塾前の悩みから、合格後の今までを、本音で。
            </p>
          </div>

          <div className="featured-tabs featured-tabs-many">
            {interviews.map((f, i) => (
              <button
                key={f.pending ? `pending-${f.no}` : f.id}
                type="button"
                className={`featured-tab ${activeIdx === i ? "active" : ""} ${f.pending ? "is-pending" : ""}`}
                onClick={() => setActiveIdx(i)}
              >
                <span className="featured-tab-en"><i>No. {f.no}</i></span>
                <span className="featured-tab-name">{f.name}</span>
                <span className="featured-tab-school">{f.school}</span>
              </button>
            ))}
          </div>

          <div className="featured-stage">
            <div className="featured-video">
              <div className="featured-video-frame">
                {videoUrl ? (
                  <a
                    className="featured-video-thumb"
                    href={videoUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={thumbStyle}
                    aria-label={`${active.name}をYouTubeで開く`}
                  >
                    <span className="featured-play" aria-hidden="true">
                      <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M8 5v14l11-7z" />
                      </svg>
                    </span>
                    <div className="featured-video-grain" />
                  </a>
                ) : (
                  <div
                    className={`featured-video-thumb is-pending${active.thumb ? " has-thumb" : ""}`}
                    style={thumbStyle}
                    aria-label={`${active.name}は準備中です`}
                  >
                    <div className="featured-video-grain" />
                    <div className="featured-pending-label">
                      {active.thumb ? (
                        <span className="featured-pending-jp">動画公開準備中</span>
                      ) : (
                        <>
                          <span className="featured-pending-en"><i>Coming Soon</i></span>
                          <span className="featured-pending-jp">公開準備中</span>
                        </>
                      )}
                    </div>
                  </div>
                )}
              </div>
            </div>

            <aside className="featured-side">
              <span className="featured-eyebrow"><i>Profile</i></span>
              <h3 className="featured-school">{active.school}</h3>
              <p className="featured-year">{active.year}</p>
              <blockquote className="featured-quote">
                <span className="quote-mark">“</span>
                {active.quote}
                <span className="quote-mark close">”</span>
              </blockquote>
              <p className="featured-story">{active.story}</p>
              {videoUrl ? (
                <a
                  href={videoUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="featured-cta"
                >
                  YouTubeで全編を見る
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                    <path d="M5 12h14M13 5l7 7-7 7" />
                  </svg>
                </a>
              ) : (
                <span className="featured-cta featured-cta-disabled">公開までお待ちください</span>
              )}
            </aside>
          </div>

          <div className="voice-playlist-cta">
            <a
              href={PLAYLIST_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="cta cta-playlist"
            >
              <svg className="yt-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.25 5 12 5 12 5s-6.25 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.76 1.77C5.75 19 12 19 12 19s6.25 0 7.84-.43A2.5 2.5 0 0 0 21.6 16.8 26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15V9l5.2 3-5.2 3z"/>
              </svg>
              <span>すべての対談動画を見る（再生リスト）</span>
              <svg className="arrow" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
              </svg>
            </a>
            <span className="voice-playlist-meta">YouTube · THINKING 対談アーカイブ</span>
          </div>
        </div>
      </section>

      <section className="voice-close">
        <div className="voice-close-inner">
          <span className="eyebrow"><i>Be the Next Voice</i></span>
          <h2 className="voice-close-title">
            次の物語を、<br />
            <em>あなた</em>から。
          </h2>
          <p className="voice-close-lead">
            ここにあるのは、合格の話ではない。<br />
            「迷いながらも、毎日進み続けた」その記録です。<br />
            あなたの志望学部にも、同じ物語を。
          </p>
          <a href={window.THINKING_LINE_LIFF_URL} target="_blank" rel="noopener noreferrer" className="cta">
            LINEで無料相談
            <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M5 12h14M13 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      </section>
    </>
  );
};

window.VoicePage = VoicePage;
