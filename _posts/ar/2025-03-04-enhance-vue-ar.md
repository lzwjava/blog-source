---
audio: false
generated: true
lang: ar
layout: post
title: تطوير VUE.js
translated: true
---

### النقاط الرئيسية
- يبدو أن هذه الحزم تستخدم لتحسين تطوير VUE.js مع ميزات مثل إعادة تحميل الساخن وتحميل المكونات.
- تشير الأبحاث إلى إعداد هذه الحزم في تكوين webpack لـ VUE.js المشاريع، مع قواعد تحميل محددة.
- تشير الأدلة إلى ضمان توافق الإصدار، وخاصة لـ "vue-hot-reload-API"، والتي قد تحتاج إلى تعديل لـ VUE.js 2.x.

---

### نظرة عامة على الإعداد
لاستخدام الحزم "vue-hot-reload-API" (^1.2.0)، "vue-html-Loader" (^1.0.0)، "vue-Loader" (8.5.3)، و "vue-style-Loader" (^1.0.0) في مشروعك VUE.js، عليك تكوينها داخل إعداد webpack. هذه الأدوات تحسن التطوير من خلال تمكين إعادة تحميل الساخن وتعامل مع مكونات VUE بشكل فعال.

#### التثبيت
أولاً، قم بتثبيت الحزم باستخدام npm:
```bash
npm install --save-dev vue-hot-reload-API@^1.2.0 vue-html-Loader@^1.0.0 vue-Loader@8.5.3 vue-style-Loader@^1.0.0
```
ملاحظة: تأكد من توافق الإصدار مع نسخة VUE.js الخاصة بك، حيث قد لا يعمل "vue-hot-reload-API" الإصدار 1.2.0 مع VUE.js 2.x؛ يُنصح باستخدام الإصدار 2.x لـ VUE.js 2.x.

#### إعداد webpack
قم بتكوين ملف `webpack.config.js` الخاص بك مع قواعد لكل تحميل:
- استخدم "vue-Loader" لملفات `.vue` لتعامل مع مكونات VUE المفردة.
- استخدم "vue-html-Loader" لملفات `.html` إذا كنت تستخدم قوالب HTML خارجية.
- استخدم "vue-style-Loader" مع "css-Loader" لملفات `.css` لمعالجة الأسلوب.

مثال على التكوين:
```javascript
module.exports = {
  module: {
    rules: [
      { test: /\.vue$/, loader: 'vue-Loader' },
      { test: /\.html$/, loader: 'vue-html-Loader' },
      { test: /\.css$/, use: ['vue-style-Loader', 'css-Loader'] },
    ]
  }
};
```

#### استبدال وحدة الساخنة
قم بتفعيل إعادة تحميل الساخن من خلال تعيين `hot: true` في إعداد خادم تطوير webpack الخاص بك، وعلاجها في ملف الدخول الخاص بك لـ VUE.js 2.x:
```javascript
import 'vue-hot-reload-API'
import App from './App.vue'
const app = new App()
if (module.hot) {
  module.hot.accept(['./App.vue'], () => {
    const newApp = require('./App.vue').default
    app.$destroy()
    const newAppInstance = new newApp()
    newAppInstance.$mount('#app')
  })
}
app.$mount('#app')
```
ومع ذلك، "vue-Loader" عادةً ما يعالج HMR تلقائيًا مع إعداد مناسب.

#### التحقق
قم بتشغيل `npx webpack serve` لبدء خادم التطوير وتجربة تحرير ملفات `.vue` لضمان أن إعادة تحميل الساخن يعمل.

---

### ملاحظة الاستطلاع: إعداد مفصل لتطوير VUE.js مع تحميلات محددة

يقدم هذا القسم دليلًا شاملًا على دمج الحزم المحددة—"vue-hot-reload-API" (^1.2.0)، "vue-html-Loader" (^1.0.0)، "vue-Loader" (8.5.3)، و "vue-style-Loader" (^1.0.0)—في مشروع VUE.js، مع التركيز على أدوارها، الإعداد، واعتبارات التوافق والوظيفة. وهذا هو ذات الصلة بشكل خاص للمطورين الذين يعملون مع VUE.js 2.x، مع الأرقام الإصدارية المقدمة.

#### الخلفية وأدوار الحزم
VUE.js، إطار عمل JavaScript التقدمي لبناء واجهات المستخدم، يعتمد على أدوات مثل webpack لتجميع وتحسين سير العمل التطويري. الحزم المذكورة هي تحميلات وAPIات تسهل وظائف محددة:

