---
audio: false
generated: true
lang: ja
layout: post
title: ログにおける空の `traceId` および `spanId` のトラブルシューティング
translated: true
type: note
---

`traceId`と`spanId`がログ行`[blog-server,,]`で空になっているのは、以下のいずれかの理由が考えられます:

  * **Sleuth依存関係の不足または不備:** `spring-cloud-starter-sleuth`依存関係がプロジェクトの`pom.xml`（Mavenの場合）または`build.gradle`（Gradleの場合）に正しく追加されていること、および互換性のあるSpring BootとSpring Cloudのバージョンを使用していることを確認してください。この依存関係がない場合、Spring Cloud Sleuthの自動設定は有効になりません。

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

  * **カスタムロギングパターン:** カスタムロギングパターン（例: `logback-spring.xml`や`application.properties`で定義）がある場合、`traceId`と`spanId`のプレースホルダーを明示的に含める必要があります。これらのプレースホルダーが欠落している場合、Sleuthが有効であってもIDはログに表示されません。

    Logbackの場合、パターンに`%X{traceId}`と`%X{spanId}`が含まれていることを確認してください:

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

  * **アクティブなTrace/Spanコンテキストがない:** Sleuthは多くのSpringコンポーネント（HTTPリクエスト用の`DispatcherServlet`など）を自動的に計装しますが、これらの特定のログメッセージがtraceやspanが開始または伝播されていないコンテキストで生成されている可能性があります。例えば、アプリケーション起動時の非常に早い段階のログや、Sleuthのコンテキスト伝播によって管理されていないスレッドからのログにはこれらのIDが含まれない場合があります。ただし、`HttpEntityMethodProcessor`や`DispatcherServlet`によるリクエスト完了時のログのように、アクティブなHTTPリクエスト処理中のログでこれが発生する場合は、Sleuthが適切に設定されていれば一般的ではありません。

トラブルシューティングでは、まず依存関係とロギング設定を確認してください。それらが正しい場合、リクエストが実際にアプリケーションに到達し、Spring MVCの`DispatcherServlet`によって処理されていることを確認してください。これによりSleuthの計装がトリガーされるはずです。