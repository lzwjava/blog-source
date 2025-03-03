---
audio: false
lang: ar
layout: post
title: استثناء تخزين تعريف الفاصوليا
translated: true
---

على أساس الخطأ الذي قدمته، فإن تطبيق Java الخاص بك الذي يعمل على IBM WebSphere مع دعم OSGi يواجه استثناء `BeanDefinitionStoreException` أثناء عملية التهيئة للمفاهيم التطبيقية Spring Framework. يشير هذا الاستثناء إلى "تعريف Bean غير صالح" والذي عادة ما ينشأ من خطأ في تكوين Spring الخاص بك. أدناه دليل شامل لتشخيص وإصلاح المشكلة.

---

## فهم المشكلة
يظهر الخطأ:
- **استثناء**: `org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition`
- **المكونات الرئيسية**: ذكر `PlaceholderConfigurerSupport` و `PropertySourcesPlaceholderConfigurer` و `AbstractApplicationContext` في مسار الاستثناء.
- **السياق**: يحدث الفشل أثناء عملية `refresh` للمفاهيم التطبيقية Spring، والتي يتم تنشيطها بواسطة `ContextLoader` في بيئة تطبيق ويب على WebSphere.
- **سبب الجذر**: ربما يكون مرتبطًا بمحددات مكانة غير محلولة، أو تعريفات Bean غير صالحة، أو مشاكل محددة بالتنصيب في بيئة WebSphere/OSGi.

هذا يشير إلى أن Spring لا يمكن أن يحدد أو يهيئ Bean أو أكثر بسبب أخطاء في التكوين. دعونا نحل هذا خطوة بخطوة.

---

## حل خطوة بخطوة

### 1. التحقق من محددات المكانة
**لماذا**: يشير مسار الاستثناء إلى `PlaceholderConfigurerSupport` و `PropertySourcesPlaceholderConfigurer`، والتي تتعامل مع حل المحددات. إذا استخدم تعريف Bean محددًا مثل `${admin.email}` ولم يتم تعريفه، فسيفشل Spring.

**كيفية إصلاح**:
- **تحديد ملفات المحددات**: تأكد من أن ملف `application.properties` أو `application.yml` موجود في مسار التصنيف (على سبيل المثال، `src/main/resources`).
- **تحقق من المحددات**: افتح الملف وتأكد من أن جميع المحددات التي يتم استدعاؤها في تعريفات Bean تم تعريفها. على سبيل المثال:
  ```properties
  admin.email=admin@example.com
  ```
- **إصلاح الأخطاء**: ابحث عن أخطاء في أسماء المحددات أو مسارات الملفات.
- **إعداد التكوين**:
  - **XML**: إذا كنت تستخدم XML، تأكد من علامة `<context:property-placeholder>`:
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **تكوين Java**: إذا كنت تستخدم `@Configuration`، تأكد من أن `PropertySourcesPlaceholderConfigurer` تم تهيئته:
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. فحص تعريفات Bean
**لماذا**: يشير "تعريف Bean غير صالح" إلى مشكلة في كيفية تعريف Bean في تهيئة Spring الخاصة بك.

**كيفية إصلاح**:
- **تكوين XML**:
  - افتح ملف Spring XML الخاص بك (على سبيل المثال، `applicationContext.xml`) وتحقق من:
    - IDs و أسماء الفئات صحيحة وموجودة في مسار التصنيف.
    - الخصائص صالحة وتطابق طرق الإعداد أو المعلمات المحددات.
    - مثال على Bean صحيح:
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - استخدم IDE للتحقق من صحة XML و المخطط.
- **تكوين Java**:
  - تحقق من فئات `@Configuration` لأدوات `@Bean`:
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - تأكد من أن أنواع العودة وأسماء الطرق صحيحة.
- **فحص المكونات**:
  - إذا كنت تستخدم `@Component`، `@Service`، إلخ، تأكد من أن الحزمة الأساسية تم فحصها:
    ```java
    @ComponentScan("com.example")
    ```

### 3. حل التبعيات الدائرية
**لماذا**: إذا كان Beanان يعتمدان على بعضهما البعض (على سبيل المثال، يحتاج Bean A إلى Bean B، ويحتاج Bean B إلى Bean A)، فربما يفشل Spring في تهيئتهما.

