---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 與 Spring Framework 比較
translated: true
type: note
---

讓我們深入探討 **Spring Boot** 與 **Spring**（通常指 Spring Framework）之間的差異。雖然它們密切相關，但在 Java 生態系統中擔當著不同的角色。我將從幾個關鍵維度進行剖析，包括用途、配置、開發速度和應用場景。

### 1. **概述與用途**
- **Spring Framework**：這是 Java 應用程式的原始基礎框架。自 2002 年推出以來，它提供全面的編程和配置模型，以簡化企業級 Java 開發。它是一個廣泛的生態系統，包含 Spring MVC、Spring Security 和 Spring Data 等模組，重點關注依賴注入和模組化。
- **Spring Boot**：建基於 Spring Framework 之上的一層，於 2014 年推出。它旨在通過提供「即開即用」的體驗和最少配置來簡化 Spring 開發。可以將其視為「內置電池」的 Spring — 專為快速應用程式開發和生產就緒而優化。

### 2. **配置**
- **Spring**：需要手動配置。您需要定義 bean、設置依賴關係並配置組件（例如通過 XML 文件或 Java 註解）。這提供了細粒度的控制，但可能耗時且容易出錯，特別是對初學者而言。
- **Spring Boot**：強調**自動配置**。它根據您包含的依賴項（例如，添加 Spring Web 會自動設置像 Tomcat 這樣的 Web 伺服器）使用合理的默認值。您可以根據需要覆蓋這些默認值，但目標是最小化設置工作。

### 3. **開發速度**
- **Spring**：起步較慢，因為您需要手動連接所有內容 — 依賴項、伺服器、數據庫連接等。它功能強大，但需要更多精力才能讓一個基本應用程式運行起來。
- **Spring Boot**：由於其「約定優於配置」的理念，開發速度更快。例如，借助嵌入式伺服器和 starter 依賴項，一個簡單的 REST API 可以在幾分鐘內用幾行代碼搭建起來。

### 4. **依賴管理**
- **Spring**：依賴您通過 Maven 或 Gradle 手動管理依賴項。您需要挑選 Spring 模組（例如 Spring Core、Spring MVC）和第三方庫，如果處理不當，可能會導致版本衝突。
- **Spring Boot**：提供 **starter 依賴項**（例如 `spring-boot-starter-web`、`spring-boot-starter-data-jpa`），這些依賴項捆綁了相容版本的庫。這減少了依賴管理的麻煩並確保一致性。

### 5. **嵌入式伺服器**
- **Spring**：不包含嵌入式伺服器。您通常將 Spring 應用程式部署到外部伺服器，如 Tomcat、JBoss 或 WebSphere，這需要額外的設置。
- **Spring Boot**：默認附帶嵌入式伺服器（Tomcat、Jetty 或 Undertow）。您可以使用 `java -jar` 將應用程式作為獨立的 JAR 文件運行，這使得部署更簡單、更便攜（例如用於 Docker）。

### 6. **生產就緒**
- **Spring**：提供 Spring Security 和 Spring Transaction Management 等工具，但您需要自行配置監控、健康檢查和指標。
- **Spring Boot**：包含 **Spring Boot Actuator**，它開箱即用地提供了生產就緒的功能 — 健康端點、指標、日誌記錄等。它設計為只需最少調整即可部署。

### 7. **靈活性 vs 簡潔性**
- **Spring**：高度靈活且可自定義。當您需要完全控制應用程式的每個方面時，它是理想的選擇，但這是以複雜性為代價的。
- **Spring Boot**：以部分靈活性換取簡潔性。它是「約定優於配置」的，意味著它強制執行約定（例如項目結構、默認設置）以簡化開發，儘管您仍然可以對其進行自定義。

### 8. **應用場景**
- **Spring**：最適合複雜的大型企業應用程式，這些應用需要整合多樣化的組件或遺留系統，並且不介意設置開銷。
- **Spring Boot**：非常適合現代化的快速開發場景 — 微服務、REST API、獨立應用程式或原型開發，其中速度和簡潔性至關重要。

### 範例比較
- **Spring（基本設置）**：
  ```java
  // 使用 Spring MVC 進行手動配置
  @Configuration
  @EnableWebMvc
  public class WebConfig implements WebMvcConfigurer {
      @Bean
      public ViewResolver viewResolver() {
          InternalResourceViewResolver resolver = new InternalResourceViewResolver();
          resolver.setPrefix("/WEB-INF/views/");
          resolver.setSuffix(".jsp");
          return resolver;
      }
  }
  ```
  此外，您還需要配置 `web.xml` 或 servlet 初始化器，並部署到外部伺服器。

- **Spring Boot（等效實現）**：
  ```java
  @RestController
  public class HelloController {
      @GetMapping("/hello")
      public String sayHello() {
          return "Hello, World!";
      }
  }
  ```
  將 `spring-boot-starter-web` 添加到您的 `pom.xml` 中，就完成了 — 使用嵌入式伺服器運行它。

### 總結表格

| 維度              | Spring Framework            | Spring Boot                 |
|---------------------|-----------------------------|-----------------------------|
| **用途**         | Java 核心框架     | 簡化 Spring 使用     |
| **配置**   | 手動（XML/註解）    | 自動配置             |
| **伺服器**          | 外部（例如 Tomcat）     | 嵌入式（Tomcat、Jetty）    |
| **依賴項**    | 手動管理           | Starter 簡化管理        |
| **速度**           | 起步較慢             | 快速設置和原型開發  |
| **靈活性**     | 高，完全可自定義    | 約定優於配置，靈活性較低  |
| **最適合**        | 複雜企業應用程式     | 微服務、快速應用程式   |

### 結論
- **Spring** 是基礎 — 功能強大、靈活，適合需要完全控制或處理遺留系統的場景。
- **Spring Boot** 是簡化版的 Spring — 專為現代化、快節奏的開發而設計，重點關注微服務和獨立應用程式。

如果您要開始一個新項目並且重視速度，請選擇 Spring Boot。如果您要維護一個複雜系統或需要深度自定義，Spring 可能是更好的基礎。想讓我深入探討任何部分嗎？