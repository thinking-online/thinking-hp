// Global site footer — common to all pages
const SiteFooter = () => {
  return (
    <footer className="site-footer">
      <div className="site-footer-grain" />

      <div className="site-footer-inner">
        {/* Top — final CTA */}
        <div className="footer-cta-block">
          <span className="eyebrow"><i>Get Started</i></span>
          <h2 className="footer-cta-title">
            まずは <em>LINE登録</em>から、<br />
            個別オンライン面談へ。
          </h2>
          <p className="footer-cta-sub">
            志望学部 / 現状 / お悩みをお聞かせください。<br />
            60分のオンライン面談で、合格までの設計図をその場でお渡しします。
          </p>
          <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta footer-cta">
            LINEで無料相談
            <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M5 12h14M13 5l7 7-7 7" />
            </svg>
          </a>
        </div>

        <div className="footer-divider" />

        {/* Sitemap grid */}
        <div className="footer-grid">
          <div className="footer-brand">
            <a href="index.html" className="footer-logo">
              THINKING<i>.</i>
            </a>
            <p className="footer-tag">
              <span><i>Designed for Your Faculty.</i></span>
              私立文系・学部別の、合格設計塾。
            </p>
            <div className="footer-sns" aria-label="公式SNS・チャンネル">
              <a
                href="https://www.instagram.com/king_of_juken/?hl=ja"
                target="_blank"
                rel="noopener noreferrer"
                className="footer-sns-link"
              >
                <span className="footer-sns-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.8" fill="currentColor"/></svg>
                </span>
                <span className="footer-sns-text">
                  <span className="footer-sns-name">Instagram</span>
                  <span className="footer-sns-desc">自社運用「受験の王様」フォロワー8.5万人以上</span>
                </span>
              </a>
              <a
                href="https://www.youtube.com/@tetta-waseda-channel"
                target="_blank"
                rel="noopener noreferrer"
                className="footer-sns-link"
              >
                <span className="footer-sns-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>
                </span>
                <span className="footer-sns-text">
                  <span className="footer-sns-name">YouTube</span>
                  <span className="footer-sns-desc">てった｜私立文系の勝ち方ch</span>
                </span>
              </a>
              <a
                href="https://www.youtube.com/@all-day-thinking"
                target="_blank"
                rel="noopener noreferrer"
                className="footer-sns-link"
              >
                <span className="footer-sns-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>
                </span>
                <span className="footer-sns-text">
                  <span className="footer-sns-name">YouTube</span>
                  <span className="footer-sns-desc">オンライン塾THINKING・合格者対談チャンネル</span>
                </span>
              </a>
            </div>
          </div>

          <div className="footer-col">
            <h4 className="footer-col-title"><i>About</i><span>サービス</span></h4>
            <ul>
              <li><a href="strategy.html">学部別戦略・合格設計</a></li>
              <li><a href="support.html">サポート体制</a></li>
              <li><a href="voice.html">合格者の声</a></li>
              <li><a href="price.html">料金・入塾まで</a></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4 className="footer-col-title"><i>Resource</i><span>情報</span></h4>
            <ul>
              <li><a href="founder.html">代表紹介</a></li>
              <li><a href="faq.html">よくある質問</a></li>
              <li><a href="blog.html">記事一覧</a></li>
              <li><a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer">無料相談予約</a></li>
            </ul>
          </div>

          <div className="footer-col footer-info">
            <h4 className="footer-col-title"><i>Company</i><span>運営</span></h4>
            <dl>
              <dt>運営</dt>
              <dd>合同会社 ARC</dd>
              <dt>会社HP</dt>
              <dd>
                <a href="https://arc-llc.jp/" target="_blank" rel="noopener noreferrer">
                  arc-llc.jp
                </a>
              </dd>
              <dt>所在地</dt>
              <dd>東京都武蔵野市境2-2-23<br />武蔵境ぺぺロッソ3F</dd>
              <dt>お問い合わせ</dt>
              <dd><a href="mailto:llcarc1110@gmail.com">llcarc1110@gmail.com</a></dd>
            </dl>
          </div>
        </div>

        <div className="footer-bottom">
          <span className="footer-copy">© {new Date().getFullYear()} THINKING. All Rights Reserved.</span>
          <ul className="footer-legal">
            <li><a href="#">プライバシーポリシー</a></li>
            <li><a href="#">特定商取引法に基づく表記</a></li>
            <li><a href="#">利用規約</a></li>
          </ul>
          <span className="footer-mark"><i>Designed for Your Faculty.</i></span>
        </div>
      </div>
    </footer>
  );
};

window.SiteFooter = SiteFooter;
