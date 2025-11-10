---
audio: false
generated: true
lang: ar
layout: post
title: تحسين أداء gtag.js على صفحات جيكل جيت هاب
translated: true
type: note
---

يُعد استخدام `gtag.js` على موقع GitHub Pages المُنشأ باستخدام Jekyll محفوفًا ببعض القيود الفريدة، نظرًا لأن GitHub Pages يمتلك تحكمًا محدودًا في جانب الخادم ولا يوفر وصولاً مباشرًا إلى عناوين التخزين المؤقت أو البرمجة النصية من جانب الخادم. ومع ذلك، لا يزال بإمكانك تحسين سرعة جلب `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` باستخدام تقنيات من جانب العميل وتكوينات محددة لـ Jekyll. فيما يلي استراتيجيات مستهدفة لتحسين أدائه في هذا السياق:

---

### 1. **تحميل `gtag.js` بشكل غير متزامن**
تأكد من تحميل البرنامج النصي `gtag.js` بشكل غير متزامن لتجنب حظر عرض الصفحة. في موقع Jekyll الخاص بك:
- أضف البرنامج النصي إلى تخطيط Jekyll أو ملف التضمين (مثل `_includes/analytics.html` أو مباشرة في تخطيط `default.html` الخاص بك).
- استخدم السمة `async`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- ضع هذا في `<head>` أو قبل `</body>` مباشرة في قالب Jekyll الخاص بك (مثل `_layouts/default.html`):
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **لماذا يساعد هذا**: تضمن `async` ألا يحظر البرنامج النصي تحليل HTML، مما يقلل من وقت التحميل المُدرك.

---

### 2. **إضافة Preconnect للنطاق الخاص بـ Google**
قلل من وقت البحث في DNS وزمن اتصال الوصل بإضافة تلميح `preconnect` لـ `googletagmanager.com`. في تخطيط Jekyll الخاص بك (`_layouts/default.html` أو `_includes/head.html`):
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- ضع هذا في `<head>` قبل البرنامج النصي `gtag.js`.
- **لماذا يساعد هذا**: يبدأ حل DNS واتصال TCP مبكرًا، مما يسرع من جلب `gtag.js`.

---

### 3. **التحميل البطيء (Lazy-Load) لـ `gtag.js`**
نظرًا لأن GitHub Pages ثابت، يمكنك استخدام التحميل البطيء لـ `gtag.js` لإعطاء الأولوية للمحتوى الحرج. أضف JavaScript التالي إلى قالب Jekyll الخاص بك أو إلى ملف JS منفصل (مثل `assets/js/analytics.js`):
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- قم بتضمين هذا البرنامج النصي في تخطيط Jekyll الخاص بك:
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **لماذا يساعد هذا**: يؤجل تحميل `gtag.js` حتى بعد تحميل موارد الصفحة الحرجة (مثل HTML، CSS)، مما يحسن من سرعة الصفحة الأولية.

---

### 4. **استخدام وكيل CDN عبر Cloudflare**
لا يسمح GitHub Pages بعناوين التخزين المؤقت المخصصة، ولكن يمكنك تمرير `gtag.js` عبر شبكة CDN مثل Cloudflare لتخزينه مؤقتًا بالقرب من مستخدميك:
1. **إعداد Cloudflare**:
   - أضف موقع GitHub Pages الخاص بك إلى Cloudflare (مثل `username.github.io`).
   - مكن DNS Cloudflare والتمرير الوكيل للنطاق الخاص بك.
2. **تمرير `gtag.js`**:
   - أنشئ قاعدة صفحة (Page Rule) في Cloudflare لتخزين البرنامج النصي `gtag.js` مؤقتًا أو استضافة نسخة محلية في مجلد `_site` بموقع Jekyll الخاص بك (مثل `assets/js/gtag.js`).
   - حدّث وسم البرنامج النصي:
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - زامن النسخة المحلية مع `gtag.js` الخاص بـ Google بشكل دوري لضمان تحديثها (عملية يدوية أو عبر برنامج نصي CI/CD).
3. **إعدادات التخزين المؤقت**:
   - في Cloudflare، عيّن قاعدة تخزين مؤقت للبرنامج النصي (مثل `Cache Everything` مع TTL لمدة ساعة واحدة).
- **لماذا يساعد هذا**: تقلّل خوادم حافة Cloudflare من زمن الوصل عن طريق تقديم البرنامج النصي من موقع أقرب لمستخدميك.
- **ملاحظة**: كن حذرًا عند تمرير البرامج النصية لـ Google، لأنها قد تتحدّث بشكل متكرر. اختبر بدقة لضمان عمل التتبع.

---

### 5. **تحسين بناء Jekyll والتسليم**
تأكد من تحسين موقع Jekyll الخاص بك لتقليل وقت تحميل الصفحة الإجمالي، مما يساعد بشكل غير مباشر في أداء `gtag.js`:
- **تصغير الأصول (Minify Assets)**:
  - استخدم إضافة Jekyll مثل `jekyll-compress` أو `jekyll-minifier` لتصغير HTML وCSS وJS.
  - أضف إلى `_config.yml` الخاص بك:
