---
audio: false
generated: true
lang: hant
layout: post
title: 死鎖創製
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

    private static final String DB_URL = "jdbc:sqlite:deadlock_example.db"; // 使用 SQLite 以簡化示範
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
        System.out.println("\n資料表最終狀態:");
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
                conn.setAutoCommit(false); // 開始交易

                System.out.println(Thread.currentThread().getName() + ": 鎖定 id " + id1 + " 的資料列");
                try (PreparedStatement pstmt1 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt1.setString(1, value1);
                    pstmt1.setInt(2, id1);
                    pstmt1.executeUpdate();
                }
                Thread.sleep(100); // 加入短暫延遲

                System.out.println(Thread.currentThread().getName() + ": 鎖定 id " + id2 + " 的資料列");
                try (PreparedStatement pstmt2 = conn.prepareStatement(UPDATE_ITEM_SQL)) {
                    pstmt2.setString(1, value2);
                    pstmt2.setInt(2, id2);
                    pstmt2.executeUpdate();
                }

                conn.commit();
                System.out.println(Thread.currentThread().getName() + ": 交易成功提交");

            } catch (SQLException e) {
                if (conn != null) {
                    try {
                        conn.rollback();
                        System.err.println(Thread.currentThread().getName() + ": 交易因錯誤而回滾: " + e.getMessage());
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
                        conn.setAutoCommit(true); // 重設自動提交
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

**說明：**

1.  **數據庫設置：**
    * `DB_URL`：指定 SQLite 數據庫文件的連接 URL（`deadlock_example.db`）。
    * `CREATE_TABLE_SQL`、`INSERT_ITEM_SQL`、`UPDATE_ITEM_SQL`：定義用於創建表、插入初始數據和更新行的 SQL 語句。
    * `createTableAndInitialData()`：如果 `items` 表不存在則創建它，並插入兩個初始行，ID 分別為 1 和 2。

2.  **並行更新：**
    * `ExecutorService`：創建一個具有 2 個固定線程池的 `ExecutorService`，以模擬兩個任務的並行執行。
    * `UpdateTask`：此內部類實現了 `Runnable` 接口。每個 `UpdateTask` 實例代表一個嘗試更新兩行數據的事務。
        * 構造函數接收要更新的兩行數據的 ID 和新值。
        * `run()` 方法執行以下操作：
            * 建立數據庫連接。
            * 設置 `conn.setAutoCommit(false)` 以開始顯式事務。
            * **第一次更新：** 對第一行（`id1`）執行 `UPDATE` 語句。
            * `Thread.sleep(100)`：引入短暫延遲以增加死鎖的機會。這允許第一個線程在第二個線程嘗試獲取鎖之前獲取第一行的鎖。
            * **第二次更新：** 對第二行（`id2`）執行 `UPDATE` 語句。
            * `conn.commit()`：嘗試提交事務。
            * **錯誤處理：** 包含一個 `try-catch` 塊來處理 `SQLException`。如果發生異常（可能是死鎖），它會嘗試使用 `conn.rollback()` 回滾事務。
            * **Finally 塊：** 確保連接關閉並將 `autoCommit` 重設為 `true`。

3.  **衝突順序：**
    * 在 `main` 方法中，兩個 `UpdateTask` 實例被提交給執行器：
        * 第一個任務嘗試更新第 1 行，然後是第 2 行。
        * 第二個任務嘗試更新第 2 行，然後是第 1 行。
    * 這種對相同資源（`items` 表中的行）獲取鎖的衝突順序是可能導致死鎖的條件。

4.  **執行與輸出：**
    * `executor.shutdown()` 和 `executor.awaitTermination()`：確保執行器等待兩個任務完成。
    * `printFinalData()`：在線程完成後，此方法打印 `items` 行的最終內容以觀察結果。

**如何運行：**

1.  **儲存：** 將代碼儲存為 `DeadlockGenerator.java`。
2.  **編譯：** 使用 Java 編譯器編譯代碼：`javac DeadlockGenerator.java`
3.  **執行：** 運行編譯後的代碼：`java DeadlockGenerator`

**預期結果：**

當你運行此代碼時，很可能會看到類似以下的輸出（確切的輸出可能會根據時機和數據庫系統的死鎖檢測而略有不同）：

```
Thread-0: 鎖定 id 1 的資料列
Thread-1: 鎖定 id 2 的資料列
Thread-0: 鎖定 id 2 的資料列
Thread-1: 鎖定 id 1 的資料列
Thread-1: 交易因錯誤而回滾: database is locked
Thread-0: 交易成功提交

資料表最終狀態:
ID: 1, Value: Updated Value 1 - Thread 0
ID: 2, Value: Updated Value 2 - Thread 0
```

或者有時 Thread-0 可能會被回滾。關鍵觀察點是其中一個線程將遇到指示鎖衝突或死鎖的 `SQLException`，並且其事務將被回滾。另一個線程通常會成功。

**重要注意事項：**

*   **數據庫系統：** 此示例使用 SQLite 以簡化示範。使用其他數據庫系統（如 PostgreSQL、MySQL 等）時，行為和錯誤訊息可能會有所不同。您可能需要調整 JDBC 驅動程序 URL 以及可能的 SQL 語句。
*   **隔離級別：** 數據庫的默認事務隔離級別會影響死鎖的可能性。較高的隔離級別可能會使死鎖更頻繁地發生。
*   **延遲：** `Thread.sleep()` 對於演示死鎖至關重要。沒有它，一個事務可能會在另一個事務有機會獲取第一個鎖之前完成。
*   **錯誤處理：** 在實際應用中，您應該具有健全的錯誤處理機制，並可能為因死鎖而失敗的事務實施重試機制。