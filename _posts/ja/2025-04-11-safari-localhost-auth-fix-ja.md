---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Safari ローカルホスト認証修正
translated: true
type: note
---

この問題は、macOS上のSafariがlocalhost URLに対してChromeよりも厳格なセキュリティポリシーを適用するために発生します。具体的には、Safariは永続的なCookieと認証セッションを許可するために安全なHTTPSコンテキストを要求し、HTTP上で動作するLibreChatのようなアプリケーションにおいて、潜在的なログアウトループや訪問毎の再認証を防止します。Chromeはlocalhost上のHTTPに対してより寛容であるため、認証が持続しますが、Safariでは持続しません。[1][2][3]

### 要因
- **ブラウザのポリシー**: Safariなどのモダンブラウザは、混合コンテンツの警告やセッションの不安定性を避けるために、localhostに対してHTTPSを要求します。
- **LibreChatの動作**: LibreChatは安全なCookieまたはlocalStorageベースのトークンを認証に使用しますが、Safariの非セキュアなoriginに対する厳格な処理により、HTTP上ではこれらが機能しません。

### 解決策 (容易さと効果でランク付け)
1. **localhostにHTTPSを設定する (推奨)**:
   - LibreChat自身のドキュメントとブログは、HTTPによるログアウトを防ぐためにこれを推奨しています。[1]
   - `mkcert` (無料ツール) を使用してlocalhost用のSSL証明書を生成し、信頼する:
     - `brew install mkcert` またはGitHubからダウンロードして `mkcert` をインストール。
     - ルートCAをインストールするために `mkcert -install` を実行。
     - 証明書を作成: `mkcert localhost 127.0.0.1`。
     - LibreChatを設定 (Docker環境変数や設定経由で): `.env` ファイルまたは環境に `HTTPS=true`, `SSL_CRT_FILE=/path/to/localhost.pem`, `SSL_KEY_FILE=/path/to/localhost-key.pem` を追加。
     - LibreChatを再起動し、`https://localhost:3080` でアクセス。
     - Safariはこれを安全として扱い、シームレスなログインを許可します。

2. **代替案: localhostの代わりに127.0.0.1を使用する**:
   - Safariは `localhost` に対して異なる動作をすることがあります (IPv6またはDNS解決による)。 `http://127.0.0.1:3080` にアクセスしてみてください – これにより同様の接続問題が解決する場合がありますが、認証の永続性を完全に修正しない可能性があります。[4][4][5]

3. **localhostのSafariウェブサイトデータをクリアする**:
   - Safari > 環境設定 > プライバシー > ウェブサイトデータを管理 > "localhost"を検索 > エントリを削除。
   - これにより、SafariがHTTPSへのアップグレードを強制したり、キャッシュされた非セキュアなコンテキストを適用するのを停止させます。[3][2]
   - Safariを再起動してテスト。LibreChatがサポートしていれば、認証は保持されるはずです。

これらが機能しない場合、LibreChatのログで認証エラーを確認し、`.env` に競合するフラグがないか確認してください (例: `ALLOW_ANONYMOUS=true` は、必要に応じて認証を完全に無効にします)。また、Safariのプライベートブラウジングモードを使用していないことを確認してください。このモードは永続的なストレージをブロックします。[6][7] 問題が解決しない場合は、LibreChatのバージョンと.env設定を提供して、より詳細なトラブルシューティングを行ってください。

引用:
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354