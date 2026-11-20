#!/bin/bash
# 使い方: finalize.sh <年度フォルダ> <id> <名前の本体（例: 早稲田大学_商学部_2022_英語）>
set -e
D=$1; ID=$2; NAME=$3
F=$D/content/out/$ID.pdf; mkdir -p $D/up; O="$D/up/【完成版】${NAME}_徹底解説.pdf"
timeout 280 gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.6 -dDetectDuplicateImages=true -dSubsetFonts=true -dCompressFonts=true -sOutputFile="$O" "$F"
NP=$(qpdf --show-npages "$F"); NO=$(qpdf --show-npages "$O")
cd $D/up; rm -f cmpa*.png cmpb*.png
for p in 2 $((NP/2)) $NP; do pdftoppm -r 50 -f $p -l $p -png "$F" cmpa$p; pdftoppm -r 50 -f $p -l $p -png "$O" cmpb$p; done
python3 - <<PY
from PIL import Image, ImageChops; import glob
bad=0
for f in sorted(glob.glob('cmpa*.png')):
    a=Image.open(f).convert('L'); b=Image.open(f.replace('cmpa','cmpb')).convert('L')
    h=ImageChops.difference(a,b).histogram(); r=sum(h[60:])/(a.size[0]*a.size[1])
    if r>0.01: bad+=1
print('visual_diff_pages_over_1pct', bad)
PY
rm -f cmpa*.png cmpb*.png
echo "pages $NP -> $NO ; size $(stat -c%s "$F") -> $(stat -c%s "$O")"
sed -i "s/PAGES/$NP/" $D/note/free.html
# 生成元パック（英文の書き起こしは入れない）
B=$D/bundle/$NAME; rm -rf $D/bundle; mkdir -p $B/note; cp -r $D/content/data $D/content/parts $B/; cp $D/work/answer_key_final.md $B/; cp $D/note/free.html $D/note/paid.html $B/note/ 2>/dev/null || true
find $B -name __pycache__ -prune -exec rm -rf {} + ; rm -rf $D/pack
python3 /home/user/thinking-hp/tettei-kaisetsu/tools/drive_pack.py pack "$NAME" $D/pack $B >/dev/null
sha256sum "$O" $D/note/free.html $D/note/paid.html $D/pack/*
