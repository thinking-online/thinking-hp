// Products listing — university search / group filter → faculty manuals

function ProductsManualCard({ uniName, m }) {
  const coming = m.status !== "available";
  const title = `${uniName} ${m.facultyJa} 完全攻略マニュアル`;
  const href = coming ? "#" : m.href || "#";
  const tags = m.tags || (coming ? ["2027年度版", "作成中"] : []);
  const markText = (m.facultyJa || "Manual").replace(/（[^）]*）/g, "").slice(0, 8);

  return (
    <a
      href={href}
      className={`product-card ${coming ? "coming" : ""}`}
      aria-disabled={coming}
      onClick={coming ? (e) => e.preventDefault() : undefined}
    >
      {m.img ? (
        <div className="product-card-image">
          <img src={m.img} alt={title} />
        </div>
      ) : (
        <div className="product-card-image placeholder">
          <span className="mark"><i>{markText}</i></span>
          <span className="note"><i>2027 Prep</i></span>
        </div>
      )}
      <div className="product-card-body">
        <div className="product-card-tags">
          {tags.map((t, j) => (
            <span key={j} className="product-card-tag">{t}</span>
          ))}
        </div>
        <h3 className="product-card-title">{title}</h3>
        <p className="product-card-lead">{m.lead}</p>
        <div className="product-card-foot">
          <span className="product-card-price">
            {coming ? (
              <i>—</i>
            ) : (
              <>
                <strong>{m.price}</strong>
                {m.priceLabel || ""}
              </>
            )}
          </span>
          <span className="product-card-arrow">
            {coming ? "2027年度版 作成中" : "詳細を見る"}
            {!coming && (
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <path d="M5 12h14M13 5l7 7-7 7" />
              </svg>
            )}
          </span>
        </div>
      </div>
    </a>
  );
}

