---
audio: false
generated: true
lang: ja
layout: post
title: マイクロメーターガイド：ツールと可観測性
translated: true
type: note
---

この包括的なガイドでは、**マイクロメータ（測定工具）**と**Micrometer（Javaアプリケーション、特にSpring Boot向けのオブザーバビリティファサード）のトレーシングソリューション**という2つの異なるトピックについて説明します。

それぞれ分解してみましょう：

-----

## 第1部：マイクロメータ（測定工具）に関する包括的ガイド

マイクロメータ（micrometer screw gaugeとも呼ばれる）は、高精度な測定を実現する精密測定器具で、通常は1/1000インチや1/100ミリメートル単位の微小な距離の測定に使用されます。精密な寸法が重要なエンジニアリング、機械加工、製造、科学分野で広く使用されています。

### 1. マイクロメータとは？

基本的に、マイクロメータは精密に加工されたネジ機構を利用して回転運動を直線運動に変換します。これにより、固定アンビルと可動スピンドルの間にワークを挟み込むことで、微調整と正確な寸法測定が可能になります。

### 2. マイクロメータの主要コンポーネント：

  * **フレーム:** すべてのコンポーネントを保持するC字形の本体。安定性を提供し、熱膨張による誤差を避けるために注意して扱う必要があります。
  * **アンビル:** ワークが接触する固定測定面。
  * **スピンドル:** シンブルを回転させるとアンビルに近づいたり離れたりする可動測定面。
  * **スリーブ（バレル）:** 主目盛りを表示する固定部分で、整数値と半目盛り（インチまたはミリメートル単位）を表示します。
  * **シンブル:** スピンドルを動かす回転部分で、より精密な読み取りのための細かい目盛りがあります。
  * **ラチェットストップ:** シンブルの端にあり、適切な測定圧力がかかるとスリップすることで一貫した測定圧力を確保し、過締めやワークの変形を防ぎます。
  * **ロックナット（ロックレバー）:** 測定後にスピンドルを固定し、偶発的な移動を防ぎ読み取り値を保持するために使用します。

### 3. マイクロメータの種類：

マイクロメータには様々な種類があり、それぞれ特定の測定タスク向けに設計されています：

  * **外側マイクロメータ（外部マイクロメータ）:** 最も一般的なタイプで、シャフトの直径やプレートの厚さなどの外部寸法の測定に使用されます。
  * **内側マイクロメータ（内部マイクロメータ）:** ボアや穴の直径などの内部寸法の測定に使用されます。チューブ式やジョー式など、異なる設計を持つことが多いです。
  * **デプスマイクロメータ:** 穴、スロット、段差の深さを測定するために使用されます。
  * **ねじ山マイクロメータ:** ねじ山の有効径を測定するために設計されています。
  * **ボールマイクロメータ:** 曲面やチューブ壁などの特定の形状の厚さを測定するためのボール形状のアンビル/スピンドルを備えています。
  * **ディスクマイクロメータ:** 薄い材料、紙、歯車の歯などを測定するための平らなディスク形状の測定面を持っています。
  * **デジタルマイクロメータ:** 直接デジタル表示する電子ディスプレイを備えており、視差誤差を排除し読み取りを容易にします。
  * **アナログマイクロメータ:** スリーブとシンブルの目盛りを手動で読み取る必要があります。
  * **バーニアマイクロメータ:** さらに高い精度を実現するための追加のバーニア目盛りを含み、シンブルの主目盛りを超えた読み取りを可能にします。

### 4. マイクロメータの読み方（アナログ/インチ例）：

特定の読み方はインチ（inch）とメートル法（millimeter）、アナログ/デジタルで異なりますが、アナログマイクロメータの一般的な原理は以下の通りです：

