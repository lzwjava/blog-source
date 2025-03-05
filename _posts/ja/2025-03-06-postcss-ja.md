---
audio: false
generated: true
lang: ja
layout: post
title: PostCSSを使ったCSSの変換
translated: true
---

PostCSSをフロントエンドプロジェクトで使用する方法を説明します。PostCSSは、JavaScriptプラグインを使用してCSSを変換するツールで、自動接頭辞付加、最小化、将来のCSS構文のサポートなどの機能を提供します。以下にステップバイステップのガイドを示します。

### 1. **プロジェクトのセットアップ**
Node.jsがインストールされているフロントエンドプロジェクトがあることを確認します。ない場合は、以下のように初期化します：
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **PostCSSと必要なツールのインストール**
PostCSS、PostCSS CLI、および使用したいプラグイン（例：`autoprefixer`はベンダープレフィックス、`cssnano`は最小化）をインストールします：
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **CSSファイルの作成**
ソースCSSファイルを作成します。例：`src/styles.css`：
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **PostCSSの設定**
プロジェクトのルートに`postcss.config.js`ファイルを作成し、プラグインを指定します：
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // ベンダープレフィックスを追加
    require('cssnano')({ preset: 'default' }) // CSSを最小化
  ]
};
```

### 5. **ビルドスクリプトの追加**
`package.json`に、PostCSSでCSSを処理するスクリプトを追加します：
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: 入力ファイル
- `dist/styles.css`: 出力ファイル

### 6. **PostCSSの実行**
ビルドコマンドを実行します：
```bash
npm run build:css
```
これにより、`src/styles.css`が処理され、`dist/styles.css`に変換されたCSSが出力されます。例えば、`autoprefixer`はプレフィックスを追加し、`cssnano`は最小化します：
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **ビルドツールとの統合（オプション）**
より強力な設定を実現するために、PostCSSをWebpack、Vite、またはGulpなどのツールと統合します：

#### **Viteを使用する場合**
Viteを使用している場合は、`postcss`をインストールし、`vite.config.js`で設定します：
```javascript
// vite.config.js
import postcss from 'postcss';
import autoprefixer from 'autoprefixer';

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
};
```
ViteはCSSファイルをインポートすると自動的にPostCSSを処理します。

#### **Webpackを使用する場合**
`postcss-loader`をインストールします：
```bash
npm install --save-dev postcss-loader
```
`webpack.config.js`を更新します：
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### 8. **変更を監視する（オプション）**
開発中にCSSを自動的に処理するために、`package.json`のスクリプトを変更します：
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
`npm run watch:css`を実行してファイルの変更を監視します。

### 9. **一般的なプラグイン**
以下は人気のあるPostCSSプラグインです：
- `autoprefixer`: ブラウザのサポートに基づいてベンダープレフィックスを追加します。
- `cssnano`: CSSを最小化します。
- `postcss-preset-env`: 今すぐ将来のCSS機能を使用できます。
- `postcss-import`: `@import`ルールを解決します。
必要に応じてインストールします：
```bash
npm install --save-dev postcss-preset-env postcss-import
```
`postcss.config.js`に追加します：
```javascript
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-preset-env'),
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' })
  ]
};
```

### 例のワークフロー
1. `src/styles.css`でモダンなCSSを書きます：
```css
@custom-media --viewport-medium (width >= 768px);

:root {
  --main-color: #1a73e8;
}

.container {
  color: var(--main-color);
  display: grid;
}

@media (--viewport-medium) {
  .container {
    grid-template-columns: 1fr 1fr;
  }
}
```
2. `npm run build:css`を実行します。
3. `dist/styles.css`にプレフィックス、解決された変数、最小化されたCSSが含まれた処理されたCSSを取得します。

### ヒント
- CLIで`--map`を使用して（`postcss src/styles.css -o dist/styles.css --map`）デバッグ用のソースマップを生成します。
- プラグインのドキュメントを確認して、特定の設定オプションを確認します。
- フロントエンドフレームワーク（React、Vueなど）と組み合わせて、出力CSSをHTMLまたはバンドラーにリンクします。

特定の設定やプラグインについてお手伝いが必要な場合はお知らせください！