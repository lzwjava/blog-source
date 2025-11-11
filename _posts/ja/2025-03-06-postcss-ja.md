---
audio: false
generated: true
lang: ja
layout: post
title: PostCSSによるCSS変換
translated: true
type: note
---

フロントエンドプロジェクトでPostCSSを使用する方法を説明します。PostCSSはJavaScriptプラグインでCSSを変換するツールで、オートプレフィックス、ミニファイ、将来のCSS構文のサポートなどの機能を提供します。ステップバイステップガイドは以下の通りです：

### 1. **プロジェクトのセットアップ**
Node.jsがインストールされたフロントエンドプロジェクトを用意してください。ない場合は初期化します：
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **PostCSSと必要なツールのインストール**
PostCSS、PostCSS CLI、使用したいプラグイン（例：ベンダープレフィックス用の`autoprefixer`やミニファイ用の`cssnano`）をインストールします：
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **CSSファイルの作成**
ソースCSSファイル（例：`src/styles.css`）を作成します：
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **PostCSSの設定**
プロジェクトルートに`postcss.config.js`ファイルを作成し、プラグインを指定します：
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // ベンダープレフィックスを追加
    require('cssnano')({ preset: 'default' }) // CSSをミニファイ
  ]
};
```

### 5. **ビルドスクリプトの追加**
`package.json`にPostCSSでCSSを処理するスクリプトを追加します：
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
これにより`src/styles.css`が処理され、変換されたCSSが`dist/styles.css`に出力されます。例えば、`autoprefixer`がプレフィックスを追加し、`cssnano`がミニファイします：
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **ビルドツールとの統合（オプション）**
より堅牢なセットアップには、PostCSSをWebpack、Vite、Gulpなどのツールと統合します：

#### **Viteの場合**
Viteを使用する場合、`postcss`をインストールし`vite.config.js`で設定します：
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
ViteはCSSファイルをインポート時に自動的にPostCSSを処理します。

#### **Webpackの場合**
`postcss-loader`をインストール：
```bash
npm install --save-dev postcss-loader
```
`webpack.config.js`を更新：
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

### 8. **変更の監視（オプション）**
開発中にCSSを自動処理するには、`package.json`のスクリプトを変更：
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
`npm run watch:css`を実行してファイル変更を監視します。

### 9. **一般的なプラグイン**
人気のあるPostCSSプラグイン：
- `autoprefixer`: ブラウザサポートに基づいてベンダープレフィックスを追加
- `cssnano`: CSSをミニファイ
- `postcss-preset-env`: 将来のCSS機能を今日使用可能に
- `postcss-import`: `@import`ルールを解決
必要に応じてインストール：
```bash
npm install --save-dev postcss-preset-env postcss-import
```
`postcss.config.js`に追加：
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

### ワークフローの例
1. `src/styles.css`にモダンなCSSを記述：
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
2. `npm run build:css`を実行
3. プレフィックス、解決された変数、ミニファイが適用された処理済みCSSを`dist/styles.css`で取得

### ヒント
- デバッグ用にソースマップを生成するにはCLIで`--map`を使用（`postcss src/styles.css -o dist/styles.css --map`）
- 特定の設定オプションについてはプラグインのドキュメントを確認
- 出力CSSをHTMLやバンドラーにリンクして、フロントエンドフレームワーク（React、Vueなど）と組み合わせて使用

特定のセットアップやプラグインについてヘルプが必要な場合はお知らせください！