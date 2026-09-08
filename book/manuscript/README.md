# manuscript

原稿の置き場。ファイル名は法則番号（法則25.md）か、パートの名前（序章.md、はじめに.md、第5章_扉.md）。
企画書は manuscript/企画書/ に。

## PDF の作り方

`book/` で次を実行する。`build/` に HTML と PDF ができる。

```
python3 scripts/build_pdf.py
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
for n in 台本 企画書; do
  "$CH" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --run-all-compositor-stages-before-draw --virtual-time-budget=20000 \
    --print-to-pdf="build/${n}.pdf" "file://$PWD/build/${n}.html"
done
```

A5、日本語は IPA Pゴシック。編集用のプレビューなので、実際の紙面（見開き2ページ組）とは
組み方が違う。問いと答えは、読み味を確かめるため別ページに割っている。

## 縦組み版（読者が見る姿）

`scripts/build_tate.py` が縦組みのHTMLを作る。判型はA5、本文は明朝（Noto Serif CJK JP）、
見出しはゴシック。横組み版と違って、docs への参照や「右ページ／左ページ」といった
編集用の注記、隅の図（デザイナー向けの作図指示）は出さない。

```
python3 scripts/build_tate.py
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
"$CH" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
  --print-to-pdf="build/台本_縦組み.pdf" "file://$PWD/build/台本_縦組み.html"
```

縦組みでの決めごと
- 算用数字は2桁までを縦中横、3桁以上は正立させて縦に積む
- 分かれ道の表は縦の表にして、右の列から左へ読ませる。本文が下に回り込むようにfloatさせる
- チェックリストと記入欄も縦組みのまま
- 章末ページは、章扉ファイルから切り出して章の最後に置く
- 柱とノンブルは入れていない（CSSの@page余白ボックスがChromiumで使えないため）

## 自己点検

原稿を直したら、必ず `book/` で次を実行する。20項目を検査する。

```
python3 scripts/check.py
```

検査するもの。
構造（見開きの必須項目と分かれ道の4行）／通貨（結論が「1行消える／1行増える」に着地）／
文体（アスタリスク、しましょう、社会人）／語彙（法則文に中学生が知らない語）／
主語（見開きに「あの子」が残っていないか）／Qの重複／用語の統一／学年比（各章4対3）／
目次とQの一致／定義整合／章扉（札・力の説明・写真指定・章末2ページ）／
販売（表紙の約束の回収、帯の言葉の回収）／左ページの分量／答えが行動になっているか／
親向け章／未確定の明示／隅の図が図の言葉か／ノートが本文と付録にあるか／
第1章の分量／各章の科目の広がり。

全項目 0件で合格。1件でも出たら直してから次に進む。
