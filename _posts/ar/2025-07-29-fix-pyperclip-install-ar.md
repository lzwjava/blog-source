---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح خطأ تثبيت بايبركلب
translated: true
type: note
---

يحدث الخطأ أثناء تثبيت حزمة `pyperclip`، تحديدًا عند إنشاء عجلتها (wheel)، بسبب مشكلة في حزمة `setuptools` تتعلق بالسمة `install_layout`. من المرجح أن يكون هذا ناتجًا عن عدم توافق بين إصدار `setuptools` وبيئة Python أو خيار قديم في عملية إعداد `pyperclip`. إليك كيفية إصلاحه:

### خطوات الحل

1.  **تحديث `setuptools` و `pip`**
    تأكد من أن لديك أحدث إصدارات `setsetuptools` و `pip`، حيث أن الإصدارات القديمة يمكن أن تسبب مشاكل في التوافق.

    ```bash
    pip install --upgrade pip setuptools
    ```

2.  **تثبيت إصدار محدد من `pyperclip`**
    قد يكون الخطأ ناتجًا عن إصدار قديم أو غير متوافق من `pyperclip`. جرب تثبيت إصدار مستقر ومحدد من `pyperclip`.

    ```bash
    pip install pyperclip==1.8.2
    ```

    إذا لم يعمل الإصدار `1.8.2`، يمكنك تجربة أحدث إصدار صراحةً:

    ```bash
    pip install pyperclip
    ```

3.  **استخدام خيار `--no-binary`**
    إذا فشلت عملية بناء العجلة (wheel)، يمكنك تجاوز ذلك عن طريق تثبيت توزيع المصدر مباشرة:

    ```bash
    pip install pyperclip --no-binary pyperclip
    ```

    هذا يجبر `pip` على التثبيت من المصدر بدلاً من محاولة بناء عجلة.

4.  **التحقق من توافق إصدار Python**
    تأكد من أن إصدار Python الخاص بك متوافق مع `pyperclip`. اعتبارًا من عام 2025، يدعم `pyperclip` Python 3.6 وما فوق، ولكن الإصدارات الأقدم قد تواجه مشاكل. تحقق من إصدار Python الخاص بك:

    ```bash
    python3 --version
    ```

    إذا كنت تستخدم إصدار Python قديم (مثل Python 3.5 أو إصدار سابق)، فقم بالترقية إلى إصدار أحدث (مثل Python 3.8+). يمكنك إدارة إصدارات Python باستخدام أدوات مثل `pyenv`.

5.  **مسح ذاكرة التخزين المؤقت لـ `pip`**
    يمكن أن تسبب ذاكرة التخزين المؤقتة لـ `pip` التالفة مشاكل. امسحها وحاول مرة أخرى:

    ```bash
    pip cache purge
    ```

6.  **استخدام بيئة افتراضية**
    لتجنب التعارضات مع حزم النظام، قم بإنشاء بيئة افتراضية:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install --upgrade pip setuptools
    pip install pyperclip
    ```

7.  **التراجع عن إصدار `setuptools` (إذا لزم الأمر)**
    إذا لم يحل تحديث `setuptools` المشكلة، جرب التراجع إلى إصدار معروف بأنه يعمل مع `pyperclip`. على سبيل المثال:

    ```bash
    pip install setuptools==59.6.0
    pip install pyperclip
    ```

8.  **التحقق من المشاكل الخاصة بالنظام**
    يشير الخطأ المذكور إلى `/usr/lib/python3/dist-packages`، مما يشير إلى أنك قد تستخدم تثبيت Python خاص بالنظام (على سبيل المثال، على Ubuntu). قد يكون لتثبيتات Python الخاصة بالنظام أذونات مقيدة أو تعارضات مع الحزم المثبتة عالميًا. يعد استخدام بيئة افتراضية (الخطوة 6) هي أفضل طريقة لتجنب ذلك. بدلاً من ذلك، تأكد من أن لديك أذونات لتثبيت الحزم:

    ```bash
    sudo pip install pyperclip
    ```

    ومع ذلك، تجنب استخدام `sudo`除非 كان ضروريًا، لأنه يمكن أن يعبث بـ Python الخاص بالنظام.

9.  **بديل: التثبيت عبر `apt` (Ubuntu/Debian)**
    إذا كنت تستخدم نظامًا قائمًا على Debian واستمر فشل `pip`، فيمكنك تثبيت `pyperclip` باستخدام مدير حزم النظام:

    ```bash
    sudo apt update
    sudo apt install python3-pyperclip
    ```

10. **مزيد من التصحيح**
    إذا لم ينجح أي مما سبق، تحقق من صفحة `pyperclip` على GitHub أو PyPI للاطلاع على المشكلات أو ملاحظات التوافق المعروفة. يمكنك أيضًا محاولة التثبيت من المصدر مباشرة:

    ```bash
    git clone https://github.com/asweigart/pyperclip.git
    cd pyperclip
    python3 setup.py install
    ```

### ملاحظات إضافية
- يشير الخطأ تحديدًا إلى `install_layout`، الذي تمت إزالته في الإصدارات الأحدث من `setuptools`. هذا يشير إلى أن سكريبت إعداد `pyperclip` قد يكون قديمًا أو غير متوافق مع إصدار `setuptools` الخاص بك.
- إذا كنت تعمل في بيئة محددة (مثل Docker أو WSL أو بناء مخصص لـ Python)، فتأكد من تثبيت جميع التبعيات مثل `build-essential` (لتجميع العجلات):

  ```bash
  sudo apt install build-essential python3-dev
  ```

- إذا استمرت المشكلة، قدم مزيدًا من السياق (مثل إصدار Python، ونظام التشغيل، وما إذا كنت تستخدم بيئة افتراضية) لمزيد من المساعدة.

### المراجع
- [Pyperclip GitHub](https://github.com/asweigart/pyperclip)
- [Setuptools Documentation](https://setuptools.pypa.io/en/latest/)
- [Pip Documentation](https://pip.pypa.io/en/stable/)