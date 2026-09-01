# students/ — 生徒別 個別戦略シート

生徒ごとの「初回戦略シート」を、**data.json を書くだけ**で A4 の PDF に組み上げる仕組みです。
レイアウト・配色・組版は共通エンジン（`_engine/`）が持っているので、生徒ごとに作るのは**中身だけ**です。

```
students/
├── README.md
├── .gitignore                    # _build/（フォント実体）は非コミット
├── _engine/
│   ├── build.mjs                 # data.json → index.html → PDF
│   ├── sheet.css                 # A4印刷用スタイル（THINKINGブランド）
│   └── setup-fonts.sh            # 日本語フォントの取得・登録（初回のみ）
├── _sample/                      # 営業・説明用のサンプル（架空の生徒）
└── <生徒スラッグ>/
    ├── data.json                 # ← 生徒ごとに書くのはこれだけ
    ├── index.html                # 自動生成（ブラウザ確認用）
    └── <名前>-strategy-sheet.pdf # 自動生成（配布物）
```

> **⚠️ 個人情報**
> このフォルダには生徒の氏名・模試成績・志望校が入ります。本リポジトリは Netlify の
> `publish = "."`（＝リポジトリ全体が公開）なので、`netlify.toml` で `/students/*` を
> **強制 404** にしてあります。この設定は消さないでください。
> 配布は生成された **PDF を手渡し／面談で** 行う運用が前提です。

---

## 使い方

### 0. 初回だけ：フォントを入れる

```bash
bash students/_engine/setup-fonts.sh
```

Zen Kaku Gothic New / Shippori Mincho B1 / Noto Sans JP / Cormorant Garamond を
`~/.fonts` に入れます。**これをやらないと PDF が豆腐（□）になります。**

### 1. 生徒フォルダを作る

直近の生徒フォルダをコピーして、`data.json` を書き換えるのが一番早いです。

```bash
cp -r students/tanaka-mayuri students/yamada-taro
rm students/yamada-taro/index.html students/yamada-taro/*.pdf
# students/yamada-taro/data.json を編集
```

### 2. ビルドする

```bash
node students/_engine/build.mjs students/yamada-taro
```

`index.html` と PDF が同じフォルダに出ます。`--no-pdf` を付けると HTML だけ。

### 3. レイアウトを確認する

**必ずこれを見てから配布**してください。ページからのはみ出しを数値で出します。

```bash
# ブラウザで開いて ?qa=1 を付ける
open students/yamada-taro/index.html?qa=1
```

```
PAGE 00  h=1123px  bodyH=0px     overflow=0px   slack=0px
PAGE 05  h=1123px  bodyH=1012px  overflow=102px slack=-102px   ← はみ出している
```

- `overflow` が **0 以外のページは中身が切れています**。文章を削るかブロックを減らす。
- `slack` はページ下端までの余り。大きすぎる（200px以上）なら中身を足す。

その他の確認用パラメータ：

| パラメータ | 効果 |
|---|---|
| `?only=3` | 4ページ目だけ表示（0が表紙） |
| `?only=3&shift=800` | そのページを 800px 上にずらす（下部の確認） |
| `?qa=1` | 全ページのはみ出し量レポート |

---

## data.json の書き方

### 全体構造

```jsonc
{
  "meta":  { "student": "…", "grade": "…", "course": "…",
             "title": "…", "date": "…", "advisor": "…",
             "pdfName": "yamada-taro-strategy-sheet.pdf" },
  "cover": { "eyebrow": "…", "title": "…", "subtitle": "…", "lead": "…",
             "kpis": [ { "label": "…", "value": "68.3", "unit": "%", "note": "…" } ] },
  "pages": [
    { "runner": "01 現在地", "foot": "…",
      "sec":    { "no": "01", "title": "…", "en": "Current Position" },
      "blocks": [ … ] }
  ]
}
```

- 表紙の **CONTENTS は `pages` から自動生成**されます（手で書く必要なし）。
- ページ番号・フッターの罫線も自動。

### 文字装飾（全ブロック共通）

| 書き方 | 結果 |
|---|---|
| `**強調**` | 紺色の太字 |
| `//注記//` | 淡いグレー |
| `\n` | 改行 |

### ブロック一覧

| `t` | 用途 | 主なキー |
|---|---|---|
| `p` | リード文 | `text`, `tight`（下余白を詰める） |
| `h` | 小見出し（金色の縦線付き） | `text` |
| `ul` / `ol` | 箇条書き／番号付き | `items[]`, `tight` |
| `cards` | カード並べ | `cols`(2/3/4), `items[{kicker,title,body,style}]`<br>`style`: `dark` / `gold` |
| `steps` | ①②③④ の工程 | `items[{title,desc,no}]` |
| `kpis` | 数値の帯（3〜4個） | `items[{label,value,unit,note,style}]`<br>`style`: `acc`(金) / `good`(緑) / `bad`(赤) |
| `callout` | 結びのメッセージ枠 | `title`, `body`, `style`:`navy` |
| `checks` | チェックボックス2列 | `items[]` |
| `wish` | 志望校リスト | `items[{univ,fac,tag,tagStyle}]`<br>`tagStyle`: `core`/`base`/`risk`/`ok` |
| `score` | 模試の得点表（**合計は自動計算**） | `rows[{name,note,conv,convMax,target,sub}]` |
| `weight` | 配点構造の帯グラフ | `segs[{label,value,cls}]`, `legend[{color,text}]` |
| `table` | 一般の表 | `head[]`, `rows[[]]`, `widths[]` |
| `flow` | 面談〜運用の流れ（横並びの帯） | `items[{title,desc,key}]`（`key:true` で金色強調） |
| `cta` | 問い合わせ導線（紺地） | `title`, `body`, `contacts[{label,value}]` |
| `memo` | 手書き用の罫線メモ欄 | `title`, `lines` |
| `space` | 余白 | `h`（例 `"4mm"`） |
| `fill` | **残り高さを吸収**し、次のブロックをページ下端へ | — |
| `row` | 2〜3カラムに入れ子 | `cols`, `items[[block…],[block…]]` |

