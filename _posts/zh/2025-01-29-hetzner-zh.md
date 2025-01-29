---
audio: true
lang: zh
layout: post
title: Hetzner 云
translated: true
---

我最近非常兴奋地试用这个云平台。

{: .centered }
![](assets/images/hertzner/h.jpg)
*来源: Hetzner*{: .caption }

一个位于赫尔辛基的服务器，配置为2个AMD VCPU、2GB内存、40GB SSD，以及20TB流量每月仅需4.49美元。

额外的IPv4地址每月仅需0.60美元，总共每月5.09美元。

他们提供服务于以下六个地点：

- 内荷尔赫姆, 德国
- 福克斯坦, 德国
- 赫尔辛基, 芬兰
- 新加坡, 新加坡
- 俄勒冈州希尔斯堡, 美国
- 维吉尼亚州阿什本, 美国

有趣的是，他们没有按趋势选择热门地点。他们的服务器位置与Vultr或DigitalOcean不同。

防火墙设置非常容易使用。虽然这是我第一次使用它，但我很快就为我的代理服务器设置了正确的配置。

```shell
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
```

赫尔辛基Hetzner服务器的速度非常快。使用Speedtest iOS应用程序，下载速度为423 Mbps，上传速度为56.1 Mbps。

在Shadowrocket中，Ping为1175 ms，但这不是一个重大问题。

一个简单的Python脚本用于获取服务器实例详细信息。

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
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")

# 如果要获取特定服务器的详细信息
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