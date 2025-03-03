---
audio: false
generated: true
lang: ar
layout: post
title: استخدام AFNetworking في iOS
translated: true
---

يبدو أنك تتحدث عن دمج مكتبة AFNetworking الإصدار 2.5.4 في مشروع iOS باستخدام CocoaPods، وهو مدير اعتمادات شهير لمشاريع Swift و Objective-C. إليك دليل خطوة بخطوة على كيفية استخدام `pod 'AFNetworking', '2.5.4'` في مشروعك:

### المتطلبات الأساسية
1. **تثبيت CocoaPods**: إذا لم يكن لديك CocoaPods مثبتًا، قم بتثبيته من خلال تنفيذ هذا الأمر في محررك:
   ```bash
   sudo gem install cocoapods
   ```
2. **مشروع Xcode**: تأكد من وجود مشروع Xcode موجود حيث تريد إضافة AFNetworking.

### خطوات استخدام `pod 'AFNetworking', '2.5.4'`

1. **التنقل إلى مجلد المشروع**
   افتح محررك وقلب إلى مجلد يحتوي على ملف مشروعك Xcode (`.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```

2. **تأهيل ملف Podfile**
   إذا لم يكن لديك ملف `Podfile`، قم بإنشائه من خلال تنفيذ:
   ```bash
   pod init
   ```
   هذا يخلق ملف `Podfile` في مجلد المشروع.

3. **تحرير ملف Podfile**
   افتح ملف `Podfile` في محرر نصي (مثل `nano Podfile` أو استخدام أي محرر كود مثل VS Code). أضف السطر التالي داخل كتلة `target` لمشروعك:
   ```ruby
   target 'YourAppTargetName' do
     # قم بتعليق السطر التالي إذا لم ترغب في استخدام الإطارات الديناميكية
     use_frameworks!

     # أضف هذا السطر لتحديد الإصدار 2.5.4 من AFNetworking
     pod 'AFNetworking', '2.5.4'
   end
   ```
   استبدل `'YourAppTargetName'` باسم الهدف الفعلي لمشروعك (يمكنك العثور عليه في Xcode تحت إعدادات المشروع).

   مثال على `Podfile`:
   ```ruby
   platform :ios, '9.0'

   target 'MyApp' do
     use_frameworks!
     pod 'AFNetworking', '2.5.4'
   end
   ```

4. **تثبيت Pod**
   احفظ ملف `Podfile`، ثم قم بتشغيل الأمر التالي في المحرر لتثبيت AFNetworking 2.5.4:
   ```bash
   pod install
   ```
   هذا ينزِل الإصدار المحدد من AFNetworking ويضعه في مشروعك. ستشاهد رسالة تشير إلى النجاح إذا كان الأمر يعمل.

5. **فتح مساحة العمل**
   بعد التثبيت، يخلق CocoaPods ملف `.xcworkspace`. افتح هذا الملف (مثل `MyApp.xcworkspace`) في Xcode بدلاً من الملف الأصلي `.xcodeproj`:
   ```bash
   open MyApp.xcworkspace
   ```

6. **استيراد واستخدام AFNetworking**
   في كود Objective-C أو Swift، استورد AFNetworking واستخدمه. نظرًا لأن الإصدار 2.5.4 قديم ومكتبة Objective-C، إليك كيفية استخدامه:

   - **Objective-C**:
     في ملف `.h` أو `.m`:
     ```objective-c
     #import <AFNetworking/AFNetworking.h>

     - (void)makeRequest {
         AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
         [manager GET:@"https://api.example.com/data"
           parameters:nil
              success:^(AFHTTPRequestOperation *operation, id responseObject) {
                  NSLog(@"Success: %@", responseObject);
              }
              failure:^(AFHTTPRequestOperation *operation, NSError *error) {
                  NSLog(@"Error: %@", error);
              }];
     }
     ```

   - **Swift (مع رأس جسر)**:
     إذا كنت تستخدم Swift، قم بإنشاء رأس جسر لاستخدام هذه المكتبة Objective-C:
     - أضف ملفًا باسم `YourApp-Bridging-Header.h` (مثل `MyApp-Bridging-Header.h`).
     - في رأس الجسر، أضف:
       ```objective-c
       #import <AFNetworking/AFNetworking.h>
       ```
     - في Xcode، انتقل إلى إعدادات البناء > "Objective-C Bridging Header" وحدد مسار رأس الجسر (مثل `MyApp/MyApp-Bridging-Header.h`).
     - ثم في ملف Swift:
       ```swift
       func makeRequest() {
           let manager = AFHTTPRequestOperationManager()
           manager.get("https://api.example.com/data",
                       parameters: nil,
                       success: { (operation, response) in
                           print("Success: \(response)")
                       },
                       failure: { (operation, error) in
                           print("Error: \(error)")
                       })
       }
       ```

7. **بناء و تشغيل**
   قم ببناء مشروعك في Xcode (`Cmd + B`) لضمان أن كل شيء تم إعداده بشكل صحيح. إذا واجهت أخطاء، تحقق من صياغة ملف Podfile أو تأكد من فتح مساحة العمل الصحيحة.

### ملاحظات
- **الإصدار 2.5.4**: هذا إصدار قديم من AFNetworking (نشر في عام 2015). أحدث إصدار حتى مارس 2025 هو بالتأكيد أحدث (مثل 4.x أو 5.x). ما لم تحتاج إلى 2.5.4 للتوافقية، فاستخدم `pod 'AFNetworking'` بدون إصدار للحصول على أحدث إصدار.
- **الاستبدال**: APIs القديمة لـ AFNetworking (مثل `AFHTTPRequestOperationManager`) مستبدلة في الإصدارات الجديدة. لمشاريع حديثة، قد تكون مكتبات مثل Alamofire (بديل Swift) تستحق الاستكشاف.
- **المنصة**: تأكد من أن ملف `Podfile` يحدد إصدار المنصة متوافق مع AFNetworking 2.5.4 (مثل `platform :ios, '9.0'`).

إذا واجهت مشاكل محددة (مثل أخطاء التثبيت أو أمثلة الكود لا تعمل)، أخبرني وسأقوم بتشخيص المشكلة! ما هو الخطوة التالية أو السؤال؟