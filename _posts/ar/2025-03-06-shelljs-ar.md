---
audio: true
generated: true
lang: ar
layout: post
title: استخدام ShellJS لإجراء الأوامر البرمجية
translated: true
---

ShellJS هو مكتبة JavaScript توفر أوامر شيل يونكس (مثل `cp`، `mkdir`، `exec`، إلخ) للاستخدام في مشاريع Node.js. تسهل كتابة scripts متقاطعة المنصات من خلال السماح لك بتنفيذ الأوامر الشائعة للشيل مباشرة في JavaScript. ومع ذلك، عندما يتعلق الأمر بتطوير واجهات المستخدم - عادة ما يشير إلى الكود الذي يعمل في المتصفح - فلا يمكن استخدام ShellJS مباشرة لأنه يعتمد على APIs Node.js غير متاحة في بيئة المتصفح. أدناه، سأشرح لماذا هذا هو الحال وكيف يمكنك استخدام ShellJS بشكل فعال في سياق workflows تطوير واجهات المستخدم.

### لماذا لا يمكن تشغيل ShellJS مباشرة في المتصفح
- **تبعية Node.js**: تم بناء ShellJS على Runtime Node.js، الذي يوفر APIs للوصول إلى نظام الملفات، تنفيذ العمليات، وغيرها من العمليات على مستوى النظام. هذه APIs غير متاحة في المتصفح بسبب نموذج أمانه المقيّد.
- **قيود أمان المتصفح**: يمنع المتصفح JavaScript من الوصول إلى نظام الملفات المحلي أو تنفيذ الأوامر العشوائية لحماية المستخدمين من scripts ضارة. نظرًا لأن الأوامر مثل `exec` (لإطلاق العمليات الخارجية) أو `cp` (لنسخ الملفات) تعتمد على هذه القدرات، فلا يمكن أن تعمل في بيئة المتصفح.

بالتالي، لا يمكنك استخدام ShellJS مباشرة في JavaScript الجانب العميل الذي يعمل في المتصفح. ومع ذلك، يمكن أن يلعب ShellJS دورًا قيمة في تطوير واجهات المستخدم من خلال دمجه في عمليات البناء أو أدوات التطوير، والتي تعمل عادة على Node.js.

### كيفية استخدام ShellJS في workflows تطوير واجهات المستخدم
على الرغم من أن ShellJS لا يعمل في المتصفح، يمكنك استغلالها في scripts Node.js لتتمكن من تفعيل المهام التي تدعم تطوير واجهات المستخدم. تعتمد مشاريع واجهات المستخدم على أدوات البناء مثل Webpack، Gulp، أو Grunt، والتي تعمل على Node.js ويمكن أن تضم ShellJS لتسهيل workflows. إليك كيفية القيام بذلك:

#### 1. تثبيت ShellJS
أكد أولاً من أن لديك Node.js مثبتًا على نظامك. ثم أضف ShellJS إلى مشروعك باستخدام npm أو yarn:

```bash
npm install shelljs
```

أو

```bash
yarn add shelljs
```

#### 2. إنشاء Script Node.js مع ShellJS
اكتب Script يستخدم ShellJS لإجراء مهام ذات صلة بمشروع واجهات المستخدم، مثل نسخ الملفات، إنشاء المجلدات، أو تشغيل أدوات سطر الأوامر. احفظ هذا Script كملف `.js` (مثلًا `build.js`).

هنا مثال Script يهيئ موارد واجهات المستخدم:

```javascript
const shell = require('shelljs');

// إنشاء مجلد بناء إذا لم يكن موجودًا
shell.mkdir('-p', 'build');

// نسخ ملفات HTML إلى مجلد البناء
shell.cp('-R', 'src/*.html', 'build/');

// تجميع Sass إلى CSS
shell.exec('sass src/styles.scss build/styles.css');

// نسخ ملفات JavaScript
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: يخلق مجلد `build`، مع `-p` لضمان عدم حدوث خطأ إذا كان موجودًا بالفعل.
- **`shell.cp('-R', 'src/*.html', 'build/')`**: ينسخ جميع ملفات HTML من `src` إلى `build`، مع `-R` للنسخ التكراري.
- **`shell.exec('sass src/styles.scss build/styles.css')`**: ينفذ مجمع Sass لإنتاج CSS.

#### 3. دمج Script في workflow
يمكنك تشغيل هذا Script بطرق مختلفة:
- **مباشرة عبر Node.js**:
  ```bash
  node build.js
  ```
- **كScript npm**: أضفه إلى `package.json`:
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  ثم قم بتشغيل:
  ```bash
  npm run build
  ```
- **مع أدوات البناء**: ادخل ShellJS في أدوات مثل Gulp. على سبيل المثال:
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. استخدامات في تطوير واجهات المستخدم
يمكن أن يتمكن ShellJS من تفعيل مهام مختلفة في workflow واجهات المستخدم:
- **إدارة الموارد**: نسخ الصور، الخطوط، أو الملفات الثابتة الأخرى إلى مجلد البناء.
- **معالجة CSS/JavaScript**: تشغيل أدوات مثل Sass، PostCSS، أو UglifyJS عبر `shell.exec`.
- **التحقيق والتحليل**: تنفيذ محركات الاختبار أو المحلل (مثلًا `shell.exec('eslint src/*.js')`).
- **إعداد النشر**: حزم الملفات أو تنظيف المجلدات (مثلًا `shell.rm('-rf', 'build/*')`).

### مثال: تفعيل عملية بناء واجهات المستخدم
فكر أنك تقوم ببناء تطبيق ويب بسيط باستخدام HTML، Sass، وJavaScript. إليك كيفية استخدام ShellJS لتفعيل البناء:

**هيكل المجلد**:
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**:
```javascript
const shell = require('shelljs');

// تنظيف مجلد البناء
shell.rm('-rf', 'build/*');

// إنشاء مجلد البناء
shell.mkdir('-p', 'build');

// نسخ HTML
shell.cp('src/index.html', 'build/');

// تجميع Sass
shell.exec('sass src/styles.scss build/styles.css');

// نسخ JavaScript
shell.cp('src/app.js', 'build/');
```

**package.json**:
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

قم بتشغيل `npm run build`، وسيعمل ShellJS على إعداد مجلد `build` مع الملفات المتجمعة والنسخة، جاهزًا للنشر.

### النقاط الرئيسية
- **غير مناسب للاستخدام في المتصفح**: لا يمكن تشغيل ShellJS في المتصفح بسبب اعتمادها على Node.js وعمليات المستوى النظامي.
- **مفيد في Scripts البناء**: استخدمها في Scripts Node.js لتفعيل مهام واجهات المستخدم مثل معالجة الملفات وعمليات التنفيذ.
- **متقاطعة المنصات**: يضمن ShellJS أن Scripts تعمل بشكل متسق عبر Windows، Linux، وmacOS، مما يجعلها مثالية للبيئات التطويرية المتنوعة.

من خلال دمج ShellJS في عمليات البناء التي تعمل على Node.js، يمكنك تحسين workflow تطوير واجهات المستخدم باستخدام التفعيل القوي، حتى لو لا يعمل مباشرة في المتصفح.