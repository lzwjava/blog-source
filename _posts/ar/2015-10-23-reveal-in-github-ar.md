---
audio: false
generated: false
lang: ar
layout: post
title: 'أداة إكسكود: كشف في جت هوب'
translated: true
---

هذا هو README.md من مشروع GitHub [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub).

---

# Reveal-In-GitHub

منبر اكسكود مصمم لتحسين التنقل السلس إلى الوظائف الرئيسية لموقع GitHub داخل مستودعك الحالي. بالضغط على زر واحد، يمكنك الوصول بسهولة إلى سجلات GitHub، التهمية، طلبات سحب، المسائل، والإشعارات، وكل ذلك في غضون ثوان.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

شركة العمل هنا تعمل على GitHub. افتتاح موقع GitHub كثيرا. أحيانا، أنا أحرر في Xcode ولا أفهم بعض الكود، فإذا ذهبت إلى GitHub للتفريق. وأحيانًا، العثور على الإلتقاطات أحدث عن ملف ما لمساعدتي في فهم كيفية تطور الكود. لذلك سأسأل هل هناك أداة تساعدني في فتح GitHub من Xcode بسرعة. كتبت هذا المنبر. أثناء تحرير بعض ملفات المصدر في Xcode، على السهولة معرفة أي مستودع GitHub أنت تعمل عليه وأيّ ملف أنت تحريره. لذلك، من المنطقي الانتقال إلى الملف على GitHub بسرعة، الانتقال إلى التهمية لسلسلات الكود الحالية على GitHub بسرعة، الانتقال إلى المسائل أو طلبات سحب للمستودع الحالي الذي تعمل عليه في Xcode بسرعة.

## عناصر القائمة

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

يحتوي على ستة عناصر القائمة:

 Menu Title     | Shortcut              | GitHub URL Pattern (عندما كنت أدخل LZAlbumManager.m السطر 40)                |
----------------|-----------------------|----------------------------------

 Setting	    |⌃⇧⌘S |
 Repo           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Quick File     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 List History   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

الاختصارات مصممة بعناية. لن تكون في تناقض مع اختصارات Xcode الافتراضية. نضارة الإختصارات هي ⌃⇧⌘ (Ctrl+Shift+Command)، بالإضافة إلى أول حرف من عنوان القائمة.

## تعديل

أحيانًا، قد ترغب في الانتقال بسرعة إلى Wiki. هذا هو الطريق، افتح الإعداد:

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

على سبيل المثال،

مفتاح السريع، النموذج والحلقة الفعلي:

```plaintext
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} هو تسلسل التجميع الأخير للمفرع الحالي. يكون أكثر من استخدام الفروع. لأنه قد تغير رأس الفرع. لذلك قد تغير الكود في #L40-L43 أيضًا.

إذا كنت تريد إضافة اختصار إلى Wiki للمستودع الحالي، فقط أضف عنصر قائمة ووضع النموذج إلى `{git_remote_url}/wiki`.

في الإعدادات، "Clear Default Repos" إذا كان لديك عدة مستودعات Git. عند التفعيل لأول مرة، سيطلب منك اختيار واحد منهم:

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

ثم يغسل المنبر ما اخترته. لذلك، عندما تفعّل القائمة مرة أخرى، ستفتح تلك المستودع البعيدة كإعداد افتراضي. زر "Clear Default Repos" سيضيء هذا الإعداد وسيطلب منك اختيار مرة أخرى.

## التثبيت

يوصى بالتثبيت مع [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

أو

1. استنساخ هذا المستودع.
2. افتح `Reveal-In-GitHub.xcodeproj`، وابنيه.
3. يجب أن يكون `Reveal-In-GitHub.xcplugin` في `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. اعادة تشغيل Xcode
5. افتح أي مشروع GitHub واضغط على ⌃⇧⌘B (Ctrl+Shift+Command+B) لتهمية الكود.

## التثبيت

نوصي باستخدام [Alcatraz](http://alcatraz.io/)، يمكنك الاستعارة من [مقالات](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/). بعد التثبيت، تبعا للصور أعلاه، ابحث عن `Reveal In GitHub` واضغط على زر `Install`.

إذا لم تستخدم هذه الأداة، فكلا أحد هذه الخطوات:

* استنساخ هذا المشروع إلى جهازك المحلي.
* افتح xcodeproj، واضغط على Build لابناء. هذا سيخلق ملف `Reveal-In-GitHub.xcplugin` في الدليل `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`.
* اعادة تشغيل Xcode، افتح أي مستودع GitHub. اضغط على `Ctrl+Shift+Command+B` لتهمية الكود.

## الاعتراف

عند تطويره، وجدت منبر آخر [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) يفعل شيئا متشابه. تعلمت منه بعض التقنيات. شكرًا لذلك.

## الرخصة

MIT