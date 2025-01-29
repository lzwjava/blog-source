---
audio: true
lang: hant
layout: post
title: 海特茲納雲
translated: true
---

我最近非常期待試用這個雲端平台。

{: .centered }
![](assets/images/hertzner/h.jpg)
*來源: Hetzner*{: .caption }

一台位於赫爾辛基的伺服器配置為2個AMD VCPU、2GB RAM、40GB SSD 以及20TB流量，每月僅需 $4.49 USD。

多一個IPv4地址，每月需額外支付 $0.60 USD，總共每月 $5.09 USD。

他們提供服務的區域有六個：

- 奧地利奧爾堡
- 奧地利福克斯坦
- 芬蘭赫爾辛基
- 新加坡
- 美國奧堡
- 美國亞什頓

很有趣的是，他們並沒有跟隨流行趨勢選擇流行的區域。他們的區域與Vultr或Digital Ocean的不同。

防火牆設置非常易於使用。雖然這是我第一次使用，但很快就能正確設置我的代理伺服器的配置。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫爾辛基的Hetzner伺服器速度非常快。使用Speedtest iOS應用，下載速度為423 Mbps，上載速度為56.1 Mbps。

在Shadowrocket中，延遲為1175 ms，但這並不是重大問題。

一個簡單的Python腳本來獲取伺服器實例的詳細資訊。

```python
from hcloud import Client
import os

# 從環境變數獲取API令牌
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("錯誤: HERTZNER_API_KEY環境變數未設置。")
    exit(1)

# 創建客戶端實例
client = Client(token=api_token)

# 列出所有伺服器
servers = client.servers.get_all()

# 打印伺服器詳細資訊
for server in servers:
    print(f"伺服器ID: {server.id}")
    print(f"伺服器名稱: {server.name}")
    print(f"伺服器狀態: {server.status}")
    print(f"伺服器IPv4: {server.public_net.ipv4.ip}")
    print(f"伺服器IPv6: {server.public_net.ipv6.ip}")
    print(f"伺服器類型: {server.server_type.name}")
    print(f"伺服器位置: {server.datacenter.location.name}")
    print("----------------------------------")

# 如果要獲取特定伺服器的詳細資訊
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"特定伺服器ID: {server.id}")
print(f"特定伺服器名稱: {server.name}")
print(f"特定伺服器狀態: {server.status}")
print(f"特定伺服器IPv4: {server.public_net.ipv4.ip}")
print(f"特定伺服器IPv6: {server.public_net.ipv6.ip}")
print(f"特定伺服器類型: {server.server_type.name}")
print(f"特定伺服器位置: {server.datacenter.location.name}")

```