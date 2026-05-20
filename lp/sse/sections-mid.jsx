/* =====================================================
   SECTION: BRAIN COMPARE — Before(日本語脳) / After(英語脳)
===================================================== */
function BrainCompareSection() {
  const compareTrackRef = useRef(null);
  const [compareActive, setCompareActive] = useState(0);

  useEffect(() => {
    const track = compareTrackRef.current;
    if (!track) return undefined;

    const updateActive = () => {
      const w = track.clientWidth || 1;
      const index = Math.round(track.scrollLeft / w);
      setCompareActive(Math.min(1, Math.max(0, index)));
    };

    updateActive();
    track.addEventListener("scroll", updateActive, { passive: true });
    window.addEventListener("resize", updateActive);
    return () => {
      track.removeEventListener("scroll", updateActive);
      window.removeEventListener("resize", updateActive);
    };
  }, []);

  const scrollToCompare = (index) => {
    const track = compareTrackRef.current;
    const slide = track?.children[index];
    if (slide) {
      slide.scrollIntoView({ behavior: "smooth", inline: "start", block: "nearest" });
    }
    setCompareActive(index);
  };

  return (
    <section id="compare" className="compare-section theme-paper" data-screen-label="02 Brain Compare">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">03</div>
          <div>
            <span className="eyebrow">BEFORE / AFTER　脳内処理の比較</span>
            <h2 className="section-title">同じ英文を見た時、<br /><em>あなたの脳の中はどちらですか？</em></h2>
            <p className="section-lead">
              これは中学英単語のみで構成された一文。<br />
              でも、読み方の<strong>型</strong>がない脳には、まったく違う景色に映ります。
            </p>
          </div>
        </div>

        <div className="compare-source">
          <span className="compare-source-label">SOURCE TEXT　原文</span>
          <p>
            The baby at first doesn't realize that the sounds he hears are his own cries or that the moving thing passing in front of his eyes is his own hand.
          </p>
        </div>

        <div className="compare-switcher">
          <div className="compare-tabs" role="tablist" aria-label="脳内処理の比較">
            <button
              type="button"
              role="tab"
              aria-selected={compareActive === 0}
              className={`compare-tab ${compareActive === 0 ? "is-active" : ""}`}
              onClick={() => scrollToCompare(0)}
            >
              日本語脳
            </button>
            <button
              type="button"
              role="tab"
              aria-selected={compareActive === 1}
              className={`compare-tab ${compareActive === 1 ? "is-active" : ""}`}
              onClick={() => scrollToCompare(1)}
            >
              英語脳
            </button>
          </div>
          <p className="compare-swipe-hint">
            {compareActive === 0 ? "→ スワイプ（タップ）で英語脳へ" : "← スワイプで日本語脳へ"}
          </p>
        </div>
        <div className="compare-swipe">
          <div className="compare-swipe-track" ref={compareTrackRef} role="list">
          {/* BEFORE — 日本語脳 */}
          <div className="compare-col fail" role="listitem">
            <div className="compare-col-head">
              <div className="compare-col-tag">
                <span className="compare-icon-brain">⚠</span>
                <span>BEFORE</span>
              </div>
              <span className="compare-col-status fail">PROCESS FAILED</span>
            </div>
            <h3 className="compare-col-title">日本語脳の末路</h3>

            <div className="compare-stage fail">
              <div className="failed-fragments">
                <span className="frag" style={{ top: "10%", left: "8%" }}>赤ちゃんは気づかない<i>?</i></span>
                <span className="frag" style={{ top: "20%", left: "55%" }}>音…<i>?</i></span>
                <span className="frag" style={{ top: "40%", left: "20%" }}>彼自身の泣き声…<i>?</i></span>
                <span className="frag" style={{ top: "38%", left: "65%" }}>または…<i>?</i></span>
                <span className="frag" style={{ top: "62%", left: "15%" }}>動いているもの…<i>?</i></span>
                <span className="frag" style={{ top: "70%", left: "55%" }}>彼自身の手？<i>?</i></span>
                <svg className="frag-net" viewBox="0 0 100 100" preserveAspectRatio="none">
                  <path d="M 15 18 L 60 28 L 30 48 L 70 46 L 25 70 L 65 78" stroke="rgba(232,87,105,0.4)" strokeWidth="0.4" fill="none" strokeDasharray="1.5 2" />
                </svg>
              </div>
              <div className="compare-stage-note">
                <span className="note-icon">!</span>
                <p><strong>or</strong> が何と何を繋いでいるか見失い、後半で「え、何が手なの？」と情報の迷子になる。<br />文の構造が崩壊し、意味不明な単語の羅列として認識される。</p>
              </div>
            </div>
          </div>

          {/* AFTER — 英語脳 */}
          <div className="compare-col clear" role="listitem">
            <div className="compare-col-head">
              <div className="compare-col-tag">
                <span className="compare-icon-brain">◈</span>
                <span>AFTER</span>
              </div>
              <span className="compare-col-status clear">PROCESS CLEARED</span>
            </div>
            <h3 className="compare-col-title">英語脳の視界</h3>

            <div className="compare-stage clear">
              <div className="cleared-stem">
                <span className="stem-en">The baby at first doesn't realize</span>
                <span className="stem-jp">（赤ちゃんは最初は気づかない）</span>
              </div>

              <div className="cleared-tree">
                <div className="tree-conn">
                  <span className="tree-or">OR</span>
                </div>
                <div className="tree-branches">
                  <div className="tree-branch">
                    <span className="branch-tag">OBJECT 1 (A)</span>
                    <div className="branch-en">that the sounds he hears are his own cries</div>
                    <div className="branch-jp">（自分が聞いている音が自分の泣き声だということ）</div>
                  </div>
                  <div className="tree-branch">
                    <span className="branch-tag">OBJECT 2 (B)</span>
                    <div className="branch-en">that the moving thing ... is his own hand.</div>
                    <div className="branch-jp">（目の前を横切る物体が自分の手だということに）</div>
                  </div>
                </div>
              </div>

              <div className="compare-stage-note clear">
                <span className="note-icon clear">✓</span>
                <p><strong>"realize that A or that B"</strong> の構造を瞬時に把握。<br />前から左→右へ、意味のかたまりで処理が流れていく。</p>
              </div>
            </div>
          </div>
          </div>
        </div>

        <div className="compare-dots" aria-hidden="true">
          <span className={compareActive === 0 ? "is-active" : ""} />
          <span className={compareActive === 1 ? "is-active" : ""} />
        </div>

        <div className="compare-conclude">
          <div className="conclude-line"></div>
          <p>同じ英文・同じ脳・同じ単語量。<br /><strong>違うのは「読み方の型」だけ。</strong></p>
          <div className="conclude-line"></div>
        </div>
      </div>
    </section>
  );
}

