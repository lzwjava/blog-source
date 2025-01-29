---
audio: true
lang: hant
layout: post
title: Hetzner 雲端
translated: true
---

我最近很期待試用這個雲端平台。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*來源: 赫茨因*{: .caption }

赫茨因的赫爾辛基伺服器配置為2個AMD VCPU，2GB RAM，40GB SSD，並且流量為20TB，每月僅需$4.49 USD。

一個IPv4位址每月額外收費$0.60 USD，總共每月$5.09 USD。

他們提供以下六個位置的服務：

- 德國奧黛律
- 德國法肯斯坦
- 芬蘭赫爾辛基
- 新加坡
- 美國奧堡
- 美國亞士本

興趣的是，他們並沒有遵循流行趨勢選擇流行地點。他們的位置與Vultr或DigitalOcean相比非常不同。

防火牆設置很易於使用。雖然這是我第一次使用它，但我很快就能設定正確的代理伺服器配置。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫茨因的赫爾辛基伺服器速度非常快。使用iOS的Speedtest應用程式，下載速度為423 Mbps，上傳速度為56.1 Mbps。

在Shadowrocket中的ping為1175 ms，但這並不是重大問題。

一個簡單的Python腳本來獲取伺服器實例詳細資訊。

```python
from hcloud import Client
import os

# 從環境變數獲取API密鑰
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# 創建客戶端實例
client = Client(token=api_token)

# 列出所有伺服器
servers = client.servers.get_all()

# 打印伺服器詳細資訊
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")

# 如果您需要獲取特定伺服器的詳細資訊
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