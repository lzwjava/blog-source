---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 多線程處理
translated: true
type: note
---

在 Spring Boot 專案中，「執行器」(executors) 與「執行緒」(threads) 的概念通常涉及應用程式如何處理並行任務及管理工作負載，特別是在非同步處理、任務排程或處理多重請求的情境中。讓我們逐步解析：

---

### **Spring Boot 中的執行器與執行緒是什麼？**

1. **執行緒**：
   - 執行緒是 Java 程式中最小的執行單位。在 Spring Boot 應用程式中，執行緒用於處理像是處理 HTTP 請求、執行背景工作或進行 I/O 操作等任務。
   - Spring Boot 預設在嵌入式網頁伺服器（例如 Tomcat、Jetty 或 Undertow）中運行，這些伺服器使用執行緒池來管理傳入的請求。每個請求通常會從此池中分配一個執行緒來處理。

2. **執行器**：
   - 在 Java（及 Spring Boot）中，`Executor` 是對執行緒管理的抽象概念。它屬於 `java.util.concurrent` 套件的一部分，提供了一種非同步管理和執行任務的方式，無需手動建立和管理執行緒。
   - 在 Spring Boot 中，執行器常用於將任務從主應用程式執行緒（例如處理 HTTP 請求的執行緒）卸載到獨立的執行緒池。這對於長時間運行的任務、並行處理或排程工作非常有用。

3. **Spring 特定情境**：
   - Spring Boot 提供了如 `ThreadPoolTaskExecutor`（用於一般任務執行）和 `ThreadPoolTaskScheduler`（用於排程任務）等工具，以簡化執行器與執行緒的操作。
   - 這些工具建基於 Java 的 `ExecutorService`，通常用於：
     - 非同步方法執行（透過 `@Async`）。
     - 任務排程（透過 `@Scheduled`）。
     - 在高並行情境中管理工作負載。

---

### **它們在 Spring Boot 中如何運作？**

#### **1. Spring Boot 中的預設執行緒管理**
- 當你啟動 Spring Boot 網頁應用程式時，嵌入式伺服器（例如 Tomcat）會初始化一個執行緒池來處理傳入的 HTTP 請求。
- 例如，Tomcat 的預設配置可能會分配 200 個執行緒（可透過 `application.properties` 中的 `server.tomcat.threads.max` 進行配置）。
- 每個傳入的請求都會從此池中分配一個執行緒。如果所有執行緒都在忙碌中且新請求到達，它可能會排隊（取決於伺服器的配置）或被拒絕。

#### **2. Spring Boot 中的執行器**
- Spring Boot 提供了 `TaskExecutor` 介面（Java `Executor` 的擴展）來管理特定任務的自訂執行緒池。
- 常見的實作是 `ThreadPoolTaskExecutor`，它允許你配置：
  - **核心池大小**：始終保持存活的執行緒數量。
  - **最大池大小**：池中允許的最大執行緒數量。
  - **隊列容量**：在產生新執行緒（最多達到最大池大小）之前，可以等待在隊列中的任務數量。
  - **執行緒命名**：便於除錯（例如 "my-executor-thread-1"）。

  在 Spring Boot 應用程式中的配置範例：
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

  @Configuration
  public class ExecutorConfig {

      @Bean
      public ThreadPoolTaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(5);      // 最少 5 個執行緒
          executor.setMaxPoolSize(10);      // 最多 10 個執行緒
          executor.setQueueCapacity(100);   // 隊列最多 100 個任務
          executor.setThreadNamePrefix("MyExecutor-");
          executor.initialize();
          return executor;
      }
  }
  ```

#### **3. 使用 `@Async` 與執行器**
- Spring Boot 支援透過 `@Async` 註解進行非同步方法執行。當你用 `@Async` 標註一個方法時，它會在由執行器管理的獨立執行緒上運行。
- 預設情況下，Spring 使用 `SimpleAsyncTaskExecutor`，它會為每個任務建立一個新執行緒（不適合高負載）。為了優化，你可以提供自己的 `ThreadPoolTaskExecutor`（如上所示）並引用它：
  ```java
  @Service
  public class MyService {

      @Async("taskExecutor") // 引用配置中的 bean 名稱
      public void doAsyncTask() {
          System.out.println("Running on thread: " + Thread.currentThread().getName());
      }
  }
  ```

#### **4. 任務排程**
- 對於排程任務（例如每 5 分鐘運行一次工作），Spring Boot 使用 `ThreadPoolTaskScheduler`。它類似於 `ThreadPoolTaskExecutor`，但專為排程而設計。
- 範例：
  ```java
  @Scheduled(fixedRate = 5000) // 每 5 秒運行一次
  public void scheduledTask() {
      System.out.println("Scheduled task on: " + Thread.currentThread().getName());
  }
  ```

#### **5. 執行緒與執行器如何互動**
- 當任務被提交給執行器（例如透過 `@Async` 或手動提交）時，執行器會決定是否：
  - 使用池中現有的空閒執行緒。
  - 建立新執行緒（如果核心池大小已超過但未達最大池大小）。
  - 將任務排入隊列（如果達到最大池大小且隊列未滿）。
  - 拒絕任務（如果隊列已滿且無法建立更多執行緒）。
- 執行緒執行任務並在完成後返回池中，準備處理下一個任務。

---

### **實際範例**
假設一個 Spring Boot 應用程式處理用戶註冊：
- **HTTP 請求執行緒**：用戶提交註冊表單，由 Tomcat 執行緒池中的一個執行緒處理。
- **非同步任務**：發送確認郵件的任務透過 `@Async` 方法卸載給 `ThreadPoolTaskExecutor`，因此 HTTP 執行緒可以立即回應，無需等待郵件發送完成。
- **排程任務**：每小時運行一次的清理工作，用於移除未驗證的帳戶，由 `ThreadPoolTaskScheduler` 管理。

---

### **關鍵要點**
- **執行器** 抽象化了執行緒管理，使擴展和調整並行處理更加容易。
- **執行緒** 執行實際工作，其生命週期由執行器或網頁伺服器管理。
- Spring Boot 的預設配置對於小型應用程式已足夠，但對於高負載或複雜應用程式，你需要配置自訂執行器以優化效能。

如果你有特定的 Spring Boot 專案，並需要協助分析其執行器/執行緒設置，歡迎分享更多細節！