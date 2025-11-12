---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootマルチスレッド
translated: true
type: note
---

Spring Bootプロジェクトにおいて、「エグゼキューター」と「スレッド」の概念は、通常、アプリケーションが並行タスクを処理し、ワークロードを管理する方法に関連します。特に、非同期処理、タスクスケジューリング、または複数のリクエストを扱うシナリオで重要です。ステップバイステップで見ていきましょう：

---

### **Spring Bootにおけるエグゼキューターとスレッドとは？**

1. **スレッド**:
   - スレッドは、Javaプログラムにおける実行の最小単位です。Spring Bootアプリケーションでは、HTTPリクエストの処理、バックグラウンドジョブの実行、I/O操作の実行などのタスクを処理するためにスレッドが使用されます。
   - Spring Bootは、デフォルトでは組み込みWebサーバー（例：Tomcat、Jetty、Undertow）内で実行され、このサーバーは着信リクエストを管理するためにスレッドプールを使用します。各リクエストは通常、このプールからのスレッドに割り当てられます。

2. **エグゼキューター**:
   - Java（およびSpring Boot）における `Executor` は、スレッド管理を抽象化したものです。これは `java.util.concurrent` パッケージの一部であり、スレッドを手動で作成および管理することなく、タスクを非同期に管理および実行する方法を提供します。
   - Spring Bootでは、エグゼキューターは、メインアプリケーションスレッド（例：HTTPリクエストを処理するスレッド）から別のスレッドプールにタスクをオフロードするためによく使用されます。これは、長時間実行されるタスク、並列処理、またはスケジュールされたジョブに有用です。

3. **Spring固有のコンテキスト**:
   - Spring Bootは、`ThreadPoolTaskExecutor`（一般的なタスク実行用）や `ThreadPoolTaskScheduler`（スケジュールされたタスク用）などのユーティリティを提供し、エグゼキューターとスレッドの操作を簡素化します。
   - これらはJavaの `ExecutorService` 上に構築されており、一般的に以下に使用されます：
     - 非同期メソッド実行（`@Async` 経由）。
     - タスクスケジューリング（`@Scheduled` 経由）。
     - 高並行性シナリオにおけるワークロード管理。

---

### **Spring Bootにおける動作**

#### **1. Spring Bootにおけるデフォルトのスレッド管理**
- Spring Boot Webアプリケーションを起動すると、組み込みサーバー（例：Tomcat）は、着信HTTPリクエストを処理するためのスレッドプールを初期化します。
- 例えば、Tomcatのデフォルト設定では200スレッドが割り当てられる場合があります（`application.properties` の `server.tomcat.threads.max` で設定可能）。
- 各着信リクエストは、このプールからのスレッドに割り当てられます。すべてのスレッドがビジー状態で新しいリクエストが到着した場合、それは（サーバーの設定に応じて）キューイングされるか、拒否される可能性があります。

#### **2. Spring Bootにおけるエグゼキューター**
- Spring Bootは、特定のタスクのためのカスタムスレッドプールを管理するために、`TaskExecutor` インターフェース（Javaの `Executor` の拡張）を提供します。
- 一般的な実装は `ThreadPoolTaskExecutor` で、以下を設定できます：
  - **コアプールサイズ**: 常に生存保持されるスレッド数。
  - **最大プールサイズ**: プールで許可される最大スレッド数。
  - **キュー容量**: 新しいスレッドが生成される前にキューで待機できるタスク数（最大プールサイズまで）。
  - **スレッド命名**: デバッグを容易にするため（例: "my-executor-thread-1"）。

  Spring Bootアプリケーションでの設定例：
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

  @Configuration
  public class ExecutorConfig {

      @Bean
      public ThreadPoolTaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(5);      // 最小5スレッド
          executor.setMaxPoolSize(10);      // 最大10スレッド
          executor.setQueueCapacity(100);   // 最大100タスクをキューイング
          executor.setThreadNamePrefix("MyExecutor-");
          executor.initialize();
          return executor;
      }
  }
  ```

#### **3. エグゼキューターと `@Async` の使用**
- Spring Bootは、`@Async` アノテーションを使用した非同期メソッド実行をサポートしています。メソッドに `@Async` を付けると、エグゼキューターによって管理される別のスレッドで実行されます。
- デフォルトでは、Springは `SimpleAsyncTaskExecutor` を使用します。これは各タスクに対して新しいスレッドを作成します（高負荷には理想的ではありません）。これを最適化するために、独自の `ThreadPoolTaskExecutor` を提供し、参照することができます：
  ```java
  @Service
  public class MyService {

      @Async("taskExecutor") // 設定からのBean名を参照
      public void doAsyncTask() {
          System.out.println("Running on thread: " + Thread.currentThread().getName());
      }
  }
  ```

#### **4. タスクスケジューリング**
- スケジュールされたタスク（例：5分ごとにジョブを実行）の場合、Spring Bootは `ThreadPoolTaskScheduler` を使用します。これは `ThreadPoolTaskExecutor` に似ていますが、スケジューリング用に調整されています。
- 例：
  ```java
  @Scheduled(fixedRate = 5000) // 5秒ごとに実行
  public void scheduledTask() {
      System.out.println("Scheduled task on: " + Thread.currentThread().getName());
  }
  ```

#### **5. スレッドとエグゼキューターの相互作用**
- タスクがエグゼキューターに送信されると（例：`@Async` または手動送信経由）、エグゼキューターは以下を決定します：
  - プールから既存のアイドルスレッドを使用する。
  - 新しいスレッドを作成する（コアプールサイズを超えているが、最大プールサイズ以下の場合）。
  - タスクをキューイングする（最大プールサイズに達しており、キューが満杯でない場合）。
  - タスクを拒否する（キューが満杯で、これ以上スレッドを作成できない場合）。
- スレッドはタスクを実行し、完了するとプールに戻り、次のタスクの準備をします。

---

### **実践的な例**
ユーザー登録を処理するSpring Bootアプリを想像してください：
- **HTTPリクエストスレッド**: ユーザーが登録フォームを送信し、Tomcatスレッドプールからのスレッドによって処理されます。
- **非同期タスク**: 確認メールの送信は、`@Async` メソッドを介して `ThreadPoolTaskExecutor` にオフロードされるため、HTTPスレッドはメール送信を待たずに即座に応答できます。
- **スケジュールされたタスク**: 未確認アカウントを削除するクリーンアップジョブが1時間ごとに実行され、`ThreadPoolTaskScheduler` によって管理されます。

---

### **重要なポイント**
- **エグゼキューター**はスレッド管理を抽象化し、並行性のスケーリングと調整を容易にします。
- **スレッド**は実際の作業を行い、そのライフサイクルはエグゼキューターまたはWebサーバーによって管理されます。
- Spring Bootのデフォルトは小規模なアプリには十分ですが、高負荷または複雑なアプリでは、パフォーマンスを最適化するためにカスタムエグゼキューターを設定します。

特定のSpring Bootプロジェクトを想定して、そのエグゼキューター/スレッド設定の分析を手伝ってほしい場合は、詳細を共有してください！