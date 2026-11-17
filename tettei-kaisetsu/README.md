# THINKINGの徹底解説シリーズ（PDF）

大学・年度ごとの過去問 英語 解説 PDF を作る仕組み。
中身（Python の辞書）→ HTML → PDF（WeasyPrint）の順に組み、最後に検査する。

## 最初に守ること：中身はこのリポジトリに置かない

このリポジトリは Netlify で `publish = "."`。**ここに置いた物はすべてサイトとして公開される。**

| 置いてよい（このフォルダ） | 置かない（中身置き場へ） |
|---|---|
| `build.py`・`templates/style.css`・`README.md` | 本物の `data/<univ>_<year>.py`（解説・全訳・正解） |
| `sample/sample_dummy.py`（中身のないダミー。`"dummy": True`） | できた PDF・HTML・ページ画像 |
| `.gitignore` | 過去問の PDF・画像、照合に使った資料 |

- 中身置き場はリポジトリの外。`--content-dir` か環境変数 `TETTEI_CONTENT_DIR` で指定する。
  指定がなければ `build.py` の `DEFAULT_CONTENT_DIR`（作業用 scratchpad の `content/`）を使う。scratchpad は消えることがあるので、本番の中身は消えない外部の場所（Google ドライブ等）にも控えを置くこと。
- 置き方：`<中身置き場>/data/<univ>_<year>.py`。PDF の既定の出力先は `<中身置き場>/out/<univ>_<year>.pdf`。
- 安全装置：
  - `build.py` は `"dummy": True` でない data がリポジトリ内にあると止まる。
  - `.gitignore` で `out/`・`*.pdf`・`*.html`・`data/`・`content/` を除外している（誤って置いてもコミットされない）。

## 準備

```
pip install weasyprint fonttools
apt-get install -y fonts-noto-cjk fonts-liberation poppler-utils
fc-list | grep "Noto Sans CJK JP"     # 入っているか確認
```

使う書体：見出し・表・札＝Noto Sans CJK JP、本文・訳＝Noto Serif CJK JP、英語＝Liberation Serif。
コンテナを作り直すと Noto CJK が消えることがある。その場合 `build.py` が「フォントが見つかりません」で止まるので入れ直す。

## 作り方

```
# 見本（ダミー）を組む
python3 build.py sample/sample_dummy.py --out /path/to/sample.pdf --png /path/to/pages

# 本番：中身置き場の data/waseda-shogaku_2026.py を組む
TETTEI_CONTENT_DIR=/path/to/content python3 build.py waseda-shogaku_2026 --png /path/to/pages
```

1. `sample/sample_dummy.py` を `<中身置き場>/data/<univ>_<year>.py` に写す（例 `waseda-shogaku_2026.py`）。`"dummy"` を消し、`footer_note` を空にする。
2. 中身を書く（下の「章立て」「書き方のルール」）。
3. `build.py` で組む。`--png` でページ画像を出し、**全ページを目で見る**（表の途中で切れていないか、見出しだけがページ末に残っていないか、マス目が崩れていないか）。
4. 検査で `ERROR` が 1 つでも出たら終了コード 1。直してから出す。

### 検査の中身（build.py が自動で行う）

- 必要フォントがあるか（無ければ止まる）
- 本文の全文字が Noto CJK JP に収録されているか（豆腐の防止）
- PDF の全フォントが埋め込まれているか、想定外の代替フォントに落ちていないか（`pdffonts`）
- PDF から文字を読み戻せるか、U+FFFD（文字化け）がないか（`pdftotext`）
- 禁止語（他社の書名・シリーズ名・社名）がないか
- 英文の載せすぎ：`[[...]]` 引用 1 つ 30 語まで、大問 1 つあたり英語 260 語まで
- 記述の答案例が指定字数に収まっているか、正解・照合欄が空でないか

## 章立て（`BOOK` 辞書の形）

