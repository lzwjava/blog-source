---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Wichtige Ausfälle der Google Cloud Platform
translated: true
type: note
---

### Größere Ausfälle in der Geschichte der Google Cloud Platform (GCP)

Die Google Cloud Platform hat seit ihren Anfängen mehrere bedeutende Ausfälle erlebt, die oft auf Softwarefehler, Hardwareausfälle, Umweltfaktoren oder Kapazitätsprobleme zurückzuführen sind. Nachfolgend ist eine Tabelle zusammengestellt, die einige der bemerkenswertesten Vorfälle zusammenfasst, ausgewählt aufgrund ihres Umfangs, ihrer Dauer oder ihrer weitreichenden Auswirkungen. Diese stammen aus historischen Aufzeichnungen bis Mitte 2025.

| Datum | Ursache | Auswirkung |
|------|--------|--------|
| 14. Dezember 2020 | Versehentliche Reduzierung der Kapazität des zentralen User-ID-Managementsystems, was die OAuth-basierte Authentifizierung beeinträchtigte. | Globaler Ausfall für ~90 Minuten; unterbrach den Zugang zu Gmail, YouTube, Google Drive, GCP-Diensten und Apps wie Pokémon GO für Millionen von Nutzern weltweit. |
| Juli 2022 | Hitzewelle (über 40°C) in London, die zu Ausfällen der Kühlsysteme in der Zone europe-west2-a führte. | Regionale Störungen für ~24 Stunden; betraf Cloud Storage, BigQuery, Compute Engine, GKE und andere Dienste, was Failover in andere Regionen erzwang. |
| 8. August 2022 | Elektrischer Vorfall, der zu einem Brand im Rechenzentrum Council Bluffs, Iowa, führte (nicht related zu gleichzeitigen Problemen mit Search/Maps). | Lokale Brandbekämpfung; globale Latenz im Cloud Logging-Dienst über Tage, was die Überwachung und Fehlerbehebung für GCP-Nutzer beeinträchtigte. |
| 28. April 2023 | Wassereinbruch und Brand in einem Pariser Rechenzentrum, die Multi-Cluster-Ausfälle in europe-west9-a auslösten. | Weitverbreitete Störungen in Europa, Asien, Amerika; betraf VPC, Load Balancing, BigQuery und Netzwerkdienste über Stunden bis Tage. |
| 7.-8. August 2024 | Fehler bei der Cloud TPU-Dienstaktivierung während der API-Freigabe für Vertex AI. | Globaler Ausfall für ~14 Stunden; blockierte Uploads und Training von Machine-Learning-Modellen in Vertex AI in allen großen Regionen. |
| 23. Oktober 2024 | Stromausfall und Lichtbogen in der Zone europe-west3-c (Frankfurt), der die Kühlinfrastruktur beeinträchtigte. | Eintägiger regionaler Ausfall (~8 Stunden); teilweise Abschaltung der Infrastruktur mit Verkehrsumleitung in andere Zonen. |
| 7.-8. Januar 2025 | Vernetzte Probleme, einschließlich SAML-Authentifizierungsfehlern in Apigee, HTTP-Fehlern in Vertex Gemini APIs und Veröffentlichungsblockaden in Pub/Sub. | Mehrtägige Störungen über 18+ Stunden; betraf API-Management, KI-Inferenz und Echtzeit-Nachrichtenübermittlung regionsübergreifend. |
| 12. Juni 2025 | Bug in einer neuen Service-Control-Funktion (Quota Policy Checks), der zu Aufgabenüberlastungen in großen Regionen wie us-central1 führte. | Globaler Ausfall für ~7 Stunden; legte Spotify, Discord, Fitbit und viele GCP-abhängige Dienste lahm, mit über 1,4 Millionen Meldungen. |

Diese Vorfälle verdeutlichen die Wachstumsschmerzen von GCP, von frühen App Engine-Problemen in den späten 2000er Jahren bis hin zu jüngeren systemischen Ausfällen. Google veröffentlicht typischerweise Post-Mortems und Sanierungspläne, wie z.B. die Modularisierung von Komponenten, um "Fail Open" zu ermöglichen. Für den neuesten Status besuchen Sie [Google Cloud Service Health](https://status.cloud.google.com/).

[A History of Google Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-google-cloud-and-data-center-outages)  
[Google services outages - Wikipedia](https://en.wikipedia.org/wiki/Google_services_outages)  
[Google Cloud Outage History | StatusGator](https://statusgator.com/blog/google-cloud-outage-history/)  
[The 10 Biggest Cloud Outages Of 2025 (So Far) - CRN](https://www.crn.com/news/cloud/2025/the-10-biggest-cloud-outages-of-2025-so-far)  
[Google Cloud Outage Analysis: June 12, 2025 - ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)