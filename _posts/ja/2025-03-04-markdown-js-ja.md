---
audio: false
generated: true
lang: ja
layout: post
title: Markdown用JavaScriptライブラリ
translated: true
---

`marked` ライブラリのバージョン `^0.3.6` の使用方法についてお尋ねのようです。これは、Markdown テキストを解析して HTML に変換する JavaScript ライブラリです。`^0.3.6` の記法（おそらく `package.json` ファイル内の Node.js プロジェクトから）を使用しているため、この古いバージョンの `marked` の使用方法を案内します。バージョン `0.3.6` は非常に古い（2016 年頃にリリース）ものであり、ライブラリはそれ以来大きく進化していますが、そのバージョンで動作するものに絞ります。

### ステップ 1: インストール
Node.js 環境で作業している場合、npm を使用して `marked` バージョン `0.3.6` をインストールできます：

```bash
npm install marked@0.3.6
```

`package.json` 内の `^0.3.6` は、`0.3.6` または互換性のあるパッチ更新（例：`0.3.7`）をインストールすることを意味しますが、上記のコマンドは明確に `0.3.6` にロックします。

### ステップ 2: 基本的な使用方法
`marked` バージョン `0.3.6` を異なる環境で使用する方法は以下の通りです：

#### Node.js で
1. **ライブラリを要求する**:
   ファイル（例：`index.js`）を作成し、以下を追加します：

   ```javascript
   var marked = require('marked');
   ```

2. **Markdown を HTML に変換する**:
   `marked()` 関数を使用して、Markdown 文字列を渡します。例えば：

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **出力**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### ブラウザで
1. **ライブラリを含める**:
   CDN を使用するか、`marked@0.3.6` をダウンロードして `<script>` タグで含めることができます。例えば、歴史的な CDN リンク（利用可能な場合）またはローカル ファイルを使用します：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **JavaScript で使用する**:
   スクリプトを含めた後、`marked` はグローバルに利用可能です：

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### ステップ 3: オプション（バージョン 0.3.6 用）
バージョン `0.3.6` はいくつかのカスタマイズ オプションをサポートしています。オプション オブジェクトを `marked()` の 2 番目の引数として渡すことができます。以下は例です：

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdown を有効にする
  tables: true,      // GFM テーブルを有効にする
  breaks: false,     // 真の場合、単一の改行に <br> を追加する
  pedantic: false,   // 真の場合、厳密な Markdown 仕様に従う
  sanitize: false,   // 真の場合、セキュリティのために HTML タグを削除する
  smartLists: true,  // リストのレンダリングを改善する
  smartypants: false // 真の場合、「スマート」タイポグラフィを使用する（例：カーブリクォート）
});
console.log(html);
```

### 0.3.6 の主要機能
- **基本的な Markdown**: 見出し (`#`)、太字 (`**`)、斜体 (`*`)、リスト、コード ブロック (```) などをサポートします。
- **GFM サポート**: `gfm: true` が設定されている場合、GitHub Flavored Markdown（例：テーブルとタスクリスト）が利用可能です。
- **レンダラーのカスタマイズなし**: 新しいバージョンとは異なり、`0.3.6` はカスタム レンダラーをサポートしていないため、デフォルトの出力に制限されます。

### より多くの Markdown を使用した例
Node.js での完全な例は以下の通りです：

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**出力**:
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### 注意点
- **サニタイズ**: ユーザー入力をレンダリングする場合、`sanitize: true` を設定してセキュリティのために生の HTML を削除します（例：`<script>` タグ）。ただし、`0.3.6` は基本的で、モダンな代替手段ほど強力ではありません。
- **制限**: このバージョンには、後続のリリースで追加された機能（例：非同期解析、カスタム トークナイザー）が欠けているため、より多く必要な場合は `5.x` などの新しいバージョンにアップグレードを検討してください。
- **デバッグ**: 動作しない場合は、ライブラリが正しく読み込まれていることを確認し、Markdown 文法を確認してください。