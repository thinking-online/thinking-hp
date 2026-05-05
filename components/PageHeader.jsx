// Common page header (breadcrumb + title + lead) for sub-pages
const PageHeader = ({ eyebrow, en, jp, lead, breadcrumbs = [], bgImage }) => {
  return (
    <section className={`page-header ${bgImage ? "has-bg-image" : ""}`}>
      <div
        className="page-header-bg"
        style={bgImage ? { backgroundImage: `url('${bgImage}')` } : undefined}
      />
      <div className="page-header-grain" />

      <div className="page-header-inner">
        {breadcrumbs.length > 0 && (
          <nav className="breadcrumb" aria-label="パンくずリスト">
            <ol>
              <li><a href="index.html">Top</a></li>
              {breadcrumbs.map((b, i) => (
                <li key={i}>
                  <span className="breadcrumb-sep">/</span>
                  {b.href ? <a href={b.href}>{b.label}</a> : <span>{b.label}</span>}
                </li>
              ))}
            </ol>
          </nav>
        )}

        <div className="page-header-eyebrow">
          <span className="page-header-en"><i>{en}</i></span>
          {eyebrow && <span className="page-header-tag">{eyebrow}</span>}
        </div>

        <h1 className="page-header-title">{jp}</h1>

        {lead && <p className="page-header-lead">{lead}</p>}

        <div className="page-header-orn">
          <span /><span className="page-header-orn-mark" /><span />
        </div>
      </div>
    </section>
  );
};

window.PageHeader = PageHeader;
