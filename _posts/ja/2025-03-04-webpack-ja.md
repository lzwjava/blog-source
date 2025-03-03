---
audio: false
generated: true
lang: ja
layout: post
title: Webpackをモジュールバンドラーとして使用する
translated: true
---

### 主要ポイント
- webpack バージョン 1.13.2 と webpack-dev-server バージョン 1.14.0 を使用するためには、特定の設定で Node.js プロジェクトを設定する必要があると考えられます。
- 研究によると、これらのバージョンを npm を通じてインストールし、設定ファイルを作成し、ライブ更新のための開発サーバーを実行することが推奨されています。
- 証拠は、index.html ファイルが存在していることを確認し、バンドルのための適切なファイルパスを含む設定が必要であることを示唆しています。

### インストールと設定
始めるには、[nodejs.org](https://nodejs.org) から Node.js がインストールされていることを確認してください。プロジェクトディレクトリを作成し、npm で初期化し、指定されたバージョンをインストールします。

- `npm init -y` を実行して package.json ファイルを設定します。
- `npm install webpack@1.13.2` と `npm install webpack-dev-server@1.14.0` でインストールします。

### 設定
`webpack.config.js` ファイルを作成して、ファイルのバンドル方法を定義します。基本的な設定には以下が含まれます。
- エントリーポイント（例：`./src/index.js`）。
- 出力パス（例：`dist` ディレクトリに `bundle.js`）。
- 開発サーバーの設定（例：静的ファイル用の `contentBase`）。

### 開発サーバーの実行
`npx webpack-dev-server` または npx が利用できない場合は `./node_modules/.bin/webpack-dev-server` を実行してサーバーを起動します。[http://localhost:8080](http://localhost:8080) にアクセスしてアプリケーションを表示し、変更時に自動的に更新されます。

### 予期せぬ詳細
これらの古いバージョンは、`contentBase` ではなく `static` を使用する必要があるなど、特定の設定が必要です。ファイルの提供には手動の調整が必要で、より自動化された新しいバージョンとは異なります。

---

### アンケートノート: Webpack 1.13.2 と Webpack-Dev-Server 1.14.0 の使用に関する詳細なガイド

この包括的なガイドでは、JavaScript プロジェクトに適した開発環境を設定し、使用するための webpack バージョン 1.13.2 と webpack-dev-server バージョン 1.14.0 の詳細な手順を提供します。これらのバージョンは 2016 年のものであり、現代の標準とは異なる設定や動作があります。このノートは、初心者がすべての必要な手順を理解し、明確さと完全性を確保することを目的としています。

#### 背景とコンテキスト
Webpack は、JavaScript のモジュールバンドラーで、歴史的にウェブアプリケーションのファイルをコンパイルし、バンドルし、依存関係を管理し、プロダクション用に最適化するために使用されてきました。Webpack-dev-server は、ライブリロード機能を備えた開発サーバーの付属ツールで、反復的な開発に最適です。指定されたバージョン、webpack 1.13.2 と webpack-dev-server 1.14.0 は 2016 年のものであり、機能的な古い設定で、レガシープロジェクトの互換性のために使用される可能性があります。

#### ステップバイステップのインストールと設定
まず、Node.js がインストールされていることを確認してください。これは、npm、パッケージマネージャーを使用するために必要です。[nodejs.org](https://nodejs.org) からダウンロードできます。現在の時間、2025 年 3 月 3 日月曜日 09:45 AM PST は設定に関係ありませんが、コンテキストとして記載されています。

1. **プロジェクトディレクトリの作成**: ターミナルを開き、新しいディレクトリ（例：`myproject`）を作成します。
   - コマンド: `mkdir myproject && cd myproject`

2. **npm プロジェクトの初期化**: `npm init -y` を実行して、デフォルト設定で `package.json` ファイルを作成し、npm 依存関係を設定します。

3. **特定のバージョンのインストール**: npm を使用して必要なバージョンをインストールします。
   - コマンド: `npm install webpack@1.13.2`
   - コマンド: `npm install webpack-dev-server@1.14.0`
   - これらのコマンドは、指定されたバージョンを `node_modules` に追加し、`package.json` の `dependencies` を更新します。

#### ディレクトリ構造とファイルの作成
開発サーバーが機能するためには、基本的なディレクトリ構造が必要です。
- 静的ファイル用の `public` ディレクトリを作成します: `mkdir public`
- アプリケーションコード用の `src` ディレクトリを作成します: `mkdir src`

`public` 内に `index.html` ファイルを作成します。これはアプリケーションを提供するために必要です。
```html
<html>
<body>
<script src="/bundle.js"></script>
</body>
</html>
```
このファイルは `bundle.js` を参照しており、webpack が生成し提供します。

`src` 内に `index.js` ファイルを作成し、基本的な内容を追加します。
```javascript
console.log('Hello, World!');
```
これはエントリーポイントで、webpack がバンドルします。

#### 設定ファイルの設定
ルートディレクトリに `webpack.config.js` ファイルを作成して webpack を設定します。
```javascript
const path = require('path');
module.exports = {
    entry: './src/index.js',
    output: {
        path: path.join(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    devServer: {
        contentBase: path.join(__dirname, 'public')
    }
};
```
- `entry`: 開始点（`src/index.js`）を指定します。
- `output`: バンドルされたファイルの場所（`dist/bundle.js`）を定義します。
- `devServer.contentBase`: 静的ファイル（例：`index.html`）を提供するための `public` ディレクトリを指します。

バージョン 1.14.0 では、古い API を反映して `contentBase` が使用されます。

#### 開発サーバーの実行
開発サーバーを起動するには、以下を使用します。
- 好まれる方法: `npx webpack-dev-server`
- 代替方法（npx が利用できない場合）: `./node_modules/.bin/webpack-dev-server`

このコマンドはサーバーを起動し、通常は [http://localhost:8080](http://localhost:8080) でアクセスできます。サーバーはメモリ上で実行されるため、ファイルはディスクに書き込まれず、動的に提供され、開発の便宜のためにライブリロードが有効になります。

#### 操作詳細と考慮事項
- **アプリケーションへのアクセス**: ブラウザを開いて [http://localhost:8080](http://localhost:8080) にアクセスします。`index.html` が表示され、`bundle.js` を読み込み、JavaScript を実行してコンソールに "Hello, World!" をログに出力します。
- **ライブ更新**: `src` 内のファイルを編集すると、サーバーが再コンパイルし、ブラウザが自動的に再読み込みされます。これは、webpack-dev-server の反復的な開発のための重要な機能です。
- **ポートの競合**: ポート 8080 が使用中の場合、サーバーが失敗する可能性があります。`webpack.config.js` の `devServer.port` で異なるポートを指定できます（例：`port: 9000`）。

#### ファイルの提供とパスの考慮事項
これらのバージョンでは、`devServer.contentBase` が指定されたディレクトリ（デフォルトでは現在のディレクトリ）からファイルを提供します。`index.html` が `public` にあることを確認してください。スクリプトタグ `<script src="/bundle.js"></script>` は、`output.publicPath` がデフォルトで '/' であり、`output.filename` が 'bundle.js' なので、`/bundle.js` でアクセスできます。

重要なポイントは、webpack-dev-server 1.14.0 は HTML ファイルを提供するために必要であり、スクリプトを自動的に挿入しないため、`index.html` に手動で含める必要があります。これは、プラグイン（例：`html-webpack-plugin`）がこれを自動化する現代的な設定とは異なります。

#### 互換性と制限
これらのバージョンは 2016 年のものであり、機能的ですが、現代の機能やセキュリティパッチが欠けている可能性があります。2025 年 3 月現在の Node.js バージョン（例：20.x）との互換性を確認することをお勧めしますが、Node.js 6 または 8 が必要な場合があり、これらのバージョンはサポートされていない可能性があります。現行の Node.js バージョン（例：20.x）でのテストは推奨されますが、廃棄警告に備えてください。

#### 表: バージョンの詳細と使用法
以下は、キーのバージョン情報と使用法の概要を示す表です。

| コンポーネント               | バージョン | リリース年 | キーの使用法のメモ                                      |
|-------------------------|---------|--------------|-----------------------------------------------------|
| Webpack                 | 1.13.2  | 2016         | モジュールバンドラー、エントリ/出力の設定が必要       |
| Webpack-Dev-Server      | 1.14.0  | 2016         | 開発サーバー、静的ファイル用に `contentBase` を使用 |

#### 高度な設定オプション
より多くの機能が必要なユーザーは、`devServer` に `hot: true` を追加してホットモジュール置換を有効にすることを検討してください。
```javascript
devServer: {
    contentBase: path.join(__dirname, 'public'),
    hot: true
}
```
これにより、モジュールの更新がページ全体の再読み込みなしで行われ、開発速度が向上します。

#### 結論
この設定は、webpack 1.13.2 と webpack-dev-server 1.14.0 を使用した基本的なが機能的な開発環境を提供します。これらのバージョンは古いため、現代のワークフローとは異なる点が多く、ファイルの提供や現行ツールとの互換性の問題が予想されます。プロダクションではこれらのバージョンは推奨されませんが、レガシープロジェクトのメンテナンスにはこのガイドが役立つでしょう。

#### キーの引用
- [Webpack 公式ドキュメントの詳細な設定ガイド](https://webpack.js.org/)
- [Webpack-dev-server の設定オプション](https://webpack.js.org/configuration/dev-server/)