---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: خيارات تطوير مجانية لـ آي بي إم ويب سبير
translated: true
type: note
---

### إصدارات IBM WebSphere Application Server (WAS) المجانية أو المجتمعية

خادم تطبيقات IBM WebSphere (WAS) التقليدي الكامل الميزات لا يقدم إصدارًا مجانيًا دائمًا أو إصدارًا مجتمعيًا للاستخدام في بيئة الإنتاج اعتبارًا من أكتوبر 2025. إن الإصدار المجتمعي التاريخي لـ WebSphere Application Server (WASCE)، والذي كان خادمًا مجانيًا متوافقًا مع Java EE 6، قد توقف حوالي عام 2012 ولم يعد مدعومًا أو متاحًا من IBM.

ومع ذلك، تقدم IBM **خيارات مجانية للتطوير والاختبار**:
- **أدوات مطوري WebSphere Application Server**: مجموعة خفيفة الوزومجانية من الأدوات القائمة على Eclipse لتطوير وتجميع ونشر تطبيقات Java EE وOSGi وتطبيقات الويب. يمكن تنزيل هذه الأدوات مباشرة من IBM ودمجها مع بيئات التطوير المتكاملة مثل Eclipse.
- **وقت التشغيل المجاني للمطورين**: تقدم IBM إصدارًا مجانيًا من وقت تشغيل WAS مخصصًا للمطورين لاختبار التطبيقات (مثل WebSphere 9). هذا الإصدار متاح للتنزيل عبر موارد المطورين من IBM وهو مناسب للبيئات غير الإنتاجية مثل التطوير المحلي أو البحث والتطوير الداخلي.

لباقات النشر في بيئة الإنتاج، يتطلب WAS التقليدي ترخيصًا مدفوعًا، على الرغم من أن IBM تقدم نسخة تجريبية لمدة 60 يومًا للتقييم.

### بديل: WebSphere Liberty
إذا كنت منفتحًا على بديل حديث وخفيف الوزن ضمن عائلة WebSphere، فإن **WebSphere Liberty** موصى به بشدة من قبل IBM لمع حالات الاستخدام:
- **Liberty Core**: هذا الإصدار مجاني لكل من التطوير والاستخدام في الإنتاج (بدون دعم من IBM). وهو يدعم مجموعة فرعية من ميزات Jakarta EE وهو مثالي للتطبيقات الصغيرة (microservices) والتطبيقات السحابية الأصلية والأحمال العملية الأبسط.
- تتطلب إصدارات Liberty الكاملة (ذات الميزات المتقدمة مثل التجميع أو الأمان المميز) الترخيص للاستخدام في الإنتاج، لكن الإصدار الأساسي يظل مجانيًا.
- ينشأ Liberty من مشروع **Open Liberty** مفتوح المصدر، والذي هو مجاني تمامًا ويقوده المجتمع.

يمكنك تنزيل Liberty للمطورين من موقع IBM دون قيود للاختبار غير التجاري.

لأحدث التنزيلات وتفاصيل الترخيص، قم بزيارة الصفحات الرسمية لـ IBM أو Passport Advantage (يتطلب ذلك معرف IBM).

**المراجع**:
- [إصدارات أدوات مطوري WebSphere Application Server وأدوات Liberty](https://www.ibm.com/support/pages/websphere-application-server-developer-tools-and-liberty-developer-tools-releases)
- [تثبيت WebSphere 9 للمطورين](https://www.genuitec.com/docs/servers/installing-websphere-9-developers/)
- [WebSphere Liberty للمطورين](https://www.ibm.com/support/pages/websphere-liberty-developers)
- [الإصدار المجتمعي لـ IBM WebSphere Application Server (ويكيبيديا)](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server_Community_Edition)
- [استكشاف IBM WebSphere Application Server](https://www.jrebel.com/blog/exploring-ibm-websphere-application-server)
- [Open Liberty](https://openliberty.io/)