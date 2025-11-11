---
audio: false
generated: true
lang: ar
layout: post
title: إعداد BeyondCompare مع Git Difftool
translated: true
type: note
---

لإعداد Beyond Compare كأداة `git difftool`، اتبع الخطوات التالية. تفترض هذه التعليمات أنك قمت بتثبيت Beyond Compare وتكوين Git على نظامك.

### خطوات تكوين Beyond Compare كأداة `git difftool`

1. **التحقق من تثبيت Beyond Compare**
   تأكد من تثبيت Beyond Compare وإمكانية الوصول إليه من سطر الأوامر. يمكنك التحقق من ذلك عن طريق تشغيل:
   ```
   bcomp
   ```
   إذا لم يتم التعرف على الأمر، فتأكد من أن الملف التنفيذي لـ Beyond Compare (مثل `BCompare.exe` على Windows أو `bcomp` على macOS/Linux) موجود في مسار النظام PATH.

2. **تكوين Git لاستخدام Beyond Compare**
   قم بتشغيل أوامر تكوين Git التالية في طرفيتك أو موجه الأوامر:

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "path/to/bcomp"
   git config --global difftool.prompt false
   ```

   - استبدل `"path/to/bcomp"` بالمسار الفعلي للملف التنفيذي لـ Beyond Compare:
     - **Windows**: عادةً ما يكون `"C:\Program Files\Beyond Compare 4\BCompare.exe"`. استخدم شرطات مائلة مزدوجة (`\\`) أو شرطات مائلة للأمام (`/`) في المسار.
     - **macOS**: عادةً `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`.
     - **Linux**: غالبًا `/usr/bin/bcomp` أو حيثما تم تثبيت `bcomp`.
   - يمنع الإعداد `difftool.prompt false` Git من مطالبتك بتشغيل أداة المقارنة لكل ملف.

3. **(اختياري) التكوين كأداة دمج**
   إذا كنت تريد أيضًا استخدام Beyond Compare كأداة `mergetool`، فأضف هذه الأوامر:

   ```bash
   git config --global merge.tool bc
   git config --global mergetool.bc.path "path/to/bcomp"
   git config --global mergetool.prompt false
   ```

4. **اختبار التكوين**
   للتحقق من الإعداد، أنشئ أو انتقل إلى مستودع Git به تغييرات وقم بتشغيل:

   ```bash
   git difftool
   ```

   يجب أن يؤدي هذا إلى تشغيل Beyond Compare لعرض الاختلافات بين الملفات المعدلة الخاصة بك وآخر commit. إذا كنت تستخدمه كأداة دمج، فاختبر باستخدام:

   ```bash
   git mergetool
   ```

   (ينطبق هذا فقط إذا كان لديك تعارضات دمج.)

5. **ملاحظات خاصة بالمنصات**
   - **Windows**: تأكد من استخدام المسار الصحيح لـ `BCompare.exe`. إذا كان المسار يحتوي على مسافات، فضع المسار بين علامتي اقتباس.
   - **macOS/Linux**: غالبًا ما يحتاج أمر `bcomp` إلى الانتظار حتى يُغلق Beyond Compare قبل إعادة السيطرة إلى الطرفية. تشير وثائق Beyond Compare إلى أنها تتعامل مع هذا تلقائيًا، ولكن إذا خرج Git مبكرًا، فقد تحتاج إلى ضبط البرامج النصية أو استخدام برنامج غلاف (راجع دعم Beyond Compare للحصول على التفاصيل).
   - إذا واجهت مشاكل، فتحقق من المسار وتأكد من أن Beyond Compare مرخص ويعمل.

6. **مثال للتكوين على Windows**
   بالنسبة لـ Beyond Compare 4 على Windows، قد تبدو الأوامر كما يلي:

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global difftool.prompt false
   git config --global merge.tool bc
   git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global mergetool.prompt false
   ```

7. **التحقق من التكوين**
   تحقق من تكوين Git الخاص بك للتأكد من تطبيق الإعدادات:

   ```bash
   git config --global --list
   ```

   ابحث عن إدخالات مثل `diff.tool=bc` و `difftool.bc.path`.

### نصائح إضافية
- **مقارنة ملفات محددة**: استخدم `git difftool <file>` لمقارنة ملف معين.
- **مقارنة الفروع**: استخدم `git difftool branch1 branch2` لمقارنة الاختلافات بين فرعين.
- **إعدادات Beyond Compare**: في Beyond Compare، يمكنك تخصيص قواعد المقارنة (مثل تجاهل المسافات البيضاء) عبر واجهته للحصول على عرض مرئي أفضل للاختلافات.
- **استكشاف الأخطاء وإصلاحها**: إذا لم يبدأ تشغيل Beyond Compare، فتحقق مرة أخرى من المسار في الإعداد `difftool.bc.path`. استخدم `which bcomp` (macOS/Linux) أو `where BCompare.exe` (Windows) لتحديد موقع الملف التنفيذي.

يجب أن يمكنك هذا الإعداد من استخدام Beyond Compare بسلاسة مع `git difftool` و، اختياريًا، `git mergetool`. إذا واجهت مشاكل محددة، فأخبرني بنظام التشغيل الخاص بك وأي رسائل خطأ للحصول على نصائح أكثر تخصيصًا!