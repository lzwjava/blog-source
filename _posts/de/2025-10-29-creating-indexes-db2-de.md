---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erstellen von Indizes in IBM DB2
translated: true
type: note
---

### Erstellen von Indizes in IBM DB2

IBM DB2 unterstützt Indizes, um die Abfrageleistung durch schnellere Datenabfrage zu optimieren. Indizes können auf einer oder mehreren Spalten einer Tabelle erstellt werden. Im Folgenden werden die Grundlagen behandelt, einschließlich eindeutiger Indizes und mehrspaltiger (zusammengesetzter) Indizes. Beachten Sie, dass "Union-Index" kein standardmäßiger Begriff in der DB2-Dokumentation ist – es könnte sich auf einen zusammengesetzten Index (der mehrere Schlüssel abdeckt) oder ein Missverständnis von UNION-Operationen in Abfragen beziehen. Wenn Sie etwas anderes gemeint haben, geben Sie bitte weitere Details an!

#### Grundlegende Indexerstellung
Verwenden Sie die `CREATE INDEX`-Anweisung, um einen einfachen Index auf einer einzelnen Spalte zu erstellen. Dies beschleunigt Suchen, Sortierungen und Joins auf dieser Spalte.

**Syntax:**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**Beispiel:**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` sortiert in aufsteigender Reihenfolge (Standard); verwenden Sie `DESC` für absteigend.
- Indizes sind standardmäßig nicht eindeutig und erlauben doppelte Werte.

#### Eindeutiger Index (Erzwingen eindeutiger Schlüssel)
Ein eindeutiger Index stellt sicher, dass keine doppelten Werte in den indizierten Spalten vorhanden sind, ähnlich einer Unique-Constraint. DB2 erstellt automatisch einen eindeutigen Index, wenn Sie einen Primärschlüssel oder eine Unique-Constraint definieren.

**Syntax:**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**Beispiel:**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- Dies verhindert das Einfügen doppelter E-Mails.
- Für partielle Eindeutigkeit (z.B. NULL-Werte ignorieren), fügen Sie `WHERE NOT NULL` hinzu:  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- Sie können Nicht-Schlüsselspalten für Query Coverage einbeziehen:  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### Zusammengesetzter Index (Mehrere Schlüssel, z.B. zwei oder mehr Spalten)
Ein zusammengesetzter (oder mehrspaltiger) Index deckt mehrere Schlüssel ab und ist nützlich für Abfragen, die nach Kombinationen von Spalten filten/joinen. Die Reihenfolge der Spalten ist wichtig – setzen Sie die selektivste Spalte an erste Stelle.

**Syntax:**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**Beispiel (Zwei Schlüssel):**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- Dies optimiert Abfragen wie `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`.
- Für einen eindeutigen zusammengesetzten Index: Fügen Sie `UNIQUE` hinzu (z.B. `CREATE UNIQUE INDEX ...`).

#### Zusätzliche Tipps
- **Index überprüfen:** Verwenden Sie `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';`.
- **Index löschen:** `DROP INDEX index_name;`.
- Indizes verbrauchen Speicher und verlangsamen Einfüge-/Aktualisierungsvorgänge – verwenden Sie sie mit Bedacht.
- Informationen zu partitionierten Tabellen oder erweiterten Optionen (z.B. Clustering) finden Sie in der DB2-Dokumentation.

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)