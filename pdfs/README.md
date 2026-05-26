# pdfs/ — PDF配布フォルダ

このフォルダに置いたPDFは、そのままドメイン直下のURLで公開されます。
WordPressのメディアライブラリ的な使い方の「置き場」です。

## 公開URL

ファイルを置いてGitにpushすると、Netlifyが自動デプロイして以下のURLでアクセスできます。

```
https://<本ドメイン>/pdfs/<ファイル名>.pdf
```

例: `pdfs/guide-2026.pdf` → `https://<本ドメイン>/pdfs/guide-2026.pdf`

## 追加手順

1. このフォルダにPDFを置く
2. ファイル名は **半角英数・ハイフン推奨**（日本語やスペースはURLが汚くなる）
   - OK: `thinking-guide-2026.pdf`
   - NG: `案内資料 (最新).pdf`
3. `git add` → `commit` → `push`
4. 30秒〜1分でNetlifyが自動反映
5. リンクとしてHTMLに貼る: `<a href="/pdfs/xxx.pdf" target="_blank" rel="noopener">資料</a>`

## ダウンロードさせたい場合

ブラウザ内で開かず強制ダウンロードしたいときは `download` 属性を付ける。

```html
<a href="/pdfs/xxx.pdf" download>ダウンロード</a>
```

## URLを綺麗にしたい場合

例えば `/docs/guide` という拡張子なしURLで配布したい場合は、ルートの `netlify.toml` にリダイレクトを追加する。

```toml
[[redirects]]
  from = "/docs/guide"
  to = "/pdfs/thinking-guide-2026.pdf"
  status = 200
```

## 注意

- 大きなPDF（数十MB級）を大量に置くとGitリポジトリが肥大化します。1ファイル数MBまでが目安。
- **URLを知っている人は誰でも見られます**。会員限定にはできません。非公開にしたい資料はファイル名を推測されないものに（例: ランダム文字列を含める）。
- 同じファイル名で内容だけ差し替えるとCDNキャッシュが残ることがあります。更新時は `-v2.pdf` などバージョンを付けると安全。
