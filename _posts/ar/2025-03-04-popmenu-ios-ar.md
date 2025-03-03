---
audio: false
generated: true
lang: ar
layout: post
title: استخدام PopMenu في iOS
translated: true
---

لاستخدام `pod 'PopMenu', '2.4'` في مشروع iOS الخاص بك، أنت تدمج مكتبة PopMenu (النسخة 2.4) عبر CocoaPods، مدير الاعتماد الشائع لـ iOS. توفر هذه المكتبة قائمة انيميشن متطايره مستوحاة من تطبيقات مثل Sina Weibo أو NetEase. أدناه خطوات التثبيت واستخدامها في مشروعك:

---

### الخطوة 1: تثبيت CocoaPods (إذا لم يكن مثبتًا بالفعل)
إذا لم يكن CocoaPods مثبتًا على نظامك، قم بتثبيته أولاً:
1. افتح محرر الأوامر.
2. قم بتشغيل الأمر التالي:
   ```bash
   sudo gem install cocoapods
   ```
3. التحقق من التثبيت:
   ```bash
   pod --version
   ```

---

### الخطوة 2: إعداد ملف Podfile
1. انتقل إلى مجلد مشروع Xcode الخاص بك في المحرر:
   ```bash
   cd /path/to/your/project
   ```
2. إذا لم يكن لديك ملف Podfile، قم بإنشائه من خلال تشغيل:
   ```bash
   pod init
   ```
3. افتح ملف `Podfile` في محرر النصوص (مثل `nano Podfile` أو استخدام Xcode).
4. أضف السطور التالية لتحديد Pod PopMenu لمشروعك:
   ```ruby
   platform :ios, '8.0'  # قم بتعديل إصدار iOS إذا لزم الأمر
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - استبدل `YourAppName` باسم الهدف الخاص بك في Xcode.
   - السطر `use_frameworks!` مطلوب لأن PopMenu هو مكتبة مبنية على إطار.

5. احفظ واغلق ملف Podfile.

---

### الخطوة 3: تثبيت Pod
1. في المحرر، قم بتشغيل:
   ```bash
   pod install
   ```
2. هذا ينزيل ويدمج PopMenu الإصدار 2.4 في مشروعك. انتظر حتى ترى رسالة مثل:
   ```
   تم تثبيت Pod! هناك X اعتماد من Podfile وX Pods مجتمعة.
   ```
3. أغلق مشروع Xcode إذا كان مفتوحًا، ثم افتح الملف الجديد الذي تم إنشاؤه `.xcworkspace` (مثل `YourAppName.xcworkspace`) بدلاً من الملف `.xcodeproj`.

---

### الخطوة 4: الاستخدام الأساسي في كودك
PopMenu مكتوب بلغة Objective-C، لذا عليك استخدامه بشكل مناسب. أدناه مثال على كيفية تنفيذها في تطبيقك:

1. **استيراد المكتبة**:
   - في ملف Objective-C الخاص بك (مثل `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - إذا كنت تستخدم Swift، قم بإنشاء رأس جسر:
     - انتقل إلى `File > New > File > Header File` (مثل `YourAppName-Bridging-Header.h`).
     - أضف:
       ```objective-c
       #import "PopMenu.h"
       ```
     - في Xcode، قم بتعيين رأس الجسر تحت `Build Settings > Swift Compiler - General > Objective-C Bridging Header` إلى مسار ملف رأسك (مثل `YourAppName/YourAppName-Bridging-Header.h`).

2. **إنشاء عناصر القائمة**:
   حدد العناصر التي تريدها في القائمة المتطايره. يمكن لكل عنصر أن يكون له عنوان، أيقونة، ولون إشعاع.
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];

   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr"
                                               iconName:@"post_type_bubble_flickr"
                                              glowColor:[UIColor grayColor]
                                                  index:0];
   [items addObject:menuItem1];

   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter"
                                               iconName:@"post_type_bubble_twitter"
                                              glowColor:[UIColor blueColor]
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **التنشيط والتعرض للقائمة**:
   قم بإنشاء مثيل `PopMenu` وعرضه في عرضك.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // الخيارات: kPopMenuAnimationTypeSina أو kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // عدد العناصر في كل صف
   [popMenu showMenuAtView:self.view];
   ```

4. **معالجة الاختيار (اختياري)**:
   يمكنك توسيع الوظائف أو فرزها لتحديد النقرات، ولكن PopMenu (النسخة الأساسية 2.4) قد لا يدعم وكيلًا بشكل أساسي. تحقق من وثائق المكتبة على GitHub (`xhzengAIB/PopMenu`) لأي تحديثات أو تعديلات.

---

### الخطوة 5: تشغيل مشروعك
بني واسق مشروعك (`Cmd + R`) في Xcode. إذا كانت الأيقونات (مثل `post_type_bubble_flickr`) جزء من مجلد الموارد الخاص بك، تأكد من إضافتها إلى مشروعك. وإلا، عليك الحصول عليها أو إنشائها.

---

### الملاحظات
- **التحديد بالنسخة**: `pod 'PopMenu', '2.4'` يحددك إلى الإصدار 2.4. إذا كنت تريد أحدث إصدار، استخدم `pod 'PopMenu'` بدون رقم الإصدار، ولكن هذا قد يجلب تغييرات تدميرية.
- **التوافق**: تأكد من أن هدف نشر مشروعك على الأقل iOS 8.0 (أو قم بتعديل `platform` في Podfile).
- **التخصيص**: تسمح PopMenu بتعديلات في نوع الأنيميشن والتخطيط (مثل `perRowItemCount`). استكشف الكود المصدر للحصول على مزيد من الخيارات.
- **إصلاح الأخطاء**: إذا واجهت أخطاء مثل "الملف غير موجود"، تأكد من أن Pods مثبتة بشكل صحيح وأن ملف العمل قيد الاستخدام.

هذا يجب أن يبدأك مع PopMenu 2.4 في تطبيق iOS الخاص بك! اتصل بي إذا كنت تحتاج إلى مزيد من التوضيح.