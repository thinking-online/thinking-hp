// Generic Product / Sales page template — driven by a `data` prop
// Pass any university/faculty/subject manual data and this renders the full sales page.
// Schema (all fields optional except `slug`, `headline`, `pricing.early.amount`):
//
// {
//   slug: "kangaku-english",                   // for sticky bar id
//   breadcrumb: "関学2/1英語 完全攻略マニュアル",
//   hero: { image, alt, tags: [{label, solid?}], stats: [{label, value}] },
//   headline: <jsx>, sublead: <string>,
//   quickCtaText: <jsx>,
//   benefits: [{strong, text}],
//   chapters: [
//     { eyebrow, title, h3?, intro?, sections: [
//        { kind: "specTable", rows: [[k,v]] }
//        { kind: "colTable", headers: [], rows: [[..]], footer? }
//        { kind: "prose", body: <jsx> }
//        { kind: "orderFlow", steps: [{no,label,time,hl}] }
//        { kind: "patterns", items: [{no,title,body,full?}] }
//        { kind: "mistakes", items: [{title,body,em}] }
//        { kind: "roadmap", steps: [{no,name,period,items}] }
//        { kind: "centerCallout", text }
//        { kind: "orderedList", items: [{strong,body}] }
//     ] }
//   ],
//   manualTitle: "...",
//   parts: [{no, icon, pages, title, lead, items: [[strong, sub?]]}],
//   bonus: { title, lead, items: [] },
//   pricing: {
//     early: {amount, deadline, label?},
//     standard: {amount, deadline, label?},
//     compare: [{label, amount, ours?}]
//   },
//   recommend: { yes: [], no: [] },
//   faqs: [{q,a}],
//   purchase: { title, priceLine, fineprint, ctaLabel? },
//   closing: { paragraphs: [<jsx>], signLine1, signLine2 },
//   stickyName: "...",
//   stickyPrice: <jsx>,
// }
const ProductPage = ({ data }) => {
  const LINE_URL = "https://line.me/R/ti/p/@thinking";
  const SNS_INSTAGRAM = "https://www.instagram.com/king_of_juken/?hl=ja";
  const SNS_YOUTUBE_TETTA = "https://www.youtube.com/@tetta-waseda-channel";
  const SNS_YOUTUBE_THINKING = "https://www.youtube.com/@all-day-thinking";
  const [stickyVisible, setStickyVisible] = React.useState(false);
  const [openFaq, setOpenFaq] = React.useState(0);

  React.useEffect(() => {
    const onScroll = () => setStickyVisible(window.scrollY > 800);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const arrow = (
    <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
      <path d="M5 12h14M13 5l7 7-7 7" />
    </svg>
  );

  const renderSection = (sec, key) => {
    if (sec.kind === "specTable") {
      return (
        <div key={key} className="product-table-wrap">
          <table className="product-table">
            <tbody>
              {sec.rows.map(([k, v], i) => (<tr key={i}><th>{k}</th><td>{v}</td></tr>))}
            </tbody>
          </table>
        </div>
      );
    }
    if (sec.kind === "colTable") {
      return (
        <div key={key} className="product-table-wrap">
          <table className="product-table col-table">
            {sec.headers && (
              <thead><tr>{sec.headers.map((h, i) => <th key={i} style={h.style}>{h.label || h}</th>)}</tr></thead>
            )}
            <tbody>
              {sec.rows.map((r, i) => (
                <tr key={i}>
                  {r.map((cell, j) => {
                    const cls = (sec.cellClass && sec.cellClass[j]) || "";
                    return <td key={j} className={cls}>{cell}</td>;
                  })}
                </tr>
              ))}
              {sec.footer && (
                <tr>{sec.footer.map((f, i) => <td key={i} colSpan={f.colSpan} className={f.cls} style={f.style}>{f.value}</td>)}</tr>
              )}
            </tbody>
          </table>
        </div>
      );
    }
    if (sec.kind === "prose") return <div key={key} className="product-prose">{sec.body}</div>;
    if (sec.kind === "h3") return <h3 key={key} className="product-h3">{sec.text}</h3>;
    if (sec.kind === "orderFlow") {
      return (
        <div key={key} className="product-order-flow">
          {sec.steps.map((s, i) => (
            <div key={i} className={`step ${s.hl ? "highlight" : ""}`}>
              <span className="step-no"><i>{s.no}</i></span>
              <span className="step-label">{s.label}</span>
              <span className="step-time">{s.time}</span>
            </div>
          ))}
        </div>
      );
    }
    if (sec.kind === "patterns") {
      return (
        <div key={key} className="product-patterns">
          {sec.items.map((p, i) => (
            <div key={i} className="product-pattern" style={p.full ? {gridColumn: "span 2"} : null}>
              <span className="no"><i>{p.no}</i></span>
              <h4>{p.title}</h4>
              <p>{p.body}</p>
            </div>
          ))}
        </div>
      );
    }
    if (sec.kind === "mistakes") {
      return (
        <div key={key} className="product-mistakes">
          {sec.items.map((m, i) => (
            <div key={i} className="product-mistake">
              <div className="product-mistake-no"><i>0{i+1}</i></div>
              <div className="product-mistake-body">
                <h4>{m.title}</h4>
                <p>{m.body} <strong>{m.em}</strong></p>
              </div>
            </div>
          ))}
        </div>
      );
    }
    if (sec.kind === "roadmap") {
      return (
        <div key={key} className="product-roadmap">
          {sec.steps.map((s, i) => (
            <div key={i} className="product-roadmap-step">
              <div className="product-roadmap-step-head">
                <span className="product-roadmap-step-no"><i>{s.no}</i></span>
                <span className="product-roadmap-step-name">{s.name}</span>
                <span className="product-roadmap-step-period">{s.period}</span>
              </div>
              <ul>{s.items.map((it, j) => <li key={j}>{it}</li>)}</ul>
            </div>
          ))}
        </div>
      );
    }
    if (sec.kind === "centerCallout") {
      return (
        <p key={key} style={{fontFamily: "var(--serif-en)", fontStyle: "italic", color: "var(--accent)", textAlign: "center", fontSize: 16, padding: "16px 24px", background: "var(--bg-1)", border: "1px solid var(--line)", letterSpacing: "0.06em"}}>
          {sec.text}
        </p>
      );
    }
    if (sec.kind === "orderedList") {
      return (
        <ol key={key} className="article-list-ordered" style={{margin: "16px 0 24px"}}>
          {sec.items.map((it, i) => (
            <li key={i}><strong>{it.strong}</strong>{it.body && <><br />{it.body}</>}</li>
          ))}
        </ol>
      );
    }
    return null;
  };

  return (
    <main className="product-page">
      {/* Breadcrumb */}
      <nav className="product-breadcrumb" aria-label="パンくず">
        <a href="/">トップ</a>
        <span className="sep">／</span>
        <a href="/products">問題集・教材</a>
        <span className="sep">／</span>
        <span className="current">{data.breadcrumb}</span>
      </nav>

      {/* Hero */}
      <section className="product-hero">
        <div className="product-hero-inner">
          <div className="product-hero-banner">
            {data.hero.image ? (
              <img src={data.hero.image} alt={data.hero.alt || data.breadcrumb} />
            ) : (
              <div style={{
                width: "100%", height: "100%",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontFamily: "var(--serif-en)", fontStyle: "italic",
                color: "var(--accent)", opacity: 0.5, fontSize: 32, letterSpacing: "0.18em",
                background: "radial-gradient(ellipse at 30% 30%, rgba(200,168,104,0.08), transparent 60%), linear-gradient(135deg, var(--bg-2), var(--bg-0))"
              }}>{data.hero.alt || "Hero Banner"}</div>
            )}
          </div>

          <div className="product-meta-row">
            {data.hero.tags && data.hero.tags.map((t, i) => (
              <span key={i} className={`product-meta-tag ${t.solid ? "solid" : ""}`}>{t.label}</span>
            ))}
            {data.hero.stats && data.hero.stats.map((s, i) => (
              <span key={i} className="product-meta-stat">
                {s.before}<strong>{s.value}</strong>{s.label}
              </span>
            ))}
            <span className="product-meta-spacer" />
            <div className="product-meta-share">
              <a href={SNS_INSTAGRAM} target="_blank" rel="noopener noreferrer" aria-label="Instagram：受験の王様（フォロワー8.5万人以上）">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"><rect x="3" y="3" width="18" height="18" rx="5" /><circle cx="12" cy="12" r="4" /><circle cx="17.5" cy="6.5" r="0.8" fill="currentColor" /></svg>
              </a>
              <a href={SNS_YOUTUBE_TETTA} target="_blank" rel="noopener noreferrer" aria-label="YouTube：てった｜私立文系の勝ち方ch">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8zM9.6 15.6V8.4l6.2 3.6z" /></svg>
              </a>
              <a href={SNS_YOUTUBE_THINKING} target="_blank" rel="noopener noreferrer" aria-label="YouTube：オンライン塾THINKING・合格者対談チャンネル">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8zM9.6 15.6V8.4l6.2 3.6z" /></svg>
              </a>
              <a
                href="#"
                aria-label="このページのURLをコピー"
                onClick={(e) => {
                  e.preventDefault();
                  if (typeof navigator !== "undefined" && navigator.clipboard?.writeText && typeof window !== "undefined") {
                    navigator.clipboard.writeText(window.location.href).catch(() => {});
                  }
                }}
              >
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><path d="M10 13a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1M14 11a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1" /></svg>
              </a>
            </div>
          </div>

          <h1 className="product-headline">{data.headline}</h1>
          <p className="product-sublead">{data.sublead}</p>

          <div className="product-quick-cta">
            <p className="product-quick-cta-text">{data.quickCtaText}</p>
            <a href="#purchase" className="cta">価格を確認する{arrow}</a>
          </div>
        </div>
      </section>

      {/* Benefits */}
      {data.benefits && (
        <section className="product-section">
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>Why Read This</i></span>
            <h2 className="product-h2">{data.benefitsTitle || <>この記事を読むだけで、<em>{data.subject || "出題"}の輪郭</em>が完全に見える。</>}</h2>
            <ul className="product-benefits">
              {data.benefits.map((b, i) => (<li key={i}><span><strong>{b.strong}</strong>{b.text}</span></li>))}
            </ul>
            {data.benefitsFooter && (
              <p style={{marginTop: 28, fontFamily: "var(--serif-jp)", fontSize: 14, color: "var(--ink-2)", lineHeight: 2, letterSpacing: "0.05em"}}>
                {data.benefitsFooter}
              </p>
            )}
          </div>
        </section>
      )}

      {/* Chapters */}
      {data.chapters && data.chapters.map((ch, ci) => (
        <section key={ci} className={`product-section ${ci % 2 === 0 ? "alt" : ""}`}>
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>{ch.eyebrow}</i></span>
            <h2 className="product-h2">{ch.title}</h2>
            {ch.sections.map((sec, si) => renderSection(sec, si))}
          </div>
        </section>
      ))}

      {/* Manual contents (parts) */}
      {data.parts && (
        <section className="product-section">
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>Manual Contents</i></span>
            <h2 className="product-h2">{data.manualTitle}</h2>
            {data.manualLead && (
              <div className="product-prose"><p>{data.manualLead}</p></div>
            )}
            <div className="product-parts">
              {data.parts.map((p, i) => (
                <div key={i} className="product-part">
                  <div className="product-part-head">
                    <span className="product-part-no"><i>{p.no}</i></span>
                    <span className="product-part-icon">{p.icon}</span>
                    <h3 className="product-part-title">{p.title}</h3>
                    <span className="product-part-pages"><i>{p.pages}</i></span>
                  </div>
                  <p className="product-part-lead">{p.lead}</p>
                  <ul className="product-part-list">
                    {p.items.map((it, j) => (
                      <li key={j}><strong>{it[0]}</strong>{it[1] ? ` ── ${it[1]}` : ""}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>

            {data.bonus && (
              <div className="product-bonus">
                <span className="product-bonus-eyebrow"><i>Bonus / 購入特典</i></span>
                <h3 className="product-bonus-title">{data.bonus.title}</h3>
                <p>{data.bonus.lead}</p>
                <ul>{data.bonus.items.map((it, i) => <li key={i}>{it}</li>)}</ul>
              </div>
            )}
          </div>
        </section>
      )}

      {/* Pricing */}
      {data.pricing && (
        <section id="purchase" className="product-section alt">
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>Pricing</i></span>
            <h2 className="product-h2"><em>価格</em>について。</h2>
            <div className="product-pricing">
              <div className="product-pricing-grid">
                <div className="product-pricing-cell early">
                  <span className="product-pricing-label"><i>Early Bird</i></span>
                  <span className="product-pricing-tag">{data.pricing.early.label || "早期割価格"}</span>
                  <div className="product-pricing-amount">
                    <span className="yen">¥</span>{data.pricing.early.amount}<span className="tax">税込</span>
                  </div>
                  <div className="product-pricing-deadline">{data.pricing.early.deadline}</div>
                </div>
                <div className="product-pricing-cell">
                  <span className="product-pricing-label"><i>Standard</i></span>
                  <span className="product-pricing-tag">{data.pricing.standard.label || "通常価格"}</span>
                  <div className="product-pricing-amount">
                    <span className="yen">¥</span>{data.pricing.standard.amount}<span className="tax">税込</span>
                  </div>
                  <div className="product-pricing-deadline">{data.pricing.standard.deadline}</div>
                </div>
              </div>
              {data.pricing.compare && (
                <div className="product-pricing-compare">
                  <h4>{data.pricing.compareTitle || "この価格設定の根拠"}</h4>
                  <ul>
                    {data.pricing.compare.map((c, i) => (
                      <li key={i} className={c.ours ? "ours" : ""}>{c.label}<strong>¥{c.amount}</strong></li>
                    ))}
                  </ul>
                </div>
              )}
              {data.pricing.note && (
                <div className="product-prose" style={{marginTop: 24}}><p>{data.pricing.note}</p></div>
              )}
            </div>
          </div>
        </section>
      )}

      {/* Recommend */}
      {data.recommend && (
        <section className="product-section">
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>For Whom</i></span>
            <h2 className="product-h2">こんな受験生に<em>おすすめ</em>。</h2>
            <div className="product-rec-grid">
              <div className="product-rec recommend">
                <h4>こんな人におすすめ</h4>
                <ul>{data.recommend.yes.map((it, i) => <li key={i}>{it}</li>)}</ul>
              </div>
              <div className="product-rec notrec">
                <h4>こんな人にはおすすめしない</h4>
                <ul>{data.recommend.no.map((it, i) => <li key={i}>{it}</li>)}</ul>
              </div>
            </div>
          </div>
        </section>
      )}

      {/* FAQ */}
      {data.faqs && (
        <section className="product-section alt">
          <div className="product-section-inner">
            <span className="product-eyebrow"><i>FAQ</i></span>
            <h2 className="product-h2">よくある<em>質問</em>。</h2>
            <div className="product-faq">
              {data.faqs.map((f, i) => (
                <div key={i} className={`product-faq-item ${openFaq === i ? "open" : ""}`}>
                  <button className="product-faq-q" onClick={() => setOpenFaq(openFaq === i ? -1 : i)}>
                    <span className="q-mark"><i>Q.</i></span>
                    <span>{f.q}</span>
                    <span className="q-toggle">+</span>
                  </button>
                  <div className="product-faq-a">{f.a}</div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Purchase CTA */}
      {data.purchase && (
        <section className="product-purchase">
          <div className="product-purchase-inner">
            <span className="product-purchase-eyebrow"><i>Buy Now / LINE</i></span>
            <h2 className="product-purchase-title">{data.purchase.title}</h2>
            <div className="product-purchase-price">{data.purchase.priceLine}</div>
            <a href={LINE_URL} target="_blank" rel="noopener noreferrer" className="cta cta-large">
              {data.purchase.ctaLabel || "LINEで購入手続きへ"}{arrow}
            </a>
            <p className="product-purchase-fineprint">{data.purchase.fineprint}</p>
          </div>
        </section>
      )}

      {/* Closing */}
      {data.closing && (
        <section className="product-closing">
          <div className="product-closing-inner">
            <span className="product-eyebrow"><i>Final Message</i></span>
            <h2 className="product-h2" style={{marginBottom: 24}}>最後に ── あなたに伝えたいこと。</h2>
            {data.closing.paragraphs.map((p, i) => <p key={i}>{p}</p>)}
            <p className="product-closing-sign">
              {data.closing.signLine1}<br />
              {data.closing.signLine2}
            </p>
          </div>
        </section>
      )}

      {/* Sticky bar */}
      <div className={`product-sticky-bar ${stickyVisible ? "visible" : ""}`}>
        <div className="product-sticky-bar-inner">
          <div className="product-sticky-bar-text">
            <span className="product-sticky-bar-name">{data.stickyName}</span>
            <span className="product-sticky-bar-price">{data.stickyPrice}</span>
          </div>
          <a href={LINE_URL} target="_blank" rel="noopener noreferrer" className="cta">
            LINEで購入する{arrow}
          </a>
        </div>
      </div>
    </main>
  );
};

window.ProductPage = ProductPage;
