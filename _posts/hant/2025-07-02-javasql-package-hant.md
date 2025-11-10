---
audio: false
generated: true
lang: hant
layout: post
title: Java SQL 數據庫連接
translated: true
type: note
---

`java.sql` 套件是 **Java JDBC API（Java 數據庫連接）的核心部分**，讓 Java 應用程式能夠與關聯式數據庫（如 MySQL、PostgreSQL、Oracle、SQL Server 等）進行互動。它提供了**連接數據庫、執行 SQL 查詢及檢索結果**所需的介面與類別。

---

## 📘 **`java.sql` 概覽**

`java.sql` 套件包含以下類別與介面：

* 連接數據庫（`DriverManager`、`Connection`）
* 執行 SQL 查詢（`Statement`、`PreparedStatement`、`CallableStatement`）
* 處理結果（`ResultSet`）
* 處理元數據（`DatabaseMetaData`、`ResultSetMetaData`）
* 管理交易
* 處理 SQL 異常（`SQLException`）

---

## 🔧 **設定：所需準備**

### 1. **JDBC 驅動程式**

* 你需要目標數據庫的 JDBC 驅動程式（例如 MySQL：`mysql-connector-java`，PostgreSQL：`postgresql`）。
* 可透過 Maven/Gradle 加入，或手動添加 `.jar` 檔案。

### 2. **數據庫 URL**

每個 JDBC 驅動程式都有其連接 URL 格式：

```java
jdbc:mysql://localhost:3306/mydatabase
jdbc:postgresql://localhost:5432/mydatabase
```

---

## 🧩 **主要類別與介面**

### 🔌 1. `DriverManager`

建立與數據庫的連接。

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

### 🧵 2. `Connection`

代表與數據庫的會話。

* 建立 `Statement` 或 `PreparedStatement`
* 管理交易（commit、rollback）
* 關閉連接

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // 用於手動交易控制
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

用於執行靜態 SQL 查詢。

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

#### `PreparedStatement`

用於執行參數化查詢。避免 SQL 注入攻擊。

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

用於儲存過程。

```java
CallableStatement cs = conn.prepareCall("{call getUser(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

儲存查詢結果。

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

### 📚 5. 元數據

* `DatabaseMetaData`：數據庫資訊
* `ResultSetMetaData`：結果欄位資訊

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **基礎範例**

```java
import java.sql.*;

public class JdbcExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            String sql = "SELECT * FROM users WHERE age > ?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setInt(1, 18);

            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " - " + rs.getString("name"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🔁 **交易處理**

```java
conn.setAutoCommit(false);  // 停用自動提交

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // 提交交易

} catch (SQLException ex) {
    conn.rollback(); // 發生錯誤時回滾
}
```

---

## ❗ **異常處理**

```java
try {
    // 數據庫程式碼
} catch (SQLException ex) {
    System.err.println("Error Code: " + ex.getErrorCode());
    System.err.println("SQL State: " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **`java.sql` 實用功能**

| 功能              | 介面/類別                     | 用途                                      |
| ----------------- | ----------------------------- | ----------------------------------------- |
| 元數據            | `DatabaseMetaData`            | 數據庫版本、支援功能、資料表等            |
| 結果欄位資訊      | `ResultSetMetaData`           | 欄位數量、類型、標籤等                    |
| BLOB/CLOB 處理    | `Blob`、`Clob`                | 儲存/檢索大型二進位/文字資料              |
| 批次執行          | `addBatch()`、`executeBatch()` | 同時執行多個語句                          |
| 可滾動 ResultSet  | `ResultSet.TYPE_SCROLL_INSENSITIVE` | 前後移動游標                          |
| 可更新 ResultSet  | `ResultSet.CONCUR_UPDATABLE`  | 直接在 `ResultSet` 中修改列               |

---

## 📦 **Maven 依賴範例（MySQL）**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **最佳實踐**

* 始終在 `finally` 區塊中關閉 `Connection`、`Statement`、`ResultSet`，或使用 try-with-resources。
* 使用 `PreparedStatement` 而非 `Statement` 以防止 SQL 注入攻擊。
* 在生產環境中使用連接池（透過 HikariCP、Apache DBCP 等函式庫）。
* 對多個相關查詢使用交易處理。
* 不要在業務邏輯中硬編碼 SQL — 考慮使用 DAO 或 ORM 模式（如 JPA、Hibernate）。

---

## 🧮 **進階主題**

* **RowSet**：斷開連接的 ResultSet 版本（`javax.sql.rowset`）
* **連接池**：使用帶有池的 `DataSource`
* **JDBC 4+ 功能**：自動加載驅動程式、try-with-resources 支援
* **JDBC + Spring**：與 Spring JDBC Template 整合
* **JDBC + ORM**：在 Hibernate、JPA、MyBatis 底層使用 `java.sql`

---

## 🧾 **摘要表格**

| 任務               | 類別/介面                     |
| ------------------ | ----------------------------- |
| 連接數據庫         | `DriverManager`、`Connection` |
| 執行 SQL           | `Statement`、`PreparedStatement` |
| 儲存過程           | `CallableStatement`           |
| 讀取結果           | `ResultSet`                   |
| 數據庫資訊         | `DatabaseMetaData`            |
| 欄位資訊           | `ResultSetMetaData`           |
| 交易處理           | `Connection.commit()`、`rollback()` |
| 異常處理           | `SQLException`                |

---

如果你需要，我還可以提供：

* 速查表
* DAO 風格的可重用封裝類別
* 真實數據庫範例（MySQL/PostgreSQL）

告訴我吧！