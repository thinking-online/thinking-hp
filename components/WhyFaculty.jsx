// "Why faculty-specific?" section — comparison cards with arrow
const WhyFaculty = () => {
  return (
    <section className="section why-section" id="why">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Why Faculty-Specific</i></span>
          <h2 className="section-title">
            なぜ、<em>"学部別"</em>なのか。
          </h2>
          <p className="section-lead">
            学部が違えば、入試問題の本質も違う。<br />
            だからこそ、汎用の対策では、合格は遠ざかる。
          </p>
          <div className="ornament">
            <span className="ornament-mark" />
          </div>
        </div>

        <div className="why-compare reveal">
          <div className="why-card why-card-old">
            <div className="why-card-label">
              <span className="why-card-tag">Conventional</span>
              <span className="why-card-tag-jp">従来の対策</span>
            </div>
            <h3 className="why-card-title">
              「網羅型」対策
            </h3>
            <p className="why-card-desc">
              全学部・全大学の幅広い問題を浅く広く演習する。<br />
              結果、志望学部の本当の出題傾向には踏み込めない。
            </p>
            <ul className="why-card-points">
              <li>共通テストの延長線上の指導</li>
              <li>学部固有の出題癖を捉えきれない</li>
              <li>合格まで遠回りになりやすい</li>
            </ul>
          </div>

          <div className="why-arrow">
            <svg viewBox="0 0 80 24" fill="none">
              <path d="M2 12h70M62 4l10 8-10 8" stroke="currentColor" strokeWidth="1.2" />
            </svg>
            <span className="why-arrow-label">VS</span>
          </div>

          <div className="why-card why-card-new">
            <div className="why-card-label">
              <span className="why-card-tag accent">THINKING</span>
              <span className="why-card-tag-jp">学部別設計</span>
            </div>
            <h3 className="why-card-title">
              <em>「学部別」</em>戦略型
            </h3>
            <p className="why-card-desc">
              志望学部ごとに、出題傾向・配点・合格点を逆算。<br />
              一人ひとり、別々の合格設計図を作り上げる。
            </p>
            <ul className="why-card-points">
              <li>過去10年分の学部別問題を解析</li>
              <li>合格点から逆算した学習計画</li>
              <li>得点源／捨て問の切り分けを最適化</li>
            </ul>
            <div className="why-card-shine" />
          </div>
        </div>

        <div className="why-quote reveal delay-2">
          <span className="quote-mark">"</span>
          <p>
            THINKING は、「学習量」よりも「設計の質」を信じます。<br />
            <span className="dim">志望学部に最短距離で届く道筋は、必ず存在する。</span>
          </p>
          <span className="quote-mark right">"</span>
        </div>

        <SectionLink href="/strategy" en="Faculty Strategy" className="reveal delay-3">
          学部別戦略・合格設計を見る
        </SectionLink>
      </div>
    </section>
  );
};

window.WhyFaculty = WhyFaculty;
