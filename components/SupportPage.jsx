// Support page — THINKING Method (三層) 完成版構成
// 固有名: 合格設計図(Master Plan) / ステージ式ロードマップ(STEP Roadmap) / THINKING Method

const ASSETS = {
  heroCoaching: "assets/support-hero-coaching.jpg?v=20260515-hero-mobile-v3",
  heroCoachingDesktop: "assets/support-hero-coaching-desktop.jpg?v=20260515-hero-pc",
  thinkingMethod: "assets/support-thinking-method.png?v=20260515-method",
  masterPlan: "assets/support-master-plan.png",
  workbook: "assets/products-series-4parts-overview.png",
  stepRoadmap: "assets/support-step-roadmap.png",
  sheetDaily: "assets/support-sheet-daily.png",
  sheetWeeklyPeriod: "assets/support-sheet-weekly-period.png",
  sheetSummary: "assets/support-sheet-weekly-summary.png",
  weekendTest: "assets/support-weekend-test.png",
};

const MANABO_VIDEO_URL = "https://utage-system.com/video/bxIu94uAdf1y";

const SupportPage = () => (
  <>
    <SupportHero />
    <SupportStickyNav />
    <SupportMethodIntro />
    <SupportLayerDesign />
    <SupportLayerExecute />
    <SupportLayerTrain />
    <SupportWeekFlow />
    <SupportFaq />
    <SupportFinalCta />
  </>
);

/* ─── Hero ───────────────────────────────────────────────── */

