---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة آي بي إم إم كيو في ويب سبير
translated: true
type: note
---

### تكوين قوائم الانتظار للرسائل في IBM WebSphere Application Server (باستخدام IBM MQ كمزود)

يدعم IBM WebSphere Application Server (WAS) نظام قوائم انتظار الرسائل من خلال تكامل Java Message Service (JMS) مع IBM MQ (المعروف سابقًا باسم WebSphere MQ). يتم التكوين عادةً عبر **وحدة التحكم المتكاملة لحلول WebSphere** (الواجهة الإدارية)، التي يمكن الوصول إليها عبر `https://your-server:9043/ibm/console` (منفذ آمن افتراضي؛ قم بتعديله حسب الحاجة). يركز هذا الدليل على WAS ذو الملف الشخصي الكامل التقليدي (مثل الإصدار 9.0+)، ولكن الخطوات مشابهة لـ WebSphere Liberty مع تعديلات طفيفة.

#### المتطلبات الأساسية
- يجب تثبيت IBM MQ وتشغيله وإتاحة الوصول إليه (مثل بدء مدير قائمة الانتظار).
- يجب أن يكون خادم WAS قيد التشغيل، وأن يكون لديك حق الوصول كمسؤول إلى وحدة التحكم.
- قم بتنزيل وتثبيت مكتبات عميل JMS لـ IBM MQ (مثل `com.ibm.mq.allclient.jar`) في المكتبات المشتركة لـ WAS إذا لم تكن موجودة مسبقًا (ضمن **Environment > Shared Libraries**).
- تأكد من تكوين موفر رسائل WebSphere MQ (ضمن **Resources > JMS > JMS providers**). إذا لم يكن كذلك، قم بإنشاء واحد بتفاصيل مثل المضيف، والمنفذ (الافتراضي 1414)، واسم مدير قائمة الانتظار.

بعد التكوين، احفظ التغييرات (زر **Save** في الأعلى) وأعد تشغيل خادم التطبيق لبدء سريانها.

#### الخطوة 1: إنشاء مصنع اتصال JMS Queue
يقوم مصنع الاتصال بإنشاء اتصالات بمدير قائمة الانتظار IBM MQ.

1.  سجّل الدخول إلى وحدة التحكم الإدارية لـ WAS.
2.  في جزء التنقل، قم بتوسيع **Resources > JMS > Queue connection factories**.
3.  حدد **Scope** المناسب (مثل Cell، Node، Server) من القائمة المنسدلة وانقر على **Apply**.
4.  انقر على **New**.
5.  حدد **WebSphere MQ messaging provider** وانقر على **OK**.
6.  في الشاشة التالية:
    *   **Name**: أدخل اسمًا وصفيًا (مثل `MyMQQueueConnectionFactory`).
    *   **JNDI name**: أدخل ربط JNDI (مثل `jms/MyQueueConnectionFactory`).
    *   انقر على **Next**.
7.  أدخل تفاصيل الاتصال:
    *   **Queue manager**: اسم مدير قائمة الانتظار IBM MQ الخاص بك (مثل `QM1`).
    *   **Host name**: اسم مضيف أو IP خادم IBM MQ.
    *   **Port**: منفذ المستمع (الافتراضي: 1414).
    *   **Transport type**: CHANNEL (لوضع العميل) أو BINDINGS (للدمج المضمن).
    *   **Channel**: اسم القناة الافتراضي (مثل `SYSTEM.DEF.SVRCONN`).
    *   **User ID** و **Password**: بيانات الاعتماد للمصادقة على MQ (إذا لزم الأمر).
    *   انقر على **Next**.
8.  راجع الملخص وانقر على **Finish**.
9.  حدد المصنع الجديد، وانتقل إلى **Additional Properties > Connection pool** (اختياري)، واضبط الإعدادات مثل **Maximum connections** (مثلًا، بناءً على الحمل المتوقع).
10. انقر على **Test connection** للتحقق.

#### الخطوة 2: إنشاء وجهة JMS Queue
يحدد هذا نقطة نهاية قائمة الانتظار الفعلية لإرسال/استقبال الرسائل.

