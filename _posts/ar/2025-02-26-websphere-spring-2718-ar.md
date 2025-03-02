---
audio: false
generated: false
lang: ar
layout: post
title: Spring Boot 2.7.18 في WebSphere Liberty Profile
translated: true
---

عند استخدام Spring Boot 2.7.18 لتوزيع تطبيق على WebSphere Liberty Profile (WLP) كما هو موضح في الدليل المقدم، فإن الأخبار الجيدة هي أن لا يتطلب أي تغييرات على فئة `DemoApplication` أو استخدام `SpringBootServletInitializer`. Spring Boot 2.7.18 هو إصدار تصحيحات ضمن السلسلة 2.7.x، مما يعني أنه يتضمن تصحيحات الأخطاء والتحسينات الصغيرة ولكن لا يقدم تغييرات تدميرية ستؤثر على التكوين القياسي لتوزيع WAR كما هو موضح في الدليل. أدناه، سأشرح لماذا هذا هو الحال وأؤكد أن الإعداد يبقى متوافقًا بالكامل.

---

### فهم الإعداد
يؤكد الدليل على تهيئة تطبيق Spring Boot لتوزيعه كملف WAR على WLP من خلال:

1. **توسيع `SpringBootServletInitializer`:**
   - توسع فئة `DemoApplication` على `SpringBootServletInitializer` لتسهيل التوزيع إلى محول Servlet خارجي مثل WLP. هذه الفئة ضرورية لأن Spring Boot يفضل تشغيله كملف JAR مستقل مع خادم مدمج، ولكن التوزيع إلى WLP يتطلب التكامل مع محول Servlet الخاص به.
   - يتم تجاوز طريقة `configure` لتحديد مصادر التطبيق، مما يضمن أن يبدأ التطبيق بشكل صحيح في المحول الخارجي.

هنا هو الكود من الدليل:
```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

@SpringBootApplication
public class DemoApplication extends SpringBootServletInitializer {

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(DemoApplication.class);
    }

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

2. **تعبئة كملف WAR:**
   - يحدد `pom.xml` `<packaging>war</packaging>` ويحدد `spring-boot-starter-tomcat` ك`<scope>provided</scope>` لتفادي خادم Tomcat المدمج، يعتمد بدلاً من ذلك على محول Servlet الخاص بـ WLP.

3. **التوزيع إلى WLP:**
   - يتم وضع ملف WAR في دليل `dropins` الخاص بـ WLP لتوزيعه تلقائيًا، ويوفر `javaee-8.0` الخاص بـ WLP دعم Servlet 4.0، وهو متوافق مع متطلبات Spring Boot.

---

### لماذا لا يتطلب أي تغييرات مع Spring Boot 2.7.18
Spring Boot 2.7.18 جزء من السلسلة 2.7.x، وتحدث التغييرات الهامة في آليات التوزيع أو واجهات برمجة التطبيقات عادةً بين الإصدارات الرئيسية (مثل 2.x إلى 3.x)، وليس ضمن الإصدارات الفرعية أو التصحيحات. إليك تحليلًا مفصلًا:

#### 1. التوافق مع `SpringBootServletInitializer`
- **الغرض:** `SpringBootServletInitializer` يبقى الطريقة القياسية لتكوين تطبيق Spring Boot لتوزيع WAR في السلسلة 2.x. يوفر التكامل مع المحول الخارجي من خلال تقديم نقطة اتصال لتكوين سياق التطبيق.
- **الاستقرار في 2.7.18:** لا توجد إهمالات أو بدائل لـ `SpringBootServletInitializer` في Spring Boot 2.7.18. تحدث التغييرات الرئيسية مثل الانتقال إلى Jakarta EE (بديل APIs Java EE) في Spring Boot 3.x، والتي تتطلب أيضًا Java 17. نظرًا لأن 2.7.18 يبقى ضمن السلسلة 2.x ويستخدم Java EE، فإن التنفيذ الحالي في `DemoApplication` يبقى صالحًا ومتغيرًا.

#### 2. التوافق مع محول Servlet
- **متطلبات Spring Boot:** يتطلب Spring Boot 2.7.x Servlet 3.1 أو أعلى. يستخدم الدليل WLP مع الميزة `javaee-8.0`، والتي تتضمن Servlet 4.0—معيار أحدث. وهذا يضمن التوافق الكامل.
- **لا يوجد تغيير في 2.7.18:** لا تتغير الإصدارات التصحيحية مثل 2.7.18 التوافق مع Servlet أو تطرح متطلبات جديدة ستؤثر على كيفية تعامل `SpringBootServletInitializer` مع WLP.

#### 3. تكوين التبعية والتعبئة
- **Tomcat ك`provided`:** يحدد الدليل `spring-boot-starter-tomcat` كـ `<scope>provided</scope>` في `pom.xml`، مما يضمن أن يتم استبعاد Tomcat المدمج من ملف WAR. وهذا هو الممارسة القياسية لتوزيع WAR إلى محولات خارجية ويبقى غير متغير في 2.7.18.
- **تكوين Maven:** نوع التعبئة (`war`) وتهيئة التبعية متسقة مع عادات Spring Boot 2.7.x، ولا توجد تحديثات محددة لـ 2.7.18.

#### 4. تفاصيل توزيع WLP
- **دليل dropins:** آلية توزيع `dropins` الخاصة بـ WLP غير متأثرة بإصدار Spring Boot، لأنها تعتمد على بنية ملف WAR ومواصفات Servlet، وكلاهما يبقى متوافقًا.
- **جذر السياق والميناء:** يحدد جذر السياق (مثل `/myapp`) والميناء الافتراضي (مثل `9080`) من قبل WLP واسم ملف WAR، وليس من قبل إصدار Spring Boot، لذا يبقى كلاهما على حاله.

#### 5. الميزات الجديدة أو الإهمالات المحتملة
- **اعتبار ملاحظات الإصدار:** عادةً ما تغطي ملاحظات إصدار Spring Boot 2.7.x (بما في ذلك 2.7.18) تحديثات التبعيات، تصحيحات الأمان، والتحسينات الصغيرة، ولكن لا تؤثر على توزيع WAR أو `SpringBootServletInitializer`. على سبيل المثال، لم يتم تقديم أي علامات أو طرق تهيئة جديدة في 2.7.18 لتحل محل النهج الحالي.
- **المقارنة مع 3.x:** في المقابل، يتخذ Spring Boot 3.x Jakarta EE ويحتاج إلى تعديلات (مثل الفئات الأساسية المختلفة أو APIs Servlet المحدثة)، ولكن 2.7.18 لا يربط إلى هذه التغييرات.

---

### الخاتمة
لم يتم تعديل فئة `DemoApplication` أو استخدام `SpringBootServletInitializer` كما هو موضح في الدليل مع Spring Boot 2.7.18. التكوين متوافق بالكامل مع:

- تعبئة WAR وتوزيعها إلى WLP.
- الميزة `javaee-8.0` في WLP (Servlet 4.0).
- متطلبات Servlet وتوزيع Spring Boot 2.7.x.

يمكنك الاستمرار باستخدام الخطوات والكود من الدليل—استخدام Spring Boot 2.7.18 بدلاً من إصدار 2.7.x العام—وتوقع أن يتم توزيع التطبيق وتشغيله بنجاح على WLP، ويعود "Hello World!" في `http://localhost:9080/myapp/`. لا يتطلب أي تهيئة إضافية أو تغييرات في الخصائص أو تعديل الكود.