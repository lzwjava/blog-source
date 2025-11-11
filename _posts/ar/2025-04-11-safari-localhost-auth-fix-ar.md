---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: إصلاح المصادقة المحلية في سفاري
translated: true
type: note
---

تحدث هذه المشكلة لأن سفاري على نظام macOS يفرض سياسات أمان أكثر صرامة من كروم لعناوين URL المحلية (localhost). على وجه التحديد، يتطلب سفاري سياق HTTPS آمنًا للسماح بملفات تعريف الارتباط المستمرة وجلسات المصادقة، مما يمنع حدوث حلقات تسجيل خروج غير مرغوب فيها أو إعادة المصادقة في كل زيارة لتطبيقات مثل LibreChat التي تعمل عبر HTTP. بينما يكون كروم أكثر تساهلاً مع HTTP على localhost، ولهذا تستمر المصادقة فيه ولكن ليس في سفاري.[1][2][3]

### العوامل الحكومية
- **سياسات المتصفح**: المتصفحات الحديثة مثل سفاري تريد HTTPS لـ localhost لتجنب تحذيرات المحتوى المختلط وثغرات أمان الجلسات.
- **سلوك LibreChat**: يستخدم LibreChat ملفات تعريف ارتباط آمنة أو رموزًا قائمة على localStorage للمصادقة، والتي تنكسر على HTTP في سفاري بسبب تعامله الأكثر صرامة مع الأصول غير الآمنة.

### الحلول (مرتبة حسب السهولة والفعالية)
1. **إعداد HTTPS لـ Localhost (موصى به)**:
   - توثيق LibreChat نفسه والمدونة الخاصة به يوصيان بذلك لمنع تسجيلات الخروج الناتجة عن HTTP.[1]
   - استخدم أداة `mkcert` (مجانية) لتوليد شهادات SSL محلية والوثوق بها لـ localhost:
     - قم بتثبيت `mkcert` عبر `brew install mkcert` أو قم بتنزيله من GitHub.
     - شغّل `mkcert -install` لتثبيت شهادة الجذر (root CA).
     - أنشئ الشهادات: `mkcert localhost 127.0.0.1`.
     - قم بتكوين LibreChat (على سبيل المثال، عبر متغيرات بيئة Docker أو الإعدادات) لاستخدام هذه الشهادات: أضف `HTTPS=true`، `SSL_CRT_FILE=/path/to/localhost.pem`، و `SSL_KEY_FILE=/path/to/localhost-key.pem` في ملف `.env` الخاص بك أو في البيئة.
     - أعد تشغيل LibreChat وادخل عبر `https://localhost:3080`.
     - سيعامل سفاري الآن الموقع على أنه آمن، مما يسمح بتسجيلات الدخول السلسة.

2. **بديل: استخدام 127.0.0.1 بدلاً من localhost**:
   - أحيانًا يتصرف سفاري بشكل مختلف مع `localhost` (بسبب IPv6 أو حل DNS). جرب الدخول عبر `http://127.0.0.1:3080` – هذا قد حل مشاكل اتصال مماثلة في بعض الحالات، على الرغم من أنه قد لا يصلح مشكلة استمرارية المصادقة بالكامل.[4][4][5]

3. **مسح بيانات موقع localhost من سفاري**:
   - اذهب إلى Safari > Preferences > Privacy > Manage Website Data > ابحث عن "localhost" > قم بإزالة أي إدخالات.
   - هذا يجبر سفاري على التوقف عن فرض ترقيات HTTPS أو سياقات غير آمنة مخزنة.[3][2]
   - أعد تشغيل سفاري واختبر؛ إذا كان LibreChat يدعم ذلك، فيجب أن تثبت المصادقة.

إذا لم ينجح أي من هذه الحلول، فتحقق من سجلات LibreChat للبحث عن أخطاء المصادقة، وتأكد من أن ملف `.env` الخاص بك لا يحتوي على إشارات متضاربة (مثل `ALLOW_ANONYMOUS=true` الذي يعطل المصادقة تمامًا إذا رغبت في ذلك)، وتأكد من أنك لا تستخدم وضع التصفح الخاص في سفاري، والذي يمنع التخزين المستمر.[6][7] إذا استمرت المشكلة، قدم إصدار LibreChat الخاص بك وتكوين ملف .env لاستكشاف الأخطاء وإصلاحها بشكل أعمق.

المراجع:
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354