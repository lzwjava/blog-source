---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استراتيجيات تهيئة قواعد البيانات الآمنة
translated: true
type: note
---

### التعامل مع إعدادات قاعدة البيانات الحساسة في مشاريع بايثون

إدارة المعلومات الحساسة مثل كلمات مرور وقواعد البيانات ومنافذ الاتصال في ملفات الإعداد تمثل تحديًا شائعًا في مشاريع بايثون. الهدف هو تجنب حفظ الأسرار في نظام التحكم بالإصدارات (مثل Git) مع الحفاظ على سهولة النشر. أدناه، سأقارن بين النهجين اللذين ذكرتهما: (1) استخدام قالب `config_example.ini` مع `.gitignore` للملف الحقيقي، والإعداد اليدوي على الخوادم مثل UAT؛ و (2) استخدام تشفير GPG لتخزين القيم المشفرة في `config.ini` وفك تشفيرها أثناء وقت التشغيل. كلا النهجين آمنان إذا تم تنفيذهما بشكل صحيح، لكنهما يوازنان بين البساطة والأتمتة.

#### النهج 1: قالب الإعداد + `.gitignore` + الإعداد اليدوي للخادم
هذه طريقة مباشرة وبسيطة. تقوم بإنشاء ملف إعداد نموذجي للمطورين وخطوط أنابيب CI/CD، وتتجاهل الملف الحقيقي في Git، وتتعامل مع الإعداد الفعلي يدويًا في بيئات تشبه بيئة الإنتاج (مثل خوادم UAT).

**خطوات التنفيذ:**
1. إنشاء `config_example.ini` مع العناصر النائبة:
   ```
   [database]
   host = localhost
   port = 5432  # منفذ مثال؛ استبدله بالمنفذ الحقيقي
   user = dbuser
   password = example_password  # استبدل بكلمة المرور الحقيقية
   database = mydb
   ```

2. إضافة `config.ini` الحقيقي إلى `.gitignore`:
   ```
   config.ini
   ```

3. في كود بايثون الخاص بك، قم بالتحميل من `config.ini` (الرجوع إلى المثال إذا كان مفقودًا للتطوير):
   ```python
   import configparser
   import os

   config = configparser.ConfigParser()
   config_file = 'config.ini' if os.path.exists('config.ini') else 'config_example.ini'
   config.read(config_file)

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_password = config['database']['password']
   db_name = config['database']['database']
   ```

4. لخوادم UAT: انسخ `config.ini` يدويًا بالقيم الحقيقية (عبر SCP أو Ansible) أثناء النشر. يمكن للمطورين نسخ `config_example.ini` إلى `config.ini` وملئه محليًا.

**الإيجابيات:**
- بسيط — لا حاجة لمكتبات إضافية أو مفاتيح للإدارة.
- لا يوجد عبء إضافي أثناء التشغيل (فك التشفير).
- سهل للفرق الصغيرة؛ يعمل جيدًا مع النشر اليدوي.

**السلبيات:**
- يزيد الإعداد اليدوي على كل خادم من خطر الخطأ (مثل نسيان تحديث كلمة المرور).
- ليس مثاليًا لـ CI/CD الآلي؛ يتطلب حقن الأسرار بشكل آمن (عبر متغيرات البيئة في خطوط الأنابيب).
- إذا قام شخص ما بحفظ `config.ini` عن طريق الخطأ، يتم الكشف عن الأسرار.

هذا النهج رائع للمشاريع في المراحل الأولى أو عندما يبدو التشفير مبالغًا فيه.

#### النهج 2: تشفير GPG لقيم الإعداد
هنا، تقوم بتشفير الحقول الحساسة (مثل كلمة المرور) باستخدام GPG، وتخزن البيانات المشفرة في `config.ini`، وتقوم بفك تشفيرها في الكود الخاص بك أثناء وقت التشغيل. يمكن حفظ الملف المشفر في Git بأمان، طالما أن المفتاح الخاص بك لا يتم مشاركته أبدًا.

**خطوات التنفيذ:**
1. قم بتثبيت GPG على نظامك (إنه قياسي على Linux/Mac؛ استخدم Gpg4win على Windows). قم بتوليد زوج المفاتيح إذا لزم الأمر:
   ```
   gpg --gen-key  # اتبع التعليمات للمفتاح الخاص بك
   ```

2. قم بتشفير القيمة الحساسة (مثل كلمة المرور) في ملف:
   ```
   echo "real_password_here" | gpg --encrypt --recipient your-email@example.com -o encrypted_password.gpg
   ```
   - ينشئ هذا `encrypted_password.gpg`. يمكنك ترميزه base64 لتخزين سهل في INI:
     ```bash
     base64 encrypted_password.gpg > encrypted_password.b64
     ```

