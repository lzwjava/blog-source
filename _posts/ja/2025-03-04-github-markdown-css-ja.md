---
audio: false
generated: true
lang: ja
layout: post
title: GitHubのマークダウンスタイリング
translated: true
type: note
---

### 主なポイント
- 「github-markdown-css」npmパッケージを使用するには、まず`npm install github-markdown-css`でインストールする必要があるようです。
- 調査によると、その後CSSファイルをプロジェクトにインポートし、Markdownコンテンツを「markdown-body」クラスのdivでラップします。
- GitHubのスタイルに合わせてオプションの幅とパディングを設定し、スタイリングの問題を避けるためにDOCTYPEを確実に含めることが推奨されています。

### インストール方法
プロジェクトディレクトリでnpmを使用してパッケージをインストールします：
- `npm install github-markdown-css`を実行して依存関係に追加します。

### 使用方法
インストール後、CSSをプロジェクトに統合します：
- CSSファイルをインポートします（例：JavaScript/Reactで`import 'github-markdown-css';`）。
- レンダリングされたMarkdownコンテンツを`<div class="markdown-body">...</div>`でラップしてスタイルを適用します。
- オプションで、GitHubの見た目に合わせて幅とパディングのCSSを追加します：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- スタイリングに影響する可能性のある互換モードを防ぐため、HTMLにDOCTYPE（例：`<!DOCTYPE html>`）を含めることを確認してください。

### 予期しない詳細
カスタマイズされたスタイルが必要な場合、関連パッケージの[generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)を使用してカスタムCSSを生成することもサポートされている点は、意外に思われるかもしれません。

---

### 調査ノート：github-markdown-css npmパッケージの包括的使用ガイド

この詳細なガイドは、WebプロジェクトでGitHubのMarkdownスタイリングを再現するために設計された「github-markdown-css」npmパッケージの使用方法を探求します。ReactやプレーンHTMLなどの様々な開発コンテキストにおける最適な使用法のための段階的なアプローチと追加の考慮事項を提供します。情報は公式パッケージドキュメント、GitHubリポジトリ、関連するWebリソースから得られ、あらゆるレベルの開発者に徹底的な理解を保証します。

