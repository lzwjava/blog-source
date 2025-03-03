---
audio: false
generated: true
lang: ja
layout: post
title: GitHubのMarkdownスタイル
translated: true
---

### 重要なポイント
- "github-markdown-css" npm パッケージを使用するためには、まず `npm install github-markdown-css` でインストールすることが推奨されています。
- 研究によると、次に CSS ファイルをプロジェクトにインポートし、Markdown コンテンツをクラス "markdown-body" を持つ div でラップする必要があります。
- 証拠は、GitHub のスタイルに合うようにオプションの幅とパディングを設定し、ドキュメントタイプを設定してスタイルの問題を避けることを示唆しています。

### インストール
プロジェクトディレクトリで npm を使用してパッケージをインストールして開始します：
- `npm install github-markdown-css` を実行して依存関係に追加します。

### 使用方法
インストール後、CSS をプロジェクトに統合します：
- JavaScript/React で `import 'github-markdown-css';` など、CSS ファイルをインポートします。
- レンダリングされた Markdown コンテンツを `<div class="markdown-body">...</div>` でラップしてスタイルを適用します。
- オプションで、幅とパディングを追加して GitHub の見た目を模倣します：
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
- HTML に DOctype を含めることで、クイックスモードの問題を防ぎ、スタイルに影響を与えることを確認します（例：`<!DOCTYPE html>`）。

### 予期せぬ詳細
このパッケージは、カスタム CSS を生成するための関連パッケージ [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) をサポートしていることが予想されません。

---

### アンケートノート: github-markdown-css npm パッケージの使用に関する包括的なガイド

この詳細なガイドでは、Web プロジェクトで GitHub の Markdown スタイルを再現するために設計された "github-markdown-css" npm パッケージの使用方法を探ります。インストールと統合のステップバイステップのアプローチ、および最適な使用のための追加の考慮事項、特に React やプレーン HTML のようなさまざまな開発コンテキストについて提供します。情報は、公式パッケージドキュメント、GitHub リポジトリ、および関連する Web リソースから得られ、すべてのレベルの開発者にとって包括的な理解を提供します。

