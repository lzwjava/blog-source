---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة VSCode لتصحيح أخطاء بايثون
translated: true
type: note
---

لحل المشكلة التي تشتكي فيها Visual Studio Code (VSCode) من "no module named `ibm_db_dbi`" عند تصحيح أخطاء (debugging) سكريبت Python، على الرغم من أن استيراد الوحدة النمطية (module) يتم بنجاح عند تشغيل `python test_db.py` مباشرة من سطر الأوامر باستخدام Python 3.11.8، اتبع هذه الخطوات. يحدث هذا التناقض عادةً بسبب الاختلافات في بيئة Python أو التكوين بين سطر الأوامر ومصحح أخطاء VSCode. إليك كيفية الإصلاح:

---

### الخطوة 1: التحقق من مترجم Python في VSCode
السبب الأكثر شيوعًا لهذه المشكلة هو أن VSCode يستخدم مترجم Python مختلف عن ذلك المستخدم في سطر الأوامر، حيث تم تثبيت `ibm_db_dbi`.

- **التحقق من المترجم المحدد في VSCode:**
  - انظر إلى الزاوية اليسرى السفلى من نافذة VSCode. يعرض هذا المترجم Python المحدد حاليًا (مثل "Python 3.11.8" أو مسار مثل `/usr/bin/python3.11`).
  - انقر عليه لفتح قائمة اختيار المترجم.

- **المقارنة مع سطر الأوامر:**
  - في طرفيتك، شغّل:
    ```bash
    python --version
    ```
  - تأكد من أن الناتج هو "Python 3.11.8". إذا كنت تستخدم `python3` بدلاً من `python`، فجرب:
    ```bash
    python3 --version
    ```
  - أيضًا، ابحث عن المسار إلى هذا الملف التنفيذي لـ Python:
    ```bash
    which python
    ```
    أو
    ```bash
    which python3
    ```
    قد يعيد هذا شيئًا مثل `/usr/local/bin/python3.11`.

- **حدد المترجم الصحيح في VSCode:**
  - إذا كان المترجم المعروض في VSCode لا يتطابق مع Python 3.11.8 أو المسار من سطر الأوامر، فحدد المترجم الصحيح:
    - في قائمة اختيار المترجم، اختر "Python 3.11.8" أو المسار الذي يتطابق مع Python في سطر الأوامر (مثل `/usr/local/bin/python3.11`).
    - إذا لم يكن مدرجًا، انقر على "Enter interpreter path" وأدخل المسار يدويًا إلى الملف التنفيذي لـ Python 3.11.8.

---

### الخطوة 2: تأكد من تثبيت `ibm_db_dbi` في البيئة المحددة
نظرًا لأن الوحدة النمطية تعمل عند تشغيل السكريبت من سطر الأوامر، فمن المرجح أنها مثبتة في بيئة Python تلك. تحقق من تطابق هذا مع مترجم VSCode.

- **تحقق من موقع الوحدة النمطية:**
  - في الطرفية، باستخدام نفس الملف التنفيذي لـ Python (مثل `python` أو `/usr/local/bin/python3.11`)، شغّل:
    ```bash
    pip show ibm_db_dbi
    ```
  - ابحث عن حقل "Location" في الناتج. قد يكون شيئًا مثل `/usr/local/lib/python3.11/site-packages`. هذا هو المكان الذي تم فيه تثبيت `ibm_db_dbi`.

- **تأكد من أن مترجم VSCode يحتوي على الوحدة النمطية:**
  - إذا قمت بتحديد مترجم مختلف في الخطوة 1، فقم بتنشيط ذلك المترجم في الطرفية:
    ```bash
    /path/to/python3.11 -m pip show ibm_db_dbi
    ```
  - استبدل `/path/to/python3.11` بالمسار من VSCode. إذا لم يُرجع أي شيء، قم بتثبيت الوحدة النمطية:
    ```bash
    /path/to/python3.11 -m pip install ibm_db_dbi
    ```

