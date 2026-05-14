// Capacity — limited enrollment / one student × one coach × daily tracking
const Capacity = () => {
  const ref = React.useRef(null);
  const [shown, setShown] = React.useState(false);

  React.useEffect(() => {
    const io = new IntersectionObserver(
      ([e]) => { if (e.isIntersecting) setShown(true); },
      { threshold: 0.25 }
    );
    if (ref.current) io.observe(ref.current);
    return () => io.disconnect();
  }, []);

  // Live progress entries — what one coach tracks daily for one student
  const trackEntries = [
    { day: "Mon", task: "英語長文 / 早稲田法 過去問", val: "2題", pct: 92, note: "論理把握◯" },
    { day: "Tue", task: "古文単語 / 200語チェック", val: "194/200", pct: 97, note: "復習要：6語" },
    { day: "Wed", task: "小論文 添削提出", val: "1本", pct: 80, note: "論証B+ / 構造A" },
    { day: "Thu", task: "現代文 / 抽象論文 精読", val: "3題", pct: 88, note: "良" },
    { day: "Fri", task: "面談（週次）", val: "60分", pct: 100, note: "次週方針更新" },
  ];

  return (
    <section className="section capacity-section" id="capacity" ref={ref}>
      <div className="capacity-bg" />
      <div className="capacity-grain" />

      <div className="section-inner capacity-inner">
        <div className="capacity-head">
          <span className="eyebrow"><i>Capacity / 定員制</i></span>
          <h2 className="capacity-title">
            ひとりに、<em>ひとり</em>。<br />
            だから、人数を<em>絞る。</em>
          </h2>
          <div className="ornament"><span className="ornament-mark" /></div>
        </div>

        <div className={`capacity-grid ${shown ? "in" : ""}`}>
          {/* Left — narrative */}
          <div className="capacity-text">
            <p className="capacity-lead">
              ひとりの生徒に、<br />
              <span className="hl">専属の担当コーチ</span>がつきます。
            </p>
            <p className="capacity-body">
              週次面談で進路を更新し、毎日の学習量・正答率・添削の出来までを<span className="hl">数字で追跡</span>。<br />
              ひとりひとりに、これだけの密度で関わるためには、預かれる人数に<span className="hl">必ず限り</span>があります。
            </p>

            <ul className="capacity-points">
              <li>
                <span className="bullet" />
                <span>
                  <b>専属コーチ × 1名</b>
                  <i>志望学部・性格・学習スタイルから、最適な1名をマッチング。</i>
                </span>
              </li>
              <li>
                <span className="bullet" />
                <span>
                  <b>1コーチが見る生徒数：最大8名</b>
                  <i>これ以上は、毎日の進捗まで丁寧に把握できないから。</i>
                </span>
              </li>
              <li>
                <span className="bullet" />
                <span>
                  <b>新規受け入れ：月10名まで</b>
                  <i>合格設計図の作成と初期マッチングに時間を割くため、慎重に。</i>
                </span>
              </li>
            </ul>

            <p className="capacity-quote">
              「<em>全員に同じ授業</em>」では、ひとりも見えなくなる。<br />
              だから THINKING は、<em>見える人数</em>しか預かりません。
            </p>
          </div>

          {/* Right — One student dashboard */}
          <div className="capacity-visual">
            <div className="capacity-card">
              <header className="capacity-card-head">
                <div>
                  <span className="capacity-card-label"><i>One Student · One Coach</i></span>
                  <span className="capacity-card-sub">担当生徒カルテ（サンプル）</span>
                </div>
                <span className="capacity-card-status">
                  <span className="status-dot" />
                  伴走中
                </span>
              </header>

              {/* Pairing visualization */}
              <div className="pair-block">
                <div className="pair-side pair-student">
                  <span className="pair-label"><i>Student</i></span>
                  <div className="pair-avatar">
                    <span className="pair-mark">M</span>
                  </div>
                  <span className="pair-name">M.K. さん</span>
                  <span className="pair-meta">高3 / 早稲田法 志望</span>
                </div>

                <div className="pair-link">
                  <span className="pair-link-line" />
                  <span className="pair-link-text"><i>1 : 1</i></span>
                  <span className="pair-link-line" />
                </div>

                <div className="pair-side pair-coach">
                  <span className="pair-label"><i>Dedicated Coach</i></span>
                  <div className="pair-avatar coach">
                    <span className="pair-mark">中</span>
                  </div>
                  <span className="pair-name">中山 塁 コーチ</span>
                  <span className="pair-meta">早稲田大学 商学部卒 / 指導歴9年</span>
                </div>
              </div>

              {/* Daily tracking table */}
              <div className="track-block">
                <div className="track-head">
                  <span className="track-title"><i>Daily Tracking</i> 今週の進捗（5/12 –)</span>
                  <span className="track-status">数値で管理</span>
                </div>
                <ul className="track-list">
                  {trackEntries.map((t, i) => (
                    <li
                      key={i}
                      className="track-row"
                      style={{ transitionDelay: `${i * 80}ms` }}
                    >
                      <span className="track-day"><i>{t.day}</i></span>
                      <span className="track-task">{t.task}</span>
                      <span className="track-val">{t.val}</span>
                      <span className="track-bar">
                        <span
                          className="track-bar-fill"
                          style={{ width: shown ? `${t.pct}%` : "0%", transitionDelay: `${i * 80 + 200}ms` }}
                        />
                      </span>
                      <span className="track-note">{t.note}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Coach load — how many students this coach has */}
              <div className="load-block">
                <div className="load-head">
                  <span className="load-label"><i>Coach Load</i> 中山コーチの担当人数</span>
                  <span className="load-val"><i>6</i> / 8 名</span>
                </div>
                <div className="load-dots">
                  {Array.from({ length: 8 }).map((_, i) => (
                    <span
                      key={i}
                      className={`load-dot ${i < 6 ? "filled" : "open"}`}
                      style={{ transitionDelay: `${i * 60}ms` }}
                    />
                  ))}
                </div>
                <p className="load-note">
                  ※ 1コーチが日々の進捗まで責任を持って追える上限は、私たちの経験上8名。
                </p>
              </div>

              <footer className="capacity-card-foot">
                <span>※ 本人の承諾を得たサンプルデータです。実名・志望は加工しています。</span>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

window.Capacity = Capacity;
