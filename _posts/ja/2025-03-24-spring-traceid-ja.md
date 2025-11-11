---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot Log4jリクエストトレーシング
translated: true
type: note
---

組み込みのトレースID設計がないLog4jを使用したJava Spring Bootアプリケーションでは、特定のログエントリをフロントエンドから開始されたリクエストに遡って追跡することは確かに困難です。Log4jの`%t`（スレッド名）が特定のスレッドに関連するログの識別に役立つことはご指摘の通りですが、リクエストが複数のスレッドにまたがる場合（非同期処理、スレッドプール、ダウンストリーム呼び出しなど）には信頼性が低下します。時間範囲でログを検索するのは回避策ですが、特に高トラフィックシステムでは不正確で面倒です。既存の設定を大幅に変更せずにこの状況を改善する実践的なアドバイスを探ってみましょう。

### 簡単で実践的な提案
1. **Log4jのMDC（Mapped Diagnostic Context）を活用**
   - Log4jはMDCをサポートしており、スレッド内（および適切な対応をすればスレッド境界を越えて伝播させることも可能）でログにコンテキストのキーと値のペアを追加できます。
   - フロントエンドリクエストがSpring Bootアプリケーションに到達した時点で一意のリクエストID（UUIDなど）を生成し、MDCに保存します。その後、このIDをログパターンに含めます。
   - **実装方法:**
     - Spring Bootのフィルターまたはインターセプター（例: `OncePerRequestFilter`）でIDを生成:
       ```java
       import org.slf4j.MDC;
       import javax.servlet.FilterChain;
       import javax.servlet.http.HttpServletRequest;
       import javax.servlet.http.HttpServletResponse;
       import java.util.UUID;

       public class RequestTracingFilter extends OncePerRequestFilter {
           @Override
           protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {
               try {
                   String traceId = UUID.randomUUID().toString();
                   MDC.put("traceId", traceId);
                   filterChain.doFilter(request, response);
               } finally {
                   MDC.clear(); // リクエスト後にクリーンアップ
               }
           }
       }
       ```
     - Spring Boot設定でフィルターを登録:
       ```java
       @Bean
       public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
           FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
           registrationBean.setFilter(new RequestTracingFilter());
           registrationBean.addUrlPatterns("/*");
           return registrationBean;
       }
       ```
     - `log4j.properties`または`log4j.xml`のLog4jパターンを更新して`traceId`を含める:
       ```properties
       log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
       ```
     - これで、そのリクエストに関連するすべてのログ行に`traceId`が含まれ、フロントエンドのボタンクリックに遡って追跡が容易になります。

2. **スレッド間でのトレースIDの伝播**
   - アプリケーションがスレッドプールや非同期呼び出し（例: `@Async`）を使用する場合、MDCコンテキストは自動的には伝播されない可能性があります。これに対処するには:
     - MDCコンテキストをコピーするカスタムエグゼキューターで非同期タスクをラップ:
       ```java
       import java.util.concurrent.Executor;
       import org.springframework.context.annotation.Bean;
       import org.springframework.context.annotation.Configuration;
       import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

       @Configuration
       public class AsyncConfig {
           @Bean(name = "taskExecutor")
           public Executor taskExecutor() {
               ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
               executor.setCorePoolSize(10);
               executor.setMaxPoolSize(20);
               executor.setQueueCapacity(100);
               executor.setTaskDecorator(task -> {
                   Map<String, String> context = MDC.getCopyOfContextMap();
                   return () -> {
                       try {
                           if (context != null) MDC.setContextMap(context);
                           task.run();
                       } finally {
                           MDC.clear();
                       }
                   };
               });
               executor.initialize();
               return executor;
           }
       }
       ```
     - これにより、スレッド境界を越えても`traceId`がリクエストに紐付けられます。

3. **フロントエンド相関の追加**
   - 可能であれば、フロントエンドがボタンクリック時にカスタムヘッダー（例: `X-Request-ID`）と一意のIDを送信するようにします。バックエンドは独自のUUIDを生成する代わりにこれを取得できます。これにより、追加の推測なしでログをフロントエンドのアクションに直接結び付けられます。

4. **フォールバック: コンテキストデータによるログの強化**
   - MDCが現在のところオーバーヘッドが大きいと感じる場合は、キーポイントでより多くのコンテキスト（ユーザーID、セッションID、エンドポイント名など）をログに追加します。例:
     ```java
     logger.info("Button clicked, endpoint=/api/example, user={}", userId);
     ```
   - これを`%t`（スレッド名）と厳密な時間範囲と組み合わせて、手動でログを絞り込みます。理想的ではありませんが、緊急時には機能します。

### なぜ時間範囲だけでは不十分なのか
タイムスタンプのみに依存することは脆弱です。なぜなら:
- 特に繁忙なシステムでは、同時リクエストからのログが重複します。
- 時間の精度（ミリ秒など）が単一のリクエストを分離するのに十分でない可能性があります。
- サービス間や深い呼び出しスタック全体でログを関連付けるのは面倒です。

### 長期的な推奨事項
このトレースの必要性が高まる場合は、Spring Bootの分散トレーシングの組み込みサポート（SleuthやMicrometer with Zipkinなど）の採用を検討してください。SleuthはトレースIDとスパンIDを自動生成し、Log4jとシームレスに統合しますが、設定はより複雑です。現時点では、MDCは軽量で効果的な中間的な解決策です。

### 最終的なアドバイス
MDCアプローチから始めてください。これはシンプルで、Log4jのネイティブ機能を活用し、ログをフロントエンド開始リクエストに結び付ける明確な方法を提供します。そのリクエストに対するすべてのログ行に`[traceId=123e4567-e89b-12d3-a456-426614174000]`のようなものが表示され、検索とトレースが簡単になります。さらに調整が必要な場合はお知らせください！