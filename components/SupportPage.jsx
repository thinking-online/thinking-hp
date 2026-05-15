// Support page — exhaustive walkthrough of the 6 mechanisms
// (Strategy / Curriculum / Roadmap / Quality / Mindset / Verbalize)

const SupportPage = () => {
  return (
    <>
      <PageHeader
        en="Support / Six Mechanisms"
        eyebrow="サポート体制"
        jp={<>合格を、<em>設計</em>する。<br /><em>6つの仕組み</em>のすべて。</>}
        lead="THINKING のサポートは、月1の面談で完結しません。戦略設計から日々の質問対応まで——合格までの全工程を6つの仕組みで支えます。このページでは、その一つひとつを徹底的に解説します。"
        bgImage="assets/campus-04.png"
      />

      {/* Intro / Index */}
      <SupportIntro />

      {/* The 6 mechanisms */}
      <Mech01Strategy />
      <Mech02Curriculum />
      <Mech03Roadmap />
      <Mech04Quality />
      <Mech05Mindset />
      <Mech06Verbalize />

      {/* How they interlock */}
      <SupportInterlock />

      {/* Final LINE CTA — reuse the global section */}
      <SupportLineCTA />
    </>
  );
};

/* =====================================================================
 *  Intro / 6 mechanism index
 * ===================================================================== */

