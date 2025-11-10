---
audio: false
generated: true
lang: hant
layout: post
title: 掌握 Spring Boot 中的 Spring Cloud Sleuth
translated: true
type: note
---

Spring Cloud Sleuth 是一個強大的工具，能為 Spring 應用程式加入分散式追蹤功能。雖然它在微服務架構中特別有用，能追蹤跨越多個服務的請求，但透過增強日誌關聯性和除錯能力，它同樣能為單體應用程式帶來顯著效益。

本指南將提供在單一 Spring Boot 應用程式中使用 Spring Cloud Sleuth 的全面概述，並借鑒 Baeldung 的實作方法。

## 1. 什麼是 Spring Cloud Sleuth？

Spring Cloud Sleuth 的核心功能是對 Spring 應用程式進行檢測，自動將追蹤資訊加入日誌，並在單一應用程式的不同元件甚至執行緒之間傳播這些資訊。它利用 OpenZipkin 的 Brave 函式庫來實現此功能。

**關鍵術語：**

  * **追蹤（Trace）：** 代表流經應用程式的單一請求或作業。每個追蹤都有唯一的 `traceId`。可將其視為請求的端到端旅程。
  * **跨度（Span）：** 代表追蹤中的一個邏輯工作單元。一個追蹤由多個跨度組成，形成樹狀結構。每個跨度都有唯一的 `spanId`。例如，傳入的 HTTP 請求可能是一個跨度，而該請求內的方法呼叫可能是另一個（子）跨度。
  * **MDC（映射診斷上下文）：** Sleuth 與 Slf4J 的 MDC 整合，將 `traceId` 和 `spanId` 注入到您的日誌訊息中，從而輕鬆篩選和關聯特定請求的日誌。

## 2. 為什麼要在單一應用程式中使用 Sleuth？

即使在單體應用程式中，請求通常也會涉及多個層次、非同步操作和不同的執行緒。手動關聯單一請求的日誌訊息既繁瑣又容易出錯。Sleuth 透過以下方式自動化此過程：

  * **簡化除錯：** 透過將 `traceId` 和 `spanId` 加入每個日誌條目，您可以輕鬆篩選日誌，查看與特定使用者請求相關的所有內容，即使該請求在您的單一應用程式中遍歷多個方法、服務或執行緒。
  * **提升可觀測性：** 更清晰地展示請求的流動方式以及潛在的瓶頸或問題可能發生的位置。
  * **一致性：** 確保日誌關聯的方法保持一致，無需在程式碼庫的每個部分手動處理。

## 3. 入門：設定與配置

### 3.1. 專案設定（Maven）

首先，建立一個新的 Spring Boot 專案（可以使用 Spring Initializr），並將 `spring-cloud-starter-sleuth` 相依性加入您的 `pom.xml`：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**重要：** 請確保您使用的是相容的 Spring Boot 和 Spring Cloud 版本。Spring Cloud 相依性通常使用物料清單（BOM）進行管理。

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

將 `${spring-cloud.version}` 替換為適當的發布列車版本（例如 `2021.0.1`、`2022.0.0`）。

### 3.2. 應用程式名稱

強烈建議在您的 `application.properties` 或 `application.yml` 檔案中設定應用程式名稱。此名稱將出現在日誌中，有助於識別日誌來源，尤其是在您後續遷移到分散式系統時。

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. 日誌模式

Spring Cloud Sleuth 會自動修改預設的日誌模式以包含 `traceId` 和 `spanId`。使用 Sleuth 的典型日誌輸出可能如下所示：

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

此處：

  * `my-single-app`：是 `spring.application.name`。
  * `a1b2c3d4e5f6a7b8`：是 `traceId`。
  * `a1b2c3d4e5f6a7b8`（第二個）：是 `spanId`（對於根跨度，traceId 和 spanId 通常相同）。
  * `false`：表示該跨度是否可匯出（true 表示它將發送到追蹤收集器如 Zipkin）。

如果您有自訂的日誌模式，則需要使用 `%X{traceId}` 和 `%X{spanId}`（針對 Logback）明確將 `traceId` 和 `spanId` 加入其中。

在 `logback-spring.xml` 中的自訂 Logback 模式範例：

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4. Sleuth 在單一應用程式中的運作原理

一旦 `spring-cloud-starter-sleuth` 相依性出現在 classpath 中，Spring Boot 的自動配置就會接管。

### 4.1. 自動檢測

Sleuth 會自動檢測常見的 Spring 元件和通訊通道：

  * **Servlet 過濾器：** 用於傳入您控制器的 HTTP 請求。
  * **RestTemplate：** 用於使用 `RestTemplate` 進行的傳出 HTTP 呼叫（確保您使用 bean 管理的 `RestTemplate`，以便 Sleuth 能自動檢測它）。
  * **排程動作：** 用於 `@Scheduled` 方法。
  * **訊息通道：** 用於 Spring Integration 和 Spring Cloud Stream。
  * **非同步方法：** 用於 `@Async` 方法（確保追蹤/跨度上下文跨執行緒傳播）。

### 4.2. 簡單的 Web 請求範例

考慮一個具有 REST 控制器的簡單 Spring Boot 應用程式：

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {

    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @GetMapping("/")
    public String helloSleuth() {
        logger.info("Hello from MyController");
        return "success";
    }
}
```

當您存取 `http://localhost:8080/` 時，您會看到類似以下的日誌訊息：

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

請注意自動加入的 `traceId` 和 `spanId`。

### 4.3. 跨方法傳播上下文（相同跨度）

