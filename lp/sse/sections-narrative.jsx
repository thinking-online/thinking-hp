/* Smart Study English — 3つの理由 + サポート4点（ナラティブ強化） */

/* =====================================================
   THREE REASONS — 英語が読めない「構造的理由」
===================================================== */
function ThreeReasonsSection() {
  const reasons = [
    {
      num: "01",
      tag: "VOCAB",
      title: "単語を「英和＝一対一」で丸暗記している",
      lead: "小テストでは通っても、英文を読む力にはつながらない。",
      body:
        "command＝「命じる」と覚えても、文中では command of English（運用力）や has the command of（〜を見渡す）で意味がつながらない。英語を「読む」ための語彙力は、和訳リストの暗記では育ちません。",
      pull: "丸暗記のままでは、一文の中で単語が「生きている意味」を取りこぼす。",
    },
    {
      num: "02",
      tag: "GRAMMAR",
      title: "文法を「ルールの暗記」だと思い込んでいる",
      lead: "用法の分類を覚えても、長文の処理速度は上がらない。",
      body:
        "不定詞の3用法、関係詞の識別… ラベル貼りの暗記は、試験本番の初見英文では使えません。ネイティブが頭の中でしているのは「ルール当て」ではなく、文の骨格と意味の流れの把握です。",
      pull: "「理解」の伴わない丸暗記は、読解の現場では無力化します。",
    },
    {
      num: "03",
      tag: "READING",
      title: "「左から右に読む」方法を、誰も最初から教えてくれない",
      lead: "日本語は構造が違う。だから英語は「別の読み方」が必要なのに。",
      body:
        "難しい語彙がなくても、意味が取れるかどうかは「読み方の型」で決まります。学校でも予備校でも、知識は積み上げられても「処理のフォーム」は放置されがち。だから努力の割に伸びない状態が続きます。",
      pull: "知識の前に、脳の使い方の順番が逆転しているのです。",
    },
  ];

  return (
    <section
      id="three-reasons"
      className="sse-three-reasons theme-paper"
      data-screen-label="Three Reasons"
    >
      <div className="wrap">
        <div className="section-head">
          <div className="section-num sse-narrative-num">III</div>
          <div>
            <span className="eyebrow">THREE STRUCTURAL TRAPS</span>
            <h2 className="section-title">
              あなたは悪くない。<br />
              <em>英語が読めない、3つの理由。</em>
            </h2>
            <p className="section-lead">
              努力不足でも、センスの問題でもありません。<br />
              日本の英語学習で「そもそも育たない設計」になっているだけです。
            </p>
          </div>
        </div>

        <figure className="sse-three-hero-visual">
          <img
            src="assets/three-reasons-hero.png"
            alt="英語が読めず悩む女子学生"
            width="1024"
            height="576"
            loading="lazy"
            decoding="async"
          />
          <figcaption className="sse-three-hero-caption">
            読めないのは才能不足ではない。多くは、
            <strong>設計ミス</strong>で起きています。
          </figcaption>
        </figure>

        <div className="sse-three-grid" role="list">
          {reasons.map((r) => (
            <article key={r.num} className="sse-three-card" role="listitem">
              <div className="sse-three-card-top">
                <span className="sse-three-num" aria-hidden="true">
                  {r.num}
                </span>
                <span className="sse-three-tag">{r.tag}</span>
              </div>
              <h3 className="sse-three-title">{r.title}</h3>
              <p className="sse-three-lead">{r.lead}</p>
              <p className="sse-three-body">{r.body}</p>
              <p className="sse-three-pull">
                <span className="sse-three-pull-mark" aria-hidden="true">
                  →
                </span>
                {r.pull}
              </p>
            </article>
          ))}
        </div>

        <div className="sse-three-bridge">
          <div className="sse-three-bridge-line" aria-hidden="true" />
          <p>
            SSE は、この3つを一度に解体し、<strong>「読める脳のフォーム」</strong>
            から入り直す45日間です。
          </p>
          <div className="sse-three-bridge-line" aria-hidden="true" />
        </div>
      </div>
    </section>
  );
}

window.ThreeReasonsSection = ThreeReasonsSection;

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
