---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erweiterte Kusto-Abfragesprache Beispiele
translated: true
type: note
---

Kusto Query Language (KQL) ist ein leistungsstarkes Werkzeug zum Abfragen großer Datensätze in Azure-Diensten wie Azure Data Explorer und Azure Monitor. Im Folgenden finden Sie mehrere komplexe Beispiele, die mehrere Operatoren, Funktionen und erweiterte Funktionen wie Zeitreihenanalyse, Anomalieerkennung, Pivotierung und benutzerdefinierte Funktionen kombinieren. Diese stammen aus realen Szenarien wie der Analyse von Sturmereignissen oder Verkaufsdaten. Jedes Beispiel enthält die Abfrage und eine kurze Erklärung.

### 1. Anomalieerkennung in Zeitreihendaten
Diese Abfrage aggregiert tägliche Durchschnittswerte aus einer Metriktabelle und verwendet Reihenzerlegung, um Anomalien zu identifizieren. Ideal für die Überwachung ungewöhnlicher Muster in Logs oder Telemetriedaten.

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. Benutzerdefinierte Funktion für parametrisierte Filterung und Zusammenfassung
Hier filtert eine wiederverwendbare Funktion Verkaufsdaten nach Region und Schwellenwert und berechnet dann Summen – nützlich für dynamische Berichte in Azure Data Explorer-Dashboards.

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. Pivotieren aggregierter Daten für Kreuztabellenanalyse
Dies aggregiert Werte nach Kategorie und Region und pivotiert dann Regionen in Spalten für einen einfacheren Vergleich, was häufig in Business Intelligence-Abfragen vorkommt.

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. Korrelationsanalyse zwischen Zeitreihenmetriken
Unter Verwendung von Sturmereignisdaten erstellt dies tägliche Reihen für zwei Metriken und berechnet ihre Korrelation, um Beziehungen aufzudecken, z. B. zwischen Schäden und Todesfällen.

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. Filterung, Top-Auswahl und Dauerberechnung für die Ereignisanalyse
Dies filtert Hochwasserereignisse in Texas, wählt die Top 5 nach Schadenshöhe aus und fügt eine berechnete Spalte für die Dauer hinzu – ideal für die Incident Response in Azure Sentinel.

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. Statische Wertzuordnung mit Let-Anweisung für Datentransformation
Definiert ein Wörterbuch zur Zuordnung von Quelltypen, filtert Ereignisse und projiziert lesbare Namen – hilfreich für die Normalisierung kategorialer Daten in Logs.

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

Diese Beispiele können direkt in der Azure Data Explorer Web UI oder in Log Analytics ausgeführt werden. Weitere Beispiele finden Sie in der offiziellen Beispielgalerie.

[Umfassender Leitfaden zur Kusto Query Language (KQL)](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[Tutorial: Häufige Operatoren der Kusto Query Language erlernen](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)