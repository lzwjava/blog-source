---
audio: false
generated: true
lang: hant
layout: post
title: 滾動結果集中的行數統計
translated: true
type: note
---

在 Java 中，當你處理 `ResultSet`（例如透過 `Statement.executeQuery()`）時，若 `fetchSize` 設為 `0`（表示 JDBC 驅動程式會按需獲取資料列），計算資料列數目可能會變得棘手。此外，使用可捲動的結果集（透過 `ResultSet.TYPE_SCROLL_INSENSITIVE` 或 `ResultSet.TYPE_SCROLL_SENSITIVE`）雖可讓你在結果集中導航，但由於所有資料列都會載入記憶體，因此需要更多記憶體空間。

以下是一種無需完整遍歷結果集即可計算 `ResultSet` 資料列數量的策略。它利用了 `ResultSet` 的可捲動特性，以及「跳至最後一列」與「取得資料列編號」的功能。

### 使用可捲動 `ResultSet` 計算資料列數的步驟：

1. **建立可捲動 ResultSet**：透過設定適當的游標類型，確保使用能產生可捲動結果集的 `Statement`
2. **移至最後一列**：可捲動結果集允許使用 `last()` 跳至最後一列
3. **取得資料列編號**：移至最後一列後，可呼叫 `getRow()` 來確定總資料列數
4. **可選步驟**：若需遍歷結果集，可使用 `first()` 返回第一列

以下是 Java 的實作範例：

```java
import java.sql.*;

public class RowCountExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/your_database";
        String username = "your_username";
        String password = "your_password";
        
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            conn = DriverManager.getConnection(url, username, password);
            stmt = conn.createStatement(
                    ResultSet.TYPE_SCROLL_INSENSITIVE, 
                    ResultSet.CONCUR_READ_ONLY);
            rs = stmt.executeQuery("SELECT * FROM your_table");
            
            // 移至最後一列以計算總資料列數
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // 可選步驟：返回第一列
                rs.first();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### 關鍵要點：

* **可捲動 ResultSet**：我們使用 `ResultSet.TYPE_SCROLL_INSENSITIVE` 建立可捲動的 `ResultSet`。此類結果集允許移至最後一列並取得資料列計數
* **資料列計數**：當游標定位於最後一列時，`rs.getRow()` 方法會傳回當前資料列編號，此值即為結果集中的總資料列數
* **獲取大小**：若 `fetchSize` 為 `0`，驅動程式會動態獲取資料列，但使用可捲動結果集能讓我們有效率地導航資料列

### 最佳實踐：

* **記憶體效率**：雖然可捲動結果集適用於計算資料列數，但請注意它們可能消耗更多記憶體，因為所有資料列都需載入記憶體。若處理大型資料集且需考慮記憶體使用量，可考慮改用其他方法（例如不使用 `last()` 逐步遍歷結果集來計數）
* **替代方案**：若記憶體有限且僅需資料列計數，可改為執行 `SELECT COUNT(*)` 查詢，這通常更有效率

```sql
SELECT COUNT(*) FROM your_table;
```

如需進一步說明，請隨時告知！