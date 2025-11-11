---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: تكوين مهلات ومواصلة اتصال Liberty HTTP
translated: true
type: note
---

### تكوين إعدادات Keep-Alive

يعالج WebSphere Liberty Profile اتصالات HTTP keep-alive من خلال عنصر `<httpEndpoint>` في ملف `server.xml`. يتحكم هذا العنصر في الاتصالات المستمرة لتقليل زمن الوصل والحمل.

- **keepAlive**: يُفعِّل أو يعطِّل خاصية keep-alive. اضبطه على `true` (القيمة الافتراضية) للسماح بطلبات متعددة عبر اتصال واحد.
- **keepAliveTimeout**: يحدد المدة (بالثواني) التي ينتظرها الخادم قبل إغلاق اتصال keep-alive الخامل. القيمة الافتراضية هي 30 ثانية.

للتكوين، أضف أو عدِّل عنصر `<httpEndpoint>` تحت جذر `<server>` في `server.xml`. مثال:

```xml
<server>
    <!-- تكوينات أخرى -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        keepAlive="true"
        keepAliveTimeout="60"/>
</server>
```

أعد تشغيل الخادم لتفعيل التغييرات. يمكن ضبط إعدادات keep-alive على مستوى TCP عبر `<tcpOptions>` إذا لزم الأمر، لكن إعداد HTTP keep-alive هو الأكثر شيوعًا لحركة مرور الويب.

### تكوين إعدادات المهلة

ترتبط مهلات الوقت في `server.xml` الخاص بـ Liberty بشكل أساسي بمهلات الاتصال تحت `<httpEndpoint>`، والتي تتحكم في المدة التي ينتظرها الخادم لانتهاء العمليات. تنطبق هذه على اتصالات HTTP.

- **connectionTimeout**: أقصى مدة (بالثواني) لإنشاء اتصال جديد. القيمة الافتراضية هي 60 ثانية.
- **readTimeout**: أقصى مدة (بالثواني) للانتظار لاستقبال البيانات أثناء الطلب. القيمة الافتراضية هي 60 ثانية.
- **writeTimeout**: أقصى مدة (بالثواني) للانتظار لإرسال البيانات الصادرة. القيمة الافتراضية هي 60 ثانية.

يتم تكوين المهلات الخاصة بالجلسة (على سبيل المثال، لجلسات تطبيقات الويب) في `web.xml` أو عبر `<sessionManager>` في `server.xml`، وليس مباشرة في `<httpEndpoint>`.

مثال على تكوين `server.xml`:

```xml
<server>
    <!-- تكوينات أخرى -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        connectionTimeout="30"
        readTimeout="120"
        writeTimeout="120"/>
</server>
```

اضبط القيم بناءً على متطلبات تطبيقك، مثل زيادة مهلات الوقت للشبكات البطيئة أو الطلبات طويلة الأمد. راجع السجلات للكشف عن الأخطاء المتعلقة بمهلات الوقت وأعد تشغيل الخادم بعد التغييرات. لمزيد من التفاصيل، راجع [توثيق IBM Liberty حول نقاط نهاية HTTP](https://www.ibm.com/docs/en/was-liberty/23.0.0?topic=configuration-http-endpoint-running-liberty).