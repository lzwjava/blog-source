---
audio: true
lang: ja
layout: post
title: Hetznerクラウド
translated: true
---

このクラウドプラットフォームについては最近試したいととても興奮です。

{: .centered }
![](assets/images/hertzner/h.jpg)
*Source: Hetzner*{: .caption }

ヘルシンキにあるサーバーの構成は2つのAMD VCPU、2GBのRAM、40GBのSSD、そして20TBのトラフィックで、月額 $4.49 USD です。

IPv4アドレスは追加で月額 $0.60 USD かかり、合計は月額 $5.09 USD になります。

彼らは以下の6つの場所でサービスを提供しています：

- ヌールンベルク、ドイツ
- ファルケンシュタイン、ドイツ
- ヘルシンキ、フィンランド
- シンガポール、シンガポール
- オレゴン州ヒルズボロー、アメリカ
- バージニア州アシュバーン、アメリカ

彼らが人気のある場所に合わせるトレンドに従わない点が興味深いです。VultrやDigital Oceanとは異なる場所を選んでいます。

ファイアウォール設定は使いやすいです。初めて使ったのに、プロキシサーバーの正しい構成を迅速に設定できました。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

ヘルシンキのHetznerサーバーの速度は非常に速いです。iOSのSpeedtestアプリを使って、ダウンロード速度は423 Mbps、アップロード速度は56.1 Mbpsです。

ShadowrocketのPingは1175 msですが、問題ありません。

サーバーインスタンスの詳細を取得するためのシンプルなPythonスクリプトです。

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

# 特定のサーバーIDでサーバーを取得
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