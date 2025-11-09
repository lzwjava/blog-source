---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 主要なGoogle Cloud Platform障害
translated: true
type: note
---

### Google Cloud Platform (GCP) の主要な障害履歴

Google Cloud Platform は、その初期からソフトウェアのバグ、ハードウェア障害、環境要因、またはキャパシティの問題により、いくつかの重大な障害を経験してきました。以下は、規模、期間、または広範な影響に基づいて選ばれた、特に注目すべき障害の一部をまとめた表です。これらは2025年半ばまでの歴史的記録に基づいています。

| 日付 | 原因 | 影響 |
|------|--------|--------|
| 2020年12月14日 | 中央ユーザーID管理システムのキャパシティ誤削減により、OAuthベースの認証に影響。 | 約90分間のグローバル障害。Gmail、YouTube、Google Drive、GCPサービス、Pokémon GOなどのアプリへのアクセスが世界中の数百万人のユーザーで中断。 |
| 2022年7月 | ロンドンでの40°Cを超える熱波により、europe-west2-aゾーンの冷却システムが故障。 | 約24時間の地域的混乱。Cloud Storage、BigQuery、Compute Engine、GKEなどのサービスに影響し、他リージョンへのフェイルオーバーを強制。 |
| 2022年8月8日 | アイオワ州カウンシルブラフスデータセンターでの電気事故による火災（同時発生した検索/マップの問題とは無関係）。 | 局所的な火災対応。Cloud Loggingサービスで数日間にわたるグローバルなレイテンシーが発生し、GCPユーザーの監視とデバッグに影響。 |
| 2023年4月28日 | パリデータセンターでの浸水と火災により、europe-west9-aでマルチクラスター障害が発生。 | 欧州、アジア、米州にわたる広範な混乱。VPC、Load Balancing、BigQuery、ネットワークサービスが数時間から数日間にわたって影響を受けた。 |
| 2024年8月7-8日 | Vertex AI の API 有効化中の Cloud TPU サービスアクティベーションの障害。 | 約14時間のグローバル障害。すべての主要リージョンにおける Vertex AI での機械学習モデルのアップロードとトレーニングをブロック。 |
| 2024年10月23日 | europe-west3-cゾーン（フランクフルト）での電源障害とアーク放電により、冷却インフラが劣化。 | 半日（約8時間）の地域的障害。インフラの一部シャットダウンと、他ゾーンへのトラフィック転送が実施された。 |
| 2025年1月7-8日 | ApigeeでのSAML認証障害、Vertex Gemini APIでのHTTPエラー、Pub/Subでの公開ブロックなど、相互に関連した問題。 | 18時間以上にわたる複数時間の混乱。複数リージョンにわたるAPI管理、AI推論、リアルタイムメッセージングに影響。 |
| 2025年6月12日 | 新機能 Service Control（クォータポリシーチェック）のバグにより、us-central1などの大規模リージョンでタスク過負荷が発生。 | 約7時間のグローバル障害。Spotify、Discord、Fitbitなど、GCPに依存する多数のサービスがダウンし、140万件以上のレポートが寄せられた。 |

これらのインシデントは、2000年代後半の初期の App Engine の問題から、より最近のシステム的な障害まで、GCPの成長に伴う苦難を浮き彫りにしています。Googleは通常、事後分析報告書と是正計画を発行し、コンポーネントを「フェイルオープン」するようにモジュール化するなどの対策を講じています。最新のステータスは、[Google Cloud Service Health](https://status.cloud.google.com/) で確認してください。

[A History of Google Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-google-cloud-and-data-center-outages)  
[Google services outages - Wikipedia](https://en.wikipedia.org/wiki/Google_services_outages)  
[Google Cloud Outage History | StatusGator](https://statusgator.com/blog/google-cloud-outage-history/)  
[The 10 Biggest Cloud Outages Of 2025 (So Far) - CRN](https://www.crn.com/news/cloud/2025/the-10-biggest-cloud-outages-of-2025-so-far)  
[Google Cloud Outage Analysis: June 12, 2025 - ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)