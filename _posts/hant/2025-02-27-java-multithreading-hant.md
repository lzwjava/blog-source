---
audio: false
generated: true
lang: hant
layout: post
title: Java 多線程編程
translated: true
type: note
---

讓我們深入探討 Java 多執行緒以及如何有效使用 `Executor` 框架。多執行緒能讓你的程式同時執行多個任務，從而提升 I/O 密集型或 CPU 密集型操作的效能。`Executor` 框架透過抽象化底層的執行緒建立與處理，簡化了執行緒管理。我將先介紹基礎知識，然後示範如何使用 `Executor` 及相關工具。

---

### 1. Java 多執行緒基礎
Java 提供兩種主要的建立執行緒方式：
- **繼承 `Thread` 類別**：

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // 啟動執行緒
    }
}
```

- **實作 `Runnable` 介面**：

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

- 呼叫 `start()`（而非 `run()`）來啟動執行緒——`run()` 僅會在當前執行緒中執行程式碼。

---

### 2. 為何使用 `Executor`？
手動建立執行緒在簡單情況下可行，但管理大量任務時效率低下（例如執行緒開銷、資源耗盡）。`Executor` 框架（於 Java 5 在 `java.util.concurrent` 下引入）提供了執行緒池與任務管理系統，使多執行緒更清晰且更具擴展性。

---

### 3. 使用 `ExecutorService`
`ExecutorService` 介面（`Executor` 的子介面）是首選工具。以下是使用方式：

#### 步驟 1：建立 ExecutorService
使用 `Executors` 工具類別建立執行緒池：
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 建立具有 4 個執行緒的固定執行緒池
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // 提交任務
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // 模擬工作
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // 關閉執行器
        executor.shutdown(); // 防止新任務，等待現有任務完成
    }
}
```
- `newFixedThreadPool(4)` 建立一個包含 4 個執行緒的池。超出的任務會在佇列中等待。
- `submit()` 接受 `Runnable` 或 `Callable` 任務（`Callable` 會回傳結果）。

#### 常見的 Executor 類型
- `Executors.newSingleThreadExecutor()`：單一執行緒，依序處理任務。
- `Executors.newCachedThreadPool()`：按需建立執行緒，重用空閒執行緒（適用於短暫任務）。
- `Executors.newScheduledThreadPool(n)`：用於排程具有延遲或週期性的任務。

---

### 4. 使用 `Callable` 和 `Future` 處理結果
若需要任務結果，請使用 `Callable` 而非 `Runnable`：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // 提交 Callable 任務
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // 在任務執行時進行其他工作
        System.out.println("Task submitted...");

        // 取得結果（會阻塞直到完成）
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` 取得結果，若任務未完成會阻塞。
- 使用 `future.isDone()` 在不阻塞的情況下檢查是否完成。

---

### 5. 進階：執行緒池調校
對於實際應用，你可能需要自訂 `ThreadPoolExecutor`：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // 自訂執行緒池：2-4 個執行緒，佇列容量為 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // 核心池大小
            4, // 最大池大小
            60L, // 空閒執行緒逾時時間
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // 任務佇列
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("Task by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        executor.shutdown();
    }
}
```
- 核心大小（2）：保持存活的最小執行緒數。
- 最大大小（4）：當佇列已滿時的最大執行緒數。
- 佇列：在所有執行緒忙碌時容納任務。

---

### 6. 最佳實踐
- **正確關閉**：始終呼叫 `shutdown()` 或 `shutdownNow()` 以避免資源洩漏。
- **處理中斷**：在迴圈中檢查 `Thread.currentThread().isInterrupted()`。
- **避免過載**：過多執行緒可能降低效能——根據 CPU 核心數調整池大小（例如 `Runtime.getRuntime().availableProcessors()`）。
- **搭配 `ExecutorService` 使用 `try-finally`**：
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // 提交任務
} finally {
    executor.shutdown();
}
```

---

### 結合 Log4j 的範例（整合應用）
將多執行緒與你之前關於 Log4j 的問題結合：
```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.concurrent.*;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                logger.info("Task {} started by {}", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("Task {} interrupted", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("Task {} completed", taskId);
            });
        }

        executor.shutdown();
    }
}
```
搭配之前的 `log4j2.xml`，此程式會將任務進度記錄到控制台和檔案中。