---
audio: true
lang: zh
layout: post
title: Lightning 转以太网适配器
translated: true
---

最近，我尝试了一款之前从未使用过的新产品。在京东上购买大约花费了44元人民币。类似的产品在沃尔玛官网上售价约为15美元。

这款产品使用起来非常顺畅，无需额外设置。插入适配器后，菜单中便会出现“以太网”选项。

我使用了Speedtest iOS应用程序来测试网速，结果如下所示。

| 网络类型                     | 距离       | 下载速度 (MBPS) | 上传速度 (MBPS) | 线路             |
|------------------------------|------------|-----------------|-----------------|------------------|
| 调制解调器 -> TP-LINK路由器 -> 手机 | 约30米     | 2.90            | 4.82            | 广州 -> 澳门     |
| 调制解调器 -> 网线 -> 手机    | 约30米     | 84.9            | 59.7            | 广州 -> 澳门     |

这是一个相对简单的测试。我怀疑速度差异的一个原因是，调制解调器到TP-LINK路由器的连接大约有20米，而TP-LINK路由器到手机的距离大约为10米。此外，TP-LINK路由器通过无线桥接方式连接到调制解调器。


{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*来源：iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*来源：Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*来源：network_plot.py*{: .caption }