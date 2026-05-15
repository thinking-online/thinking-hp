// Inline section CTA — links from homepage sections to detail pages
const SectionLink = ({ href, en, children, align = "center", compact = false, className = "" }) => (
  <div className={`section-link ${align === "left" ? "section-link--left" : ""} ${compact ? "section-link--compact" : ""} ${className}`.trim()}>
    <a href={href} className="section-link-btn">
      <span className="section-link-text">
        {en && <i className="section-link-en">{en}</i>}
        <span>{children}</span>
      </span>
      <span className="section-link-arrow" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </span>
    </a>
  </div>
);

window.SectionLink = SectionLink;
