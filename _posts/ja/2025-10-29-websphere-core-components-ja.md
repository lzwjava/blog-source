---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphereアプリケーションサーバーコアコンポーネント
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) の主要コンセプト

IBM WebSphere Application Server は、分散環境でサーバーを整理・管理するために階層構造を採用しています。これにより、集中管理、スケーラビリティ、負荷分散、高可用性が実現します。以下に、中核となるコンポーネントである **cell**、**cluster**、**node**、**server** を説明します。

- **Cell**: 分散WAS環境における最上位の論理コンテナです。単一の管理ドメインの下に1つ以上のノードをグループ化し、Deployment Manager (特別なサーバーインスタンス) によって管理されます。Cell は、共通の設定リポジトリ、セキュリティ設定、JMS バスなどのリソースを共有します。Cell により、トポロジ全体にわたるアプリケーションのデプロイやユーザー認証といった集中タスクが可能になります。ベース (スタンドアロン) 設定では、Cell は単一のノードのみを含む場合もあります。

- **Cluster**: ワークロード管理のために連携して動作する、1つ以上のアプリケーションサーバー (通常は複数のノードに跨る) の論理的なグループです。Cluster は、水平スケーリング、負荷分散、フェイルオーバー (例: 1台のサーバーが故障した場合、トラフィックが他のサーバーにルーティングされる) をサポートします。Cluster レベルで定義されたリソース (アプリケーションやデータソースなど) は、すべてのメンバーサーバーに自動的に伝搬されます。Cluster は Cell スコープであり、単一の Cell 内に存在します。

- **Node**: 1つ以上のサーバーをホストする物理マシン (または場合によってはマシンのグループ) の論理的な表現です。各 Node は Node Agent プロセスを実行し、Deployment Manager との通信の処理、設定の同期、サーバーライフサイクル (プロセスの起動/停止) の管理を行います。Node はクラスタリングの境界を定義し、Cell にフェデレート (参加) されます。

- **Server**: 基本的なランタイム単位であり、J2EE/Java EE アプリケーション (サーブレット、EJB、Webサービスなど) をホストし実行するアプリケーションサーバーのインスタンスです。Server は、スタンドアロンでも、Node/Cluster の一部でも構いません。異なるタイプがあります: アプリケーション用のアプリケーションサーバー、Cell 管理用の Deployment Manager、Node 調整用の Node Agent です。

### トポロジと階層

WAS のトポロジは分散管理のために設計された階層構造です:

1.  **Cell (最上位)**: 管理ドメイン全体を包含します。以下を含みます:
    - 1つの Deployment Manager (集中制御のため)。
    - 1つ以上の Node (Deployment Manager 経由でフェデレートされる)。
    - 0個以上の Cluster (ノードに跨る)。

2.  **Node (中位)**: 単一の Cell に属します。各 Node は:
    - ホストマシン上で実行される。
    - 1つの Node Agent を含む。
    - 1つ以上の Server をホストする。
    - リソーススコープの境界として機能する (例: 異なる Cell のノードに跨る Cluster は作成できない)。

3.  **Server (基本レベル)**: Node 内で実行されます。これらは:
    - スタンドアロン (ベース設定の場合) またはクラスタ化されている場合がある。
    - 最大1つの Cluster に属する。
    - 実際のアプリケーションワークロードを処理する。

**視覚的な階層** (簡略化):
```
Cell
├── Deployment Manager
├── Node 1
│   ├── Node Agent
│   ├── Server A
│   └── Server B
├── Node 2
│   ├── Node Agent
│   ├── Server C
│   └── Server D
└── Cluster X (members: Server B, Server C, Server D)
```

-   **通信フロー**: Deployment Manager は設定を Node Agent に同期させ、Node Agent はサーバーを管理します。Web トラフィックについては、外部のロードバランサー (IBM HTTP Server など) がリクエストを Cluster メンバーにルーティングします。
-   **スケーリング**: 成長に合わせて Cell にノード/サーバーを追加します。Cluster はノードを跨いだ冗長性を実現します。
-   **ベストプラクティス**: 関連する環境 (開発/テスト/本番) は別々の Cell に維持します。大きな Cell は管理を単純化しますが、アップグレードの複雑さを増します。

この構造は、単一サーバー設定から、数百台のサーバーを持つエンタープライズ規模のデプロイメントまで、あらゆるものをサポートします。

### 参考文献
-   [WebSphere Concepts: Cell, Node, Cluster, Server](https://itdevworld.wordpress.com/2009/05/03/websphere-concepts-cell-node-cluster-server/)
-   [How to Divide a WebSphere Topology into Cells](https://veithen.io/2013/11/04/divide-websphere-topology-into-cells.html)
-   [IBM Docs: Introduction to Clusters](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=servers-introduction-clusters)