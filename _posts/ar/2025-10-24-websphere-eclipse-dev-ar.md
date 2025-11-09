---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تطوير WebSphere باستخدام Eclipse
translated: true
type: note
---

### التطوير باستخدام IBM WebSphere Application Server (WAS) في Eclipse

IBM WebSphere Application Server (WAS) هو خادم تطبيقات Java EE، ويمثل Eclipse بيئة تطوير متكاملة (IDE) ممتازة لتطوير وتجميع ونشر التطبيقات عليه. الأداة الأساسية لهذا التكامل هي **أداة مطوري IBM WebSphere Application Server لـ Eclipse** (يُشار إليها غالبًا بالاختصار WDT). هذه الإضافة (plugin) توفر إدارة الخادم، وإنشاء المشاريع، والنشر، وإمكانيات التصحيح (debugging) مباشرة داخل Eclipse. وهي تدعم كلًا من WAS التقليدي (مثل الإصدارات 8.5 و 9.x) والملف الشخصي الخفيف Liberty.

#### الإضافة المطلوبة
- **IBM WebSphere Application Server Developer Tools for Eclipse**: هذه هي الإضافة الأساسية. اختر الإصدار الذي يتوافق مع بيئة تشغيل WAS الخاصة بك (مثل أدوات الإصدار 8.5x أو 9.x). وهي متاحة مجانًا على سوق Eclipse (Eclipse Marketplace) وتدعم إصدارات Eclipse الحديثة مثل 2024-06 أو 2025-03.

لا توجد إضافات أخرى مطلوبة بشكل صارم، ولكن للتطوير الكامل باستخدام Java EE، تأكد من أن تثبيت Eclipse الخاص بك يتضمن منصة أدوات الويب (Web Tools Platform - WTP)، والتي تكون قياسية في حزمة Eclipse IDE for Java EE Developers.

#### المتطلبات الأساسية
- Eclipse IDE for Java EE Developers (يُوصى بالإصدار 2023-09 أو أحدث للتأكد من التوافق).
- بيئة تشغيل IBM WAS مثبتة محليًا (التقليدية أو Liberty) للاختبار والنشر.
- اتصال بالإنترنت للتثبيت من السوق (أو قم بتنزيل الملفات للعمل دون اتصال).

#### خطوات التثبيت
يمكنك تثبيت WDT عبر سوق Eclipse (أسهل طريقة)، أو موقع التحديث (update site)، أو الملفات التي تم تنزيلها. أعد تشغيل Eclipse بعد التثبيت.

1. **عبر سوق Eclipse** (مُوصى به):
   - افتح Eclipse وانتقل إلى **Help > Eclipse Marketplace**.
   - ابحث عن "IBM WebSphere Application Server Developer Tools".
   - اختر الإصدار المناسب (مثل أدوات الإصدار 9.x أو 8.5x).
   - انقر على **Install** واتبع التعليمات. اقبل التراخيص وأعد تشغيل Eclipse عند الانتهاء.

2. **عبر موقع التحديث**:
   - انتقل إلى **Help > Install New Software**.
   - انقر على **Add** وأدخل عنوان URL لموقع التحديث (مثال: `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` للإصدارات الحديثة — تحقق من وثائق IBM للحصول على الأحدث).
   - حدد ميزات WDT (مثل WebSphere Application Server V9.x Developer Tools) وقم بالتثبيت.

3. **من الملفات التي تم تنزيلها** (خيار العمل دون اتصال):
   - قم بتنزيل أرشيف ZIP من [موقع مطوري IBM](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) (مثال: `wdt-update-site_<version>.zip`).
   - استخرجه إلى مجلد محلي.
   - في Eclipse، انتقل إلى **Help > Install New Software > Add > Archive** وحدد الملف `site.xml` للموقع المستخرج.
   - حدد الميزات المطلوبة وقم بتثبيتها، ثم أعد التشغيل.

بعد التثبيت، تحقق من ذلك بالانتقال إلى **Window > Show View > Servers** — يجب أن يظهر WAS كخيار لنوع الخادم.

#### الخطوات الأساسية لتطوير ونشر تطبيقات WAS
بمجرد التثبيت، يمكنك إنشاء وبناء وتشغيل تطبيقات Java EE الموجهة لـ WAS.

1. **إنشاء مشروع جديد**:
   - انتقل إلى **File > New > Project**.
   - اختر **Web > Dynamic Web Project** (لتطبيقات الويب) أو **Java EE > Enterprise Application Project** (لتطبيقات EAR الكاملة).
   - في معالج المشروع، عيّن بيئة التشغيل المستهدفة إلى تثبيت WAS المحلي الخاص بك (إذا لم يكن مدرجًا، أضفه عبر **Window > Preferences > Server > Runtime Environments > Add > WebSphere**).
   - قم بتكوين الجوانب (facets) لإصدار Java EE (مثل 7 أو 8) بما يتطابق مع إصدار WAS الخاص بك.

2. **إعداد الخادم**:
   - افتح نافذة **Servers** (**Window > Show View > Servers**).
   - انقر بزر الماوس الأيمن داخل النافذة واختر **New > Server**.
   - اختر **WebSphere Application Server** (التقليدي أو Liberty) واشير إلى دليل التثبيت المحلي لـ WAS.
   - انهي الإعداد وابدأ تشغيل الخادم (انقر بزر الماوس الأيمن > Start).

3. **طور تطبيقك**:
   - أضف فئات جافا، وJSPs، وServlets، وEJBs، إلخ، في مشروعك.
   - استخدم محرري Eclipse لملفات التكوين XML (مثل web.xml، ibm-web-bnd.xml للربط الخاص بـ WAS).
   - ابنِ المشروع (**Project > Build Project**).

4. **انشر وشغّل**:
   - انقر بزر الماوس الأيمن على مشروعك > **Run As > Run on Server** (حدد خادم WAS الخاص بك).
   - ينشر Eclipse التطبيق (النشر التلقائي لوضع التطوير) ويبدأ تشغيل الخادم.
   - قم بالتصحيح (Debug) عن طريق تعيين نقاط التوقف (breakpoints) والتشغيل في وضع التصحيح (Debug mode).
   - للنشر السريع (hot deployment) (تحديثات سريعة دون إعادة تشغيل)، فعّل خيار "Publish server changes immediately" في تكوين الخادم.

5. **نصائح متقدمة**:
   - استخدم الملف الشخصي Liberty للاختبار المحلي الأسرع — فهو مدرج في WDT ويحاكي سلوك WAS التقليدي.
   - لـ OSGi أو الخدمات المصغرة (microservices)، أنشئ مشاريع حزمة OSGi (OSGi Bundle Projects) عبر الإضافة.
   - راقب السجلات (logs) في نافذة **Console** أثناء وقت التشغيل.

إذا واجهت مشاكل (مثل أخطاء التوافق)، تحقق من صفحة المشاكل المعروفة لدى IBM أو تأكد من توافق إصدارات Eclipse و WAS الخاصة بك.

#### المراجع
- [نظرة عامة على أدوات مطوري IBM WebSphere Application Server](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [سوق Eclipse: أدوات الإصدار 9.x](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [سوق Eclipse: أدوات الإصدار 8.5x](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [دليل التثبيت من وثائق IBM](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)