#### 背景と目的
[sindresorhus](https://github.com/sindresorhus)によってメンテナンスされている「github-markdown-css」パッケージは、GitHubのMarkdownレンダリングスタイルをエミュレートする最小限のCSSを提供します。これは、ドキュメントやブログ投稿などのMarkdownコンテンツをGitHubの親しみやすくクリーンな表示と一貫して表示させたい開発者に特に有用です。このパッケージは広く使用されており、最近の更新時点でnpmレジストリ内の1,168以上の他のプロジェクトで利用されており、その人気と信頼性を示しています。

#### インストールプロセス
開始するには、Node.jsパッケージマネージャーであるnpm経由でパッケージをインストールする必要があります。コマンドは簡単です：
- プロジェクトディレクトリで`npm install github-markdown-css`を実行します。これにより、パッケージが`node_modules`フォルダに追加され、依存関係として`package.json`が更新されます。

最近のチェック時点でのパッケージの最新バージョンは5.8.1で、約3ヶ月前に最後に公開されており、活発なメンテナンスと更新を示唆しています。これにより、現代のWeb開発プラクティスやフレームワークとの互換性が確保されます。

#### 統合と使用方法
インストール後、次のステップはCSSをプロジェクトに統合することです。パッケージは`github-markdown.css`という名前のファイルを提供し、プロジェクトの設定に応じてインポートできます：

- **JavaScript/モダンフレームワークの場合（例：React、Vue）：**
  - JavaScriptまたはTypeScriptファイルで`import 'github-markdown-css';`などのインポート文を使用します。これは、WebpackやViteなどのバンドラーがCSSインポートをシームレスに処理するため、うまく機能します。
  - Reactでは、開発者がコンポーネントファイルでインポートし、スタイルがグローバルまたは必要に応じてスコープ化されることを保証する例が見られるかもしれません。

- **プレーンHTMLの場合：**
  - HTMLのheadセクションでCSSファイルを直接リンクします：
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - パスはプロジェクト構造に基づいて異なる場合があることに注意してください。相対パスが正しく`node_modules`ディレクトリを指していることを確認してください。

インポート後、レンダリングされたMarkdownコンテンツを「markdown-body」クラスを持つ`<div>`でラップしてスタイルを適用します。例：
```html
<div class="markdown-body">
  <h1>Unicorns</h1>
  <p>All the things</p>
</div>
```
このクラスは、CSSがGitHub風のスタイリング（タイポグラフィ、コードブロック、テーブルなど）を適用するために`.markdown-body`内の要素をターゲットするため、重要です。

#### スタイリングの考慮事項
GitHubのMarkdownの外観を完全に再現するには、`.markdown-body`クラスの幅とパディングを設定することを検討してください。ドキュメントでは以下が推奨されています：
- 最大幅980px、大きな画面では45pxのパディング、モバイルデバイス（画面≤767px）では15pxのパディング。
- これは以下のCSSで実現できます：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
これにより、応答性が確保され、GitHubのデザインに沿って、読みやすさとユーザーエクスペリエンスが向上します。

#### 技術的注意点とベストプラクティス
- **DOCTYPE要件：** ドキュメントは、ブラウザが互換モードに入った場合にダークモードのテーブルが正しくレンダリングされないなどのスタイリングの問題の可能性を強調しています。これを防ぐために、常にHTMLの先頭に`<!DOCTYPE html>`などのDOCTYPEを含めてください。これにより、標準準拠のレンダリングが確保され、予期しない動作が回避されます。
- **Markdownパーシング：** パッケージはCSSを提供しますが、MarkdownをHTMLにパースしません。MarkdownテキストをHTMLに変換するには、[marked.js](https://marked.js.org/)やReactプロジェクトの場合は[react-markdown](https://github.com/remarkjs/react-markdown)などのMarkdownパーサーが必要です。その後、このCSSでスタイルを適用できます。
- **カスタムCSS生成：** 上級ユーザーのために、関連パッケージの[generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)を使用すると、特定のテーマ設定や変更に有用な可能性があるカスタムCSSを生成できます。これは、パッケージが直接使用のみを目的としていると仮定する人々にとっては予期しない詳細です。

#### 特定のコンテキストでの使用法
- **Reactプロジェクト：** Reactでは、`github-markdown-css`と`react-markdown`を組み合わせることが一般的です。両方をインストール後、CSSをインポートしてコンポーネントを使用します：
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Hello, World!</ReactMarkdown>
    </div>
  );
  ```
  完全なGitHubスタイリングのためには、前述の幅とパディングのCSSも設定してください。

- **CDNを使用したプレーンHTML：** 迅速なプロトタイピングには、[cdnjs](https://cdnjs.com/libraries/github-markdown-css)で利用可能なCDNバージョンを直接リンクして使用できます：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  その後、前述のように`.markdown-body`クラスを適用します。

#### 潜在的な問題と解決策
- **スタイリングの競合：** プロジェクトが他のCSSフレームワーク（例：Tailwind、Bootstrap）を使用している場合、特異性の競合がないことを確認してください。`.markdown-body`クラスはほとんどのスタイルを上書きするはずですが、徹底的にテストしてください。
- **ダークモードサポート：** パッケージはダークモードをサポートしていますが、Markdownパーサーとプロジェクト設定が、特にコードブロックとテーブルのテーマ切り替えを正しく処理することを確認してください。
- **ブラウザ互換性：** パッケージの広範な使用を考えると、互換性は一般的に良好ですが、主要なブラウザ（Chrome、Firefox、Safari）で一貫したレンダリングを確保するために常にテストしてください。

#### 比較分析
他のMarkdown CSSオプション（[Markdown CSS](https://markdowncss.github.io/)など）と比較して、「github-markdown-css」はGitHubのスタイルを直接複製する点で際立っており、GitHubの外観を模倣するドキュメントに理想的です。ただし、初期状態で複数のテーマを提供するいくつかの代替手段とは異なり、追加のカスタマイズなしでは組み込みのテーマオプションが不足しています。

#### 表：主な機能と考慮事項

| 機能                      | 説明                                                                        |
|---------------------------|-----------------------------------------------------------------------------|
| インストールコマンド      | `npm install github-markdown-css`                                           |
| CSSインポート方法         | `import 'github-markdown-css';` またはHTMLでの`<link>`                      |
| 必要なクラス              | スタイリング適用のための`.markdown-body`                                    |
| 幅とパディング            | 最大980px、45pxパディング（デスクトップ）；15pxパディング（モバイル≤767px） |
| DOCTYPE要件               | 互換モードを避け、適切なレンダリングを確保するために不可欠                  |
| カスタムCSS生成           | [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)経由で可能 |
| 互換性                    | marked.js、react-markdownなどのMarkdownパーサーと動作；広範なブラウザサポート |

#### 結論
「github-markdown-css」を使用することは、GitHubのMarkdownスタイリングを複製したい開発者にとって簡単です。インストールと統合のステップに従い、追加のスタイリングと技術的注意点を考慮することで、Markdownコンテンツに一貫したプロフェッショナルな外観を実現できます。高度なカスタマイズについては、生成パッケージを探索し、特に複雑なプロジェクトでは互換性とレンダリングの問題について常にテストしてください。

#### 主要な引用文献
- [github-markdown-css npmパッケージページ](https://www.npmjs.com/package/github-markdown-css)
- [GitHub Markdownスタイルを複製する最小限のCSS GitHubリポジトリ](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSSデモページ](https://sindresorhus.com/github-markdown-css/)
- [github-markdown-cssのCSSを生成するnpmパッケージ](https://www.npmjs.com/package/generate-github-markdown-css)
- [cdnjsによるgithub-markdown-css CDN](https://cdnjs.com/libraries/github-markdown-css)