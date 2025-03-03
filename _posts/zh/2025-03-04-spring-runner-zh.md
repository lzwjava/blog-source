---
audio: false
generated: true
lang: zh
layout: post
title: 使用 SpringRunner 在 Java 测试中
translated: true
---

要在Java测试中使用`SpringRunner`与JUnit的`@RunWith`运行器，请按照以下步骤进行操作。请注意，我假设你在查询中提到的“SpringRuner”是一个拼写错误，你实际上指的是`SpringRunner`。以下是一个完整的指南：

### 步骤 1：添加Spring测试依赖
要使用`SpringRunner`，你需要在项目中添加Spring测试模块。如果你使用的是Maven，请将以下依赖项添加到你的`pom.xml`中：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

将`${spring.version}`替换为你使用的Spring版本（例如`5.3.22`）。如果你使用的是Gradle，请将以下内容添加到你的`build.gradle`中：

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

这将确保`SpringRunner`和其他Spring测试工具可用。

### 步骤 2：使用`@RunWith(SpringRunner.class)`注解测试类
`@RunWith`注解告诉JUnit使用特定的运行器而不是默认的运行器。对于Spring集成，使用`SpringRunner`，它是Spring TestContext框架的一部分。将此注解添加到你的测试类中：

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // 测试代码在这里
}
```

`SpringRunner`在测试中启用了Spring功能，如依赖注入和上下文加载。请注意，`@RunWith`是JUnit 4的注解，因此这个方法假设你使用的是JUnit 4。对于JUnit 5，你会使用`@ExtendWith(SpringExtension.class)`，但你提到的“RunWith运行器”表明你使用的是JUnit 4。

### 步骤 3：使用`@ContextConfiguration`配置Spring应用程序上下文
要在测试中使用Spring管理的bean，你需要加载Spring应用程序上下文。`@ContextConfiguration`注解指定了如何进行此操作。例如，如果你有一个配置类（例如`AppConfig`），请使用：

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // 测试代码在这里
}
```

如果你的配置在XML文件中（例如`applicationContext.xml`），请使用：

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

这告诉`SpringRunner`为测试加载哪些bean和配置。

### 步骤 4：使用`@Autowired`注入Spring Bean
上下文加载后，你可以使用`@Autowired`将Spring管理的bean注入到测试类中。例如，如果你有一个名为`MyService`的服务：

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // 测试方法在这里
}
```

这允许你在测试中使用注入的bean。

### 步骤 5：使用`@Test`编写测试方法
使用JUnit的`@Test`注解定义你的测试方法。例如：

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
        assertEquals("预期结果", result);
    }
}
```

`@Test`注解标记了JUnit应该执行的测试方法。使用`SpringRunner`，这些方法可以与Spring上下文交互。

### 示例：将所有内容结合在一起
以下是一个完整的示例：

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// 测试的配置类
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// 要测试的服务类
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// 测试类
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

### 附加说明
- **目的**：`SpringRunner`适用于需要Spring依赖注入或上下文功能的集成测试。对于单元测试，考虑使用Mockito或普通的JUnit。
- **常见问题**：确保包含`spring-test`依赖项，否则你会遇到`ClassNotFoundException`等错误。还要验证`@ContextConfiguration`是否指向有效的配置。
- **可选注解**：使用`@Transactional`进行修改数据库的测试（以回滚更改），或者使用`@ActiveProfiles`指定一个配置文件（例如“test”）。

这种设置允许你使用Spring的测试支持运行JUnit测试，利用依赖注入和上下文管理等功能。