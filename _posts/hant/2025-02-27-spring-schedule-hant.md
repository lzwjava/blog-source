---
audio: true
lang: hant
layout: post
title: 排程任務於Spring
translated: true
---

在 Spring 中排程任務是自動化重複工作（如發送電子郵件、生成報告或執行系統維護）的常見需求。Spring 提供了一個強大且易於使用的任務排程功能，通過其 `@Scheduled` 注解和 Spring 任務排程器。以下，我將帶您了解如何設置並解釋關鍵概念。

### 1. **在您的 Spring 應用程序中啟用排程**
要使用排程，您需要在 Spring 應用程序中啟用它。這是通過將 `@EnableScheduling` 注解添加到配置類來完成的。

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // 配置類可以是空的，除非您需要自定義排程器設置
}
```

這告訴 Spring 查找帶有 `@Scheduled` 注解的方法並按其定義的排程執行它們。

---

### 2. **創建一個要排程的任務**
您可以在任何 Spring 管理的 Bean（如 `@Component` 或 `@Service`）中定義一個方法，並用 `@Scheduled` 注解它。以下是一個示例：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // 每 5 秒運行一次
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("任務執行於: " + System.currentTimeMillis());
    }
}
```

在這個示例中：
- `@Component` 使類成為 Spring Bean。
- `@Scheduled(fixedRate = 5000)` 每 5 秒（5000 毫秒）運行一次方法。

---

### 3. **排程選項類型**
Spring 提供了幾種定義任務何時運行的方法：

#### a) **固定速率**
- 以固定間隔執行任務，無論任務需要多長時間。
- 示例：`@Scheduled(fixedRate = 5000)`（每 5 秒）。

#### b) **固定延遲**
- 以固定延遲在一個執行結束和下一個開始之間執行任務。
- 示例：`@Scheduled(fixedDelay = 5000)`（前一個任務完成後 5 秒）。

#### c) **Cron 表達式**
- 使用類似 cron 的語法進行更複雜的排程（例如，每個工作日早上 9 點）。
- 示例：`@Scheduled(cron = "0 0 9 * * MON-FRI")`。

#### d) **初始延遲**
- 延遲任務的第一次執行。與 `fixedRate` 或 `fixedDelay` 結合使用。
- 示例：`@Scheduled(fixedRate = 5000, initialDelay = 10000)`（10 秒後開始，然後每 5 秒運行一次）。

---

### 4. **Cron 語法基礎**
如果您使用 cron，這裡有一個快速參考：
- 格式：`second minute hour day-of-month month day-of-week`
- 示例：`@Scheduled(cron = "0 15 10 * * ?")`（每天早上 10:15 運行）。

| 字段         | 允許的值       |
|---------------|----------------------|
| 秒          | 0-59                |
| 分鐘        | 0-59                |
| 小時          | 0-23                |
| 月的日        | 1-31                |
| 月份         | 1-12 或 JAN-DEC     |
| 星期幾   | 0-7 或 SUN-SAT（0 或 7 是星期日） |

可以使用特殊字符如 `*`（所有）、`,`（列表）、`-`（範圍）、`/`（增量）。

---

### 5. **依賴項**
如果您使用 Spring Boot，排程功能默認包含在 `spring-boot-starter` 依賴項中。對於非 Boot Spring 專案，請確保您有：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- 使用最新版本 -->
</dependency>
```

---

### 6. **完整的 Spring Boot 示例**

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
        System.out.println("每 5 秒運行一次: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("每分鐘運行一次: " + System.currentTimeMillis());
    }
}
```

---

### 7. **自定義排程器（可選）**
默認情況下，Spring 使用單線程排程器。如果您需要並行任務執行，可以配置自定義 `TaskScheduler`：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // 線程數
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

這允許多個任務並行運行。

---

### 8. **測試您的排程任務**
- 運行您的應用程序並檢查控制台日誌以驗證任務是否按預期執行。
- 在測試期間使用較短的間隔（例如，每 2 秒）以快速看到結果。