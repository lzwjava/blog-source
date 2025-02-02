---
audio: false
lang: hi
layout: post
title: ज्ञान लाइव ब्रॉडकास्ट प्लेटफॉर्म
translated: true
---

यह `README.md` है github पर `live-server` प्रोजेक्ट से [https://github.com/lzwjava/live-server](https://github.com/lzwjava/live-server)।

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

Fun Live एक नवीन ज्ञान लाइव ब्रॉडकास्ट प्लेटफॉर्म है, जिसका डिज़ाइन विभिन्न विषयों जैसे प्रोग्रामिंग और डिजाइन में उपयोगकर्ताओं के लिए संलग्न शिक्षा अनुभवों को सुविधाजनक बनाने के लिए है। Fun Live के साथ उपयोगकर्ता आसानी से लाइव लेक्चर में भाग ले सकते हैं, शुल्क या इनाम के माध्यम से योगदान कर सकते हैं, और बढ़े हुए सुविधा के लिए पुन: चालन विकल्पों का आनंद ले सकते हैं।

#### विशेषताएँ:
- **लाइव लेक्चर**: वास्तविक समय में विभिन्न विषयों पर विविध ज्ञान लेक्चर तक पहुंचें।
- **मोनेटाइजेशन विकल्प**: उपयोगकर्ता लाइव सत्रों में भाग लेने के लिए शुल्क देना हो सकते हैं या लेक्चरर को उनके मूल्यवान अवधारणाओं के लिए इनाम प्रदान कर सकते हैं।
- **OBS एकीकरण**: लेक्चरर OBS टूल का उपयोग करके लाइव स्ट्रीम आसानी से पुश कर सकते हैं, जिससे चालित प्रसारण सुनिश्चित होता है।
- **पुन: चालन कार्यक्षमता**: वास्तविक समय में लेक्चरों में भाग लेने का लचीलापन या बाद में पुन: चालन के लिए पहुंचें।
- **सुलभ WeChat एकीकरण**: WeChat प्लेटफॉर्म के साथ सुलभ तरीके से एकीकरण, जिसमें उपयोगकर्ता एकाग्रता के लिए नोटिफिकेशन कार्यक्षमता शामिल है।

#### उपयोग:
1. रिपोजिटरी को क्लोन करें।
2. अपने पसंदीदा विकास पर्यावरण में प्रोजेक्ट खोलें।
3. आवश्यकता के अनुसार सेटिंग्स को अनुकूलित और कॉन्फ़िगर करें।
4. एप्लिकेशन को अपने सर्वर पर डिप्लॉय करें।
5. संलग्न ज्ञान लेक्चर प्रसारण शुरू करें और अपने उपयोगकर्ताओं को खुश करें!

#### आँकड़े:
- **लाइव लेक्चर**: लगभग 80 लाइव लेक्चर मेजबानी किए गए।
- **उपयोगकर्ता बेस**: 30,000 से अधिक उपयोगकर्ताओं के साथ।
- **पेज व्यू**: करोड़ों पेज व्यू उत्पन्न किए गए।

#### फाइल संरचना:
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

### योगदानकर्ता:

| Commits | Author |
| ------ | ---- |
|   555 | lzwjava|
|    28|  Liu-Sheng Xin|
|    24|  PegasusWang|
|    24 | wujunze|
|    18 | liushengxin|
|     5|  Anrika|
|     4  |Amast|