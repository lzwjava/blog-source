---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Dockerデーモンプロキシループの回避
translated: true
type: note
---

### Dockerの`daemon.json`で`"no-proxy": "localhost,127.0.0.1,.local"`が重要な理由

Dockerデーモンを`"http-proxy": "http://localhost:7890"`（Clashなどのローカルツールで一般的）のようなプロキシ設定で構成すると、デーモンはデフォルトで**すべての**外向きネットワークトラフィックにこれらのルールを適用します。これには外部レジストリ（例：`hello-world`のようなイメージをプルするための`registry-1.docker.io`）への接続も含まれます。

しかし、`no-proxy`ディレクティブがない場合、Dockerデーモンは**ローカル接続**—例えばプロキシサーバー自体への`localhost:7890`への初期TCPハンドシェイク—も同じプロキシ経由でルーティングしようとします。これにより古典的な**プロキシループ**が発生します：

1. Dockerは`registry-1.docker.io`からイメージを取得する必要があります
2. `localhost:7890`のプロキシ経由で接続を試みます
3. しかし`localhost:7890`に到達するために、プロキシ設定が再度適用され、Dockerは…`localhost:7890`のプロキシ経由で接続を強制されます
4. この無限再帰はTCPレベルで失敗します。プロキシは自身への接続をプロキシできないためです（解決策のない自己参照ループにつながります）
5. 接続は予期せず中止され、`proxyconnect tcp: EOF`エラーが発生します（EOFは「end of file」を意味し、プロキシネゴシエーション/ハンドシェイク中の早期閉鎖を示します）

`"no-proxy": "localhost,127.0.0.1,.local"`を追加することで、デーモンに対して以下の宛先へのトラフィックは**プロキシをバイパス**するように明示的に指示します：
- `localhost`（自マシンのループバックホスト名）
- `127.0.0.1`（IPv4ループバックアドレス）
- `.local`ドメイン（mDNS/ローカルネットワーク解決で一般的）

これにより、Dockerは自身をループさせることなく、localhost上のプロキシサーバーに**直接**接続できるようになります。一度接続されれば、プロキシはDockerレジストリへの外部リクエストを適切に処理できます（例：HTTPSトラフィックの場合はHTTP CONNECT経由）。

要約：これはデーモンが「プロキシをプロキシする」ことを防ぎ、ローカルプロキシアクセスを機能させながら、インターネット向けトラフィック（イメージプルなど）をプロキシ経由でルーティングすることを保証します。

他のローカルサービス（内部レジストリやローカルで通信するコンテナなど）を含む設定の場合、`no-proxy`にそれらのドメイン/IPを追加することで、同様の問題を防ぐことができます。

[Docker Daemon Proxy Configuration](https://docs.docker.com/engine/daemon/proxy/)  
[Docker Proxy Settings Forum Discussion](https://forums.docker.com/t/proxy-settings-for-the-docker-daemon/132089)  
[Docker Proxy Guide for Corporate Firewalls](https://www.datacamp.com/tutorial/docker-proxy)