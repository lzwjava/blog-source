---
audio: false
generated: true
lang: ar
layout: post
title: استكشاف أخطاء مشكلة ماث جاكس وإصلاحها
translated: true
type: note
---

يبدو أن تهيئة MathJax الخاصة بك لا تعمل كما هو متوقع. دعنا نحدد المشكلة ونصلحها بناءً على الكود الذي قدمته.

### التهيئة الحالية لديك
لديك إعداد MathJax التالي:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\[","\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

تهدف هذه التهيئة إلى:
- عرض الرياضيات المضمنة بين محددات `\( ... \)`.
- عرض الرياضيات المعروضة بين محددات `$$ ... $$` أو `\[ ... \]`.
- تمكين كسر الأسطر التلقائي للمعادلات الطويلة.
- تحجيم مخرجات الرياضيات إلى 85% من الحجم باستخدام معالج المخرجات CommonHTML.
- ترقيم المعادلات تلقائيًا باستخدام نمط AMS.

ومع ذلك، فقد أبلغت أنها "لا تعمل"، مما قد يعني أن الرياضيات لا تُعرض، أو أن ميزات معينة (مثل كسر الأسطر) لا تعمل كما هو متوقع.

### المشكلة
تكمن المشكلة الأساسية في تهيئة محددات `displayMath`:

```javascript
displayMath: [ ['$$','$$'], ["\[","\]"] ]
```

في JavaScript، يتم تفسير السلسلة `"["` حرفيًا كـ `[`، لأن `\[` ليس تسلسل هروب خاص—إنه مجرد شرطة مائلة متبوعة بقوس. وبالمثل، تصبح `"\]"` `]`. نتيجة لذلك، تم تكوين MathJax للتعرف على `[ ... ]` كمحددات للرياضيات المعروضة، **وليس** `\[ ... \]`. بما أن تعبيرات الرياضيات الخاصة بك (مثل العينة `\[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]`) تستخدم `\[ ... \]`، فإن MathJax لن تتعرف عليها كرياضيات معروضة مع الإعداد الحالي.

محددات الرياضيات المضمنة `["\\(","\\)"]` صحيحة، لأن `\\(` و `\\)` في سلسلة JavaScript تمثل `\(` و `\)`—محددات LaTeX القياسية للرياضيات المضمنة. ومع ذلك، تحتاج محددات الرياضيات المعروضة إلى تعديل.

### الحل
لإصلاح هذا، قم بتحديث تهيئة `displayMath` بحيث تتعرف MathJax بشكل صحيح على `\[ ... \]` كمحددات للرياضيات المعروضة. في JavaScript، لتمثيل السلسلة `\[`، تحتاج إلى كتابة `"\\["`، لأنه يجب تهريب كل شرطة مائلة. وبالمثل، تصبح `\]` `"\\]"`. إليك التهيئة المصححة:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

#### التغيير الرئيسي
- تم تغيير `["\[","\]"]` إلى `["\\[","\\]"]` في مصفوفة `displayMath`.
- يضمن هذا تعيين المحددات إلى `\[ ... \]` (و `$$ ... $$`)، بما يتطابق مع ترميز LaTeX القياسي.

### اعتبارات إضافية
1. **مشاكل كسر الأسطر**: لقد ذكرت أن بعض التعبيرات طويلة جدًا وتفيض، خاصة في العروض المحمولة. يجب أن يتولى إعداد `linebreaks: { automatic: true }` في معالج مخرجات "CommonHTML" هذا، ولكنه يتطلب أن تكون الرياضيات داخل حاوية بعرض محدد (مثل `width: 100%`). تأكد من أن بنية HTML الخاصة بك تتضمن شيئًا مثل:

   ```html
   <div style="width: 100%; overflow-x: auto;">
     \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   </div>
   ```

   هذا يسمح لـ MathJax بكسر الأسطر بناءً على عرض الحاوية، والتكيف مع حجم الشاشة.

2. **معالج المخرجات**: يقوم البرنامج النصي الخاص بك بتحميل `TeX-MML-AM_CHTML`، الذي يستخدم CommonHTML كمخرجات افتراضية. سيتم تطبيق إعدادات `"CommonHTML"` (مثل `scale: 85`، `linebreaks: { automatic: true }`)، ولكن إعدادات `"HTML-CSS"` قد لا تُطبق، لأن معالج المخرجات هذا غير نشط. بما أن CommonHTML حديث ومدعوم على نطاق واسع، فهذا جيد—فقط تأكد من أن إعداداتك تتماشى معه.

3. **الاختبار**: بعد تحديث التهيئة، اختبر باستخدام تعبيرك النموذجي:

   ```html
   \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   ```

   يجب أن تُعرض الآن بشكل صحيح كرياضيات معروضة مع كسر أسطر مناسب إذا لزم الأمر.

4. **توافق المتصفح**: يجب أن يعمل MathJax 2.7.7 في معظم المتصفحات الحديثة. إذا استمرت المشاكل، تأكد من عدم وجود أخطاء JavaScript في وحدة التحكم أو قواعد CSS متضاربة (مثل `white-space: nowrap`) تتجاوز عرض الرياضيات.

### الكود المصحح النهائي
إليك الإعداد الكامل والمصحح:

```html
<!-- MathJax Configuration -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<!-- Load MathJax -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<!-- Example Math -->
<div style="width: 100%; overflow-x: auto;">
  \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
</div>
```

### لماذا يعمل هذا
- **إصلاح المحددات**: `["\\[","\\]"]` يضمن أن MathJax تتعرف على `\[ ... \]` كرياضيات معروضة، بما يتطابق مع محتواك.
- **كسر الأسطر**: إعدادات `CommonHTML` مع حاوية مناسبة تمكن كسر الأسطر التلقائي للتعبيرات الطويلة.
- **العرض**: يضمن البرنامج النصي من CDN والتهيئة معًا معالجة الرياضيات وعرضها بشكل صحيح.

قم بتحديث الكود الخاص بك بهذا الإصلاح، ويجب أن يعمل إعداد MathJax الخاص بك كما هو مقصود! إذا استمرت المشاكل، يرجى مشاركة أمثلة محددة لتعبيرات الرياضيات التي تفشل أو أي رسائل خطأ تواجهها.

---

لتكوين MathJax لعرض التعبيرات الرياضية في المحتوى المقدم بشكل جيد، تحتاج إلى التأكد من أنها تتعامل بشكل صحيح مع تعبيرات الرياضيات المضمنة مثل \( T_p \) و \( 2 \times T_p \)، المحاطة بمحددات LaTeX. يستخدم المحتوى `\( ... \)` للرياضيات المضمنة، وبينما لا يتضمن رياضيات معروضة (مثل المعادلات في أسطر منفصلة)، فإنه من الجيد تكوين MathJax لكل من الرياضيات المضمنة والمعروضة لتحقيق المرونة. فيما يلي دليل خطوة بخطوة لتحقيق ذلك.

### الخطوة 1: تضمين MathJax في HTML الخاص بك
أولاً، تحتاج إلى تحميل مكتبة MathJax. يمكنك استخدام شبكة توصيل المحتوى (CDN) لتضمينها في ملف HTML الخاص بك. أضف وسم البرنامج النصي التالي إلى `<head>` في HTML الخاص بك أو قبل المحتوى الذي يحتوي على الرياضيات:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

يقوم هذا بتحميل MathJax الإصدار 2.7.9 مع تهيئة `TeX-AMS_CHTML`، التي تدخل إدخال LaTeX وتعرض الرياضيات كـ HTML مع CSS، وهو مناسب لمعظم تطبيقات الويب.

### الخطوة 2: تكوين محددات MathJax
يحتاج MathJax إلى معرفة المحددات التي يجب التعرف عليها لتعبيرات الرياضيات. يستخدم المحتوى `\( ... \)` للرياضيات المضمنة، وهو محدد LaTeX قياسي. للتأكد من أن MathJax تعالج هذه بشكل صحيح، أضف برنامجًا نصيًا للتهيئة قبل برنامج مكتبة MathJax. إليك تهيئة أساسية:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    }
  });
