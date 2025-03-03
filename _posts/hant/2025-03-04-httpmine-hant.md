---
audio: false
generated: true
lang: hant
layout: post
title: 使用 httpmine
translated: true
---

我假設你指的是 "httpmime.jar" 而不是 "httpmine.jar"，因為 "httpmime" 是 Apache HttpComponents 的一個著名庫，用於處理 HTTP 請求中的 MIME 多部分實體（例如文件上傳）。如果我搞錯了，請澄清！以下是如何在 Java 專案中使用 `httpmime.jar`：

---

### 什麼是 `httpmime.jar`？
`httpmime.jar` 是 Apache HttpComponents 專案的一部分。它通過提供對 multipart/form-data 請求的支持來擴展 `httpclient.jar` 的功能，這些請求通常用於上傳文件或通過 HTTP 發送複雜數據。

要使用它，你還需要它的依賴項，如 `httpclient.jar` 和 `httpcore.jar`，因為 `httpmime` 基於這些庫。

---

### 在 Java 專案中使用 `httpmime.jar` 的步驟

#### 1. **下載 JAR 文件**
- 訪問 [Apache HttpComponents 下載頁面](https://hc.apache.org/downloads.cgi) 或 `httpmime` 的 Maven 存儲庫（例如 [版本 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)）。
- 下載 `httpmime-<version>.jar` 文件（例如 `httpmime-4.5.14.jar`）。
- 你還需要：
  - `httpclient-<version>.jar`（例如 `httpclient-4.5.14.jar`）
  - `httpcore-<version>.jar`（例如 `httpcore-4.4.16.jar`）
- 確保版本兼容（檢查 [專案依賴項](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)）。

或者，如果你使用 Maven 或 Gradle，跳過手動下載並通過你的構建工具添加它（見步驟 2）。

#### 2. **將 JAR 添加到你的專案**
- **手動方法（無構建工具）：**
  - 將下載的 `httpmime.jar`、`httpclient.jar` 和 `httpcore.jar` 文件放在一個文件夾中（例如，專案目錄中的 `lib/`）。
  - 如果使用 IDE 如 Eclipse 或 IntelliJ：
    - **Eclipse**：右鍵點擊你的專案 > 屬性 > Java 構建路徑 > 類庫 > 添加外部 JARs > 選擇 JARs > 應用。
    - **IntelliJ**：文件 > 專案結構 > 模組 > 依賴項 > "+" > JARs 或目錄 > 選擇 JARs > 確定。
  - 如果從命令行運行，在你的類路徑中包含 JARs：
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **使用 Maven（推薦）：**
  將以下內容添加到你的 `pom.xml`：
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- 使用最新版本 -->
  </dependency>
  ```
  Maven 將自動拉取 `httpclient` 和 `httpcore` 作為轉移依賴項。

- **使用 Gradle：**
  將以下內容添加到你的 `build.gradle`：
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **編寫代碼以使用 `httpmime`**
以下是使用 `httpmime` 通過多部分 HTTP POST 請求上傳文件的示例：

```java
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.HttpResponse;
import java.io.File;

public class FileUploadExample {
    public static void main(String[] args) throws Exception {
        // 創建一個 HTTP 客戶端
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // 定義要發送請求的 URL
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // 构建多部分實體
        File file = new File("path/to/your/file.txt"); // 替換為你的文件路徑
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // 添加文件
        builder.addTextBody("description", "This is a test file"); // 添加文本字段（可選）

        // 將實體設置為 POST 請求
        httpPost.setEntity(builder.build());

        // 執行請求
        HttpResponse response = httpClient.execute(httpPost);

        // 打印響應狀態
        System.out.println("Response Code: " + response.getStatusLine().getStatusCode());

        // 清理
        httpClient.close();
    }
}
```

#### 4. **關鍵類和使用方法**
- **`MultipartEntityBuilder`**：用於構建多部分實體。你可以添加文件（`addPart`）、文本（`addTextBody`）或二進制數據（`addBinaryBody`）。
- **`FileBody`**：表示要上傳的文件。
- **`CloseableHttpClient`**：來自 `httpclient.jar` 的 HTTP 客戶端來執行請求。

#### 5. **運行你的程序**
- 如果使用 IDE，只需運行程序。
- 如果使用命令行，使用上述類路徑編譯和運行。

#### 6. **故障排除**
- **ClassNotFoundException**：確保所有所需的 JARs（`httpmime`、`httpclient`、`httpcore`）在你的類路徑中。
- **版本不匹配**：使用兼容的 JARs 版本（例如，`httpmime-4.5.14` 與 `httpclient-4.5.14` 和 `httpcore-4.4.16`）。
- **Android 專案**：Android 有一個自己的 `org.apache.http` 包，這可能會衝突。要麼排除內建版本，要麼使用重新打包的 JAR（例如，通過 JarJar）。

---

### 示例用例
如果你要將文件上傳到伺服器（例如 REST API），`httpmime` 簡化了創建 `multipart/form-data` 請求，這是文件上傳的標準。

如果你需要澄清或幫助特定情況，請告訴我！