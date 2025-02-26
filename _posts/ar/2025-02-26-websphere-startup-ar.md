---
audio: true
lang: ar
layout: post
title: مشاكل بدء تشغيل التطبيقات في WebSphere Liberty Profile
translated: true
---

يبدو أن بعد تخفيض تطبيق Spring Boot الخاص بك إلى الإصدار 2.7.18 وتنزيله إلى WebSphere Liberty Profile (WLP)، أنت تواجه مشكلة حيث لا يبدأ التطبيق في الوقت المحدد الافتراضي، كما هو موضح في الرسالة في `console.log`: *"لم يبدأ التطبيق myapp في 30.xx ثانية"*. وهذا يشير إلى أن التطبيق إما يأخذ وقتًا طويلًا في التهيئة أو فشل في البدء بشكل كامل. أدناه، سأرشدك عبر عملية تشخيصية خطوة بخطوة لتحليل وإصلاح هذه المشكلة.

---

### الخطوة 1: استقصاء سجلات الخادم للحصول على أدلة
الشيء الأول الذي يجب فعله هو فحص سجلات الخادم بشكل أكثر تفصيلاً لتحديد سبب فشل البدء. ملف `console.log` يوفر رسالة الإنتظار، ولكن قد لا يحتوي على القصة الكاملة. تحقق من الملفات السجلية التالية في دليل سجلات خادم WLP الخاص بك (`/opt/ibm/wlp/usr/servers/myServer/logs/`):

- **`messages.log`**: هذا الملف يحتوي غالبًا على رسائل خطأ أو تحذير يمكن أن يشير إلى مشاكل مثل الاعتماديات المفقودة، أخطاء التكوين، أو الاستثناءات أثناء البدء.
- **`trace.log`**: إذا تم تمكين تتبع تفصيلي، قد يحتوي هذا الملف على مزيد من السياق حول ما يحدث أثناء التنزيل.

ابحث عن:
- مسارات الاستثناءات أو الاستثناءات (مثل `ClassNotFoundException`, `NoSuchBeanDefinitionException`).
- رسائل عن الموارد المفقودة أو المكتبات غير المتوافق.
- إشارات إلى فشل تهيئة سياق التطبيق.

إذا لم ترَ تفاصيل كافية، يمكنك زيادة مستوى السجل في WLP من خلال تعديل ملف `server.xml`. أضف أو تحديث العنصر `<logging>` كما يلي:

```xml
<logging traceSpecification="*=info:com.ibm.ws.webcontainer*=all" />
```

أعد تشغيل الخادم بعد إجراء هذه التغييرات، واعد تنزيل التطبيق، واكتب السجلات مرة أخرى للحصول على مزيد من المعلومات.

---

### الخطوة 2: التحقق من بدء التطبيق مع السجل
بسبب أن هذا هو تطبيق Spring Boot، قد تكون المشكلة مرتبطة بفشل تهيئة سياق التطبيق. لتحديد إلى أي مدى وصل عملية البدء، أضف بيان سجل بسيط إلى فئة التطبيق الرئيسية باستخدام طريقة `@PostConstruct`. إليك مثال:

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import javax.annotation.PostConstruct;

@SpringBootApplication
public class DemoApplication extends SpringBootServletInitializer {

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(DemoApplication.class);
    }

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @PostConstruct
    public void init() {
        System.out.println("تم تهيئة سياق التطبيق");
    }
}
```

- أعيد بناء التطبيق (`mvn clean package`).
- أعيد تنزيل ملف WAR إلى دليل `dropins` في WLP.
- تحقق من `console.log` للحصول على الرسالة `"تم تهيئة سياق التطبيق"`.

إذا ظهرت هذه الرسالة، فإن سياق التطبيق يتم تحميله بنجاح، ويمكن أن تكون المشكلة مرتبطة مع مكونات الويب أو تهيئة الخادم. إذا لم تظهر، فإن المشكلة تحدث في وقت مبكر أثناء تهيئة السياق.

---

### الخطوة 3: تمكين السجل التوضيحي في Spring Boot
لحصول على رؤية أفضل لعملية البدء في Spring Boot، تمكين السجل التوضيحي من خلال إضافة ملف التكوين. قم بإنشاء أو تعديل `src/main/resources/application.properties` مع التالي:

```properties
debug=true
```

- أعيد بناء وتنزيل التطبيق.
- تحقق من `console.log` (أو سجلات أخرى) للحصول على إخراج توضيحي مفصل من Spring Boot.

سيسجل هذا المعلومات عن إنشاء البينات، التهيئة التلقائية، وأي أخطاء تحدث أثناء البدء. ابحث عن أدلة حول ما قد يكون متوقفًا أو فشل.

---

### الخطوة 4: التحقق من ملف WAR وتهيئة الاعتماديات
بسبب أنك تنزيل إلى WLP، الذي يوفر خادم Servlet الخاص به، تأكد من أن ملف WAR مهيأ بشكل صحيح لخدمة خارجية:

- **تعبئة WAR**: في ملف `pom.xml` الخاص بك، تأكد من أن التعبئة مخصصة إلى `war`:

```xml
<packaging>war</packaging>
```

- **Tomcat كمتوفر**: تأكد من أن Tomcat المضمن تم استبعاده من ملف WAR، حيث سيوفر WLP خادم Servlet. تحقق من ملف `pom.xml` الخاص بك للحصول على:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-tomcat</artifactId>
    <scope>provided</scope>
</dependency>
```

