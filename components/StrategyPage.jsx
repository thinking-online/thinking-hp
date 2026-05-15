// Strategy page — proves "same university, different exam" via real 大問 teardown,
// then walks through THINKING's 過去問分析シート process.
const STRATEGY_COMPARE_NUDGE_KEY = "thinking-strategy-compare-nudge-v1";

const StrategyPage = () => {
  const compareTrackRef = React.useRef(null);
  const [compareActiveIdx, setCompareActiveIdx] = React.useState(0);

  const updateCompareActive = React.useCallback(() => {
    const track = compareTrackRef.current;
    if (!track) return;
    const cols = track.querySelectorAll(".compare-col");
    if (cols.length < 2) return;
    const gap = 14;
    const w0 = cols[0].offsetWidth + gap;
    const threshold = w0 * 0.45;
    setCompareActiveIdx(track.scrollLeft > threshold ? 1 : 0);
  }, []);

  const scrollCompareTo = React.useCallback((idx) => {
    const track = compareTrackRef.current;
    if (!track) return;
    const cols = track.querySelectorAll(".compare-col");
    const target = cols[idx];
    if (!target) return;
    const pad = parseFloat(getComputedStyle(track).paddingLeft) || 0;
    track.scrollTo({ left: target.offsetLeft - pad, behavior: "smooth" });
  }, []);

  React.useEffect(() => {
    const track = compareTrackRef.current;
    if (!track) return;
    updateCompareActive();
    track.addEventListener("scroll", updateCompareActive, { passive: true });
    window.addEventListener("resize", updateCompareActive);
    return () => {
      track.removeEventListener("scroll", updateCompareActive);
      window.removeEventListener("resize", updateCompareActive);
    };
  }, [updateCompareActive]);

  /* モバイルのみ：初回だけごく短く横に動かし「スワイプできる」ことを示す（reduce 時は無効） */
  React.useEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    let t0;
    let t1;
    let t2;
    const schedule = () => {
      const mq = window.matchMedia("(max-width: 1100px)");
      const track = compareTrackRef.current;
      if (!track || !mq.matches || reduce.matches) return;
      if (track.scrollWidth <= track.clientWidth + 8) return;
      if (window.sessionStorage.getItem(STRATEGY_COMPARE_NUDGE_KEY)) return;
      const nudge = 36;
      t1 = window.setTimeout(() => {
        track.scrollBy({ left: nudge, behavior: "smooth" });
      }, 900);
      t2 = window.setTimeout(() => {
        track.scrollBy({ left: -nudge, behavior: "smooth" });
        window.sessionStorage.setItem(STRATEGY_COMPARE_NUDGE_KEY, "1");
      }, 2200);
    };
    t0 = window.setTimeout(schedule, 200);
    return () => {
      window.clearTimeout(t0);
      window.clearTimeout(t1);
      window.clearTimeout(t2);
    };
  }, []);
  // Side-by-side teardown: same uni (明治大), same subject (英語), totally different exam.
  const compare = {
    left: {
      faculty: "明治大学 経営学部",
      facultyEn: "Meiji Univ. — School of Business Administration",
      tagline: "ビジネス英語を、速く、正確に。",
      accent: "primary",
      timeMin: 60,
      questionCount: 4,
      shape: "Reading-heavy / 多肢選択",
      shapeNote: "長文の比重が圧倒的。語彙レベルは経済・経営語彙に寄る。",
      daimon: [
        {
          no: "I",
          type: "長文読解",
          ask: "経済・ビジネス系の説明文 (約700語)",
          required: "速読 + パラグラフ把握",
          detail: "段落要旨を見抜き、選択肢のパラフレーズを瞬時に判断。経営・市場・労働関連の語彙が頻出。",
        },
        {
          no: "II",
          type: "長文読解",
          ask: "社会経済系の論説文 (約700語)",
          required: "論理関係 + 内容一致",
          detail: "however / therefore など接続関係を追い、筆者の主張と例示を弁別する読み方が要求される。",
        },
        {
          no: "III",
          type: "会話文",
          ask: "ビジネス・カジュアル混在の対話",
          required: "状況把握 + 慣用表現",
          detail: "空欄補充。英米語の自然な口語表現が問われ、文法選択ではなく場面理解が決め手。",
        },
        {
          no: "IV",
          type: "文法・語法",
          ask: "短文の語彙・文法選択",
          required: "頻出構文 + コロケーション",
          detail: "難解な文法ではなく、使用頻度の高い動詞・前置詞・コロケーションの正確さで差がつく。",
        },
      ],
      verdict:
        "経営学部の英語は「読むスピード × ビジネス語彙 × 設問処理速度」の三点勝負。文学部のような精読・記述は要求されない。",
    },
    right: {
      faculty: "明治大学 文学部",
      facultyEn: "Meiji Univ. — School of Arts and Letters",
      tagline: "深く、丁寧に、味わいながら。",
      accent: "secondary",
      timeMin: 60,
      questionCount: 3,
      shape: "Reading + 和訳・記述",
      shapeNote: "長文は1〜2題と少ない代わりに、1題あたりの密度が高く、設問に和訳・説明記述が入る。",
      daimon: [
        {
          no: "I",
          type: "長文読解 (記述含む)",
          ask: "人文・思想・文学評論 (約900語)",
          required: "精読 + 和訳 + 内容説明",
          detail: "下線部和訳が必須。比喩・抽象表現の和訳には、構文把握だけでなく日本語表現力が問われる。",
        },
        {
          no: "II",
          type: "長文読解",
          ask: "文化・歴史系の論説文 (約700語)",
          required: "論理展開 + 設問記述",
          detail: "「下線部はどういうことか、〇〇字以内で説明せよ」型の記述が含まれる年も多い。論旨整理の力が直結する。",
        },
        {
          no: "III",
          type: "文法・整序英作",
          ask: "文構造の組み立て",
          required: "構文知識 + 語彙の精度",
          detail: "選択ではなく語句整序。動詞の取る形・節構造を文単位で組み立てる力が問われる。",
        },
      ],
      verdict:
        "文学部の英語は「精読 × 和訳 × 記述説明」の精度勝負。スピードよりも、抽象的な内容を日本語で表現する力で得点が決まる。",
    },
  };

  // The 過去問分析シート process — 6 columns of analysis per past paper
  const sheetColumns = [
    {
      label: "大学情報",
      en: "University",
      desc: "大学・学部・学科を一行で固定。志望順位を１〜５志望でシートを分け、本命と併願で別管理。",
    },
    {
      label: "合格最低点 / 配点",
      en: "Threshold",
      desc: "公開最低点・合計配点・最低点率を入力。ここが「何点で合格か」の絶対基準。",
    },
    {
      label: "受験日 / 残り日数",
      en: "Countdown",
      desc: "本番日と残日数を自動計算。週間課題・模試スケジュールはこの数字から逆算。",
    },
    {
      label: "問題数 / 予測 / 見込み点",
      en: "Quantitative",
      desc: "大問単位で予測点・実得点・平均を記録。「あと何点」を、科目・大問レベルで見える化。",
    },
    {
      label: "定量分析",
      en: "Quant. Analysis",
      desc: "予測時間 vs 実時間、設問別正答率、空所補充・内容一致など、設問タイプ別の数値を残す。",
    },
    {
      label: "定性分析 / 総評メモ",
      en: "Qual. Analysis",
      desc: "「ここで詰まった」「ここで時間を使った」を言語化。次回の課題設計の入力になる。",
    },
  ];

  return (
    <>
      <PageHeader
        en="Strategy / Same University, Different Exam"
        eyebrow="学部別戦略・徹底分析"
        jp={<>同じ大学でも、<br />学部が違えば、<em>別の試験</em>。</>}
        lead="明治大学 経営学部の英語と、明治大学 文学部の英語。同じ大学・同じ科目なのに、求められる力はまったく違います。THINKING の学部別戦略は、ここから始まります。"
        bgImage="assets/campus-01.png"
      />

      {/* ACT 1 — claim */}
      <section className="strategy-claim">
        <div className="strategy-claim-inner">
          <span className="eyebrow"><i>The Claim</i></span>
          <h2 className="strategy-claim-title">
            「明治の英語」<em>という科目は、存在しない。</em>
          </h2>
          <p className="strategy-claim-lead">
            あるのは、「明治<i>経営</i>の英語」と「明治<i>文学部</i>の英語」。 <br />
            出題形式・要求される力・時間配分・記述の比重——すべて違う。<br />
            だから、戦略も「明治対策」ではなく「学部対策」でなければ意味がない。
          </p>
          <div className="strategy-claim-meta">
            <div>
              <span className="meta-num">2</span>
              <span className="meta-label">学部 / 同一大学</span>
            </div>
            <div>
              <span className="meta-num">7</span>
              <span className="meta-label">大問の構造差</span>
            </div>
            <div>
              <span className="meta-num">100<i>%</i></span>
              <span className="meta-label">別物です</span>
            </div>
          </div>
        </div>
      </section>

      {/* ACT 2 — side-by-side teardown */}
      <section className="strategy-compare">
        <div className="strategy-compare-inner">
          <header className="strategy-compare-head">
            <span className="eyebrow"><i>Side by Side</i></span>
            <h2 className="strategy-compare-title">
              実際の過去問を、<em>大問単位で</em>並べて見る。
            </h2>
            <p className="strategy-compare-lead">
              明治大学 経営学部の英語と、明治大学 文学部の英語、それぞれの大問構成。<br />
              「読み方」「書き方」「時間の使い方」が、どれだけ違うかが見えるはずです。
            </p>
          </header>

          <div className="compare-grid-outer">
            <p className="compare-swipe-hint">
              <span className="compare-swipe-hint-chev compare-swipe-hint-chev--left" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M15 6l-6 6 6 6" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
              <span className="compare-swipe-hint-text">
                <strong>横にスワイプ</strong>
                <span className="compare-swipe-hint-sub">右端に文学部が少し見えます</span>
              </span>
              <span className="compare-swipe-hint-chev compare-swipe-hint-chev--right" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M9 6l6 6-6 6" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
            </p>

            <div className="compare-grid" ref={compareTrackRef}>
              <CompareColumn data={compare.left} />
              <span className="compare-vs" aria-hidden="true">
                <span className="vs-line" />
                <span className="vs-text">VS</span>
                <span className="vs-line" />
              </span>
              <CompareColumn data={compare.right} />
            </div>

            <div className="compare-scroll-controls" role="group" aria-label="比較パネルの切替">
              <button
                type="button"
                className={`compare-jump ${compareActiveIdx === 0 ? "active" : ""}`}
                aria-pressed={compareActiveIdx === 0}
                onClick={() => scrollCompareTo(0)}
              >
                経営学部
              </button>
              <button
                type="button"
                className={`compare-jump ${compareActiveIdx === 1 ? "active" : ""}`}
                aria-pressed={compareActiveIdx === 1}
                onClick={() => scrollCompareTo(1)}
              >
                文学部
              </button>
            </div>
          </div>

          <div className="compare-footnote">
            <span className="compare-foot-label"><i>So What</i></span>
            <p>
              同じ「英語」というラベルでも、経営学部は<em>速読 + 選択処理</em>、文学部は<em>精読 + 和訳・記述</em>。
              対策の入口が違うのに「明治の過去問やっとけ」では、どちらの学部にも届きません。
            </p>
          </div>
        </div>
      </section>

      {/* ACT 3 — the 過去問分析シート process */}
      <section className="strategy-sheet">
        <div className="strategy-sheet-inner">
          <header className="strategy-sheet-head">
            <span className="eyebrow"><i>How We Go Deep</i></span>
            <h2 className="strategy-sheet-title">
              だから私たちは、<em>過去問分析シート</em>で<br />
              生徒一人一人を、徹底的に解体する。
            </h2>
            <p className="strategy-sheet-lead">
              志望校・学部ごとに「合格最低点」「大問別の予測点・実得点」「設問タイプ別の正答率」「定性的な詰まりポイント」を、すべてシート上で可視化。<br />
              「あと何点」ではなく「どの大問で、どの能力を、どれだけ伸ばすか」を、毎週書き換えながら合格まで運びます。
            </p>
          </header>

          <figure className="sheet-figure">
            <img
              src="assets/kakomon-sheet.png"
              alt="THINKING 過去問分析シートのサンプル。大学情報・合格最低点・受験日カウントダウン・大問別の予測点・定量・定性分析などを一覧する運用用シート（一部）。志望校ごとに過去問を解くたびに更新する。"
            />
          </figure>

          <ul className="sheet-cols">
            {sheetColumns.map((c, i) => (
              <li key={i} className="sheet-col">
                <span className="sheet-col-no"><i>{String(i + 1).padStart(2, "0")}</i></span>
                <span className="sheet-col-en"><i>{c.en}</i></span>
                <h4>{c.label}</h4>
                <p>{c.desc}</p>
              </li>
            ))}
          </ul>

          <div className="sheet-process">
            <span className="eyebrow centered"><i>Weekly Loop</i></span>
            <h3 className="sheet-process-title">
              週次で「<em>解く → 解体 → 設計し直す</em>」を回し続ける。
            </h3>
            <ol className="sheet-process-list">
              <li>
                <span className="spx-no"><i>01</i></span>
                <h4>過去問を時間内で解く</h4>
                <p>本番と同じ時間配分・解く順序で。経営なら60分・4題、文学部なら60分・3題。シミュレーション環境を再現します。</p>
              </li>
              <li>
                <span className="spx-no"><i>02</i></span>
                <h4>大問単位で解体する</h4>
                <p>大問ごとの実得点・予測点・予測時間・実時間・正答率を入力。設問タイプ別 (空所補充・内容一致・和訳など) でも分解。</p>
              </li>
              <li>
                <span className="spx-no"><i>03</i></span>
                <h4>定性的な詰まりを言語化</h4>
                <p>「コロケーションで迷う」「文構造を見失う」「日本語化で時間を使う」など、自分の崩れ方を毎回書き残します。</p>
              </li>
              <li>
                <span className="spx-no"><i>04</i></span>
                <h4>翌週の課題に書き換える</h4>
                <p>シートの定性メモから、翌週の演習内容・教材・量を逆算。「過去問を解く意味」を、毎週新しくします。</p>
              </li>
            </ol>
          </div>
        </div>
      </section>

      {/* Closing */}
      <section className="strategy-close">
        <div className="strategy-close-inner">
          <span className="eyebrow"><i>Your Faculty</i></span>
          <h2 className="strategy-close-title">
            あなたの志望学部の過去問も、<br />
            <em>無料相談</em>で、その場で解体します。
          </h2>
          <p className="strategy-close-lead">
            申込時に志望大学・学部をお知らせください。相談当日までに過去問を解析し、<br />
            「あなたが、いま、どの大問でどれだけ伸ばせるか」を、シートにしてお渡しします。
          </p>
          <a href={window.THINKING_LINE_LIFF_URL} target="_blank" rel="noopener noreferrer" className="cta">
            無料相談で、自分の過去問を解体する
            <svg className="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M5 12h14M13 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      </section>
    </>
  );
};

