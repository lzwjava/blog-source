---
audio: false
lang: ar
layout: post
title: استخدام إكليبس
translated: true
---

### النقاط الرئيسية
- يبدو أن Eclipse يمكن استخدامه بشكل فعال مع IBM Websphere Liberty، Spring، Spring Boot، ومافن، ولكن يتطلب إعدادات محددة.
- تشير الأبحاث إلى تثبيت Spring Tool Suite (STS) وIBM Liberty Developer Tools كإضافات في Eclipse لتحسين الوظائف.
- تشير الأدلة إلى إنشاء مشروع Spring Boot باستخدام STS أو Spring Initializr، ثم تهيئته لتوزيع Websphere Liberty.

### إعداد Eclipse
لبدء العمل، قم بتنزيل وتثبيت "Eclipse IDE for Enterprise Java and Web Developers" من [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers). تأكد من أن لديك JDK 17 أو أحدث مثبتًا، يمكنك التحقق من ذلك عن طريق تشغيل `java -version` في مستودعك.

### تهيئة Spring وSpring Boot
قم بتثبيت الإضافة Spring Tool Suite (STS) عن طريق الذهاب إلى Help -> Eclipse Marketplace في Eclipse، البحث عن "Spring Tools"، وتثبيت الإصدار المناسب. هذا يحسن من تطوير Spring وSpring Boot. يمكنك إنشاء مشروع Spring Boot جديد مباشرة في Eclipse عن طريق File -> New -> Spring Starter Project، اختيار Maven كدالة بناء، وإضافة الاعتماديات اللازمة مثل Spring Web.

### التكامل مع IBM Websphere Liberty
قم بتثبيت IBM Liberty Developer Tools من Eclipse Marketplace عن طريق البحث عن "IBM Liberty Developer Tools" وتتبع تعليمات التثبيت. قم بإعداد خادم Websphere Liberty عن طريق الذهاب إلى Window -> Preferences -> Servers -> Runtime Environments، إضافة Runtime Websphere Liberty جديد، وإضافة خادم عن طريق File -> New -> Other -> Server. تأكد من أن ملف server.xml للخادم يحتوي على `<feature>springBoot-2.0</feature>` لدعم Spring Boot، كما هو موضح في [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html).

### نشر تطبيقك
قم بتعديل تطبيق Spring Boot لتوسيع `SpringBootServletInitializer` بدلاً من استخدام طريقة رئيسية تبدأ خادمًا مدمجًا، قم بتغليفه كملف WAR عن طريق تعيين `<packaging>war</packaging>` في ملف pom.xml. قم بالنشر عن طريق النقر بالزر الأيمن على المشروع، اختيار "Run As -> Run on Server"، واختيار خادم Liberty الخاص بك. هذا يضمن تشغيل التطبيق على خادم Liberty.

---

### ملاحظة الاستبيان: دليل شامل لاستخدام Eclipse مع IBM Websphere Liberty، Spring، Spring Boot، ومافن

يقدم هذا الدليل مراجعة مفصلة لاستخدام Eclipse مع IBM Websphere Liberty، Spring، Spring Boot، ومافن، مخصص للمطورين الذين يعملون في هذه الأنظمة. يتضمن العملية إعداد Eclipse، تثبيت الإضافات اللازمة، إنشاء وتهيئة المشاريع، ونشر التطبيقات، مع التركيز على التكامل والتوصيات الأفضل اعتبارًا من 27 فبراير 2025.

#### إعداد Eclipse والمتطلبات السابقة
يخدم Eclipse كبيئة تطوير متكاملة قوية للبرمجة بالجايفا، خاصة للتطبيقات التجارية. لهذا الإعداد، قم بتنزيل "Eclipse IDE for Enterprise Java and Web Developers" الإصدار 2024-06، المتاح في [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers). تأكد من أن نظامك يحتوي على JDK 17 أو أحدث، يمكنك التحقق من ذلك عن طريق تشغيل `java -version` في المستودع. يضمن هذا الإصدار التوافق مع ميزات Spring وLiberty الحديثة.

