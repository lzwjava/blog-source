---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Autoprefixer
translated: true
---

سأشرح كيفية استخدام Autoprefixer في تطوير واجهات المستخدم. Autoprefixer هو إضافة PostCSS التي تضيف تلقائيًا أسبقية المورد إلى CSS الخاص بك، مما يضمن التوافق عبر المتصفحات المختلفة.

هنا هي الطرق الرئيسية لتكامل Autoprefixer في عملية تطوير واجهات المستخدم الخاصة بك:

1. استخدام مع npm (أكثر الطرق شيوعًا)
```bash
# تثبيت autoprefixer و postcss
npm install autoprefixer postcss --save-dev
```

2. إعداد أساسي مع PostCSS CLI
```bash
# تثبيت postcss-cli
npm install postcss-cli --save-dev

# إنشاء ملف postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# إضافة إلى scripts في package.json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. مع أدوات البناء:

a) Webpack مع postcss-loader
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

b) Vite (دعم مدمج)
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

4. خيارات التكوين
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // متصفحات الهدف
      grid: true, // تمكين أسبقية الشبكة
      flexbox: 'no-2009' // خيارات دعم flexbox
    })
  ]
}
```

5. مثال على الاستخدام في CSS
```css
/* المدخل */
.container {
  display: flex;
  justify-content: space-between;
}

/* المخرج (بعد Autoprefixer) */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

الميزات الرئيسية والنصائح:
- يضيف أسبقية تلقائيًا بناءً على بيانات Can I Use
- يتم التحكم فيه بواسطة browserslist (عادة في package.json)
- يبعد الأسبقية القديمة من CSS القديم
- يعمل مع ميزات CSS الحديثة مثل الخصائص المخصصة

مثال أساسي على browserslist في package.json:
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

للتنفيذ:
```bash
# مع PostCSS CLI
npx postcss src/*.css --dir dist

# أو مع npm script الخاص بك
npm run build:css
```

اختر طريقة التكامل بناءً على إعداد مشروعك الحالي (Webpack، Vite، إلخ). فطرق Webpack أو Vite هي الأكثر شيوعًا في تطوير واجهات المستخدم الحديثة لأنها تتكامل جيدًا مع عمليات البناء الحالية.