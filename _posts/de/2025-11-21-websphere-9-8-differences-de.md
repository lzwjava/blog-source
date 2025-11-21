---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: WebSphere 9.0 vs. 8.0 Wichtige Unterschiede
translated: true
type: note
---

### Hauptunterschiede zwischen IBM WebSphere Application Server (WAS) 9.0 und 8.0

IBM WebSphere Application Server (WAS) ist ein Java EE Application Server für Unternehmen. Version 8.0 (veröffentlicht 2011) führte die Java EE 6-Konformität ein, während Version 9.0 (veröffentlicht 2017) auf Java EE 7 erweitert wurde, mit einem Fokus auf die Modernisierung des Traditional Profile, um es an leichtere, cloud-freundliche Laufzeitumgebungen wie Liberty anzupassen. Im Folgenden werde ich die wichtigsten Unterschiede in einer Tabelle zur besseren Übersicht darlegen, basierend auf der offiziellen IBM-Dokumentation und Release Notes. Diese umfassen Java-Unterstützung, Standardkonformität, Architektur und Bereitstellung.

| Aspekt                  | WAS 8.0                                                                 | WAS 9.0                                                                 |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Java SE Support**    | Standardmäßig Java SE 6; optional Unterstützung für Java SE 7 via Konfiguration. | Standardmäßig Java SE 8 als primäre Plattform, unter Verwendung von IBM SDK Java 8 für volle Kompatibilität mit Oracle Java 8. Dies ermöglicht Lambda-Ausdrücke, Streams und andere SE 8-Features. |
| **Java EE Compliance** | Volle Java EE 6-Unterstützung, inklusive JPA 2.0, JSF 2.0 und Servlet 3.0.    | Volle Java EE 7-Unterstützung, mit neuen Features wie WebSocket 1.0, JSON-P 1.0, Batch 1.0 und erweiterten Concurrency Utilities. Dies bringt die Traditional Edition auf das Niveau der Liberty-Fähigkeiten aus früheren Versionen. |
| **Liberty Profile Integration** | Liberty wurde in 8.5 eingeführt (nicht im 8.0 Core); 8.0 konzentriert sich nur auf das traditionelle Full Profile. | Tief integrierte Liberty-Laufzeitumgebung (Version 16.0.0.2) als leichte, modulare Alternative zum Full Profile, optimiert für Cloud-native Apps. Liberty ist gebündelt und unterstützt Continuous Delivery. |
| **Bereitstellungsmodell**   | Primär On-Premise; Installation via Installation Manager mit Editionen wie Base und Network Deployment (ND) für Clustering. | Erste Version, die gleichzeitig als On-Premise und als-a-Service auf IBM Cloud veröffentlicht wurde. Unterstützt Hybrid-Cloud-Bereitstellungen mit besseren Containerisierungs-Hooks. |
| **Performance & Management** | Bis zu 20-26 % Durchsatzsteigerung gegenüber WAS 7; intelligentes Management in der ND-Edition. | Baut auf 8.0 auf mit weiteren Optimierungen für Ressourceneffizienz; erweiterte Administrationswerkzeuge für Migration und Konfigurationsvergleich. |
| **Ende des Supports**     | Erweiterter Support endete 2019; erhält keine Fixes mehr.              | Aktiver Support mindestens bis 2027, mit regelmäßigen Fix Packs (z.B. 9.0.5.x), die Sicherheit und Kompatibilität adressieren. |
| **Migrationsüberlegungen** | N/A (Baseline).                                                        | Einfacherere Migration von 8.x via Tools wie dem Configuration Comparison Tool; automatische Port-Ausrichtung und Behandlung veralteter APIs für den Java SE 8-Übergang. |

#### Wichtigste Erkenntnisse
- **Größter Sprung**: Der Wechsel zu Java EE 7 und Java SE 8 ist der bedeutendste, da er moderne Java-Features und Standards ermöglicht, die zuvor in Liberty vorgestellt wurden. Wenn Sie Legacy-Java-EE-6-Apps betreiben, ist die Migration zu 9.0 unkompliziert, erfordert jedoch möglicherweise Tests für SE-8-spezifische Änderungen.
- **Wann ein Upgrade sinnvoll ist**: Wählen Sie 9.0 für Cloud-/Hybrid-Anforderungen oder EE-7-Features; bleiben Sie bei 8.0 (oder patchen auf 8.5.5) nur für die kurzfristige Wartung älterer Apps.
- Detaillierte Migrationsleitfäden finden Sie in den offiziellen IBM-Dokumenten.

**Referenzen**:
- [IBM WebSphere Application Server Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Java SE 8 in WAS Traditional V9](https://www.ibm.com/docs/en/was/9.0.5?topic=waso-java-se-8-in-websphere-application-server-traditional-v9)
- [WAS Version Comparison Slides](https://www.slideshare.net/ejlp12/ibm-websphere-application-server-version-to-version-comparison)
- [WAS Configuration Comparison Tool](https://www.ibm.com/support/pages/websphere-application-server-configuration-comparison-tool)