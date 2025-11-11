---
audio: false
generated: true
lang: hant
layout: post
title: 春季啟動中的死結
translated: true
type: note
---

讓我們深入探討如何在 Spring Boot 專案中解決當多個請求同時呼叫 bean 方法時發生的死結問題。死結通常發生在兩個或多個執行緒因競爭共享資源（如資料庫鎖定、同步區塊或執行緒安全的資料結構）而無限期互相阻塞的情況。考慮到您提到 bean 方法需處理大量請求，我將假設這是一個單例作用域的 bean（Spring 的預設作用域），並探討常見原因與解決方案。

首先，讓我們識別在此情境下可能發生的死結情況：
1. **資料庫鎖定**：如果 bean 方法與資料庫互動（例如透過 JPA/Hibernate），並行交易可能以衝突的順序鎖定資料列或資料表。
2. **同步區塊**：如果方法使用 `synchronized` 關鍵字或鎖定機制（如 `ReentrantLock`），不當的鎖定順序可能導致執行緒互相等待。
3. **共享資源**：如果 bean 修改共享的記憶體資源（如靜態變數或集合），競爭可能導致死結。
4. **外部呼叫**：如果方法呼叫外部服務或 API，延遲或阻塞行為可能加劇並行問題。

由於您未提供具體程式碼，我將提供診斷與修復問題的通用方法，並附上具體範例。

### 步驟 1：診斷死結
- **啟用日誌記錄**：添加日誌記錄（例如使用 SLF4J 與 Logback）來追蹤方法進入、退出及資源存取情況，有助於識別執行緒停滯的位置。
- **執行緒傾印**：當死結發生時，擷取執行緒傾印（例如使用 `jstack` 或 VisualVM）。檢查處於 `BLOCKED` 或 `WAITING` 狀態的執行緒，並分析其堆疊追蹤以找出鎖定競爭。
- **監控工具**：使用 Spring Actuator 或分析工具（如 YourKit）來觀察高負載下的執行緒行為。

### 步驟 2：常見修復方法
根據可能的原因，以下是解決死結的方法：

#### 情況 1：資料庫相關死結
如果 bean 方法執行資料庫操作，死結通常源自交易衝突。
- **解決方案**：最佳化交易邊界與鎖定取得順序。
  - 使用 `@Transactional` 並設定適當的隔離等級（例如，除非必要，否則使用 `READ_COMMITTED` 而非 `SERIALIZABLE`）。
  - 確保資源存取順序一致（例如總是先更新資料表 A 再更新資料表 B）。
  - 透過將非交易邏輯移至 `@Transactional` 外部來縮小交易範圍。
- **範例**：
  ```java
  @Service
  public class MyService {
      @Autowired
      private MyRepository repo;

      @Transactional
      public void processRequest(Long id1, Long id2) {
          // 確保一致順序以避免死結
          if (id1 < id2) {
              repo.updateEntity(id1);
              repo.updateEntity(id2);
          } else {
              repo.updateEntity(id2);
              repo.updateEntity(id1);
          }
      }
  }
  ```
- **進階技巧**：設定交易逾時（例如 `@Transactional(timeout = 5)`）以中止長時間運行的交易，避免無限期等待。

#### 情況 2：同步區塊或鎖定
如果方法使用顯式鎖定，當不同執行緒以不同順序取得鎖定時可能發生死結。
- **解決方案**：使用單一鎖定或強制鎖定順序。
  - 若可行，以單一粗粒度鎖定取代多個 `synchronized` 區塊。
  - 使用帶有逾時機制的 `ReentrantLock` 避免無限期阻塞。
- **範例**：
  ```java
  @Service
  public class MyService {
      private final ReentrantLock lock = new ReentrantLock();

      public void processRequest(String resourceA, String resourceB) {
          try {
              if (lock.tryLock(2, TimeUnit.SECONDS)) {
                  // 關鍵區段
                  System.out.println("Processing " + resourceA + " and " + resourceB);
              } else {
                  throw new RuntimeException("Could not acquire lock in time");
              }
          } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
          } finally {
              if (lock.isHeldByCurrentThread()) {
                  lock.unlock();
              }
          }
      }
  }
  ```

#### 情況 3：共享記憶體資源
如果 bean 修改共享集合或變數，並行存取可能導致問題。
- **解決方案**：使用執行緒安全替代方案或避免共享狀態。
  - 將 `ArrayList` 替換為 `CopyOnWriteArrayList` 或 `Collections.synchronizedList`。
  - 對映射表使用 `ConcurrentHashMap`。
  - 更佳做法是使 bean 成為無狀態或使用請求作用域的 bean（`@Scope("request")`）。
- **範例**：
  ```java
  @Service
  @Scope("prototype") // 若為有狀態則避免單例
  public class MyService {
      private final ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();

      public void processRequest(String key, int value) {
          cache.put(key, value); // 執行緒安全
      }
  }
  ```

#### 情況 4：高並行負載
如果死結源自對 bean 的請求過載，執行緒競爭可能是根本原因。
- **解決方案**：引入非同步處理或速率限制。
  - 使用 `@Async` 將工作卸載至執行緒池。
  - 透過 `TaskExecutor` 設定執行緒池來管理並行。
- **範例**：
  ```java
  @Service
  public class MyService {
      @Async
      public CompletableFuture<String> processRequest(String input) {
          // 模擬工作
          Thread.sleep(1000);
          return CompletableFuture.completedFuture("Done: " + input);
      }
  }

  @Configuration
  @EnableAsync
  public class AsyncConfig {
      @Bean
      public TaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(10);
          executor.setMaxPoolSize(50);
          executor.setQueueCapacity(100);
          return executor;
      }
  }
  ```
- **使用方式**：在控制器中呼叫 `processRequest` 並處理傳回的 `CompletableFuture`。

### 步驟 3：預防未來問題
- **負載測試**：使用 JMeter 或 Gatling 等工具模擬高並行情境，及早發現死結。
- **程式碼審查**：檢查是否存在嵌套鎖定、長時間運行交易或共享可變狀態。
- **逾時設定**：始終為鎖定、交易或外部呼叫設定逾時。

### 總結
在未看到您的 bean 程式碼的情況下，我假設這是一個承受高負載的單例 bean，可能存在資料庫或鎖定競爭。如果您能提供更多細節（例如方法程式碼、堆疊追蹤或存取的資源），我可以進一步客製化解決方案。目前，建議先透過執行緒傾印進行診斷，並應用相關修復—無論是資料庫最佳化、鎖定管理還是非同步處理。期待您的回饋！