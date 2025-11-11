---
audio: false
generated: true
lang: ar
layout: post
title: برنامج آي أو إس لـ لين كلاود
translated: true
type: note
---

لاستخدام `pod 'AVOSCloud', '3.1.6.2'` في مشروع iOS، فأنت تشير إلى دمج إطار عمل AVOSCloud SDK (على الأرجح إطار عمل LeanCloud لخدمات السحابة) عبر CocoaPods، وهو مدير تبعيات لمشاريع iOS. إليك دليل خطوة بخطوة لإعداده:

---

### المتطلبات الأساسية
1. **تثبيت CocoaPods**: إذا لم يكن لديك CocoaPods مثبتًا، قم بتثبيته أولاً بتشغيل هذا الأمر في الطرفية:
   ```bash
   sudo gem install cocoapods
   ```
2. **مشروع Xcode**: تأكد من أن لديك مشروع iOS موجود في Xcode.

---

### خطوات استخدام `pod 'AVOSCloud', '3.1.6.2'`

1. **الانتقال إلى دليل مشروعك**:
   افتح الطرفية وانتقل إلى الدليل الذي يحتوي على ملف `.xcodeproj` الخاص بك:
   ```bash
   cd /path/to/your/project
   ```

2. **تهيئة ملف Podfile** (إذا لم يكن لديك واحد بالفعل):
   قم بتشغيل الأمر التالي لإنشاء ملف `Podfile`:
   ```bash
   pod init
   ```

3. **تحرير ملف Podfile**:
   افتح ملف `Podfile` في محرر نصوص (مثل `nano Podfile` أو `open Podfile`) وأضف الـ `AVOSCloud` pod مع الإصدار المحدد `3.1.6.2`. يجب أن يبدو ملف `Podfile` الخاص بك كما يلي تقريبًا:
   ```ruby
   platform :ios, '9.0'  # حدد الحد الأدنى لإصدار iOS (عدله حسب الحاجة)

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # أضف هذا السطر لـ AVOSCloud SDK
   end
   ```
   - استبدل `'YourAppName'` بالاسم الفعلي للهدف target الخاص بك في Xcode.
   - `use_frameworks!` مطلوب إذا كنت تستخدم Swift أو أطر عمل ديناميكية.

4. **تثبيت الـ Pod**:
   احفظ ملف `Podfile`، ثم قم بتشغيل هذا الأمر في الطرفية لتثبيت الإصدار المحدد من AVOSCloud:
   ```bash
   pod install
   ```
   - سيؤدي هذا إلى تنزيل الإصدار `3.1.6.2` من إطار عمل AVOSCloud SDK وإعداد مشروعك بملف `.xcworkspace`.

5. **فتح مساحة العمل Workspace**:
   بعد التثبيت، أغلق ملف `.xcodeproj` إذا كان مفتوحًا، وافتح ملف `.xcworkspace` الذي تم إنشاؤه حديثًا:
   ```bash
   open YourAppName.xcworkspace
   ```

6. **استيراد واستخدام AVOSCloud في الكود الخاص بك**:
   - في Objective-C:
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)example {
         [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hello" forKey:@"message"];
         [testObject save];
     }
     ```
   - في Swift:
     ```swift
     import AVOSCloud

     func example() {
         AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hello"
         try? testObject.save()
     }
     ```
   - استبدل `"your_app_id"` و `"your_client_key"` ببيانات اعتماد تطبيقك من LeanCloud من لوحة التحكم الخاصة بهم.

7. **تكوين بيانات اعتماد التطبيق**:
   - سجل الدخول في [LeanCloud](https://leancloud.app) (أو موفر خدمة AVOSCloud ذي الصلة).
   - احصل على `App ID` و `Client Key` من إعدادات تطبيقك وضعهما في الكود الخاص بك (كما هو موضح أعلاه).

8. **بناء وتشغيل المشروع**:
   قم ببناء مشروعك في Xcode (`Cmd + B`) للتأكد من إعداد كل شيء بشكل صحيح. إذا كانت هناك أخطاء، تحقق من بناء جملة ملف Podfile أو اتصال الشبكة.

---

### ملاحظات
- **إصدار محدد**: من خلال تحديد `'3.1.6.2'`، فأنت تقفل إطار العمل SDK على هذا الإصدار بالضبط. قد يكون هذا الإصدار قديمًا اعتبارًا من 03 مارس 2025. لاستخدام أحدث إصدار، اكتب ببساطة `pod 'AVOSCloud'` بدون رقم إصدار.
- **التوافق**: تأكد من أن الإصدار `3.1.6.2` يدعم هدف النشر target لنظام iOS الخاص بك (مثل iOS 9.0 أو أعلى). تحقق من [توثيق LeanCloud](https://leancloud.app/docs) للحصول على التفاصيل.
- **تحديث Pod**: إذا كنت بحاجة إلى تحديث CocoaPods أو استكشاف الأخطاء وإصلاحها، قم بتشغيل:
  ```bash
  pod update
  ```
- **استكشاف الأخطاء وإصلاحها**: إذا فشل `pod install`، جرب:
  ```bash
  pod repo update
  pod install --verbose
  ```

---

أعلمني إذا كنت بحاجة إلى مساعدة في جزء محدد، مثل دمج ميزة (مثل إشعارات الدفع، المراسلة في الوقت الفعلي) من AVOSCloud!