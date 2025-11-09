---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استخدام GPG مع مجلد رئيسي مخصص
translated: true
type: note
---

### استخدام خيار `--homedir` في GPG

يخبر علم `--homedir` (ملاحظة: إنه `--homedir`، وليس `--home-dir`—GPG يستخدم كلمة واحدة) برنامج GPG باستخدام دليل مخصص كـ"منزل" له لتخزين ملفات التكوين، وحلقات المفاتيح، وقواعد بيانات الثقة، وبيانات أخرى. بشكل افتراضي، يستخدم GPG المسار `~/.gnupg` (مثال: `/c/Users/YourName/.gnupg` في Git Bash على Windows). هذا الخيار مفيد من أجل:
- عزل إعدادات متعددة لـ GPG (مثال: واحد للمفاتيح الشخصية، وآخر للعمل).
- الاختبار أو تجنب التعارضات مع إعدادات GPG العامة للنظام.
- تشغيل GPG في بيئة محمولة أو مخصصة.

#### الصيغة الأساسية
```
gpg --homedir /path/to/custom/dir [أوامر gpg أخرى]
```
- استبدل `/path/to/custom/dir` بمسار الدليل المطلوب.
- في Git Bash على Windows، **استخدم دائمًا الشرطة المائلة للأمام (`/`)** للمسارات، حتى لمحركات الأقراص في Windows (مثال: `/c/Users/YourName/my-gpg-dir`).
- يجب أن يكون الدليل موجودًا؛ لن يقوم GPG بإنشائه تلقائيًا. قم بإنشائه أولاً باستخدام `mkdir -p /path/to/custom/dir`.

#### مثال: إعداد واستخدام دليل رئيسي مخصص
1. **إنشاء الدليل المخصص** (في Git Bash):
   ```
   mkdir -p /c/Users/YourName/my-custom-gpg
   ```

2. **إنشاء زوج المفاتيح باستخدام الدليل الرئيسي المخصص**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --full-generate-key
   ```
   - يقوم هذا بتخزين مفاتيحك وإعداداتك في `my-custom-gpg`، وليس في المجلد الافتراضي.

3. **سرد المفاتيح من ذلك الدليل**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --list-secret-keys --keyid-format LONG
   ```

4. **تشفير ملف باستخدام المفاتيح من الدليل المخصص**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --encrypt --recipient RECIPIENT_EMAIL secret.txt
   ```

5. **فك تشفير ملف**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --output decrypted.txt --decrypt secret.txt.gpg
   ```

#### نصائح لـ Git Bash على Windows
- **المسارات:** التزم باستخدام `/`—على سبيل المثال، تجنب استخدام `\` أو الشرط المختلطة، لأنها قد تعطل الأوامر.
- **الأذونات:** تأكد من أن الدليل المخصص لديه صلاحية القراءة/الكتابة (استخدم `chmod 700 /path/to/custom/dir` للأمان، مثل المجلد الافتراضي `.gnupg`).
- **بديل متغير البيئة:** بدلاً من استخدام `--homedir` في كل مرة، قم بتعيين `export GNUPGHOME=/c/Users/YourName/my-custom-gpg` في ملف `.bashrc` الخاص بك (قم بتشغيل `source ~/.bashrc` بعد التعديل). بعدها سيستخدمه GPG تلقائيًا.
- **التكامل مع Git:** إذا كنت تستخدمه للتوقيع في Git، قم بتكوينه باستخدام العلم:
  ```
  git config --global gpg.program "gpg --homedir /c/Users/YourName/my-custom-gpg"
  ```
- **المشاكل الشائعة:** إذا اشتكى GPG من ملفات مفقودة، فقد يحتاج إلى التهيئة—قم بتشغيل `gpg --homedir /path --gen-key` أولاً. على Windows، تجنب المسارات التي تحتوي على مسافات ما لم تكن بين علامتي اقتباس.

للحصول على التفاصيل الكاملة، راجع دليل GPG: [GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)