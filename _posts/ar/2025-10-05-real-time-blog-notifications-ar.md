---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إشعارات تيليغرام الفورية لزيارات المدونة
translated: true
type: note
---

نعم، يمكنك إعداد نظام لتحليل سجلات Cloudflare أو حركة المرور في الوقت شبه الفعلي وإرسال إشعارات Telegram لكل زيارة للمدونة، لكنه ليس مباشرًا مع سجلات التحليلات القياسية وحدها. تحليلات Cloudflare غالبًا ما تكون مجمعة (مثل الملخصات اليومية/الأسبوعية)، وحتى ميزة Logpush (التي تصدر السجلات) تعمل على تجميع البيانات كل 1-5 دقائق، مما يجعلها غير مناسبة للتنبيهات الفورية لكل زيارة. تقدم Instant Logs بثًا فوريًا لكنه يتطلب خطة Business أو Enterprise ويحتاج إلى معالجة مخصصة (عبر WebSocket ونص برمجي) لتفعيل رسائل Telegram — وهذا مبالغ فيه لمعظم المستخدمين.

النهج الأكثر عملية وفورية هو استخدام **Cloudflare Workers** لاعتراض كل طلب وارد إلى مدونتك. هذا يشغل تعليمات برمجية بدون خادم على كل زيارة، مما يسمح لك بتسجيل الحدث وإرسال رسالة Telegram فورًا عبر واجهة برمجة التطبيقات الخاصة بهم. إنه مجاني لحركة المرور المنخفضة (حتى 100 ألف طلب/يوم)، لكن المدونات عالية الحركة قد تصل إلى الحدود أو تتكبد تكاليف — بالإضافة إلى ذلك، ستتلقى رسائل مزعجة بالإشعارات، لذا فكر في التصفية (مثل فقط لعناوين IP فريدة أو صفحات محددة).

### خطوات الإعداد السريع
1. **إنشاء بوت Telegram**:
   - راسل @BotFather على Telegram، استخدم `/newbot` لإنشاء بوت، ولاحظ رمز البوت (مثل `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
   - ابدأ محادثة مع البوت الخاص بك، ثم راسل @userinfobot للحصول على معرف المحادثة الخاص بك (مثل `123456789`).
   - اختبر إرسال رسالة عبر curl:  
     ```
     curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<YOUR_CHAT_ID>","text":"Test visit!"}'
     ```

2. **إنشاء Cloudflare Worker**:
   - سجل الدخول إلى لوحة تحكم Cloudflare > Workers & Pages > Create application > Create Worker.
   - سمّه (مثل `blog-visit-notifier`) ونشر القالب الافتراضي.

3. **أضف كود الإشعار**:
   - حرر كود الـ worker لاعتراض الطلبات والإرسال إلى Telegram. إليك مثال أساسي (استبدل العناصر النائبة):
     ```javascript
     export default {
       async fetch(request, env) {
         // اختياري: سجل أو صفِّر الزيارة (مثل: فقط للصفحة الرئيسية لمدونتك)
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // اضبط المسار حسب الحاجة
           return fetch(request);  // تخطى الصفحات غير المدونة
         }

         // أرسل رسالة Telegram (غير متزامن لتجنب الإعاقة)
         const message = `New visit to ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, User-Agent: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // للتنسيق إذا لزم الأمر
           })
         }).catch(err => console.error('Telegram send failed:', err));

         // انقل الطلب الأصلي إلى مدونتك
         return fetch(request);
       }
     };
     ```
     - هذا يعمل على كل طلب مطابق، يسجل معلومات الزائر الأساسية، ويرسلها عبر Telegram دون تأخير تحميل الصفحة.

4. **تكوين متغيرات البيئة**:
   - في إعدادات الـ worker > Variables > Add:  
     - `TELEGRAM_BOT_TOKEN`: رمز البوت الخاص بك.  
     - `TELEGRAM_CHAT_ID`: معرف المحادثة الخاص بك.  
   - احفظ وأعد النشر.

5. **توجيه الـ Worker إلى مدونتك**:
   - في إعدادات Workers > Triggers > Add route.  
   - عيّنه لنطاق/مسار مدونتك (مثل `yourblog.com/*`).  
   - هذا يضمن أن الـ worker يعمل على كل زيارة قبل الوصول إلى خادمك الأصلي.

6. **اختبر وراقب**:
   - قم بزيارة مدونتك — يجب أن تتلقى إشعار Telegram فورًا.  
   - تحقق من سجلات الـ worker في لوحة التحكم للبحث عن أخطاء. إذا وصلت إلى حدود المعدل (مثل 30 رسالة/ثانية في Telegram)، أضف تخفيفًا مع تخزين KV.

### بدائل إذا لم تكن Workers مناسبة
- **لتحليل السجلات المجمعة**: استخدم Logpush لتصدير سجلات طلبات HTTP إلى خدمة مثل AWS S3 أو Google Pub/Sub، ثم انقلها إلى أداة مثل Zapier أو n8n للحصول على تنبيهات Telegram (مثل تلخيص الزيارات كل ساعة). لكنها ليست فورية.
- **التكاملات**: يمكن لأدوات مثل Albato أو n8n ربط webhooks من Cloudflare بـ Telegram لأحداث أوسع، لكن ليس لكل زيارة.
- **القيود**: لدى Workers المجانية 10 مللي ثانية من وقت المعالج لكل طلب — هذا جيد لهذا الغرض، لكن قم بالترقية إذا لزم الأمر. تجنب استخدامها على المواقع عالية الحركة بدون تخفيف.

هذا الإعداد يحول حركة مرور Cloudflare الخاصة بك إلى تنبيهات قابلة للتنفيذ وفورية. إذا كنت بحاجة إلى تعديلات في الكود أو مساعدة في الأخطاء، شارك المزيد من التفاصيل!

[Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)  
[Telegram Bot API](https://core.telegram.org/bots/api)  
[Cloudflare Instant Logs](https://developers.cloudflare.com/logs/instant-logs/)