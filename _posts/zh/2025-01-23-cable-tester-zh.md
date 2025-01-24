---
audio: true
lang: zh
layout: post
title: 网线测试仪与网状路由器
translated: true
---

## 网线测试仪

最近我在京东购买了一款网线测试仪。之前，我见过网络顾问到我家里或雇主的办公室来测试网络。

这个设备非常便宜，仅需约10元人民币。在沃尔玛，类似的产品大约要10美元。

本文中，我使用了来自Amazon.com的图片。

{: .centered }
![](assets/images/cable-tester/c.jpg){: .responsive }
*来源：Amazon.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/c2.jpg){: .responsive }
*来源：自摄*{: .caption }

{: .centered }
![](assets/images/cable-tester/c3.jpg){: .responsive }
*来源：自摄*{: .caption }

## 网状路由器

2023年，我开始使用网状路由器。我购买了一套TP-Link AX3000系统，包含两个网状路由器——一个主单元和一个卫星单元。当时花费了约484元人民币，现在京东上仅售395元。

最初，我在大房子里使用这套系统，后来搬到了父母家。

2025年春节期间，有几天家人住在大房子里，再次遭遇WiFi网络质量不佳的问题。为了解决这个问题，我又购买了一台网状路由器——中兴AC1200，价格约为108元人民币。

沃尔玛上类似的产品包括TP-Link WiFi网状路由器、Eero双频网状路由器和NetGear Nighthawk AX3000。这些产品的价格大多在50美元到200美元之间。

对于中兴AC1200网状路由器，我只需购买一台并启用桥接模式，让它接收WiFi信号后再发射自己的WiFi信号，效果非常好。原本路由器的域名地址是192.168.5.1。启用桥接模式后，这个IP地址就无法访问了。相反，192.168.1.1会重定向到家庭网络中的主路由器。此时，你可以通过访问http://zte.home进入路由器的控制中心。

如果你能访问主路由器，就能看到连接的设备及其IP地址，然后尝试访问它们。在我的情况下，它是192.168.1.23，这是中兴AC1200网状路由器的地址。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*来源：京东*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*来源：Walmart.com*{: .caption }