1.  في جزء التنقل، قم بتوسيع **Resources > JMS > Queues**.
2.  حدد **Scope** المناسب (مطابق لمصنع الاتصال) وانقر على **Apply**.
3.  انقر على **New**.
4.  حدد **WebSphere MQ messaging provider** وانقر على **OK**.
5.  حدد الخصائص:
    *   **Name**: اسم وصفي (مثل `MyRequestQueue`).
    *   **JNDI name**: ربط JNDI (مثل `jms/MyRequestQueue`).
    *   **Base queue name**: اسم قائمة الانتظار الدقيق في IBM MQ (مثل `REQUEST.QUEUE`؛ يجب أن تكون موجودة أو يتم إنشاؤها في MQ).
    *   **Target client**: JMS (لتطبيقات JMS) أو MQ (لتطبيقات MQ الأصلية).
    *   **Target destination mode**: Once only (الافتراضي للموثوقية).
    *   انقر على **OK**.
6.  (اختياري) ضمن **Additional Properties**، قم بتكوين إعدادات الثبات أو انتهاء الصلاحية أو الأولوية.
7.  احفظ التكوين.

#### الخطوة 3: (اختياري) إنشاء مواصفات تفعيل لـ Message-Driven Beans (MDBs)
إذا كنت تستخدم MDBs لاستهلاك الرسائل بشكل غير متزامن:

1.  في جزء التنقل، قم بتوسيع **Resources > JMS > Activation specifications**.
2.  حدد **Scope** وانقر على **New**.
3.  حدد **WebSphere MQ messaging provider** وانقر على **OK**.
4.  أدخل:
    *   **Name**: مثل `MyQueueActivationSpec`.
    *   **JNDI name**: مثل `jms/MyQueueActivation`.
    *   **Destination type**: Queue.
    *   **Destination JNDI name**: JNDI الخاص بقائمة الانتظار الخاصة بك (مثل `jms/MyRequestQueue`).
    *   **Connection factory JNDI name**: JNDI الخاص بمصنع الاتصال الخاص بك (مثل `jms/MyQueueConnectionFactory`).
    *   Message selector (اختياري): محدد JMS لتصفية الرسائل.
5.  ضمن **Additional Properties > Message Listener Service > Listener Ports**، قم بإنشاء منفذ إذا لزم الأمر:
    *   **Name**: مثل `MyListenerPort`.
    *   **Connection factory JNDI**: كما هو مذكور أعلاه.
    *   **Destination JNDI**: كما هو مذكور أعلاه.
    *   **Component**: واصف النشر لـ MDB الخاص بك.
6.  انقر على **OK** واحفظ.

#### الخطوة 4: التحقق والاختبار
*   **الاختبار في وحدة التحكم**: استخدم **Test connection** على المصانع والمواصفات.
*   **نشر تطبيق**: أنشئ عميل JMS بسيط أو تطبيق MDB، ونشره، وأرسل/اختبر الرسائل عبر أدوات IBM MQ (مثل MQ Explorer).
*   **المراقبة**: ضمن **Monitoring and Tuning > Performance Viewer** أو **Troubleshooting > Logs**، تحقق من وجود أخطاء متعلقة بـ JMS.
*   المشكلات الشائعة:
    *   فشل الاتصال: تحقق من جدار الحماية، وحالة قناة MQ (`DISPLAY CHANNEL`)، وبيانات الاعتماد.
    *   أخطاء البحث في JNDI: تأكد من صحة عمليات الربط وأن التطبيق يستخدم النطاق الصحيح.
    *   الثبات: محاذاة إعدادات المتانة بين WAS و MQ.

للبدائل عبر سطر الأوامر (برمجة wsadmin)، راجع وثائق IBM. قم بالضبط بناءً على إصدارك (مثلًا، WAS 9.0.5+ يدعم JMS 2.0).

#### المراجع
*   [Configuring JMS resources in WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
*   [WebSphere MQ messaging provider queue settings](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
*   [Creating a WebSphere MQ messaging provider queue connection factory](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
*   [Configure a JMS queue destination for WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)