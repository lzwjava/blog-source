---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 雷電轉以太網轉接器
translated: true
---

我最近試用了一款從未使用過的新產品。它在京東買的花了我約44人民幣。類似的產品在Walmart.com上賣約15美元。

它運行得完美無缺，不需要額外設置。插入適配器後會出現一個「乙太網」選單項。

我使用了Speedtest iOS應用程式來測試速度。結果如下所示。

| 網絡類型                         | 距離     | 下載速度 (MBPS) | 上傳速度 (MBPS) | 線路             |
|----------------------------------|----------|-----------------|-----------------|------------------|
| 調制解調器 -> TP-LINK 路由器 -> 手機 | 約30米   | 2.90            | 4.82            | 廣州 -> 澳門     |
| 調制解調器 -> 網線 -> 手機        | 約30米   | 84.9            | 59.7            | 廣州 -> 澳門     |

在一次測試中，ping (ms) 的響應結果如下所示：

| 指標     | 值    | Jitter |
|----------|-------|--------|
| 閒置     | 33    | 68     |
| 下載     | 1885  | 110    |
| 上傳     | 127   | 54     |

這是一個有點天真的測試。我懷疑速度差異的一個原因是從調制解調器 -> TP-LINK 路由器的連接約為20米，而從TP-LINK 路由器 -> 手機的連接約為10米。此外，TP-LINK 路由器使用無線橋接連接到調制解調器。

Speedtest是一個有用的工具。如果你使用阿里雲的伺服器並將頻寬設置為5Mbps，那麼使用該應用程式測試將會得到約5Mbps的結果。

有趣的是，如果你同時連接Wi-Fi和乙太網，沒有辦法優先選擇其中一個。你只能在這個配置中使用乙太網。如果你想使用Wi-Fi，你必須拔掉乙太網適配器。

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*來源：iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*來源：Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*來源：network_plot.py*{: .caption }