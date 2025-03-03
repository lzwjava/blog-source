---
audio: false
generated: true
lang: ar
layout: post
title: 'GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling


  GitHub''s Markdown Styling'
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام حزمة "github-markdown-css" npm يتطلب أولا تثبيتها باستخدام `npm install github-markdown-css`.
- تشير الأبحاث إلى أن عليك بعد ذلك استيراد ملف CSS إلى مشروعك وتغليف محتوى Markdown الخاص بك في div مع الفئة "markdown-body".
- يشير الدليل إلى تعيين عرض وحواف اختياريين لتطابق نمط GitHub، وضمن DOctype لمنع مشاكل التصفح.

### التثبيت
ابدأ بتثبيت الحزمة باستخدام npm في مجلد مشروعك:
- قم بتشغيل `npm install github-markdown-css` لإضافةها إلى الاعتماديات.

### الاستخدام
بعد التثبيت، قم بتكامل CSS في مشروعك:
- استورد ملف CSS، على سبيل المثال، في JavaScript/React باستخدام `import 'github-markdown-css';`.
- تغليف محتوى Markdown المرسوم في `<div class="markdown-body">...</div>` لتطبيق الأسلوب.
- اضف اختياريًا CSS للعرض والحواف لتقليد مظهر GitHub:
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
- تأكد من أن HTML الخاص بك يتضمن DOctype (على سبيل المثال، `<!DOCTYPE html>`) لمنع مشاكل وضع التصفح، والتي قد تؤثر على الأسلوب.

### التفاصيل غير المتوقعة
قد لا تتوقع أن الحزمة تدعم أيضًا إنشاء CSS مخصص عبر حزمة ذات صلة، [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)، إذا كنت تحتاج إلى أنماط مخصصة.

---

### ملاحظة الاستبيان: دليل شامل لاستخدام حزمة "github-markdown-css" npm

يستعرض هذا الدليل التفصيلي استخدام حزمة "github-markdown-css" npm، التي صممت لتكرار نمط Markdown الخاص بـ GitHub في مشاريع الويب. يوفر نهجًا خطوة بخطوة للتثبيت والتكامل، بالإضافة إلى استعراضات إضافية لاستخدامها بشكل مثالي، خاصة في مختلف سياقات التطوير مثل React أو HTML البسيط. يتم استخلاص المعلومات من وثائق الحزمة الرسمية، ومخازن GitHub، والموارد الويب ذات الصلة، مما يضمن فهمًا شاملًا للمطورين في جميع المستويات.

