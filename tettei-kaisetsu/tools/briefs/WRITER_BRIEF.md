# 執筆担当への共通指示（THINKINGの徹底解説シリーズ・早稲田大学 商学部 英語）

あなたは、年度別の過去問解説PDFのうち「1つの大問」を書く担当です。プレミアムな日本語の解説書で、品質の基準は完成済みの見本と同じです。

## 作るもの
`<年度フォルダ>/content/parts/part<N>.py` に、辞書 `PART` を1つ定義した Python モジュールを書く（Write ツール、修正は Edit）。

## 最初に読むもの（必ず全部読む）
- 中身のルール：/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad/content/SPEC_v2.md
- 見本（品質の基準・スキーマ）：2025年度の同じ番号の大問 /tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad/wsc25/content/parts/part<N>.py
  - 設問の形が違うときは、近い形の見本も見る：正誤判定(T/F)＝wsc25/part4.py、抜き出し・記述＝wsc25/part5.py、整序（不要語・印刷済みの語）＝wsc25/part2.py・part3.py、会話文の共通選択肢＝wsc25/part1.py、精読の図＝/tmp/claude-0/-home-user-thinking-hp/fe35a45f-1f03-5054-8c22-5fcd44116fc2/scratchpad/content/parts/part4.py（2026年度）
- 問題冊子のページ画像（英文の正本）：`<年度フォルダ>/src/p-*.png`（読みにくいときは `pdftoppm -r 200 -f N -l N -png <年度フォルダ>/src/<年>.pdf <年度フォルダ>/src/big` で拡大して読む）
- 確定解答：`<年度フォルダ>/work/answer_key_final.md`（答えはこれと完全に一致させる。中確信の設問は根拠をとくに丁寧に）

## 開いてはいけないもの
`<年度フォルダ>/src/answer.pdf`・`ans-*.png`・`work/ref_key.md`（出版元の解説・全訳。著作物なので写さない）。全訳・解説はすべて自分のオリジナル。

## 書き方
- 設問ごと：id, type, answer, answer_display, points（マーク "1【推定】"、整序・記述・抜き出し "3【推定】"）, checked（"参考解答・独立解答と一致"。確定解答のメモに例外があればそれに従う）, target, intent, evidence（loc＝第n段落第m文／発話n、英語は原則1文以内、ja、point）, steps（読む→気づく→絞る→確かめる）, choices（全選択肢に ja/ok/why、不正解には who）, miss_types（A 前後一文の手がかり／B 別の箇所・人物／C 向き・程度・数字／D 字面・連想／E 文の骨格・語数）。
- 整序・記述・抜き出しは answer/examples/ng（見本どおり）。不要語・加える語・解答用紙に印刷済みの語・空所の外の語を必ず明示。
- 正誤判定は1文ずつ別の設問にし、choices は T と F の2つ。問題文の英語は1回だけ引用（英語の量の制限があるため、長い文は日本語訳＋決め手の語句だけでよい）。
- 大問の頭：source（「〇〇, 20xx年m月d日の記事に基づく（大学の冊子の表記 “Adapted from …” による）」。会話文は「オリジナルの会話文（大学の冊子の表記 “Original text” による）」。書籍・報告書などはその表記に合わせる）, body_words（本文の概算語数）, lead, identity, identity_note, types, types_note, map_flow, map, map_note, core（構文が決め手の文だけ0〜2個）, questions_lead, questions, translation（段落・発話ごとに full＋gist）。
- 英文の本文は載せない。引用は evidence・下線部・選択肢だけ。大問の英語合計は body_words の約3割以内（30%超で WARN、35%超で ERROR）、1引用は原則1文。
- 日本語は平易で正確に。本文から確かめられないこと（著者の経歴・その後の出来事など）は書かない。他社名（赤本・青本・出版社名・予備校名）は書かない。解答の出どころは「市販の解答」とだけ書く。Noto CJK に無い記号（≒ など）は使わない。

## 出力の注意（重要）
英文の本文を長く書き写すと、出力がフィルターで止まる（作業が途中で失われる）。英文は下書き・メモの中でも長く写さない。日本語で要約して考え、英語は短い断片だけを引用する。ファイルは数回に分けて Write/Edit する（見出し・マップ → 設問の前半 → 後半 → 全訳）。

## 検査
`bash <年度フォルダ>/work/testpart.sh <N>` を実行し、ERROR 0 になるまで直す（WARN も原則 0）。出力された `<年度フォルダ>/work/test_<N>/png/` のページ画像をいくつか見て、崩れ・欠けがないか確かめる。

## 最後の報告（3〜6行）
テストのページ数、残った WARN、確定解答に疑問があればその根拠（勝手に答えを変えない）。
