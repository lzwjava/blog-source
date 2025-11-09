---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: LibreChatのローカルホストアクセスのトラブルシューティング
translated: true
type: note
---

### localhost:3080 で LibreChat にアクセスできない場合のトラブルシューティング

ログによると、Docker イメージは（最初のタイムアウトとリトライの後）正常にプルされ、6つのコンポーネント（デフォルトネットワーク、`vectordb`、`chat-mongodb`、`chat-meilisearch`、`rag_api`、`LibreChat`）が起動しました。しかし、`api` サービス（通常はポート 3080 でバックエンドを提供する）が起動したコンテナのリストに表示されていません。これがサイトにアクセスできない理由である可能性が高いです。`LibreChat` コンテナはおそらくフロントエンドであり、`api` バックエンドに依存しています。

UID/GID の警告は、`api` コンテナが正常に起動するのを妨げる可能性のある権限の問題を示唆しています。以下に、この問題を診断して修正するためのステップバイステップガイドを示します。

#### 1. **実行中のコンテナとポートの確認**
   アクティブなコンテナ、そのステータス、ポートマッピングを確認するには、以下を実行します:
   ```
   docker ps
   ```
   - `api` コンテナ（`librechat_api` などという名前かもしれません）を探してください。もし見つからないか終了している場合は、それが問題です。
   - ポート `3080` がマッピングされているか（例: `0.0.0.0:3080->3080/tcp`）確認してください。マッピングされていない場合、サービスはポートを公開していません。
   - どのコンテナもポート 3080 を表示しない場合は、次のステップに進んでください。

#### 2. **コンテナログの確認**
   `api` および `LibreChat` サービスの起動時のエラー、特にエラーを調査します:
   ```
   docker logs LibreChat
   docker logs api  # または名前が異なる場合は docker logs librechat_api
   docker logs rag_api  # 依存関係の問題の場合
   ```
   - 一般的なエラー: 権限がありません（UID/GID が原因）、MongoDB/Meilisearch 接続失敗、またはバインドの問題（例: コンテナ内の localhost のみでリッスンしている）。
   - ログにサーバーが起動しているがコンテナ内の localhost にのみバインドしていると表示される場合は、`.env` ファイルに `HOST=0.0.0.0` を追加してください。

#### 3. **権限警告を修正するための UID と GID の設定**
   あなたの `.env` ファイル（`.env.example` からコピーされたもの）では、これらの変数がコメントアウトされている可能性が高いです。設定されていない変数は、ファイル権限の不一致によりコンテナがサイレントに失敗する原因となります。
   - `.env` を編集:
     ```
     UID=1000  # ユーザー ID を取得するには `id -u` を実行
     GID=1000  # グループ ID を取得するには `id -g` を実行
     ```
   - 保存してから再起動:
     ```
     docker compose down
     docker compose up -d
     ```
   これにより、（設定/ログなどの）ボリュームがあなたのユーザーによって所有されていることが保証されます。

#### 4. **接続のテスト**
   - ポート 3080 がローカルでリッスンしているか確認:
     ```
     curl -v http://localhost:3080
     ```
     - タイムアウトまたは接続拒否された場合、サービスは実行/公開されていません。
   - `docker ps` がポートマッピングを表示するが curl が失敗する場合は、ファイアウォール（例: `sudo ufw status`）を確認するか、`http://127.0.0.1:3080` を試してください。

#### 5. **必要に応じて追加の修正**
   - **イメージプルの問題**: 最初の試行で `ghcr.io/v2/librechat/librechat/manifests/latest` に対して「拒否されました」エラーが発生しました。再度プルが失敗する場合は、GitHub Container Registry で認証を行ってください:
     ```
     echo $YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
     ```
     （`read:packages` スコープを持つ Personal Access Token を github.com/settings/tokens で作成してください。）
   - **推奨される Compose ファイルを使用**: デフォルトの `docker-compose.yml` はローカルビルド用であり、不安定な場合があります。安定したリモートイメージには `deploy-compose.yml` に切り替えてください:
     - 現在の `docker-compose.yml` をリネームまたはバックアップします。
     - 代わりに `deploy-compose.yml` を使用: `docker compose -f deploy-compose.yml up -d`。
     - `.env` に `HOST=0.0.0.0` と `NODE_ENV=production` が設定されていることを確認してください。
   - **Prune を使用した完全な再起動**: 行き詰まった場合は、クリーンアップします:
     ```
     docker compose down -v  # ボリュームも削除
     docker system prune -f
     docker compose up -d
     ```
   - **依存関係**: MongoDB と Meilisearch が正常であることを確認します（`docker logs chat-mongodb` など）。`api` はこれらに依存しています。

これらの手順を実行した後、http://localhost:3080 へのアクセスを再試行してください。ログに特定のエラー（例: Mongo 接続）が表示される場合は、より具体的なヘルプのためにそれらを共有してください。UID/GID と依存関係が整えば、このセットアップはほとんどのユーザーで動作します。

[Local Docker Build Fails to Serve on localhost:3080](https://github.com/danny-avila/LibreChat/discussions/3425)  
[LibreChat Docker Docs](https://www.librechat.ai/docs/local/docker)  
[Env File Configuration (UID/GID)](https://www.librechat.ai/docs/configuration/dotenv)