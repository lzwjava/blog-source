---
audio: false
generated: true
lang: ar
layout: post
title: استخدام PostCSS لتحويل CSS
translated: true
type: note
---

سأشرح كيفية استخدام PostCSS في مشروع frontend. PostCSS هو أداة لتحويل CSS باستخدام إضافة JavaScript، مما يوفر ميزات مثل البادئات التلقائية، والتصغير، ودعم صيغ CSS المستقبلية. إليك دليل خطوة بخطوة:

### 1. **إعداد مشروعك**
تأكد من أن لديك مشروع frontend مع تثبيت Node.js. إذا لم يكن الأمر كذلك، قم بتهيئة مشروع:
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **تثبيت PostCSS والأدوات المطلوبة**
قم بتثبيت PostCSS و PostCSS CLI وأي إضافات تريد استخدامها (مثل `autoprefixer` للبادئات أو `cssnano` للتصغير):
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **إنشاء ملف CSS**
قم بإنشاء ملف CSS مصدري، مثل `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **تكوين PostCSS**
قم بإنشاء ملف `postcss.config.js` في مجلد مشروعك لتحديد الإضافات:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // يضيف بادئات المتصفحات
    require('cssnano')({ preset: 'default' }) // يصغر CSS
  ]
};
```

### 5. **إضافة سكريبت بناء**
في ملف `package.json` الخاص بك، أضف سكريبت لمعالجة CSS باستخدام PostCSS:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: ملف الإدخال
- `dist/styles.css`: ملف الإخراج

### 6. **تشغيل PostCSS**
شغّل أمر البناء:
```bash
npm run build:css
```
تقوم هذه العملية بمعالجة `src/styles.css` وإخراج CSS المحوّل إلى `dist/styles.css`. على سبيل المثال، قد يضيف `autoprefixer` بادئات، وسيقوم `cssnano` بتصغيره:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **التكامل مع أداة بناء (اختياري)**
لإعداد أكثر قوة، قم بدمج PostCSS مع أدوات مثل Webpack أو Vite أو Gulp:

#### **مع Vite**
إذا كنت تستخدم Vite، قم بتثبيت `postcss` وقم بتكوينه في `vite.config.js`:
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
يتعامل Vite مع PostCSS تلقائيًا عند استيراد ملفات CSS.

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
لمعالجة CSS تلقائيًا أثناء التطوير، قم بتعديل السكريبت في `package.json`:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
شغّل `npm run watch:css` لمراقبة تغييرات الملف.

### 9. **الإضافات الشائعة**
إليك بعض إضافات PostCSS الشهيرة:
- `autoprefixer`: يضيف بادئات المتصفحات بناءً على دعم المتصفح.
- `cssnano`: يصغر CSS.
- `postcss-preset-env`: يتيح لك استخدام ميزات CSS المستقبلية اليوم.
- `postcss-import`: يحل قواعد `@import`.
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

### مثال على سير العمل
1. اكتب CSS حديث في `src/styles.css`:
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
2. شغّل `npm run build:css`.
3. احصل على CSS معالج في `dist/styles.css` مع البادئات والمتغيرات المحلولة والتصغير.

### نصائح
- استخدم `--map` في سطر الأوامر (`postcss src/styles.css -o dist/styles.css --map`) لإنشاء خرائط مصدرية لتصحيح الأخطاء.
- راجع وثائق الإضافات للحصول على خيارات التكوين المحددة.
- ادمج مع إطار عمل frontend (مثل React أو Vue) عن طريق ربط CSS الناتج بـ HTML أو أداة التجميع الخاصة بك.

دعني أعلم إذا كنت بحاجة إلى مساعدة في إعداد أو إضافة معينة!