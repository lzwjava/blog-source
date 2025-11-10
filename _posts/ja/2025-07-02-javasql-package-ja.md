---
audio: false
generated: true
lang: ja
layout: post
title: Javaによるデータベース接続のためのSQL
translated: true
type: note
---

`java.sql`パッケージは、**JavaのJDBC API（Java Database Connectivity）のコア部分**であり、JavaアプリケーションがMySQL、PostgreSQL、Oracle、SQL Serverなどのリレーショナルデータベースと連携することを可能にします。このパッケージは、**データベースへの接続、SQLクエリの実行、結果の取得**に必要なインターフェースとクラスを提供します。

---

## 📘 **`java.sql`の概要**

`java.sql`パッケージには、以下のためのクラスとインターフェースが含まれています：

* データベースへの接続（`DriverManager`、`Connection`）
* SQLクエリの実行（`Statement`、`PreparedStatement`、`CallableStatement`）
* 結果の処理（`ResultSet`）
* メタデータの処理（`DatabaseMetaData`、`ResultSetMetaData`）
* トランザクションの管理
* SQL例外の処理（`SQLException`）

---

## 🔧 **セットアップ：必要なもの**

### 1. **JDBCドライバ**

* 対象のデータベース用のJDBCドライバが必要です（例：MySQL: `mysql-connector-java`、PostgreSQL: `postgresql`）。
* Maven/Gradle経由で含めるか、手動で`.jar`ファイルを追加できます。

### 2. **データベースURL**

各JDBCドライバには接続URLフォーマットがあります：

```java
jdbc:mysql://localhost:3306/mydatabase
jdbc:postgresql://localhost:5432/mydatabase
```

---

## 🧩 **主要なクラスとインターフェース**

### 🔌 1. `DriverManager`

データベースへの接続を確立します。

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

### 🧵 2. `Connection`

データベースとのセッションを表します。

* `Statement`または`PreparedStatement`の作成
* トランザクションの管理（コミット、ロールバック）
* 接続のクローズ

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // 手動トランザクション制御のため
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

静的なSQLクエリの実行に使用します。

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

#### `PreparedStatement`

パラメータ化されたクエリの実行に使用します。SQLインジェクションを防ぎます。

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

ストアドプロシージャに使用します。

```java
CallableStatement cs = conn.prepareCall("{call getUser(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

クエリの結果を保持します。

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

### 📚 5. メタデータ

* `DatabaseMetaData`: データベースに関する情報
* `ResultSetMetaData`: 結果のカラムに関する情報

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **基本的な例**

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

## 🔁 **トランザクション**

```java
conn.setAutoCommit(false);  // 自動コミットを無効化

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // トランザクションをコミット

} catch (SQLException ex) {
    conn.rollback(); // エラー時にロールバック
}
```

---

## ❗ **例外処理**

```java
try {
    // データベースコード
} catch (SQLException ex) {
    System.err.println("Error Code: " + ex.getErrorCode());
    System.err.println("SQL State: " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **`java.sql`の便利な機能**

| 機能              | インターフェース/クラス              | 目的                                         |
| ----------------- | ------------------------------------ | -------------------------------------------- |
| メタデータ        | `DatabaseMetaData`                   | DBバージョン、サポート機能、テーブルなど     |
| 結果カラム情報    | `ResultSetMetaData`                  | カラム数、型、ラベルなど                     |
| BLOB/CLOB処理     | `Blob`, `Clob`                       | 大きなバイナリ/テキストデータの保存/取得     |
| バッチ実行        | `addBatch()`, `executeBatch()`       | 複数のステートメントをまとめて実行           |
| スクロール可能ResultSet | `ResultSet.TYPE_SCROLL_INSENSITIVE` | カーソルを前後に移動                         |
| 更新可能ResultSet | `ResultSet.CONCUR_UPDATABLE`         | `ResultSet`内で直接行を変更                  |

---

## 📦 **Maven依存関係の例（MySQL）**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **ベストプラクティス**

* `Connection`、`Statement`、`ResultSet`は常に`finally`ブロックでクローズするか、try-with-resourcesを使用してください。
* SQLインジェクションを防ぐため、`Statement`よりも`PreparedStatement`を使用してください。
* 本番環境では（HikariCP、Apache DBCPなどのライブラリを介して）コネクションプーリングを使用してください。
* 複数の関連するクエリにはトランザクションを使用してください。
* ビジネスロジックにSQLをハードコードしないでください — DAOやORMパターン（JPA、Hibernateなど）を検討してください。

---

## 🧮 **高度なトピック**

* **RowSet**: 接続が切断された状態のResultSet（`javax.sql.rowset`）
* **コネクションプーリング**: プールと共に`DataSource`を使用
* **JDBC 4+ の機能**: ドライバーの自動ロード、try-with-resourcesのサポート
* **JDBC + Spring**: Spring JDBC Templateとの統合
* **JDBC + ORM**: Hibernate、JPA、MyBatisの基盤として`java.sql`を使用

---

## 🧾 **まとめテーブル**

| タスク               | クラス/インターフェース              |
| -------------------- | ------------------------------------ |
| DBへの接続           | `DriverManager`, `Connection`        |
| SQLの実行            | `Statement`, `PreparedStatement`     |
| ストアドプロシージャ | `CallableStatement`                  |
| 結果の読み取り       | `ResultSet`                          |
| DB情報               | `DatabaseMetaData`                   |
| カラム情報           | `ResultSetMetaData`                  |
| トランザクション     | `Connection.commit()`, `rollback()`  |
| 例外処理             | `SQLException`                       |

---

必要であれば、以下も提供できます：

* チートシート
* DAOスタイルの再利用可能なラッパークラス
* 実際のデータベース（MySQL/PostgreSQL）を使用した例

お知らせください！