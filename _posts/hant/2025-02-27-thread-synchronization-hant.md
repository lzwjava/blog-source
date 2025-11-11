---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的線程同步
translated: true
type: note
---

讓我們深入探討 Java 中的執行緒同步！當多個執行緒存取共享資源（如變數、集合或檔案）時，你需要防止競爭條件——即執行緒相互干擾導致不可預測的結果。Java 提供了多種工具來實現這一點：`synchronized`、`Lock` 和 `Semaphore`。我將分別解釋每種工具，展示範例並進行比較，以便你能根據需求選擇合適的工具。

---

### 1. `synchronized` 關鍵字
`synchronized` 關鍵字確保同一時間只有一個執行緒能執行某段程式碼或方法。它是最簡單的同步工具，內建於 Java 核心中。

#### 運作原理
- 鎖定物件的監視器（每個 Java 物件都有一個）。
- 其他執行緒會等待鎖定被釋放。

#### 範例：使用 `synchronized` 的計數器
```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // 總是 2000
    }
}
```
- 若沒有 `synchronized`，`count++`（讀取-修改-寫入）可能會重疊執行，導致結果少於 2000。
- `synchronized` 會鎖定 `Counter` 實例，確保原子性更新。

#### 同步區塊
你也可以鎖定特定程式碼，而非整個方法：
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- 若需要更精細的控制，可使用不同物件作為鎖：
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### 優缺點
- **優點**：簡單、內建，適用於基本用途。
- **缺點**：缺乏靈活性（例如無法中斷等待中的執行緒），會一直阻塞直到釋放。

---

### 2. `Lock` 介面 (java.util.concurrent.locks)
`Lock` 介面（例如 `ReentrantLock`）提供比 `synchronized` 更多的控制。它屬於 `java.util.concurrent` 套件，旨在解決 `synchronized` 的限制。

#### 主要功能
- 明確的 `lock()` 和 `unlock()` 呼叫。
- 支援嘗試鎖定、超時和可中斷的鎖定。
- 公平性選項（執行緒按順序等待）。

#### 範例：使用 `ReentrantLock` 的計數器
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Counter {
    private int count = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock(); // 務必在 finally 中解鎖
        }
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // 總是 2000
    }
}
```
- `try-finally` 確保即使發生異常，鎖定也會被釋放。

#### 進階功能
- **嘗試鎖定**：非阻塞地嘗試獲取鎖定：
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("Couldn’t acquire lock");
}
```
- **超時**：等待有限時間：
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **可中斷**：允許等待中的執行緒被中斷：
```java
lock.lockInterruptibly();
```

#### 優缺點
- **優點**：靈活、支援進階功能、明確控制。
- **缺點**：語法較冗長、需手動解鎖（有忘記的風險）。

---

### 3. `Semaphore`
`Semaphore` 透過維護一組許可證來控制對資源的存取。它非常適合限制並發（例如最多 5 個執行緒可存取資源）。

#### 運作原理
- 執行緒透過 `acquire()` 獲取許可證。
- 透過 `release()` 釋放許可證。
- 若無可用許可證，執行緒會等待。

#### 範例：限制資料庫連線
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // 最多 3 個連線

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " connected");
            Thread.sleep(1000); // 模擬工作
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " disconnected");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ConnectionPool pool = new ConnectionPool();
        Runnable task = () -> pool.connect();

        Thread[] threads = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threads[i] = new Thread(task, "Thread-" + i);
            threads[i].start();
        }
    }
}
```
- 同時只有 3 個執行緒能「連線」；其他執行緒會等待許可證被釋放。

#### 進階功能
- **公平性**：`new Semaphore(3, true)` 確保先進先出順序。
- **嘗試獲取**：`semaphore.tryAcquire()` 非阻塞地檢查。

#### 優缺點
- **優點**：適合資源池、靈活的許可證系統。
- **缺點**：比 `synchronized` 或 `Lock` 複雜，不適用於簡單的互斥。

---

### 與 `ExecutorService` 結合使用
以下展示這些工具如何與執行緒池協作：
```java
import java.util.concurrent.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class SharedResource {
    private int value = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            value++;
        } finally {
            lock.unlock();
        }
    }

    public int getValue() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        SharedResource resource = new SharedResource();
        ExecutorService executor = Executors.newFixedThreadPool(4);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 100; j++) {
                    resource.increment();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("Final value: " + resource.getValue()); // 總是 1000
    }
}
```

---

### 比較

| 功能特點           | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| 易用性             | 高                   | 中等                   | 低                  |
| 靈活性             | 低                   | 高                     | 中等                |
| 細緻度             | 方法/區塊            | 明確控制               | 許可證基礎          |
| 可中斷性           | 否                   | 是                     | 是                  |
| 公平性選項         | 否                   | 是                     | 是                  |
| 使用場景           | 簡單互斥             | 進階控制               | 資源限制            |

---

### 何時使用哪種工具？
- **`synchronized`**：快速、簡單的互斥（例如保護單一變數）。
- **`Lock`**：需要嘗試鎖定、超時或可中斷性時（例如複雜工作流程）。
- **`Semaphore`**：限制對資源的並行存取（例如連線池、速率限制）。