#### 背景と目的
[sindresorhus](https://github.com/sindresorhus) によってメンテナンスされている "github-markdown-css" パッケージは、GitHub の Markdown レンダリングスタイルを模倣するための最小限の CSS セットを提供します。これは、ドキュメントやブログ投稿などの Markdown コンテンツが GitHub の見慣れたクリーンなプレゼンテーションと一貫性を持つようにするために、特に有用です。このパッケージは、npm レジストリで 1,168 以上の他のプロジェクトが使用しているため、最近の更新時点での人気と信頼性を示しています。

#### インストールプロセス
まず、npm を使用してパッケージをインストールする必要があります。コマンドは簡単です：
- プロジェクトディレクトリで `npm install github-markdown-css` を実行します。これにより、パッケージが `node_modules` フォルダーに追加され、`package.json` に依存関係が更新されます。

パッケージの最新バージョンは、最近のチェックでは 5.8.1 で、約 3 か月前に公開されました。これにより、現代的な Web 開発の実践とフレームワークとの互換性が確保されます。

#### 統合と使用方法
インストール後、次のステップはプロジェクトに CSS を統合することです。パッケージには `github-markdown.css` という名前のファイルがあり、プロジェクトのセットアップに応じてインポートできます：

- **JavaScript/モダンフレームワーク（例：React、Vue）:**
  - JavaScript または TypeScript ファイルでインポートステートメントを使用します。例えば、`import 'github-markdown-css';`。これは、Webpack や Vite のようなバンドラーが CSS インポートをシームレスに処理するため、うまく機能します。
  - React の場合、開発者がコンポーネントファイルでインポートする例を見ることができます。これにより、スタイルがグローバルまたは必要に応じてスコープされます。

- **プレーン HTML:**
  - HTML の head セクションで CSS ファイルを直接リンクします：
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - パスはプロジェクト構造に応じて異なる場合があります。`node_modules` ディレクトリに正しくポイントするように相対パスを確認してください。

インポート後、レンダリングされた Markdown コンテンツをクラス "markdown-body" を持つ `<div>` でラップしてスタイルを適用します。例えば：
```html
<div class="markdown-body">
  <h1>ユニコーン</h1>
  <p>すべてのもの</p>
</div>
```
このクラスは重要です。CSS は `.markdown-body` 内の要素をターゲットにして、GitHub っぽいスタイルを適用します。タイポグラフィ、コードブロック、テーブルなどを含む。

#### スタイリングの考慮事項
GitHub の Markdown 見た目を完全に再現するために、`.markdown-body` クラスの幅とパディングを設定することを検討してください。ドキュメントには以下が示されています：
- 大画面では最大幅 980px、パディング 45px、モバイルデバイス（画面幅 ≤ 767px）ではパディング 15px。
- これを次の CSS で実現できます：
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
これにより、レスポンシブ性が確保され、GitHub のデザインに合わせて読みやすさとユーザーエクスペリエンスが向上します。

#### 技術的なノートとベストプラクティス
- **DOctype の必要性:** ドキュメントは、ブラウザがクイックスモードに入ることで、特にダークモードでテーブルが正しくレンダリングされない可能性があるスタイルの問題を強調しています。これを防ぐために、HTML の先頭に DOctype を含めるようにしてください（例：`<!DOCTYPE html>`）。これにより、標準準拠のレンダリングが確保され、予期しない動作が防がれます。
- **Markdown パース:** パッケージは CSS を提供するだけで、Markdown を HTML にパースすることはありません。[marked.js](https://marked.js.org/) や React プロジェクトの [react-markdown](https://github.com/remarkjs/react-markdown) のような Markdown パーサーを使用して、Markdown テキストを HTML に変換し、この CSS でスタイルを適用する必要があります。
- **カスタム CSS の生成:** 高度なユーザーには、関連パッケージ [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) を使用してカスタム CSS を生成することができ、特定のテーマや修正に役立つ可能性があります。これは、パッケージが直接使用されるだけだと予想する人々にとって予期せぬ詳細です。

#### 特定のコンテキストでの使用
- **React プロジェクト:** React で `github-markdown-css` を `react-markdown` と組み合わせることは一般的です。両方をインストールした後、CSS をインポートし、コンポーネントを使用します：
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># こんにちは、世界！</ReactMarkdown>
    </div>
  );
  ```
  以前に示したように、幅とパディングの CSS も設定してください。

- **プレーン HTML で CDN を使用:** クイックプロトタイピングには、[cdnjs](https://cdnjs.com/libraries/github-markdown-css) で利用可能な CDN バージョンを直接リンクすることができます：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  そして、以前と同じように `.markdown-body` クラスを適用します。

#### 可能な問題とその解決策
- **スタイリングの競合:** プロジェクトで他の CSS フレームワーク（例：Tailwind、Bootstrap）を使用している場合、`.markdown-body` クラスがほとんどのスタイルを上書きするはずですが、しっかりとテストしてください。
- **ダークモードのサポート:** パッケージにはダークモードのサポートが含まれていますが、特にコードブロックとテーブルのテーマ切り替えが正しく処理されるように、Markdown パーサーとプロジェクトのセットアップが正しく動作することを確認してください。
- **ブラウザの互換性:** パッケージの広範な使用により、互換性は一般的に良好ですが、常に主要なブラウザ（Chrome、Firefox、Safari）でテストして一貫したレンダリングを確認してください。

#### 比較分析
他の Markdown CSS オプション（例：[Markdown CSS](https://markdowncss.github.io/)）と比較すると、「github-markdown-css」は GitHub のスタイルを直接再現する点で際立っています。これにより、ドキュメントが GitHub の見た目を反映するのに理想的です。ただし、追加のカスタマイズなしでテーマオプションを提供しないため、いくつかの代替案は、ボックスに複数のテーマを提供することができます。

#### テーブル: 主要な機能と考慮事項

| 機能                  | 説明                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| インストールコマンド     | `npm install github-markdown-css`                                           |
| CSS インポート方法        | `import 'github-markdown-css';` または HTML の `<link>`                         |
| 必要なクラス           | スタイル適用のための `.markdown-body`                                    |
| 幅とパディング        | 最大 980px、デスクトップでは 45px パディング、モバイル（画面幅 ≤ 767px）では 15px パディング            |
| DOctype の必要性      | クイックスモードを避け、適切なレンダリングを確保するために必要                  |
| カスタム CSS 生成    | [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) を使用して可能 |
| 互換性            | marked.js、react-markdown などの Markdown パーサーとの互換性、広範なブラウザサポート |

#### 結論
"github-markdown-css" を使用することは、GitHub の Markdown スタイルを再現するための開発者にとって直感的です。インストールと統合の手順に従い、追加のスタイルと技術的なノートを考慮することで、Markdown コンテンツに一貫性のあるプロフェッショナルな見た目を実現できます。高度なカスタマイズには生成パッケージを探索し、特に複雑なプロジェクトで互換性とレンダリングの問題をテストすることを忘れないでください。

#### 主要な引用
- [github-markdown-css npm パッケージページ](https://www.npmjs.com/package/github-markdown-css)
- [GitHub Markdown スタイルを再現するための最小限の CSS GitHub リポジトリ](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSS デモページ](https://sindresorhus.com/github-markdown-css/)
- [github-markdown-css npm パッケージの CSS を生成する](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN by cdnjs](https://cdnjs.com/libraries/github-markdown-css)