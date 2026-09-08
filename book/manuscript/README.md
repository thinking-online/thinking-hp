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
