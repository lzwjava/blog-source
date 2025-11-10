---
audio: false
generated: true
lang: ja
layout: post
title: Spring BootにおけるSpring Cloud Sleuthのマスタリング
translated: true
type: note
---

Spring Cloud Sleuthは、Springアプリケーションに分散トレーシング機能を追加するための強力なツールです。マイクロサービスアーキテクチャで複数のサービスにまたがるリクエストを追跡するのに特に有用ですが、単一（モノリス）アプリケーションにおいても、ログ相関とデバッグを強化することで大きなメリットを提供します。

このガイドでは、Baeldungのアプローチから洞察を得ながら、単一のSpring Bootアプリケーション内でSpring Cloud Sleuthを使用する方法について包括的な概要を説明します。

## 1\. Spring Cloud Sleuthとは？

その中核として、Spring Cloud SleuthはSpringアプリケーションをインスツルメントし、トレーシング情報をログに自動的に追加し、単一アプリケーション内の異なるコンポーネントやスレッド間で伝播させます。この機能にはOpenZipkinのBraveライブラリを活用しています。

**主要な用語:**

  * **トレース:** アプリケーションを流れる単一のリクエストまたはジョブを表します。各トレースには一意の`traceId`があります。リクエストのエンドツーエンドの旅と考えてください。
  * **スパン:** トレース内の論理的な作業単位を表します。トレースは複数のスパンで構成され、木構造を形成します。各スパンには一意の`spanId`があります。例えば、着信HTTPリクエストが1つのスパンであり、そのリクエスト内のメソッド呼び出しが別の（子）スパンになる可能性があります。
  * **MDC (Mapped Diagnostic Context):** SleuthはSlf4JのMDCと統合し、`traceId`と`spanId`をログメッセージに注入します。これにより、特定のリクエストに関連するログを簡単にフィルタリングおよび相関させることができます。

## 2\. 単一アプリケーションでSleuthを使用する理由

モノリスであっても、リクエストには多くの場合、複数のレイヤー、非同期操作、および異なるスレッドが関与します。単一のリクエストに対するログメッセージを手動で相関させることは、退屈でエラーが発生しやすいものです。Sleuthは以下を自動化することでこれを解決します:

  * **デバッグの簡素化:** すべてのログエントリに`traceId`と`spanId`を追加することで、単一のユーザーリクエストに関連するすべてを簡単にフィルタリングして確認できます。たとえそれが単一アプリケーション内の複数のメソッド、サービス、またはスレッドを横断する場合でも。
  * **観測可能性の向上:** リクエストの流れと、潜在的なボトルネックや問題が発生する可能性のある場所をより明確に把握できます。
  * **一貫性:** コードベースのすべての部分で手動の努力を必要とせずに、ログ相関に対する一貫したアプローチを保証します。

## 3\. はじめに: セットアップと構成

### 3.1. プロジェクトセットアップ (Maven)

始めるには、新しいSpring Bootプロジェクトを作成し（Spring Initializrを使用できます）、`pom.xml`に`spring-cloud-starter-sleuth`依存関係を追加します:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**重要:** 互換性のあるSpring BootおよびSpring Cloudのバージョンを使用していることを確認してください。Spring Cloudの依存関係は、通常、Bill of Materials (BOM)を使用して管理されます。

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

`${spring-cloud.version}`を適切なリリーストレインのバージョン（例: `2021.0.1`, `2022.0.0`）に置き換えてください。

### 3.2. アプリケーション名

`application.properties`または`application.yml`ファイルでアプリケーション名を設定することを強くお勧めします。この名前はログに表示され、特に後で分散システムに移行した場合にログのソースを識別するのに役立ちます。

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. ロギングパターン

Spring Cloud Sleuthは、`traceId`と`spanId`を含めるようにデフォルトのロギングパターンを自動的に変更します。Sleuthを使用した典型的なログ出力は次のようになります:

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

ここで:

  * `my-single-app`: `spring.application.name`です。
  * `a1b2c3d4e5f6a7b8`: `traceId`です。
  * `a1b2c3d4e5f6a7b8` (2番目): `spanId`です（ルートスパンの場合、traceIdとspanIdはしばしば同じです）。
  * `false`: スパンがエクスポート可能かどうかを示します（trueは、Zipkinなどのトレーシングコレクタに送信されることを意味します）。

カスタムロギングパターンがある場合は、`%X{traceId}`と`%X{spanId}`を使用して（Logbackの場合）、明示的に`traceId`と`spanId`を追加する必要があります。

`logback-spring.xml`でのカスタムLogbackパターンの例:

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4\. 単一アプリケーションでのSleuthの動作

`spring-cloud-starter-sleuth`依存関係がクラスパス上にあると、Spring Bootの自動構成が引き継ぎます。

### 4.1. 自動インスツルメンテーション

