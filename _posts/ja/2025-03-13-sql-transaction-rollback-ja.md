---
audio: false
generated: true
lang: ja
layout: post
title: SpringにおけるSQLトランザクションロールバック例外
translated: true
type: note
---

`SqlTransactionRollbackException` が `DataSourceUtils.java` から JDBC 接続を取得した後に発生する問題と、関連するデータベースロックの詳細な分析について、体系的に説明します。

### SqlTransactionRollbackException のキャッチ方法

Spring ベースのアプリケーションでは、`DataSourceUtils.java` は Spring Framework 内のユーティリティクラスで、`DataSource` からの JDBC 接続の取得と管理を容易にします。具体的には、`DataSourceUtils.getConnection(DataSource)` メソッドは、接続プールから新しい接続を取得するか、現在のスレッドのトランザクションコンテキストに関連付けられた既存のトランザクション接続を再利用します。

あなたが説明したシナリオは、接続が正常に取得された後、`SqlTransactionRollbackException` がスローされることを示しています。`SqlTransactionRollbackException` は Spring の例外階層における標準的な例外ではないため（Spring は通常 `TransactionException`、`UnexpectedRollbackException`、`DeadlockLoserDataAccessException` などの例外を使用します）、これはデータベース関連の問題（ロック競合など）によりトランザクションがロールバックされたときにスローされるカスタムのアプリケーション固有の例外であると想定します。

この例外は、接続取得自体では発生せず（失敗した場合は通常 `CannotGetJdbcConnectionException` がスローされます）、ロールバックを必要とする問題に遭遇したトランザクション内での後続のデータベース操作（SQL 文の実行など）中に発生します。

この例外をキャッチするには、トランザクション操作を開始するコードを `try-catch` ブロックでラップする必要があります。以下にその方法を示します。

#### 宣言的トランザクション管理の例
Spring の `@Transactional` アノテーションを使用してトランザクションを管理している場合、例外はトランザクションが定義されているメソッドからスローされます。例：

```java
@Service
public class MyService {
    @Autowired
    private MyDao myDao;

    @Transactional
    public void performDatabaseOperation() {
        myDao.updateData(); // ロック問題によりロールバックが発生すると仮定
    }
}
```

このサービスメソッドを呼び出すときに、`SqlTransactionRollbackException` をキャッチできます：

```java
@Autowired
private MyService myService;

public void executeOperation() {
    try {
        myService.performDatabaseOperation();
    } catch (SqlTransactionRollbackException e) {
        // 例外を処理
        System.err.println("Transaction rolled back due to: " + e.getMessage());
        // オプションで操作を再試行またはユーザーに通知
    }
}
```

