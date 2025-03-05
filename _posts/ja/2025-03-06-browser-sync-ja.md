---
audio: false
generated: true
lang: ja
layout: post
title: ブラウザシンクを使用して
translated: true
---

BrowserSyncは、ブラウザのアクションを同期し、ファイルを自動的に再読み込みし、ローカル開発サーバーを提供することで、フロントエンド開発を効率化する素晴らしいツールです。以下は、フロントエンドワークフローでBrowserSyncを使用するためのステップバイステップのガイドです。

---

### 1. **Node.jsとnpmをインストール**
BrowserSyncはNode.jsツールなので、Node.jsとnpm（Node Package Manager）がインストールされている必要があります。まだインストールしていない場合：
- [nodejs.org](https://nodejs.org/)からダウンロードしてインストールします。
- インストールを確認：
  ```bash
  node -v
  npm -v
  ```

---

### 2. **BrowserSyncをインストール**
グローバルまたはプロジェクト内にBrowserSyncをインストールできます。

#### オプション1：グローバルインストール
ターミナルで次のコマンドを実行して、BrowserSyncをグローバルにインストールします：
```bash
npm install -g browser-sync
```
これにより、`browser-sync`コマンドをどこからでも使用できます。

#### オプション2：ローカルインストール（プロジェクトに推奨）
特定のプロジェクトに依存関係を結びつけたい場合：
```bash
npm install browser-sync --save-dev
```
これにより、BrowserSyncがプロジェクトの`node_modules`に追加され、`package.json`にリストされます。

---

### 3. **BrowserSyncを開始**
セットアップによっては、BrowserSyncを異なる方法で使用できます。

#### 基本的な使用方法（静的ファイル）
静的なHTML、CSS、JSファイルを使用している場合、プロジェクトフォルダに移動し、次のコマンドを実行します：
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`: ローカルサーバーを実行（現在のディレクトリからファイルを提供）。
- `--files`: これらのファイルの変更を監視し、ブラウザを自動的に再読み込みします。

例えば、フォルダ構造が以下の場合：
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
上記のコマンドを実行すると：
- `http://localhost:3000`（デフォルトポート）でサーバーが開始されます。
- デフォルトブラウザが開きます。
- `index.html`、`style.css`、または`script.js`が変更されるたびにページが再読み込みされます。

#### プロキシモード（既存のサーバー）
バックエンドサーバー（例：Node.js、PHP、Python）を使用している場合は、プロキシオプションを使用します：
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`: 要求を既存のサーバーにプロキシします（`http://localhost:8000`をサーバーのURLに置き換えます）。
- BrowserSyncは、自動再読み込みなどの機能をオーバーレイします。

---

### 4. **主要な機能**
BrowserSyncが実行されていると、以下が利用できます：
- **ライブリロード**：監視対象のファイルの変更がブラウザの即時リフレッシュをトリガーします。
- **クロスデバイス同期**：スクロール、クリック、フォーム入力がすべての接続されたデバイス（例：デスクトップ、スマートフォン、タブレット）で同期されます。
- **UIダッシュボード**：`http://localhost:3001`（デフォルト）でアクセスできるコントロールパネルを使用して設定を調整またはサーバーを停止します。

---

### 5. **ビルドツールとの統合（オプション）**
GulpやWebpackなどのツールを使用している場合、BrowserSyncはシームレスに統合できます。

#### Gulpの例
GulpとBrowserSyncをインストール：
```bash
npm install --save-dev gulp browser-sync
```
`gulpfile.js`を作成：
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // 現在のディレクトリからファイルを提供
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
実行：
```bash
gulp
```

---

### 6. **一般的なコマンドとオプション**
- ポートの変更：`--port 8080`
- 自動開きを無効にする：`--no-open`
- 特定のファイルを監視：`--files "path/to/files/*"`
- 完全なリスト：`browser-sync --help`を実行

---

### 7. **トラブルシューティング**
- ポートが使用中：`--port <number>`でポートを変更します。
- リロードなし：`--files`内のファイルパスがプロジェクト構造と一致していることを確認します。
- 権限：グローバルにインストールされている場合、Linux/macOSで`sudo`が必要になることがあります（例：`sudo npm install -g browser-sync`）。

---

これで、BrowserSyncはフロントエンド開発を加速する準備が整いました。基本的なコマンドから始め、必要に応じて調整し、よりスムーズなワークフローを楽しんでください。特定のセットアップでお手伝いが必要な場合はお知らせください！