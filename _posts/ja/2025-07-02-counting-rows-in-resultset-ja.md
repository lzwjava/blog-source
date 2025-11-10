---
audio: false
generated: true
lang: ja
layout: post
title: スクロール可能な結果セットにおける行数のカウント
translated: true
type: note
---

Javaにおいて、`ResultSet`（例: `Statement.executeQuery()`を通じて）を操作する際、`fetchSize`が`0`に設定されている場合（JDBCドライバが必要に応じて行を取得することを意味する）、行数のカウントは難しい場合があります。さらに、スクロール可能な結果セット（`ResultSet.TYPE_SCROLL_INSENSITIVE`または`ResultSet.TYPE_SCROLL_SENSITIVE`を使用）を使用すると、結果セット内を移動できますが、行がメモリに読み込まれるため、より多くのメモリを必要とします。

以下は、結果セットを完全に走査せずに`ResultSet`の行数をカウントするために使用できる戦略です。これは、`ResultSet`の`scrollable`機能と、「最後の行に移動する」および「行番号を取得する」機能を利用します。

### スクロール可能な`ResultSet`を使用して行数をカウントする手順:

1. **スクロール可能なResultSetを作成**: 適切なカーソルタイプを設定して、スクロール可能な結果セットを生成できる`Statement`を使用するようにします。
2. **最後の行に移動**: スクロール可能な結果セットでは、`last()`を使用して最後の行に移動できます。
3. **行番号を取得**: 最後の行に移動した後、`getRow()`を呼び出して行数を決定できます。
4. **オプション**: 結果セットを反復処理する必要がある場合は、`first()`を使用して最初の行に戻ります。

以下はJavaでの実装例です:

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
            
            // 最後の行に移動して総行数をカウント
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // オプションで最初の行に戻る
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

### 主なポイント:

* **スクロール可能なResultSet**: `ResultSet.TYPE_SCROLL_INSENSITIVE`を使用してスクロール可能な`ResultSet`を作成します。このタイプの結果セットでは、最後の行に移動して行数を取得できます。
* **行数**: `rs.getRow()`メソッドは、カーソルが最後の行に位置しているときの現在の行番号を返します。この値は事実上、結果セット内の総行数です。
* **フェッチサイズ**: `fetchSize`が`0`の場合、ドライバは動的に行を取得しますが、スクロール可能な結果セットを使用することで、行を効率的に移動できます。

### ベストプラクティス:

* **メモリ効率**: スクロール可能な結果セットは行数をカウントするのに便利ですが、すべての行をメモリに読み込む必要があるため、より多くのメモリを消費する可能性があります。大規模なデータセットを扱う場合、メモリ使用量が懸念される場合は、（`last()`を使用せずに結果セットを反復処理して行数をインクリメンタルにカウントするなど）別のアプローチを検討してください。
* **代替アプローチ**: メモリが問題であり、行数のみが必要な場合は、結果セット全体を取得する代わりに`SELECT COUNT(*)`クエリを実行できます。これは多くの場合、より効率的です。

```sql
SELECT COUNT(*) FROM your_table;
```

さらに説明が必要な場合はお知らせください！