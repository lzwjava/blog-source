---
audio: false
generated: true
lang: ar
layout: post
title: جافا إس كيو إل لربط قواعد البيانات
translated: true
type: note
---

حزمة `java.sql` هي **جزء أساسي من واجهة برمجة تطبيقات JDBC في جافا (اتصال قاعدة بيانات جافا)**، مما يمكن تطبيقات جافا من التفاعل مع قواعد البيانات العلائقية مثل MySQL، PostgreSQL، Oracle، SQL Server، وغيرها. توفر الواجهات والفئات المطلوبة **للوصول إلى قاعدة بيانات، وتنفيذ استعلامات SQL، واسترداد النتائج**.

---

## 📘 **نظرة عامة على `java.sql`**

تتضمن حزمة `java.sql` فئات وواجهات لـ:

* الوصول إلى قواعد البيانات (`DriverManager`, `Connection`)
* تنفيذ استعلامات SQL (`Statement`, `PreparedStatement`, `CallableStatement`)
* معالجة النتائج (`ResultSet`)
* التعامل مع البيانات الوصفية (`DatabaseMetaData`, `ResultSetMetaData`)
* إدارة المعاملات
* معالجة استثناءات SQL (`SQLException`)

---

## 🔧 **الإعداد: ما تحتاجه**

### 1. **برنامج تشغيل JDBC**

* تحتاج إلى برنامج تشغيل JDBC لقاعدة البيانات المستهدفة (مثل MySQL: `mysql-connector-java`، PostgreSQL: `postgresql`).
* يمكنك تضمينه عبر Maven/Gradle أو إضافة ملف `.jar` يدويًا.

### 2. **عنوان URL لقاعدة البيانات**

كل برنامج تشغيل JDBC له تنسيق عنوان URL للاتصال:

```java
jdbc:mysql://localhost:3306/mydatabase
jdbc:postgresql://localhost:5432/mydatabase
```

---

## 🧩 **الفئات والواجهات الرئيسية**

### 🔌 1. `DriverManager`

يُنشئ اتصالاً بقاعدة البيانات.

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

### 🧵 2. `Connection`

يمثل جلسة مع قاعدة بيانات.

* إنشاء `Statement` أو `PreparedStatement`
* إدارة المعاملات (commit, rollback)
* إغلاق الاتصال

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // للتحكم اليدوي في المعاملات
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

يُستخدم لتنفيذ استعلامات SQL ثابتة.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

#### `PreparedStatement`

يُستخدم لتنفيذ استعلامات معلمات. يتجنب حقن SQL.

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

يُستخدم للإجراءات المخزنة.

```java
CallableStatement cs = conn.prepareCall("{call getUser(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

يحمل نتيجة الاستعلام.

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

### 📚 5. البيانات الوصفية

* `DatabaseMetaData`: معلومات حول قاعدة البيانات
* `ResultSetMetaData`: معلومات حول أعمدة النتيجة

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **مثال أساسي**

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

## 🔁 **المعاملات**

```java
conn.setAutoCommit(false);  // تعطيل الالتزام التلقائي

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // إقرار المعاملة

} catch (SQLException ex) {
    conn.rollback(); // التراجع في حالة الخطأ
}
```

---

## ❗ **معالجة الاستثناءات**

```java
try {
    // كود قاعدة البيانات
} catch (SQLException ex) {
    System.err.println("Error Code: " + ex.getErrorCode());
    System.err.println("SQL State: " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **ميزات مفيدة في `java.sql`**

| الميزة                  | الواجهة/الفئة                         | الغرض                                           |
| ---------------------- | ------------------------------------ | ----------------------------------------------- |
| البيانات الوصفية        | `DatabaseMetaData`                   | إصدار قاعدة البيانات، الميزات المدعومة، الجداول، إلخ. |
| معلومات عمود النتيجة    | `ResultSetMetaData`                  | عدد الأعمدة، النوع، التسمية، إلخ.                 |
| معالجة BLOB/CLOB       | `Blob`, `Clob`                       | تخزين/استرداد بيانات ثنائية/نصية كبيرة           |
| التنفيذ المجمع          | `addBatch()`, `executeBatch()`       | تنفيذ العديد من العبارات معًا                   |
| ResultSet قابل للتمرير | `ResultSet.TYPE_SCROLL_INSENSITIVE`  | تحريك المؤشر للأمام والخلف                      |
| ResultSet قابل للتحديث  | `ResultSet.CONCUR_UPDATABLE`         | تعديل الصفوف مباشرة في `ResultSet`              |

---

## 📦 **مثال تبعية Maven (MySQL)**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **أفضل الممارسات**

* أغلق دائمًا `Connection`، `Statement`، `ResultSet` في كتلة `finally` أو استخدم try-with-resources.
* استخدم `PreparedStatement` بدلاً من `Statement` لمنع حقن SQL.
* استخدم تجميع الاتصالات في بيئة الإنتاج (عبر مكتبات مثل HikariCP، Apache DBCP).
* استخدم المعاملات للاستعلامات المتعددة ذات الصلة.
* لا تقم بتشفير SQL في منطق الأعمال — فكر في أنماط DAO أو ORM (مثل JPA، Hibernate).

---

## 🧮 **مواضيع متقدمة**

* **RowSet**: نسخة غير متصلة من ResultSet (`javax.sql.rowset`)
* **تجميع الاتصالات**: استخدم `DataSource` مع المجمعات
* **ميزات JDBC 4+**: تحميل برامج التشغيل تلقائيًا، دعم try-with-resources
* **JDBC + Spring**: التكامل مع Spring JDBC Template
* **JDBC + ORM**: استخدم `java.sql` تحت Hibernate، JPA، MyBatis

---

## 🧾 **جدول الملخص**

| المهمة                | الفئة/الواجهة                        |
| --------------------- | ------------------------------------ |
| الاتصال بقاعدة البيانات | `DriverManager`, `Connection`        |
| تنفيذ SQL             | `Statement`, `PreparedStatement`     |
| الإجراءات المخزنة     | `CallableStatement`                  |
| قراءة النتائج         | `ResultSet`                          |
| معلومات قاعدة البيانات | `DatabaseMetaData`                   |
| معلومات العمود        | `ResultSetMetaData`                  |
| المعاملات             | `Connection.commit()`, `rollback()`  |
| معالجة الاستثناءات    | `SQLException`                       |

---

إذا كنت ترغب، يمكنني أيضًا تقديم:

* ورقة غش
* فئة غلاف قابلة لإعادة الاستخدام بأسلوب DAO
* أمثلة مع قاعدة بيانات حقيقية (MySQL/PostgreSQL)

أعلمني!