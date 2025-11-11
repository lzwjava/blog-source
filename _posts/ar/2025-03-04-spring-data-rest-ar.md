---
audio: false
generated: true
lang: ar
layout: post
title: مودول Spring Data REST
translated: true
type: note
---

لاستخدام **spring-data-rest-core**، يمكنك الاستفادة من وحدة Spring Data REST لعرض مستودعات Spring Data الخاصة بك كنقاط نهاية RESTful في تطبيقك. فيما يلي دليل كامل خطوة بخطوة لمساعدتك على البدء:

---

### 1. إضافة تبعية Spring Data REST
لاستخدام Spring Data REST، تحتاج إلى تضمين تبعيته في مشروعك. إذا كنت تستخدم **Spring Boot** (وهو السيناريو الشائع)، أضف التبعية التالية إلى ملف البناء لديك:

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

هذه الحزمة الأساسية تجلب `spring-data-rest-core` مع المكونات الضرورية الأخرى. لمشاريع غير Spring Boot، يمكنك تضمين `spring-data-rest-core` مباشرة، ولكن يُوصى باستخدام الحزمة الأساسية لـ Spring Boot من أجل البساطة.

---

### 2. تعريف الكيانات الخاصة بك
أنشئ نموذج النطاق الخاص بك عن طريق تعريف فئات الكيانات باستخدام تقنية استمرارية مثل JPA. على سبيل المثال:

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // المنشئات
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // وسائل الوصول (Getters and Setters)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

كيان `User` هذا يمثل جدولاً بسيطًا في قاعدة البيانات الخاصة بك يحتوي على `id` و `name`.

---

### 3. إنشاء واجهات المستودع
عرّف واجهة مستودع للكيان الخاص بك عن طريق تمديد إحدى واجهات مستودع Spring Data، مثل `JpaRepository`. على سبيل المثال:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

عن طريق تمديد `JpaRepository`، تحصل على عمليات CRUD الأساسية مجانًا. ستعرض Spring Data REST هذا المستودع تلقائيًا كنقطة نهاية RESTful.

---

### 4. تشغيل تطبيقك
بعد إضافة التبعية وتحديد الكيانات والمستودعات الخاصة بك، شغّل تطبيق Spring Boot الخاص بك. سوف تقوم Spring Data REST تلقائيًا بتوليد نقاط نهاية REST بناءً على مستودعك. بالنسبة لـ `UserRepository` أعلاه، يمكنك الوصول إلى:

- **GET /users**: استرداد قائمة بجميع المستخدمين.
- **GET /users/{id}**: استرداد مستخدم معين بواسطة المعرف.
- **POST /users**: إنشاء مستخدم جديد (مع حمولة JSON، مثال: `{"name": "Alice"}`).
- **PUT /users/{id}**: تحديث مستخدم موجود.
- **DELETE /users/{id}**: حذف مستخدم.

على سبيل المثال، إذا كان تطبيقك يعمل على `localhost:8080`، يمكنك استخدام أداة مثل `curl` أو متصفح للاختبار:

```bash
curl http://localhost:8080/users
```

سيتضمن الرد روابط HATEOAS، مما يسمح للعملاء بالتنقل بين الموارد ذات الصلة ديناميكيًا.

---

### 5. (اختياري) تخصيص نقاط نهاية REST
يمكنك تخصيص كيفية عرض مستودعاتك باستخدام التعليقات التوضيحية أو التكوين:

- **تغيير مسار نقطة النهاية**:
  استخدم التعليق التوضيحي `@RepositoryRestResource` لتحديد مسار مخصص:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  الآن، ستكون نقطة النهاية هي `/people` بدلاً من `/users`.

- **تكوين الإعدادات العامة**:
  خصص المسار الأساسي أو الإعدادات الأخرى عن طريق تنفيذ `RepositoryRestConfigurer`:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // جميع نقاط النهاية ستبدأ بـ /api
      }
  }
  ```
  مع هذا، سيكون المستخدمون الخاصون بك متاحين على `/api/users`.

---

### الميزات الرئيسية لـ Spring Data REST
- **دعم HATEOAS**: تتضمن الاستجابات روابط وسائط فائطة إلى الموارد ذات الصلة.
- **ترقيم الصفحات والترتيب**: استخدم معلمات الاستعلام مثل `?page=0&size=10&sort=name,asc` لترقيم الصفحات وترتيب النتائج.
- **التصفية**: أضف طرق استعلام مخصصة إلى مستودعك (مثال: `findByName(String name)`) لعرض نقاط نهاية إضافية.

---

### الملخص
لاستخدام `spring-data-rest-core`:
1.  قم بتضمين تبعية Spring Data REST (مثال: `spring-boot-starter-data-rest` لـ Spring Boot).
2.  عرّف كياناتك باستخدام التعليقات التوضيحية المناسبة (مثال: `@Entity` لـ JPA).
3.  أنشئ واجهات مستودع تمدد واجهات Spring Data (مثال: `JpaRepository`).
4.  شغّل تطبيقك للوصول إلى نقاط نهاية REST المُولَّدة تلقائيًا.
5.  قم، اختياريًا، بتخصيص مسارات نقاط النهاية أو السلوك حسب الحاجة.

هذا الأسلوب يسمح لك ببناء واجهة برمجة تطبيقات RESTful بسرعة وبحد أدنى من التعليمات البرمجية، مستفيدًا من الوظائف الأساسية لـ Spring Data REST.