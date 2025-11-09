---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: スイス ノースにおける大規模なAzure障害
translated: true
type: note
---

### スイス北部リージョンでのAzure障害：2025年9月26日～27日

このインシデントは、スイス北部リージョンで発生した大規模なプラットフォーム全体の障害であり、複数のアベイラビリティゾーンに影響を及ぼしました。障害はUTC時間9月26日23:54に始まり、UTC時間9月27日21:59に完全に解決するまで約22時間続きました。ほとんどのサービスはUTC時間9月27日04:00頃までに回復しましたが、一部の残存する問題については、その日遅くに手動での介入が必要でした。

#### 根本原因
この障害は、ソフトウェアロードバランサーインフラストラクチャ内の通信認証に使用される証明書に対する計画的な構成変更に起因するものでした。新しい証明書の1つに、検証中に検出されなかった**不正な形式の値**が含まれていました。この変更は、迅速なデプロイメントパスに従って行われたため、正常性保護策をトリガーすることなく、複数のゾーンに展開されてしまいました。その結果、以下の状況が発生しました：
- ロードバランサーがストレージリソースおよびノードへの接続を失いました。
- 影響を受けたVMは、ディスクの長時間の切断を検出し、データ破損を回避するために自動的にシャットダウンしました。
- この影響は依存サービスへ連鎖し、影響が増幅されました。

#### 影響を受けたサービス
この障害は、スイス北部でホストされている広範なAzureサービスに影響を及ぼしました。影響を受けたサービスには以下が含まれます：
- **コアインフラストラクチャ**: Azure Storage、Azure Virtual Machines (VMs)、Azure Virtual Machine Scale Sets (VMSS)
- **データベース**: Azure Cosmos DB、Azure SQL Database、Azure SQL Managed Instance、Azure Database for PostgreSQL
- **コンピュートとアプリ**: Azure App Service、Azure API Management、Azure Kubernetes Service (AKS)、Azure Databricks
- **ネットワーキングとセキュリティ**: Azure Application Gateway、Azure Firewall、Azure Cache for Redis
- **分析と監視**: Azure Synapse Analytics、Azure Data Factory、Azure Stream Analytics、Azure Data Explorer、Azure Log Analytics、Microsoft Sentinel
- **その他**: Azure Backup、Azure Batch、Azure Site Recovery、Azure Application Insights

これらのサービスに依存するサービス（例：カスタムアプリケーション）も影響を受け、広範囲にわたる利用不可またはパフォーマンスの低下を引き起こしました。

#### タイムラインと対応
- **UTC時間9月26日23:54**: 構成変更のデプロイ後、影響が始まります。
- **UTC時間9月27日00:08**: 自動監視が問題を検出します。
- **UTC時間9月27日00:12**: Azure StorageチームとNetworkingチームによる調査が開始されます。
- **UTC時間9月27日02:33**: 構成変更がロールバックされます。
- **UTC時間9月27日03:40**: 証明書のロールバックが完了します。
- **UTC時間9月27日04:00**: 大多数のサービスが自動的に回復します。競合状態や誤ったシャットダウン信号の解釈などにより、停止/異常状態のVMなど、残存する問題が特定されます。
- **UTC時間9月27日06:19–14:15**: 回復スクリプトの開発と検証を実施。SQL Managed Instance VM、Trusted Launch VM、Service Fabricクラスターなどの影響を受けたリソースに対して、対象を絞った再起動を実行します。
- **UTC時間9月27日16:15**: 残存問題に対して部分的な回復を達成します。
- **UTC時間9月27日21:59**: 最終検証後、完全な回復が確認されます。

接続性が回復した後、ほとんどのリソースは自動的に回復しましたが、カスタム拡張機能を持つVMなどの一部のリソースについては、起動シーケンスの問題を解決するために手動での再起動が必要でした。

#### 教訓と改善策
Microsoftの予備インシデントレビューでは、以下の積極的な修正が示されています：
- デプロイメントシステムへの監査機能の追加と、リスクの高い迅速なパイプラインの削除（完了済み）。
- 自動ロールバックによる安全対策の強化（完了済み）。
- 今後の予定：リソースの正常性の監視の改善（2025年11月まで）と、手動作業を最小限に抑えるための回復力のある回復プロセスの導入。

この事象は、共有インフラストラクチャにおける構成変更のリスクを浮き彫りにしましたが、Azureの対応によりデータ損失は限定され、迅速な広範な回復が可能となりました。

[Azure Status History](https://azure.status.microsoft/en-us/status/history/)