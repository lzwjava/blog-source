---
audio: false
generated: true
lang: ar
layout: post
title: تصميم ماركداون في جيت هاب
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المحتمل أنه لاستخدام حزمة npm "github-markdown-css"، تقوم أولاً بتثبيتها باستخدام `npm install github-markdown-css`.
- تشير الأبحاث إلى أنك بعد ذلك تقوم باستيراد ملف CSS إلى مشروعك وتغليف محتوى Markdown الخاص بك داخل div يحمل الفئة "markdown-body".
- تميل الأدلة نحو تعيين عرض وحشو اختياريين لمطابقة نمط GitHub، وضمان وجود DOctype لتجنب مشاكل التنسيق.

### التثبيت
ابدأ بتثبيت الحزمة باستخدام npm في دليل مشروعك:
- قم بتشغيل `npm install github-markdown-css` لإضافتها إلى التبعيات الخاصة بك.

### الاستخدام
بعد التثبيت، قم بدمج CSS في مشروعك:
- قم باستيراد ملف CSS، على سبيل المثال، في JavaScript/React باستخدام `import 'github-markdown-css';`.
- قم بتغليف محتوى Markdown المُعرض داخل `<div class="markdown-body">...</div>` لتطبيق الأنماط.
- بشكل اختياري، أضف CSS للعرض والحشو لمحاكاة مظهر GitHub:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- تأكد من أن HTML الخاص بك يتضمن DOctype (على سبيل المثال، `<!DOCTYPE html>`) لمنع مشاكل وضع التوافق، والتي قد تؤثر على التنسيق.

### تفصيل غير متوقع
قد لا تتوقع أن الحزمة تدعم أيضًا إنشاء CSS مخصص عبر حزمة مرتبطة، [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)، إذا كنت بحاجة إلى أنماط مخصصة.

---

### ملاحظة استقصائية: دليل شامل لاستخدام حزمة npm github-markdown-css

يستكشف هذا الدليل التفصيلي استخدام حزمة npm "github-markdown-css"، المصممة لمحاكاة تنسيق Markdown الخاص بـ GitHub في المشاريع الويب. يقدم نهجًا خطوة بخطوة للتثبيت والدمج، جنبًا إلى جنب مع اعتبارات إضافية للاستخدام الأمثل، خاصة في سياقات التطوير المختلفة مثل React أو HTML العادي. تم استخلاص المعلومات من وثائق الحزمة الرسمية، ومستودعات GitHub، والموارد الويب ذات الصلة، مما يضمن فهمًا شاملاً للمطورين على جميع المستويات.