const SupportHero = () => (
  <section className="sup-hero" aria-labelledby="sup-hero-title">
    <div className="sup-hero-firstview">
      <div className="sup-hero-media">
        <picture>
          <source media="(min-width: 901px)" srcSet={ASSETS.heroCoachingDesktop} />
          <img
            className="sup-hero-photo"
            src={ASSETS.heroCoaching}
            width={576}
            height={1024}
            alt="夜の自宅でオンライン指導を受けながら学習する受講生"
            loading="eager"
            decoding="async"
          />
        </picture>
      </div>
      <div className="sup-hero-overlay sup-hero-overlay-left" aria-hidden="true" />
      <div className="sup-hero-overlay sup-hero-overlay-top" aria-hidden="true" />
      <div className="sup-hero-overlay sup-hero-overlay-bottom" aria-hidden="true" />
      <div className="sup-hero-grain" aria-hidden="true" />

      <div className="sup-hero-content">
        <p className="sup-hero-kicker">サポート体制</p>

        <h1 id="sup-hero-title" className="sup-hero-headline">
          <span className="sup-hero-headline-l1">根性論はなし。</span>
          <span className="sup-hero-headline-l2">「再現性」のあるサポート</span>
        </h1>

        <div className="sup-hero-bottom">
          <p className="sup-hero-lead">
            <span className="sup-hero-lead-pillars">
              「<em className="sup-hero-lead-em">設計する。実行する。鍛える。</em>」
            </span>
            <span className="sup-hero-lead-body">
              THINKING の<span className="sup-hero-accent">三層</span>
              が、合格までの全体行程を一枚の合格設計図イメージにし、日々の実行と思考力まで、同じロジックで整え続ける。
            </span>
          </p>
          <div className="sup-hero-ctas">
          <a
            href={window.THINKING_LINE_LIFF_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="cta"
          >
            <span>LINEで無料相談</span>
            <svg className="arrow" viewBox="0 0 16 16" fill="none" aria-hidden="true">
              <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
            </svg>
          </a>
          <a href="#thinking-method" className="cta-ghost">
            <span>THINKING Method を見る</span>
            <span className="dot" aria-hidden="true">
              ↓
            </span>
          </a>
          </div>
        </div>
      </div>
    </div>
  </section>
);

/* ─── ページ内ナビ（固定ヘッダー直下にスティック） ───────────── */

const SupportStickyNav = () => {
  const links = [
    { href: "#thinking-method", label: "Method" },
    { href: "#layer-design", label: "設計" },
    { href: "#layer-execute", label: "実行" },
    { href: "#layer-train", label: "鍛錬" },
    { href: "#week-flow", label: "週の流れ" },
    { href: "#faq", label: "FAQ" },
    { href: "#contact", label: "面談" },
  ];
  return (
    <nav className="sup-toc" aria-label="ページ内のセクションへジャンプ">
      <div className="sup-section-inner sup-toc-inner">
        {links.map((l) => (
          <a key={l.href} href={l.href} className="sup-toc-link">
            {l.label}
          </a>
        ))}
      </div>
    </nav>
  );
};

/* ─── THINKING Method 概念図 ───────────────────────────────── */

const SupportMethodIntro = () => (
  <section className="sup-method" id="thinking-method" aria-labelledby="sup-method-title">
    <div className="sup-section-inner sup-method-inner">
      <header className="sup-method-head">
        <h2 id="sup-method-title" className="sup-h2">
          THINKING Method <span className="sup-h2-sub">── 合格までの三層構造</span>
        </h2>
        <p className="sup-lead">
          多くの塾は「実行」しか提供しない。
          <br />
          THINKING は、合格までを <em>設計 → 実行 → 鍛錬</em> の三層で組み立てる。
          <br />
          ひとつでも欠ければ、合格は遠ざかる。
        </p>
      </header>

      <figure className="sup-method-figure">
        <img
          src={ASSETS.thinkingMethod}
          alt="THINKING Method 三層サポートシステム：設計する・実行する・鍛えるのピラミッドと各層の説明"
          width={1024}
          height={682}
          loading="eager"
          decoding="async"
          className="sup-method-img"
        />
      </figure>
    </div>
  </section>
);

/* ─── LAYER 01 設計 ───────────────────────────────────────── */

const SupportLayerDesign = () => (
  <section className="sup-layer sup-layer--design" id="layer-design" aria-labelledby="sup-layer-design-title">
    <div className="sup-layer-band">
      <div className="sup-section-inner sup-layer-band-inner">
        <p className="sup-layer-kicker">LAYER 01 ── 設計する</p>
        <p className="sup-layer-en" lang="en">
          DESIGN
        </p>
        <h2 id="sup-layer-design-title" className="sup-layer-title">
          「いつまでに、何を、どのくらい」
        </h2>
        <p className="sup-layer-lead">
          それが決まっていない努力は、合格に向かわない。
          <br />
          THINKING は入塾後、最初に合格までの全行程を1枚の地図にする。
          <br />
          迷う時間を、ゼロにする。
        </p>
      </div>
    </div>

    <div className="sup-section-inner">
      <article className="sup-block" id="master-plan" aria-labelledby="sup-master-plan-h">
        <h3 id="sup-master-plan-h" className="sup-h3">
          合格設計図<span className="sup-h3-paren">（Master Plan）</span>
        </h3>
        <p className="sup-tagline">入試本番から逆算した、あなただけの全行程図。</p>
        <p className="sup-body">
          入試本番日から逆算し、科目ごとに「いつ・何を・どれだけ」やるかを1枚の地図に描く。
          英単語・英文法・解釈・長文・古文単語・漢文・日本史 ── すべての科目、すべての教材、すべてのマイルストーン。
          受験までのすべてが、1枚で見える。
        </p>
        <ul className="sup-features sup-features--3">
          <li>
            <span className="sup-feat-no">01</span>
            <strong>入試本番から逆算</strong>
            <span>ゴール日（入試本番）を起点に、すべての教材の開始日・完了日が自動で決まる。</span>
          </li>
          <li>
            <span className="sup-feat-no">02</span>
            <strong>科目をまたいで俯瞰</strong>
            <span>英語・国語・日本史 ── 全科目の進捗が1枚で見える。バランスが崩れない。</span>
          </li>
          <li>
            <span className="sup-feat-no">03</span>
            <strong>志望校変更にも対応</strong>
            <span>コース切替によって設計図ごと組み替え可能。戦略の柔軟性を担保する。</span>
          </li>
        </ul>
        <SupportMasterPlanMedia />
      </article>

      <article className="sup-block sup-block--tight" id="faculty-strategy" aria-labelledby="sup-faculty-h">
        <h3 id="sup-faculty-h" className="sup-h3">
          学部別戦略
        </h3>
        <p className="sup-tagline">私立文系専門だからこそ、ここまで深く分析できる。</p>
        <p className="sup-body">
          THINKING は私立文系の各大学・各学部の過去問を徹底的に分析している。
          出題傾向、頻出テーマ、時間配分、頻出語彙 ── すべてを学部単位で言語化し、教材に落とし込む。
          <br />
          その分析を元に、オリジナル教材を内製している。
        </p>
        <ul className="sup-material-grid">
          <li>
            <span className="sup-mat-no">01</span>
            <strong>構造・出題データ分析</strong>
            <span>過去問を徹底分析し、出題傾向と時間配分を可視化。</span>
          </li>
          <li>
            <span className="sup-mat-no">02</span>
            <strong>頻出英単語熟語帳</strong>
            <span>入試で差がつく頻出語彙を厳選。意味・同義語・例文まで網羅。</span>
          </li>
          <li>
            <span className="sup-mat-no">03</span>
            <strong>オリジナル大問別擬似演習教材</strong>
            <span>入試本番を想定したオリジナル問題で、実戦力を鍛える。</span>
          </li>
          <li>
            <span className="sup-mat-no">04</span>
            <strong>総合模試</strong>
            <span>本番さながらの総合模試で、実力を最終チェック。</span>
          </li>
        </ul>
        <figure className="sup-figure sup-figure--book">
          <img
            src={ASSETS.workbook}
            alt="学部別に内製したTHINKINGオリジナル教材の4部構成：構造分析・頻出語彙・大問別演習・総合模試"
            width={1200}
            height={800}
            loading="lazy"
            decoding="async"
            className="sup-figure-img"
          />
          <figcaption className="sup-cap">学部別に内製している、THINKING オリジナル教材</figcaption>
        </figure>
      </article>
    </div>
  </section>
);

const SupportMasterPlanMedia = () => {
  const [open, setOpen] = React.useState(false);

  React.useEffect(() => {
    if (!open) return undefined;
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const onKey = (e) => {
      if (e.key === "Escape") setOpen(false);
    };
    window.addEventListener("keydown", onKey);
    return () => {
      document.body.style.overflow = prev;
      window.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <figure className="sup-figure sup-figure--scroll">
      <div className="sup-scroll-hint">横スクロールで全体を表示 · 画像をタップで拡大</div>
      <div className="sup-scroll-x">
        <button
          type="button"
          className="sup-master-plan-btn"
          onClick={() => setOpen(true)}
          aria-haspopup="dialog"
          aria-expanded={open}
        >
          <img
            src={ASSETS.masterPlan}
            alt="学習ナビゲーションマップ（合格設計図イメージ）のサンプル。科目別の工程・教材・週次ペースが時系列で一覧されている"
            loading="lazy"
            decoding="async"
            className="sup-master-plan-img"
          />
        </button>
      </div>
      <figcaption className="sup-cap">合格設計図イメージ（英語・現代文・古文・漢文・日本史）</figcaption>
      {open && (
        <div
          className="sup-lightbox"
          role="dialog"
          aria-modal="true"
          aria-label="合格設計図イメージの拡大表示"
        >
          <button type="button" className="sup-lightbox-close" onClick={() => setOpen(false)}>
            閉じる
          </button>
          <button type="button" className="sup-lightbox-backdrop" onClick={() => setOpen(false)} aria-label="閉じる" />
          <div className="sup-lightbox-body">
            <img src={ASSETS.masterPlan} alt="" />
          </div>
        </div>
      )}
    </figure>
  );
};

/* ─── LAYER 02 実行 ───────────────────────────────────────── */

const SupportLayerExecute = () => (
  <section className="sup-layer sup-layer--execute" id="layer-execute" aria-labelledby="sup-layer-exec-title">
    <div className="sup-layer-band sup-layer-band--gold">
      <div className="sup-section-inner sup-layer-band-inner">
        <p className="sup-layer-kicker">LAYER 02 ── 実行する</p>
        <p className="sup-layer-en" lang="en">
          EXECUTE
        </p>
        <h2 id="sup-layer-exec-title" className="sup-layer-title">
          設計図を、「今日のチェックリスト」まで落とし込む。
        </h2>
        <p className="sup-layer-lead">
          設計図があっても、1日に何をやるかが曖昧なら手は止まる。
          <br />
          THINKING は、設計図を「今日のチェックリスト」まで落とし込む。
          <br />
          迷う時間を、ゼロにする。
        </p>
      </div>
    </div>

    <div className="sup-section-inner">
      <article className="sup-block" id="step-roadmap" aria-labelledby="sup-step-h">
        <h3 id="sup-step-h" className="sup-h3">
          ステージ式ロードマップ<span className="sup-h3-paren">（STEP Roadmap）</span>
        </h3>
        <p className="sup-tagline">1ステップずつ、迷わず進める。</p>
        <p className="sup-body">
          合格設計図に沿って、各科目を1ステップごとに分解。
          「次にやるべき1ステップ」だけが目の前にある状態をつくる。
          <br />
          各ステップには、何をどう進めるかの詳細解説がついている。
          やり方で迷うことも、教材の使い方で迷うこともない。
        </p>
        <figure className="sup-figure sup-figure--roadmap">
          <img
            src={ASSETS.stepRoadmap}
            alt="ステージ式ロードマップのアプリ画面。STEP10英文法・不定詞のタスク一覧と修了テスト、次のSTEP11への進行が表示されている"
            loading="lazy"
            decoding="async"
            className="sup-figure-img sup-figure-img--natural"
          />
          <figcaption className="sup-cap">各STEPには詳細解説とチェックリストがついている</figcaption>
        </figure>
      </article>

      <article className="sup-block" id="weekly-sheet" aria-labelledby="sup-sheet-h">
        <h3 id="sup-sheet-h" className="sup-h3">
          週間・日次やること管理シート
        </h3>
        <p className="sup-tagline">今日やることが、1秒で分かる。</p>
        <p className="sup-body">
          毎週のコーチングで、次の1週間にやることを1日単位で決定する。
          朝起きたら、今日のリストを開く。終わったらチェックする。それだけでいい。
          <br />
          進捗は自動で集計され、達成率まで可視化される。
          うまくいった日・うまくいかなかった日が、数字で残る。
          だから、振り返りができる。だから、改善できる。
        </p>
        <ul className="sup-features sup-features--3">
          <li>
            <span className="sup-feat-no">01</span>
            <strong>1日単位で「やること」が確定</strong>
            <span>毎週のコーチングで、次週の1日1日が決まる。</span>
          </li>
          <li>
            <span className="sup-feat-no">02</span>
            <strong>達成率が自動で集計</strong>
            <span>学習時間・タスク達成率がリアルタイムで見える化。</span>
          </li>
          <li>
            <span className="sup-feat-no">03</span>
            <strong>数字に基づくPDCA</strong>
            <span>感覚ではなく、数字で振り返り、数字で改善する。</span>
          </li>
        </ul>
        <div className="sup-sheet-grid">
          <figure className="sup-figure sup-figure--sheet">
            <img
              src={ASSETS.sheetDaily}
              alt="日次の学習目標・時間枠・タスク・達成率を記録する管理シート"
              loading="lazy"
              decoding="async"
            />
            <figcaption className="sup-cap">日次タスク</figcaption>
          </figure>
          <figure className="sup-figure sup-figure--sheet">
            <img
              src={ASSETS.sheetWeeklyPeriod}
              alt="週間および期間中に完了させるタスクを管理するシート"
              loading="lazy"
              decoding="async"
            />
            <figcaption className="sup-cap">週間タスク・期間中タスク</figcaption>
          </figure>
          <figure className="sup-figure sup-figure--sheet">
            <img
              src={ASSETS.sheetSummary}
              alt="週次の目標時間・実績・達成率とタスク達成状況の結果サマリー"
              loading="lazy"
              decoding="async"
            />
            <figcaption className="sup-cap">週次サマリー</figcaption>
          </figure>
        </div>
      </article>

      <article className="sup-block" id="weekend-test" aria-labelledby="sup-wt-h">
        <h3 id="sup-wt-h" className="sup-h3">
          週末テスト制度
        </h3>
        <p className="sup-tagline">「わかったつもり」を、毎週潰す。</p>
        <p className="sup-body">
          毎週日曜日、その週に進めた範囲を週末テストで確認する。
          一定ラインを突破しないと、次のステップに進めない。志望校の出願も認めない。
          <br />
          「やった」ではなく「できる」になっているか。
          毎週、数字で証明する。緊張感が、習慣をつくる。
        </p>
        <figure className="sup-figure sup-figure--weekend">
          <img
            src={ASSETS.weekendTest}
            alt="週末テストの教材と、科目別得点率・理解度推移を示す結果ダッシュボード"
            loading="lazy"
            decoding="async"
            className="sup-figure-img sup-figure-img--natural"
          />
        </figure>
      </article>

      <article className="sup-block" id="manabo" aria-labelledby="sup-manabo-h">
        <h3 id="sup-manabo-h" className="sup-h3">
          24時間質問対応 ── manabo
        </h3>
        <p className="sup-tagline">分からない、を5分以内に解決する。</p>
        <p className="sup-body">
          駿台グループのスポット指導サービス「manabo」と業務提携。
          24時間いつでも、スマホで質問を送れば、最速1分で講師がオンライン指導を開始する。
          1問あたり5分のショート指導で、分からないをその場で潰す。
          <br />
          指導するのは、東大・京大・早慶など難関大に在籍・卒業の実力講師。
          あなたの志望校に在籍している講師の指名も可能。
        </p>
        <ul className="sup-manabo-grid">
          <li>
            <span className="sup-mat-no">01</span>
            <strong>24時間365日対応</strong>
            <span>深夜でも早朝でも、いつでも質問できる。</span>
          </li>
          <li>
            <span className="sup-mat-no">02</span>
            <strong>最速1分で指導開始</strong>
            <span>質問を送って、ほぼ即時に指導が始まる。</span>
          </li>
          <li>
            <span className="sup-mat-no">03</span>
            <strong>5分のスポット指導</strong>
            <span>1問完結。学習の流れを止めない。</span>
          </li>
          <li>
            <span className="sup-mat-no">04</span>
            <strong>難関大講師が直接対応</strong>
            <span>東大・京大・早慶など、実力講師のみが指導。</span>
          </li>
        </ul>
        <div className="sup-manabo-panel">
          <div className="sup-manabo-flow" aria-hidden="true">
            <div className="sup-manabo-step">
              <span className="sup-manabo-step-no">1</span>
              <span className="sup-manabo-step-tx">アプリから質問</span>
            </div>
            <span className="sup-manabo-arrow">→</span>
            <div className="sup-manabo-step">
              <span className="sup-manabo-step-no">2</span>
              <span className="sup-manabo-step-tx">講師がマッチ</span>
            </div>
            <span className="sup-manabo-arrow">→</span>
            <div className="sup-manabo-step">
              <span className="sup-manabo-step-no">3</span>
              <span className="sup-manabo-step-tx">ライブ指導 約5分</span>
            </div>
          </div>
          <div className="sup-manabo-chat" aria-label="指導の流れイメージ">
            <div className="sup-manabo-chat-head">
              <span className="sup-manabo-dot" />
              manabo スポット指導
            </div>
            <div className="sup-manabo-bubble sup-manabo-bubble--stu">
              この関係詞の先行詞、本文だと2つありそうで…
            </div>
            <div className="sup-manabo-bubble sup-manabo-bubble--coach">
              主節の主語に引きずられず、修飾のかかり先を印で切ってみよう。次は同じ構造を1分で説明して。
            </div>
            <div className="sup-manabo-meta">
              <span>最速レスポンス</span>
              <span className="sup-manabo-pill">1問完結</span>
            </div>
          </div>
        </div>
        <p className="sup-manabo-video-wrap">
          <a className="sup-manabo-video-btn" href={MANABO_VIDEO_URL} target="_blank" rel="noopener noreferrer">
            指導風景のイメージを見る
            <span className="sup-manabo-video-hint">（動画・別タブ）</span>
          </a>
        </p>
      </article>
    </div>
  </section>
);

/* ─── LAYER 03 鍛錬 ───────────────────────────────────────── */

const SupportLayerTrain = () => (
  <section className="sup-layer sup-layer--train" id="layer-train" aria-labelledby="sup-layer-train-title">
    <div className="sup-layer-band sup-layer-band--crimson">
      <div className="sup-section-inner sup-layer-band-inner">
        <p className="sup-layer-kicker">LAYER 03 ── 鍛える</p>
        <p className="sup-layer-en" lang="en">
          TRAIN
        </p>
        <h2 id="sup-layer-train-title" className="sup-layer-title">
          やり方を、根本から書き換える。
        </h2>
        <p className="sup-layer-lead">
          設計通りに実行しても、伸びない子がいる。
          原因は「やり方そのもの」にある。
          <br />
          THINKING は知識を教えない。
          やり方を、根本から書き換える。
          <br />
          考える力・解決する力 ── 受験の先でも武器になる力を鍛える。
        </p>
      </div>
    </div>

    <div className="sup-section-inner">
      <article className="sup-block" id="coaching" aria-labelledby="sup-coach-h">
        <h3 id="sup-coach-h" className="sup-h3">
          週1個別コーチング
        </h3>
        <p className="sup-tagline">「やったこと」ではなく「やり方」を直す。</p>
        <p className="sup-body">
          週1回、1対1のコーチングを実施する。
          ただし、振り返りだけで終わらせない。
          <br />
          THINKING のコーチングが他と決定的に違うのは、知識を提供しないこと。
          代わりに、その生徒が「どう読んだか・どう解いたか・なぜそう判断したか」を徹底的に言語化させる。
          <br />
          やり方の甘い部分・思考の抜け漏れを、そこで発見し、修正する。
          書き換えるのは知識ではなく、思考のプロセスそのもの。
        </p>
        <ol className="sup-coach-steps">
          <li>
            <span className="sup-coach-step-label">STEP 1</span>
            <strong>数字で振り返る</strong>
            <span>ロードマップ進捗、自習室滞在時間、達成率 ── すべての数字を一緒に見る。</span>
          </li>
          <li>
            <span className="sup-coach-step-label">STEP 2</span>
            <strong>来週の計画を1日単位で決める</strong>
            <span>合格設計図と現在地を照らし、来週やるべきことを1日ずつ確定させる。</span>
          </li>
          <li>
            <span className="sup-coach-step-label">STEP 3</span>
            <strong>やり方を点検し、書き換える</strong>
            <span>解き方・読み方・覚え方 ── 思考のプロセスそのものを点検する。ここがTHINKING の核。</span>
          </li>
        </ol>
        <aside className="sup-diff-box" aria-label="THINKINGの差別化">
          <p className="sup-diff-title">THINKING の差別化ポイント</p>
          <div className="sup-diff-rows">
            <div>
              <span className="sup-diff-label">他塾のコーチング</span>
              <p>進捗確認と計画立て</p>
            </div>
            <div className="sup-diff-highlight">
              <span className="sup-diff-label">THINKING のコーチング</span>
              <p>
                進捗確認 <span className="sup-diff-plus">+</span> 計画立て <span className="sup-diff-plus">+</span>{" "}
                <em>思考プロセスの修正</em>
              </p>
            </div>
          </div>
        </aside>
      </article>

      <article className="sup-block" id="verbalize" aria-labelledby="sup-verb-h">
        <h3 id="sup-verb-h" className="sup-h3">
          言語化特訓
        </h3>
        <p className="sup-tagline">読めたつもりを、撃ち抜く。</p>
        <p className="sup-body">
          多くの生徒が成績を飛躍的に伸ばしてきた、THINKING の看板特訓。
          <br />
          英文を解くのではない。解説を聞くのでもない。
          <br />
          「どう読んだか・どう判断したか・なぜその選択肢を選んだか」
          全選択肢に対して、生徒自身が言語化する。
          甘い部分には、即座にフィードバックが入る。
          <br />
          複数の生徒が参加するLIVE形式。緊張感の中で、思考が磨かれる。
        </p>
        <ul className="sup-features sup-features--3">
          <li>
            <span className="sup-feat-no">01</span>
            <strong>全選択肢に言語化</strong>
            <span>「なんとなく」を許さない。すべての選択肢に根拠を持たせる。</span>
          </li>
          <li>
            <span className="sup-feat-no">02</span>
            <strong>LIVE形式で実施</strong>
            <span>緊張感のある場で、思考力を鍛える。</span>
          </li>
          <li>
            <span className="sup-feat-no">03</span>
            <strong>徹底的な復習教材</strong>
            <span>1つの英文を完全に理解するための解説資料がついてくる。</span>
          </li>
        </ul>
        <a
          className="sup-sample-card"
          href="https://thinking-llcarc.github.io/english-lesson/okayama-rika-2023.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          <span className="sup-sample-eyebrow">Sample</span>
          <span className="sup-sample-title">実際の復習用解説資料を見る</span>
          <span className="sup-sample-arrow" aria-hidden="true">
            →
          </span>
        </a>
      </article>
    </div>
  </section>
);

/* ─── 1週間の流れ ───────────────────────────────────────── */

const SupportWeekFlow = () => {
  const weekStrip = [
    { short: "月", tone: "design" },
    { short: "火", tone: "execute" },
    { short: "水", tone: "execute" },
    { short: "木", tone: "execute" },
    { short: "金", tone: "train" },
    { short: "土", tone: "review" },
    { short: "日", tone: "test" },
  ];

  const days = [
    {
      day: "月曜日",
      layer: "設計",
      layerTone: "design",
      icon: "dialog",
      text: "週次コーチング（60分）── 先週の数字を振り返り、今週の1日単位のタスクを確定する。",
    },
    {
      day: "火・水・木曜日",
      layer: "実行",
      layerTone: "execute",
      icon: "check",
      text: "ステージ式ロードマップに沿って学習。分からない点は manabo で即解決（24時間）。日次シートで進捗を記録する。",
    },
    {
      day: "金曜日",
      layer: "鍛錬",
      layerTone: "train",
      icon: "mic",
      text: "言語化特訓（LIVE）── 緊張感のある場で、思考プロセスそのものを鍛える。",
    },
    {
      day: "土曜日",
      layer: "実行",
      layerTone: "review",
      icon: "graph",
      text: "週次サマリーを確認し、1週間の振り返りシートを記入。日曜の週末テストに向けて仕上げる。",
    },
    {
      day: "日曜日",
      layer: "実行",
      layerTone: "test",
      icon: "pen",
      highlight: true,
      text: "週末テスト ── 今週進めた範囲を、数字で証明する。結果は理解度推移に記録され、月曜のコーチングへつながる。",
    },
  ];
  const icons = {
    dialog: (
      <svg viewBox="0 0 32 32" className="sup-wf-icon" aria-hidden="true">
        <path
          fill="currentColor"
          d="M6 8h20a2 2 0 012 2v10a2 2 0 01-2 2H12l-6 4v-4H6a2 2 0 01-2-2V10a2 2 0 012-2z"
          opacity="0.9"
        />
      </svg>
    ),
    check: (
      <svg viewBox="0 0 32 32" className="sup-wf-icon" aria-hidden="true">
        <path fill="none" stroke="currentColor" strokeWidth="2" d="M8 16l6 6 10-14" />
      </svg>
    ),
    mic: (
      <svg viewBox="0 0 32 32" className="sup-wf-icon" aria-hidden="true">
        <path
          fill="currentColor"
          d="M16 4a4 4 0 014 4v8a4 4 0 11-8 0V8a4 4 0 014-4zm-8 12v2a8 8 0 007 7.93V28h2v-4.07A8 8 0 0024 18v-2h-2v2a6 6 0 11-12 0v-2H8z"
        />
      </svg>
    ),
    pen: (
      <svg viewBox="0 0 32 32" className="sup-wf-icon" aria-hidden="true">
        <path
          fill="currentColor"
          d="M22 4l6 6-14 14H8v-6L22 4zm-2 4L10 18v4h4l10-10-4-4z"
        />
      </svg>
    ),
    graph: (
      <svg viewBox="0 0 32 32" className="sup-wf-icon" aria-hidden="true">
        <path fill="currentColor" d="M4 26h24v2H4zm4-8h3v6H8zm6-6h3v12h-3zm6-8h3v20h-3z" />
      </svg>
    ),
  };
  return (
    <section className="sup-weekflow" id="week-flow" aria-labelledby="sup-wf-title">
      <div className="sup-section-inner">
        <header className="sup-wf-head">
          <p className="sup-wf-eyebrow" lang="en">
            Weekly Flow
          </p>
          <h2 id="sup-wf-title" className="sup-h2">
            1週間の動きイメージ
          </h2>
          <p className="sup-lead">
            設計 → 実行 → 鍛錬の三層が、月曜から日曜までこう連動する。
            <br />
            週末テストは<strong className="sup-wf-lead-strong">日曜日</strong>。数字で締め、月曜のコーチングへ戻る。
          </p>
        </header>

        <div className="sup-wf-weekbar" aria-label="1週間の流れ（月曜から日曜）">
          {weekStrip.map((cell) => (
            <div
              key={cell.short}
              className={`sup-wf-weekcell sup-wf-weekcell--${cell.tone}`}
            >
              <span className="sup-wf-weekcell-day">{cell.short}</span>
              {cell.tone === "test" && (
                <span className="sup-wf-weekcell-tag">週末テスト</span>
              )}
            </div>
          ))}
        </div>

        <ol className="sup-wf-timeline">
          {days.map((d, i) => (
            <li
              key={d.day}
              className={`sup-wf-item${d.highlight ? " sup-wf-item--highlight" : ""}`}
            >
              <div className="sup-wf-iconwrap">{icons[d.icon]}</div>
              <div className="sup-wf-body">
                <div className="sup-wf-meta">
                  <span className="sup-wf-day">{d.day}</span>
                  <span className={`sup-wf-layer sup-wf-layer--${d.layerTone}`}>
                    {d.layer}
                  </span>
                </div>
                <p>{d.text}</p>
              </div>
              {i < days.length - 1 && <span className="sup-wf-connector" aria-hidden="true" />}
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
};

/* ─── FAQ ─────────────────────────────────────────────────── */

const SupportFaq = () => {
  const qa = [
    {
      q: "入塾後すぐに合格設計図はもらえますか?",
      a: "はい。入塾後の最初の面談で、志望校・現在の学力・残り期間を踏まえて、専属コーチがあなた専用の合格設計図を作成します。最短で当日中、遅くとも1週間以内にお渡しします。",
    },
    {
      q: "志望校を途中で変更したくなった場合は?",
      a: "問題ありません。THINKING はコース切替制度を採用しており、志望校変更に応じて合格設計図そのものを組み替えます。途中変更で不利になることはありません。",
    },
    {
      q: "オンラインだけで本当に成績は伸びますか?",
      a: "THINKING は完全オンライン特化型の塾として設計されています。週1コーチング・言語化特訓（LIVE）・24時間質問対応・週末テストまで、すべてオンラインで完結する仕組みです。対面塾と同等以上の学習密度を実現しています。",
    },
    {
      q: "部活動や学校行事との両立はできますか?",
      a: "はい。合格設計図は生徒一人ひとりの生活リズムに合わせて作成します。部活引退時期や定期テスト期間も考慮した設計が可能です。",
    },
    {
      q: "保護者への報告はありますか?",
      a: "週次・月次で学習状況のレポートをお送りします。コーチングの内容、進捗状況、達成率まで透明に共有します。",
    },
    {
      q: "体験面談ではどのようなことをしますか?",
      a: "志望校・現状の学力・残り期間をヒアリングし、その場で合格までの簡易設計図をお見せします。THINKING の三層構造を、実際にイメージしていただけます。",
    },
  ];
  return (
    <section className="sup-faq" id="faq" aria-labelledby="sup-faq-title">
      <div className="sup-section-inner sup-faq-inner">
        <h2 id="sup-faq-title" className="sup-h2 sup-h2--center">
          よくあるご質問
        </h2>
        <div className="sup-faq-list">
          {qa.map((item) => (
            <details key={item.q} className="sup-faq-item">
              <summary>{item.q}</summary>
              <p>{item.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
};

/* ─── CTA ─────────────────────────────────────────────────── */

const SupportFinalCta = () => (
  <section className="sup-final-cta" id="contact" aria-labelledby="sup-cta-title">
    <div className="sup-final-cta-grid" aria-hidden="true" />
    <div className="sup-section-inner sup-final-cta-inner">
      <h2 id="sup-cta-title" className="sup-final-cta-title">
        「頑張る」を、「合格する」に変える。
      </h2>
      <p className="sup-final-cta-lead">合格までの設計図イメージ、まずは無料でお見せします。</p>
      <div className="sup-final-cta-btns">
        <a
          className="sup-cta-primary"
          href={window.THINKING_LINE_LIFF_URL}
          target="_blank"
          rel="noopener noreferrer"
        >
          無料体験面談に申し込む
        </a>
        <a className="sup-cta-secondary" href="/products">
          資料を請求する
        </a>
      </div>
    </div>
  </section>
);

window.SupportPage = SupportPage;
