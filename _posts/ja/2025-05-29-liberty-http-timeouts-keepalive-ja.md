---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: Liberty HTTPタイムアウトとキープアライブの設定
translated: true
type: note
---

### Keep-Alive設定の構成

WebSphere Liberty Profileは、HTTP keep-alive接続を`server.xml`内の`<httpEndpoint>`要素を通じて処理します。この要素は、レイテンシとオーバーヘッドを削減するための永続的接続を制御します。

- **keepAlive**: keep-aliveを有効または無効にします。単一の接続で複数のリクエストを許可するには`true`（デフォルト）に設定します。
- **keepAliveTimeout**: サーバーがアイドル状態のkeep-alive接続を閉じるまでの待機時間（秒単位）を定義します。デフォルトは30秒です。

設定するには、`server.xml`の`<server>`ルートの下に`<httpEndpoint>`要素を追加または変更します。例:

```xml
<server>
    <!-- その他の設定 -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        keepAlive="true"
        keepAliveTimeout="60"/>
</server>
```

変更を有効にするにはサーバーを再起動します。TCPレベルのkeep-aliveは、必要に応じて`<tcpOptions>`で調整できますが、HTTP keep-aliveはWebトラフィックにより一般的です。

### タイムアウト設定の構成

Libertyの`server.xml`におけるタイムアウトは、主に`<httpEndpoint>`の下の接続タイムアウトに関連し、サーバーが操作を待機する時間を制御します。これらはHTTP通信に適用されます。

- **connectionTimeout**: 新しい接続を確立する最大時間（秒単位）。デフォルトは60秒です。
- **readTimeout**: リクエスト中の受信データを待機する最大時間（秒単位）。デフォルトは60秒です。
- **writeTimeout**: 送信データが送信されるのを待機する最大時間（秒単位）。デフォルトは60秒です。

セッション固有のタイムアウト（例: Webアプリセッション用）は、`web.xml`または`server.xml`の`<sessionManager>`で設定され、`<httpEndpoint>`では直接設定されません。

`server.xml`設定の例:

```xml
<server>
    <!-- その他の設定 -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        connectionTimeout="30"
        readTimeout="120"
        writeTimeout="120"/>
</server>
```

低速ネットワークや長時間実行されるリクエストに対して高いタイムアウト値を設定するなど、アプリケーションの要件に基づいて値を調整します。タイムアウト関連のエラーについてはログを監視し、変更後はサーバーを再起動します。詳細は、[IBM LibertyドキュメントのHTTPエンドポイント](https://www.ibm.com/docs/en/was-liberty/23.0.0?topic=configuration-http-endpoint-running-liberty)を参照してください。