#### プログラムによるトランザクション管理の例
`TransactionTemplate` または `PlatformTransactionManager` を使用してプログラムでトランザクションを管理している場合、トランザクション実行の周囲で例外をキャッチします：

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void executeOperation() {
    try {
        transactionTemplate.execute(status -> {
            // データベース操作を実行
            myDao.updateData();
            return null;
        });
    } catch (SqlTransactionRollbackException e) {
        // 例外を処理
        System.err.println("Transaction rolled back due to: " + e.getMessage());
    }
}
```

#### 考慮事項
- **例外階層**: `SqlTransactionRollbackException` がカスタム例外の場合、そのスーパークラスを確認してください。Spring の `DataAccessException` を拡張している場合、代わりに `DataAccessException` をキャッチして特定のタイプをチェックできます：
  ```java
  catch (DataAccessException e) {
      if (e instanceof SqlTransactionRollbackException) {
          // SqlTransactionRollbackException を具体的に処理
      }
  }
  ```
- **トランザクションコンテキスト**: 例外は、接続が取得された後に、トランザクションマネージャーまたは JDBC ドライバーが問題（ロールバック専用状態やデータベースエラーなど）を検出したときに発生します。したがって、サービスレベルまたは呼び出し元レベルでキャッチすることが適切です。

### データベースロックの詳細な分析

あなたのクエリで言及されている「この種のデータベースロック」は、ロールバック例外と組み合わさって、トランザクションロールバックにつながる一般的なデータベースロック問題である **デッドロック** への関連を示唆しています。これを詳細に分析しましょう。

#### デッドロックとは？
デッドロックは、2つ以上のトランザクションが互いに必要なロックを保持しているために進行できなくなり、循環依存を作り出すときにデータベースで発生します。例：

- **トランザクション T1**:
  1. `TableA` の排他ロックを取得
  2. `TableB` の排他ロックを取得しようとする（T2 が保持しているため待機）
- **トランザクション T2**:
  1. `TableB` の排他ロックを取得
  2. `TableA` の排他ロックを取得しようとする（T1 が保持しているため待機）

ここで、T1 は T2 が `TableB` を解放するのを待ち、T2 は T1 が `TableA` を解放するのを待ち、デッドロックが発生します。

#### デッドロックがロールバックにつながる仕組み
ほとんどのリレーショナルデータベース（MySQL、PostgreSQL、Oracle など）にはデッドロック検出メカニズムがあります。デッドロックが識別されると：
1. データベースは「犠牲」トランザクションを選択します（多くの場合、作業量が最も少ないものまたは設定可能なポリシーに基づく）
2. 犠牲トランザクションがロールバックされ、そのロックが解放されます
3. データベースは特定のエラーコード（MySQL エラー 1213、PostgreSQL エラー 40P01 など）を含む `SQLException` をアプリケーションにスローします
4. Spring では、この `SQLException` は通常 `DeadlockLoserDataAccessException` に変換されます。アプリケーションが代わりに `SqlTransactionRollbackException` をスローする場合、これはそのようなイベントをラップするカスタムラッパーである可能性があります

あなたのシナリオでは、`DataSourceUtils` が接続を取得した後、トランザクション内のデータベース操作がデッドロックに遭遇し、ロールバックと `SqlTransactionRollbackException` のスローにつながります。

#### 関連するロックタイプ
- **共有ロック**: 読み取り操作に使用。複数のトランザクションが同じリソースの共有ロックを保持できます
- **排他ロック**: 書き込み操作に使用。1つのトランザクションのみが排他ロックを保持でき、他のトランザクションが保持する共有ロックおよび排他ロックと競合します

デッドロックは通常、排他ロックを含みます。これらはより制限的であるためです。

#### デッドロックが発生する理由
デッドロックは以下が原因で発生します：
- **一貫性のないロック順序**: トランザクションがリソース（テーブル、行など）に異なる順序でアクセスする
- **長時間のトランザクション**: ロックを長時間保持すると、競合の可能性が高まる
- **高並行性**: 複数のトランザクションが同時に同じデータを操作する

#### 例のシナリオ
アプリケーション内の2つのメソッドが2つのテーブルを更新すると仮定：

```java
@Transactional
public void updateUserAndOrder1() {
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Alice", 1); // users 行をロック
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Shipped", 1); // orders 行をロック
}

