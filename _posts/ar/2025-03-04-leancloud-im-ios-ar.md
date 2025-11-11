---
audio: false
generated: true
lang: ar
layout: post
title: إس دي كي آي أو إس لنظام لين كلاود في الوقت الفعلي
translated: true
type: note
---

لاستخدام `pod 'AVOSCloudIM', '3.1.6.2'` في مشروع iOS الخاص بك مع CocoaPods، اتبع هذه الخطوات. يفترض هذا أنك قمت بتثبيت CocoaPods وأنك على دراية بتطوير iOS الأساسي باستخدام Xcode.

---

### الخطوة 1: إعداد CocoaPods (إذا لم يكن مثبتًا مسبقًا)
إذا لم تكن قد قمت بتثبيت CocoaPods بعد، قم بتثبيته عبر الطرفية:
```bash
sudo gem install cocoapods
```
تحقق من التثبيت:
```bash
pod --version
```

---

### الخطوة 2: إنشاء أو فتح مشروع Xcode الخاص بك
1. افتح مشروع Xcode الحالي أو أنشئ مشروعًا جديدًا في Xcode.
2. أغلق Xcode الآن (سنعيد فتحه لاحقًا باستخدام مساحة العمل workspace).

---

### الخطوة 3: تهيئة ملف Podfile
1. افتح الطرفية وانتقل إلى الدليل الجذري لمشروعك (حيث يوجد ملف `.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```
2. إذا لم يكن لديك ملف Podfile بالفعل، قم بإنشائه عن طريق تشغيل:
   ```bash
   pod init
   ```
   يولد هذا ملف `Podfile` أساسي في دليل مشروعك.

---

### الخطوة 4: تعديل ملف Podfile
1. افتح ملف `Podfile` في محرر نصوص (مثل `nano`، `vim`، أو أي محرر أكواد مثل VS Code):
   ```bash
   open Podfile
   ```
2. قم بتعديل `Podfile` لتضمين الـ pod `AVOSCloudIM` مع الإصدار `3.1.6.2`. إليك مثالًا على كيف قد يبدو `Podfile` الخاص بك:
   ```ruby
   platform :ios, '9.0'  # حدد الحد الأدنى لإصدار iOS (قم بتعديله حسب الحاجة)
   use_frameworks!       # اختياري: استخدم هذا إذا كان مشروعك يستخدم Swift أو الأطر frameworks

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # أضف هذا السطر لتضمين AVOSCloudIM الإصدار 3.1.6.2
   end
   ```
   - استبدل `'YourAppName'` بالاسم الفعلي للهدف target الخاص بـ Xcode (عادةً اسم تطبيقك).
   - يحدد سطر `platform :ios, '9.0'` الحد الأدنى لإصدار iOS؛ قم بتعديله بناءً على متطلبات مشروعك.
   - `use_frameworks!` مطلوب إذا كان مشروعك يستخدم Swift أو إذا كان الـ pod يتطلب أطر ديناميكية dynamic frameworks.

3. احفظ ملف `Podfile` وأغلقه.

---

### الخطوة 5: تثبيت الـ Pod
1. في الطرفية، قم بتشغيل الأمر التالي من الدليل الجذري لمشروعك:
   ```bash
   pod install
   ```
   - يقوم هذا بتنزيل ودمج مكتبة `AVOSCloudIM` (الإصدار 3.1.6.2) في مشروعك.
   - إذا نجحت العملية، سترى ناتجًا مثل:  
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. إذا واجهت أخطاء (مثل عدم العثور على الـ pod)، تأكد من أن الإصدار `3.1.6.2` لا يزال متاحًا في مستودع CocoaPods. قد لا تكون الإصدارات الأقدم مدعومة بعد الآن. يمكنك التحقق من أحدث إصدار على [CocoaPods.org](https://cocoapods.org) تحت `AVOSCloudIM` أو التحديث إلى إصدار أحدث (مثال: `pod 'AVOSCloudIM', '~> 12.3'`).

---

### الخطوة 6: فتح مساحة العمل Workspace
1. بعد التثبيت، سيتم إنشاء ملف `.xcworkspace` في دليل مشروعك (مثال: `YourAppName.xcworkspace`).
2. افتح هذا الملف في Xcode:
   ```bash
   open YourAppName.xcworkspace
   ```
   - من الآن فصاعدًا، استخدم دائمًا ملف `.xcworkspace` بدلاً من ملف `.xcodeproj` للعمل على مشروعك.

---

### الخطوة 7: استيراد واستخدام AVOSCloudIM في الكود الخاص بك
1. في ملفات Swift أو Objective-C الخاصة بك، قم باستيراد وحدة `AVOSCloudIM`:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. ابدأ في استخدام ميزات المكتبة. `AVOSCloudIM` هو جزء من LeanCloud SDK، يُستخدم عادةً للرسائل الفورية. راجع [توثيق LeanCloud](https://leancloud.app/docs/) للحصول على أمثلة استخدام محددة، مثل إعداد عميل دردشة:
   - مثال (Swift):
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \\(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### الخطوة 8: تكوين مشروعك (إذا لزم الأمر)
- **مفتاح التطبيق والتهيئة**: تتطلب LeanCloud SDKs غالبًا معرف التطبيق ومفتاحًا. أضف كود التهيئة هذا (مثال: في `AppDelegate`):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - استبدل `"yourAppID"` و `"yourAppKey"` ببيانات الاعتماد من حساب LeanCloud الخاص بك.
- **الأذونات**: تأكد من أن تطبيقك لديه الأذونات اللازمة (مثل الوصول إلى الإنترنت) في ملف `Info.plist`:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### ملاحظات
- **تحديد الإصدار**: استخدام `pod 'AVOSCloudIM', '3.1.6.2'` يثبتك على هذا الإصدار المحدد بالضبط. إذا كنت تريد مرونة للتحديثات الطفيفة، استخدم `~>` (مثال: `pod 'AVOSCloudIM', '~> 3.1.6'` يسمح بتحديثات مثل 3.1.6.1 ولكن ليس 3.2).
- **استكشاف الأخطاء وإصلاحها**: إذا فشل `pod install`، جرب:
  - تحديث CocoaPods: `sudo gem install cocoapods`
  - مسح الذاكرة المؤقتة: `pod cache clean --all`
  - تشغيل `pod repo update` لتحديث مستودع مواصفات CocoaPods المحلي.
- **LeanCloud SDK**: نظرًا لأن `AVOSCloudIM` هو جزء من LeanCloud، تأكد من اتباع دليل الإعداد الخاص بهم للتكوين الإضافي (مثل التسجيل على منصتهم).

---

هذا كل شيء! لقد قمت الآن بدمج `AVOSCloudIM` الإصدار 3.1.6.2 في مشروع iOS الخاص بك. قم ببناء وتشغيل تطبيقك في Xcode لاختباره. دعني أعرف إذا كنت بحاجة إلى مساعدة في ميزات LeanCloud المحددة!