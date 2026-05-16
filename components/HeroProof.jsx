// HeroProof — social proof strip directly below hero
const HeroProof = () => (
  <section className="hero-proof" aria-labelledby="hero-proof-heading">
    <div className="hero-proof-inner">
      <div className="hero-proof-copy reveal">
        <p id="hero-proof-heading" className="hero-proof-line hero-proof-line-main">
          累計<strong>2000</strong>名以上参加
        </p>
        <p className="hero-proof-line">受講生から高評価！</p>
        <p className="hero-proof-line hero-proof-line-cta">次は、あなたが変わる番。</p>
      </div>

      <figure className="hero-proof-visual reveal">
        <img
          src="assets/hero-proof-2000.png"
          alt="参加者2000名・手書き感想多数の実績"
          width="1024"
          height="682"
          loading="eager"
        />
      </figure>
    </div>
  </section>
);

window.HeroProof = HeroProof;
