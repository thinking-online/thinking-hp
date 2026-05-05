// 5 mechanisms section + animated counters
const Mechanisms = () => {
  const items = [
    {
      no: "01",
      en: "Faculty-Specific Strategy",
      title: "大学・学部別の完全カスタム戦略",
      desc: "志望学部の過去10年分の出題を解析し、得点源・配点・必要点数まで逆算。あなただけの「合格設計図」を、初回面談から作成します。",
      large: true,
    },
    {
      no: "02",
      en: "Weekly 1:1 Coaching",
      title: "週次・1対1の学習面談",
      desc: "毎週、専属コーチと1対1で進捗確認・軌道修正。机に向かう前に「今週何をやるか」が完全に明確に。",
    },
    {
      no: "03",
      en: "Pass-Date Roadmap",
      title: "合格までの完全ロードマップ",
      desc: "週単位・月単位で、合格までやるべき学習を全て可視化。日々の積み上げが、確実に合格に繋がる安心感を。",
    },
    {
      no: "04",
      en: "24h Q&A System",
      title: "24時間質問システム",
      desc: "わからない問題は、いつでも質問。専属コーチが24時間以内に音声・テキストで回答します。",
    },
    {
      no: "05",
      en: "Faculty-Specific Faculty",
      title: "現役合格者を含む、合格実績講師",
      desc: "すべての講師が、担当学部に過去合格した実績者。学部ごとの「肌感覚」を持つ指導者から学べる。",
    },
  ];

  // counter
  const stats = [
    { num: 3, suffix: "Y+", label: "Years of Practice", sub: "創立3年目の実績" },
    { num: 30, suffix: "+", label: "Student Voices", sub: "受講生の声" },
    { num: 24, suffix: "h", label: "Question Answers", sub: "いつでも質問対応" },
    { num: 1, suffix: "1", label: "Faculty Coaching", sub: "学部専属指導", colon: true },
  ];

  return (
    <section className="section mechanisms-section" id="method">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Our Method</i></span>
          <h2 className="section-title">
            合格を、<em>設計する</em> 5つの仕組み。
          </h2>
          <div className="ornament">
            <span className="ornament-mark" />
          </div>
        </div>

        <div className="mech-grid">
          {items.map((it, i) => (
            <article
              key={i}
              className={`mech-card reveal delay-${(i % 3) + 1} ${it.large ? "is-large" : ""}`}
            >
              <div className="mech-card-no">
                <span className="num">{it.no}</span>
                <span className="line" />
              </div>
              <div className="mech-card-body">
                <span className="mech-en"><i>{it.en}</i></span>
                <h3 className="mech-title">{it.title}</h3>
                <p className="mech-desc">{it.desc}</p>
              </div>
            </article>
          ))}
        </div>

        <div className="mech-stats">
          {stats.map((s, i) => (
            <div key={i} className="mech-stat reveal" data-delay={i}>
              <span className="mech-stat-num">
                {s.colon ? (
                  <>1<i>:</i>1</>
                ) : (
                  <>
                    <Counter target={s.num} />
                    <i>{s.suffix}</i>
                  </>
                )}
              </span>
              <span className="mech-stat-label"><i>{s.label}</i></span>
              <span className="mech-stat-sub">{s.sub}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

const Counter = ({ target }) => {
  const ref = React.useRef(null);
  const [val, setVal] = React.useState(0);
  React.useEffect(() => {
    const el = ref.current;
    if (!el) return;
    let started = false;
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting && !started) {
          started = true;
          const dur = 1400;
          const t0 = performance.now();
          const tick = (t) => {
            const p = Math.min((t - t0) / dur, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            setVal(Math.round(target * eased));
            if (p < 1) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
        }
      });
    }, { threshold: 0.5 });
    obs.observe(el);
    return () => obs.disconnect();
  }, [target]);
  return <span ref={ref}>{val}</span>;
};

window.Mechanisms = Mechanisms;
