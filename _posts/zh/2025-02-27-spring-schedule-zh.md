---
audio: false
lang: zh
layout: post
title: 任务调度在Spring中
translated: true
---

在 Spring 中安排任务是自动化重复性工作（如发送电子邮件、生成报告或执行系统维护）的常见需求。Spring 提供了强大且易于使用的任务调度功能，通过其 `@Scheduled` 注解和 Spring 任务调度器。下面，我将带您了解设置步骤并解释关键概念。

### 1. **在 Spring 应用程序中启用调度**
要使用调度功能，您需要在 Spring 应用程序中启用它。这可以通过在配置类中添加 `@EnableScheduling` 注解来实现。

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // 配置类可以为空，除非您需要自定义调度器设置
}
```

这告诉 Spring 查找用 `@Scheduled` 注解的方法并按其定义的时间表执行它们。

---

### 2. **创建要调度的任务**
您可以在任何 Spring 管理的 bean（如 `@Component` 或 `@Service`）中定义一个方法，并用 `@Scheduled` 注解它。以下是一个示例：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // 每 5 秒运行一次
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("任务执行于: " + System.currentTimeMillis());
    }
}
```

在这个示例中：
- `@Component` 使类成为 Spring bean。
- `@Scheduled(fixedRate = 5000)` 每 5 秒（5000 毫秒）运行一次方法。

---

### 3. **调度选项类型**
Spring 提供了多种定义任务何时运行的方式：

#### a) **固定速率**
- 以固定间隔执行任务，无论任务需要多长时间。
- 示例：`@Scheduled(fixedRate = 5000)`（每 5 秒）。

#### b) **固定延迟**
- 以固定延迟在一个执行结束和下一个执行开始之间执行任务。
- 示例：`@Scheduled(fixedDelay = 5000)`（在前一个任务完成后 5 秒）。

#### c) **Cron 表达式**
- 使用类似 cron 的语法进行更复杂的调度（例如，“每个工作日 9 点”）。
- 示例：`@Scheduled(cron = "0 0 9 * * MON-FRI")`。

#### d) **初始延迟**
- 延迟任务的首次执行。与 `fixedRate` 或 `fixedDelay` 结合使用。
- 示例：`@Scheduled(fixedRate = 5000, initialDelay = 10000)`（10 秒后开始，然后每 5 秒运行一次）。

---

### 4. **Cron 语法基础**
如果使用 cron，以下是快速参考：
- 格式：`second minute hour day-of-month month day-of-week`
- 示例：`@Scheduled(cron = "0 15 10 * * ?")`（每天 10:15 运行）。

| 字段           | 允许的值       |
|---------------|----------------|
| 秒             | 0-59          |
| 分钟           | 0-59          |
| 小时           | 0-23          |
| 月的日         | 1-31          |
| 月             | 1-12 或 JAN-DEC|
| 周的日         | 0-7 或 SUN-SAT（0 或 7 是星期日）|

可以使用特殊字符，如 `*`（所有）、`,`（列表）、`-`（范围）、`/`（增量）。

---

### 5. **依赖项**
如果使用 Spring Boot，调度功能默认包含在 `spring-boot-starter` 依赖项中。对于非 Boot Spring 项目，请确保您有：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- 使用最新版本 -->
</dependency>
```

---

### 6. **完整的 Spring Boot 示例**
以下是一个完整的 Spring Boot 示例：

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
class ScheduledTasks {

    @Scheduled(fixedRate = 5000)
    public void runEveryFiveSeconds() {
        System.out.println("每 5 秒运行一次: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("每分钟运行一次: " + System.currentTimeMillis());
    }
}
```

---

### 7. **自定义调度器（可选）**
默认情况下，Spring 使用单线程调度器。如果需要并发任务执行，可以配置自定义 `TaskScheduler`：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // 线程数
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

这允许多个任务并行运行。

---

### 8. **测试您的调度任务**
- 运行您的应用程序并检查控制台日志以验证任务是否按预期执行。
- 在测试期间使用较短的间隔（例如，每 2 秒）以快速看到结果。