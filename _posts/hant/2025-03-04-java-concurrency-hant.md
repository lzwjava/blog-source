---
audio: false
generated: true
lang: hant
layout: post
title: Java 並行處理
translated: true
type: note
---

### 重點摘要
- `java.util.concurrent` 套件能協助管理 Java 中的多重任務，讓程式執行更快速且回應更靈敏。
- 使用 `ExecutorService` 似乎是處理執行緒的常見方式，可讓您在背景執行任務。
- 研究顯示並行集合（如 `ConcurrentHashMap`）具備執行緒安全性，能確保多個執行緒安全地存取資料。
- 證據傾向使用同步工具（如 `Lock`）來比傳統方法更精確地控制共享資源。

### Java 實用並行套件簡介
`java.util.concurrent` 套件是 Java 標準程式庫的一部分，旨在簡化同時執行多個任務的程式撰寫。這對於提升效能特別有幫助，尤其是在配備多核心的現代電腦上。

### 使用 ExecutorService
`ExecutorService` 是管理執行緒的關鍵工具。它讓您建立執行緒池並提交任務在背景執行。例如，您可以設定執行緒池並執行會回傳結果的任務，然後等待它們完成。

### 並行集合
此套件包含具執行緒安全性的集合，例如 `ConcurrentHashMap`，多個執行緒可同時讀寫而不會發生衝突。這與一般集合不同，後者可能需要額外的同步處理。

### 同步工具
像 `Lock` 和 `Condition` 這樣的工具，比 `synchronized` 關鍵字提供更多彈性。它們有助於控制對共享資源的存取，確保一次只有一個執行緒能修改資料。

---

### 調查筆記：Java 實用並行套件使用全面指南

本節詳細探討 `java.util.concurrent` 套件，擴展重點摘要內容，並為需要在 Java 中實作並行程式設計的使用者提供完整指南。內容結構仿照專業文章，確保涵蓋初步分析的所有相關細節，並增加技術理解的深度。

#### Java 並行與 `java.util.concurrent` 套件概覽
Java 中的並行能讓多個任務並行執行，提升應用程式效能與回應靈敏度，特別是在多核心處理器上。`java.util.concurrent` 套件於 Java 5 引入，是 Java 標準程式庫的關鍵組成部分，提供一系列類別與介面來簡化並行程式設計。此套件解決了執行緒管理、同步與資料共享的挑戰，這些以往需手動處理，且常導致複雜易錯的程式碼。

此套件包含執行緒池、並行資料結構與同步輔助工具等公用程式，讓開發可擴展且高效能的應用程式更加容易。例如，現代應用程式（如網頁伺服器）受益於同時處理多個請求，而此套件提供了有效實現此目標的工具。

#### 關鍵元件與其用法

##### ExecutorService：高效管理執行緒
`ExecutorService` 是管理執行緒執行的核心介面，提供高階 API 來處理執行緒池與非同步任務執行。它抽象化了執行緒的建立與管理，讓開發者能專注於任務邏輯而非執行緒生命週期管理。

要使用 `ExecutorService`，您可以使用 `Executors` 類別的工廠方法建立執行緒池，例如 `newFixedThreadPool`、`newCachedThreadPool` 或 `newSingleThreadExecutor`。以下範例展示其用法：

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        // 建立包含 2 個執行緒的固定執行緒池
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // 提交任務給執行器
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
            // 等待任務完成並取得結果
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

此範例展示如何建立執行緒池、透過 `Future` 提交會回傳結果的任務，並確保正確關閉。`Future` 物件讓您檢查任務是否完成並取得其結果，同時適當處理例外。這對於非同步程式設計特別有用，例如處理交易或處理請求等任務可獨立執行。

##### 並行集合：具執行緒安全性的資料結構
並行集合是標準 Java 集合的執行緒安全實作，專為多執行緒環境設計。範例包括 `ConcurrentHashMap`、`ConcurrentSkipListMap`、`ConcurrentSkipListSet`、`CopyOnWriteArrayList` 與 `CopyOnWriteArraySet`。這些集合無需外部同步處理，降低了死結風險並提升效能。

例如，`ConcurrentHashMap` 是 `HashMap` 的執行緒安全替代方案，允許多個執行緒同時讀寫而不阻塞。以下為範例：

