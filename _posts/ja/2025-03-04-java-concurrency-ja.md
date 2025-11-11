---
audio: false
generated: true
lang: ja
layout: post
title: Java並行処理
translated: true
type: note
---

### 主なポイント
- `java.util.concurrent`パッケージは、Javaで複数のタスクを同時に管理し、プログラムを高速化して応答性を向上させる
- `ExecutorService`を使用したスレッド管理は一般的な手法であり、バックグラウンドでのタスク実行を可能にする
- `ConcurrentHashMap`などの並行コレクションはスレッドセーフであり、複数のスレッドが安全にデータにアクセスできる
- 従来の方法と比較して、`Lock`などの同期ツールを使用すると共有リソースに対する制御を強化できる

### Java Utility Concurrentの紹介
`java.util.concurrent`パッケージはJava標準ライブラリの一部であり、複数のタスクを同時に実行するプログラムの記述を簡素化するために設計されています。これは、特にマルチコアを搭載した現代のコンピューターにおいて、パフォーマンスを向上させるのに有用です。

### ExecutorServiceの使用
`ExecutorService`はスレッドを管理するための主要なツールです。スレッドプールを作成し、バックグラウンドで実行するタスクを投入することができます。例えば、スレッドプールを設定して結果を返すタスクを実行し、それらが完了するのを待つことができます。

### 並行コレクション
このパッケージには`ConcurrentHashMap`などのスレッドセーフなコレクションが含まれており、複数のスレッドが競合することなく読み書きできます。これは、追加の同期化が必要な可能性がある通常のコレクションとは異なります。

### 同期ユーティリティ
`Lock`や`Condition`などのツールは、`synchronized`キーワードよりも柔軟性を提供します。これらは共有リソースへのアクセスを制御し、一度に1つのスレッドのみがデータを変更できるようにします。

---

### サーベイノート: Java Utility Concurrent使用包括的ガイド

このセクションでは、`java.util.concurrent`パッケージの詳細な探求を提供し、主要なポイントを拡張して、Javaで並行プログラミングを実装しようとするユーザー向けに徹底的なガイドを提供します。内容は専門的な記事を模倣して構成され、初期分析からの関連する詳細をすべて含み、技術的理解のために追加の深みを持たせています。

#### Java並行処理と`java.util.concurrent`パッケージの概要
Javaにおける並行処理は、複数のタスクを並列に実行することを可能にし、特にマルチコアプロセッサ上でアプリケーションのパフォーマンスと応答性を向上させます。Java 5で導入された`java.util.concurrent`パッケージは、Java標準ライブラリの重要なコンポーネントであり、並行プログラミングを促進する一連のクラスとインターフェースを提供します。このパッケージは、以前は手動で処理され、複雑でエラーが発生しやすいコードにつながっていたスレッド管理、同期、およびデータ共有の課題に対処します。

このパッケージには、スレッドプール、並行データ構造、および同期支援のためのユーティリティが含まれており、スケーラブルで効率的なアプリケーションの開発を容易にします。例えば、Webサーバーのような現代のアプリケーションは、複数のリクエストを同時に処理することで恩恵を受け、このパッケージはそれを効果的に行うためのツールを提供します。

#### 主要コンポーネントとその使用法

##### ExecutorService: 効率的なスレッド管理
`ExecutorService`は、スレッド実行を管理するための中心的なインターフェースであり、スレッドプールと非同期タスク実行を処理するための高レベルAPIを提供します。これはスレッドの作成と管理を抽象化し、開発者がスレッドのライフサイクル管理ではなくタスクロジックに集中できるようにします。

`ExecutorService`を使用するには、`Executors`クラスのファクトリメソッド（`newFixedThreadPool`、`newCachedThreadPool`、`newSingleThreadExecutor`など）を使用してスレッドプールを作成できます。以下はその使用法を示す例です：

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        // 2つのスレッドで固定サイズのスレッドプールを作成
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // エグゼキュータにタスクを投入
        Future<String> future1 = executor.submit(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Task 1 completed";
        });

        Future<String> future2 = executor.submit(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Task 2 completed";
        });

        try {
            // タスクが完了するのを待ち、結果を取得
            System.out.println(future1.get());
            System.out.println(future2.get());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // エグゼキュータをシャットダウン
            executor.shutdown();
        }
    }
}
```

この例は、スレッドプールの作成方法、`Future`を介して結果を返すタスクの投入方法、および適切なシャットダウンを確保する方法を示しています。`Future`オブジェクトを使用すると、タスクが完了したかどうかを確認し、その結果を取得でき、例外を適切に処理できます。これは、トランザクションの処理やリクエストの処理などのタスクが独立して実行できる非同期プログラミングに特に有用です。

##### 並行コレクション: スレッドセーフなデータ構造
並行コレクションは、マルチスレッドコンテキストで使用するために設計された、標準Javaコレクションのスレッドセーフな実装です。例としては、`ConcurrentHashMap`、`ConcurrentSkipListMap`、`ConcurrentSkipListSet`、`CopyOnWriteArrayList`、`CopyOnWriteArraySet`などがあります。これらのコレクションは外部同期の必要性を排除し、デッドロックのリスクを減らし、パフォーマンスを向上させます。

例えば、`ConcurrentHashMap`は`HashMap`のスレッドセーフな代替品であり、複数のスレッドがブロックすることなく同時に読み書きできます。以下はその例です：

```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

        map.put("apple", 1);
        map.put("banana", 2);

        // 複数のスレッドがこのマップに安全に読み書きできる
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

この例は、`ConcurrentHashMap`が追加の同期なしで複数のスレッドからアクセスできる方法を示しており、キャッシングシステムなどのように同時読み書き操作が頻繁に行われるシナリオに理想的です。

