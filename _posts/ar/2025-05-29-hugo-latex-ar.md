---
audio: false
generated: true
lang: ar
layout: post
title: عرض اللاتيك في هوغو
translated: true
type: note
---

المشكلة التي تصفها تنشأ في **Jekyll** عند استخدام **Kramdown** مع **MathJax** كمحرك الرياضيات. عندما يتم تكوين Kramdown مع `math_engine: mathjax`، فإنه يفسر الأقواس `( )` في محتوى Markdown كمحددات LaTeX للرياضيات المضمنة (مثل `\( \)`)، مما يمكن أن يكسر النص العادي الذي يحتوي على أقواس. هذا لأن MathJax تم إعداده لتحليل `\( \)` أو `$ $` للرياضيات المضمنة، كما هو موضح في التكوين الخاص بك.

في **Hugo**، من غير المرجح أن تحدث هذه المشكلة افتراضيًا، لكن ذلك يعتمد على كيفية تكوين معالج Markdown في Hugo وتكامل MathJax. أدناه، سأشرح لماذا يتجنب Hugo هذه المشكلة في معظم الحالات، وكيفية منعها أو إصلاحها في Jekyll، وكيفية التأكد من عدم حدوثها في Hugo.

---

### **هل يواجه Hugo هذه المشكلة؟**
عادةً ما يتجنب Hugo هذه المشكلة لأن:
1.  **معالج Markdown**: يستخدم Hugo **Goldmark** (أو Blackfriday اختياريًا) كعارض Markdown الافتراضي، والذي لا يقوم بتمكين MathJax أو تحليل LaTeX افتراضيًا. ما لم تقم بتكوين Hugo صراحةً لاستخدام MathJax وإعداد محددات الرياضيات المضمنة مثل `\( \)`، فلن يتم تفسير الأقواس العادية `( )` في محتوىك عن طريق الخطأ على أنها LaTeX.
2.  **تكامل MathJax**: لا يقوم Hugo بتحليل LaTeX بشكل أصلي. إذا كنت تريد دعم MathJax، يجب عليك إضافة نصوص MathJax يدويًا (مثل الذي قدمته) إلى قوالب السمة الخاصة بك (على سبيل المثال، في `layouts/partials/head.html`) وتكوين المحددات. مرونة Hugo تتيح لك التحكم في كيفية معالجة MathJax للمحتوى، مما يتجنب التحليل التلقائي لـ `( )` ما لم يتم تمكينه صراحةً.
3.  **الرموز المختصرة للرياضيات**: غالبًا ما ينفذ مستخدمو Hugo عرض LaTeX باستخدام الرموز المختصرة (مثل `{{< math >}}...{{< /math >}}`)، والتي تحدد صراحةً محتوى الرياضيات، مما يمنع الأقواس العادية من أن يُساء فهمها على أنها LaTeX.

باختصار، لن تواجه Hugo هذه المشكلة ما لم تقم بتكوين MathJax بنفس المحددات المضمنة (`\( \)`) وتمكين التحليل التلقائي دون ضوابط مناسبة. باستخدام الرموز المختصرة أو تجنب `\( \)` كمحددات، يمكن لـ Hugo تجنب هذه المشكلة تمامًا.

---

### **إصلاح المشكلة في Jekyll**
في Jekyll، تحدث المشكلة لأن إعداد Kramdown `math_engine: mathjax`، المدمج مع تكوين MathJax الخاص بك، يتسبب في تحليل `( )` على أنها LaTeX. إليك كيفية إصلاح ذلك:

#### **1. تغيير محددات MathJax المضمنة**
قم بتعديل تكوين MathJax لاستخدام محددات رياضيات مضمنة مختلفة، مثل `$ $`، بدلاً من `\( \)` لتجنب التعارض مع الأقواس العادية. قم بتحديث النص في HTML لموقع Jekyll الخاص بك (على سبيل المثال، في `_includes/head.html`):

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // استخدم $ $ للرياضيات المضمنة
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // اسمح بعمل escape لـ $ لاستخدامه حرفيًا
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **لماذا يعمل**: من خلال إزالة `['\(','\)']` من `inlineMath`، لم يعد MathJax يفسر `( )` كمحددات LaTeX، مما يحافظ عليها للنص العادي. يسمح لك الإعداد `processEscapes: true` بكتابة `\$` في Markdown لعرض `$` حرفي إذا لزم الأمر.
-   **في Markdown الخاص بك**: استخدم `$x^2$` للرياضيات المضمنة بدلاً من `\(x^2\)`. على سبيل المثال:
    ```markdown
    هذه معادلة: $x^2 + y^2 = z^2$. نص عادي (غير محلول).
    ```

