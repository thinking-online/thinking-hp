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

const SUPPORT_SYSTEMS = [
  {
    num: "01",
    title: "課題提出システム",
    titleEm: "システム",
    subtitle: "学んだ内容を、提出とフィードバックでしっかり定着。",
    layout: "split",
    image: "assets/program-support-assignment.png",
    imageAlt: "課題提出システム。ノートパソコンで学習する生徒",
    imageCrop: "left",
    features: [
      {
        icon: "clipboard",
        title: "提出で学習を習慣化",
        desc: "課題の提出を通じて、学習のリズムをつくります。",
      },
      {
        icon: "feedback",
        title: "個別フィードバックで理解を深める",
        desc: "一人ひとりに合わせたフィードバックで、つまずきを解消し、理解を深めます。",
      },
      {
        icon: "chart",
        title: "学習状況がひと目でわかる",
        desc: "提出状況やフィードバック履歴を一覧で確認できます。",
      },
    ],
    foot:
      "学んだ内容をしっかり定着させるために、課題を提出。個別のフィードバックで理解を深めます。",
  },
  {
    num: "02",
    title: "実践ワーク付き",
    subtitle: "講義で学んだことを、すぐにアウトプット。",
    layout: "centered",
    image: "assets/program-support-workbook.png",
    imageAlt: "実践ワーク。英文の穴埋めワークに取り組む様子",
    imageCrop: "workbook",
    points: [
      { icon: "clipboard", lines: ["学んだ", "直後に", "演習できる"] },
      { icon: "book", lines: ["解ける力", "を", "実践で身につける"] },
      { icon: "target", lines: ["理解", "から", "定着までをつなぐ"] },
    ],
    foot: "講義で学んだことをすぐにアウトプット。実践的なワークで、解ける力を身につけます。",
  },
  {
    num: "03",
    title: "モチベUPメッセージ",
    subtitle: "やる気を支え、継続を後押しする。",
    layout: "split-bubble",
    image: "assets/program-support-motivation.png",
    imageAlt: "モチベUPメッセージ。スマホを見て笑顔の生徒",
    imageCrop: "left",
    bubble: [
      "よく頑張っていますね！",
      "昨日より今日、また一歩前進しています！",
      "その調子で、目標に向かって進んでいきましょう！ ✨",
    ],
    features: [
      {
        icon: "mail",
        title: "定期的に応援メッセージが届く",
        desc: "学習の進捗や取り組みに合わせて、温かいメッセージをお届けします。",
      },
      {
        icon: "heart",
        title: "努力を見てもらえるから続けやすい",
        desc: "頑張りをしっかり認めてもらえるから、自信につながり、継続の力になります。",
      },
      {
        icon: "trend",
        title: "学習習慣を前向きにキープ",
        desc: "やる気を引き出すメッセージで、前向きな気持ちを維持できます。",
      },
    ],
    foot: (
      <>
        学習の進捗や努力を応援するメッセージを定期的にお届け。
        <strong>やる気をキープし、継続をサポートします。</strong>
      </>
    ),
  },
  {
    num: "04",
    titleLead: "24",
    titleMid: "hチャット",
    titleEm: "システム",
    subtitle: "疑問をすぐに解消できる、安心の質問環境。",
    layout: "split",
    image: "assets/program-support-chat.png",
    imageAlt: "24時間チャットサポート。スマホで質問する様子",
    imageCrop: "left",
    features: [
      {
        icon: "headset",
        title: "いつでも質問できる",
        desc: "24時間いつでも質問OK。時間を気にせず相談できます。",
      },
      {
        icon: "question",
        title: "わからないをすぐ解消",
        desc: "経験豊富なスタッフが丁寧に回答。疑問をその場でスッキリ解決します。",
      },
      {
        icon: "bookcheck",
        title: "学習が止まらない",
        desc: "疑問をすぐに解消できるから、つまずかずに学習を続けられます。",
      },
    ],
    foot: (
      <>
        いつでも質問できるチャットシステムを完備。疑問をすぐに解消できるので、
        <strong>学習が止まりません。</strong>
      </>
    ),
  },
];

