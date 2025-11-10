---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح psycopg2 بتثبيت PostgreSQL
translated: true
type: note
---

يشير الخطأ الذي تواجهه إلى أن حزمة `psycopg2` تتطلب تنفيذ `pg_config` من PostgreSQL للبناء من المصدر، ولكن لم يتم العثور عليه في نظامك. هذا يعني أنك بحاجة إلى تثبيت PostgreSQL على نظام macOS الخاص بك لتوفير التبعيات اللازمة. فيما يلي الخطوات لتثبيت PostgreSQL على نظام macOS وحل المشكلة.

### خطوات تثبيت PostgreSQL على macOS

#### 1. **تثبيت PostgreSQL باستخدام Homebrew (موصى به)**
يعتبر Homebrew أسهل طريقة لتثبيت وإدارة PostgreSQL على macOS.

1. **تثبيت Homebrew (إذا لم يكن مثبتًا بالفعل)**:
   - افتح Terminal وقم بتشغيل:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - اتبع التعليمات الظاهرة على الشاشة لإكمال تثبيت Homebrew.

2. **تثبيت PostgreSQL**:
   - في الـ Terminal، قم بتشغيل:
     ```bash
     brew install postgresql
     ```
   - يقوم هذا الأمر بتثبيت PostgreSQL وتبعياته، بما في ذلك تنفيذ `pg_config` المطلوب لـ `psycopg2`.

3. **بدء تشغيل PostgreSQL**:
   - لبدء خدمة PostgreSQL، قم بتشغيل:
     ```bash
     brew services start postgresql
     ```
   - بدلاً من ذلك، لبدء تشغيله يدويًا لجلسة واحدة:
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **التحقق من التثبيت**:
   - تحقق مما إذا كان PostgreSQL مثبتًا ويعمل:
     ```bash
     psql --version
     ```
   - يجب أن ترى إصدار PostgreSQL (مثال: `psql (PostgreSQL) 17.0`).
   - يمكنك أيضًا تسجيل الدخول إلى shell الخاص بـ PostgreSQL للتأكيد:
     ```bash
     psql -U $(whoami)
     ```

#### 2. **تثبيت `psycopg2` بعد PostgreSQL**
بمجرد تثبيت PostgreSQL، أعد محاولة تثبيت `psycopg2`. يجب أن يكون تنفيذ `pg_config` متاحًا الآن في المسار PATH الخاص بك.

1. **تثبيت `psycopg2`**:
   - قم بتشغيل:
     ```bash
     pip install psycopg2
     ```
   - إذا كنت تستخدم ملف متطلبات، قم بتشغيل:
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **بديل: تثبيت `psycopg2-binary` (خيار أسهل)**:
   - إذا كنت تريد تجنب بناء `psycopg2` من المصدر (والذي يتطلب تبعيات PostgreSQL)، يمكنك تثبيت حزمة `psycopg2-binary` المترجمة مسبقًا:
     ```bash
     pip install psycopg2-binary
     ```
   - ملاحظة: لا يُوصى بـ `psycopg2-binary` لبيئات الإنتاج بسبب مشاكل التوافق المحتملة، ولكنه مناسب للتطوير أو الاختبار.

#### 3. **اختياري: إضافة `pg_config` إلى PATH (إذا لزم الأمر)**
إذا لم يتم العثور على تنفيذ `pg_config` بعد تثبيت PostgreSQL، قد تحتاج إلى إضافته إلى المسار PATH يدويًا.

1. تحديد موقع `pg_config`:
   - عادةً ما يقوم Homebrew بتثبيت PostgreSQL في `/opt/homebrew/bin` (لـ Apple Silicon) أو `/usr/local/bin` (لـ Intel Macs).
   - تحقق من الموقع:
     ```bash
     find /opt/homebrew -name pg_config
     ```
     أو
     ```bash
     find /usr/local -name pg_config
     ```

2. الإضافة إلى PATH:
   - إذا تم العثور على `pg_config` (مثال: في `/opt/homebrew/bin`)، أضفه إلى المسار PATH الخاص بك عن طريق تحرير ملف تكوين shell الخاص بك (مثال: `~/.zshrc` أو `~/.bash_profile`):
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - طبق التغييرات:
     ```bash
     source ~/.zshrc
     ```

3. التحقق من `pg_config`:
   - قم بتشغيل:
     ```bash
     pg_config --version
     ```
   - إذا أعاد إصدارًا، فهذا يعني أن المسار PATH مضبوط بشكل صحيح.

#### 4. **استكشاف الأخطاء وإصلاحها**
- **استمرار الخطأ**: إذا فشل `pip install psycopg2`، فتأكد من أن لديك أدوات البناء اللازمة:
  - قم بتثبيت Xcode Command Line Tools:
    ```bash
    xcode-select --install
    ```
  - قم بتثبيت `libpq` (مكتبة عميل PostgreSQL) بشكل صريح إذا لزم الأمر:
    ```bash
    brew install libpq
    ```

- **توافق إصدار Python**: تأكد من أن إصدار Python الخاص بك (3.13 في حالتك) متوافق مع `psycopg2`. إذا استمرت المشاكل، ففكر في استخدام بيئة افتراضية بإصدار أقدم قليلاً من Python (مثال: 3.11 أو 3.12):
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **التحقق من Homebrew**: تأكد من أن Homebrew محدث:
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **طرق التثبيت البديلة (اختياري)**
إذا كنت تفضل عدم استخدام Homebrew، يمكنك تثبيت PostgreSQL عبر:
- **Postgres.app**:
  - قم بالتحميل من [postgresapp.com](https://postgresapp.com/).
  - اتبع تعليمات الإعداد لتثبيت وبدء تشغيل PostgreSQL.
  - أضف دليل `bin` (مثال: `/Applications/Postgres.app/Contents/Versions/latest/bin`) إلى المسار PATH الخاص بك كما هو موضح أعلاه.
- **مثبت PostgreSQL الرسمي**:
  - قم بتحميل مثبت macOS من [postgresql.org](https://www.postgresql.org/download/macosx/).
  - اتبع معالج التثبيت.

#### 6. **أعد محاولة تشغيل مشروعك**
بعد تثبيت PostgreSQL و `psycopg2` (أو `psycopg2-binary`)، أعد محاولة تشغيل مشروعك أو إعادة تثبيت المتطلبات:
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### ملاحظات إضافية
- **سبب حدوث الخطأ**: تتطلب حزمة `psycopg2` مكتبات تطوير PostgreSQL (تحديدًا `libpq`) للبناء من المصدر. يوفر تثبيت PostgreSQL عبر Homebrew هذه المكتبات.
- **اعتبارات الإنتاج**: للإنتاج، استخدم `psycopg2` (وليس `psycopg2-binary`) وتأكد من أن إصدار PostgreSQL الخاص بك يتطابق مع بيئة الهدف.
- **التوثيق**: لمزيد من التفاصيل، راجع دليل تثبيت `psycopg2` على [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html).

إذا واجهت المزيد من المشاكل، فيرجى مشاركة رسالة الخطأ المحددة، ويمكنني المساعدة في استكشاف الأخطاء وإصلاحها بشكل أكبر!