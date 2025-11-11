---
audio: false
generated: true
lang: hant
layout: post
title: Oracle JDBC 驅動程式
translated: true
type: note
---

Oracle JDBC（Java 資料庫連接）驅動程式允許 Java 應用程式連接並與 Oracle 資料庫進行互動。讓我說明關鍵組件及使用方法。

Oracle JDBC 連接的主要類別是 `oracle.jdbc.driver.OracleDriver`，但在較新版本中通常會使用 `oracle.jdbc.OracleDriver`（這是自 Oracle 10g 起推薦使用的類別）。

以下是在 Java 應用程式中使用 Oracle JDBC 的方法：

1. 首先，您需要在專案中包含 Oracle JDBC 驅動程式 JAR（通常是 ojdbc.jar）。

2. 載入驅動程式類別：
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. 使用連接 URL 建立連接：
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// 或使用服務名稱進行連接
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. 建立並執行語句：
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // 處理每一行資料
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. 完成後務必關閉資源：
```java
resultSet.close();
statement.close();
connection.close();
```

Oracle JDBC 驅動程式分為以下幾種類型：
- Thin 驅動程式：純 Java 實現，無需安裝 Oracle 客戶端
- OCI 驅動程式：使用 Oracle Call Interface，需要 Oracle 客戶端軟體
- Kerberos 驅動程式：用於 Kerberos 身份驗證
- JDBC-OCI 驅動程式：結合 JDBC 與 OCI

由於 Thin 驅動程式無需在客戶端機器上安裝額外的 Oracle 客戶端軟體，因此最常被使用。

您是否需要有關連接池、預編譯語句或 Oracle JDBC 使用其他方面的具體資訊？