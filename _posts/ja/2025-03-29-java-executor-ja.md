---
audio: false
generated: true
lang: ja
layout: post
title: エグゼキューターサービスとスレッドプールエグゼキューターの理解
translated: true
type: note
---

Javaで`ExecutorService`のパラメータを設定するには、システムのリソース（8コアCPUなど）とタスクの性質（CPUバウンドまたはI/Oバウンドなど）に基づいてスレッドプールを構成し、パフォーマンスを最適化する必要があります。以下では、8コアCPU向けに`ExecutorService`を構成する方法を、`ThreadPoolExecutor`のような一般的な実装に焦点を当てて説明し、ユースケースに合わせた実用的な例を提供します。

---

### ExecutorServiceとThreadPoolExecutorの理解

`ExecutorService`インターフェースは通常、`ThreadPoolExecutor`のようなクラスによって実装され、スレッドプールのパラメータをきめ細かく制御できます。8コアCPU向けに構成する際には、以下を考慮する必要があります：
- **コアプールサイズ**: アイドル状態でも維持するスレッド数。
- **最大プールサイズ**: プールで許可される最大スレッド数。
- **キュー容量**: 実行前にタスクを保持するタスクキューのサイズ。
- **スレッド作成戦略**: スレッドの作成と管理方法。
- **タスクタイプ**: タスクがCPUバウンド（計算処理など）かI/Oバウンド（データベースアクセスなど）か。

8コアCPUの場合、最適な構成はタスクがCPU集中型かI/O集中型（検証シナリオでのデータベースアクセスなど）かによって異なります。

---

### ThreadPoolExecutorの主要パラメータ

`ThreadPoolExecutor`の設定方法は以下のとおりです：

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // 維持する生存スレッド数
    maximumPoolSize,   // 許可される最大スレッド数
    keepAliveTime,     // アイドルスレッドの生存時間（例：60L）
    TimeUnit.SECONDS,  // keepAliveTimeの単位
    workQueue,         // タスクを保持するキュー（例：new LinkedBlockingQueue<>()）
    threadFactory,     // オプション：カスタムスレッド名や優先度
    rejectionHandler   // キューが満杯で最大スレッド数に達したときの処理
);
```

#### パラメータの詳細
1. **`corePoolSize`**:
   - 常に生存し続ける最小スレッド数。
   - CPUバウンドタスクの場合：コア数に設定（例：8）。
   - I/Oバウンドタスクの場合：スレッドが待機時間を要するため、より高く設定可能（例：16以上）。

2. **`maximumPoolSize`**:
   - キューが満杯になった場合に許可される最大スレッド数。
   - CPUバウンドの場合：`corePoolSize`と同じ（例：8）が一般的。
   - I/Oバウンドの場合：バースト処理のために高く設定（例：20または50）。

3. **`keepAliveTime`**:
   - `corePoolSize`を超える余分なアイドルスレッドが終了されるまでの生存時間。
   - 例：`60L`秒が一般的なデフォルト。

4. **`workQueue`**:
   - 実行待機タスク用のキュー：
     - `LinkedBlockingQueue`: 無制限キュー（多くの場合デフォルト）。
     - `ArrayBlockingQueue`: 制限付きキュー（例：`new ArrayBlockingQueue<>(100)`）。
     - `SynchronousQueue`: キューなし；タスクは直接スレッドに渡される（`Executors.newCachedThreadPool()`で使用）。

5. **`threadFactory`**（オプション）:
   - スレッド作成をカスタマイズ（例：デバッグのためのスレッド名付け）。
   - デフォルト：`Executors.defaultThreadFactory()`。

6. **`rejectionHandler`**（オプション）:
   - タスクが`maximumPoolSize`とキュー容量を超えたときのポリシー：
     - `AbortPolicy`（デフォルト）：`RejectedExecutionException`をスロー。
     - `CallerRunsPolicy`：呼び出し元スレッドでタスクを実行。
     - `DiscardPolicy`：タスクを暗黙的に破棄。

---

### 8コアCPU向けの構成

#### シナリオ1: CPUバウンドタスク
タスクがCPU集中型（重い計算処理など）の場合、スレッド数をCPUコア数に合わせて、システムに過負荷をかけずにスループットを最大化します。

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // 8コアに合わせる
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60秒

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // 無制限キュー
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **理由**: 8スレッドで8コアを完全に活用します。これ以上スレッドを追加するとコンテキストスイッチのオーバーヘッドが発生し、パフォーマンスが低下します。

#### シナリオ2: I/Oバウンドタスク（例：データベース検証）
データベースアクセスを伴う検証シナリオでは、タスクはI/Oバウンドです。一部のスレッドがデータベースの応答を待機している間もCPUをビジー状態に保つため、コア数より多くのスレッドを使用できます。

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // I/Oバウンドタスク用にコア数の2倍
        int maximumPoolSize = 20; // バースト対応のための余裕
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // メモリ制限のための制限付きキュー
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // カスタム名付け
            new ThreadPoolExecutor.CallerRunsPolicy() // 過負荷時は呼び出し元で実行
        );
    }
}
```

