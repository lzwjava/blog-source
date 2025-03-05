---
audio: false
generated: true
lang: ar
layout: post
title: استخدام BrowserSync
translated: true
---

BrowserSync هو أداة رائعة لتسهيل تطوير واجهات المستخدم من خلال تزامن أفعال المتصفح، تحميل الملفات تلقائيًا، وتوفير خادم تطوير محلي. إليك دليل خطوة بخطوة على كيفية استخدام BrowserSync في عملية تطوير واجهات المستخدم الخاصة بك:

---

### 1. **تثبيت Node.js و npm**
BrowserSync هو أداة Node.js، لذا تحتاج إلى تثبيت Node.js و npm (Node Package Manager). إذا لم يكن لديكهما بعد:
- قم بتنزيل وتثبيت من [nodejs.org](https://nodejs.org/).
- التحقق من التثبيت:
  ```bash
  node -v
  npm -v
  ```

---

### 2. **تثبيت BrowserSync**
يمكنك تثبيت BrowserSync عالميًا أو محليًا في مشروعك.

#### خيار 1: تثبيت عالمي
أدخل هذا الأمر في مستودعك لتثبيت BrowserSync عالميًا:
```bash
npm install -g browser-sync
```
هذا يسمح لك باستخدام الأمر `browser-sync` من أي مكان.

#### خيار 2: تثبيت محلي (موصى به للمشاريع)
إذا كنت تفضل ربط الاعتماديات بمشروع معين:
```bash
npm install browser-sync --save-dev
```
هذا يضيف BrowserSync إلى `node_modules` لمشروعك ويضيفه إلى `package.json`.

---

### 3. **بدء BrowserSync**
حسب إعدادك، يمكنك استخدام BrowserSync بطرق مختلفة:

#### الاستخدام الأساسي (ملفات ثابتة)
إذا كنت تعمل مع ملفات HTML، CSS، و JS ثابتة، انتقل إلى مجلد المشروع واكتب:
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`: يبدء خادمًا محليًا (يخدم الملفات من الدليل الحالي).
- `--files`: يراقب هذه الملفات للتغييرات ويجدد المتصفح تلقائيًا.

على سبيل المثال، إذا كان هيكل مجلدك:
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
إدخال الأمر أعلاه سيؤدي إلى:
- بدء خادم على `http://localhost:3000` (المنفذ الافتراضي).
- فتح المتصفح الافتراضي.
- تجديد الصفحة كلما تغيرت `index.html` أو `style.css` أو `script.js`.

#### وضع الوكيل (خادم موجود)
إذا كنت تستخدم خادم خلفي (مثل Node.js، PHP، أو Python)، استخدم خيار الوكيل:
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`: يوجه الطلبات إلى خادمك الموجود (استبدل `http://localhost:8000` بURL خادمك).
- BrowserSync سيضيف ميزاته (مثل تجديد تلقائي) فوقه.

---

### 4. **الميزات الرئيسية**
بعد بدء تشغيل BrowserSync، ستحصل على:
- **تجديد مباشر**: يتسبب التغييرات في الملفات المراقبة في تجديد المتصفح فورًا.
- **تزامن عبر الأجهزة**: التمرير، النقر، و إدخال البيانات في النموذج يتزامن عبر جميع الأجهزة المتصلة (مثل الكمبيوتر، الهاتف، والحواسيب اللوحية).
- **لوحة تحكم UI**: الوصول إلى لوحة تحكم في `http://localhost:3001` (المنفذ الافتراضي) لتعديل الإعدادات أو إيقاف الخادم.

---

### 5. **الدمج مع أدوات البناء (اختياري)**
إذا كنت تستخدم أدوات مثل Gulp أو Webpack، يمكن دمج BrowserSync بسهولة.

#### مثال مع Gulp
تثبيت Gulp و BrowserSync:
```bash
npm install --save-dev gulp browser-sync
```
إنشاء ملف `gulpfile.js`:
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // تقديم الملفات من الدليل الحالي
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
إدخاله:
```bash
gulp
```

---

### 6. **الأوامر الشائعة والأختيارات**
- تغيير المنفذ: `--port 8080`
- تعطيل فتح تلقائي: `--no-open`
- مراقبة ملفات محددة: `--files "path/to/files/*"`
- قائمة كاملة: أدخل `browser-sync --help`

---

### 7. **إصلاح الأخطاء**
- **المنفذ قيد الاستخدام**: تغيير المنفذ باستخدام `--port <number>`.
- **لا تجديد**: تأكد من أن مسارات الملفات في `--files` تتطابق مع هيكل المشروع.
- **الصلاحيات**: إذا كان التثبيت عالميًا، قد تحتاج إلى `sudo` (مثل `sudo npm install -g browser-sync` في Linux/macOS).

---

هذا هو كل شيء! الآن BrowserSync جاهز لتسريع عملية تطوير واجهات المستخدم الخاصة بك. ابدأ باستخدام الأمر الأساسي، قم بتعديله حسب الحاجة، واستمتع بعملية عمل أكثر سلاسة. اتصل بي إذا كنت تحتاج إلى مساعدة في إعداد معين!