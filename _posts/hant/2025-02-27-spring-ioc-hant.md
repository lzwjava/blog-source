---
audio: false
lang: hant
layout: post
title: Spring IoC (控制反轉) 容器
translated: true
---

讓我以清晰和實際的方式分解如何使用 Spring IoC（控制反轉）容器。Spring IoC 容器是 Spring 框架的核心，負責管理應用程式物件（稱為 beans）的生命週期和配置。它通過處理物件創建和依賴注入來「反轉」控制，而不是你手動創建和連接它們。

以下是開始的分步指南：

---

### 1. **了解基本概念**
- **功能**：IoC 容器根據你提供的元數據（通過 XML、Java 注釋或 Java 代碼）創建、配置和管理 beans（你的應用程式物件）。
- **關鍵概念**：
  - **Beans**：由容器管理的物件。
  - **依賴注入（DI）**：容器將依賴（其他 beans 或值）注入到你的物件中。
  - **配置**：你告訴容器創建哪些 beans 以及如何連接它們。

---

### 2. **設置你的項目**
要使用 Spring IoC，你需要一個 Spring 項目。如果你是從頭開始：
- 使用 **Spring Boot**（最簡單的方法）或普通的 Spring。
- 在你的 `pom.xml` 中添加依賴（如果使用 Maven）：
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- 使用最新版本 -->
  </dependency>
  ```
- 如果是 Spring Boot，使用：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- 目前最新版本 -->
  </dependency>
  ```

---

### 3. **定義你的 Beans**
你可以通過三種主要方式定義 beans：

#### a) **使用註解（最常見）**
- 創建一個簡單的 Java 類並用 `@Component`（或專門的註解如 `@Service`、`@Repository` 等）註解它。
- 範例：
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **使用 Java 配置**
- 創建一個帶有 `@Configuration` 的配置類並用 `@Bean` 定義 beans。
- 範例：
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

#### c) **使用 XML（傳統方法）**
- 在 XML 文件（例如 `beans.xml`）中定義 beans：
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **初始化 IoC 容器**
你需要啟動容器來管理你的 beans。

#### a) **使用 Spring Boot**
- Spring Boot 會自動完成這一步。只需創建一個帶有 `@SpringBootApplication` 的主類：
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
- 容器會掃描 `@Component` 類並管理它們。

#### b) **使用普通 Spring（基於註解）**
- 使用 `AnnotationConfigApplicationContext`：
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

#### c) **使用 XML**
- 使用 `ClassPathXmlApplicationContext`：
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

### 5. **注入依賴**
IoC 容器可以將依賴注入到你的 beans 中。

#### a) **構造函數注入（推薦）**
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

#### b) **設置方法注入**
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

#### c) **字段注入（不太推薦）**
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
- 使用 `@Autowired`（Spring 特定）或 `@Inject`（JSR-330 標準）來標記注入點。

---

### 6. **運行和使用 Beans**
- 一旦容器運行，它就會連接你的 beans 和它們的依賴。你可以使用 `context.getBean()`（普通 Spring）獲取 beans，或者讓 Spring Boot 自動處理它們。

使用 Spring Boot 的範例：
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

### 7. **額外提示**
- **範圍**：默認情況下，beans 是單例的。使用 `@Scope("prototype")` 為每個請求創建新實例。
- **組件掃描**：如果 beans 在不同的包中，請在配置類中添加 `@ComponentScan`。
- **配置文件**：使用 `@Profile` 在特定環境（例如「dev」、「prod」）中激活 beans。
- **關閉上下文**：在非 Spring Boot 應用中，調用 `context.close()` 以釋放資源。

---

這就是大致的內容！從 Spring Boot 和註解開始，以簡化操作。如果你在某個特定部分遇到困難——例如連接一個複雜的依賴或調試——隨時問我，我會深入探討！