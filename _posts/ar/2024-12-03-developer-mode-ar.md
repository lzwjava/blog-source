---
audio: false
generated: false
lang: ar
layout: post
title: وضع المطور لنظام iOS وأداة ideviceinstaller
translated: true
---

## وضع المطور

كنت في وقت ما مطورًا لتطبيقات iOS لفترة من الوقت. لكن تركيزي المهني تحول إلى تقنيات أخرى. ومع ذلك، لا يزال من المفيد جدًا تطبيق معرفة تطوير iOS حتى لو لم أكن مطورًا محترفًا لتطبيقات iOS الآن.

مؤخرًا، أردت مشاركة التطبيقات المثبتة على جهازي. لكن إذا قمت بالتقاط لقطات شاشة لجميع التطبيقات من الشاشة الرئيسية أو من قائمة التطبيقات في الإعدادات، سيكون الأمر فوضويًا. لذا كنت بحاجة إلى إيجاد طريقة لعرض جميع التطبيقات المثبتة.

إليك الخطوات لعرض جميع التطبيقات المثبتة باستخدام Xcode:

1. قم بتوصيل iPhone الخاص بك بـ Mac عبر USB  
2. افتح Xcode  
3. انتقل إلى Window → Devices and Simulators (أو اضغط على Shift + Cmd + 2)  
4. اختر iPhone الخاص بك من الشريط الجانبي الأيسر  
5. في اللوحة الرئيسية، قم بالتمرير لأسفل إلى قسم "Installed Apps"

لديها وظائف أخرى مفيدة:

1. التقاط لقطات الشاشة  
2. فتح السجلات الحديثة  
3. فتح وحدة التحكم

## xcrun

`xcrun` هو أداة سطر أوامر تُستخدم في أنظمة macOS لتشغيل أدوات تطوير Apple (مثل `clang`، `swift`، وغيرها) من سطر الأوامر. تُستخدم `xcrun` للعثور على الأدوات المناسبة وتشغيلها من خلال سطر الأوامر دون الحاجة إلى تحديد المسار الكامل للأداة.

على سبيل المثال، إذا كنت تريد تشغيل مترجم Swift من سطر الأوامر، يمكنك استخدام الأمر التالي:

```bash
xcrun swift
```

سيقوم `xcrun` بالعثور على الإصدار الصحيح من Swift وتشغيله تلقائيًا.

يمكن أيضًا استخدام `xcrun` لتشغيل أدوات أخرى مثل `clang`، `lldb`، وغيرها. على سبيل المثال:

```bash
xcrun clang -o program program.c
```

سيقوم هذا الأمر بترجمة ملف `program.c` إلى ملف قابل للتنفيذ باستخدام مترجم `clang`.

بشكل عام، `xcrun` هي أداة مفيدة لتسهيل الوصول إلى أدوات تطوير Apple من سطر الأوامر دون الحاجة إلى تذكر المسارات الكاملة للأدوات.

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
تم تفعيل التسجيل التفصيلي.
2024-12-03 16:24:18.579+0800  تم تفعيل خدمات صورة قرص المطور.
2024-12-03 16:24:18.637+0800  تم الحصول على تأكيد الاستخدام.
التطبيقات المثبتة:
  - 0 عناصر
```

تم تنفيذ الأمر، استغرق 0.120 ثانية
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

**ترجمة الأوامر:**

- `brew install ideviceinstaller`: يقوم بتثبيت أداة `ideviceinstaller` باستخدام مدير الحزم `Homebrew`.
- `ideviceinstaller -l`: يعرض قائمة بالتطبيقات المثبتة على الجهاز المتصل.

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