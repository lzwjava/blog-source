---
audio: false
generated: true
lang: ja
layout: post
title: マルチスレッド検証のCompletableFutureによる実装
translated: true
type: note
---

Spring Bootアプリケーションで`CompletableFuture`を使用してマルチスレッド検証を行う場合、非同期タスクを処理する現代的で柔軟な方法を提供します。以下では、その実装方法を説明し、利点と課題を強調し、複数のルールを同時に検証するための完全なソリューションを提供します。

### CompletableFutureを使用したマルチスレッド検証の実装

`CompletableFuture`はJavaの並行処理APIの一部であり、タスクを非同期で実行し、操作をチェーンし、結果や例外をエレガントに処理することができます。以下に、複数のルールを並列で検証し、1つでも失敗した時点で停止する方法を示します。

#### ステップ1: 検証ロジックの定義

まず、個々の検証ルールを定義するサービスがあると仮定します。各ルールはデータベースアクセスや複雑なロジックを含む可能性があるため、適切なトランザクション管理のためにSpringの`@Transactional`アノテーションを使用します。

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // 検証ロジックのシミュレーション（例：データベースクエリ）
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // 例：偶数のルールIDは合格、奇数のルールIDは不合格
        return ruleId % 2 == 0;
    }
}
```

#### ステップ2: CompletableFutureを使用した検証サービスの実装

次に、`CompletableFuture`を使用して複数の検証ルールを同時に実行するサービスを作成します。スレッドを管理し、いずれかのルールが失敗した場合に他の処理を停止できるように、`ExecutorService`を使用します。

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;

@Service
public class ValidationService {
    private static final Logger log = LoggerFactory.getLogger(ValidationService.class);
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // すべてのfutureを保持するリストを作成
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // 10個の検証ルールをサブミット（例）
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // 例外は失敗として扱う
                }
            }, executorService);
            futures.add(future);
        }

        // 全体の結果を追跡するfutureを作成
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // 各futureの失敗を監視
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // 最初の失敗を検出
                    resultFuture.complete(false);
                    // 残りのタスクをキャンセル
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // すべてのfutureが正常に完了した場合、trueでマーク
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // 結果が利用可能になるまでブロック
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### 動作の仕組み

1. **タスクのサブミット**:
   - `supplyAsync()`を使用して各ルールの`CompletableFuture`を作成し、検証ロジックを非同期で実行します。
   - `executorService`（Spring経由で注入）がスレッドプールを管理します。

2. **失敗の検出**:
   - 各futureは`thenAccept()`を使用して監視されます。いずれかのルールが`false`を返した場合、`resultFuture`を`false`で完了させ、残りのfutureをキャンセルします。

3. **成功の場合**:
   - `CompletableFuture.allOf()`はすべてのfutureが完了するのを待機します。失敗が発生しなかった場合、`resultFuture`を`true`で完了させます。

4. **結果の取得**:
   - 最終結果を取得するために`resultFuture.get()`でブロックし、発生する可能性のある例外を処理します。

### CompletableFutureを使用する利点

- **柔軟性**: 結果をさらに処理するために操作をチェーン（例: `thenApply`, `thenCompose`）できます。
- **例外処理**: `exceptionally()`や`handle()`などの組み込みメソッドにより、エラーを簡単に管理できます。
- **非ブロッキング設計**: 反応型プログラミングスタイルをサポートし、より複雑なワークフローに拡張できます。

### 課題

- **キャンセル**: `CompletionService`を使用した`ExecutorService`（最初の結果を簡単にポーリングして他をキャンセルできる）とは異なり、`CompletableFuture`では1つが失敗した場合に他のfutureを手動でキャンセルする必要があります。これにより複雑さが増します。
- **複雑さ**: `ExecutorService`を使用した単純なループベースのアプローチと比較して、コードの可読性と保守性が低下する可能性があります。

### 使用例

Spring Bootアプリケーションでこれを使用するには、`ExecutorService` Beanを設定します:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 必要に応じてサイズを調整
    }
}
```

その後、コントローラーや別のコンポーネントからサービスを呼び出します:

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

### 結論

Spring Bootでのマルチスレッド検証に`CompletableFuture`を使用することは、特にその非同期でチェーン可能な性質を重視する場合に有効なアプローチです。これにより、検証ルールを同時に実行し、結果を柔軟に処理することができます。ただし、最初の失敗を検出して残りのタスクをキャンセルするという主目的が単純さである場合、従来の`ExecutorService`と`CompletionService`の方が実装と保守が容易かもしれません。`CompletableFuture`を使用すると、わずかに複雑なキャンセルロジックの代償として、力と柔軟性を得ることができます。