---
audio: false
generated: true
lang: ja
layout: post
title: オートプレフィクサーの使い方
translated: true
type: note
---

フロントエンド開発におけるAutoprefixerの使用方法について説明します。AutoprefixerはPostCSSプラグインで、CSSにベンダープレフィックスを自動的に追加し、クロスブラウザ互換性を確保します。

以下はAutoprefixerをフロントエンドワークフローに統合する主な方法です：

1. npmを使用する方法（最も一般的なアプローチ）
```bash
# autoprefixerとpostcssをインストール
npm install autoprefixer postcss --save-dev
```

2. PostCSS CLIを使用した基本設定
```bash
# postcss-cliをインストール
npm install postcss-cli --save-dev

# postcss.config.jsファイルを作成
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# package.jsonのscriptsに追加
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. ビルドツールとの連携：

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
      grid: true, // グリッドプレフィックスを有効化
      flexbox: 'no-2009' // Flexboxサポートオプション
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

/* 出力（Autoprefixer適用後） */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

主な機能とヒント：
- Can I Useデータに基づいてプレフィックスを自動追加
- browserslistで制御（通常package.jsonに記載）
- 古いCSSから不要なプレフィックスを削除
- カスタムプロパティなどの最新CSS機能に対応

package.jsonでの基本的なbrowserslistの例：
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

プロジェクトの既存の設定（Webpack、Viteなど）に基づいて統合方法を選択してください。WebpackやViteを使用するアプローチは、既存のビルドプロセスと上手く連携するため、現代のフロントエンド開発では最も一般的です。