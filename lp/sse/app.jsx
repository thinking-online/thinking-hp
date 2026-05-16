/* Smart Study English — main app */
const { useState, useEffect, useRef } = React;

/* =====================================================
   HERO  v3 — Refined, airy, premium
===================================================== */
function Hero() {
  return (
    <header className="hero-r" data-screen-label="01 Hero">
      <div className="hero-r-bg">
        <div className="hero-r-bg-gradient"></div>
        <div className="hero-r-bg-grain"></div>
      </div>

      {/* Header */}
      <div className="hero-r-header wrap">
        <div className="brand-mark">
          <div className="brand-shield">
            <svg viewBox="0 0 60 70" width="44" height="52">
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
        <nav className="hero-r-nav">
          <a href="#why">なぜ読めないか</a>
          <a href="#program">プログラム</a>
          <a href="#voices">体験談</a>
          <a href="#faq">Q&A</a>
        </nav>
      </div>

      {/* Hero body — 2-column with content + photo */}
      <div className="hero-r-body wrap">
        <div className="hero-r-content">
          <div className="hero-r-eyebrow">
            <span className="eb-dot"></span>
            <span>FOR STUDENTS &nbsp;/&nbsp; GUARDIANS</span>
          </div>

          <h1 className="hero-r-title">
            <span className="t-row">33日で、</span>
            <span className="t-row">英語が<span className="t-mark">読める
ように</span>なる。</span>
          </h1>

          <div className="hero-r-flourish">
            <svg viewBox="0 0 520 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="flGrad" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#d8a942" stopOpacity="0" />
                  <stop offset="40%" stopColor="#d8a942" />
                  <stop offset="100%" stopColor="#d8a942" stopOpacity="0" />
                </linearGradient>
              </defs>
              <path d="M 8 14 Q 130 4, 260 12 T 510 14" stroke="url(#flGrad)" strokeWidth="1.6" fill="none" strokeLinecap="round" />
              <circle cx="508" cy="14" r="2" fill="#d8a942" />
              <circle cx="498" cy="8" r="0.8" fill="#d8a942" />
              <circle cx="514" cy="20" r="0.8" fill="#d8a942" />
            </svg>
          </div>

          <p className="hero-r-lead">
            <strong>2,000名</strong>が証明した「読み方」を、<br />
            毎日提出 × 個別フィードバックで身につける<strong>33日間</strong>。
          </p>
        </div>

        <div className="hero-r-photo">
          <div className="hr-photo-frame">
            <img src="assets/hero-student.png" alt="" />
            <div className="hr-photo-fade"></div>
          </div>
        </div>
      </div>

      {/* Stat cards row */}
      <div className="hero-r-cards wrap">
        <div className="hr-card">
          <div className="hr-card-icon">
            <svg viewBox="0 0 28 28" width="20" height="20">
              <path d="M3 24 V 14 H 8 V 24 M 12 24 V 8 H 17 V 24 M 21 24 V 16 H 26 V 24" fill="none" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
              <line x1="2" y1="24" x2="27" y2="24" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
          </div>
          <div className="hr-card-body">
            <span className="hr-card-label">特別プログラム価格</span>
            <div className="hr-card-value">
              <span className="hr-num">33,000</span>
              <span className="hr-unit">円</span>
            </div>
            <span className="hr-card-sub">税込・1日あたり約1,000円</span>
          </div>
        </div>

        <div className="hr-card">
          <div className="hr-card-icon">
            <svg viewBox="0 0 28 28" width="20" height="20">
              <circle cx="10" cy="11" r="3.5" fill="none" stroke="#d8a942" strokeWidth="1.6" />
              <circle cx="20" cy="12" r="2.5" fill="none" stroke="#d8a942" strokeWidth="1.6" />
              <path d="M3 24 C 3 19, 6 16, 10 16 C 14 16, 17 19, 17 24" fill="none" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
              <path d="M17 24 C 17 20, 19 18, 21 18 C 24 18, 26 20, 26 24" fill="none" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
          </div>
          <div className="hr-card-body">
            <span className="hr-card-label">各期 募集上限</span>
            <div className="hr-card-value">
              <span className="hr-num">50</span>
              <span className="hr-unit">名</span>
            </div>
            <span className="hr-card-sub">少人数制で毎日FBします</span>
          </div>
        </div>

        <div className="hr-card">
          <div className="hr-card-icon">
            <svg viewBox="0 0 28 28" width="20" height="20">
              <rect x="3" y="5" width="22" height="20" rx="2" fill="none" stroke="#d8a942" strokeWidth="1.6" />
              <line x1="3" y1="10" x2="25" y2="10" stroke="#d8a942" strokeWidth="1.6" />
              <line x1="9" y1="3" x2="9" y2="7" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
              <line x1="19" y1="3" x2="19" y2="7" stroke="#d8a942" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
          </div>
          <div className="hr-card-body">
            <span className="hr-card-label">次回開講</span>
            <div className="hr-card-value">
              <span className="hr-num medium">2026.06.01</span>
            </div>
            <span className="hr-card-sub">先行枠 受付中</span>
          </div>
        </div>
      </div>

      {/* Gold script line */}
      <div className="hero-r-script">
        <span className="hr-script-rule"></span>
        <div className="hr-script-text">
          読む力が、<span className="hr-script-em">未来を変える。</span>
        </div>
        <span className="hr-script-rule"></span>
      </div>

      {/* CTA */}
      <div className="hero-r-cta">
        <a href="#cta" className="hr-cta-primary">
          <span>33日間集中合宿に申し込む</span>
          <span className="hr-cta-arrow">→</span>
        </a>
        <a href="#" className="hr-cta-line">
          <svg viewBox="0 0 32 32" width="22" height="22">
            <rect x="2" y="2" width="28" height="28" rx="6" fill="#06C755" />
            <text x="16" y="22" textAnchor="middle" fontFamily="Arial Black, sans-serif" fontSize="11" fontWeight="900" fill="white">LINE</text>
          </svg>
          <span>LINEで個別相談する</span>
        </a>
      </div>

      {/* Trust strip */}
      <div className="hero-r-trust wrap">
        <span className="hr-trust-label">FEATURED ON</span>
        <div className="hr-trust-list">
          <div className="hr-trust-item"><span className="hr-trust-tag">TV</span>東京MX「Powered by TV」</div>
          <div className="hr-trust-item"><span className="hr-trust-tag">WEB</span>新R25 単独インタビュー</div>
          <div className="hr-trust-item"><span className="hr-trust-tag">OP</span>法人運営 合同会社ARC</div>
          <div className="hr-trust-item"><span className="hr-trust-tag">★</span>累計 2,000名 / 平均 9.8</div>
        </div>
      </div>
    </header>);
}

window.Hero = Hero;