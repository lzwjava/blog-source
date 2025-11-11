---
audio: false
generated: true
lang: ar
layout: post
title: ربيع البيانات جي بي إيه
translated: true
type: note
---

يُعد استخدام مستودع كمصدر للبيانات في مشروع Spring Boot عادةً عملية دمج Spring Data JPA (واجهة برمجة تطبيقات Java للاستمرارية) لإدارة تفاعلات قاعدة البيانات. إليك دليل خطوة بخطوة حول كيفية إعداد هذا:

### 1. إضافة التبعيات
أولاً، تحتاج إلى إضافة التبعيات اللازمة إلى ملف `pom.xml` الخاص بك إذا كنت تستخدم Maven. بالنسبة لـ Spring Data JPA، ستحتاج إلى ما يلي:

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

### 2. تكوين قاعدة البيانات
قم بتكوين إعدادات قاعدة البيانات في ملف `application.properties`. على سبيل المثال، إذا كنت تستخدم قاعدة بيانات H2 في الذاكرة:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
```

### 3. إنشاء كيان (Entity)
قم بتعريف فئة كيان تُرسم إلى جدول في قاعدة البيانات. استخدم تعريفات JPA لتحديد عملية الرسم:

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

### 4. إنشاء واجهة المستودع (Repository)
أنشئ واجهة مستودع تمتد `JpaRepository`. ستوفر هذه الواجهة عمليات CRUD لكيان `User`:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // يمكن تعريف طرق الاستعلام المخصصة هنا
}
```

### 5. استخدام المستودع في خدمة (Service)
احقن المستودع في فئة خدمة لتنفيذ عمليات قاعدة البيانات:

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

### 6. إنشاء وحدة تحكم (Controller)
أنشئ وحدة تحكم REST لتوفير نقاط نهاية للتفاعل مع كيان `User`:

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
شغّل تطبيق Spring Boot الخاص بك. يجب أن تكون قادرًا الآن على تنفيذ عمليات CRUD على كيان `User` باستخدام نقاط النهاية REST.

يوفر هذا الإعداد هيكلًا أساسيًا لاستخدام مستودع كمصدر للبيانات في مشروع Spring Boot. يمكنك توسيعه further بإضافة استعلامات مخصصة، ومعالجة الاستثناءات، وتنفيذ منطق أعمال أكثر تعقيدًا.