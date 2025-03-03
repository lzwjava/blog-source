---
audio: false
generated: true
lang: hant
layout: post
title: Google 雲端 Java 用戶端
translated: true
---

### 關鍵要點
- 使用 `com.google.cloud` 在 Java 中，似乎需要設置 Java 開發環境，包含 Google Cloud 客戶端庫依賴項，配置身份驗證，並使用這些庫與 Google Cloud 服務進行交互。
- 研究表明，身份驗證可以在 Google Cloud 平台上自動處理，或者在本地開發中使用服務帳戶憑證手動設置。
- 依賴項管理建議使用 Maven 或 Gradle，並提供了 Cloud Storage 作為常見用例的示例。

### 設置開發環境
開始之前，請確保已安裝 Java Development Kit (JDK) 版本 8 或更高版本，並配備 Maven 或 Gradle 等構建工具。這些工具有助於管理項目依賴項和構建過程。

### 包含依賴項
將 Google Cloud 客戶端庫依賴項添加到您的項目中。對於 Maven，在 `pom.xml` 文件中包含 Bill of Materials (BOM) 和特定服務庫。例如，使用 Cloud Storage：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

將 "latest_version" 替換為 [Google Cloud Java 客戶端庫 GitHub 存儲庫](https://github.com/googleapis/google-cloud-java) 中的實際版本。

### 配置身份驗證
如果應用程序在 Google Cloud 平台（如 Compute Engine 或 App Engine）上運行，身份驗證通常會自動處理。對於本地開發，請將 `GOOGLE_APPLICATION_CREDENTIALS` 環境變量設置為指向服務帳戶的 JSON 密鑰文件，或者以編程方式配置。

### 使用庫
設置完成後，導入必要的類，創建服務對象並進行 API 請求。例如，列出 Cloud Storage 中的桶：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

意外的細節是，這些庫支持各種 Google Cloud 服務，每個服務都有自己的子包，例如 `com.google.cloud.bigquery` 用於 BigQuery，提供的功能遠不僅僅是存儲。

---

### 調查備忘錄：使用 `com.google.cloud` 在 Java 中的全面指南

這份備忘錄提供了使用 Google Cloud Java 客戶端庫的詳細探討，特別關注 `com.google.cloud` 包，以與 Google Cloud 服務進行交互。它通過包括所有相關研究細節，組織清晰和深入，適合尋求全面理解的開發人員。

#### Google Cloud Java 客戶端庫簡介
Google Cloud Java 客戶端庫，可通過 `com.google.cloud` 包訪問，提供了與 Google Cloud 服務（如 Cloud Storage、BigQuery 和 Compute Engine）交互的直觀和直觀接口。這些庫旨在減少樣板代碼，處理低級通信細節，並與 Java 開發實踐無縫集成。它們特別適合構建雲原生應用程序，利用 Spring、Maven 和 Kubernetes 等工具，如官方文檔中所強調的。

#### 設置開發環境
開始時，需要 Java Development Kit (JDK) 版本 8 或更高版本，以確保與庫的兼容性。推薦的發行版是 Eclipse Temurin，這是一個開源的 Java SE TCK 認證選項，如設置指南中所指出的。此外，還需要一個構建自動化工具，如 Maven 或 Gradle，以管理依賴項。還可以安裝 Google Cloud CLI (`gcloud`) 以從命令行與資源進行交互，從而促進部署和監控任務。

#### 管理依賴項
依賴項管理通過 Google Cloud 提供的 Bill of Materials (BOM) 簡化，這有助於跨多個庫管理版本。對於 Maven，將以下內容添加到您的 `pom.xml`：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

對於 Gradle，適用類似的配置，確保版本一致。版本號應與 [Google Cloud Java 客戶端庫 GitHub 存儲庫](https://github.com/googleapis/google-cloud-java) 中的最新更新進行檢查。該存儲庫還詳細說明了支持的平台，包括 x86_64、Mac OS X、Windows 和 Linux，但指出了 Android 和 Raspberry Pi 的限制。

#### 身份驗證機制
身份驗證是一個關鍵步驟，選項因環境而異。在 Google Cloud 平台（如 Compute Engine、Kubernetes Engine 或 App Engine）上，憑證會自動推斷，簡化了過程。對於其他環境（如本地開發），可用以下方法：

- **服務帳戶（推薦）**：從 Google Cloud 控制台生成 JSON 密鑰文件，並將 `GOOGLE_APPLICATION_CREDENTIALS` 環境變量設置為其路徑。或者，以編程方式加載它：
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **本地開發/測試**：使用 Google Cloud SDK 並使用 `gcloud auth application-default login` 獲取臨時憑證。
- **現有 OAuth2 令牌**：使用 `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` 進行特定用例。

項目 ID 規範的優先順序包括服務選項、環境變量 `GOOGLE_CLOUD_PROJECT`、App Engine/Compute Engine、JSON 憑證文件和 Google Cloud SDK，`ServiceOptions.getDefaultProjectId()` 幫助推斷項目 ID。

#### 使用客戶端庫
設置依賴項和身份驗證後，開發人員可以使用這些庫與 Google Cloud 服務進行交互。每個服務都有自己的子包，例如 `com.google.cloud.storage` 用於 Cloud Storage 或 `com.google.cloud.bigquery` 用於 BigQuery。以下是 Cloud Storage 的詳細示例：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

此示例列出了所有桶，但庫支持上傳對象、下載文件和管理桶策略等操作。對於其他服務，適用類似的模式，詳細方法可在相應的 javadocs 中找到，例如 [Google Cloud Java 參考文檔](https://googleapis.dev/java/google-cloud-clients/latest/) 中的 BigQuery。

#### 高級功能和考慮因素
這些庫支持高級功能，如使用 `OperationFuture` 的長時間運行操作（LRO），具有可配置的超時和重試策略。例如，AI Platform (v3.24.0) 默認值包括初始重試延遲 5000ms、乘數 1.5、最大重試延遲 45000ms 和總超時 300000ms。還支持代理配置，使用 `https.proxyHost` 和 `https.proxyPort` 進行 HTTPS/gRPC，並使用 `ProxyDetector` 進行 gRPC 的自定義選項。

某些 API 支持 API 密鑰身份驗證，可以通過 gRPC 或 REST 手動設置標頭，如 Language 服務中的示例。測試通過提供的工具進行，詳細信息在存儲庫的 TESTING.md 中，並且 IntelliJ 和 Eclipse 的 IDE 插件增強了開發，與庫集成。

#### 支持的平台和限制
這些庫與各種平台兼容，HTTP 客戶端無處不在，gRPC 客戶端支持 x86_64、Mac OS X、Windows 和 Linux。然而，它們不支持 Android、Raspberry Pi 或 App Engine Standard Java 7，除 Datastore、Storage 和 BigQuery 之外。支持的環境包括 Windows x86_64、Mac OS X x86_64、Linux x86_64、GCE、GKE、GAE Std J8、GAE Flex 和 Alpine Linux（Java 11+）。

#### 資源和進一步閱讀
有關進一步指導，[Google Cloud Java 客戶端庫 GitHub 存儲庫](https://github.com/googleapis/google-cloud-java) 提供了代碼示例、貢獻指南和故障排除資源。如 [Baeldung](https://www.baeldung.com/java-google-cloud-storage) 上的教程，提供了實際示例，例如使用 Cloud Storage，而 [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) 的官方文檔涵蓋了更廣泛的應用程序開發概念。

#### 表：關鍵配置詳細信息

| **方面**               | **詳細信息**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java 版本             | 需要 Java 8 或更高版本。                                                                       |
| 依賴項管理            | 使用 BOM 以保持版本一致，例如 Maven `libraries-bom`。                                  |
| 身份驗證方法           | 在 GCE/GKE/GAE 上自動，手動通過 `GOOGLE_APPLICATION_CREDENTIALS` 或以編程方式。          |
| 支持的平台              | HTTP 客戶端無處不在，gRPC 在 x86_64、Mac OS X、Windows 和 Linux 上；不在 Android 和 Raspberry Pi 上。|
| 示例服務                | Cloud Storage：`com.google.cloud.storage`，用於桶列表和對象管理的方法。       |

這份全面指南確保開發人員擁有所有必要的信息，以有效地在 Java 中使用 `com.google.cloud`，涵蓋設置、身份驗證、使用和高級功能，並參考權威來源進行進一步探索。

#### 關鍵引用
- [Google Cloud Java 客戶端庫 GitHub 存儲庫詳細代碼和設置](https://github.com/googleapis/google-cloud-java)
- [Google Cloud 文檔 Java 開發概述](https://cloud.google.com/products/anthos)
- [Baeldung 教程 Google Cloud Storage 使用 Java 實際示例](https://www.baeldung.com/java-google-cloud-storage)