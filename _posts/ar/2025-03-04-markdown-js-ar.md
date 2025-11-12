---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة جافا سكريبت لمعالجة ماركداون
translated: true
type: note
---

يبدو أنك تسأل عن كيفية استخدام مكتبة `marked`، الإصدار `^0.3.6`، وهي مكتبة جافا سكريبت لتحليل نص Markdown وتحويله إلى HTML. بما أنك تشير إلى إصدار محدد بتدوين `^0.3.6` (على الأرجح من ملف `package.json` في مشروع Node.js)، سأرشدك خلال استخدام هذا الإصدار القديم من `marked`. لاحظ أن الإصدار `0.3.6` قديم جدًا (تم إصداره حوالي عام 2016)، وقد تطورت المكتبة بشكل كبير منذ ذلك الحين. ومع ذلك، سألتزم بما يعمل في ذلك الإصدار.

### الخطوة 1: التثبيت
إذا كنت تعمل في بيئة Node.js، يمكنك تثبيت `marked` الإصدار `0.3.6` باستخدام npm:

```bash
npm install marked@0.3.6
```

إن `^0.3.6` في ملف `package.json` تعني أنها ستثبت `0.3.6` أو أي تحديثات ترقيعية متوافقة (مثل `0.3.7`)، ولكن للتوضيح، الأمر أعلاه يثبت `0.3.6` بالضبط.

### الخطوة 2: الاستخدام الأساسي
إليك كيفية استخدام `marked` الإصدار `0.3.6` في بيئات مختلفة:

#### في Node.js
1. **استدعاء المكتبة**:
   أنشئ ملفًا (مثل `index.js`) وأضف ما يلي:

   ```javascript
   var marked = require('marked');
   ```

2. **تحويل Markdown إلى HTML**:
   استخدم الدالة `marked()` عن طريق تمرير سلسلة Markdown إليها. على سبيل المثال:

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **الناتج**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### في المتصفح
1. **تضمين المكتبة**:
   يمكنك استخدام CDN أو تنزيل `marked@0.3.6` وتضمينها عبر وسم `<script>`. على سبيل المثال، باستخدام رابط CDN تاريخي (إذا كان متاحًا) أو ملف محلي:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **استخدامها في جافا سكريبت**:
   بعد تضمين السكريبت، ستصبح `marked` متاحة بشكل عام:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### الخطوة 3: الخيارات (للإصدار 0.3.6)
يدعم الإصدار `0.3.6` بعض خيارات التخصيص. يمكنك تمرير كائن خيارات كوسيط ثانٍ لـ `marked()`. إليك مثال:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // تمكين GitHub Flavored Markdown
  tables: true,      // تمكين جداول GFM
  breaks: false,     // إذا كانت true، تضيف <br> عند فواصل الأسطر المفردة
  pedantic: false,   // إذا كانت true، تتبع مواصفات Markdown الصارمة
  sanitize: false,   // إذا كانت true، تزيل وسوم HTML للأمان
  smartLists: true,  // يحسن عرض القوائم
  smartypants: false // إذا كانت true، تستخدم طباعة "ذكية" (مثل علامات الاقتباس المتعرجة)
});
console.log(html);
```

### الميزات الرئيسية في 0.3.6
- **Markdown الأساسي**: يدعم العناوين (`#`)، والنص العريض (`**`)، والمائل (`*`)، والقوائم، وكتل الكود (```)، إلخ.
- **دعم GFM**: GitHub Flavored Markdown (مثل الجداول وقوائم المهام) متاح إذا تم ضبط `gfm: true`.
- **لا يوجد تخصيص للعارض**: على عكس الإصدارات الأحدث، لا يدعم `0.3.6` العارضين المخصصين، لذا أنت محدود بمخرجاته الافتراضية.

### مثال بمزيد من Markdown
إليك مثالاً أكثر اكتمالاً في Node.js:

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

**الناتج**:
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

### ملاحظات
- **التطهير**: إذا كنت تعرض مدخلات المستخدم، اضبط `sanitize: true` لإزالة HTML الخام للأمان (مثل وسوم `<script>`). ومع ذلك، هذا أساسي في `0.3.6` وليس قويًا مثل البدائل الحديثة.
- **القيود**: يفتقر هذا الإصدار إلى الميزات المضافة في الإصدارات اللاحقة (مثل التحليل غير المتزامن، ومحللات الرموز المخصصة)، لذا إذا كنت بحاجة إلى المزيد، ففكر في الترقية إلى إصدار أحدث مثل `5.x`.
- **تصحيح الأخطاء**: إذا لم يعمل، تأكد من تحميل المكتبة بشكل صحيح وتحقق من صيغة Markdown.