- **التوافق مع API Servlet**: يستخدم Spring Boot 2.7.18 `javax.servlet:javax.servlet-api:4.0.1`، وهو متوافق مع ميزة `javaee-8.0` في WLP (Servlet 4.0). للتحقق من عدم وجود اعتماديات متعارضة، قم بإطلاق:

```bash
mvn dependency:tree
```

ابحث عن أي إصدارات API Servlet غير متوقعة (مثل `jakarta.servlet-api`، التي تستخدم في Spring Boot 3.x وغير متوافق مع `javaee-8.0`).

إذا كنت تعتقد أن هناك مشاكل في الاعتماديات، فكك ملف WAR واكتب `WEB-INF/lib` للتحقق من عدم وجود JARات Servlet غير متوقعة.

---

### الخطوة 5: اختبار محلي لإزالة المشكلة
لتحديد إذا كانت المشكلة محددة لـ WLP أو التطبيق نفسه، اختبر التطبيق محليًا باستخدام Tomcat المضمن:

```bash
mvn spring-boot:run
```

إذا بدأ بنجاح وتتمكن من الوصول إلى نقاط النهاية الخاصة بك (مثل خادم REST بسيط `"Hello World!"`), فإن المشكلة قد تكون مرتبطة بتنزيل WLP بدلاً من كود التطبيق.

---

### الخطوة 6: تعديل وقت انتظار البدء في WLP (حل مؤقت)
إذا أشارت السجلات إلى أن التطبيق يبدأ ولكن يأخذ وقتًا أطول من 30 ثانية، يمكنك زيادة وقت انتظار البدء في ملف `server.xml` في WLP:

```xml
<applicationMonitor startTimeout="60s" />
```

- أعيد تنزيل التطبيق واكتب السجلات.
- إذا بدأ بعد الوقت المحدد المتأخر، فهذا يؤكد عملية البدء البطيئة، ويجب عليك تحسين التطبيق (مثل تقليل مسح المكونات أو مهام التهيئة).

لكن هذا هو حل مؤقت - في الواقع، يجب أن يبدأ تطبيق بسيط في غضون 30 ثانية، لذا استمر في التحقيق في السبب الجذر.

---

### الخطوة 7: تبسيط وتقارن مع مشروع جديد
إذا استمرت المشكلة، قم بإنشاء مشروع Spring Boot 2.7.18 بسيط لتجربة التنزيل على WLP:
1. استخدم [Spring Initializr](https://start.spring.io/) مع:
   - Spring Boot 2.7.18
   - Java (مطابق لنسخة WLP الخاصة بك، مثل 8 أو 11)
   - الاعتمادية: Spring Web
2. أضف خادم REST أساسي:

```java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/")
    public String hello() {
        return "Hello World!";
    }
}
```

3. قم بتكوينه لتنزيل WAR (توسيع `SpringBootServletInitializer` كما هو موضح سابقًا).
4. قم بإنشاء ملف WAR (`mvn clean package`) واكتبه إلى دليل `dropins` في WLP.

إذا بدأ هذا المشروع الجديد بنجاح، قم بمقارنة ملف `pom.xml` الخاص بك، فئة الرئيسية، والتكوين مع المشروع الأصلي لتحديد الاختلافات التي تسبب الفشل.

---

### الخطوة 8: تشخيص إضافي لـ WLP
إذا لم يحل أي من ما سبق المشكلة، اعتبر هذه الفحوصات الخاصة بـ WLP:
- **تنظيف الدليل العمل**: قم بإزالة البيانات المخزنة التي قد تتداخل مع التنزيل:
  ```bash
  rm -rf /opt/ibm/wlp/usr/servers/myServer/workarea
  ```
  ثم أعيد تشغيل الخادم واكتب التطبيق مرة أخرى.
- **تحقق من إصدار WLP**: قم بإطلاق `/opt/ibm/wlp/bin/productInfo version` للتحقق من أن إصدار WLP الخاص بك يدعم تنزيلات Spring Boot 2.7.x مع `javaee-8.0`.
- **إصدار Java**: تأكد من أن إصدار Java المستخدم من قبل WLP (تحقق باستخدام `java -version` في بيئة WLP) مطابق لنسخة يدعمها Spring Boot 2.7.18 (Java 8، 11، أو 17).

---

### الحل الموصى به
بناء على المعلومات المقدمة، فإن المشكلة الأكثر احتمالًا هي مشكلة أثناء تهيئة سياق التطبيق أو خلل بسيط في التكوين مع WLP. إليك كيفية إصلاحها:

1. **ابدأ مع السجل**:
   - أضف السجل `@PostConstruct` (الخطوة 2) وتمكين `debug=true` (الخطوة 3).
   - أعيد تنزيل واكتب `console.log` و`messages.log` للحصول على أخطاء أو أين يتوقف البدء.

2. **تحقق من التكوين**:
   - تأكد من إعداد ملف WAR و الاعتماديات (الخطوة 4).
   - اختبر محليًا (الخطوة 5) لإزالة المشاكل على مستوى التطبيق.

3. **تكرار وتبسيط**:
   - إذا لزم الأمر، اختبر مشروعًا بسيطًا (الخطوة 7) لإزالة المشكلة.

بمتابعة هذه الخطوات، يجب أن تكون قادرًا على تحديد السبب - سواء كان خلل في الاعتماديات، مكون بطيء البدء، أو مشكلة في تهيئة WLP - وإصلاحه وفقًا لذلك. إذا كنت لا تزال تواجه صعوبات، شارك رسائل الخطأ المحددة من السجلات للحصول على مساعدة إضافية!