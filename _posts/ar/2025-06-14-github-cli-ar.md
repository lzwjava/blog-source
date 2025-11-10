---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت GitHub CLI
translated: true
type: note
---

لتثبيت GitHub CLI (`gh`) على Ubuntu واستخدامه لتنفيذ مسارات عمل GitHub Actions باستخدام أمر `gh workflow run`، اتبع الخطوات التالية:

### خطوات التثبيت لـ GitHub CLI (`gh`) على Ubuntu

1. **إضافة مستودع GitHub CLI ومفتاح GPG**:
   قم بتشغيل الأوامر التالية في طرفيتك لإعداد مستودع حزمة GitHub CLI الرسمي:

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   يقوم هذا السكريبت بما يلي:
   - يثبت `wget` إذا لم يكن موجودًا مسبقًا.
   - ينشئ دليلًا لحلقات مفاتيح APT.
   - يقوم بتنزيل وإضافة مفتاح GPG الخاص بـ GitHub CLI.
   - يهيئ مستودع GitHub CLI لنظامك.

2. **تحديث فهرس الحزم وتثبيت `gh`**:
   قم بتحديث قائمة الحزم الخاصة بك وقم بتثبيت أداة سطر الأوامر `gh`:

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **التحقق من التثبيت**:
   تحقق من تثبيت `gh` بشكل صحيح عن طريق تشغيل:

   ```bash
   gh --version
   ```

   يجب أن ترى ناتجًا مشابهًا لـ `gh version X.Y.Z (YYYY-MM-DD)`، مما يؤكد التثبيت.

4. **المصادقة مع GitHub**:
   قبل استخدام `gh`، قم بالمصادقة باستخدام حساب GitHub الخاص بك:

   ```bash
   gh auth login
   ```

   اتبع المطالبات:
   - اختر `GitHub.com` (أو خادم المؤسسة الخاص بك إذا كان مطبقًا).
   - حدد البروتوكول المفضل لديك (`HTTPS` أو `SSH`؛ يوصى بـ `SSH` إذا كان لديك مفتاح SSH معين).
   - اختر طريقة المصادقة (المتصفح هو الأسهل؛ حيث يفتح صفحة ويب لتسجيل الدخول).
   - انسخ الرمز لمرة واحدة المقدم، والصقه في المتصفح، وقم بتفويض `gh`.
   - قم بتأكيد الإعدادات الافتراضية أو تعديلها حسب الحاجة.

   بعد المصادقة الناجحة، سترى رسالة تأكيد.

### استخدام `gh workflow run` لـ GitHub Actions

يقوم أمر `gh workflow run` بتنفيذ مسار عمل GitHub Actions. إليك كيفية استخدامه:

1. **انتقل إلى مستودعك** (اختياري):
   إذا كنت في مستودع Git محلي مرتبط بـ GitHub، فسيقوم `gh` باكتشافه تلقائيًا. وإلا، حدد المستودع باستخدام علم `--repo`.

2. **اعرض مسارات العمل المتاحة** (اختياري):
   للعثور على معرف مسار العمل أو اسم الملف، قم بتشغيل:

   ```bash
   gh workflow list
   ```

   يعرض هذا جميع مسارات العمل في المستودع، موضحًا أسماءها، ومعرفاتها، وحالاتها (مثل `active`).

3. **شغّل مسار عمل**:
   استخدم أمر `gh workflow run` مع اسم ملف مسار العمل أو معرفه. على سبيل المثال:

   ```bash
   gh workflow run workflow.yml
   ```

   أو باستخدام معرف مسار العمل (مثل `123456`):

   ```bash
   gh workflow run 123456
   ```

   إذا كان مسار العمل يقبل مدخلات، قم بتوفيرها باستخدام علم `--field`:

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   لتحديد فرع أو مرجع، استخدم علم `--ref`:

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **راقب مسار العمل**:
   بعد التنفيذ، تحقق من حالة التشغيل:

   ```bash
   gh run list
   ```

   لمشاهدة تشغيل محدد في الوقت الفعلي، استخدم:

   ```bash
   gh run watch <run-id>
   ```

   استبدل `<run-id>` بمعرف التشغيل من `gh run list`.

### نصائح استكشاف الأخطاء وإصلاحها

- **أخطاء توقيع GPG**: إذا واجهت مشاكل متعلقة بـ GPG أثناء `apt update`، فارجع إلى متعقب المشكلات في GitHub للحصول على الإصلاحات (مثل `cli/cli#9569`) أو أعد محاولة خطط استيراد المفتاح. [](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **مشاكل الجدار الناري**: إذا فشل `keyserver.ubuntu.com`، جرب:

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   أو قم بتثبيت `dirmngr` إذا لزم الأمر:

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **تحذير تثبيت Snap**: تثبط GitHub استخدام حزمة Snap لـ `gh` بسبب مشاكل وقت التشغيل. التزم بطريقة APT المذكورة أعلاه. [](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **نطاقات المصادقة**: إذا فشل `gh workflow run` بسبب الأذونات، فتأكد من أن الرمز المميز (token) الخاص بك يحتوي على نطاق `workflow`. أعد المصادقة باستخدام:

   ```bash
   gh auth refresh -s workflow
   ```

### ملاحظات إضافية

- **دليل GitHub CLI**: للحصول على مزيد من التفاصيل حول أوامر `gh`، قم بتشغيل `gh help` أو قم بزيارة الدليل الرسمي على [cli.github.com](https://cli.github.com). [](https://cli.github.com/manual/)
- **متطلبات مسار العمل**: تأكد من وجود ملف مسار العمل (مثل `workflow.yml`) في الدليل `.github/workflows/` الخاص بمستودعك وأنه مضبوط للتنفيذ اليدوي (مثل حدث `workflow_dispatch`).
- **طرق التثبيت البديلة**: يمكنك أيضًا تثبيت `gh` عبر Homebrew (`brew install gh`) أو عن طريق تنزيل الملفات الثنائية من [صفحة الإصدارات](https://github.com/cli/cli/releases)، ولكن طريقة APT هي الموصى بها لـ Ubuntu. [](https://github.com/cli/cli)

يسمح لك هذا الإعداد بإدارة مسارات عمل GitHub Actions بكفاءة من سطر الأوامر على Ubuntu. أعلمني إذا كنت بحاجة إلى مساعدة في أوامر `gh` محددة أو تكوينات مسار العمل!