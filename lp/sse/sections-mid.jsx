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
    <section id="check" className="self-check sse-hook-section" data-screen-label="Diagnosis + 95 Hook">
      <div className="sse-hook-glow" aria-hidden="true" />

      <div className="wrap">
        <div className="sse-hook-quiz-intro">
          <div className="section-head sse-hook-quiz-head">
            <div className="section-num">04</div>
            <div>
              <span className="eyebrow">READING CHECK</span>
              <h2 className="section-title">
                中学英単語で構成された文
                <br />
                <em>あなたはスラスラ読める？</em>
              </h2>
              <p className="section-lead">
                声に出しても頭の中だけでもOK。
                <br />
                止まらず、左から意味がつながるかだけ見てください。
              </p>
            </div>
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

          <div className="check-stat sse-hook-check-stat sse-hook-readsign">
            <p className="check-stat-line">途中で意味が途切れたり、同じところを何度も辿ったりしたら——</p>
            <p className="sse-hook-readsign-result">
              <span className="sse-hook-readsign-row">それは<strong>「読み方の型」</strong>が</span>
              <span className="sse-hook-readsign-row">まだ乗っていない<span className="sse-hook-readsign-tail">サインです。</span></span>
            </p>
          </div>
        </div>

        <div className="sse-hook-result-bridge" aria-hidden="true">
          <span className="sse-hook-result-arrow">↓</span>
          <p className="sse-hook-result-text">
            結果はどうだったかというと・・・
          </p>
        </div>

        <div className="sse-hook-reveal">
          <span className="sse-hook-reveal-ornament" aria-hidden="true" />
          <p className="sse-hook-reveal-kicker">では、数字でいいます。</p>
          <h3 className="sse-hook-reveal-title">
            <span className="sse-hook-reveal-title-row">
              実は<strong>95％以上</strong>の中高生が
            </span>
            <span className="sse-hook-reveal-title-row">中学レベルの英文ですら</span>
            <span className="sse-hook-reveal-title-row">
              <strong>スラスラ</strong>読めていません
            </span>
          </h3>
          <p className="sse-hook-reveal-note">※当社調べ（中高生対象）</p>
        </div>

        <div className="sse-hook-stat-hero">
          <figure className="sse-hook-stat-visual">
            <img
              src="assets/hook-95-stat-banner.png"
              alt="実は95％以上の中高生が、中学レベルの英文ですらスラスラ読めていません。※当社調べ・中高生対象"
              width="1024"
              height="576"
              loading="lazy"
              decoding="async"
            />
          </figure>

          <div className="sse-hook-stat-copy">
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

        <div className="check-conclude">
          <div className="conclude-line"></div>
          <p>
            これは <em>頭の良さ</em> の差ではない。
            <br />
            <strong>処理フォーム</strong>が先に整っているかどうかの差。
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
  const bucketRef = useRef(null);
  const [active, setActive] = useState(false);

  useEffect(() => {
    const el = bucketRef.current;
    if (!el) return undefined;

    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) setActive(true);
      },
      { threshold: 0.28 }
    );

    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <section id="why" className="why-section theme-deep-crimson" data-screen-label="03 Why">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">05</div>
          <div>
            <span className="eyebrow">WHY IT FAILS</span>
            <h2 className="section-title">
              このままだと、<br />
              <em>その投資、無駄になります。</em>
            </h2>
            <p className="section-lead">
              先ほどのような「積み上げ」ほど、読みの土台がグラグラだと危険です。
              ここを直さないまま単語・文法・講座にお金と時間を重ねるほど、
              <strong>その投資は回収しづらくなります。</strong>
              塾や教材が悪いのではありません。問題は、
              <strong>前から意味をつなぐ型</strong>がないまま投入してしまう順番です。
              穴の空いたバケツに注ぎ続ける状態では、努力も費用も
              <strong>水の泡になりやすい</strong>のです。
            </p>
          </div>
        </div>

        <div className="bucket-stage">
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
            <div
              ref={bucketRef}
              className={`bucket-viz${active ? " is-active" : ""}`}
              aria-hidden="true"
            >
              <svg viewBox="0 0 220 260" className="bucket-svg-anim">
                <defs>
                  <linearGradient id="whyBucketWater" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="rgba(196, 223, 240, 0.75)" />
                    <stop offset="100%" stopColor="rgba(140, 185, 220, 0.5)" />
                  </linearGradient>
                  <clipPath id="whyBucketClip">
                    <path d="M46 66 L 63 194 L 157 194 L 174 66 Z" />
                  </clipPath>
                </defs>

                <ellipse className="bucket-puddle-svg" cx="110" cy="248" rx="72" ry="10" />

                <path
                  className="bucket-outline"
                  d="M42 58 L 61 198 L 159 198 L 178 58 Z"
                  fill="rgba(10, 21, 48, 0.55)"
                  stroke="rgba(217, 169, 66, 0.55)"
                  strokeWidth="1.5"
                />
                <ellipse
                  className="bucket-rim"
                  cx="110"
                  cy="58"
                  rx="68"
                  ry="9"
                  fill="rgba(255, 255, 255, 0.04)"
                  stroke="rgba(217, 169, 66, 0.5)"
                  strokeWidth="1.2"
                />

                <g className="bucket-water-group" clipPath="url(#whyBucketClip)">
                  <rect
                    className="bucket-water-body"
                    x="54"
                    y="108"
                    width="112"
                    height="82"
                    fill="url(#whyBucketWater)"
                  />
                  <ellipse
                    className="bucket-water-surface"
                    cx="110"
                    cy="108"
                    rx="54"
                    ry="5"
                    fill="rgba(220, 235, 248, 0.5)"
                  />
                </g>

                <circle className="bucket-hole" cx="80" cy="122" r="4" fill="#0a1530" stroke="rgba(217, 169, 66, 0.65)" strokeWidth="1.2" />
                <circle className="bucket-hole" cx="120" cy="148" r="4" fill="#0a1530" stroke="rgba(217, 169, 66, 0.65)" strokeWidth="1.2" />
                <circle className="bucket-hole" cx="144" cy="108" r="4" fill="#0a1530" stroke="rgba(217, 169, 66, 0.65)" strokeWidth="1.2" />

                <line className="bucket-leak bucket-leak--a" x1="80" y1="126" x2="80" y2="248" />
                <line className="bucket-leak bucket-leak--b" x1="120" y1="152" x2="120" y2="248" />
                <line className="bucket-leak bucket-leak--c" x1="144" y1="112" x2="144" y2="248" />

                <circle className="bucket-drop bucket-drop--1" cx="98" cy="24" r="2.5" />
                <circle className="bucket-drop bucket-drop--2" cx="110" cy="18" r="3" />
                <circle className="bucket-drop bucket-drop--3" cx="122" cy="26" r="2" />
              </svg>

              <p className="bucket-hole-label">読み方の穴</p>
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
            今のままでは、せっかく払った費用も、積み上げた勉強時間も、結果に変わり切らず流れ落ちます。<br />
            <strong>だから最優先は「読み方」の穴埋め。ここを先に塞げば、同じ投資が生き始めます。</strong>
          </p>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: OFFER BRIDGE (オファー前の接続)
===================================================== */
function OfferBridgeSection() {
  return (
    <section id="offer-bridge" className="offer-bridge-section" data-screen-label="Offer Bridge">
      <div className="offer-bridge-bg" aria-hidden="true">
        <img
          src="assets/offer-bridge-sakura.png"
          alt=""
          width="1920"
          height="1080"
          loading="lazy"
          decoding="async"
        />
        <div className="offer-bridge-overlay" />
      </div>

      <div className="wrap offer-bridge-wrap">
        <div className="offer-bridge-panel">
          <p className="offer-bridge-catch">
            <span className="ob-line">努力すればするだけ</span>
            <span className="ob-line">ちゃんと報われる。</span>
            <span className="ob-line ob-line--gold">
              <strong>努力家が勝てる世界に。</strong>
            </span>
          </p>

          <div className="offer-bridge-divider" aria-hidden="true">
            <span />
          </div>

          <p className="offer-bridge-copy">
            <span className="ob-line">こんな未来をつくるために、</span>
            <span className="ob-line">「英語の読み方」を根本から解決する。</span>
            <span className="ob-line">そんな企画が、ここで誕生しました。</span>
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
window.OfferBridgeSection = OfferBridgeSection;
window.OrderSection = OrderSection;
