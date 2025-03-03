---
audio: false
generated: true
lang: hant
layout: post
title: Java 並發
translated: true
---

### 關鍵要點
- `java.util.concurrent` 套件有助於在 Java 中管理多個任務，使程序更快且更具響應性。
- 使用 `ExecutorService` 是處理線程的常見方法，允許您在後台運行任務。
- 研究表明，像 `ConcurrentHashMap` 這樣的並發集合是線程安全的，確保多個線程可以安全地訪問數據。
- 使用同步工具如 `Lock` 可以比傳統方法更好地控制共享資源。

### Java 實用並發介紹
`java.util.concurrent` 套件是 Java 標準庫的一部分，旨在簡化編寫同時運行多個任務的程序。這對於提高性能特別有用，特別是在現代多核計算機上。

### 使用 ExecutorService
`ExecutorService` 是管理線程的關鍵工具。它讓您創建一個線程池並提交要在後台運行的任務。例如，您可以設置一個線程池並運行返回結果的任務，然後等待它們完成。

### 並發集合
這個套件包括像 `ConcurrentHashMap` 這樣的線程安全集合，多個線程可以在沒有衝突的情況下讀取和寫入。這與普通集合不同，普通集合可能需要額外的同步。

### 同步工具
像 `Lock` 和 `Condition` 這樣的工具比 `synchronized` 關鍵字提供了更多的靈活性。它們有助於控制對共享資源的訪問，確保一次只有一個線程可以修改數據。

---

### 調查筆記：使用 Java 實用並發的全面指南

這一部分提供了對 `java.util.concurrent` 套件的詳細探討，擴展了關鍵要點，並為希望在 Java 中實現並發編程的用戶提供了全面的指南。內容結構模仿專業文章，確保從初步分析中包含所有相關細節，並為技術理解提供了更多深度。

#### Java 並發及 `java.util.concurrent` 套件概述
Java 中的並發使多個任務能夠並行執行，提高應用程序的性能和響應性，特別是在多核處理器上。`java.util.concurrent` 套件於 Java 5 中引入，是 Java 標準庫的關鍵組成部分，提供了一套類和接口來促進並發編程。這個套件解決了線程管理、同步和數據共享的挑戰，這些挑戰以前是手動處理的，並經常導致複雜且容易出錯的代碼。

這個套件包括線程池、並發數據結構和同步輔助工具的實用工具，使開發可擴展和高效應用程序變得更加容易。例如，現代應用程序如 Web 伺服器從並發處理多個請求中受益，這個套件提供了有效完成這一點的工具。

#### 關鍵組件及其使用

##### ExecutorService：高效管理線程
`ExecutorService` 是管理線程執行的中心接口，提供了一個高層次的 API 來處理線程池和異步任務執行。它抽象了線程的創建和管理，讓開發者可以專注於任務邏輯，而不是線程生命週期管理。

要使用 `ExecutorService`，您可以使用 `Executors` 類的工廠方法創建一個線程池，例如 `newFixedThreadPool`、`newCachedThreadPool` 或 `newSingleThreadExecutor`。以下是展示其使用的示例：

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        // 創建一個固定線程池，包含 2 個線程
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // 提交任務到執行器
        Future<String> future1 = executor.submit(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "任務 1 完成";
        });

        Future<String> future2 = executor.submit(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "任務 2 完成";
        });

        try {
            // 等待任務完成並獲取其結果
            System.out.println(future1.get());
            System.out.println(future2.get());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 關閉執行器
            executor.shutdown();
        }
    }
}
```

這個示例展示了如何創建一個線程池，提交返回結果的任務，並確保正確關閉。`Future` 對象允許您檢查任務是否完成並檢索其結果，適當地處理異常。這對於異步編程特別有用，其中任務如處理交易或處理請求可以獨立運行。

##### 並發集合：線程安全的數據結構
並發集合是標準 Java 集合的線程安全實現，專為多線程上下文設計。例如包括 `ConcurrentHashMap`、`ConcurrentSkipListMap`、`ConcurrentSkipListSet`、`CopyOnWriteArrayList` 和 `CopyOnWriteArraySet`。這些集合消除了對外部同步的需求，減少了死鎖的風險並提高了性能。

例如，`ConcurrentHashMap` 是 `HashMap` 的線程安全替代品，允許多個線程在不阻塞的情況下並發讀取和寫入。以下是示例：

```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

        map.put("蘋果", 1);
        map.put("香蕉", 2);

        // 多個線程可以安全地讀取和寫入這個地圖
        Thread t1 = new Thread(() -> {
            map.put("櫻桃", 3);
        });

        Thread t2 = new Thread(() -> {
            System.out.println(map.get("蘋果"));
        });

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

這個示例展示了 `ConcurrentHashMap` 如何被多個線程訪問而不需要額外的同步，使其適合於頻繁進行並發讀寫操作的情況，例如在緩存系統中。