- **"vue-Loader" (8.5.3)**: هذا هو التحميل الرئيسي لمكونات VUE.js المفردة (SFCs)، مما يسمح للمطورين بكتابة المكونات مع `<template>`, `<script>`, و `<style>` في ملف `.vue` واحد. يبدو أن الإصدار 8.5.3 متوافق مع VUE.js 2.x، حيث أن الأصدارات الجديدة (15 وما فوق) لـ VUE.js 3.x [Vue Loader Documentation](https://vue-loader.vuejs.org/).
- **"vue-hot-reload-API" (^1.2.0)**: هذه الحزمة تتيح استبدال وحدة الساخنة (HMR) لمكونات VUE، مما يسمح بتحديثات حية دون إعادة تحميل الصفحة بالكامل أثناء التطوير. ومع ذلك، تشير الأبحاث إلى أن الإصدار 1.x لـ VUE.js 1.x، و الإصدار 2.x لـ VUE.js 2.x، مما يشير إلى إمكانية مشاكل التوافق مع الإصدار المحدد [vue-hot-reload-API GitHub](https://github.com/vuejs/vue-hot-reload-api). وهذا هو تفصيل غير متوقع، حيث يشير إلى أن المستخدم قد يحتاج إلى تحديث إلى الإصدار 2.x لـ VUE.js 2.x.
- **"vue-html-Loader" (^1.0.0)**: fork من `html-loader`، يستخدم هذا لتعامل مع ملفات HTML، بشكل خاص لقوالب VUE، و هو محتمل استخدامه لتحميل ملفات HTML الخارجية كقوالب في المكونات [vue-html-Loader GitHub](https://github.com/vuejs/vue-html-loader).
- **"vue-style-Loader" (^1.0.0)**: هذا التحميل يعالج الأسلوب في مكونات VUE، يستخدم عادةً مع `css-loader` لتدخيل الأسلوب في DOM، مما يحسن سير عمل الأسلوب لمكونات SFCs [vue-style-Loader npm package](https://www.npmjs.com/package/vue-style-loader).

#### عملية التثبيت
لبدء، قم بتثبيت هذه الحزم كاعتمادات تطوير باستخدام npm:
```bash
npm install --save-dev vue-hot-reload-API@^1.2.0 vue-html-Loader@^1.0.0 vue-Loader@8.5.3 vue-style-Loader@^1.0.0
```
هذا الأمر يضمن إضافة الأصدارات المحددة إلى ملف `package.json` الخاص بك. لاحظ الرمز (`^`) في الأصدارات مثل "^1.2.0" يسمح بتحديث إلى أحدث إصدار ثانوي أو تصحيح في الإصدار الرئيسي، ولكن لـ "vue-Loader"، يتم تثبيت الإصدار 8.5.3 بشكل دقيق.

#### اعتبارات التوافق
مع الأصدارات، من المهم التأكد من التوافق مع نسخة VUE.js الخاصة بك. "vue-Loader" 8.5.3 يشير إلى بيئة VUE.js 2.x، حيث أن الأصدارات 15+ لـ VUE.js 3.x. ومع ذلك، "vue-hot-reload-API" الإصدار 1.2.0 يُذكر أنه لـ VUE.js 1.x، وهو قديم اعتبارًا من 3 مارس 2025، حيث أن VUE.js 2.x و 3.x أكثر شيوعًا. هذا الاختلاف يشير إلى أن المستخدم قد يواجه مشاكل، و يُنصح بتحديث إلى الإصدار 2.x لـ "vue-hot-reload-API" لـ VUE.js 2.x، وفقًا للتوثيق [vue-hot-reload-API GitHub](https://github.com/vuejs/vue-hot-reload-api).

#### تفاصيل إعداد webpack
يحتاج الإعداد إلى تكوين `webpack.config.js` لتحديد كيفية معالجة كل تحميل للملفات. أدناه هو تحليل مفصل:

| نوع الملف | تحميل (ات) المستخدم | الغرض                                                                 |
|-----------|------------------------------------|-------------------------------------------------------------------------|
| `.vue`    | `vue-Loader`                       | يعالج مكونات VUE المفردة، مع معالجة `<template>`, `<script>`, و `<style>`. |
| `.html`   | `vue-html-Loader`                  | يعالج ملفات HTML الخارجية، مفيد لتحميل القوالب بشكل منفصل، مع التعديلات لـ VUE. |
| `.css`    | `vue-style-Loader`, `css-Loader`   | يدخِل الأسلوب في DOM، مع `css-loader` يحل الواردات و `vue-style-Loader` يعالج إدخال الأسلوب. |

مثال على التكوين:
```javascript
const path = require('path');
module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-Loader'
      },
      {
        test: /\.html$/,
        loader: 'vue-html-Loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-Loader',
          'css-Loader'
        ]
      },
    ]
  },
  devServer: {
    hot: true
  }
};
```
هذا التكوين يضمن معالجة ملفات `.vue` بواسطة "vue-Loader"، ملفات `.html` بواسطة "vue-html-Loader" لقوالب خارجية، وملفات `.css` بواسطة سلسلة "vue-style-Loader" و "css-Loader". `devServer.hot: true` يفعّل HMR، يستفيد من "vue-hot-reload-API" تحت السطح.

#### إعداد استبدال وحدة الساخنة (HMR)
يتيح HMR تحديثات حية أثناء التطوير، يحفظ حالة التطبيق. "vue-Loader" عادةً ما يعالج هذا تلقائيًا عندما يكون `hot: true` في خادم التطوير. ومع ذلك، من أجل التحكم اليدوي، خاصة مع "vue-hot-reload-API"، يمكنك إضافة منطق في ملف الدخول الخاص بك. لمشروع VUE.js 2.x، مثال:
```javascript
import 'vue-hot-reload-API'
import App from './App.vue'
const app = new App()
if (module.hot) {
  module.hot.accept(['./App.vue'], () => {
    const newApp = require('./App.vue').default
    app.$destroy()
    const newAppInstance = new newApp()
    newAppInstance.$mount('#app')
  })
}
app.$mount('#app')
```
هذا الإعداد يضمن تحديث المكونات دون إعادة تحميل الصفحة بالكامل، مما يحسن كفاءة التطوير. لاحظ أن هذا الإعداد اليدوي قد يكون غير ضروري إذا كان "vue-Loader" مكوّن بشكل صحيح، حيث يستخدم "vue-hot-reload-API" داخليًا.

#### التحقق والتجربة
بعد التكوين، قم بتشغيل خادم التطوير باستخدام:
```bash
npx webpack serve
```
افتح تطبيقك في متصفح ويعدل ملف `.vue` لتجربة إعادة تحميل الساخن. يجب أن تظهر التغييرات دون إعادة تحميل كامل، مما يثبت أن HMR يعمل. إذا حدثت مشاكل، تأكد من إصدارات التحميل و تأكد من أن "vue-template-compiler" متوافقة مع نسخة VUE.js الخاصة بك، حيث أن "vue-Loader" يتطلب تنسيق [Vue Loader Documentation](https://vue-loader.vuejs.org/guide/).

#### ملاحظات إضافية والتفاصيل غير المتوقعة
تفصيل غير متوقع هو إمكانية عدم توافق "vue-hot-reload-API" الإصدار 1.2.0، والذي قد لا يدعم VUE.js 2.x، وفقًا للتوثيق الذي يشير إلى أن الإصدار 2.x لـ VUE.js 2.x. وهذا قد يؤدي إلى فشل إعادة تحميل الساخن، مما يتطلب تحديث. ملاحظات أخرى هي "vue-html-Loader"، الذي يستخدم بشكل أقل شيوعًا في إعدادات VUE.js الحديثة، حيث أن "vue-Loader" عادةً ما يعالج القوالب داخل SFCs، مما يشير إلى أن المستخدم قد يستخدم قوالب HTML خارجية، وهي ممارسة قديمة.

#### الخاتمة
يستخدم هذا الإعداد التحميلات المحددة لإنشاء بيئة تطوير VUE.js 2.x قوية، مع التركيز على التوافق والوظيفة HMR. تأكد من أن جميع الاعتماديات متوافقة، واختبر بشكل شامل لتحل أي مشاكل التوافق، خاصة مع "vue-hot-reload-API."

---

### الإشارات الرئيسية
- [Hot reload API for Vue components GitHub](https://github.com/vuejs/vue-hot-reload-api)
- [html loader module for webpack GitHub](https://github.com/vuejs/vue-html-loader)
- [Webpack loader for Vue.js components documentation](https://vue-loader.vuejs.org/)
- [Vue.js style loader module for webpack npm package](https://www.npmjs.com/package/vue-style-loader)