---
audio: false
generated: true
lang: ja
layout: post
title: ヘッツネルクラウド
translated: true
---

最近、このクラウドプラットフォームに対して非常に興奮しています。

{: .centered }
![](assets/images/hertzner/h.jpg)
*Source: Hetzner*{: .caption }

ヘルシンキのサーバー、2つのAMD VCPU、2GB RAM、40GB SSD、20TBのトラフィックで4.49 USD/月という仕様は、IPv4アドレスを追加した5.09 USD/月となります。

彼らは以下の6か所でサービスを提供しています：

- ヌールベルク、ドイツ
- ファルケンシュタイン、ドイツ
- ヘルシンキ、フィンランド
- シンガポール、シンガポール
- ヒルズボロー、オレゴン州、アメリカ
- アシュバーン、バージニア州、アメリカ

テンデンシーに従わず人気のある場所を選ぶのではなく、VultrやDigital Oceanとは異なる場所を選んでいるのが面白いです。

ファイアウォールの設定は使いやすいです。初めて使うのにもかかわらず、プロキシサーバーの正しい設定をすぐに行うことができました。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

ヘルシンキのHetznerサーバーのスピードは非常に速いです。iOS用のSpeedtestアプリを使って、ダウンロード速度は423 Mbps、アップロード速度は56.1 Mbpsとなりました。

Shadowrocketのpingは1175 msですが、これは大きな問題ではありません。

サーバーインスタンスの詳細を取得するための簡単なPythonスクリプトです。

```python
from hcloud import Client
import os

# 環境変数からAPIトークンを取得
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# クライアントインスタンスを作成
client = Client(token=api_token)

# 全サーバーをリスト
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

# 特定のサーバーIDでサーバーを取得する場合
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