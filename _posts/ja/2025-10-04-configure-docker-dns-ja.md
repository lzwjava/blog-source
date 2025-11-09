---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: DockerデーモンDNSサーバーの設定
translated: true
type: note
---

Dockerデーモン（コンテナレベルで上書きされない限り、コンテナによって使用される）のDNSサーバーを設定するには、`/etc/docker/daemon.json`ファイルを編集します。このファイルを使用してDockerのランタイム動作をカスタマイズできます。

### DNS設定の手順

1. **daemon.jsonファイルを編集**:
   - ファイルが存在しない場合は、root権限で作成します（例: `sudo nano /etc/docker/daemon.json` またはお好みのエディタを使用）。
   - DNSサーバーのIPアドレスの配列として`dns`キーを追加または更新します。例えば、GoogleのパブリックDNS（8.8.8.8と8.8.4.4）を使用する場合:

     ```json
     {
       "dns": ["8.8.8.8", "8.8.4.4"]
     }
     ```

     - 必要に応じて、さらにサーバーを追加できます（例: Cloudflareの1.1.1.1）。
     - この設定は、特に指定がない限り、デフォルトネットワークで作成されるすべてのコンテナに適用されます。

2. **JSONを検証**:
   - ファイルが有効なJSONであることを確認します。`jq`などのツールを使用してチェックできます: `jq . /etc/docker/daemon.json`。エラーが発生した場合は、構文を修正してください。

3. **Dockerサービスを再起動**:
   - 変更を適用するためにDockerを再起動します:
     ```
     sudo systemctl restart docker
     ```
     - systemdを使用しないシステム（例: 古いLinuxディストリビューション）では、`sudo service docker restart`を使用します。
   - ステータスを確認: `sudo systemctl status docker`.

4. **設定をテスト**:
   - テストコンテナを実行し、そのDNS解決を確認します:
     ```
     docker run --rm busybox nslookup google.com
     ```
     - 設定したDNSサーバーを使用して解決されるはずです。

### 注意点
- **スコープ**: これはホスト上のDockerデーモンのDNSを設定し、コンテナの発信名前解決に影響します。ホストのシステムDNSは変更しません。
- **上書き**: コンテナが異なるDNSを必要とする場合（例: `docker run`の`--dns`フラグ経由）、このデーモンレベルの設定を上書きします。
- **セキュリティ**: 8.8.8.8のようなパブリックDNSの使用はほとんどの場合問題ありませんが、エンタープライズ環境では内部DNSを検討してください。
- **ドキュメント**: その他のオプション（例: DNS検索ドメイン）については、[公式Dockerドキュメントのdaemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)を参照してください。

エラーが発生した場合（例: 権限の問題やJSONの解析エラー）、詳細を共有していただければ、さらにトラブルシューティングを行います。