**كيفية إصلاح**:
- **استخدام `@Lazy`**:
  - أضف علامة `@Lazy` إلى أحد التبعيات لتأخير تهيئتها:
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **إعادة تصميم**: إعادة تصميم Bean الخاصة بك لتجنب التبعيات الدائرية إذا كان ذلك ممكنًا.

### 4. التحقق من التبعيات و مسار التصنيف
**لماذا**: يمكن أن يسبب مكتبات مفقودة أو غير متوافقة أن تكون الفئات التي يتم استدعاؤها في تعريفات Bean غير متاحة.

**كيفية إصلاح**:
- **Maven/Gradle**:
  - تأكد من أن جميع التبعيات المطلوبة من Spring موجودة في `pom.xml` (Maven) أو `build.gradle` (Gradle). مثال لمافن:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - قم بتشغيل `mvn dependency:tree` أو `gradle dependencies` للتحقق من التعارضات.
- **مسار التصنيف**: تأكد من أن جميع الفئات (على سبيل المثال، `com.example.MyClass`) تم تجميعها وتوفر في التطبيق الموزع.

### 5. تمكين تسجيلات التشفير
**لماذا**: يمكن أن يحدد سجلات أكثر تفصيلاً تحديد Bean أو المحددات التي تسبب الفشل.

**كيفية إصلاح**:
- أضف إلى `application.properties`:
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- أعيد تشغيل التطبيق وتفحص السجلات للحصول على أخطاء محددة حول إنشاء Bean أو حل المحددات.

### 6. التحقق من تهيئة WebSphere/OSGi
**لماذا**: يشير مسار الاستثناء إلى مكونات WebSphere و OSGi، والتي قد تجلب مشاكل محددة بالتنصيب.

**كيفية إصلاح**:
- **حل الحزم**: تأكد من أن جميع حزم OSGi تم نشرها بشكل صحيح و تم حل تبعياتها في WebSphere.
- **مسار التصنيف**: تأكد من أن ClassLoader WebSphere يتضمن JARs و ملفات المحددات للتطبيق الخاص بك.
- **سجلات الخادم**: تحقق من سجلات WebSphere (على سبيل المثال، `SystemOut.log`) للحصول على أخطاء أو تحذيرات إضافية.

### 7. مراجعة السجلات السابقة
**لماذا**: يبدأ مقطع السجل بنجاح تحميل المحددات في 10:15:57، ولكن يحدث الخطأ في 16:56:57. قد يكون قد تسبب في الفشل.

**كيفية إصلاح**:
- انزل في ملف السجل أو تحقق من السجلات المأرشفة للحصول على تحذيرات أو أخطاء قبل `BeanDefinitionStoreException`.

---

## حالات شائعة وحلول
- **محدد غير محلول**:
  - **المشكلة**: `${admin.email}` في تعريف Bean، ولكن ليس في `application.properties`.
  - **الحل**: أضف `admin.email=somevalue` إلى الملف.
- **فئة مفقودة**:
  - **المشكلة**: `<bean class="com.example.NonExistentClass">`
  - **الحل**: تصحيح اسم الفئة أو إضافة التبعية المفقودة.
- **خطأ في النطق**:
  - **المشكلة**: XML أو تهيئة Java غير صحيحة.
  - **الحل**: التحقق باستخدام IDE أو أداة مثل `xmllint` لـ XML.

---

## الخطوات النهائية
1. **تطبيق الحلول**: ابدأ بمحددات المكانة و تعريفات Bean، حيث أنها الأكثر احتمالًا للسبب بناءً على مسار الاستثناء.
2. **اختبار محليًا**: إعادة نشر وتجربة في بيئة التطوير الخاصة بك.
3. **نشر إلى WebSphere**: إذا كان يعمل محليًا، أعيد نشره إلى WebSphere و راقب السجلات.
4. **تكرار**: إذا استمر الخطأ، استخدم سجلات التشفير لتحديد Bean أو المحددات الفاشلة.

بمتابعة هذه الخطوات، يجب أن تحل `BeanDefinitionStoreException` وتتم تهيئة مفاهيم Spring الخاصة بك بنجاح. إذا استمر المشكلة، قم بتقديم تفاصيل أكثر تحديدًا (على سبيل المثال، ملفات التهيئة أو السجلات الكاملة) للحصول على مساعدة إضافية.