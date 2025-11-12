---
audio: false
generated: true
lang: ar
layout: post
title: استخدام AFNetworking في iOS
translated: true
type: note
---

يبدو أنك تشير إلى دمج مكتبة AFNetworking الإصدار 2.5.4 في مشروع iOS باستخدام CocoaPods، مدير التبعيات الشائع لمشاريع Swift وObjective-C. إليك دليلًا خطوة بخطوة حول كيفية استخدام `pod 'AFNetworking', '2.5.4'` في مشروعك:

### المتطلبات الأساسية
1. **تثبيت CocoaPods**: إذا لم يكن لديك CocoaPods مثبتًا، فقم بتثبيته عن طريق تشغيل هذا الأمر في الطرفية:
   ```bash
   sudo gem install cocoapods
   ```
2. **مشروع Xcode**: تأكد من أن لديك مشروع Xcode موجودًا حيث تريد إضافة AFNetworking.

### خطوات استخدام `pod 'AFNetworking', '2.5.4'`

1. **الانتقال إلى دليل مشروعك**  
   افتح الطرفية وانتقل إلى الدليل الذي يحتوي على مشروع Xcode الخاص بك (ملف `.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```

2. **تهيئة Podfile**  
   إذا لم يكن لديك `Podfile` بالفعل، فقم بإنشائه عن طريق تشغيل:
   ```bash
   pod init
   ```
   يولد هذا `Podfile` في دليل مشروعك.

3. **تحرير الـ Podfile**  
   افتح `Podfile` في محرر نصوص (مثل `nano Podfile` أو استخدم أي محرر أكواد مثل VS Code). أضف السطر التالي داخل كتلة `target` لتطبيقك:
   ```ruby
   target 'YourAppTargetName' do
     # علق على السطر التالي إذا كنت لا تريد استخدام أطر عمل ديناميكية
     use_frameworks!

     # أضف هذا السطر لتحديد إصدار AFNetworking 2.5.4
     pod 'AFNetworking', '2.5.4'
   end
   ```
   استبدل `'YourAppTargetName'` باسم الهدف الفعلي لتطبيقك (يمكنك العثور على هذا في Xcode ضمن إعدادات مشروعك).

   مثال `Podfile`:
   ```ruby
   platform :ios, '9.0'

   target 'MyApp' do
     use_frameworks!
     pod 'AFNetworking', '2.5.4'
   end
   ```

4. **تثبيت الـ Pod**  
   احفظ `Podfile`، ثم شغل الأمر التالي في الطرفية لتثبيت AFNetworking 2.5.4:
   ```bash
   pod install
   ```
   يقوم هذا بتنزيل الإصدار المحدد من AFNetworking وإعداده في مشروعك. سترى رسالة تشير إلى النجاح إذا عملت العملية.

5. **فتح مساحة العمل Workspace**  
   بعد التثبيت، ينشئ CocoaPods ملف `.xcworkspace`. افتح هذا الملف (مثل `MyApp.xcworkspace`) في Xcode بدلاً من ملف `.xcodeproj` الأصلي:
   ```bash
   open MyApp.xcworkspace
   ```

6. **استيراد واستخدام AFNetworking**  
   في كود Objective-C أو Swift الخاص بك، قم باستيراد AFNetworking وابدأ في استخدامه. نظرًا لأن الإصدار 2.5.4 أقدم ومكتوب بلغة Objective-C، فإليك كيفية استخدامه:

   - **Objective-C**:
     في ملفك `.h` أو `.m`:
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

   - **Swift (مع Bridging Header)**:  
     إذا كنت تستخدم Swift، فأنشئ bridging header لاستخدام هذه المكتبة المكتوبة بـ Objective-C:
     - أضف ملفًا باسم `YourApp-Bridging-Header.h` (مثل `MyApp-Bridging-Header.h`).
     - في الـ bridging header، أضف:
       ```objective-c
       #import <AFNetworking/AFNetworking.h>
       ```
     - في Xcode، انتقل إلى Build Settings > "Objective-C Bridging Header" وعيّن المسار إلى bridging header الخاص بك (مثل `MyApp/MyApp-Bridging-Header.h`).
     - ثم في ملف Swift الخاص بك:
       ```swift
       func makeRequest() {
           let manager = AFHTTPRequestOperationManager()
           manager.get("https://api.example.com/data", 
                       parameters: nil, 
                       success: { (operation, response) in
                           print("Success: \\(response)")
                       }, 
                       failure: { (operation, error) in
                           print("Error: \\(error)")
                       })
       }
       ```

7. **بناء وتشغيل المشروع**  
   ابنِ مشروعك في Xcode (`Cmd + B`) للتأكد من أن كل شيء تم إعداده بشكل صحيح. إذا واجهت أخطاء، فتحقق من صيغة Podfile الخاصة بك أو تأكد من فتح مساحة العمل الصحيحة.

### ملاحظات
- **الإصدار 2.5.4**: هذا إصدار أقدم من AFNetworking (تم إصداره حوالي عام 2015). أحدث إصدار اعتبارًا من مارس 2025 هو على الأرجح أحدث بكثير (مثل 4.x أو 5.x). ما لم تكن بحاجة تحديدًا إلى الإصدار 2.5.4 لأسباب التوافق، ففكر في استخدام `pod 'AFNetworking'` بدون تحديد إصدار للحصول على الأحدث.
- **إهالة API**: واجهات برمجة التطبيقات القديمة لـ AFNetworking (مثل `AFHTTPRequestOperationManager`) أصبحت مهجورة في الإصدارات الأحدث. للمشاريع الحديثة، قد تكون مكتبات مثل Alamofire (بديل Swift) تستحق الاستكشاف.
- **المنصة**: تأكد من أن `Podfile` الخاص بك يحدد إصدار منصة متوافق مع AFNetworking 2.5.4 (مثل `platform :ios, '9.0'`).

إذا واجهت مشاكل محددة (مثل أخطاء التثبيت أو أمثلة التعليمات البرمجية التي لا تعمل)، فأخبرني، وسأحاول استكشاف الأخطاء وإصلاحها بشكل أكبر! ما هي خطوتك أو سؤالك التالي؟