1.  **スリーブ目盛り（主目盛り）を読む：**
      * **整数インチ:** 見えている最大の整数インチの目盛りを確認します。
      * **1/10インチ (0.100")：** スリーブの番号付き線はそれぞれ0.100インチを表します。
      * **25/1000インチ (0.025")：** 1/10インチ目盛り間の番号なし線はそれぞれ0.025インチを表します。
2.  **シンブル目盛りを読む：**
      * シンブルには25の目盛りがあり、各目盛りは0.001インチを表します。
      * スリーブの基準線と一致するシンブルの線を読み取ります。
3.  **読み取り値を合算する：** スリーブからの値（整数インチ、1/10インチ、25/1000インチ）とシンブルからの値（1000分の1インチ）を加算して最終的な測定値を得ます。

**例（インチ）：**

  * スリーブ：
      * 「1」が見える（1.000インチ）
      * 「1」の後に3本の線（3 x 0.100" = 0.300"）
      * 主線の下に2本の線（2 x 0.025" = 0.050"）
      * スリーブからの合計：1.000 + 0.300 + 0.050 = 1.350"
  * シンブル：
      * シンブルの15番目の目盛りが基準線と一致（0.015"）
  * **合計読み取り値：** 1.350" + 0.015" = **1.365"**

### 5. 適切な使用方法とベストプラクティス：

  * **清潔さ:** 測定面（アンビルとスピンドル）が常に清潔で、ほこり、油、異物がないことを確認してください。
  * **ゼロ調整:** 使用前には常にマイクロメータを「ゼロ調整」してください。ラチェットストップを使用して測定面が軽く触れるまで静かに閉じます。読み取り値は0.000（または開始範囲、例：25-50mm）である必要があります。そうでない場合は、マイクロメータをゼロ誤差に対して調整してください。デジタルマイクロメータには通常リセットボタンがあります。
  * **温度:** 特に大型のマイクロメータでは、体温による熱膨張が精度に影響する可能性があるため、断熱フレームを持つ部分を把持するか手袋を着用してください。工具とワークの両方が室温に達するのを待ちます。
  * **一貫した圧力:** 常にラチェットストップを使用して、一貫した適切な測定圧力を適用してください。過度の締め付けはワークやマイクロメータを変形させる可能性があります。
  * **ワークの配置:** ワークをアンビルとスピンドルの間に直角に配置し、歪んだ読み取りを避けてください。
  * **複数回の測定:** 重要な寸法については、ワークの異なるポイントで複数回測定し、ばらつきを考慮します。
  * **保管:** マイクロメータは保護ケースに保管して損傷を防ぎます。
  * **校正:** 精度を確保するために、既知の標準（ゲージブロックなど）に対して定期的にチェックと校正を行います。

-----

## 第2部：Spring Javaプロジェクト向けトレーシングソリューションとしてのMicrometer

Spring Javaプロジェクトの文脈では、「Micrometer」は、**アプリケーションオブザーバビリティファサード**を指し、JVMベースのアプリケーションを計装するためのベンダー中立のAPIを提供します。これにより、メトリクス、ロギング、**分散トレーシング**を含む様々なテレメトリデータを収集およびエクスポートできます。

Micrometer TracingはSpring Cloud Sleuthの後継であり、複数のサービスにまたがるリクエストを追跡することで、複雑な分散システムの可視性を提供するように設計されています。

### 1. 分散トレーシングとは？

マイクロサービスアーキテクチャでは、単一のユーザーリクエストが複数のサービスを通過することがよくあります。分散トレーシングにより、以下が可能になります：

  * **フローの追跡:** リクエストがシステム内でたどる完全なパスを確認します。
  * **ボトルネックの特定:** どのサービスまたは操作が遅延の原因であるかを特定します。
  * **依存関係の理解:** 異なるサービス間の相互作用を可視化します。
  * **デバッグの簡素化:** ログを特定のリクエストと関連付け、トラブルシューティングを大幅に容易にします。

分散トレースは**スパン**で構成されます。**スパン**は、トレース内の単一の操作または作業単位（例：サービスへのHTTPリクエスト、データベースクエリ、メソッド実行）を表します。スパンには一意のID、開始時間と終了時間があり、追加のメタデータのためのタグ（キーと値のペア）やイベントを含めることができます。スパンは親子関係で階層的に編成され、トレースを形成します。

### 2. Spring Boot 3.x+におけるMicrometer Tracing

Spring Boot 3.x+は、MicrometerのObservation APIおよびMicrometer Tracingと深く統合されており、分散トレーシングの実装が大幅に容易になります。

#### 2.1. 核心概念：

  * **Observation API:** コードを計装するためのMicrometerの統一API。単一の計装ポイントからメトリクス、トレース、ログを生成できます。
  * **Micrometer Tracing:** OpenTelemetryやOpenZipkin Braveなどの人気のあるトレーサーライブラリに対するファサード。スパンのライフサイクル、コンテキスト伝播、トレーシングバックエンドへのレポートを処理します。
  * **トレーサーブリッジ:** Micrometer Tracingは、そのAPIを特定のトレーシング実装（例：OpenTelemetry用の`micrometer-tracing-bridge-otel`、OpenZipkin Brave用の`micrometer-tracing-bridge-brave`）に接続する「ブリッジ」を提供します。
  * **レポーター/エクスポーター:** これらのコンポーネントは、収集されたトレースデータをトレーシングバックエンド（例：Zipkin、Jaeger、Grafana Tempo）に送信します。

#### 2.2. Spring Boot JavaプロジェクトでのMicrometer Tracingセットアップ：

ステップバイステップガイド：

**ステップ1: 依存関係の追加**

オブザーバビリティ機能には`spring-boot-starter-actuator`、選択したトレーシングバックエンド用のMicrometer Tracingブリッジ、およびレポーター/エクスポーターが必要です。

**OpenTelemetryとZipkinを使用した例（一般的な選択肢）：**

`pom.xml`（Maven）内：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-observation</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-otel</artifactId>
    </dependency>

    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-zipkin</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
</dependencies>
```

**ステップ2: トレーシングプロパティの設定**

`application.properties`または`application.yml`で、トレーシングの動作を設定できます。

```properties
# トレーシングを有効化（通常、actuatorとトレーシング依存関係があるとデフォルトでtrue）
management.tracing.enabled=true

# サンプリング確率を設定（1.0 = 100%のリクエストがトレースされる）
# デフォルトは0.1（10%）であることが多い。開発/テストでは1.0に設定
management.tracing.sampling.probability=1.0

# ZipkinベースURLを設定（Zipkinを使用する場合）
spring.zipkin.base-url=http://localhost:9411
```

**ステップ3: トレーシングバックエンドの実行（例：Zipkin）**

トレースを収集および可視化するためのトレーシングサーバーが必要です。Zipkinはローカル開発で一般的な選択肢です。

Docker経由でZipkinを実行できます：

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

実行後、Zipkin UIに`http://localhost:9411`でアクセスできます。

**ステップ4: 自動計装（Spring Bootの魔法！）**

Spring Bootの多くの一般的なコンポーネント（`RestController`エンドポイント、`RestTemplate`、`WebClient`、`JdbcTemplate`、Kafkaリスナー/プロデューサーなど）に対して、Micrometer Tracingは**自動計装**を提供します。これは、基本的なリクエストトレーシングが機能するために、明示的なトレーシングコードを書く必要がしばしばないことを意味します。

Spring Bootは以下を保証します：

  * 受信HTTPリクエストは、新しいトレースを自動的に作成するか、トレースヘッダーが存在する場合は既存のトレースを継続します。
  * 自動設定された`RestTemplateBuilder`、`RestClient.Builder`、または`WebClient.Builder`で作成された送信リクエストは、トレースコンテキストをダウンストリームサービスに伝播します。
  * ログステートメントには自動的に`traceId`と`spanId`が含まれます（ロギングパターンを設定した場合）。

**ロギングパターンの例（`application.properties`内）：**

```properties
logging.pattern.level=%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}] %c{1.}:%M:%L - %m%n
```

このパターンは、`traceId`と`spanId`をログ行に注入し、ログを特定のトレースと簡単に関連付けられるようにします。

**ステップ5: 手動計装（カスタムロジック用）**

自動計装は多くのことをカバーしますが、アプリケーション内の特定のビジネスロジックや重要な操作をトレースしたいことがよくあります。これは以下を使用して行えます：

  * **`@Observed`アノテーション（Spring Boot 3.x+で推奨）：**
    このアノテーションはMicrometer Observation APIの一部であり、観測（メトリクスとトレースの両方を生成できる）を作成するための推奨方法です。

    ```java
    import io.micrometer.observation.annotation.Observed;
    import org.springframework.stereotype.Service;

    @Service
    public class MyService {

        @Observed(name = "myService.processData", contextualName = "processing-data")
        public String processData(String input) {
            // ... ビジネスロジック ...
            System.out.println("Processing data: " + input);
            return "Processed: " + input;
        }
    }
    ```

    `name`属性は観測の名前（メトリクス名およびトレーススパン名になる）を定義します。`contextualName`はトレーシングツールにおけるスパンのより人間が読みやすい名前を提供します。

  * **プログラムによるAPI（より制御が必要な場合）：**
    Spring Bootによって提供される`ObservationRegistry`および`Tracer` Beanを直接使用できます。

    ```java
    import io.micrometer.observation.Observation;
    import io.micrometer.observation.ObservationRegistry;
    import org.springframework.stereotype.Service;

    @Service
    public class AnotherService {

        private final ObservationRegistry observationRegistry;

        public AnotherService(ObservationRegistry observationRegistry) {
            this.observationRegistry = observationRegistry;
        }

        public String performComplexOperation(String id) {
            return Observation.createNotStarted("complex.operation", observationRegistry)
                    .lowCardinalityKeyValue("operation.id", id) // タグを追加
                    .observe(() -> {
                        // ... 複雑なロジック ...
                        try {
                            Thread.sleep(100); // 作業をシミュレート
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        return "Completed complex operation for " + id;
                    });
        }
    }
    ```

    ここで、`observe()`はコードブロックをラップし、`lowCardinalityKeyValue`はスパンにタグを追加します。

### 3. マイクロサービスにおける分散トレーシング：

複数のSpring Bootサービスがある場合、Micrometer Tracingは`RestTemplate`、`WebClient`、および他の計装されたクライアントに対してコンテキスト伝播を自動的に促進します。これは、`traceId`と`spanId`がサービス間でHTTPヘッダー（例：W3C Trace Contextの`traceparent`ヘッダー）を介して渡されることを意味します。

リクエストがダウンストリームサービスに到着すると、Micrometer Tracingはこれらのヘッダーを検出し、既存のトレースを継続し、呼び出し元サービスの親スパンの子である新しいスパンを作成します。これにより、完全なエンドツーエンドのトレースが形成されます。

### 4. トレースの可視化：

アプリケーションが計装され、トレースがZipkin（またはJaeger、Lightstepなど）のようなバックエンドに送信されると、以下が可能になります：

1.  **UIへのアクセス:** トレーシングバックエンドのWeb UI（例：Zipkinの場合は`http://localhost:9411`）にアクセスします。
2.  **トレースの検索:** フィルター（サービス名、スパン名、トレースID）を使用して特定のトレースを見つけます。
3.  **トレース詳細の分析:** トレースをクリックして、そのタイムライン、個々のスパン、それらの期間、タグ、イベントを確認します。
4.  **依存関係グラフ:** ほとんどのトレーシングバックエンドは、収集されたトレースに基づいてサービスの依存関係を可視化できます。

### 5. Micrometer Tracingのベストプラクティス：

  * **スパンに意味のある名前を付ける:** スパンには明確で簡潔、かつ低カーディナリティの名前を使用します（例："userService.getUser"、"productService.updateStock"）。動的なデータをスパン名に含めないでください。
  * **詳細にはタグを使用する（高カーディナリティデータ）：** 動的なデータをスパン名に置く代わりに、追加のコンテキストのためにタグ（キーと値のペア）を使用します。例えば、`userId`、`orderId`、`customerType`。**高カーディナリティ**タグは、トレーシングバックエンドのストレージコストとクエリ時間を大幅に増加させる可能性があるため、注意して使用してください。
  * **スパンを細かくしすぎない：** 重要な操作に対してスパンを作成しますが、あまりにも多くの小さなスパンを作成することは避け、オーバーヘッドを追加しないようにします。システムを圧倒することなく十分な可視性を提供するバランスを目指します。
  * **コンテキストの伝播:** トレースコンテキストがサービス境界を越えて適切に伝播することを確認してください。Spring Bootの自動設定は一般的なシナリオでこれを処理しますが、カスタムクライアントや非同期操作を使用する場合は注意してください。
  * **サンプリング:** 高トラフィックの本番環境では、バックエンドに送信されるトレースデータの量を減らすためにサンプリング戦略の使用を検討してください。Spring Bootは`management.tracing.sampling.probability`の設定を許可します。
  * **ログの関連付け:** ログに注入された`traceId`と`spanId`を活用して、アプリケーションの動作を特定のリクエストと簡単に関連付け、デバッグを容易にします。
  * **トレーシングバックエンドの監視:** トレーシングバックエンド（例：Zipkinサーバー）が受信トレースボリュームを処理するのに十分なリソースを持っていることを確認してください。
  * **他のオブザーバビリティツールとの統合:** トレーシングはオブザーバビリティの一部です。メトリクス（Micrometer経由でも）および構造化ロギングと組み合わせて、アプリケーションの健全性とパフォーマンスの包括的なビューを実現します。

これらのガイドラインに従うことで、特に分散環境において、Spring Bootアプリケーションへの深い洞察を得るためにMicrometer Tracingを効果的に活用できます。