### `score` ブロックの注意

`conv`（換算得点）と `convMax`（換算満点）で得点率とバーを描きます。
`target` を入れると **▼マーカー**と「必要」列が出ます。合計行は自動計算です。

```jsonc
{ "name": "英語 R", "note": "リーディング 素点 91 / 100",
  "conv": 145.6, "convMax": 160, "target": 152 }
```

得点率による色分け： **80%以上=緑 / 60〜79%=黄 / 60%未満=赤**

`"sub": true` を付けると背景が薄くなります（＝二次で使わない「落とさない科目」の区別に使用）。

---

---

## 営業・説明用サンプル（`_sample/`）

面談前の説明や営業で「こういう資料を作って進めます」と見せるための**見本**です。
**実在の生徒の情報は一切含みません。**生徒名・成績・志望校はすべて架空の設定にしてあります。

```bash
node students/_engine/build.mjs students/_sample
# → students/_sample/thinking-strategy-sheet-sample.pdf（全14ページ）
```

生徒用シート（全11ページ）に、営業用の2ページを足した構成です。

| # | ページ | 役割 |
|---|---|---|
| **00** | この資料は、何のためにあるのか | **営業用**：初回面談で何が決まるか・このシートの3つの特徴 |
| 01〜11 | 戦略シート本体 | 生徒用と同じ形式（架空の生徒「山田 太郎」の例） |
| **12** | 面談から、運用までの流れ | **営業用**：無料相談→面談→シート作成→週次運用→模試ごとに更新／問い合わせ導線 |

### 見本であることの明示

`meta.sample: true` を入れると、次の3点が自動で付きます。**架空データの資料を実物と誤認させないための表示なので、外さないでください。**

1. 表紙右上の `SAMPLE` バッジ
2. 全ページのヘッダーに `SAMPLE` ラベル
3. 表紙フッターが「CONFIDENTIAL — ◯◯様専用」→「SAMPLE — 営業・説明用の見本」に変わる

加えて `meta.note` に「架空の設定である」旨を書くと、表紙のリード文の下に注記として入ります。

### サンプルをWebで配布したい場合

`/students/*` は非公開（強制404）なので、**このままではURLで共有できません。**
サンプルには個人情報が無いため、公開して問題なければ `pdfs/` にコピーすれば
`https://thinking-online.com/pdfs/…` で配布できます。

```bash
cp students/_sample/thinking-strategy-sheet-sample.pdf pdfs/
# push → Netlifyが自動デプロイ
```

**注意：** `pdfs/` に置いたファイルは**URLを知っていれば誰でも閲覧できます**（`pdfs/README.md` 参照）。
公開したくない場合はコピーせず、PDFを直接お渡しする運用にしてください。

---

## 作るときの型（生徒用シートの構成）

そのまま流用できる 11 ページ構成です。生徒が変わっても骨格は同じで問題ありません。
（営業サンプルは、この前後に 00 と 12 を足した 13 ページ構成）

| # | ページ | 中身 |
|---|---|---|
| 01 | ゴールの確認と、勝負の前提 | 志望校リスト・配点の前提（共テ／二次／総合） |
| 02 | 数字で見る現在地 | 模試の得点表・合計 KPI・読み取るべき3点 |
| 03 | どこで合否が決まるのか | 配点構造の帯グラフ・極める科目／落とさない科目 |
| 04 | 得点設計 | 現状→目標の積み上げ表・安全マージン |
| 05〜07 | 科目別戦略 | 極める科目を1科目1ページ |
| 08 | 共テ底上げ | 落とさない科目のまとめ |
| 09 | 環境ルールと運用 | 自習室・数字での判断・チェックする指標 |
| 10 | ロードマップ | 本番までの月別の動き |
| 11 | 最初の30日 | チェックリスト・メモ欄 |

**書くときの原則**

1. **主張は必ず数字で裏を取る。** 「英語を極める」ではなく「英・国・世で総合の81.6%」。
2. **配点から逆算する。** どの科目が総合の何%を握るかを最初に出すと、優先順位の説明が要らなくなる。
3. **目標はボーダーちょうどに置かない。** 本番のブレを吸収するマージンを明示する。
4. **やらないことを書く。** 「深追いしない」「時間を使わない」は、やることと同じくらい重要。
5. **1ページ1メッセージ。** 結びは `callout` で締める（`fill` を前に置くとページ下端に揃う）。