#### تثبيت الإضافات الأساسية
لزيادة من Eclipse لتطوير Spring وSpring Boot، قم بتثبيت Spring Tool Suite (STS)، الجيل التالي من أدوات Spring. قم بذلك عن طريق Help -> Eclipse Marketplace، البحث عن "Spring Tools"، وتثبيت العنصر المسمى "Spring Tools (aka Spring IDE and Spring Tool Suite)." هذه الإضافة، كما هو موضح في [Spring Tools](https://spring.io/tools/)، توفر دعمًا عالميًا للتطبيقات القائمة على Spring، وتكاملًا متكاملًا مع Eclipse لميزات مثل إنشاء المشروع والتشخيص.

للتكامل مع IBM Websphere Liberty، قم بتثبيت IBM Liberty Developer Tools، المتاحة أيضًا من خلال Eclipse Marketplace عن طريق البحث عن "IBM Liberty Developer Tools." هذه الإضافة، التي تم اختبارها لـ Eclipse 2024-06 كما هو موضح في [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)، تسهل بناء وتوزيع تطبيقات Java EE إلى Liberty، مع دعم لأصدارات تعود إلى 2019-12.

#### إنشاء مشروع Spring Boot
هناك طرقتان رئيسيتان لإنشاء مشروع Spring Boot في Eclipse مع STS مثبتًا:

1. **استخدام Spring Initializr**: زور [Spring Initializr](https://start.spring.io/)، اختر Maven كدالة بناء، اختر بيانات المشروع (Group، Artifact، إلخ)، وأضف الاعتماديات مثل Spring Web. قم بإنشاء المشروع كملف ZIP، قم بفكه، وإدخاله إلى Eclipse عن طريق File -> Import -> Existing Maven Project، واختيار المجلد المفكوك.

2. **استخدام STS مباشرة**: افتح Eclipse، اذهب إلى File -> New -> Other، توسع Spring Boot، واختر "Spring Starter Project." اتبع السحابة، تأكد من اختيار Maven كالنوع، واختر الاعتماديات. هذه الطريقة، كما هو موضح في [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)، هي المفضلة لالتكامل مع مساحة عمل Eclipse.

تضمن كلتا الطريقتين مشروعًا قائمًا على Maven، وهو ضروري لإدارة الاعتماديات مع Spring Boot.

#### تهيئة لتوزيع Websphere Liberty
لتوزيع إلى Websphere Liberty، قم بتعديل تطبيق Spring Boot لتعمل على خادم Liberty بدلاً من بدء خادم مدمج. يتضمن ذلك:

- التأكد من أن فئة التطبيق الرئيسية تمتد `SpringBootServletInitializer`. على سبيل المثال:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // لا يوجد طريقة رئيسية؛ Liberty يدير البدء
  }
  ```

- تحديث ملف pom.xml لتغليف كملف WAR عن طريق إضافة:

  ```xml
  <packaging>war</packaging>
  ```

  هذا ضروري لتوزيع خادم Servlet التقليدي، كما هو موضح في [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet).

يقدم Websphere Liberty، وخاصة نسخة المصدر المفتوح Open Liberty، دعمًا لتطبيقات Spring Boot مع ميزات محددة. تأكد من أن ملف server.xml للخادم يحتوي على `<feature>springBoot-2.0</feature>` لدعم Spring Boot 2.x، كما هو موضح في [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html). هذه التهيئة تعطيل الخادم المدمج، واستخدام Liberty بدلاً من ذلك.

#### إعداد وتهيئة خادم Websphere Liberty في Eclipse
مع IBM Liberty Developer Tools مثبتًا، قم بإعداد خادم Liberty:

- اذهب إلى Window -> Preferences -> Servers -> Runtime Environments، انقر على "Add"، واختر "WebSphere Application Server Liberty." اتبع السحابة لتحديد تثبيت Liberty الخاص بك، عادةً في مجلد مثل `<Liberty_Root>/wlp`، كما هو موضح في [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9).

- قم بإنشاء خادم جديد عن طريق File -> New -> Other -> Server، واختر "WebSphere Application Server Liberty" وruntime الذي قمت بتهيئته. اسم الخادم وتعديل الإعدادات حسب الحاجة.

- قم بتحرير ملف server.xml للخادم، متاح من خلال عرض Servers، لإضافة الميزات اللازمة. بالنسبة لSpring Boot، أضف:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- ميزات أخرى مثل servlet-3.1 لدعم الويب -->
  </featureManager>
  ```

تضمن هذه التهيئة، المدعومة من [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview)، التوافق مع تطبيقات Spring Boot.

#### نشر وتشغيل التطبيق
لالنشر، انقر بالزر الأيمن على المشروع في Project Explorer، اختر "Run As -> Run on Server"، اختر خادم Liberty الخاص بك، وانقر على Finish. سيقوم Eclipse بنشر ملف WAR إلى خادم Liberty، يمكنك مراقبة السجلات في عرض Console. تأكد من أن سياق التطبيق الجذر هو صحيح في server.xml، عادةً تحت علامات `<webApplication>`، للوصول إلى التطبيق من خلال URL المناسب، مثل `http://localhost:9080/yourapp`.

للتشخيص، استخدم منظور Debug، تعيين نقاط توقف حسب الحاجة، واستغل دعم Liberty للتشخيص عن بُعد، كما هو موضح في [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty).

#### مراعيات إضافية
- **خيارات التغليف**: بينما WAR هو القياسي لخادم Servlet، يدعم Open Liberty أيضًا نشر JAR، كما هو موضح في [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html). بالنسبة لJAR، تأكد من أن التطبيق مهيأ لبدء خادم مدمج، وهذا قد يتطلب ميزات Liberty إضافية أو تهيئات.
- **التكامل مع Maven**: استخدم Maven لإدارة الاعتماديات، تأكد من أن `liberty-maven-plugin` مدمج لتوزيع تلقائي، كما هو موضح في [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin).
- **إصلاح الأخطاء**: إذا حدثت مشاكل، تحقق من سجلات الخادم في مجلد `logs` تحت خادم Liberty الخاص بك، وتأكد من التوافق بين إصدار Liberty وSpring Boot، حيث أن إصدارات مثل Liberty 8.5.5.9 أو أحدث تدعم JAR قابلة للتنفيذ، كما هو موضح في [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application).

تضمن هذه التهيئة الشاملة استخدام Eclipse بشكل فعال لتطوير ونشر تطبيقات Spring Boot على IBM Websphere Liberty، واستخدام Maven لإدارة البناء.

#### جدول: مقارنة خيارات النشر

| نوع النشر | المزايا                                      | العيوب                                      | ملاحظات التهيئة                          |
|------------|---------------------------------------------|---------------------------------------------|----------------------------------------------|
| ملف WAR   | القياسي لخادم Servlet، مدعوم على نطاق واسع | يتطلب توسيع `SpringBootServletInitializer` | قم بإعداد `<packaging>war</packaging>` في pom.xml  |
| ملف JAR   | أبسط للتنمية، مدعوم من Open Liberty       | قد يتطلب ميزات Liberty إضافية           | تأكد من عدم بدء خادم مدمج، استخدم springBoot feature |

يساعد هذا الجدول، المستمد من [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)، في اختيار استراتيجية النشر المناسبة بناءً على احتياجات المشروع.

### الإشارات الرئيسية
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)