---
audio: false
generated: false
image: false
lang: de
layout: post
title: 'Fun Live: Wissen Live-Streaming-Plattform'
translated: true
---

Dies ist die README.md aus dem GitHub-Projekt [https://github.com/lzwjava/live-server](https://github.com/lzwjava/live-server).

---

### Fun Live: Wissens-Live-Broadcasting-Plattform

* [live-server](https://github.com/lzwjava/live-server)
* [live-web](https://github.com/lzwjava/live-web)
* [live-mobile-web](https://github.com/lzwjava/live-mobile-web)

<div align="center">

<img src="./img/img1.jpg" width="300px" /><img/>

<img src="./img/img2.jpg" width="300px" /><img/>

</div>

![img3](./img/img3.jpg)

![img14](./img/img4.jpg)

Fun Live ist eine fortschrittliche Wissens-Live-Broadcasting-Plattform, die entwickelt wurde, um ansprechende Bildungserfahrungen für Benutzer aus verschiedenen Disziplinen, einschließlich Programmierung und Design, zu ermöglichen. Mit Fun Live können Benutzer nahtlos an Live-Vorträgen teilnehmen, durch Gebühren oder Belohnungen beitragen und die Wiedergabeoptionen für zusätzlichen Komfort nutzen.

#### Funktionen:
- **Live-Vorträge**: Greifen Sie auf vielfältige Wissensvorträge in Echtzeit zu, die eine breite Palette von Themen abdecken.
- **Vermarktungsoptionen**: Benutzer können Gebühren zahlen, um an Live-Sitzungen teilzunehmen, oder Dozenten für ihre wertvollen Einblicke belohnen.
- **OBS-Integration**: Dozenten können Live-Streams mühelos mit dem OBS-Tool senden, um eine reibungslose Übertragung zu gewährleisten.
- **Wiedergabefunktionalität**: Genießen Sie die Flexibilität, an Vorträgen in Echtzeit teilzunehmen oder die Wiedergabe später zu nutzen.
- **Nahtlose WeChat-Integration**: Integrieren Sie sich nahtlos in die WeChat-Plattform, einschließlich Benachrichtigungsfunktionen für eine verbesserte Benutzerinteraktion.

#### Nutzung:
1. Klonen Sie das Repository.
2. Öffnen Sie das Projekt in Ihrer bevorzugten Entwicklungsumgebung.
3. Passen Sie die Einstellungen nach Bedarf an.
4. Bereitstellen Sie die Anwendung auf Ihrem Server.
5. Beginnen Sie mit der Übertragung ansprechender Wissensvorträge und begeistern Sie Ihre Benutzer!

#### Statistiken:
- **Gehostete Vorträge**: Etwa 80 gehostete Vorträge.
- **Benutzerbasis**: Über 30.000 engagierte Benutzer.
- **Seitenaufrufe**: Millionen von generierten Seitenaufrufen.

#### Dateistruktur:
```
├── cache
│   └── index.html
├── config
│   ├── alipay.php
│   ├── autoload.php
│   ├── cacert.pem
│   ├── config.php
│   ├── constants.php
│   ├── database.php
│   ├── doctypes.php
│   ├── foreign_chars.php
│   ├── hooks.php
│   ├── index.html
│   ├── memcached.php
│   ├── migration.php
│   ├── mimes.php
│   ├── profiler.php
│   ├── rest.php
│   ├── routes.php
│   ├── smileys.php
│   └── user_agents.php
├── controllers
│   ├── Accounts.php
│   ├── Applications.php
│   ├── Attendances.php
│   ├── Charges.php
│   ├── Coupons.php
│   ├── Files.php
│   ├── Jobs.php
│   ├── LiveHooks.php
│   ├── LiveViews.php
│   ├── Lives.php
│   ├── Packets.php
│   ├── Qrcodes.php
│   ├── RecordedVideos.php
│   ├── Rest_server.php
│   ├── Rewards.php
│   ├── Shares.php
│   ├── Staffs.php
│   ├── Stats.php
│   ├── Subscribes.php
│   ├── Topics.php
│   ├── Users.php
│   ├── Videos.php
│   ├── Wechat.php
│   ├── WechatGroups.php
│   ├── Withdraws.php
│   └── index.html
├── core
│   ├── BaseController.php
│   └── index.html
├── data
│   ├── bjfudata.txt
│   └── iDev.json
├── helpers
│   ├── base_helper.php
│   └── index.html
├── hooks
│   └── index.html
├── id
├── index.html
├── language
│   ├── english
│   │   ├── index.html
│   │   └── rest_controller_lang.php
│   └── index.html
├── libraries
│   ├── Format.php
│   ├── JSSDK.php
│   ├── LeanCloud.php
│   ├── Pay.php
│   ├── QiniuLive.php
│   ├── REST_Controller.php
│   ├── Sms.php
│   ├── WeChatAppClient.php
│   ├── WeChatClient.php
│   ├── WeChatPlatform.php
│   ├── alipay
│   │   ├── Alipay.php
│   │   └── lib
│   │       ├── alipay_core.function.php
│   │       ├── alipay_notify.class.php
│   │       ├── alipay_rsa.function.php
│   ├── index.html
│   ├── wx
│   │   ├── WxPay.JsApiPay.php
│   │   ├── WxPay.php
│   │   ├── WxPayCallback.php
│   │   ├── cert
│   │   │   ├── ...
│   │   │   └── ...
│   │   └── lib
│   │       ├── WxPay.Api.php
│   │       ├── WxPay.Config.php
│   │       ├── WxPay.Data.php
│   │       ├── WxPay.Exception.php
│   │       └── WxPay.Notify.php
│   └── wxencrypt
│       ├── WxBizDataCrypt.php
│       ├── demo.php
│       ├── errorCode.php
│       └── pkcs7Encoder.php
├── logs
│   └── index.html
├── models
│   ├── AccountDao.php
│   ├── ApplicationDao.php
│   ├── AttendanceDao.php
│   ├── BaseDao.php
│   ├── ChargeDao.php
│   ├── CouponDao.php
│   ├── JobDao.php
│   ├── JobHelperDao.php
│   ├── LiveDao.php
│   ├── LiveViewDao.php
│   ├── PacketDao.php
│   ├── ParamDao.php
│   ├── PayNotifyDao.php
│   ├── QiniuDao.php
│   ├── RecordedVideoDao.php
│   ├── RewardDao.php
│   ├── ShareDao.php
│   ├── SnsUserDao.php
│   ├── StaffDao.php
│   ├── StatusDao.php
│   ├── SubscribeDao.php
│   ├── TopicDao.php
│   ├── TransactionDao.php
│   ├── UserDao.php
│   ├── UserPacketDao.php
│   ├── VideoDao.php
│   ├── WechatEventsDao.php
│   ├── WechatGroupDao.php
│   ├── WithdrawDao.php
│   ├── WxAppDao.php
│   ├── WxDao.php
│   ├── WxSessionDao.php
│   └── index.html
├── third_party
│   └── index.html
└── views
    ├── errors
    │   ├── cli
    │   │   ├── error_404.php
    │   │   ├── error_db.php
    │   │   ├── error_exception.php
    │   │   ├── error_general.php
    │   │   ├── error_php.php
    │   │   └── index.html
    │   ├── html
    │   │   ├── error_404.php
    │   │   ├── error_db.php
    │   │   ├── error_exception.php
    │   │   ├── error_general.php
    │   │   ├── error_php.php
    │   │   └── index.html
    │   └── index.html
    └── index.html
```

### Mitwirkende

| Commits | Autor |
| ------ | ---- |
|   555 | lzwjava|
|    28|  Liu-Sheng Xin|
|    24|  PegasusWang|
|    24 | wujunze|
|    18 | liushengxin|
|     5|  Anrika|
|     4  |Amast|