const SupportIntro = () => {
  const items = [
    { no: "01", en: "Strategy", jp: "大学・学部別の完全カスタム戦略", anchor: "strategy" },
    { no: "02", en: "Curriculum", jp: "週次の学習計画 / PDCA", anchor: "curriculum" },
    { no: "03", en: "Roadmap", jp: "合格までの完全ロードマップ", anchor: "roadmap" },
    { no: "04", en: "Quality", jp: "24時間質問システム", anchor: "quality" },
    { no: "05", en: "Mindset", jp: "週次面談で、迷う暇を与えない", anchor: "mindset" },
    { no: "06", en: "Verbalize", jp: "わかる→解ける、『言語化特訓』", anchor: "verbalize" },
  ];

  return (
    <section className="sup-intro">
      <div className="sup-intro-inner">
        <div className="sup-intro-head">
          <span className="eyebrow"><i>Why It Works</i></span>
          <h2 className="sup-intro-title">
            <em>仕組み</em>がない伴走は、<br />
            <em>気合い</em>で終わる。
          </h2>
          <p className="sup-intro-lead">
            「やる気を出して」「とにかく頑張ろう」で、合格はしない。<br />
            THINKING は、根性ではなく<em>仕組み</em>で生徒を支えます。<br />
            戦略・計画・ロードマップ・質問・面談・言語化——<br />
            6つが噛み合って、初めて伴走と呼べます。
          </p>
        </div>

        <ol className="sup-intro-index">
          {items.map((it) => (
            <li key={it.no}>
              <a href={`#${it.anchor}`}>
                <span className="sup-intro-no"><i>{it.no}</i></span>
                <span className="sup-intro-en"><i>{it.en}</i></span>
                <span className="sup-intro-jp">{it.jp}</span>
                <span className="sup-intro-arrow" aria-hidden="true">↓</span>
              </a>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
};

/* =====================================================================
 *  Reusable section header for each mechanism
 * ===================================================================== */

const MechHead = ({ no, en, jp, title, lead }) => (
  <header className="mech-head">
    <div className="mech-head-no">
      <span className="mech-no"><i>{no}</i></span>
      <span className="mech-no-line" />
      <span className="mech-en"><i>{en}</i></span>
    </div>
    <span className="mech-jp-tag">{jp}</span>
    <h2 className="mech-title">{title}</h2>
    {lead && <p className="mech-lead">{lead}</p>}
  </header>
);

/* placeholder image block */
const ImgPH = ({ label, ratio = "16 / 10", note }) => (
  <div className="img-ph" style={{ aspectRatio: ratio }}>
    <div className="img-ph-frame">
      <span className="img-ph-corner img-ph-tl" />
      <span className="img-ph-corner img-ph-tr" />
      <span className="img-ph-corner img-ph-bl" />
      <span className="img-ph-corner img-ph-br" />
      <div className="img-ph-body">
        <span className="img-ph-tag"><i>Image</i></span>
        <span className="img-ph-label">{label}</span>
        {note && <span className="img-ph-note">{note}</span>}
      </div>
    </div>
  </div>
);

/* =====================================================================
 *  01 — Strategy
 * ===================================================================== */

const Mech01Strategy = () => {
  const steps = [
    {
      no: "Step 01",
      title: "ヒアリング（90分）",
      desc: "志望学部・現状学力・通学・部活・性格・家庭環境まで。現状を360度から把握します。",
    },
    {
      no: "Step 02",
      title: "学力診断テスト",
      desc: "英語・国語・選択科目を実施。模試の点数では見えない、単元別の穴・癖を特定。",
    },
    {
      no: "Step 03",
      title: "志望学部の合格点を分解",
      desc: "学部別に「何点取れば受かるか」を明確化。配点・出題形式・時間配分まで分解します。",
    },
    {
      no: "Step 04",
      title: "個別戦略書の作成",
      desc: "ギャップを埋める順序・教材・時間配分を、A4 4–6枚の戦略書に。本人と保護者にも共有。",
    },
  ];

  const inputs = [
    { label: "志望学部", value: "早稲田 商 / 慶應 経済 / 上智 経済" },
    { label: "残り期間", value: "10ヶ月" },
    { label: "現状偏差値", value: "英語 58 / 国語 52 / 日本史 49" },
    { label: "1日学習可能時間", value: "平日 4h / 休日 9h" },
    { label: "苦手単元", value: "英語長文・古文文法・近現代史" },
    { label: "性格傾向", value: "完璧主義・先延ばし傾向" },
  ];

  return (
    <section className="mech-section mech-01" id="strategy">
      <div className="mech-inner">
        <MechHead
          no="01"
          en="Strategy"
          jp="戦略設計"
          title={<>大学・学部別の<br /><em>完全カスタム戦略</em>。</>}
          lead="受験戦略は、人によってまるで違う。志望学部・現状学力・残り期間・性格——あらゆる変数から、合格点までの最短ルートを個別に設計します。テンプレートは使いません。"
        />

        {/* 4-step process */}
        <div className="mech-block">
          <h3 className="mech-h3">入塾後 14日間で、<em>戦略書</em>を完成させる。</h3>
          <ol className="mech-steps">
            {steps.map((s, i) => (
              <li key={i} className="mech-step">
                <span className="mech-step-no"><i>{s.no}</i></span>
                <h4>{s.title}</h4>
                <p>{s.desc}</p>
              </li>
            ))}
          </ol>
        </div>

        {/* input → output diagram */}
        <div className="mech-strategy-diag">
          <div className="strategy-inputs">
            <span className="strategy-col-label"><i>Inputs / 入力</i></span>
            <ul>
              {inputs.map((x, i) => (
                <li key={i}>
                  <span className="strategy-input-label">{x.label}</span>
                  <span className="strategy-input-value">{x.value}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="strategy-arrow" aria-hidden="true">
            <span className="strategy-arrow-line" />
            <span className="strategy-arrow-tag"><i>Custom Design</i></span>
            <span className="strategy-arrow-line" />
          </div>

          <div className="strategy-output">
            <span className="strategy-col-label"><i>Output / 戦略書</i></span>
            <ImgPH
              label="個別戦略書（A4 4–6ページ）"
              note="※ 後日、実際の戦略書サンプル画像を差し替え"
              ratio="3 / 4"
            />
          </div>
        </div>

        <div className="mech-callout">
          <span className="mech-callout-mark"><i>Quote</i></span>
          <p>
            「全範囲を完璧に」は、志望校が決まっていないときの言葉。<br />
            <em>志望学部が決まった瞬間、やるべきことは半分以下になる。</em>
          </p>
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  02 — Curriculum / PDCA
 * ===================================================================== */

const Mech02Curriculum = () => {
  const pdca = [
    { letter: "P", en: "Plan", title: "計画", desc: "毎週日曜、翌週のタスクをコーチと一緒に設計。教材・ページ数・所要時間まで。" },
    { letter: "D", en: "Do", title: "実行", desc: "平日は本人主導で実行。朝のタスク配信、夜の完了報告で進捗を可視化。" },
    { letter: "C", en: "Check", title: "確認", desc: "週末に達成率・正答率・所要時間をレビュー。コーチが3観点で評価。" },
    { letter: "A", en: "Act", title: "改善", desc: "未達タスクの原因を分析。翌週の計画に反映。同じ失敗を、二度繰り返させない。" },
  ];

  return (
    <section className="mech-section mech-02" id="curriculum">
      <div className="mech-inner">
        <MechHead
          no="02"
          en="Curriculum"
          jp="週次PDCA"
          title={<>1週間単位の精緻な計画と、<br /><em>月次の到達度レビュー</em>。</>}
          lead="「今週、何をどこまでやるか」が曖昧なまま机に向かう生徒は、必ず迷子になります。THINKING は週ごとにPDCAを回し、毎週月曜の朝、やるべきことが明確な状態でスタートさせます。"
        />

        {/* PDCA loop */}
        <div className="mech-block">
          <h3 className="mech-h3">毎週まわす、<em>4つの動作</em>。</h3>
          <div className="pdca-grid">
            {pdca.map((p, i) => (
              <article key={i} className="pdca-card">
                <span className="pdca-letter">{p.letter}</span>
                <span className="pdca-en"><i>{p.en}</i></span>
                <h4>{p.title}</h4>
                <p>{p.desc}</p>
              </article>
            ))}
          </div>
        </div>

        {/* Notion / sheet placeholder + sample numbers */}
        <div className="mech-block mech-curriculum-grid">
          <div className="mech-curriculum-img">
            <ImgPH
              label="進捗管理シート（Notion）"
              note="※ 後日、実際の管理画面の画像をここに差し替え"
              ratio="16 / 10"
            />
            <p className="mech-img-cap">
              タスク・所要時間・達成率・コーチコメントを、1画面に集約。<br />
              本人・コーチ・保護者の3者が、同じ画面を見ながら走ります。
            </p>
          </div>

          <div className="mech-curriculum-stats">
            <span className="mech-stats-label"><i>Real Numbers / ある生徒の1週間</i></span>
            <ul className="mech-stats-list">
              <li>
                <span className="mech-stats-num">37<i>h</i></span>
                <span className="mech-stats-jp">週間学習時間</span>
              </li>
              <li>
                <span className="mech-stats-num">42<i>個</i></span>
                <span className="mech-stats-jp">完了タスク数</span>
              </li>
              <li>
                <span className="mech-stats-num">93<i>%</i></span>
                <span className="mech-stats-jp">計画達成率</span>
              </li>
              <li>
                <span className="mech-stats-num">4<i>件</i></span>
                <span className="mech-stats-jp">未達 → 翌週繰越</span>
              </li>
            </ul>
            <p className="mech-stats-note">
              「やった / やってない」では終わらせない。<br />
              数字で見続けることで、来週の計画は今週より確実に精緻になります。
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  03 — Roadmap
 * ===================================================================== */

const Mech03Roadmap = () => {
  const phases = [
    { period: "4–6月", phase: "Phase 1", title: "基礎完成期", desc: "英単語・文法・古文単語・選択科目の基礎インプット。「全範囲を一周」が目標。" },
    { period: "7–8月", phase: "Phase 2", title: "応用演習期", desc: "夏で一気に演習量を稼ぐ。長文・記述・整序問題を週2セットペース。" },
    { period: "9–10月", phase: "Phase 3", title: "過去問導入期", desc: "第二志望校から過去問着手。出題傾向を体に入れ、戦略を再調整。" },
    { period: "11–12月", phase: "Phase 4", title: "第一志望対策期", desc: "本命校の過去問を10年分以上。時間配分・捨て問判断まで体得。" },
    { period: "1–2月", phase: "Phase 5", title: "実戦・本番期", desc: "私大入試→国公立2次の連戦。コンディション管理と最後のミスつぶし。" },
  ];

  return (
    <section className="mech-section mech-03" id="roadmap">
      <div className="mech-inner">
        <MechHead
          no="03"
          en="Roadmap"
          jp="完全ロードマップ"
          title={<>合格までの、<br /><em>揺らがない設計図</em>。</>}
          lead="全範囲をいつ終え、いつ過去問に入るか。受験本番から逆算した5フェーズのロードマップで、生徒は「次に何をやるか」を、いつでも遠くまで見渡せます。"
        />

        {/* Horizontal timeline */}
        <div className="mech-block">
          <h3 className="mech-h3">本番から逆算した、<em>5つのフェーズ</em>。</h3>
          <div className="roadmap-rail">
            <div className="roadmap-rail-line" />
            <ol className="roadmap-phases">
              {phases.map((p, i) => (
                <li key={i} className="roadmap-phase" style={{ "--i": i }}>
                  <span className="roadmap-dot" />
                  <span className="roadmap-period"><i>{p.period}</i></span>
                  <span className="roadmap-phase-tag"><i>{p.phase}</i></span>
                  <h4>{p.title}</h4>
                  <p>{p.desc}</p>
                </li>
              ))}
            </ol>
          </div>
        </div>

        <div className="mech-block">
          <ImgPH
            label="ロードマップ全体図（科目別×月別）"
            note="※ 後日、実際の生徒ロードマップ画像をここに差し替え"
            ratio="21 / 9"
          />
          <p className="mech-img-cap">
            科目ごと・週ごとに、教材と進度を全て可視化。<br />
            「今、自分は受験全体のどこにいるか」が、一目で分かります。
          </p>
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  04 — Quality / 24h Q&A
 * ===================================================================== */

const Mech04Quality = () => {
  const responseLevels = [
    { plan: "Basic", time: "24時間以内", desc: "テキストでの返答。担当コーチが確実に対応。" },
    { plan: "Premium", time: "平均30分", desc: "テキスト＋必要に応じて音声/動画解説。" },
    { plan: "Elite", time: "即時", desc: "コーチに直電可。複雑な問題も画面共有で即解決。" },
  ];

  const chatLog = [
    { from: "student", time: "21:43", text: "この英文の it が指すものが2つあって、どっち取るべきか分かりません…" },
    { from: "student", time: "21:43", text: "（写真添付）", isImage: true },
    { from: "coach", time: "22:07", name: "中山コーチ", text: "前文の \"the policy\" が正解。it の直前にある \"the proposal\" は同格で説明している節だから、主語の候補にはなりにくい。" },
    { from: "coach", time: "22:08", name: "中山コーチ", text: "代名詞は「直前の名詞」じゃなく「直前の主語級の名詞」を取る、を原則にすると外しません。次に同じパターン来たら、構造図書いて送ってみて。" },
    { from: "student", time: "22:11", text: "なるほど！主語級ですね。今日の長文でもう一度試します🙏" },
  ];

  return (
    <section className="mech-section mech-04" id="quality">
      <div className="mech-inner">
        <MechHead
          no="04"
          en="Quality"
          jp="24時間質問システム"
          title={<>「<em>分からない</em>」を、<br />24時間以内に消す。</>}
          lead="独学の最大の敵は、分からないまま放置することです。THINKING はチャットで講師に直接質問でき、最短即時、遅くとも24時間以内に回答。学習が、止まりません。"
        />

        {/* Response time matrix */}
        <div className="mech-block">
          <h3 className="mech-h3">プラン別、<em>レスポンス品質</em>。</h3>
          <div className="quality-grid">
            {responseLevels.map((r, i) => (
              <article key={i} className="quality-card">
                <span className="quality-plan"><i>{r.plan}</i></span>
                <h4 className="quality-time">{r.time}</h4>
                <p>{r.desc}</p>
              </article>
            ))}
          </div>
        </div>

        {/* Chat mockup */}
        <div className="mech-block mech-quality-chat">
          <div className="chat-frame">
            <header className="chat-frame-head">
              <span className="chat-avatar" />
              <div className="chat-frame-meta">
                <span className="chat-frame-name">THINKING 質問チャット</span>
                <span className="chat-frame-sub">担当：中山コーチ（早稲田 商）</span>
              </div>
              <span className="chat-frame-status">
                <span className="status-dot" />Online
              </span>
            </header>

            <div className="chat-body">
              {chatLog.map((m, i) => (
                <div key={i} className={`chat-row chat-${m.from}`}>
                  {m.from === "coach" && <span className="chat-name">{m.name}</span>}
                  <div className={`chat-bubble ${m.isImage ? "is-image" : ""}`}>
                    {m.isImage ? (
                      <span className="chat-img-ph">
                        <i>question_photo.jpg</i>
                      </span>
                    ) : (
                      m.text
                    )}
                  </div>
                  <span className="chat-time">{m.time}</span>
                </div>
              ))}
            </div>

            <footer className="chat-frame-foot">
              <span className="chat-input-mock">質問を入力…</span>
              <span className="chat-input-icons">
                <span>📎</span><span>↗</span>
              </span>
            </footer>
          </div>

          <p className="mech-img-cap mech-img-cap-center">
            ※ 実際のチャット画面のイメージ。質問数に上限はありません。
          </p>
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  05 — Mindset / Weekly 1on1
 * ===================================================================== */

const Mech05Mindset = () => {
  const agenda = [
    { time: "0–10分", title: "今週の振り返り", desc: "学習時間・達成率・つまずきポイントを、数字とエピソードの両面から確認。" },
    { time: "10–25分", title: "つまずきの深掘り", desc: "「なぜ詰まったか」を構造的に分解。本人の言葉で再定義してもらう。" },
    { time: "25–40分", title: "翌週の計画", desc: "Notion上で翌週タスクを一緒に組み直し。優先順位と所要時間を握る。" },
    { time: "40–55分", title: "メンタル・体調・生活", desc: "睡眠・食事・部活・家庭関係まで。学習以外もコーチが把握しておく。" },
    { time: "55–60分", title: "今週のひと言", desc: "コーチから一言メッセージ。Notionにも残し、必要な時に読み返せる形に。" },
  ];

  return (
    <section className="mech-section mech-05" id="mindset">
      <div className="mech-inner">
        <MechHead
          no="05"
          en="Mindset"
          jp="週次面談"
          title={<>毎週60分、<br /><em>迷う暇</em>を与えない。</>}
          lead="独学を1年続けられる人は、ごくわずかです。THINKING は毎週1on1の面談で進捗・悩み・モチベーションを丁寧に管理。一人で抱え込ませず、迷う暇を与えません。"
        />

        <div className="mech-mindset-grid">
          {/* Zoom mock */}
          <div className="mech-mindset-img">
            <ImgPH
              label="週次1on1（Zoom）"
              note="※ 後日、面談の様子の写真をここに差し替え"
              ratio="16 / 10"
            />
            <ul className="mindset-bullets">
              <li><span className="mindset-bullet-dot" /> 録画は全て蓄積。後から見返し可能。</li>
              <li><span className="mindset-bullet-dot" /> 議事録は Notion に自動保存。</li>
              <li><span className="mindset-bullet-dot" /> 保護者の方も、月1回まで同席可。</li>
            </ul>
          </div>

          {/* 60-min agenda */}
          <div className="mech-mindset-agenda">
            <span className="mindset-agenda-label"><i>60-min Agenda</i></span>
            <ol className="mindset-agenda-list">
              {agenda.map((a, i) => (
                <li key={i}>
                  <span className="mindset-agenda-time"><i>{a.time}</i></span>
                  <div className="mindset-agenda-body">
                    <h4>{a.title}</h4>
                    <p>{a.desc}</p>
                  </div>
                </li>
              ))}
            </ol>
          </div>
        </div>

        <div className="mech-callout">
          <span className="mech-callout-mark"><i>Quote</i></span>
          <p>
            受験は、孤独な戦いです。<br />
            でも、<em>毎週60分、隣に伴走者がいる</em>だけで、走り方は変わる。
          </p>
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  06 — Verbalize
 * ===================================================================== */

const Mech06Verbalize = () => {
  const steps = [
    { no: "01", title: "解いた直後に、口に出す", desc: "「なぜこの選択肢か」を声に出して、コーチに10秒で説明する。" },
    { no: "02", title: "詰まったら、書き出す", desc: "言葉にできなかった瞬間が、理解の穴。Notionに「説明できなかったこと」を記録。" },
    { no: "03", title: "翌週、もう一度説明させる", desc: "1週間後、同じ問題をもう一度、口頭で説明。完全に言語化できれば、本物の理解。" },
  ];

  return (
    <section className="mech-section mech-06" id="verbalize">
      <div className="mech-inner">
        <MechHead
          no="06"
          en="Verbalize"
          jp="言語化特訓"
          title={<>説明できない<em>理解</em>は、<br />理解じゃない。</>}
          lead="「なんとなく解けた」は、本番で必ず崩れます。THINKING は「なぜその答えか」を言葉にする訓練を徹底。理解の解像度を一段引き上げ、初見問題にも対応できる本物の力を育てます。"
        />

        {/* Before / After */}
        <div className="mech-block">
          <h3 className="mech-h3"><em>Before / After</em>。同じ問題、同じ生徒。</h3>
          <div className="verbalize-ba">
            <article className="verbalize-card verbalize-before">
              <span className="verbalize-tag"><i>Before</i></span>
              <h4>「なんとなく、ウかな…」</h4>
              <p>消去法で残った気がするから選んだ。説明はできない。次に同じパターンが出ても、また勘で答える。</p>
              <span className="verbalize-meta">理解の解像度：<i>低</i></span>
            </article>
            <span className="verbalize-arrow" aria-hidden="true">→</span>
            <article className="verbalize-card verbalize-after">
              <span className="verbalize-tag"><i>After</i></span>
              <h4>「主節の主語が筆者で、傍線部の it は前段落の policy。だからウ。」</h4>
              <p>構造から答えを導けている。再現性がある。次に同じ構造の問題が来たら、同じ手順で必ず解ける。</p>
              <span className="verbalize-meta">理解の解像度：<i>高</i></span>
            </article>
          </div>
        </div>

        {/* 3-step training */}
        <div className="mech-block">
          <h3 className="mech-h3">3ステップで、<em>言語化</em>を習慣にする。</h3>
          <ol className="verbalize-steps">
            {steps.map((s, i) => (
              <li key={i}>
                <span className="verbalize-step-no"><i>{s.no}</i></span>
                <h4>{s.title}</h4>
                <p>{s.desc}</p>
              </li>
            ))}
          </ol>
        </div>

        <div className="mech-block">
          <ImgPH
            label="言語化ノートの実例"
            note="※ 後日、生徒の実物のノート画像をここに差し替え"
            ratio="16 / 10"
          />
        </div>
      </div>
    </section>
  );
};

/* =====================================================================
 *  Interlock — how the 6 mechanisms reinforce each other
 * ===================================================================== */

const SupportInterlock = () => {
  return (
    <section className="sup-interlock">
      <div className="sup-interlock-inner">
        <span className="eyebrow"><i>One System</i></span>
        <h2 className="sup-interlock-title">
          6つは、<em>独立していない</em>。<br />
          噛み合って、<em>合格</em>を作る。
        </h2>

        <ImgPH
          label="6つの仕組みの相関図"
          note="※ 後日、円環状の関係図を画像で差し替え予定"
          ratio="16 / 8"
        />

        <p className="sup-interlock-lead">
          戦略がなければ、計画は立たない。<br />
          計画がなければ、ロードマップは描けない。<br />
          質問できなければ、計画は止まる。<br />
          面談がなければ、軌道修正できない。<br />
          言語化がなければ、本番で再現できない。<br />
          <em>6つ全てが揃ったとき、初めて「合格」は、設計可能になる。</em>
        </p>
      </div>
    </section>
  );
};

/* =====================================================================
 *  Final LINE CTA — local section, mirrors FlowAndCTA
 * ===================================================================== */

const SupportLineCTA = () => (
  <section className="section line-cta-section" id="contact">
    <div className="line-cta-photo" aria-hidden="true">
      <img src="assets/consult-hero.png" alt="" />
      <div className="line-cta-veil" />
    </div>

    <div className="line-cta-inner">
      <div className="line-cta-text">
        <span className="line-cta-eyebrow">
          <span className="line-cta-eyebrow-line" />
          <i>Online Consultation</i>
        </span>

        <h2 className="line-cta-title">
          6つの仕組みを、<br />
          <em>あなたのために</em>動かす。
        </h2>

        <p className="line-cta-lead">
          まずは60分の無料オンライン面談で、<br />
          現状と志望学部に合わせた戦略の概要をお話しします。
        </p>

        <a
          className="line-cta-button"
          href={window.THINKING_LINE_LIFF_URL}
          target="_blank"
          rel="noopener noreferrer"
        >
          <span className="line-cta-button-icon" aria-hidden="true">
            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M16 4C8.27 4 2 9.06 2 15.3c0 5.6 4.97 10.27 11.7 11.15.45.1 1.07.3 1.23.7.14.36.09.92.04 1.28l-.2 1.2c-.06.36-.28 1.4 1.23.76 1.5-.63 8.1-4.78 11.05-8.18C29.1 19.78 30 17.65 30 15.3 30 9.06 23.73 4 16 4Z"
                fill="currentColor"
              />
            </svg>
          </span>
          <span className="line-cta-button-label">LINEで無料相談</span>
          <svg className="arrow" viewBox="0 0 16 16" fill="none">
            <path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" strokeWidth="1.4" />
          </svg>
        </a>

        <p className="line-cta-note">
          <span><i>全国オンライン対応</i></span>
          <span className="sep">/</span>
          <span><i>初回相談 60分・無料</i></span>
        </p>
      </div>
    </div>
  </section>
);

window.SupportPage = SupportPage;