#### **2. تهريب الأقواس في Markdown**
إذا كنت تريد الاحتفاظ بـ `\( \)` كمحددات، قم بتهريب الأقواس في محتوى Markdown الخاص بك لمنع Kramdown/MathJax من تحليلها على أنها LaTeX. استخدم شرطة مائلة للخلف `\` قبل كل قوس:

```markdown
نص عادي \(ليس معادلة\). هذه معادلة حقيقية: \(x^2 + y^2\).
```

-   **المخرجات**: يُعرض `\(ليس معادلة\)` المهرب كـ `(ليس معادلة)`، بينما يُعرض `\(x^2 + y^2\)` كمعادلة LaTeX.
-   **العيب**: هذا يتطلب تهريب كل حالة من `( )` يدويًا في محتواك، مما قد يكون مملًا.

#### **3. تعطيل MathJax لصفحات محددة**
إذا كنت تحتاج MathJax فقط في صفحات معينة (على سبيل المثال، للمنشورات التي تحتوي على الكثير من الرياضيات)، قم بتعطيله افتراضيًا وتمكينه فقط حيث الحاجة:
-   أزل نص MathJax من `_layouts/default.html` العالمي أو `_includes/head.html`.
-   أضف تضمينًا شرطيًا في تخطيطك أو في front matter للصفحة. على سبيل المثال، في `_layouts/post.html`:

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

-   في front matter لملف Markdown الخاص بك، قم بتمكين MathJax فقط لصفحات محددة:
    ```yaml
    ---
    title: منشور الرياضيات الخاص بي
    mathjax: true
    ---
    ```

-   **لماذا يعمل**: الصفحات التي لا تحتوي على `mathjax: true` لن تقوم بتحميل MathJax، لذلك لن يتم تحليل `( )` على أنها LaTeX.

#### **4. استخدام محرك رياضيات مختلف**
قم بالتبديل من MathJax إلى محرك رياضيات آخر مدعوم من قبل Kramdown، مثل **KaTeX**، وهو أسرع وأقل احتمالية لإساءة تفسير الأقواس ما لم يتم تكوينه صراحةً. قم بتثبيت KaTeX في موقع Jekyll الخاص بك:
-   أضف نصوص KaTeX إلى `_includes/head.html`:
    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    ```
-   قم بتحديث `_config.yml`:
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **لماذا يعمل**: KaTeX أكثر صرامة فيما يتعلق بالتحليل ويستخدم افتراضيًا `$ $` للرياضيات المضمنة، مما يقلل من التعارضات مع `( )`. وهو أيضًا أسرع من MathJax.

---

### **ضمان تجنب Hugo لهذه المشكلة**
لاستخدام MathJax في Hugo دون مواجهة مشكلة تحليل `( )`، اتبع هذه الخطوات:

1.  **إضافة MathJax إلى Hugo**:
    -   ضع نص MathJax في partials السمة الخاصة بك (على سبيل المثال، `layouts/partials/head.html`):
        ```html
        {{ if .Params.mathjax }}
        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [['$','$']],
              displayMath: [['$$','$$'], ['\[','\]']],
              processEscapes: true
            },
            "HTML-CSS": { linebreaks: { automatic: true } },
            "CommonHTML": { linebreaks: { automatic: true } },
            TeX: { equationNumbers: { autoNumber: "AMS" } }
          });
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {{ end }}
        ```
    -   قم بتمكين MathJax في صفحات محددة عن طريق الإضافة إلى front matter:
        ```yaml
        ---
        title: منشور الرياضيات الخاص بي
        mathjax: true
        ---
        ```

2.  **استخدم الرموز المختصرة للرياضيات**:
    أنشئ رمزًا مختصرًا (على سبيل المثال، `layouts/shortcodes/math.html`) لتغليف محتوى الرياضيات صراحةً:
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    استخدمه في Markdown الخاص بك:
    ```markdown
    نص عادي (غير محلول). معادلة: {{< math >}}$x^2 + y^2${{< /math >}}.
    ```
    -   **لماذا يعمل**: تضمن الرموز المختصرة معالجة المحتوى المحدد صراحةً فقط كرياضيات، تاركةً `( )` في النص العادي دون مساس.

3.  **استخدم KaTeX بدلاً من ذلك**:
    غالبًا ما يفضل مستخدمو Hugo KaTeX بسبب سرعته. أضف KaTeX إلى `layouts/partials/head.html`:
    ```html
    {{ if .Params.math }}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    {{ end }}
    ```
    قم بتمكينه في front matter:
    ```yaml
    math: true
    ```
    استخدم `$ $` للرياضيات المضمنة لتجنب تعارضات `( )`.

---

### **التوصية**
-   **لـ Jekyll**: انتقل إلى محددات `$ $` لـ MathJax أو استخدم KaTeX لتجنب مشاكل تحليل `( )`. يعد تهريب الأقواس حلًا بديلاً ولكنه أقل عملية للمواقع الكبيرة.
-   **لـ Hugo**: من غير المرجح أن تواجه هذه المشكلة ما لم تقم بتكوين MathJax صراحةً بمحددات `\( \)`. استخدم الرموز المختصرة أو KaTeX لعرض الرياضيات لضمان سلامة الأقواس العادية.

إذا كنت تقوم بالترحيل من Jekyll إلى Hugo وتريد الاحتفاظ بمحتوى الرياضيات الخاص بك، أوصي باستخدام KaTeX في Hugo مع الرموز المختصرة للتحكم الصريح. دعني أعلم إذا كنت بحاجة إلى مساعدة في إعداد تكامل MathJax/KaTeX في Hugo أو تحويل محتوى الرياضيات في موقع Jekyll الخاص بك!