</script>
```

- **`inlineMath`**: يخبر MathJax بالتعامل مع النص بين `\( ... \)` كرياضيات مضمنة. الأقواس المزدوجة `[ ['\\(', '\\)'] ]` مستخدمة لأن MathJax تقبل مصفوفة من أزواج المحددات.
- **`displayMath`**: يهيئ MathJax للتعرف على `$$ ... $$` و `\[ ... \]` كرياضيات معروضة، حتى لو أن المحتوى الحالي لا يستخدمها. يضمن هذا التوافق مع المحتوى المستقبلي.
- **`processEscapes`**: يسمح بتهريب المحددات (مثل استخدام `\$` لعرض علامة الدولار حرفيًا)، على الرغم من أنه ليس حاسمًا لهذا المحتوى المحدد.

### الخطوة 3: تحسين العرض للتجاوب
لجعل الرياضيات المعروضة قابلة للتكيف مع أحجام الشاشات المختلفة (مثل منع الفيض في الأجهزة المحمولة)، قم بتمكين كسر الأسطر التلقائي للتعبيرات الطويلة. قم بتحديث التهيئة هكذا:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
```

- **`HTML-CSS`, `CommonHTML`, `SVG`**: هذه هي معالجات المخرجات التي يستخدمها MathJax لعرض الرياضيات. تمكين `linebreaks: { automatic: true }` يضمن أن التعبيرات الطويلة تلف بشكل طبيعي، على الرغم من أن التعبيرات في هذا المحتوى (\( T_p \), \( 2 \times T_p \)) قصيرة وغير مرجح أن تحتاج إلى اللف.

