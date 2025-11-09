---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Großer Azure-Ausfall in der Schweiz Nord
translated: true
type: note
---

### Azure-Ausfall in der Schweiz, Norden: 26.-27. September 2025

Bei diesem Vorfall handelte es sich um eine schwerwiegende, plattformweite Störung in der Region „Schweiz, Norden“, die mehrere Verfügbarkeitszonen betraf. Sie dauerte etwa 22 Stunden, begann um 23:54 UTC am 26. September und war um 21:59 UTC am 27. September vollständig behoben. Während die meisten Dienste gegen 04:00 UTC am 27. September wiederhergestellt waren, erforderten einige verbleibende Probleme später am Tag manuelle Eingriffe.

#### Grundursache
Der Ausfall resultierte aus einer geplanten Konfigurationsänderung an Zertifikaten, die für die Autorisierung der Kommunikation in der Software-Load-Balancer-Infrastruktur verwendet werden. Eines der neuen Zertifikate wies einen **fehlerhaften Wert** auf, der während der Validierung nicht erkannt wurde. Diese Änderung wurde über einen beschleunigten Bereitstellungspfad durchgeführt, der sie unerwartet über mehrere Zonen hinweg ausrollte, ohne die Gesundheitsprüfungen auszulösen. Infolgedessen:
- Load Balancer verloren die Konnektivität zu Speicherressourcen und Knoten.
- Betroffene VMs erkannten langandauernde Datenträgertrennungen und fuhren automatisch herunter, um Datenbeschädigung zu vermeiden.
- Dies wirkte sich kaskadenartig auf abhängige Dienste aus und verstärkte die Auswirkungen.

#### Betroffene Dienste
Die Störung betraf eine breite Palette von Azure-Diensten, die in „Schweiz, Norden“ gehostet werden, darunter:
- **Kerninfrastruktur**: Azure Storage, Azure Virtual Machines (VMs), Azure Virtual Machine Scale Sets (VMSS)
- **Datenbanken**: Azure Cosmos DB, Azure SQL-Datenbank, Azure SQL Managed Instance, Azure Database for PostgreSQL
- **Compute und Apps**: Azure App Service, Azure API Management, Azure Kubernetes Service (AKS), Azure Databricks
- **Netzwerke und Sicherheit**: Azure Application Gateway, Azure Firewall, Azure Cache for Redis
- **Analyse und Überwachung**: Azure Synapse Analytics, Azure Data Factory, Azure Stream Analytics, Azure Data Explorer, Azure Log Analytics, Microsoft Sentinel
- **Andere**: Azure Backup, Azure Batch, Azure Site Recovery, Azure Application Insights

Dienste, die auf diesen aufbauen (z. B. benutzerdefinierte Anwendungen), waren ebenfalls betroffen, was zu weitverbreiteter Nichtverfügbarkeit oder beeinträchtigter Leistung führte.

#### Zeitablauf und Maßnahmen
- **23:54 UTC, 26. Sep.**: Die Auswirkungen beginnen nach dem Deployment der Konfigurationsänderung.
- **00:08 UTC, 27. Sep.**: Automatisierte Überwachung erkennt das Problem.
- **00:12 UTC, 27. Sep.**: Untersuchung beginnt durch die Azure Storage- und Networking-Teams.
- **02:33 UTC, 27. Sep.**: Die Konfigurationsänderung wird zurückgesetzt.
- **03:40 UTC, 27. Sep.**: Zurücksetzen der Zertifikate abgeschlossen.
- **04:00 UTC, 27. Sep.**: Die Mehrheit der Dienste erholt sich automatisch; verbleibende Probleme werden identifiziert (z. B. bestimmte VMs in angehaltenen/fehlerhaften Zuständen aufgrund von Race Conditions oder fehlinterpretierten Herunterfahr-Signalen).
- **06:19–14:15 UTC, 27. Sep.**: Entwicklung und Validierung von Wiederherstellungsskripts; gezielte Neustarts für betroffene Ressourcen wie SQL Managed Instance-VMs, Trusted Launch-VMs und Service Fabric-Cluster.
- **16:15 UTC, 27. Sep.**: Teilweise Wiederherstellung für verbleibende Probleme.
- **21:59 UTC, 27. Sep.**: Vollständige Wiederherstellung nach endgültigen Validierungen bestätigt.

Die meisten Ressourcen erholten sich automatisch nach der Wiederherstellung der Konnektivität, aber Teilbereiche (z. B. VMs mit benutzerdefinierten Erweiterungen) benötigten manuelle Neustarts, um Probleme in der Startsequenz zu beheben.

#### Erkenntnisse und Verbesserungen
Microsofts vorläufige Störungsanalyse hebt proaktive Korrekturen hervor:
- Hinzufügung von Audit-Funktionen in Bereitstellungssystemen und Entfernung riskanter beschleunigter Pipelines (abgeschlossen).
- Verbesserte Sicherheitsmaßnahmen mit automatischen Rollbacks (abgeschlossen).
- Geplant: Bessere Überwachung der Ressourcengesundheit (bis Nov. 2025) und robustere Wiederherstellungsprozesse zur Minimierung manueller Arbeit.

Dieser Vorfall unterstreicht die Risiken von Konfigurationsänderungen in gemeinsamer Infrastruktur, doch die Reaktion von Azure begrenzte Datenverluste und ermöglichte eine schnelle, breite Wiederherstellung.

[Azure Statusverlauf](https://azure.status.microsoft/en-us/status/history/)