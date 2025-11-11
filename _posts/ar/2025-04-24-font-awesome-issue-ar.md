---
audio: false
generated: true
lang: ar
layout: post
title: مشكلة فونت أويسم
translated: true
type: note
---

يحدث خطأ "can't resolve .../fonts/fontawesome-webfont.woff2" عادةً عندما يشير ملف Font Awesome CSS إلى ملف خط (مثل `fontawesome-webfont.woff2`) لا يمكن العثور عليه في المسار المحدد. غالبًا ما تظهر هذه المشكلة في المشاريع التي تستخدم npm أو Webpack أو حزم الوحدات الأخرى. فيما يلي خطوات لحل هذا الخطأ:

---

### 1. التحقق من تثبيت Font Awesome
تأكد من تثبيت Font Awesome بشكل صحيح في مشروعك.

- **إذا كنت تستخدم npm**:
  ```bash
  npm install @fortawesome/fontawesome-free
  ```
  يقوم هذا بتثبيت الإصدار المجاني من Font Awesome.

- تحقق من إدراج الحزمة في ملف `package.json` الخاص بك:
  ```json
  "dependencies": {
    "@fortawesome/fontawesome-free": "^6.x.x"
  }
  ```

---

### 2. التحقق من مسار ملف الخط في CSS
غالبًا ما يحدث الخطأ لأن ملف `fontawesome.css` يشير إلى ملفات الخطوط بمسار نسبي (مثل `../fonts/fontawesome-webfont.woff2`) لا يتوافق مع هيكل ملفات مشروعك أو عملية البناء.

- **حدد موقع ملف CSS**:
  ابحث عن ملف Font Awesome CSS في `node_modules/@fortawesome/fontawesome-free/css/all.css` (أو ما شابه).

