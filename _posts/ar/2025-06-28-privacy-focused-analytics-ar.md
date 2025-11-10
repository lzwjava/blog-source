---
audio: false
generated: true
lang: ar
layout: post
title: دليل تحليلات الويب المرتكز على الخصوصية
translated: true
type: note
---

Cloudflare Web Analytics هو أداة مجانية تركز على الخصوصية مصممة لمساعدة مالكي المواقع على تتبع وفهم أداء الموقع وسلوك الزوار دون المساس بخصوصية المستخدم. فيما يلي دليل شامل لإعداد واستخدام Cloudflare Web Analytics، استنادًا إلى أحدث المعلومات المتاحة.

### نظرة عامة على Cloudflare Web Analytics
يوفر Cloudflare Web Analytics رؤى حول حركة مرور الموقع، ومشاهدات الصفحة، ومقاييس الأداء مع إعطاء الأولوية لخصوصية المستخدم. على عكس أدوات التحليلات التقليدية التي قد تتعقب البيانات الشخصية أو تستخدم ملفات تعريف الارتباط، يتجنب حل Cloudflare طرق التتبع التطفلية مثل البصمة الرقمية أو ملفات تعريف الارتباط أو التخزين المحلي لأغراض التحليلات. إنه مناسب لمواقع الويب بجميع الأحجام ويمكن استخدامه مع أو بدون خدمات الوكيل الخاصة بـ Cloudflare.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### الميزات الرئيسية
- **الخصوصية أولاً**: لا يجمع بيانات شخصية، ولا يستخدم ملفات تعريف الارتباط، ولا يتتبع المستخدمين عبر عناوين IP أو وكلاء المستخدم، مما يضمن الامتثال للوائح الخصوصية مثل GDPR.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **طريقتان لجمع البيانات**:
  - **JavaScript Beacon**: يجمع snippet JavaScript خفيف الوزن مقاييس من جانب العميل باستخدام Performance API في المتصفح. مثالي لبيانات مراقبة المستخدم الحقيقي (RUM) التفصيلية، مثل أوقات تحميل الصفحة ومقاييس الويب الأساسية.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Edge Analytics**: يجمع البيانات من جانب الخادم من خوادم الحافة التابعة لـ Cloudflare للمواقع التي يتم تمريرها عبر وكيل Cloudflare. لا حاجة لتغييرات في التعليمات البرمجية، وهو يلتقط جميع الطلبات، بما في ذلك تلك الصادرة عن الروبوتات أو المستخدمين الذين قاموا بتعطيل JavaScript.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **المقاييس المقدمة**: يتتبع مشاهدات الصفحة، والزيارات، والصفحات الأولى، والمراجع، والبلدان، وأنواع الأجهزة، ورموز الحالة، ومقاييس الأداء مثل أوقات تحميل الصفحة.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Adaptive Bit Rate (ABR)**: يضبط دقة البيانات تلقائيًا بناءً على حجم البيانات، ونطاق التاريخ، وظروف الشبكة للحصول على أفضل أداء.[](https://developers.cloudflare.com/web-analytics/about/)
- **مجاني الاستخدام**: متاح لأي شخص لديه حساب Cloudflare، حتى دون تغيير DNS أو استخدام وكيل Cloudflare.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **لوحة التحكم والمرشحات**: يقدم لوحة تحكم بديهية لعرض البيانات وتصفيتها حسب اسم المضيف، وعنوان URL، والبلد، ونطاق الوقت. يمكنك التكبير في فترات زمنية محددة أو تجميع البيانات لإجراء تحليل أعمق.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **دعم Single Page Application (SPA)**: يتتبع تغييرات المسار في SPAs تلقائيًا عن طريق تجاوز وظيفة `pushState` في History API (لا يتم دعم الموجهات القائمة على الهاش).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### القيود
- **الاحتفاظ بالبيانات**: يقتصر على 30 يومًا من البيانات التاريخية، مما قد لا يناسب المستخدمين الذين يحتاجون إلى تحليلات طويلة الأجل.[](https://plausible.io/vs-cloudflare-web-analytics)
- **أخذ عينات البيانات**: تستند المقاييس إلى عينة بنسبة 10% من أحداث تحميل الصفحة، مما قد يؤدي إلى عدم دقة مقارنة بأدوات مثل Plausible أو Fathom Analytics.[](https://plausible.io/vs-cloudflare-web-analytics)
- **مخاوف بشأن الدقة**: يمكن أن تتضمن تحليلات جانب الخادم (edge analytics) حركة مرور الروبوتات، مما يضخم الأرقام مقارنة بتحليلات جانب العميل مثل Google Analytics. قد تفوت تحليلات جانب العميل البيانات من المستخدمين الذين قاموا بتعطيل JavaScript أو أدوات منع الإعلانات.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **لا يوجد دعم لمعلمات UTM**: حاليًا، لا يتم تسجيل سلاسل الاستعلام مثل معلمات UTM لتجنب جمع البيانات الحساسة.[](https://developers.cloudflare.com/web-analytics/faq/)
- **قيود التصدير**: لا توجد طريقة مباشرة لتصدير البيانات (مثلًا إلى CSV)، على عكس بعض المنافسين مثل Fathom Analytics.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **تحليلات أساسية**: تفتقر إلى الميزات المتقدمة مثل تتبع التحويلات أو تحليل رحلة المستخدم التفصيلي مقارنة بـ Google Analytics.[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### إعداد Cloudflare Web Analytics
#### المتطلبات الأساسية
- حساب Cloudflare (يمكن إنشاؤه مجانًا على cloudflare.com).
- الوصول إلى كود موقعك (لـ JavaScript beacon) أو إعدادات DNS (لـ edge analytics إذا كنت تستخدم وكيل Cloudflare).

#### خطوات الإعداد
1. **تسجيل الدخول إلى لوحة تحكم Cloudflare**:
   - انتقل إلى [cloudflare.com](https://www.cloudflare.com) وقم بتسجيل الدخول أو إنشاء حساب.
   - من الصفحة الرئيسية للحساب، انتقل إلى **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/web-analytics/get-started/)

2. **إضافة موقع**:
   - انقر فوق **Add a site** في قسم Web Analytics.
   - أدخل اسم المضيف لموقعك (على سبيل المثال، `example.com`) وحدد **Done**.[](https://developers.cloudflare.com/web-analytics/get-started/)

3. **اختر طريقة جمع البيانات**:
   - **JavaScript Beacon (موصى به للمواقع غير التي تمر عبر الوكيل)**:
     - انسخ snippet JavaScript المقدم من قسم **Manage site**.
     - الصقه في HTML لموقعك قبل وسم `</body>` الختامي. تأكد من أن موقعك يحتوي على HTML صالح لكي يعمل snippet.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
     - بالنسبة لتطبيقات الصفحة الواحدة، تأكد من `spa: true` في التكوين لتتبع المسار التلقائي (لا يتم دعم الموجهات القائمة على الهاش).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
     - مثال لتطبيقات Nuxt: استخدم composable `useScriptCloudflareWebAnalytics` أو أضف الرمز المميز إلى تكوين Nuxt الخاص بك للتحميل العام.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
   - **Edge Analytics (للمواقع التي تمر عبر الوكيل)**:
     - قم بتمرير موقعك عبر Cloudflare عن طريق تحديث إعدادات DNS للإشارة إلى خوادم أسماء Cloudflare. يمكن القيام بذلك في دقائق ولا يتطلب أي تغييرات في التعليمات البرمجية.[](https://www.cloudflare.com/en-in/web-analytics/)
     - ستظهر المقاييس في لوحة تحكم Cloudflare تحت **Analytics & Logs**.[](https://developers.cloudflare.com/web-analytics/faq/)
   - **Cloudflare Pages**:
     - لمشاريع Pages، قم بتمكين Web Analytics بنقرة واحدة: من **Workers & Pages**، حدد مشروعك، انتقل إلى **Metrics**، وانقر فوق **Enable** تحت Web Analytics.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4. **التحقق من الإعداد**:
   - قد تستغرق البيانات بضع دقائق حتى تظهر في لوحة التحكم. تحقق من قسم **Web Analytics Sites** لتأكيد إضافة الموقع.[](https://developers.cloudflare.com/web-analytics/get-started/)
   - إذا كنت تستخدم edge analytics، فتأكد من اكتمال نشر DNS (قد يستغرق 24-72 ساعة).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5. **تكوين القواعد (اختياري)**:
   - قم بإعداد قواعد لتتبع مواقع ويب أو مسارات محددة. استخدم الأبعاد لتصنيف المقاييس (مثلًا، حسب اسم المضيف أو عنوان URL).[](https://developers.cloudflare.com/web-analytics/)

#### ملاحظات
- إذا كان موقعك يحتوي على رأس `Cache-Control: public, no-transform`، فلن يتم حقن JavaScript beacon تلقائيًا، وقد لا يعمل Web Analytics. اضبط إعدادات ذاكرة التخزين المؤقت أو أضف snippet يدويًا.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- قد تمنع بعض أدوات منع الإعلانات JavaScript beacon، لكن edge analytics لا تتأثر بهذا لأنها تعتمد على سجلات الخادم.[](https://developers.cloudflare.com/web-analytics/faq/)
- للإعداد اليدوي، يبلغ beacon إلى `cloudflareinsights.com/cdn-cgi/rum`؛ للمواقع التي تمر عبر الوكيل، يستخدم نقطة النهاية `/cdn-cgi/rum` الخاصة بالنطاق.[](https://developers.cloudflare.com/web-analytics/faq/)

### استخدام Cloudflare Web Analytics
1. **الوصول إلى لوحة التحكم**:
   - سجل الدخول إلى لوحة تحكم Cloudflare، حدد حسابك ونطاقك، وانتقل إلى **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
   - اعرض مقاييس مثل مشاهدات الصفحة، والزيارات، والصفحات الأولى، والمراجع، والبلدان، وأنواع الأجهزة، وبيانات الأداء (مثل أوقات تحميل الصفحة، ومقاييس الويب الأساسية).[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2. **تصفية البيانات وتحليلها**:
   - استخدم المرشحات للتركيز على مقاييس محددة (مثلًا، حسب اسم المضيف، أو عنوان URL، أو البلد).
   - قم بالتكبير في نطاقات زمنية للتحقيق في ذروات حركة المرور أو تجميع البيانات حسب مقاييس مثل المراجع أو الصفحات.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - للمستخدمين المتقدمين، استعلم عن البيانات عبر **GraphQL Analytics API** لإنشاء لوحات تحكم مخصصة.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3. **فهم المقاييس الرئيسية**:
   - **مشاهدات الصفحة**: إجمالي المرات التي يتم فيها تحميل صفحة (نوع محتوى HTML مع استجابة HTTP ناجحة).[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
   - **الزيارات**: مشاهدات الصفحة من مرجع مختلف (لا يتطابق مع اسم المضيف) أو روابط مباشرة.[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - **الزوار الفريدون**: يعتمد على عناوين IP، ولكن لا يتم تخزينها لأسباب الخصوصية. قد يكون الرقم أعلى من الأدوات الأخرى بسبب حركة مرور الروبوتات أو عدم وجود إزالة تكرار قائمة على JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
   - **مقاييس الأداء**: تشمل أوقات تحميل الصفحة، والرسم الأول، ومقاييس الويب الأساسية (جانب العميل فقط).[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4. **المقارنة مع الأدوات الأخرى**:
   - على عكس Google Analytics، لا يتتبع Cloudflare رحلات المستخدم أو التحويلات ولكنه يتضمن حركة مرور الروبوتات والتهديدات، مما يمكن أن يضخم الأرقام (20-50% من حركة المرور لمعظم المواقع).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
   - مقارنة بـ Plausible أو Fathom Analytics، فإن بيانات Cloudflare أقل تفصيلاً بسبب أخذ العينات والاحتفاظ المحدود.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
   - قد تظهر edge analytics أرقامًا أعلى من أدوات جانب العميل مثل Google Analytics، التي تستبعد طلبات الروبوتات وطلبات غير JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### أفضل الممارسات
- **اختر الطريقة الصحيحة**: استخدم JavaScript beacon للمقاييس التي تركز على الخصوصية من جانب العميل أو edge analytics لبيانات شاملة من جانب الخادم إذا كان موقعك يمر عبر الوكيل.[](https://www.cloudflare.com/web-analytics/)
- **اجمع مع أدوات أخرى**: زوّد مع Google Analytics أو البدائل التي تركز على الخصوصية مثل Plausible أو Fathom للحصول على رؤى أعمق، حيث أن تحليلات Cloudflare أساسية.[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **راقب الأداء**: استخدم مقاييس الأداء لتحديد الصفحات ذات التحميل البطيء واستفد من توصيات Cloudflare (مثل تحسينات التخزين المؤقت).[](https://developers.cloudflare.com/web-analytics/)
- **تحقق من مشاكل أداة منع الإعلانات**: إذا كنت تستخدم JavaScript beacon، فأبلغ المستخدمين بالسماح بـ `cloudflare.com` أو تعطيل أدوات منع الإعلانات لضمان جمع البيانات.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **راجع البيانات بانتظام**: تحقق من لوحة التحكم بشكل متكرر لاكتشاف الاتجاهات أو الشذوذات، حيث يتم الاحتفاظ بالبيانات لمدة 30 يومًا فقط.[](https://plausible.io/vs-cloudflare-web-analytics)

### استكشاف الأخطاء وإصلاحها
- **لا تظهر أي بيانات**:
  - تحقق من أن snippet JavaScript موضوعة بشكل صحيح وأن الموقع يحتوي على HTML صالح.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - بالنسبة لـ edge analytics، تأكد من أن DNS يشير إلى Cloudflare (قد يستغرق النشر 24-72 ساعة).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - تحقق من رؤوس `Cache-Control: no-transform` التي تمنع حقن beacon التلقائي.[](https://developers.cloudflare.com/web-analytics/get-started/)
- **إحصائيات غير دقيقة**:
  - تتضمن edge analytics حركة مرور الروبوتات، مما يضخم الأرقام. استخدم تحليلات جانب العميل للحصول على أعداد زوار أكثر دقة.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - قد يسبب أخذ عينات البيانات (10%) تناقضات. خذ هذا في الاعتبار عند المقارنة مع أدوات أخرى.[](https://plausible.io/vs-cloudflare-web-analytics)
- **مشاكل أداة منع الإعلانات**: تمنع بعض إضافات المتصفح JavaScript beacon. edge analytics محصنة ضد هذا.[](https://developers.cloudflare.com/web-analytics/faq/)
- **مقاييس SPA مفقودة**: تأكد من تمكين دعم SPA (`spa: true`) وتجنب الموجهات القائمة على الهاش.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### الاستخدام المتقدم
- **GraphQL Analytics API**: للتحليلات المخصصة، استعلم عن واجهة برمجة تطبيقات Cloudflare لإنشاء لوحات تحكم مخصصة أو دمجها مع أنظمة أخرى. يتطلب خبرة تقنية.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers**: أرسل بيانات التحليلات إلى قاعدة بيانات time-series للمعالجة المخصصة أو استخدم Workers للتحليلات serverless المتقدمة.[](https://developers.cloudflare.com/analytics/)
- **رؤى الأمان**: اجمع مع Security Analytics التابع لـ Cloudflare لمراقبة التهديدات والروبوتات إلى جانب بيانات الزوار.[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### المقارنة مع البدائل
- **Google Analytics**: يقدم تتبعًا تفصيليًا لرحلة المستخدم والتحويلات ولكنه يعتمد على ملفات تعريف الارتباط وJavaScript، والتي قد يتم حظرها. Cloudflare أبسط ويركز على الخصوصية ولكنه أقل ثراءً بالميزات.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics**: مفتوح المصدر، يركز على الخصوصية، مع احتفاظ غير محدود بالبيانات وبدون أخذ عينات. أكثر دقة للزوار الفريدين ولكنه يتطلب خطة مدفوعة.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics**: مشابه لـ Plausible، مع بيانات قابلة للتصدير وميزات متقدمة مثل تتبع الحملات. العرض المجاني لـ Cloudflare أقل قوة ولكنه أسهل في الإعداد للاحتياجات الأساسية.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats**: مخصص لـ WordPress، مع احتفاظ محدود بالبيانات (28 يومًا) وبدون تتبع على مستوى المستخدم. تركيز مماثل على الخصوصية ولكنه أقل مرونة من Cloudflare.[](https://wordpress.com/support/stats/)

### موارد إضافية
- **التوثيق الرسمي**: [Cloudflare Web Analytics Docs](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **دليل الإعداد**: [Enabling Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **الأسئلة الشائعة**: [Cloudflare Web Analytics FAQs](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **مقالة المدونة**: [Cloudflare’s Privacy-First Web Analytics](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **دعم المجتمع**: تحقق من منتديات مجتمع Cloudflare للحصول على مساعدة إضافية.[](https://developers.cloudflare.com/web-analytics/faq/)

### خاتمة
يعد Cloudflare Web Analytics خيارًا ممتازًا لمالكي مواقع الويب الذين يبحثون عن أداة تحليلات مجانية تركز على الخصوصية مع الحد الأدنى من الإعداد. إنه مثالي لمراقبة حركة المرور والأداء الأساسية ولكن قد يكون غير كافٍ للاحتياجات المتقدمة بسبب أخذ عينات البيانات، والاحتفاظ المحدود، ونقص الميزات مثل تتبع التحويلات. للحصول على رؤى أعمق، فكر في دمجه مع أدوات مثل Plausible أو Fathom Analytics. تحقق دائمًا من دقة الإعداد وكن على علم بالقيود عند تفسير البيانات.

إذا كنت بحاجة إلى مساعدة محددة بشأن الإعداد أو لديك أسئلة حول دمج Cloudflare Web Analytics مع موقعك، فأخبرني!