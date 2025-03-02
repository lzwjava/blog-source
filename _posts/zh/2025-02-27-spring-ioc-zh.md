---
audio: true
generated: true
lang: zh
layout: post
title: Spring IoC（控制反转）容器
translated: true
---

让我以清晰和实用的方式分解如何使用 Spring IoC（控制反转）容器。Spring IoC 容器是 Spring 框架的核心，负责管理应用程序对象（称为 beans）的生命周期和配置。它通过处理对象创建和依赖注入来“反转”控制，而不是你手动创建和连接它们。

以下是一个逐步指南，帮助你入门：

---

### 1. **了解基础知识**
- **功能**：IoC 容器根据你提供的元数据（通过 XML、Java 注解或 Java 代码）创建、配置和管理 beans（你的应用程序对象）。
- **关键概念**：
  - **Beans**：由容器管理的对象。
  - **依赖注入（DI）**：容器将依赖项（其他 beans 或值）注入到你的对象中。
  - **配置**：你告诉容器创建哪些 beans 以及如何连接它们。

---

### 2. **设置你的项目**
要使用 Spring IoC，你需要一个 Spring 项目。如果你是从头开始：
- 使用 **Spring Boot**（最简单的方式）或普通的 Spring。
- 在 `pom.xml` 中添加依赖项（如果使用 Maven）：
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- 使用最新版本 -->
  </dependency>
  ```
- 对于 Spring Boot，使用：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- 目前最新版本 -->
  </dependency>
  ```

---

### 3. **定义你的 Beans**
你可以通过三种主要方式定义 beans：

#### a) **使用注解（最常见）**
- 创建一个简单的 Java 类，并用 `@Component`（或专用注解如 `@Service`、`@Repository` 等）进行注解。
- 示例：
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
- 创建一个带有 `@Configuration` 的配置类，并用 `@Bean` 定义 beans。
- 示例：
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

#### c) **使用 XML（传统方法）**
- 在 XML 文件（例如 `beans.xml`）中定义 beans：
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
你需要启动容器来管理你的 beans。

#### a) **使用 Spring Boot**
- Spring Boot 会自动完成。只需创建一个带有 `@SpringBootApplication` 的主类：
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
- 容器会扫描 `@Component` 类并管理它们。

#### b) **使用普通 Spring（基于注解）**
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

### 5. **注入依赖**
IoC 容器可以将依赖项注入到你的 beans 中。

#### a) **构造函数注入（推荐）**
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

#### b) **Setter 注入**
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

#### c) **字段注入（不太推荐）**
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
- 使用 `@Autowired`（Spring 特定）或 `@Inject`（JSR-330 标准）来标记注入点。

---

### 6. **运行和使用 Beans**
- 一旦容器运行，它就会连接你的 beans 和它们的依赖项。你可以使用 `context.getBean()`（普通 Spring）获取 beans，或者让 Spring Boot 自动处理注入。

使用 Spring Boot 的示例：
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

### 7. **额外提示**
- **作用域**：默认情况下，beans 是单例的。使用 `@Scope("prototype")` 为每个请求创建新实例。
- **组件扫描**：如果 beans 在不同的包中，请在配置类中添加 `@ComponentScan`。
- **配置文件**：使用 `@Profile` 在特定环境（例如“dev”、“prod”）中激活 beans。
- **关闭上下文**：在非 Spring Boot 应用中，调用 `context.close()` 以释放资源。

---

这就是大致的内容！从 Spring Boot 和注解开始，以简化操作。如果你在某个特定部分遇到困难——例如连接复杂的依赖或调试——请随时提问，我会深入探讨！