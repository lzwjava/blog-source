---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azureの主要な障害の歴史
translated: true
type: note
---

Microsoft Azureは2010年にローンチされて以来、設定エラー、ハードウェア障害、気象などの外部要因により、いくつかの重大な障害を経験してきました。以下は、地域やサービスを横断して広範な影響を与えた主な障害を年代順にまとめたものです。このリストは公式レポート、歴史的分析、インシデントレビューに基づき、日付、原因、影響範囲、利用可能な場合は継続時間を記載しています。

| 日付 | 原因 | 影響を受けた地域/サービス | 継続時間/影響 |
|------|-------|---------------------------|-----------------|
| 2012年2月29日 | コード内の閏年計算バグ | 北米 (Azure Compute) | 約8時間；ユーザーのアプリケーション管理とサービスが中断。 |
| 2012年7月26日 | 設定誤りのあるネットワークデバイス | 西ヨーロッパ (Azure Compute) | 2時間以上；ヨーロッパでの部分的な利用不可。 |
| 2013年2月22日 | SSL証明書の期限切れ | グローバル (Azure Storage) | 数時間；サービスクレジット発行。Xbox Live、Music、Videoにも影響。 |
| 2013年10月30日 | 部分的なコンピュート障害 (スロットリング問題) | 全世界 (Azure Compute、管理機能) | 約3-4時間；ファイルアップロードとサイト管理に影響。 |
| 2013年11月22日 | ストレージおよびネットワークの問題 | 米国中北部 (Xbox Live) | Xbox One発売日に数時間；顧客への影響は低いが注目度は高かった。 |
| 2014年11月19日 | Blobストレージで無限ループを引き起こす設定変更 | グローバル (20以上のサービス、Azure Storageを含む) | 約6-10時間；複数リージョンで容量低下。Xbox Live、MSN、Visual Studio Onlineに影響。 |
| 2016年9月15日 | グローバルDNS障害 | 全世界 (Azure DNS) | 約2時間；広範なサービス中断。 |
| 2017年3月7日 & 23日 | 複数のインシデント (ネットワークおよびストレージ) | グローバル (Office 365, Skype, Xbox Live) | それぞれ最大16時間以上；広範なユーザーアクセス問題。 |
| 2017年9月29日 | メンテナンス中の消火ガス放出によるシャットダウン作動 | 米国リージョン (各種サービス) | 約7時間；断続的な不具合。 |
| 2018年9月4日 | 落雷による電圧急上昇と冷却システム障害 | 米国中南部、複数リージョン (40以上のサービス) | 25時間以上、一部影響は3日間継続；サービス全体で大きなダウンタイム。 |
| 2020年1月25日 | Azure SQL Databaseのバックエンド依存関係の障害 | グローバル (ほぼ全リージョン、米国政府/国防総省を含む) | 約6時間；SQL DB、Application Gateway、Bastion、Firewallに影響。 |
| 2021年4月1日 | ネットワークインフラでの広範なDNS問題 | グローバル (米国、ヨーロッパ、アジア等) | 約1.5時間；コアネットワークに依存するサービスに影響。 |
| 2022年6月1日 | Azure Active Directory サインインログの問題 | グローバル (複数リージョン) | 約9.5時間；AAD、Sentinel、Monitor、Resource Managerに影響。 |
| 2022年6月29日 | 詳細不明のバックエンド不安定性 | グローバル (数十のリージョン) | 約24時間断続的；Firewall、Synapse、Backupなどに影響。 |
| 2023年1月25日 | 欠陥のあるルーターコマンドによるネットワーク障害 | グローバル (25以上のリージョン、東部 US、西ヨーロッパを含む) | 約3.5時間；M365 (Teams、Outlook)、SharePoint、Office 365で遅延と障害。 |
| 2023年6月9日 | Anonymous Sudanが主張するDDoS攻撃 | グローバル (Azure Portal とクラウドサービス) | 約2.5時間；ポータルおよび関連サービスがダウン。 |
| 2024年11月13日 | StorageのDNS解決障害 | 複数 (東部 US/2、中部 US、西部 US/2 等) | 約8.5時間；DatabricksとStorage Accountsに影響。 |
| 2024年12月26日 | アベイラビリティゾーンでの電力インシデント | 米国中南部 (Zone 03) | 約18時間；Storage、VM、Cosmos DB、SQL DBなどに影響。 |
| 2025年1月9日 | ネットワーク障害 | 東部 US 2 | 48時間以上；Databricks、Synapse、Functions、App Service、VMに影響。 |
| 2025年9月10日 | スロットリング変更によるアロケーターサービスの過負荷 | 東部 US 2 (Zone 02/03) | 約10.5時間；VM操作が劣化、Backup、Batch、Kubernetes、Synapseに影響。 |
| 2025年9月26-27日 | 設定変更における不正な証明書値 | スイス北部 (複数ゾーン) | 約22時間；API Management、App Service、Cosmos DB、VM、Sentinelで広範な障害。 |
| 2025年10月9日 | Azure Front Door コントロールプレーンの欠陥 | ヨーロッパおよびアフリカ | 約8時間；ポータルとサービスでの遅延/タイムアウト (アフリカでは最大17%の失敗率)。 |
| 2025年10月9日 | 自動化スクリプトによる後続の設定削除 | グローバル (管理ポータル) | 約4時間；AFDインシデント後のAzure Portalなどへのアクセス問題。 |

これらのインシデントは全事例の一部ですが、範囲と継続時間に基づいて最も破壊的なものとなっています。Microsoftは通常、教訓を得るために事後インシデントレビュー(PIR)を発行しており、時間の経過とともに可用性は向上し、SLAでは99.99%の稼働率を目標としています。

## 参考資料
- [A History of Microsoft Azure Outages](https://www.datacenterknowledge.com/outages/a-history-of-microsoft-azure-outages)
- [Microsoft Azure Outage History Overview](https://statusgator.com/blog/azure-outage-history/)
- [Azure Status History](https://azure.status.microsoft/en-us/status/history/)
- [Microsoft Azure Wikipedia - Outages Section](https://en.wikipedia.org/wiki/Microsoft_Azure#Outages)