---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 異常處理
translated: true
type: note
---

在使用 Spring Boot 或更廣泛的 Spring Framework 時，開發人員經常會因配置問題、運行時錯誤或 API 使用不當而遇到異常。以下是您可能會遇到的常見異常列表，以及它們的典型原因和潛在解決方案。為清晰起見，這些異常已按類別分組。

---

### **1. 配置相關異常**

- **`org.springframework.beans.factory.BeanCreationException`**：
  - **原因**：由於缺少依賴項、配置錯誤或實例化錯誤，導致 Bean 創建失敗。
  - **範例**：缺少 `@Component`、`@Service` 或 `@Autowired` 依賴項未找到。
  - **解決方法**：檢查 Bean 定義，確保依賴項可用，並驗證註解。

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`**：
  - **原因**：Spring 在應用程式上下文中找不到請求類型或名稱的 Bean。
  - **範例**：嘗試 `@Autowired` 一個未定義或未被掃描到的 Bean。
  - **解決方法**：確保 Bean 已添加註解（例如 `@Component`）並且位於組件掃描路徑內。

- **`org.springframework.context.ApplicationContextException`**：
  - **原因**：Spring 應用程式上下文初始化失敗。
  - **範例**：`application.properties` 中的配置無效或 `@Configuration` 類別中存在語法錯誤。
  - **解決方法**：查看堆疊追蹤以找出根本原因（例如，無效的屬性或缺少資源）。

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`**：
  - **原因**：Bean 所需的依賴項無法滿足。
  - **範例**：循環依賴或介面缺少實作。
  - **解決方法**：打破循環依賴（例如，使用 `@Lazy`）或提供缺少的依賴項。

---

### **2. Web 和 REST 相關異常**

- **`org.springframework.web.bind.MissingServletRequestParameterException`**：
  - **原因**：HTTP 請求中缺少必需的請求參數。
  - **範例**：指定了 `@RequestParam("id")`，但客戶端未發送 `id`。
  - **解決方法**：將參數設為可選（`required = false`）或確保客戶端包含該參數。

