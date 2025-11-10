---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Node.js OpenSSL レガシープロバイダーフラグ
translated: true
type: note
---

### 問題の理解
Node.js 16（およびそれ以前のバージョン）は OpenSSL 1.x を使用していますが、Node.js 22 ではより厳格なセキュリティデフォルトを持つ OpenSSL 3.x が導入されています。これにより、特にレガシーな暗号プロバイダや非推奨アルゴリズム（例：MD4ハッシュ）に依存するアプリケーションでエラーが発生する可能性があります。`--openssl-legacy-provider` フラグは、アップグレード期間中のこれらの問題を修正するために、OpenSSL 1.x の動作との互換性を一時的に有効にします。

**注意**: このフラグは回避策であり、将来の Node.js バージョンでは削除される可能性があります。可能な場合は、現代的な OpenSSL 3.x API を使用するようにコードを更新することが最善策です。

### フラグの使用方法
このフラグは、Node.js を直接実行する場合や npm/yarn スクリプト経由で適用できます。これは永続的な設定ではなく、ランタイムオプションです。

#### 直接 Node コマンドを実行する場合
スクリプトやコマンドの前にフラグを追加します。例:
- 基本的なスクリプト実行: `node --openssl-legacy-provider app.js`
- REPL（対話モード）: `node --openssl-legacy-provider`
- モジュールを実行する場合: `node --openssl-legacy-provider --input-type=module index.mjs`
- 追加フラグと共に使用: `node --openssl-legacy-provider --max-old-space-size=4096 script.js`

これにより、レガシープロバイダのサポートが有効になり、「digital envelope routines unsupported」（古いハッシュや暗号に関連する）などの一般的なエラーを回避できます。

#### npm/Yarn スクリプトの場合
`package.json` の `"scripts"` セクションで、関連するコマンドにフラグを含めるように修正します。例:
```json
{
  "scripts": {
    "start": "node --openssl-legacy-provider app.js",
    "dev": "node --openssl-legacy-provider --watch app.js"
  }
}
```
その後、通常通り実行します: `npm start` または `yarn dev`。

nodemon や vite のように Node プロセスを生成するツールを使用する場合は、その設定でフラグを先頭に追加します（例: nodemon.json で `"exec": "node --openssl-legacy-provider"`）。

#### グローバルコマンドの場合（nvm やシステムの Node 経由など）
nvm で Node バージョンを管理している場合は、Node 22 に切り替え、前述のようにフラグを付けてコマンドを実行します。Docker や CI/CD の場合は、実行スクリプトに追加します（例: `CMD ["node", "--openssl-legacy-provider", "app.js"]`）。

### トラブルシューティングと代替案
- **フラグが機能するか確認**: `node --openssl-legacy-provider --version` を実行します。エラーなく Node 22 のバージョンが出力されるはずです。
- **修正される一般的な問題**: crypto モジュールの `require()`、webpack ビルド、またはアプリ起動時のエラー。それでも問題が解決しない場合は、OpenSSL 固有のコード（例: `crypto.createCipher` の代わりに `crypto.createCipheriv` を使用するなど）を確認してください。
- **長期的な解決策**: 非推奨の crypto 使用法をスキャンし（ESLint プラグインなどのツールを使用）、OpenSSL 3.x 互換のメソッドに更新します。Node 22 のドキュメントでは、ハッシュ化に `bcrypt` や `crypto.scrypt` などのライブラリを使用することが推奨されています。
- **パフォーマンス/互換性に関する注意**: レガシープロバイダモードは、セキュリティ/機能にわずかな影響を与える可能性がありますが、移行期間中に役立ちます。OpenSSL 3 の一部機能（例：強化されたエントロピーソース）は利用できないため、十分にテストしてください。

詳細については、Node.js OpenSSL ドキュメント（nodejs.org/api/crypto.html）を参照してください。具体的なエラーメッセージを共有していただければ、より的を絞ったアドバイスを提供できます！