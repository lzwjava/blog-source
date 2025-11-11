---
audio: false
generated: true
lang: de
layout: post
title: Schritte zur Überprüfung von Oracle-DB-Tabellen auf Daten mit DBeaver
translated: true
type: note
---

Ich nehme an, Sie fragen, wie Sie DBeaver verwenden können, um zu überprüfen, welche Oracle Database Tabellen Daten enthalten, basierend auf Ihrer vorherigen Frage zur Suche nach Tabellen mit Daten in Oracle DB. DBeaver ist ein beliebtes, kostenloses, plattformübergreifendes Datenbanktool, das gut mit Oracle und anderen Datenbanken funktioniert. Im Folgenden zeige ich Ihnen, wie Sie DBeaver verwenden können, um Ihre Oracle-Schemata zu inspizieren und Tabellen mit Daten zu identifizieren.

---

#### 1. **Eine Verbindung zu Ihrer Oracle-Datenbank einrichten**
   - **DBeaver installieren**: Laden Sie DBeaver herunter und installieren Sie es (die Community Edition ist ausreichend) von [dbeaver.io](https://dbeaver.io/), falls Sie dies noch nicht getan haben.
   - **Eine neue Verbindung erstellen**:
     1. Öffnen Sie DBeaver und klicken Sie im Menü auf **Datenbank** > **Neue Datenbankverbindung**.
     2. Wählen Sie **Oracle** aus der Liste aus und klicken Sie auf **Weiter**.
     3. Geben Sie Ihre Verbindungsdetails ein:
        - **Host**: Der Hostname oder die IP-Adresse Ihres Oracle-Servers.
        - **Port**: Typischerweise 1521 (Standard für Oracle).
        - **Datenbank/SID oder Service Name**: Abhängig von Ihrem Setup (z.B. SID = `XE` für Express Edition oder ein Service Name).
        - **Benutzername** und **Passwort**: Ihre Oracle-Anmeldedaten.
     4. Klicken Sie auf **Verbindung testen**, um zu überprüfen, ob sie funktioniert. Sie müssen möglicherweise den Oracle JDBC-Treiber herunterladen, wenn Sie dazu aufgefordert werden (DBeaver kann dies automatisch erledigen).
     5. Klicken Sie auf **Fertig stellen**, um die Verbindung zu speichern.

#### 2. **Schemata im Datenbank-Navigator erkunden**
   - Erweitern Sie im **Datenbank-Navigator** (linker Bereich) Ihre Oracle-Verbindung.
   - Sie sehen eine Liste von Schemata (z.B. Ihren Benutzernamen oder andere, auf die Sie Zugriff haben). Erweitern Sie das Schema, das Sie inspizieren möchten.
   - Erweitern Sie unter jedem Schema den Knoten **Tabellen**, um alle Tabellen zu sehen.

#### 3. **Überprüfen Sie Tabellen auf Daten über die GUI**
   - **Tabellendaten anzeigen**:
     1. Doppelklicken Sie auf einen Tabellennamen oder klicken Sie mit der rechten Maustaste darauf und wählen Sie **Tabelle bearbeiten**.
     2. Wechseln Sie im sich öffnenden Editor zum Tab **Daten**.
     3. Wenn die Tabelle Daten enthält, werden Zeilen angezeigt. Wenn sie leer ist, werden keine Zeilen angezeigt (oder eine Meldung wie "Keine Daten").
     - Standardmäßig ruft DBeaver bis zu 200 Zeilen ab. Um alle Zeilen abzurufen, klicken Sie auf die Schaltfläche **Alle Zeilen abrufen** (ein kleines Pfeilsymbol) in der unteren Symbolleiste des Daten-Tabs.
   - **Zeilen schnell zählen**:
     1. Klicken Sie mit der rechten Maustaste auf die Tabelle im Datenbank-Navigator.
     2. Wählen Sie **Navigieren** > **Zeilenzahl**.
     3. DBeaver führt eine `SELECT COUNT(*)`-Abfrage aus und zeigt das Ergebnis in einem Pop-up-Fenster an. Wenn der Wert 0 ist, ist die Tabelle leer.

#### 4. **Führen Sie SQL-Abfragen aus, um mehrere Tabellen zu überprüfen**
   - Wenn Sie viele Tabellen auf einmal überprüfen möchten (effizienter als das Anklicken jeder einzelnen), verwenden Sie den SQL-Editor:
     1. Klicken Sie auf **SQL Editor** > **Neues SQL-Skript** (oder drücken Sie `Strg + [`).
     2. Setzen Sie den Schema-Kontext:
        - Verwenden Sie das Dropdown-Menü oben im SQL-Editor, um Ihr Schema auszuwählen, oder führen Sie aus:
          ```sql
          ALTER SESSION SET CURRENT_SCHEMA = schema_name;
          ```
          Ersetzen Sie `schema_name` durch Ihr Ziel-Schema (z.B. `HR`).
     3. Fragen Sie die Zeilenanzahl für alle Tabellen ab:
        - Verwenden Sie dieses SQL, um Tabellen mit Daten aufzulisten (ähnlich wie in meiner vorherigen Antwort):
          ```sql
          SELECT table_name, num_rows
          FROM user_tables
          WHERE num_rows > 0
          ORDER BY num_rows DESC;
          ```
        - Führen Sie es durch Drücken von `Strg + Eingabe` aus. Die Ergebnisse erscheinen im Tab **Ergebnisse** unten.
        - `USER_TABLES` zeigt Tabellen in Ihrem Schema an. Verwenden Sie `ALL_TABLES` für Tabellen, auf die Sie schemaübergreifend Zugriff haben:
          ```sql
          SELECT owner, table_name, num_rows
          FROM all_tables
          WHERE num_rows > 0
          AND owner = UPPER('schema_name');
          ```
     4. **Hinweis**: `NUM_ROWS` ist eine Schätzung basierend auf dem letzten Statistik-Update. Wenn sie ungenau ist, aktualisieren Sie die Statistiken mit:
        ```sql
        EXEC DBMS_STATS.GATHER_SCHEMA_STATS('schema_name');
        ```