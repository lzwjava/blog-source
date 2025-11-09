---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS 關聯式數據庫服務概覽
translated: true
type: note
---

### AWS 上的關聯式資料庫

AWS 提供多種用於關聯式資料庫的託管服務，其中 **Amazon Relational Database Service (RDS)** 是主要服務。它負責處理各種熱門資料庫引擎的設定、修補、備份和擴展。此外，**Amazon Aurora** 是一款高效能、相容於 MySQL 和 PostgreSQL 的關聯式資料庫，內建於 RDS 中。

以下是 AWS 上主要關聯式資料庫選項的摘要：

| 服務/引擎 | 描述 | 使用案例 |
|---------------|-------------|-----------|
| **Amazon RDS for PostgreSQL** | 全託管 PostgreSQL，支援 JSONB 和全文檢索等進階功能。 | 交易型應用程式、網路應用程式和分析。 |
| **Amazon RDS for MySQL** | 託管 MySQL，具高可用性和讀取複本。 | 電子商務、內容管理和通用應用程式。 |
| **Amazon RDS for MariaDB** | MySQL 的分支，具增強效能和儲存引擎。 | 網路應用程式和讀取密集型工作負載。 |
| **Amazon RDS for SQL Server** | Microsoft SQL Server，提供 Standard、Enterprise 和 Web 等版本。 | 企業應用程式、商業智慧和 Windows 系統。 |
| **Amazon RDS for Oracle** | Oracle Database，提供自帶授權 (BYOL) 或含授權選項。 | 關鍵任務企業應用程式。 |
| **Amazon RDS for Db2** | IBM Db2，支援 LUW (Linux、UNIX、Windows)。 | 大規模交易和分析工作負載。 |
| **Amazon Aurora (MySQL 相容)** | 雲原生關聯式資料庫，效能比標準 MySQL 快達 5 倍。 | 高吞吐量 OLTP 和全球應用程式。 |
| **Amazon Aurora (PostgreSQL 相容)** | 相容於 PostgreSQL，提供無伺服器選項和自動擴展儲存。 | 需要 ACID 相容性和高可用性的可擴展應用程式。 |

針對資料倉儲（以 OLAP 為主的關聯式工作負載），AWS 還提供 **Amazon Redshift**，這是一個基於 PostgreSQL 的全託管、PB 級資料倉儲。

這些服務與其他 AWS 工具（如 EC2、Lambda 和 S3）無縫整合。若要開始使用，請查閱 [AWS RDS 文件](https://aws.amazon.com/rds/) 或 [AWS 資料庫服務概覽](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/)。