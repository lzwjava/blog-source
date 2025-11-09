---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تحديث مسار سياق ويب سبير
translated: true
type: note
---

### تحديث جذر سياق الويب في IBM WebSphere Application Server (WAS)

يُعرّف جذر سياق الويب مسار URL الأساسي لتطبيق الويب الخاص بك (مثال: `/myapp`). في IBM WebSphere Application Server، يمكنك تحديثه إما أثناء النشر الأولي أو لتطبيق موجود عبر وحدة التحكم الإدارية. فيما يلي الخطوات الخاصة بتطبيق موجود. تأكد من حصولك على صلاحيات وصول إدارية لوحدة تحكم WAS.

#### المتطلبات الأساسية
- الوصول إلى وحدة التحكم الإدارية لـ WebSphere (عادةً عبر الرابط `https://your-server:9043/ibm/console`).
- يجب أن يكون التطبيق مثبتًا ومتوقفًا (يُوصى بذلك) قبل إجراء أي تغييرات لتجنب التعارضات.

#### خطوات تحديث جذر السياق
1. **تسجيل الدخول إلى وحدة التحكم الإدارية**:
   - افتح متصفح ويب وانتقل إلى عنوان URL لوحدة تحكم WAS.
   - أدخل بيانات الاعتماد الخاصة بالمشرف.

2. **الانتقال إلى التطبيق**:
   - في جزء التنقل الأيسر، قم بتوسيع **Applications** > **Application Types** > **WebSphere enterprise applications**.
   - ابحث عن التطبيق الذي قمت بنشره وحدده من القائمة.

3. **الوصول إلى إعدادات جذر السياق**:
   - في صفحة تفاصيل التطبيق، انتقل لأسفل إلى قسم **Web Module Properties**.
   - انقر على **Context root for web modules**.

4. **تحرير جذر السياق**:
   - في الجدول الذي يظهر، ابحث عن وحدة الويب (مثال: اسم ملف WAR الخاص بك).
   - قم بتحديث حقل **Context root** بالقيمة الجديدة (مثال: تغيير من `/oldapp` إلى `/newapp`). تجنب استخدام الشرطة المائلة الأولى إذا لم تكن مطلوبة، ولكن قم بتضمينها للمسارات مثل `/myapp`.
   - انقر على **OK** لحفظ التغييرات.

5. **حفظ ومزامنة التكوين**:
   - انقر على **Save** في وحدة التحكم (أو **Save directly to the master configuration** إذا تمت المطالبة بذلك).
   - إذا كنت في بيئة نشر مجمعة أو شبكية:
     - انتقل إلى **System administration** > **Nodes**.
     - حدد جميع العقد ذات الصلة وانقر على **Full Resynchronize**.

6. **إعادة تشغيل التطبيق**:
   - ارجع إلى **Applications** > **WebSphere enterprise applications**.
   - حدد تطبيقك وانقر على **Stop**، ثم **Start**.
   - بدلاً من ذلك، يمكنك إعادة تشغيل الخادم بالكامل عبر **Servers** > **Server Types** > **WebSphere application servers** > حدد الخادم > **Restart**.

7. **التحقق من التغيير**:
   - قم بالوصول إلى عنوان URL للتطبيق في المتصفح (مثال: `http://your-server:9080/newapp`).
   - تحقق من سجلات الخادم (مثال: `SystemOut.log`) للبحث عن أي أخطاء متعلقة بالنشر.

#### ملاحظات إضافية
- **أثناء النشر الأولي**: إذا كنت تقوم بنشر تطبيق جديد، فحدد جذر السياق في خطوة **Select installation options** تحت **Context root** لكل وحدة ويب.
- **ملفات EAR**: للتطبيقات المجمعة في ملف EAR، تأكد من أن ملف `application.xml` لا يحدد جذر السياق بشكل ثابت؛ حيث أن التجاوزات في وحدة التحكم لها الأولوية.
- **المشاكل الشائعة**:
  - قد لا تُطبق التغييرات إذا كان التطبيق قيد التشغيل — توقف عنه دائمًا أولاً.
  - في WebSphere Liberty أو Open Liberty، استخدم تكوينات ملف `server.xml` بدلاً من ذلك.
  - بالنسبة للخوادم الافتراضية أو الملحقات، قم بتحديث تكوين ملحق خادم الويب بعد التغييرات.
- إذا كان التطبيق يستخدم الأمان أو المكتبات المشتركة، قم باختباره بدقة بعد التحديث.

لمزيد من التفاصيل، راجع الوثائق الرسمية من IBM أو أدلة المجتمع.

#### المراجع
- [Context root for web modules settings](https://www.ibm.com/docs/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/uweb_contextroot.html)
- [IBM WebSphere - Context root of an application](https://www.freekb.net/Article?id=1647)
- [WebSphere 8.5 context root change not applying to WAR file](https://stackoverflow.com/questions/24472790/websphere-8-5-context-root-change-not-applying-to-war-file)