---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Apache DataFusion Comet beschleunigt Spark
translated: true
type: note
---

### Apache DataFusion Comet

Apache DataFusion Comet ist ein Open-Source-Projekt unter der Apache Software Foundation, das als hochperformanter Beschleuniger für Apache Spark dient. Es basiert auf der Apache DataFusion-Abfrage-Engine und zielt darauf ab, die Leistung von Spark-Workloads zu steigern – wie schnellere Datenverarbeitung und beschleunigte Erkenntnisgewinnung – während es auf Standard-Hardware läuft. Für die Integration sind keine Code-Änderungen erforderlich und es beschleunigt auch Apache Iceberg-Operationen, die Parquet-Scans von Spark betreffen.

#### Wichtige Funktionen
- **Leistungssteigerung**: Ermöglicht erhebliche Geschwindigkeitsvorteile für Abfragen. Beispielsweise zeigen Benchmarks von 22 TPC-H-Abfragen gegen 100 GB Parquet-Daten eine durchschnittliche Verbesserung um den Faktor 2,2 (von 687 Sekunden auf 302 Sekunden auf einem einzelnen 8-Core-Executor). TPC-DS-Benchmarks sind ebenfalls verfügbar, mit reproduzierbaren Ergebnissen über die Anleitungen des Projekts.
- **Hardware-Effizienz**: Funktioniert mit Standard-Hardware und vermeidet die Notwendigkeit teurer GPUs oder FPGAs.
- **Nahtlose Kompatibilität**: Vollständig kompatibel mit unterstützten Apache Spark-Versionen und gewährleistet eine einfache Integration in bestehende Setups.
- **Enge DataFusion-Integration**: Nutzt die DataFusion-Execution-Engine für optimierte Effizienz.
- **Community-getrieben**: Lizenziert unter der Apache License 2.0, mit einer aktiven Community für Beiträge, einschließlich Fehlerbehebungen, neuer Funktionen und Dokumentation.

Das Projekt wird aktiv gepflegt, mit Ressourcen für den Einstieg, Anleitungen für Mitwirkende und Community-Kanälen wie Slack und Discord.

Weitere Details, einschließlich der Installation (über die Dokumentation auf datafusion.apache.org) und Benchmarks, finden Sie im Repository.

[Apache DataFusion Comet GitHub Repository](https://github.com/apache/datafusion-comet)