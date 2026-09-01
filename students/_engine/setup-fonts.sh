#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# 個別戦略シートの PDF 化に使う日本語フォントを取得してシステムに登録する。
# 初回のみ実行すれば OK（~/.fonts に入れて fc-cache する）。
#   bash students/_engine/setup-fonts.sh
# ---------------------------------------------------------------------------
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_build/fonts"
mkdir -p "$DIR"

# Google Fonts の TTF 実体（CJK 全字形入り）。URL は css2 API が返すもの。
declare -A FONTS=(
  [NotoSansJP-Regular.ttf]="https://fonts.gstatic.com/s/notosansjp/v56/-F6jfjtqLzI2JPCgQBnw7HFyzSD-AsregP8VFBEj75s.ttf"
  [NotoSansJP-Medium.ttf]="https://fonts.gstatic.com/s/notosansjp/v56/-F6jfjtqLzI2JPCgQBnw7HFyzSD-AsregP8VFCMj75s.ttf"
  [NotoSansJP-Bold.ttf]="https://fonts.gstatic.com/s/notosansjp/v56/-F6jfjtqLzI2JPCgQBnw7HFyzSD-AsregP8VFPYk75s.ttf"
  [ZenKakuGothicNew-Regular.ttf]="https://fonts.gstatic.com/s/zenkakugothicnew/v18/gNMYW2drQpDw0GjzrVNFf_valaDBcznOkjs.ttf"
  [ZenKakuGothicNew-Medium.ttf]="https://fonts.gstatic.com/s/zenkakugothicnew/v18/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqs9LaWQ.ttf"
  [ZenKakuGothicNew-Bold.ttf]="https://fonts.gstatic.com/s/zenkakugothicnew/v18/gNMVW2drQpDw0GjzrVNFf_valaDBcznOqodNaWQ.ttf"
  [ShipporiMinchoB1-SemiBold.ttf]="https://fonts.gstatic.com/s/shipporiminchob1/v24/wXK1E2wCr44tulPdnn-xbIpJ9RgT9-nKVo5P3g.ttf"
  [ShipporiMinchoB1-Bold.ttf]="https://fonts.gstatic.com/s/shipporiminchob1/v24/wXK1E2wCr44tulPdnn-xbIpJ9RgT9-nKMo9P3g.ttf"
  [CormorantGaramond-Medium.ttf]="https://fonts.gstatic.com/s/cormorantgaramond/v21/co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_s06GnM.ttf"
  [CormorantGaramond-SemiBold.ttf]="https://fonts.gstatic.com/s/cormorantgaramond/v21/co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_iE9GnM.ttf"
  [CormorantGaramond-Bold.ttf]="https://fonts.gstatic.com/s/cormorantgaramond/v21/co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_hg9GnM.ttf"
)

for name in "${!FONTS[@]}"; do
  if [ -s "$DIR/$name" ]; then
    echo "= $name (取得済み)"
  else
    echo "↓ $name"
    curl -fsSL -o "$DIR/$name" "${FONTS[$name]}"
  fi
done

mkdir -p "$HOME/.fonts"
cp "$DIR"/*.ttf "$HOME/.fonts/"
fc-cache -f >/dev/null 2>&1 || true

echo
echo "✓ フォント登録完了:"
fc-match "Zen Kaku Gothic New"
fc-match "Shippori Mincho B1"
fc-match "Cormorant Garamond"
