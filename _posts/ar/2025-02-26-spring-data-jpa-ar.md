---
audio: false
generated: false
lang: ar
layout: post
title: Spring Data JPA
translated: true
---

استخدام مستودع كمصدر بيانات في مشروع Spring Boot عادةً يتضمن دمج Spring Data JPA (Java Persistence API) لإدارة التفاعلات مع قاعدة البيانات. إليك دليل خطوة بخطوة على كيفية إعداد ذلك:

### 1. إضافة الاعتماديات
أولاً، يجب عليك إضافة الاعتماديات اللازمة إلى ملف `pom.xml` إذا كنت تستخدم Maven. بالنسبة لSpring Data JPA، ستحتاج إلى التالي:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

### 2. تهيئة قاعدة البيانات
قم بتهيئة إعدادات قاعدة البيانات في ملف `application.properties`. على سبيل المثال، إذا كنت تستخدم قاعدة بيانات H2 في الذاكرة:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
```

### 3. إنشاء كيان
قم بتحديد فئة كيان تتوافق مع جدول قاعدة البيانات. استخدم تعليقات JPA لتحديد التحويل:

```java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;

    // Getters and setters
}
```

### 4. إنشاء واجهة مستودع
قم بإنشاء واجهة مستودع تمتد من `JpaRepository`. ستوفر هذه الواجهة عمليات CRUD للكيان `User`:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // يمكن تعريف أسئلة مخصصة هنا
}
```

### 5. استخدام المستودع في خدمة
قم بإدخال المستودع في فئة الخدمة لإجراء عمليات قاعدة البيانات:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

### 6. إنشاء Controller
قم بإنشاء Controller REST لتقديم نقاط النهاية للتفاعل مع الكيان `User`:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.saveUser(user);
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

### 7. تشغيل التطبيق
قم بتشغيل تطبيق Spring Boot الخاص بك. يجب أن تكون قادرًا الآن على تنفيذ عمليات CRUD على الكيان `User` باستخدام نقاط النهاية REST.

يوفر هذا الإعداد بنية أساسية لاستخدام مستودع كمصدر بيانات في مشروع Spring Boot. يمكنك توسيعه بشكل أكبر من خلال إضافة أسئلة مخصصة، معالجة الاستثناءات، وتطبيق منطق أعمال أكثر تعقيدًا.