- **理由**:
  - `corePoolSize = 16`: I/Oバウンドタスクの一般的なヒューリスティックは`N * 2`（`N`はCPUコア数）ですが、データベース接続制限やタスクの待機時間に基づいて調整可能です。
  - `maximumPoolSize = 20`: ピーク負荷に対応するための追加スレッドを許可。
  - `ArrayBlockingQueue(100)`: キューされたタスクの無制限な増加を防ぎ、メモリ問題を回避。
  - `CallerRunsPolicy`: 過負荷時に呼び出し元スレッドでタスクを実行することで、システムの優雅な劣化を確保。

#### Spring Boot統合
Spring Bootアプリケーションでは、`ExecutorService`をBeanとして定義します：

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // 検証用I/Oバウンド想定
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **注意**: カスタム名付けが必要ない場合は、`ThreadFactoryBuilder`の代わりに`Executors.defaultThreadFactory()`を使用できます。`ThreadFactoryBuilder`を使用するにはGuava（`com.google.guava:guava`）を依存関係に追加してください。

#### 検証サービスでの使用例
前述の例のように注入して使用します：

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // 前述の例のようにCompletableFutureまたはExecutorServiceロジックで使用
}
```

---

### 8コアCPU向けチューニングのヒント

1. **パフォーマンスの計測**:
   - VisualVMなどのプロファイリングツールを使用してスレッド使用率を監視し、`corePoolSize`と`maximumPoolSize`を調整します。

2. **データベース制限**:
   - ルールがデータベースにアクセスする場合、スレッドプールサイズが接続プールサイズ（HikariCPの`maximumPoolSize`など）を超えないようにします。これらの設定を調整してください。

3. **動的計算**:
   - `Runtime.getRuntime().availableProcessors()`を使用してコアプールサイズを動的に設定：
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // 8コアCPUで8を返す
     int corePoolSize = cores * 2; // I/Oバウンドタスク用
     ```

4. **スレッドの事前起動**:
   - `executor.prestartAllCoreThreads()`を呼び出してすべてのコアスレッドを事前に初期化し、遅延作成を回避します。

---

### 結論

データベースアクセスを伴う検証ルールのようなI/Oバウンドタスクを8コアCPUで実行する場合：
- `ThreadPoolExecutor`を`corePoolSize = 16`、`maximumPoolSize = 20`、制限付きキュー（例：`ArrayBlockingQueue(100)`）で使用します。
- Spring Beanとして統合し、依存性注入を可能にします。
- プロファイリングとデータベース制約に基づいて調整します。

この設定は、並列性、リソース使用量、システム安定性のバランスを取るため、ユースケースに適しています。特定のプロジェクトへの統合に助けが必要な場合はお知らせください！