/* Smart Study English — program & 45-day design */

const LEARNING_SYSTEMS = [
  {
    num: "01",
    title: "構造理解・文章講義",
    subtitle: "丸暗記ではなく、「核」で理解する。",
    image: "assets/program-feature-lecture.png",
    imageAlt: "文章講義の解析シート。英文の骨格と補足を色分けして可視化",
    frame: "sheet",
    points: [
      { icon: "clock", label: "1本10分前後で要点だけ" },
      { icon: "chat", label: "なぜその訳になるか説明できる" },
      { icon: "shield", label: "初見文でも崩れにくい土台" },
    ],
  },
  {
    num: "02",
    title: "動画解説講義",
    subtitle: "図解で、核から理解する。",
    image: "assets/program-feature-video.png",
    imageAlt: "動画講義の画面。講師が5文型の図解を解説している様子",
    frame: "video",
    points: [
      { icon: "bulb", label: "図解でわかる" },
      { icon: "list", label: "短く要点整理" },
      { icon: "replay", label: "何度でも見返せる" },
    ],
  },
  {
    num: "03",
    title: "電子教材",
    subtitle: "英語が読める生徒の脳内を可視化。",
    badge: "実況中継のように、読むプロセスを見える化",
    image: "assets/program-feature-ebook.png",
    imageAlt: "電子教材の画面。タブレットとスマホで英文の構造解析を表示",
    frame: "device",
    points: [
      { icon: "brain", label: "脳内プロセスを見える化" },
      { icon: "structure", label: "構造で理解できる" },
      { icon: "phone", label: "スマホでも確認できる" },
    ],
  },
];

function LearningPointIcon({ type }) {
  const common = { width: 18, height: 18, viewBox: "0 0 24 24", fill: "none", "aria-hidden": true };
  switch (type) {
    case "clock":
      return (
        <svg {...common}>
          <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth="1.8" />
          <path d="M12 8v4l3 2" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
        </svg>
      );
    case "chat":
      return (
        <svg {...common}>
          <path d="M6 8h12v8H10l-4 3V8z" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" />
        </svg>
      );
    case "shield":
      return (
        <svg {...common}>
          <path d="M12 4l7 3v5c0 4.2-3 6.8-7 8-4-1.2-7-3.8-7-8V7l7-3z" stroke="currentColor" strokeWidth="1.8" />
        </svg>
      );
    case "bulb":
      return (
        <svg {...common}>
          <path d="M9 18h6M10 21h4" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
          <path d="M12 3a6 6 0 0 1 3.5 10.8V16H8.5v-2.2A6 6 0 0 1 12 3z" stroke="currentColor" strokeWidth="1.8" />
        </svg>
      );
    case "list":
      return (
        <svg {...common}>
          <path d="M8 7h11M8 12h11M8 17h11" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
          <circle cx="5" cy="7" r="1" fill="currentColor" />
          <circle cx="5" cy="12" r="1" fill="currentColor" />
          <circle cx="5" cy="17" r="1" fill="currentColor" />
        </svg>
      );
    case "replay":
      return (
        <svg {...common}>
          <path d="M8 8H5v3" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
          <path d="M5 11a7 7 0 1 1 2 5" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
        </svg>
      );
    case "brain":
      return (
        <svg {...common}>
          <path d="M8 10a3 3 0 0 1 6 0 3 3 0 0 1 6 0c0 3-2 5-6 6-4-1-6-3-6-6z" stroke="currentColor" strokeWidth="1.8" />
        </svg>
      );
    case "structure":
      return (
        <svg {...common}>
          <rect x="5" y="5" width="6" height="6" rx="1" stroke="currentColor" strokeWidth="1.8" />
          <rect x="13" y="5" width="6" height="6" rx="1" stroke="currentColor" strokeWidth="1.8" />
          <rect x="9" y="13" width="6" height="6" rx="1" stroke="currentColor" strokeWidth="1.8" />
        </svg>
      );
    case "phone":
      return (
        <svg {...common}>
          <rect x="8" y="4" width="8" height="16" rx="2" stroke="currentColor" strokeWidth="1.8" />
          <circle cx="12" cy="17" r="0.8" fill="currentColor" />
        </svg>
      );
    default:
      return null;
  }
}

function LearningSystemCard({ item }) {
  return (
    <article className="learning-system-card">
      <div className="learning-system-head">
        <span className="learning-system-spark" aria-hidden="true" />
        <h4 className="learning-system-title">{item.title}</h4>
        <span className="learning-system-spark learning-system-spark--right" aria-hidden="true" />
      </div>
      <p className="learning-system-subtitle">
        <span className="learning-system-subline" aria-hidden="true" />
        {item.subtitle}
        <span className="learning-system-subline" aria-hidden="true" />
      </p>
      {item.badge ? <p className="learning-system-badge">{item.badge}</p> : null}
      <div className={`learning-system-visual learning-system-visual--${item.frame}`}>
        <img src={item.image} alt={item.imageAlt} loading="lazy" decoding="async" />
        {item.frame === "video" ? (
          <div className="learning-system-player" aria-hidden="true">
            <span className="learning-system-play" />
            <span className="learning-system-progress">
              <span />
            </span>
            <span className="learning-system-time">06:18 / 14:35</span>
          </div>
        ) : null}
      </div>
      <ul className="learning-system-points">
        {item.points.map((point) => (
          <li key={point.label}>
            <span className="learning-system-point-icon">
              <LearningPointIcon type={point.icon} />
            </span>
            <span>{point.label}</span>
          </li>
        ))}
      </ul>
    </article>
  );
}

