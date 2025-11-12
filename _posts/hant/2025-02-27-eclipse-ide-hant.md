---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Eclipse
translated: true
type: note
---

### 重點摘要
- Eclipse 似乎能有效搭配 IBM Websphere Liberty、Spring、Spring Boot 及 Maven 使用，但設定需要特定配置。
- 研究建議在 Eclipse 中安裝 Spring Tool Suite (STS) 和 IBM Liberty Developer Tools 作為外掛程式以增強功能。
- 現有證據傾向於使用 STS 或 Spring Initializr 建立 Spring Boot 專案，然後配置以部署至 Websphere Liberty。

### 設定 Eclipse
首先，從 [Eclipse 下載頁面](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 下載並安裝「Eclipse IDE for Enterprise Java and Web Developers」。請確保已安裝 JDK 17 或更新版本，您可以在終端機中執行 `java -version` 來驗證。

### 配置 Spring 與 Spring Boot
在 Eclipse 中前往 Help -> Eclipse Marketplace，搜尋「Spring Tools」並安裝相應版本，以安裝 Spring Tool Suite (STS) 外掛程式。這將增強 Spring 和 Spring Boot 的開發功能。您可以直接在 Eclipse 中透過 File -> New -> Spring Starter Project 建立新的 Spring Boot 專案，選擇 Maven 作為建置工具，並添加必要的依賴項如 Spring Web。

### 整合 IBM Websphere Liberty
在 Eclipse Marketplace 中搜尋「IBM Liberty Developer Tools」並按照安裝提示進行安裝。前往 Window -> Preferences -> Servers -> Runtime Environments，添加新的 Websphere Liberty 運行環境，並透過 File -> New -> Other -> Server 建立伺服器實例。請確保伺服器的 server.xml 包含 `<feature>springBoot-2.0</feature>` 以支援 Spring Boot，詳情請參閱 [Open Liberty 文件](https://openliberty.io/docs/latest/deploy-spring-boot.html)。

### 部署應用程式
修改您的 Spring Boot 應用程式，使其繼承 `SpringBootServletInitializer` 而非使用啟動嵌入式伺服器的 main 方法，並在 pom.xml 中設定 `<packaging>war</packaging>` 將其打包為 WAR 檔案。右鍵點擊專案，選擇「Run As -> Run on Server」並選擇您的 Liberty 伺服器進行部署。這將確保應用程式在 Liberty 的 Web 容器中運行。

---

### 調查備註：使用 Eclipse 搭配 IBM Websphere Liberty、Spring、Spring Boot 及 Maven 的完整指南

本指南提供詳細步驟，說明如何有效使用 Eclipse 搭配 IBM Websphere Liberty、Spring、Spring Boot 及 Maven，專為在這些生態系統中工作的開發人員量身定制。流程包括設定 Eclipse、安裝必要外掛程式、建立與配置專案，以及部署應用程式，重點在於整合與最佳實踐（截至 2025 年 2 月 27 日）。

#### Eclipse 設定與先決條件
Eclipse 作為 Java 開發的強大 IDE，特別適用於企業級應用程式。對於此設定，請下載「Eclipse IDE for Enterprise Java and Web Developers」2024-06 版本，可從 [Eclipse 下載頁面](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) 取得。請確保系統已安裝 JDK 17 或更新版本，您可以在終端機中執行 `java -version` 來檢查。此版本確保與現代 Spring 及 Liberty 功能的相容性。

#### 安裝必要外掛程式
為增強 Eclipse 的 Spring 和 Spring Boot 開發功能，請安裝 Spring Tool Suite (STS)，這是 Spring 工具的新一代版本。透過 Help -> Eclipse Marketplace 存取，搜尋「Spring Tools」並安裝標示為「Spring Tools (aka Spring IDE and Spring Tool Suite)」的項目。此外掛程式在 [Spring Tools](https://spring.io/tools/) 中有詳細說明，為 Spring 基礎應用程式提供頂級支援，並與 Eclipse 無縫整合以實現專案建立和除錯等功能。

對於 IBM Websphere Liberty 整合，請安裝 IBM Liberty Developer Tools，同樣可透過 Eclipse Marketplace 搜尋「IBM Liberty Developer Tools」取得。此外掛程式經測試適用於 Eclipse 2024-06，如 [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) 中所述，便於將 Java EE 應用程式建置並部署至 Liberty，並支援回溯至 2019-12 的版本。

#### 建立 Spring Boot 專案
在已安裝 STS 的 Eclipse 中，有兩種主要方法可建立 Spring Boot 專案：

1. **使用 Spring Initializr**：造訪 [Spring Initializr](https://start.spring.io/)，選擇 Maven 作為建置工具，選擇專案元數據（Group、Artifact 等），並添加依賴項如 Spring Web。將專案生成為 ZIP 檔案，解壓縮後透過 File -> Import -> Existing Maven Project 匯入至 Eclipse，選擇解壓縮的資料夾。

2. **直接使用 STS**：開啟 Eclipse，前往 File -> New -> Other，展開 Spring Boot，並選擇「Spring Starter Project」。按照精靈操作，確保選擇 Maven 作為類型，並選擇依賴項。此方法如 [使用 Eclipse 和 Maven 建立 Spring Boot 專案](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) 中所述，因其與 Eclipse 工作區的整合而受到推薦。

兩種方法均確保建立基於 Maven 的專案，這對於使用 Spring Boot 進行依賴管理至關重要。

#### 配置 Websphere Liberty 部署
要部署至 Websphere Liberty，需修改您的 Spring Boot 應用程式，使其在 Liberty 的 Web 容器上運行，而非啟動嵌入式伺服器。這包括：

- 確保主應用程式類別繼承 `SpringBootServletInitializer`。例如：

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // 無 main 方法；Liberty 處理啟動
  }
  ```

- 更新 pom.xml 以打包為 WAR 檔案，添加：

  ```xml
  <packaging>war</packaging>
  ```

  這對於傳統 Servlet 容器部署是必要的，如 [部署 Spring Boot 應用程式](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) 中所述。

Websphere Liberty，特別是其開源變體 Open Liberty，透過特定功能支援 Spring Boot 應用程式。請確保 Liberty 伺服器的 server.xml 包含 `<feature>springBoot-2.0</feature>` 以支援 Spring Boot 2.x，如 [Open Liberty 文件](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中詳細說明。此配置會停用嵌入式 Web 容器，轉而利用 Liberty 的容器。

#### 在 Eclipse 中設定與配置 Websphere Liberty 伺服器
安裝 IBM Liberty Developer Tools 後，設定 Liberty 伺服器：

- 前往 Window -> Preferences -> Servers -> Runtime Environments，點擊「Add」，並選擇「WebSphere Application Server Liberty」。按照精靈定位您的 Liberty 安裝目錄，通常位於如 `<Liberty_Root>/wlp` 的目錄中，如 [Liberty 與 Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) 中所述。

- 透過 File -> New -> Other -> Server 建立新的伺服器實例，選擇「WebSphere Application Server Liberty」及您配置的運行環境。為伺服器命名並根據需要調整設定。

- 編輯伺服器的 server.xml（可透過 Servers 視圖存取）以包含必要功能。對於 Spring Boot，添加：

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- 其他功能如 servlet-3.1 以支援 Web -->
  </featureManager>
  ```

此設定由 [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) 支援，確保與 Spring Boot 應用程式的相容性。

#### 部署與運行應用程式
要部署，請在 Project Explorer 中右鍵點擊您的專案，選擇「Run As -> Run on Server」，選擇您的 Liberty 伺服器，然後點擊 Finish。Eclipse 會將 WAR 檔案部署至 Liberty 伺服器，您可以在 Console 視圖中監控日誌。請確保在 server.xml 中正確設定應用程式上下文根（通常在 `<webApplication>` 標籤下），以便透過適當的 URL（例如 `http://localhost:9080/yourapp`）存取您的應用程式。

對於除錯，請使用 Debug 視角，根據需要設定中斷點，並利用 Liberty 對遠端除錯的支援，如 [使用 Eclipse 和 Liberty 進行除錯](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) 中討論。

#### 其他注意事項
- **打包選項**：雖然 WAR 是 Servlet 容器的標準，但 Open Liberty 也支援 JAR 部署，如 [配置並部署 Spring Boot 至 Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) 中所示。對於 JAR，請確保應用程式配置為不啟動嵌入式伺服器，這可能需要額外的 Liberty 功能或配置。
- **Maven 整合**：使用 Maven 進行依賴管理，確保包含 `liberty-maven-plugin` 以實現自動化部署，如 [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) 中所述。
- **疑難排解**：若出現問題，請檢查 Liberty 伺服器實例下 `logs` 目錄中的伺服器日誌，並確保 Liberty 版本與 Spring Boot 相容，例如 Liberty 8.5.5.9 或更高版本支援可運行 JAR，根據 [Stack Overflow 討論](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application)。

此完整設定確保能有效使用 Eclipse 來開發並部署 Spring Boot 應用程式至 IBM Websphere Liberty，同時利用 Maven 進行建置管理。

#### 表格：部署選項比較

| 部署類型       | 優點                                      | 缺點                                      | 配置注意事項                          |
|----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR 檔案       | Servlet 容器的標準，廣泛支援 | 需要繼承 `SpringBootServletInitializer` | 在 pom.xml 中設定 `<packaging>war</packaging>`  |
| JAR 檔案       | 開發更簡單，Open Liberty 支援 | 可能需要額外的 Liberty 功能   | 確保不啟動嵌入式伺服器，使用 springBoot 功能 |

此表格源自 [Open Liberty 文件](https://openliberty.io/docs/latest/deploy-spring-boot.html)，有助於根據專案需求選擇合適的部署策略。

### 主要參考文獻
- [使用 Eclipse 和 Maven 建立 Spring Boot 專案，逐步指南](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools，適用於 Java EE 應用程式的 Eclipse 外掛程式](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty 文件，部署 Spring Boot 應用程式](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools，新一代 Spring 開發工具](https://spring.io/tools/)
- [Eclipse 下載，企業級 Java 開發套件](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty 與 Eclipse，安裝開發環境](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [部署 Spring Boot 應用程式，Spring Boot 參考文獻](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)