---
audio: false
generated: true
lang: ar
layout: post
title: استخدام كا تيكس في جيكل
translated: true
type: note
---

لاستخدام KaTeX بدلاً من MathJax في Jekyll مع إعداداتك الحالية، ستحتاج إلى استبدال نصوص MathJax بـ KaTeX وتعديل تكوين Jekyll الخاص بك. KaTeX أسرع وأخف من MathJax، لكنه يتطلب نهجًا مختلفًا لأنه لا يدعم جميع ميزات MathJax (على سبيل المثال، ترقيم المعادلات التلقائي يكون يدويًا أكثر). فيما يلي دليل خطوة بخطوة للتبديل إلى KaTeX في موقع Jekyll الخاص بك:

### 1. تحديث تكوين Jekyll
قم بتعديل `_config.yml` لاستخدام KaTeX كمحرك الرياضيات لـ Kramdown. قم بتحديث قسم `kramdown` على النحو التالي:

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

يخبر هذا Kramdown بعرض تعبيرات LaTeX الرياضية باستخدام KaTeX بدلاً من MathJax.

### 2. تضمين KaTeX في HTML الخاص بك
قم بإزالة نصوص MathJax من HTML الخاص بك واستبدلها بـ KaTeX. يمكنك تضمين KaTeX عبر CDN. أضف ما يلي إلى قسم `<head>` لملف تخطيط Jekyll الخاص بك (على سبيل المثال، `_layouts/default.html`):

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Auto-render extension (اختياري، للتقديم التلقائي للرياضيات) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Auto-render configuration -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // Block math
        {left: "\\[", right: "\\]", display: true}, // Block math
        {left: "\\(", right: "\\)", display: false}, // Inline math
        {left: "$", right: "$", display: false} // Inline math
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. إزالة تكوين MathJax
احذف الكود المتعلق بـ MathJax من ملف التخطيط الخاص بك، بما في ذلك كتلة `<script type="text/x-mathjax-config">` ونص CDN الخاص بـ MathJax. لا يستخدم KaTeX تكوينًا مثل `tex2jax` الخاص بـ MathJax، ونص التقديم التلقائي أعلاه يتعامل مع وظيفة مماثلة.

### 4. كتابة الرياضيات في Markdown الخاص بك
مع تكوين KaTeX و Kramdown، يمكنك كتابة LaTeX الرياضي في ملفات Markdown الخاصة بك باستخدام نفس المحددات كما كان من قبل:

- **الرياضيات المضمنة**: استخدم `$...$` أو `\(...\)` (على سبيل المثال، `$E=mc^2$` أو `\(E=mc^2\)`).
- **الرياضيات المعروضة**: استخدم `$$...$$` أو `\[...\]` (على سبيل المثال، `$$E=mc^2$$` أو `\[E=mc^2\]`).

على سبيل المثال:

```markdown
الرياضيات المضمنة: $E=mc^2$ أو \(E=mc^2\).

الرياضيات المعروضة:
$$E=mc^2$$

أو

\[E=mc^2\]
```

سيعالج Kramdown مع محرك الرياضيات KaTeX هذه إلى HTML يقوم KaTeX بتقديمها.

### 5. ملاحظات حول KaTeX مقابل MathJax
- **الترقيم التلقائي للمعادلات**: لا يدعم KaTeX الترقيم التلقائي للمعادلات مثل `autoNumber: "AMS"` الخاص بـ MathJax. إذا كنت بحاجة إلى أرقام المعادلات، يجب عليك إضافتها يدويًا باستخدام `\tag{}` في كود LaTeX الخاص بك (على سبيل المثال، `$$E=mc^2 \tag{1}$$`).
- **الأداء**: KaTeX أسرع بشكل ملحوظ من MathJax، مما يجعله مثاليًا للمواقع الثابتة مثل Jekyll.
- **مجموعة الميزات**: يدعم KaTeX أوامر LaTeX أقل من MathJax. تحقق من [وظائف KaTeX المدعومة](https://katex.org/docs/supported.html) للتأكد من توافق تعبيراتك الرياضية.
- **التقديم**: يحاكي نص التقديم التلقائي أعلاه سلوك MathJax من خلال تقديم تعبيرات الرياضيات تلقائيًا ضمن المحددات المحددة. اضبط مصفوفة `delimiters` في النص إذا كنت تريد تغيير أو تحديد المحددات.

### 6. اختر إعداداتك
شغّل موقع Jekyll الخاص بك محليًا (`jekyll serve`) وتحقق من أن تعبيرات الرياضيات تُعرض بشكل صحيح. إذا واجهت مشاكل:
- تحقق من وحدة تحكم المتصفح للبحث عن أخطاء متعلقة بـ KaTeX.
- تأكد من أن عناوين URL لـ CDN الخاصة بـ KaTeX محدثة (تستخدم العناوين أعلاه الإصدار 0.16.11، وهو الأحدث حسب معرفتي).
- تأكد من أن ملفات Markdown الخاصة بك تستخدم بناء جملة LaTeX صالحًا ومتوافقًا مع KaTeX.

### 7. اختياري: ملفات KaTeX محليًا
إذا كنت تفضل استضافة ملفات KaTeX محليًا لتجنب الاعتماد على CDN:
1. قم بتنزيل `katex.min.css`، و `katex.min.js`، و `auto-render.min.js` من [إصدارات KaTeX على GitHub](https://github.com/KaTeX/KaTeX/releases).
2. ضعهم في مجلد الأصول (assets) الخاص بـ Jekyll (على سبيل المثال، `assets/katex/`).
3. قم بتحديث علامات `<link>` و `<script>` للإشارة إلى ملفاتك المحلية (على سبيل المثال، `/assets/katex/katex.min.css`).

### 8. استكشاف الأخطاء وإصلاحها
- **الرياضيات لا تُعرض**: تأكد من تحميل نصوص KaTeX بشكل صحيح وأن `kramdown.math_engine` مضبوط على `katex`.
- **مشاكل في المحددات**: تحقق من أن المحددات في نص التقديم التلقائي تطابق تلك الموجودة في Markdown الخاص بك.
- **أوامر غير مدعومة**: إذا فشل أمر LaTeX، تحقق من وثائق KaTeX للأوامر المدعومة أو أعد كتابة التعبير.

إذا كنت بحاجة إلى مساعدة محددة بشأن تعبير رياضي معين أو تكوين، شارك التفاصيل، ويمكنني تقديم إرشادات مخصصة!