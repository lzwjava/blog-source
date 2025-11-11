---
audio: false
generated: true
lang: ja
layout: post
title: Javaアプリケーションメトリクス
translated: true
type: note
---

`com.yammer.metrics`ライブラリは、元々Yammerによって開発され、現在は**Dropwizard Metrics**ライブラリの一部となっています。Javaアプリケーションのメトリクスを収集・レポートする強力な方法を提供し、リクエスト数、レスポンス時間などのパフォーマンス側面を監視するのに役立ちます。以下はその効果的な使用方法に関するガイドです。

---

### ステップ1: 依存関係の追加
`com.yammer.metrics`はDropwizard Metricsに進化したため、Dropwizard Metricsライブラリを使用すべきです。Mavenを使用している場合は、`pom.xml`に以下の依存関係を追加してください：

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- 利用可能な最新バージョンを使用してください -->
</dependency>
```

必要に応じて、以下のような追加モジュールも検討してください：
- JVM関連メトリクスのための `metrics-jvm`
- HTTPクライアントメトリクスのための `metrics-httpclient`
- Jerseyウェブフレームワークとの統合のための `metrics-jersey`

最新バージョンと利用可能なモジュールについては、[Dropwizard Metricsドキュメント](https://metrics.dropwizard.io/)を確認してください。

---

### ステップ2: メトリクスレジストリの作成
`MetricRegistry`は、すべてのメトリクスが保存される中心的な場所です。通常、アプリケーションに対して1つのインスタンスを作成します：

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### ステップ3: 様々なタイプのメトリクスを使用する
Dropwizard Metricsは、異なる監視ニーズに適したいくつかのタイプのメトリクスをサポートしています：

#### **カウンター**
カウンターは増減する値を追跡するために使用されます（例：処理されたリクエスト数）。

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 1つ増加
counter.inc(5); // 5つ増加
counter.dec();  // 1つ減少
```

#### **ゲージ**
ゲージは特定の瞬間の値のスナップショットを提供します（例：現在のキューサイズ）。`Gauge`インターフェースを実装してゲージを定義します：

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // 実際のロジックに置き換えてください
    }
});
```

#### **ヒストグラム**
ヒストグラムは値の統計的分布を追跡します（例：リクエストサイズ）：

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // 値を記録
```

#### **メーター**
メーターはイベントのレートを測定します（例：1秒あたりのリクエスト数）：

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // イベントを記録
```

#### **タイマー**
タイマーはイベントのレートと期間の両方を測定します（例：リクエスト処理時間）：

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // 何らかの作業をシミュレート
    Thread.sleep(100);
} finally {
    context.stop(); // 期間を記録
}
```

---

### ステップ4: メトリクスのレポート
メトリクスを有用なものにするには、どこかにレポートする必要があります。Dropwizard Metricsは、コンソール、JMX、Graphiteなどの様々なレポーターをサポートしています。以下は、10秒ごとにメトリクスをログ出力するコンソールレポーターの例です：

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // 10秒ごとにレポート
```

本番環境での使用では、Graphiteのようなシステムとの統合や、JMXを介したメトリクスの公開を検討してください。

---

### ステップ5: フレームワークとの統合（オプション）
Jerseyのようなウェブフレームワークを使用している場合は、`metrics-jersey`モジュールを使用してエンドポイントを自動的に計装できます。さらに、`@Timed`や`@Counted`のようなアノテーションを使用すると、メトリクス収集を簡素化できます：

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

この機能を有効にするには、`metrics-jersey`依存関係を追加し、Jerseyアプリケーションで設定してください。

---

### ベストプラクティス
- **命名規則**: 明確さのために階層的な命名スキームを使用してください（例：`com.example.myapp.requests.total`）
- **パフォーマンス**: メトリクスの数と頻度には注意してください。過剰な収集はパフォーマンスに影響を与える可能性があります
- **ドキュメント**: 最新の例と高度な機能については、[Dropwizard Metricsドキュメント](https://metrics.dropwizard.io/)を参照してください

---

### 例：すべてを組み合わせる
以下は、いくつかの概念を組み合わせた簡単な例です：

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // カウンターを作成
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // タイマーを作成
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // 作業をシミュレート
        context.stop();

        // コンソールレポーターを開始
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // レポートを確認するためにプログラムを実行し続ける
        Thread.sleep(5000);
    }
}
```

このコードはカウンターとタイマーを追跡し、1秒ごとに結果をコンソールにレポートします。

---

### 最終的な注意点
`com.yammer.metrics`ライブラリはDropwizard Metricsに進化したため、常に`io.dropwizard.metrics`グループの最新バージョンを使用してください。新しいプロジェクトを開始する場合は、Micrometerのような現代的な代替手段も検討できますが、Dropwizard Metricsは多くのJavaアプリケーションにとって堅実な選択肢であり続けています。詳細については、公式ドキュメントを確認してください！