---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 如何在電視上看 YouTube
translated: true
---

這裡假設我們知道如何科學上網，那如何在電視上看Youtube呢。刷路由有點麻煩。這裡借助一個應用。

## SmartYoutubeTV

![smart](assets/images/youtube-tv/smart.jpg)

把它下載下來。用U盤安裝到電視上。

![clash](assets/images/youtube-tv/clash.jpg)

接下來在科學上網應用客戶端上選上，`Allow connnect from Lan`。意思是支持局域網其它設備連接我們這台設備來上網。

接著在`SmartYoutubeTV`的設置選項，設置上端口就行了。

![proxy1](assets/images/youtube-tv/proxy1.jpeg)

設置完後。點擊`測試`按鈕試試看。注意到我這裡用了`SOCKS`類型的代理。用`HTTP`的試過幾次沒成功。測試成功後，點擊確定，然後測試看看。其次，你那裡不一定設置成`192.168.1.3`，得看你電腦局域網地址是什麼。

這樣就看上了，很方便。

![tan](assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

這是一個 GitHub 項目。項目主頁有使用說明。這裡主要補充一些額外的要點。

![seeker](assets/images/youtube-tv/seeker.jpg)

它通過使用 tun 來實現透明代理。實現了類似 surge 增強模式與網關模式。

一開始我就用`seeker`來把我電腦變成科學上網路由器。這裡說說我的配置：

```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53  
dns_timeout: 1s
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2s
probe_timeout: 30ms
connect_timeout: 1s
read_timeout: 30s
write_timeout: 5s
max_connect_errors: 2 

servers:
  - name: http proxy server
    addr: 0.0.0.0:7890
    protocol: Http

  - name: https proxy server
    addr: 0.0.0.0:7890
    protocol: Https

rules:
  - 'MATCH,PROXY'
```

一開始我用的是 `socks5`代理。把配置寫成這樣：

```yml
servers:
  - name: socks5 proxy server
    addr: 0.0.0.0:7891
    protocol: Socks5
```

然而有挺多問題。經常連接不上。文檔有這麼一段話：

> 使用 socks5 代理的時候，需要將所有直連的域名設置在配置文件裡面，如果使用 ss 或者 vmess 之類的，需要將 ss 或 vmess server 的域名也加入配置文件。否則有可能會導致死循環，沒法正常使用。

可能是這個原因。

用`seeker`，意味著需要有台電腦運行著它，把它當做路由器來用。而用`proxy`配置的方式，則靈活很多。我可以用iPhone或Android手機來分享代理端口。

## 電視截圖

在寫這篇文章時，琢磨了如何在電視上截圖。我家用的是小米電視。可以在遙控器上連按兩下`Home`健，喚出應用管理菜單。

![tv_screen](assets/images/youtube-tv/tv_screen.jpeg)

看到截圖按鈕了嗎。接著還可以把應用程序都關掉。有些應用卡掉的話，則可以這樣處理。

好了。讓我們用大屏電視來看世界吧。