```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

        map.put("apple", 1);
        map.put("banana", 2);

        // 多個執行緒可安全地讀寫此映射
        Thread t1 = new Thread(() -> {
            map.put("cherry", 3);
        });

        Thread t2 = new Thread(() -> {
            System.out.println(map.get("apple"));
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

此範例展示 `ConcurrentHashMap` 如何被多個執行緒存取而無需額外同步，使其非常適合需要頻繁並行讀寫操作的場景，例如快取系統。

##### 同步工具：超越 `synchronized`
此套件包含同步工具如 `Lock`、`ReentrantLock`、`Condition`、`CountDownLatch`、`Semaphore` 與 `Phaser`，提供比 `synchronized` 關鍵字更多的彈性。這些工具對於協調執行緒存取共享資源與管理複雜同步情境至關重要。

例如，`ReentrantLock` 提供更彈性的鎖定機制，允許更精細地控制鎖定與解鎖操作。以下為範例：

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // 關鍵區段
            System.out.println("執行某些操作");
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

此範例展示如何使用 `Lock` 來同步存取關鍵區段，確保一次只有一個執行緒執行。與 `synchronized` 不同，`Lock` 允許更進階的功能，例如計時鎖與可中斷鎖，這在需要處理逾時或中斷的場景中非常有用。

其他工具包括：
- **CountDownLatch**：一種同步輔助工具，允許一個或多個執行緒等待其他執行緒中的一組操作完成。例如，可用於確保所有工作執行緒完成後才繼續。
- **Semaphore**：透過維護可用許可數來控制對共享資源的存取，適用於限制存取資源的執行緒數量，例如資料庫連線。
- **Phaser**：一種可重複使用的屏障，用於協調執行緒的階段，適用於具有多個執行階段的應用程式，例如迭代演算法。

#### 其他工具與最佳實踐
此套件還包含原子類別如 `AtomicInteger`、`AtomicLong` 與 `AtomicReference`，它們為變數提供原子操作，確保執行緒安全而無需鎖定。例如：

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

        System.out.println("最終計數: " + example.getCount());
    }
}
```

此範例展示 `AtomicInteger` 如何安全地從多個執行緒遞增計數器，避免競爭條件而無需明確同步。

最佳實踐包括：
- 始終使用 `shutdown()` 或 `shutdownNow()` 關閉 `ExecutorService`，以防資源洩漏。
- 在讀取密集的場景中，使用並行集合而非同步集合以獲得更好效能。
- 使用 `Future.get()` 處理提交給 `ExecutorService` 的任務中的例外，該方法可能拋出 `ExecutionException`。

#### 比較分析：傳統與並行方法
為突顯優點，請考慮使用傳統執行緒與 `java.util.concurrent` 套件的差異。傳統方法通常涉及手動建立 `Thread` 實例與管理同步，這可能導致樣板程式碼與死結等錯誤。相比之下，此套件提供高階抽象，降低複雜度並提升可維護性。

例如，手動同步 `HashMap` 需使用 `Collections.synchronizedMap` 包裝，但仍可能導致競爭問題。然而，`ConcurrentHashMap` 使用細粒度鎖定，允許並行讀寫，這對於習慣傳統同步方法的人來說是個意想不到的細節。

#### 進一步學習資源
對於想深入理解的使用者，有以下資源可供參考：
- 官方 [Oracle Java 並行教學](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)提供詳細文件與範例。
- [Baeldung 的 java.util.concurrent 概覽](https://www.baeldung.com/java-util-concurrent)提供實用指南與程式碼片段。
- [Jenkov 的 Java 並行工具](https://jenkov.com/tutorials/java-util-concurrent/index.html)包含一系列深入涵蓋每個元件的教學。

這些資源截至 2025 年 3 月為最新，確保使用者能取得實作 Java 並行程式設計的最新資訊。

#### 表格：`java.util.concurrent` 關鍵類別比較

| 類別/介面           | 用途                                       | 範例使用場景                     |
|---------------------|--------------------------------------------|----------------------------------|
| `ExecutorService`   | 管理執行緒池與任務執行                     | 執行多個 HTTP 請求              |
| `ConcurrentHashMap` | 具執行緒安全性的雜湊映射                   | 在網頁應用程式中快取資料        |
| `ReentrantLock`     | 彈性鎖定機制                               | 保護關鍵區段                    |
| `CountDownLatch`    | 等待多個操作完成                           | 確保所有執行緒完成設定          |
| `Semaphore`         | 控制對共享資源的存取                       | 限制資料庫連線池                |

此表格總結主要用途，有助於針對特定並行需求選擇合適工具。

總而言之，`java.util.concurrent` 套件對於現代 Java 開發至關重要，為並行程式設計提供穩健工具。透過利用這些公用程式，開發者能建構高效能、可擴展的應用程式，以滿足當代運算環境的需求。

#### 主要引用文獻
- [Oracle Java 教學並行摘要](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)
- [Baeldung java.util.concurrent 概覽](https://www.baeldung.com/java-util-concurrent)
- [Jenkov Java 並行工具索引](https://jenkov.com/tutorials/java-util-concurrent/index.html)