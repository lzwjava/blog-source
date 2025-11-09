---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إنتيلي جي آي دي إي لتطوير ويب سبير
translated: true
type: note
---

### استخدام IntelliJ IDEA لتطوير IBM WebSphere Application Server (WAS)

يُعد IntelliJ IDEA خيارًا قويًا لتطوير تطبيقات Java EE الموجهة لخادم تطبيقات IBM WebSphere (WAS). فهو يدعم معايير Java EE، والتي يلتزم بها WAS، ويوفر أدوات ممتازة لبناء ونشر وتصحيح أخطاء التطبيقات المؤسسية. بينما يتمتع Eclipse بتكامل أصلي أكبر مع WAS عبر أدوات IBM، فإن IntelliJ يعمل بشكل جيد مع بعض الإعدادات. أدناه، سأغطي الأساسيات، والتصحيح عن بُعد (نعم، يمكنك الربط بآلة JVM الخاصة بـ WAS)، ونصائح إضافية.

#### 1. الإعداد الأولي لتطوير WAS في IntelliJ
- **تثبيت الإضافات المطلوبة**:
  - انتقل إلى **File > Settings > Plugins** وابحث عن "WebSphere Server" في JetBrains Marketplace. قم بتثبيتها لإدارة أفضل للخادم المحلي (مثل بدء/إيقاف WAS من IntelliJ). هذه الإضافة غير مضمنة بشكل افتراضي، لذا فهي اختيارية ولكن موصى بها للتطوير المحلي.
  - تأكد من تمكين إضافات Java EE و Jakarta EE (عادة ما تكون مثبتة مسبقًا).

- **إنشاء مشروع**:
  - ابدأ مشروع **Java Enterprise** جديدًا (أو استورد مشروعًا موجودًا).
  - اختر نموذج **Web Application وقم بتكوينه لـ Java EE (مثل الإصدار 8 أو 9، اعتمادًا على إصدار WAS الخاص بك مثل 9.x).
  - أضف التبعيات للمكتبات الخاصة بـ WAS إذا لزم الأمر (على سبيل المثال، عبر Maven/Gradle: `com.ibm.websphere.appserver.api:jsp-2.3` لدعم JSP).

- **تكوين خادم WAS المحلي (اختياري للتشغيل المحلي)**:
  - انتقل إلى **Run > Edit Configurations > + > WebSphere Server > Local**.
  - حدد مسار تثبيت WAS المحلي الخاص بك (مثال: `/opt/IBM/WebSphere/AppServer`).
  - عيّن اسم الخادم، و JRE (استخدم JDK الخاص بـ IBM إذا كان مضمنًا مع WAS)، وخيارات النشر (مثال: WAR مُفكك لإعادة التحميل الفوري Hot-reload).
  - للنشر: في علامة التبويب **Deployment**، أضف القطعة artifact الخاصة بك (مثل ملف WAR) وعيّن مسار السياق context path.

يتيح لك هذا الإعداد التشغيل/النشر مباشرة من IntelliJ للاختبار المحلي.

#### 2. التصحيح عن بُعد: ربط IntelliJ بآلة JVM الخاصة بـ WAS
نعم، يمكنك تمامًا ربط مصحح أخطاء IntelliJ بآلة JVM عن بُعد لـ WAS. هذا هو التصحيح عن بُعد القياسي لـ Java عبر JDWP (بروتوكول سلك تصحيح Java). وهو يعمل لكل من نسخ WAS المحلية والبعدية – عامل الخادم على أنه "JVM بعيدة".

**الخطوة 1: تمكين التصحيح على خادم WAS**
- **عبر وحدة التحكم الإدارية (موصى به للإعدادات الشبيهة بالإنتاج)**:
  - سجّل الدخول إلى وحدة التحكم الإدارية لـ WAS (مثال: `https://your-host:9043/ibm/console`).
  - انتقل إلى **Servers > Server Types > WebSphere Application Servers > [اسم الخادم الخاص بك] > Debugging Service**.
  - حدد **Enable service at server startup**.
  - عيّن **JVM debug port** (الافتراضي هو 7777؛ اختر منفذًا غير مستخدم مثل 8000 لتجنب التعارضات).
  - احفظ وأعد تشغيل الخادم.

- **عبر server.xml (للإعدادات المستقلة أو التعديلات السريعة)**:
  - حرر الملف `$WAS_HOME/profiles/[الملف الشخصي]/config/cells/[الخلية]/nodes/[العقدة]/servers/[الخادم]/server.xml`.
  - في قسم `<jvmEntries>` تحت `<processDefinitions>`، أضف أو حدّث:
    ```
    <jvmEntries xmi:id="..." debugMode="true">
      <debugArgs>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:8000</debugArgs>
    </jvmEntries>
    ```
    - `suspend=n` يبدأ الخادم بشكل طبيعي (استخدم `suspend=y` لإيقافه مؤقتًا عند بدء التشغيل).
    - استبدل `8000` بالمنفذ الخاص بك.
  - احفظ، ثم أعد تشغيل الخادم: `./startServer.sh [اسم الخادم]` (أو عبر وحدة التحكم).

- التحقق: افحص سجلات الخادم للعثور على "JDWP: transport=dt_socket, address=*:8000" أو ما شابه.

