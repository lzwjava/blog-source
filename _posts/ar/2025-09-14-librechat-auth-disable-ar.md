---
audio: false
date: 2025-09-14
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: تعطيل طرق التحايل على مصادقة LibreChat
translated: true
type: note
---

إجابة مختصرة: لا يمكنك إيقاف المصادقة تمامًا في LibreChat، لكن يمكنك إيقاف مشكلة "الاستمرار في طلب تسجيل الدخول" وجعلها تشعر بأنها قريبة من "عدم الحاجة لتسجيل الدخول". إليك ما ينجح فعليًا (والسبب):

### 1) لا يمكنك تعطيل المصادقة بالكامل

هذا مؤكد من قبل المُصدر: يمكن تعطيل التسجيل، لكن نظام المصادقة نفسه لا يمكن إيقافه. ([GitHub][1])

### 2) لماذا تستمر في الخروج تلقائيًا

إذا وصلت إلى نسختك عبر **HTTP** (على سبيل المثال، عنوان IP للشبكة المحلية)، يتم وضع علامة `secure` على ملفات تعريف الارتباط في بيئة الإنتاج لذا لن يحتفظ المتصفح بها؛ مما يؤدي إلى إعادتك إلى شاشة تسجيل الدخول. استخدم **HTTPS** (حتى لو كان ذاتي التوقيع) أو شغّل الـ API في وضع المطور الذي يعطل ملفات تعريف الارتباط الآمنة. ([GitHub][1])

### 3) حلان موثوقان

#### الخيار أ — صحيح/آمن (موصى به)

* ضع LibreChat خلف HTTPS (مثل nginx/caddy/traefik؛ التوقيع الذاتي مقبول على الشبكة المحلية).
* ثم زد من مهلات الجلسة في ملف `.env` الخاص بك:

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24 ساعة
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30 يومًا
  ```
* أعد تشغيل الحاويات بعد تغيير ملف البيئة.
  هذا يبقيك مسجل الدخول لأيام/أسابيع ويصلح مشكلة فقدان ملفات تعريف الارتباط. ([GitHub][2])

#### الخيار ب — "أنا على شبكة محلية خاصة وأريد فقط أن يتوقف تسجيل الخروج"

* أنشئ ملف `docker-compose.override.yml` وشغّل الـ API في وضع المطور (يعطل ملفات تعريف الارتباط الآمنة):

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* نفذ `docker compose up -d` للتطبيق.
  هذا أقل أمانًا (ملفات تعريف الارتباط ليست `secure`)، لكنه يوقف إعادة تسجيل الدخول الإجباري عبر HTTP العادي. ([librechat.ai][3])

### 4) تعديلات تحسين تجربة المستخدم الاختيارية

* **عطّل عمليات التسجيل الجديدة** لتصبح فعليًا للمستخدم الفردي:

  ```
  ALLOW_REGISTRATION=false
  ```

  (لا يزال بإمكانك إضافة مستخدمين عبر `npm run create-user` إذا لزم الأمر.) ([librechat.ai][4])
* حافظ على مفاتيح تبديل المصادقة الأخرى في `.env` (علامات البريد الإلكتروني/تسجيل الدخول الاجتماعي) إذا كنت تريد أبسط مسار لتسجيل الدخول. ([librechat.ai][5])

### 5) قائمة مراجعة سريعة لحالتك (الإصدار v0.8.0-rc3)

1. قرر: وكيل HTTPS (الأفضل) **أو** وضع المطور (حل سريع للشبكة المحلية).
2. عيّن قيم أطول لـ `SESSION_EXPIRY` و `REFRESH_TOKEN_EXPIRY` في `.env`.
3. أعد تشغيل مجموعة الحاويات حتى يتم تطبيق تغييرات البيئة.
4. (اختياري) أوقف التسجيل للحصول على إحساس "للمستخدم الفردي".

إذا أردت، الصق محتويات `docker-compose.yml` و `.env` الحاليين (بدون الأسرار). سأحدد بالضبط ما يجب إضافته/تغييره لإعدادك.

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"