window.BrainCompareSection = BrainCompareSection;

/* Smart Study English — middle sections */

/* =====================================================
   SECTION: SELF CHECK
===================================================== */
function SelfCheckSection() {
  return (
    <section id="check" className="self-check sse-hook-section" data-screen-label="95 Reality Hook">
      <div className="sse-hook-glow" aria-hidden="true" />

      <div className="wrap">
        <div className="section-head">
          <div className="section-num">04</div>
          <div>
            <span className="eyebrow">95% REALITY CHECK</span>
            <h2 className="section-title">
              衝撃の事実。<br />
              <em>高校生の約95％が、中学レベルの英文をスラスラ読めていない。</em>
            </h2>
            <p className="section-lead">
              使っている単語も文法も、すべて中学範囲。それでも意味が左からつながらない——それはあなたのせいではなく、
              <strong>「読み方」が教えられてこなかった結果</strong>です。
            </p>
          </div>
        </div>

        <div className="sse-hook-stat-hero">
          <div className="sse-hook-ring-wrap" aria-hidden="true">
            <svg className="sse-hook-ring-svg" viewBox="0 0 160 160">
              <defs>
                <linearGradient id="sseHookRingGold" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stopColor="#f5d98a" />
                  <stop offset="50%" stopColor="#d8a942" />
                  <stop offset="100%" stopColor="#b88728" />
                </linearGradient>
              </defs>
              <circle cx="80" cy="80" r="68" fill="none" stroke="rgba(255,255,255,0.08)" strokeWidth="10" />
              <circle
                className="sse-hook-ring-arc"
                cx="80"
                cy="80"
                r="68"
                fill="none"
                stroke="url(#sseHookRingGold)"
                strokeWidth="10"
                strokeLinecap="round"
                strokeDasharray="427"
                strokeDashoffset="21"
                transform="rotate(-90 80 80)"
              />
            </svg>
            <div className="sse-hook-ring-label">
              <span className="sse-hook-ring-num">95</span>
              <span className="sse-hook-ring-pct">%</span>
            </div>
          </div>

          <div className="sse-hook-stat-copy">
            <p className="sse-hook-stat-kicker">※指導・面談で見えてきた傾向の表現です</p>
            <p className="sse-hook-stat-main">
              中学＋高校で<strong>6年</strong>英語を学んでも、
              <br />
              <span className="sse-hook-stat-em">「読む処理」が未完成のまま</span>受験に突入しているケースが圧倒的多数。
            </p>
            <ul className="sse-hook-stat-bullets">
              <li>単語帳は進むのに、長文の意味が取れない</li>
              <li>読み返し・戻り読みが癖になっている</li>
              <li>文法用語は知っているのに、並びを前から処理できない</li>
            </ul>
          </div>
        </div>

        <div className="check-frame sse-hook-frame">
          <div className="check-frame-corner tl"></div>
          <div className="check-frame-corner tr"></div>
          <div className="check-frame-corner bl"></div>
          <div className="check-frame-corner br"></div>

          <p className="sse-hook-frame-label">中学英単語のみで書かれた、たった一文。</p>
          <div className="check-quote-mark">"</div>

          <p className="check-sentence">
            In the examples I am talking of the person continues to behave in what most people agree is a normal manner.
          </p>

          <div className="check-stat sse-hook-check-stat">
            <p className="check-stat-line">声に出して読んでみてください。</p>
            <p className="check-stat-line">途中で意味が途切れたり、同じ行を何度も辿ったりしたら——</p>
            <p className="check-stat-line check-stat-em">それは「95％側」の読み方です。</p>
          </div>
        </div>

        <div className="check-conclude">
          <div className="conclude-line"></div>
          <p>
            これは <em>頭の良さ</em> の差ではない。
            <br />
            <strong>処理フォーム</strong>がインストールされているかどうかの差。
          </p>
          <div className="conclude-line"></div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: WHY (バケツの穴)
===================================================== */
function WhySection() {
  const [pour, setPour] = useState(false);
  const bucketRef = useRef(null);

  useEffect(() => {
    const obs = new IntersectionObserver(([e]) => {
      if (e.isIntersecting) setPour(true);
    }, { threshold: 0.3 });
    if (bucketRef.current) obs.observe(bucketRef.current);
    return () => obs.disconnect();
  }, []);

  return (
    <section id="why" className="why-section theme-deep-crimson" data-screen-label="03 Why">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">05</div>
          <div>
            <span className="eyebrow">WHY IT FAILS</span>
            <h2 className="section-title">原因は、<br /><em>「読み方」にあります。</em></h2>
            <p className="section-lead">
              英語が読めない最大の原因は、単語量でも文法力でも演習量でもありません。<br />
              「読み方」そのものに、原因があります。
            </p>
          </div>
        </div>

        <div className="bucket-stage" ref={bucketRef}>
          <div className="bucket-side resource">
            <span className="bucket-side-label">RESOURCE　投入されるもの</span>
            <ul>
              <li><span>◎</span>高額な講座</li>
              <li><span>◎</span>単語の暗記</li>
              <li><span>◎</span>無限の努力時間</li>
              <li><span>◎</span>分厚い参考書</li>
            </ul>
            <div className="resource-arrow">↓</div>
          </div>

          <div className="bucket-center">
            <div className={`bucket-pour ${pour ? "active" : ""}`}>
              {[...Array(8)].map((_, i) => (
                <span key={i} className="drop" style={{ animationDelay: `${i * 0.15}s` }}></span>
              ))}
            </div>

            <svg viewBox="0 0 220 220" className="bucket-svg">
              <defs>
                <linearGradient id="bucketBody" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#1a2c66" />
                  <stop offset="100%" stopColor="#0a1530" />
                </linearGradient>
              </defs>
              <path d="M40 60 L 60 200 L 160 200 L 180 60 Z"
                fill="url(#bucketBody)"
                stroke="rgba(232,194,103,0.6)"
                strokeWidth="1.5" />
              <ellipse cx="110" cy="60" rx="70" ry="10" fill="rgba(232,194,103,0.1)" stroke="rgba(232,194,103,0.6)" strokeWidth="1.5" />
              {/* holes */}
              <g className="hole-group">
                <circle cx="80" cy="120" r="5" fill="#0a1530" stroke="#c8364a" strokeWidth="1.5" />
                <circle cx="120" cy="150" r="5" fill="#0a1530" stroke="#c8364a" strokeWidth="1.5" />
                <circle cx="145" cy="105" r="5" fill="#0a1530" stroke="#c8364a" strokeWidth="1.5" />
              </g>
              {/* leaks */}
              {pour && (
                <g className="leak-group">
                  <line x1="80" y1="125" x2="80" y2="220" stroke="#c8364a" strokeWidth="1" strokeDasharray="2 3" opacity="0.7">
                    <animate attributeName="stroke-dashoffset" values="0;-10" dur="0.8s" repeatCount="indefinite" />
                  </line>
                  <line x1="120" y1="155" x2="120" y2="220" stroke="#c8364a" strokeWidth="1" strokeDasharray="2 3" opacity="0.7">
                    <animate attributeName="stroke-dashoffset" values="0;-10" dur="0.9s" repeatCount="indefinite" />
                  </line>
                  <line x1="145" y1="110" x2="145" y2="220" stroke="#c8364a" strokeWidth="1" strokeDasharray="2 3" opacity="0.6">
                    <animate attributeName="stroke-dashoffset" values="0;-10" dur="0.7s" repeatCount="indefinite" />
                  </line>
                </g>
              )}
            </svg>

            <div className="bucket-label">
              <span>そのバケツ、<br />穴が空いている。</span>
            </div>
          </div>

          <div className="bucket-side causes">
            <span className="bucket-side-label">CAUSE　穴の正体</span>
            <ol>
              <li>
                <span className="cause-num">01</span>
                <div>
                  <strong>単語を一つひとつ日本語に置き換える</strong>
                  <p>情報がバラバラになり、文の意味がつながらない。</p>
                </div>
              </li>
              <li>
                <span className="cause-num">02</span>
                <div>
                  <strong>読み返す癖がついている</strong>
                  <p>時間が足りなくなる。情報が頭に残らない。</p>
                </div>
              </li>
              <li>
                <span className="cause-num">03</span>
                <div>
                  <strong>文法を「ルール」として暗記している</strong>
                  <p>実際の長文では、ルールが使えない。</p>
                </div>
              </li>
            </ol>
          </div>
        </div>

        <div className="why-conclude">
          <div className="conclude-row">
            <span className="x-mark">×</span>
            <span>個別塾で知識の解説を増やす</span>
          </div>
          <div className="conclude-row">
            <span className="x-mark">×</span>
            <span>集団授業で講義を聞き続ける</span>
          </div>
          <div className="conclude-row">
            <span className="x-mark">×</span>
            <span>効率的とされる参考書を回す</span>
          </div>
          <p className="why-conclude-note">
            どれだけ単語を覚えても、読み方の穴が空いている限り、抜け落ち続けます。<br />
            <strong>順番が逆。先に「読み方」の穴を塞ぐ必要があります。</strong>
          </p>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: ORDER (順番の論理)
===================================================== */
function OrderSection() {
  return (
    <section id="order" className="order-section theme-deep-gold" data-screen-label="04 Order">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">06</div>
          <div>
            <span className="eyebrow">THE ORDER OF EFFORT</span>
            <h2 className="section-title">努力は否定しない。<br /><em>順番だけを、変える。</em></h2>
            <p className="section-lead">
              先に「読み方の型」を矯正し、その上に単語・文法・演習を積む。<br />
              この構造的な順序だけが、成果の差を生みます。
            </p>
          </div>
        </div>

        <div className="order-flow">
          <div className="order-step">
            <div className="step-marker">
              <span className="step-num">STEP 01</span>
              <div className="step-icon">⌂</div>
            </div>
            <h3>型を矯正する</h3>
            <p>前から意味のかたまりで処理するフォームを確立。<br />読みの土台を脳にインストール。</p>
          </div>

          <div className="order-arrow">→</div>

          <div className="order-step">
            <div className="step-marker">
              <span className="step-num">STEP 02</span>
              <div className="step-icon">▣</div>
            </div>
            <h3>知識を投入する</h3>
            <p>単語・文法・演習を、型がある状態の上に積み上げる。<br />同じ努力でも、定着率が変わる。</p>
          </div>

          <div className="order-arrow">→</div>

          <div className="order-step">
            <div className="step-marker">
              <span className="step-num">STEP 03</span>
              <div className="step-icon">◐</div>
            </div>
            <h3>時間内に出力する</h3>
            <p>共通テスト・難関私大の高速処理に対応。<br />速く・正確に・安定して解ける状態へ。</p>
          </div>
        </div>

        <div className="order-warn">
          <span className="warn-icon">⚠</span>
          <p>順番を誤ると、その後の単語・文法・演習の <strong>投資効率は極端に下がる</strong>。<br />
          だからこそ、短期間で一気に矯正しきる必要があります。</p>
        </div>
      </div>
    </section>
  );
}

window.SelfCheckSection = SelfCheckSection;
window.WhySection = WhySection;
window.OrderSection = OrderSection;
