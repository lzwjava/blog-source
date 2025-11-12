---
audio: false
generated: true
lang: ja
layout: post
title: マルチスレッドの事例
translated: true
type: note
---

Java Spring Bootプロジェクトで10個のルールをマルチスレッド検証する場合、一部のルールがデータベースにアクセスする可能性があり、時間の無駄を避けるために1つでも失敗したら他の検証をキャンセルしたいときは、Javaの並行処理ユーティリティとSpringの機能を組み合わせて使用できます。以下に完全かつ効率的なソリューションを示します：

### アプローチ概要
- **検証の並行実行**: 複数のスレッドを使用して10個の検証ルールを並列実行し、すべてのルールが通過する場合の処理速度を向上させます
- **失敗時のキャンセル**: いずれかのルールが失敗した時点で残りの検証を停止し、不要な作業を最小限に抑えます
- **Springの活用**: データベースアクセスを行うルールに対して、Springの依存性注入とトランザクション管理を活用します

これを実現する最良の方法は、`ExecutorService`と`CompletionService`を組み合わせて使用することです。`CompletionService`を使用すると、タスクの結果が完了次第処理できるため、失敗を即座に検出し、保留中のタスクをキャンセルできます。

---

### ステップバイステップのソリューション

#### 1. 検証ルールの定義
10個の各ルールは独立した検証タスクであるべきです。一部のルールはデータベースアクセスを含む可能性があるため、トランザクションメソッドを持つサービスにカプセル化します。

```java
@Service
public class RuleValidator {
    // 例：データベースにアクセスするルール
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // ルール検証をシミュレート（例：データベースクエリ）
        // ルールが通過する場合はtrue、失敗する場合はfalseを返す
        return performValidation(ruleId); // 実装はロジックに依存
    }

    private boolean performValidation(int ruleId) {
        // 実際の検証ロジックに置き換え
        return ruleId % 2 == 0; // 例：偶数のルールIDが通過
    }
}
```

- データベースから読み取りのみ行うルールには`@Transactional(readOnly = true)`を使用し、各ルールがスレッドセーフな方法で独自のトランザクションコンテキストで実行されるようにします

#### 2. ExecutorServiceの設定
検証タスクの並行実行を管理するスレッドプールを定義します。SpringではBeanとして作成できます：

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10個のルール用に10スレッド
    }
}
```

- システムの能力（CPUコア数、データベース接続制限など）に基づいてスレッドプールサイズを調整します

#### 3. マルチスレッド検証の実装
`CompletionService`を使用して検証プロセスを調整するサービスを作成します：

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

    public boolean validateAllRules() {
        // ステップ1：検証タスクの作成
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // 例外（データベースエラーなど）を失敗として処理
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // ステップ2：CompletionServiceの設定とタスクの投入
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // ステップ3：完了次第結果を処理
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // 次のタスクが完了するまでブロック
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // 失敗が見つかった時点でチェックを停止
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // ステップ4：失敗が発生した場合、残りのタスクをキャンセル
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // 実行中のタスクを中断
                }
            }
            return false; // 検証失敗
        }

        return true; // すべてのルールが通過
    }
}
```

#### 動作の仕組み
- **タスク作成**: 各検証ルールは`Callable<Boolean>`にラップされ、ルールが通過すると`true`、失敗すると`false`を返します。例外はキャッチされ失敗として扱われます
- **並行実行**: タスクは`CompletionService`に投入され、スレッドプールを使用して並列実行されます。Futureはタスクステータスを追跡するために収集されます
- **結果処理**: `completionService.take()`は次に完了したタスクの結果を取得します。いずれかの結果が`false`の場合、ループが中断され`hasFailed`が設定されます
- **キャンセル**: 失敗時には、`future.cancel(true)`を使用して未完了のすべてのタスクがキャンセルされ、実行中のスレッドの中断が試みられます
- **結果**: いずれかのルールが失敗すると`false`を、すべてが通過すると`true`を返します

---

### 主な考慮事項
- **データベースアクセス**: ルールがデータベースにアクセスする可能性があるため、`@Transactional`はスレッドセーフな操作を保証します。各タスクは独自のトランザクションで実行され、独立した検証に適しています
- **タスクキャンセル**: `Future`をキャンセルするとスレッドは中断されますが、進行中のデータベースクエリは即座に停止しない可能性があります。ただし、これによりさらなる処理が防止され、メインスレッドの進行が可能になります
- **例外処理**: 例外（データベースエラーなど）はタスク内でキャッチされ失敗として扱われるため、堅牢な動作が保証されます
- **スレッドプールサイズ**: シンプルにするために10に設定されています（ルールごとに1スレッド）が、アプリケーションのニーズとリソースに基づいて最適化してください

---

### このアプローチが最良である理由
- **効率性**: 検証が並行して実行され、すべてが通過する場合の総時間が短縮されます
- **早期終了**: `CompletionService`により即時の失敗検出が可能になり、キャンセルによって不要な作業が停止されます
- **シンプルさ**: 標準的なJava並行処理ユーティリティを活用し、Spring Bootとシームレスに統合します
- **拡張性**: スレッドプールとタスクリストを調整するだけで、より多くのルールに簡単に拡張できます

`CompletableFuture`やタイムアウト付きの`Future`結果のポーリングなどの代替アプローチも検討されましたが、`CompletionService`はこのユースケースに対してより直接的であり、完了順に効率的に結果を処理し、キャンセルをサポートします

---

### 使用例
コントローラーやビジネスロジックでサービスを注入して呼び出します：

```java
@RestController
public class ValidationController {
    private final ValidationService validationService;

    @Autowired
    public ValidationController(ValidationService validationService) {
        this.validationService = validationService;
    }

    @GetMapping("/validate")
    public ResponseEntity<String> validate() {
        boolean result = validationService.validateAllRules();
        return ResponseEntity.ok(result ? "All rules passed" : "Validation failed");
    }
}
```

このソリューションはあなたの要件を満たしています：10個の検証ルールを並列実行し、1つが失敗した時点で残りのタスクをキャンセルし、時間の無駄を避けつつ、Spring Bootときれいに統合します。