---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおけるスレッド同期
translated: true
type: note
---

Javaでのスレッド同期について詳しく見ていきましょう！複数のスレッドが（変数、コレクション、ファイルなどの）共有リソースにアクセスする場合、スレッドが互いに干渉して予測不能な結果を招く競合状態を防ぐ必要があります。Javaではこのためにいくつかのツールを提供しています：`synchronized`、`Lock`、そして`Semaphore`です。それぞれを説明し、例を示し、比較するので、あなたのニーズに合ったものを選べるようにします。

---

### 1. `synchronized` キーワード
`synchronized`キーワードは、一度に一つのスレッドだけがコードブロックやメソッドを実行できるようにします。Javaのコアに組み込まれた、最もシンプルな同期ツールです。

#### 仕組み
- オブジェクトのモニターをロックします（すべてのJavaオブジェクトが持っています）。
- 他のスレッドはロックが解除されるまで待機します。

#### 例: `synchronized`を使ったカウンター
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

        System.out.println("Final count: " + counter.getCount()); // 常に 2000
    }
}
```
- `synchronized`なしでは、`count++`（読み取り-変更-書き込み）が重複する可能性があり、結果が2000未満になることがあります。
- `synchronized`は`Counter`インスタンスをロックし、アトミックな更新を保証します。

#### 同期ブロック
メソッド全体ではなく特定のコードをロックすることもできます：
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- より細かい制御が必要な場合は、別のオブジェクトをロックとして使用します：
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### 長所と短所
- **長所**: シンプル、組み込み、基本的な使用に適している。
- **短所**: 柔軟性がない（例：待機中のスレッドを中断できない）、解放されるまでブロックする。

---

### 2. `Lock` インターフェース (java.util.concurrent.locks)
`Lock`インターフェース（例：`ReentrantLock`）は、`synchronized`よりも多くの制御を提供します。`java.util.concurrent`パッケージの一部であり、`synchronized`の制限に対処するために導入されました。

#### 主な機能
- 明示的な`lock()`と`unlock()`の呼び出し。
- トライロック、タイムアウト、中断可能なロックをサポート。
- 公平性オプション（スレッドが順番待ち）。

#### 例: `ReentrantLock`を使ったカウンター
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
            lock.unlock(); // finallyブロックで常にアンロック
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

        System.out.println("Final count: " + counter.getCount()); // 常に 2000
    }
}
```
- `try-finally`により、例外が発生してもロックが確実に解放されます。

#### 高度な機能
- **トライロック**: 非ブロッキングでロックの取得を試みる：
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
- **タイムアウト**: 限られた時間だけ待機する：
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **中断可能**: 待機中のスレッドが中断されることを許可する：
```java
lock.lockInterruptibly();
```

#### 長所と短所
- **長所**: 柔軟、高度な機能をサポート、明示的な制御。
- **短所**: より冗長、手動でのアンロックが必要（忘れるリスクあり）。

---

### 3. `Semaphore`
`Semaphore`は、一連の許可を管理することでリソースへのアクセスを制御します。同時実行性を制限する（例：最大5スレッドがあるリソースにアクセス可能）のに最適です。

#### 仕組み
- スレッドは`acquire()`で許可を取得します。
- `release()`で許可を解放します。
- 利用可能な許可がない場合、スレッドは待機します。

#### 例: データベース接続の制限
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // 最大3接続

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " が接続しました");
            Thread.sleep(1000); // 作業をシミュレート
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " が切断しました");
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
- 同時に3つのスレッドだけが「接続」できます。他は許可が解放されるまで待機します。

#### 高度な機能
- **公平性**: `new Semaphore(3, true)`はFIFO順を保証します。
- **トライアクワイア**: `semaphore.tryAcquire()`はブロックせずに確認します。

#### 長所と短所
- **長所**: リソースプールに理想的、柔軟な許可システム。
- **短所**: `synchronized`や`Lock`よりも複雑、単純な相互排他には向かない。

---

### `ExecutorService`との組み合わせ
これらのツールがスレッドプールでどのように動作するかを示します：
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
        System.out.println("Final value: " + resource.getValue()); // 常に 1000
    }
}
```

---

### 比較

| 特徴             | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|------------------|----------------------|------------------------|---------------------|
| 使いやすさ       | 高い                | 中程度                | 低い               |
| 柔軟性           | 低い                 | 高い                  | 中程度             |
| 粒度             | メソッド/ブロック   | 明示的                | 許可ベース         |
| 中断可能         | いいえ              | はい                   | はい                |
| 公平性オプション | いいえ              | はい                   | はい                |
| 使用例           | 単純な相互排他      | 高度な制御            | リソース制限       |

---

### いつ何を使うべき？
- **`synchronized`**: 迅速でシンプルな相互排他（例：単一変数の保護）。
- **`Lock`**: トライロック、タイムアウト、または中断可能性が必要な場合（例：複雑なワークフロー）。
- **`Semaphore`**: リソースへの同時アクセスを制限する場合（例：接続プール、レート制限）。