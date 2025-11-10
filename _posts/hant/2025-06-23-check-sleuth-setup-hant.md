---
audio: false
generated: true
lang: hant
layout: post
title: 排查日誌中缺失追蹤ID與跨度ID的問題
translated: true
type: note
---

您的日誌行 `[blog-server,,]` 中 `traceId` 和 `spanId` 為空，可能由以下原因導致：

* **缺少或錯誤的 Sleuth 依賴項：** 請確保在專案的 `pom.xml`（Maven）或 `build.gradle`（Gradle）中正確添加了 `spring-cloud-starter-sleuth` 依賴項，並且您使用的 Spring Boot 和 Spring Cloud 版本相容。若缺少此依賴項，Spring Cloud Sleuth 的自動配置將無法啟動。

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

* **自定義日誌模式：** 如果您定義了自定義日誌模式（例如在 `logback-spring.xml` 或 `application.properties` 中），則必須明確包含 `traceId` 和 `spanId` 的佔位符。若缺少這些佔位符，即使 Sleuth 已啟用，這些 ID 也不會出現在日誌中。

    對於 Logback，請確保模式包含 `%X{traceId}` 和 `%X{spanId}`：

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

* **無活躍的追蹤/跨度上下文：** 雖然 Sleuth 會自動檢測許多 Spring 組件（例如用於 HTTP 請求的 `DispatcherServlet`），但這些特定日誌訊息可能是在尚未初始化或傳播追蹤或跨度的上下文中生成的。例如，某些應用程式啟動初期的日誌，或來自不受 Sleuth 上下文傳播管理的執行緒的日誌，可能不會包含這些 ID。然而，對於活躍 HTTP 請求處理期間的日誌（如 `HttpEntityMethodProcessor` 和 `DispatcherServlet` 完成請求時），若 Sleuth 設置正確，這種情況較為少見。

進行故障排除時，請先驗證您的依賴項和日誌配置。若這些配置正確，請確保請求確實到達您的應用程式並由 Spring MVC `DispatcherServlet` 處理，這應會觸發 Sleuth 的檢測功能。