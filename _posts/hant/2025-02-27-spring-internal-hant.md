---
audio: false
generated: true
lang: hant
layout: post
title: 春季內部運作
translated: true
type: note
---

讓我們深入探討 Spring 及其內部運作原理。Spring 是一個用於構建 Java 應用程式的強大框架，我將逐步解答您的疑問並提供清晰說明。

### Spring 如何運作？
Spring 基於**控制反轉（IoC）**原則運作。這意味著不再由您的應用程式代碼控制物件的創建和管理，而是由 Spring 接管。它透過名為 **IoC 容器**的組件實現此功能。IoC 容器負責：

- **實例化**物件（在 Spring 中稱為 bean）
- 根據您的設定**配置**它們
- 透過管理其依賴關係來**組裝**它們

這種方法減少了代碼中的緊密耦合，使其更具模組化且更易於維護。

### Spring 如何管理 Bean？
在 Spring 中，**bean** 是由 IoC 容器管理的物件。以下是 Spring 處理它們的方式：

1. **定義**：您可以透過以下方式定義 bean：
   - **XML 設定檔**
   - 使用註解（如 `@Bean`、`@Component`、`@Service` 等）的 **Java 設定**
2. **創建**：當應用程式啟動時，IoC 容器讀取這些定義並創建 bean
3. **依賴注入（DI）**：Spring 會自動將依賴項（其他 bean）注入到需要的地方，使用以下方式：
   - **建構子注入**
   - **Setter 注入**
   - **欄位注入**（透過 `@Autowired`）

容器管理這些 bean 的整個生命週期——從創建到銷毀——並確保在需要時可用。

### Service 與 Controller 的區別
在 **Spring MVC**（Spring 的網頁框架）情境中，這兩個組件具有不同的用途：

- **Controller**：
  - 處理來自使用者的 **HTTP 請求**
  - 處理輸入、調用業務邏輯，並決定返回哪個**視圖**（例如網頁）
  - 使用 `@Controller` 或 `@RestController` 註解
  - 位於 **Web 層**

- **Service**：
  - 封裝應用程式的**業務邏輯**
  - 執行計算、資料處理或與資料庫互動等任務
  - 使用 `@Service` 註解
  - 位於**業務層**

**範例**：
- Controller 可能接收顯示使用者個人資料的請求，並調用 Service 來獲取使用者資料
- Service 從資料庫檢索資料並返回給 Controller，後者將其發送到視圖

簡而言之：**Controller 管理網頁互動**，而 **Service 處理核心功能**。

### Spring 提供哪些功能？
Spring 是一個全面的框架，為企業應用程式提供多種工具。主要功能包括：

- **依賴注入**：簡化物件依賴關係的管理
- **面向切面程式設計（AOP）**：添加橫切關注點，如日誌記錄或安全性
- **事務管理**：確保操作間的資料一致性
- **Spring MVC**：構建強大的網頁應用程式
- **Spring Boot**：透過預設設定和嵌入式伺服器簡化設定
- **Spring Data**：簡化資料庫存取
- **安全性**：提供身份驗證和授權工具

Spring 的模組化設計讓您可以僅選擇所需的功能。

### Spring 如何尋找物件或 Bean？
當 Spring 應用程式啟動時：

1. **IoC 容器**初始化
2. 它在以下位置掃描 **bean 定義**：
   - XML 檔案
   - 帶註解的類別（例如 `@Component`、`@Bean`）
3. 容器創建 bean 並將其儲存在以名稱或類型索引的**映射**中
4. 當需要 bean 時（例如用於注入或直接檢索），容器透過以下方式提供：
   - **按名稱查找**
   - **按類型查找**（例如透過 `@Autowired`）

此過程確保 bean 在整個應用程式中隨時可用。

### 如何使用 Tomcat 或 Netty 作為伺服器？
Spring Boot 是 Spring 的擴展，透過將伺服器直接嵌入您的應用程式來簡化伺服器設定。以下是與 **Tomcat** 和 **Netty** 的運作方式：

- **Tomcat**（基於 Servlet）：
  - Spring Boot 的 `spring-boot-starter-web` 依賴項中的預設伺服器
  - 將以下內容添加到您的 `pom.xml`：
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot 嵌入 Tomcat，您的應用程式作為獨立的可執行 JAR 運行

- **Netty**（非基於 Servlet）：
  - 用於響應式網頁應用程式（例如與 Spring WebFlux 一起使用）
  - 透過排除 Tomcat 並添加 Netty 來替換：
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot 改為嵌入 Netty，支援非同步、非阻塞 I/O

您可以透過 `application.properties` 設定伺服器（例如使用 `server.port=8080` 設定連接埠）。無需外部伺服器部署——Spring Boot 處理所有事項。

### 總結
- **Spring 核心**：使用 IoC 容器進行物件管理
- **Bean 管理**：透過 XML 或註解定義，自動注入依賴項
- **Service 與 Controller**：Service 處理業務邏輯；Controller 管理網頁請求
- **功能**：提供 DI、AOP、網頁支援等
- **Bean 查找**：容器從設定中尋找並提供 bean
- **伺服器**：Spring Boot 透過簡單的依賴項變更嵌入 Tomcat 或 Netty