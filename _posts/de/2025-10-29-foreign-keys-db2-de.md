---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erstellen von Fremdschlüsseln in Db2
translated: true
type: note
---

### Erstellen von Fremdschlüsseln in IBM Db2

Fremdschlüssel in Db2 erzwingen die referenzielle Integrität, indem sie eine Spalte (oder eine Gruppe von Spalten) in einer Tabelle (der Kindtabelle) mit dem Primärschlüssel oder einem eindeutigen Schlüssel in einer anderen Tabelle (der Elterntabelle) verknüpfen. Dies stellt sicher, dass die Werte in der Kindtabelle mit vorhandenen Werten in der Elterntabelle übereinstimmen, und verhindert verwaiste Datensätze.

Sie können Fremdschlüssel entweder während der Tabellenerstellung mit `CREATE TABLE` definieren oder sie zu einer bestehenden Tabelle mit `ALTER TABLE` hinzufügen. Die Syntax ist Standard-SQL und funktioniert über alle Db2-Plattformen hinweg (z. B. LUW, z/OS).

#### 1. Definieren eines Fremdschlüssels während der Tabellenerstellung (`CREATE TABLE`)
Verwenden Sie die `FOREIGN KEY`-Klausel innerhalb der Spaltendefinitionen oder am Ende der Tabellendefinition.

**Grundlegende Syntax:**
```
CREATE TABLE child_table (
    child_column1 datatype,
    foreign_key_column datatype,
    -- Weitere Spalten...
    CONSTRAINT constraint_name
    FOREIGN KEY (foreign_key_column) 
    REFERENCES parent_table (parent_key_column)
);
```

**Beispiel:**
Angenommen, Sie haben eine Tabelle `departments` mit einem Primärschlüssel `dept_id`:
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

Erstellen Sie nun eine Tabelle `employees` mit einem Fremdschlüssel, der auf `dept_id` verweist:
```
CREATE TABLE employees (
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INTEGER,
    CONSTRAINT fk_emp_dept 
    FOREIGN KEY (dept_id) 
    REFERENCES departments (dept_id)
);
```

Dies erstellt einen Fremdschlüssel namens `fk_emp_dept` auf `dept_id` in `employees`.

#### 2. Hinzufügen eines Fremdschlüssels zu einer bestehenden Tabelle (`ALTER TABLE`)
Verwenden Sie `ALTER TABLE`, um die Constraint nachträglich hinzuzufügen. Der Elterntabellenschlüssel muss bereits existieren.

**Grundlegende Syntax:**
```
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name 
FOREIGN KEY (foreign_key_column) 
REFERENCES parent_table (parent_key_column);
```

**Beispiel:**
Um denselben Fremdschlüssel zu einer bestehenden `employees`-Tabelle hinzuzufügen:
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### Zusätzliche Optionen
Sie können Aktionen für den Fall festlegen, dass ein Elterndatensatz aktualisiert oder gelöscht wird:
- `ON DELETE CASCADE`: Löscht Kinddatensätze, wenn der Elterndatensatz gelöscht wird.
- `ON DELETE SET NULL`: Setzt den Fremdschlüssel in den Kinddatensätzen auf NULL.
- `ON UPDATE CASCADE`: Aktualisiert die Schlüssel in den Kinddatensätzen, wenn sich der Schlüssel der Elterntabelle ändert.
- `ON UPDATE SET NULL`: Setzt den Wert auf NULL, wenn der Schlüssel der Elterntabelle aktualisiert wird.

**Beispiel mit Optionen:**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### Wichtige Regeln und Überlegungen
- Die Fremdschlüsselspalten müssen im Datentyp und in der Länge mit den Spalten des Elterntabellenschlüssels übereinstimmen.
- Die Elterntabelle muss vor dem Erstellen des Fremdschlüssels einen Primärschlüssel oder eindeutigen Schlüssel definiert haben.
- Fremdschlüssel können auf dieselbe Tabelle verweisen (selbstreferenziell).
- Mehrere Spalten können einen zusammengesetzten Fremdschlüssel bilden: `FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`.
- So entfernen Sie einen Fremdschlüssel: `ALTER TABLE child_table DROP CONSTRAINT constraint_name;`.
- Es wird empfohlen, für eine bessere Performance einen Index auf den Fremdschlüsselspalten zu erstellen.

Testen Sie dies in einer Entwicklungsumgebung, da das Hinzufügen von Constraints fehlschlagen kann, wenn bestehende Daten dagegen verstoßen (z. B. verwaiste Zeilen).

#### Referenzen
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)