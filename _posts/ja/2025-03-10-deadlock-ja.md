---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootにおけるデッドロック
translated: true
type: note
---

Spring Bootプロジェクトで、複数のリクエストがBeanのメソッドに同時にアクセスした際のデッドロック問題の解決について掘り下げていきましょう。デッドロックは、2つ以上のスレッドがデータベースロック、synchronizedブロック、スレッドセーフなデータ構造などの共有リソースを競合することで、互いに永久にブロックし合う状況で発生します。Beanのメソッドが多くのリクエストを処理しているとのことなので、ここではシングルトンスコープのBean（Springのデフォルトスコープ）を想定し、一般的な原因と解決策を探っていきます。

まず、このコンテキストで考えられるデッドロックのシナリオを特定しましょう：
1. **データベースロック**: Beanのメソッドがデータベース（例：JPA/Hibernate経由）とやり取りする場合、同時実行トランザクションが行やテーブルを矛盾する順序でロックする可能性があります。
2. **Synchronizedブロック**: メソッドが`synchronized`キーワードやロック（例：`ReentrantLock`）を使用している場合、不適切なロック順序によりスレッドが互いに待機状態になる可能性があります。
3. **共有リソース**: Beanが共有のインメモリリソース（例：静的変数やコレクション）を変更する場合、競合がデッドロックを引き起こす可能性があります。
4. **外部呼び出し**: メソッドが外部サービスやAPIを呼び出す場合、遅延やブロッキング動作が並行処理の問題を悪化させる可能性があります。

具体的なコードが共有されていないため、問題を診断して修正する一般的なアプローチを提供した後、具体的な例を示します。

### ステップ1: デッドロックの診断
- **ロギングの有効化**: メソッドの開始、終了、リソースアクセスを追跡するためにロギング（例：SLF4JとLogback）を追加します。これにより、スレッドが停止する場所を特定できます。
- **スレッドダンプ**: デッドロックが発生した時に、スレッドダンプを取得します（例：`jstack`やVisualVMを使用）。`BLOCKED`または`WAITING`状態のスレッドを探し、ロック競合についてスタックトレースを確認します。
- **モニタリング**: Spring Actuatorやプロファイラー（例：YourKit）などのツールを使用して、負荷下でのスレッドの動作を観察します。

### ステップ2: 一般的な修正方法
考えられる原因に基づいてデッドロックに対処する方法は以下の通りです：

#### ケース1: データベース関連のデッドロック
Beanのメソッドがデータベース操作を実行する場合、デッドロックはトランザクションの競合から発生することが多いです。
- **解決策**: トランザクションの境界とロック取得順序を最適化します。
  - 適切な分離レベル（例：厳密に必要でない限り`SERIALIZABLE`ではなく`READ_COMMITTED`）で`@Transactional`を使用します。
  - リソースアクセスの順序を一貫させる（例：常にテーブルAをテーブルBの前に更新する）。
  - 非トランザクションロジックを`@Transactional`の外に移動して、トランザクションスコープを縮小します。
- **例**:
  ```java
  @Service
  public class MyService {
      @Autowired
      private MyRepository repo;

      @Transactional
      public void processRequest(Long id1, Long id2) {
          // デッドロックを避けるため一貫した順序を確保
          if (id1 < id2) {
              repo.updateEntity(id1);
              repo.updateEntity(id2);
          } else {
              repo.updateEntity(id2);
              repo.updateEntity(id1);
          }
      }
  }
  ```
- **ボーナス**: トランザクションタイムアウト（例：`@Transactional(timeout = 5)`）を設定して、長時間実行されるトランザクションを中止し、無限の待機を防ぎます。

#### ケース2: Synchronizedブロックまたはロック
メソッドが明示的なロックを使用する場合、ロックがスレッド間で異なる順序で取得されるとデッドロックが発生する可能性があります。
- **解決策**: 単一のロックを使用するか、ロック順序を強制します。
  - 複数の`synchronized`ブロックを単一の粗粒度ロックに置き換えます（可能な場合）。
  - 無限のブロッキングを避けるためにタイムアウト付きの`ReentrantLock`を使用します。
- **例**:
  ```java
  @Service
  public class MyService {
      private final ReentrantLock lock = new ReentrantLock();

      public void processRequest(String resourceA, String resourceB) {
          try {
              if (lock.tryLock(2, TimeUnit.SECONDS)) {
                  // クリティカルセクション
                  System.out.println("Processing " + resourceA + " and " + resourceB);
              } else {
                  throw new RuntimeException("Could not acquire lock in time");
              }
          } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
          } finally {
              if (lock.isHeldByCurrentThread()) {
                  lock.unlock();
              }
          }
      }
  }
  ```

#### ケース3: 共有インメモリリソース
Beanが共有コレクションや変数を変更する場合、同時アクセスが問題を引き起こす可能性があります。
- **解決策**: スレッドセーフな代替手段を使用するか、共有状態を避けます。
  - `ArrayList`を`CopyOnWriteArrayList`または`Collections.synchronizedList`に置き換えます。
  - マップには`ConcurrentHashMap`を使用します。
  - さらに良いのは、Beanをステートレスにするか、リクエストスコープのBean（`@Scope("request")`）を使用することです。
- **例**:
  ```java
  @Service
  @Scope("prototype") // ステートフルな場合はシングルトンを避ける
  public class MyService {
      private final ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();

      public void processRequest(String key, int value) {
          cache.put(key, value); // スレッドセーフ
      }
  }
  ```

#### ケース4: 高並行性負荷
デッドロックがBeanへの過剰なリクエストに起因する場合、スレッド競合が根本原因である可能性があります。
- **解決策**: 非同期処理またはレート制限を導入します。
  - `@Async`を使用して作業をスレッドプールにオフロードします。
  - `TaskExecutor`でスレッドプールを設定して並行性を管理します。
- **例**:
  ```java
  @Service
  public class MyService {
      @Async
      public CompletableFuture<String> processRequest(String input) {
          // 作業をシミュレート
          Thread.sleep(1000);
          return CompletableFuture.completedFuture("Done: " + input);
      }
  }

  @Configuration
  @EnableAsync
  public class AsyncConfig {
      @Bean
      public TaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(10);
          executor.setMaxPoolSize(50);
          executor.setQueueCapacity(100);
          return executor;
      }
  }
  ```
- **使用方法**: `processRequest`を呼び出し、コントローラーで`CompletableFuture`を処理します。

### ステップ3: 将来の問題を防止
- **負荷テスト**: JMeterやGatlingなどのツールで高並行性をシミュレートし、デッドロックを早期に検出します。
- **コードレビュー**: ネストされたロック、長時間実行されるトランザクション、共有可変状態を確認します。
- **タイムアウト**: ロック、トランザクション、外部呼び出しには常にタイムアウトを設定します。

### 最終的な考え
Beanのコードを確認していないため、高負荷下のシングルトンBeanでデータベースやロック競合の可能性があると想定しました。詳細（メソッドのコード、スタックトレース、アクセスするリソースなど）を共有していただければ、さらに解決策を絞り込むことができます。今のところ、スレッドダンプで診断を開始し、関連する修正（データベースの最適化、ロック管理、非同期処理）を適用してください。経過を教えてください！