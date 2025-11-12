---
audio: false
generated: true
lang: ar
layout: post
title: استخدام PopMenu في iOS
translated: true
type: note
---

لاستخدام `pod 'PopMenu', '2.4'` في مشروع iOS الخاص بك، فأنت تقوم بدمج مكتبة PopMenu (الإصدار 2.4) عبر CocoaPods، وهو مدير تبعيات شائع لنظام iOS. توفر هذه المكتبة قائمة منبثقة متحركة مستوحاة من تطبيقات مثل Sina Weibo أو NetEase. فيما يلي الخطوات لإعدادها واستخدامها في مشروعك:

---

### الخطوة 1: تثبيت CocoaPods (إذا لم يكن مثبتًا مسبقًا)
إذا لم يكن لديك CocoaPods مثبتًا على نظامك، قم بتثبيته أولاً:
1. افتح الطرفية (Terminal) الخاصة بك.
2. نفّذ هذا الأمر:
   ```bash
   sudo gem install cocoapods
   ```
3. تحقق من التثبيت:
   ```bash
   pod --version
   ```

---

### الخطوة 2: إعداد ملف Podfile
1. انتقل إلى دليل مشروع Xcode الخاص بك في الطرفية:
   ```bash
   cd /path/to/your/project
   ```
2. إذا لم يكن لديك ملف Podfile مسبقًا، قم بإنشائه عن طريق تنفيذ:
   ```bash
   pod init
   ```
3. افتح ملف `Podfile` في محرر نصوص (مثل `nano Podfile` أو باستخدام Xcode).
4. أضف السطور التالية لتحديد حزمة PopMenu للهدف (target) الخاص بك:
   ```ruby
   platform :ios, '8.0'  # اضبط إصدار iOS إذا لزم الأمر
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - استبدل `YourAppName` باسم الهدف (target) الخاص بك في Xcode.
   - سطر `use_frameworks!` مطلوب لأن PopMenu هي على الأرجح مكتبة قائمة على الأطر (frameworks).

5. احفظ ملف Podfile وأغلقه.

---

### الخطوة 3: تثبيت الحزمة (Pod)
1. في الطرفية، نفّذ:
   ```bash
   pod install
   ```
2. سيؤدي هذا إلى تنزيل ودمج PopMenu الإصدار 2.4 في مشروعك. انتظر حتى تظهر رسالة مثل:
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. أغلق مشروع Xcode الخاص بك إذا كان مفتوحًا، ثم افتح ملف `.xcworkspace` الذي تم إنشاؤه حديثًا (مثل `YourAppName.xcworkspace`) بدلاً من ملف `.xcodeproj`.

---

### الخطوة 4: الاستخدام الأساسي في الكود الخاص بك
PopMenu مكتوبة بلغة Objective-C، لذا ستحتاج إلى استخدامها وفقًا لذلك. إليك مثالاً حول كيفية تنفيذها في تطبيقك:

1. **استيراد المكتبة**:
   - في ملف Objective-C الخاص بك (مثل `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - إذا كنت تستخدم Swift، قم بإنشاء جسر رأس (bridging header):
     - انتقل إلى `File > New > File > Header File` (مثل `YourAppName-Bridging-Header.h`).
     - أضف:
       ```objective-c
       #import "PopMenu.h"
       ```
     - في Xcode، عيّن جسر الرأس تحت `Build Settings > Swift Compiler - General > Objective-C Bridging Header` إلى مسار ملف الرأس الخاص بك (مثل `YourAppName/YourAppName-Bridging-Header.h`).

2. **إنشاء عناصر القائمة**:
   عرّف العناصر التي تريدها في القائمة المنبثقة. يمكن أن يحتوي كل عنصر على عنوان وأيقونة ولون توهج.
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

3. **تهيئة وعرض القائمة**:
   أنشئ نسخة من `PopMenu` واعرضها في الواجهة (view) الخاصة بك.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // الخيارات: kPopMenuAnimationTypeSina أو kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // عدد العناصر في كل صف
   [popMenu showMenuAtView:self.view];
   ```

4. **معالجة الاختيار (اختياري)**:
   يمكنك إنشاء فئة فرعية (subclass) أو توسيع الوظائف لاكتشاف النقرات، على الرغم أن الإصدار الأساسي من PopMenu (حوالي الإصدار 2.4) قد لا يدعم المفوّض (delegate) بشكل افتراضي. تحقق من وثائق المكتبة على GitHub (`xhzengAIB/PopMenu`) للحصول على أي تحديثات أو تخصيصات.

---

### الخطوة 5: تشغيل مشروعك
ابنِ وشغّل مشروعك (`Cmd + R`) في Xcode. إذا كانت الأيقونات (مثل `post_type_bubble_flickr`) جزءًا من كتالوج الأصول (asset catalog) الخاص بك، فتأكد من إضافتها إلى مشروعك. إذا لم تكن مضافة، فستحتاج إلى الحصول عليها أو إنشائها.

---

### ملاحظات
- **تحديد الإصدار**: `pod 'PopMenu', '2.4'` يثبتك عند الإصدار 2.4. إذا أردت أحدث إصدار، استخدم `pod 'PopMenu'` بدون رقم إصدار، ولكن قد يؤدي هذا إلى تغييرات غير متوافقة.
- **التوافق**: تأكد من أن الهدف (deployment target) لمشروعك هو iOS 8.0 على الأقل (أو اضبط `platform` في ملف Podfile).
- **التخصيص**: تسمح PopMenu بتعديل نوع الحركة وإعدادات التخطيط (مثل `perRowItemCount`). استكشف الكود المصدري للحصول على المزيد من الخيارات.
- **استكشاف الأخطاء وإصلاحها**: إذا واجهت أخطاء مثل "file not found"، فتأكد من تثبيت الحزم (Pods) بشكل صحيح وأنك تستخدم مساحة العمل (workspace).

هذا يجب أن يبدأ مع PopMenu 2.4 في تطبيق iOS الخاص بك! دعني أعرف إذا كنت بحاجة إلى مزيد من التوضيح.