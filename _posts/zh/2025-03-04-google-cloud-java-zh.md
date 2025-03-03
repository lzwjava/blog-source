---
audio: false
generated: true
lang: zh
layout: post
title: Google 云 Java 客户端
translated: true
---

### 关键点
- 使用 `com.google.cloud` 在 Java 中，似乎需要设置 Java 开发环境，包含 Google Cloud 客户端库依赖项，配置身份验证，并使用库与 Google Cloud 服务进行交互。
- 研究表明，身份验证可以在 Google Cloud 平台上自动处理，或者在本地开发中使用服务账户凭据手动设置。
- 证据倾向于使用 Maven 或 Gradle 来管理依赖项，并提供了 Cloud Storage 作为常见用例的示例。

### 设置开发环境
要开始，请确保安装了 Java 开发工具包 (JDK) 版本 8 或更高版本，以及构建工具如 Maven 或 Gradle。这些工具有助于管理项目依赖项和构建过程。

### 包含依赖项
将 Google Cloud 客户端库依赖项添加到项目中。对于 Maven，在 `pom.xml` 文件中包含物料清单 (BOM) 和特定服务库。例如，使用 Cloud Storage：

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

将 "latest_version" 替换为 [Google Cloud Java 客户端库 GitHub 仓库](https://github.com/googleapis/google-cloud-java) 中的实际版本。

### 配置身份验证
如果应用程序在 Google Cloud 平台（如 Compute Engine 或 App Engine）上运行，身份验证通常会自动处理。对于本地开发，将 `GOOGLE_APPLICATION_CREDENTIALS` 环境变量设置为指向服务账户的 JSON 密钥文件，或者以编程方式配置。

### 使用库
设置完成后，导入必要的类，创建服务对象，并进行 API 调用。例如，列出 Cloud Storage 中的存储桶：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

一个意外的细节是，这些库支持各种 Google Cloud 服务，每个服务都有自己的子包，例如 `com.google.cloud.bigquery` 用于 BigQuery，提供了超出存储的广泛功能。

---

### 调查说明：使用 `com.google.cloud` 在 Java 中的全面指南

此说明提供了使用 Google Cloud Java 客户端库的详细探讨，特别是 `com.google.cloud` 包，以与 Google Cloud 服务进行交互。它通过包括所有相关详细信息，组织清晰和深入，适合寻求全面理解的开发人员。

#### 介绍 Google Cloud Java 客户端库
Google Cloud Java 客户端库，可在 `com.google.cloud` 包中访问，为与 Google Cloud 服务（如 Cloud Storage、BigQuery 和 Compute Engine）进行交互提供了习惯用法和直观的接口。这些库旨在减少样板代码，处理低级通信细节，并与 Java 开发实践无缝集成。它们特别适用于构建云原生应用程序，利用 Spring、Maven 和 Kubernetes 等工具，如官方文档中所强调的。

#### 设置开发环境
开始时，需要 Java 开发工具包 (JDK) 版本 8 或更高版本，以确保与库的兼容性。推荐的发行版是 Eclipse Temurin，这是一个开源的 Java SE TCK 认证选项，如设置指南中所述。此外，还需要构建自动化工具（如 Maven 或 Gradle）来管理依赖项。Google Cloud CLI (`gcloud`) 也可以安装，以从命令行与资源进行交互，从而简化部署和监控任务。

#### 管理依赖项
依赖项管理通过 Google Cloud 提供的物料清单 (BOM) 简化，它有助于管理多个库之间的版本。对于 Maven，将以下内容添加到 `pom.xml`：

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

对于 Gradle，应用类似的配置，确保版本一致。版本号应与 [Google Cloud Java 客户端库 GitHub 仓库](https://github.com/googleapis/google-cloud-java) 中的最新更新进行检查。该仓库还详细说明了支持的平台，包括 x86_64、Mac OS X、Windows 和 Linux，但指出了 Android 和 Raspberry Pi 的限制。

#### 身份验证机制
身份验证是一个关键步骤，环境各异。在 Google Cloud 平台（如 Compute Engine、Kubernetes Engine 或 App Engine）上，凭据会自动推断，简化了过程。对于其他环境（如本地开发），可用以下方法：

- **服务账户（推荐）：** 从 Google Cloud 控制台生成 JSON 密钥文件，并将 `GOOGLE_APPLICATION_CREDENTIALS` 环境变量设置为其路径。或者，以编程方式加载它：
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **本地开发/测试：** 使用 Google Cloud SDK 与 `gcloud auth application-default login` 进行临时凭据。
- **现有 OAuth2 令牌：** 使用 `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` 进行特定用例。

项目 ID 的优先顺序包括服务选项、环境变量 `GOOGLE_CLOUD_PROJECT`、App Engine/Compute Engine、JSON 凭据文件和 Google Cloud SDK，`ServiceOptions.getDefaultProjectId()` 有助于推断项目 ID。

#### 使用客户端库
设置好依赖项和身份验证后，开发人员可以使用库与 Google Cloud 服务进行交互。每个服务都有自己的子包，例如 `com.google.cloud.storage` 用于 Cloud Storage 或 `com.google.cloud.bigquery` 用于 BigQuery。以下是 Cloud Storage 的详细示例：

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

此示例列出了所有存储桶，但库支持上传对象、下载文件和管理存储桶策略等操作。对于其他服务，适用类似的模式，详细方法可在相应的 javadocs 中找到，例如 [Google Cloud Java 参考文档](https://googleapis.dev/java/google-cloud-clients/latest/) 中的 BigQuery。

#### 高级功能和考虑事项
这些库支持高级功能，如使用 `OperationFuture` 的长时间运行操作 (LROs)，具有可配置的超时和重试策略。例如，AI Platform (v3.24.0) 默认包括初始重试延迟 5000ms、乘数 1.5、最大重试延迟 45000ms 和总超时 300000ms。还支持代理配置，使用 `https.proxyHost` 和 `https.proxyPort` 进行 HTTPS/gRPC，并通过 `ProxyDetector` 进行 gRPC 的自定义选项。

API 密钥身份验证适用于某些 API，手动通过头文件进行 gRPC 或 REST 设置，如 Language 服务的示例所示。测试通过提供的工具进行，详细信息在仓库的 TESTING.md 中，IDE 插件（如 IntelliJ 和 Eclipse）增强了开发，与库集成。

#### 支持的平台和限制
这些库与各种平台兼容，HTTP 客户端无处不在，gRPC 客户端支持 x86_64、Mac OS X、Windows 和 Linux。但它们不支持 Android、Raspberry Pi 或 App Engine Standard Java 7，除了 Datastore、Storage 和 BigQuery。支持的环境包括 Windows x86_64、Mac OS X x86_64、Linux x86_64、GCE、GKE、GAE Std J8、GAE Flex 和 Alpine Linux（Java 11+）。

#### 资源和进一步阅读
有关更多指导，[Google Cloud Java 客户端库 GitHub 仓库](https://github.com/googleapis/google-cloud-java) 提供代码示例、贡献指南和故障排除资源。如 [Baeldung](https://www.baeldung.com/java-google-cloud-storage) 上的教程，提供了使用 Cloud Storage 的实践示例，而官方文档 [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) 则涵盖了更广泛的应用程序开发概念。

#### 表：关键配置详细信息

| **方面**               | **详细信息**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java 版本             | 需要 Java 8 或更高版本。                                                                       |
| 依赖项管理            | 使用 BOM 进行版本一致性，例如 Maven `libraries-bom`。                                  |
| 身份验证方法           | 在 GCE/GKE/GAE 上自动处理，通过 `GOOGLE_APPLICATION_CREDENTIALS` 或编程方式手动处理。          |
| 支持的平台            | HTTP 客户端无处不在，gRPC 客户端在 x86_64、Mac OS X、Windows 和 Linux 上；不在 Android 和 Raspberry Pi 上。|
| 示例服务              | Cloud Storage：`com.google.cloud.storage`，用于存储桶列表和对象管理的方法。       |

此全面指南确保开发人员拥有所有必要的信息，以有效地在 Java 中使用 `com.google.cloud`，涵盖了设置、身份验证、使用和高级功能，并引用了权威来源以供进一步探索。

#### 关键引用
- [Google Cloud Java 客户端库 GitHub 仓库详细代码和设置](https://github.com/googleapis/google-cloud-java)
- [Google Cloud 文档 Java 开发概述](https://cloud.google.com/products/anthos)
- [Baeldung 教程 Google Cloud Storage 与 Java 实践示例](https://www.baeldung.com/java-google-cloud-storage)