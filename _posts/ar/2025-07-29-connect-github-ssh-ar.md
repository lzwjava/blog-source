---
audio: false
generated: true
image: false
lang: ar
layout: post
title: الاتصال إلى GitHub عبر SSH
translated: true
type: note
---

للاتصال بـ GitHub باستخدام SSH، اتبع هذه الخطوات بناءً على التوثيق المقدم من GitHub. يفترض هذا الدليل أنك تبدأ من الصفر ويتضمن التحقق من وجود مفاتيح موجودة، وإنشاء مفتاح جديد، وإضافته إلى GitHub، واختبار الاتصال.

### 1. التحقق من وجود مفاتيح SSH موجودة
قبل إنشاء مفتاح SSH جديد، تحقق إذا كان لديك واحد بالفعل:
- افتح طرفية (على macOS/Linux) أو Git Bash (على Windows).
- نفّذ:
  ```bash
  ls -al ~/.ssh
  ```
- ابحث عن ملفات مثل `id_rsa` و `id_rsa.pub` (أو ما شابه، مثل `id_ed25519`، `id_ed25519.pub`). إذا كانت موجودة، فقد يكون لديك مفتاح بالفعل. إذا أردت استخدام مفتاح موجود، انتقل إلى الخطوة 3. إذا لم يكن الأمر كذلك، تابع لإنشاء مفتاح جديد.

### 2. إنشاء مفتاح SSH جديد
إذا لم يكن لديك مفتاح SSH أو أردت مفتاحًا جديدًا:
- في طرفيتك، أنشئ مفتاح SSH جديدًا:
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
  - استبدل `your_email@example.com` بالبريد الإلكتروني المرتبط بحسابك على GitHub.
  - إذا كان نظامك لا يدعم `ed25519`، استخدم:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
- عند المطالبة، اضغط على Enter لحفظ المفتاح في الموقع الافتراضي (`~/.ssh/id_ed25519` أو `~/.ssh/id_rsa`).
- اختياريًا، أدخل عبارة مرور لأمان إضافي (أو اضغط Enter لعدم استخدام أي عبارة).

### 3. إضافة مفتاح SSH إلى وكيل SSH
يدير وكيل SSH مفاتيحك للمصادقة:
- ابدأ تشغيل وكيل SSH:
  ```bash
  eval "$(ssh-agent -s)"
  ```
- أضف مفتاحك الخاص إلى الوكيل:
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - إذا استخدمت RSA، استبدل `id_ed25519` بـ `id_rsa`.
- إذا قمت بتعيين عبارة مرور، سيُطلب منك إدخالها.

### 4. إضافة مفتاح SSH إلى حسابك على GitHub
- انسخ مفتاحك العام إلى الحافظة:
  - على macOS:
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - على Linux:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    ثم انسخ الناتج يدويًا.
  - على Windows (Git Bash):
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - إذا استخدمت RSA، استبدل `id_ed25519.pub` بـ `id_rsa.pub`.
- اذهب إلى GitHub:
  - سجّل الدخول إلى [GitHub](https://github.com).
  - انقر على صورة ملفك الشخصي (أعلى اليمين) → **Settings** → **SSH and GPG keys** → **New SSH key** أو **Add SSH key**.
  - الصق مفتاحك العام في حقل "Key"، أعطه عنوانًا (مثل "My Laptop")، وانقر على **Add SSH key**.

### 5. اختبار اتصال SSH الخاص بك
تحقق من أن مفتاح SSH يعمل مع GitHub:
- نفّذ:
  ```bash
  ssh -T git@github.com
  ```
- إذا تمت المطالبة، قم بالتأكيد بكتابة `yes`.
- يجب أن ترى رسالة مثل:
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  هذا يؤكد أن اتصال SSH يعمل.

### 6. تكوين Git لاستخدام SSH
تأكد من أن مستودع Git الخاص بك يستخدم SSH للمصادقة:
- تحقق من عنوان URL البعيد لمستودعك:
  ```bash
  git remote -v
  ```
- إذا كان عنوان URL يبدأ بـ `https://`، غيّره إلى SSH:
  ```bash
  git remote set-url origin git@github.com:username/repository.git
  ```
  - استبدل `username/repository` باسم مستخدم GitHub واسم المستودع الخاصين بك.

### 7. اختياري: إدارة عبارات مرور مفتاح SSH
إذا قمت بتعيين عبارة مرور، يمكنك تكوين وكيل SSH لتجنب إعادة إدخالها:
- على macOS، أضف مفتاحك إلى سلسلة المفاتيح:
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- على Linux/Windows، يطلب وكيل SSH عادةً عبارة المرور مرة واحدة فقط لكل جلسة.

### 8. اختياري: استخدام توجيه وكيل SSH أو مفاتيح النشر
- **توجيه وكيل SSH**: إذا كنت تقوم بالنشر على خادم، فعّل توجيه الوكيل لاستخدام مفاتيح SSH المحلية بأمان. أضف إلى ملف `~/.ssh/config`:
  ```bash
  Host example.com
      ForwardAgent yes
  ```
  استبدل `example.com` باسم المضيف لخادمك.
- **مفاتيح النشر**: للنصوص البرمجية الآلية، أنشئ مفتاح SSH منفصل لكل خادم وأضفه كمفتاح نشر في إعدادات مستودع GitHub الخاص بك.

### استكشاف الأخطاء وإصلاحها
- إذا فشل `ssh -T git@github.com`، تأكد من:
  - أن مفتاحك العام مضاف بشكل صحيح إلى GitHub.
  - أن وكيل SSH يعمل وأن مفتاحك مضاف (`ssh-add -l` لعرض المفاتيح المحملة).
  - أن أذونات الملف صحيحة:
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- لمزيد من المشكلات، تحقق من دليل استكشاف الأخطاء وإصلاحها في GitHub.

الآن يمكنك استخدام SSH للتفاعل مع GitHub بأمان دون إدخال بيانات الاعتماد بشكل متكرر.

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)