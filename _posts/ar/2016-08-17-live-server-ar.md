---
audio: false
lang: ar
layout: post
title: منصة بث مباشر المعرفة
translated: true
---

هذا هو README.md من مشروع GitHub [https://github.com/lzwjava/live-server](https://github.com/lzwjava/live-server).

---

### Fun Live: منصة بث مباشر للمعرفة

* [live-server](https://github.com/lzwjava/live-server)
* [live-web](https://github.com/lzwjava/live-web)
* [live-mobile-web](https://github.com/lzwjava/live-mobile-web)

<div align="center">

<img src="./img/img1.jpg" width="300px" /><img/>

<img src="./img/img2.jpg" width="300px" /><img/>

</div>

![img3](./img/img3.jpg)

![img14](./img/img4.jpg)

Fun Live هي منصة بث مباشر للمعرفة تقدم تجارب تعليمية مثيرة للاهتمام للمستخدمين من مختلف التخصصات، بما في ذلك البرمجة والتصميم. مع Fun Live، يمكن للمستخدمين المشاركة في المحاضرات المباشرة، المساهمة من خلال الرسوم أو الجوائز، واستمتاع بخيارات إعادة التشغيل للرفاهية الإضافية.

#### الميزات:
- **محاضرات مباشرة**: الوصول إلى محاضرات متنوعة في الوقت الفعلي، تغطي مجموعة واسعة من المواضيع.
- **خيارات التحويل إلى أموال**: يمكن للمستخدمين دفع الرسوم للمشاركة في جلسات مباشرة أو مكافأة المحاضرين على رؤيتهم القيمة.
- **تكامل OBS**: يمكن للمحاضرين دفع بث مباشر باستخدام أداة OBS، مما يضمن بثًا سلسًا.
- **وظيفة إعادة التشغيل**: استمتع بالتمكن من المشاركة في المحاضرات في الوقت الفعلي أو الوصول إلى إعادة التشغيل لاحقًا.
- **تكامل WeChat السلس**: التكامل السلس مع منصة WeChat، بما في ذلك وظائف الإشعارات لتحسين مشاركة المستخدم.

#### الاستخدام:
1. استنساخ المستودع.
2. فتح المشروع في بيئة تطويرك المفضلة.
3. تخصيص وإعداد الإعدادات حسب الحاجة.
4. نشر التطبيق على خادمك.
5. بدء بث محاضرات المعرفة المثيرة للمستخدمين!

#### الإحصائيات:
- **المحاضرات المستضافة**: حوالي 80 محاضرة مستضيفة.
- **قاعدة المستخدمين**: أكثر من 30,000 مستخدم مشارك.
- **مشاهدة الصفحات**: ملايين مشاهدات الصفحات.

#### هيكل الملفات:
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

### المساهمون

| التزامات | المؤلف |
| ------ | ---- |
|   555 | lzwjava|
|    28|  Liu-Sheng Xin|
|    24|  PegasusWang|
|    24 | wujunze|
|    18 | liushengxin|
|     5|  Anrika|
|     4  |Amast|