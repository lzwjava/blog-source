---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تعطيل الاستشهادات من البحث على الويب في LibreChat
translated: true
type: note
---

## تعطيل الاستشهادات في وضع البحث على الويب في LibreChat

ميزة البحث على الويب في LibreChat (المدعومة من مزودين مثل Serper.dev أو SearxNG، جنبًا إلى جنب مع أدوات استخراج البيانات مثل Firecrawl) تتضمن تلقائيًا استشهادات في الردود لتكريم المصادر وتحسين الشفافية. استنادًا إلى الوثائق الرسمية والمناقشات المجتمعية، لا يوجد مفتاح تبديل مدمج موجه للمستخدم يعطل بشكل محدد استشهادات البحث على الويب على مستوى المستخدم الفردي. ومع ذلك، يمكنك تحقيق ذلك أو تقريبه من خلال تغييرات التكوين، بشكل أساسي للمسؤولين أو المضيفين الذاتيين. إليك الطريقة:

### 1. **تكوين مستوى المسؤول (الطريقة الموصى بها)**
   إذا كنت تشغل نسختك الخاصة من LibreChat (مضيف ذاتيًا)، قم بتعديل ملفات التكوين للحد من عرض الاستشهادات أو إزالته. يتم التعامل مع الاستشهادات عبر واجهة المستخدم ومكونات البحث.

   - **تحرير `librechat.yaml` لإعدادات الواجهة**:
     يستخدم LibreChat ملف YAML للإعدادات العامة. ابحث عن قسم `interface`، الذي يتحكم في رؤية الاستشهادات (مستوحى من عناصر التحكم في استشهادات الملفات، والتي قد تمتد إلى عرض البحث على الويب).
     - عيّن `fileCitations` إلى `false` لتعطيل أذونات الاستشهاد عالميًا. بينما يكون هذا مخصصًا بشكل صريح لعمليات البحث في الملفات، إلا أنه يمكن أن يؤثر على عرض واجهة مستخدم البحث على الويب في بعض الإعدادات.
       ```yaml
       interface:
         fileCitations: false  # يعطل عرض الاستشهادات للعمليات البحث بشكل عام
       ```
     - للبحث على الويب بشكل محدد، ضمن قسم `webSearch`، يمكنك تعطيل أو تخصيص المزودين لتجنب ربط المصادر التفصيلي:
       ```yaml
       webSearch:
         enabled: true  # حافظ على التمكين، ولكن اضبط المزودين
         serper:  # أو مزودك
           enabled: true
           # لا يوجد علم 'citations' مباشر، ولكن حذف مفاتيح API لأدوات الاستخراج مثل Firecrawl يقلل من الاستشهادات/المقتطفات التفصيلية
         firecrawl:
           enabled: false  # يعطل استخراج المحتوى، الذي غالبًا ما يولد استشهادات
       ```
     - أعد تشغيل نسخة LibreChat الخاصة بك بعد التغييرات. مصدر تكوين الواجهة: [LibreChat Interface Object Structure](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1].

   - **متغيرات البيئة (ملف `.env`)**:
     في ملف `.env` الخاص بك، عطل وضع التصحيح أو التسجيل الذي قد يفرض الاستشهادات، أو عيّن البحث على الويب لاستخدام مزود أساسي.
     - مثال:
       ```
       DEBUG_PLUGINS=false  # يقلل الناتج المفصل، بما في ذلك الاستشهادات
       SERPER_API_KEY=your_key  # استخدم مزود بحث أساسي بدون استخراج للحصول على استشهادات أقل
       FIRECRAWL_API_KEY=  # اتركه فارغًا لتعطيل أداة الاستخراج (لا توجد مقتطفات صفحات/استشهادات)
       ```
     - هذا يحول الردود إلى نتائج بحث موجزة فقط بدون استشهادات مضمنة. الإعداد الكامل: [LibreChat .env Configuration](https://www.librechat.ai/docs/configuration/dotenv)[2].

   - **تخصيص مزود البحث على الويب**:
     انتقل إلى مزود مثل SearxNG، والذي يمكن تكوينه من جانب الخادم لحذف روابط المصادر.
     - عيّن `SEARXNG_INSTANCE_URL=your_minimal_searxng_url` في `.env`.
     - في نسخة SearxNG الخاصة بك، قم بتحرير إعداداتها لقمع البيانات الوصفية للنتائج (على سبيل المثال، عبر `settings.yml` في SearxNG: عطل `reveal_version: false` وخصص القوالب لإزالة الروابط).
     - الوثائق: [Web Search Configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3].

### 2. **الحلول البديلة على مستوى المستخدم (بدون صلاحيات مسؤول)**
   إذا كنت تستخدم LibreChat مستضاف (مثل نسخة عامة)، فإن الخيارات محدودة حيث يتم غالبًا فرض الاستشهادات لضمان الدقة:
   - **هندسة الأوامر (Prompt Engineering)**: أعط تعليمات صريحة للذكاء الاصطناعي في رسائلك، على سبيل المثال، "ابحث على الويب ولكن لا تدرج استشهادات أو مصادر في ردك." هذا يعمل بشكل غير متسق لأن أداة البحث قد تظل تضيفها، ولكن العديد من النماذج ستستجيب جزئيًا.
   - **تعطيل البحث على الويب بالكامل**: إذا كانت الاستشهادات هي المشكلة الرئيسية، قم بإيقاف تشغيل البحث على الويب لكل محادثة:
     - في واجهة الدردشة، تجنب النقر على زر "Web Search".
     - للوكلاء (Agents): عند إنشاء/تحرير الوكيل، قم بإزالة القدرة `web_search` من تكوين الوكيل (عبر واجهة مستخدم الوكلاء). المصدر: [Agents Documentation](https://www.librechat.ai/docs/features/agents)[4].
     - اطلب من المسؤولين إضافة مفتاح تبديل؛ تشير المناقشات المجتمعية إلى أن هذا مطلوب كاقتراح ميزة (على سبيل المثال، [GitHub Discussion on Web Search Toggle](https://github.com/danny-avila/LibreChat/discussions/7738)[5]).

### 3. **القيود والملاحظات**
   - تمثل الاستشهادات جزءًا أساسيًا من البحث على الويب لضمان الاستخدام الأخلاقي للذكاء الاصطناعي وإمكانية التتبع، لذا فإن تعطيلها بالكامل قد يتطلب تعديلات تعليمات برمجية مخصصة (على سبيل المثال، تحرير مكونات الواجهة الأمامية مثل `WebSearchResults.jsx` في مستودع GitHub لإخفاء عناصر الاستشهاد).
   - لا يوجد علم مباشر "لإيقاف تشغيل الاستشهادات" في الإصدارات الحالية (اعتبارًا من أكتوبر 2025). تحقق من التحديثات في [Web Search Feature Docs](https://www.librechat.ai/docs/features/web_search)[6]، حيث تتطور الميزات.
   - إذا كنت تستخدم الاستضافة الذاتية، اختبر التغييرات في بيئة تطوير — قد يؤدي تعطيل أدوات الاستخراج إلى تقليل جودة الاستجابة.
   - تلاحظ الملاحظات المجتمعية (مثل Reddit) وجود أخطاء عرضية في ميزات البحث، ولكن لا شيء محدد للاستشهادات: [Reddit Thread on LibreChat Issues](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7].

للحصول على الدعم الرسمي، انضم إلى Discord الخاص بـ LibreChat أو افتح مشكلة على GitHub مع تفاصيل إعدادك. إذا لم يحل هذا المشكلة، قدم المزيد من السياق حول إصدار LibreChat الخاص بك أو طريقة الاستضافة!

الاستشهادات:
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/