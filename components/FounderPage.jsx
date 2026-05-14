// Founder page — long-form profile of the代表
const FounderPage = () => {
  const timeline = [
  { year: "1998", event: "東京生まれ。" },
  { year: "2018", event: "早稲田大学 商学部 入学。在学中、予備校勤務をして個別指導・エリアリーダーも務める" },
  { year: "2022", event: "早稲田大学 商学部 卒業。" },
  { year: "2014", event: "「画一的な授業では、ひとりひとりが見えない」と感じ、独立を決意。" },
  { year: "2015", event: "THINKING. 創業。当初の生徒は6名、自宅マンションが教室。" },
  { year: "2018", event: "学部別戦略の体系化を完成。第一志望合格率が50%を超える。" },
  { year: "2020", event: "オンライン化を完全実施。全国・海外からの受講が可能に。" },
  { year: "2023", event: "累計合格者数1,200名を突破。新R25・テレビ番組などメディア取材が増加。" },
  { year: "2025", event: "受講生のべ1,800名。第一志望合格率62%を維持。" }];


  const beliefs = [
  {
    no: "01",
    title: "「教える」のではなく、「考えさせる」。",
    body: "答えを与えるのは簡単です。しかし、それでは試験本番で応用が効きません。私は、生徒が自ら考え、自ら答えにたどり着けるよう、問いを投げかけ続けます。塾名に「THINKING.」と冠したのは、これが理由です。"
  },
  {
    no: "02",
    title: "全員には、教えない。",
    body: "現場に立ち続けてわかったことがあります。「全員に同じ授業」は、誰のためにもなりません。だから私たちは、見られる人数しか受け入れません。月10名、これが私たちの限界であり、矜持です。"
  },
  {
    no: "03",
    title: "数字より、ひとりの物語を。",
    body: "合格率や偏差値の伸びも大切です。しかし、それ以上に大切なのは、ひとりの受験生が、人生の重要な一年をどう過ごすか。受験は通過点ですが、その過程で得る自走力は一生ものです。私はそこに最も価値を置いています。"
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
        lead="THINKING. 代表 — 朝倉 徹大。私立文系の指導歴9年。早稲田・慶應への合格実績は毎年途切れなく続いています。いま考えていることを、お話しさせてください。"
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
              THINKING. 代表 / 教育設計家
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
                「全員には教えない」と言うと、<br />
                よく驚かれます。<br />
                でもそれは、私たちが本気だ、ということです。
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
            なぜ、THINKING. を<em>始めたのか。</em>
          </h2>

          <div className="founder-essay-body">
            <p className="essay-lead">
              新卒で大手予備校に入った2008年。私は、自分が想像していた仕事と、現実のギャップに、ずっと悩んでいました。
            </p>

            <p>
              入社初日、上司に言われました。「教師の仕事は、効率よく授業を回すこと。一人ひとりに時間をかけるな」と。
            </p>

            <p>
              200名の生徒を前に、同じ板書、同じ問題、同じ解説。授業のあと、わからない顔をしている生徒に声をかけたくても、次のクラスが始まる。質問に来る生徒は限られた数名だけで、本当に助けが必要な、声を上げられない生徒には、結局なにも届かない。
            </p>

            <p>
              そんな日々を6年続けて、わかったことがあります。<em>「全員に同じ授業」は、誰のためにもなっていない</em>、ということ。学力上位の生徒は退屈し、下位の生徒はついていけず、真ん中の生徒だけがなんとかついていく。これが「効率のいい」授業の正体でした。
            </p>

            <p>
              2014年、私は独立を決意しました。お金もコネもありませんでした。最初の生徒は、知人の紹介で集まった6名。教室は、自宅マンションの一室。
            </p>

            <p>
              でも、ひとつだけ決めていたことがあります。<em>「絶対に、見られる人数しか取らない」</em>。これだけは、どれだけ経営が苦しくても、譲りませんでした。
            </p>

            <p>
              理由は、シンプルです。一人ひとりに本気で向き合うなら、人数には限界があるから。コーチひとりが日々の進捗まで把握できる人数は、せいぜい7〜8名。学部責任者が戦略を更新できる人数も、月20〜30名が限界。だから、月10名。これが、私たちが本気でやれる、唯一の規模です。
            </p>

            <p>
              「もっと拡大しないんですか」と、よく聞かれます。正直、申し訳ない気持ちもあります。問い合わせをくださって、お断りすることになる方も、年間100名以上いらっしゃいますから。
            </p>

            <p>
              それでも、私たちは規模を追わない選択をしました。<em>「数を取って質を落とす」のは、創業の理念に背くから</em>です。少数だからこそ、第一志望合格率62%という、業界平均の4倍以上の数字を、毎年維持できています。
            </p>

            <p>
              受験は、人生の通過点です。でも、人生を変えうる通過点でもあります。10代後半の1〜2年を、どんな密度で過ごすか。何を考え、何を諦めず、何を掴むか。それは、その後の人生のあり方を、確実に変えていきます。
            </p>

            <p>
              だから、私は、ひとりひとりに、本気で向き合います。<br />
              これが、THINKING. を始めた理由であり、いまも続けている理由です。
            </p>

            <p className="essay-signature">
              THINKING. 代表<br />
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
              30分、あなたの話を、聞かせてください。
            </p>
          </div>
          <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta cta-large">
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