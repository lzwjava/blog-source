---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح أخطاء تثبيت PyYAML
translated: true
type: note
---

### فهم الخطأ

يبدو هذا الناتج من أمر `python setup.py install` أو `pip install pyyaml` (من المصدر) على نظام Linux مزود بـ Python 3.13. هناك مشكلتان رئيسيتان:

1.  **فشل تجميع امتداد C**:
    *   تحاول عملية البناء تجميع امتداد C (`yaml._yaml`) ولكنها لا تستطيع العثور على ملف المصدر `yaml/_yaml.c`.
    *   يحدث هذا لأن الإصدارات الأحدث من PyYAML (بدءًا من حوالي الإصدار 4.x) تقوم بإنشاء ملف `_yaml.c` ديناميكيًا باستخدام Cython أثناء عملية البناء. لا يتضمن توزيع المصدر على PyPI ملف `.c` المُنشأ مسبقًا، لذا يجب تثبيت Cython مسبقًا لإنشائه.
    *   نتيجة لذلك، يتراجع إلى إصدار Python الخالص (الذي يعمل ولكنه أبطأ ويخلو من بعض الميزات مثل دعم libyaml).

2.  **رفض الإذن أثناء التثبيت**:
    *   يحاول التثبيت الكتابة في دليل Python العام للنظام (`/usr/local/lib/python3.13/dist-packages`)، الأمر الذي يتطلب صلاحيات root.
    *   هذا شائع عند التشغيل بدون `sudo` أو علم `--user`.

### الحلول

#### إصلاح مشكلة التجميع
قم بتثبيت Cython أولاً، ثم أعد محاولة تثبيت PyYAML. سيؤدي هذا إلى إنشاء ملف `_yaml.c` المفقود والسماح لامتداد C بالبناء.

*   **باستخدام pip (موصى به)**:
    ```
    pip install cython
    pip install pyyaml
    ```
    *   إذا كنت تريد امتداد C الأسرع مع دعم libyaml (يتطلب تثبيت libyaml-dev للنظام عبر مدير الحزم الخاص بك، على سبيل المثال `sudo apt install libyaml-dev` على Ubuntu/Debian):
        ```
        pip install cython libyaml
        pip install --upgrade --force-reinstall --no-cache-dir pyyaml
        ```

*   **إذا كنت تستخدم setup.py مباشرة** (غير موصى به، يُفضل استخدام pip):
    ```
    pip install cython
    python setup.py build_ext --inplace
    python setup.py install
    ```

ملاحظة: Python 3.13 جديد نسبيًا، لذا تأكد من استخدام أحدث إصدار من Cython (مثل 3.0.11 أو أحدث) لضمان التوافق. إذا كنت تستخدم إصدار Python المجاني الخيوط (free-threaded)، فقد تكون هناك حاجة إلى تعديلات إضافية في التجميع — تحقق من مشكلات PyYAML على GitHub للحصول على التحديثات.

#### إصلاح مشكلة الإذن
*   **التثبيت في دليل المستخدم** (الأكثر أمانًا، لا حاجة لـ sudo):
    ```
    pip install --user cython pyyaml
    ```
    *   هذا يثبت في `~/.local/lib/python3.13/site-packages`.

*   **استخدم sudo للتثبيت على مستوى النظام** (استخدم بحذر، حيث قد يتعارض مع مديري الحزم):
    ```
    sudo pip install cython pyyaml
    ```

*   **أفضل ممارسة: استخدم بيئة افتراضية**:
    لتجنب مشاكل الأذونات تمامًا:
    ```
    python -m venv myenv
    source myenv/bin/activate  # On Linux/Mac
    pip install cython pyyaml
    ```
    هذا يحافظ على عزل كل شيء.

بعد التثبيت، اختبر باستخدام `python -c "import yaml; print(yaml.__version__)"`. إذا تم الاستيراد بدون أخطاء، فأنت على ما يرام.

إذا لم تحل هذه الحلول المشكلة (على سبيل المثال، بسبب خصوصية في Python 3.13)، قدم المزيد من التفاصيل مثل الأمر الدقيق الذي تستخدمه وإصدار نظام التشغيل.

[Building on Mac - _yaml.c not found](https://github.com/yaml/pyyaml/issues/122)  
[extension _yaml is not built](https://github.com/yaml/pyyaml/issues/179)  
[Installing Pyyaml with libyaml support on MacOS](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)