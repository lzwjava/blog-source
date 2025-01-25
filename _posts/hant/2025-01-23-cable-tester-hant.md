---
audio: true
lang: hant
layout: post
title: 網絡線纜測試儀與網狀路由器
translated: true
---

## 網絡線測試儀

最近我在京東購買了一個網絡線測試儀。我曾經見過網絡顧問來我家或僱主辦公室測試網絡。

這個設備非常便宜，只需約10元人民幣。在沃爾瑪，類似產品大約要10美元。

這篇文章中，我使用了來自Amazon.com的圖片。

{: .centered }
![](assets/images/cable-tester/c.jpg){: .responsive }
*來源：Amazon.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/c2.jpg){: .responsive }
*來源：自攝*{: .caption }

{: .centered }
![](assets/images/cable-tester/c3.jpg){: .responsive }
*來源：自攝*{: .caption }

## 網狀路由器

我於2023年開始使用網狀路由器。我購買了一套TP-Link AX3000系統，包含兩個網狀路由器——一個主機和一個衛星機。當時花了我約484元人民幣，但現在京東上只需395元。

起初，我在大房子裡使用這套系統，後來搬到了父母家。

2025年春節期間的某些日子，我們全家住在大房子裡，再次經歷了WiFi網絡質量不佳的問題。為了解決這個問題，我購買了另一款網狀路由器——中興AC1200，價格約108元人民幣。

沃爾瑪上有類似產品，如TP-Link WiFi網狀路由器、Eero雙頻網狀路由器和NetGear Nighthawk AX3000。這些產品大多價格在50美元到200美元之間。

對於中興AC1200網狀路由器，我只需購買一個並啟用橋接模式，讓它接收WiFi信號後再發射自己的WiFi信號。效果非常好。原本路由器的域名地址是192.168.5.1。啟用橋接模式後，這個IP地址就無法訪問了。相反，192.168.1.1會將你重定向到家中的主路由器。此時，你可以通過訪問http://zte.home進入路由器的控制中心。

如果你能訪問主路由器，就能看到連接的設備及其IP地址。然後，你可以嘗試訪問每個設備，確定哪個是子路由器。在我的情況下，它是192.168.1.23，這是中興AC1200網狀路由器的地址。

對於手機，我們在家中移動時，最好使用2.4 GHz頻道，因為它更穩定。對於筆記本電腦或台式機，我們通常在臥室或書房使用，最好使用5 GHz頻道，因為它更快。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*來源：京東*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*來源：Walmart.com*{: .caption }

## 路由器的12V電源

可以使用USB升壓線為路由器供電，利用移動電源。

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*來源：京東*{: .caption }

## 幫助子路由器找到主路由器的兩種方法

有時，當信號較弱時，子路由器不容易找到主路由器。

如果我們必須將子路由器放在遠離主路由器的位置，我想知道是否先在附近位置連接，然後再移動到遠處，會比直接在遠處嘗試連接更快。

在附近保持連接，讓它們能夠互相通信。我發現這種方法更有效。