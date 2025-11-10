---
audio: false
generated: true
image: false
lang: de
layout: post
title: Statement vs. CallableStatement in JDBC
translated: true
type: note
---

In Java’s JDBC (und anderen darauf aufbauenden Frameworks wie Hibernate oder Spring) sind die Konzepte **`Statement`** und **`CallableStatement`** beide Interfaces, die verwendet werden, um SQL-Befehle an die Datenbank zu senden, sie erfüllen jedoch unterschiedliche Zwecke.

---

### 1. `Statement`

* **Zweck**: Wird verwendet, um einfache SQL-Abfragen ohne Parameter auszuführen.
* **Verwendung**: Man erstellt ein `Statement`-Objekt von einer `Connection` und verwendet es, um SQL-Strings auszuführen.
* **Typische Methoden**:

  * `executeQuery(sql)` → für `SELECT`-Abfragen, gibt ein `ResultSet` zurück.
  * `executeUpdate(sql)` → für `INSERT`, `UPDATE`, `DELETE`.
  * `execute(sql)` → generisch, gibt `true` zurück, wenn das Ergebnis ein `ResultSet` ist.

**Beispiel**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **Wann zu verwenden**: Für statische SQL-Anweisungen ohne Parameter.
* **Nachteil**: Kann zu SQL-Injection führen, wenn es mit dynamischer Benutzereingabe verwendet wird.

---

### 2. `CallableStatement`

* **Zweck**: Wird verwendet, um **Stored Procedures** in der Datenbank auszuführen.
* **Verwendung**: Wird mit `Connection.prepareCall()` erstellt und erlaubt das Aufrufen von Datenbankroutinen mit **IN**-, **OUT**- und **INOUT**-Parametern.
* **Typische Methoden**:

  * `setInt`, `setString`, etc. → zum Setzen von Eingabeparametern.
  * `registerOutParameter` → zum Registrieren von Ausgabeparametern.
  * `execute()` oder `executeQuery()` → zum Ausführen der gespeicherten Prozedur.
  * `getInt`, `getString`, etc. → zum Abrufen von Ausgabewerten.

**Beispiel**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// IN-Parameter setzen
cstmt.setInt(1, 101);

// OUT-Parameter registrieren
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// Ausführen
cstmt.execute();

// OUT-Parameter abrufen
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **Wann zu verwenden**: Für gespeicherte Prozeduren/Funktionen, die Logik in der Datenbank kapseln.
* **Vorteile**: Unterstützt komplexe Logik, mehrere Ergebnisse und Eingabe-/Ausgabeparameter.

---

### Wichtige Unterschiede (ohne Tabelle)

* `Statement` ist für **statisches SQL** (Ad-hoc-Abfragen).
* `CallableStatement` ist für **gespeicherte Prozeduren/Funktionen**.
* `Statement` führt SQL direkt aus, während `CallableStatement` mit Datenbankroutinen interagiert, die mehrere Resultsets und Parameter zurückgeben können.
* `Statement` ist einfach, aber weniger sicher bei dynamischer Eingabe, während `CallableStatement` eine strukturierte Möglichkeit bietet, wiederverwendbare, in der DB gespeicherte Logik aufzurufen.

---

👉 Falls gewünscht, kann ich auch erklären, wie sich **`PreparedStatement`** zwischen diesen beiden einordnet (sicherer, parametrisiertes SQL, aber nicht für gespeicherte Prozeduren). Soll ich das hinzufügen?