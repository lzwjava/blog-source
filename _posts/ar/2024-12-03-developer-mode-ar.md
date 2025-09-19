---
audio: false
generated: false
image: false
lang: ar
layout: post
title: وضع المطور لنظام iOS وبرنامج ideviceinstaller
translated: true
---

## الوضع المطور

كنت في يوم من الأيام مطورًا لنظام iOS لفترة من الوقت. لكن تركيزي المهني تحول إلى تقنيات أخرى. ومع ذلك، لا يزال من المفيد جدًا تطبيق معرفتي بتطوير iOS حتى لو لم أعد مطورًا محترفًا لنظام iOS الآن.

أردت مؤخرًا مشاركة التطبيقات المثبتة لدي. لكن إذا التقطت لقطات شاشة لجميع التطبيقات من شاشة الرئيسة أو من قائمة التطبيقات في الإعدادات، فسيكون الأمر فوضى. لذلك كنت بحاجة إلى العثور على طريقة لعرض جميع التطبيقات المثبتة.

هذه هي خطوات عرض جميع التطبيقات المثبتة باستخدام Xcode:

1. قُم بتوصيل iPhone الخاص بك بجهاز Mac عبر USB
2. افتح Xcode
3. انتقل إلى Window → Devices and Simulators (أو اضغط Shift + Cmd + 2)
4. اختر iPhone الخاص بك من الشريط الجانبي الأيسر
5. في اللوحة الرئيسية، قُم بالتمرير لأسفل إلى قسم "Installed Apps"

يحتوي على وظائف مفيدة أخرى:

1. التقاط لقطات الشاشة
2. فتح السجلات الأخيرة
3. فتح وحدة التحكم

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

---

## الكتابة بالتمرير السريع

*2024.12.01*

إذا أردت إدخال كلمة "threads" في نظام iOS، فكل ما تحتاجه هو رسم خط سريع يغطي مواضع أحرف "threads" للحصول على النتيجة. دعنا نرى كيف يعمل ذلك.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  متصفحك لا يدعم علامة الفيديو.
</video>

عثرت على ذلك عن طريق الصدفة. عندما تلمس إصبعي بسرعة منطقة الإدخال، يظهر خط. لم أكن أعرف ما يعنيه ذلك. بعد بعض التجارب، اكتشفت الاكتشاف أعلاه.