---
audio: false
generated: true
lang: de
layout: post
title: Abfragemaschine
translated: true
type: note
---

Eine Query-Engine ist eine Komponente eines Datenbankmanagementsystems (DBMS), die Datenbankabfragen (typischerweise in SQL oder einer ähnlichen Sprache geschrieben) interpretiert und ausführt. Ihre Hauptfunktion ist die Verarbeitung der Abfragen und die Rückgabe der entsprechenden Ergebnisse. Hier ist eine Aufschlüsselung, wie sie funktioniert:

### 1. **Parsen der Abfrage:**
   - **Lexikalische Analyse:** Der erste Schritt ist das Parsen der Abfrage, um ihre Syntax zu überprüfen. Die Engine verwendet einen lexikalischen Analysator, um die Abfrage in Tokens (z.B. Schlüsselwörter, Bezeichner, Operatoren) zu zerlegen.
   - **Syntaxanalyse:** Anschließend werden die Tokens in einen Query Tree oder Parse Tree geparst, um zu validieren, dass die Struktur der Abfrage korrekt ist. Es wird überprüft, ob die Abfrage der richtigen Grammatik folgt und ob die referenzierten Tabellen, Spalten und Bedingungen gültig sind.

### 2. **Optimierung:**
   - **Query Rewrite:** Nach dem Parsen kann die Engine die Abfrage umschreiben, um sie zu optimieren. Dies könnte das Vereinfachen bestimmter Teile der Abfrage beinhalten (z.B. das Entfernen redundanter Bedingungen oder das Kombinieren von Subqueries).
   - **Kostenbasierte Optimierung:** Der Query Optimizer generiert mehrere Ausführungspläne und bewertet dann die "Kosten" (basierend auf Faktoren wie Festplatten-I/O, CPU-Auslastung etc.) jedes Plans. Der Plan mit den niedrigsten Kosten wird zur Ausführung ausgewählt. Der Optimierer kann basierend auf Statistiken über die Daten Indizes, Join-Methoden (z.B. Nested Loops, Hash Join) und Zugriffspfade wählen.

### 3. **Generierung des Ausführungsplans:**
   - Die Query-Engine wählt den optimalen Ausführungsplan aus. Dazu gehört die Entscheidung, wie Daten abgerufen werden (unter Verwendung von Indizes, sequenziellen Scans etc.) und wie mehrere Tabellen gejoint werden.
   - Der Plan kann auch Operationen wie Sortieren, Filtern, Gruppieren und Aggregation beinhalten.

### 4. **Ausführung:**
   - Die Engine führt den Plan aus, indem sie die notwendigen Operationen in einer bestimmten Reihenfolge durchführt. Wenn sie beispielsweise zwei Tabellen joinen muss, könnte sie je nach dem vom Optimierer gewählten Plan einen Hash Join oder einen Nested Loop Join verwenden.
   - Während der Ausführung kann die Engine Daten von der Festplatte abrufen (falls sie nicht zwischengespeichert sind) und die Ergebnisse verarbeiten.

### 5. **Rückgabe der Ergebnisse:**
   - Nach der Ausführung gibt die Query-Engine die Ergebnisse an den Benutzer oder die Anwendung zurück. Die Ergebnisse könnten in Form eines Satzes von Zeilen und Spalten (für SELECT-Abfragen), einer Bestätigung (für INSERT/UPDATE-Abfragen) oder einer Fehlermeldung, falls etwas schiefgelaufen ist, vorliegen.

### Wichtige Komponenten einer Query-Engine:
- **Parser:** Validiert und parst SQL-Abfragen in eine interne Form.
- **Optimierer:** Findet den bestmöglichen Ausführungsplan für die Abfrage.
- **Executor:** Führt den gewählten Plan aus und ruft Daten aus der Datenbank ab.
- **Cache:** Häufig abgerufene Daten können zwischengespeichert werden, um die Ausführung nachfolgender Abfragen zu beschleunigen.

### Beispiel:
Nehmen wir an, Sie führen eine Abfrage wie diese aus:
```sql
SELECT name, age FROM users WHERE age > 30 ORDER BY age;
```

1. **Parsing:** Die Abfrage wird in einen Syntaxbaum geparst.
2. **Optimierung:** Der Optimierer könnte den besten Weg bestimmen, um Benutzer über 30 zu filtern und möglicherweise einen Index auf der Spalte `age` verwenden, falls vorhanden.
3. **Ausführung:** Die Engine ruft die relevanten Zeilen aus der Tabelle `users` ab, wendet den Filter an und sortiert die Ergebnisse nach `age`.
4. **Rückgabe der Ergebnisse:** Die Engine gibt die sortierten Ergebnisse zurück (z.B. eine Liste von Benutzern, die älter als 30 sind).

Möchten Sie tiefer in einen bestimmten Teil dieses Prozesses eintauchen?