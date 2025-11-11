---
audio: false
generated: true
lang: de
layout: post
title: SQL SELECT-Anweisungen
translated: true
type: note
---

Um Ihre Frage zur Verwendung von `SELECT`, `LEFT JOIN`, `RIGHT JOIN`, komplexem `SELECT`, `FROM`, `GROUP BY`, `WHERE NOT IN` und `IN` in SQL zu beantworten, werde ich jede Komponente klar erklären und praktische Beispiele liefern. Dies sind grundlegende SQL-Operationen, die zum Abrufen und Manipulieren von Daten aus Datenbanken verwendet werden. Lassen Sie uns das Schritt für Schritt aufschlüsseln, wobei wir für Konsistenz ein einfaches Datenbankschema verwenden:

- **Tabellen:**
  - `employees` (Spalten: `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (Spalten: `department_id`, `department_name`)
  - `projects` (Spalten: `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
Die `SELECT`-Klausel wird verwendet, um die Spalten anzugeben, die Sie aus einer Datenbanktabelle abrufen möchten. Sie bildet die Grundlage jeder SQL-Abfrage.

- **Zweck:** Auswählen, welche Daten angezeigt werden sollen.
- **Beispiel:**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  Dies ruft die Spalten `employee_name` und `salary` aus der Tabelle `employees` ab.

---

### 2. FROM
Die `FROM`-Klausel identifiziert die Tabelle (oder Tabellen), aus der die Daten gezogen werden sollen. Sie wird immer mit `SELECT` verwendet.

- **Zweck:** Die Datenquelle angeben.
- **Beispiel:**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  Hier ist `employees` die abgefragte Tabelle.

---

### 3. LEFT JOIN
Ein `LEFT JOIN` (oder `LEFT OUTER JOIN`) kombiniert Zeilen aus zwei Tabellen. Er gibt alle Datensätze aus der linken Tabelle und die passenden Datensätze aus der rechten Tabelle zurück. Wenn keine Übereinstimmung vorliegt, enthält das Ergebnis `NULL`-Werte für die Spalten der rechten Tabelle.

- **Zweck:** Alle Zeilen der linken Tabelle einbeziehen, unabhängig von Übereinstimmungen in der rechten Tabelle.
- **Beispiel:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Dies listet alle Mitarbeiter und ihre Abteilungsnamen auf. Wenn ein Mitarbeiter keiner Abteilung zugeordnet ist, wird `department_name` `NULL` sein.

---

### 4. RIGHT JOIN
Ein `RIGHT JOIN` (oder `RIGHT OUTER JOIN`) ähnelt einem `LEFT JOIN`, gibt aber alle Datensätze aus der rechten Tabelle und die passenden Datensätze aus der linken Tabelle zurück. Nicht übereinstimmende Zeilen der linken Tabelle führen zu `NULL`-Werten.

- **Zweck:** Alle Zeilen der rechten Tabelle einbeziehen, unabhängig von Übereinstimmungen in der linken Tabelle.
- **Beispiel:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Dies zeigt alle Abteilungen und ihre Mitarbeiter. Abteilungen ohne Mitarbeiter haben `NULL` in `employee_name`.

---

### 5. Komplexes SELECT
Ein "komplexes `SELECT`" ist kein formaler SQL-Begriff, bezieht sich aber typischerweise auf eine `SELECT`-Anweisung, die mehrere Klauseln, Joins, Unterabfragen oder Aggregatfunktionen kombiniert, um eine erweiterte Datenabfrage durchzuführen.

- **Zweck:** Komplexe Abfragen mit mehreren Operationen bewältigen.
- **Beispiel:**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  Dies findet Abteilungen mit mehr als 5 Mitarbeitern, zählt die Mitarbeiter pro Abteilung und filtert die Ergebnisse.

---

### 6. GROUP BY
Die `GROUP BY`-Klausel gruppiert Zeilen mit denselben Werten in bestimmten Spalten zu zusammenfassenden Zeilen, oft verwendet mit Aggregatfunktionen wie `COUNT`, `SUM` oder `AVG`.

- **Zweck:** Daten auf Basis von Spaltenwerten aggregieren.
- **Beispiel:**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  Dies zählt die Anzahl der Mitarbeiter in jeder Abteilung.

---

### 7. WHERE NOT IN
Die `WHERE NOT IN`-Klausel filtert Zeilen, in denen der Wert einer Spalte nicht in einer bestimmten Liste oder im Ergebnis einer Unterabfrage vorhanden ist. Vorsicht: Wenn die Liste/die Unterabfrage `NULL` enthält, werden möglicherweise keine Zeilen zurückgegeben.

- **Zweck:** Zeilen auf Basis einer Wertemenge ausschließen.
- **Beispiel:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  Dies ruft Mitarbeiter ab, die nicht in den Abteilungen 1 oder 2 sind.

- **Mit Unterabfrage:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  Dies findet Mitarbeiter, die nicht in als 'Inactive' markierten Abteilungen sind.

---

### 8. IN
Die `IN`-Klausel filtert Zeilen, in denen der Wert einer Spalte mit einem beliebigen Wert in einer Liste oder Unterabfrage übereinstimmt. Es ist eine Kurzform für mehrere `OR`-Bedingungen.

- **Zweck:** Zeilen auf Basis einer Wertemenge einbeziehen.
- **Beispiel:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  Dies ruft Mitarbeiter in den Abteilungen 3 oder 4 ab.

- **Mit Unterabfrage:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (
      SELECT department_id
      FROM employees
      GROUP BY department_id
      HAVING COUNT(employee_id) > 5
  );
  ```
  Dies findet Mitarbeiter in Abteilungen mit mehr als 5 Mitarbeitern.

---

### Alles zusammenfügen
Hier ist ein Beispiel, das mehrere dieser Operationen kombiniert:
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **Erklärung:**
  - `FROM departments d`: Beginnt mit der Tabelle `departments`.
  - `LEFT JOIN employees e`: Bezieht alle Abteilungen ein, auch solche ohne Mitarbeiter.
  - `WHERE NOT IN (1, 2)`: Schließt Mitarbeiter aus den Abteilungen 1 und 2 aus.
  - `GROUP BY d.department_name`: Gruppiert die Ergebnisse nach Abteilungsnamen.
  - `SELECT ... COUNT`: Zählt die Mitarbeiter pro Abteilung.

---

### Wichtige Tipps
- **Joins:** Wählen Sie `LEFT JOIN` oder `RIGHT JOIN` basierend darauf, welche Zeilen der Tabelle (links oder rechts) Sie vollständig behalten möchten.
- **NULLs mit NOT IN:** Wenn eine Unterabfrage `NULL` zurückgibt, schließt `NOT IN` möglicherweise unerwartet alle Zeilen aus. Ziehen Sie `NOT EXISTS` als Alternative in Betracht.
- **Komplexe Abfragen:** Unterteilen Sie sie in Teile (z. B. Joins separat testen), um die Richtigkeit zu gewährleisten.
- **Reihenfolge ist wichtig:** Platzieren Sie `WHERE` vor `GROUP BY` und verwenden Sie `HAVING` nach `GROUP BY` für Filter auf Gruppenebene.

Indem Sie diese SQL-Komponenten verstehen und kombinieren – `SELECT`, `FROM`, `LEFT JOIN`, `RIGHT JOIN`, `GROUP BY`, `WHERE NOT IN` und `IN` – können Sie Abfragen erstellen, um Daten effektiv aus jeder relationalen Datenbank abzurufen und zu analysieren.