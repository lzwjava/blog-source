---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة خادم تطبيقات ويب سبير لـ IBM MQ
translated: true
type: note
---

### المتطلبات الأساسية
قبل تكوين IBM MQ (المعروف سابقًا باسم WebSphere MQ) في IBM WebSphere Application Server (WAS)، تأكد من الآتي:
- تثبيت IBM MQ على خادم مخصص (أو على نفس خادم WAS لوضع الربط المحلي).
- إنشاء مدير قوائم queue manager في IBM MQ (على سبيل المثال، باستخدام الأمر `crtmqm QMNAME`).
- إنشاء القوائم queues المطلوبة في مدير القوائم queue manager (على سبيل المثال، باستخدام MQ Explorer أو الأمر `runmqsc`).
- توفر مكتبات عميل IBM MQ (ملفات JAR مثل `com.ibm.mq.allclient.jar`، `com.ibm.mqjms.jar`). إذا كان WAS بعيدًا عن MQ، قم بتثبيت عميل IBM MQ على جهاز WAS.
- إضافة مستخدم عملية WAS إلى مجموعة `mqm` للحصول على الأذونات.
- للمستخدمين غير الجذر root على أنظمة Unix-like، استخدم الأمر `setmqaut` لمنح الأذونات.

### التكوين خطوة بخطوة
يتضمن التكوين إعداد موفر JMS، ومصانع الاتصال connection factories، والوجهات destinations في وحدة تحكم إدارة WAS Administrative Console. يفترض هذا اتصالًا في الوضع الموزع (العميل) عبر TCP/IP؛ قم بالتعديل لوضع الربط bindings mode إذا كان محليًا.

1. **الوصول إلى وحدة تحكم إدارة WAS Administrative Console**:
   - ابدأ تشغيل خادم WAS.
   - افتح متصفحًا وانتقل إلى `https://localhost:9043/ibm/console` (استبدل باسم المضيف host والمنفذ port الخاصين بك).
   - سجل الدخول باستخدام بيانات اعتماد المسؤول.

2. **تكوين موفر IBM MQ JMS Provider**:
   - انتقل إلى **Resources > JMS > Providers**.
   - انقر فوق **New**.
   - حدد **WebSphere MQ messaging provider**.
   - املأ التفاصيل:
     - **الاسم Name**: على سبيل المثال، `MQProvider`.
     - **الوصف Description**: اختياري.
     - **مسار الفئة Class path**: المسار إلى ملفات MQ JAR (على سبيل المثال، `/opt/mqm/java/lib/*` أو انسخها إلى `<WAS_HOME>/lib/ext`).
     - **مسار المكتبة الأصلية Native library path**: مطلوب لوضع الربط bindings mode (المسار إلى مكتبات MQ، على سبيل المثال، `/opt/mqm/lib64`).
     - **اسم مصنف السياق الأولي الخارجي External initial context factory name**: `com.ibm.mq.jms.context.WMQInitialContextFactory` (لوضع العميل client mode).
     - **عنURL موفر السياق الخارجي External context provider URL**: على سبيل المثال، `host:1414/CHANNEL` (host = عنوان IP لخادم MQ، 1414 = المنفذ الافتراضي، CHANNEL = على سبيل المثال، `SYSTEM.DEF.SVRCONN`).
   - احفظ التكوين.

3. **إنشاء مصنع اتصال قائمة Queue Connection Factory**:
   - انتقل إلى **Resources > JMS > Queue connection factories** (حدد النطاق scope لخادمك أو الخلية cell).
   - انقر فوق **New**.
   - حدد الموفر الذي تم إنشاؤه في الخطوة 2.
   - املأ:
     - **الاسم Name**: على سبيل المثال، `MQQueueCF`.
     - **اسم JNDI JNDI name**: على سبيل المثال، `jms/MQQueueCF`.
     - **مدير القوائم Queue manager**: اسم مدير قوائم MQ الخاص بك (على سبيل المثال، `QM1`).
     - **المضيف Host**: اسم المضيف host أو عنوان IP لخادم MQ.
     - **المنفذ Port**: 1414 (افتراضي).
     - **القناة Channel**: على سبيل المثال، `SYSTEM.DEF.SVRCONN`.
     - **نوع النقل Transport type**: `CLIENT` (لـ TCP/IP) أو `BINDINGS` (محلي).
     - **بيانات اعتماد الأمان Security credentials**: معرف المستخدم User ID وكلمة المرور password إذا لزم الأمر.
   - الخصائص المتقدمة الاختيارية: حدد أحجام تجمع الاتصال connection pool (على سبيل المثال، الحد الأقصى للاتصالات بناءً على الحمل load).
   - احفظ.

