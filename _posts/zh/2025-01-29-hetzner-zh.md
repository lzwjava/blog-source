---
audio: true
lang: zh
layout: post
title: Hetzner 云
translated: true
---

我最近非常兴奋地尝试了这个云平台。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*来源: Hetzner*{: .caption }

在赫尔辛基的一个服务器配置为2个AMD VCPU，2GB RAM，40GB SSD，并且带宽20TB，每月仅需$4.49 USD。

一个IPv4地址每月额外收费$0.60 USD，总共每月$5.09 USD。

他们提供服务在以下六个地点：

- 德国纽伦堡
- 德国法克堡
- 芬兰赫尔辛基
- 新加坡
- 美国俄勒冈州希尔斯堡
- 美国弗吉尼亚州阿什本

他们不跟随热门地点的趋势选择服务区域，与Vultr或Digital Ocean不同。

防火墙设置非常容易使用。虽然这是我第一次使用它，但我很快为我的代理服务器正确配置了设置。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫尔辛基的Hetzner服务器速度非常快。使用Speedtest iOS应用，下载速度为423 Mbps，上传速度为56.1 Mbps。

在Shadowrocket中，ping为1175 ms，但这不是一个重大问题。