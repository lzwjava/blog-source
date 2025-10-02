---
audio: false
generated: false
image: true
lang: ar
layout: post
title: بيكسل يو إس بي، أدوات مطور آي أو إس، الكتابة بالسحب
translated: true
---

### جدول المحتويات

1. [خيارات USB بكسل](#pixels-usb-options)
   - استخدام بكسل ككاميرا ويب
   - تمكين وضع المطور في الإعدادات
   - تفعيل تصحيح أخطاء USB للاتصال
   - التحقق من الاتصال باستخدام أمر ADB

2. [وضع المطور لنظام iOS و ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - عرض التطبيقات المثبتة عبر Xcode
   - استخدام Xcode لقطات الشاشة والسجلات
   - سرد التطبيقات باستخدام أمر xcrun
   - تثبيت واستخدام أداة ideviceinstaller

3. [الكتابة السريعة بالسحب](#quick-swipe-typing)
   - إدخال الكلمات عن طريق السحب فوق الحروف
   - ميزة اكتشفت بالصدفة
   - يظهر الخط أثناء اللمس السريع


## خيارات USB بكسل

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

يوفر Pixel العديد من خيارات USB، ومن الميزات المثيرة للاهتمام بشكل خاص قدرته على العمل ككاميرا ويب. على macOS، يمكن لـ QuickTime الوصول إلى كاميرا الويب Android كمصدر فيديو، مما يوفر حلاً بسيطًا وفعالًا.

لإعداد ذلك:

1. انتقل إلى "حول الهاتف" في الإعدادات وانقر على "رقم الإصدار" سبع مرات لتمكين وضع المطور.
2. افتح "خيارات المطور" وقم بتمكين "تصحيح أخطاء USB".
3. قم بتوصيل جهاز Pixel بجهاز الكمبيوتر الخاص بك عبر USB وقم بتشغيل الأمر التالي في Terminal للتحقق من الاتصال:
   ```bash
   adb devices
   ```

---

## وضع المطور لنظام iOS و ideviceinstaller

*2024.12.03*

## وضع المطور

كنت في السابق مطور iOS لبعض الوقت. لكن تركيز مسيرتي المهنية تحول إلى تقنيات أخرى. ومع ذلك، لا يزال من المفيد جدًا تطبيق معرفة تطوير iOS على الرغم من أنني لست مطور iOS محترفًا الآن.

مؤخرًا، أردت مشاركة تطبيقاتي المثبتة. ولكن إذا التقطت لقطات شاشة لجميع التطبيقات من الشاشة الرئيسية أو من قائمة التطبيقات في الإعدادات، فسيكون الأمر فوضويًا. لذلك احتجت إلى إيجاد طريقة لعرض جميع التطبيقات المثبتة.

إليك الخطوات لعرض جميع التطبيقات المثبتة باستخدام Xcode:

1. قم بتوصيل جهاز iPhone الخاص بك بجهاز Mac عبر USB
2. افتح Xcode
3. انتقل إلى Window ← Devices and Simulators (أو اضغط على Shift + Cmd + 2)
4. حدد جهاز iPhone الخاص بك من الشريط الجانبي الأيسر
5. في اللوحة الرئيسية، مرر لأسفل إلى قسم "Installed Apps"

يحتوي على وظائف مفيدة أخرى:

1. التقاط لقطات الشاشة
2. فتح السجلات الحديثة
3. فتح وحدة التحكم

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800 Enabling developer disk image services.
2024-12-03 16:24:18.637+0800 Acquired usage assertion.
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

## الكتابة السريعة بالسحب

*2024.12.01*

إذا أردت إدخال كلمة "threads" في iOS، ما عليك سوى رسم خط سريع لتغطية مواضع أحرف "threads" للحصول على النتيجة. دعونا نرَ كيف يعمل ذلك.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  متصفحك لا يدعم وسم الفيديو.
</video>

لقد اكتشفت هذا بالصدفة. عندما يلامس إصبعي منطقة الإدخال بسرعة، سيظهر خط. لا أعرف ما يعنيه ذلك. بعد بعض التجارب، توصلت إلى الاكتشاف المذكور أعلاه.