---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة موارد JMS في WebSphere
translated: true
type: note
---

### المتطلبات الأساسية
- تأكد من أن لديك حق الوصول الإداري إلى وحدة تحكم الحلول المتكاملة (Admin Console) لخادم تطبيقات IBM WebSphere.
- يجب أن يكون الخادم قيد التشغيل، ويجب أن تقرر النطاق (مثل: الخلية، العقدة، الخادم) للموارد.
- يركز هذا الدليل على موفر المراسلة الافتراضي (باستخدام Service Integration Bus أو SIBus)، وهو موفر JMS المدمج في WAS. إذا كنت تستخدم WebSphere MQ، فستكون هناك حاجة إلى تكوين إضافي لموفر MQ.
- أعد تشغيل الخادم بعد إجراء تغييرات كبيرة إذا تمت مطالبتك بذلك.

### الخطوة 1: إنشاء ناقل تكامل الخدمة (Service Integration Bus)
يعمل ناقل تكامل الخدمة ك العمود الفقري للمراسلة لموارد JMS.

1.  سجّل الدخول إلى وحدة تحكم الحلول المتكاملة لـ WebSphere.
2.  انتقل إلى **Service integration > Buses**.
3.  انقر على **New**.
4.  أدخل اسمًا فريدًا للناقل (مثل: `MyJMSBus`).
5.  امسح خيار **Bus security** ما لم يكن مطلوبًا.
6.  انقر على **Next**، ثم **Finish** لإنشاء الناقل.

### الخطوة 2: إضافة الخادم كعضو في الناقل (Bus Member)
هذا يمكن الخادم من استضافة محركات المراسلة على الناقل.

1.  حدد الناقل الذي أنشأته (مثل: `MyJMSBus`).
2.  ضمن **Additional properties**، انقر على **Bus members**.
3.  انقر على **Add**.
4.  في معالج **Add a New Bus Member**:
    - حدد **Messaging engine** كنوع عضو الناقل.
    - اختر خادمك (مثل: `server1`) من القائمة.
    - بالنسبة لمستودع الرسائل (message store)، حدد **File store** (الافتراضي للبيئات غير المجمعة) أو **Data store** للثبات في قاعدة البيانات، وقم بتكوين الخصائص إذا لزم الأمر.
5.  انقر على **Next**، ثم **Finish**.
6.  أعد تشغيل خادم تطبيقات WebSphere لتفعيل عضو الناقل.

### الخطوة 3: إنشاء مصنع اتصال JMS (JMS Connection Factory)
مصنع الاتصال مطلوب لتوصيل عملاء JMS بموفر الخدمة.

1.  انتقل إلى **Resources > JMS > Connection factories**.
2.  حدد النطاق المناسب (مثل: Server scope لـ `server1`) وانقر على **New**.
3.  حدد **Default messaging provider** وانقر على **OK**.
4.  أدخل التفاصيل:
    - **الاسم**: مثل `MyJMSConnectionFactory`.
    - **اسم JNDI**: مثل `jms/MyConnectionFactory`.
    - **اسم الناقل (Bus name)**: حدد `MyJMSBus` من القائمة المنسدلة.
    - اترك الإعدادات الافتراضية الأخرى (مثل: Provider endpoints كما هي مكتشفة تلقائيًا).
5.  انقر على **Apply**، ثم **Save** لحفظ التكوين الرئيسي.

### الخطوة 4: إنشاء طابور JMS (JMS Queue)
يحدد هذا الوجهة (طابور) للمراسلة من نقطة إلى نقطة.

1.  انتقل إلى **Resources > JMS > Queues**.
2.  حدد النطاق المناسب وانقر على **New**.
3.  حدد **Default messaging provider** وانقر على **OK**.
4.  أدخل التفاصيل:
    - **الاسم**: مثل `MyJMSQueue`.
    - **اسم JNDI**: مثل `jms/MyQueue`.
    - **اسم الناقل (Bus name)**: حدد `MyJMSBus`.
    - **اسم الطابور (Queue name)**: حدد **Create Service Integration Bus Destination**، وأدخل معرفًا فريدًا (مثل: `MyQueueDestination`)، وحدد عضو الناقل الذي تم إنشاؤه مسبقًا.
    - **اسم الطابور الأساسي (Base queue name)**: مثل `$MyJMSBus:MyQueueDestination` (يتم إنشاؤه تلقائيًا).
5.  قم بتكوين خصائص إضافية إذا لزم الأمر (مثل: وضع التسليم، انتهاء الصلاحية).
6.  انقر على **Apply**، ثم **Save** لحفظ التكوين الرئيسي.

### الخطوة 5: (اختياري) إنشاء مواصفات التنشيط لحبوب الرسائل الموجهة (MDBs)
إذا كنت تستخدم MDBs لاستهلاك الرسائل من الطابور، قم بتكوين مواصفات التنشيط.

1.  انتقل إلى **Resources > JMS > Activation specifications**.
2.  حدد النطاق المناسب وانقر على **New**.
3.  حدد **Default messaging provider** وانقر على **OK**.
4.  أدخل التفاصيل:
    - **الاسم**: مثل `MyActivationSpec`.
    - **اسم JNDI**: مثل `jms/activation/MyActivationSpec`.
    - **اسم الناقل (Bus name)**: حدد `MyJMSBus`.
    - **نوع الوجهة (Destination type)**: Queue.
    - **الوجهة (Destination)**: أدخل اسم JNDI للطابور (مثل: `jms/MyQueue`).
5.  انقر على **Apply**، ثم **Save** لحفظ التكوين الرئيسي.

### التحقق والاختبار
- بعد الحفظ، قم بمزامنة العقد إذا كنت في بيئة مجمعة.
- أعد تشغيل الخادم.
- استخدم تطبيق عميل JMS لاختبار إرسال/استقبال الرسائل عبر أسماء JNDI.
- راقب عبر **Service integration > Buses > [اسم الناقل الخاص بك] > Bus members > [العضو الخاص بك] > Messaging engines**.

للحصول على تكوينات متقدمة (مثل: الأمان، التجميع)، راجع وثائق IBM.

[تكوين IBM WebSphere Application Server لـ Decision Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[إدارة المراسلة باستخدام موفر المراسلة الافتراضي](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)