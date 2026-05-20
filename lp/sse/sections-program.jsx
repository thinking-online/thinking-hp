/* Smart Study English — program & 45-day design */

const LEARNING_SYSTEMS = [
  {
    num: "01",
    title: "文章講義",
    subtitle: "脱・丸暗記で、文法のコアをつかむ。",
    frame: "showcase",
    showcaseVariant: "lecture",
    image: "assets/learning-lecture-bunsho-detail.png",
    imageAlt:
      "文章講義の詳細。視覚で理解するオリジナル講義と、使役動詞・不定詞などの図解サンプル、3つの学習メリット",
    imageWidth: 1024,
    imageHeight: 768,
    features: [
      {
        icon: "bulb",
        title: "丸暗記しないで文法のコアを掴む！",
        desc: "イメージで理解するから、忘れない！本質をつかんで応用力が身につきます。",
      },
      {
        icon: "book",
        title: "前置詞も英文法も脱丸暗記！",
        desc: "イメージでつながる学習法で、苦手な文法もスッと理解できます。",
      },
      {
        icon: "palette",
        title: "オリジナルイラストで英語がどんどん好きに！",
        desc: "思わずクスッとするイラストで楽しく学べる！理解が深まり、学ぶことがもっと楽しくなります。",
      },
    ],
  },
  {
    num: "02",
    title: "動画解説講義",
    subtitle: "脱丸暗記で、核から理解する。",
    frame: "showcase",
    showcaseVariant: "video",
    image: "assets/learning-video-lecture-detail.png",
    imageAlt:
      "動画解説講義の詳細。図解ベースの講義画面と、脱丸暗記・10分以内・要点復習・何度でも見返せるの4つの特徴",
    imageWidth: 1024,
    imageHeight: 768,
    features: [
      { icon: "bulb", title: "脱丸暗記", desc: "丸暗記ではなく、核から理解" },
      { icon: "clock", title: "1本10分以内", desc: "短いからスキマ時間で見やすい" },
      { icon: "list", title: "要点だけ確認", desc: "必要なポイントをサッと復習" },
      { icon: "replay", title: "何度でも見返せる", desc: "わからない所を自分のペースで反復" },
    ],
  },
  {
    num: "03",
    title: "電子教材",
    subtitle: "英語が読める生徒の脳内を可視化。",
    frame: "showcase",
    showcaseVariant: "ebook",
    image: "assets/learning-ebook-brain-steps.png",
    imageAlt:
      "電子教材の詳細。英語を読む6つのステップ（骨格・補足・意味・構造・背景・要点）と脳内イメージ図",
    imageWidth: 1024,
    imageHeight: 682,
    showcaseFoot:
      "英語を「なんとなく」読むのではなく、正しい順番で、正しく処理する。この6つのステップを身につけることで、英文は驚くほどスラスラ読めるようになります。",
    steps: [
      { num: "01", title: "骨格をつかむ", desc: "S・V・O・Mなど、骨格を瞬時につかむ" },
      { num: "02", title: "補足をつかむ", desc: "修飾・補足情報を理解し、意味をつなげる" },
      { num: "03", title: "意味を理解する", desc: "直訳ではなく、文全体の意味をつかむ" },
      { num: "04", title: "構造を整理する", desc: "情報を整理し、論理的な構造をつくる" },
      { num: "05", title: "背景をイメージする", desc: "場面や状況をイメージして理解を深める" },
      { num: "06", title: "要点をつかむ", desc: "筆者が伝えたいこと・結論をつかむ" },
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
    case "book":
      return (
        <svg {...common}>
          <path d="M6 6h6a2 2 0 0 1 2 2v12H8a2 2 0 0 0-2 2V6z" stroke="currentColor" strokeWidth="1.8" />
          <path d="M8 6h8a2 2 0 0 1 2 2v12" stroke="currentColor" strokeWidth="1.8" />
        </svg>
      );
    case "palette":
      return (
        <svg {...common}>
          <path
            d="M12 4c-4 0-7 2.5-7 6.5 0 2.2 1.2 4 3 4.8.6.3 1 .9 1 1.6v.1c0 .8.7 1.5 1.5 1.5H11c1.4 0 2.5-1.1 2.5-2.5 0-.5.2-1 .5-1.3.3-.4.5-.9.5-1.4C17 6.5 14.5 4 12 4z"
            stroke="currentColor"
            strokeWidth="1.8"
          />
          <circle cx="9" cy="9" r="0.9" fill="currentColor" />
          <circle cx="14" cy="8" r="0.9" fill="currentColor" />
          <circle cx="15" cy="12" r="0.9" fill="currentColor" />
        </svg>
      );
    default:
      return null;
  }
}

const SUPPORT_WORRY_FLOWS = [
  {
    num: "01",
    worry: "継続できるかな…",
    worryImage: "assets/support-worry-01-continue.png",
    worryAlt: "継続できるか不安な生徒。カレンダーを見て悩んでいるイラスト",
    solutionTitle: "提出課題システム",
    solutionCopy: (
      <>
        課題が決まった時間に届き、期限までに提出する必要があります。サボり癖があっても、
        <mark className="support-worry-mark">半強制的にもやらざるを得ない状況</mark>
        が生まれます。1日も続かなかった生徒が、
        <mark className="support-worry-mark">1ヶ月以上続けられた</mark>
        システムです。
      </>
    ),
    image: "assets/support-solution-01-assignment.png",
    imageAlt: "提出課題のワークシート。Day9の英文を色分け・手書きメモで解析している様子",
  },
  {
    num: "02",
    worry: "ちゃんと理解できるかな…",
    worryImage: "assets/support-worry-02-understand.png",
    worryAlt: "理解できるか不安な生徒。複雑な構造に悩むイラスト",
    solutionTitle: "実践ワーク付き",
    solutionCopy: (
      <>
        講義で学んだ「核」を、その日のうちにワークで確認。頭の中がごちゃごちゃでも、
        <mark className="support-worry-mark">手を動かすうちに構造が整理</mark>
        され、
        <mark className="support-worry-mark">ちゃんと理解できた</mark>
        実感につながります。
      </>
    ),
    image: "assets/support-solution-02-workbook.png",
    imageAlt: "タブレットの教材とノートに書き込む実践ワークの学習風景",
  },
  {
    num: "03",
    worry: "わからない問題はどうすれば？",
    worryImage: "assets/support-worry-03-stuck.png",
    worryAlt: "わからない問題に困っている生徒のイラスト",
    solutionTitle: "24hチャットシステム",
    solutionCopy: (
      <>
        一人で抱え込まなくてOK。いつでも質問でき、
        <mark className="support-worry-mark">わからないをその場で解消</mark>
        。つまずいて止まる前に、
        <mark className="support-worry-mark">次の問題へ進める</mark>
        環境です（目安：24時間以内に返信）。
      </>
    ),
    image: "assets/support-solution-03-chat.png",
    imageAlt: "24時間チャットで質問と回答のやり取り。スマホを見て安心する生徒",
  },
  {
    num: "04",
    worry: "モチベが続かない、やる気の持続が心配…",
    worryImage: "assets/support-worry-04-motivation.png",
    worryAlt: "やる気が続かないと不安な生徒。バッテリーが切れたように疲れたイラスト",
    solutionTitle: "モチベUPメッセージ",
    solutionCopy: (
      <>
        学習の進捗や努力を見て、温かい応援メッセージが届きます。一人で抱え込まず、
        <mark className="support-worry-mark">やる気をキープ</mark>
        しながら、
        <mark className="support-worry-mark">45日間走り切れる</mark>
        リズムをつくります。
      </>
    ),
    image: "assets/support-solution-04-motivation.png",
    imageAlt: "スマホの応援メッセージを見てやる気になった制服の女子生徒",
  },
];

function SupportWorryFlow({ item }) {
  const ref = React.useRef(null);
  const [visible, setVisible] = React.useState(false);

  React.useEffect(() => {
    const el = ref.current;
    if (!el) return undefined;

    const reduced =
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (reduced) {
      setVisible(true);
      return undefined;
    }

    const narrow = window.matchMedia("(max-width: 900px)").matches;
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        setVisible(true);
        obs.disconnect();
      },
      {
        threshold: narrow ? [0, 0.12] : [0, 0.2],
        rootMargin: narrow ? "30px 0px 50px 0px" : "20px 0px 40px 0px",
      }
    );

    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <article
      ref={ref}
      className={`support-worry-flow${item.num === "03" ? " support-worry-flow--chat" : ""}${visible ? " is-visible" : ""}`}
      aria-labelledby={`support-worry-${item.num}`}
    >
      <div className="support-worry-card">
        <span className="support-worry-num">悩み{item.num}</span>
        <p id={`support-worry-${item.num}`} className="support-worry-text">
          {item.worry}
        </p>
        <figure className="support-worry-figure">
          <img
            src={item.worryImage}
            alt={item.worryAlt}
            loading="lazy"
            decoding="async"
          />
        </figure>
      </div>

      <div className="support-worry-arrow" aria-hidden="true">
        <span className="support-worry-arrow-icon">↓</span>
      </div>

      <div className="support-worry-solution">
        <h4 className="support-worry-solution-title">{item.solutionTitle}</h4>
        <p className="support-worry-solution-copy">{item.solutionCopy}</p>
        <div className="support-worry-solution-visual">
          <img src={item.image} alt={item.imageAlt} loading="lazy" decoding="async" />
        </div>
      </div>
    </article>
  );
}

