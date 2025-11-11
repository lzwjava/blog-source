---
audio: false
generated: true
lang: hant
layout: post
title: Spring 中的 SQL 交易回滾異常
translated: true
type: note
---

針對您關於捕獲 `SqlTransactionRollbackException`（該異常發生於 `DataSourceUtils.java` 從 `DataSource` 獲取 JDBC 連接之後）以及對相關數據庫鎖進行詳細分析的查詢，讓我們系統性地分解這個問題。

### 捕獲 SqlTransactionRollbackException

在基於 Spring 的應用程序中，`DataSourceUtils.java` 是 Spring Framework 內的一個工具類，用於促進從 `DataSource` 獲取和管理 JDBC 連接。具體來說，`DataSourceUtils.getConnection(DataSource)` 方法獲取一個連接，該連接可以是從連接池中獲取的新連接，也可以是如果當前線程的事務上下文中已存在關聯的事務連接，則複用該連接。

您描述的情況表明，在成功獲取連接後，拋出了 `SqlTransactionRollbackException`。由於 `SqlTransactionRollbackException` 不是 Spring 異常層次結構中的標準異常（Spring 通常使用 `TransactionException`、`UnexpectedRollbackException` 或 `DeadlockLoserDataAccessException` 等異常），我將假設它是一個自定義的應用程序特定異常，在事務由於數據庫相關問題（例如鎖衝突）而回滾時拋出。

此異常很可能不是發生在連接檢索本身（如果檢索失敗，通常會拋出 `CannotGetJdbcConnectionException`），而是發生在事務內後續的數據庫操作期間——例如執行 SQL 語句時——遇到了需要回滾的問題。

要捕獲此異常，您需要將啟動事務操作的代碼包裝在 `try-catch` 塊中。以下是操作方法：

#### 使用聲明式事務管理的示例
如果您使用 Spring 的 `@Transactional` 註解來管理事務，則異常將從定義事務的方法中拋出。例如：

```java
@Service
public class MyService {
    @Autowired
    private MyDao myDao;

    @Transactional
    public void performDatabaseOperation() {
        myDao.updateData(); // 假設此操作因鎖問題導致回滾
    }
}
```

在調用此服務方法時，您可以捕獲 `SqlTransactionRollbackException`：

```java
@Autowired
private MyService myService;

public void executeOperation() {
    try {
        myService.performDatabaseOperation();
    } catch (SqlTransactionRollbackException e) {
        // 處理異常
        System.err.println("Transaction rolled back due to: " + e.getMessage());
        // 可選擇重試操作或通知用戶
    }
}
```

