---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PCFログのためのKibanaセットアップ
translated: true
type: note
---

「kabana」はおそらく **Kibana**（Elasticsearch 用のオープンソースデータ可視化ダッシュボード）を指していると思われます。**Pivotal Cloud Foundry (PCF)**（現在は VMware Tanzu Application Service にリブランド）のコンテキストでは、Kibana はプラットフォームのログシステム（Loggregator）を通じてログの検索、可視化、分析によく使用されます。PCF は Kibana をスタンドアロンでネイティブ実行することはありませんが、**Log Search** タイル/サービスを介して統合します。これはログを Elasticsearch に保存し、クエリ用に Kibana を公開します。

もしこれが意図した内容でなければ、お気軽に詳細を説明してください！以下では、PCF ログで Kibana をセットアップして使用する方法を説明します。これは、PCF Ops Manager にアクセスできる管理者であり、実行中の PCF デプロイメント（バージョン 2.0 以上）があることを前提としています。PCF のログ機能は進化していることに注意してください。詳細はお使いのバージョンのドキュメントを確認してください。

### 前提条件
- **PCF バージョン**: Log Search（Kibana 含む）は PCF 2.2 以降で利用可能です。以前のバージョンでは別個の「ELK」（Elasticsearch、Logstash、Kibana）タイルが使用されていました。
- **タイル/サービス**: **Elastic Runtime** タイル（Loggregator 用）と **Log Search** タイルが Pivotal Network（現在は Broadcom Support Portal）を通じてインストールされていることを確認してください。
- **アクセス**: Ops Manager および PCF CLI（cf コマンドラインツール）での管理者権限。
- **リソース**: 十分なリソースを割り当ててください（例：ログ量に応じて Log Search に 4-8 GB の RAM）。

### ステップ 1: Ops Manager で Log Search タイルをインストールおよび設定する
Log Search タイルは、PCF のログ（アプリ、プラットフォーム、システムコンポーネントからのもの）を Elasticsearch に転送し、Kibana を通じて検索可能にします。

1. **タイルのダウンロードとインポート**:
   - Broadcom Support Portal（旧 Pivotal Network）にログインします。
   - **Log Search for PCF** タイル（例：お使いの PCF リリースに合ったバージョン）をダウンロードします。
   - Ops Manager（Web UI）で、**Catalog** > **Import a Product** に移動し、タイルをアップロードします。

2. **タイルの設定**:
   - Ops Manager で、**Elastic Runtime** タイル > **Loggregator** タブに移動します：
     - **Loggregator forwarding to external systems** を有効にします（必要に応じて syslog や HTTP 転送を設定しますが、Log Search の場合は内部処理されます）。
     - **Loggregator log retention** を 5-30 日などの値に設定します。
   - **Log Search** タイルに移動します：
     - **Assign Availability Zones**: 高可用性のために少なくとも 1 つの AZ を選択します。
     - **Elasticsearch Configuration**:
       - インスタンス数を設定します（本番環境では 3 から開始）。
       - ストレージを設定します（例：100 GB の永続ディスク）。
       - セキュリティを有効にします（例：Elasticsearch 用の TLS）。
     - **Kibana Configuration**:
       - Kibana を有効にします（バンドルされています）。
       - 管理者資格情報（ユーザー名/パスワード）を設定します。
     - **Loggregator Integration**:
       - 最大ログ行数/秒を設定します（例：負荷に基づいて 1000-5000）。
       - インデックスパターンを定義します（例：ログを 7-30 日間保持）。
     - **Networking**: ルートを介して Kibana を公開します（例：`kibana.YOUR-PCF-DOMAIN.com`）。
   - **Apply Changes** をクリックしてデプロイします。これには 30-60 分かかる場合があります。

3. **デプロイメントの確認**:
   - `cf tiles` を実行するか、Ops Manager で成功を確認します。
   - Log Search VM に SSH 接続し（BOSH CLI を使用：`bosh ssh log-search/0`）、Elasticsearch が実行されていることを確認します（`curl localhost:9200`）。

### ステップ 2: Kibana にアクセスする
デプロイ後：

