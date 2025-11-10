---
audio: false
generated: true
lang: de
layout: post
title: Vergleich von Java SQL-Anweisungstypen
translated: true
type: note
---

In Java's `java.sql` package sind `Statement`, `PreparedStatement` und `CallableStatement` Schnittstellen, die zur Ausführung von SQL-Abfragen verwendet werden, aber sie haben unterschiedliche Zwecke und Eigenschaften. Hier ist ein kurzer Vergleich:

1. **Statement**:
   - **Zweck**: Wird zur Ausführung statischer SQL-Abfragen ohne Parameter verwendet.
   - **Funktionsweise**: Man übergibt eine vollständige SQL-Abfrage als String an die Methode `executeQuery()` oder `executeUpdate()`.
   - **Hauptmerkmale**:
     - Geeignet für einfache, einmalige Abfragen.
     - Keine Parameterbindung, daher werden Werte manuell in den SQL-String konkateniert, was SQL-Injection-Risiken birgt.
     - Weniger effizient für wiederholte Abfragen, da die Datenbank den SQL-Code jedes Mal neu parsen muss.
   - **Beispiel**:
     ```java
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = 1");
     ```

2. **PreparedStatement**:
   - **Zweck**: Wird für vorkompilierte, parametrisierte SQL-Abfragen verwendet.
   - **Funktionsweise**: Man definiert eine Abfrage mit Platzhaltern (`?`) und setzt Parameterwerte mit Methoden wie `setInt()`, `setString()` usw.
   - **Hauptmerkmale**:
     - Verhindert SQL-Injection durch Trennung von SQL-Logik und Daten.
     - Effizienter für wiederholte Abfragen, da der SQL-Code einmal kompiliert und wiederverwendet wird.
     - Unterstützt dynamische Parameterbindung, was sie sicherer und flexibler macht.
   - **Beispiel**:
     ```java
     PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     pstmt.setInt(1, 1);
     ResultSet rs = pstmt.executeQuery();
     ```

3. **CallableStatement**:
   - **Zweck**: Wird zur Ausführung von gespeicherten Prozeduren in der Datenbank verwendet.
   - **Funktionsweise**: Erweitert `PreparedStatement`, um Aufrufe gespeicherter Prozeduren zu behandeln, und unterstützt Eingabe- (`IN`), Ausgabe- (`OUT`) und Ein-/Ausgabeparameter (`IN OUT`).
   - **Hauptmerkmale**:
     - Speziell für gespeicherte Datenbankprozeduren entwickelt.
     - Ermöglicht die Registrierung von Ausgabeparametern mit Methoden wie `registerOutParameter()`.
     - Unterstützt komplexe Parameterbehandlung für die Logik gespeicherter Prozeduren.
   - **Beispiel**:
     ```java
     CallableStatement cstmt = conn.prepareCall("{call getUserName(?, ?)}");
     cstmt.setInt(1, 1);
     cstmt.registerOutParameter(2, Types.VARCHAR);
     cstmt.execute();
     String username = cstmt.getString(2);
     ```

**Hauptunterschiede**:
| Merkmal                | Statement                          | PreparedStatement                  | CallableStatement                 |
|------------------------|------------------------------------|------------------------------------|------------------------------------|
| **Zweck**              | Statische SQL-Abfragen            | Parametrisierte SQL-Abfragen      | Ausführung gespeicherter Prozeduren |
| **SQL-Injection**      | Anfällig (manuelle Konkatenation) | Sicher (Parameterbindung)         | Sicher (Parameterbindung)         |
| **Performance**        | Weniger effizient (keine Vorkompilierung)| Effizienter (vorkompiliert)   | Effizient für gespeicherte Prozeduren |
| **Anwendungsfall**     | Einfache, einmalige Abfragen      | Wiederholte oder parametrisierte Abfragen | Gespeicherte Prozeduren mit Parametern |
| **Parameterunterstützung** | Keine                           | Nur Eingabeparameter              | Eingabe-, Ausgabe- und IN/OUT-Parameter |

**Wann verwendet man was**:
- Verwenden Sie `Statement` für einfache, nicht wiederholte Abfragen, bei denen Sicherheit und Performance weniger kritisch sind.
- Verwenden Sie `PreparedStatement` für parametrisierte Abfragen, wiederholte Ausführungen oder wenn Sicherheit (SQL-Injection-Prävention) ein Anliegen ist.
- Verwenden Sie `CallableStatement` beim Aufruf von gespeicherten Datenbankprozeduren mit Eingabe-/Ausgabeparametern.

Diese Erklärung basiert auf dem Standardverhalten der Java SQL-API zum Stand meines Wissens. Falls Sie weitere Details oder Beispiele benötigen, lassen Sie es mich wissen!