---
audio: false
lang: hant
layout: post
title: 使用 Eclipse
translated: true
---

### 關鍵要點
- 似乎 Eclipse 可以有效地與 IBM Websphere Liberty、Spring、Spring Boot 和 Maven 一起使用，但設置需要特定的配置。
- 研究建議在 Eclipse 中安裝 Spring Tool Suite (STS) 和 IBM Liberty Developer Tools 作為插件，以增強功能。
- 證據表明應該使用 STS 或 Spring Initializr 創建 Spring Boot 專案，然後將其配置為 Websphere Liberty 部署。

### 設置 Eclipse
首先，從 [Eclipse 下載](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 下載並安裝 "Eclipse IDE for Enterprise Java and Web Developers"。確保已安裝 JDK 17 或更高版本，可以通過在終端中運行 `java -version` 來驗證。

### 配置 Spring 和 Spring Boot
通過在 Eclipse 中選擇 Help -> Eclipse Marketplace，搜索 "Spring Tools" 並安裝適當版本來安裝 Spring Tool Suite (STS) 插件。這將增強 Spring 和 Spring Boot 開發。可以通過 File -> New -> Spring Starter Project 在 Eclipse 中直接創建新的 Spring Boot 專案，選擇 Maven 作為構建工具並添加必要的依賴項，例如 Spring Web。

### 與 IBM Websphere Liberty 集成
通過在 Eclipse Marketplace 搜索 "IBM Liberty Developer Tools" 並按照安裝提示進行安裝來安裝 IBM Liberty Developer Tools。通過 Window -> Preferences -> Servers -> Runtime Environments，添加新的 Websphere Liberty 運行時，並通過 File -> New -> Other -> Server 創建伺服器實例。確保伺服器的 server.xml 包含 `<feature>springBoot-2.0</feature>` 以支持 Spring Boot，如 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中所述。

### 部署您的應用程序
修改 Spring Boot 應用程序以擴展 `SpringBootServletInitializer` 而不是使用啟動嵌入式伺服器的主方法，通過在 pom.xml 中設置 `<packaging>war</packaging>` 將其打包為 WAR 文件。通過右鍵點擊專案，選擇 "Run As -> Run on Server"，然後選擇您的 Liberty 伺服器進行部署。這將確保應用程序在 Liberty 的 Web 容器上運行。

---

### 調查筆記：使用 Eclipse 與 IBM Websphere Liberty、Spring、Spring Boot 和 Maven 的全面指南

本指南提供了有關在 Eclipse 中有效使用 IBM Websphere Liberty、Spring、Spring Boot 和 Maven 的詳細步驟，針對在這些生態系統中工作的開發人員。該過程涉及設置 Eclipse、安裝必要的插件、創建和配置專案以及部署應用程序，重點放在集成和最佳實踐上，截至 2025 年 2 月 27 日。

#### Eclipse 設置和先決條件
Eclipse 作為 Java 開發的強大 IDE，特別適用於企業應用程序。對於此設置，下載 "Eclipse IDE for Enterprise Java and Web Developers" 版本 2024-06，可在 [Eclipse 下載](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 獲得。確保您的系統安裝了 JDK 17 或更高版本，可以通過在終端中運行 `java -version` 來檢查。此版本確保與現代 Spring 和 Liberty 功能的兼容性。

#### 安裝必要的插件
要增強 Eclipse 的 Spring 和 Spring Boot 開發，安裝 Spring Tool Suite (STS)，即 Spring 工具的下一代。通過 Help -> Eclipse Marketplace 訪問，搜索 "Spring Tools"，並安裝標有 "Spring Tools (aka Spring IDE and Spring Tool Suite)" 的條目。此插件，詳細信息請參閱 [Spring Tools](https://spring.io/tools/)，為基於 Spring 的應用程序提供了世界一流的支持，與 Eclipse 無縫集成，具有項目創建和調試等功能。

要與 IBM Websphere Liberty 集成，安裝 IBM Liberty Developer Tools，也可以通過 Eclipse Marketplace 搜索 "IBM Liberty Developer Tools" 獲得。此插件，測試了 Eclipse 2024-06，如 [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) 中所述，便於在 Liberty 上構建和部署 Java EE 應用程序，支持自 2019-12 以來的版本。

#### 創建 Spring Boot 專案
在安裝了 STS 的 Eclipse 中有兩種主要方法來創建 Spring Boot 專案：

1. **使用 Spring Initializr**：訪問 [Spring Initializr](https://start.spring.io/)，選擇 Maven 作為構建工具，選擇項目元數據（組、工藝品等），並添加依賴項，例如 Spring Web。將項目生成為 ZIP 文件，解壓縮並通過 File -> Import -> Existing Maven Project 將其導入 Eclipse，選擇解壓縮的文件夾。

2. **直接使用 STS**：打開 Eclipse，選擇 File -> New -> Other，展開 Spring Boot，然後選擇 "Spring Starter Project"。按照向導操作，確保選擇 Maven 作為類型，並選擇依賴項。此方法，如 [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) 中所述，是首選，因為它與 Eclipse 的工作區集成。

這兩種方法都確保了基於 Maven 的專案，這對於 Spring Boot 的依賴管理至關重要。

#### 配置 Websphere Liberty 部署
要部署到 Websphere Liberty，請修改 Spring Boot 應用程序以在 Liberty 的 Web 容器上運行，而不是啟動嵌入式伺服器。這包括：

- 確保主應用程序類擴展 `SpringBootServletInitializer`。例如：

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // 沒有主方法；Liberty 處理啟動
  }
  ```

- 更新 pom.xml 以將其打包為 WAR 文件，添加：

  ```xml
  <packaging>war</packaging>
  ```

  這對於傳統的 Servlet 容器部署是必要的，如 [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) 中所述。

Websphere Liberty，特別是其開源變體 Open Liberty，支持具體功能的 Spring Boot 應用程序。確保 Liberty 伺服器的 server.xml 包含 `<feature>springBoot-2.0</feature>` 以支持 Spring Boot 2.x，如 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中所述。此配置禁用嵌入式 Web 容器，改用 Liberty 的容器。

#### 在 Eclipse 中設置和配置 Websphere Liberty 伺服器
安裝 IBM Liberty Developer Tools 後，設置 Liberty 伺服器：

- 導航到 Window -> Preferences -> Servers -> Runtime Environments，點擊 "Add"，然後選擇 "WebSphere Application Server Liberty"。按照向導操作，找到您的 Liberty 安裝，通常在類似 `<Liberty_Root>/wlp` 的目錄中，如 [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) 中所述。

- 通過 File -> New -> Other -> Server 創建新的伺服器實例，選擇 "WebSphere Application Server Liberty" 和您配置的運行時。命名伺服器並根據需要調整設置。

- 編輯伺服器的 server.xml，通過 Servers 視圖可訪問，以包含必要的功能。對於 Spring Boot，添加：

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- 其他功能，例如 servlet-3.1 以支持 Web -->
  </featureManager>
  ```

此設置，由 [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) 支持，確保與 Spring Boot 應用程序的兼容性。

#### 部署和運行應用程序
要部署，右鍵點擊項目資源管理器中的專案，選擇 "Run As -> Run on Server"，選擇您的 Liberty 伺服器，然後點擊完成。Eclipse 將 WAR 文件部署到 Liberty 伺服器，您可以在控制台視圖中監控日誌。確保在 server.xml 中正確設置應用程序上下文根，通常在 `<webApplication>` 標籤下，以通過適當的 URL 訪問您的應用程序，例如 `http://localhost:9080/yourapp`。

對於調試，使用調試視圖，根據需要設置斷點，利用 Liberty 對遠程調試的支持，如 [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) 中所述。

#### 額外考慮
- **打包選項**：雖然 WAR 是 Servlet 容器的標準，但 Open Liberty 也支持 JAR 部署，如 [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中所述。對於 JAR，請確保應用程序配置為不啟動嵌入式伺服器，這可能需要額外的 Liberty 功能或配置。
- **Maven 集成**：使用 Maven 進行依賴管理，確保包含 `liberty-maven-plugin` 以進行自動部署，如 [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) 中所述。
- **故障排除**：如果出現問題，請檢查 Liberty 伺服器實例下的 `logs` 目錄中的伺服器日誌，並確保 Liberty 版本與 Spring Boot 兼容，因為版本如 Liberty 8.5.5.9 或更高版本支持可運行的 JAR，如 [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application) 中所述。

此全面設置確保了在 IBM Websphere Liberty 上開發和部署 Spring Boot 應用程序的有效使用 Eclipse，利用 Maven 進行構建管理。

#### 表：部署選項比較

| 部署類型 | 優點                                      | 缺點                                      | 配置說明                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR 文件        | Servlet 容器的標準，廣泛支持 | 需要擴展 `SpringBootServletInitializer` | 在 pom.xml 中設置 `<packaging>war</packaging>`  |
| JAR 文件        | 開發更簡單，由 Open Liberty 支持 | 可能需要額外的 Liberty 功能   | 確保沒有嵌入式伺服器啟動，使用 springBoot 功能 |

此表，源自 [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)，有助於根據項目需求選擇適當的部署策略。

### 關鍵引用
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)