/* =====================================================
   SECTION: SSE METHOD (3要素)
===================================================== */
function MethodSection() {
  return (
    <section id="program" className="method-section theme-paper" data-screen-label="05 Method">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">06</div>
          <div>
            <span className="eyebrow">SSE METHOD</span>
            <h2 className="section-title">45日間で、英語の読み方を<br /><em>根本から変える。</em></h2>
            <p className="section-lead">
              延べ2000名以上が結果を出した、英語の読み方トレーニングプログラム。<br />
              スポーツのフォーム矯正と同じ。まず「読み方のフォーム」を徹底的に矯正します。
            </p>
          </div>
        </div>

        <div className="method-overview">
          <p className="method-overview-label">Smart Study Englishの概要</p>
          <p className="method-overview-copy">
            学校の授業で使う英文も<br />
            模試で出題される初見の英文も<br />
            受験で出題される難しい英文も
          </p>
          <p className="method-overview-highlight">
            左から右へネイティブのように<br />
            スラスラ英文を読めるようになる
          </p>
          <p className="method-overview-project">英語の0→1プロジェクト</p>
          <p className="method-overview-voice">
            「自分でも、英語が読めた！」<br />
            英語嫌いから、英語を得点源に！
          </p>

          <div className="method-overview-pillars">
            <p>
              <span>1</span>「読む」に特化したカリキュラム
            </p>
            <p>
              <span>2</span>徹底的なサポート体制
            </p>
          </div>

          <p className="method-overview-guarantee">
            この2つであなたの英語の読み方を<br />
            基礎から徹底的に固めていくことを保証します！
          </p>

          <figure className="method-overview-figure method-overview-figure--solo">
            <img
              src="assets/program-support-system.png"
              alt="徹底的なサポート体制"
              loading="lazy"
              decoding="async"
            />
            <figcaption>徹底的なサポート体制</figcaption>
          </figure>
        </div>

        {/* Program contents */}
        <div className="method-contents">
          <div className="contents-head">
            <span className="eyebrow">PROGRAM CONTENTS</span>
            <h3 className="contents-title">矯正のための<em>3要素</em>と、自走を支える<em>サポート体制</em></h3>
          </div>

          <div className="learning-systems-showcase">
            {LEARNING_SYSTEMS.map((item) => (
              <LearningSystemCard key={item.num} item={item} />
            ))}
          </div>

          <div className="support-row">
            <span className="support-label">SUPPORT　自走を支える</span>
            <div className="support-items">
              <span>✓ 毎日提出システム</span>
              <span>✓ 個別LINE質問</span>
              <span>✓ 講義・動画 無期限閲覧</span>
            </div>
          </div>
        </div>

        {/* Daily routine */}
        <div className="daily-block">
          <div className="daily-head">
            <span className="eyebrow">DAILY ROUTINE</span>
            <h3 className="contents-title">迷わせず、<em>放置しない。</em>1日の流れ</h3>
          </div>

          <div className="daily-timeline">
            <div className="timeline-line"></div>

            <div className="timeline-step">
              <div className="step-time">05:00</div>
              <div className="step-card">
                <div className="step-card-icon">✉</div>
                <span className="step-card-tag">MORNING MISSION</span>
                <h4>朝5時のミッション送付</h4>
                <p>目が覚めた瞬間から、変革は始まる。<br />その日の課題とポイントを明確にお届け。</p>
              </div>
            </div>

            <div className="timeline-step">
              <div className="step-time">DAYTIME</div>
              <div className="step-card">
                <div className="step-card-icon">◷</div>
                <span className="step-card-tag">15-MIN INSTALL</span>
                <h4>隙間時間15分でインストール</h4>
                <p>視線の動かし方をコピー。<br />プロの「読み方」を脳に焼き付ける。</p>
              </div>
            </div>

            <div className="timeline-step">
              <div className="step-time">22:30</div>
              <div className="step-card">
                <div className="step-card-icon">◈</div>
                <span className="step-card-tag">SUBMIT &amp; FB</span>
                <h4>提出と個別フィードバック</h4>
                <p>提出ですべて可視化。<br />スタンプとして積み上がり、孤独な戦いにさせない。</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: 45 DAYS DESIGN — 積み上がる視覚化
===================================================== */
function DaysSection() {
  const ref = useRef(null);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const onScroll = () => {
      if (!ref.current) return;
      const rect = ref.current.getBoundingClientRect();
      const vh = window.innerHeight;
      const start = vh * 0.85;
      const end = vh * 0.15;
      const total = start - end;
      const passed = start - rect.top;
      const p = Math.max(0, Math.min(1, passed / total));
      setProgress(p);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const filledDays = Math.floor(progress * 45);

  return (
    <section id="days" className="days-section theme-deep-gold" data-screen-label="06 45 Days">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">10</div>
          <div>
            <span className="eyebrow">45 DAYS — DESIGN PHILOSOPHY</span>
            <h2 className="section-title">なぜ「45日」なのか。<br /><em>習慣化と定着の、ギリギリの設計。</em></h2>
            <p className="section-lead">
              短すぎれば癖に戻る。長すぎれば中だるみが起きる。<br />
              <strong>45日</strong>は、依存ではなく<strong>自走</strong>へ移行するための、最短かつ現実的な期間です。
            </p>
          </div>
        </div>

        {/* 45 day grid + progress */}
        <div className="days-grid-wrap" ref={ref}>
          <div className="days-grid-head">
            <span>DAY 01 → DAY 45　毎日の積み上げ</span>
            <span className="days-progress-text">完走率 <strong>{Math.round(progress * 100)}%</strong></span>
          </div>
          <div className="days-grid">
            {[...Array(45)].map((_, i) => {
              const filled = i < filledDays;
              const phase = i < 15 ? "phase-1" : i < 30 ? "phase-2" : "phase-3";
              return (
                <div key={i} className={`day-cell ${filled ? "filled" : ""} ${phase}`}>
                  <span className="day-num">{i + 1}</span>
                  {filled && <span className="day-check">✓</span>}
                </div>
              );
            })}
          </div>
          <div className="days-phases">
            <div className="phase-bar phase-1">
              <span className="phase-tag">Phase 1 / Day 1–15</span>
              <strong>理解 — 正しい型を論理的に</strong>
              <p>感覚読みを排除し、構造的に読むためのルールを脳にインプット。</p>
            </div>
            <div className="phase-bar phase-2">
              <span className="phase-tag">Phase 2 / Day 16–30</span>
              <strong>矯正 — 反復で無意識レベルへ</strong>
              <p>間違った読み方の癖を修正し、正しいフォームを定着させる。</p>
            </div>
            <div className="phase-bar phase-3">
              <span className="phase-tag">Phase 3 / Day 31–45</span>
              <strong>自走 — 一人で積み上げられる状態</strong>
              <p>指導者なしで自分で気づき・修正できる「自走」の完成形へ。</p>
            </div>
          </div>
        </div>

        {/* Stack visualization — 積み上がる */}
        <div className="stack-block">
          <div className="stack-head">
            <span className="eyebrow">COMPOUND VALUE</span>
            <h3 className="contents-title">SSEは「使い切り」ではない。<br /><em>受験終了まで、積み上がり続ける。</em></h3>
            <p className="section-lead" style={{ marginBottom: 32 }}>
              SSEの45日は、塾で高いお金を払って消費する「知識」ではない。<br />
              受験が終わるまで、<strong>毎日の学習に乗り続ける土台</strong>です。
            </p>
          </div>

          <div className="stack-vis">
            <div className="stack-bars">
              <div className="stack-bar bar-base">
                <div className="bar-content">
                  <span className="bar-label">SSE 45日 / 読み方の土台</span>
                  <span className="bar-sub">一度入れたら、抜けない</span>
                </div>
              </div>
              <div className="stack-bar bar-1">
                <div className="bar-content">
                  <span className="bar-label">単語の暗記</span>
                  <span className="bar-sub">→ 読み方の上に乗るから定着する</span>
                </div>
              </div>
              <div className="stack-bar bar-2">
                <div className="bar-content">
                  <span className="bar-label">文法の理解</span>
                  <span className="bar-sub">→ 構造把握で意味が腑に落ちる</span>
                </div>
              </div>
              <div className="stack-bar bar-3">
                <div className="bar-content">
                  <span className="bar-label">長文演習</span>
                  <span className="bar-sub">→ 速く正確に解ける</span>
                </div>
              </div>
              <div className="stack-bar bar-4">
                <div className="bar-content">
                  <span className="bar-label">過去問・模試</span>
                  <span className="bar-sub">→ 時間内に処理しきれる</span>
                </div>
              </div>
              <div className="stack-bar bar-top">
                <div className="bar-content">
                  <span className="bar-label">志望校 合格</span>
                </div>
              </div>
            </div>

            <div className="stack-side">
              <div className="stack-arrow">↑</div>
              <p className="stack-side-text">
                土台がある人の<br />
                <em>すべての学習</em>が、<br />
                ここに乗っていく。
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

window.MethodSection = MethodSection;
window.DaysSection = DaysSection;
