---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erste Schritte mit der Kusto-Abfragesprache
translated: true
type: note
---

### Erste Schritte mit KQL (Kusto Query Language) in Azure

KQL ist eine leistungsstarke, schreibgeschützte Abfragesprache, die für die Analyse großer Mengen strukturierter, halbstrukturierter und unstrukturierter Daten in Azure-Diensten wie Azure Data Explorer, Azure Monitor (Log Analytics) und Microsoft Sentinel entwickelt wurde. Sie ist intuitiv, basiert auf einer Pipe-Struktur (Verwendung von `|` für den Datenfluss) und für Big-Data-Szenarien wie Protokollanalyse, Telemetrie und Bedrohungserkennung optimiert. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur Verwendung.

#### Voraussetzungen
- Ein aktives Azure-Abonnement mit Zugriff auf einen relevanten Dienst (z. B. Azure Data Explorer-Cluster, Log Analytics-Arbeitsbereich oder Sentinel-Instanz).
- Angemessene Berechtigungen: Mindestens Lesezugriff auf Datenbanken, Tabellen oder Arbeitsbereiche.
- Grundlegende Kenntnisse von Datenkonzepten (wie Tabellen und Filterung) sind hilfreich, aber KQL ist einsteigerfreundlich.
- Optional: Installieren Sie die Azure Data Explorer-App oder verwenden Sie die Web-UI für einen schnellen Start – zunächst ist keine Code-Umgebung erforderlich.

#### Schritt 1: Wählen Sie aus, wo Sie Ihre Abfragen ausführen möchten
KQL wird in mehreren Azure-Diensten ausgeführt. Beginnen Sie mit demjenigen, der zu Ihrer Datenquelle passt:
- **Azure Data Explorer**: Ideal für die Big-Data-Exploration. Rufen Sie die Web-UI unter [dataexplorer.azure.com](https://dataexplorer.azure.com/) auf. Wählen Sie einen Cluster und eine Datenbank aus und öffnen Sie dann den Abfrage-Editor.
- **Azure Monitor / Log Analytics**: Für Protokolle und Metriken. Gehen Sie im Azure-Portal (portal.azure.com) zu **Monitor > Protokolle**, wählen Sie einen Arbeitsbereich aus und verwenden Sie den Abfrage-Editor.
- **Microsoft Sentinel**: Für Sicherheitsanalysen. Navigieren Sie im Azure-Portal zu **Microsoft Sentinel > Protokolle** in Ihrem Arbeitsbereich.
- **Andere Optionen**: Microsoft Fabric (über den KQL-Abfrage-Editor) oder Integration mit Tools wie Power BI zur Visualisierung.

Daten sind in einer Hierarchie organisiert: Datenbanken > Tabellen > Spalten. Abfragen sind schreibgeschützt; verwenden Sie Verwaltungsbefehle (beginnend mit `.`) für Schemaänderungen.

#### Schritt 2: Grundlegende Syntax verstehen
KQL-Abfragen sind reine Textanweisungen, die durch Semikolons (`;`) getrennt sind. Sie verwenden ein Datenflussmodell:
- Beginnen Sie mit einem Tabellennamen (z. B. `StormEvents`).
- Leiten Sie Daten mit einer Pipe (`|`) durch Operatoren für Filterung, Aggregation usw.
- Beenden Sie die Abfrage mit einer Ausgabe wie `count` oder `summarize`.
- Groß-/Kleinschreibung wird bei Namen/Operatoren beachtet; schließen Sie Schlüsselwörter in `['Schlüsselwort']` ein, falls erforderlich.

Eine einfache Abfragestruktur:
```
TableName
| where Condition
| summarize Count = count() by GroupByColumn
```

Verwaltungsbefehle (keine Abfragen) beginnen mit `.` (z. B. `.show tables`, um Tabellen aufzulisten).

#### Schritt 3: Schreiben und Ausführen Ihrer ersten Abfrage
1. Öffnen Sie den Abfrage-Editor in Ihrem gewählten Dienst (z. B. Azure Data Explorer Web-UI).
2. Geben Sie eine einfache Abfrage ein. Beispiel mit Beispieldaten (Tabelle `StormEvents`, in den meisten Umgebungen verfügbar):
   ```
   StormEvents
   | where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
   | where State == "FLORIDA"
   | count
   ```
   - Dies filtert Stürme in Florida für November 2007 und gibt die Anzahl zurück (z. B. 28).
3. Klicken Sie auf **Ausführen**, um die Abfrage zu starten. Ergebnisse werden als Tabelle angezeigt; verwenden Sie die UI, um sie als Diagramme zu visualisieren oder zu exportieren.
4. Iterieren Sie: Fügen Sie Operatoren wie `project` (Spalten auswählen), `summarize` (aggregieren) oder `extend` (berechnete Spalten hinzufügen) hinzu.

Häufige Operatoren für den Anfang:
- `where`: Zeilen filtern (z. B. `| where Level == "Error"`).
- `summarize`: Aggregieren (z. B. `| summarize avg(Duration) by User`).
- `join`: Tabellen kombinieren.
- `search`: Volltextsuche über Tabellen hinweg.

#### Schritt 4: Erweiterte Funktionen und Best Practices erkunden
- **Zeitreihen und Analysen**: Verwenden Sie Funktionen wie `make-series` für Trends oder `detect-anomalies` für Ausreißer.
- **Visualisierung**: Wechseln Sie im Editor zur Raster-/Diagrammansicht. Exportieren Sie nach Power BI für Dashboards.
- **Leistungstipps**: Ordnen Sie Operatoren logisch an (früh filtern), begrenzen Sie Ergebnisse mit `take 100` und testen Sie mit kleinen Datensätzen.
- **Häufige Anwendungsfälle**:
  - **Protokollanalyse**: Fehler in Apps abfragen (`| where Level == "Error" | take 50`).
  - **Sicherheitsuntersuchung**: In Sentinel nach Bedrohungen suchen (`search "suspicious login"`).
  - **Datenexploration**: Metriken zusammenfassen (`| summarize count() by bin(TimeGenerated, 1h)`).

#### Problembehandlung
- Fehler? Überprüfen Sie die Syntax im Editor (er markiert Probleme). Stellen Sie sicher, dass Tabellen-/Spaltennamen exakt übereinstimmen.
- Keine Daten? Stellen Sie sicher, dass Ihr Arbeitsbereich Protokolle erfasst hat, oder verwenden Sie Beispieldatensätze.
- Erfahren Sie mehr über interaktive Tutorials im Azure-Portal oder in der Dokumentation.

Laden Sie zum praktischen Üben Beispieldaten in Azure Data Explorer und experimentieren Sie.

[Referenzen]  
[Übersicht über die Kusto Query Language (KQL)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)  
[Schreiben und Ausführen Ihrer ersten KQL-Abfrage](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster)  
[Häufige KQL-Operatoren](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster&tabs=beginner)