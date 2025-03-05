---
audio: false
generated: true
lang: ar
layout: post
title: استخدام PostCSS لتحويل CSS
translated: true
---

سأشرح كيفية استخدام PostCSS في مشروع واجهة المستخدم. PostCSS هو أداة لتحويل CSS باستخدام الإضافات JavaScript، وتقدم ميزات مثل إضافة الأوامر التمهيدية، والتقليل، ودعم اللغة CSS المستقبلية. إليك دليل خطوة بخطوة:

### 1. **إعداد مشروعك**
تأكد من أن لديك مشروع واجهة المستخدم مع Node.js مرفوع. إذا لم يكن كذلك، قم بإنشائه:
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **تثبيت PostCSS والأدوات المطلوبة**
قم بتثبيت PostCSS، وواجهة PostCSS، وكل الإضافات التي تريد استخدامها (مثل `autoprefixer` للأوامر التمهيدية، أو `cssnano` للتقليل):
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **إنشاء ملف CSS**
إنشاء ملف CSS المصدر، مثل `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **تكوين PostCSS**
إنشاء ملف `postcss.config.js` في جذور مشروعك لتحديد الإضافات:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // يضيف الأوامر التمهيدية
    require('cssnano')({ preset: 'default' }) // يقلل من CSS
  ]
};
```

### 5. **إضافة نص بناء**
في ملف `package.json` الخاص بك، أضف نصًا لتعمل على CSS باستخدام PostCSS:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: ملف الإدخال
- `dist/styles.css`: ملف الإخراج

### 6. **تشغيل PostCSS**
قم بتشغيل النص بناء:
```bash
npm run build:css
```
هذا يعالج `src/styles.css` ويخرج CSS المعالج إلى `dist/styles.css`. على سبيل المثال، قد يضيف `autoprefixer` الأوامر التمهيدية، ويقلل `cssnano` منه:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **الدمج مع أداة بناء (اختياري)**
لإعداد أكثر قوة، قم بالدمج بين PostCSS وأدوات مثل Webpack، Vite، أو Gulp:

#### **مع Vite**
إذا كنت تستخدم Vite، قم بتثبيت `postcss` وتكوينه في `vite.config.js`:
```javascript
// vite.config.js
import postcss from 'postcss';
import autoprefixer from 'autoprefixer';

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
};
```
Vite يعالج PostCSS تلقائيًا عند استيراد ملفات CSS.

#### **مع Webpack**
قم بتثبيت `postcss-loader`:
```bash
npm install --save-dev postcss-loader
```
قم بتحديث ملف `webpack.config.js` الخاص بك:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### 8. **مراقبة التغييرات (اختياري)**
لعمل CSS تلقائيًا أثناء التطوير، قم بتعديل النص في `package.json`:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
قم بتشغيل `npm run watch:css` لمراقبة التغييرات في الملفات.

### 9. **الإضافات الشائعة**
هنا بعض الإضافات الشائعة لـ PostCSS:
- `autoprefixer`: يضيف الأوامر التمهيدية喀ياس على دعم المتصفح.
- `cssnano`: يقلل من CSS.
- `postcss-preset-env`: يسمح لك باستخدام ميزات CSS المستقبلية اليوم.
- `postcss-import`: يحل `@import` القواعد.
قم بتثبيتها حسب الحاجة:
```bash
npm install --save-dev postcss-preset-env postcss-import
```
أضفها إلى `postcss.config.js`:
```javascript
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-preset-env'),
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' })
  ]
};
```

### مثال على عملية العمل
1. أكتب CSS حديثًا في `src/styles.css`:
```css
@custom-media --viewport-medium (width >= 768px);

:root {
  --main-color: #1a73e8;
}

.container {
  color: var(--main-color);
  display: grid;
}

@media (--viewport-medium) {
  .container {
    grid-template-columns: 1fr 1fr;
  }
}
```
2. قم بتشغيل `npm run build:css`.
3. احصل على CSS المعالج في `dist/styles.css` مع الأوامر التمهيدية، والمتغيرات المحلولة، والتقليل.

### نصائح
- استخدم `--map` في الواجهة (postcss src/styles.css -o dist/styles.css --map) لإنشاء خريطة المصدر للتشخيص.
- تحقق من وثائق الإضافات للحصول على خيارات التكوين المحددة.
- قم بالدمج مع إطار عمل واجهة المستخدم (React، Vue، إلخ.) عن طريق ربط CSS الإخراج إلى HTML أو المجمع الخاص بك.

أعلمني إذا كنت تحتاج إلى مساعدة في إعداد معين أو إضافة!