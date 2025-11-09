---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: ELG 堆疊設定與安裝指南
translated: true
type: note
---

### ELG 技術堆疊概覽（Elasticsearch、Logstash、Grafana）

ELG 堆疊（通常是 ELK 堆疊的變體，其中 Kibana 被 Grafana 取代以進行視覺化）是一套功能強大的開源套件，用於收集、處理、儲存和視覺化大量數據，特別是來自應用程式、伺服器和基礎架構的日誌。它支援即時監控、分析和警報。關鍵組件：

- **Elasticsearch**：一個分散式搜尋和分析引擎，用於大規模儲存、搜尋和分析數據。
- **Logstash**：一個數據處理管道，從多個來源擷取數據，進行轉換，然後發送到 Elasticsearch。
- **Grafana**：一個視覺化和監控儀表板工具，可連接至如 Elasticsearch 的數據源，用於創建圖表、圖形和警報。

本指南假設具備基本的 Linux 知識（例如 Ubuntu/Debian；請根據其他作業系統進行調整）。詳細資訊請參閱官方文件。可透過 elastic.co 和 grafana.com 下載進行安裝。

#### 1. 安裝 Elasticsearch
Elasticsearch 負責數據儲存和索引。

- **先決條件**：Java 11+（透過 `sudo apt update && sudo apt install openjdk-11-jdk` 安裝）。
- 下載並安裝：
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- 啟動並啟用：`sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`。
- 驗證：訪問 `http://localhost:9200` – 應返回包含集群資訊的 JSON。
- 基本配置（編輯 `/etc/elasticsearch/elasticsearch.yml`）：設定 `network.host: 0.0.0.0` 以允許遠程訪問（在生產環境中需使用 TLS/防火牆進行安全保護）。

#### 2. 安裝 Logstash
Logstash 從來源（例如檔案、系統日誌）拉取數據並發送至 Elasticsearch。

- 與 Elasticsearch 一同安裝：
  ```
  sudo apt install logstash
  ```
- 啟動並啟用：`sudo systemctl start logstash && sudo systemctl enable logstash`。
- 用於擷取日誌的範例配置（`/etc/logstash/conf.d/simple.conf`）：
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
- 測試管道：`sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf`（持續使用時請在後台運行）。
- 重新載入配置：`sudo systemctl restart logstash`。

#### 3. 安裝 Grafana
Grafana 提供用於視覺化 Elasticsearch 數據的儀表板。

- 安裝：
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- 啟動並啟用：`sudo systemctl start grafana-server && sudo systemctl enable grafana-server`。
- 訪問：訪問 `http://localhost:3000`（預設登入：admin/admin；請更改密碼）。
- 連接至 Elasticsearch：
  1. 前往 Configuration > Data Sources > Add data source。
  2. 選擇 "Elasticsearch"，設定 URL 為 `http://localhost:9200`、索引名稱（例如 `logstash-*`）和時間字段（例如 `@timestamp`）。
  3. 儲存並測試連接。

#### 設定完整 ELG 管道
1. **數據流**：Logstash 收集/解析日誌 → 發送至 Elasticsearch → Grafana 查詢並視覺化。
2. **範例工作流程**：
   - 發送範例數據：使用 Logstash 輸入插件或如 `stdout` 的工具進行測試。
   - 在 Elasticsearch 中建立索引：日誌以文件形式出現（例如透過 Kibana API 或直接使用 curl：`curl -X GET "localhost:9200/_search?pretty"`）。
   - 在 Grafana 中建立儀表板：創建面板（例如，使用 Lucene 查詢如 `program:kern*` 來顯示隨時間變化的日誌錯誤折線圖）。
3. **基本安全**：使用 HTTPS/TLS、身份驗證（例如 Elasticsearch 的 X-Pack）和防火牆。在生產環境中，需透過多個節點/集群進行擴展。
4. **監控**：在 Elasticsearch 中啟用 JVM 監控；Grafana 具有用於閾值的內建警報。

#### 常見問題與提示
- **記憶體不足**：在 `/etc/elasticsearch/jvm.options` 中增加 JVM 堆記憶體（例如 `-Xms1g -Xmx1g`）。
- **端口衝突**：預設端口：Elasticsearch 9200/9300、Logstash 5044、Grafana 3000 – 使用 `netstat -tulpn` 檢查。
- **效能**：使用 beats（例如 Filebeat）代替 Logstash 進行輕量級傳輸。
- **學習資源**：Elastic 官方指南（elastic.co/guide）、Grafana 文件（grafana.com/docs）。使用 Docker 進行練習：在 GitHub 上搜尋 "ELG stack Docker Compose"。

如需自訂設定或針對特定錯誤進行故障排除，請提供更多詳細資訊。這是一個起點；ELG 在日誌分析、物聯網數據和應用程式監控方面表現卓越。