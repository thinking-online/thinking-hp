// Faculty list — grid on PC, swipe carousel on mobile
const Faculties = () => {
  const groups = [
    {
      group: "Group 01",
      tier: "Top Tier",
      title: "早慶",
      sub: "早稲田・慶應義塾",
      faculties: ["法", "政経", "商", "文", "教育", "社会", "国際教養", "SFC（総合政策・環境情報）"],
      accent: "high",
    },
    {
      group: "Group 02",
      tier: "Top Tier",
      title: "上智・ICU",
      sub: "上智大学・国際基督教大学",
      faculties: ["法", "経済", "外国語", "総合人間", "国際教養", "Arts and Sciences", "TEAP対策"],
      accent: "high",
    },
    {
      group: "Group 03",
      tier: "Upper",
      title: "GMARCH",
      sub: "学習院・明治・青山・立教・中央・法政",
      faculties: ["法", "経済", "経営", "商", "文", "国際", "社会", "総合政策"],
      accent: "mid",
    },
    {
      group: "Group 04",
      tier: "Upper",
      title: "関関同立",
      sub: "関西・関学・同志社・立命館",
      faculties: ["法", "経済", "商", "文", "社会", "国際", "政策"],
      accent: "mid",
    },
    {
      group: "Group 05",
      tier: "Women's",
      title: "女子大",
      sub: "津田塾・東京女子・日本女子・聖心・白百合・フェリス・神戸女学院 ほか",
      faculties: ["英文", "国際関係", "心理", "文化", "現代教養", "人間社会", "推薦入試対策"],
      accent: "high",
    },
    {
      group: "Group 06",
      tier: "Mid",
      title: "成成明学獨國武",
      sub: "成蹊・成城・明学・獨協・國學院・武蔵",
      faculties: ["法", "経済", "経営", "文", "国際", "社会", "外国語"],
      accent: "low",
    },
    {
      group: "Group 07",
      tier: "Mid",
      title: "日東駒専・産近甲龍",
      sub: "日大・東洋・駒澤・専修／京産・近大・甲南・龍谷",
      faculties: ["法", "経済", "経営", "商", "文", "国際", "社会"],
      accent: "low",
    },
    {
      group: "Group 08",
      tier: "All Others",
      title: "その他の私立文系",
      sub: "上記以外の私立大学文系学部すべて",
      faculties: ["地方私大", "ミッション系", "芸術系大学", "外大", "推薦・総合型", "社会人受験", "学士編入"],
      accent: "low",
    },
  ];

  const trackRef = React.useRef(null);
  const [activeIdx, setActiveIdx] = React.useState(0);

  const updateActive = React.useCallback(() => {
    const el = trackRef.current;
    if (!el) return;
    const cards = el.querySelectorAll(".faculty-card");
    if (!cards.length) return;
    const left = el.scrollLeft;
    let nearest = 0, dist = Infinity;
    cards.forEach((c, i) => {
      const d = Math.abs(c.offsetLeft - left);
      if (d < dist) { dist = d; nearest = i; }
    });
    setActiveIdx(nearest);
  }, []);

  React.useEffect(() => {
    const el = trackRef.current;
    if (!el) return;
    updateActive();
    el.addEventListener("scroll", updateActive, { passive: true });
    window.addEventListener("resize", updateActive);
    return () => {
      el.removeEventListener("scroll", updateActive);
      window.removeEventListener("resize", updateActive);
    };
  }, [updateActive]);

  const scrollToCard = (idx) => {
    const el = trackRef.current;
    if (!el) return;
    const card = el.querySelectorAll(".faculty-card")[idx];
    if (!card) return;
    el.scrollTo({ left: card.offsetLeft, behavior: "smooth" });
  };

  return (
    <section className="section faculties-section" id="faculties">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Target Universities</i></span>
          <h2 className="section-title">
            私立文系の、<em>あらゆる学部</em>へ。
          </h2>
          <p className="section-lead">
            早慶・上智ICU・GMARCH・関関同立はもちろん、女子大も、その他の私立文系も。<br />
            私たちは、すべての学部の出題傾向と入試構造を徹底的に調べ上げています。<br />
            <span className="lead-hl">合格のために、一人ひとりに専属の個別担当を。</span>
          </p>
          <div className="ornament">
            <span className="ornament-mark" />
          </div>
        </div>

        {/* Campus atmosphere banner — sets the aspiration before the list */}
        <div className="faculties-banner reveal">
          <div className="faculties-banner-img" style={{ backgroundImage: "url('assets/campus-04.png')" }} />
          <div className="faculties-banner-overlay" />
          <div className="faculties-banner-text">
            <span className="faculties-banner-en">First choice. Alma mater.</span>
            <span className="faculties-banner-jp">第一志望を、母校に。</span>
          </div>
        </div>

        <div className="faculties-track" ref={trackRef}>
          {groups.map((g, i) => (
            <article key={i} className={`faculty-card reveal delay-${(i % 3) + 1}`} data-tier={g.accent}>
              <header className="faculty-card-head">
                <span className="faculty-card-no">{g.group}</span>
                <span className="faculty-card-tier">{g.tier}</span>
              </header>
              <div className="faculty-card-body">
                <h3 className="faculty-card-title">
                  <span className="title-main">{g.title}</span>
                  <span className="title-sub">{g.sub}</span>
                </h3>
                <ul className="faculty-card-tags">
                  {g.faculties.map((f, j) => (
                    <li key={j}>{f}</li>
                  ))}
                </ul>
              </div>
              <footer className="faculty-card-foot">
                <span>過去問解析 ✓ 専門コーチ在籍 ✓</span>
              </footer>
            </article>
          ))}
        </div>

        {/* Mobile pagination dots */}
        <div className="faculties-pagination">
          {groups.map((_, i) => (
            <button
              key={i}
              type="button"
              className={`faculty-dot ${i === activeIdx ? "active" : ""}`}
              onClick={() => scrollToCard(i)}
              aria-label={`${i + 1}番目`}
            />
          ))}
        </div>
        <div className="faculties-hint">
          <span className="faculties-hint-arrow">←</span>
          <span>swipe</span>
          <span className="faculties-hint-arrow">→</span>
        </div>

        <p className="faculties-note reveal">
          ※ ここに記載のない大学・学部でも、私立文系であれば対応可能です。お気軽にお問い合わせください。
        </p>
      </div>
    </section>
  );
};

window.Faculties = Faculties;
