---
audio: false
generated: true
lang: hant
layout: post
title: 多線程案例
translated: true
type: note
---

要在 Java Spring Boot 專案中處理包含 10 條規則的多執行緒驗證，其中某些規則可能需要存取資料庫，且希望在任一規則失敗時立即取消其他規則以避免浪費時間，您可以結合使用 Java 的並行工具與 Spring 的功能。以下提供完整且高效的解決方案：

### 方法概述
- **並行執行驗證**：使用多執行緒並行執行 10 條驗證規則，在所有規則都通過時加快處理速度
- **失敗時取消**：當任一規則失敗時立即停止剩餘驗證，盡量減少不必要的工作
- **利用 Spring 功能**：運用 Spring 的依賴注入和交易管理來處理需要存取資料庫的規則

最佳實現方式是使用 `ExecutorService` 搭配 `CompletionService`。`CompletionService` 允許您在任務完成時立即處理結果，從而能夠即時檢測失敗並取消待處理任務。

---

### 逐步解決方案

#### 1. 定義驗證規則
每條規則都應是獨立的驗證任務。某些規則可能涉及資料庫存取，因此將它們封裝在具有交易方法的服务中。

```java
@Service
public class RuleValidator {
    // 範例：存取資料庫的規則
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // 模擬規則驗證，例如資料庫查詢
        // 如果規則通過則返回 true，失敗則返回 false
        return performValidation(ruleId); // 具體實現取決於您的邏輯
    }

    private boolean performValidation(int ruleId) {
        // 替換為實際的驗證邏輯
        return ruleId % 2 == 0; // 範例：偶數規則 ID 通過
    }
}
```

- 對於僅從資料庫讀取的規則，使用 `@Transactional(readOnly = true)` 確保每個規則在各自的交易上下文中以執行緒安全的方式運行。

#### 2. 配置 ExecutorService
定義一個執行緒池來管理驗證任務的並行執行。在 Spring 中，您可以將其創建為一個 bean：

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10 個執行緒對應 10 條規則
    }
}
```

- 根據系統能力（例如 CPU 核心數、資料庫連接限制）調整執行緒池大小。

#### 3. 實現多執行緒驗證
創建一個使用 `CompletionService` 來協調驗證過程的服務：

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
        // 步驟 1：創建驗證任務
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // 將異常（例如資料庫錯誤）視為失敗處理
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // 步驟 2：設置 CompletionService 並提交任務
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // 步驟 3：在任務完成時處理結果
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // 阻塞直到下個任務完成
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // 發現失敗後停止檢查
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // 步驟 4：如果發生失敗，取消剩餘任務
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // 中斷正在運行的任務
                }
            }
            return false; // 驗證失敗
        }

        return true; // 所有規則通過
    }
}
```

#### 運作原理
- **任務創建**：每條驗證規則被封裝在 `Callable<Boolean>` 中，規則通過時返回 `true`，失敗時返回 `false`。捕獲的異常會被視為失敗處理。
- **並行執行**：任務被提交到 `CompletionService`，該服務使用執行緒池並行運行它們。收集 Future 對象以追蹤任務狀態。
- **結果處理**：`completionService.take()` 獲取下個已完成任務的結果。如果任何結果為 `false`，循環中斷，並設置 `hasFailed`。
- **取消機制**：失敗時，使用 `future.cancel(true)` 取消所有未完成任務，這會嘗試中斷正在運行的執行緒。
- **結果輸出**：如果有任何規則失敗則返回 `false`，全部通過則返回 `true`。

---

### 關鍵注意事項
- **資料庫存取**：由於規則可能需要存取資料庫，`@Transactional` 確保了執行緒安全操作。每個任務在各自的交易中運行，這對於獨立驗證是合適的。
- **任務取消**：取消 `Future` 會中斷執行緒，但正在進行的資料庫查詢可能不會立即停止。不過這仍然能阻止進一步處理並讓主執行緒繼續執行。
- **異常處理**：任務內捕獲的異常（例如資料庫錯誤）會被視為失敗處理，確保了穩健的行為。
- **執行緒池大小**：為簡單起見設置為 10（每條規則一個執行緒），但請根據應用程式需求和資源進行優化。

---

### 為何這是最佳方法
- **高效性**：驗證並行運行，在所有規則通過時減少總耗時
- **早期終止**：`CompletionService` 允許即時失敗檢測，取消機制可停止不必要的工作
- **簡潔性**：利用標準 Java 並行工具並與 Spring Boot 無縫整合
- **可擴展性**：通過調整執行緒池和任務列表，可輕鬆擴展到更多規則

我們考慮過使用 `CompletableFuture` 或透過超時輪詢 `Future` 結果等替代方法，但對於此使用情境，`CompletionService` 更為直接，它能有效按完成順序處理結果並支援取消。

---

### 使用範例
在控制器或業務邏輯中注入並調用服務：

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

此解決方案符合您的需求：並行運行 10 條驗證規則，在任一規則失敗時取消剩餘任務，避免浪費時間，同時與 Spring Boot 整潔整合。