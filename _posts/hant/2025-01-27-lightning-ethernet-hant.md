---
audio: true
lang: hant
layout: post
title: Lightning 至乙太網路轉接器
translated: true
---

最近，我嘗試了一款從未使用過的新產品。這款產品在京東上花了我大約44元人民幣。而在沃爾瑪網站上，類似產品的價格約為15美元。

它運作得非常完美，無需額外設置。插入適配器後，會出現一個“以太網”菜單項。

我使用了Speedtest iOS應用程序來測試速度。結果如下所示。

| 網絡類型                     | 距離   | 下載速度 (MBPS) | 上傳速度 (MBPS) | 線路             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| 調制解調器 -> TP-LINK路由器 -> 手機 | 約30米 | 2.90                  | 4.82                | 廣州 -> 澳門 |
| 調制解調器 -> 網線 -> 手機          | 約30米 | 84.9                  | 59.7                | 廣州 -> 澳門 |

這是一個相對簡單的測試。我懷疑速度差異的一個原因是，從調制解調器到TP-LINK路由器的連接約為20米，而從TP-LINK路由器到手機的連接約為10米。此外，TP-LINK路由器使用無線橋接方式連接到調制解調器。


{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*來源：iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*來源：Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*來源：network_plot.py*{: .caption }