---
audio: true
lang: zh
layout: post
title: 网络电缆测试仪与网状路由器
translated: true
---

## 网络电缆测试仪

最近我在京东购买了一款网络电缆测试仪。之前，我曾见过网络顾问到我家中或雇主办公室进行网络测试。

这款设备非常便宜，仅需约10元人民币。在沃尔玛，类似产品的价格大约为10美元。

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

## Mesh路由器

2023年，我开始使用Mesh路由器。我购买了一套TP-Link AX3000系统，包含两个Mesh路由器——一个主路由和一个卫星路由。当时花费了约484元人民币，而现在在京东上仅售395元。

起初，我在大房子里使用这套系统，后来将其搬到了父母家。

2025年春节期间，有几天我们全家住在大房子里，再次遭遇了WiFi网络质量不佳的问题。为了解决这个问题，我又购买了一台中兴AC1200 Mesh路由器，价格约为108元人民币。

沃尔玛上类似的商品包括TP-Link WiFi Mesh路由器、Eero双频Mesh路由器和NetGear Nighthawk AX3000。这些产品的价格大多在50美元到200美元之间。

对于中兴AC1200 Mesh路由器，我只需购买一台并启用桥接模式，让它接收WiFi信号后再发射自己的WiFi信号，效果非常好。原本路由器的域名地址是192.168.5.1，启用桥接模式后，这个IP地址就无法访问了。取而代之的是，192.168.1.1会重定向到家庭网络中的主路由器。此时，你可以通过访问http://zte.home进入路由器的控制中心。

如果你能访问主路由器，就能看到连接的设备及其IP地址。然后，你可以尝试访问每个设备，以确定哪个是子路由器。在我的情况下，它是192.168.1.23，这就是中兴AC1200 Mesh路由器的地址。

对于在家中移动使用的手机，最好使用2.4 GHz频段，因为它更稳定。而对于通常在卧室或书房使用的笔记本电脑或台式电脑，最好使用5 GHz频段，因为它速度更快。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*来源：京东*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*来源：Walmart.com*{: .caption }