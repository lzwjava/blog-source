---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 開發工具自動重啟
translated: true
type: note
---

當你使用 `mvn spring-boot:run` 運行 Spring Boot 應用程式時，檔案監聽和自動重啟或熱重載功能預設是不啟用的。不過，你可以透過在專案中加入 `spring-boot-devtools` 依賴來啟用這些功能。這個模組提供了自動重啟和 LiveReload 等功能，以加快開發速度。

### 詳細說明
1. **沒有 DevTools 時的預設行為**：
   - 在沒有 `spring-boot-devtools` 的情況下運行 `mvn spring-boot:run`，不會包含檔案監聽或自動重啟功能。你需要手動停止並重啟應用程式，以應用對 Java 類別、靜態資源或模板的更改。
   - 靜態資源（例如 HTML、CSS、JS）可能需要完整重建或重啟，除非另行配置。

2. **使用 `spring-boot-devtools`**：
   - **檔案監聽**：DevTools 會監控 classpath 中 Java 檔案、屬性檔案以及某些資源（例如 `/resources`、`/static`、`/templates`）的更改。
   - **自動重啟**：當 classpath 上的檔案發生更改（例如 Java 類別或屬性檔案），DevTools 會觸發應用程式的自動重啟。這比冷啟動更快，因為它使用了兩個 classloader：一個用於未更改的第三方函式庫（基礎 classloader），另一個用於你的應用程式碼（重啟 classloader）。
   - **LiveReload**：對靜態資源（例如 `/static`、`/public` 或 `/templates` 中的 HTML、CSS、JS）或模板（例如 Thymeleaf）的更改會觸發瀏覽器刷新，而不是完整重啟，前提是你已安裝 LiveReload 瀏覽器擴充功能（支援 Chrome、Firefox、Safari）。
   - **排除項目**：預設情況下，`/META-INF/maven`、`/META-INF/resources`、`/resources`、`/static`、`/public` 和 `/templates` 中的資源不會觸發重啟，但會觸發 LiveReload。你可以使用 `spring.devtools.restart.exclude` 來自訂此行為。

3. **DevTools 的設定**：
   在你的 `pom.xml` 中加入以下依賴：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - `<optional>true</optional>` 確保 DevTools 不會包含在生產環境建置中。
   - 使用 `mvn spring-boot:run` 運行應用程式。DevTools 會自動啟用檔案監聽和自動重啟。

4. **在 IDE 中的行為**：
   - **Eclipse**：儲存更改（Ctrl+S）會自動觸發建置，DevTools 會偵測到並重啟應用程式。
   - **IntelliJ IDEA**：你需要手動觸發建置（Ctrl+F9 或 "Make Project"）才能讓 DevTools 偵測到更改，除非你配置了自動建置。或者，在 IntelliJ 設定中啟用 "Build project automatically" 以實現無縫重啟。
   - 對於 LiveReload，請從 http://livereload.com/extensions/ 安裝瀏覽器擴充功能並啟用它。

5. **替代方案：Spring Loaded**：
   - 除了 DevTools，你還可以使用 Spring Loaded 來實現更高級的熱替換（例如方法簽名更改）。將其加入 `spring-boot-maven-plugin`：
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - 相較於 DevTools，Spring Loaded 較不推薦，因為它維護不那麼活躍，且可能不支援所有框架。

6. **靜態資源的熱重載**：
   - 沒有 DevTools 時，你可以透過設定 `spring-boot-maven-plugin` 的 `addResources` 屬性來啟用靜態資源的熱重載：
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - 這會將 `src/main/resources` 加入 classpath，允許就地編輯靜態檔案，但它的功能不如 DevTools 全面。

7. **注意事項**：
   - DevTools 在多模組專案中可能會引起類別載入問題。如果發生這種情況，嘗試使用 `spring.devtools.restart.enabled=false` 停用重啟，或使用 JRebel 來實現更高級的重載功能。
   - 對於非 classpath 檔案，使用 `spring.devtools.restart.additional-paths` 來監控其他目錄。
   - LiveReload 需要瀏覽器擴充功能，且可能不適用於所有前端設定（例如使用 Webpack 的 React）。
   - 如果重啟速度較慢，調整 `spring.devtools.restart.poll-interval` 和 `spring.devtools.restart.quiet-period` 以優化檔案監聽。

### 簡單應用程式的步驟
1. 建立一個基本的 Spring Boot 應用程式（例如使用 Spring Initializr 並加入 `spring-boot-starter-web`）。
2. 將 `spring-boot-devtools` 依賴加入 `pom.xml`。
3. 運行 `mvn spring-boot:run`。
4. 修改 Java 檔案、屬性檔案或靜態資源（例如 `src/main/resources/static` 中的 HTML）。
5. 觀察自動重啟（針對 Java/屬性檔案）或瀏覽器刷新（針對啟用了 LiveReload 的靜態資源）。