#### 使用編程式事務管理的示例
如果您使用 `TransactionTemplate` 或 `PlatformTransactionManager` 以編程方式管理事務，則需要在事務執行周圍捕獲異常：

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void executeOperation() {
    try {
        transactionTemplate.execute(status -> {
            // 執行數據庫操作
            myDao.updateData();
            return null;
        });
    } catch (SqlTransactionRollbackException e) {
        // 處理異常
        System.err.println("Transaction rolled back due to: " + e.getMessage());
    }
}
```

#### 注意事項
- **異常層次結構**：如果 `SqlTransactionRollbackException` 是自定義異常，請驗證其超類。如果它繼承自 Spring 的 `DataAccessException`，您可以改為捕獲 `DataAccessException` 並檢查具體類型：
  ```java
  catch (DataAccessException e) {
      if (e instanceof SqlTransactionRollbackException) {
          // 具體處理 SqlTransactionRollbackException
      }
  }
  ```
- **事務上下文**：異常很可能在連接獲取之後，當事務管理器或 JDBC 驅動程序檢測到問題（例如，僅回滾狀態或數據庫錯誤）時出現。因此，在服務層或調用者層級捕獲它是合適的。

### 數據庫鎖的詳細分析

您的查詢中提到的「這種數據庫鎖」，結合回滾異常，強烈暗示與**死鎖**有關——這是一種常見的數據庫鎖定問題，可能導致事務回滾。讓我們詳細分析這一點。

#### 什麼是死鎖？
當兩個或多個事務無法繼續進行，因為每個事務都持有另一個事務需要的鎖，從而形成循環依賴時，數據庫中就會發生死鎖。例如：

- **事務 T1**：
  1. 獲取 `TableA` 的獨佔鎖。
  2. 嘗試獲取 `TableB` 的獨佔鎖（等待，因為 T2 持有它）。
- **事務 T2**：
  1. 獲取 `TableB` 的獨佔鎖。
  2. 嘗試獲取 `TableA` 的獨佔鎖（等待，因為 T1 持有它）。

在這裡，T1 等待 T2 釋放 `TableB`，而 T2 等待 T1 釋放 `TableA`，導致死鎖。

#### 死鎖如何導致回滾
大多數關係型數據庫（例如 MySQL、PostgreSQL、Oracle）都有死鎖檢測機制。當檢測到死鎖時：
1. 數據庫選擇一個「犧牲者」事務（通常是完成工作最少的事務或基於可配置的策略）。
2. 犧牲者事務被回滾，釋放其鎖。
3. 數據庫向應用程序拋出帶有特定錯誤代碼的 `SQLException`（例如，MySQL 錯誤 1213，PostgreSQL 錯誤 40P01）。
4. 在 Spring 中，此 `SQLException` 通常被轉換為 `DeadlockLoserDataAccessException`。如果您的應用程序改為拋出 `SqlTransactionRollbackException`，它可能是圍繞此類事件的自定義包裝器。

在您的情況下，在 `DataSourceUtils` 獲取連接之後，事務內的數據庫操作遇到死鎖，導致回滾並拋出 `SqlTransactionRollbackException`。

#### 涉及的鎖類型
- **共享鎖**：用於讀操作；多個事務可以對同一資源持有共享鎖。
- **獨佔鎖**：用於寫操作；只有一個事務可以持有獨佔鎖，並且它與其他事務持有的共享鎖和獨佔鎖衝突。
死鎖通常涉及獨佔鎖，因為它們更具限制性。

#### 死鎖發生的原因
死鎖的產生原因包括：
- **不一致的鎖定順序**：事務以不同順序訪問資源（例如，表、行）。
- **長事務**：長時間持有鎖會增加衝突的機會。
- **高併發性**：多個事務同時操作相同的數據。

#### 示例場景
假設您的應用程序中有兩個方法更新兩個表：

```java
@Transactional
public void updateUserAndOrder1() {
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Alice", 1); // 鎖定 users 行
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Shipped", 1); // 鎖定 orders 行
}

