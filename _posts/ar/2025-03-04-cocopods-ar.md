---
audio: false
generated: true
lang: ar
layout: post
title: إدارة الاعتماديات باستخدام CocoaPods في مشاريع iOS
translated: true
---

دعونا نغوص في استخدام CocoaPods، إنشاء ملف Podfile، إدارة المكتبات، وبعض توصيات الشريحة الشائعة! سأقوم بتفصيل ذلك خطوة بخطوة لجعله واضحًا ومفعولًا.

### ما هو CocoaPods وPodfile؟
CocoaPods هو مدير الاعتمادات لمشاريع Swift وObjective-C، يستخدم على نطاق واسع في تطوير iOS/macOS. يسهل إضافة المكتبات (تسمى "pods") إلى مشروعك. `Podfile` هو ملف التكوين الذي تحدد فيه أي pods تحتاجها مشروعك، وأصداراتها، وكيفية تفاعلها مع أهدافك.

### كيفية استخدام CocoaPods وخلق Podfile
1. **تثبيت CocoaPods** (إذا لم تفعل ذلك بالفعل):
   - افتح Terminal واكتب:
     ```bash
     sudo gem install cocoapods
     ```
   - التحقق من التثبيت:
     ```bash
     pod --version
     ```

2. **إعداد Podfile**:
   - انتقل إلى مجلد مشروع Xcode في Terminal:
     ```bash
     cd /path/to/your/project
     ```
   - إنشاء Podfile:
     ```bash
     pod init
     ```
   - هذا يخلق `Podfile` أساسيًا في مجلد المشروع.

3. **تحرير Podfile**:
   - افتح `Podfile` في محرر النصوص (مثل `open Podfile`). يبدو Podfile الأساسي كالتالي:
     ```ruby
     platform :ios, '13.0'  # تحديد الإصدار الأدنى من iOS
     use_frameworks!        # استخدام الإطارات الديناميكية بدلاً من المكتبات الثابتة

     target 'YourAppName' do
       # pods هنا
       pod 'Alamofire', '~> 5.6'  # مثال على pod
     end

     post_install do |installer|
       installer.pods_project.targets.each do |target|
         target.build_configurations.each do |config|
           config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
         end
       end
     end
     ```
   - استبدل `'YourAppName'` بإسم هدف Xcode.
   - أضف pods تحت كتلة `target` (أكثر من الشريحة الشائعة لاحقًا).

4. **تثبيت pods**:
   - في Terminal، اكتب:
     ```bash
     pod install
     ```
   - هذا ينزّل pods المحددة ويخلق ملف `.xcworkspace`. من الآن فصاعدًا، افتح هذا المساحة العمل (لا `.xcodeproj`) في Xcode.

5. **استخدام pods في كودك**:
   - استورد pod في ملف Swift:
     ```swift
     import Alamofire  // مثال على Alamofire pod
     ```
   - استخدم المكتبة كما هو مستند في README (عادة ما يتم العثور عليه على GitHub أو صفحة pod CocoaPods).

---

### استخدام المكتبات (pods) ومفاهيم Podfile الرئيسية
- **تحديد pods**:
  - أضف pod مع قيود الإصدار:
    ```ruby
    pod 'Alamofire', '~> 5.6'  # ~> يعني "حتى الإصدار الرئيسي التالي"
    pod 'SwiftyJSON'           # لا يتم تحديد الإصدار = أحدث
    ```
- **أهداف متعددة**:
  - إذا كان مشروعك يحتوي على أهداف متعددة (مثل التطبيق والتمديد):
    ```ruby
    target 'YourAppName' do
      pod 'Alamofire'
    end

    target 'YourAppExtension' do
      pod 'SwiftyJSON'
    end
    ```
- **متغيرات البيئة (مثل `COCOAPODS_DISABLE_STATS`)**:
  - CocoaPods يرسل إحصائيات مجهولة الهوية بشكل افتراضي. لإلغاء التفعيل:
    ```bash
    export COCOAPODS_DISABLE_STATS=1
    pod install
    ```
  - أضف هذا إلى `~/.zshrc` أو `~/.bashrc` لجعله دائمًا.
- **إيقاف التحذيرات**:
  - لإسكات تحذيرات pods:
    ```ruby
    inhibit_all_warnings!
    ```

---

### توصيات الشريحة الشائعة
هنا بعض الشريحة الشائعة المستخدمة في تطوير iOS، بناءً على فائدتها وقبول المجتمع:

1. **Alamofire**:
   - الاستخدام: شبكات (تسهيل طلبات HTTP).
   - Podfile: `pod 'Alamofire', '~> 5.6'`
   - لماذا: يسهل طلبات URL، معالجة JSON، وما إلى ذلك.

2. **SwiftyJSON**:
   - الاستخدام: تحليل JSON.
   - Podfile: `pod 'SwiftyJSON'`
   - لماذا: يجعل العمل مع JSON أكثر أمانًا ونظافة من القوائم الأصلية في Swift.

3. **SnapKit**:
   - الاستخدام: Auto Layout مع صياغة أبسط.
   - Podfile: `pod 'SnapKit'`
   - لماذا: رائع للواجهة المستخدمية البرمجية دون تعقيد Storyboard.

4. **Kingfisher**:
   - الاستخدام: تحميل الصور والتخزين المؤقت.
   - Podfile: `pod 'Kingfisher'`
   - لماذا: مثالي لتحميل الصور في UIImageViews بشكل فعال.

5. **RealmSwift**:
   - الاستخدام: تخزين قاعدة بيانات محلية.
   - Podfile: `pod 'RealmSwift'`
   - لماذا: أسرع وأكثر فهماً من Core Data في العديد من الحالات.

6. **Firebase** (موضوعي):
   - الاستخدام: خدمات الخلفية (تحليل، إشعارات الدفع، وما إلى ذلك).
   - مثال Podfile:
     ```ruby
     pod 'Firebase/Analytics'
     pod 'Firebase/Messaging'
     ```
   - لماذا: مجموعة شاملة لتحليل التطبيق والتفاعل.

7. **Lottie**:
   - الاستخدام: الرسوم المتحركة.
   - Podfile: `pod 'lottie-ios'`
   - لماذا: إضافة رسوم متحركة عالية الجودة من Adobe After Effects بسهولة.

---

### نصائح حل المشكلات
- **فشل في تثبيت pod**: اكتب `pod repo update` ثم `pod install` مرة أخرى.
- **تعارض الأصدارات**: تحديد الأصدارات الدقيقة (مثل `pod 'Alamofire', '5.6.4'`) أو استخدام `pod update`.
- **بناء نظيف**: بعد تثبيت pods، قم بتنظيف مشروعك في Xcode (`Cmd + Shift + K`).

---

### مثال Podfile مع الشريحة الشائعة
هنا مثال عملي يجمع بعض من ما سبق:
```ruby
platform :ios, '13.0'
use_frameworks!

target 'MyAwesomeApp' do
  pod 'Alamofire', '~> 5.6'      # شبكات
  pod 'SwiftyJSON'               # تحليل JSON
  pod 'SnapKit'                  # Auto Layout
  pod 'Kingfisher'               # تحميل الصور

  post_install do |installer|
    installer.pods_project.targets.each do |target|
      target.build_configurations.each do |config|
        config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
      end
    end
  end
end
```

اكتب `pod install`، افتح `.xcworkspace`، وأنت مستعد للبرمجة!

---

أعلمني إذا كنت تريد غوصًا أعمق في أي pod أو خطوة معينة! ما نوع التطبيق الذي تقوم ببنائه؟ ذلك يمكن أن يساعدني في تقديم توصيات أكثر تحديدًا.