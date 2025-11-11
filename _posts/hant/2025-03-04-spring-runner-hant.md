---
audio: false
generated: true
lang: hant
layout: post
title: 在Java測試中使用SpringRunner
translated: true
type: note
---

要在 Java 測試中使用 `SpringRunner` 配合 JUnit 的 `@RunWith` runner，請遵循以下步驟。請注意，我假設您查詢中的 "SpringRuner" 是拼寫錯誤，您實際指的是 `SpringRunner`。以下是完整指南：

### 步驟 1：添加 Spring Test 依賴
要使用 `SpringRunner`，您需要在專案中加入 Spring Test 模組。如果您使用 Maven，請在 `pom.xml` 中添加此依賴：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

將 `${spring.version}` 替換為您使用的 Spring 版本（例如 `5.3.22`）。如果您使用 Gradle，請在 `build.gradle` 中添加：

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

這確保 `SpringRunner` 和其他 Spring 測試工具可用。

### 步驟 2：使用 `@RunWith(SpringRunner.class)` 標註測試類別
`@RunWith` 註解告訴 JUnit 使用特定的 runner 而非預設的。對於 Spring 整合，請使用 `SpringRunner`，它是 Spring TestContext Framework 的一部分。在測試類別上添加此註解：

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // 測試代碼放在這裡
}
```

`SpringRunner` 啟用 Spring 功能，如依賴注入和上下文加載，在您的測試中。請注意 `@RunWith` 是 JUnit 4 註解，因此此方法假設您使用 JUnit 4。對於 JUnit 5，您會使用 `@ExtendWith(SpringExtension.class)`，但您提到 "RunWith runner" 表明是 JUnit 4。

### 步驟 3：使用 `@ContextConfiguration` 配置 Spring 應用程式上下文
要在測試中使用 Spring 管理的 bean，您需要加載 Spring 應用程式上下文。`@ContextConfiguration` 註解指定如何進行。例如，如果您有配置類別（如 `AppConfig`），請使用：

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // 測試代碼放在這裡
}
```

如果您的配置在 XML 檔案中（如 `applicationContext.xml`），請使用：

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

這告訴 `SpringRunner` 要為測試加載哪些 bean 和配置。

### 步驟 4：使用 `@Autowired` 注入 Spring Bean
上下文加載後，您可以使用 `@Autowired` 將 Spring 管理的 bean 注入測試類別。例如，如果您有名為 `MyService` 的服務：

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // 測試方法放在這裡
}
```

這允許您在測試中使用注入的 bean。

### 步驟 5：使用 `@Test` 編寫測試方法
使用 JUnit 的 `@Test` 註解定義測試方法。例如：

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
        assertEquals("Expected result", result);
    }
}
```

`@Test` 註解標記 JUnit 應作為測試執行的方法。使用 `SpringRunner` 時，這些方法可以與 Spring 上下文互動。

### 範例：完整整合
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

// 測試用的配置類別
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// 要測試的服務類別
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// 測試類別
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

### 補充說明
- **目的**：`SpringRunner` 適用於需要 Spring 依賴注入或上下文功能的整合測試。對於單元測試，請考慮使用 Mockito 或純 JUnit。
- **常見問題**：確保包含 `spring-test` 依賴，否則會出現如 `ClassNotFoundException` 的錯誤。同時驗證 `@ContextConfiguration` 指向有效的配置。
- **可選註解**：使用 `@Transactional` 用於修改數據庫的測試（以回滾更改）或 `@ActiveProfiles` 指定配置檔（例如 "test"）。

此設置允許您使用 Spring 測試支援運行 JUnit 測試，利用依賴注入和上下文管理等功能。