3. قم بتحديث `config.ini` لتضمين القيمة المشفرة (والمشفرة بـ base64). احفظ هذا — إنه آمن:
   ```
   [database]
   host = localhost
   port = 5432
   user = dbuser
   password_encrypted = <base64-encoded-encrypted-blob-here>  # From encrypted_password.b64
   database = mydb
   ```

4. في كود بايثون الخاص بك، قم بفك التشفير باستخدام مكتبة `gnupg` (قم بالتثبيت عبر `pip install python-gnupg` للتطوير، ولكن افترض أنها متاحة):
   ```python
   import configparser
   import gnupg
   import base64
   import tempfile
   import os

   config = configparser.ConfigParser()
   config.read('config.ini')  # يمكن حفظ هذا بأمان

   # فك تشفير كلمة المرور
   gpg = gnupg.GPG()  # يفترض أن GPG مثبت وأن المفتاح متاح
   encrypted_b64 = config['database']['password_encrypted']
   encrypted_data = base64.b64decode(encrypted_b64)

   with tempfile.NamedTemporaryFile(delete=False) as tmp:
       tmp.write(encrypted_data)
       tmp.flush()
       decrypted = gpg.decrypt_file(None, passphrase=None, extra_args=['--batch', '--yes'], output=tmp.name)
       if decrypted.ok:
           db_password = decrypted.data.decode('utf-8').strip()
       else:
           raise ValueError("فشل فك التشفير")

   os.unlink(tmp.name)  # تنظيف

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_name = config['database']['database']

   # الآن استخدم db_password...
   ```

5. لخوادم UAT: انشر `config.ini` كما هو (عبر Git أو النسخ). تأكد من وضع مفتاح GPG الخاص بشكل آمن على الخادم (عبر Ansible vault أو النسخ الآمن اليدوي). سيقوم الكود بفك التشفير عند بدء التشغيل.

**الإيجابيات:**
- يمكن التحكم في إصدارات الإعداد المشفر — لا حاجة لـ `.gitignore` للأسرار.
- يؤتمت النشر؛ يعمل مع CI/CD (فقط قبسق المفتاح بأمان).
- قابل للتدقيق: يتم تتبع التغييرات في القيم المشفرة.

**السلبيات:**
- يتطلب إعداد GPG وإدارة المفاتيح (مثل تدوير المفاتيح دوريًا؛ لا تحفظ المفاتيح الخاصة أبدًا).
- اعتماد وقت التشغيل على GPG و `python-gnupg`؛ فشل فك التشفير إذا كان المفتاح مفقودًا.
- أكثر تعقيدًا قليلاً للمبتدئين؛ تأثير محتمل على الأداء أثناء فك التشفير (ضئيل لكلمات المرور).

استخدم هذا للفرق التي لديها نشر آلي أو عند مشاركة الإعدادات عبر البيئات.

#### جدول المقارنة

| الجانب              | قالب + .gitignore + يدوي | تشفير GPG + فك تشفير أثناء التشغيل |
|---------------------|--------------------------------|----------------------------------|
| **الأمان**       | عالي إذا كانت الخطوات اليدوية حذرة؛ خطر الخطأ البشري. | عالي؛ الأسرار never في نص عادي. |
| **سهولة الإعداد**  | سهل جدًا (لا حاجة لأدوات).  | متوسط (GPG + مكتبة).       |
| **التحكم بالإصدار**| القالب محفوظ؛ الملف الحقيقي متجاهل. | الإعداد الكامل محفوظ (مشفر). |
| **النشر**     | يدوي لكل خادم (مثل SCP).| آلي (حاجة لمزامنة المفتاح).    |
| **العبء الإضافي**       | لا شيء.                         | طفيف (فك التشفير عند التحميل).        |
| **الأفضل لـ**       | المشاريع الصغيرة/اليدوية.        | خطوط أنابيب CI/CD الآلية.      |

#### التوصيات
- ابدأ **بالنهج 1** إذا كان مشروعك بسيطًا أو فريقك صغيرًا — إنه مجرب ومثبت.
- انتقل إلى **النهج 2** (أو تطور إلى متغيرات البيئة/مديري الأسرار مثل AWS SSM/HashiCorp Vault) للتوسع.
- اجمع دائمًا مع متغيرات البيئة للتجاوزات (مثل `os.getenv('DB_PASSWORD', db_password)`).
- اختبر فك التشفير في بيئة تجريبية قبل UAT.

إذا شاركت المزيد من التفاصيل (مثل أداة النشر الخاصة بك أو الإعداد الكامل)، يمكنني تحسين الكود!