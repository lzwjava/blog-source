---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Größte AWS-Ausfälle der Geschichte
translated: true
type: note
---

### Größte Ausfälle in der Geschichte von AWS

Amazon Web Services (AWS) betreibt seit 2006 einen Großteil des Internets, aber wie jede groß angelegte Infrastruktur kam es auch hier gelegentlich zu Unterbrechungen. Ausfälle sind im Verhältnis zum umfangreichen Betrieb selten, doch größere Vorfälle können sich auf abhängige Dienste auswirken, von Social Media bis hin zu Finanzplattformen. Die folgende Tabelle fasst wichtige historische Ausfälle zusammen und konzentriert sich dabei auf weitreichende oder folgenschwere Ereignisse. Diese stammen aus dokumentierten Vorfällen, die mehrere Dienste oder namhafte Kunden betrafen.

| Datum              | Betroffene Dienste/Regionen | Ursache                          | Auswirkung |
|-------------------|---------------------------|--------------------------------|--------|
| 15. Februar 2008 | S3, EC2 (global)         | Nicht näher benannter technischer Fehler | Unterbrach die Bildspeicherung und das Hosting für verschiedene Websites und markierte einen der ersten größeren Vorfälle bei AWS. |
| 21. April 2011    | Mehrere Dienste (US-East-1) | Längerer Rechenzentrumsausfall | Legte prominente Websites wie Reddit und Quora für Stunden lahm und unterstrich frühe Zuverlässigkeitsbedenken. |
| 28. Februar 2017 | EC2, S3, RDS und andere (US-East-1) | Menschliches Versagen: Falsch eingegebener Befehl während des Debuggings | Mehrstündiger Ausfall betraf Slack, Docker, Exora und andere; geschätzte Verluste in hunderten Millionen Dollar; das AWS-Cloud-Dashboard war ebenfalls down. |
| 7. Dezember 2021  | Control-Plane-Dienste, einschließlich EC2, RDS, Lambda (US-East-1) | Softwarefehler in der Control Plane während eines Failovers, der zu kaskadierenden Fehlern führte | Längster Ausfall der jüngeren Geschichte (8+ Stunden); unterbrach Netflix, Disney+, Capital One und Regierungs-Websites; ein zweiter, kleinerer Ausfall am 15. Dezember betraf ähnliche Dienste. |
| 13. Juni 2023     | EC2 und verwandte Dienste (mehrere Regionen) | Nicht näher benannte regionale Probleme | Weitreichende Downtime traf Nachrichtenagenturen (z. B. Associated Press, Boston Globe) und Transitsysteme (NY MTA) und dauerte mehrere Stunden. |
| 20. Oktober 2025  | DynamoDB-Endpunkte, EC2-Starts und mehrere Dienste (US-East-1, mit globalen Auswirkungen) | DNS-Auflösungsfehler für DynamoDB-Dienstendpunkte | Tägliche Unterbrechung (beginnend spät am 19. Oktober PDT, gelöst bis zum Nachmittag des 20. Oktober); betraf Snapchat, Reddit, Roblox, Fortnite, Banken (z. B. Lloyds) und HMRC; betraf Millionen von Nutzern, indem der Zugang zu ~1/3 der internetabhängigen Apps blockiert wurde; AWS drosselte einige Operationen zur Wiederherstellung. |

Diese Vorfälle sind oft auf menschliches Versagen, Netzwerkprobleme oder Umweltfaktoren zurückzuführen, und AWS hat die Widerstandsfähigkeit durch Redundanzen wie Multi-Region-Setups verbessert. Der Ausfall von 2025 unterstreicht die fortbestehenden Risiken der Überabhängigkeit von US-East-1, der geschäftigsten AWS-Region.

Weitere Details:
- [A History of AWS Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)
- [The Biggest AWS Outage in History: December 7, 2021](https://aws.plainenglish.io/the-biggest-aws-outage-in-history-the-december-7-2021-us-east-1-meltdown-and-lessons-learned-2efab5a02de5)
- [What caused the AWS outage](https://www.bbc.com/news/articles/cev1en9077ro)
- [AWS Update on October 2025 Outage](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)