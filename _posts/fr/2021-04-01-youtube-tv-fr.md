---
lang: fr
layout: post
title: "## 如何在电视上观看 YouTube\n\nYouTube 提供了多种方式让您在大屏幕上享受视频内容。以下是几种常见的方法：\n\n**1. 使用智能电视的内置\
  \ YouTube 应用：**\n\n* 大多数现代智能电视都预装了 YouTube 应用。\n* 打开电视，找到 YouTube 应用并启动它。\n* 使用遥控器登录您的\
  \ YouTube 帐户，即可开始浏览和观看视频。\n\n**2. 使用流媒体设备：**\n\n* 如果您的电视不是智能电视，您可以使用流媒体设备，例如：\n\
  \    * **Chromecast:** 将您的手机、平板电脑或电脑上的 YouTube 视频投射到电视上。\n    * **Roku:** 提供各种流媒体频道，包括\
  \ YouTube。\n    * **Apple TV:** 提供无缝的 Apple 生态系统集成和 YouTube 应用。\n    * **Amazon\
  \ Fire TV Stick:** 提供对 Amazon Prime Video 和其他流媒体服务的访问，包括 YouTube。\n* 将流媒体设备连接到电视的\
  \ HDMI 端口，按照屏幕上的说明进行设置，然后启动 YouTube 应用。\n\n**3. 使用游戏机：**\n\n* 许多游戏机，例如 PlayStation\
  \ 和 Xbox，都有 YouTube 应用。\n* 在游戏机上启动 YouTube 应用，登录您的帐户，即可开始观看。\n\n**4. 使用 HDMI 线缆：**\n\
  \n* 将您的笔记本电脑或电脑连接到电视的 HDMI 端口。\n* 在您的电脑上打开 YouTube 网站，选择您要观看的视频，然后将其全屏显示。\n\n**5.\
  \ 使用 AirPlay（适用于 Apple 设备）：**\n\n* 如果您的电视支持 AirPlay，您可以将 iPhone、iPad 或 Mac 上的 YouTube\
  \ 视频无线传输到电视上。\n* 在您的 Apple 设备上打开 YouTube 应用，选择您要观看的视频，然后点击 AirPlay 图标并选择您的电视。\n\n\
  **提示：**\n\n* 确保您的电视和流媒体设备连接到互联网。\n* 使用遥控器或游戏手柄浏览 YouTube 应用。\n* 您可以使用语音搜索功能来查找特定的视频。\n\
  * 创建播放列表以便于访问您喜爱的视频。\n\n通过以上方法，您可以轻松地在电视上享受 YouTube 的海量视频内容。"
---

Supposons que nous sachions comment accéder à Internet de manière scientifique, alors comment regarder YouTube sur une télévision ? Configurer le routeur peut être un peu compliqué. Ici, nous allons utiliser une application pour y parvenir.

## SmartYoutubeTV

![smart](assets/images/youtube-tv/smart.jpg)

Téléchargez-le. Installez-le sur votre télévision à l'aide d'une clé USB.

![clash](assets/images/youtube-tv/clash.jpg)

Ensuite, dans l'application cliente de l'accès scientifique à Internet, sélectionnez `Allow connnect from Lan`. Cela signifie que d'autres appareils sur le réseau local peuvent se connecter à notre appareil pour accéder à Internet.

Ensuite, dans les options de configuration de `SmartYoutubeTV`, il suffit de définir le port.

![proxy1](assets/images/youtube-tv/proxy1.jpeg)

Après avoir effectué les réglages, cliquez sur le bouton `Tester` pour essayer. Notez que j'ai utilisé ici un proxy de type `SOCKS`. J'ai essayé plusieurs fois avec `HTTP` sans succès. Une fois le test réussi, cliquez sur OK, puis testez à nouveau. Ensuite, il n'est pas nécessaire que vous configuriez `192.168.1.3`, cela dépend de l'adresse de votre réseau local sur votre ordinateur.

C'est vraiment pratique, on peut voir tout de suite.

![tan](assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

Voici un projet GitHub. La page d'accueil du projet contient des instructions d'utilisation. Ici, nous allons principalement ajouter quelques points supplémentaires.

![seeker](assets/images/youtube-tv/seeker.jpg)

Il utilise tun pour implémenter un proxy transparent. Il réalise des fonctionnalités similaires au mode amélioré et au mode passerelle de Surge.

Dès le début, j'ai utilisé `seeker` pour transformer mon ordinateur en routeur de navigation scientifique. Voici ma configuration :

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

servers:
  - name: serveur proxy HTTP
    addr: 0.0.0.0:7890
    protocol: Http

```yaml
  - name: serveur proxy https
    addr: 0.0.0.0:7890
    protocol: Https
```

rules:
  - 'MATCH,PROXY'
```

Au début, j'utilisais un proxy `socks5`. J'ai configuré comme ceci :

```yml
servers:
  - name: serveur proxy socks5
    addr: 0.0.0.0:7891
    protocol: Socks5
```

Cependant, il y a pas mal de problèmes. La connexion échoue souvent. La documentation contient ce passage :

> Lorsque vous utilisez un proxy socks5, vous devez configurer tous les domaines en connexion directe dans le fichier de configuration. Si vous utilisez ss ou vmess, vous devez également ajouter le domaine du serveur ss ou vmess dans le fichier de configuration. Sinon, cela pourrait entraîner une boucle infinie et empêcher une utilisation normale.

C'est peut-être la raison.

Utiliser `seeker` implique qu'il faut avoir un ordinateur qui le fait tourner, en l'utilisant comme un routeur. En revanche, la configuration via `proxy` offre beaucoup plus de flexibilité. Je peux utiliser un iPhone ou un téléphone Android pour partager le port du proxy.

## Capture d'écran de télévision

En écrivant cet article, j'ai réfléchi à la manière de capturer des captures d'écran sur une télévision. Chez moi, nous utilisons une télévision Xiaomi. Vous pouvez appuyer deux fois de suite sur le bouton `Home` de la télécommande pour faire apparaître le menu de gestion des applications.

![tv_screen](assets/images/youtube-tv/tv_screen.jpeg)

Vous voyez le bouton de capture d'écran ? Ensuite, il est très pratique de partager directement sur WeChat. Ici, vous pouvez également fermer toutes les applications. Si certaines applications se bloquent, vous pouvez les gérer de cette manière.

Très bien. Utilisons une télévision grand écran pour observer le monde.