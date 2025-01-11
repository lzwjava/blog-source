---
lang: de
layout: post
title: '如何在电视上观看 YouTube


  在现代生活中，YouTube 已经成为了我们获取娱乐、学习和信息的重要平台。虽然大多数人习惯在手机或电脑上观看 YouTube，但在电视上观看 YouTube
  也能带来更好的视觉体验。以下是几种在电视上观看 YouTube 的方法：


  ### 1. 使用智能电视的内置 YouTube 应用

  大多数现代智能电视都预装了 YouTube 应用。你只需打开电视，找到并启动 YouTube 应用，然后登录你的 Google 账户即可开始观看。


  **步骤：**

  1. 打开智能电视。

  2. 在主菜单中找到 YouTube 应用。

  3. 启动应用并登录你的 Google 账户。

  4. 搜索或浏览你想观看的视频。


  ### 2. 使用流媒体设备（如 Chromecast、Apple TV、Roku）

  如果你的电视不是智能电视，或者没有内置 YouTube 应用，你可以通过流媒体设备将 YouTube 内容投射到电视上。


  **使用 Chromecast 的步骤：**

  1. 将 Chromecast 插入电视的 HDMI 端口。

  2. 确保 Chromecast 和你的手机或电脑连接到同一个 Wi-Fi 网络。

  3. 在手机或电脑上打开 YouTube 应用或网站。

  4. 点击“投射”图标，选择你的 Chromecast 设备。

  5. 视频将开始在电视上播放。


  **使用 Apple TV 的步骤：**

  1. 打开 Apple TV 并确保连接到 Wi-Fi。

  2. 在主屏幕上找到并打开 YouTube 应用。

  3. 登录你的 Google 账户。

  4. 搜索或浏览你想观看的视频。


  ### 3. 使用 HDMI 线连接电脑或手机

  如果你没有智能电视或流媒体设备，你可以通过 HDMI 线将电脑或手机直接连接到电视。


  **步骤：**

  1. 使用 HDMI 线将电脑或手机连接到电视。

  2. 将电视切换到相应的 HDMI 输入源。

  3. 在电脑或手机上打开 YouTube 并播放视频。

  4. 视频将显示在电视上。


  ### 4. 使用游戏主机（如 PlayStation、Xbox）

  许多游戏主机也支持 YouTube 应用，你可以通过这些设备在电视上观看 YouTube。


  **步骤：**

  1. 打开你的游戏主机并确保连接到互联网。

  2. 在主菜单中找到并启动 YouTube 应用。

  3. 登录你的 Google 账户。

  4. 搜索或浏览你想观看的视频。


  ### 5. 使用 DLNA 或 Miracast

  如果你的电视支持 DLNA 或 Miracast，你可以通过这些协议将手机或电脑上的 YouTube 内容无线投射到电视上。


  **步骤：**

  1. 确保你的电视和手机/电脑连接到同一个 Wi-Fi 网络。

  2. 在手机或电脑上启用屏幕镜像功能。

  3. 选择你的电视作为投射设备。

  4. 打开 YouTube 并播放视频，内容将显示在电视上。


  ### 总结

  无论你使用的是智能电视、流媒体设备、游戏主机还是简单的 HDMI 连接，都可以轻松地在电视上享受 YouTube 的内容。选择最适合你的方法，享受大屏幕带来的沉浸式体验吧！'
---

Hier nehmen wir an, dass wir wissen, wie man das Internet wissenschaftlich nutzt. Wie kann man dann YouTube auf dem Fernseher ansehen? Das Flashen des Routers ist etwas umständlich. Hier verwenden wir eine App.

## SmartYoutubeTV

![smart](assets/images/youtube-tv/smart.jpg)

Laden Sie es herunter. Installieren Sie es mit einem USB-Stick auf dem Fernseher.

![clash](assets/images/youtube-tv/clash.jpg)

