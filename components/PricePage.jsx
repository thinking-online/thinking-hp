// Price page — plans + admission flow + payment FAQ
const PricePage = () => {
  // Common base — applied to all plans
  const baseRows = [
    { label: "システム利用料", value: "月額 2,980円", muted: true },
    { label: "対応科目", value: "全教科" },
    { label: "個別コーチング", value: "月4回" },
  ];

  // Standard support items — the foundation every plan inherits
  const standardSupport = [
    "志望校\u201d学部別\u201d逆算コーチング",
    "科目別ロードマップ",
    "週末テスト",
    "全体学習コーチング",
    "英語読解特訓",
    "24時間質問 manabo",
    "オンライン自習室",
  ];

  const plans = [
    {
      key: "standard",
      tier: "Standard",
      jp: "スタンダード",
      tag: "全教科対応・自走の基盤を作る",
      price: { monthly: "55,000" },
      lead: "受験勉強の土台を作る、すべてのプランの基準。学部別の逆算コーチングと、7つのサポートで自走を支えます。",
      kind: "base",
      base: standardSupport,
      addons: [],
      recommended: false,
    },
    {
      key: "advance",
      tier: "Advance",
      jp: "逆転合格アドバンス",
      tag: "過去問FB + TKメソッド月1",
      price: { monthly: "72,000" },
      lead: "夏以降、過去問演習にギアを入れる受講生の標準プラン。出題傾向への適応を、月次で固めます。",
      kind: "addon",
      base: standardSupport,
      addons: [
        { label: "過去問FB", desc: "志望校過去問の演習 → フィードバック → 再演習を、サイクルで回します。" },
        { label: "月1回 TKメソッド指導", desc: "生徒一人一人、個別で、直接、答案再構築・思考プロセスの矯正を月1回。" },
      ],
      recommended: true,
    },
    {
      key: "premium",
      tier: "Premium",
      jp: "逆転合格プレミアム",
      tag: "過去問FB + TKメソッド月2",
      price: { monthly: "85,000" },
      lead: "難関学部・残り期間が短い受験生に。代表が直接見る回数を倍にし、合格までの最短距離を引きます。",
      kind: "addon",
      base: standardSupport,
      addons: [
        { label: "過去問FB", desc: "志望校過去問の演習 → フィードバック → 再演習を、サイクルで回します。" },
        { label: "月2回 TKメソッド指導", desc: "生徒一人一人、個別で、直接、答案再構築・思考プロセスの矯正を月2回。" },
      ],
      recommended: false,
    },
  ];

  const flow = [
    {
      no: "01",
      en: "Application",
      jp: "LINEで友達追加 → 面談予約",
      desc: "公式LINEに「無料相談希望」とメッセージ。担当コーチから当日中に日程候補をご返信します。所要1〜3分。",
      duration: "申込から最短当日",
    },
    {
      no: "02",
      en: "Hearing",
      jp: "学習状況のヒアリング",
      desc: "現状の学力・志望学部・残り期間・お悩みを丁寧に伺います。担当：代表または学部責任者。",
      duration: "30〜45分",
    },
    {
      no: "03",
      en: "Design",
      jp: "合格設計図の提示",
      desc: "あなた専用のロードマップを、その場で提示。学部別の戦略・必要な学習量・想定スケジュールを共有。",
      duration: "相談中",
    },
    {
      no: "04",
      en: "Match",
      jp: "コーチのマッチング",
      desc: "志望学部・性格・学習スタイルを踏まえ、最適なコーチを2〜3名提案。体験面談で相性を確認できます。",
      duration: "1週間以内",
    },
    {
      no: "05",
      en: "Start",
      jp: "正式入塾・指導開始",
      desc: "ご納得いただけたら、契約・入金を経て、指導をスタート。当月分は日割り計算でご請求します。",
      duration: "随時開始可",
    },
  ];

  const paymentFaqs = [
    { q: "支払い方法は？", a: "クレジットカード（VISA / Mastercard / JCB / AMEX）、銀行振込のいずれか。月払いまたは年一括払いをお選びいただけます。" },
    { q: "途中解約はできますか？", a: "可能です。月単位での解約が可能で、違約金はかかりません。次月の引き落とし日の7日前までにご連絡ください。" },
    { q: "兄弟姉妹割引はありますか？", a: "ございます。同時受講の場合、2人目以降は月額料金から10,000円を割引します。" },
    { q: "教育ローンは使えますか？", a: "提携教育ローン（オリコ・ジャックス）をご利用いただけます。年率は3.5%〜。詳細は無料相談時にご案内します。" },
    { q: "途中でプラン変更できますか？", a: "可能です。月単位でアップグレード / ダウングレードが可能です。" },
  ];

  return (
    <>
      <PageHeader
        en="Pricing / How to Begin"
        eyebrow="料金・入塾まで"
        jp={<>料金は、すべて<em>公開</em>します。</>}
        lead="不透明な追加料金は一切ありません。3つのプランから、志望と学習スタイルに合わせてお選びいただけます。まずは無料相談で、あなたに合うプランを一緒に決めましょう。"
        bgImage="assets/campus-02.png"
      />

      {/* Plans */}
      <section className="price-plans">
        <div className="price-plans-inner">
          <div className="price-section-head">
            <span className="eyebrow"><i>Plans</i></span>
            <h2 className="price-section-title">
              3つのプランから、<br />
              <em>志望に合った設計</em>を。
            </h2>
            <p className="price-section-lead">
              すべてのプランで、専属コーチ + 学部責任者 + 添削講師の<br />
              「複数の目」体制は変わりません。違いは、伴走の頻度と深さです。
            </p>
          </div>

          <div className="plan-grid">
            {plans.map((p, i) => (
              <article
                key={p.key}
                className={`plan-card ${p.recommended ? "recommended" : ""} kind-${p.kind}`}
              >
                {p.recommended && (
                  <span className="plan-badge"><i>Most Popular</i></span>
                )}
                <header className="plan-head">
                  <span className="plan-tier"><i>{p.tier}</i></span>
                  <h3 className="plan-name">{p.jp}</h3>
                  <p className="plan-tag">{p.tag}</p>
                </header>

                <div className="plan-price">
                  <span className="plan-price-label">月額</span>
                  <span className="plan-price-currency">¥</span>
                  <span className="plan-price-num">{p.price.monthly}</span>
                </div>

                <ul className="plan-base-rows">
                  {baseRows.map((r, j) => (
                    <li key={j} className={r.muted ? "muted" : ""}>
                      <span className="base-label">{r.label}</span>
                      <span className="base-value">{r.value}</span>
                    </li>
                  ))}
                </ul>

                <p className="plan-lead">{p.lead}</p>

                <div className="plan-divider" />

                <span className="plan-support-label"><i>Support</i><em>サポート内容</em></span>

                {p.kind === "base" ? (
                  <ul className="plan-support-list">
                    {p.base.map((f, j) => (
                      <li key={j} className="support-pill">
                        <span className="pill-no"><i>{String(j + 1).padStart(2, "0")}</i></span>
                        <span className="pill-text">{f}</span>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <div className="plan-support-stack">
                    <div className="stack-block stack-base">
                      <div className="stack-head">
                        <span className="stack-en"><i>Standard Inclusive</i></span>
                        <h4>スタンダードの内容</h4>
                      </div>
                      <p className="stack-base-note">上記スタンダードの全7サポートを、すべてそのまま含みます。</p>
                    </div>
                    <span className="stack-plus" aria-hidden="true">+</span>
                    {p.addons.map((a, j) => (
                      <React.Fragment key={j}>
                        <div className="stack-block stack-addon">
                          <div className="stack-head">
                            <span className="stack-en"><i>Add-on {String(j + 1).padStart(2, "0")}</i></span>
                            <h4>{a.label}</h4>
                          </div>
                          <p className="stack-addon-desc">{a.desc}</p>
                        </div>
                        {j < p.addons.length - 1 && <span className="stack-plus" aria-hidden="true">+</span>}
                      </React.Fragment>
                    ))}
                  </div>
                )}

                <a
                  href="#apply"
                  className={p.recommended ? "cta plan-cta" : "cta-ghost plan-cta"}
                >
                  このプランで相談する
                  <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                    <path d="M5 12h14M13 5l7 7-7 7" />
                  </svg>
                </a>
              </article>
            ))}
          </div>

          <p className="plan-foot-note">
            ※ 表示価格はすべて税込。<br />
            ※ 全プラン共通：システム利用料 月額 2,980円が別途必要です。<br />
            ※ 中学生・高1高2は別プラン（月額 38,000円〜）あり。詳細は無料相談で。
          </p>
        </div>
      </section>

      {/* Flow */}
      <section className="price-flow" id="apply">
        <div className="price-flow-inner">
          <div className="price-section-head">
            <span className="eyebrow"><i>How to Start</i></span>
            <h2 className="price-section-title">
              入塾までの<em>5つのステップ</em>。
            </h2>
            <p className="price-section-lead">
              無料相談から指導開始まで、最短1週間。<br />
              強引な勧誘は一切ありません。
            </p>
          </div>

          <ol className="price-flow-list">
            {flow.map((s, i) => (
              <li key={i} className="price-flow-step">
                <div className="flow-step-rail">
                  <span className="flow-step-no"><i>{s.no}</i></span>
                  {i < flow.length - 1 && <span className="flow-step-line" />}
                </div>
                <div className="flow-step-body">
                  <span className="flow-step-en"><i>{s.en}</i></span>
                  <h3 className="flow-step-title">{s.jp}</h3>
                  <p className="flow-step-desc">{s.desc}</p>
                  <span className="flow-step-duration">所要：{s.duration}</span>
                </div>
              </li>
            ))}
          </ol>

          {/* LINE CTA — replaces application form */}
          <div className="price-line-cta" id="apply">
            <header className="price-line-head">
              <span className="eyebrow"><i>Online Consultation</i></span>
              <h3 className="price-line-title">
                予約は、<em>LINE登録</em>から。
              </h3>
              <p className="price-line-lead">
                公式LINEに「無料相談希望」と一言。<br />
                担当コーチから当日中に日程候補をお送りします。<br />
                <span className="dim">※ 強引な勧誘・自動応答は一切ありません。</span>
              </p>
            </header>

            <a
              className="line-cta-button"
              href="https://line.me/R/ti/p/@thinking"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span className="line-cta-button-icon" aria-hidden="true">
                <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                  <path
                    fill="currentColor"
                    d="M16 3C8.27 3 2 7.96 2 14.07c0 3.66 2.31 6.9 5.86 8.92c-.26.97-.95 3.55-1.09 4.1c-.17.69.25.68.53.49c.22-.15 3.5-2.38 4.92-3.34c1.22.18 2.5.27 3.78.27c7.73 0 14-4.96 14-11.07S23.73 3 16 3z"
                  />
                  <text x="16" y="17.5" textAnchor="middle" fontFamily="Helvetica, Arial, sans-serif" fontSize="6.5" fontWeight="700" fill="#0a0907" letterSpacing="0.05em">LINE</text>
                </svg>
              </span>
              <span className="line-cta-button-label">
                <span className="line-cta-button-jp">LINEで無料相談</span>
                <span className="line-cta-button-en"><i>Add Friend & Start</i></span>
              </span>
              <svg className="arrow" viewBox="0 0 16 16" fill="none">
                <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
              </svg>
            </a>

            <ul className="price-line-points">
              <li><span className="dot" />全国オンライン対応 / 60分</li>
              <li><span className="dot" />当日中に日程をご返信</li>
              <li><span className="dot" />相談中・相談後の勧誘は一切なし</li>
            </ul>
          </div>
        </div>
      </section>

      {/* Payment FAQ */}
      <section className="price-faq">
        <div className="price-faq-inner">
          <div className="price-section-head">
            <span className="eyebrow"><i>Payment FAQ</i></span>
            <h2 className="price-section-title">
              料金に関する<em>よくある質問</em>。
            </h2>
          </div>

          <ul className="price-faq-list">
            {paymentFaqs.map((f, i) => (
              <PriceFaqItem key={i} q={f.q} a={f.a} />
            ))}
          </ul>

          <div className="price-faq-foot">
            <span>その他の質問は</span>
            <a href="faq.html">よくある質問ページへ →</a>
          </div>
        </div>
      </section>
    </>
  );
};

const PriceFaqItem = ({ q, a }) => {
  const [open, setOpen] = React.useState(false);
  return (
    <li className={`price-faq-item ${open ? "open" : ""}`}>
      <button onClick={() => setOpen((v) => !v)}>
        <span className="faq-q-mark"><i>Q</i></span>
        <span className="faq-q-text">{q}</span>
        <span className="faq-q-toggle" aria-hidden="true" />
      </button>
      <div className="price-faq-a">
        <span className="faq-a-mark"><i>A</i></span>
        <p>{a}</p>
      </div>
    </li>
  );
};

window.PricePage = PricePage;
