---
audio: false
lang: hant
layout: post
title: 春季內部運作
translated: true
---

讓我們深入了解 Spring 及其內部運作。Spring 是一個用於構建 Java 應用程式的強大框架，我將逐步解答您的每個查詢，並提供清晰的解釋。

### Spring 是如何運作的？
Spring 基於 **控制反轉（IoC）** 的原則運作。這意味著，您的應用程式代碼不再控制物件的創建和管理，而是由 Spring 控制。它通過一個稱為 **IoC 容器** 的組件來實現這一點。IoC 容器負責：

- **實例化** 物件（在 Spring 中稱為 beans）。
- **配置** 它們根據您的規範。
- **組裝** 它們通過管理它們的依賴。

這種方法減少了代碼中的緊密耦合，使其更加模組化且易於維護。

### Spring 是如何管理 Beans 的？
在 Spring 中，**beans** 是由 IoC 容器管理的物件。以下是 Spring 如何處理它們的方法：

1. **定義**：您可以在以下位置定義 beans：
   - **XML 配置文件**。
   - **基於 Java 的配置** 使用註解如 `@Bean`、`@Component`、`@Service` 等。
2. **創建**：當應用程式啟動時，IoC 容器讀取這些定義並創建 beans。
3. **依賴注入（DI）**：Spring 自動將依賴（其他 beans）注入到需要的 bean 中，使用：
   - **構造函數注入**。
   - **設置方法注入**。
   - **字段注入**（通過 `@Autowired`）。

容器管理這些 beans 的整個生命週期——從創建到銷毀——並確保它們在需要時可用。

### Service 和 Controller 的區別
在 **Spring MVC**（Spring 的 Web 框架）的上下文中，這兩個組件有不同的用途：

- **Controller**：
  - 處理來自用戶的 **HTTP 請求**。
  - 處理輸入，調用業務邏輯，並決定返回哪個 **視圖**（例如，網頁）。
  - 使用 `@Controller` 或 `@RestController` 註解。
  - 屬於 **Web 層**。

- **Service**：
  - 封裝應用程式的 **業務邏輯**。
  - 執行計算、數據處理或與數據庫交互等任務。
  - 使用 `@Service` 註解。
  - 屬於 **業務層**。

**範例**：
- 控制器可能會接收顯示用戶個人資料的請求並調用服務來獲取用戶數據。
- 服務從數據庫中檢索數據並將其返回給控制器，控制器再將其發送給視圖。

簡而言之：**控制器管理 Web 交互**，而 **服務處理核心功能**。

### Spring 提供了什麼？
Spring 是一個全面的框架，為企業應用程式提供了廣泛的工具。主要功能包括：

- **依賴注入**：簡化管理物件依賴。
- **面向切面編程（AOP）**：添加跨切面關注點如記錄或安全性。
- **事務管理**：確保操作的數據一致性。
- **Spring MVC**：構建強大的 Web 應用程式。
- **Spring Boot**：通過預配置的默認值和嵌入式伺服器簡化設置。
- **Spring Data**：簡化數據庫訪問。
- **安全性**：提供身份驗證和授權工具。

Spring 的模組化設計讓您只能選擇所需的功能。

### Spring 是如何查找物件或 Beans 的？
當 Spring 應用程式啟動時：

1. **IoC 容器** 初始化。
2. 它在以下位置掃描 **bean 定義**：
   - XML 文件。
   - 註解類（例如 `@Component`、`@Bean`）。
3. 容器創建 beans 並將它們存儲在一個 **map** 中，按名稱或類型索引。
4. 當需要 bean（例如，用於注入或直接檢索）時，容器使用以下方法提供它：
   - **按名稱查找**。
   - **按類型查找**（例如，通過 `@Autowired`）。

這個過程確保 beans 在應用程式中隨時可用。

### 如何使用 Tomcat 或 Netty 作為伺服器？
Spring Boot，Spring 的擴展，通過直接將伺服器嵌入到應用程式中簡化了伺服器設置。以下是它與 **Tomcat** 和 **Netty** 的工作方式：

- **Tomcat**（基於 Servlet）：
  - Spring Boot 的 `spring-boot-starter-web` 依賴項中的默認伺服器。
  - 將其添加到您的 `pom.xml` 中：
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot 嵌入 Tomcat，您的應用程式作為獨立的可執行 JAR 運行。

- **Netty**（非 Servlet 基於）：
  - 用於反應式 Web 應用程式（例如，使用 Spring WebFlux）。
  - 通過排除 Tomcat 並添加 Netty 來替換 Tomcat：
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot 嵌入 Netty，支持非阻塞的非同步 I/O。

您可以通過 `application.properties` 配置伺服器（例如，設置端口 `server.port=8080`）。不需要外部伺服器部署——Spring Boot 會處理所有事務。

### 總結
- **Spring 的核心**：使用 IoC 容器管理物件。
- **Bean 管理**：通過 XML 或註解定義，依賴自動注入。
- **Service vs. Controller**：服務處理業務邏輯；控制器管理 Web 請求。
- **功能**：提供 DI、AOP、Web 支持等。
- **Bean 查找**：容器從配置中查找並提供 beans。
- **伺服器**：Spring Boot 通過簡單的依賴項更改嵌入 Tomcat 或 Netty。