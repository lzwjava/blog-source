---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: جايثون في خادم تطبيقات ويب سبير
translated: true
type: note
---

### استخدام Jython في IBM WebSphere Application Server

ملاحظة: "jPython" تشير إلى Jython، وهي تنفيذ لـ Python يعمل على آلة جافا الافتراضية (JVM). تُستخدم عادة في WebSphere للأعمال الإدارية النصية ويمكن أيضًا دمجها في التطبيقات المُنشأة. يُضمّن WebSphere Application Server (WAS) Jython (عادة الإصدار 2.1 أو أحدث، اعتمادًا على إصدار WAS) في المسار `<WAS_HOME>/optionalLibraries/jython`، لذا لا تكون هناك حاجة عادةً لتثبيت منفصل. أدناه، سأغطي حالتي الاستخدام الأساسيتين: المهام الإدارية والاستخدام أثناء التشغيل في التطبيقات.

#### 1. البرمجة النصية الإدارية باستخدام wsadmin
الطريقة الأكثر شيوعًا لاستخدام Jython في WebSphere هي لمهام إدارة الخادم مثل نشر التطبيقات، بدء/إيقاف الخوادم، تكوين الموارد، وعرض قائمة التطبيقات المثبتة. يتم ذلك عبر أداة `wsadmin`، التي تدعم Jython كلغة برمجة نصية مفضلة (بدلاً من Jacl القديمة).

**المتطلبات الأساسية:**
- تأكد من أن خادم WebSphere قيد التشغيل.
- حدد موقع `wsadmin` في `<WAS_HOME>/bin/wsadmin.sh` (Linux/Unix) أو `wsadmin.bat` (Windows).
- Jython مُضمّن مسبقًا؛ للحصول على ميزات أحدث (مثل بناء جملة Python 2.5+)، قد تحتاج إلى الترقية عبر مسار فئات مخصص (انظر الملاحظات المتقدمة أدناه).

**الخطوات الأساسية لتشغيل نص Jython:**
1. أنشئ ملف نص Jython (مثل `example.py`) مع الكود الخاص بك. استخدم كائنات AdminConfig وAdminControl وAdminApp للعمليات الخاصة بـ WebSphere.
   
   مثال على نص لسرد جميع التطبيقات المثبتة (`listApps.py`):
   ```
   # سرد جميع التطبيقات
   apps = AdminApp.list()
   print("التطبيقات المثبتة:")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # اختياري: حفظ تغييرات التكوين
   ```

2. شغّل النص باستخدام `wsadmin`:
   - الاتصال عبر SOAP (افتراضي للاتصال البعيد):  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <اسم_المضيف> -port <منفذ_soap> -user <مستخدم_المسؤول> -password <كلمة_مرور_المسؤول>
     ```
   - للمحلي (بدون مضيف/منفذ):  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - مثال على الناتج: يسرد تطبيقات مثل `DefaultApplication`.

3. للوضع التفاعلي (REPL):  
   ```
   wsadmin.sh -lang jython
   ```
   ثم اكتب أوامر Jython مباشرة، مثل `print AdminApp.list()`.

**أمثلة شائعة:**
- **نشر EAR/WAR:** أنشئ `deployApp.py`:
  ```
  appName = 'MyApp'
  earPath = '/path/to/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('تم نشر ' + appName)
  ```
   التشغيل: `wsadmin.sh -lang jython -f deployApp.py`.

- **بدء/إيقاف الخادم:**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # أو 'stop'
  ```

- **تحديد إصدار Jython (إذا لزم الأمر):** لـ Jython 2.1 صراحةً:  
  `wsadmin.sh -usejython21 true -f script.py`. للإصدارات المخصصة، أضف إلى مسار الفئات: `-wsadmin_classpath /path/to/jython.jar`.

**نصائح:**
- استخدم `AdminConfig.help('نوع_الكائن')` للحصول على مساعدة بالأوامر.
- يمكن أتمتة النصوص في CI/CD (مثل Jenkins) عن طريق استدعاء `wsadmin` في ملفات الدُفعات.
- للعميل الخفيف (بدون تثبيت WAS كامل): حمّل برامج جافا الخاصة بالعميل من IBM وضبط مسار الفئات.

