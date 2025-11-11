---
audio: false
generated: true
lang: hant
layout: post
title: Spring 任務排程
translated: true
type: note
---

在 Spring 中排程任務是實現自動化重複性工作（例如發送電子郵件、生成報告或執行系統維護）的常見需求。Spring 透過 `@Scheduled` 註解和 Spring Task Scheduler 提供強大且易用的任務排程功能。以下我將逐步引導您進行設定，並解釋關鍵概念。

### 1. **在 Spring 應用程式中啟用排程功能**
要使用排程功能，您需要在 Spring 應用程式中啟用它。這可以透過在配置類別上添加 `@EnableScheduling` 註解來實現。

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // 配置類別可以為空，除非您需要自訂排程器設定
}
```

這會告訴 Spring 尋找帶有 `@Scheduled` 註解的方法，並根據其定義的排程時間執行它們。

---

### 2. **建立要排程的任務**
您可以在任何 Spring 管理的 bean（例如 `@Component` 或 `@Service`）中定義一個方法，並使用 `@Scheduled` 註解它。以下是一個範例：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // 每 5 秒執行一次
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("任務執行時間: " + System.currentTimeMillis());
    }
}
```

在此範例中：
- `@Component` 將類別標記為 Spring bean。
- `@Scheduled(fixedRate = 5000)` 使該方法每 5 秒（5000 毫秒）執行一次。

---

### 3. **排程選項的類型**
Spring 提供多種方式來定義任務應何時執行：

#### a) **固定速率**
- 以固定間隔執行任務，無論任務執行時間長短。
- 範例：`@Scheduled(fixedRate = 5000)`（每 5 秒一次）。

#### b) **固定延遲**
- 在一次執行結束與下一次執行開始之間，以固定延遲執行任務。
- 範例：`@Scheduled(fixedDelay = 5000)`（上一次任務完成後 5 秒執行）。

#### c) **Cron 表達式**
- 使用類似 cron 的語法來定義更複雜的排程（例如「每個工作日上午 9 點」）。
- 範例：`@Scheduled(cron = "0 0 9 * * MON-FRI")`。

#### d) **初始延遲**
- 延遲任務的首次執行。可與 `fixedRate` 或 `fixedDelay` 結合使用。
- 範例：`@Scheduled(fixedRate = 5000, initialDelay = 10000)`（10 秒後開始執行，之後每 5 秒執行一次）。

---

### 4. **Cron 語法基礎**
如果您使用 cron，以下是一個快速參考：
- 格式：`秒 分 時 日 月 星期幾`
- 範例：`@Scheduled(cron = "0 15 10 * * ?")`（每天上午 10:15 執行）。

| 欄位          | 允許的值            |
|---------------|---------------------|
| 秒            | 0-59               |
| 分            | 0-59               |
| 時            | 0-23               |
| 日            | 1-31               |
| 月            | 1-12 或 JAN-DEC    |
| 星期幾        | 0-7 或 SUN-SAT（0 或 7 代表星期日） |

可以使用特殊字符，例如 `*`（所有）、`,`（列表）、`-`（範圍）、`/`（增量）。

---

### 5. **相依性**
如果您使用 Spring Boot，排程功能已預設包含在 `spring-boot-starter` 相依性中。對於非 Spring Boot 的 Spring 專案，請確保您擁有：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- 請使用最新版本 -->
</dependency>
```

---

### 6. **使用 Spring Boot 的完整範例**
以下是一個完整的 Spring Boot 範例：

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
        System.out.println("每 5 秒執行一次: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("每分鐘執行一次: " + System.currentTimeMillis());
    }
}
```

---

### 7. **自訂排程器（可選）**
預設情況下，Spring 使用單線程排程器。如果您需要並發執行任務，可以配置自訂的 `TaskScheduler`：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // 線程數量
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

這允許多個任務並行執行。

---

### 8. **測試您的排程任務**
- 執行您的應用程式並檢查控制台日誌，以驗證任務是否按預期執行。
- 在測試期間使用較短的間隔（例如每 2 秒一次）以快速查看結果。