---
audio: false
generated: true
lang: de
layout: post
title: Datenbank-Deadlock
translated: true
type: note
---

Ein **Datenbank-Deadlock** tritt auf, wenn zwei oder mehr Transaktionen darauf warten, dass die andere Sperren für Ressourcen aufhebt. Dadurch entsteht eine zirkuläre Abhängigkeit, die verhindert, dass eine der Transaktionen fortfahren kann. Das Datenbankmanagementsystem (DBMS) erkennt diese Situation in der Regel und löst sie, indem eine der Transaktionen zurückgesetzt wird. Nachfolgend ein detailliertes Beispiel für ein Deadlock-Szenario:

---

### Beispiel: Deadlock zwischen zwei Transaktionen
- **Szenario**:
  - Transaktion T1 aktualisiert eine Zeile in der Tabelle `Orders` und muss anschließend eine Zeile in der Tabelle `Customers` aktualisieren.
  - Transaktion T2 aktualisiert eine Zeile in der Tabelle `Customers` und muss anschließend eine Zeile in der Tabelle `Orders` aktualisieren.
  - Beide Transaktionen sperren Ressourcen in einer unterschiedlichen Reihenfolge, was zu einem Deadlock führt.

- **Schritt für Schritt**:
  1. T1 sperrt eine Zeile in `Orders`.
  2. T2 sperrt eine Zeile in `Customers`.
  3. T1 versucht, die Zeile in `Customers` zu sperren (wird durch T2 blockiert).
  4. T2 versucht, die Zeile in `Orders` zu sperren (wird durch T1 blockiert).
  - Ergebnis: Keine der Transaktionen kann fortfahren, es entsteht ein Deadlock.

- **SQL-Beispiel**:
  ```sql
  -- Transaktion T1
  BEGIN TRANSACTION;
  UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 100;  -- Sperrt OrderID 100
  -- (eine Verzögerung oder Verarbeitung)
  UPDATE Customers SET LastOrderDate = '2025-03-27' WHERE CustomerID = 1;  -- Wird durch T2 blockiert

  -- Transaktion T2
  BEGIN TRANSACTION;
  UPDATE Customers SET Balance = Balance - 50 WHERE CustomerID = 1;  -- Sperrt CustomerID 1
  -- (eine Verzögerung oder Verarbeitung)
  UPDATE Orders SET PaymentStatus = 'Paid' WHERE OrderID = 100;  -- Wird durch T1 blockiert
  ```

- **Was passiert**:
  - T1 hält eine exklusive Sperre auf `OrderID = 100` und wartet auf `CustomerID = 1`.
  - T2 hält eine exklusive Sperre auf `CustomerID = 1` und wartet auf `OrderID = 100`.
  - Diese zirkuläre Wartebedingung ist ein Deadlock.
  - Das DBMS erkennt dies (z.B. durch einen Timeout oder einen Deadlock-Erkennungsalgorithmus) und setzt eine Transaktion zurück (z.B. T2), sodass T1 abgeschlossen werden kann.

---

### Visuelle Darstellung des Deadlocks
```
T1: Sperrt Orders(100) --> Möchte Customers(1)
   |                              ↑
   |                              |
T2: Möchte Orders(100)  <-- Sperrt Customers(1)
```

- **Auflösung**: Das DBMS könnte eine Fehlermeldung wie die folgende ausgeben:
  ```
  Transaction T2 was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction.
  ```

---

### Warum es passiert
- **Sperrreihenfolge**: T1 und T2 erlangen Sperren in einer unterschiedlichen Abfolge (T1: Orders → Customers; T2: Customers → Orders).
- **Nebenläufigkeit**: Beide Transaktionen laufen gleichzeitig ab und benötigen überlappende Ressourcen.
- **Exklusive Sperren**: Updates erfordern exklusive Sperren, die andere Transaktionen am Zugriff auf die gleichen Daten hindern.

---

### Wie man Deadlocks vermeidet
1. **Konsistente Sperrreihenfolge**: Stellen Sie sicher, dass alle Transaktionen Sperren in der gleichen Reihenfolge anfordern (z.B. immer zuerst `Orders`, dann `Customers`).
   ```sql
   -- Sowohl T1 als auch T2 sollten zuerst Orders, dann Customers sperren
   ```
2. **Transaktionszeit reduzieren**: Minimieren Sie Verzögerungen innerhalb von Transaktionen, um die Wahrscheinlichkeit von Überlappungen zu verringern.
3. **Niedrigere Isolationslevel verwenden**: Verwenden Sie, falls angemessen, einen weniger strengen Isolationslevel (z.B. Read Committed), um die Sperrdauer zu verkürzen.
4. **Timeouts**: Setzen Sie kürzere Sperr-Timeouts, um bei Konflikten schnell zu scheitern und einen erneuten Versuch zu starten.

---

Lass mich wissen, wenn du ein spezifischeres Beispiel (z.B. mit einem bestimmten DBMS wie PostgreSQL oder SQL Server) oder weitere Erklärungen wünschst!