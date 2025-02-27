---
audio: false
lang: hi
layout: post
title: ज्ञान लाइव ब्रॉडकास्ट प्लेटफॉर्म
translated: true
---

यह [https://github.com/lzwjava/live-server](https://github.com/lzwjava/live-server) से GitHub प्रोजेक्ट का README.md है।

---

### Fun Live: ज्ञान लाइव ब्रॉडकास्ट प्लेटफॉर्म

* [live-server](https://github.com/lzwjava/live-server)
* [live-web](https://github.com/lzwjava/live-web)
* [live-mobile-web](https://github.com/lzwjava/live-mobile-web)

<div align="center">

<img src="./img/img1.jpg" width="300px" /><img/>

<img src="./img/img2.jpg" width="300px" /><img/>

</div>

![img3](./img/img3.jpg)

![img14](./img/img4.jpg)

Fun Live एक अग्रणी ज्ञान लाइव ब्रॉडकास्ट प्लेटफॉर्म है, जो विभिन्न विषयों जैसे प्रोग्रामिंग और डिजाइन में उपयोगकर्ताओं के लिए रोचक शिक्षा अनुभवों को सुविधाजनक बनाने के लिए डिज़ाइन किया गया है। Fun Live के साथ, उपयोगकर्ता लाइव लेक्चर में आसानी से भाग ले सकते हैं, फीस या इनाम के माध्यम से योगदान कर सकते हैं, और अतिरिक्त सुविधा के लिए प्लेबैक विकल्प का आनंद ले सकते हैं।

#### विशेषताएं:
- **लाइव लेक्चर**: विभिन्न विषयों पर विविध ज्ञान लेक्चर को वास्तविक समय में एक्सेस करें।
- **मोनेटाइज़ेशन विकल्प**: उपयोगकर्ता लाइव सत्रों में भाग लेने के लिए फीस दे सकते हैं या लैक्टरर्स को उनके मूल्यवान विचारों के लिए इनाम दे सकते हैं।
- **OBS एकीकरण**: लैक्टरर्स OBS टूल का उपयोग करके लाइव स्ट्रीम को आसानी से पुश कर सकते हैं, जिससे सुलभ ब्रॉडकास्टिंग सुनिश्चित होती है।
- **प्लेबैक कार्यक्षमता**: वास्तविक समय में लेक्चर में भाग लेने या बाद में प्लेबैक तक पहुंचने की सुविधा का आनंद लेना।
- **सुलभ वीचैट एकीकरण**: वीचैट प्लेटफॉर्म के साथ आसानी से एकीकृत करें, जिसमें उपयोगकर्ता संलग्नता के लिए नोटिफिकेशन कार्यक्षमता शामिल है।

#### उपयोग:
1. रिपोजिटरी को क्लोन करें।
2. प्रिय विकास वातावरण में प्रोजेक्ट खोलें।
3. आवश्यकता के अनुसार सेटिंग्स को अनुकूलित और कॉन्फ़िगर करें।
4. एप्लिकेशन को अपने सर्वर पर डिप्लॉय करें।
5. रोचक ज्ञान लेक्चर को ब्रॉडकास्ट करना शुरू करें और अपने उपयोगकर्ताओं को खुश करें!

#### आँकड़े:
- **लाइव लेक्चर**: लगभग 80 लाइव लेक्चर होस्ट किए गए।
- **उपयोगकर्ता आधार**: 30,000 से अधिक उपयोगकर्ताओं ने भाग लिया।
- **पेज व्यू**: करोड़ों पेज व्यू उत्पन्न किए गए।

#### फ़ाइल संरचना:
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

### सहयोगी

| Commits | Author |
| ------ | ---- |
|   555 | lzwjava|
|    28|  Liu-Sheng Xin|
|    24|  PegasusWang|
|    24 | wujunze|
|    18 | liushengxin|
|     5|  Anrika|
|     4  |Amast|