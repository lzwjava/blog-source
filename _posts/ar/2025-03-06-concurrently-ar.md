---
audio: false
generated: true
lang: ar
layout: post
title: استخدام بالتزامن
translated: true
type: note
---

يبدو أنك تسأل عن استخدام "concurrently" في سياق تطوير الواجهات الأمامية. ومع ذلك، فإن "concurrently" عادةً ما تكون حزمة Node.js تُستخدم لتشغيل أوامر أو نصوص برمجية متعددة في نفس الوقت، غالبًا في سياق سير عمل backend أو التطوير بدلاً من استخدامها مباشرة في كود الواجهة الأمامية. هل قصدت كيفية استخدامها في إعداد مشروع frontend (مثل تشغيل النصوص البرمجية)، أم كنت تشير إلى شيء آخر مثل العمليات المتزامنة في JavaScript للواجهات الأمامية (مثل الوعود، async/await)? سأفترض السيناريو الأول الآن، ولكن لا تتردد في التوضيح!

### استخدام `concurrently` في مشروع Frontend

إذا كنت تعمل على مشروع frontend (مثل React أو Vue أو Angular)، فغالبًا ما يُستخدم `concurrently` في التطوير لتشغيل عمليات متعددة في وقت واحد—مثل بدء خادم تطوير ومراقب بناء. إليك كيفية استخدامه:

#### 1. تثبيت `concurrently`
أولاً، قم بتثبيته كتبع للتطوير في مشروعك:
```bash
npm install --save-dev concurrently
```

#### 2. إضافة نصوص برمجية إلى `package.json`
حدد النصوص البرمجية التي تريد تشغيلها في وقت واحد في ملف `package.json`. على سبيل المثال، إذا كنت تقوم بتشغيل خادم تطوير frontend ومعالج CSS مسبقًا مثل Sass:
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // أو أمر تطوير frontend الخاص بك
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: يشغل خادم تطوير frontend الخاص بك (مثل React أو Vite، إلخ).
- `watch:css`: يراقب ويحزم ملفات CSS الخاصة بك.
- `dev`: يستخدم `concurrently` لتشغيل كلا الأمرين في وقت واحد.

#### 3. تشغيل النصوص البرمجية المتزامنة
في طرفيتك، ما عليك سوى تشغيل:
```bash
npm run dev
```
سيؤدي هذا إلى بدء كل من خادم frontend ومراقب CSS في نفس الوقت. سترى مخرجات من كلا العمليتين في نفس الطرفية، ويحافظ `concurrently` على تشغيلهما معًا.

#### 4. التهيئة الاختيارية
يمكنك تخصيص `concurrently` بخيارات مثل:
- `--kill-others`: يوقف جميع العمليات إذا فشلت واحدة.
- `--names`: يضع تسمية لكل عملية للحصول على مخرجات أوضح.

مثال مع الخيارات في `package.json`:
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
قد تبدو المخرجات كالتالي:
```
[Frontend] بدء خادم الواجهة الأمامية...
[CSS] مراقبة ملفات CSS...
```

#### حالة استخدام في سير عمل Frontend
تخيل أنك تبني تطبيق React مع خادم API منفصل:
- الواجهة الأمامية: `npm run start` (خادم تطوير React على المنفذ 3000).
- API: `npm run start:api` (مثلاً، خادم Node.js على المنفذ 5000).
باستخدام `concurrently`، يمكنك تشغيل كليهما:
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### إذا كنت تقصد JavaScript المتزامن في الواجهة الأمامية
إذا كنت تسأل عن التعامل مع العمليات المتزامنة في كود الواجهة الأمامية (مثل جلب واجهات برمجة تطبيقات متعددة في وقت واحد)، إليك مثال سريع باستخدام `Promise.all`:
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
هذا يشغل استدعاءات API بشكل متزامن وينتظر حتى يحل كليهما.

### وضح إذا لزم الأمر!
أخبرني إذا كنت تقصد شيئًا مختلفًا بـ "concurrently في frontend"—مثل مكتبة محددة، أو إطار عمل، أو حالة استخدام—وسأخصص الإجابة بشكل أكبر!