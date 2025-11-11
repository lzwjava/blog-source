---
audio: false
generated: true
lang: ar
layout: post
title: تكوين TortoiseGit كأداة دمج Git
translated: true
type: note
---

لتكوين TortoiseGit كأداة دمج لـ Git، تحتاج إلى إعداد TortoiseGitMerge (أداة الدمج المضمنة مع TortoiseGit) في إعدادات Git الخاصة بك. فيما يلي الخطوات لتحقيق ذلك:

### المتطلبات الأساسية
- تأكد من تثبيت TortoiseGit على نظامك. يمكنك تنزيله من [tortoisegit.org](https://tortoisegit.org).
- تحقق من توفر ملف TortoiseGitMerge القابل للتنفيذ (يوجد عادةً في المسار `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`).

### خطوات تكوين TortoiseGitMerge كأداة دمج لـ Git

1. **افتح موجه الأوامر أو Git Bash**
   - يمكنك استخدام موجه أوامر Windows، أو PowerShell، أو Git Bash لتشغيل أوامر تكوين Git اللازمة.

2. **تعيين TortoiseGitMerge كأداة دمج**
   قم بتشغيل الأوامر التالية لتكوين Git لاستخدام TortoiseGitMerge:

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **الشرح**:
   - `merge.tool tortoisegitmerge`: يحدد اسم أداة الدمج كـ `tortoisegitmerge` (يمكنك اختيار أي اسم، ولكن هذا هو الاتفاق الشائع).
   - `mergetool.tortoisemerge.cmd`: يحدد الأمر لتشغيل TortoiseGitMerge مع المعلمات المناسبة:
     - `-base:"$BASE"`: ملف السلف المشترك.
     - `-theirs:"$REMOTE"`: الملف من الفرع الذي يتم دمجه.
     - `-mine:"$LOCAL"`: الملف من فرعك الحالي.
     - `-merged:"$MERGED"`: ملف الإخراج حيث سيتم حفظ الدمج الذي تم حله.
   - استخدم الشرطات المائلة للأمام (`/`) في المسار وقم بحماية علامات الاقتباس حسب الحاجة، خاصة إذا كان المسار يحتوي على مسافات.

   **ملاحظة**: اضبط المسار (`C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`) إذا تم تثبيت TortoiseGit في موقع مختلف (مثل `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`).

3. **اختياري: تعطيل مطالبة أداة الدمج**
   لتجنب ظهور مطالبة في كل مرة تقوم فيها بتشغيل `git mergetool`، يمكنك تعطيل المطالبة:

   ```bash
   git config --global mergetool.prompt false
   ```

4. **اختياري: تأكد من أن TortoiseGitMerge موجود في مسار النظام PATH**
   إذا لم يتمكن Git من العثور على TortoiseGitMerge، فتأكد من أن الدليل الخاص به موجود في متغير بيئة PATH في نظامك:
   - انقر بزر الماوس الأيمن على "This PC" أو "My Computer" → Properties → Advanced system settings → Environment Variables.
   - ضمن "System Variables"، ابحث عن متغير `Path` وقم بتعديله لتضمين `C:\Program Files\TortoiseGit\bin`.
   - بدلاً من ذلك، قم بتعيين المسار صراحةً في تكوين Git:

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **اختبر التكوين**
   - أنشئ تعارض دمج في مستودع Git (على سبيل المثال، عن طريق دمج فرعين بهما تغييرات متعارضة).
   - قم بتشغيل الأمر التالي لبدء تشغيل أداة الدمج:

     ```bash
     git mergetool
     ```

   - يجب أن يفتح TortoiseGitMerge، مع عرض عرض ثلاثي الأجزاء يحتوي على الإصدارات base و theirs و mine لملف التعارض. الجزء السفلي هو نتيجة الدمج.

6. **حل التعارضات في TortoiseGitMerge**
   - في العرض ثلاثي الأجزاء، يظهر TortoiseGitMerge:
     - **الجزء الأيسر**: إصدار "theirs" (من الفرع الذي يتم دمجه).
     - **الجزء الأيمن**: إصدار "mine" (من فرعك الحالي).
     - **الجزء الأوسط**: إصدار base (السلف المشترك).
     - **الجزء السفلي**: نتيجة الدمج حيث تقوم بحل التعارضات.
   - انقر بزر الماوس الأيمن على الأقسام المتعارضة لاختيار خيارات مثل "Use text block from 'theirs'" أو "Use text block from 'mine'"، أو قم بتعديل ملف الدمج يدويًا.
   - بمجرد الحل، احفظ الملف (File → Save) وأغلق TortoiseGitMerge.
   - سيقوم Git بوضع علامة على الملف على أنه تم حله إذا أغلق TortoiseGitMerge بنجاح (كود خروج 0). إذا تمت مطالبتك، قم بتأكيد وضع علامة على التعارض على أنه تم حله.

7. **قم بإجراء commit للدمج الذي تم حله**
   بعد حل التعارضات، قم بإجراء commit للتغييرات:

   ```bash
   git commit
   ```

   **ملاحظة**: إذا حدث التعارض أثناء إعادة التطبيق rebase أو cherry-pick، فاستخدم مربعات حوار TortoiseGit المناسبة (Rebase أو Cherry-pick) لمتابعة العملية بدلاً من مربع حوار commit القياسي.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### استخدام TortoiseGitMerge عبر واجهة المستخدم الرسومية لـ TortoiseGit
إذا كنت تفضل استخدام واجهة المستخدم الرسومية لـ TortoiseGit لحل التعارضات:
1. انقر بزر الماوس الأيمن على ملف التعارض في Windows Explorer.
2. اختر **TortoiseGit → Edit Conflicts**.
3. سيفتح TortoiseGitMerge، مما يسمح لك بحل التعارضات كما هو موضح أعلاه.
4. بعد الحفظ، انقر بزر الماوس الأيمن مرة أخرى واختر **TortoiseGit → Resolved** لوضع علامة على الملف على أنه تم حله.
5. قم بإجراء commit للتغييرات باستخدام مربع حوار Commit في TortoiseGit.

### استكشاف الأخطاء وإصلاحها
- **الخطأ: "Unsupported merge tool 'tortoisemerge'"**
  - تأكد من أن المسار إلى `TortoiseGitMerge.exe` صحيح ويمكن الوصول إليه.
  - تحقق من تطابق اسم الأداة تمامًا في تكوينات `merge.tool` و `mergetool.<tool>.cmd`.
  - تحقق من أن TortoiseGitMerge موجود في PATH أو تم تعيينه صراحةً باستخدام `mergetool.tortoisemerge.path`.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **المسافات في مسارات الملفات**
  - إذا كانت مسارات الملفات تحتوي على مسافات، فيجب أن يتعامل بناء جملة الأمر مع علامات الاقتباس المحمية (كما هو موضح أعلاه) معها بشكل صحيح.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **مستخدمو Cygwin**
  - إذا كنت تستخدم Cygwin، فاضبط المسار لاستخدام نقطة التحميل الخاصة بـ Cygwin، مثل:

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    يأخذ هذا في الاعتبار هيكل المسار `/cygdrive/c/` الخاص بـ Cygwin.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **لم يتم العثور على TortoiseGitMerge**
  - إذا كنت قد استخدمت سابقًا TortoiseMerge الخاص بـ TortoiseSVN، فتأكد من أنك تشير إلى `TortoiseGitMerge.exe`، حيث تغير اسم الملف القابل للتنفيذ في TortoiseGit الإصدار 1.8.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### ملاحظات إضافية
- يدعم TortoiseGitMerge عرضًا ثلاثي الأجزاء لحل التعارضات، وهو مثالي للدمج. يقوم تلقائيًا بدمج التغييرات غير المتعارضة ويبرز التعارضات للحل اليدوي.[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- إذا كنت ترغب في استخدام TortoiseGitMerge كأداة مقارنة diff أيضًا، فقم بتكوينها بشكل مشابه:

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  ثم استخدم `git difftool` لمقارنة الملفات.[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- للإعدادات المتقدمة، يمكنك تكوين TortoiseGit للانتظار حتى تغلق أداة الدمج ووضع علامة تلقائيًا على الملفات على أنها تم حلها بناءً على كود الخروج. في إعدادات TortoiseGit → External Programs → Merge Tool، اختر "Block TortoiseGit while executing the external merge tool" وقم بتمكين "Trust exit code."[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### المصادر
- وثائق TortoiseGit:[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow ومصادر ويب أخرى:[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

باتباع هذه الخطوات، يجب أن تكون قادرًا على استخدام TortoiseGitMerge كأداة دمج لـ Git بشكل فعال، سواء من سطر الأوامر أو عبر واجهة المستخدم الرسومية لـ TortoiseGit.