Als nächstes wählen Sie in der Anwendung des Science-Internet-Clients die Option `Allow connect from LAN` aus. Dies bedeutet, dass andere Geräte im lokalen Netzwerk über dieses Gerät auf das Internet zugreifen können.

Gehen Sie dann zu den Einstellungen von `SmartYoutubeTV` und legen Sie den Port fest.

![proxy1](assets/images/youtube-tv/proxy1.jpeg)

Nachdem Sie alles eingerichtet haben, klicken Sie auf die Schaltfläche `Test`, um es auszuprobieren. Beachten Sie, dass ich hier einen Proxy vom Typ `SOCKS` verwendet habe. Ich habe es einige Male mit `HTTP` versucht, aber es hat nicht funktioniert. Wenn der Test erfolgreich ist, klicken Sie auf OK und testen Sie es erneut. Außerdem müssen Sie nicht unbedingt `192.168.1.3` einstellen, das hängt davon ab, welche lokale IP-Adresse Ihr Computer im Netzwerk hat.

So einfach ist das, sehr praktisch.

![tan](assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

Dies ist ein GitHub-Projekt. Die Projektseite enthält eine Bedienungsanleitung. Hier werden hauptsächlich einige zusätzliche Punkte ergänzt.

![seeker](assets/images/youtube-tv/seeker.jpg)

Es erreicht transparente Proxies durch die Verwendung von tun. Es implementiert Funktionen ähnlich dem Surge Enhanced Mode und dem Gateway Mode.

Zuerst habe ich `seeker` verwendet, um meinen Computer in einen Router für wissenschaftliches Surfen im Internet zu verwandeln. Hier sind meine Konfigurationen:

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

```yaml
servers:
  - name: HTTP-Proxy-Server
    addr: 0.0.0.0:7890
    protocol: Http
```

  - name: HTTPS-Proxy-Server
    addr: 0.0.0.0:7890
    protocol: Https

rules:
  - 'MATCH,PROXY'
```

Zuerst habe ich einen `socks5`-Proxy verwendet. Die Konfiguration sah so aus:

```yml
servers:
  - name: socks5 proxy server
    addr: 0.0.0.0:7891
    protocol: Socks5
```

Es gibt jedoch einige Probleme. Oft kann keine Verbindung hergestellt werden. In der Dokumentation steht folgender Abschnitt:

> Bei der Verwendung eines SOCKS5-Proxys müssen alle direkt verbundenen Domains in der Konfigurationsdatei festgelegt werden. Wenn Sie beispielsweise SS oder Vmess verwenden, müssen Sie auch die Domains der SS- oder Vmess-Server in die Konfigurationsdatei aufnehmen. Andernfalls könnte es zu einer Endlosschleife kommen, die die ordnungsgemäße Nutzung verhindert.

Das könnte der Grund sein.

Die Verwendung von `seeker` bedeutet, dass ein Computer benötigt wird, der es ausführt und als Router fungiert. Die Konfiguration mit `proxy` hingegen ist viel flexibler. Ich kann einen iPhone- oder Android-Handy verwenden, um den Proxy-Port freizugeben.

## Fernseh-Screenshot

Beim Schreiben dieses Artikels habe ich überlegt, wie man Screenshots auf dem Fernseher macht. Bei mir zu Hause verwenden wir einen Xiaomi-Fernseher. Man kann zweimal hintereinander die `Home`-Taste auf der Fernbedienung drücken, um das Anwendungsverwaltungsmenü aufzurufen.

![tv_screen](assets/images/youtube-tv/tv_screen.jpeg)

Siehst du den Screenshot-Button? Dann kannst du es auch ganz einfach mit WeChat teilen. Hier kannst du auch alle Anwendungen schließen. Wenn einige Anwendungen hängen bleiben, kannst du sie auf diese Weise behandeln.

Gut. Lassen Sie uns die Welt mit einem großen Fernseher betrachten.