---
audio: false
generated: true
lang: ar
layout: post
title: LeanCloud iOS SDK
translated: true
---

لاستخدام `pod 'AVOSCloud', '3.1.6.2'` في مشروع iOS، فإنك تتحدث عن دمج SDK AVOSCloud (ربما SDK LeanCloud للخدمات السحابية) عبر CocoaPods، مدير الاعتماديات لمشاريع iOS. إليك دليل خطوة بخطوة لتثبيته:

---

### المتطلبات الأساسية
1. **تثبيت CocoaPods**: إذا لم يكن لديك CocoaPods مثبتًا، قم بتثبيته أولاً من خلال تنفيذ الأمر التالي في الموجه:
   ```bash
   sudo gem install cocoapods
   ```
2. **مشروع Xcode**: تأكد من وجود مشروع iOS موجود في Xcode.

---

### خطوات لاستخدام `pod 'AVOSCloud', '3.1.6.2'`

1. **الانتقال إلى مجلد المشروع**:
   افتح الموجه واذهب إلى المجلد الذي يحتوي على ملف `.xcodeproj`:
   ```bash
   cd /path/to/your/project
   ```

2. **تهيئة ملف Podfile** (إذا لم يكن لديك واحدًا بالفعل):
   قم بتنفيد الأمر التالي لإنشاء ملف `Podfile`:
   ```bash
   pod init
   ```

3. **تحرير ملف Podfile**:
   افتح ملف `Podfile` في محرر النصوص (مثل `nano Podfile` أو `open Podfile`) واضف الحزمة `AVOSCloud` مع الإصدار المحدد `3.1.6.2`. يجب أن يبدو ملف `Podfile` مثل هذا:
   ```ruby
   platform :ios, '9.0'  # تحديد الإصدار الأدنى من iOS (قم بتعديله حسب الحاجة)

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # أضف هذا السطر لمكتبة SDK AVOSCloud
   end
   ```
   - استبدل `'YourAppName'` باسم الهدف الفعلي في Xcode.
   - `use_frameworks!` مطلوب إذا كنت تستخدم Swift أو الإطارات الديناميكية.

4. **تثبيت الحزمة**:
   احفظ ملف `Podfile` ثم قم بتنفيد الأمر التالي في الموجه لتثبيت الإصدار المحدد من AVOSCloud:
   ```bash
   pod install
   ```
   - هذا سيقوم بتنزيل الإصدار `3.1.6.2` من SDK AVOSCloud ويضع مشروعك مع ملف `.xcworkspace`.

5. **فتح مساحة العمل**:
   بعد التثبيت، اغلق ملف `.xcodeproj` إذا كان مفتوحًا، وافتح الملف `.xcworkspace` الجديد:
   ```bash
   open YourAppName.xcworkspace
   ```

6. **استيراد واستخدام AVOSCloud في كودك**:
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
   - استبدل `"your_app_id"` و `"your_client_key"` بمعلومات اعتماد تطبيق LeanCloud الخاص بك من لوحة التحكم.

7. **تكوين بيانات اعتماد التطبيق**:
   - سجل الدخول في [LeanCloud](https://leancloud.app) (أو مزود الخدمة AVOSCloud المناسب).
   - احصل على `App ID` و `Client Key` من إعدادات تطبيقك وضعهما في كودك (كما هو موضح أعلاه).

8. **بناء و تشغيل**:
   قم ببناء مشروعك في Xcode (`Cmd + B`) لضمان أن كل شيء قد تم إعداده بشكل صحيح. إذا كان هناك أخطاء، تحقق من صياغة ملف Podfile أو اتصال الشبكة.

---

### ملاحظات
- **إصدار محدد**: من خلال تحديد `'3.1.6.2'،` أنت تقفل SDK على هذا الإصدار بالضبط. قد يكون هذا قديمًا اعتبارًا من 3 مارس 2025. لاستخدام أحدث الإصدار، قم بكتابة `pod 'AVOSCloud'` بدون رقم الإصدار.
- **التوافق**: تأكد من أن الإصدار `3.1.6.2` يدعم هدف نشر iOS الخاص بك (مثل iOS 9.0 أو أعلى). تحقق من [التوثيق الرسمي لـ LeanCloud](https://leancloud.app/docs) للحصول على التفاصيل.
- **تحديث الحزمة**: إذا كنت بحاجة إلى تحديث CocoaPods أو حل المشاكل، قم بتنفيد:
  ```bash
  pod update
  ```
- **حل المشاكل**: إذا فشل `pod install`، حاول:
  ```bash
  pod repo update
  pod install --verbose
  ```

---

أعلمني إذا كنت تحتاج إلى مساعدة في جزء معين، مثل دمج ميزة (مثل الإشعارات الدفعية، الرسائل في الوقت الحقيقي) من AVOSCloud!