---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Chokidar لمراقبة الملفات
translated: true
---

Chokidar هو مكتبة Node.js مصممة أساسًا لمراقبة الملفات على جانب الخادم، لذلك استخدامه مباشرة في الواجهة الأمامية (أي في بيئة المتصفح) ليس هو استخدامه المعتاد. لا يمكن للمتصفح الوصول مباشرة إلى نظام الملفات مثل Node.js، وهذا هو السبب في أن Chokidar أكثر ملاءمة للبيئات الخلفية أو زمن البناء. ومع ذلك، إذا كنت تعمل على مشروع تستخدم فيه مجموعة أدوات مثل Webpack، Vite، أو Parcel في إعداد التطوير، أو إذا كنت تبني تطبيق Electron (الذي يجمع بين Node.js وواجهة الأمامية)، يمكنك استغلال Chokidar بشكل غير مباشر. دعني أشرح لك كيف يمكنك ذلك بناءً على السياق.

### لماذا لا يعمل Chokidar مباشرة في المتصفح
- Chokidar يعتمد على APIs Node.js مثل `fs` (نظام الملفات) لمراقبة الملفات، والتي ليست متاحة في بيئة المتصفح.
- يجرى الكود الأمامي في بيئة محمية (المتصفح)، حيث يتم حظر الوصول إلى نظام الملفات لأسباب أمنية.

### السيناريوهات الممكنة لاستخدام Chokidar في سياق "الواجهة الأمامية"
هنا كيفية استخدام Chokidar بطريقة تتعلق بتطوير الواجهة الأمامية:

#### 1. **خلال التطوير مع أداة بناء**
إذا كنت تسأل عن استخدام Chokidar لمراقبة الملفات (مثلًا، لإعادة التحميل الساخن أو التحديثات الحية) أثناء تطوير الواجهة الأمامية، فستدمجه في عملية البناء بدلاً من وقت تشغيل المتصفح.

مثال مع كود Node.js مخصص:
```javascript
const chokidar = require('chokidar');

// مراقبة التغييرات في ملفات مصدر الواجهة الأمامية
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // إشعال إعادة البناء أو إشعار خادم تطوير الواجهة الأمامية هنا
});
```
- **حالة الاستخدام**: يمكنك دمجه مع اتصال WebSocket لإرسال التحديثات إلى المتصفح أثناء التطوير.
- **الأدوات**: قم بدمجه مع شيء مثل `esbuild` أو خادم تطوير (مثلًا، Vite لديه مراقبة الملفات مدمجة بالفعل، ولكن يمكنك تخصيصه باستخدام Chokidar).

#### 2. **في تطبيق Electron**
إذا كانت "الواجهة الأمامية" جزء من تطبيق Electron، يمكنك استخدام Chokidar في العملية الرئيسية (Node.js) وإرسال التغييرات إلى العملية المروحة (الواجهة الأمامية).

مثال:
```javascript
// main.js (العملية الرئيسية في Electron)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // إرسال الحدث إلى المروحة
});
```
```javascript
// renderer.js (الواجهة الأمامية)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`تغير الملف: ${path}`);
  // تحديث الواجهة المستخدمية وفقًا لذلك
});
```

#### 3. **واجهة الأمامية مع بروفكسي الخلفية**
إذا كنت تبني تطبيق ويب وتريد وظيفة مراقبة الملفات، فستنفذ Chokidar على خادم Node.js وترسل التحديثات إلى الواجهة الأمامية عبر WebSockets أو أحداث إرسال من الخادم.

مثال (الخلفية مع Express و WebSocket):
```javascript
const express = require('express');
const WebSocket = require('ws');
const chokidar = require('chokidar');

const app = express();
const server = app.listen(3000);
const wss = new WebSocket.Server({ server });

chokidar.watch('./public').on('change', (path) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`تغير الملف: ${path}`);
    }
  });
});
```
الواجهة الأمامية (مثال React):
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "تغير الملف: ..."
  // تحديث الحالة أو الواجهة المستخدمية
};
```

### التثبيت
لاستخدام Chokidar في أي من هذه الإعدادات، يجب عليك تثبيته في مشروع Node.js الخاص بك:
```bash
npm install chokidar
```

### أساليب Chokidar الرئيسية
- `chokidar.watch(path, [options])`: بدء مراقبة ملف أو مجلد.
- الأحداث: `.on('add', callback)`, `.on('change', callback)`, `.on('unlink', callback)`, `.on('all', (event, path) => {})`.
- الخيار: `{ ignored: /node_modules/, persistent: true }` (تخصيص حسب الحاجة).

### إذا كنت تقصد شيئًا آخر
إذا كنت لا تعمل مع بيئة Node.js على الإطلاق وتريد سلوك مراقبة الملفات بشكل كامل في المتصفح (مثلًا، مراقبة تغييرات `<input type="file">`), فإخبرني! ذلك سيشمل API الملفات وlisteners الأحداث، وليس Chokidar.

ما هو إعدادك أو هدفك؟ يمكنني تخصيص ذلك أكثر!