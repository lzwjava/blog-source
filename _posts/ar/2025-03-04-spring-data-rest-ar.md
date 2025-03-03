---
audio: false
generated: true
lang: ar
layout: post
title: مодуل Spring Data REST
translated: true
---

لاستخدام **spring-data-rest-core**، يمكنك الاستفادة من وحدة Spring Data REST لتعرض مستودعات Spring Data الخاصة بك كنقاط RESTful في تطبيقك. أدناه دليل شامل، خطوة بخطوة، للحصول على البدء:

---

### 1. إضافة التبعية Spring Data REST
لاستخدام Spring Data REST، يجب عليك تضمين التبعية في مشروعك. إذا كنت تستخدم **Spring Boot** (سيناريو شائع)، أضف التبعية التالية إلى ملف البناء الخاص بك:

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

تجلب هذه البدء `spring-data-rest-core` مع المكونات اللازمة الأخرى. بالنسبة للمشاريع غير Spring Boot، يمكنك تضمين `spring-data-rest-core` مباشرة، ولكن البدء Spring Boot مفضل من أجل السهولة.

---

### 2. تعريف كياناتك
إنشاء نموذج المجال الخاص بك من خلال تعريف فئات الكيان باستخدام تقنية استدامة مثل JPA (Java Persistence API). على سبيل المثال:

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

    // Constructors
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

يمثل هذا الكيان المستخدم جدولاً بسيطاً في قاعدة البيانات الخاصة بك مع `id` و `name`.

---

### 3. إنشاء واجهات المستودع
تعريف واجهة مستودع لكيانك من خلال امتداد واحدة من واجهات مستودع Spring Data، مثل `JpaRepository`. على سبيل المثال:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

من خلال امتداد `JpaRepository`، تحصل على عمليات CRUD (إنشاء، قراءة، تحديث، حذف) الأساسية مجاناً. سيعرض Spring Data REST هذا المستودع تلقائياً كنقطة RESTful.

---

### 4. تشغيل تطبيقك
مع إضافة التبعية و تعريف كياناتك و واجهات المستودع، ابدأ تطبيق Spring Boot الخاص بك. سيعمل Spring Data REST تلقائياً على إنشاء نقاط REST بناءً على المستودع الخاص بك. بالنسبة إلى `UserRepository` أعلاه، يمكنك الوصول إلى:

- **GET /users**: استرجاع قائمة جميع المستخدمين.
- **GET /users/{id}**: استرجاع مستخدم محدد من خلال ID.
- **POST /users**: إنشاء مستخدم جديد (مع حمولة JSON، مثل `{"name": "Alice"}`).
- **PUT /users/{id}**: تحديث مستخدم موجود.
- **DELETE /users/{id}**: حذف مستخدم.

على سبيل المثال، إذا كان تطبيقك يعمل على `localhost:8080`، يمكنك استخدام أداة مثل `curl` أو المتصفح لاختبار:

```bash
curl http://localhost:8080/users
```

ستشمل الإجابة روابط HATEOAS، مما يسمح للعميل بالتنقل بين الموارد ذات الصلة بشكل ديناميكي.

---

### 5. (اختياري) تخصيص نقاط REST
يمكنك تخصيص كيفية عرض مستودعاتك باستخدام التعليقات أو التكوين:

- **تغيير مسار النقطة**:
  استخدم التعليق `@RepositoryRestResource` لتحديد مسار مخصص:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  الآن، ستكون النقطة `/people` بدلاً من `/users`.

- **تكوين الإعدادات العالمية**:
  تخصيص مسار الأساس أو إعدادات أخرى من خلال تنفيذ `RepositoryRestConfigurer`:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // جميع النقاط ستبدأ بـ /api
      }
  }
  ```
  مع هذا، يمكن الوصول إلى المستخدمين في `/api/users`.

---

### الميزات الرئيسية لSpring Data REST
- **دعم HATEOAS**: تشمل الإجابات روابط هايبر ميديا للموارد ذات الصلة.
- **التصفح والتصفية**: استخدم معلمات الاستعلام مثل `?page=0&size=10&sort=name,asc` لتصفح وتصفية النتائج.
- **التصفية**: أضف طرق الاستعلام المخصصة إلى مستودعك (على سبيل المثال، `findByName(String name)`) لتعرض نقاط النهاية الإضافية.

---

### ملخص
لاستخدام `spring-data-rest-core`:
1. أضف التبعية Spring Data REST (على سبيل المثال، `spring-boot-starter-data-rest` لـ Spring Boot).
2. تعريف كياناتك مع التعليقات المناسبة (على سبيل المثال، `@Entity` لـ JPA).
3. إنشاء واجهات المستودع من خلال امتداد واجهات Spring Data (على سبيل المثال، `JpaRepository`).
4. تشغيل تطبيقك للوصول إلى نقاط النهاية REST التي تم إنشاؤها تلقائياً.
5. اختيارياً، تخصيص مسارات النقاط أو السلوك حسب الحاجة.

يتيح لك هذا النهج بناء API RESTful بسرعة مع أقل قدر من الكود، مستفيداً من الوظائف الأساسية لSpring Data REST.