- **افحص تعريف font-face**:
  افتح ملف CSS وابحث عن قاعدة `@font-face`. قد تبدو هكذا:
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('../fonts/fontawesome-webfont.woff2') format('woff2'),
         url('../fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- **تحقق من ملفات الخطوط**:
  تحقق مما إذا كانت ملفات الخطوط المشار إليها موجودة في `node_modules/@fortawesome/fontawesome-free/webfonts/`. يحتوي مجلد `webfonts` عادةً على ملفات مثل `fontawesome-webfont.woff2`.

---

### 3. إصلاح مشاكل المسار
إذا لم يتم حل ملفات الخطوط، فقد تحتاج إلى ضبط كيفية معالجة المسارات في عملية البناء الخاصة بك.

#### الخيار 1: نسخ ملفات الخطوط إلى الدليل العام (Public) الخاص بك
انسخ ملفات الخطوط يدويًا إلى دليل يمكن لتطبيقك الوصول إليه (مثل `public/fonts` أو `src/fonts`).

- **انسخ الملفات**:
  ```bash
  mkdir -p public/fonts
  cp -r node_modules/@fortawesome/fontawesome-free/webfonts/* public/fonts/
  ```

- **حدّث ملف CSS**:
  عدّل ملف `fontawesome.css` ليشير إلى موقع الخطوط الجديد:
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('/fonts/fontawesome-webfont.woff2') format('woff2'),
         url('/fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- بدلاً من ذلك، يمكنك استخدام معالج CSS مسبق أو لاحق لإعادة كتابة المسارات.

#### الخيار 2: تكوين Webpack (أو الحزم الأخرى)
إذا كنت تستخدم Webpack، فتأكد من أنه يمكنه حل ملفات الخطوط وتحميلها.

- **ثبّت file-loader أو url-loader**:
  ```bash
  npm install file-loader --save-dev
  ```

- **حدّث تكوين Webpack** (`webpack.config.js`):
  أضف قاعدة للتعامل مع ملفات الخطوط:
  ```javascript
  module: {
    rules: [
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/',
              publicPath: '/fonts/',
            },
          },
        ],
      },
    ],
  }
  ```

- تأكد من استيراد Font Awesome CSS في JavaScript الخاص بك:
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```

#### الخيار 3: استخدام CDN
إذا كنت لا تريد تضمين ملفات الخطوط، يمكنك استخدام CDN لتحميل Font Awesome.

- استبدال الاستيراد المحلي برابط CDN في HTML الخاص بك:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  ```

- أزل استيراد Font Awesome CSS المحلي من الكود الخاص بك.

---

### 4. التحقق من حساسية حالة الأحرف (Case Sensitivity)
مسارات الملفات حساسة لحالة الأحرف في بعض الأنظمة (مثل Linux). تأكد من أن أسماء الملفات والمسارات في CSS تطابق أسماء الملفات الفعلية تمامًا.

- على سبيل المثال، إذا كان الملف اسمه `fontawesome-webfont.woff2`، لكن CSS يشير إلى `FontAwesome-WebFont.woff2`، فسيفشل.

---

### 5. مسح الذاكرة المؤقتة وإعادة البناء
في بعض الأحيان، تسبب ذاكرة التخزين المؤقتة القديمة مشاكل في الحل.

- امسح ذاكرة التخزين المؤقتة npm:
  ```bash
  npm cache clean --force
  ```

- احذف `node_modules` و `package-lock.json`، ثم أعد التثبيت:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

- أعد بناء مشروعك:
  ```bash
  npm run build
  ```

---

### 6. بديل: استخدام Font Awesome عبر SCSS
إذا كنت تستخدم SCSS، يمكنك استيراد ملفات SCSS الخاصة بـ Font Awesome وتكوين مسار الخط.

- ثبّت Font Awesome كما هو مذكور أعلاه.
- استورد SCSS في ملف SCSS الرئيسي الخاص بك:
  ```scss
  $fa-font-path: '~@fortawesome/fontawesome-free/webfonts';
  @import '~@fortawesome/fontawesome-free/scss/fontawesome';
  @import '~@fortawesome/fontawesome-free/scss/solid';
  ```

- تأكد من أن مترجم SCSS الخاص بك يحل مجلد `webfonts` بشكل صحيح.

---

### 7. نصائح لتصحيح الأخطاء
- **تحقق من console المتصفح**:
  ابحث عن أخطاء 404 لملفات الخطوط ولاحظ عنوان URL المطلوب.
- **افحص ناتج البناء**:
  تحقق من تضمين ملفات الخطوط في دليل الإخراج (مثل `dist/fonts/`).
- **استخدم `resolve-url-loader`**:
  إذا كنت تستخدم Webpack مع SCSS، فثبّت `resolve-url-loader` للمساعدة في حل عناوين URL النسبية:
  ```bash
  npm install resolve-url-loader --save-dev
  ```

---

### 8. إذا كنت تستخدم إطار عمل (Framework)
قد تتطلب بعض أطر العمل (مثل React أو Vue أو Angular) تكوينًا إضافيًا:

- **React**:
  تأكد من أنك تستورد CSS في `index.js` أو `App.js` الخاص بك:
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```
  استخدم تكوين Webpack أعلاه إذا لزم الأمر.

- **Vue**:
  إذا كنت تستخدم Vue CLI، أضف قاعدة Webpack إلى `vue.config.js`:
  ```javascript
  module.exports = {
    chainWebpack: (config) => {
      config.module
        .rule('fonts')
        .test(/\.(woff|woff2|eot|ttf|otf)$/)
        .use('file-loader')
        .loader('file-loader')
        .options({
          name: '[name].[ext]',
          outputPath: 'fonts/',
          publicPath: '/fonts/',
        });
    },
  };
  ```

- **Angular**:
  أضف Font Awesome CSS إلى `angular.json`:
  ```json
  "styles": [
    "node_modules/@fortawesome/fontawesome-free/css/all.css",
    "src/styles.css"
  ]
  ```

---

### 9. اختيار الإصلاح
- شغّل خادم التطوير الخاص بك:
  ```bash
  npm start
  ```
- افتح تطبيقك في المتصفح وتحقق من تحميل أيقونات Font Awesome بشكل صحيح دون أخطاء في الـ console.

---

### 10. إذا استمرت المشكلة
- **تحقق من وجود إصدارات متضاربة**:
  تأكد من أنك لا تخلط بين إصدارات مختلفة من Font Awesome (مثل الإصدار 5 والإصدار 6).
- **ابحث عن مشاكل مشابهة**:
  ابحث عن أخطاء محددة لإعداداتك (مثل Webpack أو Create React App) على Stack Overflow أو GitHub.
- **قدّم المزيد من التفاصيل**:
  إذا كنت بحاجة إلى مزيد من المساعدة، شارك:
  - إعداد مشروعك (مثل Webpack أو React، إلخ).
  - رسالة الخطأ الدقيقة.
  - مقاطع الكود ذات الصلة (مثل كيفية استيرادك لـ Font Awesome).

---

يجب أن يحل هذا خطأ "can't resolve .../fonts/fontawesome-webfont.woff2". أعلمني إذا كنت بحاجة إلى مساعدة في خطوة محددة!