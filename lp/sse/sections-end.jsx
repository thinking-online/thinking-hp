/* Smart Study English — voices, media, guarantee, FAQ, price, final CTA */

/* =====================================================
   SECTION: VOICES — 手書き感想ギャラリー
===================================================== */
function VoicesSection() {
  const voices = [
    "assets/testimonial-01.png",
    "assets/testimonial-02.png",
    "assets/testimonial-03.png",
    "assets/testimonial-04.png",
    "assets/testimonial-05.png",
    "assets/testimonial-06.png",
    "assets/testimonial-07.png",
    "assets/testimonial-08.png",
    "assets/testimonial-09.png",
    "assets/testimonial-10.png",
    "assets/testimonial-11.png",
    "assets/testimonial-12.png",
  ];

  const LOOP_SETS = 3;
  const carouselRef = React.useRef(null);
  const jumpingRef = React.useRef(false);
  const loopItems = React.useMemo(
    () => Array.from({ length: LOOP_SETS }, () => voices).flat(),
    []
  );

  const syncLoopPosition = React.useCallback(() => {
    const el = carouselRef.current;
    if (!el || jumpingRef.current) return;

    const setWidth = el.scrollWidth / LOOP_SETS;
    if (setWidth <= 0) return;

    if (el.scrollLeft < setWidth * 0.5) {
      jumpingRef.current = true;
      el.scrollLeft += setWidth;
      jumpingRef.current = false;
    } else if (el.scrollLeft >= setWidth * 2.5) {
      jumpingRef.current = true;
      el.scrollLeft -= setWidth;
      jumpingRef.current = false;
    }
  }, []);

  React.useEffect(() => {
    const el = carouselRef.current;
    if (!el) return undefined;

    const jumpToMiddle = () => {
      const setWidth = el.scrollWidth / LOOP_SETS;
      if (setWidth > 0) {
        el.scrollLeft = setWidth;
      }
    };

    jumpToMiddle();
    const t = window.setTimeout(jumpToMiddle, 120);
    const t2 = window.setTimeout(jumpToMiddle, 600);

    const onScroll = () => syncLoopPosition();
    el.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", jumpToMiddle);

    return () => {
      window.clearTimeout(t);
      window.clearTimeout(t2);
      el.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", jumpToMiddle);
    };
  }, [syncLoopPosition]);

  return (
    <section id="voices" className="voices-section theme-paper" data-screen-label="08 Voices">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">07</div>
          <div>
            <span className="eyebrow">REAL VOICES</span>
            <h2 className="section-title">手書き感想1000枚超が、<br /><em>すべてを語る。</em></h2>
            <p className="section-lead">
              プログラムを終えた生徒たちが、自らの手で書いてくれた感想です。<br />
              スマホで打てる時代に、わざわざ手書きで書いてくれる。それが、本物の変化の証明です。
            </p>
          </div>
        </div>

        <div className="voices-strip">
          <p className="voices-swipe-hint" aria-hidden="true">← スワイプで他の感想を見る →</p>
          <div
            className="voices-carousel"
            ref={carouselRef}
            role="region"
            aria-label="手書き感想ギャラリー"
            tabIndex={0}
          >
            <div className="voices-track">
              {loopItems.map((src, i) => (
                <article key={`${src}-${i}`} className="voice-card voice-card--image">
                  <img src={src} alt="受講生の手書き感想" loading="lazy" decoding="async" />
                </article>
              ))}
            </div>
          </div>
        </div>

        <div className="voices-stats">
          <p className="voices-stats-bar">
            <span className="vsb-item"><strong>2,000+</strong> 累計参加者</span>
            <span className="vsb-sep" aria-hidden="true">·</span>
            <span className="vsb-item"><strong>手書き感想1000枚超</strong></span>
            <span className="vsb-sep" aria-hidden="true">·</span>
            <span className="vsb-item"><strong>★9.8</strong>/10 平均評価</span>
          </p>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: MEDIA & TRUST
===================================================== */
function MediaSection() {
  return (
    <section className="media-section" data-screen-label="09 Media">
      <div className="wrap">
        <div className="media-grid">
          <div className="media-card">
            <div className="media-card-img">
              <img src="assets/media-mx.png" alt="東京MX Powered by TV 元気ジャパン" loading="lazy" />
            </div>
            <span className="media-tag">TV BROADCAST</span>
            <h3>東京MX「Powered by TV」で紹介</h3>
            <p>偏差値40台からの逆転を可能にする独自の英語メソッドと、生徒一人ひとりに寄り添う個別コーチング体制が評価され、番組で紹介されました。</p>
            <a href="https://powered-by-tv.com/2023/08/12/powernews11/" target="_blank" rel="noopener" className="media-link">記事を読む →</a>
          </div>
          <div className="media-card">
            <span className="media-tag">WEB MEDIA</span>
            <h3>新R25 単独インタビュー掲載</h3>
            <p>徹底的な数字分析に基づいた戦略と、再現性を担保する指導メソッドが評価され、代表・朝倉が単独インタビューを受けました。</p>
          </div>
          <div className="media-card">
            <span className="media-tag">OPERATION</span>
            <h3>法人運営 / 合同会社ARC</h3>
            <p>個人の教材販売ではなく、法人が運営し社会的責任を持って提供する正規プログラム。代表 朝倉 徹大が責任を持って指導します。</p>
          </div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: 代表メッセージ
===================================================== */
function MessageSection() {
  return (
    <section className="message-section theme-deep-warm" data-screen-label="10 Message">
      <div className="wrap-narrow">
        <div className="section-head">
          <div className="section-num">15</div>
          <div>
            <span className="eyebrow">MESSAGE FROM CEO</span>
            <h2 className="section-title">なぜ、このプログラムを<br /><em>作ったのか。</em></h2>
          </div>
        </div>

        <div className="message-card">
          <div className="message-intro">
            <figure className="message-photo">
              <img
                src="assets/founder-portrait.png"
                alt="朝倉 徹大 — THINKING 代表"
                width="400"
                height="520"
                loading="lazy"
                decoding="async"
              />
            </figure>
            <div className="message-intro-copy">
              <p className="message-profile-label">代表メッセージ</p>
              <h3 className="message-profile-name">朝倉 徹大</h3>
              <p className="message-profile-role">
                合同会社ARC 代表社員 / 難関私大専門オンライン塾 THINKING 代表
              </p>
            </div>
          </div>

          <div className="message-content">
            <div className="message-body">
              <p className="message-lead">
                なぜ、これだけ時間をかけて勉強しても、英語が伸びない高校生が、これほど多いのか。
                それは、能力不足でも、努力不足でもありません。
                ただ、「正しい読み方」を知らないまま、我流で走り続けているからです。
              </p>
              <p>
                スポーツと同じく、間違ったフォームで何千回素振りをしても、悪い癖がつくだけで上達はしません。
                それどころか、自信を失い、学ぶこと自体が嫌いになってしまう。これほど残酷なことはありません。
              </p>
              <p>
                だからこそ私たちは、「知識」を教える前に、「知識を使いこなすための<em>型</em>」を徹底的にインストールします。
                どこも教えてくれなかった「脳の使い方」を根本から解決する。
              </p>
              <p className="message-strong">
                お子様に必要なのは、一時的な詰め込みではない。
                未来を自らの手で切り拓くための、本質的な解決策です。
              </p>
            </div>

            <div className="message-sign">
              <div className="sign-line" aria-hidden="true" />
              <div className="sign-name">
                <span className="sign-role">難関私大専門オンライン塾 THINKING 代表</span>
                <span className="sign-en">Tetta Asakura</span>
                <span className="sign-jp">朝倉 徹大</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: 全額返金保証
===================================================== */
function GuaranteeSection() {
  return (
    <section className="guarantee-section theme-paper" data-screen-label="11 Guarantee">
      <div className="wrap">
        <div className="guarantee-card">
          <div className="seal">
            <svg viewBox="0 0 120 120" width="120" height="120">
              <circle cx="60" cy="60" r="56" fill="none" stroke="#e9c267" strokeWidth="1.2" strokeDasharray="2 3" />
              <circle cx="60" cy="60" r="48" fill="none" stroke="#e9c267" strokeWidth="0.8" />
              <text x="60" y="48" textAnchor="middle" fontFamily="Cormorant Garamond" fontSize="11" fill="#e9c267" letterSpacing="2">FULL REFUND</text>
              <text x="60" y="74" textAnchor="middle" fontFamily="Cormorant Garamond" fontSize="32" fontWeight="600" fill="#f5d98a">45</text>
              <text x="60" y="92" textAnchor="middle" fontFamily="Cormorant Garamond" fontSize="11" fill="#e9c267" letterSpacing="2">DAYS</text>
            </svg>
          </div>

          <div className="guarantee-body">
            <span className="eyebrow">FULL REFUND GUARANTEE</span>
            <h2>全額返金保証 — リスクは私たちが引き受ける。</h2>
            <p>
              45日間のカリキュラムを全てやり遂げ、それでも変化を実感できなかった場合、
              頂いた参加費を <strong>全額返金</strong> いたします。
              金銭的なリスクは、親御様には一切負わせません。
            </p>
            <ul className="guarantee-conds">
              <li>✓ 45日間の課題・提出をすべて指定時間内に実施</li>
              <li>✓ 指導側のフィードバックを反映</li>
              <li>✓ プログラム終了後のヒアリング面談に参加</li>
              <li>✓ 終了後7日以内に申請</li>
            </ul>
            <p className="guarantee-note">
              ※「点数保証」ではなく、読み方の変化に対する保証です。本気で取り組んだのに変化がなかった場合の責任を、運営側が引き取る制度です。
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: 勧めないケース
===================================================== */
function NotForSection() {
  return (
    <section className="notfor-section theme-deep-crimson" data-screen-label="12 Not For">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">09</div>
          <div>
            <span className="eyebrow">PREREQUISITES</span>
            <h2 className="section-title">このプログラムを<br /><em>勧めないケース。</em></h2>
            <p className="section-lead">本質的な成果をお約束するため、以下の前提条件を設けています。</p>
          </div>
        </div>

        <div className="notfor-grid">
          <div className="notfor-card">
            <span className="x">×</span>
            <h4>「楽に」「一発逆転」を期待する方</h4>
            <p>魔法は存在しません。地道に向き合えない場合、SSEは機能しません。</p>
          </div>
          <div className="notfor-card">
            <span className="x">×</span>
            <h4>毎日の提出・振り返りができない方</h4>
            <p>45日間、毎日の積み上げが前提です。継続意思のない方は対象外。</p>
          </div>
          <div className="notfor-card">
            <span className="x">×</span>
            <h4>小手先のテクニックを優先したい方</h4>
            <p>SSEは「読み方（型）」の習得を最優先します。即席のテク講座ではありません。</p>
          </div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: FAQ
===================================================== */
function FAQItem({ q, a }) {
  const [open, setOpen] = useState(false);
  return (
    <div className={`faq-item ${open ? "open" : ""}`}>
      <button className="faq-q" onClick={() => setOpen(o => !o)}>
        <span className="faq-q-mark">Q</span>
        <span className="faq-q-text">{q}</span>
        <span className="faq-toggle">{open ? "−" : "+"}</span>
      </button>
      {open && (
        <div className="faq-a">
          <span className="faq-a-mark">A</span>
          <div className="faq-a-text">{a}</div>
        </div>
      )}
    </div>
  );
}

function FAQSection() {
  return (
    <section id="faq" className="faq-section theme-paper" data-screen-label="13 FAQ">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">17</div>
          <div>
            <span className="eyebrow">FAQ</span>
            <h2 className="section-title">よくあるご質問。</h2>
          </div>
        </div>

        <div className="faq-list">
          <FAQItem
            q="今は英語より他科目を優先すべきでは？"
            a={<>英語は習得に最も時間がかかり、一度崩れると他科目の足を引っ張り続ける科目です。「後回しにするほど効率が下がる」性質があるため、受験戦略上、先に土台を固めることが推奨されます。</>}
          />
          <FAQItem
            q="学校や一般的な塾では代替できないのか？"
            a={<>一般的なカリキュラムは「知識の積み上げ」が主で、「読み方の矯正」に特化した時間は確保されにくい構造です。SSEは既存の学習と競合せず、それらを<strong>加速させるための土台作り</strong>を行います。</>}
          />
          <FAQItem
            q="本当に45日で変わるのか？"
            a={<>変えるのは膨大な「知識量」ではなく、脳の「処理フォーム（型）」です。スポーツのフォーム矯正と同様、集中的なトレーニングで短期間に根本的な読み方を書き換えることは十分に可能です。</>}
          />
          <FAQItem
            q="部活をやりながらでも参加できるか？"
            a={<>過去には週6日の練習で12月末まで全国大会に出場した生徒様も完走されています。大会等で日程が重なる場合でも、開始日をご家庭で自由に選択いただけます。</>}
          />
          <FAQItem
            q="支払い方法は？"
            a={<>原則として銀行振込（合同会社ARC法人口座）にてお願いしております。お振込が難しい事情がある場合は個別にご相談いただけます。</>}
          />
          <FAQItem
            q="途中でどうしても用事があった場合は？"
            a={<>事前にご連絡いただければ、提出ペースの調整が可能です。45日経過後もテキストや動画講義は<strong>無期限で</strong>閲覧いただけます。</>}
          />
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: PRICE & FINAL CTA
===================================================== */
function PriceSection() {
  return (
    <section id="cta" className="price-section theme-paper-gold" data-screen-label="14 Price">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">13</div>
          <div>
            <span className="eyebrow">MONITOR OFFER</span>
            <h2 className="section-title">期間限定<br /><em>モニター募集</em></h2>
            <p className="section-lead">
              先着30名様限定・2026年5月31日まで。<br />
              リスクは私たちが負います。あなたは本気で取り組むことだけ。
            </p>
          </div>
        </div>

        <div className="price-card">
          <div className="price-card-head">
            <span className="price-tag">モニター募集</span>
            <h3>SSE 45日間 集中合宿</h3>
            <span className="price-period">先着30名　2026年5月31日まで</span>
          </div>

          <div className="price-body">
            <div className="price-compare">
              <div className="compare-row">
                <span className="compare-label">通常価格</span>
                <span className="compare-old">¥69,800</span>
              </div>
              <div className="compare-divider"></div>
              <div className="compare-row main">
                <span className="compare-label">モニター価格</span>
                <span className="compare-prev">¥69,800</span>
                <span className="compare-new">
                  <span className="new-num">¥39,800</span>
                  <span className="new-tax">税込43,780円</span>
                </span>
              </div>
              <p className="sse-price-off">約3万円OFF</p>
              <div className="price-perday">1日あたり <strong>約890円</strong> の投資で、一生モノの読み方を。</div>
            </div>

            <ul className="price-includes">
              <li><span>✓</span>動画講義（50本以上）・60の電子教材</li>
              <li><span>✓</span>オリジナル教材・課題 + 模範解答</li>
              <li><span>✓</span>LINE質問・受講生コミュニティ</li>
              <li><span>✓</span>スタート / アフター面談（各45分）</li>
              <li><span>✓</span>ライブ英語特訓参加権・修了証</li>
              <li><span>✓</span>全額返金保証</li>
            </ul>

            <div className="price-cta">
              <a
                href="#"
                className="btn-primary big"
                onClick={(e) => {
                  e.preventDefault();
                  const el = document.getElementById("final");
                  if (el) window.scrollTo({ top: el.offsetTop - 60, behavior: "smooth" });
                }}
              >
                モニター生として参加する
                <span className="arrow">→</span>
              </a>
              <div className="price-cta-meta">
                <span>◇ 銀行振込（三井住友銀行 / 合同会社ARC）</span>
                <span>◇ スマホ・PCで受講可能</span>
              </div>
            </div>
          </div>

          <div className="price-card-corner tl"></div>
          <div className="price-card-corner tr"></div>
          <div className="price-card-corner bl"></div>
          <div className="price-card-corner br"></div>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   SECTION: FINAL — その小さな火を
===================================================== */
function FinalSection() {
  return (
    <section id="final" className="final-section" data-screen-label="15 Final">
      <div className="final-bg">
        <div className="final-stars"></div>
      </div>

      <div className="wrap-narrow final-inner">
        <div className="final-figure">
          <svg viewBox="0 0 80 120" width="60" height="90">
            <ellipse cx="40" cy="115" rx="22" ry="3" fill="rgba(232,194,103,0.2)" />
            <line x1="40" y1="60" x2="40" y2="105" stroke="#0a1530" strokeWidth="6" />
            <circle cx="40" cy="50" r="8" fill="#0a1530" />
            <line x1="40" y1="70" x2="28" y2="90" stroke="#0a1530" strokeWidth="5" />
            <line x1="40" y1="70" x2="52" y2="92" stroke="#0a1530" strokeWidth="5" />
            <line x1="40" y1="105" x2="32" y2="120" stroke="#0a1530" strokeWidth="5" />
            <line x1="40" y1="105" x2="48" y2="120" stroke="#0a1530" strokeWidth="5" />
          </svg>
        </div>

        <span className="eyebrow center">LAST MESSAGE</span>
        <h2 className="final-title">
          その小さな火を、<br />
          <em>消さないであげてください。</em>
        </h2>

        <p className="final-lead">
          この販売ページを最後まで読み切ったということは、<br />
          あなた、または、お子様の中で<br />
          <strong>「今のままじゃダメだ」「本気で変わりたい」</strong>という<br />
          覚悟が、すでに芽生えているということです。
        </p>

        <p className="final-lead small">
          読み方を変えれば、英語の景色は本当に変わります。<br />
          45日後、きっと「<em>やればできる自分</em>」と出会えます。
        </p>

        <div className="final-cta">
          <a href="#" className="btn-primary big" onClick={e => { e.preventDefault(); window.scrollTo({ top: document.getElementById("cta").offsetTop - 60, behavior: "smooth" }); }}>
            45日間集中合宿に申し込む
            <span className="arrow">→</span>
          </a>
        </div>

        <div className="final-sign">
          <span>難関私大専門オンライン塾 THINKING　代表 朝倉 徹大</span>
          <span>賢明なご判断を、心よりお待ちしております。</span>
        </div>
      </div>

      <footer className="footer">
        <div className="wrap footer-inner">
          <div>© 合同会社ARC / 難関私大専門オンライン塾 THINKING</div>
          <div className="footer-links">
            <a href="#">特定商取引法に基づく表記</a>
            <a href="#">プライバシーポリシー</a>
            <a href="#">運営会社</a>
          </div>
        </div>
      </footer>
    </section>
  );
}

window.VoicesSection = VoicesSection;
window.MediaSection = MediaSection;
window.MessageSection = MessageSection;
window.GuaranteeSection = GuaranteeSection;
window.NotForSection = NotForSection;
window.FAQSection = FAQSection;
window.PriceSection = PriceSection;
window.FinalSection = FinalSection;