@Transactional
public void updateUserAndOrder2() {
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Processed", 1); // orders 行をロック
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Bob", 1); // users 行をロック
}
```

これらのメソッドが同時に実行されると、`updateUserAndOrder1` は `users` をロックしながら `orders` を待ち、`updateUserAndOrder2` は `orders` をロックしながら `users` を待ち、デッドロックが発生します。

#### デッドロックの処理と防止
1. **例外をキャッチ**:
   前述のように、`try-catch` ブロックを使用して `SqlTransactionRollbackException` を処理します。以下を行う可能性があります：
   - デバッグのためにエラーをログに記録
   - 操作を再試行（無限ループを避けるために注意）：
     ```java
     int retries = 3;
     for (int i = 0; i < retries; i++) {
         try {
             myService.performDatabaseOperation();
             break;
         } catch (SqlTransactionRollbackException e) {
             if (i < retries - 1) {
                 Thread.sleep(1000 * (i + 1)); // 指数バックオフ
                 continue;
             }
             throw e; // 最大再試行後に再スロー
         }
     }
     ```

2. **一貫したロック順序を確保**:
   コードを変更して、テーブルに同じ順序でアクセスする（例：常に `users` を `orders` の前にロック）

3. **ロック期間を最小化**:
   非トランザクションロジックを `@Transactional` 境界の外に移動して、トランザクションを短く保つ

4. **適切な分離レベルを使用**:
   アプリケーション要件が許せば、トランザクション分離レベルを調整する（例：`SERIALIZABLE` の代わりに `READ_COMMITTED`）。ただし、これでデッドロックが完全に排除されるわけではありません

5. **データベース固有の機能**:
   - デッドロック検出ログを有効にする（例：MySQL の `innodb_print_all_deadlocks`）
   - 可能な場合は行レベルロックを使用（ただし、行レベルでもデッドロックは発生する可能性があります）

#### デッドロックの分析
特定のデッドロックを診断するには：
- **データベースログ**: デッドロックの詳細（関連するトランザクション、ロックされたリソース）についてデータベースサーバーログを確認
- **Spring デバッグ**: Spring トランザクションログを有効にする（`logging.level.org.springframework.transaction=DEBUG`）
- **アプリケーショントレース**: 例外につながる操作のシーケンスをログに記録

### 結論
`SqlTransactionRollbackException` をキャッチするには、`@Transactional` でマークされたサービスメソッドなど、トランザクション操作を呼び出すコードの周囲に `try-catch` ブロックを配置します。データベースロック（おそらくデッドロック）については、トランザクションが一貫した順序でリソースにアクセスすることを確保し、トランザクションを短く保ち、一時的な障害に対して再試行ロジックを検討します。デッドロックは循環ロック依存関係が原因で発生し、データベースは犠牲トランザクションをロールバックすることで解決しますが、予防的な設計で発生を最小限に抑えることができます。

---

Spring アプリケーションで `SqlTransactionRollbackException` を扱う場合、特に別のトランザクションがロックを保持しているシナリオでは、接続取得の失敗と約20回の失敗試行後の例外スローにつながることがあります。この例外は通常、データベースロックまたは並行性の問題により操作が正常に完了できない場合のトランザクションロールバック中に発生します。以下では、この問題に対処するための予防、処理、回復に焦点を当てた包括的なアプローチを概説します。

---

### 問題の理解
`SqlTransactionRollbackException`（または Spring ではより一般的に `TransactionRollbackException`）は、別のトランザクションが必要なデータベースリソースのロックを保持しているため、トランザクションをロールバックできなかったことを示します。このロック競合により、トランザクションマネージャーは接続の取得に失敗し、複数回（あなたのケースでは約20回）再試行し、最終的にロールバックが完了できないときに例外をスローします。これは、ロック競合やデッドロックなどの並行性問題を示唆し、Spring のトランザクション管理が内部で再試行した後にあきらめることで悪化します。

---

### 例外を処理する戦略

#### 1. 短いトランザクションでロック競合を最小化
長時間実行されるトランザクションは、データベースロックを長時間保持するため、ロック競合の可能性を高めます。このリスクを減らすには：

- **短命トランザクションを設計**: `@Transactional` メソッドがデータベース操作を迅速に実行し、速やかにコミットまたはロールバックすることを確保します。トランザクションスコープ内で時間のかかるビジネスロジックや外部呼び出しを含めないでください
- **大きなトランザクションを分割**: 単一のトランザクションに複数の操作が含まれる場合、可能であれば小さな独立したトランザクションに分割します。これにより、ロックが保持される期間が短縮されます

#### 2. データベースクエリを最適化
最適化されていないクエリは、必要以上に長くロックを保持することでロック競合を悪化させます。これに対処するには：

- **クエリを分析および最適化**: データベースプロファイリングツールを使用して遅いクエリを特定します。適切なインデックスを追加し、不要なテーブルスキャンを避け、ロックされる行の範囲を最小限に抑えます（例：正確な `WHERE` 句を使用）
- **過度に広範なロックを避ける**: `SELECT ... FOR UPDATE` のような明示的に行をロックする文には注意し、必要な場合にのみ使用し、影響する行を最小限に抑えます

#### 3. トランザクション設定を調整
Spring の `@Transactional` アノテーションは、トランザクション動作を微調整する属性を提供します。これらはロールバック失敗を直接解決しませんが、並行性の管理に役立ちます：

- **分離レベル**: デフォルトの分離レベル（`DEFAULT`）は通常、データベースのデフォルト（多くの場合 `READ_COMMITTED`）にマッピングされます。`REPEATABLE_READ` または `SERIALIZABLE` に上げるとデータ一貫性が確保される可能性がありますが、ロック競合が悪化する可能性があります。逆に、`READ_COMMITTED` またはそれ以下（サポートされている場合）にすると、ユースケースに応じてロック問題が減少する可能性があります。適切なバランスを見つけるために注意深くテストしてください
- **伝播動作**: デフォルトの `REQUIRED` は既存のトランザクションに参加するか、新しいトランザクションを開始します。`REQUIRES_NEW` を使用すると、現在のトランザクションを中断し、新しいトランザクションを開始し、ロックされたトランザクションとの競合を回避する可能性があります。ただし、これはロールバック固有の問題に対処しない可能性があります
- **タイムアウト**: `@Transactional(timeout = 10)` でタイムアウト値（秒単位）を設定し、トランザクションがロックを待機している場合に迅速に失敗させます。これにより長時間の再試行が防止されますが、根本原因は修正されません

例：
```java
@Transactional(timeout = 5, propagation = Propagation.REQUIRES_NEW)
public void performDatabaseOperation() {
    // ここにコードを記述
}
```

#### 4. 再試行ロジックを実装（注意して）
例外が複数の内部再試行（約20回）後に発生するため、Spring のトランザクションマネージャーはすでに問題の処理を試みている可能性があります。ただし、より高いレベルでカスタム再試行ロジックを実装できます：

- **Spring Retry を使用**:
  サービスメソッドに `@Retryable` を付けて、`TransactionRollbackException` で再試行します。試行回数と再試行間の遅延を指定します。再試行が尽きた後の失敗を処理するために `@Recover` メソッドと組み合わせます
  ```java
  import org.springframework.retry.annotation.Backoff;
  import org.springframework.retry.annotation.Retryable;
  import org.springframework.retry.annotation.Recover;
  import org.springframework.transaction.annotation.Transactional;

  @Service
  public class MyService {

      @Retryable(value = TransactionRollbackException.class, maxAttempts = 3, backoff = @Backoff(delay = 1000))
      public void executeOperation() {
          performTransactionalWork();
      }

      @Transactional
      private void performTransactionalWork() {
          // 失敗する可能性のあるデータベース操作
      }

      @Recover
      public void recover(TransactionRollbackException e) {
          // エラーをログに記録、管理者に通知、または是正措置を実行
          System.err.println("All retries failed: " + e.getMessage());
      }
  }
  ```
  **注意**: 各再試行は新しいトランザクションを開始するため、再試行全体での原子性が必要な場合は理想的ではない可能性があります。可能であれば、`@Transactional` メソッドの外側にこれを適用してください

- **TransactionTemplate を使用した手動再試行**:
  より制御するために、`TransactionTemplate` を使用してトランザクションコードを再試行ループでラップします：
  ```java
  import org.springframework.transaction.PlatformTransactionManager;
  import org.springframework.transaction.TransactionStatus;
  import org.springframework.transaction.support.TransactionCallbackWithoutResult;
  import org.springframework.transaction.support.TransactionTemplate;

  @Service
  public class MyService {
      private final TransactionTemplate transactionTemplate;
      private static final int MAX_RETRIES = 3;
      private static final long RETRY_DELAY_MS = 1000;

      public MyService(PlatformTransactionManager transactionManager) {
          this.transactionTemplate = new TransactionTemplate(transactionManager);
      }

      public void executeWithRetry() {
          for (int i = 0; i < MAX_RETRIES; i++) {
              try {
                  transactionTemplate.execute(new TransactionCallbackWithoutResult() {
                      @Override
                      protected void doInTransactionWithoutResult(TransactionStatus status) {
                          // トランザクションコードをここに記述
                      }
                  });
                  return; // 成功、ループを終了
              } catch (TransactionRollbackException e) {
                  if (i == MAX_RETRIES - 1) {
                      throw e; // 最大再試行後に再スロー
                  }
                  try {
                      Thread.sleep(RETRY_DELAY_MS);
                  } catch (InterruptedException ie) {
                      Thread.currentThread().interrupt();
                  }
              }
          }
      }
  }
  ```
  **注意**: ロックが持続する場合、再試行は問題を解決しない可能性があり、ロールバックが失敗する前に部分的な変更が適用された場合、不整合状態につながる可能性があります。再試行が冪等であるか安全であることを確認してください

#### 5. 例外を適切に処理
ロールバックが永続的なロックのために失敗した場合、データベース状態が不整合になる可能性があり、注意深い処理が必要です：

- **キャッチしてログに記録**:
  トランザクション呼び出しを try-catch ブロックでラップし、例外をログに記録し、管理者に通知します：
  ```java
  try {
      myService.performTransactionalWork();
  } catch (TransactionRollbackException e) {
      // エラーをログに記録
      logger.error("Transaction rollback failed after retries: " + e.getMessage(), e);
      // 管理者に通知（メールまたは監視システム経由）
      alertSystem.notify("Critical: Transaction rollback failure");
      // 安全に失敗するか安全な状態に入る
      throw new RuntimeException("Operation failed due to transaction issues", e);
  }
  ```

- **安全に失敗**: トランザクションの状態が不確実な場合、それに依存するさらなる操作を停止し、手動介入の必要性を通知します

#### 6. データベース機能を活用
ロック関連の問題を軽減するためにデータベース設定を調整します：

- **ロックタイムアウト**: ロック待機でデータベースが迅速にタイムアウトするように設定します（例：SQL Server の `SET LOCK_TIMEOUT 5000` または MySQL の `innodb_lock_wait_timeout`）。これにより、トランザクションが早期に失敗し、Spring が例外をより早く処理できるようになります
- **デッドロック検出**: データベースのデッドロック検出が有効で、1つのトランザクションを自動的にロールバックして競合を解決するように設定されていることを確認します
- **楽観的ロック**: JPA を使用している場合、エンティティに `@Version` を適用して楽観的ロックを使用し、物理的ロック競合を減らします：
  ```java
  @Entity
  public class MyEntity {
      @Id
      private Long id;
      @Version
      private Integer version;
      // 他のフィールド
  }
  ```
  これは競合検出をコミット時にシフトしますが、ロールバック失敗に直接対処するわけではありません

#### 7. 監視と調査
この例外が頻繁に発生する場合は、根本的な問題を示しています：

- **監視を追加**: Spring Boot Actuator やロギングフレームワークなどのツールを使用して、これらの例外とその頻度を追跡します
- **ログを分析**: ロックを引き起こす特定のクエリやトランザクションのパターンについて、データベースとアプリケーションログを確認します
- **並行性を調整**: 競合が持続する場合、アプリケーションの並行性モデルまたはデータベース設計を見直します

---

### ロールバックが失敗する理由
20回の試行後のロールバック失敗は、Spring のトランザクションマネージャーが、ロックされたリソースまたは失われた接続に遭遇したときにロールバック操作を再試行し、最終的にあきらめることを示唆しています。これは以下が原因である可能性があります：

- **永続的なロック**: 別のトランザクションが再試行ウィンドウ内に解放しないロックを保持している
- **接続問題**: データベース接続プール（HikariCP など）が接続を取得する再試行を尽くしている
- **データベース設定ミス**: データベースまたは接続プールのタイムアウトまたは再試行設定が過度に積極的または不十分

---

### 推奨アプローチ
上記の戦略を組み合わせた実用的なソリューションを以下に示します：

1. **トランザクションとクエリを最適化**: トランザクションを短く保ち、クエリを効率的にしてロック期間を短縮します
2. **トランザクションタイムアウトを設定**: ロックが持続する場合に迅速に失敗するために `@Transactional(timeout = 5)` を使用します
3. **再試行と回復で処理**:
   ```java
   @Service
   public class MyService {
       @Autowired
       private MyRepository repository;

       public void executeOperationWithRetry() {
           int maxAttempts = 3;
           for (int i = 0; i < maxAttempts; i++) {
               try {
                   performTransactionalWork();
                   return;
               } catch (TransactionRollbackException e) {
                   if (i == maxAttempts - 1) {
                       logger.error("Failed after {} attempts: {}", maxAttempts, e.getMessage(), e);
                       alertSystem.notify("Transaction rollback failure");
                       throw e;
                   }
                   try {
                       Thread.sleep(1000); // 再試行前に待機
                   } catch (InterruptedException ie) {
                       Thread.currentThread().interrupt();
                   }
               }
           }
       }

       @Transactional
       private void performTransactionalWork() {
           // データベース操作
           repository.save(someEntity);
       }
   }
   ```
4. **監視と調整**: 例外をログに記録し、アラートを設定し、ロック競合の原因を調査します

---

### 結論
Spring で別のトランザクションがロックを保持しているために接続取得失敗と繰り返しの試行を引き起こす `SqlTransactionRollbackException` を処理するには、短いトランザクションと最適化されたクエリによるロック競合の最小化に焦点を当て、必要に応じてトランザクション設定を調整し、より高いレベルで注意深い再試行ロジックを実装し、例外を適切にログ記録および通知して処理します。これにより、根本原因を時間をかけて監視および調整しながら、システムの安定性とデータ整合性が確保されます。

---

IBM DB2 Java ドライバ（具体的には JDBC ドライバ）を扱う場合、トランザクションロールバックシナリオの処理は、堅牢なデータベース対話に不可欠です。クエリで言及されている `SqlTransactionRollbackException` は、軽微なスペルミスのようです。標準的な JDBC、特にバージョン 4.0 以降（現代の IBM DB2 ドライバ `db2jcc4.jar` でサポート）では、正しい例外は **`SQLTransactionRollbackException`** です。この例外は `SQLException` のサブクラスであり、デッドロックやタイムアウトなどの場合にデータベーストランザクションが自動的にロールバックされたときにスローされます。

IBM DB2 JDBC ドライバを使用する際に Java コードで `SQLTransactionRollbackException` を効果的に処理する方法を以下に示します：

### 例外処理のアプローチ

1. **Try-Catch ブロックを使用**: トランザクショナルなデータベース操作を `try` ブロックでラップし、`SQLTransactionRollbackException` をキャッチして、データベースによってトランザクションがロールバックされた場合を処理します
2. **適切なアクションを実行**: アプリケーションの要件に応じて、エラーをログに記録したり、トランザクションを再試行したり（デッドロックなどの一時的な問題の場合）、ユーザーに失敗を通知したりする可能性があります
3. **リソースクリーンアップを確保**: リソースリークを避けるために、データベースリソース（接続のクローズなど）を `finally` ブロックで適切に管理します
4. **古いドライバのフォールバック**: JDBC 4.0 をサポートしていない古い DB2 ドライバを使用している場合、`SQLException` をキャッチし、エラーコード（DB2 でのデッドロックによるロールバックの場合 `-911`）をチェックする必要があるかもしれません

### コード例

`SQLTransactionRollbackException` を処理する実用的な例を以下に示します：

```java
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.SQLTransactionRollbackException;
import javax.sql.DataSource;

