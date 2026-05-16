/* Smart Study English — wireframe sections */

function sseLineUrl() {
  return window.THINKING_LINE_LIFF_URL || "#";
}

/* =====================================================
   AUTHORITY — 権威性
===================================================== */
function AuthoritySection() {
  const operatingResults = [
    {
      thumb: "../../assets/media-r25-1.png",
      url: "https://r25.jp/companies/all-day-thinking/interview/1026804627472908290",
      label: "新R25 塾代表インタビュー",
    },
    {
      thumb: "../../assets/media-r25-2.png",
      url: "https://r25.jp/companies/all-day-thinking/interview/970960432984489985",
      label: "新R25 英語指導インタビュー",
    },
    {
      thumb: "../../assets/media-tv.png",
      url: "https://powered-by-tv.com/2023/08/12/powernews11/",
      label: "東京MX 地上波テレビ出演",
    },
  ];

  const trustPills = [
    { label: "法人運営", sub: "合同会社ARC" },
    { label: "2000名以上", sub: "指導実績" },
  ];

  const achievements = [
    "偏差値50台高校から、早慶全勝 → 慶應大学法学部 進学",
    "通信制高校から、全国1位 → 早稲田大学法学部・社会科学部 合格",
    "野球部マネージャー、夏前過去問30% → 早稲田大学文学部 現役合格",
    "高3 11月まで部活、E判定 → 青山学院大学 現役合格",
    "非進学校から、MARCH全勝合格",
  ];

  return (
    <section id="authority" className="sse-authority theme-paper">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">01</div>
          <div>
            <span className="eyebrow">TRUST / AUTHORITY</span>
            <h2 className="section-title">社会から認められた、<br /><em>確かな実績。</em></h2>
            <p className="section-lead">
              運営塾 <strong>THINKING</strong> のメディア掲載・取材実績です。タップで記事へ。
            </p>
          </div>
        </div>

        <div className="sse-operating-results">
          <h3 className="sse-operating-label">運営塾の実績</h3>
          <div className="sse-thumb-carousel">
            <div className="sse-thumb-track" role="list">
              {operatingResults.map((item, i) => (
                <a
                  key={i}
                  href={item.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="sse-thumb-slide"
                  role="listitem"
                  aria-label={item.label}
                >
                  <img src={item.thumb} alt={item.label} width="640" height="360" loading="lazy" />
                </a>
              ))}
            </div>
          </div>
        </div>

        <ul className="sse-trust-pills">
          {trustPills.map((t, i) => (
            <li key={i}>
              <strong>{t.label}</strong>
              <span>{t.sub}</span>
            </li>
          ))}
        </ul>

        <div className="sse-achieve-block">
          <h3 className="sse-achieve-title">▼ 運営塾 THINKING の合格実績</h3>
          <ul className="sse-achieve-list">
            {achievements.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   EMPATHY — 共感
===================================================== */
function EmpathySection() {
  const pains = [
    "単語をいくら覚えても、長文の意味が取れない",
    "試験で時間が足りず、最後まで解けない",
    "文法を理解しているのに、応用問題で詰まる",
    "努力しても、点数が比例して伸びない",
    "何が原因かわからないまま、時間だけが過ぎる",
  ];

  return (
    <section id="empathy" className="sse-empathy">
      <div className="sse-empathy-hero">
        <div className="sse-empathy-visual">
          <img
            src="assets/empathy-student.png"
            alt="勉強しているのに英語が伸び悩む高校生"
            width="1024"
            height="768"
            loading="lazy"
          />
          <div className="sse-empathy-overlay">
            <span className="sse-empathy-eyebrow">
              <span className="sse-empathy-num">02</span> EMPATHY
            </span>
            <h2 className="sse-empathy-title">
              なぜ、こんなに勉強してるのに<br />
              <em>英語が伸びないんだろう。</em>
            </h2>
          </div>
        </div>
      </div>

      <div className="sse-empathy-body wrap">
        <p className="sse-empathy-lead">
          時間も労力もかけている。それなのに、思うように点数が上がらない。そう感じたことはありませんか？
        </p>

        <ul className="sse-pain-list">
          {pains.map((p, i) => (
            <li key={i}><span className="sse-check">✓</span>{p}</li>
          ))}
        </ul>

        <div className="sse-empathy-close">
          <p>それは、努力不足でも、能力不足でもありません。</p>
          <p><strong>原因は、もっと根本的なところにあります。</strong></p>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   ROADMAP — 45日間の流れ
===================================================== */
function RoadmapSection() {
  const steps = [
    {
      tag: "STEP 1",
      title: "スタート面談（Day 0）",
      body: "あなたの現在の状況・目標を確認し、45日後のゴールを一緒に設計します。",
    },
    {
      tag: "STEP 2",
      title: "集中トレーニング期（Day 1〜33）",
      body: "毎日の動画講義 + 課題提出 + フィードバック。朝ミッション配信、日中に取り組み、夜に提出。読み方が確実に変わっていきます。",
    },
    {
      tag: "STEP 3",
      title: "定着・応用期（Day 34〜45）",
      body: "身につけた読み方を過去問や実践問題で完成。「読める」から「使える」への移行です。",
    },
    {
      tag: "STEP 4",
      title: "アフター面談（Day 45以降）",
      body: "45日間で身についた力を一緒に確認。これからの学習の指針を明確にします。",
    },
  ];

  return (
    <section id="roadmap" className="sse-roadmap theme-deep-gold">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">—</div>
          <div>
            <span className="eyebrow">45-DAY ROADMAP</span>
            <h2 className="section-title">45日間で、<br /><em>どう変わるのか。</em></h2>
            <p className="section-lead">
              段階的に「読み方」を変えていく、45日間のロードマップです。
            </p>
          </div>
        </div>

        <div className="sse-roadmap-steps">
          {steps.map((s, i) => (
            <article key={i} className="sse-roadmap-step">
              <span className="sse-roadmap-tag">{s.tag}</span>
              <h3>{s.title}</h3>
              <p>{s.body}</p>
            </article>
          ))}
        </div>

        <p className="sse-roadmap-summary">
          スタート面談 → <strong>33日集中</strong> → <strong>12日定着</strong> → アフター面談<br />
          この45日間で、英語の読み方は完全に変わります。
        </p>
      </div>
    </section>
  );
}

/* =====================================================
   ROUTINE — 1日のルーティン
===================================================== */
function RoutineSection() {
  const blocks = [
    { time: "朝 05:00", icon: "📩", title: "今日のミッションが届く", desc: "その日にやるべきことが LINE で自動配信。「何をやるか迷う」時間をゼロに。" },
    { time: "日中（30分程度）", icon: "📚", title: "隙間時間で取り組む", desc: "通学中、休み時間、寝る前。1日30分ほどの積み重ねで、読み方が変わっていきます。" },
    { time: "夜 22:30まで", icon: "📝", title: "提出 → フィードバック", desc: "その日の課題を提出。個別にコメント・フィードバックが返ってきます。" },
  ];

  const supports = [
    "LINE で質問し放題（24時間以内に返信）",
    "受講生コミュニティで仲間と励まし合える",
    "動画講義は何度でも見返せる",
  ];

  return (
    <section id="routine" className="sse-routine theme-paper">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">—</div>
          <div>
            <span className="eyebrow">DAILY ROUTINE</span>
            <h2 className="section-title">1日たった30分。<br /><em>続けられる仕組み。</em></h2>
            <p className="section-lead">
              「忙しくて続けられないかも」という不安を、仕組みで解消します。<br />
              部活・課題・習い事… そんな日々の中でも、確実に続けられる設計です。
            </p>
          </div>
        </div>

        <div className="sse-routine-timeline">
          {blocks.map((b, i) => (
            <article key={i} className="sse-routine-block">
              <span className="sse-routine-time">{b.time}</span>
              <span className="sse-routine-icon" aria-hidden="true">{b.icon}</span>
              <h3>{b.title}</h3>
              <p>{b.desc}</p>
            </article>
          ))}
        </div>

        <div className="sse-routine-support">
          <h3>▼ 支援体制</h3>
          <ul>
            {supports.map((s, i) => (
              <li key={i}><span>✓</span>{s}</li>
            ))}
          </ul>
          <p className="sse-routine-note">
            忙しい毎日でも、続けられる。そう設計されているから、<strong>2000名以上の生徒が完走</strong>してきました。
          </p>
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   PROGRAM CONTENTS — プログラム内容
===================================================== */
function ProgramContentsSection() {
  const items = [
    { icon: "📹", title: "動画講義（50本以上）", desc: "読み方の本質をわかりやすく解説。何度でも見返せます。" },
    { icon: "📖", title: "電子教材（60コンテンツ）", desc: "プロが英文を読むときの「思考回路」を完全可視化。今まで誰も教えてくれなかった部分を言語化。" },
    { icon: "📄", title: "オリジナル教材（PDF）", desc: "2000名以上が学んだ実証済み教材。スマホ・PCで閲覧可能。" },
    { icon: "✏️", title: "課題と模範解答", desc: "毎日の課題で確実に身につける。個別フィードバック付き。" },
    { icon: "💬", title: "LINE質問サポート", desc: "24時間以内に返信。「わからない」を残しません。" },
    { icon: "👥", title: "受講生コミュニティ", desc: "仲間と一緒に頑張れる環境。モチベーション維持にも。" },
    { icon: "🎤", title: "スタート面談（45分）", desc: "あなただけの学習計画を作成。" },
    { icon: "🎤", title: "アフター面談（45分）", desc: "45日後、身についた力を確認。" },
    { icon: "⭐", title: "塾生限定ライブ英語特訓", desc: "THINKING 塾生だけが参加できる週1ライブ特訓にモニター生として特別招待（45日間で6〜7回）。" },
    { icon: "📜", title: "修了テスト + 修了証", desc: "45日後の到達点を確認。" },
  ];

  return (
    <section id="contents" className="sse-program-contents">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">—</div>
          <div>
            <span className="eyebrow">PROGRAM</span>
            <h2 className="section-title">45日間に含まれる、<br /><em>すべて。</em></h2>
            <p className="section-lead">
              スタート面談から、修了テストまで。<br />
              読み方を変えるために必要な、すべてを揃えました。
            </p>
          </div>
        </div>

        <div className="sse-prog-list">
          {items.map((item, i) => (
            <article key={i} className="sse-prog-item">
              <span className="sse-prog-icon" aria-hidden="true">{item.icon}</span>
              <div>
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

/* =====================================================
   APPLY FLOW — 申込みの流れ
===================================================== */
function ApplyFlowSection() {
  const steps = [
    { num: "01", title: "申込みフォーム入力", desc: "下のボタンから申込みフォームへ。3分で完了。" },
    { num: "02", title: "スタート日の決定", desc: "申込み後、スタート日のご案内をお送りします。ご都合に合わせて開始日を選べます。" },
    { num: "03", title: "お支払い", desc: "銀行振込にてお支払いください。（三井住友銀行 / 合同会社ARC法人口座）入金確認後、プログラムスタート。" },
    { num: "04", title: "プログラム開始", desc: "スタート日から、45日間のプログラムが始まります。全力でサポートします。" },
  ];

  return (
    <section id="flow" className="sse-apply-flow theme-paper">
      <div className="wrap">
        <div className="section-head">
          <div className="section-num">—</div>
          <div>
            <span className="eyebrow">HOW TO JOIN</span>
            <h2 className="section-title">申込みは、<br /><em>シンプル4ステップ。</em></h2>
            <p className="section-lead">迷っている方は、まず公式LINEで個別相談も可能です。</p>
          </div>
        </div>

        <div className="sse-flow-steps">
          {steps.map((s, i) => (
            <article key={i} className="sse-flow-step">
              <span className="sse-flow-num">STEP {s.num}</span>
              <h3>{s.title}</h3>
              <p>{s.desc}</p>
            </article>
          ))}
        </div>

        <div className="sse-flow-cta">
          <a href="#cta" className="btn-primary big">申込みフォームへ進む <span className="arrow">→</span></a>
          <p className="sse-flow-line-lead">「自分に合うか不安…」「もう少し詳しく知りたい…」</p>
          <a href={sseLineUrl()} target="_blank" rel="noopener noreferrer" className="hero-m-cta-line sse-flow-line-btn">
            公式LINEで相談する
          </a>
          <p className="sse-flow-note">強引な勧誘は一切ありません。</p>
        </div>
      </div>
    </section>
  );
}

window.AuthoritySection = AuthoritySection;
window.EmpathySection = EmpathySection;
window.RoadmapSection = RoadmapSection;
window.RoutineSection = RoutineSection;
window.ProgramContentsSection = ProgramContentsSection;
window.ApplyFlowSection = ApplyFlowSection;
