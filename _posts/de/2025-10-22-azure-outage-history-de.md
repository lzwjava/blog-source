---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Größere Azure-Ausfälle in der Geschichte
translated: true
type: note
---

Microsoft Azure, das 2010 gestartet wurde, hat im Laufe der Jahre mehrere bedeutende Ausfälle erlebt, die oft auf Konfigurationsfehler, Hardwareausfälle oder externe Ereignisse wie Wetterphänomene zurückzuführen sind. Nachfolgend finden Sie eine chronologische Zusammenfassung der bemerkenswertesten Ausfälle, mit Fokus auf solche mit weitreichenden Auswirkungen über Regionen oder Dienste hinweg. Diese Liste stützt sich auf offizielle Berichte, historische Analysen und Störungsberichte und hebt Daten, Ursachen, betroffene Bereiche und verfügbare Dauer hervor.

| Datum | Ursache | Betroffene Regionen/Dienste | Dauer/Auswirkung |
|-------|---------|-----------------------------|------------------|
| 29. Februar 2012 | Schaltjahr-Berechnungsfehler im Code | Nordamerika (Azure Compute) | ~8 Stunden; unterbrach Anwendungsverwaltung und -dienste für Benutzer. |
| 26. Juli 2012 | Fehlkonfiguriertes Netzwerkgerät | Westeuropa (Azure Compute) | >2 Stunden; teilweise Nichtverfügbarkeit in Europa. |
| 22. Februar 2013 | Abgelaufenes SSL-Zertifikat | Global (Azure Storage) | Mehrere Stunden; Service-Gutschriften ausgestellt; betraf auch Xbox Live, Music und Video. |
| 30. Oktober 2013 | Teilweiser Compute-Ausfall (Throttling-Problem) | Weltweit (Azure Compute, Verwaltungsfunktionen) | ~3-4 Stunden; betraf Datei-Uploads und Website-Verwaltung. |
| 22. November 2013 | Speicher- und Netzwerkprobleme | North Central US (Xbox Live) | Mehrere Stunden am Xbox One Launch-Tag; geringe Kundenauswirkung, aber hohe Sichtbarkeit. |
| 19. November 2014 | Konfigurationsänderung verursachte Endlosschleife im Blob-Speicher | Global (20+ Dienste, inkl. Azure Storage) | ~6-10 Stunden; reduzierte Kapazität in mehreren Regionen; betraf Xbox Live, MSN und Visual Studio Online. |
| 15. September 2016 | Globaler DNS-Ausfall | Weltweit (Azure DNS) | ~2 Stunden; breite Dienstunterbrechungen. |
| 7. & 23. März 2017 | Mehrere Vorfälle (Netzwerk und Speicher) | Global (Office 365, Skype, Xbox Live) | Bis zu 16+ Stunden pro Vorfall; weitverbreitete Benutzerzugriffsprobleme. |
| 29. September 2017 | Auslösung von Brandschutzgas während Wartung löste Abschaltungen aus | US-Regionen (verschiedene Dienste) | ~7 Stunden; intermittierende Störungen. |
| 4. September 2018 | Blitzeinschlag verursachte Überspannung und Kühlungsausfall | US South Central, mehrere Regionen (40+ Dienste) | >25 Stunden, einige Auswirkungen bis zu 3 Tage; größere Downtime across Dienste. |
| 25. Januar 2020 | Backend-Abhängigkeitsfehler in Azure SQL-Datenbank | Global (fast alle Regionen, inkl. US Gov/DoD) | ~6 Stunden; betraf SQL DB, Application Gateway, Bastion und Firewall. |
| 1. April 2021 | Weitverbreitetes DNS-Problem in der Netzwerkinfrastruktur | Global (USA, Europa, Asien, etc.) | ~1,5 Stunden; betraf kernnetzwerkabhängige Dienste. |
| 1. Juni 2022 | Probleme mit Azure Active Directory-Anmeldeprotokollen | Global (mehrere Regionen) | ~9,5 Stunden; betraf AAD, Sentinel, Monitor und Resource Manager. |
| 29. Juni 2022 | Nicht spezifizierte Backend-Instabilität | Global (Dutzende Regionen) | ~24 Stunden intermittierend; betraf Firewall, Synapse, Backup und mehr. |
| 25. Januar 2023 | Fehlerhafter Routerbefehl verursachte Netzwerkunterbrechung | Global (25+ Regionen, inkl. East US, West Europe) | ~3,5 Stunden; Latenz und Fehler in M365 (Teams, Outlook), SharePoint und Office 365. |
| 9. Juni 2023 | DDoS-Angriff, beansprucht von Anonymous Sudan | Global (Azure-Portal und Cloud-Dienste) | ~2,5 Stunden; Portal und zugehörige Dienste ausgefallen. |
| 13. November 2024 | DNS-Auflösungsfehler für Storage | Mehrere (East US/2, Central US, West US/2, etc.) | ~8,5 Stunden; betraf Databricks und Storage Accounts. |
| 26. Dezember 2024 | Stromvorfall in Availability Zone | South Central US (Zone 03) | ~18 Stunden; betraf Storage, VMs, Cosmos DB, SQL DB und mehr. |
| 9. Januar 2025 | Netzwerkausfall | East US 2 | >48 Stunden; betraf Databricks, Synapse, Functions, App Service und VMs. |
| 10. September 2025 | Allocator-Service-Überlastung durch Throttling-Änderung | East US 2 (Zonen 02/03) | ~10,5 Stunden; beeinträchtigte VM-Operationen, betraf Backup, Batch, Kubernetes und Synapse. |
| 26.-27. September 2025 | Fehlerhafter Zertifikatwert in Konfigurationsänderung | Schweiz, Norden (mehrere Zonen) | ~22 Stunden; weitverbreitete Ausfälle in API Management, App Service, Cosmos DB, VMs und Sentinel. |
| 9. Oktober 2025 | Azure Front Door Control Plane-Defekt | Europa und Afrika | ~8 Stunden; Latenz/Timeouts in Portalen und Diensten (bis zu 17 % Fehlerrate in Afrika). |
| 9. Oktober 2025 | Nachfolgende Konfigurationsentfernung durch Automatisierungsskripte | Global (Verwaltungsportale) | ~4 Stunden; Zugriffsprobleme auf Azure-Portal und andere nach AFD-Vorfall. |

Diese Vorfälle repräsentieren einen Bruchteil der gesamten Ereignisse, aber die disruptivsten basierend auf Umfang und Dauer. Microsoft veröffentlicht typischerweise Post-Incident Reviews (PIRs) zum Lernen, und die Verfügbarkeit hat sich im Laufe der Zeit verbessert, mit SLAs, die 99,99 % Betriebszeit anstreben.

## Referenzen
- [A History of Microsoft Azure Outages](https://www.datacenterknowledge.com/outages/a-history-of-microsoft-azure-outages)
- [Microsoft Azure Outage History Overview](https://statusgator.com/blog/azure-outage-history/)
- [Azure Status History](https://azure.status.microsoft/en-us/status/history/)
- [Microsoft Azure Wikipedia - Outages Section](https://en.wikipedia.org/wiki/Microsoft_Azure#Outages)