---

### الخطوة 3: ضبط تكوين التصحيح في VSCode
إذا كان المترجم صحيحًا ولكن التصحيح لا يزال فاشلًا، فقد تكون المشكلة في بيئة تصحيح VSCode. قم بتعديل ملف `launch.json` لضمان استخدام المصحح لنفس البيئة المستخدمة في سطر الأوامر.

- **افتح تكوين التصحيح:**
  - انتقل إلى عرض "Run and Debug" في VSCode (Ctrl+Shift+D أو Cmd+Shift+D على macOS).
  - انقر على أيقونة الترس لتعديل `launch.json`. إذا كان غير موجود، فسيقوم VSCode بإنشائه عند بدء التصحيح.

- **عدّل `launch.json`:**
  - تأكد من أنه يتضمن تكوينًا لسكريبتك. مثال أساسي يبدو كالتالي:
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            }
        ]
    }
    ```

- **عيّن متغيرات البيئة (إذا لزم الأمر):**
  - قد تتطلب وحدة `ibm_db_dbi`، المستخدمة لقواعد بيانات IBM DB2، متغيرات بيئة مثل `LD_LIBRARY_PATH` أو إعدادات محددة لـ DB2 لتحديد موقع المكتبات المشتركة (shared libraries).
  - في الطرفية حيث يعمل `python test_db.py`، ابحث عن المتغيرات ذات الصلة:
    ```bash
    env | grep -i db2
    ```
    أو ادرج جميع المتغيرات:
    ```bash
    env
    ```
  - ابحث عن متغيرات مثل `DB2INSTANCE` أو `LD_LIBRARY_PATH`.
  - أضف هذه إلى `launch.json` تحت المفتاح `"env"`. على سبيل المثال:
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {
                    "LD_LIBRARY_PATH": "/path/to/db2/libraries",
                    "DB2INSTANCE": "db2inst1"
                }
            }
        ]
    }
    ```
  - استبدل القيم بتلك من بيئة سطر الأوامر الخاصة بك.

- **عيّن PYTHONPATH (إذا لزم الأمر):**
  - إذا كان `ibm_db_dbi` في موقع غير قياسي، فتأكد من أن المصحح يمكنه العثور عليه عن طريق تعيين `PYTHONPATH`.
  - من ناتج `pip show ibm_db_dbi`، لاحظ "Location" (مثل `/usr/local/lib/python3.11/site-packages`).
  - أضفه إلى `launch.json`:
    ```json
    "env": {
        "PYTHONPATH": "/usr/local/lib/python3.11/site-packages"
    }
    ```

---

### الخطوة 4: الاختبار واستكشاف الأخطاء وإصلاحها
- **شغّل المصحح:**
  - احفظ `launch.json`، ثم اضغط F5 أو انقر على زر "Start Debugging" الأخضر لتصحيح سكريبتك.
  - تحقق من وحدة تحكم التصحيح (Debug Console) للبحث عن الأخطاء. قد تُظهر الملف التنفيذي لـ Python المستخدم (مثل "Starting debug adapter with python executable: /path/to/python").

- **تحقق من الملف التنفيذي:**
  - إذا كان المسار في وحدة تحكم التصحيح لا يتطابق مع Python 3.11.8 المتوقع، فارجع إلى الخطوة 1 للتأكد من تحديد المترجم الصحيح.

- **اختبر بدون تصحيح:**
  - شغّل السكريبت بدون تصحيح (Ctrl+F5 أو "Run Without Debugging"). إذا كان هذا يعمل ولكن التصحيح يفشل، فإن المشكلة محددة بتكوين التصحيح، مما يؤكد الحاجة إلى تعديلات `launch.json`.

---

