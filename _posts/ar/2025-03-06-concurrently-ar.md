---
audio: false
generated: true
lang: ar
layout: post
title: استخدامًا متزامنًا
translated: true
---

يبدو أنك تسأل عن استخدام "concurrently" في سياق تطوير واجهات المستخدم. ومع ذلك، "concurrently" هو عادةً حزمة Node.js تستخدم لتشغيل عدة أوامر أو scripts في نفس الوقت، وغالبًا ما يكون في سياق سير العمل الخلفي أو تطويري بدلاً من استخدامه مباشرة في الكود الأمامي. هل كنت تقصد كيفية استخدامه في إعداد مشروع واجهات المستخدم (مثل تشغيل scripts)، أو كنت تقصد شيئًا آخر مثل العمليات المتزامنة في JavaScript الأمامي (مثل الوعدات، async/await)? سأفترض الأخير الآن، ولكن يرجى التوضيح!

### استخدام `concurrently` في مشروع واجهات المستخدم

إذا كنت تعمل على مشروع واجهات المستخدم (مثل React، Vue، أو Angular)، يتم استخدام `concurrently` عادةً في تطوير تشغيل عدة عمليات في نفس الوقت - مثل بدء خادم تطوير و مراقب بناء. إليك كيفية استخدامه:

#### 1. تثبيت `concurrently`
أولًا، قم بتثبيته كاعتماد تطويري في مشروعك:
```bash
npm install --save-dev concurrently
```

#### 2. إضافة scripts إلى `package.json`
حدد scripts التي تريد تشغيلها بشكل متزامن في `package.json`. على سبيل المثال، إذا كنت تجرى خادم تطوير واجهات المستخدم و مبرمج CSS مسبقًا مثل Sass:
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // أو أمر تطوير واجهات المستخدم الخاص بك
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: يجرى خادم تطوير واجهات المستخدم (مثل React، Vite، إلخ).
- `watch:css`: يراقب ويجمع ملفات CSS.
- `dev`: يستخدم `concurrently` لجرى كلا الأمرين في نفس الوقت.

#### 3. تشغيل scripts المتزامنة
في terminal الخاص بك، قم ببساطة بجرى:
```bash
npm run dev
```
سيبدأ هذا كلا من خادم واجهات المستخدم و مراقب CSS في نفس الوقت. ستشاهد إخراجًا من كلا العملية في نفس terminal، و `concurrently` يظل يجرىهما معًا.

#### 4. إعدادات اختيارية
يمكنك تخصيص `concurrently` مع خيارات مثل:
- `--kill-others`: يوقف جميع العمليات إذا فشلت واحدة.
- `--names`: يعلل كل عملية للحصول على إخراج أكثر وضوحًا.

مثال مع خيارات في `package.json`:
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
يمكن أن يبدو الإخراج مثل:
```
[Frontend] Starting frontend server...
[CSS] Watching CSS files...
```

#### حالة استخدام في سير عمل واجهات المستخدم
فكر في أنك تقوم ببناء تطبيق React مع خادم API منفصل:
- واجهات المستخدم: `npm run start` (خادم تطوير React على الميناء 3000).
- API: `npm run start:api` (مثل خادم Node.js على الميناء 5000).
مع `concurrently`، يمكنك تشغيل كلا الأمرين:
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### إذا كنت تقصد JavaScript المتزامنة في واجهات المستخدم

إذا كنت تسأل عن معالجة العمليات المتزامنة في الكود الأمامي (مثل استدعاء عدة APIs في نفس الوقت)، إليك مثال سريع باستخدام `Promise.all`:
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
يجرى هذا الاستدعاءات API بشكل متزامن وي انتظار كلاهما حتى يتم حلها.

### توضيح إذا لزم الأمر!

أعلمني إذا كنت تقصد شيئًا مختلفًا بـ "concurrently في واجهات المستخدم" - مثل مكتبة أو إطار عمل أو حالة استخدام محددة - وسأعدل الإجابة بشكل أكثر تخصيصًا!