// Side-by-side comparison column
const CompareColumn = ({ data }) => {
  return (
    <article className={`compare-col accent-${data.accent}`}>
      <header className="compare-col-head">
        <span className="compare-col-en"><i>{data.facultyEn}</i></span>
        <h3 className="compare-col-jp">{data.faculty}</h3>
        <p className="compare-col-tag">「{data.tagline}」</p>
      </header>

      <ul className="compare-meta">
        <li>
          <span className="cm-label">試験時間</span>
          <span className="cm-value"><em>{data.timeMin}</em><i>min</i></span>
        </li>
        <li>
          <span className="cm-label">大問数</span>
          <span className="cm-value"><em>{data.questionCount}</em><i>題</i></span>
        </li>
        <li>
          <span className="cm-label">出題形式</span>
          <span className="cm-value-text">{data.shape}</span>
        </li>
      </ul>
      <p className="compare-shape-note">{data.shapeNote}</p>

      <div className="compare-daimon-label">
        <span><i>Question Breakdown</i></span>
        <em>大問構成</em>
      </div>

      <ol className="compare-daimon">
        {data.daimon.map((d, i) => (
          <li key={i} className="daimon-item">
            <div className="daimon-head">
              <span className="daimon-no"><i>{d.no}</i></span>
              <div>
                <h5 className="daimon-type">{d.type}</h5>
                <p className="daimon-ask">{d.ask}</p>
              </div>
            </div>
            <div className="daimon-required">
              <span className="dr-label">求められる力</span>
              <span className="dr-text">{d.required}</span>
            </div>
            <p className="daimon-detail">{d.detail}</p>
          </li>
        ))}
      </ol>

      <div className="compare-verdict">
        <span className="verdict-mark">“</span>
        <p>{data.verdict}</p>
      </div>
    </article>
  );
};

window.StrategyPage = StrategyPage;
