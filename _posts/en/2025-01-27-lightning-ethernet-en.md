---
audio: true
lang: en
layout: post
title: Lightning to Ethernet Adapter
translated: false
---


I recently tried a new product that I had never used before. It cost me about 44 CNY on JD.com. Similar products cost around 15 USD on Walmart.com.

It works perfectly, and no extra settings are needed. An "Ethernet" menu item appears after plugging in the adapter.

I used the Speedtest iOS app to test the speed. The results are shown below.

| Network Type                     | Distance   | Download Speed (MBPS) | Upload Speed (MBPS) | Line             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Modem -> TP-LINK Router -> Phone | around 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Modem -> Cable -> Phone          | around 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

This is a somewhat naive test. I suspect one reason for the difference in speeds is that the connection from Modem -> TP-LINK Router is about 20m, and the connection from TP-LINK Router -> Phone is about 10m. Additionally, the TP-LINK Router uses a wireless bridge to connect to the modem.


{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Source: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Source: Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*Source: network_plot.py*{: .caption }
