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
            <p className="brand-product">Smart Study English</p>
          </div>
        </div>

        <div className="hero-m-copy">
          <h1 className="hero-m-title">
            <span className="hero-m-title-row">45日で、英語が</span>
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

        <div className="hero-m-visual-spacer" aria-hidden="true" />

        <div className="hero-m-actions">
          <a href="#cta" className="hero-m-cta-primary">
            <span>申し込みはコチラ</span>
            <span className="hero-m-cta-arrow" aria-hidden="true">→</span>
          </a>
        </div>
      </div>
    </header>
  );
}

window.Hero = Hero;

/* =====================================================
   HERO PROOF — 2000名実績（ヒーロー直下）
===================================================== */
function HeroProof() {
  return (
    <section className="hero-m-proof" aria-labelledby="hero-m-proof-heading">
      <div className="wrap hero-m-proof-inner">
        <div className="hero-m-proof-copy">
          <p id="hero-m-proof-heading" className="hero-m-proof-line hero-m-proof-line-main">
            累計<strong>2000</strong>名以上参加
          </p>
          <p className="hero-m-proof-line">受講生から高評価！</p>
          <p className="hero-m-proof-line hero-m-proof-line-cta">次は、あなたが変わる番。</p>
        </div>
        <figure className="hero-m-proof-visual">
          <img
            src="assets/hero-proof-2000.png"
            alt="参加者2000名・手書き感想多数の実績"
            width="1024"
            height="682"
            loading="eager"
            decoding="async"
          />
        </figure>
      </div>
    </section>
  );
}

window.HeroProof = HeroProof;