@Transactional
public void updateUserAndOrder2() {
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Processed", 1); // 鎖定 orders 行
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Bob", 1); // 鎖定 users 行
}
```

如果這些方法同時運行，`updateUserAndOrder1` 可能鎖定 `users` 同時等待 `orders`，而 `updateUserAndOrder2` 可能鎖定 `orders` 同時等待 `users`，從而導致死鎖。

#### 處理和預防死鎖
1. **捕獲異常**：
   如前所述，使用 `try-catch` 塊處理 `SqlTransactionRollbackException`。您可能：
   - 記錄錯誤以進行調試。
   - 重試操作（注意避免無限循環）：
     ```java
     int retries = 3;
     for (int i = 0; i < retries; i++) {
         try {
             myService.performDatabaseOperation();
             break;
         } catch (SqlTransactionRollbackException e) {
             if (i < retries - 1) {
                 Thread.sleep(1000 * (i + 1)); // 指數退避
                 continue;
             }
             throw e; // 在最大重試次數後重新拋出
         }
     }
     ```

2. **確保一致的鎖定順序**：
   修改代碼以相同的順序訪問表（例如，總是先鎖定 `users` 再鎖定 `orders`）。

3. **最小化鎖定持續時間**：
   通過將非事務邏輯移到 `@Transactional` 邊界之外來保持事務簡短。

4. **使用適當的事務隔離級別**：
   如果應用程序要求允許，調整事務隔離級別（例如，使用 `READ_COMMITTED` 而不是 `SERIALIZABLE`），儘管這不能完全消除死鎖。

5. **數據庫特定功能**：
   - 啟用死鎖檢測日誌記錄（例如，MySQL 的 `innodb_print_all_deadlocks`）。
   - 在可能的情況下使用行級鎖定，儘管死鎖仍然可能在行級發生。

#### 分析死鎖
要診斷具體的死鎖：
- **數據庫日誌**：檢查數據庫服務器日誌以獲取死鎖詳細信息（例如，涉及的事務、鎖定的資源）。
- **Spring 調試**：啟用 Spring 事務日誌記錄（`logging.level.org.springframework.transaction=DEBUG`）以跟踪事務事件。
- **應用程序跟踪**：記錄導致異常的操作序列。

### 結論
要捕獲 `SqlTransactionRollbackException`，請在調用事務操作（例如標有 `@Transactional` 的服務方法）的代碼周圍放置 `try-catch` 塊。對於數據庫鎖——很可能是死鎖——請確保事務以一致的順序訪問資源，保持事務簡短，並考慮對瞬態故障使用重試邏輯。死鎖是由於循環鎖依賴而發生的，雖然數據庫通過回滾犧牲者事務來解決它們，但主動設計可以最大限度地減少其發生。

---

在 Spring 應用程序中處理 `SqlTransactionRollbackException` 時——特別是在另一事務持有鎖導致連接獲取失敗並且在大約 20 次失敗嘗試後拋出異常的情況下——您可以採用多種策略來處理並可能緩解此問題。此異常通常發生在事務回滾期間，當數據庫鎖或併發問題阻止操作成功完成時。下面，我概述了一個全面的方法來解決此問題，重點關注預防、處理和恢復。

---

### 理解問題
`SqlTransactionRollbackException`（或者在 Spring 中更可能是 `TransactionRollbackException`，因為前者不是標準的 Spring 異常）表明事務無法回滾，可能是因為另一事務持有所需數據庫資源的鎖。這種鎖爭用導致事務管理器無法獲取連接，重試多次（在您的情況下約為 20 次），並最終在回滾無法完成時拋出異常。這表明存在併發問題，例如鎖爭用或死鎖，並因 Spring 的事務管理在放棄之前內部重試而加劇。

---

### 處理異常的策略

#### 1. 通過短事務最小化鎖爭用
長時間運行的事務會增加鎖爭用的可能性，因為它們長時間持有數據庫鎖，從而阻塞其他事務。為降低此風險：

- **設計短生命週期的事務**：確保您的 `@Transactional` 方法快速執行其數據庫操作並及時提交或回滾。避免在事務範圍內包含耗時的業務邏輯或外部調用。
- **分解大事務**：如果單個事務涉及多個操作，請考慮在可能的情況下將其拆分為較小的獨立事務。這減少了持有鎖的持續時間。

#### 2. 優化數據庫查詢
未經優化的查詢可能因持有鎖的時間超過必要時間而加劇鎖爭用。為解決此問題：

- **分析和優化查詢**：使用數據庫分析工具識別慢查詢。添加適當的索引，避免不必要的表掃描，並最小化鎖定行的範圍（例如，使用精確的 `WHERE` 子句）。
- **避免過於寬泛的鎖定**：對像 `SELECT ... FOR UPDATE` 這樣的語句要謹慎，它們會顯式鎖定行並可能阻塞其他事務。僅在必要時使用它們，並確保它們影響的行數最少。

#### 3. 調整事務設置
Spring 的 `@Transactional` 註解提供了用於微調事務行為的屬性。雖然這些不會直接解決回滾失敗，但它們可以幫助管理併發：

- **隔離級別**：默認隔離級別（`DEFAULT`）通常映射到數據庫的默認級別（通常是 `READ_COMMITTED`）。將其增加到 `REPEATABLE_READ` 或 `SERIALIZABLE` 可能會確保數據一致性，但可能加劇鎖爭用。相反，堅持使用 `READ_COMMITTED` 或更低級別（如果支持）可能會減少鎖定問題，具體取決於您的用例。仔細測試以找到正確的平衡點。
- **傳播行為**：默認的 `REQUIRED` 會加入現有事務或啟動新事務。使用 `REQUIRES_NEW` 會暫停當前事務並啟動新事務，可能避免與被鎖定的事務發生衝突。但是，這可能無法解決特定於回滾的問題。
- **超時**：在 `@Transactional(timeout = 10)` 中設置 `timeout` 值（以秒為單位），以便在事務等待鎖時快速失敗。這可以防止長時間重試，但無法解決根本原因。

示例：
```java
@Transactional(timeout = 5, propagation = Propagation.REQUIRES_NEW)
public void performDatabaseOperation() {
    // 您的代碼在這裡
}
```

#### 4. 實施重試邏輯（需謹慎）
由於異常在多次內部重試（約 20 次）後發生，Spring 的事務管理器很可能已經在嘗試處理該問題。但是，您可以在更高層級實施自定義重試邏輯：

- **使用 Spring Retry**：
  使用 `@Retryable` 註解服務方法，以便在 `TransactionRollbackException` 上重試。指定嘗試次數和重試之間的延遲。將其與 `@Recover` 方法配對，以在重試耗盡後處理失敗。
  ```java
  import org.springframework.retry.annotation.Backoff;
  import org.springframework.retry.annotation.Retryable;
  import org.springframework.retry.annotation.Recover;
  import org.springframework.transaction.annotation.Transactional;

  @Service
  public class MyService {

      @Retryable(value = TransactionRollbackException.class, maxAttempts = 3, backoff = @Backoff(delay = 1000))
      public void executeOperation() {
          performTransactionalWork();
      }

      @Transactional
      private void performTransactionalWork() {
          // 可能失敗的數據庫操作
      }

      @Recover
      public void recover(TransactionRollbackException e) {
          // 記錄錯誤、通知管理員或採取糾正措施
          System.err.println("All retries failed: " + e.getMessage());
      }
  }
  ```
  **注意**：每次重試都會啟動一個新事務，如果需要在重試之間保持原子性，這可能不理想。如果可能，請在 `@Transactional` 方法之外應用此註解。

- **使用 TransactionTemplate 手動重試**：
  為了更好地控制，使用 `TransactionTemplate` 將您的事務代碼包裝在重試循環中：
  ```java
  import org.springframework.transaction.PlatformTransactionManager;
  import org.springframework.transaction.TransactionStatus;
  import org.springframework.transaction.support.TransactionCallbackWithoutResult;
  import org.springframework.transaction.support.TransactionTemplate;

  @Service
  public class MyService {
      private final TransactionTemplate transactionTemplate;
      private static final int MAX_RETRIES = 3;
      private static final long RETRY_DELAY_MS = 1000;

      public MyService(PlatformTransactionManager transactionManager) {
          this.transactionTemplate = new TransactionTemplate(transactionManager);
      }

      public void executeWithRetry() {
          for (int i = 0; i < MAX_RETRIES; i++) {
              try {
                  transactionTemplate.execute(new TransactionCallbackWithoutResult() {
                      @Override
                      protected void doInTransactionWithoutResult(TransactionStatus status) {
                          // 事務代碼在這裡
                      }
                  });
                  return; // 成功，退出循環
              } catch (TransactionRollbackException e) {
                  if (i == MAX_RETRIES - 1) {
                      throw e; // 在最大重試次數後重新拋出
                  }
                  try {
                      Thread.sleep(RETRY_DELAY_MS);
                  } catch (InterruptedException ie) {
                      Thread.currentThread().interrupt();
                  }
              }
          }
      }
  }
  ```
  **注意**：如果鎖持續存在，重試可能無法解決問題，並且如果在回滾失敗之前應用了部分更改，則可能導致狀態不一致。確保重試是冪等的或安全的。

#### 5. 優雅地處理異常
如果由於持續鎖定導致回滾失敗，數據庫狀態可能變得不一致，需要仔細處理：

- **捕獲並記錄**：
  將事務調用包裝在 try-catch 塊中，記錄異常，並通知管理員：
  ```java
  try {
      myService.performTransactionalWork();
  } catch (TransactionRollbackException e) {
      // 記錄錯誤
      logger.error("Transaction rollback failed after retries: " + e.getMessage(), e);
      // 通知管理員（例如，通過電子郵件或監控系統）
      alertSystem.notify("Critical: Transaction rollback failure");
      // 優雅地失敗或進入安全狀態
      throw new RuntimeException("Operation failed due to transaction issues", e);
  }
  ```

- **安全失敗**：如果事務狀態不確定，請停止依賴於它的進一步操作，並發出需要手動干預的信號。

#### 6. 利用數據庫功能
調整數據庫設置以減輕鎖相關問題：

- **鎖超時**：配置數據庫以在鎖等待時快速超時（例如，在 SQL Server 中使用 `SET LOCK_TIMEOUT 5000` 或在 MySQL 中使用 `innodb_lock_wait_timeout`）。這會使事務更早失敗，讓 Spring 更早處理異常。
- **死鎖檢測**：確保啟用數據庫的死鎖檢測並配置為通過自動回滾一個事務來解決衝突。
- **樂觀鎖定**：如果使用 JPA，對實體應用 `@Version` 以使用樂觀鎖定，減少物理鎖爭用：
  ```java
  @Entity
  public class MyEntity {
      @Id
      private Long id;
      @Version
      private Integer version;
      // 其他字段
  }
  ```
  這將衝突檢測轉移到提交時，但可能無法直接解決回滾失敗。

#### 7. 監控和調查
頻繁發生此異常表明存在潛在問題：

- **添加監控**：使用 Spring Boot Actuator 或日誌記錄框架等工具來跟踪這些異常及其頻率。
- **分析日誌**：檢查數據庫和應用程序日誌以查找模式（例如，導致鎖定的特定查詢或事務）。
- **調整併發性**：如果爭用持續存在，請重新審視應用程序的併發模型或數據庫設計。

---

### 回滾失敗的原因
在 20 次嘗試後回滾失敗表明 Spring 的事務管理器在遇到鎖定資源或丟失連接時重試回滾操作，最終放棄。這可能源於：

- **持續鎖定**：另一事務持有的鎖在重試窗口內未釋放。
- **連接問題**：數據庫連接池（例如 HikariCP）耗盡了其獲取連接的重試次數。
- **數據庫配置錯誤**：數據庫或連接池中的超時或重試設置過於激進或不足。

---

### 推薦方法
以下是結合上述策略的實用解決方案：

1. **優化事務和查詢**：保持事務簡短和查詢高效，以減少鎖定持續時間。
2. **設置事務超時**：使用 `@Transactional(timeout = 5)` 在鎖持續存在時快速失敗。
3. **使用重試和恢復處理**：
   ```java
   @Service
   public class MyService {
       @Autowired
       private MyRepository repository;

       public void executeOperationWithRetry() {
           int maxAttempts = 3;
           for (int i = 0; i < maxAttempts; i++) {
               try {
                   performTransactionalWork();
                   return;
               } catch (TransactionRollbackException e) {
                   if (i == maxAttempts - 1) {
                       logger.error("Failed after {} attempts: {}", maxAttempts, e.getMessage(), e);
                       alertSystem.notify("Transaction rollback failure");
                       throw e;
                   }
                   try {
                       Thread.sleep(1000); // 重試前等待
                   } catch (InterruptedException ie) {
                       Thread.currentThread().interrupt();
                   }
               }
           }
       }

       @Transactional
       private void performTransactionalWork() {
           // 數據庫操作
           repository.save(someEntity);
       }
   }
   ```
4. **監控和調整**：記錄異常，設置警報，並調查鎖爭用的原因。

---

### 結論
要在 Spring 中處理當另一事務持有鎖導致連接獲取失敗和重複嘗試時的 `SqlTransactionRollbackException`，請重點關注通過短事務和優化查詢來最小化鎖爭用，根據需要調整事務設置，在更高層級實施謹慎的重試邏輯，並通過記錄和適當通知來處理異常。這確保了系統穩定性和數據完整性，同時通過監控和調整隨時間推移解決根本原因。

---

在使用 IBM DB2 Java 驅動程序（特別是 JDBC 驅動程序）時，處理事務回滾場景對於實現穩健的數據庫交互至關重要。查詢中提到的 `SqlTransactionRollbackException` 似乎是一個輕微的拼寫錯誤。在標準 JDBC 中，特別是從版本 4.0 開始（由現代 IBM DB2 驅動程序如 `db2jcc4.jar` 支持），正確的異常是 **`SQLTransactionRollbackException`**。此異常是 `SQLException` 的子類，並在數據庫事務自動回滾時拋出，例如在死鎖或超時的情況下。

以下是在使用 IBM DB2 JDBC 驅動程序時，如何在 Java 代碼中有效處理 `SQLTransactionRollbackException`：

### 處理異常的方法

1. **使用 Try-Catch 塊**：將您的事務性數據庫操作包裝在 `try` 塊中，並捕獲 `SQLTransactionRollbackException` 以處理數據庫回滾事務的情況。
2. **採取適當措施**：根據應用程序的要求，您可能需要記錄錯誤、重試事務（如果問題是瞬態的，如死鎖）或通知用戶失敗。
3. **確保資源清理**：在 `finally` 塊中正確管理數據庫資源（例如，關閉連接）以避免資源洩漏。
4. **對舊驅動程序的回退**：如果您使用的舊版 DB2 驅動程序不支持 JDBC 4.0，則可能需要捕獲 `SQLException` 並檢查錯誤代碼（例如，在 DB2 中，死鎖導致的回滾錯誤代碼為 `-911`）。

### 示例代碼

以下是一個演示如何處理 `SQLTransactionRollbackException` 的實用示例：

```java
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.SQLTransactionRollbackException;
import javax.sql.DataSource;

