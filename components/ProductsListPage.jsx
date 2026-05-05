// Products listing page
const ProductsListPage = () => {
  const products = [
    {
      href: "product-kangaku-english.html",
      img: "assets/kangaku-hero.png",
      tags: ["2027年度最新版", "英語"],
      title: "関西学院大学 2/1試験 英語 完全攻略マニュアル",
      lead: "過去5年分を徹底分析。オリジナル問題集90題・頻出単語180・整序50題・総合模試1回分・個別相談会チケット付き。",
      price: "¥19,800",
      priceLabel: "〜（早期割）",
      coming: false,
    },
    {
      href: "#",
      img: null,
      tags: ["近日公開", "国語"],
      title: "早稲田大学 法学部 国語 完全攻略マニュアル",
      lead: "早稲田法の現代文・古文・漢文を、過去問徹底分析と頻出構文・頻出語彙で完全攻略。",
      price: "Coming",
      priceLabel: "",
      coming: true,
    },
    {
      href: "#",
      img: null,
      tags: ["近日公開", "英語"],
      title: "慶應義塾大学 経済学部 英語 完全攻略マニュアル",
      lead: "速読・図表問題・自由英作文。慶應経済特有の出題形式に完全特化した実戦演習。",
      price: "Coming",
      priceLabel: "",
      coming: true,
    },
    {
      href: "#",
      img: null,
      tags: ["近日公開", "日本史"],
      title: "MARCH 日本史 完全攻略マニュアル",
      lead: "明治・青学・立教・中央・法政の頻出テーマと年代問題を一冊に集約。",
      price: "Coming",
      priceLabel: "",
      coming: true,
    },
  ];

  return (
    <>
      <PageHeader
        eyebrow="Manuals & Workbooks"
        title="学部別 完全攻略マニュアル。"
        lead="過去5年分の徹底分析と、合格者を出してきた現場知見を凝縮した、学部別の問題集・教材シリーズ。" />

      <section className="products-list-section">
        <div className="products-list-inner">
          <p className="products-list-intro">
            予備校のテキストや市販の参考書では届かない解像度で、各大学・各学部に特化した完全攻略マニュアルを順次リリースしていきます。すべてのマニュアルに、代表 朝倉徹大との<strong style={{color: "var(--accent)"}}>個別相談会チケット（60分）</strong>を購入特典として付属。
          </p>

          <div className="products-grid">
            {products.map((p, i) => (
              <a
                key={i}
                href={p.href}
                className={`product-card ${p.coming ? "coming" : ""}`}
                aria-disabled={p.coming}
                onClick={p.coming ? (e) => e.preventDefault() : undefined}
              >
                {p.img ? (
                  <div className="product-card-image">
                    <img src={p.img} alt={p.title} />
                  </div>
                ) : (
                  <div className="product-card-image placeholder">
                    <span className="mark"><i>{p.tags[1] || "Manual"}</i></span>
                    <span className="note"><i>Coming Soon</i></span>
                  </div>
                )}
                <div className="product-card-body">
                  <div className="product-card-tags">
                    {p.tags.map((t, j) => (
                      <span key={j} className="product-card-tag">{t}</span>
                    ))}
                  </div>
                  <h3 className="product-card-title">{p.title}</h3>
                  <p className="product-card-lead">{p.lead}</p>
                  <div className="product-card-foot">
                    <span className="product-card-price">
                      {p.coming ? <i>{p.price}</i> : <><strong>{p.price}</strong>{p.priceLabel}</>}
                    </span>
                    <span className="product-card-arrow">
                      {p.coming ? "近日公開" : "詳細を見る"}
                      {!p.coming && (
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                          <path d="M5 12h14M13 5l7 7-7 7" />
                        </svg>
                      )}
                    </span>
                  </div>
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>
    </>
  );
};

window.ProductsListPage = ProductsListPage;
