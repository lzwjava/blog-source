---
audio: false
generated: true
lang: ja
layout: post
title: デッドロック・クリエイションズ
translated: true
type: note
---

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class DeadlockGenerator {

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // 簡略化のためSQLiteを使用
    private static final String CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value TEXT)";
    private static final String INSERT_ITEM_SQL = "INSERT OR IGNORE INTO items (id, value) VALUES (?, ?)";
    private static final String UPDATE_ITEM_SQL = "UPDATE items SET value = ? WHERE id = ?";

    public static void main(String[] args) throws InterruptedException {
        createTableAndInitialData();

        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(new UpdateTask(1, "Updated Value 1 - Thread 1", 2, "Updated Value 2 - Thread 1"));
        executor.submit(new UpdateTask(2, "Updated Value 2 - Thread 2", 1, "Updated Value 1 - Thread 2"));

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);

        printFinalData();
    }

    private static void createTableAndInitialData() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             java.sql.Statement stmt = conn.createStatement()) {
            stmt.execute(CREATE_TABLE_SQL);
            try (PreparedStatement pstmt = conn.prepareStatement(INSERT_ITEM_SQL)) {
                pstmt.setInt(1, 1);
                pstmt.setString(2, "Value 1");
                pstmt.executeUpdate();
                pstmt.setInt(1, 2);
                pstmt.setString(2, "Value 2");
                pstmt.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void printFinalData() {
        System.out.println("\nテーブルの最終状態:");
        try (Connection conn = DriverManager.getConnection(DB_URL);
             java.sql.Statement stmt = conn.createStatement();
             java.sql.ResultSet rs = stmt.executeQuery("SELECT * FROM items")) {
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") + ", Value: " + rs.getString("value"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static class UpdateTask implements Runnable {
        private final int id1;
        private final String value1;
        private final int id2;
        private final String value2;

        public UpdateTask(int id1, String value1, int id2, String value2) {
            this.id1 = id1;
            this.value1 = value1;
            this.id2 = id2;
            this.value2 = value2;
        }

        @Override
        public void run() {
            Connection conn = null;
            try {
                conn = DriverManager.getConnection(DB_URL);
                conn.setAutoCommit(false); // トランザクション開始

                System.out.println(Thread.currentThread().getName() + ": ID " + id1 + " の行をロック中");
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // 小さな遅延を導入

                System.out.println(Thread.currentThread().getName() + ": ID " + id2 + " の行をロック中");
                try (PreparedStatement pstmt2 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt2.setString(1, value2);
                    pstmt2.setInt(2, id2);
                    pstmt2.executeUpdate();
                }

                conn.commit();
                System.out.println(Thread.currentThread().getName() + ": トランザクションが正常にコミットされました");

            } catch (SQLException e) {
                if (conn != null) {
                    try {
                        conn.rollback();
                        System.err.println(Thread.currentThread().getName() + ": エラーによりトランザクションがロールバックされました: " + e.getMessage());
                    } catch (SQLException rollbackException) {
                        rollbackException.printStackTrace();
                    }
                } else {
                    e.printStackTrace();
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                if (conn != null) {
                    try {
                        conn.setAutoCommit(true); // 自動コミットをリセット
                        conn.close();
                    } catch (SQLException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
```

**説明:**

1.  **データベース設定:**
    * `DB_URL`: SQLiteデータベースファイル（`deadlock_example.db`）への接続URLを指定
    * `CREATE_TABLE_SQL`, `INSERT_ITEM_SQL`, `UPDATE_ITEM_SQL`: テーブル作成、初期データ挿入、行更新のためのSQL文を定義
    * `createTableAndInitialData()`: `items`テーブルが存在しない場合は作成し、ID 1と2の2つの初期行を挿入

2.  **並行更新:**
    * `ExecutorService`: 2つの固定スレッドプールを持つ`ExecutorService`を作成し、2つのタスクの並行実行をシミュレート
    * `UpdateTask`: この内部クラスは`Runnable`インターフェースを実装。各`UpdateTask`インスタンスは2つの行を更新しようとするトランザクションを表す
        * コンストラクタは更新する2つの行のIDと新しい値を受け取る
        * `run()`メソッドは以下を実行:
            * データベース接続を確立
            * `conn.setAutoCommit(false)`で明示的なトランザクションを開始
            * **最初の更新:** 最初の行（`id1`）に対して`UPDATE`文を実行
            * `Thread.sleep(100)`: デッドロックの発生確率を高めるための小さな遅延を導入。これにより、2番目のスレッドがロックを取得しようとする前に、最初のスレッドが最初の行のロックを取得できる
            * **2番目の更新:** 2番目の行（`id2`）に対して`UPDATE`文を実行
            * `conn.commit()`: トランザクションのコミットを試行
            * **エラーハンドリング:** `SQLException`を処理する`try-catch`ブロックを含む。例外（デッドロックの可能性あり）が発生した場合、`conn.rollback()`を使用してトランザクションのロールバックを試行
            * **Finallyブロック:** 接続が確実に閉じられ、`autoCommit`が`true`にリセットされることを保証

3.  **競合する順序:**
    * `main`メソッドで、2つの`UpdateTask`インスタンスがexecutorに送信される:
        * 最初のタスクは行1、次に行2を更新しようとする
        * 2番目のタスクは行2、次に行1を更新しようとする
    * 同じリソース（`items`テーブルの行）に対するロック取得のこの競合順序が、デッドロックを引き起こす可能性のある条件

4.  **実行と出力:**
    * `executor.shutdown()`と`executor.awaitTermination()`: executorが両方のタスクの完了を待つことを保証
    * `printFinalData()`: スレッドが終了した後、このメソッドは結果を観察するために`items`テーブルの最終内容を表示

**実行方法:**

1.  **保存:** コードを`DeadlockGenerator.java`として保存
2.  **コンパイル:** Javaコンパイラを使用してコードをコンパイル: `javac DeadlockGenerator.java`
3.  **実行:** コンパイルされたコードを実行: `java DeadlockGenerator`

**予想される結果:**

このコードを実行すると、以下のような出力が表示される可能性が高い（正確な出力はタイミングとデータベースシステムのデッドロック検出によって若干異なる）:

```
Thread-0: ID 1 の行をロック中
Thread-1: ID 2 の行をロック中
Thread-0: ID 2 の行をロック中
Thread-1: ID 1 の行をロック中
Thread-1: エラーによりトランザクションがロールバックされました: database is locked
Thread-0: トランザクションが正常にコミットされました

テーブルの最終状態:
ID: 1, Value: Updated Value 1 - Thread 0
ID: 2, Value: Updated Value 2 - Thread 0
```

または、時々Thread-0がロールバックされることもある。重要な観察点は、一方のスレッドがロック競合またはデッドロックを示す`SQLException`に遭遇し、そのトランザクションがロールバックされることである。もう一方のスレッドは通常成功する。

**重要な注意点:**

*   **データベースシステム:** この例は簡略化のためSQLiteを使用。動作やエラーメッセージはPostgreSQL、MySQLなどの他のデータベースシステムでは異なる可能性がある。JDBCドライバーのURLやSQL文を調整する必要があるかもしれない
*   **分離レベル:** データベースのデフォルトのトランザクション分離レベルはデッドロックの発生確率に影響を与える可能性がある。高い分離レベルではデッドロックがより頻繁に発生する可能性がある
*   **遅延:** `Thread.sleep()`はデッドロックを実証するために重要。これがないと、一方のトランザクションが最初のロックを取得する機会を得る前に、もう一方のトランザクションが完了する可能性がある
*   **エラーハンドリング:** 実際のアプリケーションでは、堅牢なエラーハンドリングと、デッドロックにより失敗したトランザクションのための再試行メカニズムが必要