---
audio: true
generated: false
lang: en
layout: post
title: Lightning to Ethernet Adapter
---

I recently tried a new product that I had never used before. It cost me about 44 CNY on JD.com. Similar products cost around 15 USD on Walmart.com.

It works perfectly, and no extra settings are needed. An "Ethernet" menu item appears after plugging in the adapter.

I used the Speedtest iOS app to test the speed. The results are shown below.

| Network Type                     | Distance   | Download Speed (MBPS) | Upload Speed (MBPS) | Line             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Modem -> TP-LINK Router -> Phone | around 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Modem -> Cable -> Phone          | around 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

In one test, the ping (ms) responsiveness results are shown below:

| Metric   | Value | Jitter |
|----------|-------|--------|
| Idle     | 33    | 68     |
| Download | 1885  | 110    |
| Upload   | 127   | 54     |

This is a somewhat naive test. I suspect one reason for the difference in speeds is that the connection from Modem -> TP-LINK Router is about 20m, and the connection from TP-LINK Router -> Phone is about 10m. Additionally, the TP-LINK Router uses a wireless bridge to connect to the modem.

Speedtest is a useful tool. If you use a server in Alibaba Cloud and set the bandwidth to 5Mbps, then using the app to test it will yield results around 5Mbps.

The interesting thing is that if you connect both Wi-Fi and Ethernet, there is no way to prioritize one over the other. You can only use Ethernet in this configuration. If you want to use Wi-Fi, you have to unplug the Ethernet adapter.

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Source: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Source: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*Source: network_plot.py*{: .caption }