4. **إنشاء وجهات القوائم Queue Destinations**:
   - انتقل إلى **Resources > JMS > Queues**.
   - انقر فوق **New**.
   - حدد الموفر.
   - لكل قائمة queue:
     - **الاسم Name**: على سبيل المثال، `MyQueue`.
     - **اسم JNDI JNDI name**: على سبيل المثال، `jms/MyQueue`.
     - **اسم القائمة Queue name**: اسم القائمة المحدد في MQ (على سبيل المثال، `MY.LOCAL.QUEUE`).
     - **مدير القوائم Queue manager**: نفس ما ورد أعلاه.
     - **نوع العميل المستهدف Target client type**: `MQ` أو `JMS`.
   - احفظ. كرر للمواضيع topics إذا كنت تستخدم النشر/الاشتراك pub/sub.

5. **(اختياري) تكوين خادم WebSphere MQ Server لوضع الربط Bindings Mode**:
   - إذا كنت تستخدم الربط المحلي local bindings، انتقل إلى **Servers > Server Types > WebSphere MQ servers**.
   - انقر فوق **New**.
   - عيّن **الاسم Name**، **اسم مدير القوائم Queue manager name**.
   - حدد **تثبيتات MQ MQ installations** (المسار إلى تثبيت MQ).
   - احفظ وأعد تشغيل الخادم.

6. **تكوين محول المورد JCA (لـ MDBs)**:
   - انتقل إلى **Resources > Resource Adapters > J2C connection factories**.
   - إذا كنت تستخدم محول MQ المضمن MQ RA، فتأكد من نشره (يتضمن WAS الملف `wmq.jmsra.rar`).
   - عيّن خصائص مثل الحد الأقصى للاتصالات max connections (على سبيل المثال، 10-50 بناءً على الحمل load).

7. **اختبار التكوين**:
   - انشر تطبيق JMS نموذجي أو استخدم نموذج JMS الموجود في WAS.
   - افحص السجلات logs للبحث عن أخطاء (على سبيل المثال، رفض الاتصال على المنفذ 1414).
   - تحقق في MQ: استخدم MQ Explorer لمراقبة أعماق القوائم queue depths والقنوات channels.

8. **الأمان والإعداد المتقدم**:
   - تمكين SSL: قم بتكوين مستودعات المفاتيح keystores في WAS و MQ (قناة مع `SSLCIPH`).
   - تعيين المصادقة authentication: استخدم مجموعات مستخدمي MQ أو هويات مستخدمين بديلة alternate user IDs.
   - بالنسبة للتجمعات clusters: قم بمزامنة التكوينات عبر العقد nodes.

### نصائح لاستكشاف الأخطاء وإصلاحها
- **ClassNotFoundException**: تأكد من وجود ملفات MQ JAR في مسار الفئة classpath.
- **فشل الاتصال Connection failures**: افحص جدار الحماية firewall على المنفذ 1414، وحالة القناة channel status (استخدم الأمر `DISPLAY CHSTATUS(*)` في runmqsc).
- **مشاكل وضع الربط Bindings mode issues**: تحقق من المكتبات الأصلية native libs والمستخدم في مجموعة `mqm`.
- أعد تشغيل WAS بعد إجراء التغييرات.

للحصول على تفاصيل محددة للإصدار (على سبيل المثال، WAS 9.x مع MQ 9.x)، راجع وثائق IBM الرسمية.

[Using WebSphere Application Server with IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuring WebSphere Application Server for use with IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Creating a WebSphere MQ server definition](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)