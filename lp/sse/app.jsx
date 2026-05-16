/* Smart Study English — main app */
const { useState, useEffect, useRef } = React;

/* =====================================================
   HERO — Full-bleed photo + overlay (HP top style)
===================================================== */
function Hero() {
  return (
    <header className="hero-m" data-screen-label="01 Hero">
      <div className="hero-m-bg" aria-hidden="true">
        <img
          className="hero-m-bg-img"
          src="assets/hero-student.png"
          alt=""
          width="576"
          height="1024"
          fetchPriority="high"
        />
      </div>
      <div className="hero-m-scrim hero-m-scrim-top" aria-hidden="true" />
      <div className="hero-m-scrim hero-m-scrim-left" aria-hidden="true" />
      <div className="hero-m-scrim hero-m-scrim-bottom" aria-hidden="true" />

      <div className="hero-m-inner wrap">
        <div className="hero-m-header">
          <div className="brand-mark">
            <div className="brand-shield">
              <svg viewBox="0 0 60 70" width="40" height="46" aria-hidden="true">
                <defs>
                  <linearGradient id="shieldGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#0d1a3d" />
                    <stop offset="100%" stopColor="#060c1c" />
                  </linearGradient>
                </defs>
                <path d="M30 2 L 56 10 L 56 36 C 56 52, 44 64, 30 68 C 16 64, 4 52, 4 36 L 4 10 Z" fill="url(#shieldGrad)" stroke="#d8a942" strokeWidth="1" />
                <text x="30" y="44" textAnchor="middle" fontFamily="Cormorant Garamond" fontSize="32" fontWeight="700" fill="#e9c267">T</text>
                <circle cx="30" cy="13" r="1.6" fill="#e9c267" />
              </svg>
            </div>
            <div className="brand-name-stack">
              <div className="brand-corp">合同会社ARC <span className="sep">/</span> THINKING</div>
              <div className="brand-product">Smart Study English</div>
            </div>
          </div>
        </div>

        <div className="hero-m-copy">
          <h1 className="hero-m-title">
            <span className="hero-m-title-row">
              <span className="hero-m-day">45</span>日で、英語が
            </span>
            <span className="hero-m-title-row">読めるようになる。</span>
          </h1>

          <div className="hero-m-rule" aria-hidden="true">
            <svg viewBox="0 0 320 20" preserveAspectRatio="none">
              <defs>
                <linearGradient id="heroRuleGrad" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#d8a942" stopOpacity="0" />
                  <stop offset="35%" stopColor="#d8a942" />
                  <stop offset="100%" stopColor="#d8a942" stopOpacity="0.2" />
                </linearGradient>
              </defs>
              <path d="M 4 12 Q 80 4, 160 11 T 316 12" stroke="url(#heroRuleGrad)" strokeWidth="1.4" fill="none" strokeLinecap="round" />
              <circle cx="312" cy="12" r="1.8" fill="#d8a942" />
            </svg>
          </div>

          <p className="hero-m-lead">
            <strong>2,000名</strong>が証明した「読み方」を、<br />
            個別面談付きで身につける<strong>45日間</strong>。
          </p>
        </div>

        <div className="hero-m-cards" role="list">
          <article className="hero-m-card" role="listitem">
            <div className="hero-m-card-icon" aria-hidden="true">
              <svg viewBox="0 0 28 28" width="18" height="18">
                <path d="M3 24 V 14 H 8 V 24 M 12 24 V 8 H 17 V 24 M 21 24 V 16 H 26 V 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
                <line x1="2" y1="24" x2="27" y2="24" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
              </svg>
            </div>
            <div className="hero-m-card-body">
              <span className="hero-m-card-label">モニター価格</span>
              <span className="hero-m-card-value"><span className="num">39,800</span><span className="unit">円〜</span></span>
              <span className="hero-m-card-sub">税込43,780円〜</span>
            </div>
          </article>

          <article className="hero-m-card" role="listitem">
            <div className="hero-m-card-icon" aria-hidden="true">
              <svg viewBox="0 0 28 28" width="18" height="18">
                <circle cx="10" cy="11" r="3.5" fill="none" stroke="currentColor" strokeWidth="1.6" />
                <circle cx="20" cy="12" r="2.5" fill="none" stroke="currentColor" strokeWidth="1.6" />
                <path d="M3 24 C 3 19, 6 16, 10 16 C 14 16, 17 19, 17 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
                <path d="M17 24 C 17 20, 19 18, 21 18 C 24 18, 26 20, 26 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
              </svg>
            </div>
            <div className="hero-m-card-body">
              <span className="hero-m-card-label">先着</span>
              <span className="hero-m-card-value"><span className="num">30</span><span className="unit">名</span></span>
              <span className="hero-m-card-sub">限定募集</span>
            </div>
          </article>

          <article className="hero-m-card" role="listitem">
            <div className="hero-m-card-icon" aria-hidden="true">
              <svg viewBox="0 0 28 28" width="18" height="18">
                <rect x="3" y="5" width="22" height="20" rx="2" fill="none" stroke="currentColor" strokeWidth="1.6" />
                <line x1="3" y1="10" x2="25" y2="10" stroke="currentColor" strokeWidth="1.6" />
                <line x1="9" y1="3" x2="9" y2="7" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
                <line x1="19" y1="3" x2="19" y2="7" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
              </svg>
            </div>
            <div className="hero-m-card-body">
              <span className="hero-m-card-label">2026年</span>
              <span className="hero-m-card-value hero-m-card-value--date"><span className="num">5/31</span></span>
              <span className="hero-m-card-sub">まで</span>
            </div>
          </article>
        </div>

        <p className="hero-m-script" aria-label="読む力が、未来を変える。">
          <span className="hero-m-script-deco" aria-hidden="true" />
          <span className="hero-m-script-line">読む力が、</span>
          <span className="hero-m-script-line hero-m-script-em">未来を変える。</span>
        </p>

        <div className="hero-m-actions">
          <a href="#cta" className="hero-m-cta-primary">
            <span>モニター生として参加する</span>
            <span className="hero-m-cta-arrow" aria-hidden="true">→</span>
          </a>
          <a href={window.THINKING_LINE_LIFF_URL || "#"} target="_blank" rel="noopener noreferrer" className="hero-m-cta-line">
            <svg viewBox="0 0 32 32" width="22" height="22" aria-hidden="true">
              <rect x="2" y="2" width="28" height="28" rx="6" fill="#06C755" />
              <text x="16" y="22" textAnchor="middle" fontFamily="Arial Black, sans-serif" fontSize="11" fontWeight="900" fill="white">LINE</text>
            </svg>
            <span>LINEで個別相談する</span>
          </a>
        </div>

      </div>
    </header>
  );
}

window.Hero = Hero;
