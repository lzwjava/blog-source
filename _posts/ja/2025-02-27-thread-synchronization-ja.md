---
audio: true
generated: true
lang: ja
layout: post
title: スレッド同期のJava
translated: true
---

Javaのスレッド同期に飛び込みましょう！複数のスレッドが共有リソース（変数、コレクション、ファイルなど）にアクセスする場合、競合条件を防ぐ必要があります。競合条件とは、スレッドがお互いに干渉し、予測不可能な結果を引き起こすことです。Javaにはこのためのいくつかのツールがあります：`synchronized`、`Lock`、および`Semaphore`です。それぞれを説明し、例を示し、比較して、あなたのニーズに最適なものを選ぶ手助けをします。

---

### 1. `synchronized` キーワード
`synchronized` キーワードは、一度に1つのスレッドのみがコードブロックまたはメソッドを実行できるようにします。これは、Javaのコアに組み込まれた最も簡単な同期ツールです。

#### 仕組み
- オブジェクトのモニタをロックします（すべてのJavaオブジェクトには1つあります）。
- 他のスレッドはロックが解放されるまで待機します。

#### 例：`synchronized`を使ったカウンター
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

        System.out.println("最終カウント: " + counter.getCount()); // いつも2000
    }
}
```
- `synchronized`なしでは、`count++`（読み取り-修正-書き込み）が重なり、2000未満の結果になる可能性があります。
- `synchronized`は`Counter`インスタンスをロックし、原子的な更新を保証します。

#### 同期ブロック
特定のコードをロックすることもできます：
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- より細かい制御が必要な場合は、異なるオブジェクトをロックとして使用します：
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### 利点と欠点
- **利点**：簡単、組み込み、基本的な使用に適しています。
- **欠点**：柔軟性がない（例：待機中のスレッドを中断できない）、解放されるまでブロックします。

---

### 2. `Lock` インターフェース (java.util.concurrent.locks)
`Lock` インターフェース（例：`ReentrantLock`）は、`synchronized`よりもより多くの制御を提供します。これは`java.util.concurrent`パッケージの一部であり、`synchronized`の制限を解決するために導入されました。

#### 主要な機能
- 明示的な`lock()`および`unlock()`呼び出し。
- トライロック、タイムアウト、中断可能なロックのサポート。
- 公平性オプション（スレッドは順番に待機します）。

#### 例：`ReentrantLock`を使ったカウンター
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
            lock.unlock(); // 例外が発生しても必ず解除
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

        System.out.println("最終カウント: " + counter.getCount()); // いつも2000
    }
}
```
- `try-finally`は、例外が発生してもロックが解放されることを保証します。

#### 高度な機能
- **トライロック**：非ブロックのロック取得の試み：
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("ロックを取得できませんでした");
}
```
- **タイムアウト**：制限時間を待ちます：
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **中断可能**：待機中のスレッドを中断可能：
```java
lock.lockInterruptibly();
```

#### 利点と欠点
- **利点**：柔軟、高度な機能をサポート、明示的な制御。
- **欠点**：冗長、手動で解除が必要（忘れるリスクがある）。

---

### 3. `Semaphore`
`Semaphore`は、パーミットを維持することでリソースへのアクセスを制御します。これは、リソースへの同時アクセスを制限するのに最適です（例：最大5つのスレッドがリソースにアクセス）。

#### 仕組み
- スレッドは`acquire()`でパーミットを取得します。
- `release()`でパーミットを解放します。
- パーミットが利用できない場合、スレッドは待機します。

#### 例：データベース接続の制限
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // 最大3つの接続

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " 接続");
            Thread.sleep(1000); // 作業をシミュレート
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " 切断");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ConnectionPool pool = new ConnectionPool();
        Runnable task = () -> pool.connect();

        Thread[] threads = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threads[i] = new Thread(task, "スレッド-" + i);
            threads[i].start();
        }
    }
}
```
- 1つのスレッドが「接続」できるのは3つまでで、他のスレッドはパーミットが解放されるまで待機します。

#### 高度な機能
- **公平性**：`new Semaphore(3, true)`はFIFO順序を保証します。
- **トライアクワイア**：`semaphore.tryAcquire()`はブロックせずに確認します。

#### 利点と欠点
- **利点**：リソースプールに最適、柔軟なパーミットシステム。
- **欠点**：`synchronized`や`Lock`よりも複雑、単純な相互排他には適していません。

---

### `ExecutorService`と組み合わせる
これらのツールがスレッドプールとどのように動作するか：
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
        System.out.println("最終値: " + resource.getValue()); // いつも1000
    }
}
```

---

### 比較
| 特徴            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| 使用のしやすさ        | 高                | 中                | 低                |
| 柔軟性        | 低                 | 高                  | 中                |
| 粒度        | メソッド/ブロック        | 明示的              | パーミットベース       |
| 中断可能      | いいえ                  | はい                   | はい                |
| 公平性オプション    | いいえ                  | はい                   | はい                |
| 使用ケース           | 単純な相互排他 | 高度な制御 | リソース制限           |

---

### どれを使うべきか？
- **`synchronized`**：迅速で簡単な相互排他（例：単一の変数の保護）。
- **`Lock`**：トライロック、タイムアウト、または中断可能性が必要な場合（例：複雑なワークフロー）。
- **`Semaphore`**：リソースへの同時アクセスを制限する場合（例：接続プール、レート制限）。