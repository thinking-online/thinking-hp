#!/usr/bin/env python3
"""Generate static blog article HTML shells with OG tags for LINE / SNS previews."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "blog" / "pages"
PAGES_DIR.mkdir(parents=True, exist_ok=True)

# slug -> (seoTitle suffix handled, seoDescription, shareDescription, ogImage path)
ARTICLES = {
    "why-faculty-strategy": {
        "title": "なぜ「学部別」でしか難関大に受からないのか｜私立文系受験戦略",
        "description": "早稲田法学部と慶應経済学部では合格に必要な力がまるで違います。「難関大文系」一括り指導の限界と、学部別戦略の3つの効果をTHINKING代表が解説。",
        "share": "早慶でも「難関大文系」一括りでは届かない。法学部と経済学部で求められる力の違い、知っていますか？",
        "image": "/assets/campus-03.png",
    },
    "june-strategy": {
        "title": "高3の6月にやるべきこと｜残り8ヶ月の受験戦略【私立文系】",
        "description": "高3の6月は志望学部の型と英語の処理速度を固める最適な時期。残り8ヶ月を逆算した学習の優先順位と、やめるべき3つの錯覚を解説します。",
        "share": "受験の天王山は夏じゃない。高3の6月にやるべきこと・やめるべきことを、8ヶ月逆算で整理しました。",
        "image": "/assets/campus-03.png",
    },
    "essay-correction": {
        "title": "添削の「赤」が多い答案ほど伸びる理由｜小論文・記述対策",
        "description": "添削で赤が多い答案ほど伸びやすい理由と、THINKINGが重視する「次の一手に落ちる赤」の見方。私立文系の記述・小論文対策に。",
        "share": "赤だらけの答案、落ち込んでませんか？ 実は「赤が多い答案ほど伸びる」——添削の正しい受け止め方を解説。",
        "image": "/assets/campus-03.png",
    },
    "parent-relationship": {
        "title": "親が「がんばれ」と言わないほうが伸びる｜受験生と家族の関わり方",
        "description": "「がんばれ」が重く響く理由と、受験生が伸びる家庭の関わり方。保護者面談で伝えている、介入の型を変えるヒント。",
        "share": "受験生に「がんばれ」は逆効果かも。伸びている子の家庭に共通する、親の関わり方をお伝えします。",
        "image": "/assets/campus-03.png",
    },
    "memorize-vs-think": {
        "title": "「暗記」と「思考」の境界線｜私立文系受験の学習法",
        "description": "暗記が悪いのではなく、考えずに暗記することが問題。私立文系受験で「覚えるべきこと」と「考えるべきこと」の見極め方。",
        "share": "暗記は悪じゃない。悪いのは「考えずに暗記すること」。受験で暗記と思考を使い分ける基準を解説。",
        "image": "/assets/campus-03.png",
    },
    "ranking-trap": {
        "title": "偏差値ランキングを見ない受験戦略｜学部別の正しい指標",
        "description": "偏差値ランキングに振り回されないための考え方。同じ大学でも学部で入試は違う——志望学部で本当に見るべき指標を整理。",
        "share": "偏差値ランキング、見すぎていませんか？ 志望学部で本当に大事な指標と、見ない戦略の話。",
        "image": "/assets/campus-03.png",
    },
    "self-driven": {
        "title": "「自走できる受験生」が最後に勝つ理由｜自立した受験勉強",
        "description": "コーチがいないと勉強できない受験生は本番で崩れる。目的・手段・検証のループを自分で回す「自走力」の育て方。",
        "share": "コーチ依存の受験生は本番で崩れる。最後に勝つ「自走できる受験生」の共通点を解説します。",
        "image": "/assets/campus-03.png",
    },
    "mock-exam": {
        "title": "模試の判定が悪くても絶望しなくていい3つの理由",
        "description": "E判定からの逆転合格が毎年起きる理由。模試の判定を感情のスイッチにせず、弱点リストの材料に変える分析方法。",
        "share": "模試E判定、終わりじゃない。毎年逆転合格が起きる3つの理由と、判定の正しい使い方。",
        "image": "/assets/campus-03.png",
    },
    "winter-mental": {
        "title": "本番1ヶ月前にメンタルが崩れた時の対処法｜受験生の不安",
        "description": "直前期に訪れるメンタルのサインと、回復の手順。睡眠・不安の言い換え・信頼できる大人への共有まで、本番前の心の整え方。",
        "share": "本番直前、メンタルが崩れたときの対処法。気合では抑え込まないで。回復の手順をまとめました。",
        "image": "/assets/campus-03.png",
    },
    "interview-prep": {
        "title": "総合型選抜の面接で合否を分ける一言｜志望理由の伝え方",
        "description": "面接200回以上の指導経験から、総合型選抜で差がつく「志望理由の核心を言い切る一文」と、練習の回し方を解説。",
        "share": "総合型の面接、合否を分けるのは派手なエピソードじゃない。決定的な「一言」の作り方を解説。",
        "image": "/assets/campus-03.png",
    },
    "leap-oboeho-benkyoho": {
        "title": "必携英単語LEAPの覚え方・勉強法｜小テスト・ランダム問題集の使い方【完全ガイド】",
        "description": "必携英単語LEAPの覚え方・勉強法を完全解説。連番・MIXランダム小テスト・問題集の回し方、週テスト前の活用法、無料PDFサンプルまで。",
        "share": "LEAPを何周しても本番で出ない人へ。覚え方・小テストの回し方を完全解説。無料PDFサンプルあり。",
        "image": "/leap/assets/hero.png",
    },
}

TEMPLATE = """<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{doc_title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="THINKING" />
  <meta property="og:locale" content="ja_JP" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{share}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title}" />
  <meta name="twitter:description" content="{share}" />
  <meta name="twitter:image" content="{og_image}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Noto+Sans+JP:wght@300;400;500;600&family=Noto+Serif+JP:wght@400;500;600;700&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../styles.css" />
  <link rel="stylesheet" href="../../styles-site.css" />
  <link rel="stylesheet" href="../../styles-line-cta.css" />
  <link rel="stylesheet" href="../../styles-founder.css" />
  <link rel="stylesheet" href="../../styles-blog.css" />
