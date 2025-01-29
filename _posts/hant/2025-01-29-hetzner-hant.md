---
audio: true
lang: hant
layout: post
title: 海特諾雲端
translated: true
---

我最近非常期待试用這個雲端平台。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*來源: Hetzner*{: .caption }

一台位於赫爾辛基的伺服器，配置為2個AMD VCPU、2GB RAM、40GB SSD，並有20TB的流量，每月僅需支付$4.49 USD。

一個IPv4地址每月額外支付$0.60 USD，總計每月$5.09 USD。

他們提供六個位置的服務：

- 德國維倫堡
- 德國福克斯坦
- 芬蘭赫爾辛基
- 新加坡
- 美國奧勒岡州希爾斯堡
- 美國弗吉尼亞州阿什本

有趣的是，他們並不遵循流行趨勢選擇流行地點。他們的位置與Vultr或Digital Ocean不同。

防火牆設置非常容易使用。雖然這是我第一次使用它，但我很快就設置了正確的配置以供我的代理伺服器使用。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

赫爾辛基的Hetzner伺服器速度非常快。使用Speedtest iOS應用程式，下載速度為423 Mbps，上傳速度為56.1 Mbps。

Shadowrocket中的Ping為1175 ms，但這並不是重大問題。