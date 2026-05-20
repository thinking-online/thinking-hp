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

/* =====================================================
   SUPPORT FOUR — 悩み × 仕組みで完走させる
===================================================== */
function SupportFourSection() {
  const items = [
    {
      worryNum: "悩み 01",
      worry: "継続できるか不安…",
      title: "提出課題システム",
      desc: "毎日、決まった時間に課題が届き、期限内に提出。サボり癖があっても「締切」が背中を押し、半強制的に積み上がる設計です。",
      icon: (
        <svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true">
          <rect x="8" y="10" width="32" height="28" rx="2" fill="none" stroke="currentColor" strokeWidth="1.5" />
          <path d="M8 18h32M16 10v-3M32 10v-3" stroke="currentColor" strokeWidth="1.5" fill="none" />
          <path d="M16 26l6 6 12-12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        </svg>
      ),
    },
    {
      worryNum: "悩み 02",
      worry: "わかったつもりで終わりそう…",
      title: "実践ワークつき",
      desc: "動画・講義だけでは伸びにくい「わかったつもり」を防ぎます。手を動かす演習で、理解をその日のうちに力に変えます。",
      icon: (
        <svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true">
          <path d="M14 36l20-20M14 16h8v8M26 28h8v8" stroke="currentColor" strokeWidth="1.8" fill="none" strokeLinecap="round" />
          <circle cx="14" cy="36" r="3" fill="currentColor" />
        </svg>
      ),
    },
    {
      worryNum: "悩み 03",
      worry: "わからないと止まってしまう…",
      title: "LINE 質問サポート",
      desc: "予備校の「質問できる時間」に縛られません。LINEでいつでも相談でき、返信まで待つ不安を減らします（目安：24時間以内）。",
      icon: (
        <svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true">
          <path
            d="M24 8c-8.5 0-15 5-15 11.2c0 3.5 2.2 6.6 5.5 8.5c-.3 1-.9 2.8-1 3.2c-.15.6.1.6.35.45c.2-.12 3-2 4.2-2.8c1 .12 2 .18 3 .18c8.5 0 15-5 15-11.2S32.5 8 24 8z"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.5"
          />
          <circle cx="18" cy="21" r="1.5" fill="currentColor" />
          <circle cx="24" cy="21" r="1.5" fill="currentColor" />
          <circle cx="30" cy="21" r="1.5" fill="currentColor" />
        </svg>
      ),
    },
    {
      worryNum: "悩み 04",
      worry: "やる気が続かない…",
      title: "モチベーション配信",
      desc: "毎朝、ミッションとともに背中を押すメッセージが届きます。一人で続ける孤独感を、リズムと言葉で軽くします。",
      icon: (
        <svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true">
          <path d="M24 6l3 9h9l-7 5 3 9-8-6-8 6 3-9-7-5h9z" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round" />
        </svg>
      ),
    },
  ];

  return (
    <section
      id="support-four"
      className="sse-support-four theme-deep-warm"
      data-screen-label="Support Four"
    >
      <div className="wrap">
        <div className="section-head">
          <div className="section-num sse-narrative-num">4</div>
          <div>
            <span className="eyebrow">CONTINUITY ENGINE</span>
            <h2 className="section-title">
              「続けられるか」は、<br />
              <em>根性ではなく仕組み。</em>
            </h2>
            <p className="section-lead">
              多くの生徒が抱える4つの不安を、SSE では最初から設計で潰しています。<br />
              忙しい受験期でも、最後まで走り切れる理由があります。
            </p>
          </div>
        </div>

        <div className="sse-support-grid" role="list">
          {items.map((item, i) => (
            <article key={i} className="sse-support-card" role="listitem">
              <div className="sse-support-card-head">
                <span className="sse-support-worry-label">{item.worryNum}</span>
                <span className="sse-support-worry">{item.worry}</span>
              </div>
              <div className="sse-support-solution">
                <div className="sse-support-icon-wrap" aria-hidden="true">
                  {item.icon}
                </div>
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
              </div>
            </article>
          ))}
        </div>

        <p className="sse-support-foot">
          どれか一つでも欠けると脱落しやすい。<br />
          だから SSE では<strong>4つをセット</strong>で、45日間の伴走を設計しています。
        </p>
      </div>
    </section>
  );
}

window.SupportFourSection = SupportFourSection;
