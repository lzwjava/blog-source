---
audio: false
generated: true
lang: hant
layout: post
title: Spring Data JPA
translated: true
type: note
---

在 Spring Boot 專案中使用儲存庫作為資料來源，通常需要整合 Spring Data JPA（Java Persistence API）來管理資料庫互動。以下是設定步驟的詳細指南：

### 1. 添加依賴項
首先，如果您使用 Maven，需要在 `pom.xml` 檔案中添加必要的依賴項。對於 Spring Data JPA，您需要以下內容：

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

### 2. 設定資料庫
在 `application.properties` 檔案中設定資料庫配置。例如，如果您使用 H2 記憶體資料庫：

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
```

### 3. 建立實體類別
定義一個映射到資料庫表格的實體類別。使用 JPA 註解來指定映射關係：

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

    // Getter 和 Setter 方法
}
```

### 4. 建立儲存庫介面
建立一個繼承 `JpaRepository` 的儲存庫介面。該介面將為 `User` 實體提供 CRUD 操作：

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // 可在此定義自訂查詢方法
}
```

### 5. 在服務層使用儲存庫
將儲存庫注入服務類別以執行資料庫操作：

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

### 6. 建立控制器
建立 REST 控制器以提供與 `User` 實體互動的端點：

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

### 7. 執行應用程式
執行您的 Spring Boot 應用程式。現在您應該能夠透過 REST 端點對 `User` 實體執行 CRUD 操作。

此設定提供了在 Spring Boot 專案中使用儲存庫作為資料來源的基本結構。您可以透過添加自訂查詢、處理例外情況和實作更複雜的業務邏輯來進一步擴展功能。