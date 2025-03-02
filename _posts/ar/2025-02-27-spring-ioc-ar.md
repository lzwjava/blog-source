---
audio: true
generated: true
lang: ar
layout: post
title: 'Spring IoC (Inversion of Control) Container


  Spring IoC (Inversion of Control) Container'
translated: true
---

أفهم كيف يمكن استخدام Spring IoC (Inversion of Control) Container بطريقة واضحة وممارسات. Spring IoC Container هو قلب Spring Framework، مسؤول عن إدارة دورة حياة وتكوين كائنات التطبيق (المعروفة باسم beans). إنه "ينقل" التحكم من خلال معالجة إنشاء الكائنات و حقن الاعتماديات لك، بدلاً من إنشاءها وربطها يدويًا.

هنا دليل خطوة بخطوة للحصول على البدء:

---

### 1. **فهم الأساسيات**
- **ما يفعله**: IoC Container يخلق، يهيئ، ويدير beans (كائنات التطبيق) بناءً على البيانات التي توفره (من خلال XML، أو تعليقات Java، أو كود Java).
- **مفاهيم رئيسية**:
  - **Beans**: كائنات يديرها الحاوية.
  - **حقن الاعتماديات (DI)**: الحاوية تحقن الاعتماديات (beans أخرى أو قيم) في كائناتك.
  - **التكوين**: تشرح الحاوية ما يجب أن تخلق beans وكيف يجب أن تربطها.

---

### 2. **إعداد مشروعك**
لاستخدام Spring IoC، تحتاج إلى مشروع Spring. إذا كنت تبدأ من الصفر:
- استخدم **Spring Boot** (أسرع طريقة) أو Spring العادي.
- أضف الاعتماديات في ملف `pom.xml` (إذا كنت تستخدم Maven):
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- استخدم أحدث الإصدار -->
  </dependency>
  ```
- بالنسبة لـ Spring Boot، استخدم:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- أحدث الآن -->
  </dependency>
  ```

---

### 3. **تعريف beans**
يمكنك تعريف beans بطرق رئيسية ثلاثة:

#### a) **استخدام التعليقات (الأكثر شيوعًا)**
- أنشئ فئة Java بسيطة و أضف إليها تعليق `@Component` (أو تعليقات متخصصة مثل `@Service`, `@Repository`، إلخ).
- مثال:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **استخدام التكوين Java**
- أنشئ فئة تكوين مع `@Configuration` و حدد beans مع `@Bean`.
- مثال:
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;

  @Configuration
  public class AppConfig {
      @Bean
      public MyService myService() {
          return new MyService();
      }
  }
  ```

#### c) **استخدام XML (طريقة قديمة)**
- حدد beans في ملف XML (مثل `beans.xml`):
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **إطلاق الحاوية IoC**
يجب عليك بدء الحاوية لإدارة beans.

#### a) **مع Spring Boot**
- Spring Boot يفعل ذلك تلقائيًا. فقط أنشئ فئة رئيسية مع `@SpringBootApplication`:
  ```java
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class MyApp {
      public static void main(String[] args) {
          SpringApplication.run(MyApp.class, args);
      }
  }
  ```
- الحاوية تبحث عن فئات `@Component` وتديرها.

#### b) **مع Spring العادي (تكوين تعليقات)**
- استخدم `AnnotationConfigApplicationContext`:
  ```java
  import org.springframework.context.annotation.AnnotationConfigApplicationContext;

  public class Main {
      public static void main(String[] args) {
          AnnotationConfigApplicationContext context =
              new AnnotationConfigApplicationContext(AppConfig.class);
          MyService service = context.getBean(MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

#### c) **مع XML**
- استخدم `ClassPathXmlApplicationContext`:
  ```java
  import org.springframework.context.support.ClassPathXmlApplicationContext;

  public class Main {
      public static void main(String[] args) {
          ClassPathXmlApplicationContext context =
              new ClassPathXmlApplicationContext("beans.xml");
          MyService service = context.getBean("myService", MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

---

### 5. **حقن الاعتماديات**
يمكن للحاوية IoC حقن الاعتماديات في beans.

#### a) **حقن البناء (موصى به)**
```java
@Component
public class MyController {
    private final MyService myService;

    public MyController(MyService myService) {
        this.myService = myService;
    }

    public void execute() {
        myService.doSomething();
    }
}
```

#### b) **حقن المحدد**
```java
@Component
public class MyController {
    private MyService myService;

    @Autowired
    public void setMyService(MyService myService) {
        this.myService = myService;
    }
}
```

#### c) **حقن الحقل (أقل تفضيلًا)**
```java
@Component
public class MyController {
    @Autowired
    private MyService myService;

    public void execute() {
        myService.doSomething();
    }
}
```
- استخدم `@Autowired` (مخصص لـ Spring) أو `@Inject` (معيار JSR-330) لتحديد نقاط الحقن.

---

### 6. **تشغيل واستخدام beans**
- بعد تشغيل الحاوية، تربط beans و اعتمادياتها. يمكنك استرجاع beans باستخدام `context.getBean()` (Spring العادي) أو السماح لـ Spring Boot بإدارة ذلك تلقائيًا عبر الحقن.

مثال مع Spring Boot:
```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(MyApp.class, args);
        MyController controller = context.getBean(MyController.class);
        controller.execute();
    }
}
```

---

### 7. **نصائح إضافية**
- **الأحجام**: بافتراض، beans هي من نوع singleton. استخدم `@Scope("prototype")` للحصول على نسخ جديدة لكل طلب.
- **فحص المكونات**: أضف `@ComponentScan` إلى فئة التكوين إذا كانت beans في حزم مختلفة.
- **الملفات**: استخدم `@Profile` لتفعيل beans في بيئات محددة (مثل "dev", "prod").
- **إغلاق السياق**: في تطبيقات غير Spring Boot، استخدم `context.close()` لتحرير الموارد.

---

هذا هو الجوهر! ابدأ مع Spring Boot و التعليقات من أجل السهولة. إذا كنت متعثرًا في جزء معين - مثل ربط اعتمادية معقدة أو تصحيح - فلا تتردد في السؤال، وسأغوص معك في التفاصيل!