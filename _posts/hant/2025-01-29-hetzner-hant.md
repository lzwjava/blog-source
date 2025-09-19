---
audio: false
generated: false
image: true
lang: hant
layout: post
title: Hetzner Cloud 雲端服務
translated: true
---

我最近很興奮地嘗試這個雲端平台。

{: .centered }
![](assets/images/hertzner/h.jpg)
*來源: Hetzner*{: .caption }

一台位於赫爾辛基的伺服器，配置為2個AMD VCPU、2GB RAM、40GB SSD和20TB的流量，每月僅需支付4.49 USD。

一個IPv4地址每月額外收取0.60 USD，總計每月為5.09 USD。

他們提供服務於六個地點：

- 德國讚賓
- 德國法克恩斯坦
- 芬蘭赫爾辛基
- 新加坡
- 美國奧勒冈州希爾斯博羅
- 美國弗吉尼亞州阿舒本

很有趣的是，他們沒有icism 選擇流行地點。他們的地點與 Vultr 或 Digital Ocean 不同。

防火牆設置非常易於使用。雖然這是我第一次使用，但我很快就能正確設定我的代理伺服器。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫爾辛基的 Hetzner 伺服器速度非常快。使用 Speedtest iOS 應用程式，下載速度為 423 Mbps，上傳速度為 56.1 Mbps。

在 Shadowrocket 中的 ping 為 1175 ms，但這並不是重大問題。

一個簡單的 Python 腳本來獲取伺服器實例詳細信息。

```python
from hcloud import Client
import os

# 從環境變量獲取 API 令牌
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY 環境變量未設置。")
    exit(1)

# 創建一個客戶端實例
client = Client(token=api_token)

# 列出所有伺服器
servers = client.servers.get_all()

# 打印伺服器詳細信息
for server in servers:
    print(f"伺服器 ID: {server.id}")
    print(f"伺服器名稱: {server.name}")
    print(f"伺服器狀態: {server.status}")
    print(f"伺服器 IPv4: {server.public_net.ipv4.ip}")
    print(f"伺服器 IPv6: {server.public_net.ipv6.ip}")
    print(f"伺服器類型: {server.server_type.name}")
    print(f"伺服器位置: {server.datacenter.location.name}")
    print("----------------------------------")

# 如果要獲取特定伺服器的詳細信息
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"特定伺服器 ID: {server.id}")
print(f"特定伺服器名稱: {server.name}")
print(f"特定伺服器狀態: {server.status}")
print(f"特定伺服器 IPv4: {server.public_net.ipv4.ip}")
print(f"特定伺服器 IPv6: {server.public_net.ipv6.ip}")
print(f"特定伺服器類型: {server.server_type.name}")
print(f"特定伺服器位置: {server.datacenter.location.name}")

```