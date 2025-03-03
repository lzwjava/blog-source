---
audio: false
generated: true
lang: ar
layout: post
title: LeanCloud Realtime iOS SDK
translated: true
---

لاستخدام `pod 'AVOSCloudIM', '3.1.6.2'` في مشروع iOS الخاص بك باستخدام CocoaPods، اتبع هذه الخطوات. يُفترض أن لديك CocoaPods مثبتًا وأنك تعرف كيفية تطوير iOS الأساسي باستخدام Xcode.

---

### الخطوة 1: إعداد CocoaPods (إذا لم يتم ذلك بالفعل)
إذا لم تقم بتثبيت CocoaPods حتى الآن، قم بتثبيته من خلال المصفوفة:
```bash
sudo gem install cocoapods
```
تحقق من التثبيت:
```bash
pod --version
```

---

### الخطوة 2: إنشاء أو فتح مشروع Xcode الخاص بك
1. افتح مشروع Xcode الحالي أو قم بإنشاء مشروع جديد في Xcode.
2. أغلق Xcode مؤقتًا (سنفتحه لاحقًا مع مساحة العمل).

---

### الخطوة 3: تهيئة ملف Podfile
1. افتح المصفوفة وقلب إلى دليل المشروع الرئيسي (حيث يوجد ملف `.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```
2. إذا لم يكن لديك ملف Podfile، قم بإنشائه من خلال تشغيل:
   ```bash
   pod init
   ```
   هذا يخلق ملف `Podfile` أساسي في دليل المشروع.

---

### الخطوة 4: تحرير ملف Podfile
1. افتح ملف `Podfile` في محرر النصوص (مثل `nano`, `vim`, أو أي محرر كود مثل VS Code):
   ```bash
   open Podfile
   ```
2. قم بتعديل ملف `Podfile` لإدراج حزمة `AVOSCloudIM` مع الإصدار `3.1.6.2`. إليك مثال على ما قد يكون ملف `Podfile`:
   ```ruby
   platform :ios, '9.0'  # تحديد الإصدار الأدنى من iOS (قم بتعديله حسب الحاجة)
   use_frameworks!       # اختياري: استخدم هذا إذا كان مشروعك يستخدم Swift أو الحزم

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # أضف هذا السطر لإدراج AVOSCloudIM الإصدار 3.1.6.2
   end
   ```
   - استبدل `'YourAppName'` باسم الهدف الفعلي في Xcode (عادةً اسم التطبيق).
   - السطر `platform :ios, '9.0'` يحدد الإصدار الأدنى من iOS؛ قم بتعديله بناءً على متطلبات مشروعك.
   - `use_frameworks!` مطلوب إذا كان مشروعك يستخدم Swift أو إذا تتطلب الحزمة حزمًا ديناميكيًا.

3. احفظ واغلق ملف `Podfile`.

---

### الخطوة 5: تثبيت الحزمة
1. في المصفوفة، قم بتشغيل الأمر التالي من دليل المشروع الرئيسي:
   ```bash
   pod install
   ```
   - هذا ينزيل ويدمج مكتبة `AVOSCloudIM` (الإصدار 3.1.6.2) في مشروعك.
   - إذا كان النجاح، ستشاهد إخراجًا مثل:
     ```
     تم تثبيت الحزمة! هناك X اعتمادًا من ملف Podfile وX حزمًا مجتمعة.
     ```

2. إذا واجهت أخطاء (مثل عدم العثور على الحزمة)، تأكد من أن الإصدار `3.1.6.2` ما زال متاحًا في مستودع CocoaPods. قد لا يتم دعم الإصدارات القديمة anymore. يمكنك التحقق من الإصدار الأخير على [CocoaPods.org](https://cocoapods.org) تحت `AVOSCloudIM` أو تحديث إلى إصدار أحدث (مثل `pod 'AVOSCloudIM', '~> 12.3'`).

---

### الخطوة 6: فتح ملف العمل
1. بعد التثبيت، سيتم إنشاء ملف `.xcworkspace` في دليل المشروع (مثل `YourAppName.xcworkspace`).
2. افتح هذا الملف في Xcode:
   ```bash
   open YourAppName.xcworkspace
   ```
   - من الآن فصاعدًا، استخدم دائمًا ملف `.xcworkspace` بدلاً من ملف `.xcodeproj` للعمل مع مشروعك.

---

### الخطوة 7: استيراد واستخدام AVOSCloudIM في كودك
1. في ملفات Swift أو Objective-C، استورد حزمة `AVOSCloudIM`:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. ابدأ باستخدام ميزات المكتبة. `AVOSCloudIM` جزء من SDK LeanCloud، يستخدم عادةً للرسائل الفورية. استعرض [التوثيق الرسمي لـ LeanCloud](https://leancloud.app/docs/) للحصول على أمثلة استخدام محددة، مثل إعداد عميل الدردشة:
   - مثال (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### الخطوة 8: إعداد مشروعك (إذا لزم الأمر)
- **مفتاح التطبيق والتهيئة**: غالبًا ما تتطلب SDK LeanCloud معرف التطبيق و المفتاح. أضف هذا الكود التهيئي (مثلًا في `AppDelegate`):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - استبدل `"yourAppID"` و `"yourAppKey"` بالبيانات من حساب LeanCloud الخاص بك.
- **الأذونات**: تأكد من أن تطبيقك لديه الأذونات اللازمة (مثل الوصول إلى الإنترنت) في `Info.plist`:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### ملاحظات
- **التحديد الإصدار**: استخدام `pod 'AVOSCloudIM', '3.1.6.2'` يقيّدك إلى هذا الإصدار بالضبط. إذا كنت تريد مرونة للتحديثات الصغيرة، استخدم `~>` (مثل `pod 'AVOSCloudIM', '~> 3.1.6'` يسمح بتحديثات مثل 3.1.6.1 ولكن ليس 3.2).
- **إصلاح الأخطاء**: إذا فشل `pod install`، حاول:
  - تحديث CocoaPods: `sudo gem install cocoapods`
  - تنظيف المخزن المؤقت: `pod cache clean --all`
  - تشغيل `pod repo update` لتحديث مستودع CocoaPods المحلي.
- **SDK LeanCloud**: نظرًا لأن `AVOSCloudIM` جزء من LeanCloud، تأكد من اتباع دليلهم التهيئي للحصول على إعدادات إضافية (مثل التسجيل على منصتهم).

---

هذا هو كل شيء! الآن قمت بتكامل `AVOSCloudIM` الإصدار 3.1.6.2 في مشروع iOS الخاص بك. قم ببناء وتشغيل تطبيقك في Xcode للاختبار. اتصل بي إذا كنت تحتاج إلى مساعدة في ميزات LeanCloud محددة!