public class DB2TransactionExample {
    public void performTransaction(DataSource dataSource) {
        Connection conn = null;
        try {
            // 接続を取得し、自動コミットを無効にしてトランザクションを開始
            conn = dataSource.getConnection();
            conn.setAutoCommit(false);

            // ここでデータベース操作を実行
            // 例：INSERT、UPDATE などの文を実行

            // すべての操作が成功した場合、トランザクションをコミット
            conn.commit();
        } catch (SQLTransactionRollbackException e) {
            // DB2 によってトランザクションがロールバックされた場合を処理
            System.err.println("Transaction rolled back by the database: " + e.getMessage());
            System.err.println("SQL State: " + e.getSQLState() + ", Error Code: " + e.getErrorCode());
            // 例：SQLState '40001' および ErrorCode -911 は DB2 でのデッドロックまたはタイムアウトを示す
            // オプションでトランザクションを再試行またはユーザーに通知
        } catch (SQLException e) {
            // 他の SQL 例外を処理
            System.err.println("SQL Error: " + e.getMessage());
            // トランザクションがまだアクティブな場合、手動でロールバックを試みる
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("Transaction rolled back manually.");
                } catch (SQLException rollbackEx) {
                    System.err.println("Rollback failed: " + rollbackEx.getMessage());
                }
            }
        } finally {
            // リソースをクリーンアップ
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // デフォルトの動作を復元
                    conn.close();
                } catch (SQLException closeEx) {
                    System.err.println("Failed to close connection: " + closeEx.getMessage());
                }
            }
        }
    }
}
```

### コードの重要なポイント

- **`SQLTransactionRollbackException` のキャッチ**: これにより、DB2 がトランザクションをロールバックする場合（エラーコード `-911` または SQL 状態 `40001` で示されるデッドロックなど）を具体的にキャッチします
- **一般的な `SQLException` キャッチ**: 他のデータベースエラーのためのフォールバックとして機能し、より広範なエラー処理を確保します
- **手動ロールバック**: `SQLException` が発生し、トランザクションが自動的にロールバックされていない場合、手動ロールバックを試みます
- **リソース管理**: `finally` ブロックは接続が閉じられることを確保し、リソースリークを防止します

### 追加の考慮事項

- **ドライババージョン**: JDBC 4.0 準拠の IBM DB2 ドライバ（`db2jcc4.jar` など）を使用していることを確認してください。古いドライバ（`db2jcc.jar` など）は `SQLException` のみをスローする可能性があり、エラーコードを手動でチェックする必要があります。例：
  ```java
  catch (SQLException e) {
      if (e.getErrorCode() == -911) {
          // デッドロックまたはタイムアウトによるトランザクションロールバックを処理
      }
  }
  ```
- **SQL 状態とエラーコード**: DB2 はシリアル化失敗（デッドロックなど）に SQL 状態 `40001` を使用し、トランザクションが自動的にロールバックされるときにエラーコード `-911` を使用します。エラーコード `-913` はデッドロックによる文の失敗を示しますが、トランザクションは明示的にロールバックされるまでアクティブのままです
- **再試行ロジック**: デッドロックなどの一時的な問題に対して、再試行メカニズムを実装する可能性があります：
  ```java
  int maxRetries = 3;
  for (int attempt = 1; attempt <= maxRetries; attempt++) {
      try {
          performTransaction(dataSource);
          break; // 成功、ループを終了
      } catch (SQLTransactionRollbackException e) {
          if (attempt == maxRetries) {
              throw e; // 最大再試行後に再スロー
          }
          Thread.sleep(1000 * attempt); // 再試行前にバックオフ
      }
  }
  ```

### 結論

IBM DB2 Java ドライバで `SQLTransactionRollbackException`（正しくは `SQLTransactionRollbackException`）を処理するには、トランザクションロールバックシナリオに対してこの特定の例外をキャッチするために `try-catch` ブロックを使用します。適切なリソース管理と組み合わせ、必要に応じて `-911` などのエラーコードをチェックする古いドライバのフォールバックロジックを含めます。このアプローチにより、アプリケーションはトランザクションロールバックを適切に処理し、データベース整合性とユーザーエクスペリエンスを維持します。