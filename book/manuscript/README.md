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