1. **PCF Apps Manager (GUI) 経由**:
   - Apps Manager にログインします（例：`https://apps.YOUR-PCF-DOMAIN.com`）。
   - "Log Search" サービスインスタンスを検索します（自動的に 1 つ作成されます）。
   - サービスインスタンスをクリック > **Logs** タブ。これにより、簡易ログ検索用の組み込み Kibana ビューが開きます。

2. **Kibana への直接アクセス**:
   - タイルで設定した Kibana URL に移動します（例：`https://kibana.YOUR-PCF-DOMAIN.com`）。
   - 設定した管理者資格情報でログインします。
   - カスタムドメインを使用している場合は、DNS が正しくポイントされ、ルートが登録されていることを確認します（確認するには `cf routes`）。

3. **CLI アクセス（オプション）**:
   - 基本的なログには `cf logs APP-NAME` を使用しますが、高度なクエリには Kibana UI または API を使用します。
   - アプリに Log Search をバインドします：`cf create-service log-search standard my-log-search`、次に `cf bind-service APP-NAME my-log-search`。

### ステップ 3: PCF ログでの Kibana の使用
Kibana は、PCF コンポーネント（例：アプリログ、Diego セル、Gorouter など）からのログをクエリ、フィルタリング、可視化するための Web ベースのインターフェースを提供します。

1. **基本ナビゲーション**:
   - **Discover タブ**: Lucene クエリ構文を使用してログを検索します。
     - 例：特定のアプリのエラーを検索：`source_id:APP:your-app-name AND json.message:ERROR`。
     - 利用可能なフィールド：`timestamp`、`source_id`（例：`APP:your-app`、`RTR:router`）、`message`、`deployment` など。
   - **Visualize タブ**: チャート用のダッシュボードを作成します（例：時間経過に伴うログ量、エラーレート）。
     - サンプル可視化：source_id によるログの棒グラフ。
   - **Dashboard タブ**: 事前構築済みのダッシュボードを保存および共有します（Log Search には PCF ログ用のデフォルトが含まれています）。

2. **一般的なクエリとヒント**:
   - **アプリでフィルタ**: `source_id:APP:your-app-name`（実際のアプリ GUID または名前に置き換え）。
   - **時間でフィルタ**: タイムピッカーを使用します（例：過去 24 時間）。
   - **システムログ**: `source_id:DEA`（Diego セル用）または `source_id:LOGGREGATOR`。
   - **ログのエクスポート**: Discover から CSV/JSON としてダウンロードします。
   - **高度な使用法**: Kibana の Dev Tools（コンソール）を使用して Elasticsearch に直接クエリを実行します、例：
     ```
     GET /logstash-*/_search
     {
       "query": { "match": { "message": "error" } },
       "sort": [ { "timestamp": { "order": "desc" } } ]
     }
     ```
   - **保持とインデックス作成**: ログは日単位でインデックス化されます（例：`logstash-YYYY.MM.DD`）。ストレージを管理するには、タイルでロールオーバーを設定します。

3. **ログのトラブルシューティング**:
   - **ログが表示されない？** Loggregator の転送ルールを確認します（Ops Manager > Elastic Runtime > Loggregator）。アプリがログを出力していることを確認します（例：Node.js での `console.log` 経由）。
   - **パフォーマンスの問題？** Elasticsearch インスタンスをスケールアップするか、ログレート制限を調整します。
   - **セキュリティ**: Kibana への SSO ログインのために、Log Search で UAA 統合を有効にします。
   - **エラー**: `cf logs log-search` または Ops Manager の errand ログで PCF ログを確認します。

### 追加リソース
- **公式ドキュメント**: [Log Search](https://docs.vmware.com/en/VMware-Tanzu-Application-Service/10.0/tas/GUID-log-search-index.html) に関する VMware Tanzu ドキュメント（お使いのバージョンを検索）。
- **CLI ツール**: 必要に応じて UAA 認証用に `uaac` をインストールするか、API アクセスに `cf curl` を使用します。
- **代替手段**: より単純なニーズには、PCF 組み込みの **Log Cache**（cf CLI: `cf tail APP-NAME`）を使用するか、syslog 転送を介して Splunk などの外部ツールと統合します。
- **アップグレード**: レガシー PCF を使用している場合は、ELK タイルに移行するか、Broadcom サポートに連絡してください。

詳細（例：PCF バージョン、エラーメッセージ、または特定のユースケース）を提供していただければ、さらに詳細を説明できます！