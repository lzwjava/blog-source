---
audio: false
generated: true
lang: ar
layout: post
title: استخدام JSBadgeView في iOS
translated: true
---

يبدو أنك تتحدث عن دمج البود `JSBadgeView` (النسخة 1.4.1) في مشروع iOS باستخدام CocoaPods، وهو مدير اعتمادات شهير لمشاريع Swift و Objective-C. سأرشدك عبر الخطوات لاستخدام هذا البود في مشروعك.

### المتطلبات الأساسية
1. **CocoaPods مرفوع**: تأكد من أن CocoaPods مرفوع على نظامك. إذا لم يكن كذلك، قم بتثبيته من خلال تنفيذ:
   ```bash
   sudo gem install cocoapods
   ```
2. **مشروع Xcode**: يجب أن يكون لديك مشروع Xcode موجود حيث تريد إضافة `JSBadgeView`.

### الخطوات لاستخدام `pod 'JSBadgeView', '1.4.1'`

1. **الانتقال إلى مجلد المشروع**:
   افتح شريط الأوامر وقلب إلى مجلد يحتوي على مشروعك Xcode (ملف `.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```

2. **تفعيل CocoaPods (إذا لم يتم ذلك بالفعل)**:
   إذا لم يكن مشروعك يحتوي على `Podfile`، قم بإنشائه من خلال تنفيذ:
   ```bash
   pod init
   ```
   هذا يخلق `Podfile` في مجلد المشروع.

3. **تحرير Podfile**:
   افتح `Podfile` في محرر نص (مثل `nano`, `vim`, أو أي بيئة تطوير متكاملة) واضف البود `JSBadgeView` تحت هدفك. على سبيل المثال:
   ```ruby
   platform :ios, '9.0' # تحديد هدف التوزيع

   target 'YourProjectName' do
     use_frameworks! # مطلوب إذا كان مشروعك يستخدم Swift أو الإطارات
     pod 'JSBadgeView', '1.4.1'
   end
   ```
   استبدل `'YourProjectName'` باسم هدفك الحقيقي في Xcode.

4. **تثبيت البود**:
   احفظ `Podfile`، ثم قم بتنفيد الأمر التالي في شريط الأوامر لتثبيت البود:
   ```bash
   pod install
   ```
   هذا ينزيل `JSBadgeView` النسخة 1.4.1 ويضعه في مشروعك. إذا كان النجاح، ستشاهد خروجًا يشير إلى أن البودات تم تثبيتها.

5. **فتح مساحة العمل**:
   بعد التثبيت، يخلق CocoaPods ملف `.xcworkspace`. افتح هذا الملف (ليس `.xcodeproj`) في Xcode:
   ```bash
   open YourProjectName.xcworkspace
   ```

6. **استيراد واستخدام JSBadgeView في كودك**:
   - إذا كنت تستخدم **Objective-C**، قم باستيراد الرأس في ملفك:
     ```objective-c
     #import <JSBadgeView/JSBadgeView.h>
     ```
   - إذا كنت تستخدم **Swift**، فلا حاجة إلى استيراد إذا كان `use_frameworks!` في `Podfile`. استخدم الفئة مباشرة.
   - مثال الاستخدام (Objective-C):
     ```objective-c
     JSBadgeView *badgeView = [[JSBadgeView alloc] initWithParentView:someView alignment:JSBadgeViewAlignmentTopRight];
     badgeView.badgeText = @"5"; // تعيين نص الشارة إلى "5"
     ```
   - مثال الاستخدام (Swift):
     ```swift
     let badgeView = JSBadgeView(parentView: someView, alignment: .topRight)
     badgeView.badgeText = "5"
     ```

7. **بناء و تشغيل**:
   قم ببناء مشروعك في Xcode (`Cmd + B`) لضمان أن كل شيء تم إعداده بشكل صحيح، ثم قم بتشغيله على محاكي أو جهاز.

### الملاحظات
- **JSBadgeView**: هذه مكتبة لإضافة شارات العرض (مثل فقاعات الإشعارات) إلى عناصر الواجهة مثل الأزرار أو شريط التبويب. تحقق من [صفحته على GitHub](https://github.com/JaviSoto/JSBadgeView) للحصول على وثائق تفصيلية، على الرغم من أن النسخة 1.4.1 من عام 2016 قد لا تدعم أحدث ميزات iOS.
- **إصلاح الأخطاء**:
  - إذا فشل `pod install`، تأكد من أن نسخة CocoaPods لديك هي أحدث:
    ```bash
    pod update
    ```
  - إذا حصلت على أخطاء تتعلق بالتوافق، تأكد من أن `platform :ios` تطابق هدف توزيع مشروعك.
- **النسخة 1.4.1**: هذا يحدد البود إلى هذه النسخة المحددة. إذا كنت تريد أحدث نسخة، اكترث عن رقم الإصدار: `pod 'JSBadgeView'`.

أعلمني إذا كنت تحتاج إلى مساعدة في تفاصيل التنفيذ الخاصة أو واجهت مشاكل!