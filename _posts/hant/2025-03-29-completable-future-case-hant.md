---
audio: false
generated: true
lang: hant
layout: post
title: 使用 CompletableFuture 實現多線程驗證
translated: true
type: note
---

若我們在 Spring Boot 應用程式中使用 `CompletableFuture` 進行多線程驗證，它提供了一種現代且靈活的方式來處理非同步任務。以下我將說明實作方法，強調其優勢與挑戰，並提供專為並行驗證多項規則設計的完整解決方案。

### 使用 CompletableFuture 實作多線程驗證

`CompletableFuture` 是 Java 並行 API 的一部分，允許您非同步執行任務、鏈接操作，並優雅地處理結果或異常。以下是我們如何使用它來並行驗證多個規則，並在任一規則失敗時立即停止。

#### 步驟 1：定義驗證邏輯

首先，假設我們有一個定義個別驗證規則的服務。每個規則可能涉及資料庫存取或複雜邏輯，因此我們將使用 Spring 的 `@Transactional` 註解來確保正確的事務管理。

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // 模擬驗證邏輯（例如：資料庫查詢）
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // 範例：偶數規則 ID 通過，奇數失敗
        return ruleId % 2 == 0;
    }
}
```

#### 步驟 2：使用 CompletableFuture 實作驗證服務

現在，我們建立一個服務，使用 `CompletableFuture` 並行執行多個驗證規則。我們將使用 `ExecutorService` 來管理線程，並確保當任何規則失敗時，能夠停止處理其他規則。

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
        // 建立列表來保存所有 future
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // 提交 10 個驗證規則（範例）
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // 將異常視為失敗
                }
            }, executorService);
            futures.add(future);
        }

        // 建立一個 future 來追蹤整體結果
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // 監控每個 future 是否失敗
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // 偵測到首次失敗
                    resultFuture.complete(false);
                    // 取消剩餘任務
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // 若所有 future 都成功完成，標記為 true
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // 阻塞直到結果可用
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### 運作原理

1. **任務提交**：
   - 我們使用 `supplyAsync()` 為每個規則建立 `CompletableFuture`，以非同步方式執行驗證邏輯。
   - `executorService`（透過 Spring 注入）負責管理線程池。

2. **失敗偵測**：
   - 使用 `thenAccept()` 監控每個 future。若任何規則返回 `false`，我們將以 `false` 完成 `resultFuture` 並取消剩餘的 futures。

3. **成功情況**：
   - `CompletableFuture.allOf()` 等待所有 futures 完成。若未發生失敗，則以 `true` 完成 `resultFuture`。

4. **結果獲取**：
   - 我們在 `resultFuture.get()` 上阻塞以取得最終結果，並處理可能發生的異常。

### 使用 CompletableFuture 的優勢

- **靈活性**：您可以鏈接操作（例如 `thenApply`、`thenCompose`）以進一步處理結果。
- **異常處理**：內建方法如 `exceptionally()` 或 `handle()` 讓錯誤管理更輕鬆。
- **非阻塞設計**：支援響應式程式設計風格，可擴展至更複雜的工作流程。

### 挑戰

- **取消機制**：與使用 `CompletionService` 的 `ExecutorService`（可輕鬆輪詢首個結果並取消其他任務）不同，`CompletableFuture` 需要在失敗時手動取消其他 futures，增加了複雜度。
- **複雜性**：相較於使用 `ExecutorService` 的簡單循環方法，程式碼可能更難閱讀與維護。

### 使用範例

在 Spring Boot 應用程式中使用時，您需要配置 `ExecutorService` bean：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 根據需要調整大小
    }
}
```

然後在控制器或其他組件中呼叫服務：

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

在 Spring Boot 中使用 `CompletableFuture` 進行多線程驗證是可行的方案，特別適合重視非同步與鏈接操作特性的場景。它能讓您並行執行驗證規則，並靈活處理結果。然而，若您的主要目標是簡潔性（特別是偵測首次失敗並取消剩餘任務），傳統的 `ExecutorService` 搭配 `CompletionService` 可能更易實作與維護。使用 `CompletableFuture` 時，您能以稍複雜的取消邏輯為代價，換取更強大的功能與靈活性。