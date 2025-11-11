---
audio: false
generated: true
lang: hant
layout: post
title: 理解 ExecutorService 與 ThreadPoolExecutor
translated: true
type: note
---

為 Java 中的 `ExecutorService` 設定參數，需要根據系統資源（例如 8 核心 CPU）和任務性質（例如 CPU 密集型或 I/O 密集型）來配置其線程池以優化性能。以下我將說明如何針對 8 核心 CPU 配置 `ExecutorService`，重點介紹常見的實現如 `ThreadPoolExecutor`，並提供針對您使用場景的實用範例。

---

### 理解 ExecutorService 與 ThreadPoolExecutor

`ExecutorService` 接口通常由 `ThreadPoolExecutor` 這類類別實現，它允許對線程池參數進行細粒度控制。針對 8 核心 CPU 進行配置時，您需要考慮：
- **核心線程數**：即使空閒也保持存活的最小線程數。
- **最大線程數**：池中允許的最大線程數。
- **隊列容量**：在任務執行前用於暫存任務的隊列大小。
- **線程建立策略**：線程的建立和管理方式。
- **任務類型**：任務是 CPU 密集型（例如計算）還是 I/O 密集型（例如數據庫調用）。

對於 8 核心 CPU，最佳配置取決於您的任務是 CPU 密集型還是 I/O 密集型（例如您驗證場景中的數據庫訪問）。

---

### ThreadPoolExecutor 的關鍵參數

以下是設定 `ThreadPoolExecutor` 的方式：

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // 保持存活的核心線程數
    maximumPoolSize,   // 允許的最大線程數
    keepAliveTime,     // 空閒線程存活時間（例如 60L）
    TimeUnit.SECONDS,  // keepAliveTime 的時間單位
    workQueue,         // 用於暫存任務的隊列（例如 new LinkedBlockingQueue<>()）
    threadFactory,     // 可選：自定義線程命名或優先級
    rejectionHandler   // 當隊列已滿且達到最大線程數時的處理策略
);
```

#### 參數詳解
1. **`corePoolSize`**：
   - 始終保持存活的最小線程數。
   - 對於 CPU 密集型任務：設定為核心數（例如 8）。
   - 對於 I/O 密集型任務：可以設定更高（例如 16 或更多），因為線程可能會花時間等待。

2. **`maximumPoolSize`**：
   - 當隊列填滿時允許建立的最大線程數。
   - 對於 CPU 密集型：通常與 `corePoolSize` 相同（例如 8）。
   - 對於 I/O 密集型：設定更高以處理突發負載（例如 20 或 50）。

3. **`keepAliveTime`**：
   - 超出 `corePoolSize` 的空閒線程在終止前可存活的時間。
   - 範例：`60L` 秒是常見的預設值。

4. **`workQueue`**：
   - 用於等待執行任務的隊列：
     - `LinkedBlockingQueue`：無界隊列（許多情況下的預設值）。
     - `ArrayBlockingQueue`：有界隊列（例如 `new ArrayBlockingQueue<>(100)`）。
     - `SynchronousQueue`：無隊列；任務直接交給線程（用於 `Executors.newCachedThreadPool()`）。

5. **`threadFactory`**（可選）：
   - 自定義線程建立（例如為調試目的命名線程）。
   - 預設：`Executors.defaultThreadFactory()`。

6. **`rejectionHandler`**（可選）：
   - 當任務數超過 `maximumPoolSize` 和隊列容量時的處理策略：
     - `AbortPolicy`（預設）：拋出 `RejectedExecutionException`。
     - `CallerRunsPolicy`：在調用線程中執行任務。
     - `DiscardPolicy`：靜默丟棄任務。

---

### 針對 8 核心 CPU 進行配置

#### 場景 1：CPU 密集型任務
如果您的任務是 CPU 密集型（例如重度計算），您需要將線程數與 CPU 核心數匹配，以最大化吞吐量而不使系統超載。

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // 匹配 8 核心
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 秒

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // 無界隊列
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **原因**：8 個線程能充分利用 8 個核心。增加更多線程會導致上下文切換開銷，降低性能。

#### 場景 2：I/O 密集型任務（例如數據庫驗證）
對於您涉及數據庫訪問的驗證場景，任務屬於 I/O 密集型——線程會花時間等待數據庫響應。您可以使用比核心數更多的線程，以便在一些線程等待時保持 CPU 忙碌。

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // I/O 密集型任務設為核心數的 2 倍
        int maximumPoolSize = 20; // 允許一定的突發容量
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // 有界隊列以限制記憶體使用
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // 自定義命名
            new ThreadPoolExecutor.CallerRunsPolicy() // 若負載過高則退回給調用者執行
        );
    }
}
```

- **原因**：
  - `corePoolSize = 16`：對於 I/O 密集型任務，常見的經驗法則是 `N * 2`（其中 `N` 是 CPU 核心數），但您可以根據數據庫連接限制和任務等待時間進行調整。
  - `maximumPoolSize = 20`：允許額外線程處理峰值負載。
  - `ArrayBlockingQueue(100)`：防止隊列任務無限制增長，避免記憶體問題。
  - `CallerRunsPolicy`：通過在調用者線程中執行任務，確保系統在超載時能優雅降級。

#### Spring Boot 整合
在 Spring Boot 應用程式中，將 `ExecutorService` 定義為一個 Bean：

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // 針對驗證任務的 I/O 密集型假設
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **注意**：如需使用 `ThreadFactoryBuilder`，請將 Guava（`com.google.guava:guava`）加入您的依賴項，或者如果不需要自定義命名，可以使用 `Executors.defaultThreadFactory()`。

#### 在驗證服務中使用
如您之前的範例所示，注入並使用它：

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // 如前所述，在 CompletableFuture 或 ExecutorService 邏輯中使用
}
```

---

### 8 核心 CPU 的調優提示

1. **測量性能**：
   - 使用性能分析工具（例如 VisualVM）監控線程使用情況，並相應調整 `corePoolSize` 和 `maximumPoolSize`。

2. **數據庫限制**：
   - 如果規則需要訪問數據庫，請確保線程池大小不超過您的連接池大小（例如 HikariCP 的 `maximumPoolSize`）。協調這些設定。

3. **動態計算**：
   - 使用 `Runtime.getRuntime().availableProcessors()` 動態設定核心線程數：
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // 在 8 核心 CPU 上返回 8
     int corePoolSize = cores * 2; // 對於 I/O 密集型任務
     ```

4. **預先啟動線程**：
   - 調用 `executor.prestartAllCoreThreads()` 預先初始化所有核心線程，避免延遲建立。

---

### 結論

對於運行 I/O 密集型任務（例如您的驗證規則涉及數據庫訪問）的 8 核心 CPU：
- 使用 `ThreadPoolExecutor`，設定 `corePoolSize = 16`、`maximumPoolSize = 20`，並使用有界隊列（例如 `ArrayBlockingQueue(100)`）。
- 將其整合為 Spring Bean 以便依賴注入。
- 根據性能分析和數據庫限制進行調整。

此設定能平衡並行性、資源使用和系統穩定性，非常適合您的使用場景。如果您需要協助將此整合到特定專案中，請告訴我！