---
audio: false
generated: true
lang: ja
layout: post
title: Markdown向けJavaScriptライブラリ
translated: true
type: note
---

`marked`ライブラリのバージョン`^0.3.6`（JavaScriptでMarkdownテキストを解析しHTMLに変換するライブラリ）の使用方法についてお問い合わせのようです。`package.json`ファイルで指定される`^0.3.6`という表記（Node.jsプロジェクトで使用）を参照されているため、この古いバージョンの`marked`の使用方法を説明します。バージョン`0.3.6`は非常に古い（2016年頃リリース）もので、それ以降ライブラリは大きく進化していますが、このバージョンで動作する内容に限定して説明します。

### ステップ 1: インストール
Node.js環境で作業している場合、npmを使用して`marked`バージョン`0.3.6`をインストールできます：

```bash
npm install marked@0.3.6
```

`package.json`での`^0.3.6`は、`0.3.6`または互換性のあるパッチアップデート（例: `0.3.7`）をインストールすることを意味しますが、明確にするために上記のコマンドは正確に`0.3.6`に固定します。

### ステップ 2: 基本的な使用方法
以下に、さまざまな環境で`marked`バージョン`0.3.6`を使用する方法を示します：

#### Node.jsの場合
1. **ライブラリを読み込む**：
   ファイル（例: `index.js`）を作成し、以下を追加します：

   ```javascript
   var marked = require('marked');
   ```

2. **MarkdownをHTMLに変換する**：
   Markdown文字列を渡して`marked()`関数を使用します。例：

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

#### ブラウザの場合
1. **ライブラリを含める**：
   CDNを使用するか、`marked@0.3.6`をダウンロードし、`<script>`タグを介して含めます。例：歴史的なCDNリンク（利用可能な場合）またはローカルファイルを使用：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **JavaScriptで使用する**：
   スクリプトを含めた後、`marked`はグローバルに利用可能になります：

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### ステップ 3: オプション（バージョン 0.3.6用）
バージョン`0.3.6`はいくつかのカスタマイズオプションをサポートしています。オプションオブジェクトを`marked()`の第2引数として渡せます。例：

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdownを有効化
  tables: true,      // GFMテーブルを有効化
  breaks: false,     // trueの場合、単一行の改行で<br>を追加
  pedantic: false,   // trueの場合、厳格なMarkdown仕様に従う
  sanitize: false,   // trueの場合、セキュリティのためにHTMLタグを除去
  smartLists: true,  // リストレンダリングを改善
  smartypants: false // trueの場合、「スマート」なタイポグラフィを使用（例: カールした引用符）
});
console.log(html);
```

### バージョン 0.3.6の主な機能
- **基本的なMarkdown**: 見出し（`#`）、太字（`**`）、斜体（`*`）、リスト、コードブロック（```）などをサポート。
- **GFMサポート**: GitHub Flavored Markdown（テーブルやタスクリストなど）は`gfm: true`を設定すると利用可能。
- **レンダラーのカスタマイズ不可**: 新しいバージョンとは異なり、`0.3.6`はカスタムレンダラーをサポートせず、デフォルトの出力に限定されます。

### より詳細なMarkdownの例
Node.jsでの完全な例：

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
- **サニタイズ**: ユーザー入力をレンダリングする場合、セキュリティのために`sanitize: true`を設定して生のHTML（例: `<script>`タグ）を除去します。ただし、これは`0.3.6`では基本的なもので、現代の代替手段ほど堅牢ではありません。
- **制限事項**: このバージョンは後続のリリースで追加された機能（非同期解析、カスタムトークナイザーなど）を欠いているため、さらに多くの機能が必要な場合は`5.x`などの新しいバージョンへのアップグレードを検討してください。
- **デバッグ**: 動作しない場合は、ライブラリが正しく読み込まれていることを確認し、Markdown構文をチェックしてください。