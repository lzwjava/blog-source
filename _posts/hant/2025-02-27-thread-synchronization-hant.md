---
audio: true
generated: true
lang: hant
layout: post
title: Java 同步執行緒
translated: true
---

讓我們深入探討 Java 中的線程同步！當多個線程訪問共享資源（如變量、集合或文件）時，您需要防止競爭條件——線程相互干擾，導致不可預測的結果。Java 提供了幾種工具來實現這一點：`synchronized`、`Lock` 和 `Semaphore`。我將解釋每一種，展示範例，並進行比較，以便您能夠選擇最適合您需求的工具。

---

### 1. `synchronized` 關鍵字
`synchronized` 關鍵字確保只有一個線程可以執行一段代碼或方法。它是最簡單的同步工具，內建於 Java 的核心。

#### 運作方式
- 鎖定一個對象的監視器（每個 Java 對象都有一個）。
- 其他線程等待直到鎖被釋放。

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

        System.out.println("最終計數: " + counter.getCount()); // 總是 2000
    }
}
```
- 如果沒有 `synchronized`，`count++`（讀取-修改-寫入）可能會重疊，結果小於 2000。
- `synchronized` 鎖定 `Counter` 實例，確保原子更新。

#### 同步區塊
您也可以鎖定特定的代碼而不是整個方法：
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- 如果您想要更細粒度的控制，可以使用不同的對象作為鎖：
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### 優缺點
- **優點**：簡單，內建，適合基本用途。
- **缺點**：沒有靈活性（例如，無法中斷等待的線程），直到釋放才解鎖。

---

### 2. `Lock` 接口 (java.util.concurrent.locks)
`Lock` 接口（例如 `ReentrantLock`）提供比 `synchronized` 更多的控制。它是 `java.util.concurrent` 套件的一部分，旨在解決 `synchronized` 的局限性。

#### 主要特點
- 顯式的 `lock()` 和 `unlock()` 调用。
- 支持試鎖、超時和可中斷鎖定。
- 公平選項（線程按順序等待）。

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
            lock.unlock(); // 總是在 finally 中解鎖
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

        System.out.println("最終計數: " + counter.getCount()); // 總是 2000
    }
}
```
- `try-finally` 確保即使發生異常也會釋放鎖。

#### 高級特點
- **試鎖**：非阻塞嘗試獲取鎖：
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("無法獲取鎖");
}
```
- **超時**：等待有限時間：
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **可中斷**：允許等待的線程被中斷：
```java
lock.lockInterruptibly();
```

#### 優缺點
- **優點**：靈活，支持高級特點，顯式控制。
- **缺點**：更冗長，需要手動解鎖（忘記解鎖的風險）。

---

### 3. `Semaphore`
`Semaphore` 通過維護一組許可來控制對資源的訪問。它非常適合限制並發（例如，最多 5 個線程可以訪問一個資源）。

#### 運作方式
- 線程通過 `acquire()` 获取許可。
- 通過 `release()` 釋放許可。
- 如果沒有可用的許可，線程等待。

#### 範例：限制數據庫連接
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // 最多 3 個連接

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " 已連接");
            Thread.sleep(1000); // 模擬工作
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " 已斷開連接");
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
- 只能有 3 個線程“連接”；其他線程等待直到釋放許可。

#### 高級特點
- **公平性**：`new Semaphore(3, true)` 確保 FIFO 順序。
- **試獲取**：`semaphore.tryAcquire()` 進行檢查而不阻塞。

#### 優缺點
- **優點**：適合資源池，靈活的許可系統。
- **缺點**：比 `synchronized` 或 `Lock` 更複雜，不適合簡單的互斥。

---

### 與 `ExecutorService` 結合
這是這些工具如何與線程池一起工作的：
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
        System.out.println("最終值: " + resource.getValue()); // 總是 1000
    }
}
```

---

### 比較
| 特點            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| 易用性        | 高                | 中等                | 低                |
| 靈活性        | 低                 | 高                  | 中等             |
| 粒度        | 方法/區塊        | 顯式              | 基於許可       |
| 可中斷      | 否                  | 是                   | 是                |
| 公平選項    | 否                  | 是                   | 是                |
| 用例           | 簡單互斥 | 高級控制 | 資源限制 |

---

### 何時使用什麼？
- **`synchronized`**：快速、簡單的互斥（例如，保護單個變量）。
- **`Lock`**：需要試鎖、超時或可中斷（例如，複雜的工作流）。
- **`Semaphore`**：限制對資源的並發訪問（例如，連接池、速率限制）。