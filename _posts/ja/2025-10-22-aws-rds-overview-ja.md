---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AWS リレーショナルデータベースサービス概要
translated: true
type: note
---

### AWS のリレーショナルデータベース

AWS はリレーショナルデータベース向けに複数のマネージドサービスを提供しており、主要なサービスとして **Amazon Relational Database Service (RDS)** があります。RDS は、さまざまな人気データベースエンジンのセットアップ、パッチ適用、バックアップ、スケーリングを管理します。さらに、**Amazon Aurora** は、RDS に組み込まれた MySQL および PostgreSQL 互換の高性能なリレーショナルデータベースです。

以下は、AWS の主要なリレーショナルデータベースオプションの概要です：

| サービス/エンジン | 説明 | 主な用途 |
|---------------|-------------|-----------|
| **Amazon RDS for PostgreSQL** | JSONB や全文検索などの高度な機能をサポートする、フルマネージドな PostgreSQL。 | トランザクションアプリケーション、Web アプリ、分析。 |
| **Amazon RDS for MySQL** | 高可用性と読み取りレプリカを備えたマネージド MySQL。 | E コマース、コンテンツ管理、汎用アプリケーション。 |
| **Amazon RDS for MariaDB** | パフォーマンスとストレージエンジンが強化された MySQL のフォーク。 | Web アプリケーション、読み取り負荷の高いワークロード。 |
| **Amazon RDS for SQL Server** | Standard、Enterprise、Web などのエディションを持つ Microsoft SQL Server。 | エンタープライズアプリ、BI、Windows ベースのシステム。 |
| **Amazon RDS for Oracle** | BYOL (Bring Your Own License) またはライセンス込みオプションを提供する Oracle Database。 | ミッションクリティカルなエンタープライズアプリケーション。 |
| **Amazon RDS for Db2** | LUW (Linux, UNIX, Windows) をサポートする IBM Db2。 | 大規模なトランザクションおよび分析ワークロード。 |
| **Amazon Aurora (MySQL 互換)** | 標準 MySQL と比較して最大 5 倍高速なパフォーマンスを発揮するクラウドネイティブなリレーショナル DB。 | 高スループットな OLTP およびグローバルアプリケーション。 |
| **Amazon Aurora (PostgreSQL 互換)** | サーバーレスオプションと自動スケーリングストレージを備えた PostgreSQL 互換データベース。 | ACID 準拠と高可用性を必要とするスケーラブルなアプリケーション。 |

データウェアハウジング (OLAP に焦点を当てたリレーショナルワークロード) 向けには、AWS は PostgreSQL ベースのフルマネージドでペタバイト規模のデータウェアハウスである **Amazon Redshift** も提供しています。

これらのサービスは、EC2、Lambda、S3 などの他の AWS ツールとシームレスに統合されます。利用を開始するには、[AWS RDS ドキュメント](https://aws.amazon.com/rds/) または [AWS データベースサービス概要](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/) を参照してください。