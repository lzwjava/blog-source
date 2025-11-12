---
audio: false
generated: true
lang: ar
layout: post
title: حاوية التحكم العكسي في سبرينغ
translated: true
type: note
---

دعوني أوضح كيفية استخدام حاوية Spring IoC (انعكاس التحكم) بطريقة واضحة وعملية. تُعتبر حاوية Spring IoC هي نواة إطار عمل Spring، وهي مسؤولة عن إدارة دورة الحياة وتهيئة كائنات التطبيق (المسماة beans). إنها "تعكس" التحكم من خلال التعامل مع إنشاء الكائنات وحقن التبعيات نيابة عنك، بدلاً من قيامك بإنشائها وتوصيلها يدويًا.

إليك دليلًا خطوة بخطوة لتبدأ:

---

### 1. **فهم الأساسيات**
- **ما الذي تقوم به**: تقوم حاوية IoC بإنشاء وتهيئة وإدارة beans (كائنات تطبيقك) استنادًا إلى البيانات الوصفية التي تقدمها (عبر XML، أو شروحات Java، أو كود Java).
- **المفاهيم الأساسية**:
  - **Beans**: كائنات تديرها الحاوية.
  - **حقن التبعيات (DI)**: تقوم الحاوية بحقن التبعيات (beans أخرى أو قيم) في كائناتك.
  - **التهيئة**: تخبر الحاوية بأي beans يجب إنشاؤها وكيفية توصيلها.

---

### 2. **إعداد مشروعك**
لاستخدام Spring IoC، تحتاج إلى مشروع Spring. إذا كنت تبدأ من الصفر:
- استخدم **Spring Boot** (أبسط طريقة) أو Spring عادي.
- أضف التبعيات في ملف `pom.xml` الخاص بك (إذا كنت تستخدم Maven):
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- استخدم أحدث إصدار -->
  </dependency>
  ```
- بالنسبة لـ Spring Boot، استخدم:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- الأحدث حتى الآن -->
  </dependency>
  ```

---

### 3. **تحديد الـ Beans الخاصة بك**
يمكنك تحديد beans بثلاث طرق رئيسية:

#### أ) **باستخدام الشروحات (الأكثر شيوعًا)**
- أنشئ فئة Java بسيطة وعلّمها بـ `@Component` (أو شروحات متخصصة مثل `@Service`، `@Repository`، إلخ).
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

#### ب) **باستخدام تهيئة Java**
- أنشئ فئة تهيئة باستخدام `@Configuration` وعرّف beans باستخدام `@Bean`.
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

#### ج) **باستخدام XML (نهج قديم)**
- عرّف beans في ملف XML (مثل `beans.xml`):
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **تهيئة حاوية IoC**
تحتاج إلى بدء تشغيل الحاوية لإدارة beans الخاصة بك.

#### أ) **مع Spring Boot**
- تقوم Spring Boot بهذا تلقائيًا. فقط أنشئ فئة رئيسية بها `@SpringBootApplication`:
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
- تفحص الحاوية فئات `@Component` وتديرها.

#### ب) **مع Spring عادي (قائم على الشروحات)**
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

#### ج) **مع XML**
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

### 5. **حقن التبعيات**
يمكن لحاوية IoC حقن التبعيات في beans الخاصة بك.

#### أ) **حقن عبر المُنشئ (مُوصى به)**
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

#### ب) **حقن عبر setter**
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

#### ج) **حقن عبر الحقل (أقل تفضيلاً)**
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
- استخدم `@Autowired` (خاص بـ Spring) أو `@Inject` (معيار JSR-330) لتحديد نقاط الحقن.

---

### 6. **تشغيل واستخدام الـ Beans**
- بمجرد تشغيل الحاوية، تقوم بتوصيل beans وتبعياتها. يمكنك استرداد beans باستخدام `context.getBean()` (في Spring عادي) أو ترك Spring Boot يتعامل معها تلقائيًا عبر الحقن.

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
- **النطاقات**: بشكل افتراضي، الـ beans هي singleton. استخدم `@Scope("prototype")` للحصول على نسخ جديدة لكل طلب.
- **مسح المكونات**: أضف `@ComponentScan` إلى فئة التهيئة الخاصة بك إذا كانت beans في حزم مختلفة.
- **الملفات الشخصية**: استخدم `@Profile` لتفعيل beans في بيئات محددة (مثل "dev"، "prod").
- **أغلق السياق**: في التطبيقات غير Spring Boot، استدعِ `context.close()` لتحرير الموارد.

---

هذا هو جوهر الأمر! ابدأ بـ Spring Boot والشروحات من أجل البساطة. إذا كنت عالقًا في جزء معين — مثل توصيل تبعية صعبة أو تصحيح الأخطاء — فلا تتردد في السؤال، وسأتعمق معك أكثر!