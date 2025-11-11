---
audio: false
generated: true
lang: ja
layout: post
title: Font Awesome の問題
translated: true
type: note
---

「can't resolve .../fonts/fontawesome-webfont.woff2」エラーは、通常、Font AwesomeのCSSファイルが参照しているフォントファイル（`fontawesome-webfont.woff2`など）が指定されたパスに見つからない場合に発生します。この問題は、npm、Webpack、または他のモジュールバンドラーを使用するプロジェクトで頻繁に発生します。以下にこのエラーを解決する手順を示します。

---

### 1. Font Awesomeのインストールを確認する
プロジェクトにFont Awesomeが正しくインストールされていることを確認してください。

- **npmを使用している場合**:
  ```bash
  npm install @fortawesome/fontawesome-free
  ```
  これにより、Font Awesomeの無料版がインストールされます。

- パッケージが`package.json`にリストされていることを確認してください:
  ```json
  "dependencies": {
    "@fortawesome/fontawesome-free": "^6.x.x"
  }
  ```

---

### 2. CSS内のフォントファイルパスを確認する
このエラーは、`fontawesome.css`ファイルが、プロジェクトのファイル構造やビルドプロセスに合致しない相対パス（例: `../fonts/fontawesome-webfont.woff2`）でフォントファイルを参照しているために発生することがよくあります。

- **CSSファイルを探す**:
  `node_modules/@fortawesome/fontawesome-free/css/all.css`（または類似のパス）にあるFont AwesomeのCSSファイルを見つけてください。

