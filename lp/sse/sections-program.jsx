/* Smart Study English — program & 45-day design */

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

          <div className="method-overview-media">
            <figure className="method-overview-figure">
              <img
                src="assets/program-learning-contents.png"
                alt="3つの学習コンテンツ"
                loading="lazy"
                decoding="async"
              />
              <figcaption>学習コンテンツ</figcaption>
            </figure>

            <div className="method-overview-plus" aria-hidden="true">
              ＋
            </div>

            <figure className="method-overview-figure">
              <img
                src="assets/program-support-system.png"
                alt="徹底的なサポート体制"
                loading="lazy"
                decoding="async"
              />
              <figcaption>徹底的なサポート体制</figcaption>
            </figure>
          </div>
        </div>

        {/* Program contents */}
        <div className="method-contents">
          <div className="contents-head">
            <span className="eyebrow">PROGRAM CONTENTS</span>
            <h3 className="contents-title">矯正のための<em>3要素</em>と、自走を支える<em>サポート体制</em></h3>
          </div>

          <div className="contents-grid">
            <div className="contents-card">
              <span className="contents-num">▢ 01</span>
              <h4>構造理解・文章講義</h4>
              <p>丸暗記ではなく英文法のコアイメージを理解。<br />「なぜそう読むのか」の理屈を、長文読解の土台としてインストール。</p>
            </div>
            <div className="contents-card">
              <span className="contents-num">▶ 02</span>
              <h4>50本以上の映像講義</h4>
              <p>「どう処理するか」を可視化した映像で、日々のトレーニング手順を明確化。<br />いつでも見返してフォームを確認できる。</p>
            </div>
            <div className="contents-card">
              <span className="contents-num">✏ 03</span>
              <h4>毎日提出と個別質問</h4>
              <p>「分かったつもり」を防ぐ出力ワーク。<br />できている箇所/いない箇所を明確にし、ズレをその場で修正。</p>
            </div>
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
