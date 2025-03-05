---
audio: true
generated: true
lang: zh
layout: post
title: 应用程序指标
translated: true
---

`com.yammer.metrics` 库最初由 Yammer 开发，现在是 **Dropwizard Metrics** 库的一部分。它提供了一种收集和报告 Java 应用程序指标的强大方式，帮助你监控性能方面的指标，如请求计数、响应时间等。以下是如何有效使用它的指南。

---

### 第 1 步：添加依赖
由于 `com.yammer.metrics` 已经演变为 Dropwizard Metrics，你应该使用 Dropwizard Metrics 库。如果你使用 Maven，请将以下依赖项添加到你的 `pom.xml`：

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- 使用最新可用版本 -->
</dependency>
```

根据你的需求，你可能还需要其他模块，例如：
- `metrics-jvm` 用于 JVM 相关的指标。
- `metrics-httpclient` 用于 HTTP 客户端指标。
- `metrics-jersey` 用于与 Jersey Web 框架集成。

请查看 [Dropwizard Metrics 文档](https://metrics.dropwizard.io/) 以获取最新版本和可用模块。

---

### 第 2 步：创建指标注册表
`MetricRegistry` 是存储所有指标的中央位置。你通常为你的应用程序创建一个实例：

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### 第 3 步：使用不同类型的指标
Dropwizard Metrics 支持多种类型的指标，每种指标都适用于不同的监控需求：

#### **计数器**
计数器用于跟踪可以增加或减少的值（例如，处理的请求数量）。

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 增加 1
counter.inc(5); // 增加 5
counter.dec();  // 减少 1
```

#### **仪表盘**
仪表盘提供特定时刻的值快照（例如，当前队列大小）。你可以通过实现 `Gauge` 接口来定义一个仪表盘：

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // 替换为你的逻辑
    }
});
```

#### **直方图**
直方图跟踪值的统计分布（例如，请求大小）：

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // 记录一个值
```

#### **计量器**
计量器测量事件的速率（例如，每秒请求数）：

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // 记录一个事件
```

#### **计时器**
计时器测量事件的速率和持续时间（例如，请求处理时间）：

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // 模拟一些工作
    Thread.sleep(100);
} finally {
    context.stop(); // 记录持续时间
}
```

---

### 第 4 步：报告指标
为了使指标有用，你需要将它们报告给某个地方。Dropwizard Metrics 支持各种报告器，例如控制台、JMX 或 Graphite。以下是一个每 10 秒记录一次指标的控制台报告器示例：

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // 每 10 秒报告一次
```

对于生产使用，请考虑与 Graphite 等系统集成或通过 JMX 公开指标。

---

### 第 5 步：与框架集成（可选）
如果你使用像 Jersey 这样的 Web 框架，可以使用 `metrics-jersey` 模块自动对你的端点进行仪表化。此外，注解如 `@Timed` 或 `@Counted` 可以简化指标收集：

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

添加 `metrics-jersey` 依赖项并将其与你的 Jersey 应用程序配置以启用此功能。

---

### 最佳实践
- **命名约定**：使用分层命名方案以便于理解（例如，`com.example.myapp.requests.total`）。
- **性能**：注意指标的数量和频率，因为过多的收集可能会影响性能。
- **文档**：请参考 [Dropwizard Metrics 文档](https://metrics.dropwizard.io/) 以获取最新的示例和高级功能。

---

### 示例：将所有内容结合起来
以下是结合多个概念的简单示例：

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // 创建一个计数器
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // 创建一个计时器
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // 模拟工作
        context.stop();

        // 启动一个控制台报告器
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // 保持程序运行以查看报告
        Thread.sleep(5000);
    }
}
```

此代码跟踪一个计数器和一个计时器，每秒将结果报告给控制台。

---

### 最后说明
`com.yammer.metrics` 库已经演变为 Dropwizard Metrics，因此始终使用 `io.dropwizard.metrics` 组中的最新版本。如果你开始一个新项目，你也可以探索现代替代方案，如 Micrometer，但 Dropwizard Metrics 对许多 Java 应用程序来说仍然是一个坚实的选择。有关更多详细信息，请查看官方文档！