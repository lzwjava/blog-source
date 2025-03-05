---
audio: false
generated: true
lang: ja
layout: post
title: Autoprefixerを使う
translated: true
---

Autoprefixerの使用方法をフロントエンド開発で説明します。Autoprefixerは、CSSに自動的にベンダープレフィックスを追加し、クロスブラウザ互換性を確保するPostCSSプラグインです。

Autoprefixerをフロントエンドワークフローに統合する主な方法は以下の通りです：

1. npmを使用する（最も一般的なアプローチ）
```bash
# autoprefixerとpostcssをインストール
npm install autoprefixer postcss --save-dev
```

2. PostCSS CLIの基本設定
```bash
# postcss-cliをインストール
npm install postcss-cli --save-dev

# postcss.config.jsファイルを作成
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# package.jsonのスクリプトに追加
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. ビルドツールを使用する：

a) Webpackとpostcss-loader
```bash
npm install postcss-loader --save-dev
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: ['autoprefixer']
              }
            }
          }
        ]
      }
    ]
  }
}
```

b) Vite（組み込みサポート）
```javascript
// vite.config.js
import autoprefixer from 'autoprefixer'

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
}
```

4. 設定オプション
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // 対象ブラウザ
      grid: true, // グリッドプレフィックスを有効にする
      flexbox: 'no-2009' // フレックスボックスサポートオプション
    })
  ]
}
```

5. CSSでの使用例
```css
/* 入力 */
.container {
  display: flex;
  justify-content: space-between;
}

/* 出力（Autoprefixer後） */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

主要な機能とヒント：
- Can I Useデータに基づいて自動的にプレフィックスを追加
- browserslist（通常はpackage.json）で制御
- 古いCSSから古いプレフィックスを削除
- カスタムプロパティなどの最新CSS機能と連携

package.jsonの基本的なbrowserslist例：
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

実行方法：
```bash
# PostCSS CLIを使用
npx postcss src/*.css --dir dist

# またはnpmスクリプトを使用
npm run build:css
```

プロジェクトの既存設定（Webpack、Viteなど）に基づいて統合方法を選択してください。WebpackまたはViteのアプローチは、既存のビルドプロセスとよく連携するため、現代のフロントエンド開発で最も一般的です。