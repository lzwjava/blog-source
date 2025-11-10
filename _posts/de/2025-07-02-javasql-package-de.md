---
audio: false
generated: true
lang: de
layout: post
title: Java SQL Für Datenbankkonnektivität
translated: true
type: note
---

Das `java.sql`-Paket ist ein **Kernbestandteil von Javas JDBC-API (Java Database Connectivity)**, das Java-Anwendungen ermöglicht, mit relationalen Datenbanken wie MySQL, PostgreSQL, Oracle, SQL Server und anderen zu interagieren. Es stellt die Schnittstellen und Klassen bereit, die benötigt werden, um **eine Verbindung zu einer Datenbank herzustellen, SQL-Abfragen auszuführen und Ergebnisse abzurufen**.

---

## 📘 **Überblick über `java.sql`**

Das `java.sql`-Paket enthält Klassen und Schnittstellen für:

* Verbinden mit Datenbanken (`DriverManager`, `Connection`)
* Ausführen von SQL-Abfragen (`Statement`, `PreparedStatement`, `CallableStatement`)
* Verarbeiten von Ergebnissen (`ResultSet`)
* Handhaben von Metadaten (`DatabaseMetaData`, `ResultSetMetaData`)
* Verwalten von Transaktionen
* Behandeln von SQL-Ausnahmen (`SQLException`)

---

## 🔧 **Setup: Was Sie benötigen**

### 1. **JDBC-Treiber**

* Sie benötigen einen JDBC-Treiber für Ihre Zieldatenbank (z.B. MySQL: `mysql-connector-java`, PostgreSQL: `postgresql`).
* Sie können ihn über Maven/Gradle einbinden oder die `.jar`-Datei manuell hinzufügen.

### 2. **Datenbank-URL**

Jeder JDBC-Treiber hat ein eigenes URL-Format für die Verbindung:

```java
jdbc:mysql://localhost:3306/mydatabase
jdbc:postgresql://localhost:5432/mydatabase
```

---

## 🧩 **Wichtige Klassen und Schnittstellen**

### 🔌 1. `DriverManager`

Stellt eine Verbindung zu einer Datenbank her.

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

### 🧵 2. `Connection`

Repräsentiert eine Sitzung mit einer Datenbank.

* Erstellt `Statement` oder `PreparedStatement`
* Verwaltet Transaktionen (Commit, Rollback)
* Schließt die Verbindung

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // für manuelle Transaktionskontrolle
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

Wird für die Ausführung statischer SQL-Abfragen verwendet.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

#### `PreparedStatement`

Wird für die Ausführung parametrisierter Abfragen verwendet. Verhindert SQL-Injection.

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

Wird für gespeicherte Prozeduren verwendet.

```java
CallableStatement cs = conn.prepareCall("{call getUser(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

Enthält das Ergebnis einer Abfrage.

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

### 📚 5. Metadaten

* `DatabaseMetaData`: Informationen über die Datenbank
* `ResultSetMetaData`: Informationen über die Ergebnisspalten

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **Einfaches Beispiel**

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

## 🔁 **Transaktionen**

```java
conn.setAutoCommit(false);  // Auto-Commit deaktivieren

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // Transaktion committen

} catch (SQLException ex) {
    conn.rollback(); // Bei Fehler zurückrollen
}
```

---

## ❗ **Ausnahmebehandlung**

```java
try {
    // DB-Code
} catch (SQLException ex) {
    System.err.println("Error Code: " + ex.getErrorCode());
    System.err.println("SQL State: " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **Nützliche Funktionen in `java.sql`**

| Funktion              | Schnittstelle/Klasse                | Zweck                                        |
| --------------------- | ----------------------------------- | -------------------------------------------- |
| Metadaten             | `DatabaseMetaData`                  | DB-Version, unterstützte Features, Tabellen etc. |
| Spalteninformationen  | `ResultSetMetaData`                 | Spaltenanzahl, Typ, Bezeichnung etc.         |
| BLOB/CLOB-Behandlung  | `Blob`, `Clob`                      | Große binäre/Text-Daten speichern/abrufen    |
| Batch-Ausführung      | `addBatch()`, `executeBatch()`      | Viele Anweisungen zusammen ausführen         |
| Scrollbares ResultSet | `ResultSet.TYPE_SCROLL_INSENSITIVE` | Cursor vor- und zurückbewegen                |
| Aktualisierbares ResultSet | `ResultSet.CONCUR_UPDATABLE`   | Zeilen direkt im `ResultSet` ändern          |

---

## 📦 **Maven-Abhängigkeitsbeispiel (MySQL)**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **Best Practices**

* Schließen Sie `Connection`, `Statement`, `ResultSet` immer im `finally`-Block oder verwenden Sie try-with-resources.
* Verwenden Sie `PreparedStatement` anstelle von `Statement`, um SQL-Injection zu verhindern.
* Verwenden Sie Connection Pooling im Produktivbetrieb (über Bibliotheken wie HikariCP, Apache DBCP).
* Verwenden Sie Transaktionen für mehrere zusammenhängende Abfragen.
* Hardcodieren Sie SQL nicht in der Geschäftslogik – erwägen Sie DAO- oder ORM-Muster (wie JPA, Hibernate).

---

## 🧮 **Fortgeschrittene Themen**

* **RowSet**: Trennbare Version von ResultSet (`javax.sql.rowset`)
* **Connection Pooling**: Verwenden Sie `DataSource` mit Pools
* **JDBC 4+ Features**: Automatisches Laden von Treibern, Try-with-Resources-Unterstützung
* **JDBC + Spring**: Integration mit Spring JDBC Template
* **JDBC + ORM**: Verwenden Sie `java.sql` unter Hibernate, JPA, MyBatis

---

## 🧾 **Zusammenfassungstabelle**

| Aufgabe               | Klasse/Schnittstelle                |
| --------------------- | ----------------------------------- |
| Mit DB verbinden      | `DriverManager`, `Connection`       |
| SQL ausführen         | `Statement`, `PreparedStatement`    |
| Gespeicherte Prozeduren | `CallableStatement`               |
| Ergebnisse lesen      | `ResultSet`                         |
| DB-Informationen      | `DatabaseMetaData`                  |
| Spalteninformationen  | `ResultSetMetaData`                 |
| Transaktionen         | `Connection.commit()`, `rollback()` |
| Ausnahmebehandlung    | `SQLException`                      |

---

Falls gewünscht, kann ich auch bereitstellen:

* Ein Spickzettel
* Eine wiederverwendbare Wrapper-Klasse im DAO-Stil
* Beispiele mit einer echten Datenbank (MySQL/PostgreSQL)

Lassen Sie es mich wissen!