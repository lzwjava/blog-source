---
audio: false
generated: true
lang: de
layout: post
title: Tabellen mit Daten in Oracle DB identifizieren
translated: true
type: note
---

In Oracle Database, wenn Sie Schemas untersuchen und feststellen, dass einige Tabellen "leer" erscheinen, wenn Sie darauf klicken (z. B. über ein GUI-Tool wie SQL Developer oder Toad), bedeutet das nicht unbedingt, dass sie keine Daten enthalten. Es könnte mehrere Gründe geben: Berechtigungen, Filter, oder Sie schauen schlichtweg auf die falschen Tabellen. Um systematisch herauszufinden, welche Tabellen in einem Schema Daten enthalten, können Sie die Datenbank-Metadaten abfragen oder die Tabellen direkt überprüfen. So geht's:

#### 1. **Überprüfen Sie Ihre Berechtigungen**
   - Wenn Sie leere Tabellen sehen, fehlen Ihnen möglicherweise die Berechtigungen, um die Daten einzusehen. Stellen Sie sicher, dass Sie `SELECT`-Berechtigungen für die Tabellen im Schema haben.
   - Führen Sie diese Abfrage aus, um Ihre Berechtigungen für eine bestimmte Tabelle zu prüfen:
     ```sql
     SELECT privilege
     FROM dba_tab_privs
     WHERE grantee = UPPER('ihr_benutzername')
     AND table_name = UPPER('tabellenname');
     ```
     Ersetzen Sie `'ihr_benutzername'` und `'tabellenname'` entsprechend. Wenn nichts angezeigt wird, bitten Sie den Schema-Besitzer oder den DBA, Ihnen Zugriff zu gewähren.

#### 2. **Abfragen der Zeilenanzahl in Tabellen**
   - Oracle verwaltet Statistiken über Tabellen, einschließlich Zeilenanzahlen, in den Views `USER_TABLES`, `ALL_TABLES` oder `DBA_TABLES` (abhängig von Ihrem Zugriffslevel).
   - So sehen Sie Tabellen mit Daten im aktuellen Schema:
     ```sql
     SELECT table_name, num_rows
     FROM user_tables
     WHERE num_rows > 0
     ORDER BY num_rows DESC;
     ```
     - `USER_TABLES`: Zeigt Tabellen, die dem aktuellen Benutzer gehören.
     - `NUM_ROWS`: Ungefähre Anzahl der Zeilen (basierend auf dem letzten Statistik-Update).

   - Wenn Sie Zugriff auf ein anderes Schema haben (z. B. via `ALL_TABLES`):
     ```sql
     SELECT owner, table_name, num_rows
     FROM all_tables
     WHERE num_rows > 0
     AND owner = UPPER('schema_name')
     ORDER BY num_rows DESC;
     ```
     Ersetzen Sie `'schema_name'` durch das Schema, das Sie untersuchen.

   **Hinweis**: `NUM_ROWS` könnte veraltet sein, wenn die Statistiken nicht kürzlich aktualisiert wurden. Siehe Schritt 5, um sie zu aktualisieren.

#### 3. **Manuelles Überprüfen bestimmter Tabellen**
   - Wenn Sie vermuten, dass `NUM_ROWS` unzuverlässig ist, oder Sie es verifizieren möchten, führen Sie ein `COUNT(*)` für einzelne Tabellen aus:
     ```sql
     SELECT table_name
     FROM user_tables;
     ```
     Dies listet alle Tabellen in Ihrem Schema auf. Dann für jede Tabelle:
     ```sql
     SELECT COUNT(*) FROM tabellenname;
     ```
     Wenn die Anzahl größer als 0 ist, hat die Tabelle Daten. Seien Sie vorsichtig bei großen Tabellen – `COUNT(*)` kann langsam sein.

