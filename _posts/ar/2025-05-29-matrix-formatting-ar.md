---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح تنسيق المصفوفات في مدونة جيكل
translated: true
type: note
---

المشكلة التي تواجهها تتعلق بكيفية معالجة Markdown (kramdown) للمحتوى قبل أن يقوم MathJax بعرضه. الشرطتان المائلتان للخلف (`\\`) في المصفوفة الخاصة بك يتم تفسيرهما بواسطة Markdown قبل أن يصل إليهما MathJax، مما يؤدي إلى كسر تنسيق المصفوفة.

إليك بعض الحلول لإصلاح هذا:

### الحل 1: تهريب الشرطات المائلة للخلف
يمكنك تهريب كل شرطة مائلة للخلف بشرطة مائلة للخلف أخرى:

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### الحل 2: استخدام `\\` داخل كتل الرياضيات
للرياضيات المعروضة (وليس داخل النص)، استخدم `$$` أو `\\\[ \\\]`:

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### الحل 3: استخدام وسوم HTML لمنع معالجة Markdown
لف الرياضيات في وسوم `div` في HTML لمنع معالجة Markdown:

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### الحل 4: تعديل إعدادات kramdown الخاصة بك
أضف هذا إلى ملف `_config.yml` الخاص بك لمنع kramdown من معالجة كتل الرياضيات:

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

ثم يمكنك استخدام:

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

جرب هذه الحلول واحدًا تلو الآخر لترى أيها يعمل بشكل أفضل مع إعداد Jekyll الخاص بك. الحل الأكثر موثوقية هو عادةً استخدام الرياضيات المعروضة (`$$` أو `\\\[ \\\]`) بدلاً من الرياضيات داخل النص (`$`) للمصفوفات والمعادلات المعقدة الأخرى.