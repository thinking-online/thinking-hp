// 5 mechanisms / method section
const Method = () => {
  const items = [
    {
      no: "01",
      en: "Strategy",
      title: "大学・学部別の完全カスタム戦略",
      desc: "受験戦略は人によってまるで違う。志望学部・現状学力・残り期間から、合格点までの最短ルートを個別に設計します。",
      large: true,
    },
    {
      no: "02",
      en: "Curriculum",
      title: "週次の学習計画/PDCA",
      desc: "1週間単位の精緻な計画と、月次の到達度レビュー。やるべきことが、いつも明確に。",
    },
    {
      no: "03",
      en: "Roadmap",
      title: "合格までの完全ロードマップ",
      desc: "全範囲をいつ終え、いつ過去問に入るか。受験本番から逆算した、揺らがない設計図。",
    },
    {
      no: "04",
      en: "Quality",
      title: "24時間質問システム",
      desc: "わからない、を24時間以内に解消。チャットで講師に直接質問でき、学習が止まらない。",
    },
    {
      no: "05",
      en: "Mindset",
      title: "週次面談で、迷う暇を与えない",
      desc: "毎週1on1の面談で進捗・悩み・モチベーションを丁寧に管理。一人で抱え込ませない。",
    },
    {
      no: "06",
      en: "Verbalize",
      title: "わかる→解ける、『言語化特訓』",
      desc: "説明できない理解は、理解じゃない。「なぜその答えか」を言葉にする訓練で、理解の解像度を一段引き上げる。",
      link: { href: "/support#thinking-method", en: "Support System", label: "THINKING Method とは" },
    },
  ];

  return (
    <section className="section method-section" id="method">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Six Mechanisms</i></span>
          <h2 className="section-title">
            合格を、<em>設計</em>する6つの仕組み。
          </h2>
          <div className="ornament"><span className="ornament-mark" /></div>
        </div>

        <div className="method-grid">
          {items.map((m, i) => (
            <article
              key={i}
              className={`method-card reveal delay-${(i % 4) + 1} ${m.large ? "method-card-lg" : ""}`}
            >
              <div className="method-card-no">
                <span className="no">{m.no}</span>
                <span className="en">{m.en}</span>
              </div>
              <h3 className="method-card-title">{m.title}</h3>
              <p className="method-card-desc">{m.desc}</p>
              {m.link && (
                <SectionLink href={m.link.href} en={m.link.en} compact className="method-card-link">
                  {m.link.label}
                </SectionLink>
              )}
              <div className="method-card-line" />
            </article>
          ))}
        </div>

        <Stats />
      </div>
    </section>
  );
};

const Stats = () => {
  const stats = [
    { num: "2000+", label: "Coached Students", jp: "個別指導実績（人）" },
    { num: "30+", label: "Student Voices", jp: "合格者の声" },
    { num: "24h", label: "Question Answers", jp: "いつでも質問対応" },
    { num: "1:1", label: "Faculty Coaching", jp: "学部別個別指導" },
  ];

  const ref = React.useRef(null);
  const [shown, setShown] = React.useState(false);
  React.useEffect(() => {
    const io = new IntersectionObserver(
      ([e]) => { if (e.isIntersecting) setShown(true); },
      { threshold: 0.3 }
    );
    if (ref.current) io.observe(ref.current);
    return () => io.disconnect();
  }, []);

  return (
    <div className={`stats-row ${shown ? "in" : ""}`} ref={ref}>
      {stats.map((s, i) => (
        <React.Fragment key={i}>
          <div className="stat-block" style={{ transitionDelay: `${i * 120}ms` }}>
            <span className="stat-num-big">{s.num}</span>
            <span className="stat-label-en">{s.label}</span>
            <span className="stat-label-jp">{s.jp}</span>
          </div>
          {i < stats.length - 1 && <span className="stat-divider" />}
        </React.Fragment>
      ))}
    </div>
  );
};

window.Method = Method;
