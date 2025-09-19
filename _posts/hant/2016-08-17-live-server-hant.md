---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 知識直播平台
translated: true
---

這是來自 GitHub 專案 [https://github.com/lzwjava/live-server](https://github.com/lzwjava/live-server) 的 README.md。

---

### 有趣直播：知識直播平台

* [live-server](https://github.com/lzwjava/live-server)
* [live-web](https://github.com/lzwjava/live-web)
* [live-mobile-web](https://github.com/lzwjava/live-mobile-web)

<div align="center">

<img src="./img/img1.jpg" width="300px" /><img/>

<img src="./img/img2.jpg" width="300px" /><img/>

</div>

![img3](./img/img3.jpg)

![img14](./img/img4.jpg)

有趣直播是一個前沿的知識直播平台，旨在為用戶提供各種學科的互動式教育體驗，包括編程和設計。透過有趣直播，用戶可以順利參加直播講座，通過費用或獎勵進行貢獻，並享受播放選項以增加便利。

#### 功能：
- **直播講座**：即時訪問多樣化的知識講座，涵蓋廣泛的主題。
- **收益選項**：用戶可以支付費用參加直播會議或獎勵講師的寶貴見解。
- **OBS 整合**：講師可以輕鬆地使用 OBS 工具推送直播，確保順暢的廣播。
- **播放功能**：享受即時參加講座或稍後訪問播放的靈活性。
- **無縫微信整合**：與微信平台無縫整合，包括通知功能以增強用戶參與度。

#### 使用方法：
1. 克隆存儲庫。
2. 在您喜歡的開發環境中打開項目。
3. 根據需要自定義和配置設置。
4. 將應用程序部署到您的伺服器。
5. 开始廣播引人入勝的知識講座，讓您的用戶感到愉快！

#### 統計數據：
- **舉辦講座**：約 80 場講座舉辦。
- **用戶基數**：超過 30,000 名用戶參與。
- **頁面瀏覽量**：數百萬頁面瀏覽量產生。

#### 文件結構：
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

### 貢獻者

| 提交 | 作者 |
| ------ | ---- |
| 555 | lzwjava|
| 28 | Liu-Sheng Xin|
| 24 | PegasusWang|
| 24 | wujunze|
| 18 | liushengxin|
| 5 | Anrika|
| 4 | Amast|