### الخطوة 4: اجمع كل شيء معًا
إليك الإعداد الكامل المطلوب تضمينه في ملف HTML الخاص بك قبل المحتوى:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

### الخطوة 5: تحقق من عرض المحتوى بشكل صحيح
مع هذه التهيئة، سيتم عرض الرياضيات المضمنة في محتواك—مثل \( T_p \) و \( 2 \times T_p \)—كتعبيرات رياضية منسقة بشكل صحيح. على سبيل المثال:
- \( T_p \) تصبح متغيرًا منخفضًا.
- \( 2 \times T_p \) تعرض مع رمز الضرب (×) والمتغير المنخفض \( T_p \).

### ملاحظات إضافية
- **لا توجد رياضيات معروضة**: بما أن محتواك يستخدم فقط الرياضيات المضمنة، فإن إعدادات `displayMath` ليست ضرورية تمامًا ولكنها مُضمنة للاكتمال.
- **تنسيق CSS**: تأكد من أن حاوية HTML لمحتواك (مثل `<div>`) لديها `width: 100%` أو تنسيق مناسب للحفاظ على التخطيط متجاوبًا.
- **الاختبار**: بعد إضافة هذه التهيئة، قم بتحميل صفحتك في متصفح لتأكيد أن \( T_p \) و \( 2 \times T_p \) تُعرض كما هو متوقع.

يضمن هذا الإعداد عرض MathJax للتعبيرات الرياضية في شرح CSMA/CD الخاص بك بوضوح واحترافية، مما يعزز قابلية القراءة للمستخدمين.

---

لإصلاح مشاكل عرض MathJax مع الأقواس `\(...\)` ومحددات LaTeX الأخرى، اضبط تهيئتك لتهريب الشرطات المائلة بشكل صحيح في سلاسل JavaScript. إليك الإعداد المصحح:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],  // Correctly escaped for JavaScript
      displayMath: [ ['$$','$$'], ['\\[','\\]'] ],  // Fixed escaping for \[ and \]
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

### الإصلاحات الرئيسية:
1. **الشرطات المائلة المهربة**:
   - تم تغيير `["\\(","\\)"]` إلى `['\\(','\\)']` (علامات الاقتباس المفردة تتجنب التهريب الإضافي).
   - تم إصلاح `["\[","\]"]` إلى `['\\[','\\]']` لضمان عمل `\[...\]` للمعادلات المعروضة.

2. **التوصيات**:
   - استخدم `'$$...$$'` أو `\\[...\\]` للمعادلات المعروضة.
   - استخدم `\\(...\\)` للمعادلات المضمنة.
   - تأكد من عدم وجود معالجات Markdown متضاربة تغير LaTeX الخاص بك.

### مثال للاستخدام:
```html
<p>Inline math: \( E = mc^2 \).</p>

<p>Display math:</p>
\[
  \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}
\]
```

تضمن هذه التهيئة أن MathJax تحلل جميع محددات LaTeX بشكل صحيح.

---

أفهم أنك تستخدم Jekyll مع Kramdown لعرض منشورات Markdown وتريد تكوين MathJax لعرض التعبيرات الرياضية بشكل صحيح. لقد قدمت تهيئة MathJax وأشرت إلى أنك تعرض الرياضيات داخل منشورات Markdown، وليس وسوم HTML. دعنا نتأكد من أن MathJax تعمل بسلاسة مع إعدادك.

### إعدادك الحالي
أنت تستخدم:
- **Jekyll مع Kramdown**: Kramdown هو محلل Markdown الافتراضي لـ Jekyll ويدعم تعبيرات الرياضيات بأسلوب LaTeX.
- **MathJax**: تحدد تهيئتك محددات للرياضيات المضمنة والمعروضة:
  - مضمنة: `\( ... \)`
  - معروضة: `$$ ... $$` و `\[ ... \]`

لقد قمت أيضًا بتضمين برنامج نصي `marked.min.js`، على الرغم من أنه على الأرجح غير ذي صلة لأن Jekyll تعرض Markdown من جانب الخادم باستخدام Kramdown، وليس من جانب العميل.

### لماذا قد لا يعمل العرض
يحتاج Kramdown و MathJax إلى التوافق حول كيفية التعامل مع محددات الرياضيات. إعداد MathJax الخاص بك يتعرف على `\( ... \)` للرياضيات المضمنة وكل من `$$ ... $$` و `\[ ... \]` للرياضيات المعروضة. ومع ذلك، قد لا يمرر السلوك الافتراضي لـ Kramdown كل هذه المحددات إلى MathJax بشكل صحيح ما لم يتم تكوينه بشكل صحيح، خاصة إذا ظهرت مشاكل تهريب في Markdown.