| 順 | 章 | data のキー |
|---|---|---|
| 1 | 表紙 | `univ` `faculty` `year` `subject` `cover_color` |
| 2 | 目次 | 自動（ページ番号も自動） |
| 3 | この年度の全体像（大問構成・試験時間・時間配分・差がつく所） | `overview` |
| 4 | 大問ごと（`parts` の数だけ繰り返す） | `parts[]` |
|   | この文章の正体（一行） | `identity` `identity_note` |
|   | 設問タイプと攻め方 | `types` |
|   | 英文マップ（段落の流れと設問の在りか） | `map_flow` `map` `map_note` |
|   | 心臓部の精読（構文の図と訳） | `core[]`（`lines` に 英文の区切り／働き／訳／`level`＝字下げ） |
|   | 設問ごとの解説 | `questions[]`（下記） |
|   | 全訳 2 種（原文に忠実な訳・かみくだいた訳。段落番号・文番号つき） | `translation[]` |
| 5 | 総まとめ：解答一覧（照合欄つき）・失点の型別の復習動線・自己採点表 | 自動＋`summary` `sources` |

設問 1 つ（`questions[]` の要素）：

- 共通：`id` `type` `answer` `points` `checked`（照合結果） `target`（下線部・設問の要約） `miss_types`（失点の型のキー）
- `intent` 出題意図 / `steps` 解く人の頭の中の手順 / `basis` 正解の根拠
- 選択式：`wrong[]` = `choice`・`why`（ダメな理由）・`lack`（その誤答を選ぶ人に足りないもの）
- 記述：`rubric[]`（採点の要素・配点・判定） `chars`（字数。マス目が出る） `examples[]`（答案例） `ng[]`（減点される書き方）

解答一覧・自己採点表・復習動線の「該当設問」は `questions` から自動で作る（正解を二か所に書かない）。

## 書き方のルール

- **問題文・英文本文は載せない。** 生徒は問題冊子を印刷して手元に置いて使う。載せてよいのは設問の下線部と短い引用（`[[...]]`、1 つ 30 語まで）と、心臓部の精読で扱う数文だけ。
- **全訳は THINKING のオリジナル。** 市販の解答資料・他サイトの訳を写さない、言い換えて使わない。自分で英文から訳す。
- **照合資料の扱い。** 正解は自分で解いて決め、そのあと大学公表の解答・市販の解答資料と照合する。照合欄（`checked`）には「一致」「不一致（相手の解答と、こちらが採った根拠）」「公表なし」を書く。他社の書名・シリーズ名・社名は書かず「市販の解答資料」と総称する（表紙にも本文にも入れない。`build.py` が検査する）。
- **推定の明記。** 配点・試験時間・採点基準など、公表資料で確かめられないものには必ず `【推定】` をつける。記述の採点の要素は原則 THINKING の推定。
- **札は太字の【】だけ。** 色付きの箱・背景色・影・角丸・アイコン・飾りは使わない。強調は `**太字**`、下線部の引用は `__下線__`。
- **書き方の調子**（手本：リポジトリ直下の `gakushuin-university-2022-english-q2-full.html`）。
  - 「この文章の正体」は一行で、素朴な読みとの違いを言い切る（例：「観光客が悪い、ではない。犯人を途中ですり替えている文章。」）。
  - 根拠は段落番号・文番号で指す（「第9段落第3文」）。答えは下線部の外にある、という読み方を繰り返し示す。
  - 誤答は「なぜダメか」と「どんな読み方をした人が選ぶか（足りないもの）」を必ず両方書く。
  - 失点の型は、知識の不足ではなく「どの手がかりを見落としたか」で分ける。

## 表紙

A4 縦 1 ページ。単色の地（`cover_color`、落ち着いた深い色 1 色）＋白文字、太い白帯 1 本。
上部の小さな行「学部別・逆算戦略設計 THINKING」、中央に大学名・学部、その下に「〇〇年度 科目」、帯の下にシリーズ名「THINKINGの徹底解説シリーズ」。グラデーション・影・角丸・写真は使わない。

## ファイル

```
tettei-kaisetsu/
  build.py              中身 → HTML → PDF ＋ 検査
  templates/style.css   組版（ページ・見出し・表・構文の図・マス目・表紙）
  sample/sample_dummy.py 見本（ダミー。早稲田大学 商学部 2026年度 英語の体裁）
  README.md
  .gitignore
```
