---
audio: false
generated: true
lang: hant
layout: post
title: Java 應用程式指標
translated: true
type: note
---

`com.yammer.metrics` 函式庫最初由 Yammer 開發，現已成為 **Dropwizard Metrics** 函式庫的一部分。它提供了一種穩健的方式來收集和報告 Java 應用程式的指標，協助您監控效能面向，例如請求計數、回應時間等。以下是如何有效使用它的指南。

---

### 步驟 1：添加依賴項
由於 `com.yammer.metrics` 已演進為 Dropwizard Metrics，您應使用 Dropwizard Metrics 函式庫。若您使用 Maven，請將以下依賴項添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- 請使用可用的最新版本 -->
</dependency>
```

根據您的需求，您可能還需要其他模組，例如：
- `metrics-jvm` 用於 JVM 相關指標。
- `metrics-httpclient` 用於 HTTP 客戶端指標。
- `metrics-jersey` 用於與 Jersey web 框架整合。

請查閱 [Dropwizard Metrics 文件](https://metrics.dropwizard.io/) 以獲取最新版本和可用模組。

---

### 步驟 2：建立指標註冊表
`MetricRegistry` 是儲存所有指標的中心位置。您通常會為應用程式建立一個實例：

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### 步驟 3：使用不同類型的指標
Dropwizard Metrics 支援多種指標類型，每種適用於不同的監控需求：

#### **計數器**
計數器用於追蹤可增加或減少的數值（例如，已處理的請求數量）。

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 增加 1
counter.inc(5); // 增加 5
counter.dec();  // 減少 1
```

#### **測量器**
測量器提供特定時刻的數值快照（例如，當前佇列大小）。您可以透過實作 `Gauge` 介面來定義測量器：

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
直方圖追蹤數值的統計分佈（例如，請求大小）：

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // 記錄一個數值
```

#### **計量器**
計量器測量事件的速率（例如，每秒請求數）：

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // 記錄一個事件
```

#### **計時器**
計時器同時測量事件的速率和持續時間（例如，請求處理時間）：

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

### 步驟 4：報告指標
為了使指標有用，您需要將它們報告到某處。Dropwizard Metrics 支援多種報告器，例如控制台、JMX 或 Graphite。以下是一個控制台報告器的範例，每 10 秒記錄一次指標：

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // 每 10 秒報告一次
```

對於生產環境使用，請考慮與 Graphite 等系統整合，或透過 JMX 公開指標。

---

### 步驟 5：與框架整合（可選）
如果您使用像 Jersey 這樣的 web 框架，可以使用 `metrics-jersey` 模組自動檢測您的端點。此外，像 `@Timed` 或 `@Counted` 這樣的註解可以簡化指標收集：

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

添加 `metrics-jersey` 依賴項並將其與您的 Jersey 應用程式配置以啟用此功能。

---

### 最佳實踐
- **命名慣例**：使用層次化命名方案以確保清晰度（例如 `com.example.myapp.requests.total`）。
- **效能**：注意指標的數量和頻率，因為過度收集可能會影響效能。
- **文件**：請參閱 [Dropwizard Metrics 文件](https://metrics.dropwizard.io/) 以獲取最新範例和進階功能。

---

### 範例：整合所有概念
以下是一個結合多個概念的簡單範例：

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // 建立計數器
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // 建立計時器
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // 模擬工作
        context.stop();

        // 啟動控制台報告器
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // 保持程式運行以查看報告
        Thread.sleep(5000);
    }
}
```

此程式碼追蹤一個計數器和一個計時器，每秒將結果報告到控制台。

---

### 最後說明
`com.yammer.metrics` 函式庫已演進為 Dropwizard Metrics，因此請始終使用 `io.dropwizard.metrics` 群組的最新版本。如果您正在開始新專案，也可以探索現代替代方案如 Micrometer，但 Dropwizard Metrics 對於許多 Java 應用程式來說仍然是可靠的選擇。更多詳細資訊，請查閱官方文件！