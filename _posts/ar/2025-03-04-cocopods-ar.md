---
audio: false
generated: true
lang: ar
layout: post
title: إدارة التبعيات باستخدام CocoaPods في مشاريع iOS
translated: true
type: note
---

لنبدأ في استخدام CocoaPods، وإنشاء Podfile، وإدارة المكتبات، وبعض التوصيات الشائعة للبود! سأقوم بتفصيل هذا خطوة بخطوة لجعله واضحًا وقابلًا للتنفيذ.

### ما هي CocoaPods و Podfile؟
CocoaPods هو مدير تبعيات لمشاريع Swift و Objective-C، ويُستخدم على نطاق واسع في تطوير تطبيقات iOS/macOS. فهو يبسط عملية إضافة المكتبات (المسماة "pods") إلى مشروعك. `Podfile` هو ملف تكوين تحدد فيه البودات التي يحتاجها مشروعك، وإصداراتها، وكيفية تكاملها مع أهدافك (targets).

### كيفية استخدام CocoaPods وإنشاء Podfile
1. **تثبيت CocoaPods** (إذا لم تكن قد قمت بذلك بالفعل):
   - افتح Terminal وقم بتشغيل:
     ```bash
     sudo gem install cocoapods
     ```
   - تحقق من التثبيت:
     ```bash
     pod --version
     ```

2. **إعداد Podfile**:
   - انتقل إلى دليل مشروع Xcode الخاص بك في Terminal:
     ```bash
     cd /path/to/your/project
     ```
   - أنشئ Podfile:
     ```bash
     pod init
     ```
   - يولد هذا `Podfile` أساسيًا في مجلد مشروعك.

3. **تحرير الـ Podfile**:
   - افتح `Podfile` في محرر نصوص (مثل `open Podfile`). يبدو Podfile الأساسي كالتالي:
     ```ruby
     platform :ios, '13.0'  # حدد الحد الأدنى لإصدار iOS
     use_frameworks!        # استخدم الأطر الديناميكية بدلاً من المكتبات الثابتة

     target 'YourAppName' do
       # توضع البودات هنا
       pod 'Alamofire', '~> 5.6'  # بود مثال
     end

     post_install do |installer|
       installer.pods_project.targets.each do |target|
         target.build_configurations.each do |config|
           config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
         end
       end
     end
     ```
   - استبدل `'YourAppName'` باسم الهدف (target) في Xcode الخاص بك.
   - أضف البودات تحت كتلة `target` (المزيد عن البودات الشائعة لاحقًا).

4. **تثبيت البودات**:
   - في Terminal، قم بتشغيل:
     ```bash
     pod install
     ```
   - يقوم هذا بتنزيل البودات المحددة وإنشاء ملف `.xcworkspace`. من الآن فصاعدًا، افتح مساحة العمل (workspace) هذه (وليس ملف `.xcodeproj`) في Xcode.

5. **استخدام البودات في الكود الخاص بك**:
   - قم باستيراد البود في ملف Swift الخاص بك:
     ```swift
     import Alamofire  // مثال لبود Alamofire
     ```
   - استخدم المكتبة كما هو موثق في ملف README الخاص بها (عادةً ما يوجد على GitHub أو صفحة البود على CocoaPods).

---

### استخدام المكتبات (البودات) ومفاهيم Podfile الرئيسية
- **تحديد البودات**:
  - أضف بودًا بشرط إصدار:
    ```ruby
    pod 'Alamofire', '~> 5.6'  # ~> تعني "حتى الإصدار الرئيسي التالي"
    pod 'SwiftyJSON'           # لم يتم تحديد إصدار = الأحدث
    ```
- **أهداف متعددة**:
  - إذا كان لمشروعك أهداف متعددة (مثل التطبيق والامتداد):
    ```ruby
    target 'YourAppName' do
      pod 'Alamofire'
    end

    target 'YourAppExtension' do
      pod 'SwiftyJSON'
    end
    ```
- **متغيرات البيئة (مثل `COCOAPODS_DISABLE_STATS`)**:
  - ترسل CocoaPods إحصائيات مجهولة المصدر افتراضيًا. لتعطيل ذلك:
    ```bash
    export COCOAPODS_DISABLE_STATS=1
    pod install
    ```
  - أضف هذا إلى ملف `~/.zshrc` أو `~/.bashrc` لجعله دائمًا.
- **كبت التحذيرات**:
  - لكتم تحذيرات البود:
    ```ruby
    inhibit_all_warnings!
    ```

---

### بودات شائعة موصى بها
إليك بعض البودات المستخدمة على نطاق واسع في تطوير تطبيقات iOS، بناءً على فائدتها واعتماد المجتمع لها:

1. **Alamofire**:
   - الاستخدام: الشبكات (جعل طلبات HTTP سهلة).
   - Podfile: `pod 'Alamofire', '~> 5.6'`
   - السبب: يبطل طلبات URL، ومعالجة JSON، والمزيد.

2. **SwiftyJSON**:
   - الاستخدام: تحليل JSON.
   - Podfile: `pod 'SwiftyJSON'`
   - السبب: يجعل التعامل مع JSON أكثر أمانًا ونظافة من القواميس الأصلية في Swift.

3. **SnapKit**:
   - الاستخدام: Auto Layout مع بناء جملة أبسط.
   - Podfile: `pod 'SnapKit'`
   - السبب: رائع لواجهة المستخدم البرمجية بدون تعقيدات الـ storyboard.

4. **Kingfisher**:
   - الاستخدام: تنزيل الصور والتخزين المؤقت.
   - Podfile: `pod 'Kingfisher'`
   - السبب: مثالي لتحميل الصور في UIImageViews بكفاءة.

5. **RealmSwift**:
   - الاستخدام: تخزين قاعدة البيانات المحلية.
   - Podfile: `pod 'RealmSwift'`
   - السبب: أسرع وأكثر بديهية من Core Data في العديد من حالات الاستخدام.

6. **Firebase** (موديولار):
   - الاستخدام: خدمات الخلفية (التحليلات، إشعارات الدفع، إلخ).
   - مثال Podfile:
     ```ruby
     pod 'Firebase/Analytics'
     pod 'Firebase/Messaging'
     ```
   - السبب: مجموعة شاملة لتحليلات التطبيقات والمشاركة.

7. **Lottie**:
   - الاستخدام: الرسومات المتحركة.
   - Podfile: `pod 'lottie-ios'`
   - السبب: أضف بسهولة رسوميات متحركة عالية الجودة من Adobe After Effects.

---

### نصائح لاستكشاف الأخطاء وإصلاحها
- **فشل تثبيت البود**: قم بتشغيل `pod repo update` ثم `pod install` مرة أخرى.
- **تعارضات الإصدار**: حدد الإصدارات الدقيقة (مثل `pod 'Alamofire', '5.6.4'`) أو استخدم `pod update`.
- **بناء نظيف**: بعد تثبيت البودات، نظف مشروعك في Xcode (`Cmd + Shift + K`).

---

### مثال على Podfile يحتوي على بودات شائعة
إليك مثالًا عمليًا يجمع بعض ما ورد أعلاه:
```ruby
platform :ios, '13.0'
use_frameworks!

target 'MyAwesomeApp' do
  pod 'Alamofire', '~> 5.6'      # الشبكات
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

قم بتشغيل `pod install`، وافتح `.xcworkspace`، وأنت جاهز للبرمجة!

---

أعلمني إذا كنت تريد تعمقًا أكبر في أي بود أو خطوة محددة! أي نوع من التطبيقات تبني؟ قد يساعدني هذا في تخصيص المزيد من التوصيات.