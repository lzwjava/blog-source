---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ مسار الفئات في جافا
translated: true
type: note
---

الخطأ الذي واجهته (`Could not find or load main class scripts.benchmark.MultiMark`) حدث لأنك حاولت تشغيل برنامج Java من دليل المشروع الجذري (`~/projects/lzwjava.github.io`) باستخدام الاسم الكامل المحدد للفئة (`scripts.benchmark.MultiMark`)، لكن وقت تشغيل Java يتوقع تشغيل الفئة من الدليل الذي تبدأ فيه هيكلية الحزمة، أو أنك بحاجة إلى تحديد classpath بشكل صحيح. عندما انتقلت إلى دليل `scripts/benchmark` وقمت بتشغيل `java MultiMark`، عمل الأمر لأن الفئة كانت في الدليل الصحيح بالنسبة للأمر.

لتشغيل `MultiMark.java` أو `MultiMark.class` من دليل المشروع الجذري (`~/projects/lzwjava.github.io`) دون تغيير الأدلة، يمكنك استخدام خيار `-cp` (classpath) مع أمر `java` لإخبار Java بمكان العثور على ملف الفئة المترجم. إليك طريقتان لتحقيق هذا، مع بقائك في الدليل الجذري:

---

### **الخيار 1: تشغيل الفئة المترجمة باستخدام Classpath**
إذا كان `MultiMark.class` موجودًا بالفعل في `scripts/benchmark/` (كما هو موضح في ناتج `ls` الخاص بك)، يمكنك تشغيله من الدليل الجذري عن طريق تحديد classpath.

1. **ابق في الدليل الجذري**
   تأكد من أنك في `~/projects/lzwjava.github.io`.

2. **شغّل البرنامج**
   استخدم خيار `-cp` للإشارة إلى الدليل الذي يحتوي على ملف الفئة:
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` يخبر Java بالبحث عن الفئات في دليل `scripts/benchmark`.
   - `MultiMark` هو اسم الفئة (بدون `.class` أو بادئة الحزمة، حيث أن `MultiMark.java` لا يحتوي على بيان `package`).

   يجب أن ينتج عن هذا ناتجًا مثل:
   ```
   CPU cores: 32
   ...
   ```

3. **ملاحظة**: إذا كان `MultiMark.class` قديمًا أو مفقودًا، قم بترجمة ملف المصدر أولاً من الدليل الجذري:
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   ثم شغّل الأمر أعلاه.

---

### **الخيار 2: تشغيل ملف المصدر مباشرة باستخدام Classpath (Java 11+)**
إذا كنت تفضل تشغيل ملف المصدر مباشرة (مثل `python script.py`)، يمكنك استخدام أمر `java` مع مسار ملف المصدر، مع تحديد classpath.

1. **ابق في الدليل الجذري**
   تأكد من أنك في `~/projects/lzwjava.github.io`.

2. **شغّل ملف المصدر**
   استخدم:
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` يضبط classpath إلى الدليل الذي يحتوي على المصدر.
   - `scripts/benchmark/MultiMark.java` يحدد ملف المصدر ليتم ترجمته وتشغيله.

   يقوم هذا بترجمة وتشغيل `MultiMark.java` في خطوة واحدة، منتجًا نفس الناتج كما قبل.

---

### **الخيار 3: إنشاء سكريبت shell في الدليل الجذري**
لجعل الأمر أكثر ملاءمة (مثل تشغيل `./multimark` من الدليل الجذري)، يمكنك إنشاء سكريبت shell في الدليل الجذري (`~/projects/lzwjava.github.io`).

1. **أنشئ سكريبت Shell**
   أنشئ ملفًا باسم `multimark` في الدليل الجذري:
   ```bash
   nano multimark
   ```
   أضف:
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   احفظ واخرج.

2. **اجعله قابلًا للتنفيذ**
   ```bash
   chmod +x multimark
   ```

3. **شغّل السكريبت**
   من الدليل الجذري:
   ```bash
   ./multimark
   ```
   هذا يشغّل برنامج Java دون الحاجة إلى تغيير الأدلة.

4. **اختياري: الترجمة في السكريبت**
   إذا أردت أن يتعامل السكريبت مع الترجمة (مثلاً، إذا تغير ملف المصدر)، عدّل السكريبت:
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **ملاحظات رئيسية**
- **Classpath (`-cp`)**: خيار `-cp` يخبر Java بمكان العثور على الفئات أو ملفات المصدر. بما أن `MultiMark.java` لا يحتوي على بيان `package`، فإن اسم الفئة هو ببساطة `MultiMark`، وليس `scripts.benchmark.MultiMark`. إذا كان يحتوي على سطر `package scripts.benchmark;`، فستحتاج إلى استخدام `java -cp . scripts.benchmark.MultiMark` من الدليل الجذري.
- **إصدار Java**: تشغيل ملف المصدر مباشرة (`java scripts/benchmark/MultiMark.java`) يتطلب Java 11 أو أحدث. يبدو أن نظامك يحتوي على Java مثبتة، حيث أن الأمر عمل من دليل `scripts/benchmark`.
- **الدليل**: هذه الحلول تبقي في الدليل الجذري (`~/projects/lzwjava.github.io`)، متطابقة مع تفضيلك.
- **الأتمتة**: سكريبت shell (الخيار 3) هو الأقرب لتجربة تشبه Python، حيث يمكنك تشغيل `./multimark` مثل سكريبت Python. يمكنك أيضًا إضافته إلى `PATH` الخاص بك للوصول العالمي، لكن هذا اختياري.
- **معالجة الأخطاء**: إذا حصلت على أخطاء مثل `NoClassDefFoundError`، تأكد من وجود `MultiMark.class` في `scripts/benchmark/` أو أعد الترجمة. إذا لم يتم العثور على Java، تحقق من التثبيت (`java --version`).

إذا كنت تريد دمج هذا مع سكريبتات Python الخاصة بك أو تحتاج إلى سير عمل محدد (مثل تشغيل `multimark.py` و `MultiMark.java` معًا)، أعلمني!