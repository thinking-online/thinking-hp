/* Smart Study English — 基礎のグラグラ + サポート4点（ナラティブ） */

/* =====================================================
   FOUNDATION PITFALLS — 基礎がグラグラなのに…
===================================================== */
function FoundationPitfallsSection() {
  const itemRefs = React.useRef([]);
  const markedRef = React.useRef(new Set());
  const [marked, setMarked] = React.useState(() => new Set());

  const pitfalls = [
    {
      line1: "ひたすら英単語を",
      line2: "毎日暗記頑張ってる",
    },
    {
      line1: "文法問題集を解いて",
      line2: "文法の知識を入れる",
    },
    {
      line1: "長文演習をして",
      line2: "英文に慣れようとする",
    },
    {
      line1: "塾に通い授業を",
      line2: "たくさん受けようとする",
    },
    {
      line1: "学校の授業についていけず",
      line2: "英文の訳を書き写すだけ",
    },
  ];

  React.useEffect(() => {
    const items = itemRefs.current.filter(Boolean);
    if (!items.length) return undefined;

    const obs = new IntersectionObserver(
      (entries) => {
        let changed = false;
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const idx = Number(entry.target.dataset.index);
          if (Number.isNaN(idx) || markedRef.current.has(idx)) return;
          markedRef.current.add(idx);
          changed = true;
        });
        if (changed) setMarked(new Set(markedRef.current));
      },
      {
        root: null,
        rootMargin: "-36% 0px -46% 0px",
        threshold: 0.08,
      }
    );

    items.forEach((el) => obs.observe(el));
    return () => obs.disconnect();
  }, []);

  return (
    <section
      id="foundation-pitfalls"
      className="sse-foundation theme-paper"
      data-screen-label="Foundation pitfalls"
    >
      <div className="wrap">
        <div className="section-head">
          <div className="section-num sse-narrative-num">III</div>
          <div>
            <span className="eyebrow">SHAKY BASE</span>
            <h2 className="section-title sse-foundation-title">
              <span className="sse-foundation-title-line">基礎がグラグラなのに、</span>
              <span className="sse-foundation-title-line">
                <em>こんなことしてませんか？</em>
              </span>
            </h2>
            <p className="section-lead">
              中学英単語で構成された英文ですらスラスラ読めない状態で、闇雲に努力をしている生徒が多くいます。
            </p>
          </div>
        </div>

        <ul className="sse-foundation-list" role="list">
          {pitfalls.map((p, i) => (
            <li
              key={i}
              ref={(el) => {
                itemRefs.current[i] = el;
              }}
              data-index={i}
              className={`sse-foundation-item${marked.has(i) ? " is-crossed" : ""}`}
              role="listitem"
            >
              <span className="sse-foundation-item-mark" aria-hidden="true">
                {String(i + 1).padStart(2, "0")}
              </span>
              <div className="sse-foundation-item-body">
                <span className="sse-foundation-line1">{p.line1}</span>
                <span className="sse-foundation-line2">{p.line2}</span>
              </div>
              <span className="sse-foundation-cross" aria-hidden="true">
                <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
                  <line className="sse-foundation-cross-line sse-foundation-cross-line-a" x1="18" y1="18" x2="102" y2="102" />
                  <line className="sse-foundation-cross-line sse-foundation-cross-line-b" x1="102" y1="18" x2="18" y2="102" />
                </svg>
              </span>
            </li>
          ))}
        </ul>

        <p className="sse-foundation-warn">
          このままだと正直、<strong>受験は相当危険</strong>。
        </p>

        <div className="sse-foundation-to-why">
          <span className="sse-foundation-to-why-arrow" aria-hidden="true">
            ↓
          </span>
          <p className="sse-foundation-to-why-text">
            では、その先の<strong>時間とお金の投資</strong>は、どこに流れていくのか。
          </p>
        </div>
      </div>
    </section>
  );
}

window.FoundationPitfallsSection = FoundationPitfallsSection;
