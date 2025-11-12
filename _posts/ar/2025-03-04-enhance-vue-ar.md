---
audio: false
generated: true
lang: ar
layout: post
title: تحسين تطوير VUE.js
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المرجح أن هذه الحزم تُستخدم لتحسين تطوير VUE.js بميزات مثل إعادة التحميل الفوري (hot reloading) وتحميل المكونات.
- تشير الأبحاث إلى ضرورة إعداد هذه الحزم في تكوين webpack لمشاريع VUE.js، بما يتضمن قواعد محمل (loader) محددة.
- تميل الأدلة إلى التأكيد على ضرورة ضمان توافق الإصدارات، خاصةً بالنسبة لـ "vue-hot-reload-API"، والتي قد تحتاج إلى تعديل للعمل مع VUE.js 2.x.

---

### نظرة عامة على الإعداد
لاستخدام الحزم "vue-hot-reload-API" (^1.2.0)، و "vue-html-Loader" (^1.0.0)، و "vue-Loader" (8.5.3)، و "vue-style-Loader" (^1.0.0) في مشروع VUE.js الخاص بك، ستحتاج إلى تكوينها ضمن إعداد webpack. تعمل هذه الأدوات على تحسين عملية التطوير من خلال تمكين إعادة التحميل الفوري والتعامل مع مكونات VUE بكفاءة.

#### التثبيت
أولاً، قم بتثبيت الحزم باستخدام npm:
```bash
npm install --save-dev vue-hot-reload-API@^1.2.0 vue-html-Loader@^1.0.0 vue-Loader@8.5.3 vue-style-Loader@^1.0.0
```
ملاحظة: تأكد من التوافق مع إصدار VUE.js الخاص بك، حيث أن إصدار "vue-hot-reload-API" 1.2.0 قد لا يعمل مع VUE.js 2.x؛ يوصى باستخدام الإصدار 2.x لـ VUE.js 2.x.

#### تكوين Webpack
قم بتكوين ملف `webpack.config.js` الخاص بك بقواعد لكل محمل (loader):
- استخدم "vue-Loader" لملفات `.vue` للتعامل مع مكونات VUE ذات الملف الواحد (single-file components).
- استخدم "vue-html-Loader" لملفات `.html` إذا كنت تستخدم قوالب HTML خارجية.
- استخدم "vue-style-Loader" مع "css-Loader" لملفات `.css` لمعالجة الأنماط.

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

#### استبدال الوحدة الساخنة (Hot Module Replacement)
مكن إعادة التحميل الفوري عن طريق تعيين `hot: true` في تكوين خادم تطوير webpack، ويمكنك التعامل معه يدويًا في ملف الدخول الخاص بك لـ VUE.js 2.x:
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
ومع ذلك، فإن "vue-Loader" يتعامل عادةً مع HMR تلقائيًا مع الإعداد الصحيح.

#### التحقق
شغِّل `npx webpack serve` لبدء خادم التطوير واختبر العملية عن طريق تحرير ملفات `.vue` للتأكد من عمل إعادة التحميل الفوري.

---

### ملاحظة المسح: الإعداد التفصيلي لتطوير VUE.js باستخدام المحملات المحددة

يقدم هذا القسم دليلاً شاملاً لدمج الحزم المحددة—"vue-hot-reload-API" (^1.2.0)، و "vue-html-Loader" (^1.0.0)، و "vue-Loader" (8.5.3)، و "vue-style-Loader" (^1.0.0)—في مشروع VUE.js، مع التركيز على أدوارها وإعدادها واعتبارات التوافق والوظيفة. هذا ذو صلة خاصة بالمطورين الذين يعملون مع VUE.js 2.x، نظرًا لأرقام الإصدارات المقدمة.

#### الخلفية وأدوار الحزم
يعتمد VUE.js، وهو إطار عمل JavaScript تقدمي لبناء واجهات المستخدم، على أدوات مثل webpack للتجميع وتحسين سير عمل التطوير. الحزم المذكورة هي محملات (loaders) وواجهات برمجة تطبيقات (APIs) تسهل وظائف محددة:

