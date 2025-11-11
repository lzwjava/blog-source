---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるCompletableFuture
translated: true
type: note
---

Java Spring Bootプロジェクトには、JavaScriptの`Promise.all`（複数のPromiseが完了するのを待ち、その結果を提供する）に直接相当するものはありません。しかし、`java.util.concurrent`パッケージの`CompletableFuture`、特に`CompletableFuture.allOf`メソッドを使用することで、同様の機能（forループ内で複数のタスクを並行実行し、すべてのスレッドが完了した後にその結果を使用する）を実現できます。このアプローチは、Springの非同期プログラミング機能と組み合わせることで、Spring Bootプロジェクトに非常によく適合します。以下では、完全な例を含めて、この方法をステップバイステップで説明します。

### `CompletableFuture`を選ぶ理由
`CompletableFuture`（Java 8で導入）を使用すると、非同期操作を実行し、その完了を管理できます。`allOf`メソッドは複数の`CompletableFuture`インスタンスを受け取り、指定されたすべてのFutureが完了した時に完了する新しい`CompletableFuture`を返します。これは、以下のようなシナリオに理想的です：
- forループ内でタスクを並列実行する。
- すべてのタスクの終了を待つ。
- その後で結果を使用する。

### 実装の手順
Spring Bootプロジェクトでソリューションを構築する方法は以下の通りです：

1. **非同期タスクを定義する**  
   forループの各反復は、独立して実行できるタスクを表します。これらのタスクは、最終的な結果を表す`CompletableFuture`インスタンスを返します。

2. **Futureを収集する**  
   ループ内で作成したすべての`CompletableFuture`オブジェクトをリストに保存します。

3. **すべてのタスクの完了を待つ**  
   `CompletableFuture.allOf`を使用して、Futureを単一のFutureに結合し、すべてのタスクが終了した時点で完了するようにします。

4. **結果を取得して使用する**  
   すべてのタスクが完了した後、各`CompletableFuture`から結果を抽出し、必要に応じて処理します。

5. **例外を処理する**  
   タスク実行中の潜在的なエラーに対処します。

### 実装例
並行処理するアイテムのリスト（例：サービスを呼び出す、何らかの計算を実行する）があると仮定します。以下に、Springの`@Async`アノテーションを使用する方法と、`CompletableFuture.supplyAsync`を使用する方法の2つのアプローチを示します。

#### アプローチ1: Springの`@Async`を使用する
Spring Bootは、メソッドを非同期で実行するための`@Async`アノテーションを提供します。アプリケーションで非同期サポートを有効にする必要があります。

**ステップ1: 非同期サポートを有効にする**
設定クラスまたはメインアプリケーションクラスに`@EnableAsync`アノテーションを追加します：

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**ステップ2: 非同期メソッドを持つサービスを定義する**
各アイテムを非同期に処理するメソッドを持つサービスを作成します：

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // 何らかの作業（例：I/Oや計算）をシミュレート
        try {
            Thread.sleep(1000); // 1秒の遅延
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**ステップ3: コントローラーまたはサービスでアイテムを処理する**
コントローラーまたは別のサービスで、forループを使用してタスクを送信し、すべての結果を待ちます：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // すべてのFutureを保持するリスト
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // forループで各タスクを送信
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // すべてのタスクの完了を待つ
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // すべてのタスクが終了するまでブロック
        allFutures.join();

        // 結果を収集
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // 各結果を取得
            .collect(Collectors.toList());

        return results;
    }
}
```

**使用例:**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // 出力: [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### アプローチ2: `CompletableFuture.supplyAsync`を使用する
`@Async`を使用したくない場合は、`Executor`と`CompletableFuture.supplyAsync`を使用してスレッドを手動で管理できます。

**ステップ1: スレッドプールを設定する**
スレッドプールを制御するための`TaskExecutor` Beanを定義します：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // プールに保持するスレッド数
        executor.setMaxPoolSize(10);    // 最大スレッド数
        executor.setQueueCapacity(25);  // 保留中のタスクのキュー容量
        executor.initialize();
        return executor;
    }
}
```

**ステップ2: `supplyAsync`でアイテムを処理する**
Executorを使用してタスクを非同期に実行します：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // supplyAsyncを使用してFutureを作成
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // すべてのタスクの完了を待つ
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // 結果を収集
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // 何らかの作業をシミュレート
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### 重要なポイント
- **完了待機**: `CompletableFuture.allOf(...).join()`または`.get()`を使用すると、メインスレッドはすべてのタスクが終了するまで待機します。チェック例外の処理を避けるには`join()`を使用します。タスクが失敗した場合、`CompletionException`をスローします。
- **例外処理**: 例外を処理する必要がある場合は、`.join()`または`.get()`呼び出しをtry-catchブロックで囲みます：

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // 割り込みを処理
} catch (ExecutionException e) {
    // タスクの失敗を処理
    e.printStackTrace();
}
```

- **スレッドプールの設定**: ワークロードに基づいてスレッドプールのサイズを調整します。I/Oバウンドのタスク（例：データベース呼び出し、APIリクエスト）の場合、より大きなプール（例：5〜10スレッド）が適しています。CPUバウンドのタスクの場合、CPUコア数に合わせます（例：`Runtime.getRuntime().availableProcessors()`）。
- **結果の順序**: Futureは入力リストと同じ順序で収集されるため、結果は順序を保持します。

### どちらのアプローチを選ぶべきか？
- **`@Async`を使用する**: タスクが自然にSpringサービスの一部であり、Springにスレッド管理を任せたい場合。よりクリーンで、Spring Bootとの統合も良好です。
- **`supplyAsync`を使用する**: タスク実行をより細かく制御する必要がある場合、またはSpringの非同期フレームワークに依存したくない場合。

### 最終的な答え
Java Spring Bootプロジェクトで、マルチスレッド実行後にスレッドの結果を使用したいforループジョブに対して`Promise.all`を再現するには、`CompletableFuture`インスタンスのリストと`CompletableFuture.allOf`を使用します。シンプルさではSpringの`@Async`アプローチが推奨されますが、カスタムExecutorを使用した`supplyAsync`も機能します。上記の`@Async`の例はこれを示しています：

- `@Async`メソッドを使用してforループ内で`CompletableFuture`インスタンスを作成する。
- `CompletableFuture.allOf`を使用してすべてのタスクを待つ。
- 完了後に結果を収集して使用する。

これにより、すべてのタスクが並行して実行され、すべてが完了した時点でその結果を処理できるようになり、要件を効果的に満たします。