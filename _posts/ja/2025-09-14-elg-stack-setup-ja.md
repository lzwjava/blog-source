---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: ELGスタックセットアップとインストールガイド
translated: true
type: note
---

### ELGスタック（Elasticsearch、Logstash、Grafana）の概要

ELGスタック（可視化ツールとしてKibanaの代わりにGrafanaを使用するELKスタックの変種）は、アプリケーション、サーバー、インフラからのログなど、大量のデータを収集、処理、保存、可視化するための強力なオープンソーススイートです。リアルタイム監視、分析、アラート機能を実現します。主な構成要素：

- **Elasticsearch**: 分散型の検索・分析エンジン。大規模なデータの保存、検索、分析を担当。
- **Logstash**: 複数のソースからデータを取り込み、変換し、Elasticsearchに送信するデータ処理パイプライン。
- **Grafana**: Elasticsearchなどのデータソースに接続し、チャート、グラフ、アラートを作成する可視化・監視ダッシュボードツール。

このガイドは基本的なLinux知識（例：Ubuntu/Debian；他OSでは適宜読み替え）を前提とします。詳細は公式ドキュメントを参照してください。elastic.coとgrafana.comからのダウンロードによるインストール方法を説明します。

#### 1. Elasticsearchのインストール
Elasticsearchはデータの保存とインデックス作成を担当します。

- **前提条件**: Java 11以上（`sudo apt update && sudo apt install openjdk-11-jdk`でインストール）。
- ダウンロードとインストール:
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- 起動と有効化: `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`。
- 確認: `http://localhost:9200` にアクセス – クラスタ情報を含むJSONが返されるはずです。
- 基本設定（`/etc/elasticsearch/elasticsearch.yml`を編集）: リモートアクセスのため `network.host: 0.0.0.0` を設定（本番環境ではTLS/ファイアウォールで保護）。

#### 2. Logstashのインストール
Logstashはソース（例：ファイル、syslog）からデータを取得し、Elasticsearchに送信します。

- Elasticsearchと併せてインストール:
  ```
  sudo apt install logstash
  ```
- 起動と有効化: `sudo systemctl start logstash && sudo systemctl enable logstash`。
- ログ取り込みの設定例（`/etc/logstash/conf.d/simple.conf`）:
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- パイプラインのテスト: `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf`（永続的に使用する場合はバックグラウンドで実行）。
- 設定の再読み込み: `sudo systemctl restart logstash`。

#### 3. Grafanaのインストール
GrafanaはElasticsearchデータを可視化するダッシュボードを提供します。

- インストール:
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- 起動と有効化: `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`。
- アクセス: `http://localhost:3000` にアクセス（デフォルトログイン: admin/admin；パスワード変更推奨）。
- Elasticsearchへの接続:
  1. Configuration > Data Sources > Add data source に移動。
  2. "Elasticsearch"を選択、URLを `http://localhost:9200`、インデックス名（例: `logstash-*`）、時間フィールド（例: `@timestamp`）を設定。
  3. 保存し接続をテスト。

#### 完全なELGパイプラインの構築
1. **データフロー**: Logstashがログを収集/解析 → Elasticsearchに送信 → Grafanaがクエリを実行し可視化。
2. **ワークフローの例**:
   - サンプルデータの送信: Logstash入力プラグインや `stdout` などのツールを使用してテスト。
   - Elasticsearchでのインデックス作成: ログはドキュメントとして表示（例: Kibana APIまたは直接curl: `curl -X GET "localhost:9200/_search?pretty"`）。
   - Grafanaでのダッシュボード: パネルを作成（例: Luceneクエリ `program:kern*` を使用した経時的なログエラーの折れ線グラフ）。
3. **セキュリティの基本**: HTTPS/TLS、認証（例: ElasticsearchのX-Pack）、ファイアウォールを使用。本番環境では複数ノード/クラスタでスケール。
4. **監視**: ElasticsearchでJVM監視を有効化；Grafanaには閾値のための組み込みアラート機能あり。

#### 一般的な問題とヒント
- **メモリ不足**: `/etc/elasticsearch/jvm.options` でJVMヒープを増加（例: `-Xms1g -Xmx1g`）。
- **ポート競合**: デフォルトポート: Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – `netstat -tulpn` で確認。
- **パフォーマンス**: 軽量なデータ転送にはLogstashの代わりにbeats（例: Filebeat）を使用。
- **学習リソース**: Elastic公式ガイド (elastic.co/guide), Grafanaドキュメント (grafana.com/docs)。Dockerでの練習: GitHubで「ELG stack Docker Compose」を検索。

カスタム設定や特定のエラーのトラブルシューティングについては、詳細を提供してください。これは出発点です；ELGはログ分析、IoTデータ、アプリケーション監視に優れています。