### الحل: تكوين MathJax مع Kramdown
إليك كيفية جعلها تعمل:

#### 1. تكوين Kramdown في Jekyll
تأكد من أن ملف Jekyll `_config.yml` الخاص بك يمكّن MathJax كمحرك رياضيات لـ Kramdown. أضف أو تحقق من التالي:

```yaml
markdown: kramdown
kramdown:
  math_engine: mathjax
```

يخبر هذا Kramdown بمعالجة تعبيرات الرياضيات وتمريرها إلى MathJax. بشكل افتراضي، يتعرف Kramdown على:
- `\( ... \)` للرياضيات المضمنة.
- `$$ ... $$` للرياضيات المعروضة.

بينما يدعم إعداد MathJax الخاص بك أيضًا `\[ ... \]` للرياضيات المعروضة، فإن Kramdown لا يستخدم هذا المحدد أصلاً، مما قد يسبب مشاكل ما لم يتم التعامل معه بشكل صحيح.

#### 2. استخدام محددات رياضيات متسقة في Markdown
لتجنب الارتباك أو مشاكل التهريب، التزم بمحددات Kramdown الافتراضية في منشورات Markdown الخاصة بك:
- **الرياضيات المضمنة**: استخدم `\( ... \)`.
  مثال: `This is inline: \( E = mc^2 \)` يُعرض كـ "This is inline: \( E = mc^2 \)".
- **الرياضيات المعروضة**: استخدم `$$ ... $$`.
  مثال:
  ```markdown
  $$
  \int_0^1 x^2 \, dx = \frac{1}{3}
  $$
  ```
  يُعرض هذا كمعادلة في الوسط: \( \int_0^1 x^2 \, dx = \frac{1}{3} \).

إذا كنت تفضل `\[ ... \]`، يمكنك استخدامها، ولكن تهريب الشرطة المائلة في Markdown قد يتطلب عناية إضافية (مثل `\\[ ... \\]`). ومع ذلك، فإن `$$ ... $$` أبسط ويتوافق مع إعدادات Kramdown الافتراضية، مما يقلل من الأخطاء المحتملة.

#### 3. تبسيط تهيئة MathJax الخاصة بك
بما أن Kramdown تعالج الرياضيات مسبقًا، يمكن لتهيئة MathJax الخاصة بك أن تركز على العرض. إليك نسخة مبسطة بناءً على إعدادك:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],
      displayMath: [ ['$$','$$'] ], // Stick to $$ for simplicity
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

- لقد قمت بإزالة `['\\[','\\]']` من `displayMath` لتتوافق مع تفضيل Kramdown لـ `$$ ... $$`. إذا كنت لا تزال تريد `\[ ... \]`، فاحتفظ بها، ولكن اختبرها بدقة.
- تمت إزالة `"HTML-CSS"` لأن `"CommonHTML"` كافية لعرض MathJax الحديث.

ضع هذا في قسم `<head>` في تخطيط Jekyll الخاص بك.

#### 4. إزالة البرامج النصية غير الضرورية
لقد قمت بتضمين `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>`، لكن Jekyll يستخدم Kramdown من جانب الخادم، لذا فإن Marked.js (محلل من جانب العميل) ليس مطلوبًا إلا إذا كنت تقوم بشيء محدد به. إذا لم يكن الأمر كذلك، قم بإزالته لتجنب التعارضات أو الارتباك المحتمل.

#### 5. اختبر إعدادك
أضف هذه الأمثلة إلى منشور Markdown لتأكيد أن العرض يعمل:
- مضمنة: `The energy is \( E = mc^2 \).`
- معروضة:
  ```markdown
  $$
  \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bps}
  $$
  ```

شغّل `jekyll serve`، وافتح الموقع في متصفحك، وتحقق مما إذا كانت الرياضيات تُعرض بشكل صحيح. إذا لم تكن كذلك، فافحص وحدة تحكم المتصفح للبحث عن أخطاء MathJax.

### ملاحظات نهائية
- **الاتساق**: استخدام `\( ... \)` و `$$ ... $$` يضمن التوافق بين Kramdown و MathJax دون متاعب تهريب إضافية.
- **استكشاف الأخطاء وإصلاحها**: إذا كانت الرياضيات لا تزال لا تُعرض، تحقق من:
  - تحميل برامج MathJax النصية بدون أخطاء (تحقق من وحدة تحكم المتصفح).
  - اكتمال بناء Jekyll بنجاح.
  - عدم وجود أخطاء إملائية في المحددات أو التهيئة.

يجب أن يعرض هذا الإعداد تعبيرات الرياضيات الخاصة بك بشكل جميل في منشورات Jekyll Markdown! دعني أعرف إذا واجهت مشاكل محددة مع الأمثلة التي تحاول عرضها.