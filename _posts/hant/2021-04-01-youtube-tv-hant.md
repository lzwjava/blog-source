---
lang: hant
layout: post
title: 如何在电视上观看 YouTube
---

这里假设我们已经掌握了科学上网的方法，那么如何在电视上观看YouTube呢？直接刷路由器设置可能有些复杂。这里我们可以借助一个应用程序来实现。

## 智能YouTube电视

![智能](assets/images/youtube-tv/smart.jpg)

把它下载下来，用U盘安装到电视上。

![clash](assets/images/youtube-tv/clash.jpg)

接下来在科学上网应用客户端上勾选`允许局域网连接`（Allow connect from LAN）。这意味着支持局域网内的其他设备通过我们这台设备进行上网。

接着在`SmartYoutubeTV`的设置选项中，配置好端口即可。

![代理1](assets/images/youtube-tv/proxy1.jpeg)

设置完成后，点击`测试`按钮进行尝试。请注意，我这里使用了`SOCKS`类型的代理。之前尝试过几次`HTTP`类型的代理，但未能成功。测试成功后，点击确定，然后再次测试确认。另外，你的设置中不一定需要填写`192.168.1.3`，这取决于你电脑在局域网中的实际地址。

這樣就看上了，很方便。

![tan](assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

這是一個 GitHub 專案。專案主頁上有使用說明。這裡主要補充一些額外的要點。

![探索者](assets/images/youtube-tv/seeker.jpg)

它通过使用 tun 实现透明代理，提供了类似于 Surge 增强模式和网关模式的功能。

一开始，我就使用`seeker`将我的电脑转变为科学上网的路由器。下面分享一下我的配置情况：

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
```

翻譯成繁體中文：

```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53  
dns_timeout: 1秒
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2秒
probe_timeout: 30毫秒
connect_timeout: 1秒
read_timeout: 30秒
write_timeout: 5秒
max_connect_errors: 2
```

服务器：
  - 名称：HTTP 代理服务器
    地址：0.0.0.0:7890
    协议：Http

  - 名称: HTTPS 代理服务器
    地址: 0.0.0.0:7890
    协议: HTTPS

規則：
  - '匹配,代理'
```

一开始我用的是 `socks5` 代理。把配置写成这样：

```yml
servers:
  - name: socks5 代理伺服器
    addr: 0.0.0.0:7891
    protocol: Socks5
```

然而存在不少問題。經常無法連接。文檔中有這樣一段話：

> 使用 socks5 代理时，需将所有直连的域名配置在文件中，若使用 ss 或 vmess 等协议，还需将 ss 或 vmess 服务器的域名一并加入配置文件。否则，可能会引发死循环，导致无法正常使用。

可能是這個原因。

使用`seeker`意味着需要有一台电脑持续运行它，并将其当作路由器来使用。而采用`proxy`配置的方式则灵活得多。我可以利用iPhone或Android手机来分享代理端口。

## 电视画面捕捉

在撰写这篇文章时，我思考了如何在电视上进行截图。我家使用的是小米电视。只需在遥控器上连续按两下`Home`键，即可唤出应用管理菜单。

![电视屏幕](assets/images/youtube-tv/tv_screen.jpeg)

看到截圖按鈕了嗎？接著還能很方便地分享到微信。這裡還可以關閉所有應用程序。如果有些應用卡住了，就可以這樣處理。

好的。让我们用大屏幕电视来探索世界吧。