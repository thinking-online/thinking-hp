// Voice page — testimonials with YouTube interview videos + atmospheric backdrop
const VoicePage = () => {
  // 8 long-form interviews. Tabs let you switch the featured video.
  const interviews = [
    {
      id: "8R0aILkSbhc",
      name: "卒業生 01",
      en: "Interview 01",
      school: "早稲田大学 法学部",
      year: "2025年度合格",
      tag: "現役合格 / 高3春から",
      quote: "条文を覚えるのではなく、論理を読む。学部別の戦略があるから、毎日の勉強に迷いがなくなった。",
      story:
        "高3の春、模試の判定はDだった。法学部志望と決めた瞬間から、コーチは「論理構成」と「要約力」だけに焦点を絞ってくれた。日々のSlack報告と週次面談で、自分の弱点が可視化されていった。",
    },
    {
      id: "Qp17tvgggOQ",
      name: "卒業生 02",
      en: "Interview 02",
      school: "慶應義塾大学 経済学部",
      year: "2025年度合格",
      tag: "数学受験 / 浪人",
      quote: "数学受験で経済学部を狙うと決めた瞬間から、戦略がガラリと変わった。1年で得点期待値が圧倒的に上がった。",
      story:
        "現役で英国社受験で全滅。「数学受験の方が合格可能性が高い」とコーチに分析された時は信じられなかった。微積と確率に絞った1年。気づけば、慶應経済A方式で合格していた。",
    },
    {
      id: "e5OzmZKSe28",
      name: "卒業生 03",
      en: "Interview 03",
      school: "上智大学 国際教養学部",
      year: "2024年度合格",
      tag: "TEAP活用 / 帰国子女",
      quote: "外部試験スコアの戦略を組み直してくれた。同じ学習量でも、出願戦略で結果が変わる。",
      story:
        "TOEFLでは点数が伸び悩んでいた。コーチが「TEAP一本に絞る」と決めてくれた瞬間、霧が晴れた。3ヶ月で必要スコアに到達。出願時点で勝負はほぼ決まっていた。",
    },
    {
      id: "HP_5tDBODaY",
      name: "卒業生 04",
      en: "Interview 04",
      school: "明治大学 政治経済学部",
      year: "2024年度合格",
      tag: "現役合格 / 部活両立",
      quote: "学習計画が「自分専用」だったから、部活と両立できた。週次のコーチングで、毎週ちゃんと前に進めた。",
      story:
        "サッカー部を引退したのは高3の6月。残された時間は限られていた。志望学部の傾向に絞った演習だけを徹底。無駄な時間がない計画だった。",
    },
    {
      id: "NwrlH_tyukA",
      name: "卒業生 05",
      en: "Interview 05",
      school: "立教大学 異文化コミュニケーション",
      year: "2025年度合格",
      tag: "英語特化 / 推薦も併願",
      quote: "推薦と一般、両方の戦略を最後まで諦めずに走らせてくれた。一人では絶対に無理だった。",
      story:
        "学校推薦と一般、両方狙うのは無謀と言われた。でもコーチは「両立できる時間配分」を緻密に組んでくれた。結果、第一志望に推薦合格できた。",
    },
    {
      id: "Rseh2QY53xQ",
      name: "卒業生 06",
      en: "Interview 06",
      school: "中央大学 法学部",
      year: "2024年度合格",
      tag: "国語論理 / 偏差値+18",
      quote: "国語の論理構造を初めてちゃんと理解できた。読み方が変わると、現代文の点数は本当に安定する。",
      story:
        "現代文は「センス」と諦めかけていた。でもコーチに「論理を追う技術」を教わってから、得点が安定した。最後の模試では偏差値が18上がっていた。",
    },
    {
      id: "6vRUDEt9aFc",
      name: "卒業生 07",
      en: "Interview 07",
      school: "青山学院大学 国際政治経済",
      year: "2025年度合格",
      tag: "学部別戦略 / 個別最適",
      quote: "学部別の戦略は、こんなに違うのかと衝撃を受けた。同じ大学でも、学部によって全く違う対策が必要だった。",
      story:
        "「同じ大学なら対策は同じ」と思っていた自分が恥ずかしい。学部別の出題傾向を分析してもらい、その学部の問題だけに最適化した。",
    },
    {
      id: "bcYQYTCSs8o",
      name: "卒業生 08",
      en: "Interview 08",
      school: "法政大学 法学部",
      year: "2024年度合格",
      tag: "添削の質 / 24h質問対応",
      quote: "添削の質が違う。返却が早く、改善点が明確。Slackでいつでも質問できる安心感が、最後まで支えてくれた。",
      story:
        "夜中に詰まった時も、翌朝にはコーチからの返信が届いていた。一人じゃない、という感覚が、最後の追い込み期に何より大きかった。",
    },
  ];

  const PLAYLIST_URL =
    "https://youtube.com/playlist?list=PLe1Lus8pQKOSWIKGd1VlF3q12vdsXAxm3";

  // Featured tabs
  const [activeIdx, setActiveIdx] = React.useState(0);
  const [playing, setPlaying] = React.useState(false);
  const active = interviews[activeIdx];

  // Reset playing when tab switches
  React.useEffect(() => {
    setPlaying(false);
  }, [activeIdx]);

  return (
    <>
      {/* Custom voice page hero — full-bleed diploma photo */}
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
            合格は、<em>結果</em>でしかない。<br />
            本当の物語は、<em>そこ</em>にある。
          </h1>
          <p className="voice-hero-lead">
            数字や偏差値の話ではなく、それぞれの「迷い」と「決断」を聞いてください。<br />
            私たちと走り抜けた卒業生の言葉が、ここにあります。
          </p>
          <div className="voice-hero-scroll">
            <span>Scroll</span>
            <span className="voice-hero-scroll-line" />
          </div>
        </div>
      </section>

      {/* Featured interview videos — 8 talks via tabs */}
      <section className="voice-featured">
        <div className="voice-featured-inner">
          <div className="voice-section-head">
            <span className="eyebrow"><i>Long-form Interview · 8 Talks</i></span>
            <h2 className="voice-section-title">
              対談動画で、<em>合格までの道のり</em>を。
            </h2>
            <p className="voice-section-lead">
              代表と卒業生の対談。<br />
              入塾前の悩みから、合格後の今までを、本音で。
            </p>
          </div>

          {/* Tabs — 8 interviews */}
          <div className="featured-tabs featured-tabs-8">
            {interviews.map((f, i) => (
              <button
                key={f.id}
                className={`featured-tab ${activeIdx === i ? "active" : ""}`}
                onClick={() => setActiveIdx(i)}
              >
                <span className="featured-tab-en"><i>No. {String(i + 1).padStart(2, "0")}</i></span>
                <span className="featured-tab-name">{f.name}</span>
                <span className="featured-tab-school">{f.school}</span>
              </button>
            ))}
          </div>

          {/* Featured player */}
          <div className="featured-stage">
            <div className="featured-video">
              <div className="featured-video-frame">
                {playing ? (
                  <iframe
                    key={active.id}
                    className="featured-iframe"
                    src={`https://www.youtube.com/embed/${active.id}?autoplay=1&rel=0&modestbranding=1`}
                    title={`${active.name} interview`}
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowFullScreen
                  />
                ) : (
                  <a
                    className="featured-video-thumb"
                    href={`https://youtu.be/${active.id}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={(e) => {
                      e.preventDefault();
                      setPlaying(true);
                    }}
                    style={{
                      backgroundImage: `url('https://i.ytimg.com/vi/${active.id}/hqdefault.jpg')`,
                    }}
                    aria-label={`${active.name}との対談を再生`}
                  >
                    <div className="featured-video-grain" />
                    <button className="featured-play" aria-label="動画を再生" tabIndex={-1}>
                      <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M8 5v14l11-7z" />
                      </svg>
                    </button>
                    <div className="featured-video-meta">
                      <span className="featured-duration"><i>No. {String(activeIdx + 1).padStart(2, "0")}</i></span>
                      <span className="featured-tag">{active.tag}</span>
                    </div>
                    <div className="featured-name-overlay">
                      <span className="featured-en"><i>{active.en}</i></span>
                      <span className="featured-name">{active.name}</span>
                    </div>
                  </a>
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
              <a
                href={`https://youtu.be/${active.id}`}
                target="_blank"
                rel="noopener noreferrer"
                className="featured-cta"
              >
                YouTubeで全編を見る
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M5 12h14M13 5l7 7-7 7" />
                </svg>
              </a>
            </aside>
          </div>

          {/* Playlist CTA */}
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
            <span className="voice-playlist-meta">YouTube · THINKING. 対談アーカイブ</span>
          </div>
        </div>
      </section>

      {/* Final */}
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
          <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta">
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
