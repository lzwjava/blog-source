---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: VMware Tanzu Application Service 概要
translated: true
type: note
---

## VMware Tanzu Application Service for VMs (TAS for VMs) の紹介

VMware Tanzu Application Service for VMs (TAS for VMs) は、オープンソースの Cloud Foundry プロジェクトを基盤とする商用のプラットフォーム・アズ・ア・サービス (PaaS) です。インフラストラクチャの管理ではなく、コードの記述に開発者が集中できるよう、クラウドネイティブアプリケーションのデプロイ、スケーリング、管理を簡素化するように設計されています。TAS for VMs は、オンプレミス (vSphere など) やパブリッククラウド (AWS、Azure、GCP、OpenStack) など、さまざまな環境での迅速なアプリケーションのデプロイを可能にし、自己管理型セットアップと認定された商用プロバイダーの両方をサポートします。

### 主な機能
- **オープンソース基盤**: Cloud Foundry の拡張性を活用してベンダーロックインを回避し、複数の言語、フレームワーク、サービスをサポートします。
- **自動化されたデプロイ**: コード変更なしで使い慣れたツール (CLI など) を使用してアプリケーションをプッシュします。アプリケーションは迅速なステージングと実行のために「droplet」(事前コンパイル済みバンドル) にパッケージ化されます。
- **スケーラビリティと回復性**: Diego を使用して VM 間でインテリジェントな負荷分散、自動スケーリング、フォールトトレランスを実現し、トラフィックの急増や障害に対処します。
- **ユーザー管理**: UAA (User Account and Authentication) サーバーを介して、チームを「組織 (Organization)」と「スペース (Space)」に分け、ロールベースのアクセス (管理者、開発者など) を設定します。
- **サービス統合**: Service Broker を介して、アプリケーションコードを変更することなく、データベースや API などのサービスにアプリケーションを簡単にバインドします。
- **モニタリングとロギング**: Loggregator を使用してログとメトリクスを「Firehose」ストリームに集約し、リアルタイム分析、アラート、ツールとの連携を実現します。
- **スモールフットプリントオプション**: 標準版の 13+ VM に対してわずか 4 VM で動作する軽量版で、小規模なチームやテストに最適ですが、スケールに制限があります。
- **柔軟なインフラストラクチャ**: BOSH (自動化ツール) を介してデプロイされ、Tanzu Operations Manager で管理され、効率的な構成を実現します。

### 利点
TAS for VMs は、アプリケーションを数分で公開可能にし、自動スケーリングとグローバルなアクセス性を提供することで、製品化までの時間を短縮します。インフラストラクチャのオーバーヘッドを削減し、区画化されたワークスペースを通じてセキュリティを強化し、アプリケーションが環境間で一貫して実行されるため、移植性を促進します。VM 管理を抽象化することで、コストと複雑さを削減し、Cloud Foundry コミュニティが継続的な革新とサポートを保証します。

### 仕組み
中核において、TAS for VMs はマルチテナントの PaaS として機能します:
1.  **デプロイ**: Tanzu Operations Manager を使用して、BOSH で管理される VM 上でプラットフォームを構成、デプロイします。
2.  **アプリケーションライフサイクル**: 開発者は CLI 経由でコードをプッシュします。Cloud Controller が buildpack (言語固有のセットアップ用) を使用してコードをステージングし droplet に変換します。その後、Diego がホスト VM 全体でインスタンスのオークションを行い、実行します。
3.  **ルーティングとアクセス**: Gorouter が着信トラフィックを処理し、外部でロードバランシングされます。UAA がユーザーを認証します。
4.  **運用**: 内部コンポーネントは NATS メッセージングと BOSH DNS を介して通信します。blob や設定などのリソースは、GitHub、blobstore、または MySQL に保存されます。

TAS for VMs は、オープンソースの Cloud Foundry を、VMware のエンタープライズグレードの機能、サポート、認定で拡張し、本番ワークロードに対する堅牢な選択肢となっています。

詳細については、公式ドキュメントを参照してください: [TAS for VMs Overview](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform-for-cloud-foundry/6-0/tpcf/concepts-overview.html)