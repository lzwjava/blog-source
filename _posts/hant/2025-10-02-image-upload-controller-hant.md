---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Java OSS 圖片上傳控制器
translated: true
type: note
---

### 程式碼運作原理

這是一個 Java Spring Boot 控制器 (`FileController`)，設計用於透過 HTTP POST 請求處理檔案上傳。它整合了**阿里雲物件儲存服務 (OSS)**，將上傳的檔案儲存在雲端。此程式碼專注於圖片上傳（限制為 JPEG/PNG 格式），並提供一個簡單、無需身份驗證的端點。它在處理過程中使用了本機暫存檔案，並在上傳後將其刪除。

#### 關鍵組件與流程：
1. **類別結構**：
   - 這是一個 `@RestController`，映射到基礎路徑 `"file"`，並繼承了 `BaseController`（可能用於共享邏輯）。
   - 主要方法是 `upload()`，映射到 `"/file/upload"`。
   - 註解：
     - `@RequestMapping`：定義端點和允許的 HTTP 方法（POST）。
     - `@ResponseBody`：確保回應為 JSON 格式（透過 `LQResponse`）。
     - `@NoAuth`：表示此端點無需身份驗證（自訂 AOP 註解）。

2. **依賴項**：
   - Spring Framework（例如 `@RestController`、`@RequestMapping`、`@RequestParam`、用於檔案處理的 `MultipartFile`）。
   - 阿里雲 OSS SDK（例如用於與 OSS 互動的 `OSSClient`）。
   - Apache Commons Lang（例如用於生成隨機金鑰的 `RandomStringUtils`、用於字串操作的 `StringUtils`）。
   - 自訂類別如 `LQException`、`LQError` 和 `LQResponse`（可能是應用程式錯誤處理和回應工具的一部分）。

3. **`upload()` 方法逐步解析**：
   - **輸入驗證**：
     - 接收 `MultipartFile`（上傳的檔案）。
     - 使用 `URLConnection.guessContentTypeFromStream()` 判斷內容類型（MIME 類型）。這會根據檔案的位元組檢查其是否為真正的圖片檔案。
     - 僅允許特定類型：`"image/jpeg"`、`"image/jpg"` 或 `"image/png"`。若非這些類型，則拋出帶有錯誤代碼 `UNSUPPORTED_IMAGE_FILE` 的 `LQException`。
     - 從內容類型中提取副檔名（例如 `.jpg`）。

   - **檔案準備**：
     - 使用原始檔案名稱建立本機暫存 `File` 物件。
     - 使用 `FileOutputStream` 將檔案的位元組寫入本機磁碟。此步驟是必要的，因為 OSS SDK 的 `putObject` 需要 `File` 或 `InputStream`。

   - **OSS 上傳**：
     - 初始化 `OSSClient`，參數包括：
       - **端點**：`https://oss-cn-qingdao.aliyuncs.com`（中國青島區域）。
       - **存取金鑰 ID**：`"LTAIuXm7..`（硬編碼 — 注意：在生產環境中，應從環境變數或設定檔安全載入，以避免暴露憑證）。
       - **秘密存取金鑰**：`"GP8FRF..."`（同樣為硬編碼 — 安全注意事項相同）。
       - **儲存貯體**：空字串 (`""`) — 這可能是一個佔位符，必須設定為有效的 OSS 儲存貯體名稱（例如 `"my-bucket"`）。
     - 生成唯一的物件金鑰：一個隨機的 6 字元英數字串 + 檔案副檔名（例如 `a3bS9k.jpg`）。
     - 呼叫 `ossClient.putObject()`，並傳入指向儲存貯體、金鑰和本機檔案的 `PutObjectRequest`。這會將檔案上傳至 OSS。
     - 捕獲 `OSSException`（OSS 端錯誤）或 `ClientException`（客戶端/網路錯誤），並拋出自訂的 `LQException`，錯誤代碼為 `FILE_UPLOAD_FAIL`。

   - **清理與回應**：
     - 使用 `newFile.delete()` 刪除本機暫存檔案，避免磁碟雜亂。
     - 返回 `LQResponse.success()`，包含上傳檔案的公開 URL：`FILE_HOST + "/" + key`。
       - `FILE_HOST` 是另一個空字串佔位符 — 將其設定為 OSS 儲存貯體的網域（例如 `"https://my-bucket.oss-cn-qingdao.aliyuncs.com"`）。

   - **錯誤處理**：使用自訂例外 (`LQException`) 處理驗證和上傳失敗，確保應用程式範圍內錯誤回應的一致性。

