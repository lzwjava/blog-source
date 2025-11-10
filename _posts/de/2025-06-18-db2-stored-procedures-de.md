---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Aufruf von DB2-Gespeicherten Prozeduren mit Parametern
translated: true
type: note
---

### Annahmen und Kontext
Ihre Anfrage scheint sich auf den Aufruf einer *Stored Procedure* (wahrscheinlich ein Tippfehler für "stored procedure") in einem IBM-Datenbanksystem wie IBM DB2 (auf Linux/Unix/Windows, z/OS oder iSeries) zu beziehen. Stored Procedures sind ausführbare Skripte, die in der Datenbank gespeichert sind und Eingabeparameter akzeptieren, Operationen durchführen sowie Ausgaben oder Ergebnisse zurückgeben können. Die genaue Syntax hängt von der Programmiersprache und der IBM-Umgebung ab (z.B. SQL, COBOL, RPG oder Java über JDBC). Ich konzentriere mich auf den häufigsten Fall: SQL-basierte CALL-Anweisungen in DB2, da dies für relationale Datenbanken Standard ist.

Falls Sie eine andere IBM-Plattform verwenden (z.B. IBM i CL-Befehle, MQ oder Watson Query), geben Sie bitte weitere Details für eine maßgeschneiderte Beratung an.

### Wie Parameter in einem DB2 Stored Procedure Aufruf übergeben werden
Stored Procedures in DB2 werden mit der `CALL`-Anweisung in SQL aufgerufen. Parameter werden in einer kommagetrennten Liste innerhalb von Klammern übergeben, entsprechend der Definition der Prozedur (z.B. IN für Eingabe, OUT für Ausgabe, INOUT für beides).

#### Schritt-für-Schritt Anleitung
1. **Definieren oder Kennen der Prozedursignatur**: Stellen Sie sicher, dass Sie den Namen und die Parameter der Prozedur kennen. Beispielsweise könnte eine Prozedur so definiert sein:
   ```sql
   CREATE PROCEDURE update_employee (IN emp_id INT, IN new_salary DECIMAL(10,2), OUT status_msg VARCHAR(100))
   ```
   - Hier ist `emp_id` eine Eingabe (IN), `new_salary` eine Eingabe und `status_msg` eine Ausgabe (OUT).

2. **Verwenden der CALL-Anweisung**: Rufen Sie die Prozedur in einer SQL-Umgebung auf (z.B. DB2 Command Line Processor oder eingebettet in Programmen wie Java):
   ```sql
   CALL update_employee(12345, 75000.00, ?);
   ```
   - Das `?` ist ein Platzhalter für OUT-Parameter. In programmatischen Aufrufen werden Ausgaben über Result Sets oder Host-Variablen behandelt.
   - Eingaben werden als Literale oder Variablen übergeben; Ausgaben werden über Platzhalter oder gebundene Variablen erfasst.

3. **Behandlung von Parametertypen**:
   - **IN-Parameter**: Übergeben Sie Werte direkt (z.B. Zahlen, Zeichenketten in Anführungszeichen).
   - **OUT/INOUT-Parameter**: Verwenden Sie `?` im CALL, binden Sie diese dann in Ihrem Code, um die Werte nach der Ausführung abzurufen.
   - Passen Sie die Reihenfolge und Typen exakt an; Fehlanpassungen verursachen Fehler (z.B. SQLCODE -440 für ungültige Parameter).

4. **In Code-Beispielen**:
   - **Über DB2 CLP (Command Line)**: Direkte SQL-Ausführung.
     ```sql
     CALL my_proc('input_value', ?);
     ```
     Holen Sie OUT-Parameter mit `FETCH FIRST FROM` oder in Skripten ab.
   - **Über JDBC (Java)**:
     ```java
     CallableStatement stmt = conn.prepareCall("{CALL update_employee(?, ?, ?)}");
     stmt.setInt(1, 12345);          // IN-Parameter
     stmt.setBigDecimal(2, new java.math.BigDecimal("75000.00")); // IN-Parameter
     stmt.registerOutParameter(3, Types.VARCHAR); // OUT-Parameter
     stmt.execute();
     String status = stmt.getString(3); // OUT-Parameter abrufen
     ```
   - **Über RPG auf IBM i**: Verwenden Sie `CALLP` mit Variablendeklarationen, die den Parametertypen entsprechen.
     ```rpg
     D PROC_PARAM    S                   LIKE(PARAM_TYPE)
     PROC_PARAM = 'value';
     CALLP MY_PROC(PROC_PARAM);
     ```
   - **Fehlerbehandlung**: Überprüfen Sie SQLSTATE oder SQLCODE nach dem Aufruf; z.B. bedeutet '00000' Erfolg.

#### Wichtige Tipps und Belege
- **Belege aus der DB2-Dokumentation**: Laut dem offiziellen DB2 SQL Reference von IBM (z.B. für LUW v11.5 oder z/OS) ist die `CALL`-Anweisung mit optionalen Parameterlisten definiert. Die Syntax lautet beispielsweise: `CALL procedure-name [(parameter [, parameter] ...)]`. Dies entspricht den Industriestandards für relationale Datenbanken und wird für Konsistenz über DB2-Varianten hinweg unterstützt (siehe IBM Knowledge Center).
- **Varianten**: Auf IBM i (AS400) könnten Prozeduren CL-Befehle (Command Language) wie `CALL PGM(MYPROC) PARM('value')` für RPG-Programme verwenden. Für Mainframe COBOL betten Sie `EXEC SQL CALL...` mit Host-Variablen ein.
- **Tests**: Verwenden Sie `db2 describe routine procedure_name`, um Parameter vor dem Aufruf zu inspizieren.
- **Einschränkungen**: Große Parametersätze benötigen möglicherweise Arrays oder Result Sets; komplexe Typen erfordern eine spezifische Behandlung.

Falls dies nicht Ihrer Einrichtung entspricht (z.B. wenn es sich um IBM Watson oder ein anderes Tool handelt), teilen Sie bitte mehr Kontext wie die Plattform oder Sprache mit, um präzise Anweisungen zu erhalten.