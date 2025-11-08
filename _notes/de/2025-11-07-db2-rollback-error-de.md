---
audio: false
generated: true
image: false
lang: de
layout: post
model: moonshotai/kimi-k2-thinking
title: DB2-Transaktionsrollback und Fehlererkennung
translated: true
type: note
---

## Wenn DB2 aufgrund von Systemfehlern einen Rollback durchführt

IBM DB2 führt automatisch Rollbacks von Transaktionen durch, wenn kritische Systemfehler auftreten, die die Datenintegrität gefährden. Häufige Szenarien sind:

- **Deadlocks oder Timeouts**: SQLCODE -911 mit SQLSTATE 40001, Grundcode "2" zeigt an, dass die Transaktion aufgrund eines Deadlocks zurückgesetzt wurde
- **Prozess-Abend (abnormales Ende)**: In allen DB2-Umgebungen löst ein Prozessabbruch ein implizites Rollback aus
- **Systemressourcen-Fehler**: Speicher-, Festplatten- oder Netzwerkfehler, die den Abschluss der Transaktion verhindern
- **Timestamp-Konflikte**: SQLCODE -818 tritt auf, wenn interne Timestamps zwischen Modul und DBRM nicht übereinstimmen
- **Connection-Pooling-Sicherheitsnetze**: Einige Implementierungen setzen Verbindungen beim Freigeben automatisch zurück, um zu verhindern, dass nicht commitete Transaktionen Locking-Probleme verursachen

## Wie man detaillierte Fehlerinformationen erkennt

### 1. Primäre Fehlererkennungsmechanismen

**SQLCODE und SQLSTATE**
Nach jeder SQL-Anweisung setzt DB2 diese Variablen:

```sql
-- Unmittelbar nach Anweisungsausführung prüfen
IF SQLCODE < 0 THEN
    -- Fehler ist aufgetreten
    ROLLBACK;
END IF;
```

SQLSTATE-Class-Codes identifizieren spezifisch Fehlertypen:
- **Class 58**: Systemfehler (z.B. Ressource nicht verfügbar, Operator-Eingriff)
- **Class 40**: Transaktions-Rollback
- **Class 25**: Ungültiger Transaktionszustand

**GET DIAGNOSTICS-Anweisung**
Für detaillierte Fehlerinformationen in SQL PL gespeicherten Prozeduren:

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. Kommandozeilen-Fehlererkennung

Bei der Ausführung von Scripts über die `db2`-Kommandozeile Exit-Codes prüfen:

- **Exit code 8**: Systemfehler
- **Exit code 4**: DB2-Fehler (Constraint-Verletzung, Objekt nicht gefunden)
- **Exit code 2**: DB2-Warnung
- **Exit code 1**: Keine Zeilen gefunden

**Empfohlenes Script-Muster**:
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # Detaillierten Fehler überprüfen
else
    db2 commit
fi
```

### 3. Fehlerbehandlung in gespeicherten Prozeduren

Für umfassende Fehlererkennung in SQL PL deklarierte Handler verwenden:

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- Exit-Handler für jede Exception deklarieren
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- Fehlerdetails in Tabelle oder Datei protokollieren
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- Ihre transaktionale Logik hier
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. DB2-Diagnoseprotokolldateien

Für System-Level-Fehler immer prüfen:

- **db2diag.log**: Primäres Diagnoseprotokoll mit detaillierten Systemfehlerinformationen
- **Notification log**: Enthält Fehlerzusammenfassungen
- **Kommandozeilenprotokolle**: Option `-l logfile.txt` verwenden, um Fehler zu erfassen

## Best Practices für die Fehlererkennung

1. **Immer SQLCODE/SQLSTATE unmittelbar** nach kritischen Operationen prüfen
2. **GET DIAGNOSTICS verwenden** für umfangreichen Fehlerkontext in gespeicherten Prozeduren
3. **Transaction-Rollback-Prozentsatz überwachen** - alles über 1% rechtfertigt eine Untersuchung
4. **Kommandooptionen für Script-Ausführung aktivieren**:
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   Wobei `+c` Autocommit deaktiviert und `-s` bei Fehler anhält
5. **Savepoints verwenden** für partielle Rollbacks innerhalb komplexer Transaktionen
6. **Fehlerdetails protokollieren** in persistenten Tabellen vor Rollback, um Diagnoseinformationen zu erhalten

## Wichtige Systemfehler-SQLSTATEs zur Überwachung

| SQLSTATE | Beschreibung | Aktion |
|----------|-------------|--------|
| **58004** | Systemfehler (verschiedene Ursachen) | db2diag.log sofort prüfen |
| **58008** | Kommunikationsfehler | Netzwerk/Verbindung überprüfen |
| **HY000** | Allgemeiner Treiberfehler | ODBC/JDBC-Treiberprotokolle prüfen |
| **40001** | Deadlock/Timeout | Transaktion mit Backoff wiederholen |

Für Produktionsumgebungen sollten Monitoring-Tools bei **SQLCODE < 0** und **Class 58 SQLSTATEs** alarmieren, um System-Level-Probleme proaktiv zu erkennen, bevor sie kaskadieren.