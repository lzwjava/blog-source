---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: JWTシークレットエラーの修正
translated: true
type: note
---

### LibreChatでのJWTシークレットエラーの修正

ログによると、APIは起動しているものの、JWTシークレットの欠如によりクラッシュしています: `JwtStrategy requires a secret or key`。これはLibreChatでよくある設定の問題です。バックエンドは認証にJWT（JSON Web Tokens）を使用しており、シークレットキーがないとこの戦略を初期化できません。RAG API、パーミッション、その他のサービスは正常ですが、これがメインAPIの完全な起動を妨げ、http://localhost:3080 へのアクセスを阻止しています。

#### クイックフィックス: JWT_SECRETの設定
1. **安全なシークレットを生成**:
   - 以下のコマンドを実行して、ランダムな32文字以上の文字列を生成します（これをJWT_SECRETとして使用します）:
     ```
     openssl rand -base64 32
     ```
     出力例: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6`

2. **`.env`ファイルを更新**:
   - `.env`（LibreChatプロジェクトのルートディレクトリ内）を開きます。
   - 以下の行を追加するか、コメントアウトを解除します（生成したシークレットに置き換えてください）:
     ```
     JWT_SECRET=your_generated_secret_here
     ```
   - すでに存在しているが空欄またはコメントアウトされている場合は、入力してください。
   - ファイルを保存します。

3. **サービスを再起動**:
   ```
   docker compose down
   docker compose up -d
   ```
   - ログを確認: `docker logs -f api`（または名前が異なる場合は `docker logs -f librechat_api`）。
   - JWTエラーなしで正常に起動したことを確認してください。"Server running on port 3080"のようなログが表示されるはずです。

#### 動作確認
- 再起動後、実行中のコンテナを確認:
  ```
  docker ps
  ```
  - `api`コンテナのステータスが "Up" で、ポート3080が公開されているはずです。
- アクセスをテスト: ブラウザで http://localhost:3080 を開きます。LibreChatのログイン/セットアップページが表示されるはずです。
- まだ問題がある場合は、新しいエラーのログを確認: `docker logs api`。

#### ログからのその他の注意点
- **古い設定**: 現在v1.2.1を使用中ですが、v1.3.0が利用可能です。JWTを修正した後、[変更履歴](https://www.librechat.ai/changelog)を確認して新機能（例: 改良された認証オプション）を確認してください。最新のイメージをプルして更新: `docker compose pull`。
- **Turnstile無効**: ローカル開発では問題ありません。本番環境用のCAPTCHAとして後で有効にしてください。
- **UID/GID警告**: これらが引き続き表示される場合は、前述の通りに設定して将来のパーミッションの問題を回避してください。

これで動作するはずです。JWT_SECRETは認証エンドポイントに必要です。修正後にログに別のエラーが表示される場合は、ここに貼り付けてください。

[LibreChat環境変数](https://www.librechat.ai/docs/configuration/dotenv#jwt_secret)  
[一般的なDockerの問題](https://github.com/danny-avila/LibreChat/issues?q=is%3Aissue+is%3Aopen+label%3Adocker)