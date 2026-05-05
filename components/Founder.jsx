// Founder section — 朝倉 徹大
const Founder = () => {
  return (
    <section className="section founder-section" id="founder">
      <div className="section-inner">
        <div className="section-head">
          <span className="eyebrow"><i>Founder &amp; Head Coach</i></span>
          <h2 className="section-title">
            <em>THINKING</em> 創設者
          </h2>
          <div className="ornament"><span className="ornament-mark" /></div>
        </div>

        <div className="founder-layout">
          <div className="founder-photo reveal">
            <div className="founder-photo-frame">
              <img src="assets/founder-asakura.jpg" alt="朝倉 徹大" />
              <div className="founder-photo-glow" />
            </div>
            <div className="founder-photo-deco" />
            <div className="founder-photo-caption">
              <span className="mono">— Tetta Asakura, 2026</span>
            </div>
          </div>

          <div className="founder-text reveal delay-2">
            <p className="founder-en"><i>Tetta Asakura — Founder of THINKING.</i></p>
            <p className="founder-name-jp">朝倉 徹大</p>
            <p className="founder-role">THINKING. 創設者 / 代表 / ヘッドコーチ</p>

            <div className="founder-bio">
              <p>
                早稲田大学商学部卒。大手予備校・個別指導塾で
                <span className="hl">10年以上</span>
                指導の最前線に立ち、
                延べ<span className="hl">2000名以上</span>の私立文系受験生と向き合ってきた。
              </p>
              <p>
                その過程で痛感したのは、 「同じ大学でも、学部が違えば、合格までの道は別物」という事実。
                <br />
                "全員に同じ授業を受けさせる" 受験指導の限界を超えるために、
                <span className="hl">学部別 × 完全個別</span>に振り切った塾——
                THINKING. を創設した。
              </p>
              <p className="founder-quote">
                「学習量で殴る指導は、もう終わりにしたい。<br />
                一人ひとりに合った設計図を、自分の手で渡したい。」
              </p>
            </div>

            <ul className="founder-points">
              <li>
                <span className="bullet" />
                <span>早稲田大学 商学部 卒業</span>
              </li>
              <li>
                <span className="bullet" />
                <span>大手予備校／個別指導塾で10年以上の指導歴</span>
              </li>
              <li>
                <span className="bullet" />
                <span>累計2000名以上の私立文系受験生を指導</span>
              </li>
              <li>
                <span className="bullet" />
                <span>第一志望合格率 82%（直近3年平均）</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>);

};

window.Founder = Founder;