#### الخلفية والغرض
تقدم حزمة "github-markdown-css"، التي يحافظ عليها [sindresorhus](https://github.com/sindresorhus)، مجموعة دنيا من CSS لمحاكاة نمط عرض Markdown الخاص بـ GitHub. هذا مفيد بشكل خاص للمطورين الذين يريدون أن يظهر محتوى Markdown الخاص بهم، مثل الوثائق أو منشورات المدونات، متسقًا مع العرض المألوف والنظيف لـ GitHub. تُستخدم الحزمة على نطاق واسع، حيث يستخدمها أكثر من 1,168 مشروعًا آخر في سجل npm، مما يشير إلى شعبيتها وموثوقيتها اعتبارًا من التحديثات الأخيرة.

#### عملية التثبيت
للبدء، تحتاج إلى تثبيت الحزمة عبر npm، مدير حزم Node.js. الأمر واضح ومباشر:
- نفذ `npm install github-markdown-css` في دليل مشروعك. هذا يضيف الحزمة إلى مجلد `node_modules` الخاص بك ويحدث `package.json` الخاص بك بالتبعية.

أحدث إصدار من الحزمة، اعتبارًا من الفحوصات الأخيرة، هو 5.8.1، تم نشره منذ حوالي ثلاثة أشهر، مما يشير إلى الصيانة النشطة والتحديثات. هذا يضمن التوافق مع ممارسات تطوير الويب الحديثة والأطر.

#### الدمج والاستخدام
بمجرد التثبيت، تكون الخطوة التالية هي دمج CSS في مشروعك. توفر الحزمة ملفًا باسم `github-markdown.css`، والذي يمكنك استيراده اعتمادًا على إعداد مشروعك:

- **لأطر عمل JavaScript الحديثة (مثل React, Vue):**
  - استخدم عبارة الاستيراد في ملفات JavaScript أو TypeScript الخاصة بك، مثل `import 'github-markdown-css';`. هذا يعمل بشكل جيد مع أدوات التجميع مثل Webpack أو Vite، والتي تتعامل مع استيراد CSS بسلاسة.
  - بالنسبة لـ React، قد ترى أمثلة حيث يقوم المطورون باستيرادها في ملف مكون، مما يضمن توفر الأنماط على النطاق العالمي أو حسب النطاق حسب الحاجة.

- **لـ HTML العادي:**
  - رابط ملف CSS مباشرة في قسم head في HTML الخاص بك:
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - لاحظ أن المسار قد يختلف بناءً على هيكل مشروعك؛ تأكد من أن المسار النسبي يشير بشكل صحيح إلى دليل `node_modules`.

بعد الاستيراد، قم بتطبيق الأنماط عن طريق تغليف محتوى Markdown المُعرض الخاص بك داخل `<div>` مع الفئة "markdown-body". على سبيل المثال:
```html
<div class="markdown-body">
  <h1>Unicorns</h1>
  <p>All the things</p>
</div>
```
هذه الفئة حاسمة حيث تستهدف CSS العناصر داخل `.markdown-body` لتطبيق التنسيق الشبيه بـ GitHub، بما في ذلك الطباعة، وكتل التعليمات البرمجية، والجداول، والمزيد.

#### اعتبارات التنسيق
لمحاكاة مظهر Markdown الخاص بـ GitHub بشكل كامل، فكر في تعيين العرض والحشو لفئة `.markdown-body`. تقترح الوثائق:
- عرض أقصى يبلغ 980 بكسل، مع حشو 45 بكسل على الشاشات الأكبر، و 15 بكسل حشو على الأجهزة المحمولة (شاشات ≤ 767 بكسل).
- يمكنك تحقيق ذلك باستخدام CSS التالي:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
هذا يضمن الاستجابة للمختلفة المقاسات ومحاذاة تصميم GitHub، مما يعزز قابلية القراءة وتجربة المستخدم.

#### ملاحظات فنية وأفضل الممارسات
- **متطلب DOctype:** تبرز الوثائق مشاكل التنسيق المحتملة، مثل عرض الجداول في الوضع الداكن بشكل غير صحيح، إذا دخل المتصفح في وضع التوافق. لمنع هذا، قم دائمًا بتضمين DOctype في أعلى HTML الخاص بك، مثل `<!DOCTYPE html>`. هذا يضمن العرض المتوافق مع المعايير ويتجنب السلوك غير المتوقع.
- **تحليل Markdown:** بينما توفر الحزمة CSS، فإنها لا تقوم بتحليل Markdown إلى HTML. ستحتاج إلى محلل Markdown مثل [marked.js](https://marked.js.org/) أو [react-markdown](https://github.com/remarkjs/react-markdown) لمشاريع React لتحويل نص Markdown إلى HTML، والذي يمكن بعد ذلك تنسيقه باستخدام CSS هذا.
- **توليد CSS مخصص:** للمستخدمين المتقدمين، تسمح الحزمة المرتبطة [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) بتوليد CSS مخصص، مما قد يكون مفيدًا للتخصيص أو التعديلات المحددة. هذا تفصيل غير متوقع لأولئك الذين قد يفترضون أن الحزمة مخصصة للاستخدام المباشر فقط.

#### الاستخدام في سياقات محددة
- **مشاريع React:** في React، يعد الجمع بين `github-markdown-css` و `react-markdown` شائعًا. بعد تثبيت كليهما، قم باستيراد CSS واستخدم المكون:
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Hello, World!</ReactMarkdown>
    </div>
  );
  ```
  تأكد أيضًا من تعيين عرض وحشو CSS كما هو موضح سابقًا للحصول على تنسيق GitHub الكامل.

- **HTML عادي مع CDN:** للنماذج الأولية السريعة، يمكنك استخدام إصدار CDN، المتوفر على [cdnjs](https://cdnjs.com/libraries/github-markdown-css)، عن طريق الربط المباشر:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  ثم قم بتطبيق فئة `.markdown-body` كما كان من قبل.

#### المشكلات المحتملة والحلول
- **تعارضات التنسيق:** إذا كان مشروعك يستخدم أطر عمل CSS أخرى (مثل Tailwind، Bootstrap)، تأكد من عدم وجود تعارضات في الخصوصية. يجب أن تتجاوز فئة `.markdown-body` معظم الأنماط، ولكن اختبر بدقة.
- **دعم الوضع الداكن:** تتضمن الحزمة دعمًا للوضع الداكن، ولكن تأكد من أن محلل Markdown وإعداد المشروع الخاص بك يتعاملان مع تبديل السمة بشكل صحيح، خاصة لكتل التعليمات البرمجية والجداول.
- **توافق المتصفح:** نظرًا للاستخدام الواسع النطاق للحزمة، فإن التوافق جيد بشكل عام، ولكن اختبر دائمًا عبر المتصفحات الرئيسية (Chrome، Firefox، Safari) لضمان عرض متسق.

#### التحليل المقارن
مقارنة بخيارات CSS الأخرى لـ Markdown، مثل [Markdown CSS](https://markdowncss.github.io/)، تبرز "github-markdown-css" لمحاكاتها المباشرة لنمط GitHub، مما يجعلها مثالية للوثائق التي تعكس مظهر GitHub. ومع ذلك، فإنها تفتقر إلى خيارات السمات المدمجة دون تخصيص إضافي، على عكس بعض البدائل التي تقدم سمات متعددة جاهزة للاستخدام.

#### الجدول: الميزات والاعتبارات الرئيسية

| الميزة                     | الوصف                                                                        |
|----------------------------|-------------------------------------------------------------------------------|
| أمر التثبيت                | `npm install github-markdown-css`                                             |
| طريقة استيراد CSS          | `import 'github-markdown-css';` أو `<link>` في HTML                          |
| الفئة المطلوبة             | `.markdown-body` لتطبيق التنسيق                                              |
| العرض والحشو               | أقصى 980 بكسل، حشو 45 بكسل (سطح المكتب)؛ حشو 15 بكسل (محمول ≤ 767 بكسل)      |
| متطلب DOctype              | أساسي لتجنب وضع التوافق وضمان العرض الصحيح                                   |
| توليد CSS مخصص             | ممكن عبر [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| التوافق                    | يعمل مع محللين Markdown مثل marked.js، react-markdown؛ دعم واسع للمتصفحات     |

#### الخلاصة
يعد استخدام "github-markdown-css" واضحًا للمطورين الذين يسعون لمحاكاة تنسيق Markdown الخاص بـ GitHub. باتباع خطوات التثبيت والدمج، ومراعاة الملاحظات الفنية والتنسيقية الإضافية، يمكنك تحقيق مظهر متسق واحترافي لمحتوى Markdown الخاص بك. للتخصيص المتقدم، استكشف حزمة التوليد، واختبر دائمًا من أجل التوافق ومشاكل العرض، خاصة في المشاريع المعقدة.

#### الاقتباسات الرئيسية
- [صفحة حزمة npm github-markdown-css](https://www.npmjs.com/package/github-markdown-css)
- [الحد الأدنى من CSS لمحاكاة نمط GitHub Markdown - مستودع GitHub](https://github.com/sindresorhus/github-markdown-css)
- [صفحة عرض GitHub Markdown CSS](https://sindresorhus.com/github-markdown-css/)
- [توليد CSS لحزمة npm github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN بواسطة cdnjs](https://cdnjs.com/libraries/github-markdown-css)