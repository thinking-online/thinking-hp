// 4 steps to enrollment + final CTA + footer
const FlowAndCTA = () => {
  const steps = [
    { no: "01", title: "LINEで友だち追加", desc: "「無料相談希望」と一言。約1分。" },
    { no: "02", title: "日程調整・面談予約", desc: "コーチから候補日を返信。希望を選ぶだけ。" },
    { no: "03", title: "60分オンライン面談", desc: "学力・志望・残期間を整理し、その場でロードマップ提示。" },
    { no: "04", title: "納得後に指導開始", desc: "勧誘なし。専属コーチの伴走をご自身のペースで。" },
  ];

  return (
    <>
      <section className="section flow-section" id="flow">
        <div className="section-inner">
          <div className="section-head flow-section-head">
            <span className="eyebrow"><i>4 Steps</i></span>
            <h2 className="section-title flow-section-title">
              <em>LINE登録</em>から指導開始まで
            </h2>
            <p className="section-lead flow-section-lead">
              無料相談の流れはシンプルです。4ステップで完了します。
            </p>
            <div className="ornament"><span className="ornament-mark" /></div>
          </div>

          <ol className="flow-list">
            {steps.map((s, i) => (
              <li key={i} className={`flow-item reveal delay-${i + 1}`}>
                <span className="flow-no">{s.no}</span>
                <div className="flow-body">
                  <h3 className="flow-title">{s.title}</h3>
                  <p className="flow-desc">{s.desc}</p>
                </div>
                <span className="flow-line" />
              </li>
            ))}
          </ol>
        </div>
      </section>

      <section className="section line-cta-section" id="contact">
        <div className="line-cta-photo" aria-hidden="true">
          <img src="assets/consult-hero.png" alt="" />
          <div className="line-cta-veil" />
        </div>

        <div className="line-cta-inner">
          <div className="line-cta-text">
            <span className="line-cta-eyebrow">
              <span className="line-cta-eyebrow-line" />
              <i>Online Consultation</i>
            </span>

            <h2 className="line-cta-title">
              <em>LINE登録</em>で無料面談へ
            </h2>

            <p className="line-cta-lead">
              志望学部までの道筋を、60分のオンライン面談で整理します。
            </p>

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
              <span className="line-cta-button-label">LINEで無料相談</span>
              <svg className="arrow" viewBox="0 0 16 16" fill="none">
                <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
              </svg>
            </a>

            <p className="line-cta-note">
              <span><i>全国オンライン対応</i></span>
              <span className="sep">/</span>
              <span><i>60分・無料</i></span>
              <span className="sep">/</span>
              <span><i>勧誘なし</i></span>
            </p>
          </div>
        </div>
      </section>
    </>
  );
};

window.FlowAndCTA = FlowAndCTA;