public class DB2TransactionExample {
    public void performTransaction(DataSource dataSource) {
        Connection conn = null;
        try {
            // 獲取連接並禁用自動提交以啟動事務
            conn = dataSource.getConnection();
            conn.setAutoCommit(false);

            // 在此處執行您的數據庫操作
            // 例如，執行 INSERT、UPDATE 等語句

            // 如果所有操作成功，提交事務
            conn.commit();
        } catch (SQLTransactionRollbackException e) {
            // 處理數據庫回滾事務的情況
            System.err.println("Transaction rolled back by the database: " + e.getMessage());
            System.err.println("SQL State: " + e.getSQLState() + ", Error Code: " + e.getErrorCode());
            // 示例：SQLState '40001' 和 ErrorCode -911 表示 DB2 中的死鎖或超時
            // 可選擇重試事務或通知用戶
        } catch (SQLException e) {
            // 處理其他 SQL 異常
            System.err.println("SQL Error: " + e.getMessage());
            // 如果事務仍處於活動狀態，嘗試手動回滾
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("Transaction rolled back manually.");
                } catch (SQLException rollbackEx) {
                    System.err.println("Rollback failed: " + rollbackEx.getMessage());
                }
            }
        } finally {
            // 清理資源
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // 恢復默認行為
                    conn.close();
                } catch (SQLException closeEx) {
                    System.err.println("Failed to close connection: " + closeEx.getMessage());
                }
            }
        }
    }
}
```

### 代碼中的關鍵點

- **捕獲 `SQLTransactionRollbackException`**：這專門捕獲 DB2 回滾事務的情況（例如，由於死鎖，由錯誤代碼 `-911` 或 SQL 狀態 `40001` 指示）。
- **通用 `SQLException` 捕獲**：這作為其他數據庫錯誤的後備，確保更廣泛的錯誤處理。
- **手動回滾**：如果發生 `SQLException` 且事務尚未自動回滾，您可以嘗試手動回滾。
- **資源管理**：`finally` 塊確保連接關閉，防止資源洩漏。

### 其他注意事項

- **驅動程序版本**：確保您使用的是符合 JDBC 4.0 的 IBM DB2 驅動程序（例如 `db2jcc4.jar`）。舊版驅動程序（例如 `db2jcc.jar`）可能僅拋出 `SQLException`，要求您手動檢查錯誤代碼。例如：
  ```java
  catch (SQLException e) {
      if (e.getErrorCode() == -911) {
          // 處理由於死鎖或超時導致的事務回滾
      }
  }
  ```
- **SQL 狀態和錯誤代碼**：DB2 使用 SQL 狀態 `40001` 表示序列化失敗（如死鎖），錯誤代碼 `-911` 表示事務自動回滾。錯誤代碼 `-913` 表示由於死鎖導致的語句失敗，但除非顯式回滾，否則事務仍處於活動狀態。
- **重試邏輯**：對於像死鎖這樣的瞬態問題，您可以實施重試機制：
  ```java
  int maxRetries = 3;
  for (int attempt = 1; attempt <= maxRetries; attempt++) {
      try {
          performTransaction(dataSource);
          break; // 成功，退出循環
      } catch (SQLTransactionRollbackException e) {
          if (attempt == maxRetries) {
              throw e; // 在最大重試次數後重新拋出
          }
          Thread.sleep(1000 * attempt); // 重試前退避等待
      }
  }
  ```

### 結論

要在 IBM DB2 Java 驅動程序中處理 `SQLTransactionRollbackException`（正確拼寫為 `SQLTransactionRollbackException`），請使用 `try-catch` 塊捕獲此特定異常以處理事務回滾場景。結合適當的資源管理，並在必要時通過檢查像 `-911` 這樣的錯誤代碼為舊驅動程序提供回退邏輯。這種方法確保您的應用程序能夠優雅地處理事務回滾，同時保持數據庫完整性和用戶體驗。