##### 同步工具：超越 `synchronized`
這個套件包括像 `Lock`、`ReentrantLock`、`Condition`、`CountDownLatch`、`Semaphore` 和 `Phaser` 這樣的同步工具，提供了比 `synchronized` 關鍵字更多的靈活性。這些工具對於協調線程訪問共享資源和管理複雜的同步情況至關重要。

例如，`ReentrantLock` 提供了一種更靈活的鎖定機制，允許對鎖定和解鎖操作進行更細粒度的控制。以下是示例：

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // 臨界區
            System.out.println("正在做某事");
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        LockExample example = new LockExample();

        Thread t1 = new Thread(() -> example.doSomething());
        Thread t2 = new Thread(() -> example.doSomething());

        t1.start();
        t2.start();
    }
}
```

這個示例展示了如何使用 `Lock` 同步訪問臨界區，確保一次只有一個線程執行它。與 `synchronized` 不同，`Lock` 允許更高級的功能，例如定時鎖和可中斷鎖，這些功能在需要超時處理或中斷的情況下非常有用。

其他工具包括：
- **CountDownLatch**：一種同步輔助工具，允許一個或多個線程等待其他線程中的一組操作完成。例如，它可以用來確保所有工作線程都完成了再繼續。
- **Semaphore**：通過維護可用許可證的計數來控制對共享資源的訪問，適合限制訪問資源的線程數量，例如數據庫連接。
- **Phaser**：一個可重用的屏障，用於協調線程的階段，適合具有多個執行階段的應用程序，例如迭代算法。

#### 額外的實用工具和最佳實踐
這個套件還包括原子類如 `AtomicInteger`、`AtomicLong` 和 `AtomicReference`，它們為變量提供了原子操作，確保線程安全而不需要鎖。例如：

```java
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicIntegerExample {
    private AtomicInteger count = new AtomicInteger(0);

    public void increment() {
        count.incrementAndGet();
    }

    public int getCount() {
        return count.get();
    }

    public static void main(String[] args) throws InterruptedException {
        AtomicIntegerExample example = new AtomicIntegerExample();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        });

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("最終計數：" + example.getCount());
    }
}
```

這個示例展示了如何從多個線程安全地增加計數器，避免競爭條件而不需要顯式同步。

最佳實踐包括：
- 使用 `shutdown()` 或 `shutdownNow()` 關閉 `ExecutorService`，以防止資源洩漏。
- 在讀取密集型情況下，使用並發集合而不是同步集合，以獲得更好的性能。
- 使用 `Future.get()` 來處理提交到 `ExecutorService` 的任務中的異常，這可能會拋出 `ExecutionException`。

#### 比較分析：傳統方法與並發方法
為了突出優勢，考慮傳統線程和 `java.util.concurrent` 套件之間的區別。傳統方法通常涉及手動創建 `Thread` 實例並管理同步，這可能會導致冗長的代碼和錯誤，如死鎖。相反，這個套件提供了高層次的抽象，減少了複雜性並提高了可維護性。

例如，手動同步 `HashMap` 需要將其包裹在 `Collections.synchronizedMap` 中，這仍然可能導致爭用問題。`ConcurrentHashMap` 使用細粒度鎖定，允許並發讀取和寫入，這是對於那些習慣於傳統同步方法的人來說意想不到的細節。

#### 進一步學習的資源
對於希望深入了解的用戶，有幾個資源可用：
- 官方的 [Oracle Java 教程並發](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html) 提供了詳細的文檔和示例。
- [Baeldung 的 java.util.concurrent 概述](https://www.baeldung.com/java-util-concurrent) 提供了實用的指南和代碼片段。
- [Jenkov 的 Java 並發實用工具](https://jenkov.com/tutorials/java-util-concurrent/index.html) 包含了一系列深入探討每個組件的教程。

這些資源，截至 2025 年 3 月，確保用戶能夠訪問最新的信息，以在 Java 中實現並發編程。

#### 表：`java.util.concurrent` 中的關鍵類的比較

| 類/接口          | 目的                                      | 示例用例                     |
|------------------|------------------------------------------|----------------------------------|
| `ExecutorService` | 管理線程池和任務執行                     | 運行多個 HTTP 請求               |
| `ConcurrentHashMap` | 線程安全的哈希表                         | Web 應用中的緩存數據             |
| `ReentrantLock`   | 靈活的鎖定機制                           | 保護臨界區                     |
| `CountDownLatch`  | 等待多個操作完成                         | 確保所有線程完成設置             |
| `Semaphore`       | 控制對共享資源的訪問                     | 限制數據庫連接池                 |

這個表總結了主要用途，有助於選擇特定並發需求的正確工具。

總結來說，`java.util.concurrent` 套件對於現代 Java 開發至關重要，提供了並發編程的強大工具。通過利用這些實用工具，開發者可以構建高效、可擴展的應用程序，滿足當前計算環境的需求。

#### 關鍵引用
- [Oracle Java 教程並發摘要](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)
- [Baeldung java.util.concurrent 概述](https://www.baeldung.com/java-util-concurrent)
- [Jenkov Java 並發實用工具索引](https://jenkov.com/tutorials/java-util-concurrent/index.html)