---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 源碼探索指南
translated: true
type: note
---

閱讀一個使用 Maven、Spring Boot 和 Java 建構的大型專案源碼，特別是包含多模組和網路配置的專案，起初可能會讓人感到無從下手。然而，透過結構化的方法，您就能快速導航並理解程式碼庫。以下是一份逐步指南，幫助您有效率地閱讀和理解這類專案。

---

### **1. 理解專案結構**
首先從高層次視角了解專案：
- **根目錄 `pom.xml`**：由於這是 Maven 多模組專案，請打開根目錄的 `pom.xml` 檔案。這裡列出了所有模組（例如 `<modules>` 區段），並提供了專案結構的概覽。每個模組通常負責特定功能或層次（例如網路、資料、核心）。
- **目錄佈局**：熟悉 Maven 的標準結構：
  - `src/main/java`：主要的 Java 原始碼。
  - `src/main/resources`：配置檔案（例如 `application.properties` 或 `application.yml`）。
  - `src/test/java`：測試類別。
- **Spring Boot 進入點**：尋找帶有 `@SpringBootApplication` 註解的類別。這是 Spring Boot 應用的主要類別，也是應用的啟動點。

---

### **2. 探索配置與依賴關係**
關鍵檔案揭示了專案的設定方式：
- **配置檔案**：檢查 `src/main/resources` 中的 `application.properties` 或 `application.yml`。這些檔案定義了資料庫連接、伺服器端口和 Spring Boot 配置等設定。
- **依賴關係**：檢視根目錄和各模組中的 `pom.xml` 檔案。`<dependencies>` 區段顯示了使用的函式庫（例如 Spring Data、Hibernate），幫助您理解專案的功能。
- **網路配置**：對於網路模組，尋找帶有 `@Controller` 或 `@RestController` 註解的類別，這些類別處理 HTTP 請求，或是擴展 `WebMvcConfigurer` 的配置類別。

---

### **3. 追蹤應用流程**
跟隨執行路徑來了解應用的運作方式：
- **進入點**：從帶有 `main` 方法的 `@SpringBootApplication` 類別開始，該方法用於啟動應用。
- **請求處理**：對於網路應用：
  - 尋找帶有 `@GetMapping` 或 `@PostMapping` 等映射的控制器。
  - 檢查控制器呼叫的服務類別，這些類別負責業務邏輯。
  - 探索服務用於與資料互動的儲存庫或資料存取物件。
- **組件掃描**：Spring Boot 預設會掃描主要類別所在套件下的組件（例如 `@Service`、`@Repository`）。如果此行為被自訂，請尋找 `@ComponentScan`。

---

### **4. 分析模組互動**
了解模組之間的連接方式：
- **模組依賴關係**：檢查每個模組的 `pom.xml` 中的 `<dependencies>`，了解哪些模組依賴於其他模組。
- **共享模組**：尋找包含共享工具、實體或服務的「核心」或「通用」模組。
- **打包方式**：注意模組是打包為 JAR 檔案，還是合併為 WAR 檔案進行部署。

---

### **5. 利用工具進行導航**
使用工具讓探索更輕鬆：
- **IDE 功能**：在 IntelliJ IDEA 或 Eclipse 中：
  - 使用「前往定義」跳轉到類別/方法的定義。
  - 使用「查找用法」查看某個元素的使用位置。
  - 檢查「呼叫層次結構」以追蹤方法呼叫。
- **Maven 指令**：在終端機中執行 `mvn dependency:tree`，以視覺化模組和函式庫之間的依賴關係。
- **Spring Boot Actuator**：如果啟用，存取 `/actuator/beans` 以列出應用上下文中的所有 Spring bean。

---

### **6. 聚焦關鍵區域**
優先關注程式碼庫的關鍵部分：
- **業務邏輯**：尋找包含核心功能的服務類別。
- **資料存取**：檢查儲存庫介面（例如 `@Repository`）或 DAO 類別，了解資料庫互動方式。
- **安全性**：如果存在安全性配置，尋找如 `WebSecurityConfigurerAdapter` 或 `@EnableGlobalMethodSecurity` 等配置。
- **錯誤處理**：搜尋全域異常處理器（例如 `@ControllerAdvice`）或自訂錯誤設定。

---

### **7. 使用文件與註解**
在專案中尋找指引：
- **README 檔案**：根目錄或模組中的 `README.md` 通常會解釋專案和設定步驟。
- **程式碼註解**：閱讀複雜類別/方法中的 JavaDoc 或行內註解，以獲得清晰的理解。
- **配置說明**：檢查 `application.properties` 或 `application.yml` 中的註解，了解設定的解釋。

---

### **8. 執行與除錯應用**
透過實際操作加深理解：
- **建置與執行**：使用 `mvn clean install` 建置專案，並使用 `mvn spring-boot:run` 啟動應用。
- **除錯**：在 IDE 中設定中斷點，並逐步執行程式碼以觀察運行時的流程。
- **日誌**：查看日誌語句（例如透過 SLF4J），了解應用在執行過程中報告的內容。

---

### **9. 識別模式與實踐**
辨識程式碼的結構方式：
- **Spring 功能**：注意依賴注入（`@Autowired`）、事務管理（`@Transactional`）或切面（`@Aspect`）的使用。
- **設計模式**：尋找如 Repository、Factory 或 Singleton 等模式，以理解架構。
- **分層結構**：觀察套件組織（例如 `controller`、`service`、`repository`），了解關注點分離的實現。

---

### **10. 分解與迭代**
管理複雜性：
- **從小處著手**：一次專注於一個模組或功能，而不是整個專案。
- **記錄筆記**：在探索過程中記下關鍵類別、流程和配置。
- **迭代**：根據需要重複上述步驟，逐步建立對程式碼庫的更完整理解。

---

透過這種方法，您將能快速掌握基於 Maven 的多模組 Spring Boot 專案源碼，即使其中包含複雜的網路配置。保持耐心，善用工具，並一步步深入探索！