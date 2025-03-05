---
audio: true
generated: true
lang: hant
layout: post
title: 應用程序指標
translated: true
---

`com.yammer.metrics` 圖書館，原本由 Yammer 開發，現已成為 **Dropwizard Metrics** 圖書館的一部分。它提供了一種強大的方法來收集和報告 Java 應用程序的指標，幫助您監控諸如請求計數、響應時間等性能方面。以下是如何有效使用它的指南。

---

### 第 1 步：添加依賴
由於 `com.yammer.metrics` 已經演變為 Dropwizard Metrics，您應該使用 Dropwizard Metrics 圖書館。如果您使用 Maven，請將以下依賴項添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- 使用最新可用版本 -->
</dependency>
```

根據您的需求，您可能還需要其他模塊，例如：
- `metrics-jvm` 用於 JVM 相關指標。
- `metrics-httpclient` 用於 HTTP 客戶端指標。
- `metrics-jersey` 用於與 Jersey Web 框架集成。

請參閱 [Dropwizard Metrics 文檔](https://metrics.dropwizard.io/) 以獲取最新版本和可用模塊。

---

### 第 2 步：創建指標註冊表
`MetricRegistry` 是存儲所有指標的中心位置。您通常為應用程序創建一個實例：

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### 第 3 步：使用不同類型的指標
Dropwizard Metrics 支持多種指標類型，每種都適合不同的監控需求：

#### **計數器**
計數器用於跟蹤可以增加或減少的值（例如，處理的請求數量）。

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 增加 1
counter.inc(5); // 增加 5
counter.dec();  // 減少 1
```

#### **儀表**
儀表提供特定時刻的值快照（例如，當前隊列大小）。您可以通過實現 `Gauge` 接口來定義儀表：

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // 替換為您的邏輯
    }
});
```

#### **直方圖**
直方圖跟蹤值的統計分佈（例如，請求大小）：

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // 記錄一個值
```

#### **計量器**
計量器測量事件的速率（例如，每秒請求數）：

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // 記錄一個事件
```

#### **計時器**
計時器測量事件的速率和持續時間（例如，請求處理時間）：

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // 模擬一些工作
    Thread.sleep(100);
} finally {
    context.stop(); // 記錄持續時間
}
```

---

### 第 4 步：報告指標
要使指標有用，您需要將它們報告到某個地方。Dropwizard Metrics 支持各種報告器，例如控制台、JMX 或 Graphite。以下是一個每 10 秒鐘記錄一次指標的控制台報告器示例：

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // 每 10 秒鐘報告一次
```

在生產環境中，請考慮與 Graphite 等系統集成或通過 JMX 公開指標。

---

### 第 5 步：與框架集成（可選）
如果您使用像 Jersey 這樣的 Web 框架，可以使用 `metrics-jersey` 模塊來自動儀器化您的端點。此外，註釋如 `@Timed` 或 `@Counted` 可以簡化指標收集：

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "Hello, world!";
    }
}
```

添加 `metrics-jersey` 依賴項並將其與您的 Jersey 應用程序配置以啟用此功能。

---

### 最佳實踐
- **命名約定**：使用分層命名方案以提高清晰度（例如，`com.example.myapp.requests.total`）。
- **性能**：對指標的數量和頻率要謹慎，因為過多的收集可能會影響性能。
- **文檔**：參閱 [Dropwizard Metrics 文檔](https://metrics.dropwizard.io/) 以獲取最新的示例和高級功能。

---

### 示例：將所有內容結合起來
以下是結合多個概念的簡單示例：

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // 創建一個計數器
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // 創建一個計時器
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // 模擬工作
        context.stop();

        // 開始一個控制台報告器
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // 保持程序運行以查看報告
        Thread.sleep(5000);
    }
}
```

此代碼跟蹤一個計數器和一個計時器，每秒鐘將結果報告到控制台。

---

### 最後說明
`com.yammer.metrics` 圖書館已經演變為 Dropwizard Metrics，因此始終使用 `io.dropwizard.metrics` 組中的最新版本。如果您開始一個新項目，您也可以探索現代替代方案如 Micrometer，但 Dropwizard Metrics 仍然是許多 Java 應用程序的堅實選擇。有關更多詳細信息，請查看官方文檔！