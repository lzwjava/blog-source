---
audio: false
generated: true
lang: ja
layout: post
title: Javaマルチスレッド
translated: true
type: note
---

Javaのマルチスレッドと`Executor`フレームワークの効果的な使い方について詳しく見ていきましょう。マルチスレッドを使用すると、プログラムで複数のタスクを同時に実行でき、I/OバウンドまたはCPU集約型の操作のパフォーマンスが向上します。`Executor`フレームワークは、低レベルのスレッド作成と処理を抽象化することで、スレッド管理を簡素化します。基本から始めて、`Executor`と関連ツールの使用方法を説明します。

---

### 1. Javaでのマルチスレッドの基本
Javaでは、主に2つの方法でスレッドを作成できます：
- **`Thread`クラスを拡張する**:

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
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

- スレッドを起動するには`run()`ではなく`start()`を呼び出します。`run()`は現在のスレッドでコードを実行するだけです。

---

### 2. `Executor`を使用する理由
単純なケースでは手動でスレッドを作成できますが、多くのタスクを管理するには非効率的です（例：スレッドのオーバーヘッド、リソース枯渇）。`Executor`フレームワーク（Java 5で`java.util.concurrent`に導入）は、スレッドプールとタスク管理システムを提供し、マルチスレッドをよりクリーンでスケーラブルにします。

---

### 3. `ExecutorService`の使用
`ExecutorService`インターフェース（`Executor`のサブインターフェース）は主要なツールです。使用方法は以下の通りです：

#### ステップ 1: ExecutorServiceの作成
`Executors`ユーティリティクラスを使用してスレッドプールを作成します：
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 4つのスレッドを持つ固定サイズのスレッドプール
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // タスクを投入
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // 作業をシミュレート
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // Executorをシャットダウン
        executor.shutdown(); // 新しいタスクを防止し、既存のタスクの終了を待機
    }
}
```
- `newFixedThreadPool(4)`は4つのスレッドを持つプールを作成します。超過したタスクはキューで待機します。
- `submit()`は`Runnable`または`Callable`タスクを受け入れます（`Callable`は結果を返します）。

#### 一般的なExecutorのタイプ
- `Executors.newSingleThreadExecutor()`: 1つのスレッドで、タスクを順次処理します。
- `Executors.newCachedThreadPool()`: 必要に応じてスレッドを作成し、アイドル状態のスレッドを再利用します（短命なタスクに適しています）。
- `Executors.newScheduledThreadPool(n)`: 遅延や定期実行でタスクをスケジュールするために使用します。

---

### 4. `Callable`と`Future`を使用した結果の処理
タスクの結果が必要な場合は、`Runnable`の代わりに`Callable`を使用します：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Callableタスクを投入
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // タスク実行中に他の作業を実行
        System.out.println("Task submitted...");

        // 結果を取得（終了するまでブロック）
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()`は結果を取得します。タスクが完了していない場合はブロックします。
- ブロックせずに完了を確認するには`future.isDone()`を使用します。

---

### 5. 上級: スレッドプールのチューニング
実世界のアプリケーションでは、カスタムの`ThreadPoolExecutor`が必要な場合があります：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // カスタムスレッドプール: 2-4スレッド、キュー容量10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // コアプールサイズ
            4, // 最大プールサイズ
            60L, // アイドルスレッドのタイムアウト
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // タスクキュー
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
- コアサイズ (2): 維持される最小スレッド数。
- 最大サイズ (4): キューが満杯の場合の最大スレッド数。
- キュー: すべてのスレッドがビジーの場合にタスクを保持します。

---

### 6. ベストプラクティス
- **適切にシャットダウンする**: リソースリークを避けるために、常に`shutdown()`または`shutdownNow()`を呼び出します。
- **割り込みの処理**: ループ内で`Thread.currentThread().isInterrupted()`を確認します。
- **過負荷を避ける**: スレッドが多すぎるとパフォーマンスが低下する可能性があります。CPUコア数に基づいてプールサイズを調整します（例：`Runtime.getRuntime().availableProcessors()`）。
- **`ExecutorService`で`try-finally`を使用する**:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // タスクを投入
} finally {
    executor.shutdown();
}
```

---

### Log4jを使用した例（まとめ）
マルチスレッドと以前のLog4jの質問を組み合わせます：
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
以前の`log4j2.xml`を使用すると、タスクの進捗がコンソールとファイルにログ出力されます。