- **`org.springframework.http.converter.HttpMessageNotReadableException`**：
  - **原因**：請求主體無法反序列化（例如，格式錯誤的 JSON）。
  - **範例**：向 `@RequestBody` 端點發送無效的 JSON。
  - **解決方法**：驗證請求承載並確保其與目標物件結構匹配。

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`**：
  - **原因**：方法參數無法轉換為預期類型。
  - **範例**：將字串（如 `"abc"`）傳遞給期望 `int` 類型的參數。
  - **解決方法**：驗證輸入或使用自定義轉換器。

- **`org.springframework.web.servlet.NoHandlerFoundException`**：
  - **原因**：請求的 URL 沒有對應的控制器映射。
  - **範例**：`@RequestMapping` 中存在拼寫錯誤或缺少控制器。
  - **解決方法**：驗證端點映射並確保控制器已被掃描。

---

### **3. 資料存取（Spring Data/JPA/Hibernate）異常**

- **`org.springframework.dao.DataIntegrityViolationException`**：
  - **原因**：資料庫操作違反了約束（例如，唯一鍵或外來鍵）。
  - **範例**：插入重複的主鍵值。
  - **解決方法**：檢查資料的唯一性，或優雅地處理異常。

- **`org.springframework.orm.jpa.JpaSystemException`**：
  - **原因**：與 JPA 相關的運行時錯誤，通常包裝了 Hibernate 異常。
  - **範例**：約束違反或連接問題。
  - **解決方法**：檢查嵌套異常（例如 `SQLException`）以獲取詳細資訊。

- **`org.hibernate.LazyInitializationException`**：
  - **原因**：嘗試在活躍的 Session 之外存取延遲加載的實體。
  - **範例**：在事務結束後存取 `@OneToMany` 關係。
  - **解決方法**：使用積極載入（eager fetching）、在查詢中獲取（例如 `JOIN FETCH`）或確保 Session 處於開啟狀態。

- **`org.springframework.dao.InvalidDataAccessApiUsageException`**：
  - **原因**：不正確地使用 Spring Data 或 JDBC API。
  - **範例**：向需要值的查詢傳遞 null 參數。
  - **解決方法**：驗證查詢參數和 API 使用方式。

---

### **4. 安全性相關異常**

- **`org.springframework.security.access.AccessDeniedException`**：
  - **原因**：已驗證的使用者缺乏對資源的權限。
  - **範例**：在沒有所需角色的情況下存取受保護的端點。
  - **解決方法**：檢查 `@PreAuthorize` 或安全性配置，並調整角色/權限。

- **`org.springframework.security.authentication.BadCredentialsException`**：
  - **原因**：由於使用者名稱或密碼不正確導致驗證失敗。
  - **範例**：使用者在登入表中輸入錯誤的憑證。
  - **解決方法**：確保憑證正確；自定義錯誤處理以提供使用者回饋。

- **`org.springframework.security.authentication.DisabledException`**：
  - **原因**：使用者帳戶已被停用。
  - **範例**：`UserDetails` 實作返回 `isEnabled() == false`。
  - **解決方法**：啟用帳戶或更新使用者狀態。

---

### **5. 其他運行時異常**

- **`java.lang.IllegalStateException`**：
  - **原因**：Spring 在執行過程中遇到無效狀態。
  - **範例**：在尚未完全初始化的 Bean 上呼叫方法。
  - **解決方法**：檢查生命週期方法或 Bean 的初始化順序。

- **`org.springframework.transaction.TransactionException`**：
  - **原因**：在事務管理期間發生問題。
  - **範例**：由於未處理的異常導致事務回滾。
  - **解決方法**：確保正確使用 `@Transactional` 並在事務內處理異常。

- **`java.lang.NullPointerException`**：
  - **原因**：嘗試存取 null 物件參考。
  - **範例**：由於配置錯誤，`@Autowired` 依賴項未被注入。
  - **解決方法**：添加 null 檢查或偵錯找出依賴項缺失的原因。

---

### **6. Spring Boot 特定異常**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`**（舊版本）或 **`org.springframework.boot.web.server.WebServerException`**（新版本）：
  - **原因**：無法啟動內嵌的 Web 伺服器（例如 Tomcat、Jetty）。
  - **範例**：連接埠已被佔用（例如 `8080`）。
  - **解決方法**：在 `application.properties` 中更改連接埠（`server.port=8081`）或釋放被佔用的連接埠。

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`**：
  - **原因**：配置資料來源失敗。
  - **範例**：缺少或不正確的 `spring.datasource.url/username/password`。
  - **解決方法**：驗證 `application.properties` 或 `application.yml` 中的資料來源屬性。

- **`org.springframework.boot.SpringApplication - Application run failed`**：
  - **原因**：Spring Boot 啟動期間發生一般性失敗。
  - **範例**：配置錯誤、缺少 Bean 或依賴項衝突。
  - **解決方法**：檢查完整的堆疊追蹤以找出根本原因。

---

### **處理異常的最佳實踐**

1. **全域異常處理**：
   - 使用 `@ControllerAdvice` 與 `@ExceptionHandler` 來捕獲並在整個應用程式中一致地處理異常。
   - 範例：
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("發生資料完整性違規。");
         }
     }
     ```

2. **日誌記錄**：
   - 使用 SLF4J/Logback 等框架記錄異常，以協助偵錯。

3. **自定義異常**：
   - 定義應用程式特定的異常，並將它們映射到適當的 HTTP 狀態碼。

4. **驗證**：
   - 使用 `@Valid` 和 Bean Validation（例如 `@NotNull`）來及早捕獲錯誤，避免運行時異常。

5. **偵錯**：
   - 在 `application.properties` 中啟用詳細日誌記錄（`logging.level.org.springframework=DEBUG`）來追蹤問題。

---

### **結論**

這些是您在使用 Spring Boot 或 Spring Framework 時最常遇到的異常。了解它們的原因和解決方法可以顯著加快開發和偵錯速度。如果您遇到特定異常並需要更深入的了解，請隨時分享詳細資訊，我將提供量身訂製的解釋！