##### 同期ユーティリティ: `synchronized`を超えて
このパッケージには、`Lock`、`ReentrantLock`、`Condition`、`CountDownLatch`、`Semaphore`、`Phaser`などの同期ユーティリティが含まれており、`synchronized`キーワードよりも柔軟性を提供します。これらのツールは、共有リソースへのスレッドアクセスを調整し、複雑な同期シナリオを管理するために不可欠です。

例えば、`ReentrantLock`は、ロックとアンロック操作に対するより細かい制御を可能にする、より柔軟なロックメカニズムを提供します。以下はその例です：

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // クリティカルセクション
            System.out.println("Doing something");
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

この例は、`Lock`を使用してクリティカルセクションへのアクセスを同期化し、一度に1つのスレッドのみがそれを実行することを確保する方法を示しています。`synchronized`とは異なり、`Lock`はタイムドロックや割り込み可能なロックなどのより高度な機能を可能にし、タイムアウト処理や割り込みを必要とするシナリオで有用です。

その他のユーティリティには以下が含まれます：
- **CountDownLatch**: 1つ以上のスレッドが他のスレッドでの一連の操作が完了するまで待機できるようにする同期支援。例えば、すべてのワーカースレッドが終了したことを確保してから進むために使用できます。
- **Semaphore**: 利用可能な許可の数を維持することにより、共有リソースへのアクセスを制御し、データベース接続などのリソースにアクセスするスレッドの数を制限するのに有用です。
- **Phaser**: フェーズでスレッドを調整するための再利用可能なバリアであり、反復アルゴリズムなどのような複数の実行段階を持つアプリケーションに適しています。

#### 追加ユーティリティとベストプラクティス
このパッケージには、`AtomicInteger`、`AtomicLong`、`AtomicReference`などのアトミッククラスも含まれており、変数に対するアトミック操作を提供し、ロックなしでスレッドセーフを確保します。例えば：

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

        System.out.println("Final count: " + example.getCount());
    }
}
```

この例は、`AtomicInteger`が明示的な同期なしで、競合状態を回避しながら、複数のスレッドから安全にカウンターをインクリメントする方法を示しています。

ベストプラクティスには以下が含まれます：
- リソースリークを防ぐために、`shutdown()`または`shutdownNow()`を使用して常に`ExecutorService`をシャットダウンする
- 読み取りが多いシナリオでは、同期化コレクションの代わりに並行コレクションを使用する
- `ExecutorService`に投入されたタスクの例外を、`ExecutionException`をスローできる`Future.get()`を使用して処理する

#### 比較分析: 従来のアプローチと並行アプローチ
利点を強調するために、従来のスレッド処理と`java.util.concurrent`パッケージの使用の違いを考慮してください。従来のアプローチでは、`Thread`インスタンスを手動で作成し、同期を管理することが多く、ボイラープレートコードやデッドロックなどのエラーにつながる可能性があります。対照的に、このパッケージは高レベルの抽象化を提供し、複雑さを減らし、保守性を向上させます。

例えば、`HashMap`を手動で同期化するには、`Collections.synchronizedMap`でラップする必要がありますが、それでも競合の問題につながる可能性があります。しかし、`ConcurrentHashMap`は細粒度ロックを使用し、同時読み書きを可能にします。これは、従来の同期方法に慣れている人にとっては予想外の詳細です。

#### さらなる学習のためのリソース
理解を深めたい人向けに、いくつかのリソースが利用可能です：
- 公式の[Oracle Javaチュートリアル並行処理](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)は、詳細なドキュメントと例を提供します。
- [Baeldungのjava.util.concurrent概要](https://www.baeldung.com/java-util-concurrent)は、実用的なガイドとコードスニペットを提供します。
- [JenkovのJava並行処理ユーティリティ](https://jenkov.com/tutorials/java-util-concurrent/index.html)は、各コンポーネントを深くカバーする一連のチュートリアルを含みます。

これらのリソースは、2025年3月現在のものであり、ユーザーがJavaで並行プログラミングを実装するための最新の情報にアクセスできることを確保します。

#### 表: `java.util.concurrent`の主要クラスの比較

| クラス/インターフェース     | 目的                                          | 使用例                              |
|---------------------------|-----------------------------------------------|-------------------------------------|
| `ExecutorService`         | スレッドプールとタスク実行の管理               | 複数のHTTPリクエストの実行          |
| `ConcurrentHashMap`       | スレッドセーフなハッシュマップ                 | Webアプリケーションでのデータキャッシング |
| `ReentrantLock`           | 柔軟なロックメカニズム                         | クリティカルセクションの保護        |
| `CountDownLatch`          | 複数の操作が完了するのを待機                   | すべてのスレッドのセットアップ完了を確保 |
| `Semaphore`               | 共有リソースへのアクセス制御                   | データベース接続プールの制限        |

この表は主要な用途を要約し、特定の並行処理ニーズに適したツールの選択を支援します。

結論として、`java.util.concurrent`パッケージは現代のJava開発に不可欠であり、並行プログラミングのための堅牢なツールを提供します。これらのユーティリティを活用することにより、開発者は効率的でスケーラブルなアプリケーションを構築し、現代のコンピューティング環境の要求に対処できます。

#### 主要な引用文献
- [Oracle Javaチュートリアル並行処理サマリー](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)
- [Baeldung java.util.concurrent概要](https://www.baeldung.com/java-util-concurrent)
- [Jenkov Java並行処理ユーティリティ索引](https://jenkov.com/tutorials/java-util-concurrent/index.html)