</head>
<body>
  <div id="root"></div>
  <script>window.__BLOG_PRESET_SLUG__ = "{slug}";</script>
  <script src="https://unpkg.com/react@18.3.1/umd/react.development.js" crossorigin="anonymous"></script>
  <script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" crossorigin="anonymous"></script>
  <script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" crossorigin="anonymous"></script>
  <script src="../../data/line-url.js"></script>
  <script src="../../data/blog-meta.js"></script>
  <script type="text/babel" src="../../components/SiteHeader.jsx"></script>
  <script type="text/babel" src="../../components/SiteFooter.jsx"></script>
  <script src="../../data/blog-articles.js?v=20260702-share"></script>
  <script type="text/babel" src="../../components/BlogArticlePage.jsx?v=20260702-share"></script>
  <script type="text/babel">
    function App() {{
      return (
        <>
          <SiteHeader current="blog" />
          <BlogArticlePage />
          <SiteFooter />
        </>
      );
    }}
    ReactDOM.createRoot(document.getElementById("root")).render(<App />);
  </script>
</body>
</html>
"""

SITE = "https://thinking-online.com"

for slug, data in ARTICLES.items():
    canonical = f"{SITE}/blog/{slug}"
    og_image = SITE + data["image"]
    og_title = data["title"]
    doc_title = og_title + " — THINKING"
    html = TEMPLATE.format(
        slug=slug,
        doc_title=doc_title,
        description=data["description"],
        share=data["share"],
        og_title=og_title,
        canonical=canonical,
        og_image=og_image,
    )
    out = PAGES_DIR / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
