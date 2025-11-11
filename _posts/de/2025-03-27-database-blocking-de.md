---
audio: false
generated: true
lang: de
layout: post
title: Datenbankblockierung
translated: true
type: note
---

Ich nehme an, Sie fragen nach Beispielen für Database Blocking im Kontext von Datenbankmanagementsystemen (DBMS). Blocking tritt auf, wenn eine Transaktion in einer Datenbank eine andere Transaktion am Fortfahren hindert, weil sie gleichzeitig auf dieselben Daten zugreifen oder diese ändern möchten. Dies wird typischerweise durch Locking verwaltet, um Datenkonsistenz und -integrität sicherzustellen. Nachfolgend sind einige Beispiele für Szenarien mit Database Blocking aufgeführt:

---

### Beispiel 1: Read-Write Blocking
- **Szenario**: Transaktion T1 aktualisiert eine Zeile in einer Tabelle (z.B. ändert den Kontostand eines Kunden), und Transaktion T2 versucht, dieselbe Zeile zu lesen.
- **Was passiert**: T1 erwirbt einen exklusiven Lock auf die Zeile, um zu verhindern, dass andere Transaktionen sie lesen oder ändern, bis die Aktualisierung abgeschlossen ist. T2 wird blockiert und muss warten, bis T1 committed oder einen Rollback durchführt.
- **SQL-Beispiel**:
  ```sql
  -- Transaktion T1
  BEGIN TRANSACTION;
  UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;

  -- Transaktion T2 (blockiert)
  SELECT Balance FROM Accounts WHERE AccountID = 1;
  ```
  T2 wartet, bis T1 beendet ist, wegen des exklusiven Locks auf der Zeile.

---

### Beispiel 2: Write-Write Blocking
- **Szenario**: Transaktion T1 aktualisiert die Lagerbestandsmenge eines Produkts, und Transaktion T2 versucht gleichzeitig, den Lagerbestand desselben Produkts zu aktualisieren.
- **Was passiert**: T1 hält einen exklusiven Lock auf der Zeile, und T2 wird blockiert, bis T1 abgeschlossen ist. Dies verhindert konfligierende Aktualisierungen, die zu Dateninkonsistenz führen könnten.
- **SQL-Beispiel**:
  ```sql
  -- Transaktion T1
  BEGIN TRANSACTION;
  UPDATE Products SET Stock = Stock - 5 WHERE ProductID = 100;

  -- Transaktion T2 (blockiert)
  UPDATE Products SET Stock = Stock + 10 WHERE ProductID = 100;
  ```
  T2 wird blockiert, bis T1 committed oder einen Rollback durchführt.

---

### Beispiel 3: Deadlock (Blocking führt zu Pattsituation)
- **Szenario**: Transaktion T1 sperrt Zeile A und muss Zeile B aktualisieren, während Transaktion T2 Zeile B sperrt und Zeile A aktualisieren muss.
- **Was passiert**: T1 wird durch T2s Lock auf Zeile B blockiert, und T2 wird durch T1s Lock auf Zeile A blockiert. Dies erzeugt einen Deadlock, und das DBMS muss eingreifen (z.B. durch Rollback einer Transaktion).
- **SQL-Beispiel**:
  ```sql
  -- Transaktion T1
  BEGIN TRANSACTION;
  UPDATE Table1 SET Value = 10 WHERE ID = 1;  -- Sperrt Zeile A
  UPDATE Table2 SET Value = 20 WHERE ID = 2;  -- Wird durch T2 blockiert

  -- Transaktion T2
  BEGIN TRANSACTION;
  UPDATE Table2 SET Value = 30 WHERE ID = 2;  -- Sperrt Zeile B
  UPDATE Table1 SET Value = 40 WHERE ID = 1;  -- Wird durch T1 blockiert
  ```
  Keine der Transaktionen kann fortfahren, bis das DBMS den Deadlock auflöst.

---

### Beispiel 4: Table-Level Blocking
- **Szenario**: Transaktion T1 führt eine umfangreiche Aktualisierung einer gesamten Tabelle ohne geeignete Indizierung durch, und Transaktion T2 versucht, eine einzelne Zeile aus derselben Tabelle zu lesen.
- **Was passiert**: T1 könnte seine Zeilen-Locks zu einem Tabellen-Lock eskalieren, was T2 sogar am Lesen nicht-betroffener Zeilen hindert, bis T1 abgeschlossen ist.
- **SQL-Beispiel**:
  ```sql
  -- Transaktion T1
  BEGIN TRANSACTION;
  UPDATE Employees SET Salary = Salary * 1.1;  -- Sperrt die gesamte Tabelle

  -- Transaktion T2 (blockiert)
  SELECT Name FROM Employees WHERE EmployeeID = 5;
  ```
  T2 wird blockiert, weil T1 einen exklusiven Tabellen-Lock besitzt.

---

### Wie Blocking verwaltet wird
- **Locks**: Datenbanken verwenden Shared Locks (zum Lesen) und Exclusive Locks (zum Schreiben), um den Zugriff zu steuern.
- **Isolationslevel**: Höhere Isolationslevel (z.B. Serializable) erhöhen das Blocking, um Konsistenz zu gewährleisten, während niedrigere Level (z.B. Read Uncommitted) das Blocking reduzieren, aber das Risiko von Dirty Reads bergen.
- **Timeouts**: Transaktionen können timeouten, wenn sie zu lange blockiert werden, und werden zwangsweise zurückgesetzt.
- **Deadlock-Erkennung**: Das DBMS erkennt und löst Deadlocks auf, indem es eine Transaktion abbricht.

Lassen Sie mich wissen, wenn Sie weitere Details oder Beispiele für ein bestimmtes Datenbanksystem (z.B. MySQL, PostgreSQL, SQL Server) wünschen!