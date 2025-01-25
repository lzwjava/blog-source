---
audio: true
lang: zh
layout: post
title: 网络电缆测试仪与网状路由器
translated: true
---

## 网线测试仪

最近我在京东购买了一款网线测试仪。我曾见过网络顾问到我家中或雇主的办公室进行网络测试。

这款设备非常便宜，仅需约10元人民币。在沃尔玛，类似产品售价约为10美元。

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

2023年，我开始使用Mesh路由器。我购买了一套TP-Link AX3000系统，包含两个Mesh路由器——一个主单元和一个卫星单元。当时花费约484元人民币，现在京东上仅售395元。

起初，我在大房子里使用这套系统，后来搬到了父母家。

2025年春节期间，有几天我们全家住在大房子里，再次遭遇WiFi网络质量不佳的问题。为此，我又购买了一台中兴AC1200 Mesh路由器，价格约108元人民币。

沃尔玛上类似的产品有TP-Link WiFi Mesh路由器、Eero双频Mesh路由器和NetGear Nighthawk AX3000。这些产品大多价格在50美元到200美元之间。

对于中兴AC1200 Mesh路由器，我只需购买一台并启用桥接模式，让它接收WiFi信号后再发射自己的WiFi信号，效果非常好。原本路由器的域地址是192.168.5.1，启用桥接模式后，这个IP地址无法访问，而192.168.1.1会重定向到家庭网络中的主路由器。此时，你可以通过访问http://zte.home进入路由器的控制中心。

如果你能访问主路由器，就能看到连接的设备及其IP地址。然后，你可以尝试访问每个设备，以确定哪个是子路由器。在我的情况下，它是192.168.1.23，即中兴AC1200 Mesh路由器的地址。

对于在家中移动的手机，使用2.4 GHz频段更为稳定。而对于通常在卧室或书房使用的笔记本电脑或台式电脑，5 GHz频段速度更快。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*来源：京东*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*来源：Walmart.com*{: .caption }

## 路由器的12V电源

可以使用USB升压线通过移动电源为路由器供电。

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*来源：京东*{: .caption }

## 帮助子路由器找到主路由器的两种方法

有时，当信号较弱时，子路由器难以找到主路由器。

如果必须将子路由器放置在远离主路由器的地方，我想知道是否先在附近连接再移远，比直接在远处尝试连接更快。

保持近距离连接能让它们彼此通信。我发现这种方法更为有效。