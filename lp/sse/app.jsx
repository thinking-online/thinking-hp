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
          src="assets/hero-reading.png"
          alt=""
          width="576"
          height="1024"
          fetchPriority="high"
        />
      </div>
      <div className="hero-m-overlay hero-m-overlay-top" aria-hidden="true" />
      <div className="hero-m-overlay hero-m-overlay-left" aria-hidden="true" />
      <div className="hero-m-overlay hero-m-overlay-bottom" aria-hidden="true" />

      <div className="hero-m-inner">
        <div className="hero-m-header">
          <p className="hero-m-brand">Smart Study English</p>
          <p className="hero-m-badge" aria-label="累計2000名突破">
            <span className="hero-m-badge-pre">累計</span>
            <span className="hero-m-badge-num">2000</span>
            <span className="hero-m-badge-post">名突破</span>
          </p>
        </div>

        <h1 className="hero-m-vertical-panel" aria-label="左から右にスラスラ、英語が読めるを。">
          <span>左から右にスラスラ</span>
          <span>英語が<em>「読める」</em>を。</span>
        </h1>

        <div className="hero-m-foot">
          <div className="hero-m-foot-copy">
            <p className="hero-m-tagline">45日間で、英語の読み方の根本治療</p>
            <p className="hero-m-subcopy">
              <strong>2,000名</strong>が証明した「読み方」を、<br />
              個別面談付きで身につける<strong>45日間</strong>。
            </p>
          </div>
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
        <a
          href="https://assaaa-blog.com/post_lp/tsakansou/"
          target="_blank"
          rel="noopener noreferrer"
          className="btn-primary hero-m-proof-btn"
        >
          手書き感想を見てみる <span className="arrow">→</span>
        </a>
      </div>
    </section>
  );
}

window.HeroProof = HeroProof;