function SupportFeatureIcon({ type }) {
  const common = { width: 22, height: 22, viewBox: "0 0 24 24", fill: "none", "aria-hidden": true };
  switch (type) {
    case "clipboard":
      return (
        <svg {...common}>
          <rect x="6" y="5" width="12" height="14" rx="2" stroke="currentColor" strokeWidth="1.7" />
          <path d="M9 5V4a3 3 0 0 1 6 0v1" stroke="currentColor" strokeWidth="1.7" />
          <path d="M9 11h6M9 14h4" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
      );
    case "feedback":
      return (
        <svg {...common}>
          <path d="M6 7h12v9H11l-5 3V7z" stroke="currentColor" strokeWidth="1.7" strokeLinejoin="round" />
          <circle cx="9" cy="11" r="0.8" fill="currentColor" />
          <circle cx="12" cy="11" r="0.8" fill="currentColor" />
          <circle cx="15" cy="11" r="0.8" fill="currentColor" />
        </svg>
      );
    case "chart":
      return (
        <svg {...common}>
          <path d="M6 18V10M11 18V6M16 18v-5M20 18H4" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
      );
    case "book":
      return (
        <svg {...common}>
          <path d="M6 6h5v12H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z" stroke="currentColor" strokeWidth="1.7" />
          <path d="M13 6h5a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-5V6z" stroke="currentColor" strokeWidth="1.7" />
        </svg>
      );
    case "target":
      return (
        <svg {...common}>
          <circle cx="12" cy="12" r="7" stroke="currentColor" strokeWidth="1.7" />
          <circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="1.7" />
          <path d="M12 5V3M19 12h2M12 19v2M3 12H1" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
      );
    case "mail":
      return (
        <svg {...common}>
          <rect x="4" y="6" width="16" height="12" rx="2" stroke="currentColor" strokeWidth="1.7" />
          <path d="M4 8l8 5 8-5" stroke="currentColor" strokeWidth="1.7" />
        </svg>
      );
    case "heart":
      return (
        <svg {...common}>
          <circle cx="8" cy="9" r="2.5" stroke="currentColor" strokeWidth="1.7" />
          <path d="M4 18c2-4 4-6 8-6s6 2 8 6" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
      );
    case "trend":
      return (
        <svg {...common}>
          <path d="M5 18V8M10 18V12M15 18V6M20 18H4" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
          <path d="M14 8l3-2 3 3" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "headset":
      return (
        <svg {...common}>
          <path d="M5 12a7 7 0 0 1 14 0v4a3 3 0 0 1-3 3h-1v-5" stroke="currentColor" strokeWidth="1.7" />
          <path d="M19 16a3 3 0 0 1-3 3h-1" stroke="currentColor" strokeWidth="1.7" />
        </svg>
      );
    case "question":
      return (
        <svg {...common}>
          <circle cx="12" cy="12" r="8" stroke="currentColor" strokeWidth="1.7" />
          <path d="M10 9a2 2 0 1 1 3.2 1.6c-.8.5-1.2 1.1-1.2 2.4" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
          <circle cx="12" cy="17" r="0.8" fill="currentColor" />
        </svg>
      );
    case "bookcheck":
      return (
        <svg {...common}>
          <path d="M6 6h6v12H7a2 2 0 0 1-2-2V6z" stroke="currentColor" strokeWidth="1.7" />
          <path d="M12 6h6a2 2 0 0 1 2 2v7l-3 2-3-2V6z" stroke="currentColor" strokeWidth="1.7" />
          <path d="M15 12l1.5 1.5L19 11" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
      );
    default:
      return null;
  }
}

function SupportFeatureTitle({ item }) {
  if (item.titleLead) {
    return (
      <>
        <span className="support-feature-title-mark">{item.titleLead}</span>
        {item.titleMid}
        {item.titleEm ? <span className="support-feature-title-em">{item.titleEm}</span> : null}
      </>
    );
  }

  if (item.titleEm) {
    const base = item.title.slice(0, item.title.indexOf(item.titleEm));
    return (
      <>
        {base}
        <span className="support-feature-title-em">{item.titleEm}</span>
      </>
    );
  }

  return item.title;
}

function SupportFeatureCard({ item }) {

  if (item.layout === "centered") {
    return (
      <article className={`support-feature-card support-feature-card--${item.layout}`}>
        <span className="support-feature-num">{item.num}</span>
        <h4 className="support-feature-title">
          <SupportFeatureTitle item={item} />
        </h4>
        <p className="support-feature-subtitle">
          <span className="support-feature-subspark" aria-hidden="true" />
          {item.subtitle}
          <span className="support-feature-subspark support-feature-subspark--right" aria-hidden="true" />
        </p>
        <div
          className={`support-feature-visual support-feature-visual--wide${
            item.imageCrop ? ` support-feature-visual--${item.imageCrop}` : ""
          }`}
        >
          <img src={item.image} alt={item.imageAlt} loading="lazy" decoding="async" />
        </div>
        <ul className="support-feature-pillars">
          {item.points.map((point) => (
            <li key={point.lines.join("")}>
              <span className="support-feature-pillar-icon">
                <SupportFeatureIcon type={point.icon} />
              </span>
              <p>
                <strong>{point.lines[0]}</strong>
                {point.lines[1]}
                <strong>{point.lines[2]}</strong>
              </p>
            </li>
          ))}
        </ul>
        <p className="support-feature-foot">{item.foot}</p>
      </article>
    );
  }

  return (
    <article className={`support-feature-card support-feature-card--${item.layout}`}>
      <span className="support-feature-num">{item.num}</span>
      <h4 className="support-feature-title">
        <SupportFeatureTitle item={item} />
      </h4>
      <p className="support-feature-subtitle">{item.subtitle}</p>
      <div className="support-feature-body">
        <div
          className={`support-feature-visual${
            item.imageCrop ? ` support-feature-visual--${item.imageCrop}` : ""
          }`}
        >
          <img src={item.image} alt={item.imageAlt} loading="lazy" decoding="async" />
          {item.bubble ? (
            <div className="support-feature-bubble" aria-hidden="true">
              <span className="support-feature-bubble-icon">✉</span>
              {item.bubble.map((line) => (
                <p key={line}>{line}</p>
              ))}
            </div>
          ) : null}
        </div>
        <ul className="support-feature-list">
          {item.features.map((feature) => (
            <li key={feature.title}>
              <span className="support-feature-list-icon">
                <SupportFeatureIcon type={feature.icon} />
              </span>
              <div>
                <strong>{feature.title}</strong>
                <p>{feature.desc}</p>
              </div>
            </li>
          ))}
        </ul>
      </div>
      <p className="support-feature-foot">{item.foot}</p>
    </article>
  );
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

          <div className="method-support">
            <div className="contents-head method-support-head">
              <span className="eyebrow">THOROUGH SUPPORT</span>
              <h3 className="contents-title">
                自走を支える、<em>徹底的なサポート体制</em>
              </h3>
              <p className="method-support-lead">
                学習が止まらない・続く・定着する。4つの仕組みで、45日間を一人にしません。
              </p>
            </div>

            <div className="support-systems-showcase">
              {SUPPORT_SYSTEMS.map((item) => (
                <SupportFeatureCard key={item.num} item={item} />
              ))}
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