const ProductsListPage = () => {
  const catalog =
    typeof PRODUCTS_MANUAL_CATALOG !== "undefined" ? PRODUCTS_MANUAL_CATALOG : null;

  const [query, setQuery] = React.useState("");
  const [groupId, setGroupId] = React.useState("all");
  const [selectedUniId, setSelectedUniId] = React.useState(null);

  const orderedUniIds = React.useMemo(() => {
    if (!catalog) return [];
    const out = [];
    const seen = new Set();
    catalog.groups.forEach((g) => {
      g.universityIds.forEach((id) => {
        if (!seen.has(id) && catalog.universities[id]) {
          seen.add(id);
          out.push(id);
        }
      });
    });
    return out;
  }, [catalog]);

  const filteredUniIds = React.useMemo(() => {
    if (!catalog) return [];
    const q = query.trim().toLowerCase();
    let ids =
      groupId === "all"
        ? orderedUniIds.slice()
        : (catalog.groups.find((g) => g.id === groupId)?.universityIds || []).filter(
            (id) => catalog.universities[id]
          );

    if (q) {
      ids = ids.filter((id) => {
        const u = catalog.universities[id];
        const blob = `${u.name} ${u.searchKeys || ""}`.toLowerCase();
        return blob.includes(q);
      });
    }
    return ids;
  }, [catalog, groupId, query, orderedUniIds]);

  const selectedUni =
    catalog && selectedUniId ? catalog.universities[selectedUniId] : null;

  const scrollToCatalog = () => {
    const el = document.getElementById("products-catalog");
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  const openUniversity = (id) => {
    setSelectedUniId(id);
    scrollToCatalog();
  };

  const closeUniversity = () => {
    setSelectedUniId(null);
    scrollToCatalog();
  };

  if (!catalog) {
    return (
      <>
        <PageHeader
          en="Manuals & Workbooks"
          eyebrow="問題集シリーズ"
          jp={<>学部別 <em>完全攻略</em>マニュアル。</>}
          lead="カタログの読み込みに失敗しました。ページを再読み込みしてください。"
          bgImage="assets/products-manuals-hero.png"
          headerClassName="page-header--products-manuals"
        />
        <section className="products-list-section">
          <div className="products-list-inner">
            <p className="products-list-intro">カタログの読み込みに失敗しました。ページを再読み込みしてください。</p>
          </div>
        </section>
      </>
    );
  }

  return (
    <>
      <PageHeader
        en="Manuals & Workbooks"
        eyebrow="問題集シリーズ"
        jp={<>学部別 <em>完全攻略</em>マニュアル。</>}
        lead="掲載は私立文系の入試区分に該当する学部のみです。大学名を検索するか、エリアを選んで大学をタップすると、その大学の一覧が表示されます。現在販売中は関西学院大学 2/1試験（英語）のみ。その他は「2027年度版 作成中」として枠をご用意しています。"
        bgImage="assets/products-manuals-hero.png"
        headerClassName="page-header--products-manuals"
      />

      <section className="products-list-section" id="products-catalog">
        <div className="products-list-inner">
          <p className="products-list-intro">
            予備校のテキストや市販の参考書では届かない解像度で、各大学・各学部に特化した完全攻略マニュアルを順次リリースしていきます。販売開始分には、代表 朝倉徹大との
            <strong style={{ color: "var(--accent)" }}>個別相談会チケット（60分）</strong>
            を購入特典として付属する予定です。
          </p>

          {!selectedUni && (
            <div className="products-catalog-toolbar">
              <div className="products-search-wrap">
                <label htmlFor="products-uni-search" className="products-search-label">
                  大学名で検索
                </label>
                <input
                  id="products-uni-search"
                  type="search"
                  className="products-search-input"
                  placeholder="例：明治、関学、早稲田、G MARCH…"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  autoComplete="off"
                />
              </div>

              <div className="products-group-wrap">
                <span className="products-group-label">エリア</span>
                <div className="products-group-scroll" role="tablist" aria-label="大学グループ">
                  <button
                    type="button"
                    role="tab"
                    aria-selected={groupId === "all"}
                    className={`products-group-tab ${groupId === "all" ? "active" : ""}`}
                    onClick={() => setGroupId("all")}
                  >
                    すべて
                  </button>
                  {catalog.groups.map((g) => (
                    <button
                      key={g.id}
                      type="button"
                      role="tab"
                      aria-selected={groupId === g.id}
                      className={`products-group-tab ${groupId === g.id ? "active" : ""}`}
                      onClick={() => setGroupId(g.id)}
                    >
                      <span className="products-group-tab-ja">{g.labelJa}</span>
                      <span className="products-group-tab-en"><i>{g.labelEn}</i></span>
                    </button>
                  ))}
                </div>
              </div>

              <p className="products-uni-hint">
                掲載は<strong>私立文系入試</strong>に該当する学部のみです。大学名のボタンを押すと、学部別マニュアルの一覧が開きます。
              </p>

              <div className="products-uni-grid">
                {filteredUniIds.length === 0 ? (
                  <p className="products-uni-empty">該当する大学が見つかりませんでした。検索語を変えてお試しください。</p>
                ) : (
                  filteredUniIds.map((id) => {
                    const u = catalog.universities[id];
                    const availableCount = u.manuals.filter((m) => m.status === "available").length;
                    return (
                      <button
                        key={id}
                        type="button"
                        className="products-uni-btn"
                        onClick={() => openUniversity(id)}
                      >
                        <span className="products-uni-btn-name">{u.name}</span>
                        <span className="products-uni-btn-meta">
                          {availableCount > 0 ? (
                            <span className="products-uni-badge on">販売中 {availableCount}</span>
                          ) : (
                            <span className="products-uni-badge">2027年度版 作成中</span>
                          )}
                        </span>
                        <span className="products-uni-btn-arrow" aria-hidden="true">→</span>
                      </button>
                    );
                  })
                )}
              </div>
            </div>
          )}

          {selectedUni && (
            <div className="products-selected-block">
              <div className="products-selected-head">
                <button type="button" className="products-back-btn" onClick={closeUniversity}>
                  ← 大学一覧へ
                </button>
                <div>
                  <h2 className="products-selected-title">{selectedUni.name}</h2>
                  <p className="products-selected-lead">
                    学部別マニュアル {selectedUni.manuals.length} 件
                    <span className="products-selected-dot"> · </span>
                    販売中はカードから詳細ページへ進めます。
                  </p>
                </div>
              </div>

              <div className="products-grid">
                {selectedUni.manuals.map((m) => (
                  <ProductsManualCard
                    key={m.id || `${selectedUni.id}-${m.facultyJa}`}
                    uniName={selectedUni.name}
                    m={m}
                  />
                ))}
              </div>
            </div>
          )}
        </div>
      </section>
    </>
  );
};

window.ProductsListPage = ProductsListPage;