```yaml
plugins:
  - jekyll-compress
```
- **تمكين ضغط Gzip**:
  - يقوم GitHub Pages تلقائيًا بتمكين Gzip للملفات المدعومة، ولكن تأكد من ضغط ملفات CSS/JS الخاصة بك عن طريق التحقق من رأس `Content-Encoding` في أدوات مطوري المتصفح.
- **تقليل الموارد المعيقة (Blocking Resources)**:
  - قلل عدد ملفات CSS/JS التي تعيق العرض والتي يتم تحميلها قبل `gtag.js`.
  - استخدم `jekyll-assets` أو ما شابه لتحسين تسليم الأصول:
```yaml
plugins:
  - jekyll-assets
```
- **إدراج CSS الحرج داخل الصفحة (Inline Critical CSS)**:
  - أدرج CSS الحرج في `<head>` وأجّل CSS غير الحرج لتقليل الوقت المعيق للعرض، مما قد يجعل `gtag.js` يبدو وكأنه يتم تحميله بشكل أسرع.
- **تحسين الصور**:
  - ضغط الصور باستخدام `jekyll-picture-tag` أو إضافة مماثلة لتقليل وزن الصفحة الإجمالي، مما يحرر عرض النطاق الترددي لـ `gtag.js`.

---

### 6. **التبديل إلى Minimal Analytics**
إذا بقي `gtag.js` بطيئًا أو إذا لم يكن التحليلات حاسمًا:
- فكّر في بدائل خفيفة الوزن مثل Plausible أو Fathom، والتي تستخدم برامج نصية أصغر حجمًا (~1 كيلوبايت مقابل ~50 كيلوبايت لـ `gtag.js`).
- مثال لـ Plausible:
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- أضف هذا إلى `_includes/analytics.html` في Jekyll الخاص بك وقم بتضمينه في تخطيطك.
- **لماذا يساعد هذا**: يتم تحميل البرامج النصية الأصغر حجمًا بشكل أسرع، خاصةً على البنية التحتية الثابتة لـ GitHub Pages.

---

### 7. **اختبار ومراقبة الأداء**
- **قياس وقت الجلب**:
  - استخدم Chrome DevTools (علامة تبويب Network) للتحقق من وقت تحميل `gtag.js`.
  - اختبر باستخدام أدوات مثل Lighthouse أو WebPageTest لتقييم أداء الصفحة الإجمالي.
- **محاكاة مواقع المستخدمين**:
  - استخدم أداة مثل Pingdom لاختبار أوقات التحميل من المناطق التي يتواجد فيها جمهورك، حيث يختلف أداء GitHub Pages وCDN الخاص بـ Google جغرافيًا.
- **مراقبة مقاييس المستخدم الفعلي (Real User Metrics)**:
  - إذا كنت تستخدم Google Analytics، فتحقق من تقرير سرعة الموقع (Site Speed report) لتتبع تأثير `gtag.js`.
- **تصحيح الأخطاء المحدد لـ Jekyll**:
  - شغّل `jekyll build --profile` لتحديد المكونات ذات البناء البطيء في موقعك والتي قد تؤثر بشكل غير مباشر على الأداء.

---

### 8. **القيود مع GitHub Pages**
- **لا يوجد تحكم في جانب الخادم**: GitHub Pages هو مضيف ثابت، لذا لا يمكنك تنفيذ الوسم من جانب الخادم أو عناوين التخزين المؤقت المخصصة لـ `gtag.js`.
- **لا يوجد دعم لـ HTTP/3**: يستخدم GitHub Pages HTTP/2، وهو سريع ولكن ليس مُحسنًا مثل HTTP/3. يمكن لشبكة CDN مثل Cloudflare الترقية إلى HTTP/3.
- **زمن الوصل الجغرافي**: توجد خوادم GitHub Pages بشكل أساسي في الولايات المتحدة، لذا قد يواجه المستخدمون البعيدون عن الولايات المتحدة تحميلًا أبطأ. يمكن لشبكة CDن التخفيف من هذا.

---

### مثال على إعداد Jekyll
إليك نموذج لـ `_includes/analytics.html` لموقع Jekyll الخاص بك يجمع بين `preconnect` و `async`:
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
قم بتضمينه في تخطيطك (`_layouts/default.html`):
```html
<head>
</head>
```

---

### الخطوات التالية
- **اختبار الأداء الحالي**: شارك وقت الجلب الحالي لـ `gtag.js` (من أدوات مطوري المتصفح) أو عنوان URL لموقعك، ويمكنني تحليله further.
- **السياق الجغرافي**: أعلمني بالموقع الأساسي لجمهورك (مثل الولايات المتحدة، أوروبا، آسيا) لتخصيص توصيات CDN أو الوكيل.
- **إعداد Cloudflare**: إذا كنت منفتحًا على استخدام Cloudflare، فيمكنني تقديم خطوات مفصلة لتمرير `gtag.js`.
- **التحليلات البديلة**: إذا كنت منفتحًا على التبديل من Google Analytics، فيمكنني التوصية بأدوات محددة خفيفة الوزن وتكاملها مع Jekyll.

هل تريد مني التركيز على أي من هذه الجوانب أو إجراء تحليل محدد (مثل اختبار أداء موقعك أو تقديم دليل إعداد Cloudflare)؟