Sleuthは一般的なSpringコンポーネントと通信チャネルを自動的にインスツルメントします:

  * **Servlet Filter:** コントローラへの着信HTTPリクエスト用。
  * **RestTemplate:** `RestTemplate`を使用して行われる発信HTTP呼び出し用（Sleuthが自動インスツルメントするには、Bean管理の`RestTemplate`を使用していることを確認してください）。
  * **Scheduled Actions:** `@Scheduled`メソッド用。
  * **Message Channels:** Spring IntegrationおよびSpring Cloud Stream用。
  * **Asynchronous Methods:** `@Async`メソッド用（トレース/スパンコンテキストがスレッド間で伝播されることを保証します）。

### 4.2. 単純なWebリクエストの例

単純なRESTコントローラを持つSpring Bootアプリケーションを考えてみます:

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

`http://localhost:8080/`にアクセスすると、次のようなログメッセージが表示されます:

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

`traceId`と`spanId`が自動的に追加されていることに注意してください。

### 4.3. メソッド間でのコンテキストの伝播（同じスパン）

リクエストが単一アプリケーション内の複数のメソッドを流れ、これらのメソッドを*同じスパン*の一部にしたい場合、Sleuthはこれを自動的に処理します。

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
        Thread.sleep(100); // 何らかの作業をシミュレート
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

`/same-span-example`のログは、コントローラとサービスの両方のメソッドで同じ`traceId`と`spanId`を示します:

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. 手動での新しいスパンの作成

アプリケーション内の明確な作業単位に対して、同じトレースの一部であっても新しいスパンを作成したい場合があります。これにより、より細かい粒度での追跡とタイミングが可能になります。Spring Cloud Sleuthはこのために`Tracer` APIを提供します。

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
    private Tracer tracer; // Brave Tracerを注入

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // 説明的な名前で新しいスパンを作成
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // 新しいスパン内で何らかの作業をシミュレート
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // 常にスパンを終了
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

`/new-span-example`のログは、トレースIDが同じままであるが、"custom-internal-work"に対して新しい`spanId`が表示されることを示します:

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

`custom-internal-work`セクション内で`spanId`が`8a9b0c1d2e3f4a5b`に変わり、その後元に戻ることに注意してください。

### 4.5. 非同期処理

SleuthはSpringの`@Async`アノテーションとシームレスに統合し、トレースコンテキストをスレッド境界を越えて伝播させます。

まず、メインアプリケーションクラスで非同期処理を有効にします:

```java
@SpringBootApplication
@EnableAsync // 非同期実行を有効化
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

次に、非同期サービスを作成します:

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
        Thread.sleep(500); // 長時間実行されるタスクをシミュレート
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

ログは、非同期メソッドに対して同じ`traceId`だが異なる`spanId`を示します。これは、新しいスレッドで実行され、新しい作業単位を表すためです:

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... しばらくして ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

`traceId`は同じままですが、非同期メソッドの`spanId`が変わり、スレッド名も非同期エグゼキュータを反映していることに注意してください。

### 4.6. `@SpanName`を使用したスパン名のカスタマイズ

`@SpanName`アノテーションを使用して、自動生成されるスパンにより意味のある名前を付けることができます。

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // カスタムスパン名
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... コントローラまたは別のサービスで ...
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

ログはカスタムスパン名を反映します:

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5\. Zipkinとの統合（オプションだが推奨）

このガイドは単一アプリケーションに焦点を当てていますが、Sleuthの真の力は、Zipkinのような分散トレーシングシステムと統合したときに発揮されます。Zipkinは、Sleuthによってエクスポートされたトレースとスパンデータを収集し、リクエストの流れとタイミングを視覚化するUIを提供します。

Zipkinと統合するには、`spring-cloud-starter-zipkin`依存関係を追加します:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

デフォルトでは、Sleuthはトレースを`http://localhost:9411`で実行されているZipkinコレクタに送信しようとします。これは`application.properties`で構成できます:

```properties
spring.zipkin.base-url=http://localhost:9411
```

DockerでZipkinサーバーを簡単に実行できます:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Zipkinが実行されると、単一のSpring Bootアプリケーションは自動的にそのトレースデータを送信し、`http://localhost:9411/`でトレースを表示できます。

## 6\. サンプリング

デフォルトでは、Sleuthはデータでトレーシングシステムが圧倒されるのを避けるためにサンプリング戦略を適用します。通常、リクエストの一定の割合をサンプリングします。サンプリングレートは`application.properties`で構成できます:

```properties
# リクエストの100%をサンプリング
spring.sleuth.sampler.probability=1.0
```

`1.0`の値はすべてのリクエストがトレースされることを意味し、`0.1`は10%がトレースされることを意味します。

## 7\. 結論

Spring Cloud Sleuthは、単一アプリケーションであっても、`traceId`と`spanId`をログメッセージに自動的に注入することで、ロギングとデバッグを大幅に強化します。これにより、単一のリクエストの実行フローを、異なるメソッドやスレッドを横断する場合でも簡単に追跡できます。トレースとスパンの核心概念を理解し、Sleuthの自動インスツルメンテーションまたは手動スパン作成を利用することで、モノリスアプリケーションに対するはるかに優れた観測可能性を得ることができます。Zipkinとの統合は、アプリケーションの動作を視覚化および分析する可能性をさらに解き放ちます。