#### الخلفية والأهداف
توفر حزمة "github-markdown-css"، التي يديرها [sindresorhus](https://github.com/sindresorhus)، مجموعة من CSS البسيطة لتقليد نمط عرض Markdown الخاص بـ GitHub. هذا مفيد بشكل خاص للمطورين الذين يريدون أن يبدو محتوى Markdown الخاص بهم، مثل الوثائق أو منشورات المدونات، موحدًا مع عرض GitHub المعروف بصفته نظيفة. تستخدم الحزمة بشكل واسع، مع أكثر من 1,168 مشروعًا آخر في سجل npm يستخدمها، مما يشير إلى شعبيتها وثباتها وفقًا لتحديثات حديثة.

#### عملية التثبيت
لبدء العمل، عليك تثبيت الحزمة عبر npm، مدير حزم Node.js. الأمر بسيط:
- قم بتشغيل `npm install github-markdown-css` في مجلد مشروعك. هذا يضيف الحزمة إلى مجلد `node_modules` الخاص بك ويحديث ملف `package.json` الخاص بك بالاعتماد.

أحدث إصدار للحزمة، وفقًا لتحديثات حديثة، هو 5.8.1، تم نشره قبل ثلاثة أشهر تقريبًا، مما يشير إلى الصيانة النشطة والتحديثات. هذا يضمن التوافق مع الممارسات الحديثة للتطوير الويب والأطر.

#### التكامل والاستخدام
بعد التثبيت، الخطوة التالية هي تكامل CSS في مشروعك. توفر الحزمة ملفًا باسم `github-markdown.css` يمكنك استيراده بناءً على إعدادات مشروعك:

- **لJavaScript/الأطر الحديثة (على سبيل المثال، React، Vue):**
  - استخدم بيان استيراد في ملفات JavaScript أو TypeScript الخاص بك، مثل `import 'github-markdown-css';`. هذا يعمل جيدًا مع المجمعين مثل Webpack أو Vite، الذين يديرون استيراد CSS بشكل سلس.
  - في React، قد ترى أمثلة حيث يقوم المطورون باستيراده في ملف المكون، مما يضمن أن الأسلوب متاح عالميًا أو محليًا حسب الحاجة.

- **لHTML البسيط:**
  - ربط ملف CSS مباشرة في قسم الرأس HTML الخاص بك:
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - لاحظ أن المسار قد يختلف بناءً على بنية مشروعك؛ تأكد من أن المسار النسبي يشير بشكل صحيح إلى مجلد `node_modules`.

بعد الاستيراد، قم بتطبيق الأسلوب عن طريق تغليف محتوى Markdown المرسوم في `<div>` مع الفئة "markdown-body". على سبيل المثال:
```html
<div class="markdown-body">
  <h1>الوحوش</h1>
  <p>كل الأشياء</p>
</div>
```
هذه الفئة حاسمة لأن CSS يهدف إلى العناصر داخل `.markdown-body` لتطبيق الأسلوب مشابه لـ GitHub، بما في ذلك النصوص، كتل الكود، الجداول، وما إلى ذلك.

#### استعراضات الأسلوب
لتكرار مظهر Markdown الخاص بـ GitHub بالكامل، اعتبر تعيين العرض والحواف للفئة `.markdown-body`. يوصي الدليل:
- عرض أقصى 980px، مع حواف 45px على شاشات أكبر، وحواف 15px على الأجهزة المحمولة (شاشات ≤ 767px).
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
هذا يضمن الاستجابة والتوافق مع تصميم GitHub، مما يحسن قابلية القراءة والتجربة المستخدم.

#### ملاحظات فنية وأفضل الممارسات
- **إحتياج DOctype:** يوضح الدليل إمكانية مشاكل الأسلوب، مثل عرض الجداول في الوضع المظلم بشكل غير صحيح، إذا دخل المتصفح وضع التصفح. لمنع ذلك، تأكد دائمًا من تضمين DOctype في أعلى HTML الخاص بك، مثل `<!DOCTYPE html>`. هذا يضمن عرض معيار وتجنب السلوك غير المتوقع.
- **تحليل Markdown:** بينما توفر الحزمة CSS، فإنها لا تحلل Markdown إلى HTML. ستحتاج إلى محلل Markdown مثل [marked.js](https://marked.js.org/) أو [react-markdown](https://github.com/remarkjs/react-markdown) لمشاريع React لتحويل نص Markdown إلى HTML، والذي يمكن بعد ذلك تصفيته باستخدام هذا CSS.
- **إنشاء CSS مخصص:** للمستخدمين المتقدمين، تسمح الحزمة ذات الصلة [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) بإنشاء CSS مخصص، مما قد يكون مفيدًا لتخصيصات معينة أو تعديلات. هذا هو تفاصيل غير متوقعة للمستخدمين الذين قد يتوقعون أن الحزمة تستخدم فقط مباشرة.

#### الاستخدام في سياقات محددة
- **مشاريع React:** في React، من الشائع استخدام `github-markdown-css` مع `react-markdown`. بعد التثبيت، استورد CSS واستخدم المكون:
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># مرحبا، عالم!</ReactMarkdown>
    </div>
  );
  ```
  تأكد أيضًا من تعيين CSS العرض والحواف كما هو موضح سابقًا للحصول على كامل الأسلوب الخاص بـ GitHub.

- **HTML البسيط مع CDN:** للبرمجة السريعة، يمكنك استخدام نسخة CDN، متاحة على [cdnjs](https://cdnjs.com/libraries/github-markdown-css)، عن طريق الرابط المباشر:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  ثم قم بتطبيق الفئة `.markdown-body` كما هو موضح سابقًا.

#### المشاكل المحتملة وحلولها
- **تعارض الأسلوب:** إذا استخدم مشروعك أطر CSS أخرى (على سبيل المثال، Tailwind، Bootstrap)، تأكد من عدم وجود تعارضات في التحديد. يجب أن تتغلب الفئة `.markdown-body` على معظم الأسلوب، ولكن اختبر بشكل شامل.
- **دعم الوضع المظلم:** تحتوي الحزمة على دعم للوضع المظلم، ولكن تأكد من أن محلل Markdown واعدادات مشروعك يدعمان التبديل بين الأسلوب بشكل صحيح، خاصة للكتل الكودية والجداول.
- **التوافق مع المتصفح:** نظرًا لانتشار استخدام الحزمة، فإن التوافق عادةً جيد، ولكن اختبر دائمًا عبر المتصفحات الرئيسية (Chrome، Firefox، Safari) لضمان العرض المتسق.

#### تحليل المقارنة
مقارنةً بأختيار CSS Markdown آخر، مثل [Markdown CSS](https://markdowncss.github.io/)، "github-markdown-css" يبرز بتكرار نمط GitHub بشكل مباشر، مما يجعله مثاليًا للوثائق التي تقليد مظهر GitHub. ومع ذلك، فإنه لا يحتوي على خيارات التصفح المدمجة دون تخصيص إضافي، unlike some alternatives that offer multiple themes out of the box.

#### جدول: الميزات الرئيسية والاستعراضات

| الميزة                  | الوصف                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| أمر التثبيت             | `npm install github-markdown-css`                                           |
| طريقة استيراد CSS        | `import 'github-markdown-css';` أو `<link>` في HTML                         |
| الفئة المطلوبة           | `.markdown-body` لتطبيق الأسلوب                                    |
| العرض والحواف        | أقصى 980px، حواف 45px (السطح المكتب)؛ حواف 15px (المحمول ≤ 767px)            |
| إحتياج DOctype      | حاسمة لمنع وضع التصفح وتضمن العرض الصحيح                  |
| إنشاء CSS مخصص    | ممكن عبر [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| التوافق            | يعمل مع محلل Markdown مثل marked.js، react-markdown؛ دعم متصفح واسع |

#### الخاتمة
استخدام "github-markdown-css" بسيط للمطورين الذين يبحثون عن تقليد نمط Markdown الخاص بـ GitHub. من خلال اتباع خطوات التثبيت والتكامل، واستعراضات الأسلوب والتقنية، يمكنك تحقيق مظهر موحد ومهني لمحتوى Markdown الخاص بك. لاستخدامات متقدمة، استكشف حزمة التوليد، واختبر دائمًا التوافق والإظهار، خاصة في مشاريع معقدة.

#### الاستشهادات الرئيسية
- [صفحة حزمة github-markdown-css npm](https://www.npmjs.com/package/github-markdown-css)
- [الكمية الأقل من CSS لتكرار نمط Markdown GitHub GitHub repo](https://github.com/sindresorhus/github-markdown-css)
- [صفحة عرض GitHub Markdown CSS](https://sindresorhus.com/github-markdown-css/)
- [إنشاء CSS لحزمة github-markdown-css npm](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN بواسطة cdnjs](https://cdnjs.com/libraries/github-markdown-css)