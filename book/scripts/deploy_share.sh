#!/bin/bash
# ご確認ページを、thinking-online.com に置く（入れかえる）。
#   置く場所：https://thinking-online.com/genko-p9zz2u/
#   やること：main に、genko-p9zz2u/ のフォルダだけを足す（中身は book/build/共有ページ/site/）。ほかのものには、さわらない
#   2026-11-20：著者「フォルダとか付け加えていいよ、名前もそれでいい」
# 使い方（先に、python3 -I scripts/build_share.py で、ページを作り直しておく）：
#   GIT_AUTHOR_NAME=… GIT_AUTHOR_EMAIL=… GIT_COMMITTER_NAME=… GIT_COMMITTER_EMAIL=… bash scripts/deploy_share.sh "何を変えたか"
set -euo pipefail
NAME=genko-p9zz2u
MSG=${1:-ご確認ページを更新}
ROOT=$(git rev-parse --show-toplevel)
# ふつうは、作り直した一式（site/）を、そのまま置く。一部のページだけを入れかえたい時は、置くもの一式を別の所に用意して、SHARE_SRC で渡す
SRC="${SHARE_SRC:-$ROOT/book/build/共有ページ/site}"
test -f "$SRC/index.html"
WT=$(mktemp -d)
git -C "$ROOT" fetch -q origin main
git -C "$ROOT" worktree add -q --detach "$WT" origin/main
trap 'git -C "$ROOT" worktree remove --force "$WT" >/dev/null 2>&1 || true' EXIT
rm -rf "${WT:?}/$NAME"
mkdir -p "$WT/$NAME"
cp -r "$SRC/." "$WT/$NAME/"
git -C "$WT" add -A -- "$NAME"
if git -C "$WT" diff --cached --quiet; then
  echo "変わった所は、ありません（置いてあるものと同じ）"
  exit 0
fi
# 念のため：このフォルダの外に、変わるものが1つもないことを確かめる
OUTSIDE=$(git -C "$WT" diff --cached --name-only | grep -v "^$NAME/" || true)
if [ -n "$OUTSIDE" ]; then echo "フォルダの外が変わっています。中止: $OUTSIDE"; exit 1; fi
git -C "$WT" diff --cached --stat | tail -3
git -C "$WT" commit -q -m "原稿のご確認ページ（/$NAME/）：$MSG

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0154mWKKExSVXqR6nXqMNkgX"
for i in 1 2 3 4; do
  if git -C "$WT" push -q origin HEAD:main; then echo "置きました： https://thinking-online.com/$NAME/"; exit 0; fi
  sleep $((i * 3))
done
echo "main に入れられませんでした"
exit 1