#### 2. استخدام Jython في التطبيقات المُنشأة
لتنفيذ كود Jython داخل تطبيق جافا (مثل servlet أو EJB) يعمل على WebSphere، قم بتضمين وقت تشغيل Jython (jython.jar) في مسار فئات التطبيق. هذا يسمح بتضمين نصوص Python أو استخدام Jython كمحرك برمجة نصية. حمّل أحدث jython.jar من موقع Jython الرسمي إذا كانت النسخة المضمنة قديمة.

هناك طريقتان رئيسيتان: **مسار الفئات** (على مستوى الخادم) أو **المكتبة المشتركة** (قابلة لإعادة الاستخدام عبر التطبيقات).

**الطريقة 1: مسار الفئات (إضافة مباشرة إلى JVM)**
1. احفظ `jython.jar` في مسار يمكن الوصول إليه على مضيف WebSphere (مثل `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`).
2. سجّل الدخول إلى وحدة تحكم إدارة WebSphere.
3. انتقل إلى **Servers > Server Types > WebSphere application servers > [خادمك]**.
4. انتقل إلى **Java and Process Management > Process definition > Java Virtual Machine > Classpath**.
5. أضف المسار الكامل لـ `jython.jar` (مثل `/opt/.../jython.jar`).
6. في **Generic JVM arguments**، أضف مسار Python:  
   `-Dpython.path=/opt/.../jython.jar/Lib` (يشير إلى المكتبة القياسية لـ Jython).
7. انقر **OK**، احفظ التكوين، وأعد تشغيل الخادم.
8. زامن العقد إذا كنت في بيئة عنقودية (عبر **System administration > Nodes > Synchronize**).
9. في كود جافا الخاص بك، استخدم `org.python.util.PythonInterpreter` لتشغيل نصوص Jython:
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hello from Jython in WebSphere!')");
   ```

**الطريقة 2: المكتبة المشتركة (مُوصى بها لتطبيقات متعددة)**
1. ضع `jython.jar` في دليل مشترك (مثل `/shared/libs/jython.jar`).
2. في وحدة تحكم الإدارة: **Environment > Shared libraries > [النطاق: Server أو Cell] > New**.
3. أدخل اسمًا (مثل `JythonLib`)، حدد **Use a native library directory**، وضبط **Classpath** على `/shared/libs/jython.jar`.
4. احفظ.
5. لتطبيق محدد: **Applications > Application Types > WebSphere enterprise applications > [تطبيقك] > Reference shared libraries**.
6. تحت **Shared library references**، انقر **Add**، اختر `JythonLib`، وضبط **Classpath** ليطابق.
7. احفظ، حدّث التطبيق (أعد التشغيل إذا لزم الأمر)، وزامن العقد.
8. أشر إليه في الكود كما في طريقة مسار الفئات.

**نصائح للتطبيقات:**
- لتطبيقات Jython القائمة على servlet، استخدم PyServlet (مُضمن في Jython) لمعالجات Python.
- اختبر في بيئة تطوير؛ راقب السجلات بحثًا عن مشاكل في مسار الفئات.
- إذا كنت تستخدم إصدار Jython أحدث (مثل 2.7)، تأكد من التوافق مع جافا 8+.

#### ملاحظات متقدمة
- **توافق الإصدارات:** WAS 9.x يستخدم Jython 2.7+. للترقيات، استبدل الملف jar المضمن ولكن اختبر بدقة.
- **معالجة الأخطاء:** في النصوص، استخدم `try: ... except Exception as e: print(e)`.
- **دعم IDE:** استخدم IBM Rational Application Developer (RAD) أو Eclipse مع إضافات WebSphere لتصحيح أخطاء نصوص Jython/wsadmin.
- **الموارد:** للحصول على دروس كاملة، انظر كتاب *WebSphere Application Server Administration Using Jython* أو وثائق wsadmin من IBM.

إذا كان هذا لا يتطابق مع سيناريوك المحدد (مثل إصدار WAS محدد أو حالة استخدام)، قدم المزيد من التفاصيل للحصول على نصيحة مخصصة.

**المراجع:**  
- [Using wsadmin scripting with Jython (IBM Docs)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [Deploying Jython on WebSphere (Oracle Guide)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [WebSphere Jython Integration (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [Jython Wiki on WebSphere](https://wiki.python.org/jython/WebSphere)  
- [Deploy App with Jython Example](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)