---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht des IBM Db2-Systemkatalogs
translated: true
type: note
---

### Einführung in IBM Db2 Systemtabellen

Der Systemkatalog in IBM Db2 (auch bekannt als der Db2-Katalog) ist ein integriertes Metadaten-Repository, das detaillierte Informationen über jedes Objekt und jedes Element in Ihrer Datenbank speichert. Dazu gehören Tabellen, Views, Indizes, Spalten, Benutzer, Berechtigungen, Routinen und mehr. Es ist im Wesentlichen das "Telefonbuch" Ihrer Datenbank – automatisch von Db2 verwaltet, wenn Sie Objekte erstellen, ändern oder löschen. Der Katalog hilft Datenbankadministratoren (DBAs), Entwicklern und Tools, die Struktur und den Status der Datenbank abzufragen, ohne Anwendungscode oder externe Dateien parsen zu müssen.

Im Gegensatz zu regulären Benutzertabellen ist der Systemkatalog für die meisten Benutzer schreibgeschützt und für das Abfragen von Metadaten anstelle von datenintensiven Operationen optimiert. Er wird automatisch erstellt, wenn Sie eine neue Datenbank anlegen, und befindet sich in speziellen Table Spaces (wie SYSCATSPACE in Db2 LUW).

#### Wichtige Komponenten und Struktur
Der Systemkatalog besteht aus:
- **Basis-Tabellen**: Dies sind die zugrunde liegenden, normalisierten Tabellen, in denen die Rohmetadaten gespeichert sind. Sie befinden sich im Schema **SYSIBM** und sind für Endbenutzer nicht direkt abfragbar, um versehentliche Änderungen oder Leistungsprobleme zu vermeiden. Beispiele sind SYSIBM.SYSTABLES (grundlegende Tabelleninformationen) und SYSIBM.SYSCOLUMNS (Spaltendetails).
- **Katalog-Views**: Benutzerfreundliche, denormalisierte Views, die auf den Basistabellen aufbauen. Diese sind einfacher abzufragen und bieten eine standardisierte, SQL-konforme Schnittstelle (wie ISO). Sie sind in Schemata gruppiert:
  - **SYSCAT**: Kernmetadaten über Datenbankobjekte (z.B. Tabellen, Indizes, Trigger).
  - **SYSCOLUMNS**: Detaillierte Informationen auf Spaltenebene.
  - **SYSSTAT**: Statistische Daten, die vom Query-Optimizer verwendet werden (z.B. Zeilenanzahlen, Kardinalitäten).
  - **SYSPROC** und andere: Für Prozeduren, Funktionen und XML-bezogene Informationen.

In Db2 for z/OS befindet sich der Katalog in der Datenbank DSNDB06, aber die Konzepte sind plattformübergreifend (LUW, z/OS, i) ähnlich.

#### Zweck
- **Ermittlung**: Herausfinden, welche Objekte existieren, ihre Eigenschaften und Beziehungen.
- **Administration**: Überwachen von Berechtigungen, Abhängigkeiten und Leistungsstatistiken.
- **Entwicklung**: Generieren von DDL-Skripten, Validieren von Schemata oder Integration mit Tools wie Db2 Data Studio.
- **Optimierung**: Der Query-Optimizer verwendet SYSSTAT-Views, um Ausführungspläne auszuwählen.

#### Zugriff und Abfrage
1. **Mit der Datenbank verbinden**: Verwenden Sie `db2 connect to <dbname>`.
2. **Berechtigungen**: Standardmäßig hat PUBLIC SELECT-Berechtigung auf die Katalog-Views. Für grundlegende Abfragen sind keine speziellen Grants erforderlich, aber für die SYSIBM-Basistabellen sind SYSADM oder höhere Berechtigungen erforderlich.
3. **Abfragen**: Verwenden Sie standardmäßige SQL SELECT-Anweisungen. Views sind schemaqualifiziert (z.B. `SELECT * FROM SYSCAT.TABLES`).

**Beispielabfragen**:
- **Alle Tabellen im aktuellen Schema auflisten**:
  ```
  SELECT TABSCHEMA, TABNAME, TYPE FROM SYSCAT.TABLES
  WHERE TABSCHEMA = CURRENT SCHEMA;
  ```
  - Ausgabe: Zeigt Schema, Tabellenname und Typ (z.B. 'T' für Tabelle, 'V' für View).

- **Spaltendetails für eine Tabelle abrufen**:
  ```
  SELECT COLNAME, TYPENAME, LENGTH, NULLS
  FROM SYSCOLUMNS
  WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';
  ```
  - Ausgabe: Spaltennamen, Datentypen, Längen und Nullfähigkeit.

- **Tabellenstatistiken prüfen**:
  ```
  SELECT CARD, NPAGES FROM SYSSTAT.TABLES
  WHERE TABNAME = 'YOUR_TABLE';
  ```
  - CARD: Geschätzte Zeilenanzahl; NPAGES: Anzahl der Seiten.

Für vollständige Listen führen Sie `SELECT * FROM SYSCAT.VIEWS WHERE VIEWNAME LIKE 'SYSCAT%'` aus, um alle verfügbaren Views zu entdecken.

#### Wichtige Hinweise
- **Leistung**: Katalogabfragen sind schnell, können aber bei großen Datenbanken ressourcenintensiv sein; verwenden Sie Filter (z.B. WHERE-Klauseln), um die Ergebnisse einzuschränken.
- **Aktualisierungen**: Db2 aktualisiert den Katalog automatisch – versuchen Sie nicht, ihn manuell mit INSERT/UPDATE zu ändern.
- **Versionsunterschiede**: In Db2 11.5+ sind die Views stärker standardisiert. Für z/OS haben einige Views plattformspezifische Spalten.
- **Tool-Integration**: Verwenden Sie den Db2 `db2look`-Befehl, um DDL aus Katalogdaten zu generieren: `db2look -d <dbname> -t <table>`.
- Vermeiden Sie den direkten Zugriff auf Basistabellen, es sei denn, Sie sind ein Sysadmin, da dies zu Inkonsistenzen führen kann.

Für tiefergehende Einblicke, erkunden Sie die offizielle Dokumentation oder experimentieren Sie in einer Testdatenbank.

#### Referenzen
- [Db2 Catalog Overview](https://www.ibm.com/docs/en/db2-for-zos/12?topic=objects-db2-catalog)
- [System Catalog Views in Db2 LUW](https://www.ibm.com/docs/en/db2/11.5?topic=views-system-catalog)
- [Getting Useful Info from DB2 System Catalog](https://developer.ibm.com/articles/dm-0411melnyk/)