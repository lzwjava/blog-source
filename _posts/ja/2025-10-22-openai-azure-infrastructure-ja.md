---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenAIインフラストラクチャとAzureへの依存
translated: true
type: note
---

### OpenAIの技術スタック概要

OpenAIのインフラストラクチャは、大規模なAI研究、トレーニング、デプロイメントに最適化されており、スケーラビリティ、セキュリティ、迅速な実験に重点を置いています。2017年初頭にAWSから移行して以来、その多くはMicrosoft Azureを中心に構築されており、スーパーコンピューターとワークロードの基盤クラウドプラットフォームを提供しています。この移行により、専用ハードウェアとのより良い統合とコスト効率が実現しました。主な要素には、開発のための統一されたPythonモノレポ、オーケストレーションのためのKubernetes、Apache Kafkaのようなストリーミングツールが含まれます。以下では、カテゴリー別に分解し、Azureへの依存とKubernetesの詳細について説明します。

#### クラウドインフラストラクチャ: Azureへの高い依存
OpenAIは、研究および本番環境でAzureを広範囲に使用しており、GPTシリーズのようなフロンティアモデルのトレーニングも含まれます。これには以下が含まれます：
- **中核プラットフォームとしてのAzure**: すべての主要なワークロードはAzure上で実行され、機密データ（モデル重みなど）にはインターネットへの露出を最小限にするためにプライベートリンクストレージが使用されます。認証はAzure Entra IDと連携し、リスクベースのアクセス制御と異常検出を可能にします。
- **なぜこれほどAzureなのか？**: 流出した内部文書（おそらく2024年のセキュリティアーキテクチャに関する投稿を指す）は、トレーニング中の知的財産保護におけるAzureの役割を強調しています。Azureは、ロボティクス、ゲームなどのAI実験における大規模なGPUクラスターをサポートします。OpenAIとMicrosoftのパートナーシップにより、Azure OpenAI Serviceを介したモデルへの低遅延アクセスが保証されますが、内部的には、カスタムスーパーコンピューティングの基盤となっています。また、GPU負荷の高いタスクではオンプレミスデータセンターとハイブリッド化し、信頼性とバックアップのためにコントロールプレーン（例: etcd）をAzureで管理しています。

この深い統合により、OpenAIのスタックは簡単に移植可能ではなく、パフォーマンスとコンプライアンスのためにAzureのエコシステムに合わせて調整されています。

#### オーケストレーションとスケーリング: Kubernetes (AKS) とAzureによる最適化
Kubernetesはワークロード管理の中心であり、バッチスケジューリング、コンテナオーケストレーション、クラスター間の移植性を処理します。OpenAIは実験をAzure Kubernetes Service (AKS) 上で実行し、近年では7,500ノード以上にスケールしています（2017年の2,500ノードから増加）。
- **Azureエコシステム内でのAKSの信頼性**: ご指摘の通り、AzureのKubernetesサービスは、Azure製品に完全に組み込まれた場合に真価を発揮します。OpenAIはネットワーキングにAzure CNI (Container Network Interface) に切り替えました。これはAzureクラウド向けに特別に構築されたもので、Flannelのような汎用CNIではこの規模で確実に処理できない高パフォーマンスで大規模な環境を扱います。これにより、ボトルネックなしの動的スケーリング、自動ポッドヘルスチェック、障害時のフェイルオーバーが可能になります。Azureのネイティブ統合（例: Blob StorageとWorkload Identityのため）がないと、遅延、認証問題、または容量制約により信頼性が低下します。彼らのカスタムオートスケーラーはノードを動的に追加/削除し、アイドル状態のリソースコストを削減しながら、数日で実験を10倍にスケールすることを可能にします。
- **セキュリティレイヤー**: Kubernetesは、最小権限アクセスのためのRBAC、コンテナポリシーのためのアドミッションコントローラー、デフォルト拒否のネットワークエグレス（承認されたパス用の許可リスト付き）を実施します。高リスクジョブでは、追加の分離のためにgVisorを重ねて使用します。マルチクラスターフェイルオーバーにより、地域的な問題発生時もジョブを実行し続けます。

#### 開発とコード管理: モノレポアプローチ
OpenAIは、ほとんどの研究およびエンジニアリング作業のために単一のPythonモノレポを維持しています。これにより、コード、ライブラリ、依存関係が一元化され、チームはAI固有のパイプラインと並行して使い慣れたPythonツール（例: NumPy, PyTorch）を使用できます。これはストリーム処理とシームレスに統合され、実験のための摩擦を減らします。CI/CDパイプラインは、マルチパーティ承認とIaC (Infrastructure as Code) によってロックダウンされ、一貫したデプロイを実現します。

#### データ処理とストリーミング
- **Apache Kafka**: ログ、トレーニングデータ、結果のためのイベント基盤です。高可用性のためにマルチプライマリ構成となっており、カスタムコネクタ（例: 読み取りのためのユニオンストリーム、書き込みのためのPrism Sink）と、フェイルオーバーのようなトポロジ変化に適応するためのウォッチドッグを備えています。
- **Kubernetes上のPyFlink**: GenAIストリーム処理のため、Flink Kubernetes Operatorを使用した自動化を実現しています。PythonでのDataStream/Table APIをサポートし、状態管理にRocksDB、チェックポイントにAzure Blob Storageを使用します。セキュリティはWorkload Identityを介して確保され（長期間有効なキーは使用しない）、保護されています。

#### 監視と通信
- **Prometheus**: デバッグとメトリクスのため。
- **gRPC**: サービス間通信のため。

#### 2025年の進化
最近のアップデート（例: OpenAI DevDay 2025からの情報）は、モデルAPIやAgentKitのようなエージェントツールに焦点を当てる傾向がありますが、インフラスタックはAzure-Kubernetes中心のままです。彼らは学びを共有するために、オートスケーラーなどのツールをオープンソース化しています。

このスタックは、より迅速な反復のための「データフライホイール」を優先しますが、ハイパースケールにおけるAzureの信頼性と引き換えに移植性を犠牲にしています。同様のものを構築する場合、AKS + Kafkaから始めることで模倣できますが、Azure外では調整が必要になることを想定してください。

[How OpenAI Uses Kubernetes And Apache Kafka for GenAI](https://blog.bytebytego.com/p/how-openai-uses-kubernetes-and-apache)  
[Securing Research Infrastructure for Advanced AI](https://openai.com/index/securing-research-infrastructure-for-advanced-ai/)  
[OpenAI Kubernetes Case Study](https://kubernetes.io/case-studies/openai/)  
[How OpenAI Scaled Kubernetes with Azure CNI](https://medium.com/@PlanB./how-openai-scaled-kubernetes-with-azure-cni-to-handle-7-500-nodes-591162d0efa5)