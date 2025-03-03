---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة JavaScript لماركداون
translated: true
---

يبدو أنك تسأل عن كيفية استخدام مكتبة `marked`، الإصدار `^0.3.6`، وهي مكتبة JavaScript لتحليل نص Markdown وتحويلها إلى HTML. نظرًا لأنك تحدد إصدارًا معينًا باستخدام `^0.3.6` (ربما من ملف `package.json` في مشروع Node.js)، سأرشدك في استخدام هذا الإصدار القديم من المكتبة. يجب أن نلاحظ أن الإصدار `0.3.6` قديم جدًا (صدر حوالي عام 2016)، وتطورت المكتبة بشكل كبير منذ ذلك الحين. ومع ذلك، سأبقى على ما يعمل لهذا الإصدار.

### الخطوة 1: التثبيت
إذا كنت تعمل في بيئة Node.js، يمكنك تثبيت `marked` الإصدار `0.3.6` باستخدام npm:

```bash
npm install marked@0.3.6
```

يعد `^0.3.6` في ملف `package.json` يعني أنه سيثبت `0.3.6` أو أي تحديثات لبرمجيات (مثل `0.3.7`), ولكن من أجل الوضوح، سيقوم الأمر أعلاه بحجزه على `0.3.6` بالضبط.

### الخطوة 2: الاستخدام الأساسي
هنا كيفية استخدام `marked` الإصدار `0.3.6` في بيئات مختلفة:

#### في Node.js
1. **استدعاء المكتبة**:
   انشئ ملفًا (مثل `index.js`) وأضف التالي:

   ```javascript
   var marked = require('marked');
   ```

2. **تحويل Markdown إلى HTML**:
   استخدم دالة `marked()` عن طريق تمرير نص Markdown إليها. على سبيل المثال:

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **الخروج**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### في المتصفح
1. **شمل المكتبة**:
   يمكنك استخدام CDN أو تحميل `marked@0.3.6` وضمها عبر علامة `<script>`. على سبيل المثال، باستخدام رابط CDN تاريخي (إذا كان متاحًا) أو ملف محلي:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **استخدامها في JavaScript**:
   بعد تضمين النص، ستكون `marked` متاحة عالميًا:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### الخطوة 3: الخيارات (لإصدار 0.3.6)
يوفر الإصدار `0.3.6` بعض خيارات التخصيص. يمكنك تمرير كائن خيارات كحجج ثانية إلى `marked()`. هنا مثال:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // تمكين Markdown من GitHub
  tables: true,      // تمكين جداول GFM
  breaks: false,     // إذا كان صحيحًا، يضيف <br> على انقطاع السطر الواحد
  pedantic: false,   // إذا كان صحيحًا، يتبع مواصفات Markdown الصارمة
  sanitize: false,   // إذا كان صحيحًا، يخلع علامات HTML لأغراض الأمان
  smartLists: true,  // تحسين عرض القوائم
  smartypants: false // إذا كان صحيحًا، يستخدم "smart" Typography (مثل علامات الاقتباس المنحنية)
});
console.log(html);
```

### الميزات الرئيسية في 0.3.6
- **Markdown الأساسي**: يدعم العناوين (`#`), الغليظ (`**`), المائل (`*`), القوائم، كتل الكود (```), إلخ.
- **دعم GFM**: Markdown من GitHub (مثل الجداول والقوائم المهام) متاح إذا تم تعيين `gfm: true`.
- **لا يوجد تخصيص للمعرض**: عكس الإصدارات الأحدث، لا يدعم `0.3.6` المعارضات المخصصة، لذا أنت مقيد بالخرج الافتراضي.

### مثال مع أكثر من Markdown
هنا مثال كامل في Node.js:

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**الخروج**:
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### الملاحظات
- **التطهير**: إذا كنت ترغب في عرض المدخلات المستخدم، قم بتعيين `sanitize: true` لإزالة HTML الخام لأغراض الأمان (مثل علامات `<script>`). ومع ذلك، فهو أساسي في `0.3.6` ولا يكون قويًا مثل البدائل الحديثة.
- **القيود**: هذا الإصدار يفتقر إلى الميزات التي أضيفت في الإصدارات اللاحقة (مثل تحليل غير متزامن، مصنعي الرموز المخصصة)، لذا إذا كنت تحتاج إلى المزيد، فاعتبر الترقية إلى إصدار أحدث مثل `5.x`.
- **التشخيص**: إذا لم يعمل، تأكد من تحميل المكتبة بشكل صحيح وتحقق من صياغة Markdown.