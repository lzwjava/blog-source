---
audio: false
generated: true
lang: ar
layout: post
title: التقديم باستخدام Markdown مع MathJax أو KaTeX
translated: true
type: note
---

لدمج عرض معادلات LaTeX الرياضية مع عرض **Markdown** على صفحة ويب، تستخدم عادةً مكتبة جافا سكريبت (مثل **MathJax** أو **KaTeX**) إلى جانب محلل Markdown يمكنه معالجة صيغة Markdown القياسية. الهدف هو السماح للمستخدمين بكتابة الصيغ الرياضية بـ LaTeX داخل Markdown وعرضها بشكل صحيح على الصفحة.

إليك كيف يمكنك تحقيق ذلك:

### 1. **عرض Markdown مع MathJax أو KaTeX**

يمكنك استخدام **محلل Markdown** مثل **marked.js** أو **remarkable.js** لعرض محتوى Markdown الأساسي. ثم، بعد عرض محتوى Markdown، استخدم MathJax أو KaTeX لعرض معادلات LaTeX الرياضية بداخله.

فيما يلي نهج خطوة بخطوة لتحقيق ذلك.

---

### **الخطوة 1: تضمين المكتبات**

تحتاج إلى تضمين كل من **محلل Markdown** و **مكتبة عرض الرياضيات** (MathJax أو KaTeX) في ملف HTML الخاص بك.

إليك كيف يمكنك تضمينهم:

```html
<!-- تضمين KaTeX (أو MathJax) لعرض LaTeX -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- تضمين محلل Markdown (مثل marked.js) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

بدلاً من ذلك، إذا كنت تفضل **MathJax** بدلاً من KaTeX، يمكنك تضمين MathJax هكذا:

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **الخطوة 2: إعداد عملية عرض Markdown إلى LaTeX**

الآن، يمكنك كتابة هيكل HTML الخاص بك واستخدام جافا سكريبت لعرض Markdown ثم معالجة أي صيغ LaTeX داخل ذلك Markdown.

إليك مثالًا بسيطًا:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown + Math Rendering</title>

  <!-- تضمين KaTeX لعرض الرياضيات -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- تضمين marked.js لعرض Markdown -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>مثال عرض Markdown + الرياضيات</h1>

  <!-- Textarea لإدخال Markdown -->
  <textarea id="markdownInput" rows="10" cols="50">
هذا محرر Markdown. يمكنك إضافة صيغ LaTeX الرياضية هكذا:

الرياضيات المضمنة في السطر: \( E = mc^2 \)

الرياضيات في كتلة منفصلة:
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- حاوية لعرض Markdown المُصيَّر -->
  <div id="markdownOutput"></div>

  <script>
    // دالة لعرض Markdown + الرياضيات
    function renderMarkdown() {
      // الحصول على Markdown المدخل
      const markdownText = document.getElementById('markdownInput').value;

      // عرض محتوى Markdown
      const htmlContent = marked(markdownText);

      // إدخال HTML المُصيَّر في div الإخراج
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // عرض الرياضيات داخل محتوى HTML باستخدام KaTeX
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // رياضيات مضمنة في السطر
          { left: "\\[", right: "\\]", display: true }   // رياضيات في كتلة منفصلة
        ]
      });
    }

    // استدعاء دالة renderMarkdown عند تحميل الصفحة وعندما يغير المستخدم المدخلات
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **شرح الكود:**

1. **تحليل Markdown:**
   - تُستخدم مكتبة `marked.js` لتحويل Markdown المدخل (المكتوب في `<textarea>`) إلى HTML. سيتم معالجة صيغة Markdown وتحويلها إلى HTML في الحاوية `<div id="markdownOutput"></div>`.

2. **عرض الرياضيات:**
   - يتم عرض معادلات LaTeX في Markdown (المضمنة `\( ... \)` والكتلة المنفصلة `\[ ... \]`) باستخدام دالة `renderMathInElement()` الخاصة بـ **KaTeX**.
   - تبحث **KaTeX** عن `\( ... \)` للرياضيات المضمنة في السطر و `\[ ... \]` للرياضيات في كتلة منفصلة في محتوى HTML وتقوم بعرضها تلقائيًا.

3. **محرر Markdown التفاعلي:**
   - بينما يقوم المستخدم بالكتابة في `<textarea>`، يتم استدعاء الدالة `renderMarkdown` لتحديث المحتوى ديناميكيًا، وتحليل Markdown وعرض صيغ LaTeX.

---

### **الخطوة 3: التخصيص لأطر عمل الواجهة الأمامية المختلفة**

يمكنك تكييف هذا الحل للعمل مع أي إطار عمل للواجهة الأمامية مثل **React** أو **Vue** أو **Angular**. على سبيل المثال، إليك تنفيذ باستخدام **React** لعرض Markdown و LaTeX في الوقت الفعلي:

#### **مثال React**

1. **تثبيت KaTeX و marked عبر npm:**

```bash
npm install katex marked
```

2. **مكون React لعرض Markdown + الرياضيات:**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // عرض الصيغ الرياضية باستخدام KaTeX بعد تحميل المكون
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // عرض صيغ LaTeX الرياضية باستخدام KaTeX
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // رياضيات مضمنة في السطر
        { left: "\\[", right: "\\]", display: true }   // رياضيات في كتلة منفصلة
      ]
    });
  };

  return (
    <div>
      <h1>عرض Markdown + الرياضيات</h1>
      <textarea
        value={markdown}
        onChange={(e) => setMarkdown(e.target.value)}
        rows="10"
        cols="50"
      />
      <hr />
      <div id="markdownOutput"></div>
    </div>
  );
};

export default MarkdownEditor;
```

في إصدار React، نستخدم مكتبة `marked` لتحويل نص Markdown إلى HTML، ودالة `renderMathInElement()` الخاصة بـ KaTeX لمعالجة وعرض أي صيغ رياضية بـ LaTeX داخل HTML.

---

### **الخلاصة**
- استخدم **محلل Markdown** (مثل `marked.js`) لتحويل صيغة Markdown إلى HTML.
- استخدم **MathJax** أو **KaTeX** لعرض تعبيرات LaTeX الرياضية المضمنة في محتوى Markdown.
- اجمع بين الاثنين عن طريق عرض Markdown إلى HTML ومعالجة الصيغ الرياضية ديناميكيًا باستخدام KaTeX/MathJax.

يسمح هذا النهج للمستخدمين بكتابة ومعاينة محتوى Markdown مع المعادلات الرياضية في الوقت الفعلي، مما يجعله مثاليًا للتطبيقات مثل محررات المدونات، وأنظمة قواعد المعرفة، أو الأدوات التعليمية!