---
audio: false
generated: true
lang: ar
layout: post
title: استخدام إكلبس
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المحتمل أن Eclipse يمكن استخدامه بفعالية مع IBM Websphere Liberty وSpring وSpring Boot وMaven، لكن الإعداد يتطلب تكوينات محددة.
- تشير الأبحاث إلى تثبيت Spring Tool Suite (STS) وأدوات مطوري IBM Liberty كإضافات في Eclipse لتعزيز الوظائف.
- تميل الأدلة نحو إنشاء مشروع Spring Boot باستخدام STS أو Spring Initializr، ثم تكوينه لنشر Websphere Liberty.

### إعداد Eclipse
للبدء، قم بتنزيل وتثبيت "Eclipse IDE for Enterprise Java and Web Developers" من [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers). تأكد من تثبيت JDK 17 أو إصدار أحدث، يمكنك التحقق من ذلك بتشغيل الأمر `java -version` في الطرفية.

### التكوين لـ Spring وSpring Boot
قم بتثبيت إضافة Spring Tool Suite (STS) بالذهاب إلى Help -> Eclipse Marketplace في Eclipse، والبحث عن "Spring Tools"، وتثبيت الإصدار المناسب. هذا يعزز تطوير Spring وSpring Boot. يمكنك إنشاء مشروع Spring Boot جديد مباشرة في Eclipse عبر File -> New -> Spring Starter Project، واختيار Maven كأداة بناء وإضافة التبعيات الضرورية مثل Spring Web.

### التكامل مع IBM Websphere Liberty
قم بتثبيت أدوات مطوري IBM Liberty من سوق Eclipse بالبحث عن "IBM Liberty Developer Tools" ومتابعة إرشادات التثبيت. قم بإعداد خادم Websphere Liberty بالذهاب إلى Window -> Preferences -> Servers -> Runtime Environments، وإضافة وقت تشغيل Websphere Liberty جديد، وإنشاء مثيل خادم عبر File -> New -> Other -> Server. تأكد من أن server.xml الخاص بالخادم يتضمن `<feature>springBoot-2.0</feature>` لدعم Spring Boot، كما هو مفصل في [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html).

### نشر تطبيقك
قم بتعديل تطبيق Spring Boot الخاص بك ليمتد `SpringBootServletInitializer` بدلاً من استخدام دالة main التي تبدأ خادمًا مضمنًا، وتعبئته كملف WAR عن طريق تعيين `<packaging>war</packaging>` في ملف pom.xml الخاص بك. انشر بالنقر بزر الماوس الأيمن على المشروع، واختيار "Run As -> Run on Server"، واختيار خادم Liberty الخاص بك. هذا يضمن تشغيل التطبيق على حاوية الويب الخاصة بـ Liberty.

---

### ملاحظة المسح: دليل شامل لاستخدام Eclipse مع IBM Websphere Liberty وSpring وSpring Boot وMaven

يقدم هذا الدليل شرحًا تفصيليًا لاستخدام Eclipse بشكل فعال مع IBM Websphere Liberty وSpring وSpring Boot وMaven، مصممًا للمطورين العاملين في هذه النظم البيئية. تتضمن العملية إعداد Eclipse، وتثبيت الإضافات الضرورية، وإنشاء وتكوين المشاريع، ونشر التطبيقات، مع التركيز على التكامل وأفضل الممارسات اعتبارًا من 27 فبراير 2025.

#### إعداد Eclipse والمتطلبات الأساسية
يخدم Eclipse كبيئة تطوير متكاملة قوية لتطوير Java، خاصة للتطبيقات المؤسسية. لهذا الإعداد، قم بتنزيل إصدار "Eclipse IDE for Enterprise Java and Web Developers" 2024-06، المتوفر على [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers). تأكد من أن نظامك يحتوي على JDK 17 أو إصدار أحدث، يمكنك التحقق من ذلك بتشغيل الأمر `java -version` في الطرفية. يضمن هذا الإصدار التوافق مع ميزات Spring وLiberty الحديثة.

