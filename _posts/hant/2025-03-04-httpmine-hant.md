---
audio: false
generated: true
lang: hant
layout: post
title: 使用Httpmine
translated: true
type: note
---

我猜你指的是「httpmime.jar」而非「httpmine.jar」，因為「httpmime」是 Apache HttpComponents 中一個著名的函式庫，用於處理 HTTP 請求中的 MIME 多部分實體（例如檔案上傳）。如果我理解有誤，請指正！以下是在 Java 專案中使用 `httpmime.jar` 的方法：

---

### 什麼是 `httpmime.jar`？
`httpmime.jar` 是 Apache HttpComponents 專案的一部分。它擴展了 `httpclient.jar` 的功能，提供對 multipart/form-data 請求的支援，這類請求常用於上傳檔案或透過 HTTP 傳送複雜資料。

使用時，你還需要其依賴項，例如 `httpclient.jar` 和 `httpcore.jar`，因為 `httpmime` 是基於這些函式庫構建的。

---

### 在 Java 專案中使用 `httpmime.jar` 的步驟

#### 1. **下載 JAR 檔案**
- 訪問 [Apache HttpComponents 下載頁面](https://hc.apache.org/downloads.cgi) 或 Maven Repository 中的 `httpmime`（例如 [版本 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)）。
- 下載 `httpmime-<版本>.jar` 檔案（例如 `httpmime-4.5.14.jar`）。
- 你還需要：
  - `httpclient-<版本>.jar`（例如 `httpclient-4.5.14.jar`）
  - `httpcore-<版本>.jar`（例如 `httpcore-4.4.16.jar`）
- 確保版本相容（檢查 [專案依賴關係](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)）。

如果你使用 Maven 或 Gradle，可以跳過手動下載，透過建置工具添加（見步驟 2）。

#### 2. **將 JAR 添加到你的專案**
- **手動方法（無建置工具）：**
  - 將下載的 `httpmime.jar`、`httpclient.jar` 和 `httpcore.jar` 檔案放在一個資料夾中（例如專案目錄下的 `lib/`）。
  - 如果使用 IDE 如 Eclipse 或 IntelliJ：
    - **Eclipse**：右鍵點擊專案 > Properties > Java Build Path > Libraries > Add External JARs > 選擇 JARs > Apply。
    - **IntelliJ**：File > Project Structure > Modules > Dependencies > "+" > JARs or directories > 選擇 JARs > OK。
  - 如果從命令列執行，請將 JARs 包含在 classpath 中：
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
  Maven 會自動拉取 `httpclient` 和 `httpcore` 作為傳遞依賴。

- **使用 Gradle：**
  將以下內容添加到你的 `build.gradle`：
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **編寫使用 `httpmime` 的程式碼**
以下是使用 `httpmime` 透過 multipart HTTP POST 請求上傳檔案的範例：

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
        // 建立 HTTP client
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // 定義請求發送的 URL
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // 建置 multipart entity
        File file = new File("path/to/your/file.txt"); // 替換為你的檔案路徑
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // 添加檔案
        builder.addTextBody("description", "This is a test file"); // 添加文字欄位（可選）

        // 將 entity 設定到 POST 請求
        httpPost.setEntity(builder.build());

        // 執行請求
        HttpResponse response = httpClient.execute(httpPost);

        // 輸出回應狀態
        System.out.println("Response Code: " + response.getStatusLine().getStatusCode());

        // 清理資源
        httpClient.close();
    }
}
```

#### 4. **關鍵類別與用法**
- **`MultipartEntityBuilder`**：用於建置 multipart entity。你可以添加檔案（`addPart`）、文字（`addTextBody`）或二進位資料（`addBinaryBody`）。
- **`FileBody`**：代表要上傳的檔案。
- **`CloseableHttpClient`**：來自 `httpclient.jar` 的 HTTP client，用於執行請求。

#### 5. **執行程式**
- 如果使用 IDE，直接執行程式即可。
- 如果使用命令列，請按照上述方式編譯並執行，並設定 classpath。

#### 6. **疑難排解**
- **ClassNotFoundException**：確保所有必需的 JARs（`httpmime`、`httpclient`、`httpcore`）都在你的 classpath 中。
- **版本不匹配**：使用相容的 JAR 版本（例如 `httpmime-4.5.14` 搭配 `httpclient-4.5.14` 和 `httpcore-4.4.16`）。
- **Android 專案**：Android 有自己的 `org.apache.http` 套件，可能會衝突。請排除內建版本或使用重新封裝的 JAR（例如透過 JarJar）。

---

### 使用範例
如果你要上傳檔案到伺服器（例如 REST API），`httpmime` 可以簡化建立 `multipart/form-data` 請求的過程，這是檔案上傳的標準格式。

如果你需要進一步澄清或在特定場景中需要幫助，請告訴我！