---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Alibaba ersetzt IBM Oracle EMC
translated: true
type: note
---

### Alibabas „Remove IOE“-Initiative

Alibabas „Remove IOE“-Kampagne (oder „去IOE“), die um 2008-2009 gestartet wurde, war eine strategische Bemühung, die Abhängigkeit von proprietären Anbieterstacks von **IBM**, **Oracle** und **EMC** (das IOE-Akronym) zu beseitigen. Das Ziel war es, Kosten zu senken, die Skalierbarkeit zu verbessern und Innovation zu fördern, indem auf Open-Source- und hausintern entwickelte Technologien umgestellt wurde. Dies war entscheidend für das E-Commerce-Wachstum von Alibaba, da IOE-Systeme teuer und für massive Skalierung weniger flexibel waren.

#### Was entfernt wurde: Der IOE-Stack
„IOE“ bezog sich auf einen eng integrierten, hochwertigen Enterprise-Stack, der von diesen Anbietern dominiert wurde. Hier ist eine Aufschlüsselung der wichtigsten Komponenten, die Alibaba ausgemustert hat:

1.  **IBM (Hardware und Middleware)**:
    *   **Hauptkomponenten entfernt**:
        *   IBM-Mainframes (z.B. zSeries oder System z) und High-End-Server wie Power Systems.
        *   IBMs AIX-Betriebssystem (proprietäre Unix-Variante).
        *   IBM WebSphere (Application Server/Middleware für Java-Apps).
        *   IBM DB2-Datenbank in einigen Fällen (obwohl Oracle das primäre Ziel für Datenbanken war).
    *   **Warum entfernt?** IBM-Hardware war zuverlässig, aber kostspielig, mit starker Vendor-Lock-in und nicht optimiert für cloud-scale horizontale Skalierung. Alibaba ersetzte sie durch günstigere Commodity-x86-Hardware (z.B. Intel/AMD-Server mit Linux).

2.  **Oracle (Datenbank)**:
    *   **Hauptkomponenten entfernt**:
        *   Oracle Database (Enterprise-Relationaldatenbank, z.B. Oracle 10g/11g RAC für Hochverfügbarkeit).
        *   Oracle-Middleware wie Oracle Fusion Middleware oder WebLogic Server.
    *   **Warum entfernt?** Die Lizenzgebühren waren exorbitant (skalierten mit CPU-Kernen und Benutzern), und sie war nicht ideal für Alibabas massive Lese-/Schreib-Last (z.B. Taobao's Transaktionsspitzen). Der proprietäre Charakter von Oracle limitierte die Anpassbarkeit.

3.  **EMC (Storage)**:
    *   **Hauptkomponenten entfernt**:
        *   EMC Symmetrix oder Clariion Storage Arrays (SAN/NAS Enterprise-Storage-Systeme).
    *   **Warum entfernt?** Teurer proprietärer Storage mit Vendor-Lock-in; schwer linear zu skalieren für Petabyte-Daten im E-Commerce.

Der gesamte IOE-Stack war ein „geschlossenes“ Ökosystem: IBM-Server mit AIX, Oracle DB darauf, gespeichert auf EMC-Arrays, mit IBM-Middleware, die alles zusammenhielt. Dies war in traditionellen Unternehmen üblich, aber ein Engpass für Alibabas Bedürfnisse.

#### Was den IOE-Stack ersetzte
Alibaba baute alles auf Open-Source-Grundlagen, Commodity-Hardware und eigenen Entwicklungen neu auf. Wichtige Ersetzungen:

*   **Hardware/OS-Layer (Ersatz für IBM)**:
    *   Commodity-x86-Server (z.B. von Dell, HP oder maßgefertigt).
    *   Linux-Distributionen (zunächst CentOS/RHEL; später Alibaba Clouds eigenes ALINUX).
    *   Hausinterne Orchestrierungstools für Cluster-Management.

*   **Datenbank-Layer (Ersatz für Oracle)**:
    *   **Open-Source-Start**: MySQL (Alibaba steuerte wesentlich bei; es ist jetzt ein Fork von MySQL 5.5/5.6 mit AliSQL-Patches für hohe Parallelität).
    *   **Eigenentwicklungen**:
        *   **OceanBase**: Alibabas verteilte relationale Datenbank (NewSQL), entwickelt für Finanz-Level-Zuverlässigkeit (unterstützt ACID-Transaktionen bei massiver Skalierung). Sie ist jetzt Open-Source und wird in der Ant Groups Alipay verwendet.
        *   Tair/DRDS: In-Memory-Caching (wie Redis) und verteiltes SQL-Sharding für horizontale Skalierung.
    *   Dies ermöglichte die Abwicklung von Milliarden von Abfragen täglich ohne Oracles Lizenzkosten.

*   **Storage-Layer (Ersatz für EMC)**:
    *   Ceph- oder HDFS-basierter Distributed Storage.
    *   Alibabas PolarFS oder maßgeschneiderter Block-/Object-Storage auf Commodity-Festplatten.
    *   Später entwickelt zu Alibaba Cloud OSS (Object Storage Service) und EBS (Elastic Block Store).

*   **Middleware/Application-Layer**:
    *   HSF (High-Speed Service Framework) für Microservices (Ersatz für WebSphere).
    *   Apache Dubbo für RPC/Service Discovery.
    *   Hausinterne Tools wie SOFA (Scalable Open Framework Architecture).

#### Auswirkungen und Vermächtnis
*   **Kosteneinsparungen**: Reduzierte Hardware-/Datenbankkosten anfänglich um 70-80 %.
*   **Skalierbarkeit**: Ermöglichte Alibaba, die Spitzenlasten am Double 11 (Singles' Day) zu bewältigen (z.B. 500.000+ Bestellungen/Sekunde).
*   **Innovation**: Löste Alibabas Cloud-Geschäft aus (Alibaba Cloud, jetzt nach einigen Metriken die weltweit größte) und Open-Source-Beiträge (z.B. wird OceanBase von Banken weltweit genutzt).
*   **Zeitplan**: Vollständiger Übergang um ca. 2012-2015; „Remove IOE“ wurde ein Mantra für chinesische Tech-Firmen.

Wenn Sie nach Details fragen (z.B. Migrationsherausforderungen oder aktueller Alibaba-Stack), lassen Sie es mich wissen für mehr Informationen! Quellen: Alibabas offizielle Blogs, Jack Mas Reden und Technikberichte aus dieser Ära.