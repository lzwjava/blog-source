---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح أخطاء يامِل والملفات في جيكيل
translated: true
type: note
---

يُظهر الناتج الذي قدمته نوعين من الأخطاء:

1.  **استثناء YAML:** يشير هذا إلى وجود مشكلة في front matter (كتلة YAML في الأعلى) لملفات Markdown الخاصة بك:

      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        يشير الخطأ "did not find expected key while parsing a block mapping at line 2 column 1" إلى أن بناء جملة YAML في هذه الملفات غير صحيح، على الأرجح مفتاح مفقود أو مشكلة في المسافة البادئة في front matter.

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`**: يشير هذا الخطأ إلى أن Jekyll يحاول الوصول إلى ملف أو دليل غير موجود، تحديدًا `/wandb/debug-internal.log`. قد يكون هذا ملفًا مؤقتًا أو تبعية من أداة أخرى (مثل Weights & Biases - `wandb`) يحاول Jekyll معالجتها.

للإجابة على سؤالك حول كيفية جعل Jekyll يتجاهل بعض الأدلة، يمكنك استخدام الخيار `exclude` في ملف `_config.yml` الخاص بك.

إليك كيفية القيام بذلك:

1.  **افتح ملف `_config.yml`** (موجود في المجلد الجذري لمشروع Jekyll الخاص بك).

2.  **أضف أو عدل التوجيه `exclude`.** يأخذ هذا التوجيه مصفوفة من المسارات (ملفات أو أدلة) يجب على Jekyll تجاهلها أثناء عملية البناء.

    على سبيل المثال، لتجاهل دليل `wandb` وأي أدلة أخرى تريد استبعادها، أضف ما يلي إلى `_config.yml` الخاص بك:

    ```yaml
    exclude:
      - wandb/
      - some_other_directory/
      - another_file_to_ignore.md
    ```

    **ملاحظات مهمة:**

      * تأكد من تضمين الشرطة المائلة الأخيرة (`/`) للأدلة لضمان تجاهل كل المحتوى بداخلها.
      * المسارات تكون نسبية بالنسبة للمجلد الجذري لمشروع Jekyll الخاص بك.

**معالجة الأخطاء المحددة لديك باستخدام `exclude`:**

  * **لخطأ دليل `wandb`:** إضافة `wandb/` إلى قائمة `exclude` في `_config.yml` يجب أن تمنع Jekyll من محاولة قراءة الملفات بداخله، مما يحل خطأ `No such file or directory` لـ `wandb/debug-internal.log`.

  * **لاستثناء YAML:** التوجيه `exclude` لن يصلح أخطاء YAML في ملفات Markdown الخاصة بك. تحتاج إلى **تصحيح front matter يدويًا** في `notes/2025-06-25-company-valuation-comparison-en.md` و `notes/2025-06-25-top-companies-evolve-en.md`.

    **هيكل front matter النموذجي لـ Jekyll:**

    ```yaml
    ---
    layout: post
    title: "My Awesome Post"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    محتواك يذهب هنا.
    ```

    راجع الملفات المذكورة في استثناء YAML للتأكد من أنها تتبع هذا الهيكل، خاصة فيما يتعلق بالمسافة البادئة وأزواج المفتاح-القيمة الصحيحة. يشير الخطأ "did not find expected key while parsing a block mapping at line 2 column 1" إلى وجود خطأ ما في بداية front matter الخاص بك، ربما مفتاح مفقود أو مسافة إضافية حيث يجب أن يكون المفتاح.

بعد إجراء هذه التغييرات على `_config.yml` الخاص بك وتصحيح ملفات Markdown الخاصة بك، حاول تشغيل أمر بناء أو تشغيل Jekyll الخاص بك مرة أخرى.