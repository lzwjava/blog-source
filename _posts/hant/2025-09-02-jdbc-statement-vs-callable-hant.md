---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JDBC 中的 Statement 與 CallableStatement 比較
translated: true
type: note
---

在 Java 的 JDBC（以及基於它構建的其他框架，如 Hibernate 或 Spring）中，**`Statement`** 和 **`CallableStatement`** 這兩個概念都是用於向數據庫發送 SQL 命令的接口，但它們的用途不同。

---

### 1. `Statement`

* **用途**：用於執行不帶參數的簡單 SQL 查詢。
* **使用方法**：從 `Connection` 創建一個 `Statement` 對象，並用它來執行 SQL 字符串。
* **典型方法**：

  * `executeQuery(sql)` → 用於 `SELECT` 查詢，返回一個 `ResultSet`。
  * `executeUpdate(sql)` → 用於 `INSERT`、`UPDATE`、`DELETE`。
  * `execute(sql)` → 通用方法，如果結果是 `ResultSet` 則返回 `true`。

**範例**：

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **使用時機**：適用於沒有參數的靜態 SQL 語句。
* **缺點**：如果與動態用戶輸入一起使用，可能導致 SQL 注入。

---

### 2. `CallableStatement`

* **用途**：用於執行數據庫中的**存儲過程**。
* **使用方法**：通過 `Connection.prepareCall()` 創建，允許調用具有 **IN**、**OUT** 和 **INOUT** 參數的數據庫例程。
* **典型方法**：

  * `setInt`、`setString` 等 → 用於設置輸入參數。
  * `registerOutParameter` → 用於註冊輸出參數。
  * `execute()` 或 `executeQuery()` → 用於運行存儲過程。
  * `getInt`、`getString` 等 → 用於檢索輸出值。

**範例**：

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// 設置 IN 參數
cstmt.setInt(1, 101);

// 註冊 OUT 參數
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// 執行
cstmt.execute();

// 獲取 OUT 參數
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **使用時機**：適用於封裝在數據庫中的存儲過程/函數。
* **優點**：支持複雜邏輯、多個結果集和輸入/輸出參數。

---

### 主要區別（不使用表格）

* `Statement` 用於**靜態 SQL**（即席查詢）。
* `CallableStatement` 用於**存儲過程/函數**。
* `Statement` 直接執行 SQL，而 `CallableStatement` 與可能返回多個結果集和參數的數據庫例程交互。
* `Statement` 簡單但與動態輸入一起使用時安全性較低，而 `CallableStatement` 提供了一種結構化的方式來調用數據庫中可重用的邏輯。

---

👉 如果你需要，我也可以解釋 **`PreparedStatement`** 如何在這兩者之間定位（更安全、參數化的 SQL，但不適用於存儲過程）。你想讓我補充這部分嗎？