如果您的請求在單一應用程式中流經多個方法，並且您希望這些方法屬於*同一跨度*，Sleuth 會自動處理這一點。

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.stereotype.Service;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    public void doSomeWork() throws InterruptedException {
        Thread.sleep(100); // 模擬一些工作
        logger.info("Doing some work in MyService");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/same-span-example")
    public String sameSpanExample() throws InterruptedException {
        logger.info("Entering same-span-example endpoint");
        myService.doSomeWork();
        logger.info("Exiting same-span-example endpoint");
        return "success";
    }
}
```

`/same-span-example` 的日誌將顯示控制器和服務方法具有相同的 `traceId` 和 `spanId`：

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. 手動建立新跨度

您可能希望在應用程式中為一個獨立的工作單元建立一個新跨度，即使它是同一整體追蹤的一部分。這允許進行更細粒度的追蹤和計時。Spring Cloud Sleuth 提供了 `Tracer` API 來實現這一點。

```java
import brave.Tracer;
import brave.Span;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    @Autowired
    private Tracer tracer; // 注入 Brave Tracer

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // 建立一個具有描述性名稱的新跨度
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // 在新跨度中模擬一些工作
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // 始終完成跨度
        }

        logger.info("I'm back in the original span");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/new-span-example")
    public String newSpanExample() throws InterruptedException {
        logger.info("Entering new-span-example endpoint");
        myService.doSomeWorkNewSpan();
        logger.info("Exiting new-span-example endpoint");
        return "success";
    }
}
```

`/new-span-example` 的日誌將顯示追蹤 ID 保持不變，但會為 "custom-internal-work" 出現一個新的 `spanId`：

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

請注意，在 `custom-internal-work` 部分內，`spanId` 變更為 `8a9b0c1d2e3f4a5b`，然後恢復。

### 4.5. 非同步處理

Sleuth 與 Spring 的 `@Async` 註解無縫整合，以跨執行緒邊界傳播追蹤上下文。

首先，在您的主應用程式類別中啟用非同步處理：

```java
@SpringBootApplication
@EnableAsync // 啟用非同步執行
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

然後，建立一個非同步服務：

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class AsyncService {
    private static final Logger logger = LoggerFactory.getLogger(AsyncService.class);

    @Async
    public void performAsyncTask() throws InterruptedException {
        logger.info("Starting async task");
        Thread.sleep(500); // 模擬一些長時間執行的任務
        logger.info("Finished async task");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private AsyncService asyncService;

    @GetMapping("/async-example")
    public String asyncExample() throws InterruptedException {
        logger.info("Calling async task");
        asyncService.performAsyncTask();
        logger.info("Async task initiated, returning from controller");
        return "success";
    }
}
```

日誌將顯示非同步方法具有相同的 `traceId` 但不同的 `spanId`，因為它在新的執行緒中執行並代表一個新的工作單元：

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... 一段時間後 ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

請注意，`traceId` 保持不變，但非同步方法的 `spanId` 發生變化，並且執行緒名稱也反映了非同步執行器。

### 4.6. 使用 `@SpanName` 自訂跨度名稱

您可以使用 `@SpanName` 註解為自動產生的跨度提供更具意義的名稱。

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // 自訂跨度名稱
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... 在您的控制器或其他服務中 ...
@Autowired
private AnnotatedService annotatedService;

@GetMapping("/annotated-span")
public String annotatedSpanExample() throws InterruptedException {
    logger.info("Calling annotated method");
    annotatedService.annotatedMethod();
    logger.info("Finished calling annotated method");
    return "success";
}
```

日誌將反映自訂的跨度名稱：

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5. 與 Zipkin 整合（可選但推薦）

雖然本指南側重於單一應用程式，但 Sleuth 的真正威力在於與分散式追蹤系統（如 Zipkin）整合時顯現。Zipkin 收集 Sleuth 匯出的追蹤和跨度資料，並提供一個 UI 來視覺化請求的流動和計時。

要與 Zipkin 整合，請加入 `spring-cloud-starter-zipkin` 相依性：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

預設情況下，Sleuth 會嘗試將追蹤發送到運行在 `http://localhost:9411` 的 Zipkin 收集器。您可以在 `application.properties` 中配置此設定：

```properties
spring.zipkin.base-url=http://localhost:9411
```

您可以使用 Docker 輕鬆運行 Zipkin 伺服器：

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

一旦 Zipkin 運行，您的單一 Spring Boot 應用程式將自動發送其追蹤資料，您可以在 `http://localhost:9411/` 查看追蹤。

## 6. 取樣

預設情況下，Sleuth 應用取樣策略以避免追蹤系統被資料淹沒。它通常對一定百分比的請求進行取樣。您可以在 `application.properties` 中配置取樣率：

```properties
# 對 100% 的請求進行取樣
spring.sleuth.sampler.probability=1.0
```

值為 `1.0` 表示所有請求都將被追蹤，而 `0.1` 表示 10% 的請求將被追蹤。

## 7. 結論

Spring Cloud Sleuth 即使在單一應用程式中，也能透過自動將 `traceId` 和 `spanId` 注入到您的日誌訊息中，顯著增強日誌記錄和除錯能力。這使您能夠輕鬆追蹤單一請求的執行流程，即使它遍歷不同的方法和執行緒。透過理解追蹤和跨度的核心概念，並利用 Sleuth 的自動檢測或手動跨度建立，您可以對單體應用程式獲得更好的可觀測性。與 Zipkin 整合進一步釋放了視覺化和分析應用程式行為的潛力。