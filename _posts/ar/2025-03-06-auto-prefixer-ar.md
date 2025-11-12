---
audio: false
generated: true
lang: ar
layout: post
title: استخدام أتوبريفيكسر
translated: true
type: note
---

سأشرح كيفية استخدام Autoprefixer في تطوير الواجهات الأمامية. Autoprefixer هو إضافة PostCSS تضيف بادئات البائعين تلقائيًا إلى CSS الخاص بك، مما يضمن التوافق بين المتصفحات.

إليك الطرق الرئيسية لدمج Autoprefixer في سير عمل الواجهة الأمامية الخاصة بك:

1. الاستخدام مع npm (النهج الأكثر شيوعًا)
```bash
# تثبيت autoprefixer و postcss
npm install autoprefixer postcss --save-dev
```

2. الإعداد الأساسي مع PostCSS CLI
```bash
# تثبيت postcss-cli
npm install postcss-cli --save-dev

# إنشاء ملف postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# الإضافة إلى scripts في package.json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. مع أدوات البناء:

أ) Webpack مع postcss-loader
```bash
npm install postcss-loader --save-dev
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: ['autoprefixer']
              }
            }
          }
        ]
      }
    ]
  }
}
```

ب) Vite (مدعوم مدمج)
```javascript
// vite.config.js
import autoprefixer from 'autoprefixer'

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
}
```

4. خيارات التهيئة
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // المتصفحات المستهدفة
      grid: true, // تمكين بادئات الـ grid
      flexbox: 'no-2009' // خيارات دعم الـ flexbox
    })
  ]
}
```

5. مثال للاستخدام في CSS
```css
/* الإدخال */
.container {
  display: flex;
  justify-content: space-between;
}

/* المخرجات (بعد Autoprefixer) */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

الميزات والنصائح الرئيسية:
- يضيف البادئات تلقائيًا بناءً على بيانات Can I Use
- يتم التحكم فيه عن طريق browserslist (عادة في package.json)
- يزيل البادئات القديمة من CSS الأقدم
- يعمل مع ميزات CSS الحديثة مثل الخصائص المخصصة

مثال أساسي لـ browserslist في package.json:
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

للتشغيل:
```bash
# مع PostCSS CLI
npx postcss src/*.css --dir dist

# أو مع npm script الخاص بك
npm run build:css
```

اختر طريقة الدمج بناءً على الإعداد الحالي لمشروعك (Webpack, Vite، إلخ). نهجي Webpack أو Vite هما الأكثر شيوعًا في تطوير الواجهات الأمامية الحديثة حيث يتم دمجهما جيدًا مع عمليات البناء الحالية.