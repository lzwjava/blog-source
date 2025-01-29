---
audio: true
lang: ja
layout: post
title: Hetznerクラウド
translated: true
---

最近このクラウドプラットフォームを試してみるのを楽しみにしています。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*Source: Hetzner*{: .caption }

ヘルシンキのサーバーで、2 AMD VCPUs、2GB RAM、40GB SSD、20TB のトラフィックを持つ設定は、 $4.49 USD 毎月です。

IPv4 アドレスは追加で $0.60 USD 毎月かかり、合計で $5.09 USD 毎月になります。

彼らは6つの場所でサービスを提供しています：

- ヌールベルク、ドイツ
- ファルケンシュタイン、ドイツ
- ヘルシンキ、フィンランド
- シンガポール、シンガポール
- オレゴン州のヒルズボロ、アメリカ
- バージニア州のアシュバーン、アメリカ

人気の場所を選ぶというトレンドに従わないことが興味深いです。Vultr や DigitalOcean とは異なる場所を選んでいます。

ファイアウォールの設定は非常に使いやすいです。最初に使用するのですが、プロキシサーバーの正しい設定をすぐに行うことができました。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

ヘルシンキのヘッツナーサーバーの速度は非常に速いです。Speedtest iOS アプリを使用して、ダウンロード速度は 423 Mbps、アップロード速度は 56.1 Mbps です。

Shadowrocket のピングは 1175 ms ですが、これは大きな問題ではありません。

サーバーインスタンスの詳細を取得するためのシンプルな Python スクリプトです。

```python
from hcloud import Client
import os

# 環境変数から API トークンを取得
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# クライアントインスタンスを作成
client = Client(token=api_token)

# すべてのサーバーをリスト
servers = client.servers.get_all()

# サーバーの詳細を表示
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")

# 特定のサーバーを ID で取得
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"Specific Server ID: {server.id}")
print(f"Specific Server Name: {server.name}")
print(f"Specific Server Status: {server.status}")
print(f"Specific Server IPv4: {server.public_net.ipv4.ip}")
print(f"Specific Server IPv6: {server.public_net.ipv6.ip}")
print(f"Specific Server Type: {server.server_type.name}")
print(f"Specific Server Location: {server.datacenter.location.name}")
```