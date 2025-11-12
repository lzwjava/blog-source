---
audio: false
generated: true
lang: ar
layout: post
title: استخدام iVersion في نظام iOS
translated: true
type: note
---

لاستخدام pod `iVersion` في مشروع iOS الخاص بك، تحتاج إلى اتباع هذه الخطوات:

1. **افتح مشروعك في Xcode**: تأكد من أن مشروع Xcode الخاص بك مفتوح حيث تريد إضافة pod `iVersion`.

2. **تهيئة CocoaPods**: إذا لم تكن قد قمت بتهيئة CocoaPods في مشروعك بعد، افتح Terminal، وانتقل إلى دليل مشروعك، وقم بتشغيل:
   ```bash
   pod init
   ```
   سيؤدي هذا إلى إنشاء `Podfile` في دليل مشروعك.

3. **تحرير الـ Podfile**: افتح `Podfile` في محرر نصوص أو في Xcode. أضف pod `iVersion` إلى `Podfile` الخاص بك عن طريق تضمين السطر التالي داخل قسم الهدف (target section):
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **تثبيت الـ Pod**: احفظ `Podfile` وعد إلى Terminal. قم بتشغيل الأمر التالي لتثبيت pod `iVersion`:
   ```bash
   pod install
   ```

5. **افتح ملف `.xcworkspace`**: بعد اكتمال التثبيت، أغلق مشروع Xcode الخاص بك إذا كان مفتوحًا، ثم افتح ملف `.xcworkspace` newly created. يقع هذا الملف عادة في نفس الدليل مثل ملف `.xcodeproj` الأصلي الخاص بك.

6. **استيراد iVersion**: في ملفات Swift أو Objective-C الخاصة بك، قم باستيراد وحدة `iVersion` لبدء استخدامها:
   ```swift
   import iVersion
   ```

7. **استخدم iVersion في الكود الخاص بك**: يمكنك الآن استخدام مكتبة `iVersion` في مشروعك. على سبيل المثال، يمكنك التحقق من إصدار التطبيق أو رقم البناء (build number) باستخدام الطرق التي توفرها `iVersion`.

باتباع هذه الخطوات، يجب أن تكون قادرًا على دمج واستخدام pod `iVersion` بنجاح في مشروع iOS الخاص بك.