---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu des services de base de données relationnelle AWS
translated: true
type: note
---

### Bases de données relationnelles sur AWS

AWS propose plusieurs services managés pour les bases de données relationnelles, **Amazon Relational Database Service (RDS)** étant l'offre principale. Il gère la configuration, les correctifs, les sauvegardes et la mise à l'échelle pour différents moteurs de base de données populaires. De plus, **Amazon Aurora** est une base de données relationnelle haute performance, compatible MySQL et PostgreSQL, intégrée à RDS.

Voici un résumé des principales options de bases de données relationnelles sur AWS :

| Service/Moteur | Description | Cas d'utilisation |
|---------------|-------------|-----------|
| **Amazon RDS for PostgreSQL** | PostgreSQL entièrement managé, prenant en charge des fonctionnalités avancées comme JSONB et la recherche en texte intégral. | Applications transactionnelles, applications web et analytique. |
| **Amazon RDS for MySQL** | MySQL managé avec haute disponibilité et réplicas de lecture. | Commerce électronique, gestion de contenu et applications à usage général. |
| **Amazon RDS for MariaDB** | Fork de MySQL avec des performances améliorées et des moteurs de stockage. | Applications web et charges de travail intensives en lecture. |
| **Amazon RDS for SQL Server** | Microsoft SQL Server avec des éditions comme Standard, Enterprise et Web. | Applications d'entreprise, BI et systèmes basés sur Windows. |
| **Amazon RDS for Oracle** | Oracle Database avec des options BYOL (Bring Your Own License) ou licence incluse. | Applications d'entreprise critiques. |
| **Amazon RDS for Db2** | IBM Db2 avec prise en charge de LUW (Linux, UNIX, Windows). | Charges de travail transactionnelles et analytiques à grande échelle. |
| **Amazon Aurora (compatible MySQL)** | Base de données relationnelle cloud-native avec des performances jusqu'à 5 fois supérieures à MySQL standard. | OLTP à haut débit et applications globales. |
| **Amazon Aurora (compatible PostgreSQL)** | Compatible PostgreSQL avec des options serverless et un stockage à mise à l'échelle automatique. | Applications scalables nécessitant la conformité ACID et une haute disponibilité. |

Pour l'entrepôt de données (charges de travail relationnelles orientées OLAP), AWS propose également **Amazon Redshift**, un entrepôt de données entièrement managé et à l'échelle du pétaoctet, basé sur PostgreSQL.

Ces services s'intègrent parfaitement avec d'autres outils AWS comme EC2, Lambda et S3. Pour commencer, consultez la [documentation AWS RDS](https://aws.amazon.com/rds/) ou la [vue d'ensemble des services de base de données AWS](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/).