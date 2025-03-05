---
audio: false
generated: true
lang: ja
layout: post
title: Chokidarを使用したファイル監視
translated: true
---

Chokidarは、サーバーサイドでのファイル監視を主に設計されたNode.jsライブラリであり、ブラウザ環境（フロントエンド）で直接使用するのが一般的な用途ではありません。ブラウザはNode.jsのようにファイルシステムへの直接アクセスができないため、Chokidarはバックエンドやビルド時の環境に適しています。しかし、Webpack、Vite、またはParcelなどのバンドラーを使用した開発セットアップでプロジェクトを作成している場合、またはNode.jsとフロントエンドを組み合わせたElectronアプリを構築している場合、間接的にChokidarを活用することができます。具体的な方法を説明します。

### Chokidarがブラウザで直接実行されない理由
- Chokidarは、ファイルを監視するためにNode.jsのAPIである`fs`（ファイルシステム）に依存しており、ブラウザ環境では利用できません。
- フロントエンドコードはセキュリティ上の理由でファイルシステムへのアクセスが制限されたサンドボックス環境（ブラウザ）で実行されます。

### フロントエンドコンテキストでのChokidarの使用可能なシナリオ
フロントエンド開発に関連する方法でChokidarを使用する方法を以下に示します。

#### 1. **ビルドツールを使用した開発中**
フロントエンド開発中にファイルを監視する（例えば、ホットリロードやライブ更新のため）場合、ビルドプロセスに組み込むのが一般的です。

カスタムNode.jsスクリプトの例:
```javascript
const chokidar = require('chokidar');

// フロントエンドソースファイルの変更を監視
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // ここで再ビルドをトリガーするか、フロントエンド開発サーバーに通知します
});
```
- **用途**: 開発中にWebSocket接続を使用してブラウザに更新をプッシュすることができます。
- **ツール**: `esbuild`や開発サーバー（例えば、Viteにはファイル監視が組み込まれているが、Chokidarでカスタマイズすることもできます）と組み合わせることができます。

#### 2. **Electronアプリ**
「フロントエンド」がElectronアプリケーションの一部である場合、メインプロセス（Node.js）でChokidarを使用し、変更をレンダラープロセス（フロントエンド）に通信することができます。

例:
```javascript
// main.js (Electronメインプロセス)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // レンダラープロセスにイベントを送信
});
```
```javascript
// renderer.js (フロントエンド)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`ファイルが変更されました: ${path}`);
  // UIを適切に更新
});
```

#### 3. **フロントエンドとバックエンドプロキシ**
Webアプリを構築し、ファイル監視機能を実現したい場合、Node.jsバックエンドでChokidarを実行し、WebSocketやサーバーサイドイベントを通じてフロントエンドに更新を送信します。

例（ExpressとWebSocketを使用したバックエンド）：
```javascript
const express = require('express');
const WebSocket = require('ws');
const chokidar = require('chokidar');

const app = express();
const server = app.listen(3000);
const wss = new WebSocket.Server({ server });

chokidar.watch('./public').on('change', (path) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`ファイルが変更されました: ${path}`);
    }
  });
});
```
フロントエンド（Reactの例）：
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "ファイルが変更されました: ..."
  // ステートやUIを更新
};
```

### インストール
これらのセットアップのいずれかでChokidarを使用するには、まずNode.jsプロジェクトにインストールします：
```bash
npm install chokidar
```

### 主要なChokidarメソッド
- `chokidar.watch(path, [options])`: ファイルまたはディレクトリの監視を開始します。
- イベント: `.on('add', callback)`, `.on('change', callback)`, `.on('unlink', callback)`, `.on('all', (event, path) => {})`.
- オプション: `{ ignored: /node_modules/, persistent: true }`（必要に応じてカスタマイズ）。

### もし他のことを指していた場合
Node.js環境を全く使用せず、ブラウザ内でファイル監視のような動作を実現したい場合（例えば、`<input type="file">`の変更を監視する場合）、お知らせください！それは`File` APIとイベントリスナーを使用するもので、Chokidarではありません。

具体的なセットアップや目標は何ですか？さらに詳細に調整できます！