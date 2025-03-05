---
audio: false
generated: true
lang: ja
layout: post
title: ShellJSを使用してシェルコマンドを実行する
translated: true
---

ShellJSは、Node.jsプロジェクトで使用するためのUnixシェルコマンド（`cp`、`mkdir`、`exec`など）を提供するJavaScriptライブラリです。これにより、JavaScriptで直接熟知のあるシェルコマンドを実行できるため、クロスプラットフォームのスクリプトの作成が簡単になります。しかし、ブラウザで実行されるコード（通常はフロントエンド開発と呼ばれます）に対しては、ShellJSを直接適用することはできません。これは、ブラウザ環境ではNode.jsのAPIが利用できないためです。以下に、その理由とフロントエンド開発ワークフローの中でShellJSを効果的に使用する方法について説明します。

### ShellJSがブラウザで実行できない理由
- **Node.js依存性**: ShellJSは、ファイルシステムへのアクセスやプロセスの実行、その他のシステムレベルの操作を提供するNode.jsランタイムの上に構築されています。これらのAPIは、ブラウザのサンドボックス型のセキュリティモデルにより利用できません。
- **ブラウザのセキュリティ制限**: ブラウザは、ユーザーを悪意のあるスクリプトから保護するために、JavaScriptがローカルファイルシステムにアクセスするか、任意のコマンドを実行することを防ぎます。ShellJSのコマンド（例：`exec`（外部プロセスの実行）や`cp`（ファイルのコピー））は、これらの機能に依存しているため、ブラウザ環境では機能しません。

その結果、ブラウザで実行されるクライアントサイドのJavaScriptではShellJSを直接使用することはできません。しかし、Node.jsで実行されるビルドプロセスや開発ツールにShellJSを統合することで、フロントエンド開発においても有益な役割を果たすことができます。

### フロントエンド開発ワークフローでのShellJSの使用方法
ShellJSはブラウザで実行されませんが、Node.jsベースのスクリプトを使用して、フロントエンド開発をサポートするタスクを自動化するために利用できます。フロントエンドプロジェクトは、Node.jsで実行されるビルドツール（例：Webpack、Gulp、Grunt）に依存することが多く、これらにはShellJSを組み込んでワークフローを簡素化することができます。以下にその方法を示します。

#### 1. ShellJSのインストール
まず、システムにNode.jsがインストールされていることを確認し、npmまたはyarnを使用してプロジェクトにShellJSを追加します：

```bash
npm install shelljs
```

または

```bash
yarn add shelljs
```

#### 2. ShellJSを使用したNode.jsスクリプトの作成
フロントエンドプロジェクトに関連するタスク（例：ファイルのコピー、ディレクトリの作成、コマンドラインツールの実行）を実行するスクリプトを作成します。このスクリプトを`.js`ファイル（例：`build.js`）として保存します。

以下は、フロントエンドアセットを準備する例スクリプトです：

```javascript
const shell = require('shelljs');

// ビルドディレクトリが存在しない場合は作成
shell.mkdir('-p', 'build');

// HTMLファイルをビルドディレクトリにコピー
shell.cp('-R', 'src/*.html', 'build/');

// SassをCSSにコンパイル
shell.exec('sass src/styles.scss build/styles.css');

// JavaScriptファイルをコピー
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: `-p`オプションを使用して、`build`ディレクトリが既に存在する場合でもエラーを出さずに作成します。
- **`shell.cp('-R', 'src/*.html', 'build/')`**: `-R`オプションを使用して、`src`から`build`にすべてのHTMLファイルを再帰的にコピーします。
- **`shell.exec('sass src/styles.scss build/styles.css')`**: Sassコンパイラを実行してCSSを生成します。

#### 3. スクリプトのワークフローへの統合
このスクリプトは以下のように実行できます：
- **Node.jsを直接使用**:
  ```bash
  node build.js
  ```
- **npmスクリプトとして**: `package.json`に追加します：
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  そして実行します：
  ```bash
  npm run build
  ```
- **ビルドツールと一緒に**: GulpなどのツールにShellJSを組み込みます。例えば：
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. フロントエンド開発での使用例
ShellJSは、フロントエンドワークフローのさまざまなタスクを自動化することができます：
- **アセット管理**: 画像、フォント、その他の静的ファイルをビルドディレクトリにコピーします。
- **CSS/JavaScript処理**: Sass、PostCSS、UglifyJSなどのツールを`shell.exec`を使用して実行します。
- **テストとリント**: テストランナーやリントツール（例：`shell.exec('eslint src/*.js')`）を実行します。
- **デプロイメント準備**: ファイルをバンドルするかディレクトリをクリーンアップします（例：`shell.rm('-rf', 'build/*')`）。

### 例: フロントエンドビルドプロセスの自動化
HTML、Sass、JavaScriptを使用してシンプルなWebアプリを構築しているとします。以下のようにShellJSを使用してビルドを自動化できます。

**ディレクトリ構造**:
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**:
```javascript
const shell = require('shelljs');

// ビルドディレクトリをクリーンアップ
shell.rm('-rf', 'build/*');

// ビルドディレクトリを作成
shell.mkdir('-p', 'build');

// HTMLをコピー
shell.cp('src/index.html', 'build/');

// Sassをコンパイル
shell.exec('sass src/styles.scss build/styles.css');

// JavaScriptをコピー
shell.cp('src/app.js', 'build/');
```

**package.json**:
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

`npm run build`を実行すると、ShellJSはコンパイルされたファイルとコピーされたファイルを`build`ディレクトリに準備し、デプロイメントに備えます。

### 主要なポイント
- **ブラウザでの使用不可**: システムレベルの操作に依存するため、ブラウザではShellJSを実行できません。
- **ビルドスクリプトに最適**: ファイル操作やコマンド実行などのフロントエンドタスクを自動化するために、Node.jsベースのスクリプトで使用します。
- **クロスプラットフォーム**: ShellJSは、Windows、Linux、macOSの異なる開発環境でも一貫して動作するため、クロスプラットフォームに最適です。

Node.jsで動作するビルドプロセスにShellJSを組み込むことで、ブラウザで直接実行できないにもかかわらず、強力な自動化をフロントエンド開発ワークフローに追加できます。