- **"vue-Loader" (8.5.3)**: هذا هو المحمل الأساسي لمكونات VUE.js ذات الملف الواحد (SFCs)، مما يسمح للمطورين بكتابة المكونات بأقسام `<template>`، و `<script>`، و `<style>` في ملف `.vue` واحد. من المرجح أن الإصدار 8.5.3 متوافق مع VUE.js 2.x، حيث أن الإصدارات الأحدث (15 وما فوق) مخصصة لـ VUE.js 3.x [Vue Loader Documentation](https://vue-loader.vuejs.org/).
- **"vue-hot-reload-API" (^1.2.0)**: تمكن هذه الحزمة استبدال الوحدة الساخنة (HMR) لمكونات VUE، مما يسمح بالتحديثات المباشرة دون الحاجة إلى تحديث الصفحة بالكامل أثناء التطوير. ومع ذلك، تشير الأبحاث إلى أن الإصدار 1.x مخصص لـ VUE.js 1.x، وأن الإصدار 2.x مخصص لـ VUE.js 2.x، مما يشير إلى وجود مشاكل توافق محتملة مع الإصدار المحدد [vue-hot-reload-API GitHub](https://github.com/vuejs/vue-hot-reload-api). هذه تفصيلة غير متوقعة، لأنها تشير إلى أن المستخدم قد يحتاج إلى التحديث إلى الإصدار 2.x لمشاريع VUE.js 2.x.
- **"vue-html-Loader" (^1.0.0)**: وهي نسخة مشتقة (fork) من `html-loader`، تُستخدم للتعامل مع ملفات HTML، خاصةً لقوالب VUE، ومن المرجح أنها تُستخدم لتحميل ملفات HTML الخارجية كقوالب في المكونات [vue-html-Loader GitHub](https://github.com/vuejs/vue-html-loader).
- **"vue-style-Loader" (^1.0.0)**: يعالج هذا المحمل أنماط CSS في مكونات VUE، ويُستخدم عادةً بالتزامن مع `css-loader` لحقن الأنماط في DOM، مما يعزز سير العمل الخاص بالأنماط لـ SFCs [vue-style-Loader npm package](https://www.npmjs.com/package/vue-style-loader).

#### عملية التثبيت
للبدء، قم بتثبيت هذه الحزم كتبعيات تطوير باستخدام npm:
```bash
npm install --save-dev vue-hot-reload-API@^1.2.0 vue-html-Loader@^1.0.0 vue-Loader@8.5.3 vue-style-Loader@^1.0.0
```
يضمن هذا الأمر إضافة الإصدارات المحددة إلى ملف `package.json` الخاص بك. لاحظ أن علامة الإقحام (`^`) في إصدارات مثل "^1.2.0" تسمح بالتحديثات إلى أحدث إصدار ثانوي أو إصاححي ضمن الإصدار الرئيسي، ولكن بالنسبة لـ "vue-Loader"، فإن الإصدار المحدد 8.5.3 مثبت بدقة.

#### اعتبارات التوافق
نظرًا للإصدارات، من الضروري التأكد من التوافق مع إصدار VUE.js الخاص بك. يشير "vue-Loader" 8.5.3 إلى بيئة VUE.js 2.x، حيث أن الإصدارات 15+ مخصصة لـ VUE.js 3.x. ومع ذلك، يُلاحظ أن إصدار "vue-hot-reload-API" 1.2.0 مخصص لـ VUE.js 1.x، والذي أصبح قديمًا اعتبارًا من 3 مارس 2025، حيث أصبح VUE.js 2.x و 3.x أكثر شيوعًا. يشير هذا التناقض إلى أن المستخدم قد يواجه مشاكل، ويوصى بالترقية إلى الإصدار 2.x من "vue-hot-reload-API" لـ VUE.js 2.x، وفقًا للتوثيق [vue-hot-reload-API GitHub](https://github.com/vuejs/vue-hot-reload-api).

#### تفاصيل تكوين Webpack
يتطلب الإعداد تكوين `webpack.config.js` لتحديد كيفية معالجة كل محمل (loader) للملفات. فيما يلي تفصيل مفصل:

| نوع الملف | المحمل(ات) المستخدمة               | الغرض                                                                 |
|-----------|------------------------------------|-------------------------------------------------------------------------|
| `.vue`    | `vue-Loader`                       | يتعامل مع مكونات VUE ذات الملف الواحد، معالجة أقسام `<template>`، و `<script>`، و `<style>`. |
| `.html`   | `vue-html-Loader`                  | يعالج ملفات HTML الخارجية، مفيد لتحميل القوالب بشكل منفصل، مع تعديلات لـ VUE. |
| `.css`    | `vue-style-Loader`, `css-Loader`   | يحقن CSS في DOM، حيث يحل `css-loader` عمليات الاستيراد ويتعامل `vue-style-Loader` مع حقن الأنماط. |

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
يضمن هذا التكوين معالجة ملفات `.vue` بواسطة "vue-Loader"، وملفات `.html` بواسطة "vue-html-Loader" للقوالب الخارجية، وملفات `.css` بواسطة سلسلة "vue-style-Loader" و "css-Loader". يقوم `devServer.hot: true` بتمكين HMR، مستفيدًا من "vue-hot-reload-API" في الخلفية.

#### إعداد استبدال الوحدة الساخنة (HMR)
يسمح HMR بإجراء تحديثات مباشرة أثناء التطوير، مع الحفاظ على حالة التطبيق. يتعامل "vue-Loader" مع هذا تلقائيًا عادةً عند تعيين `hot: true` في خادم التطوير. ومع ذلك، للتحكم اليدوي، خاصةً مع "vue-hot-reload-API"، يمكنك إضافة منطق في ملف الدخول الخاص بك. لـ VUE.js 2.x، إليك مثال:
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
يضمن هذا الإعداد تحديث المكونات دون إعادة تحميل كامل للصفحة، مما يعزز كفاءة التطوير. لاحظ أن هذا الإعداد اليدوي قد يكون زائدًا عن الحاجة إذا تم تكوين "vue-Loader" بشكل صحيح، لأنه يستخدم "vue-hot-reload-API" داخليًا.

#### التحقق والاختبار
بعد التكوين، شغِّل خادم التطوير باستخدام:
```bash
npx webpack serve
```
افتح تطبيقك في متصفح وقم بتحرير ملف `.vue` لاختبار إعادة التحميل الفوري. يجب أن تنعكس التغييرات دون تحديث كامل، مما يؤكد عمل HMR. إذا ظهرت مشاكل، تحقق من إصدارات المحملات وتأكد من تطابق إصدار "vue-template-compiler" مع إصدار VUE.js الخاص بك، لأن "vue-Loader" يتطلب التزامن [Vue Loader Documentation](https://vue-loader.vuejs.org/guide/).

#### ملاحظات إضافية وتفاصيل غير متوقعة
إحدى التفاصيل غير المتوقعة هي عدم التطابق المحتمل مع إصدار "vue-hot-reload-API" 1.2.0، والذي قد لا يدعم VUE.js 2.x، نظرًا لأن التوثيق يشير إلى استخدام الإصدار 2.x لـ VUE.js 2.x. قد يؤدي هذا إلى فشل إعادة التحميل الفوري، مما يتطلب ترقية. اعتبار آخر هو "vue-html-Loader"، والذي يُستخدم بشكل أقل شيوعًا في إعدادات VUE.js الحديثة، حيث أن "vue-Loader" يتعامل عادةً مع القوالب داخل SFCs، مما يشير إلى أن المستخدم قد يستخدم قوالب HTML خارجية، وهي ممارسة أقدم.

#### الخاتمة
يستفيد هذا الإعداد من المحملات المحددة لتوفير بيئة تطوير قوية لـ VUE.js 2.x، مع الاهتمام بتوافق الإصدارات ووظيفة HMR. تأكد من محاذاة جميع التبعيات، واختبر بدقة لمعالجة أي مشاكل توافق، خاصةً مع "vue-hot-reload-API."

---

### الاقتباسات الرئيسية
- [Hot reload API for Vue components GitHub](https://github.com/vuejs/vue-hot-reload-api)
- [html loader module for webpack GitHub](https://github.com/vuejs/vue-html-loader)
- [Webpack loader for Vue.js components documentation](https://vue-loader.vuejs.org/)
- [Vue.js style loader module for webpack npm package](https://www.npmjs.com/package/vue-style-loader)