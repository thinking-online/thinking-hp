// Price page — THINKINGサポート + admission flow + payment FAQ
const PricePage = () => {
  const supportItems = [
    { label: "全体学習コーチング", freq: "週2回" },
    { label: "英語言語化特訓", freq: "週1回" },
    { label: "個別コーチング", freq: "週1回" },
    { label: "合格設計図の作成" },
    { label: "学部別特化サポート" },
    { label: "ステージ式ロードマップ" },
    { label: "1日単位のやることリスト" },
    { label: "24時間質問サポート manabo" },
    { label: "24時間オンライン自習室" },
    { label: "週末テスト" },
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
    { q: "37,000円〜とは、どういう意味ですか？", a: "志望学部・残り期間・科目数によって最適な学習設計が変わるため、月額は37,000円からの目安です。無料相談でヒアリングしたうえで、あなたに必要なサポート内容と料金をその場でご提示します。料金表から選ぶ必要はありません。" },
    { q: "1科目だけでも入塾できますか？", a: "可能です。英語のみ、数学のみなど、科目単位でのスタートにも対応しています。まずは無料相談で、現状と志望に合わせた設計をご提案します。" },
    { q: "兄弟姉妹割引はありますか？", a: "ございます。同時受講の場合、2人目以降は月額料金から10,000円を割引します。詳細は無料相談時にご案内します。" },
    { q: "支払い方法は？", a: "クレジットカード（VISA / Mastercard / JCB / AMEX）、銀行振込のいずれか。月払いまたは年一括払いをお選びいただけます。" },
    { q: "途中解約はできますか？", a: "可能です。月単位での解約が可能で、違約金はかかりません。次月の引き落とし日の7日前までにご連絡ください。" },
    { q: "教育ローンは使えますか？", a: "提携教育ローン（オリコ・ジャックス）をご利用いただけます。年率は3.5%〜。詳細は無料相談時にご案内します。" },
  ];

  return (
    <>
      <PageHeader
        en="Pricing / How to Begin"
        eyebrow="料金・入塾まで"
        jp={<>私立文系合格に必要なことを、<em>すべて</em>詰め込みます。</>}
        lead="料金表から選ぶのではなく、THINKINGサポートというひとつの設計で、合格まで伴走します。まずは無料相談で、あなたの志望と学習量に合わせたプランを一緒に組み立てましょう。"
        bgImage="assets/campus-02.png"
      />

      <section className="price-plans">
        <div className="price-plans-inner">
          <div className="price-section-head">
            <span className="eyebrow"><i>THINKING Support</i></span>
            <h2 className="price-section-title">
              ひとつのサポートに、<br />
              <em>合格の仕組み</em>を。
            </h2>
            <p className="price-section-lead">
              コーチング、英語特訓、設計図、自習室、質問対応まで。<br />
              私立文系合格に必要なことを、ひとつにまとめました。
            </p>
          </div>

          <article className="support-hub">
            <div className="support-hub-intro">
              <header className="support-hub-head">
                <span className="support-hub-tier"><i>THINKING Support</i></span>
                <h3 className="support-hub-name">THINKINGサポート</h3>
                <p className="support-hub-tag">私立文系合格のために、必要なことをすべて。</p>
              </header>

              <div className="support-hub-price">
                <span className="support-hub-price-label">月額</span>
                <span className="support-hub-price-currency">¥</span>
                <span className="support-hub-price-num">37,000</span>
                <span className="support-hub-price-from">〜</span>
              </div>

              <p className="support-hub-lead">
                志望学部・残り期間・科目数に合わせて設計します。
                37,000円に「何が入っているか」を探すのではなく、
                あなたの合格に必要なサポートを、最初からすべて含めます。
              </p>

              <ul className="support-hub-notes">
                <li>1科目から入塾可能</li>
                <li>兄弟姉妹割引あり（2人目以降 月額10,000円割引）</li>
              </ul>

              <a href="#apply" className="cta support-hub-cta">
                無料相談で設計を聞く
                <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M5 12h14M13 5l7 7-7 7" />
                </svg>
              </a>
            </div>

            <div className="support-hub-body">
              <span className="plan-support-label"><i>Included</i><em>含まれるサポート</em></span>
              <ul className="support-hub-list">
                {supportItems.map((item, i) => (
                  <li key={i} className="support-hub-item">
                    <span className="support-hub-item-no"><i>{String(i + 1).padStart(2, "0")}</i></span>
                    <span className="support-hub-item-label">{item.label}</span>
                    {item.freq && <span className="support-hub-item-freq">{item.freq}</span>}
                  </li>
                ))}
              </ul>
            </div>
          </article>

          <p className="plan-foot-note">
            ※ 表示価格はすべて税込。月額37,000円〜は目安であり、志望・科目数により変動します。詳細は無料相談でご提示します。<br />
            ※ システム利用料 月額2,980円が別途必要です。<br />
            ※ 中学生・高1高2は別設計（月額38,000円〜）あり。詳細は無料相談で。
          </p>
        </div>
      </section>

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

          <div className="price-line-cta">
            <header className="price-line-head">
              <span className="eyebrow"><i>Online Consultation</i></span>
              <h3 className="price-line-title">
                まずは、<em>一度相談</em>してみませんか。
              </h3>
              <p className="price-line-lead">
                料金のこと、学習のこと、何でも構いません。<br />
                公式LINEに「無料相談希望」と一言。担当コーチから当日中に日程候補をお送りします。<br />
                <span className="dim">※ 強引な勧誘・自動応答は一切ありません。</span>
              </p>
            </header>

            <a
              className="line-cta-button"
              href={window.THINKING_LINE_LIFF_URL}
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
            <a href="/faq">よくある質問ページへ →</a>
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
