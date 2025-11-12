---
audio: false
generated: true
lang: ja
layout: post
title: ブラウザシンクの使い方
translated: true
type: note
---

BrowserSyncは、ブラウザアクションの同期、ファイルの自動リロード、ローカル開発サーバーの提供を通じてフロントエンド開発を効率化する素晴らしいツールです。以下に、フロントエンドワークフローでBrowserSyncを使用するためのステップバイステップガイドを紹介します：

---

### 1. **Node.jsとnpmのインストール**
BrowserSyncはNode.jsツールなので、Node.jsとnpm（Node Package Manager）のインストールが必要です。まだお持ちでない場合は：
- [nodejs.org](https://nodejs.org/)からダウンロードしてインストールしてください。
- インストールを確認：
  ```bash
  node -v
  npm -v
  ```

---

### 2. **BrowserSyncのインストール**
BrowserSyncはグローバルまたはプロジェクトローカルにインストールできます。

#### オプション1: グローバルインストール
ターミナルで次のコマンドを実行してBrowserSyncをグローバルにインストール：
```bash
npm install -g browser-sync
```
これにより、どこからでも`browser-sync`コマンドを使用できるようになります。

#### オプション2: ローカルインストール（プロジェクト推奨）
依存関係を特定のプロジェクトに紐付けたい場合：
```bash
npm install browser-sync --save-dev
```
これにより、BrowserSyncがプロジェクトの`node_modules`に追加され、`package.json`にリストされます。

---

### 3. **BrowserSyncの起動**
セットアップに応じて、BrowserSyncをさまざまな方法で使用できます：

#### 基本使用法（静的ファイル）
静的HTML、CSS、JSファイルを扱う場合、プロジェクトフォルダに移動して実行：
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`: ローカルサーバーを実行（現在のディレクトリからファイルを提供）
- `--files`: これらのファイルの変更を監視し、ブラウザを自動的にリロード

例：フォルダ構造が以下の場合：
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
上記のコマンドを実行すると：
- `http://localhost:3000`（デフォルトポート）でサーバーが起動
- デフォルトブラウザが開く
- `index.html`、`style.css`、`script.js`が変更されるたびにページがリロード

#### プロキシモード（既存サーバー）
バックエンドサーバー（例：Node.js、PHP、Python）を使用している場合、プロキシオプションを使用：
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`: 既存サーバーへのリクエストをプロキシ（`http://localhost:8000`をサーバーのURLに置き換え）
- BrowserSyncはその機能（自動リロードなど）を上乗せします

---

### 4. **主な機能**
BrowserSyncが実行されると、以下が利用可能：
- **ライブリロード**: 監視ファイルへの変更が即座にブラウザ更新をトリガー
- **クロスデバイス同期**: スクロール、クリック、フォーム入力が全接続デバイス（デスクトップ、スマートフォン、タブレットなど）で同期
- **UIダッシュボード**: `http://localhost:3001`（デフォルト）でコントロールパネルにアクセスし、設定調整やサーバー停止が可能

---

### 5. **ビルドツールとの統合（オプション）**
GulpやWebpackなどのツールを使用する場合、BrowserSyncはシームレスに統合できます。

#### Gulpでの例
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
- ポート変更: `--port 8080`
- 自動オープン無効: `--no-open`
- 特定ファイルの監視: `--files "path/to/files/*"`
- 完全なリスト: `browser-sync --help`を実行

---

### 7. **トラブルシューティング**
- **ポート使用中**: `--port <番号>`でポートを変更
- **リロードしない**: `--files`のファイルパスがプロジェクト構造と一致していることを確認
- **権限問題**: グローバルインストールの場合、`sudo`が必要な場合があります（例：Linux/macOSでは`sudo npm install -g browser-sync`）

---

以上です！BrowserSyncはこれでフロントエンド開発を強化する準備が整いました。基本的なコマンドから始めて、必要に応じて調整し、よりスムーズなワークフローをお楽しみください。特定のセットアップについてヘルプが必要な場合はお知らせください！