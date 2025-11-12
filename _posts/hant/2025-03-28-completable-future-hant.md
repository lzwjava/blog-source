---
audio: false
generated: true
lang: hant
layout: post
title: Java中的CompletableFuture
translated: true
type: note
---

在 Java Spring Boot 專案中，沒有直接對應於 JavaScript `Promise.all` 的功能，該功能可等待多個 promise 完成並提供其結果。然而，您可以使用 `java.util.concurrent` 套件中的 `CompletableFuture`，特別是 `CompletableFuture.allOf` 方法，實現類似的功能——在 for 迴圈中並行執行多個任務，並在所有執行緒完成後使用其結果。這種方法非常適合 Spring Boot 專案，尤其是與 Spring 的非同步程式設計功能結合使用。以下我將逐步說明如何實現，包括完整範例。

### 為什麼選擇 `CompletableFuture`？
`CompletableFuture`（Java 8 引入）允許您執行非同步操作並管理其完成狀態。`allOf` 方法接受多個 `CompletableFuture` 實例，並返回一個新的 `CompletableFuture`，該 future 在所有給定的 future 完成時完成，這使其非常適合您的情境，即您希望：
- 在 for 迴圈中並行執行任務。
- 等待所有任務完成。
- 之後使用結果。

### 實現步驟
以下是在 Spring Boot 專案中結構化解決方案的方法：

1. **定義非同步任務**  
   您的 for 迴圈的每個迭代代表一個可以獨立運行的任務。這些任務將返回 `CompletableFuture` 實例，代表其最終結果。

2. **收集 Future**  
   在迴圈中建立所有 `CompletableFuture` 物件時，將它們儲存在一個列表中。

3. **等待所有任務完成**  
   使用 `CompletableFuture.allOf` 將所有 future 合併為一個 future，該 future 在所有任務完成時完成。

4. **檢索並使用結果**  
   所有任務完成後，從每個 `CompletableFuture` 中提取結果並按需處理。

5. **處理異常**  
   考慮任務執行期間可能出現的錯誤。

### 範例實現
假設您有一個需要並行處理的項目列表（例如，呼叫服務或執行某些計算）。以下是兩種方法：一種使用 Spring 的 `@Async` 註解，另一種使用 `CompletableFuture.supplyAsync`。

#### 方法 1：使用 Spring 的 `@Async`
Spring Boot 提供 `@Async` 註解以非同步方式運行方法。您需要在應用程式中啟用非同步支援。

**步驟 1：啟用非同步支援**
在配置類別或主應用程式類別中添加 `@EnableAsync` 註解：

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**步驟 2：定義帶有非同步方法的服務**
建立一個服務，其中包含非同步處理每個項目方法：

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // 模擬某些工作（例如 I/O 或計算）
        try {
            Thread.sleep(1000); // 1 秒延遲
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**步驟 3：在控制器或服務中處理項目**
在您的控制器或另一個服務中，使用 for 迴圈提交任務並等待所有結果：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // 用於保存所有 future 的列表
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // 在 for 迴圈中提交每個任務
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // 等待所有任務完成
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // 阻塞直到所有任務完成
        allFutures.join();

        // 收集結果
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // 獲取每個結果
            .collect(Collectors.toList());

        return results;
    }
}
```

**使用範例：**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // 輸出：[Processed: Item1, Processed: Item2, Processed: Item3]
```

#### 方法 2：使用 `CompletableFuture.supplyAsync`
如果您不想使用 `@Async`，可以使用 `Executor` 和 `CompletableFuture.supplyAsync` 手動管理執行緒。

**步驟 1：配置執行緒池**
定義一個 `TaskExecutor` bean 以控制執行緒池：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // 池中保留的執行緒數
        executor.setMaxPoolSize(10);    // 最大執行緒數
        executor.setQueueCapacity(25);  // 待處理任務的隊列容量
        executor.initialize();
        return executor;
    }
}
```

**步驟 2：使用 `supplyAsync` 處理項目**
使用執行器非同步運行任務：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // 使用 supplyAsync 建立 future
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // 等待所有任務完成
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // 收集結果
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // 模擬某些工作
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### 關鍵點
- **等待完成**：`CompletableFuture.allOf(...).join()` 或 `.get()` 確保主執行緒等待所有任務完成。使用 `join()` 可避免處理受檢異常；如果任務失敗，它會拋出 `CompletionException`。
- **異常處理**：如果需要處理異常，請將 `.join()` 或 `.get()` 呼叫包在 try-catch 區塊中：

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // 處理中斷
} catch (ExecutionException e) {
    // 處理任務失敗
    e.printStackTrace();
}
```

- **執行緒池配置**：根據您的工作負載調整執行緒池大小。對於 I/O 密集型任務（例如資料庫呼叫、API 請求），較大的池（例如 5–10 個執行緒）是合適的。對於 CPU 密集型任務，匹配 CPU 核心數量（例如 `Runtime.getRuntime().availableProcessors()`）。
- **結果順序**：由於 future 是按照迴圈順序收集的，因此結果保持輸入列表的順序。

### 選擇哪種方法？
- **使用 `@Async`**：如果您的任務自然屬於 Spring 服務的一部分，並且您希望 Spring 管理執行緒。這種方法更簡潔，並與 Spring Boot 良好整合。
- **使用 `supplyAsync`**：如果您需要更多控制任務執行，或不想依賴 Spring 的非同步框架。

### 最終答案
要在 Java Spring Boot 專案中複製 `Promise.all` 的功能，用於 for 迴圈作業，在多重執行緒執行後使用執行緒結果，請使用帶有 `CompletableFuture` 實例列表的 `CompletableFuture.allOf`。建議使用帶有 Spring 的 `@Async` 方法以簡化操作，但使用自定義執行器的 `supplyAsync` 也可以。上述帶有 `@Async` 的範例演示了這一點：

- 使用 `@Async` 方法在 for 迴圈中建立 `CompletableFuture` 實例。
- 使用 `CompletableFuture.allOf` 等待所有任務。
- 完成後收集並使用結果。

這確保所有任務並行運行，並且您可以在它們全部完成後處理其結果，有效滿足您的需求。