#### تثبيت الإضافات الأساسية
لتعزيز Eclipse لتطوير Spring وSpring Boot، قم بتثبيت Spring Tool Suite (STS)، الجيل التالي من أدوات Spring. يمكن الوصول إلى هذا عبر Help -> Eclipse Marketplace، والبحث عن "Spring Tools"، وتثبيت الإدخال المسمى "Spring Tools (aka Spring IDE and Spring Tool Suite)". توفر هذه الإضافة، الموضحة في [Spring Tools](https://spring.io/tools/)، دعمًا من الطراز العالمي للتطبيقات القائمة على Spring، متكاملة بسلاسة مع Eclipse لميزات مثل إنشاء المشاريع وتصحيح الأخطاء.

للتكامل مع IBM Websphere Liberty، قم بتثبيت أدوات مطوري IBM Liberty، المتاحة أيضًا عبر سوق Eclipse بالبحث عن "IBM Liberty Developer Tools". هذه الإضافة، المختبرة لـ Eclipse 2024-06 كما هو مذكور في [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)، تسهل بناء ونشر تطبيقات Java EE إلى Liberty، مع دعم للإصدارات التي تعود إلى 2019-12.

#### إنشاء مشروع Spring Boot
هناك طريقتان رئيسيتان لإنشاء مشروع Spring Boot في Eclipse مع تثبيت STS:

1. **استخدام Spring Initializr**: قم بزيارة [Spring Initializr](https://start.spring.io/)، واختر Maven كأداة بناء، واختر بيانات وصف المشروع (Group, Artifact، إلخ)، وأضف التبعيات مثل Spring Web. قم بإنشاء المشروع كملف ZIP، واستخرجه، واستورده إلى Eclipse عبر File -> Import -> Existing Maven Project، واختر المجلد المستخرج.

2. **استخدام STS مباشرة**: افتح Eclipse، واذهب إلى File -> New -> Other، وقم بتوسيع Spring Boot، واختر "Spring Starter Project". اتبع المعالج، مع التأكد من اختيار Maven كنوع، واختر التبعيات. هذه الطريقة، كما هو موضح في [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)، مفضلة لتكاملها مع مساحة عمل Eclipse.

تضمن كلتا الطريقتين مشروعًا قائمًا على Maven، وهو أمر بالغ الأهمية لإدارة التبعيات مع Spring Boot.

#### التكوين لنشر Websphere Liberty
للتوزيع على Websphere Liberty، قم بتعديل تطبيق Spring Boot الخاص بك ليعمل على حاوية الويب الخاصة بـ Liberty بدلاً من بدء خادم مضمن. يتضمن هذا:

- التأكد من أن الفئة الرئيسية للتطبيق تمتد `SpringBootServletInitializer`. على سبيل المثال:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // No main method; Liberty handles startup
  }
  ```

- تحديث ملف pom.xml للتعبئة كملف WAR عن طريق إضافة:

  ```xml
  <packaging>war</packaging>
  ```

  هذا ضروري للتوزيع التقليدي لحاوية الخدمات، كما هو مذكور في [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet).

يدعم Websphere Liberty، خاصة المتغير مفتوح المصدر Open Liberty، تطبيقات Spring Boot بميزات محددة. تأكد من أن server.xml الخاص بخادم Liberty يتضمن `<feature>springBoot-2.0</feature>` لدعم Spring Boot 2.x، كما هو مفصل في [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html). يقوم هذا التكوين بتعطيل حاوية الويب المضمنة، والاستفادة من حاوية Liberty بدلاً من ذلك.

#### إعداد وتكوين خادم Websphere Liberty في Eclipse
مع تثبيت أدوات مطوري IBM Liberty، قم بإعداد خادم Liberty:

- انتقل إلى Window -> Preferences -> Servers -> Runtime Environments، انقر على "Add"، واختر "WebSphere Application Server Liberty". اتبع المعالج لتحديد موقع تثبيت Liberty الخاص بك، عادةً في دليل مثل `<Liberty_Root>/wlp`، كما هو مذكور في [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9).

- أنشئ مثيل خادم جديد عبر File -> New -> Other -> Server، واختر "WebSphere Application Server Liberty" ووقت التشغيل الذي قمت بتكوينه. اسم الخادم وضبط الإعدادات حسب الحاجة.

- حرر server.xml الخاص بالخادم، الذي يمكن الوصول إليه من خلال عرض Servers، لتضمين الميزات الضرورية. لـ Spring Boot، أضف:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- Other features like servlet-3.1 for web support -->
  </featureManager>
  ```

يضمن هذا الإعداد، المدعوم من [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview)، التوافق مع تطبيقات Spring Boot.

#### نشر وتشغيل التطبيق
للتوزيع، انقر بزر الماوس الأيمن على مشروعك في Project Explorer، واختر "Run As -> Run on Server"، واختر خادم Liberty الخاص بك، وانقر على Finish. سيقوم Eclipse بتوزيع ملف WAR إلى خادم Liberty، ويمكنك مراقبة السجلات في عرض Console. تأكد من تعيين جذر سياق التطبيق بشكل صحيح في server.xml، عادةً تحت علامات `<webApplication>`، للوصول إلى تطبيقك عبر عنوان URL المناسب، على سبيل المثال `http://localhost:9080/yourapp`.

لتصحيح الأخطاء، استخدم منظور Debug، وضع نقاط التوقف حسب الحاجة، مستفيدًا من دعم Liberty للتصحيح عن بُعد، كما نوقش في [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty).

#### اعتبارات إضافية
- **خيارات التعبئة**: بينما يعتبر WAR معياريًا لحاويات الخدمات، يدعم Open Liberty أيضًا توزيعات JAR، كما هو موضح في [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html). بالنسبة لـ JAR، تأكد من تكوين التطبيق لعدم بدء خادم مضمن، مما قد يتطلب ميزات أو تكوينات إضافية لـ Liberty.
- **تكامل Maven**: استخدم Maven لإدارة التبعيات، مع التأكد من تضمين `liberty-maven-plugin` للتوزيع الآلي، كما هو مذكور في [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin).
- **استكشاف الأخطاء وإصلاحها**: إذا ظهرت مشاكل، تحقق من سجلات الخادم في الدليل `logs` تحت مثيل خادم Liberty الخاص بك، وتأكد من التوافق بين إصدار Liberty وSpring Boot، حيث تدعم إصدارات مثل Liberty 8.5.5.9 أو أعلى ملفات JAR القابلة للتشغيل، وفقًا [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application).

يضمن هذا الإعداد الشامل الاستخدام الفعال لـ Eclipse لتطوير وتوزيع تطبيقات Spring Boot على IBM Websphere Liberty، مستفيدًا من Maven لإدارة البناء.

#### جدول: مقارنة خيارات النشر

| نوع النشر       | الإيجابيات                                  | السلبيات                                  | ملاحظات التكوين                           |
|-----------------|---------------------------------------------|-------------------------------------------|--------------------------------------------|
| ملف WAR         | معياري لحاويات الخدمات، مدعوم على نطاق واسع | يتطلب تمديد `SpringBootServletInitializer` | عيّن `<packaging>war</packaging>` في pom.xml |
| ملف JAR         | أبسط للتطوير، مدعوم من Open Liberty         | قد يتطلب ميزات إضافية لـ Liberty          | تأكد من عدم بدء خادم مضمن، استخدم ميزة springBoot |

يساعد هذا الجدول، المستمد من [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)، في اختيار استراتيجية النشر المناسبة بناءً على احتياجات المشروع.

### الاقتباسات الرئيسية
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)