---
audio: true
generated: true
lang: ar
layout: post
title: تبيان الاعتماديات
translated: true
---

للتحويل الرسوم البيانية للمتطلبات التي تنتجها النص البرمجي المقدم، يمكنك استخدام **Graphviz**، أداة رسومية شائعة ومبسطة تستخدم لغة DOT لتوضيح الرسوم البيانية. ينتج النص البرمجي رسوم بيانية للمتطلبات في صيغة DOT، تمثل العلاقات بين الوحدات في مشروع Maven الخاص بك كرسوم بيانية موجهة، مع العقد المسماة بـ `artifactId`s والأحرف التي تظهر العلاقات بين المتطلبات. أدناه خطوات رسم وتوضيح هذه الرسوم البيانية باستخدام Graphviz، مع ذكر أدوات بديلة مثل Polyglot أو غيرها إذا كنت تفضل خيارات مختلفة.

---

### باستخدام Graphviz (الطريقة الموصى بها)

Graphviz مثالي هنا لأن النص البرمجي ينتج مباشرة مخرجات في صيغة DOT، والتي يدعمها Graphviz بشكل طبيعي. اتبع هذه الخطوات:

1. **تنفذ النص البرمجي**
   تنفذ النص البرمجي، وتقدم مجلد الجذر لمشروع Maven الخاص بك كحجة. هذا ينتج المخرجات DOT للرسوم البيانية للمتطلبات.
   ```bash
   python script.py /path/to/maven/project
   ```

2. **حفظ المخرجات DOT في ملف**
   احدث المخرجات النص البرمجي إلى ملف، على سبيل المثال، `dependencies.dot`. سيحتوي هذا الملف على وصف الرسوم البيانية في صيغة DOT.
   ```bash
   python script.py /path/to/maven/project > dependencies.dot
   ```

