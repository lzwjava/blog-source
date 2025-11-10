---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: IBM DB2 Sequenz Verwendungsleitfaden
translated: true
type: note
---

### Verwendung von IBM DB2-Sequenzen mit NEXT VALUE FOR

In IBM DB2 wird `NEXT VALUE FOR` verwendet, um den nächsten Wert aus einer Sequenz abzurufen, welche eindeutige, aufsteigende Zahlen generiert. Sequenzen sind nützlich, um Primärschlüssel oder andere eindeutige Identifikatoren zu erzeugen.

#### Beispiel: Erstellen und Verwenden einer Sequenz
1. **Sequenz erstellen** (führen Sie dies einmal in Ihrer DB2-Umgebung aus):
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - Dies erstellt eine Sequenz namens `my_sequence`, die bei 1 beginnt und sich jedes Mal um 1 erhöht.

2. **Verwenden Sie die Sequenz in einer INSERT-Anweisung**, um den nächsten Wert zu erhalten:
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - Dies fügt eine neue Zeile ein, wobei `id` der nächste Sequenzwert ist (z.B. 1 bei der ersten Verwendung, 2 bei der nächsten, usw.).

#### Wichtige Hinweise
- Sie können es auch in SELECT-Abfragen verwenden: `SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- Sequenzen sind von Tabellen getrennt und können bei Bedarf über mehrere Tabellen hinweg gemeinsam genutzt werden.
- Weitere Details finden Sie in der IBM DB2-Dokumentation zu Sequenzen. Wenn Sie Beispiele für andere Sequenzfunktionen wie `PREVIOUS VALUE FOR` benötigen, lassen Sie es mich wissen!