// Global site header — common to all pages
// Pass `current` prop with the route key to mark active nav item
const SiteHeader = ({ current = "" }) => {
  const [scrolled, setScrolled] = React.useState(false);
  const [open, setOpen] = React.useState(false);

  React.useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  React.useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  const nav = [
    { key: "strategy", label: "学部別戦略", en: "Strategy", href: "/strategy" },
    { key: "support",  label: "サポート体制", en: "Support",  href: "/support" },
    { key: "voice",    label: "合格者の声",   en: "Voices",   href: "/voice" },
    { key: "price",    label: "料金・入塾",   en: "Pricing",  href: "/price" },
    { key: "products", label: "問題集",       en: "Manuals",  href: "/products" },
    { key: "faq",      label: "よくある質問", en: "FAQ",      href: "/faq" },
    { key: "founder",  label: "代表紹介",     en: "Founder",  href: "/founder" },
    { key: "blog",     label: "記事一覧",     en: "Journal",  href: "/blog" },
  ];

  return (
    <>
      <header className={`site-header ${scrolled ? "scrolled" : ""}`}>
        <div className="site-header-inner">
          <a href="/" className="site-logo" aria-label="THINKING トップへ">
            <span className="site-logo-en">THINKING</span>
            <span className="site-logo-jp">学部別・合格設計塾</span>
          </a>

          <nav className="site-nav" aria-label="メイン">
            <ul>
              {nav.map((n) => (
                <li key={n.key} className={current === n.key ? "active" : ""}>
                  <a href={n.href}>
                    <span className="nav-jp">{n.label}</span>
                    <span className="nav-en">{n.en}</span>
                  </a>
                </li>
              ))}
            </ul>
          </nav>

          <div className="site-header-cta">
            <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="header-cta">
              <span className="header-cta-en"><i>LINE</i></span>
              <span className="header-cta-jp">無料相談</span>
              <svg className="header-cta-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <path d="M5 12h14M13 5l7 7-7 7" />
              </svg>
            </a>
          </div>

          <button
            className={`site-burger ${open ? "open" : ""}`}
            aria-label="メニューを開く"
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
          >
            <span /><span /><span />
          </button>
        </div>
      </header>

      {/* Mobile drawer */}
      <div className={`site-drawer ${open ? "open" : ""}`} aria-hidden={!open}>
        <div className="site-drawer-inner">
          <span className="site-drawer-eyebrow"><i>Menu</i></span>
          <ul className="site-drawer-nav">
            <li className={current === "" ? "active" : ""}>
              <a href="/" onClick={() => setOpen(false)}>
                <span className="nav-jp">トップ</span>
                <span className="nav-en">Home</span>
              </a>
            </li>
            {nav.map((n) => (
              <li key={n.key} className={current === n.key ? "active" : ""}>
                <a href={n.href} onClick={() => setOpen(false)}>
                  <span className="nav-jp">{n.label}</span>
                  <span className="nav-en">{n.en}</span>
                </a>
              </li>
            ))}
          </ul>
          <a href="https://line.me/R/ti/p/@thinking" target="_blank" rel="noopener noreferrer" className="cta site-drawer-cta" onClick={() => setOpen(false)}>
            LINEで無料相談
            <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M5 12h14M13 5l7 7-7 7" />
            </svg>
          </a>
          <div className="site-drawer-foot">
            <span><i>THINKING</i></span>
            <span>Designed for Your Faculty.</span>
          </div>
        </div>
      </div>
    </>
  );
};

window.SiteHeader = SiteHeader;
