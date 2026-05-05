// FAQ page — categorized accordion
const FaqPage = () => {
  const categories = [
    {
      key: "about",
      en: "About",
      jp: "塾について",
      items: [
        {
          q: "他の予備校・塾と何が違うのですか？",
          a: "最大の違いは、学部別に戦略を設計し、専属コーチが日々の進捗まで伴走する点です。一般的な予備校は「全員同じカリキュラム」ですが、THINKING. では「あなたの志望学部・現状・残り期間」から逆算した完全個別の合格設計図を作成します。詳しくは『なぜ学部別か』のページをご覧ください。",
        },
        {
          q: "授業形式は対面ですか、オンラインですか？",
          a: "原則オンラインです。Zoom を使い、全国どこからでも受講いただけます。Eliteプランの方は希望時のみ対面（東京）も可能です。オンラインに統一することで、業界トップ層のコーチをマッチングできるのが強みです。",
        },
        {
          q: "校舎はありますか？",
          a: "東京・恵比寿に拠点を置いていますが、通学型の校舎ではありません。代表面談や対面コーチング、保護者面談などで使用します。",
        },
        {
          q: "対応している学部を教えてください。",
          a: "現在、医学部・法学部・経済学部・文学部・理工学部・教育学部・国際教養学部の7学部に対応しています。2026年中に薬学部・看護学部の追加を予定しています。",
        },
        {
          q: "中学生・高1高2でも受講できますか？",
          a: "可能です。中学生・高1高2向けには別プラン（月額 38,000円〜）をご用意しています。早期から学部を見据えた学習設計を行うことで、高3以降の伸びが大きく変わります。",
        },
      ],
    },
    {
      key: "coaching",
      en: "Coaching",
      jp: "指導内容",
      items: [
        {
          q: "コーチはどんな方ですか？",
          a: "全員、指導歴5年以上・難関大合格実績多数のプロコーチです。各学部の責任者は、その学部の出身者かつ専門指導歴を持つ専門家。詳細はサポート体制のページでご紹介しています。",
        },
        {
          q: "コーチとの相性が合わなかった場合は？",
          a: "コーチは何度でも変更可能です。月次レビューで相性を確認し、必要に応じて学部責任者がマッチングを調整します。「合わない」と感じたら、すぐにご相談ください。",
        },
        {
          q: "添削はどのくらいのペースで返ってきますか？",
          a: "提出から72時間以内に返却します。直前期（11月〜2月）は48時間以内です。",
        },
        {
          q: "質問はいつでもできますか？",
          a: "Slack または LINE で24時間質問可能です。返信は、ベーシック：24時間以内 / プレミアム：平均30分以内 / エリート：即時対応 となります。",
        },
        {
          q: "保護者との連携はありますか？",
          a: "あります。プレミアムは月1回、エリートは月2回、保護者面談を実施します。お子様の学習状況・課題・今後の方針を、ご家族と共有しながら進めます。",
        },
      ],
    },
    {
      key: "admission",
      en: "Admission",
      jp: "入塾・申込",
      items: [
        {
          q: "入塾までの流れは？",
          a: "①無料相談予約 → ②学習状況のヒアリング → ③合格設計図の提示 → ④コーチのマッチング → ⑤正式入塾、の5ステップです。最短1週間で指導を開始できます。詳細は『料金・入塾まで』のページをご覧ください。",
        },
        {
          q: "無料相談は何分くらいですか？",
          a: "30〜45分です。代表または学部責任者が直接お話を伺い、その場で合格までの設計図をお渡しします。強引な勧誘は一切いたしません。",
        },
        {
          q: "途中入塾はできますか？",
          a: "可能です。年間を通じて、いつでも入塾いただけます。当月分は日割り計算でご請求します。ただし、月10名の定員制のため、空き枠次第となります。",
        },
        {
          q: "受験直前期（12月以降）の入塾は可能ですか？",
          a: "可能ですが、定員上、お断りすることもあります。直前期の入塾でも合格に間に合うよう、緊急対策プログラムをご用意しています。",
        },
        {
          q: "選考はありますか？",
          a: "ありません。学力・偏差値による選考は行いません。ただし、定員上、先着順となります。",
        },
      ],
    },
    {
      key: "result",
      en: "Result",
      jp: "成果・実績",
      items: [
        {
          q: "本当に偏差値が30台でも難関大に合格できますか？",
          a: "はい。実際に偏差値30台から早慶・GMARCHに合格した受講生が複数いらっしゃいます。鍵は「正しい順序で、必要なことだけを、徹底的にやる」こと。学部別戦略と日々の伴走で、これを実現します。実例は『合格者の声』ページをご覧ください。",
        },
        {
          q: "合格できなかった場合の保証はありますか？",
          a: "「合格保証」のような誇大な約束はいたしません。ただし、当塾の責に帰すべき事由（指導の重大な欠陥等）がある場合は、料金の一部返金規定があります。詳細は契約時にご説明します。",
        },
        {
          q: "合格率はどのくらいですか？",
          a: "第一志望合格率は約62%、第二志望までを含めると約87%です（2024年度実績）。一般的な予備校の第一志望合格率（10〜15%）と比較して、4倍以上の数値です。",
        },
      ],
    },
    {
      key: "other",
      en: "Other",
      jp: "その他",
      items: [
        {
          q: "推薦入試・総合型選抜にも対応していますか？",
          a: "対応しています。志望理由書・小論文・面接対策を、各学部の専門コーチが指導します。一般入試との併願プランも設計可能です。",
        },
        {
          q: "海外在住でも受講できますか？",
          a: "可能です。オンライン中心のため、時差さえ調整できれば全世界から受講いただけます。実際にシンガポール・ロンドン在住の受講生もいらっしゃいます。",
        },
        {
          q: "個人情報の取り扱いについて教えてください。",
          a: "当塾はプライバシーマーク取得済みです。受講生・保護者の個人情報は厳重に管理し、第三者への提供は行いません。詳細はプライバシーポリシーをご覧ください。",
        },
      ],
    },
  ];

  const [activeCategory, setActiveCategory] = React.useState("about");

  return (
    <>
      <PageHeader
        en="Frequently Asked Questions"
        eyebrow="よくある質問"
        jp={<>あなたの<em>不安</em>に、<br />一つずつお答えします。</>}
        lead="入塾を検討される方からよくいただく質問をまとめました。掲載のない質問は、無料相談時にお気軽にお尋ねください。"
      />

      <section className="faq-section">
        <div className="faq-section-inner">
          {/* Category nav */}
          <nav className="faq-nav" aria-label="質問カテゴリ">
            {categories.map((c) => (
              <button
                key={c.key}
                className={`faq-nav-item ${activeCategory === c.key ? "active" : ""}`}
                onClick={() => {
                  setActiveCategory(c.key);
                  document.getElementById(`faq-${c.key}`)?.scrollTo?.(0, 0);
                  const el = document.getElementById(`faq-cat-${c.key}`);
                  if (el) {
                    const top = el.getBoundingClientRect().top + window.scrollY - 100;
                    window.scrollTo({ top, behavior: "smooth" });
                  }
                }}
              >
                <span className="faq-nav-en"><i>{c.en}</i></span>
                <span className="faq-nav-jp">{c.jp}</span>
                <span className="faq-nav-count">{c.items.length}</span>
              </button>
            ))}
          </nav>

          {/* Categories */}
          <div className="faq-categories">
            {categories.map((c) => (
              <FaqCategory key={c.key} category={c} />
            ))}
          </div>

          {/* Contact CTA */}
          <div className="faq-contact">
            <div className="faq-contact-card">
              <span className="eyebrow"><i>Still Have Questions?</i></span>
              <h3 className="faq-contact-title">
                掲載のない質問は、<br />
                <em>直接お聞きください。</em>
              </h3>
              <p className="faq-contact-lead">
                無料相談（30〜45分）にて、代表または学部責任者が<br />
                すべてのご質問にお答えします。
              </p>
              <div className="faq-contact-ctas">
                <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta cta-large">
                  LINEで無料相談
                  <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                    <path d="M5 12h14M13 5l7 7-7 7" />
                  </svg>
                </a>
                <a href="mailto:info@thinking.example" className="cta-ghost cta-large">
                  メールで質問する
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

const FaqCategory = ({ category }) => {
  return (
    <div className="faq-category" id={`faq-cat-${category.key}`}>
      <header className="faq-category-head">
        <span className="faq-category-en"><i>{category.en}</i></span>
        <h2 className="faq-category-title">{category.jp}</h2>
        <span className="faq-category-line" />
      </header>
      <ul className="faq-items" id={`faq-${category.key}`}>
        {category.items.map((item, i) => (
          <FaqItem key={i} item={item} index={i} />
        ))}
      </ul>
    </div>
  );
};

const FaqItem = ({ item, index }) => {
  const [open, setOpen] = React.useState(false);
  return (
    <li className={`faq-item ${open ? "open" : ""}`}>
      <button onClick={() => setOpen((v) => !v)}>
        <span className="faq-item-no"><i>{String(index + 1).padStart(2, "0")}</i></span>
        <span className="faq-item-q">
          <span className="faq-item-mark"><i>Q.</i></span>
          {item.q}
        </span>
        <span className="faq-item-toggle" aria-hidden="true" />
      </button>
      <div className="faq-item-a">
        <span className="faq-item-mark a"><i>A.</i></span>
        <p>{item.a}</p>
      </div>
    </li>
  );
};

window.FaqPage = FaqPage;
