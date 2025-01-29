---
audio: true
lang: zh
layout: post
title: Hetzner 云
translated: true
---

我最近非常兴奋能试用这个云平台。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*来源: Hetzner*{: .caption }

位于赫尔辛基的服务器配置为2个AMD VCPU，2GB RAM，40GB SSD，以及20TB流量，每月成本为$4.49 USD。

每月额外获得一个IPv4地址需支付$0.60 USD，总共每月$5.09 USD。

他们在六个地点提供服务：

- 德国奴伦堡
- 德国法尔肯斯坦
- 芬兰赫尔辛基
- 新加坡
- 美国俄勒冈州希尔斯堡
- 美国弗吉尼亚州阿什本

有趣的是，他们并没有跟随流行趋势选择热门地点。他们的地点与Vultr或Digital Ocean不同。

防火墙设置非常简单。虽然这是我第一次使用，但我很快就能为我的代理服务器设置正确的配置。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫尔辛基的Hetzner服务器速度非常快。使用Speedtest iOS应用，下载速度为423 Mbps，上传速度为56.1 Mbps。

在Shadowrocket中，Ping为1175 ms，但这不是一个重大问题。

一个简单的Python脚本来获取服务器实例详细信息。

```python
from hcloud import Client
import os

# 从环境变量获取API令牌
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# 创建客户端实例
client = Client(token=api_token)

# 列出所有服务器
servers = client.servers.get_all()

# 打印服务器详细信息
for server in servers:
    print(f"服务器ID: {server.id}")
    print(f"服务器名称: {server.name}")
    print(f"服务器状态: {server.status}")
    print(f"服务器IPv4: {server.public_net.ipv4.ip}")
    print(f"服务器IPv6: {server.public_net.ipv6.ip}")
    print(f"服务器类型: {server.server_type.name}")
    print(f"服务器位置: {server.datacenter.location.name}")
    print("----------------------------------")

# 获取特定服务器的详细信息
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"特定服务器ID: {server.id}")
print(f"特定服务器名称: {server.name}")
print(f"特定服务器状态: {server.status}")
print(f"特定服务器IPv4: {server.public_net.ipv4.ip}")
print(f"特定服务器IPv6: {server.public_net.ipv6.ip}")
print(f"特定服务器类型: {server.server_type.name}")
print(f"特定服务器位置: {server.datacenter.location.name}")
```