### الحل النهائي
من المرجح أن السبب الجذري هو أن مصحح أخطاء VSCode لا يستخدم نفس بيئة Python أو الإعدادات مثل تنفيذ سطر الأوامر الخاص بك. من خلال التأكد من تطابق المترجم مع Python 3.11.8، والتحقق من تثبيت `ibm_db_dbi`، وتكوين `launch.json` بمتغيرات البيئة اللازمة أو `PYTHONPATH`، يمكنك محاذاة البيئات. إليك مثال `launch.json` كامل مخصص لحالتك:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "/usr/local/lib/python3.11/site-packages",
                "LD_LIBRARY_PATH": "/path/to/db2/libraries"
            }
        }
    ]
}
```

اضبط مسارات `PYTHONPATH` و `LD_LIBRARY_PATH` بناءً على ناتج `pip show ibm_db_dbi` وبيئة سطر الأوامر الخاصة بك. بعد تطبيق هذه التغييرات، يجب أن تكون قادرًا على تصحيح سكريبتك في VSCode دون خطأ "no module named `ibm_db_dbi`".

---

نظرًا لأنك تستخدم Windows وتواجه خطأ "no module named `ibm_db_dbi`" في مصحح أخطاء Python الخاص بـ VSCode، فمن المرجح أن المشكلة تنشأ لأن المصحح لا يستخدم نفس بيئة Python التي تم فيها تثبيت `ibm_db_dbi`، أو أنه يفتقد إعدادات التكوين اللازمة. فيما يلي الخطوات لحل هذه المشكلة على Windows، لضمان تشغيل سكريبتك بشكل صحيح في مصحح أخطاء VSCode.

---

### الخطوة 1: التحقق من مترجم Python في VSCode
قد يحدث الخطأ إذا كان VSCode يستخدم مترجم Python مختلف عن ذلك الذي تم تثبيت `ibm_db_dbi` عليه.

- **التحقق من المترجم الحالي في VSCode:**
  - انظر إلى الزاوية اليسرى السفلى من نافذة VSCode. تظهر المترجم Python المحدد (مثل "Python 3.11.8" أو مسار مثل `C:\Python311\python.exe`).
  - انقر عليه لفتح قائمة اختيار المترجم.

- **المقارنة مع سطر الأوامر:**
  - افتح موجه الأوامر (cmd.exe) واكتب:
    ```cmd
    python --version
    ```
  - يجب أن يعرض هذا إصدار Python (مثل "Python 3.11.8"). إذا لم يعمل `python`، فجرب `py --version` أو اضبط بناءً على إعداداتك.
  - ابحث عن مسار الملف التنفيذي لـ Python:
    ```cmd
    where python
    ```
  - قد ينتج هذا شيئًا مثل `C:\Python311\python.exe`.

- **عيّن المترجم الصحيح في VSCode:**
  - إذا كان مترجم VSCode لا يتطابق مع الإصدار أو المسار من سطر الأوامر (مثل `C:\Python311\python.exe`)، فحدده:
    - في قائمة المترجم، اختر الإصدار المطابق (مثل "Python 3.11.8") أو المسار.
    - إذا لم يكن مدرجًا، فحدد "Enter interpreter path" واكتب المسار الكامل (مثل `C:\Python311\python.exe`).

---

### الخطوة 2: تأكد من تثبيت `ibm_db_dbi`
بافتراض أن سكريبتك يعمل خارج VSCode (عبر `python test_db.py` في موجه الأوامر)، فمن المرجح أن `ibm_db_dbi` مثبت في بيئة Python تلك. دعنا نتحقق من ذلك ونوائمه مع VSCode.

- **تحقق من مكان تثبيت `ibm_db_dbi`:**
  - في موجه الأوامر، شغّل:
    ```cmd
    pip show ibm_db_dbi
    ```
  - ابحث عن حقل "Location" (مثل `C:\Python311\Lib\site-packages`). هذا هو المكان الذي توجد فيه الوحدة النمطية.

- **تحقق من أن مترجم VSCode يحتوي عليها:**
  - إذا قمت بتغيير المترجم في الخطوة 1، فاختبره:
    ```cmd
    C:\path\to\python.exe -m pip show ibm_db_dbi
    ```
  - استبدل `C:\path\to\python.exe` بمسار مترجم VSCode. إذا لم يُظهر أي ناتج، فقم بتثبيت الوحدة النمطية:
    ```cmd
    C:\path\to\python.exe -m pip install ibm_db_dbi
    ```

---

### الخطوة 3: تكوين المصحح في VSCode
حتى مع المترجم الصحيح، قد يفشل المصحح بسبب اختلافات البيئة. سنقوم بضبط ملف `launch.json`.

- **الوصول إلى `launch.json`:**
  - انتقل إلى "Run and Debug" (Ctrl+Shift+D) في VSCode.
  - انقر على أيقونة الترس لفتح أو إنشاء `launch.json`.

- **حدّث `launch.json`:**
  - أضف أو عدّل تكوينًا كالتالي:
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            }
        ]
    }
    ```