#### 4. **Verwenden Sie ein Script zur automatischen Überprüfung**
   - Um manuelles Abfragen jeder Tabelle zu vermeiden, verwenden Sie ein PL/SQL-Skript, um die Zeilenanzahlen über alle Tabellen eines Schemas hinweg zu prüfen:
     ```sql
     BEGIN
         FOR t IN (SELECT table_name FROM user_tables)
         LOOP
             EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || t.table_name INTO v_count;
             IF v_count > 0 THEN
                 DBMS_OUTPUT.PUT_LINE(t.table_name || ' hat ' || v_count || ' Zeilen');
             END IF;
         END LOOP;
     EXCEPTION
         WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Fehler bei Tabelle ' || t.table_name || ': ' || SQLERRM);
     END;
     /
     ```
     - Aktivieren Sie die Ausgabe in Ihrem Tool (z. B. `SET SERVEROUTPUT ON` in SQL*Plus oder SQL Developer).
     - Dies gibt nur Tabellen mit Daten aus. Passen Sie `user_tables` auf `all_tables` an und fügen Sie `owner`-Filterung hinzu, wenn Sie ein anderes Schema prüfen.

#### 5. **Tabellenstatistiken aktualisieren (falls nötig)**
   - Wenn `NUM_ROWS` in `USER_TABLES` oder `ALL_TABLES` 0 anzeigt oder falsch erscheint, könnten die Statistiken veraltet sein. So aktualisieren Sie sie:
     ```sql
     EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'schema_name');
     ```
     Ersetzen Sie `'schema_name'` durch den Schemanamen (verwenden Sie Ihren Benutzernamen für Ihr eigenes Schema). Führen Sie dann die `USER_TABLES`-Abfrage aus Schritt 2 erneut aus.

#### 6. **Auf partitionierte Tabellen prüfen**
   - Wenn das Schema partitionierte Tabellen verwendet, könnten die Daten über Partitionen verteilt sein, und eine einfache Abfrage spiegelt dies möglicherweise nicht wider. Prüfen Sie auf Partitionen:
     ```sql
     SELECT table_name, partition_name, num_rows
     FROM user_tab_partitions
     WHERE num_rows > 0
     ORDER BY table_name, partition_name;
     ```
     Dies zeigt an, welche Partitionen Daten enthalten.

#### 7. **GUI-Tool-Tipps (z. B. SQL Developer)**
   - Wenn Sie ein GUI wie Oracle SQL Developer verwenden:
     1. Klicken Sie mit der rechten Maustaste auf das Schema im Connections-Bereich.
     2. Erweitern Sie den "Tables"-Knoten.
     3. Klicken Sie mit der rechten Maustaste auf eine Tabelle, wählen Sie "Count Rows" oder öffnen Sie den "Data"-Tab, um eine Vorschau der Inhalte anzuzeigen (falls erlaubt).
     - Wenn der "Data"-Tab leer ist, könnte es an Berechtigungen liegen oder die Tabelle hat tatsächlich keine Zeilen.

---

### Praktisches Beispiel
Angenommen, Sie sind in einem Schema namens `HR`. Sie würden:
1. Ausführen:
   ```sql
   SELECT table_name, num_rows
   FROM user_tables
   WHERE num_rows > 0;
   ```
   Die Ausgabe könnte so aussehen:
   ```
   TABLE_NAME   NUM_ROWS
   ----------   --------
   EMPLOYEES    107
   DEPARTMENTS  27
   ```
   Dies sagt Ihnen, dass `EMPLOYEES` und `DEPARTMENTS` Daten enthalten.

2. Wenn Sie veraltete Statistiken vermuten, aktualisieren Sie sie:
   ```sql
   EXEC DBMS_STATS.GATHER_SCHEMA_STATS('HR');
   ```
3. Überprüfen Sie mit derselben Abfrage erneut.

---

### Warum Tabellen leer erscheinen könnten
- **Keine Daten**: Die Tabelle hat tatsächlich keine Zeilen.
- **Berechtigungen**: Sie können die Tabellenstruktur sehen, aber nicht die Daten.
- **Filter**: Ihr GUI-Tool könnte Filter haben, die Zeilen ausblenden (z. B. eine `WHERE`-Klausel).
- **Abgeschnittene/Gelöschte Daten**: Daten wurden möglicherweise kürzlich entfernt.
- **Synonyms/Views**: Sie schauen möglicherweise auf ein Synonym oder einen View, der auf eine leere oder nicht zugängliche Tabelle verweist.

Wenn Sie immer noch nicht weiterkommen, teilen Sie mir Ihre spezifische Einrichtung mit (z. B. Schemaname, verwendetes Tool), und ich kann die Ratschläge weiter anpassen!