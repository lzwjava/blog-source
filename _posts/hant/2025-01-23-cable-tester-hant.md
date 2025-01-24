---
audio: true
lang: hant
layout: post
title: 網絡線纜測試儀與網狀路由器
translated: true
---

## 網絡線測試儀

最近我在京東購買了一個網絡線測試儀。之前見過網絡顧問來我家或公司辦公室測試網絡。

這個設備非常便宜，只需約10元人民幣。在沃爾瑪，類似產品要價約10美元。

本文使用的圖片來自Amazon.com。

{: .centered }
![](assets/images/cable-tester/c.jpg){: .responsive }
*來源：Amazon.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/c2.jpg){: .responsive }
*來源：自拍*{: .caption }

{: .centered }
![](assets/images/cable-tester/c3.jpg){: .responsive }
*來源：自拍*{: .caption }

## 網狀路由器

2023年我開始使用網狀路由器。當時購買了TP-Link AX3000系統，包含兩個網狀路由器——主機和衛星機，花費約484元人民幣，現在京東上僅售395元。

最初我在大房子裡使用這套系統，後來搬到了父母家。

2025年春節期間，家人住在大房子裡，再次遇到WiFi網絡質量差的問題。為此，我又購買了一台中興AC1200網狀路由器，價格約108元人民幣。

沃爾瑪上類似產品有TP-Link WiFi網狀路由器、Eero雙頻網狀路由器和NetGear Nighthawk AX3000，價格大多在50至200美元之間。

對於中興AC1200網狀路由器，只需購買一台並啟用橋接模式，即可接收WiFi信號並發射自己的WiFi信號，效果很好。原本路由器的域名地址是192.168.5.1，啟用橋接模式後，這個IP地址無法訪問，192.168.1.1會重定向到家庭網絡中的主路由器。此時，可以通過訪問http://zte.home進入路由器的控制中心。

如果能訪問主路由器，就能看到連接的設備及其IP地址，然後嘗試訪問每個設備以確定哪個是子路由器。在我的情況中，是192.168.1.23，即中興AC1200網狀路由器的地址。

對於在家中移動的手機，使用2.4 GHz頻道更穩定；對於通常在臥室或書房使用的筆記本或台式電腦，使用5 GHz頻道速度更快。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*來源：京東*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*來源：Walmart.com*{: .caption }