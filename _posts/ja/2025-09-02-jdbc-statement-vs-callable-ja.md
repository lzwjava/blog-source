---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JDBCにおけるStatementとCallableStatement
translated: true
type: note
---

JavaのJDBC（およびHibernateやSpringなどのそれを基盤とする他のフレームワーク）では、**`Statement`** と **`CallableStatement`** の概念は、どちらもデータベースにSQLコマンドを送信するために使用されるインターフェースですが、異なる目的に使用されます。

---

### 1. `Statement`

* **目的**: パラメータのない単純なSQLクエリの実行に使用されます。
* **使用方法**: `Connection` から `Statement` オブジェクトを作成し、SQL文字列を実行するために使用します。
* **代表的なメソッド**:

  * `executeQuery(sql)` → `SELECT` クエリ用。`ResultSet` を返します。
  * `executeUpdate(sql)` → `INSERT`, `UPDATE`, `DELETE` 用。
  * `execute(sql)` → 汎用的なメソッド。結果が `ResultSet` の場合 `true` を返します。

**例**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **使用すべき場合**: パラメータのない静的なSQLステートメントに対して。
* **欠点**: 動的なユーザー入力と共に使用するとSQLインジェクションの原因となる可能性があります。

---

### 2. `CallableStatement`

* **目的**: データベース内の **ストアドプロシージャ** を実行するために使用されます。
* **使用方法**: `Connection.prepareCall()` で作成され、**IN**, **OUT**, **INOUT** パラメータを持つデータベースルーチンの呼び出しを可能にします。
* **代表的なメソッド**:

  * `setInt`, `setString` など → 入力パラメータを設定します。
  * `registerOutParameter` → 出力パラメータを登録します。
  * `execute()` または `executeQuery()` → ストアドプロシージャを実行します。
  * `getInt`, `getString` など → 出力値を取得します。

**例**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// IN パラメータを設定
cstmt.setInt(1, 101);

// OUT パラメータを登録
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// 実行
cstmt.execute();

// OUT パラメータを取得
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **使用すべき場合**: データベース内にロジックをカプセル化したストアドプロシージャ/関数に対して。
* **利点**: 複雑なロジック、複数の結果セット、入出力パラメータをサポートします。

---

### 主な違い (表なし)

* `Statement` は **静的なSQL** (アドホックなクエリ) 用です。
* `CallableStatement` は **ストアドプロシージャ/関数** 用です。
* `Statement` はSQLを直接実行しますが、`CallableStatement` は複数の結果セットやパラメータを返す可能性があるデータベースルーチンと対話します。
* `Statement` はシンプルですが動的な入力に対して安全性が低く、`CallableStatement` はデータベースに保存された再利用可能なロジックを呼び出す構造化された方法を提供します。

---

👉 必要であれば、**`PreparedStatement`** がこれら2つの間にどのように位置するか (より安全で、パラメータ化されたSQL用だが、ストアドプロシージャ用ではない) も説明できます。追加してほしいですか？