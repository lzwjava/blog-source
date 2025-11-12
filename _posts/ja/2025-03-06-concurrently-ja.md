---
audio: false
generated: true
lang: ja
layout: post
title: 同時実行
translated: true
type: note
---

「concurrently」についてフロントエンド開発の文脈でお尋ねのようですが、通常「concurrently」はNode.jsパッケージであり、複数のコマンドやスクリプトを同時に実行するために使用されます。これは主にバックエンドや開発ワークフローで使われるもので、フロントエンドコードで直接使用するものではありません。フロントエンドプロジェクトのセットアップ（例：スクリプトの実行）での使用方法についてお聞きでしたか？それともフロントエンドJavaScriptでの並行処理（例：Promise、async/await）についてでしたか？ここでは前者と仮定して説明しますが、必要に応じて詳細をお知らせください！

### フロントエンドプロジェクトでの `concurrently` の使用方法

React、Vue、Angularなどのフロントエンドプロジェクトでは、`concurrently` は開発サーバーとビルドウォッチャーなど、複数のプロセスを同時に起動する開発環境でよく使用されます。以下に使用方法を示します：

#### 1. `concurrently` のインストール
まず、プロジェクトに開発依存関係としてインストールします：
```bash
npm install --save-dev concurrently
```

#### 2. `package.json` にスクリプトを追加
`package.json` で同時に実行したいスクリプトを定義します。例えば、フロントエンド開発サーバーとSassのようなCSSプリプロセッサを実行する場合：
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // または使用しているフロントエンド開発コマンド
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: フロントエンド開発サーバーを実行（React、Viteなど）
- `watch:css`: CSSファイルの監視とコンパイル
- `dev`: `concurrently` を使用して両方のコマンドを同時に実行

#### 3. 並行スクリプトの実行
ターミナルで以下を実行：
```bash
npm run dev
```
これにより、フロントエンドサーバーとCSSウォッチャーの両方が同時に起動します。両方のプロセスの出力が同じターミナルに表示され、`concurrently` がそれらを同時に実行し続けます。

#### 4. オプション設定
`concurrently` は以下のオプションでカスタマイズ可能です：
- `--kill-others`: いずれかのプロセスが失敗した場合に全プロセスを停止
- `--names`: 各プロセスにラベルを付けて出力を明確化

`package.json` でのオプション使用例：
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
出力例：
```
[Frontend] フロントエンドサーバーを起動中...
[CSS] CSSファイルを監視中...
```

#### フロントエンドワークフローでの使用例
Reactアプリと別途APIサーバーを構築している場合：
- フロントエンド：`npm run start`（React開発サーバー、ポート3000）
- API：`npm run start:api`（例：Node.jsサーバー、ポート5000）
`concurrently` を使用して両方を実行：
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### フロントエンドでの並行JavaScript処理について
もしフロントエンドコードでの並行処理（例：複数APIの同時取得）についてお聞きでしたら、`Promise.all` を使用した簡単な例を示します：
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
これはAPI呼び出しを並行して実行し、両方の解決を待ちます。

### 必要に応じて詳細を！
「フロントエンドでのconcurrently」について、特定のライブラリ、フレームワーク、または使用ケースなど、別の意味でお聞きでしたら、回答をさらに調整しますのでお知らせください！