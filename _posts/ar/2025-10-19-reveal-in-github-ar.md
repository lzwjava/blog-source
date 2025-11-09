---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: كشف في جيت هاب إضافة إكس كود
translated: true
type: note
---

### ما هو Reveal-In-GitHub؟

Reveal-In-GitHub هو مكون إضافي لـ Xcode يتيح لك الانتقال بسرعة من مساحة العمل في Xcode إلى الميزات الرئيسية في GitHub لمستودعك الحالي. إنه مصمم للمطورين الذين يعملون على مشاريع Git المستضافة على GitHub، مما يسمح بالوصول بنقرة واحدة (أو باستخدام اختصار لوحة المفاتيح) إلى أشياء مثل سجل النشرات (commit history)، وعروض المسؤولية (blame views)، وطلبات السحب (pull requests)، والمشكلات (issues)، والإشعارات (notifications) — دون مغادرة Xcode أو كتابة عناوين URL يدويًا.

### المتطلبات الأساسية
- تثبيت Xcode (تم الاختبار على الإصدارات الحديثة؛ لم يُذكر حد أدنى محدد).
- يجب أن يكون مشروعك مستودع Git مستضاف على GitHub (يكتشف المكون الإضافي عنوان URL للمستودع ومسارات الملفات تلقائيًا).
- إذا كان لمشروعك عدة مخازن بعيدة (remotes) لـ Git، سيُطلب منك تحديد واحد افتراضي عند الاستخدام الأول.

### التثبيت
هناك طريقتان رئيسيتان لتثبيته:

#### الخيار 1: استخدام Alcatraz (موصى به)
1. قم بتثبيت Alcatraz إذا لم يكن لديك بالفعل (مدير حزم لمكونات Xcode الإضافية). يمكنك العثور على أدلة إعداد عبر الإنترنت، مثل [هذا الدليل](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/) إذا كنت تفضل التعليمات باللغة الصينية.
2. افتح Alcatraz في Xcode (عبر القائمة: `Window > Package Manager`).
3. ابحث عن "Reveal In GitHub".
4. انقر على **Install**.
5. أعد تشغيل Xcode.

#### الخيار 2: التثبيت اليدوي
1. استنسخ المستودع:  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. افتح ملف `Reveal-In-GitHub.xcodeproj` في Xcode.
3. أنشئ المشروع (Product > Build أو ⌘B). يولد هذا ملف `Reveal-In-GitHub.xcplugin`.
4. انقل المكون الإضافي إلى:  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. أعد تشغيل Xcode.

بعد التثبيت، يجب أن يظهر المكون الإضافي في شريط قوائم Xcode تحت **Editor > Reveal In GitHub**.

### كيفية استخدامه
بمجرد التثبيت وإعادة تشغيل Xcode:
1. افتح مشروعًا مستضافًا على GitHub في Xcode وقم بتحرير ملف مصدري (على سبيل المثال، انتقل إلى سطر محدد).
2. استخدم أحد اختصارات لوحة المفاتيح أو عناصر القائمة الموجودة تحت **Editor > Reveal In GitHub** للانتقال إلى GitHub. يكتشف المكون الإضافي تلقائيًا مستودعك، والملف الحالي، ورقم السطر، وتجزئة النشرة (commit hash) الأحدث.

إليك مرجعًا سريعًا لعناصر القائمة المدمجة واختصاراتها (تتبع الاختصارات النمط ⌃⇧⌘ + الحرف الأول من العنوان):

| عنصر القائمة      | الاختصار    | الوظيفة | مثال على عنوان URL في GitHub (للملف LZAlbumManager.m عند السطر 40 في المستودع lzwjava/LZAlbum عند النشرة fd7224) |
|----------------|-------------|--------------|-----------------------------------------------------------------------------------------------|
| **Setting**    | ⌃⇧⌘S      | يفتح لوحة التخصيص | N/A |
| **Repo**       | ⌃⇧⌘R      | يفتح الصفحة الرئيسية للمستودع | https://github.com/lzwjava/LZAlbum |
| **Issues**     | ⌃⇧⌘I      | يفتح قائمة المشكلات | https://github.com/lzwjava/LZAlbum/issues |
| **PRs**        | ⌃⇧⌘P      | يفتح قائمة طلبات السحب | https://github.com/lzwjava/LZAlbum/pulls |
| **Quick File** | ⌃⇧⌘Q      | يفتح عرض الملف عند السطر الحالي | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **List History**| ⌃⇧⌘L     | يفتح سجل النشرات للملف | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **Blame**      | ⌃⇧⌘B      | يفتح عرض المسؤولية للسطر الحالي | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **Notifications**| ⌃⇧⌘N   | يفتح إشعارات المستودع | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **نصائح**: 
  - لا تتعارض الاختصارات مع الإعدادات الافتراضية لـ Xcode.
  - إذا كنت في نطاق نص محدد، فإن بعض الإجراءات (مثل Blame) سترتبط بهذا النطاق (على سبيل المثال، #L40-L43).
  - اختبره: افتح مشروعًا، انتقل إلى سطر، واضغط على ⌃⇧⌘B — يجب أن تفتح صفحة المسؤولية في متصفحك.

### التخصيص
لضبط أو إضافة عناصر قائمة:
1. اضغط على ⌃⇧⌘S أو انتقل إلى **Editor > Reveal In GitHub > Setting**.
2. في اللوحة:
   - أضف عناصر جديدة بالنقر على زر "+": أدخل عنوانًا (على سبيل المثال، "Wiki")، واختصارًا، ونمط عنوان URL.
   - تستخدم أنماط عناوين URL عناصر نائبة مثل:
     - `{git_remote_url}`: عنوان URL الكامل للمستودع (على سبيل المثال، https://github.com/user/repo).
     - `{commit}`: تجزئة النشرة (commit hash) الأحدث للفرع الحالي.
     - `{file_path}`: المسار النسبي للملف.
     - `#{selection}`: السطر الحالي أو التحديد (على سبيل المثال، #L40).
   - مثال: للحصول على رابط Wiki، عيّن النمط إلى `{git_remote_url}/wiki`.
3. إذا كان لديك عدة مخازن بعيدة (remotes)، استخدم زر "Clear Default Repos" لإعادة تعيين الاختيارات.

هذا المكون الإضافي مستلهم من [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) ومرخص بموجب ترخيص MIT.

[مستودع Reveal-In-GitHub على GitHub](https://github.com/lzwjava/Reveal-In-GitHub)