### 範例
對於一個具有 REST 控制器的簡單應用程式：
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- 加入 DevTools，運行 `mvn spring-boot:run`，並更改 `hello()` 方法的回傳值。應用程式會自動重啟。
- 在 `src/main/resources/static` 中加入 `index.html`，安裝 LiveReload 擴充功能，並修改 HTML。瀏覽器會在不重啟的情況下刷新。

### 結論
對於簡單的 Spring Boot 應用程式，加入 `spring-boot-devtools` 是啟用檔案監聽、自動重啟和熱重載的最簡單方法。使用帶有 DevTools 的 `mvn spring-boot:run` 可以獲得無縫的開發體驗。如果你需要更高級的熱替換功能，可以考慮 Spring Loaded 或 JRebel，但 DevTools 在大多數情況下已經足夠。

---

以下是一個範例，展示如何使用 `application.yml` 檔案為你的 Spring Boot 應用程式配置 `spring-boot-devtools`，以實現檔案監聽、自動重啟和熱重載。此配置是根據你提供的日誌（顯示 DevTools 正在活動並監控 `target/classes`）為你的 `blog-server` 專案量身定制的。

### `application.yml` 配置
```yaml
spring:
  devtools:
    restart:
      # 啟用自動重啟（預設：true）
      enabled: true
      # 用於監控重啟的額外目錄（例如自訂配置資料夾）
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # 排除觸發重啟的檔案/目錄（保留預設排除項目）
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # 檔案更改的輪詢間隔（單位：毫秒，預設：1000）
      poll-interval: 1000
      # 檔案更改後重啟前的靜默期（單位：毫秒，預設：400）
      quiet-period: 400
      # 選項：用於手動觸發重啟的檔案
      trigger-file: .restart
    livereload:
      # 啟用 LiveReload 以在靜態資源更改時刷新瀏覽器（預設：true）
      enabled: true
```

### 設定說明
- **`spring.devtools.restart.enabled`**：當 classpath 檔案更改時（例如 `target/classes`，如你的日誌所示：`file:/home/lzw/Projects/blog-server/target/classes/`）啟用自動重啟。
- **`spring.devtools.restart.additional-paths`**：監控額外目錄（例如 `/home/lzw/Projects/blog-server/config`）的更改以觸發重啟。
- **`spring.devtools.restart.exclude`**：防止對 `static/`、`public/`、`templates/`、`logs/` 或 `generated/` 目錄的更改觸發重啟，同時允許對靜態資源（例如 HTML、CSS、JS）進行 LiveReload。
- **`spring.devtools.restart.poll-interval`**：設定 DevTools 檢查檔案更改的頻率（1000ms = 1 秒）。
- **`spring.devtools.restart.quiet-period`**：在偵測到更改後等待 400ms，以確保沒有進一步的更改待處理，然後再重啟。
- **`spring.devtools.restart.trigger-file`**：透過更新 `.restart` 來允許手動重啟（例如 `touch /home/lzw/Projects/blog-server/.restart`）。
- **`spring.devtools.livereload.enabled`**：啟用 LiveReload 伺服器，該伺服器會針對 `static/` 或 `templates/` 中的更改觸發瀏覽器刷新（需要 LiveReload 瀏覽器擴充功能）。

### 應用步驟
1. 建立或更新 `src/main/resources/application.yml`，加入上述配置。
2. 確保 `spring-boot-devtools` 已加入你的 `pom.xml`：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. 運行 `mvn spring-boot:run`。DevTools 將監控 `target/classes` 和 `/home/lzw/Projects/blog-server/config`（如果已加入），在 Java 或屬性檔案更改時重啟應用程式，並在靜態資源更改時刷新瀏覽器。
4. 對於 LiveReload，請安裝瀏覽器擴充功能（例如從 http://livereload.com/extensions/）或在前端整合 LiveReload 客戶端。

### 注意事項
- 你的日誌顯示啟動速度很快（0.8 秒），因此預設的 `poll-interval` 和 `quiet-period` 應該沒問題。如果在較大的專案中感覺重啟速度遲緩，請調整它們（例如 `poll-interval: 500`）。
- 如果你不需要 LiveReload（例如使用獨立的前端開發伺服器），請設定 `livereload.enabled: false`。
- 對於手動重啟，請在專案根目錄中建立 `.restart` 並在需要時更新它。

這個 YAML 配置應該可以與你的設定無縫協作，增強你已經體驗到的檔案監聽和自動重啟功能。