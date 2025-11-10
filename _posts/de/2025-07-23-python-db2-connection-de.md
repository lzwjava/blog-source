---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python mit IBM DB2 verbinden
translated: true
type: note
---

### Übersicht
IBM DB2 ist ein relationales Datenbankmanagementsystem, und Python kann mit ihm über das `ibm_db`-Paket interagieren, das eine Low-Level-Schnittstelle bereitstellt, sowie über `ibm_db_dbi`, einen DB-API-2.0-konformen Wrapper, der auf `ibm_db` aufsetzt, um eine einfachere, pythonischere Nutzung zu ermöglichen. `ibm_db` ist direkter und leistungsfähiger, erfordert aber tiefergehendes Wissen, während `ibm_db_dbi` Pythons `sqlite3`-Modul nachahmt und es so für Standard-Datenbankoperationen einfacher macht. Beide sind Teil der IBM DB2 Python-Treiber.

### Installation
Installieren Sie die Pakete mit pip:
```
pip install ibm_db
pip install ibm_db_dbi
```
Hinweis: Diese benötigen eine DB2-Client-Bibliothek. Für Windows/Linux laden Sie das IBM Data Server Driver Package von der IBM-Website herunter und installieren es. Unter macOS könnte eine zusätzliche Einrichtung erforderlich sein. Stellen Sie sicher, dass Ihr DB2-Server erreichbar ist (z.B. auf einem Host mit den entsprechenden Anmeldedaten läuft).

### Verwendung von ibm_db
`ibm_db` bietet Funktionen zum Verbinden, Ausführen von Anweisungen und Verarbeiten von Ergebnissen. Es ist nicht DB-API-konform, bietet aber mehr Kontrolle.

#### Grundlegende Verbindung und Abfrage
```python
import ibm_db

# Verbindungsstring-Format: DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Verbinden
conn = ibm_db.connect(conn_str, "", "")

# Eine Abfrage ausführen
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# Ergebnisse abrufen (einzeln)
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # Gibt ein Dictionary zurück
    row = ibm_db.fetch_assoc(stmt)

# Schließen
ibm_db.close(conn)
```
- **Wichtige Funktionen**: `connect()`, `exec_immediate()` für einfache Abfragen, `prepare()` und `execute()` für parametrisierte Abfragen zur Vermeidung von Injection.
- **Prepared Statements**: Verwenden Sie `prepare()`, um eine Abfrage vorzubereiten, und `execute()` mit Parametern.

#### Fehlerbehandlung
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"Verbindung fehlgeschlagen: {str(e)}")
```

### Verwendung von ibm_db_dbi
`ibm_db_dbi` implementiert DB-API 2.0, wodurch es mit Modulen wie `sqlite3` oder `psycopg2` austauschbar ist.

#### Grundlegende Verbindung und Abfrage
```python
import ibm_db_dbi

# Verbindungsstring ähnlich wie bei ibm_db
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Verbinden
conn = ibm_db_dbi.connect(conn_str)

# Cursor erstellen
cursor = conn.cursor()

# Eine Abfrage ausführen
cursor.execute("SELECT * FROM MYTABLE")

# Ergebnisse abrufen
rows = cursor.fetchall()  # Gibt eine Liste von Tupeln zurück
for row in rows:
    print(row)

# Schließen
cursor.close()
conn.close()
```
- **Parametrisierte Abfragen**: `cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – verwendet ?-Platzhalter.
- **Transaktionen**: `conn.commit()` oder `conn.rollback()`; Autocommit ist standardmäßig deaktiviert.

### Wichtige Unterschiede und wann man was verwendet

| Merkmal              | ibm_db                          | ibm_db_dbi                      |
|----------------------|---------------------------------|---------------------------------|
| Konformität          | Nicht DB-API (Low-Level)        | DB-API 2.0 konform             |
| Benutzerfreundlichkeit| Erfordert mehr Code; direkter Zugriff | Einfacher, Python-ähnliche Syntax |
| Leistung             | Potenziell schneller für komplexe Operationen | Overhead durch Wrapper         |
| Funktionalität       | Vollständige DB2-Features       | Teilmenge über DB-API-Schnittstelle |
| Anwendungsfall       | Benutzerdefinierte Apps, die rohe Kontrolle benötigen | Standard-CRUD-Operationen      |

Verwenden Sie `ibm_db_dbi` für Vertrautheit, wenn Sie an andere DB-API-Treiber gewöhnt sind. Wechseln Sie zu `ibm_db` für erweiterte DB2-spezifische Funktionen wie gespeicherte Prozeduren oder Bulk-Operationen.

### Best Practices
- Behandeln Sie immer Ausnahmen und schließen Sie Verbindungen in einem `try-finally`- oder `with`-Block, um Ressourcenlecks zu vermeiden.
- Verwenden Sie für große Ergebnismengen `fetchmany(size)` anstelle von `fetchall()`, um den Speicherverbrauch zu begrenzen.
- Überprüfen Sie die DB2-Version-Kompatibilität; die Pakete unterstützen DB2 LUW, z/OS, iSeries.
- Konsultieren Sie die IBM-Dokumentation für fortgeschrittene Themen wie SSL-Verbindungen oder CLPPlus-Integration.

Weitere Beispiele finden Sie im [IBM db2 Python driver repo](https://github.com/ibmdb/python-ibmdb). Wenn Sie auf Probleme stoßen, stellen Sie sicher, dass Ihre DB2-Instanz läuft und die Anmeldedaten korrekt sind.