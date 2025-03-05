---
audio: true
generated: true
lang: ja
layout: post
title: アプリケーションのメトリクスのJava
translated: true
---

`com.yammer.metrics` ライブラリは、元々 Yammer によって開発され、現在は **Dropwizard Metrics** ライブラリの一部となっています。これは、Java でアプリケーションのメトリクスを収集および報告するための強力な方法を提供し、リクエスト数、応答時間などのパフォーマンスの側面を監視するのに役立ちます。以下に、効果的に使用するためのガイドを示します。

---

### ステップ 1: 依存関係を追加
`com.yammer.metrics` は Dropwizard Metrics に進化しましたので、Dropwizard Metrics ライブラリを使用する必要があります。Maven を使用している場合は、以下の依存関係を `pom.xml` に追加してください：

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- 利用可能な最新バージョンを使用 -->
</dependency>
```

必要に応じて、以下のような追加モジュールも希望するかもしれません：
- `metrics-jvm` は JVM 関連のメトリクスのため。
- `metrics-httpclient` は HTTP クライアントのメトリクスのため。
- `metrics-jersey` は Jersey ウェブフレームワークとの統合のため。

最新バージョンと利用可能なモジュールについては、[Dropwizard Metrics ドキュメント](https://metrics.dropwizard.io/) を確認してください。

---

### ステップ 2: メトリクスレジストリを作成
`MetricRegistry` は、すべてのメトリクスが保存される中央の場所です。通常、アプリケーションに対して 1 つのインスタンスを作成します：

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### ステップ 3: 異なる種類のメトリクスを使用
Dropwizard Metrics は、異なる監視ニーズに適した複数のメトリクスタイプをサポートしています：

#### **カウンター**
カウンターは、増加または減少する値を追跡するために使用されます（例：処理されたリクエスト数）。

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 1 増加
counter.inc(5); // 5 増加
counter.dec();  // 1 減少
```

#### **ゲージ**
ゲージは、特定の瞬間の値のスナップショットを提供します（例：現在のキューのサイズ）。ゲージは `Gauge` インターフェースを実装することで定義します：

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // 独自のロジックに置き換え
    }
});
```

#### **ヒストグラム**
ヒストグラムは、値の統計的な分布を追跡します（例：リクエストサイズ）。

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // 値を記録
```

#### **メーター**
メーターは、イベントのレートを測定します（例：秒あたりのリクエスト数）。

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // イベントを記録
```

#### **タイマー**
タイマーは、イベントのレートと期間を測定します（例：リクエスト処理時間）。

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // 作業をシミュレート
    Thread.sleep(100);
} finally {
    context.stop(); // 期間を記録
}
```

---

### ステップ 4: メトリクスを報告
メトリクスを有用にするためには、どこかに報告する必要があります。Dropwizard Metrics は、コンソール、JMX、Graphite などのさまざまなレポーターをサポートしています。以下は、10 秒ごとにメトリクスをログに記録するコンソールレポーターの例です：

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // 10 秒ごとに報告
```

本番環境では、Graphite と統合するか、JMX を通じてメトリクスを公開することを検討してください。

---

### ステップ 5: フレームワークとの統合（オプション）
Jersey などのウェブフレームワークを使用している場合、`metrics-jersey` モジュールを使用してエンドポイントを自動的に計器化できます。さらに、`@Timed` や `@Counted` などのアノテーションを使用してメトリクスの収集を簡素化できます：

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

`metrics-jersey` 依存関係を追加し、Jersey アプリケーションで設定することで、この機能を有効にします。

---

### ベストプラクティス
- **命名規則**: 明確さのために階層的な命名スキームを使用します（例：`com.example.myapp.requests.total`）。
- **パフォーマンス**: メトリクスの数と頻度に注意してください。過度な収集はパフォーマンスに影響を与える可能性があります。
- **ドキュメント**: 最新の例と高度な機能については、[Dropwizard Metrics ドキュメント](https://metrics.dropwizard.io/) を参考にしてください。

---

### 例: 全てをまとめる
いくつかの概念を組み合わせた簡単な例を以下に示します：

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

        // レポートを表示するためにプログラムを実行中に保持
        Thread.sleep(5000);
    }
}
```

このコードは、カウンターとタイマーを追跡し、1 秒ごとにコンソールに結果を報告します。

---

### 最終メモ
`com.yammer.metrics` ライブラリは Dropwizard Metrics に進化しましたので、常に `io.dropwizard.metrics` グループから最新バージョンを使用してください。新しいプロジェクトを開始する場合は、Micrometer などの現代的な代替手段も検討してくださいが、Dropwizard Metrics は多くの Java アプリケーションにとって依然として堅実な選択肢です。詳細については、公式ドキュメントを確認してください！