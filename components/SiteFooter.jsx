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
            <div className="footer-social">
              <a href="#" aria-label="X (Twitter)">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
              </a>
              <a href="#" aria-label="YouTube">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>
              </a>
              <a href="#" aria-label="Instagram">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.8" fill="currentColor"/></svg>
              </a>
              <a href="#" aria-label="LINE">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.4 4.6C17.5 2.6 14.9 1.5 12 1.5c-5.8 0-10.5 4-10.5 9 0 4.4 3.6 8.1 8.5 8.9.3 0 .5.1.6.4.1.2.1.5 0 .7l-.3 1.2c-.1.3.2.6.5.5 1.4-.5 6.6-3.6 8.6-6 1.6-2.1 2.1-3.6 2.1-5.7 0-2.1-.8-4.2-2.1-5.9zM8 13.6H5.4c-.2 0-.4-.2-.4-.4V8.7c0-.2.2-.4.4-.4s.4.2.4.4v4.1H8c.2 0 .4.2.4.4s-.2.4-.4.4zm1.6-.4c0 .2-.2.4-.4.4s-.4-.2-.4-.4V8.7c0-.2.2-.4.4-.4s.4.2.4.4zm5.5 0c0 .2-.1.3-.3.4h-.1c-.1 0-.2-.1-.3-.2l-2.4-3.2v3c0 .2-.2.4-.4.4s-.4-.2-.4-.4V8.7c0-.2.1-.3.3-.4h.1c.1 0 .2.1.3.2l2.4 3.2v-3c0-.2.2-.4.4-.4s.4.2.4.4zm3.4-2.6c.2 0 .4.2.4.4s-.2.4-.4.4h-1.7v1.4h1.7c.2 0 .4.2.4.4s-.2.4-.4.4h-2.1c-.2 0-.4-.2-.4-.4V8.7c0-.2.2-.4.4-.4h2.1c.2 0 .4.2.4.4s-.2.4-.4.4h-1.7v1.4z"/></svg>
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