**الخطوة 2: تكوين التصحيح عن بُعد في IntelliJ**
- انتقل إلى **Run > Edit Configurations > + > Remote JVM Debug**.
- سمّه (مثال: "WAS Remote Debug").
- عيّن **Debugger mode** إلى "Attach to remote JVM".
- **Host**: عنوان IP/اسم مضيف خادم WAS الخاص بك (مثال: `localhost` للمحلي، `192.168.1.100` للبعيد).
- **Port**: منفذ تصحيح JVM (مثال: 8000).
- اختياريًا، عيّن **Use module classpath** إذا كان لمشروعك مكتبات محددة.
- طبق وأغلق.

**الخطوة 3: الربط والتصحيح**
- عيّن نقاط التوقف breakpoints في الكود الخاص بك (مثال: في servlet أو EJB).
- انشر تطبيقك على WAS (يدويًا عبر وحدة التحكم الإدارية أو نصوص wsadmin).
- شغّل تكوين التصحيح (**Run > Debug 'WAS Remote Debug'**).
- شغّل تطبيقك (مثال: عبر طلب HTTP). سيرتبط IntelliJ، وسيتوقف التنفيذ عند نقاط التوقف.
- المشاكل الشائعة: جدار الحماية يمنع المنفذ، إصدارات JDK غير متطابقة (استخدم IBM JDK الخاص بـ WAS في IntelliJ)، أو أن الخادم لم يُعاد تشغيله بعد تغييرات التكوين.

هذا يعمل مع WAS 7+ (بما في ذلك Liberty profile). للخوادم البعيدة، تأكد من الوصول إلى الشبكة لمنفذ التصحيح.

#### 3. نصائح أخرى لتطوير WAS فعال
- **النشر الفوري / التبديل السريع Hot Deployment/Hotswap**: للتكرارات الأسرع، انشر كـ WAR "مفكك" (غير مضغوط). يدعم WAS إعادة التحميل الفوري لـ JSPs وبعض الفئات، ولكن للتبديل السريع الكامل (تغييرات الكود دون إعادة تشغيل)، استخدم إضافة JRebel (مدفوعة) أو DCEVM + HotSwapAgent (مجانية، ولكن اختبر التوافق مع IBM JDK الخاص بـ WAS).

- **أدوات البناء**: استخدم Maven أو Gradle للتبعيات. أضف مكتبات وقت تشغيل WAS كنطاق provided لتجنب تضخم classpath:
  ```
  <dependency>
    <groupId>com.ibm.websphere.appserver.runtime</groupId>
    <artifactId>shared</artifactId>
    <version>9.0.5</version>
    <scope>provided</scope>
  </dependency>
  ```
  شغّل `mvn clean package` وانشر ملف WAR عبر وحدة التحكم الإدارية.

- **التسجيل والتحليل الأدائي Logging and Profiling**: ادمج SLF4J/Logback لتسجيلات التطبيق. للأداء، استخدم VisualVM أو YourKit (ارتبط عن بُعد مثل التصحيح). أداة PMI (بنية البنية التحتية لمراقبة الأداء) الخاصة بـ WAS رائعة – مكّنها في وحدة التحكم الإدارية للحصول على المقاييس.

- **الاختبار**: استخدم Arquillian لاختبارات التكامل ضد خادم WAS بعيد. أو ضمّن Open Liberty (متوافق مع WAS) لاختبارات الوحدة المحلية دون الحاجة إلى WAS كامل.

- **ملاحظات خاصة بالإصدار**: بالنسبة لـ WAS 9.x+، استفد من أدوات ترحيل Jakarta EE في IntelliJ. إذا كنت تستخدم WAS Liberty (مرتكز على microprofile)، فإن إضافة Liberty Tools تضيف وضع المطور مع إعادة التحميل التلقائي.

- **المزالق الشائعة**:
  - مشاكل classpath: تأكد من تطابق Project SDK في IntelliJ مع JDK الخاص بـ WAS.
  - الأمان: التصحيح عن بُعد يعرض المنفذ – استخدمه فقط في شبكات التطوير/الموثوقة.
  - قيود الإضافات: إضافة WebSphere أساسية؛ للميزات المتقدمة، فكر في IBM Rational Application Developer (ولكن التزم بـ IntelliJ لسهولة استخدامه).

هذا يجب أن يجعلك جاهزًا للتشغيل. إذا كنت تستخدم إصدارًا محددًا من WAS، شارك التفاصيل للحصول على نصائح أكثر تخصيصًا.

#### المراجع
- [Run/Debug Configuration: WebSphere Server | IntelliJ IDEA](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
- [WebSphere remote server debug configuration in IntelliJ Idea](https://stackoverflow.com/questions/33013860/websphere-remote-server-debug-configuration-in-intellij-idea)
- [Debug code running on IBM Websphere using Eclipse / Intellij IDEA](https://davanum.wordpress.com/2009/11/20/debug-code-running-on-ibm-websphere-using-eclipse-intellij-idea/)
- [Debugging applications - IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-debugging)
- [Remote Debugging with IntelliJ IDEA | Baeldung](https://www.baeldung.com/intellij-remote-debugging)