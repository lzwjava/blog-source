---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: AWS-Ausfallanalyse Oktober 2025
translated: true
type: note
---

### AWS-Ausfall am 20. Oktober 2025: Detaillierte Fallanalyse

Der AWS-Ausfall am 20. Oktober 2025 war eine schwerwiegende Störung, die in der Region US East (N. Virginia) (us-east-1) – dem größten und kritischsten Rechenzentrum von AWS – ihren Ursprung hatte. Er begann spät am 19. Oktober PDT und dauerte etwa 16 Stunden an. Über 140 Services waren betroffen, und die Auswirkungen breiteten sich aufgrund von Abhängigkeiten von dieser Region global aus. Der Vorfall verdeutlichte Schwachstellen in der DNS-Auflösung, Service-Abhängigkeiten und Wiederherstellungsprozessen und betraf Millionen von Nutzern von Apps, Websites und Services. Im Folgenden finden Sie eine Aufschlüsselung basierend auf dem offiziellen Post-Mortem von AWS und zeitgenössischen Berichten.

#### Zeitlicher Ablauf
Der Ausfall verlief in Phasen, beginnend mit der Erkennung und eskalierend zu kaskadierenden Fehlern, bevor eine gestaffelte Wiederherstellung erfolgte. Wichtige Meilensteine (alle Zeiten in PDT):

| Uhrzeit | Ereignis |
|------|-------|
| 23:49 (19. Okt.) | Erhöhte Fehlerraten und Latenzen bei mehreren AWS-Services in us-east-1 erkannt. |
| 00:11 (20. Okt.) | AWS meldet öffentlich erhöhte Fehlerraten; erste Nutzerberichte auf Monitoring-Seiten wie DownDetector schnellen in die Höhe. |
| 00:26 | Problem als DNS-Auflösungsfehler für DynamoDB-API-Endpunkte in us-east-1 identifiziert. |
| 01:26 | Bestätigte hohe Fehlerraten speziell für DynamoDB-APIs, einschließlich Global Tables. |
| 02:22 | Erste Gegenmaßnahmen angewendet; erste Anzeichen einer Wiederherstellung. |
| 02:24 | DynamoDB-DNS-Problem behoben, was eine teilweise Service-Wiederherstellung auslöst – jedoch treten Beeinträchtigungen beim EC2-Start und Fehler bei Health Checks des Network Load Balancer (NLB) auf. |
| 03:35 | DNS vollständig behoben; die meisten DynamoDB-Operationen sind erfolgreich, aber EC2-Starts bleiben über Availability Zones (AZs) hinweg beeinträchtigt. |
| 04:08 | Laufende Arbeiten an EC2-Fehlern und Lambda-Polling-Verzögerungen für SQS Event Source Mappings. |
| 05:48 | Teilweise Wiederherstellung des EC2-Starts in bestimmten AZs; SQS-Backlogs beginnen sich zu leeren. |
| 06:42 | Gegenmaßnahmen in allen AZs eingeführt; AWS führt Rate Limiting für neue EC2-Instancestarts ein, um die Stabilität zu gewährleisten. |
| 07:14 | API-Fehler und Konnektivitätsproblete bestehen bei verschiedenen Services fort; auswirkungen auf Nutzer erreichen ihren Höhepunkt (z.B. App-Ausfälle). |
| 08:04 | Untersuchung konzentriert sich auf das interne EC2-Netzwerk. |
| 08:43 | Grundursache für Netzwerkprobleme identifiziert: Beeinträchtigung im internen EC2-Subsystem für NLB-Health-Monitoring. |
| 09:13 | Zusätzliche Gegenmaßnahmen für NLB-Health-Checks. |
| 09:38 | NLB-Health-Checks vollständig wiederhergestellt. |
| 10:03 – 12:15 | Fortschreitende Verbesserungen beim EC2-Start; Lambda-Aufrufe und Konnektivität stabilisieren sich phasenweise in allen AZs. |
| 13:03 – 14:48 | Drosselungen reduziert; Backlogs für Services wie Redshift, Amazon Connect und CloudTrail werden abgearbeitet. |
| 15:01 | Vollständige operative Normalität für alle Services wiederhergestellt; geringe Backlogs (z.B. AWS Config, Redshift) werden voraussichtlich innerhalb von Stunden abgearbeitet. |
| 15:53 | AWS erklärt den Ausfall für behoben. |

Nutzerberichte auf Plattformen wie DownDetector erreichten ihren Höhepunkt gegen 6 Uhr morgens PDT mit über 5.000 Vorfällen, bevor sie zurückgingen.

#### Grundursache
Der Ausfall ging auf einen DNS-Auflösungsfehler zurück, der die DynamoDB-Service-Endpunkte in us-east-1 betraf. DynamoDB, ein NoSQL-Datenbank-Service, fungiert als kritische "Control Plane" für viele AWS-Funktionen – verwaltet Metadaten, Sitzungen und Routing. Als die DNS-Auflösung für diese Endpunkte fehlschlug, traten bei den DynamoDB-APIs erhöhte Latenzen und Fehler auf.

Dieses anfängliche Problem wurde schnell behoben, löste jedoch eine Kaskade aus:
- EC2-Instancestarts schlugen fehl aufgrund ihrer Abhängigkeit von DynamoDB für die Metadatenspeicherung.
- Ein zugrunde liegender Fehler im internen EC2-Subsystem (verantwortlich für die Überwachung der NLB-Integrität) verschärfte die Netzwerkkonnektivitätsprobleme und führte zu umfassenderen Beeinträchtigungen im Load Balancing und bei API-Aufrufen.
- Die Wiederherstellungsbemühungen umfassten Throttling (z.B. Begrenzung von EC2-Starts und Lambda-Aufrufen), um eine Überlastung zu verhindern, aber Wiederholungsversuche abhängiger Services verstärkten die Belastung.

