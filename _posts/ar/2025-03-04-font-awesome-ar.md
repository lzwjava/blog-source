---
audio: false
generated: true
lang: ar
layout: post
title: حزمة Font Awesome في NPM
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام حزمة "font-awesome" npm (النسخة 4) يتطلب أولًا تثبيتها باستخدام `npm install font-awesome`، ثم ربط ملف CSS في HTML، واستخدام الأيقونات باستخدام الفئات مثل `<i class="fa fa-home"></i>`.
- تشير الأبحاث إلى أن النسخة 4 قديمة ولا يتم صيانتها anymore؛ فاعتبر الترقية إلى النسخة 6 للحصول على التحديثات والأمن، باستخدام حزم مثل `@fortawesome/fontawesome-free`.

---

### التثبيت واستخدام أساسي
لبدء استخدام حزمة "font-awesome" npm (النسخة 4)، ابدأ بتثبيتها باستخدام الأمر `npm install font-awesome`. بعد التثبيت، أضف ملف CSS في HTML باستخدام `<link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">`. يمكنك بعد ذلك استخدام الأيقونات في صفحة الويب الخاصة بك بإضافة HTML مثل `<i class="fa fa-home"></i>`, استبدل `fa-home` باسم الأيقونة المراد، والذي يمكنك العثور عليه في [دليل Font Awesome الإصدار 4](https://fontawesome.com/v4/cheatsheet).

### طرق بديلة
إذا كنت تستخدم أداة بناء مثل webpack، يمكنك استيراد CSS مباشرة في ملف JavaScript باستخدام `import 'font-awesome/css/font-awesome.min.css';`. بالنسبة للمشاريع التي تستخدم Less أو Sass، يمكنك استيراد الملفات المناسبة، مثل `@import "node_modules/font-awesome/less/font-awesome";` في Less، مع التأكد من تعديل المسار حسب الحاجة.

### ملاحظة حول الإصدارات
تفصيل غير متوقع هو أن حزمة "font-awesome" هي الإصدار 4، والتي لم يتم تحديثها منذ أكثر من ثماني سنوات ولا يتم صيانتها anymore. للحصول على الميزات والأمن الأحدث، فاعتبر الترقية إلى الإصدار 6، المتاحة عبر `@fortawesome/fontawesome-free` (مجانية) أو `@fortawesome/fontawesome-pro` (مشترك، يتطلب الاشتراك). قم بتثبيت الإصدار 6 باستخدام `npm install @fortawesome/fontawesome-free` واستيراده باستخدام `import '@fortawesome/fontawesome-free/css/all.min.css';`. مزيد من التفاصيل في [دليل Font Awesome](https://fontawesome.com/docs/web/use-with/node-js).

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام حزمة Font Awesome npm

يقدم هذا القسم استكشافًا مفصلًا لاستخدام حزمة "font-awesome" npm، مع التركيز على الإصدار 4، بينما يعالج أيضًا الانتقال إلى الإصدار 6 الأحدث. يتم استخلاص المعلومات من الوثائق الرسمية، تفاصيل حزمة npm، ومحادثات المجتمع، مما يضمن فهمًا شاملًا للمطورين في جميع المستويات.

#### الخلفية والسياق
تتمثل حزمة "font-awesome" npm، كما هو مدرج على [npm](https://www.npmjs.com/package/font-awesome)، في الإصدار 4.7.0 من Font Awesome، الذي تم نشره منذ ثماني سنوات، مما يجعله إصدارًا قديمًا، الآن نهاية الحياة. Font Awesome هو أداة شائعة لتجميع الأيقونات المتجهية، والتي يتم استخدامها على نطاق واسع في تطوير الويب لإضافة الأيقونات إلى المواقع. يعتمد الإصدار 4 بشكل أساسي على CSS لإدخال الأيقونات، باستخدام ملفات الخط، ويعرف بسهولة استخدامه ولكن يفتقر إلى الميزات الحديثة والتحديثات التي توجد في الإصدارات اللاحقة.

بسبب عمرها، فإن الوثائق للنسخة 4 لا تزال متاحة في [دليل Font Awesome الإصدار 4](https://fontawesome.com/v4/)، ولكن الموقع الرسمي الآن يركز على الإصدار 6، مع اعتبار الإصدار 4 نهاية الحياة، كما هو موضح في محادثات GitHub في [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome). هذا الانتقال يوضح أهمية اعتبار الترقية لمشاريع مستمرة، خاصة لأسباب الأمنية وتطوير الميزات.

#### استخدام حزمة "font-awesome" (النسخة 4) عبر npm
لتعزيز حزمة "font-awesome"، اتبع هذه الخطوات، والتي تتوافق مع الممارسات القياسية لـ npm والمجتمع:

1. **التثبيت:**
   - قم بتشغيل الأمر `npm install font-awesome` في دليل المشروع الخاص بك. هذا يثبيت الإصدار 4.7.0، ويضع الملفات في دليل `node_modules/font-awesome`.
   - تحتوي الحزمة على CSS، Less، وملفات الخط، كما هو موضح في وصفها في npm، والذي يوضح الصيانة تحت نظام الإصدار السيميائي، ويشمل تعليمات لاستخدام Less.

2. **الضم في HTML:**
   - بالنسبة للاستخدام الأساسي، ربط ملف CSS في رأس HTML باستخدام:
     ```html
     <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
     ```
   - تأكد من صحة المسار؛ إذا لم يكن HTML في الجذر، فعدل حسب الحاجة (مثل `../node_modules/font-awesome/css/font-awesome.min.css`).

3. **استخدام الأيقونات:**
   - تستخدم الأيقونات باستخدام HTML مثل `<i class="fa fa-home"></i>`, حيث `fa` هو الفئة الأساسية، و `fa-home` يحدد الأيقونة. قائمة شاملة متاحة في [دليل Font Awesome الإصدار 4](https://fontawesome.com/v4/cheatsheet).
   - هذا الأسلوب يستفيد من ملفات الخط المضمنة، مما يضمن التوسع والتخصيص باستخدام CSS.

4. **الدمج البديل مع أدوات البناء:**
   - إذا كنت تستخدم أداة بناء مثل webpack، استورد CSS في JavaScript:
     ```javascript
     import 'font-awesome/css/font-awesome.min.css';
     ```
   - هذا الأسلوب شائع في تطوير الويب الحديث، مما يضمن أن CSS يتم تجميعه مع مشروعك.

5. **دعم Less و Sass:**
   - بالنسبة للمشاريع التي تستخدم Less، يمكنك استيراد الملفات مباشرة، كما هو موضح في محادثات المجتمع، مثل:
     ```less
     @import "node_modules/font-awesome/less/font-awesome";
     ```
   - بشكل مشابه، بالنسبة لـ Sass، فعدل المسارات حسب الحاجة، على الرغم من أن الحزمة تدعم Less بشكل أساسي للنسخة 4، كما هو مرئي في دمج Ruby Gem لـ Rails، والذي يتضمن `font-awesome-less` و `font-awesome-sass`.

#### استنتاجات عملية ومشاهدات المجتمع
تكشف محادثات المجتمع، مثل تلك في Stack Overflow، عن الممارسات الشائعة مثل نسخ الملفات إلى دليل عام للإنتاج، استخدام مهام gulp، أو استيراد مكونات Less المحددة لتخفيض حجم الحزمة. على سبيل المثال، اقترح مستخدم استيراد ملفات Less المحددة فقط لحفظ البايتات، على الرغم من أن المستخدم أشار إلى توفير قليل، مما يشير إلى:
   - `@import "@{fa_path}/variables.less";`
   - `@import "@{fa_path}/mixins.less";`، وغير ذلك، مع تعديل `@fa_path` إلى `"../node_modules/font-awesome/less"`.

ومع ذلك، بالنسبة لأغلبية المستخدمين، فإن ربط ملف CSS مباشرة يكون كافيًا، خاصة لمشاريع صغيرة إلى متوسطة. يحتوي محتوى حزمة npm أيضًا على متطلبات Bundler و Less Plugin، مما يشير إلى إعدادات إضافية للمستخدمين المتقدمين، مثل:
   - تثبيت Less عالميًا باستخدام `npm install -g less`.
   - استخدام Less Plugin Clean CSS باستخدام `npm install -g less-plugin-clean-css`.

#### ملاحظة حول قيود الإصدار 4 و مسار الترقية
النسخة 4، على الرغم من أنها تعمل، لا يتم صيانتها anymore، مع توفير إصلاحات الأخطاء الحرجة فقط للنسخة 5 تحت دعم طويل الأجل (LTS)، ونسخ 3 و 4 تم تحديدها نهاية الحياة، وفقًا لـ [FortAwesome/Font-Awesome GitHub](https://github.com/FortAwesome/Font-Awesome). وهذا يعني عدم وجود ميزات جديدة، أو تصحيحات أمنية، أو تحديثات، وهو قلق كبير لمشاريع طويلة الأجل.

للترقية، يقدم الإصدار 6 تغييرات كبيرة، بما في ذلك SVG مع JavaScript، وأسلوب جديد (Solid، Regular، Light، Duotone، Thin)، وأيقونات العلامة التجارية منفصلة. لتحويل، قم بتثبيت `@fortawesome/fontawesome-free` باستخدام:
   - `npm install @fortawesome/fontawesome-free`
   - استيراده باستخدام `import '@fortawesome/fontawesome-free/css/all.min.css';`، مع ملاحظة تغيير اسم ملف CSS إلى `all.min.css` من الإصدار 6، مما يعكس دعم أوسع للأيقونات.

توفر تعليمات الترقية التفصيلية في [ترقية Font Awesome من الإصدار 4](https://fontawesome.com/docs/web/setup/upgrade/upgrade-from-v4)، والتي تتضمن ملاحظات التوافق و الخطوات لإزالة ملفات الإصدار 4، مما يضمن انتقالًا سلسًا.

#### جدول المقارنة: استخدام الإصدار 4 مقابل الإصدار 6

| الجوانب                  | الإصدار 4 (font-awesome)                     | الإصدار 6 (@fortawesome/fontawesome-free)    |
|-------------------------|---------------------------------------------|---------------------------------------------|
| أمر التثبيت            | `npm install font-awesome`                  | `npm install @fortawesome/fontawesome-free` |
| اسم ملف CSS             | `font-awesome.min.css`                      | `all.min.css`                               |
| مثال استخدام الأيقونات  | `<i class="fa fa-home"></i>`                | `<i class="fas fa-home"></i>` (Solid style) |
| حالة الصيانة           | نهاية الحياة، لا تحديثات                     | يتم صيانتها بشكل فعال، الإصدار 6.7.2 الأحدث   |
| الميزات الإضافية       | CSS أساسي، دعم Less                     | SVG مع JS، أسلوب متعدد، دعم API   |
| URL الوثائق             | [وثائق الإصدار 4](https://fontawesome.com/v4/) | [وثائق الإصدار 6](https://fontawesome.com/docs/web/use-with/node-js) |

يوضح هذا الجدول التطور، مما يساعد المطورين في اتخاذ قرارات الترقية.

#### الخاتمة والتوصيات
للمشاريع الجديدة، فاعتبر بشدة الإصدار 6 بسبب دعمه الفعال وميزاته الحديثة. بالنسبة لمشاريع موجودة تستخدم الإصدار 4، فاقترن مسار الترقية، خاصة لأسباب أمنية، مع الأخذ في الاعتبار الفجوة الثمانية سنوات. تضمن الخطوات الواردة أن تكون الوظيفة مع الإصدار 4، ولكن النهج المستقبلي هو تبني الإصدار 6، مع توجيهات مفصلة في [دليل Font Awesome](https://fontawesome.com/docs/web/use-with/node-js).

يضمن هذا الدليل الشامل أن يكون للمستخدمون جميع المعلومات اللازمة، من التثبيت الأساسي إلى الدمج المتقدم، مع معالجة الحاجة الحرجة لتحديثات في منظر تكنولوجي متطور بسرعة.

---

### الإشارات الرئيسية
- [دليل Font Awesome الإصدار 4 مع جدول المساعدة](https://fontawesome.com/v4/)
- [حزمة font-awesome على npm مع تفاصيل الإصدار 4.7.0](https://www.npmjs.com/package/font-awesome)
- [مستودع GitHub FortAwesome Font-Awesome مع تاريخ الإصدار](https://github.com/FortAwesome/Font-Awesome)