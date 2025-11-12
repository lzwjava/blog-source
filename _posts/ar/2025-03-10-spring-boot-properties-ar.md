---
audio: false
generated: true
lang: ar
layout: post
title: كيف تعمل الخصائص في سبرينغ بوت
translated: true
type: note
---

دعنا نستكشف كيف تعمل الخصائص في Spring Boot، بما في ذلك كيفية استخدام ملفات YAML أو `.properties`، وكيفية تجاوزها باستخدام وسائط سطر الأوامر مثل `-D`، والطرق المختلفة لتهيئة الخصائص، وكيفية اختبارها بفعالية.

---

### **كيف تعمل الخصائص في Spring Boot**
يوفر Spring Boot نظامًا مرنًا لإدارة تكوين التطبيق من خلال الخصائص، وهي أزواج مفتاح-قيمة. يمكن تعريف هذه الخصائص في مصادر متعددة، ويقوم Spring Boot بحلها بناءً على ترتيب أولوية محدد. هذا يسمح لك بتخصيص تطبيقك لبيئات أو سيناريوهات نشر مختلفة. يتم تحميل الخصائص إلى **بيئة Spring**، مما يجعلها قابلة للوصول عبر تطبيقك بالكامل.

تشمل المصادر الرئيسية للخصائص:
- ملفات التكوين (مثل `application.properties` أو `application.yml`)
- وسائط سطر الأوامر (مثل `--server.port=8081`)
- خصائص النظام (مثل `-Dserver.port=8081`)
- متغيرات البيئة
- كود Java (عبر `@Value` أو `@ConfigurationProperties`)

---

### **استخدام ملفات YAML أو Properties**
يدعم Spring Boot تنسيقين أساسيين لملفات التكوين، يوضع كلاهما عادةً في `src/main/resources`:

#### **1. ملفات `.properties`**
هذا تنسيق بسيط من نوع مفتاح-قيمة:
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. ملفات `.yml` أو `.yaml`**
هذا تنسيق هيكلي متداخل يستخدم المسافات البادئة:
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**النقاط الرئيسية:**
- استخدم `.properties` للتكوينات البسيطة و `.yml` للإعدادات المتداخلة أو المعقدة.
- يمكن استخدام الملفات الخاصة بالبروفايل (مثل `application-dev.yml`) للإعدادات الخاصة بالبيئة.
- مثال: ضبط `server.port=8080` يغير المنفذ الذي يعمل عليه تطبيق Spring Boot الخاص بك.

---

### **استخدام وسائط سطر الأوامر لتجاوز الخصائص**
يمكنك تجاوز الخصائص المعرفة في ملفات التكوين باستخدام وسائط سطر الأوامر بطريقتين:

#### **1. استخدام `--` لخصائص Spring Boot**
مرر الخصائص مباشرة عند تشغيل التطبيق:
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
هذه تأخذ الأسبقية على ملفات التكوين.

#### **2. استخدام `-D` لخصائص النظام**
عيّن خصائص النظام باستخدام `-D`، والتي يتعرف عليها Spring Boot أيضًا:
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
خصائص النظام تتجاوز قيم ملفات التكوين أيضًا.

---

### **الطرق المختلفة لتهيئة الخصائص**
يقدم Spring Boot عدة طرق لتعريف أو تهيئة الخصائص تتجاوز المفاتيح ووسائط سطر الأوامر:

#### **1. متغيرات البيئة**
يمكن ضبط الخصائص عبر متغيرات البيئة. على سبيل المثال:
- عيّن `SERVER_PORT=8081` في بيئتك، وسيقوم Spring Boot بتعيينها إلى `server.port`.
- **اتفاقية التسمية:** تحويل أسماء الخصائص إلى أحرف كبيرة واستبدال النقاط (`.`) بشرطات سفلية (`_`)، مثال: `spring.datasource.url` تصبح `SPRING_DATASOURCE_URL`.

#### **2. كود Java**
يمكنك تهيئة الخصائص برمجيًا:
- **باستخدام `@Value`**: حقن خاصية محددة في حقل.
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **باستخدام `@ConfigurationProperties`**: ربط مجموعة من الخصائص بكائن Java.
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters and setters
  }
  ```
  هذا يربط خصائص مثل `app.name` بالحقل `name`.

#### **3. القيم الافتراضية**
وفر قيمًا احتياطية إذا لم يتم تعريف الخاصية:
- في `@Value`: `@Value("${server.port:8080}")` تستخدم `8080` إذا لم يتم تعيين `server.port`.
- في ملفات التكوين: عيّن القيم الافتراضية في `application.properties` أو YAML.

---

### **أولوية الخصائص**
يحل Spring Boot الخصائص من مصادر متعددة بهذا الترتيب (الأولوية الأعلى تتجاوز الأدنى):
1. وسائط سطر الأوامر (`--property=value`)
2. خصائص النظام (`-Dproperty=value`)
3. متغيرات البيئة
4. ملفات التكوين (`application.properties` أو `application.yml`)
5. القيم الافتراضية في الكود

**مثال:** إذا كان `server.port=8080` موجودًا في `application.properties` ولكنك قمت بتشغيل `java -jar myapp.jar --server.port=8081`، فسيكون المنفذ `8081`.

---

### **كيفية اختبار الخصائص**
يضمن اختبار الخصائص أن تطبيقك يعمل كما هو متوقع. إليك النهج الشائعة:

#### **1. استخدام `@TestPropertySource`**
تجاوز الخصائص في اختبارات الوحدة:
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // Test code
}
```

#### **2. استخدام `application-test.properties`**
ضع ملفًا مخصصًا للاختبار في `src/test/resources`:
```properties
server.port=9090
```
يقوم Spring Boot بتحميل هذا تلقائيًا أثناء الاختبارات.

#### **3. التجاوزات البرمجية**
عيّن الخصائص في إعداد الاختبار:
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. استخدام `@ActiveProfiles`**
تفعيل الخصائص المحددة للبروفايل:
- عرّف `application-test.yml` بإعدادات الاختبار.
- استخدم:
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // Test code
  }
  ```

---

### **الخلاصة**
- **ملفات التكوين**: استخدم `application.properties` أو `application.yml` للإعدادات الافتراضية.
- **وسائط سطر الأوامر**: تجاوز باستخدام `--property=value` أو `-Dproperty=value`.
- **طرق التهيئة**: استفد من متغيرات البيئة، كود Java (`@Value`, `@ConfigurationProperties`)، أو القيم الافتراضية.
- **الاختبار**: استخدم `@TestPropertySource`، أو ملفات مخصصة للاختبار، أو تجاوزات برمجية، أو بروفايلات.

هذا يغطي الأساسيات للعمل مع الخصائص في Spring Boot. دعني أعلم إذا كنت تريد المزيد من التفاصيل!