- **font-face宣言を検査する**:
  CSSファイルを開き、`@font-face`ルールを探してください。以下のようになっているはずです:
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('../fonts/fontawesome-webfont.woff2') format('woff2'),
         url('../fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- **フォントファイルを確認する**:
  参照されているフォントファイルが`node_modules/@fortawesome/fontawesome-free/webfonts/`に存在するか確認してください。`webfonts`フォルダには通常、`fontawesome-webfont.woff2`などのファイルが含まれています。

---

### 3. パス問題を修正する
フォントファイルが解決されない場合は、ビルドプロセスでパスがどのように扱われるかを調整する必要があるかもしれません。

#### オプション1: フォントファイルを公開ディレクトリにコピーする
フォントファイルをアプリケーションからアクセス可能なディレクトリ（例: `public/fonts` または `src/fonts`）に手動でコピーします。

- **ファイルをコピーする**:
  ```bash
  mkdir -p public/fonts
  cp -r node_modules/@fortawesome/fontawesome-free/webfonts/* public/fonts/
  ```

- **CSSを更新する**:
  `fontawesome.css`ファイルを変更して、新しいフォントの場所を指すようにします:
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('/fonts/fontawesome-webfont.woff2') format('woff2'),
         url('/fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- または、CSSプリプロセッサやポストプロセッサを使用してパスを書き換えてください。

#### オプション2: Webpack（または他のバンドラー）を設定する
Webpackを使用している場合は、フォントファイルを解決して読み込めることを確認してください。

- **file-loaderまたはurl-loaderをインストールする**:
  ```bash
  npm install file-loader --save-dev
  ```

- **Webpack設定を更新する** (`webpack.config.js`):
  フォントファイルを処理するルールを追加します:
  ```javascript
  module: {
    rules: [
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/',
              publicPath: '/fonts/',
            },
          },
        ],
      },
    ],
  }
  ```

- Font Awesome CSSがJavaScriptでインポートされていることを確認してください:
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```

#### オプション3: CDNを使用する
フォントファイルをバンドルしたくない場合は、CDNを使用してFont Awesomeを読み込むことができます。

- ローカルのインポートをHTML内のCDNリンクに置き換えます:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  ```

- コードからローカルのFont Awesome CSSインポートを削除します。

---

### 4. 大文字と小文字の区別を確認する
ファイルパスは、一部のシステム（例: Linux）では大文字と小文字を区別します。CSS内のファイル名とパスが実際のファイル名と正確に一致していることを確認してください。

- 例えば、ファイルが`fontawesome-webfont.woff2`であるのに、CSSが`FontAwesome-WebFont.woff2`を参照している場合、失敗します。

---

### 5. キャッシュをクリアしてリビルドする
場合によっては、古いキャッシュが解決の問題を引き起こすことがあります。

- npmキャッシュをクリアする:
  ```bash
  npm cache clean --force
  ```

- `node_modules`と`package-lock.json`を削除し、再インストールします:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

- プロジェクトをリビルドします:
  ```bash
  npm run build
  ```

---

### 6. 代替案: SCSS経由でFont Awesomeを使用する
SCSSを使用している場合は、Font AwesomeのSCSSファイルをインポートし、フォントパスを設定できます。

- 上記のようにFont Awesomeをインストールします。
- メインのSCSSファイルでSCSSをインポートします:
  ```scss
  $fa-font-path: '~@fortawesome/fontawesome-free/webfonts';
  @import '~@fortawesome/fontawesome-free/scss/fontawesome';
  @import '~@fortawesome/fontawesome-free/scss/solid';
  ```

- SCSSコンパイラが`webfonts`フォルダを正しく解決することを確認してください。

---

### 7. デバッグのヒント
- **ブラウザコンソールを確認する**:
  フォントファイルに対する404エラーを探し、要求されたURLをメモしてください。
- **ビルド出力を検査する**:
  フォントファイルが出力ディレクトリ（例: `dist/fonts/`）に含まれていることを確認してください。
- **`resolve-url-loader`を使用する**:
  WebpackをSCSSと共に使用している場合は、`resolve-url-loader`をインストールして相対URLの解決を支援します:
  ```bash
  npm install resolve-url-loader --save-dev
  ```

---

### 8. フレームワークを使用している場合
一部のフレームワーク（例: React, Vue, Angular）では追加の設定が必要な場合があります:

- **React**:
  CSSが`index.js`または`App.js`でインポートされていることを確認してください:
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```
  必要に応じて、上記のWebpack設定を使用してください。

- **Vue**:
  Vue CLIを使用している場合は、Webpackルールを`vue.config.js`に追加します:
  ```javascript
  module.exports = {
    chainWebpack: (config) => {
      config.module
        .rule('fonts')
        .test(/\.(woff|woff2|eot|ttf|otf)$/)
        .use('file-loader')
        .loader('file-loader')
        .options({
          name: '[name].[ext]',
          outputPath: 'fonts/',
          publicPath: '/fonts/',
        });
    },
  };
  ```

- **Angular**:
  Font Awesome CSSを`angular.json`に追加します:
  ```json
  "styles": [
    "node_modules/@fortawesome/fontawesome-free/css/all.css",
    "src/styles.css"
  ]
  ```

---

### 9. 修正をテストする
- 開発サーバーを実行します:
  ```bash
  npm start
  ```
- ブラウザでアプリを開き、Font Awesomeアイコンがコンソールエラーなしで正しく読み込まれることを確認してください。

---

### 10. 問題が解決しない場合
- **競合するバージョンを確認する**:
  異なるバージョンのFont Awesome（例: v5とv6）を混在させていないことを確認してください。
- **類似の問題を検索する**:
  あなたの設定（例: Webpack, Create React App）に特有のエラーをStack OverflowやGitHubで探してください。
- **詳細を提供する**:
  さらにヘルプが必要な場合は、以下を共有してください:
  - プロジェクトの設定（例: Webpack, Reactなど）。
  - 正確なエラーメッセージ。
  - 関連するコードスニペット（例: Font Awesomeをどのようにインポートしているか）。

---

これで「can't resolve .../fonts/fontawesome-webfont.woff2」エラーが解決するはずです。特定のステップでヘルプが必要な場合はお知らせください！