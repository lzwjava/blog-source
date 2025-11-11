---
audio: false
generated: true
lang: hant
layout: post
title: Google Cloud Java 用戶端
translated: true
type: note
---

### 重點摘要
- 要在 Java 中使用 `com.google.cloud`，您需要設定 Java 開發環境、包含 Google Cloud 客戶端函式庫依賴項、配置身份驗證，並使用這些函式庫與 Google Cloud 服務互動。
- 研究表明，身份驗證可以在 Google Cloud 平台上自動處理，或者使用服務帳戶憑證為本地開發手動設定。
- 證據傾向於使用 Maven 或 Gradle 來管理依賴項，並提供了 Cloud Storage 作為常見用例的示例。

### 設定開發環境
首先，確保您已安裝 Java 開發工具包 (JDK) 8 或更高版本，以及像 Maven 或 Gradle 這樣的建置工具。這些工具有助於管理專案依賴項和建置流程。

### 包含依賴項
將 Google Cloud 客戶端函式庫依賴項添加到您的專案中。對於 Maven，請在您的 `pom.xml` 檔案中包含材料清單 (BOM) 和特定服務函式庫。例如，要使用 Cloud Storage：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

將 "latest_version" 替換為 [Google Cloud Java 客戶端函式庫 GitHub 儲存庫](https://github.com/googleapis/google-cloud-java) 中的實際版本號。

### 配置身份驗證
如果您的應用程式在 Compute Engine 或 App Engine 等 Google Cloud 平台上運行，身份驗證通常會自動處理。對於本地開發，請設定 `GOOGLE_APPLICATION_CREDENTIALS` 環境變數，使其指向服務帳戶的 JSON 金鑰檔案，或以程式設計方式進行配置。

### 使用函式庫
設定完成後，導入必要的類別，建立服務物件，並進行 API 呼叫。例如，要列出 Cloud Storage 中的儲存貯體：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

一個意想不到的細節是，這些函式庫支援各種 Google Cloud 服務，每個服務在 `com.google.cloud` 下都有其自己的子套件，例如用於 BigQuery 的 `com.google.cloud.bigquery`，提供了超越儲存的廣泛功能。

---

### 調查筆記：在 Java 中使用 `com.google.cloud` 的綜合指南

本筆記詳細探討了如何使用 Google Cloud Java 客戶端函式庫，特別聚焦於 `com.google.cloud` 套件，以與 Google Cloud 服務互動。它透過包含研究中的所有相關細節，擴展了直接答案，並為尋求透徹理解的開發人員組織了清晰且深入的內容。

#### Google Cloud Java 客戶端函式庫簡介
Google Cloud Java 客戶端函式庫，可透過 `com.google.cloud` 套件存取，為與 Cloud Storage、BigQuery 和 Compute Engine 等 Google Cloud 服務互動提供了慣用且直觀的介面。這些函式庫旨在減少樣板程式碼、處理低層級通訊細節，並與 Java 開發實踐無縫整合。如官方文件所強調，它們對於建置雲端原生應用程式特別有用，可利用 Spring、Maven 和 Kubernetes 等工具。

#### 設定開發環境
首先，需要 Java 開發工具包 (JDK) 8 或更高版本，以確保與函式庫的相容性。如設定指南所述，推薦的分發版是 Eclipse Temurin，這是一個開源、通過 Java SE TCK 認證的選項。此外，像 Maven 或 Gradle 這樣的建置自動化工具對於管理依賴項至關重要。也可以安裝 Google Cloud CLI (`gcloud`) 以從命令列與資源互動，方便部署和監控任務。

#### 管理依賴項
依賴項管理透過使用 Google Cloud 提供的材料清單 (BOM) 得以簡化，它有助於管理多個函式庫的版本。對於 Maven，請將以下內容添加到您的 `pom.xml`：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

對於 Gradle，適用類似的配置，以確保版本一致性。版本號應根據 [Google Cloud Java 客戶端函式庫 GitHub 儲存庫](https://github.com/googleapis/google-cloud-java) 檢查最新更新。此儲存庫還詳細說明了支援的平台，包括 x86_64、Mac OS X、Windows 和 Linux，但註明了在 Android 和 Raspberry Pi 上的限制。

#### 身份驗證機制
身份驗證是關鍵步驟，其選項因環境而異。在 Compute Engine、Kubernetes Engine 或 App Engine 等 Google Cloud 平台上，憑證會自動推斷，從而簡化了流程。對於其他環境，例如本地開發，可使用以下方法：

- **服務帳戶（推薦）：** 從 Google Cloud 控制台產生 JSON 金鑰檔案，並將 `GOOGLE_APPLICATION_CREDENTIALS` 環境變數設定為其路徑。或者，以程式設計方式載入它：
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **本地開發/測試：** 使用 Google Cloud SDK 與 `gcloud auth application-default login` 來取得臨時憑證。
- **現有 OAuth2 令牌：** 對於特定用例，使用 `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))`。

專案 ID 規範的優先順序包括服務選項、環境變數 `GOOGLE_CLOUD_PROJECT`、App Engine/Compute Engine、JSON 憑證檔案和 Google Cloud SDK，而 `ServiceOptions.getDefaultProjectId()` 有助於推斷專案 ID。

#### 使用客戶端函式庫
一旦設定了依賴項和身份驗證，開發人員就可以使用這些函式庫與 Google Cloud 服務互動。每個服務在 `com.google.cloud` 下都有其自己的子套件，例如用於 Cloud Storage 的 `com.google.cloud.storage` 或用於 BigQuery 的 `com.google.cloud.bigquery`。以下是 Cloud Storage 的詳細範例：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

此範例列出了所有儲存貯體，但該函式庫支援上傳物件、下載檔案和管理儲存貯體政策等操作。對於其他服務，適用類似的模式，詳細方法可在各自的 javadoc 中找到，例如 [Google Cloud Java 參考文件](https://googleapis.dev/java/google-cloud-clients/latest/) 中 BigQuery 的文件。

#### 進階功能與注意事項
這些函式庫支援進階功能，例如使用 `OperationFuture` 的長時間運行操作 (LROs)，並具有可設定的逾時和重試政策。例如，AI Platform (v3.24.0) 的預設值包括初始重試延遲 5000ms、乘數 1.5、最大重試延遲 45000ms 和總逾時 300000ms。也支援代理配置，對 HTTPS/gRPC 使用 `https.proxyHost` 和 `https.proxyPort`，並透過 `ProxyDetector` 為 gRPC 提供自訂選項。

某些 API 可使用 API 金鑰身份驗證，如 Language 服務的範例所示，透過標頭為 gRPC 或 REST 手動設定。測試透過提供的工具得以促進，詳細資訊在儲存庫的 TESTING.md 中，而 IntelliJ 和 Eclipse 的 IDE 插件透過函式庫整合增強了開發體驗。

#### 支援的平台與限制
這些函式庫與各種平台相容，HTTP 客戶端到處都可以工作，而 gRPC 客戶端在 x86_64、Mac OS X、Windows 和 Linux 上受支援。但是，它們在 Android、Raspberry Pi 或 App Engine Standard Java 7 上不受支援，除了 Datastore、Storage 和 BigQuery。支援的環境包括 Windows x86_64、Mac OS X x86_64、Linux x86_64、GCE、GKE、GAE Std J8、GAE Flex 和 Alpine Linux (Java 11+)。

#### 資源與進一步閱讀
如需其他指導，[Google Cloud Java 客戶端函式庫 GitHub 儲存庫](https://github.com/googleapis/google-cloud-java) 提供了程式碼範例、貢獻指南和疑難排解資源。像 [Baeldung](https://www.baeldung.com/java-google-cloud-storage) 上的教程提供了實用範例，例如使用 Cloud Storage，而 [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) 的官方文件涵蓋了更廣泛的應用程式開發概念。

#### 表格：關鍵配置細節

| **方面**               | **細節**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java 版本             | 需要 Java 8 或以上。                                                                       |
| 依賴項管理    | 使用 BOM 以確保版本一致性，例如 Maven 的 `libraries-bom`。                                  |
| 身份驗證方法   | 在 GCE/GKE/GAE 上自動處理，或透過 `GOOGLE_APPLICATION_CREDENTIALS` 或程式設計方式手動處理。          |
| 支援的平台      | HTTP 客戶端到處可用，gRPC 在 x86_64、Mac OS X、Windows、Linux 上支援；不在 Android、Raspberry Pi 上支援。|
| 範例服務          | Cloud Storage：`com.google.cloud.storage`，包含用於儲存貯體列表、物件管理的方法。       |

本綜合指南確保開發人員擁有所有必要資訊，以有效地在 Java 中使用 `com.google.cloud`，解決了設定、身份驗證、使用和進階功能等問題，並參考了權威來源以供進一步探索。

#### 主要引用文獻
- [Google Cloud Java 客戶端函式庫 GitHub 儲存庫詳細程式碼與設定](https://github.com/googleapis/google-cloud-java)
- [Google Cloud 文件 Java 開發概述](https://cloud.google.com/products/anthos)
- [Baeldung 教程：使用 Java 的 Google Cloud Storage 實用範例](https://www.baeldung.com/java-google-cloud-storage)