3. **تثبيت Graphviz (إذا لم يكن مثبتًا بالفعل)**
   Graphviz متاح على Windows، macOS، وLinux. قم بتثبيته باستخدام مدير الحزم الخاص بك:
   - **Ubuntu/Debian**:
     ```bash
     sudo apt-get install graphviz
     ```
   - **macOS (مع Homebrew)**:
     ```bash
     brew install graphviz
     ```
   - **Windows**: قم بتنزيل وتثبيت من [موقع Graphviz](https://graphviz.org/download/).

4. **إنشاء صورة مرئية**
   استخدم الأمر `dot` من Graphviz لتحويل ملف DOT إلى صورة. على سبيل المثال، لإنشاء ملف PNG:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   - يمكنك استبدال `-Tpng` بأشكال أخرى مثل `-Tsvg` لـ SVG أو `-Tpdf` لـ PDF، حسب تفضيلك.

5. **عرض الرسوم البيانية**
   افتح الملف المولد `dependencies.png` باستخدام أي مشاهد صور لرؤية الرسوم البيانية للمتطلبات. سيمثل كل عقد وحدة `artifactId`، وسهمات تشير إلى العلاقات بين الوحدات.

---

### أدوات بديلة

إذا كنت لا تريد استخدام Graphviz أو تريد استكشاف أدوات رسومية شائعة أخرى، إليك بعض الخيارات:

#### Polyglot Notebooks (مثل Jupyter)
Polyglot Notebooks لا توضيح مباشرة ملفات DOT، ولكن يمكنك دمج Graphviz في بيئة Jupyter notebook:
- **الخطوات**:
  1. قم بتثبيت Graphviz وحزمة Python `graphviz`:
     ```bash
     pip install graphviz
     sudo apt-get install graphviz  # For Ubuntu, adjust for your OS
     ```
  2. قم بتعديل النص البرمجي لاستخدام مكتبة Python `graphviz` بدلاً من طباعة DOT الخام. أضف هذا في نهاية النص البرمجي الخاص بك:
     ```python
     from graphviz import Digraph

     dot = Digraph()
     for from_module, to_module in sorted(dependencies):
         dot.edge(from_module, to_module)
     dot.render('dependencies', format='png', view=True)
     ```
  3. تنفذ النص البرمجي المعدل لإنشاء وتوضيح `dependencies.png` مباشرة.
- **ملاحظة**: هذا لا يزال يعتمد على Graphviz تحت السطح، لذا فهو ليس أداة منفصلة تمامًا.

#### Gephi
Gephi هو أداة توضيح شبكات مفتوحة المصدر يمكن أن تستورد ملفات DOT:
- **الخطوات**:
  1. قم بتنزيل وتثبيت Gephi من [gephi.org](https://gephi.org/).
  2. تنفذ النص البرمجي وحفظ المخرجات DOT في `dependencies.dot`.
  3. افتح Gephi، انتقل إلى `File > Import > Graph File`، واختار `dependencies.dot`.
  4. قم بتعديل التكوين (مثل ForceAtlas 2) وتوضيحها بشكل تفاعلي.
- **المزايا**: ممتازة للرسوم البيانية الكبيرة مع خيارات التكوين المتقدمة.
- **العيوب**: تتطلب استيراد وتكوين يدوي.

#### أدوات Graphviz عبر الإنترنت
لخيار سريع لا يتطلب تثبيت:
- **الخطوات**:
  1. تنفذ النص البرمجي ونقل المخرجات DOT (من `digraph G {` إلى `}`).
  2. زور أداة عبر الإنترنت مثل [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/).
  3. قم بتسجيل DOT واضغط لتوضيح الرسوم البيانية.
- **المزايا**: لا يتطلب تثبيت.
- **العيوب**: يتطلب اتصال بالإنترنت؛ أقل تحكم على صيغة المخرجات.

#### yEd
yEd هو محرر رسوم بيانية مجاني، ولكن لا يدعم DOT بشكل طبيعي:
- **الخطوات**:
  1. قم بتحويل ملف DOT إلى GraphML أو صيغة أخرى مدعومة باستخدام أداة مثل `dot` (على سبيل المثال، `dot -Tgraphml dependencies.dot -o dependencies.graphml`).
  2. افتح yEd، استورد ملف GraphML، وتعديل التكوين.
- **العيوب**: خطوة تحويل إضافية مطلوبة.

---

### لماذا Graphviz أفضل هنا
مخرجات النص البرمجي مخصصة لـ DOT، مما يجعل Graphviz الخيار الأكثر مباشرة وفاعلية. هو خفيف الوزن، يدعمه سطر الأوامر، ويستخدمه العديد. ستظهر الرسوم البيانية مثل هذا (مفهوميًا):
- العقد: `artifactId` لكل وحدة (على سبيل المثال، `"module-a"`, `"module-b"`).
- الحروف: أسهم مثل `"module-a" -> "module-b"`, تشير إلى أن `module-a` تعتمد على `module-b`.

إذا كانت رسومك البيانية كبيرة، يمكنك تعديل التكوين مع خيارات Graphviz (على سبيل المثال، `dot -Kneato` لتكوين مختلف)، ولكن الخطوات الأساسية أعلاه يجب أن تكفي.

---

### التوصية النهائية
لتوضيح الرسوم البيانية للمتطلبات من النص البرمجي الخاص بك:
1. تنفذ: `python script.py /path/to/maven/project > dependencies.dot`
2. قم بتثبيت Graphviz إذا لزم الأمر.
3. قم بتحويل إلى صورة: `dot -Tpng dependencies.dot -o dependencies.png`
4. افتح `dependencies.png` لرؤية رسومك البيانية.

هذه الطريقة بسيطة، تستخدم أداة شائعة (Graphviz)، وتوافق تمامًا مع مخرجات النص البرمجي الخاص بك. إذا كنت تحتاج إلى تفاعلية أو صيغ بديلة، حاول Gephi أو أداة عبر الإنترنت بدلاً من ذلك.