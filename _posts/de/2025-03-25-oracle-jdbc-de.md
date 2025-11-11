---
audio: false
generated: true
lang: de
layout: post
title: Oracle JDBC-Treiber
translated: true
type: note
---

Oracle JDBC (Java Database Connectivity) Treiber ermöglichen Java-Anwendungen, eine Verbindung zu Oracle-Datenbanken herzustellen und mit ihnen zu interagieren. Lassen Sie mich die wichtigsten Komponenten und deren Verwendung erklären.

Die Hauptklasse für Oracle JDBC-Verbindungen ist `oracle.jdbc.driver.OracleDriver`, allerdings wird in neueren Versionen oft `oracle.jdbc.OracleDriver` verwendet (dies ist die empfohlene Klasse seit Oracle 10g).

So verwenden Sie Oracle JDBC in einer Java-Anwendung:

1. Zuerst müssen Sie das Oracle JDBC Treiber JAR in Ihr Projekt einbinden (typischerweise ojdbc.jar).

2. Laden Sie die Treiberklasse:
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. Stellen Sie eine Verbindung über eine Connection URL her:
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// Oder für Service Name basierte Verbindung
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. Erstellen und führen Sie Statements aus:
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // Verarbeite jede Zeile
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. Schließen Sie immer die Ressourcen, wenn Sie fertig sind:
```java
resultSet.close();
statement.close();
connection.close();
```

Der Oracle JDBC Treiber ist in mehreren Varianten verfügbar:
- Thin driver: Reine Java-Implementierung, die keine Oracle Client-Installation erfordert
- OCI driver: Verwendet Oracle Call Interface und benötigt Oracle Client-Software
- Kerberos driver: Für Kerberos-Authentifizierung
- JDBC-OCI driver: Kombination aus JDBC und OCI

Der Thin driver wird am häufigsten verwendet, da er keine zusätzliche Oracle Client-Software auf dem Client-Rechner benötigt.

Möchten Sie spezifischere Informationen zu Connection Pooling, Prepared Statements oder anderen Aspekten der Oracle JDBC-Nutzung?