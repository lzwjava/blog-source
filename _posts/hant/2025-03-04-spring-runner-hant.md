---
audio: true
generated: true
lang: hant
layout: post
title: 使用 SpringRunner 在 Java 測試中
translated: true
---

要在 Java 測試中使用 `SpringRunner` 並與 JUnit 的 `@RunWith` 運行器一起使用，請按照以下步驟進行。請注意，我假設您在查詢中提到的 "SpringRuner" 是拼寫錯誤，您的意思是 `SpringRunner`。以下是完整指南：

### 第一步：添加 Spring 測試依賴
要使用 `SpringRunner`，您需要在項目中使用 Spring 測試模組。如果您使用 Maven，請將以下依賴項添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

將 `${spring.version}` 替換為您使用的 Spring 版本（例如 `5.3.22`）。如果您使用 Gradle，請將以下內容添加到您的 `build.gradle`：

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

這樣可以確保 `SpringRunner` 和其他 Spring 測試工具可用。

### 第二步：使用 `@RunWith(SpringRunner.class)` 註解測試類
`@RunWith` 註解告訴 JUnit 使用特定的運行器而不是其默認運行器。對於 Spring 集成，使用 `SpringRunner`，它是 Spring TestContext Framework 的一部分。將此註解添加到您的測試類：

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // 測試代碼在此處
}
```

`SpringRunner` 使測試中可以使用 Spring 功能，如依賴注入和上下文加載。請注意，`@RunWith` 是 JUnit 4 的註解，因此這種方法假設您使用的是 JUnit 4。對於 JUnit 5，您應該使用 `@ExtendWith(SpringExtension.class)`，但您提到的 "RunWith runner" 表明您使用的是 JUnit 4。

### 第三步：使用 `@ContextConfiguration` 配置 Spring 應用程序上下文
要在測試中使用 Spring 管理的 bean，您需要加載 Spring 應用程序上下文。`@ContextConfiguration` 註解指定如何進行。例如，如果您有一個配置類（例如 `AppConfig`），請使用：

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // 測試代碼在此處
}
```

如果您的配置在 XML 文件中（例如 `applicationContext.xml`），請使用：

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

這告訴 `SpringRunner` 為測試加載哪些 bean 和配置。

### 第四步：使用 `@Autowired` 注入 Spring Bean
上下文加載後，您可以使用 `@Autowired` 將 Spring 管理的 bean 注入到測試類中。例如，如果您有一個名為 `MyService` 的服務：

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // 測試方法在此處
}
```

這使您可以在測試中使用注入的 bean。

### 第五步：使用 `@Test` 定義測試方法
使用 JUnit 的 `@Test` 註解定義您的測試方法。例如：

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("預期結果", result);
    }
}
```

`@Test` 註解標記 JUnit 應該執行作為測試的方法。使用 `SpringRunner`，這些方法可以與 Spring 上下文交互。

### 範例：將所有內容結合起來
以下是完整範例：

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// 測試的配置類
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// 要測試的服務類
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// 測試類
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hello, Spring!", result);
    }
}
```

### 附加說明
- **用途**：`SpringRunner` 適合需要 Spring 的依賴注入或上下文功能的集成測試。對於單元測試，請考慮使用 Mockito 或普通的 JUnit。
- **常見問題**：請確保包含 `spring-test` 依賴項，否則您將收到類似 `ClassNotFoundException` 的錯誤。還要驗證 `@ContextConfiguration` 是否指向有效的配置。
- **可選註解**：使用 `@Transactional` 進行修改數據庫的測試（以回滾更改）或使用 `@ActiveProfiles` 指定配置文件（例如 "test"）。

這種設置允許您使用 Spring 的測試支持運行 JUnit 測試，利用依賴注入和上下文管理等功能。