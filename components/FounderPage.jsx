// Founder page — long-form profile of the代表
const FounderPage = () => {
  const timeline = [
    { year: "1998", event: "東京生まれ。幼少期からサッカーに明け暮れ、副主将としてチームを支える一方、学業との距離が生まれる。" },
    { year: "2017", event: "大学受験で志望先にことごとく不合格。長時間の勉強が報われず、「努力の質」を問い直す。" },
    { year: "2018", event: "浪人期を経て早稲田大学商学部に逆転合格・入学。在学中より個別指導・予備校の現場へ立ち、画一的な授業の限界と、志望学部に沿った設計の必要性を痛感。" },
    { year: "2022", event: "早稲田大学 商学部 卒業。私立文系の最前線に立ち続け、延べ2,000名以上の受験生と向き合う。" },
    { year: "2023", event: "合同会社ARCを設立。11月、オンライン塾「THINKING」を開講。全国どこからでも、志望学部に特化した設計を届ける。" },
    { year: "2024", event: "新R25・テレビ番組などメディア取材が増加。指導体系と実績が紹介される。" },
    { year: "2025", event: "受講生の規模を拡げつつも、月10名限定の方針は変えない。一人ひとりに設計と伴走を届ける体制を優先する。" },
  ];


  const beliefs = [
  {
    no: "01",
    title: "「教える」のではなく、「考えさせる」。",
    body: "答えを与えるのは簡単です。しかし、それでは試験本番で応用が効きません。私たちは、生徒が自ら考え、自ら答えにたどり着けるよう、問いを投げかけ続けます。塾名に「THINKING」と冠したのは、これが理由です。"
  },
  {
    no: "02",
    title: "全員には、教えない。",
    body: "現場に立ち続けてわかったことがあります。「全員に同じ授業」は、誰のためにもなりません。だから私たちは、見られる人数しか受け入れません。月10名、これが私たちの限界であり、矜持です。"
  },
  {
    no: "03",
    title: "数字より、ひとりの物語を。",
    body: "日々の積み重ねや偏差値の伸びも大切です。それ以上に大切なのは、10代後半の1〜2年をどんな密度で過ごすかです。受験は通過点。でも、人生を変えうる通過点。その過程で身につく自走力と戦略眼は、一生ものになります。私はそこに最も価値を置いています。"
  }];


  const media = [
  { year: "2024", outlet: "新R25", topic: "ドS管理で、逆転合格へ。完全〝子〟別、人生を変えるオンライン塾。" },
  { year: "2023", outlet: "新R25", topic: "偏差値42→70早稲田大卒。最強の〝脳内インストール〟英語学習法。" },
  { year: "2023", outlet: "東京MX", topic: "首都圏・東京MXの番組で、私立文系向け個別指導の現場が紹介されました。" }];


  return (
    <>
      <PageHeader
        en="Founder"
        eyebrow="代表紹介"
        jp={<>受験は<em>通過点</em>。<br />でも、人生を<em>変えうる</em>通過点。</>}
        lead="THINKING 代表・朝倉 徹大。サッカー一筋の少年期から浪人での逆転合格、予備校と個別指導の現場を経て、オンライン塾として届けているいまの想いを綴ります。"
        bgImage="assets/campus-05.png" />
      

      {/* Profile lockup */}
      <section className="founder-profile">
        <div className="founder-profile-inner">
          <div className="founder-photo">
            <div className="founder-photo-frame">
              <img src="assets/founder-portrait.jpg" alt="朝倉 徹大" className="founder-photo-img" />
              <div className="founder-photo-grain" />
            </div>
            <div className="founder-photo-caption">
              <span className="caption-en"><i>Photographed at the Ebisu office, 2025</i></span>
            </div>
          </div>

          <div className="founder-info">
            <span className="eyebrow"><i>Founder &amp; CEO</i></span>
            <h2 className="founder-name">
              <span className="founder-name-en"><i>Tetta Asakura</i></span>
              <span className="founder-name-jp">朝倉 徹大</span>
            </h2>
            <p className="founder-role">
              THINKING 代表 / 教育設計家
            </p>

            <div className="founder-meta">
              <div className="founder-meta-row">
                <span className="meta-label">学歴</span>
                <span className="meta-value">早稲田大学 商学部 卒業</span>
              </div>
              <div className="founder-meta-row">
                <span className="meta-label">指導歴</span>
                <span className="meta-value">9年 / 累計2,000名以上</span>
              </div>
              <div className="founder-meta-row">
                <span className="meta-label">専門</span>
                <span className="meta-value">受験戦略設計、思考型学習法</span>
              </div>
              <div className="founder-meta-row">
                <span className="meta-label">メディア</span>
                <span className="meta-value">新R25・テレビ実績ほか</span>
              </div>
            </div>

            <div className="founder-quote">
              <span className="founder-quote-mark">“</span>
              <p>
                努力は報われる、の前に。<em>正しい努力</em>だけが、報われる。私はその事実の上に、THINKING を立ち上げました。
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Long-form essay */}
      <section className="founder-essay">
        <div className="founder-essay-inner">
          <span className="eyebrow"><i>Letter from the Founder</i></span>
          <h2 className="founder-essay-title">
            なぜ、THINKING を<em>始めたのか。</em>
          </h2>

          <div className="founder-essay-body">
            <p className="essay-lead">
              秘めた想いのまま、終わってほしくない。夢は「見るもの」ではなく、手を伸ばして<em>実現するもの</em>だと、私は信じています。
            </p>

            <p>
              幼いころからサッカーに明け暮れ、副主将としてチームを支ける日々は、かけがえのない誇りでした。けれど受験の場では、勉強との距離がそのまま結果に表れます。初めての大学受験では、志望先にことごとく不合格。長時間机に向かっても、点数は伸びない——そこで痛感したのは、<em>努力は量だけでは報われず、「正しい努力」だけが報われる</em>という、あまりに残酷で、あまりに正直な事実でした。
            </p>

            <p>
              浪人期は、中学レベルの基礎からやり直すところから始まりました。約10ヶ月後、早稲田大学商学部への逆転合格。戦略を立て直し、学び方そのものを組み替えたからこそ辿り着けたゴールラインだったと、いまなら言えます。
            </p>

            <p>
              大学に入ってからは、個別指導と予備校の現場に立ち続けました。科目の説明は丁寧でも、「どう知識を自分のものにするか」「どう計画を立てるか」「受験という勝負の読み方」まで踏み込んで教えてくれる場所は、驚くほど少ない。だからこそ、間違った努力で消耗する受験生を、あまりにも多く見てきました。
            </p>

            <p>
              在学中から、その後も——私立文系の最前線で、延べ<em>2,000名以上</em>の受験生と向き合うなかで、私が一番大切にしたいのは、画一的な型ではなく、<em>ひとりひとりの志望学部に沿った設計図</em>です。東大・早慶といった最難関への合格実績も増えてきましたが、数字の背後にある「ひとりの物語」を、決して忘れたくありません。
            </p>

            <p>
              2023年11月、合同会社ARCを立ち上げ、オンライン塾「THINKING」として全国の受験生に届ける道を選びました。住んでいる場所で、情報と伴走の質に差がつく——そんな格差を、オンラインの力で少しでも埋めたい。地方にいても、都会と同じ解像度で第一志望に挑める環境を、これからも磨き続けます。
            </p>

            <p>
              だからこそ、私たちは<em>月10名</em>という、あえて小さな枠にこだわります。コーチが日々の進捗と志望学部の戦略を握り切れる人数には限界があるからです。問い合わせをお断りすることもありますが、<em>「数を取って質を落とす」ことだけは、したくない</em>。少数だからこそ、設計の解像度と伴走の密度を、毎年積み上げています。
            </p>

            <p className="essay-pull">
              受験は通過点。<br />
              でも、人生を変えうる通過点。
            </p>

            <p>
              10代後半の1〜2年を、どんな密度で過ごすか。何を信じ、何を捨て、何を手に入れるか。その先の「きっとできる」への手応えこそが、受験を超えたあともあなたを支えると、私は知っています。
            </p>

            <p>
              THINKING は、合格のための塾である前に、<em>夢を実現する力</em>を養う場でありたい。「できたらいいな」を、言い訳にしないでほしい。あなたの挑戦に、本気で伴走します。
            </p>

            <p className="essay-signature">
              THINKING 代表<br />
              <em>朝倉 徹大</em>
            </p>
          </div>
        </div>
      </section>

      {/* Beliefs */}
      <section className="founder-beliefs">
        <div className="founder-beliefs-inner">
          <div className="founder-section-head">
            <span className="eyebrow"><i>Three Beliefs</i></span>
            <h2 className="founder-section-title">
              指導の<em>3つの信念</em>。
            </h2>
          </div>
          <ol className="beliefs-list">
            {beliefs.map((b, i) =>
            <li key={i} className="belief-item">
                <span className="belief-no"><i>{b.no}</i></span>
                <h3 className="belief-title">{b.title}</h3>
                <p className="belief-body">{b.body}</p>
              </li>
            )}
          </ol>
        </div>
      </section>

      {/* Timeline */}
      <section className="founder-timeline">
        <div className="founder-timeline-inner">
          <div className="founder-section-head">
            <span className="eyebrow"><i>Timeline</i></span>
            <h2 className="founder-section-title">
              これまでの<em>歩み</em>。
            </h2>
          </div>
          <ol className="timeline-list">
            {timeline.map((t, i) =>
            <li key={i} className="timeline-item">
                <span className="timeline-year"><i>{t.year}</i></span>
                <span className="timeline-dot" />
                <p className="timeline-event">{t.event}</p>
              </li>
            )}
          </ol>
        </div>
      </section>

      {/* Media */}
      <section className="founder-works">
        <div className="founder-works-inner">
          <div className="founder-section-head left">
            <span className="eyebrow"><i>Media Appearances</i></span>
            <h2 className="founder-section-title small">メディア掲載・出演</h2>
          </div>
          <ul className="media-list">
            {media.map((m, i) =>
            <li key={i} className="media-item">
                <span className="media-year"><i>{m.year}</i></span>
                <div className="media-body">
                  <h3 className="media-outlet">{m.outlet}</h3>
                  <p className="media-topic">{m.topic}</p>
                </div>
              </li>
            )}
          </ul>
        </div>
      </section>

      {/* Closing message */}
      <section className="founder-closing">
        <div className="founder-closing-inner">
          <span className="eyebrow"><i>To You</i></span>
          <h2 className="founder-closing-title">
            最後に、<br />
            これを読んでくださっている<em>あなたへ。</em>
          </h2>
          <div className="founder-closing-body">
            <p>
              受験は孤独です。誰も代わりに勉強してはくれません。<br />
              でも、ひとりで戦う必要はありません。
            </p>
            <p>
              本気で向き合ってくれる伴走者がいれば、<br />
              あなたの可能性は、想像以上に拓けます。
            </p>
            <p>
              まずは、無料相談で、お会いしましょう。<br />
              60分、あなたの話を、聞かせてください。
            </p>
          </div>
          <a href={window.THINKING_LINE_LIFF_URL} target="_blank" rel="noopener noreferrer" className="cta cta-large">
            LINEで無料相談
            <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M5 12h14M13 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      </section>
    </>);

};

window.FounderPage = FounderPage;