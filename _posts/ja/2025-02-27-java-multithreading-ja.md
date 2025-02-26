---
audio: false
lang: ja
layout: post
title: Java マルチスレッド
translated: true
---

Javaのマルチスレッドと`Executor`フレームワークの効果的な使用方法について深掘りしていきましょう。マルチスレッドは、プログラムが複数のタスクを並行して実行することを可能にし、I/O待ちやCPU集約型の操作のパフォーマンスを向上させます。`Executor`フレームワークは、低レベルのスレッド作成と管理を抽象化することで、スレッド管理を簡素化します。基本的な部分から始めて、`Executor`と関連するツールの使用方法をご紹介します。

---

### 1. Javaのマルチスレッドの基本
Javaは、スレッドを作成するための2つの主要な方法を提供しています：
- **`Thread`クラスを拡張する**:
```java
class MyThread extends Thread {
    public void run() {
        System.out.println("スレッドが実行中: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // スレッドを開始
    }
}
```
- **`Runnable`インターフェースを実装する**:
```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnableが実行中: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```
- スレッドを起動するには`start()`（`run()`ではなく）を呼び出してください—`run()`は現在のスレッドでコードを実行します。

---

### 2. `Executor`を使用する理由
手動でスレッドを作成することは、簡単な場合には機能しますが、多くのタスクを管理するためには非効率です（例：スレッドのオーバーヘッド、リソースの枯渇）。`Executor`フレームワーク（Java 5で`java.util.concurrent`に導入）は、スレッドプールとタスク管理システムを提供し、マルチスレッドをよりクリーンでスケーラブルにします。

---

### 3. `ExecutorService`の使用
`ExecutorService`インターフェース（`Executor`のサブインターフェース）は、使用するためのツールです。以下にその使用方法を示します：

#### ステップ1: `ExecutorService`を作成する
`Executors`ユーティリティクラスを使用してスレッドプールを作成します：
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 4スレッドの固定スレッドプール
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // タスクを送信
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("タスクが実行されました: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // 作業をシミュレート
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // エグゼキュータをシャットダウン
        executor.shutdown(); // 新しいタスクを防ぎ、既存のタスクが完了するまで待機
    }
}
```
- `newFixedThreadPool(4)`は4スレッドのプールを作成します。余剰のタスクはキューに待機します。
- `submit()`は`Runnable`または`Callable`タスクを受け入れます（`Callable`は結果を返します）。

#### 一般的なエグゼキュータの種類
- `Executors.newSingleThreadExecutor()`: 1スレッド、タスクを順次処理します。
- `Executors.newCachedThreadPool()`: 必要に応じてスレッドを作成し、アイドル状態のスレッドを再利用します（短期間のタスクに適しています）。
- `Executors.newScheduledThreadPool(n)`: 遅延や周期性のあるタスクをスケジュールするために使用します。

---

### 4. `Callable`と`Future`を使用して結果を処理する
タスクの結果が必要な場合は、`Runnable`の代わりに`Callable`を使用します：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Callableタスクを送信
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // タスクが実行中に他の作業を行う
        System.out.println("タスクが送信されました...");

        // 結果を取得（タスクが完了するまでブロック）
        Integer result = future.get();
        System.out.println("結果: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()`は結果を取得し、タスクが完了するまでブロックします。
- `future.isDone()`を使用して、ブロックせずに完了を確認します。

---

### 5. 高度なスレッドプールの調整
リアルワールドのアプリケーションでは、カスタム`ThreadPoolExecutor`が必要になるかもしれません：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // カスタムスレッドプール: 2-4スレッド、キューの容量は10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // コアプールサイズ
            4, // 最大プールサイズ
            60L, // アイドルスレッドのタイムアウト
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // タスクキュー
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("タスクが実行されました: " + Thread.currentThread().getName());
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
- コアサイズ（2）: 最小限のスレッド数。
- 最大サイズ（4）: キューが満杯の場合の最大スレッド数。
- キュー: すべてのスレッドが忙しいときにタスクを保持します。

---

### 6. ベストプラクティス
- **適切にシャットダウンする**: リソースリークを防ぐために、`shutdown()`または`shutdownNow()`を必ず呼び出してください。
- **割り込みを処理する**: ループ内で`Thread.currentThread().isInterrupted()`を確認してください。
- **オーバーロードを避ける**: 多すぎるスレッドはパフォーマンスを低下させます—CPUコアに基づいてプールサイズを調整してください（例：`Runtime.getRuntime().availableProcessors()`）。
- `ExecutorService`で`try-finally`を使用する：
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // タスクを送信
} finally {
    executor.shutdown();
}
```

---

### Log4jを使用した例（まとめ）
マルチスレッドを先ほどのLog4jの質問と組み合わせる：
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
                logger.info("タスク {} が {} によって開始されました", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("タスク {} が中断されました", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("タスク {} が完了しました", taskId);
            });
        }

        executor.shutdown();
    }
}
```
先ほどの`log4j2.xml`を使用すると、このコードはタスクの進行状況をコンソールとファイルにログに記録します。