AWS bestätigte, dass es sich nicht um einen Cyberangriff, sondern um einen infrastrukturbedingten Fehler handelte, möglicherweise verbunden mit einer fehlerhaften DNS-Datenbankaktualisierung oder einem Backup-Systemausfall. Die globale Ausbreitung erfolgte, weil us-east-1 wichtige Control Planes für Services wie IAM und Lambda hostet, selbst für Ressourcen in anderen Regionen.

#### Betroffene Services
Über 142 AWS-Services waren betroffen, primär solche, die von DynamoDB, EC2 oder us-east-1-Endpunkten abhängen. Kernkategorien:

- **Datenbanken & Storage**: DynamoDB (primär), RDS, Redshift, SQS (Backlogs).
- **Compute & Orchestrierung**: EC2 (Starts), Lambda (Aufrufe, Polling), ECS, EKS, Glue.
- **Netzwerk & Load Balancing**: Network Load Balancer (Health Checks), API Gateway.
- **Monitoring & Management**: CloudWatch, CloudTrail, EventBridge, IAM (Updates), AWS Config.
- **Andere**: Amazon Connect, Athena und globale Funktionen wie DynamoDB Global Tables.

Nicht alle Services waren vollständig ausgefallen – viele verzeichneten teilweise Fehler oder Verzögerungen – aber die vernetzte Natur bedeutete, dass selbst kleinere Probleme sich fortpflanzten.

#### Auswirkungen
Der Ausfall unterbrach etwa 1/3 der internetabhängigen Anwendungen und betraf schätzungsweise über 100 Millionen Nutzer weltweit. Bekannte Beispiele:
- **Soziale Medien & Medien**: Snapchat (Login-Fehler), Reddit (Ausfälle), Twitch (Streaming-Probleme).
- **Gaming**: Roblox (Server-Abstürze), Fortnite (Matchmaking-Fehler).
- **Finanzen & Zahlungen**: Venmo, Banken wie Lloyds (Transaktionsverzögerungen), HMRC (britische Steuerdienste).
- **Einzelhandel & E-Commerce**: Teile von Amazons eigenem Retail-Site; Check-Ins von Fluglinien (z.B. Delta, United Verzögerungen).
- **Andere**: Alexa-Geräte (Sprachfehler), Twilio (Kommunikationsstörungen).

Wirtschaftliche Schätzungen beziffern die Verluste auf über 500 Millionen US-Dollar, mit einem Anstieg von Cybersecurity-Scans um 300 %, als Nutzer in Panik gerieten. Es unterstrich die Zentralisierung des Internets: us-east-1 verarbeitet etwa 30 % des AWS-Datenverkehrs, was es trotz Multi-AZ-Designs zu einem einzelnen Schwachpunkt macht.

#### Lösung und Erkenntnisse
AWS löste das Problem durch gezielte Gegenmaßnahmen: DNS-Korrekturen, Subsystem-Patches für EC2/NLB und schrittweise Reduzierung der Drosselungen. Nach dem Vorfall rieten sie:
- Fehlgeschlagene Anfragen erneut zu versuchen.
- DNS-Caches zu leeren.
- Ressourcen über mehrere AZs/Regionen zu verteilen (z.B. via Auto Scaling Groups).
- Service-Quotas und Caching zu nutzen, um sich gegen Wiederholungsversuche abzupuffern.

Umfassendere Erkenntnisse beinhalten die Notwendigkeit einer besseren Redundanz in Control Planes, KI-gestützte Anomalieerkennung für eine schnellere Triagierung und diversifizierte Cloud-Strategien. AWS verpflichtete sich zu einer vollständigen Root Cause Analysis (RCA) für Kunden und betonte, dass solche Ereignisse, wenn auch selten, Skalierungsherausforderungen im Hyperscale-Bereich aufzeigen.

Dies war der disruptivste us-east-1-Ausfall von AWS seit 2021, aber die Wiederherstellung war aufgrund automatisierter Tools schneller als bei historischen Präzedenzfällen.

#### Referenzen
- [AWS Health Dashboard: Service Health - Oct 20, 2025](https://health.aws.amazon.com/health/status?eventID=arn:aws:health:us-east-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_BA540_514A652BE1A)
- [AWS Outage Analysis: October 20, 2025](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [Amazon's massive AWS outage points to a key weakness in the modern internet](https://finance.yahoo.com/news/amazons-massive-aws-outage-points-to-a-key-weakness-in-the-modern-internet-145418180.html)
- [What caused Amazon's AWS outage, and why did so many major apps go offline?](https://www.aljazeera.com/news/2025/10/21/what-caused-amazons-aws-outage-and-why-did-so-many-major-apps-go-offline)
- [AWS Outage on October 20: How a DNS Glitch in DynamoDB Disrupted the Internet](https://medium.com/@ansababy/aws-outage-on-october-20-how-a-dns-glitch-in-dynamodb-disrupted-the-internet-40e1f0440a12)
- [Update - AWS services operating normally](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)
- [AWS was down — live updates following massive outage](https://www.tomsguide.com/news/live/amazon-outage-october-2025)