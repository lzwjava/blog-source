---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: キバナログチェックガイド
translated: true
type: note
---

Kibanaは、Elasticによって開発されたオープンソースのデータ可視化・探索ツールです。**ELK Stack**（Elasticsearch、Logstash、Kibana）の主要コンポーネントであり、集中ロギング、監視、分析に広く使用されています。Kibanaは、Elasticsearchに保存されたデータと対話するためのWebベースのインターフェースを提供し、ログをリアルタイムで検索、可視化、分析できます。アプリケーション、サーバー、またはクラウドサービスからのログを確認する際に特に強力です。

このガイドでは、Kibanaを使用してログを検査およびクエリする方法に焦点を当てます。セットアップ、基本的な使用方法、ログ確認のワークフロー、および高度なヒントについて説明します。基本的なELKセットアップで作業していることを想定しています。ELKが初めての場合は、まずElasticsearchとLogstashをインストールすることから始めてください（Kibanaは動作するためにElasticsearchを必要とします）。

## 1. 前提条件
Kibanaを使用する前に：
- **Elasticsearch**: バージョン8.x以降（KibanaはElasticsearchのバージョンと密接に連携します）。 [elastic.co](https://www.elastic.co/downloads/elasticsearch) からダウンロードしてください。
- **Java**: ElasticsearchにはJDK 11以降が必要です。
- **システム要件**: 開発用には少なくとも4GBのRAM。本番環境ではそれ以上。
- **データソース**: Logstash、Filebeatを介して、または直接Elasticsearchに取り込まれたログ（例：タイムスタンプ付きのJSON形式）。
- **ネットワークアクセス**: Kibanaはデフォルトでポート5601で実行されます。アクセス可能であることを確認してください。

まだログがない場合は、Filebeatなどのツールを使用してサンプルログ（例：システムログ）をElasticsearchに送信してください。

## 2. Kibanaのインストール
Kibanaのインストールは簡単で、プラットフォームに依存しません。最新バージョンを [elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) からダウンロードしてください（Elasticsearchのバージョンと一致させること）。

### Linux (Debian/Ubuntu) の場合:
1. Elasticのリポジトリを追加:
   ```
   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   sudo apt-get install apt-transport-https
   echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   sudo apt-get update && sudo apt-get install kibana
   ```
2. Kibanaを起動:
   ```
   sudo systemctl start kibana
   sudo systemctl enable kibana  # ブート時の自動起動用
   ```

### Windowsの場合:
1. ZIPアーカイブをダウンロードし、`C:\kibana-8.x.x-windows-x86_64` に展開します。
2. 管理者としてコマンドプロンプトを開き、展開したフォルダに移動します。
3. 実行: `bin\kibana.bat`

### macOSの場合:
1. Homebrewを使用: `brew tap elastic/tap && brew install elastic/tap/kibana-full`.
2. または、TAR.GZをダウンロードし、展開して `./bin/kibana` を実行します。

Dockerの場合: 公式イメージを使用:
```
docker run --name kibana -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 docker.elastic.co/kibana/kibana:8.10.0
```

## 3. 基本的な設定
設定ファイル `kibana.yml`（Linuxでは `/etc/kibana/`、その他では `config/` フォルダ内）を編集します。

ログ確認のための主要設定:
```yaml
# Elasticsearchへの接続（デフォルトはlocalhost:9200）
elasticsearch.hosts: ["http://localhost:9200"]

# サーバー設定
server.port: 5601
server.host: "0.0.0.0"  # リモートアクセスのためにすべてのインターフェースにバインド

# セキュリティ（本番環境で有効化）
# elasticsearch.username: "elastic"
# elasticsearch.password: "your_password"

# ロギング
logging.verbose: true  # Kibana自体のデバッグ用

# インデックスパターン（オプションのデフォルト）
defaultIndex: "logs-*"
```
- 変更後はKibanaを再起動: `sudo systemctl restart kibana`.
- セキュリティ機能（X-Pack）を使用する場合は、証明書を生成するか、基本認証を使用してください。

## 4. Kibanaの起動とアクセス
- まずElasticsearchを起動（例: `sudo systemctl start elasticsearch`）。
- 上記のようにKibanaを起動。
- Webブラウザを開き、`http://localhost:5601`（またはサーバーのIP:5601）に移動。
- 初回ログイン時には、セットアップウィザードが表示されます。プロンプトが表示されたら管理者ユーザーを作成してください（デフォルト: elastic/changeme）。

インターフェースには、**Discover**（ログ用）、**Visualize**、**Dashboard**、**Dev Tools**、**Management**などのアプリが含まれます。

## 5. データの準備: インデックスパターン
Elasticsearch内のログは**インデックス**（例: `logs-2023-10-01`）に保存されます。Kibanaでクエリするには、**インデックスパターン**を作成します。

1. **Stack Management** > **Index Patterns**（左サイドバー、ハンバーガーメニュー > Management）に移動。
2. **Create index pattern** をクリック。
3. `logs-*`（すべてのログインデックスに一致）や `filebeat-*`（Filebeatログ用）などのパターンを入力。
4. **Time field**（例: ログのタイムスタンプ用の `@timestamp` — 時間ベースのクエリに重要）を選択。
5. **Create index pattern** をクリック。
   - これにより、`message`（ログテキスト）、`host.name`、`level`（error/warn/info）などのフィールドがマッピングされます。

ログが変更された場合はフィールドを更新してください。**Discover**を使用してプレビューします。

## 6. Discoverを使用したログの確認
**Discover**アプリは、ログを検査するための主要なツールです。検索可能なログビューアのようなものです。

### 基本的なナビゲーション:
1. 左サイドバーの **Discover** をクリック。
2. ドロップダウン（左上）からインデックスパターンを選択。
3. 時間範囲（右上）を設定: 「Last 15 minutes」などのクイックオプション、またはカスタム（例: Last 7 days）を使用。これにより、`@timestamp` でログがフィルタリングされます。

### ログの表示:
- **ヒット数**: 合致するログの総数（例: 1,234 hits）を表示。
- **ドキュメントテーブル**: 生のログエントリをJSONまたはフォーマットされたテキストとして表示。
  - 列: デフォルトは `@timestamp` と `_source`（完全なログ）。左サイドバーからフィールド（例: `message`、`host.name`）をドラッグして列を追加。
  - 行を展開（矢印をクリック）して完全なJSONドキュメントを表示。
- **ヒストグラム**: 上部のチャートは時間経過に伴うログ量を表示。ドラッグしてズーム。

### ログの検索:
検索バー（上部）を使用してクエリを実行。Kibanaはデフォルトで**KQL (Kibana Query Language)**を使用します — シンプルで直感的です。

- **基本検索**:
  - キーワードの検索: `error`（「error」を含むログを検索）。
  - フィールド指定: `host.name:webserver AND level:error`（「webserver」からのエラーレベルのログ）。
  - フレーズ: `"user login failed"`（完全一致）。

- **フィルター**:
  - サイドバーから追加: フィールド値（例: `level: ERROR`）をクリック > Add filter（クエリにピン留め）。
  - ブール論理: `+error -info`（「error」を含む必要があり、「info」を除外）。
  - 範囲: 数値/時間用、例: `bytes:>1000`（フィールド > 1000）。

- **高度なクエリ**:
  - 複雑なニーズには**Luceneクエリ構文**に切り替え（クエリ言語ドロップダウン経由）: `message:(error OR warn) AND host.name:prod*`.
  - Elasticsearchネイティブのクエリには、Dev Toolsで**Query DSL**を使用（例: POST /logs-*/_search with JSON body）。

### 検索の保存:
- **Save**（右上）をクリックして検索を保存し、再利用。
- **Share** > CSV/URL 経由でエクスポート用に共有。

例: アプリケーションログの確認ワークフロー
1. ログの取り込み（例: Logstash経由: 入力ファイル > フィルターgrok/parse > 出力Elasticsearch）。
2. Discoverで: 時間範囲「Last 24 hours」。
3. 検索: `app.name:myapp AND level:ERROR`.
4. フィルター追加: `host.name` = 特定のサーバー。
5. 検査: `message` でスタックトレースを確認、`@timestamp` と相関。

## 7. ログの可視化
Discoverが生の確認用であるのに対し、Visualizeはパターン用です。

### 可視化の作成:
1. **Visualize Library** > **Create new visualization** に移動。
2. タイプを選択:
   - **Lens**（簡単）: フィールドをバケットにドラッグ（例: X軸: `@timestamp`、Y軸: エラーのカウント）。
   - **Area/Line Chart**: 時間経過に伴うログ量用（Metrics: Count、Buckets: Date Histogram on `@timestamp`）。
   - **Data Table**: 表形式のログ要約。
   - **Pie Chart**: `level` による内訳（error 40%、info 60%）。
3. Discoverからのフィルター/検索を適用。
4. 保存し、**Dashboard**に追加（Analytics > Dashboard > Create new > Add visualization）。

例: エラーレートダッシュボード
- 可視化: 時間ごとのエラーログの折れ線グラフ。
- フィルター: グローバルな時間範囲。
- 監視用にダッシュボードに埋め込み。

## 8. ログ分析のための高度な機能
- **アラートと監視**:
  - **Alerts**（Stack Management > Rules）を使用して、ログパターンに基づいて通知（例: 「critical」が1時間に5回以上出現した場合にメール送信）。
  - アプリログには**Uptime Monitoring**または**APM**。

- **機械学習**:
  - MLジョブを有効化（Stack Management > Machine Learning）して、ログ量の異常を検出。

- **Dev Tools**:
  - 生のElasticsearchクエリ用コンソール: 例:
    ```
    GET logs-*/_search
    {
      "query": { "match": { "message": "error" } },
      "sort": [ { "@timestamp": "desc" } ]
    }
    ```
  - インデックスパターンやデータ取り込みのテスト。

- **ロールとセキュリティ**:
  - 本番環境では、**Spaces**を使用してログビューを分離（例: dev/prod）。
  - ロールベースのアクセス: ユーザーを特定のインデックスに制限。

- **エクスポート/インポート**:
  - **Stack Management > Saved Objects** 経由で検索/ダッシュボードをNDJSONとしてエクスポート。
  - **Console**またはBeats経由でログをインポート。

- **パフォーマンスのヒント**:
  - カスタムマッピングには**Field Analyzer**（Index Patterns > field）を使用。
  - 大きな結果にはページネーション: ページごとのヒット数を調整（Discover設定）。
  - ビッグデータには、インデックスをシャード化し、ILM（Index Lifecycle Management）を使用。

## 9. ログソースとの統合
- **Filebeat/Logstash**: ログをElasticsearchに送信。
  - Filebeat設定の例（`filebeat.yml`）:
    ```yaml
    filebeat.inputs:
    - type: log
      paths: [/var/log/*.log]
      fields:
        app: myapp
    output.elasticsearch:
      hosts: ["localhost:9200"]
      index: "logs-%{+yyyy.MM.dd}"
    ```
  - 実行: `./filebeat -e`.
- **クラウドログ**: AWS S3、Azure、またはElastic Cloudと統合して管理セットアップ。

## 10. 一般的な問題のトラブルシューティング
- **Discoverにデータが表示されない**:
  - Elasticsearch接続を確認: `curl localhost:9200/_cat/indices`.
  - インデックスパターンがインデックスと一致することを確認（例: `*` の不一致がない）。
  - `@timestamp` が日付としてマッピングされていることを確認。

- **Kibanaが起動しない**:
  - ログ: `/var/log/kibana/kibana.log` またはコンソール出力を確認。
  - 一般的な原因: ポート5601が使用中、またはElasticsearchが実行されていない/セキュア。

- **クエリが遅い**:
  - 最適化: フィルターにはキーワードフィールドを使用、大きなテキストでのワイルドカードを避ける。
  - ヒープを増加: Elasticsearchの `jvm.options` を編集（例: `-Xms4g -Xmx4g`）。

- **ログ内のエラー**:
  - 403/401: 認証問題 — `elasticsearch.yml` でセキュリティを有効化。
  - バージョンの不一致: Kibana == Elasticsearch バージョンであることを確認。

- **リソース**:
  - 公式ドキュメント: [elastic.co/guide/en/kibana/current](https://www.elastic.co/guide/en/kibana/current/index.html).
  - フォーラム: Elastic Discuss または Stack Overflow.
  - サンプルデータ: Kibana経由でロード（Stack Management > Kibana > Sample Data）。

このガイドが、ログ確認のためのKibanaの使用を始める手助けとなるはずです。小さく始めましょう: ローカルELKスタックをセットアップし、サンプルログを取り込み、Discoverで実験してください。本番環境では、簡単さのためにElastic Cloudを検討してください。特定のセットアップ（例: Docker、AWS）がある場合は、詳細を提供して tailored advice を得てください！