function LearningSystemCard({ item }) {
  let visual = null;

  if (item.frame === "thumbs") {
    visual = (
      <div className="learning-system-thumbs" role="list" aria-label="文章講義のサムネイル">
        {item.thumbnails.map((thumb) => (
          <figure key={thumb.src} className="learning-system-thumb" role="listitem">
            <img src={thumb.src} alt={thumb.alt} loading="lazy" decoding="async" />
          </figure>
        ))}
      </div>
    );
  } else if (item.frame === "showcase") {
    visual = (
      <div className={`learning-system-showcase learning-system-showcase--${item.showcaseVariant}`}>
        <figure className="learning-system-showcase-figure">
          <img
            src={item.image}
            alt={item.imageAlt}
            width={item.imageWidth}
            height={item.imageHeight}
            loading="lazy"
            decoding="async"
          />
        </figure>

        {item.features ? (
          <ul className="learning-system-features" aria-label={`${item.title}の特徴`}>
            {item.features.map((feature) => (
              <li key={feature.title}>
                <span className="learning-system-feature-icon">
                  <LearningPointIcon type={feature.icon} />
                </span>
                <span className="learning-system-feature-copy">
                  <strong>{feature.title}</strong>
                  <span>{feature.desc}</span>
                </span>
              </li>
            ))}
          </ul>
        ) : null}

        {item.steps ? (
          <ol className="learning-system-steps" aria-label="英語を読む6つのステップ">
            {item.steps.map((step) => (
              <li key={step.num}>
                <span className="learning-system-step-num">{step.num}</span>
                <span className="learning-system-step-copy">
                  <strong>{step.title}</strong>
                  <span>{step.desc}</span>
                </span>
              </li>
            ))}
          </ol>
        ) : null}

        {item.showcaseFoot ? (
          <p className="learning-system-showcase-foot">{item.showcaseFoot}</p>
        ) : null}
      </div>
    );
  } else {
    visual = (
      <div className={`learning-system-visual learning-system-visual--${item.frame}`}>
        <img src={item.image} alt={item.imageAlt} loading="lazy" decoding="async" />
      </div>
    );
  }

  const isShowcase = item.frame === "showcase";

  return (
    <article
      className={`learning-system-card${isShowcase ? ` learning-system-card--showcase learning-system-card--showcase-${item.showcaseVariant}` : ""}`}
    >
      {isShowcase ? (
        <h4 className="learning-system-sr-only">{item.title}</h4>
      ) : (
        <>
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
        </>
      )}
      {visual}
      {item.points ? (
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
      ) : null}
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
            <div className="method-support-intro">
              <span className="eyebrow">THOROUGH SUPPORT</span>
              <h3 className="method-support-catch">
                <span className="method-support-catch-line">3日坊主でもやり切れる！</span>
                <span className="method-support-catch-line method-support-catch-line--em">
                  徹底的なサポート体制
                </span>
              </h3>
              <p className="method-support-resolve">
                あなたのその悩みや心配
                <br />
                <em>全部、解決します！</em>
              </p>
            </div>

            <div className="support-worry-flows">
              {SUPPORT_WORRY_FLOWS.map((item) => (
                <SupportWorryFlow key={item.num} item={item} />
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
