---
audio: false
generated: true
lang: ja
layout: post
title: Webpackをモジュールバンドラーとして使用する
translated: true
type: note
---

### 主なポイント
- webpackバージョン1.13.2とwebpack-dev-serverバージョン1.14.0を使用するには、特定の設定でNode.jsプロジェクトをセットアップする必要があるようです。
- 調査によると、これらのバージョンをnpm経由でインストールし、設定ファイルを作成し、ライブアップデートのための開発サーバーを実行する必要があります。
- 証拠から、index.htmlファイルを適切に配置し、バンドリング用の適切なファイルパスが設定に含まれていることを確認する傾向があります。

### インストールとセットアップ
開始するには、[nodejs.org](https://nodejs.org)からNode.jsがインストールされていることを確認してください。プロジェクトディレクトリを作成し、npmで初期化し、指定されたバージョンをインストールします：

- `npm init -y`を実行してpackage.jsonファイルをセットアップします。
- `npm install webpack@1.13.2`と`npm install webpack-dev-server@1.14.0`でインストールします。

### 設定
ファイルのバンドル方法を定義するために`webpack.config.js`ファイルを作成します。基本的なセットアップには以下が含まれます：
- エントリーポイント（例：`./src/index.js`）
- 出力パス（例：`dist`ディレクトリに`bundle.js`）
- 静的ファイル用の`contentBase`などのDev Server設定

### 開発サーバーの実行
`npx webpack-dev-server`またはnpxが利用できない場合は`./node_modules/.bin/webpack-dev-server`でサーバーを起動します。[http://localhost:8080](http://localhost:8080)でアプリケーションにアクセスでき、変更時に自動更新されます。

### 予期しない詳細
予期しない側面は、これらの古いバージョンでは現代的な`static`の代わりに`contentBase`などの特定の設定が必要であり、セットアップが新しいバージョンよりも自動化が少なく、ファイル提供のために手動での調整が必要な場合があることです。

---

### 調査ノート：Webpack 1.13.2とWebpack-Dev-Server 1.14.0の使用に関する詳細ガイド

この包括的なガイドは、webpackバージョン1.13.2とwebpack-dev-serverバージョン1.14.0のセットアップと使用に関する詳細な手順を提供し、JavaScriptプロジェクトに適した開発環境に焦点を当てています。これらのバージョンは古いため、特定の設定と動作が現代的な標準とは異なり、このノートは素人でも明確かつ完全に理解できるように必要なすべてのステップをカバーすることを目的としています。

#### 背景とコンテキスト
WebpackはJavaScriptのモジュールバンドラーで、歴史的にWebアプリケーション用のファイルをコンパイルおよびバンドルし、依存関係を管理し、本番用に最適化するために使用されてきました。Webpack-dev-serverは、ライブリロード機能を備えた開発サーバーを提供するコンパニオンツールで、反復的な開発に理想的です。指定されたバージョンであるwebpack 1.13.2とwebpack-dev-server 1.14.0は2016年のもので、古いですがまだ機能するセットアップを示しており、レガシープロジェクトの互換性のために使用される可能性があります。

#### ステップバイステップのインストールとセットアップ
開始するには、npm（使用するパッケージマネージャー）に必要なNode.jsがインストールされていることを確認してください。[nodejs.org](https://nodejs.org)からダウンロードできます。現在時刻である2025年3月3日月曜日午前9時45分PSTはセットアップには無関係ですが、コンテキストのために記載されています。

1. **プロジェクトディレクトリの作成**: ターミナルを開き、新しいディレクトリを作成します（例："myproject"）：
   - コマンド：`mkdir myproject && cd myproject`

2. **npmプロジェクトの初期化**: `npm init -y`を実行して、デフォルト設定で`package.json`ファイルを作成し、npm依存関係のためのプロジェクトをセットアップします。

3. **特定バージョンのインストール**: npmを使用して必要なバージョンをインストールします：
   - コマンド：`npm install webpack@1.13.2`
   - コマンド：`npm install webpack-dev-server@1.14.0`
   - これらのコマンドは、指定されたバージョンを`node_modules`に追加し、`package.json`の`dependencies`を更新します。

#### ディレクトリ構造とファイル作成
開発サーバーが機能するためには、基本的なディレクトリ構造が必要です：
- 静的ファイル用に`public`ディレクトリを作成：`mkdir public`
- アプリケーションコード用に`src`ディレクトリを作成：`mkdir src`

`public`内に、アプリケーション提供に不可欠な`index.html`ファイルを作成します：
```html
<html>
<body>
<script src="/bundle.js"></script>
</body>
</html>
```
このファイルは、webpackが生成して提供する`bundle.js`を参照しています。

`src`内に、基本的な内容で`index.js`ファイルを作成します：
```javascript
console.log('Hello, World!');
```
これはwebpackがバンドルするエントリーポイントです。

#### 設定ファイルのセットアップ
ルートディレクトリに`webpack.config.js`ファイルを作成してwebpackを設定します：
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
- `output`: バンドルファイルの出力先（`dist/bundle.js`）を定義します。
- `devServer.contentBase`: `index.html`などの静的ファイルを提供するための`public`ディレクトリを指します。

バージョン1.14.0では、現代的な`static`の代わりに`contentBase`が使用され、古いAPIを反映していることに注意してください。

#### 開発サーバーの実行
開発サーバーを起動するには、以下を使用します：
- 推奨：`npx webpack-dev-server`
- 代替（npxが利用できない場合）：`./node_modules/.bin/webpack-dev-server`

このコマンドはサーバーを起動し、通常は[http://localhost:8080](http://localhost:8080)でアクセス可能です。サーバーはメモリ内で実行され、ファイルはディスクに書き込まれず動的に提供され、開発の利便性のためにライブリロードが有効になります。

#### 操作の詳細と考慮事項
- **アプリケーションへのアクセス**: ブラウザで[http://localhost:8080](http://localhost:8080)を開きます。`index.html`が表示され、`bundle.js`をロードしてJavaScriptを実行し、コンソールに"Hello, World!"をログ出力するはずです。
- **ライブアップデート**: `src`内のファイルを編集すると、サーバーは自動的に再コンパイルし、ブラウザをリロードします。これは反復的な開発のためのwebpack-dev-serverの主要な機能です。
- **ポート競合**: ポート8080が使用中の場合、サーバーは失敗する可能性があります。`webpack.config.js`の`devServer.port`で異なるポートを指定できます（例：`port: 9000`）。

#### ファイル提供とパスの考慮事項
バージョンにより、`devServer.contentBase`は指定されたディレクトリ（設定されていない場合は現在のディレクトリがデフォルト）からファイルを提供します。ルートで提供されるように`index.html`が`public`内にあることを確認してください。スクリプトタグ`<script src="/bundle.js"></script>`は、`output.publicPath`がデフォルトで'/'であり、`output.filename`が'bundle.js'であるため、`/bundle.js`でアクセス可能になります。

重要な詳細は、webpack-dev-server 1.14.0は提供のためにHTMLファイルを必要とし、スクリプトを自動的に注入しないため、`index.html`への手動での包含が必要であることです。これは、`html-webpack-plugin`のようなプラグインがこれを自動化する可能性がある現代的なセットアップとは対照的です。

#### 互換性と制限
これらのバージョンは2016年のもので、機能しますが、現代的な機能とセキュリティパッチが欠けています。現在のNode.jsバージョン（2025年3月時点）との互換性を確認する必要があります。古いバージョンはサポートされていないNode.js 6または8を必要とする可能性があるためです。現在のNode.jsバージョン（例：20.x）でのテストを推奨しますが、非推奨警告の可能性に備えてください。

#### 表：バージョンの詳細と使用法
以下は、主要なバージョン情報と使用上の注意をまとめた表です：

| コンポーネント          | バージョン | リリース年 | 主な使用上の注意                                      |
|-------------------------|------------|------------|-----------------------------------------------------|
| Webpack                 | 1.13.2     | 2016       | モジュールバンドラー、エントリー/出力の設定が必要        |
| Webpack-Dev-Server      | 1.14.0     | 2016       | 開発サーバー、静的ファイルに`contentBase`を使用          |

#### 高度な設定オプション
さらに必要なユーザーは、`devServer`に`hot: true`を追加してホットモジュール置換を有効にすることを検討してください：
```javascript
devServer: {
    contentBase: path.join(__dirname, 'public'),
    hot: true
}
```
これにより、フルページリロードなしでモジュールの更新が可能になり、開発速度が向上します。

#### 結論
このセットアップは、webpack 1.13.2とwebpack-dev-server 1.14.0を使用した基本的ながら機能する開発環境を提供します。これらのバージョンは古いため、手動でのファイル提供や現在のツールとの潜在的な互換性問題など、現代的なワークフローとの違いを予想してください。本番用には、更新の欠如によりこれらのバージョンは推奨されませんが、レガシープロジェクトのメンテナンスにはこのガイドで十分です。

#### 主要な引用文献
- [Webpack documentation detailed setup guide](https://webpack.js.org/)
- [Webpack-dev-server configuration options](https://webpack.js.org configuration/dev-server/)