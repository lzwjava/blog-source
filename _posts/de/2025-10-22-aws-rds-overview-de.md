---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht der AWS-Relationalen Datenbankdienste
translated: true
type: note
---

### Relationale Datenbanken auf AWS

AWS bietet mehrere verwaltete Dienste für relationale Datenbanken, wobei **Amazon Relational Database Service (RDS)** das primäre Angebot ist. Er übernimmt Einrichtung, Patches, Backups und Skalierung für verschiedene beliebte Datenbank-Engines. Zusätzlich ist **Amazon Aurora** eine hochleistungsfähige, mit MySQL und PostgreSQL kompatible relationale Datenbank, die in RDS integriert ist.

Hier ist eine Zusammenfassung der wichtigsten Optionen für relationale Datenbanken auf AWS:

| Dienst/Engine | Beschreibung | Anwendungsfälle |
|---------------|-------------|-----------|
| **Amazon RDS for PostgreSQL** | Vollständig verwaltetes PostgreSQL mit Unterstützung für erweiterte Funktionen wie JSONB und Volltextsuche. | Transaktionale Anwendungen, Web-Apps und Analysen. |
| **Amazon RDS for MySQL** | Verwaltetes MySQL mit hoher Verfügbarkeit und Read Replicas. | E-Commerce, Content-Management und Allzweck-Apps. |
| **Amazon RDS for MariaDB** | Fork von MySQL mit verbesserter Leistung und Storage Engines. | Webanwendungen und leseintensive Workloads. |
| **Amazon RDS for SQL Server** | Microsoft SQL Server mit Editionen wie Standard, Enterprise und Web. | Enterprise-Apps, BI und Windows-basierte Systeme. |
| **Amazon RDS for Oracle** | Oracle Database mit BYOL (Bring Your Own License) oder lizenzinkludierten Optionen. | Mission-Critical Enterprise-Anwendungen. |
| **Amazon RDS for Db2** | IBM Db2 mit Unterstützung für LUW (Linux, UNIX, Windows). | Groß angelegte transaktionale und analytische Workloads. |
| **Amazon Aurora (MySQL-kompatibel)** | Cloud-native relationale DB mit bis zu 5-fach schnellerer Leistung als Standard-MySQL. | Hochdurchsatz-OLTP und globale Apps. |
| **Amazon Aurora (PostgreSQL-kompatibel)** | PostgreSQL-kompatibel mit serverlosen Optionen und automatisch skaliierendem Speicher. | Skalierbare Apps, die ACID-Compliance und hohe Verfügbarkeit erfordern. |

Für Data Warehousing (auf OLAP fokussierte relationale Workloads) bietet AWS auch **Amazon Redshift**, ein vollständig verwaltetes, petabytegroßes Data Warehouse, das auf PostgreSQL basiert.

Diese Dienste integrieren sich nahtlos mit anderen AWS-Tools wie EC2, Lambda und S3. Um zu beginnen, lesen Sie die [AWS RDS-Dokumentation](https://aws.amazon.com/rds/) oder die [Übersicht über AWS Database Services](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/).