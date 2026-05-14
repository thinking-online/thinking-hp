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
          a: "最大の違いは、学部別に戦略を設計し、専属コーチが日々の進捗まで伴走する点です。一般的な予備校は「全員同じカリキュラム」ですが、THINKING では「あなたの志望学部・現状・残り期間」から逆算した完全個別の合格設計図を作成します。詳しくは『なぜ学部別か』のページをご覧ください。",
        },
        {
          q: "授業形式は対面ですか、オンラインですか？",
          a: "オンライン塾のため、指導の主軸はすべてオンラインです。Zoom 等を用い、全国どこからでも受講いただけます。対面の校舎での通学型の授業は行っていません。",
        },
        {
          q: "校舎はありますか？運営会社はどこにありますか？",
          a: "通学用の校舎はありません。運営は東京に拠点があります。夏休みの期間などには、東京・大阪・福岡などでオフ会や勉強会を開催することもあります（日程・場所は都度ご案内します）。",
        },
        {
          q: "対応している学部を教えてください。",
          a: "私立文系の入試に対応しています。法学・経済・商・文学・国際・社会・政策など、学部別の設計と伴走が中心です。志望学部によって可否・プランが異なる場合がありますので、無料相談時に個別にご説明します。",
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
          a: "全員が「指導歴5年以上」という表現には当てはまりません。難関大学に現役合格した大学生コーチも在籍しており、THINKING の指導を受けて志望校に合格したうえで、厳しい研修を経て指導にあたるメンバーもいます。一方で、大手予備校で校舎長などを務めてきたスタッフもおり、責任を持って運営できる体制でお届けしています。詳細はサポート体制のページもご覧ください。",
        },
        {
          q: "コーチとの相性が合わなかった場合は？",
          a: "コーチの変更はご相談いただくことで可能です。一方で、THINKING は結果にコミットする塾です。成果が伸び悩む局面では、現状維持を手放し、学習の立て直しに踏み込む場面もあります。受講の「心地よさ」だけを優先すると合格から遠ざかることがあるため、プロとしての基準と向き合い方を徹底しています。そのうえで、ご本人の状況に沿って最善のマッチングと伴走を続けます。",
        },
        {
          q: "添削はどのくらいのペースで返ってきますか？",
          a: "従来型の提出添削に加え、24時間指導 manabo を活用すると、最速1分以内に講師とつながり、その場で解説を受けることも可能です。課題の種類や混雑状況により前後しますが、詰まったところをすぐに潰したいときの選択肢としてご利用いただけます。",
        },
        {
          q: "質問はいつでもできますか？",
          a: "可能です。勉強の進め方や学習設計に関しては専用フォームからもご相談いただけます。固定面談の中で整理することもできますし、24時間指導 manabo を通じて相談することもできます。",
        },
        {
          q: "保護者との連携はありますか？",
          a: "力を入れています。面談後の状況共有はもちろん、保護者様向けの専用チャットもご用意しています。出願の時期には、ご希望に応じて三者面談の機会を設け、進路・学習状況・方針をじっくり擦り合わせることも可能です（参加は任意です）。",
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
          a: "選考テストのようなものは一切ありません。いまの現状からどう合格に近づけるかを一緒に設計します。一方で、受け身のまま変化を起こす意思が見えない場合や、本人に前向きに取り組む意思が感じられない場合は、お断りすることがあります。一人ひとりと本気で向き合うからこそ、お互いにとって良いスタートになるかを大切にしています。",
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
          q: "合格率の数字は公表していますか？",
          a: "公表しておりません。志望の変化や集計の定義によって数字が大きく変わるため、率だけを切り取ってお伝えすると誤解を生みやすいと考えているからです。代わりに、日々の確認やロードマップ上の進捗を総合し、無謀な出願にならないよう、データと面談を重ねながら出願戦略を組み立てていきます。個別の状況は無料相談でお話しします。",
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
          a: "可能です。オンラインで指導するため、基本的にどこからでも受講いただけます。ロンドン在住の方はこれまでお見かけしたことはありませんが、ベトナム在住の受講生の指導を実際に行った経験もあります。時差と通信環境さえ整えば、国や地域を問わずご相談ください。",
        },
        {
          q: "個人情報の取り扱いについて教えてください。",
          a: "受講生・保護者の個人情報は、当塾の体制で厳重に管理しています。プライバシーマークの取得はしておりませんが、目的の範囲内での利用にとどめ、第三者への提供は行いません。取り扱いの詳細はプライバシーポリシーをご覧ください。",
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
                <a href="mailto:llcarc1110@gmail.com" className="cta-ghost cta-large">
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
      <button type="button" onClick={() => setOpen((v) => !v)}>
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