#### 安全注意事項：
- 硬編碼憑證是一個主要問題 — 應使用環境變數、AWS SSM 或阿里雲 KMS。
- 端點和儲存貯體不完整 — 在實際使用時需填寫。
- 無身份驗證 (`@NoAuth`) 意味著任何人都可以上傳；如有需要，應添加身份驗證（例如透過 JWT）。
- 內容類型檢查較為基礎；考慮使用更穩健的驗證方法（例如 Apache Tika）以防止欺騙。

### 如何使用阿里雲 OSS SDK 導入

列出的導入是針對阿里雲 OSS Java SDK（通常透過 Maven/Gradle 添加為 `com.aliyun.oss:aliyun-sdk-oss`）。它們提供了與 OSS 互動的類別。以下是每個導入在上下文中的使用方式及範例。

1. **`import com.aliyun.oss.OSSClient;`**：
   - 用於 OSS 操作的主要客戶端類別（現已棄用，建議使用 `OSSClientBuilder`，但在舊程式碼中仍可使用）。
   - **用法**：建立實例以連接至 OSS。
     ```java
     OSSClient ossClient = new OSSClient(ENDPOINT, ACCESS_KEY_ID, SECRET_ACCESS_KEY);
     // 然後使用 putObject()、getObject()、deleteObject() 等方法。
     ```
   - **在此處用途**：用於驗證並將檔案上傳至指定的儲存貯體。

2. **`import com.aliyun.oss.ClientException;`**：
   - 因客戶端問題而拋出（例如網路故障、無效憑證）。
   - **用法**：捕獲它以處理錯誤。
     ```java
     try {
         // OSS 操作
     } catch (ClientException e) {
         // 處理客戶端錯誤（例如重試或記錄）
     }
     ```
   - **在此處用途**：在上傳方法中捕獲，以實現彈性的錯誤處理。

3. **`import com.aliyun.oss.OSSException;`**：
   - 因 OSS 服務端錯誤而拋出（例如儲存貯體不存在、權限不足）。
   - **用法**：與 `ClientException` 類似，但專注於服務特定錯誤。
     ```java
     try {
         // OSS 操作
     } catch (OSSException e) {
         // 記錄 e.getErrorCode() 和 e.getErrorMessage()
     }
     ```
   - **在此處用途**：捕獲以透過 `LQException` 提供使用者友好的失敗訊息。

4. **`import com.aliyun.oss.model.PutObjectRequest;`**：
   - 用於構建上傳請求的模型類別（包括儲存貯體、金鑰、檔案/輸入流、元資料）。
   - **用法**：
     ```java
     PutObjectRequest request = new PutObjectRequest(BUCKET, KEY, FILE);
     // 可選：添加元資料，例如 request.setObjectMetadata(metadata);
     ossClient.putObject(request);
     ```
   - **在此處用途**：用於指定上傳詳細資訊（儲存貯體、金鑰、本機檔案）。

5. **`import com.aliyun.oss.model.PutObjectResult;`**：
   - 由 `putObject()` 返回；包含上傳元資料（例如用於完整性檢查的 ETag）。
   - **用法**：
     ```java
     PutObjectResult result = ossClient.putObject(request);
     String etag = result.getETag();  // 用於驗證
     ```
   - **在此處用途**：已賦值但未在程式碼中深入使用（可用於除錯記錄）。

#### 設定與整合提示：
- **替換佔位符**：更新 `BUCKET` 和 `FILE_HOST` 為實際值。確保您的阿里雲帳戶允許 OSS 存取。
- **Maven 依賴項**（添加到 `pom.xml`）：
  ```xml
  <dependency>
      <groupId>com.aliyun.oss</groupId>
      <artifactId>aliyun-sdk-oss</artifactId>
      <version>3.17.4</version>  <!-- 使用最新穩定版本 -->
  </dependency>
  ```
- **測試**：使用 Postman 等工具發送 POST 請求至 `/file/upload`，並附帶檔案參數。回應應為包含檔案 URL 的 JSON 物件。
- **完整 OSS 文件**：參考[阿里雲 OSS Java SDK 文件](https://help.aliyun.com/document_detail/31856.html)以了解進階功能，如元資料、ACL 或多部分上傳。

如果您提供更多詳細資訊（例如特定錯誤或自訂設定），我可以進一步完善此說明！