---
audio: false
generated: true
lang: ja
layout: post
title: Oracle JDBCドライバ
translated: true
type: note
---

Oracle JDBC (Java Database Connectivity) ドライバは、JavaアプリケーションがOracleデータベースに接続し、操作することを可能にします。主要なコンポーネントと使用方法について説明します。

Oracle JDBC接続のメインクラスは `oracle.jdbc.driver.OracleDriver` ですが、新しいバージョンでは `oracle.jdbc.OracleDriver` をよく使用します（これはOracle 10g以降で推奨されているクラスです）。

以下はJavaアプリケーションでOracle JDBCを使用する方法です：

1. まず、プロジェクトにOracle JDBCドライバのJAR（通常はojdbc.jar）を含める必要があります。

2. ドライバクラスをロードします：
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. 接続URLを使用して接続を確立します：
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// またはサービス名ベースの接続の場合
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. ステートメントを作成して実行します：
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // 各行を処理
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. 完了したら必ずリソースをクローズします：
```java
resultSet.close();
statement.close();
connection.close();
```

Oracle JDBCドライバにはいくつかの種類があります：
- Thinドライバ：Oracleクライアントのインストールを必要としないPure Java実装
- OCIドライバ：Oracle Call Interfaceを使用し、Oracleクライアントソフトウェアが必要
- Kerberosドライバ：Kerberos認証用
- JDBC-OCIドライバ：JDBCとOCIの組み合わせ

Thinドライバは、クライアントマシンに追加のOracleクライアントソフトウェアを必要としないため、最も一般的に使用されます。

コネクションプーリング、プリペアドステートメント、またはOracle JDBC使用法の他の側面について、より具体的な情報が必要ですか？