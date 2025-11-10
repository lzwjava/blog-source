---
audio: false
generated: true
image: false
lang: zh
layout: post
title: JDBC中Statement与CallableStatement的对比
translated: true
type: note
---

在Java的JDBC（以及构建于其上的其他框架，如Hibernate或Spring）中，**`Statement`** 和 **`CallableStatement`** 都是用于向数据库发送SQL命令的接口，但它们的用途有所不同。

---

### 1. `Statement`

* **用途**：用于执行不带参数的简单SQL查询。
* **用法**：通过 `Connection` 创建 `Statement` 对象，并使用它来执行SQL字符串。
* **典型方法**：

  * `executeQuery(sql)` → 用于 `SELECT` 查询，返回 `ResultSet`。
  * `executeUpdate(sql)` → 用于 `INSERT`、`UPDATE`、`DELETE`。
  * `execute(sql)` → 通用方法，如果结果是 `ResultSet` 则返回 `true`。

**示例**：

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **使用场景**：适用于不带参数的静态SQL语句。
* **缺点**：如果与动态用户输入一起使用，可能导致SQL注入。

---

### 2. `CallableStatement`

* **用途**：用于执行数据库中的**存储过程**。
* **用法**：通过 `Connection.prepareCall()` 创建，允许调用具有 **IN**、**OUT** 和 **INOUT** 参数的数据库例程。
* **典型方法**：

  * `setInt`、`setString` 等 → 用于设置输入参数。
  * `registerOutParameter` → 用于注册输出参数。
  * `execute()` 或 `executeQuery()` → 用于运行存储过程。
  * `getInt`、`getString` 等 → 用于检索输出值。

**示例**：

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// 设置IN参数
cstmt.setInt(1, 101);

// 注册OUT参数
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// 执行
cstmt.execute();

// 获取OUT参数
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **使用场景**：适用于封装了数据库逻辑的存储过程/函数。
* **优势**：支持复杂逻辑、多结果集和输入/输出参数。

---

### 主要区别（无表格形式）

* `Statement` 用于**静态SQL**（即席查询）。
* `CallableStatement` 用于**存储过程/函数**。
* `Statement` 直接执行SQL，而 `CallableStatement` 与可能返回多个结果集和参数的数据库例程交互。
* `Statement` 简单但在处理动态输入时安全性较低，而 `CallableStatement` 提供了一种结构化的方式来调用数据库中可重用的逻辑。

---

👉 如果你需要，我也可以解释 **`PreparedStatement`** 如何在这两者之间起到作用（更安全、参数化的SQL，但不用于存储过程）。需要我补充这一点吗？