- **أضف متغيرات البيئة (إذا لزم الأمر):**
  - قد تحتاج وحدة `ibm_db_dbi` إلى إعدادات متعلقة بـ DB2 (مثل `PATH` إلى مكتبات DB2 الديناميكية DLLs). تحقق من بيئة سطر الأوامر الخاصة بك:
    ```cmd
    set
    ```
  - ابحث عن إدخالات مثل `PATH` (بما في ذلك مسارات DB2) أو `DB2INSTANCE`.
  - أضفها إلى `launch.json`. مثال:
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {
                    "PATH": "C:\\path\\to\\db2\\bin;${env:PATH}",
                    "DB2INSTANCE": "db2inst1"
                }
            }
        ]
    }
    ```
  - استبدل `C:\\path\\to\\db2\\bin` و `db2inst1` بقيم من نظامك.

- **عيّن `PYTHONPATH` (إذا لزم الأمر):**
  - من ناتج `pip show ibm_db_dbi`، لاحظ "Location" (مثل `C:\Python311\Lib\site-packages`).
  - أضفه إلى `launch.json`:
    ```json
    "env": {
        "PYTHONPATH": "C:\\Python311\\Lib\\site-packages"
    }
    ```

---

### الخطوة 4: اختيار المصحح
- احفظ `launch.json`.
- اضغط F5 أو انقر على "Start Debugging" لتشغيل سكريبتك في المصحح.
- تحقق من وحدة تحكم التصحيح (Debug Console) للبحث عن الأخطاء. قد تظهر مسار Python المستخدم (مثل `C:\Python311\python.exe`). إذا كان خاطئًا، ارجع إلى الخطوة 1.
- إذا فشل التصحيح ولكن التشغيل بدون تصحيح (Ctrl+F5) يعمل، فإن المشكلة في `launch.json`، لذا راجع إعدادات `env` مرة أخرى.

---

### مثال كامل
إليك `launch.json` مخصص لإصلاح مشكلتك:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "C:\\Python311\\Lib\\site-packages",
                "PATH": "C:\\path\\to\\db2\\bin;${env:PATH}"
            }
        }
    ]
}
```
- اضبط `PYTHONPATH` ليطابق "Location" من ناتج `pip show ibm_db_dbi`.
- حدّث `PATH` بأي مسارات DB2 من ناتج `set` في سطر الأوامر.

---

### الخلاصة
يحدث خطأ "no module named `ibm_db_dbi`" لأن مصحح أخطاء VSCode غير متوافق مع بيئة Python التي تم تثبيت الوحدة النمطية عليها. من خلال تعيين المترجم الصحيح، والتأكد من توفر `ibm_db_dbi`، وتكوين `launch.json` بمتغيرات البيئة الصحيحة، ستقوم بحل المشكلة والتصحيح بنجاح في VSCode على Windows.