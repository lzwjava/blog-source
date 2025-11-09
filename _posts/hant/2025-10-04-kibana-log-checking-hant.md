---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Kibana 記錄檢查指南
translated: true
type: note
---

Kibana 是由 Elastic 開發的開源資料視覺化與探索工具。它是 **ELK Stack**（Elasticsearch、Logstash、Kibana）的核心組件，廣泛應用於集中式日誌記錄、監控與分析。Kibana 提供網頁介面來操作儲存在 Elasticsearch 中的資料，讓您能即時搜尋、視覺化與分析日誌。它在檢查來自應用程式、伺服器或雲端服務的日誌方面尤其強大。

本指南重點在於使用 Kibana 檢查與查詢日誌。我們將涵蓋設定、基礎用法、日誌檢查工作流程與進階技巧。假設您已具備基礎 ELK 環境；若您是 ELK 新手，請先安裝 Elasticsearch 與 Logstash（Kibana 需依賴 Elasticsearch 才能運作）。

## 1. 前置準備
使用 Kibana 前需備妥：
- **Elasticsearch**：8.x 或更新版本（Kibana 與 Elasticsearch 版本需嚴格對應）。請從 [elastic.co](https://www.elastic.co/downloads/elasticsearch) 下載。
- **Java**：Elasticsearch 需要 JDK 11 或更新版本。
- **系統需求**：開發環境至少 4GB RAM；生產環境需更多資源。
- **資料來源**：透過 Logstash、Filebeat 或直接寫入 Elasticsearch 的日誌（例如含時間戳的 JSON 格式）。
- **網路存取**：Kibana 預設運行於連接埠 5601，請確保可存取。

若尚無日誌資料，可使用 Filebeat 等工具傳送範例日誌（如系統日誌）至 Elasticsearch。

## 2. 安裝 Kibana
Kibana 安裝流程簡單且跨平台。請從 [elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) 下載最新版本（需與 Elasticsearch 版本匹配）。

### Linux（Debian/Ubuntu）環境：
1. 添加 Elastic 軟體庫：
   ```
   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   sudo apt-get install apt-transport-https
   echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   sudo apt-get update && sudo apt-get install kibana
   ```
2. 啟動 Kibana：
   ```
   sudo systemctl start kibana
   sudo systemctl enable kibana  # 開機自動啟動
   ```

### Windows 環境：
1. 下載 ZIP 壓縮檔並解壓至 `C:\kibana-8.x.x-windows-x86_64`。
2. 以管理員身分開啟命令提示字元並導覽至解壓縮的資料夾。
3. 執行：`bin\kibana.bat`

### macOS 環境：
1. 使用 Homebrew：`brew tap elastic/tap && brew install elastic/tap/kibana-full`。
2. 或下載 TAR.GZ 壓縮檔，解壓後執行 `./bin/kibana`。

Docker 環境：使用官方映像檔：
```
docker run --name kibana -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 docker.elastic.co/kibana/kibana:8.10.0
```

## 3. 基礎設定
編輯設定檔 `kibana.yml`（Linux 位於 `/etc/kibana/`，其他系統位於 `config/` 資料夾）。

日誌檢查的關鍵設定：
```yaml
# 連接至 Elasticsearch（預設為 localhost:9200）
elasticsearch.hosts: ["http://localhost:9200"]

# 伺服器設定
server.port: 5601
server.host: "0.0.0.0"  # 綁定所有介面以支援遠端存取

# 安全性（生產環境請啟用）
# elasticsearch.username: "elastic"
# elasticsearch.password: "your_password"

# 記錄設定
logging.verbose: true  # 用於除錯 Kibana 本身

# 索引模式（可選預設值）
defaultIndex: "logs-*"
```
- 變更後請重啟 Kibana：`sudo systemctl restart kibana`。
- 若啟用安全性功能（X-Pack），請產生憑證或使用基礎驗證。

## 4. 啟動與存取 Kibana
- 請先啟動 Elasticsearch（例如 `sudo systemctl start elasticsearch`）。
- 依上述方式啟動 Kibana。
- 開啟網頁瀏覽器並前往 `http://localhost:5601`（或您的伺服器 IP:5601）。
- 首次登入時會顯示設定精靈。若提示請建立管理員使用者（預設帳密：elastic/changeme）。

介面包含多個應用模組，例如 **Discover**（用於日誌）、**Visualize**、**Dashboard**、**Dev Tools** 與 **Management**。

## 5. 準備資料：索引模式
Elasticsearch 中的日誌儲存於**索引**中（例如 `logs-2023-10-01`）。若要在 Kibana 中查詢，需建立**索引模式**。

1. 前往 **Stack Management** > **Index Patterns**（左側導覽列，漢堡選單 > Management）。
2. 點擊 **Create index pattern**。
3. 輸入模式名稱，例如 `logs-*`（匹配所有日誌索引）或 `filebeat-*`（用於 Filebeat 日誌）。
4. 選擇**時間欄位**（例如日誌時間戳 `@timestamp`——對時間型查詢至關重要）。
5. 點擊 **Create index pattern**。
   - 此操作將映射欄位如 `message`（日誌文字）、`host.name`、`level`（error/warn/info）等。

若日誌結構變更，請重新整理欄位。可透過 **Discover** 預覽資料。

## 6. 使用 Discover 檢查日誌
**Discover** 應用是檢視日誌的主要工具，功能類似可搜尋的日誌檢視器。

### 基礎操作：
1. 點擊左側導覽列的 **Discover**。
2. 從下拉選單（左上角）選擇您的索引模式。
3. 設定時間範圍（右上角）：使用快速選項如「Last 15 minutes」或自訂範圍（例如 Last 7 days）。此設定會根據 `@timestamp` 篩選日誌。

### 檢視日誌：
- **命中計數**：顯示符合條件的日誌總數（例如 1,234 hits）。
- **文件表格**：以 JSON 或格式化文字顯示原始日誌條目。
  - 欄位：預設顯示 `@timestamp` 與 `_source`（完整日誌）。可從左側導覽列拖曳欄位（例如 `message`、`host.name`）以新增欄位。
  - 點擊列旁的箭頭可展開檢視完整 JSON 文件。
- **長條圖**：頂部圖表顯示隨時間變化的日誌量。可透過拖曳縮放時間範圍。

### 搜尋日誌：
使用頂部搜尋列進行查詢。Kibana 預設使用 **KQL（Kibana Query Language）**——語法簡潔直觀。

- **基礎搜尋**：
  - 關鍵字搜尋：`error`（找出包含 "error" 的日誌）。
  - 指定欄位：`host.name:webserver AND level:error`（來自 "webserver" 且層級為 error 的日誌）。
  - 片語搜尋：`"user login failed"`（完全匹配）。

- **篩選器**：
  - 從側邊欄新增：點擊欄位值（例如 `level: ERROR`）> 新增篩選器（將固定至查詢條件）。
  - 布林邏輯：`+error -info`（必須包含 "error"，排除 "info"）。
  - 範圍查詢：針對數字/時間欄位，例如 `bytes:>1000`（欄位值大於 1000）。

- **進階查詢**：
  - 切換至 **Lucene 查詢語法**（透過查詢語言下拉選單）以滿足複雜需求：`message:(error OR warn) AND host.name:prod*`。
  - 在 Dev Tools 中使用 **Query DSL** 進行原生 Elasticsearch 查詢（例如 POST /logs-*/_search 搭配 JSON 主體）。

### 儲存搜尋：
- 點擊**儲存**（右上角）可儲存搜尋條件供重複使用。
- 透過**分享** > CSV/URL 匯出或分享搜尋結果。

範例工作流程：檢查應用程式日誌
1. 擷取日誌（例如透過 Logstash：輸入檔案 > 篩選器 grok/解析 > 輸出至 Elasticsearch）。
2. 在 Discover 中：設定時間範圍為「Last 24 hours」。
3. 搜尋：`app.name:myapp AND level:ERROR`。
4. 新增篩選器：`host.name` = 特定伺服器。
5. 檢查：檢視 `message` 中的堆疊追蹤，並與 `@timestamp` 進行關聯分析。

## 7. 視覺化日誌
Discover 用於原始日誌檢查，視覺化功能則用於分析模式。

### 建立視覺化：
1. 前往 **Visualize Library** > **Create new visualization**。
2. 選擇類型：
   - **Lens**（簡易模式）：拖曳欄位至維度（例如 X 軸：`@timestamp`，Y 軸：錯誤計數）。
   - **區域/折線圖**：用於顯示隨時間變化的日誌量（指標：計數，維度：`@timestamp` 的日期長條圖）。
   - **資料表**：表格化日誌摘要。
   - **圓餅圖**：按 `level` 分類顯示（錯誤 40%，資訊 60%）。
3. 套用來自 Discover 的篩選器/搜尋條件。
4. 儲存並加入**儀表板**（Analytics > Dashboard > Create new > Add visualization）。

範例：錯誤率儀表板
- 視覺化：每小時錯誤日誌的折線圖。
- 篩選器：全域時間範圍。
- 嵌入儀表板以供監控。

## 8. 日誌分析進階功能
- **警示與監控**：
  - 使用**警示**（Stack Management > Rules）在日誌出現特定模式時發送通知（例如每小時出現超過 5 次 "critical" 時發送郵件）。
  - 使用 **Uptime Monitoring** 或 **APM** 處理應用程式日誌。

- **機器學習**：
  - 啟用 ML 任務（Stack Management > Machine Learning）以偵測日誌量的異常情況。

- **Dev Tools**：
  - 主控台用於執行原始 Elasticsearch 查詢，例如：
    ```
    GET logs-*/_search
    {
      "query": { "match": { "message": "error" } },
      "sort": [ { "@timestamp": "desc" } ]
    }
    ```
  - 測試索引模式或擷取資料。

- **角色與安全性**：
  - 在生產環境中，使用**空間**隔離日誌檢視（例如開發/生產環境）。
  - 基於角色的存取控制：限制使用者僅能存取特定索引。

- **匯出/匯入**：
  - 透過 **Stack Management > Saved Objects** 將搜尋/儀表板匯出為 NDJSON。
  - 透過 **Console** 或 Beats 匯入日誌。

- **效能優化技巧**：
  - 使用**欄位分析器**（Index Patterns > 欄位）進行自訂映射。
  - 大型結果分頁：調整每頁顯示筆數（Discover 設定）。
  - 處理巨量資料時，請分片索引並使用 ILM（索引生命週期管理）。

## 9. 與日誌來源整合
- **Filebeat/Logstash**：傳送日誌至 Elasticsearch。
  - Filebeat 設定範例（`filebeat.yml`）：
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
  - 執行：`./filebeat -e`。
- **雲端日誌**：與 AWS S3、Azure 或 Elastic Cloud 整合以實現託管設定。

## 10. 常見問題疑難排解
- **Discover 中無資料**：
  - 檢查 Elasticsearch 連線：`curl localhost:9200/_cat/indices`。
  - 確認索引模式是否匹配索引（例如無 `*` 誤配）。
  - 確保 `@timestamp` 已映射為日期類型。

- **Kibana 無法啟動**：
  - 檢查記錄檔：`/var/log/kibana/kibana.log` 或主控台輸出。
  - 常見原因：連接埠 5601 被佔用，或 Elasticsearch 未運行/安全性設定錯誤。

- **查詢速度緩慢**：
  - 優化方法：對篩選條件使用關鍵字欄位，避免對大型文字欄位使用萬用字元。
  - 增加堆積記憶體：編輯 Elasticsearch 的 `jvm.options`（例如 `-Xms4g -Xmx4g`）。

- **日誌中的錯誤**：
  - 403/401 錯誤：驗證問題——請在 `elasticsearch.yml` 中啟用安全性功能。
  - 版本不匹配：確保 Kibana 與 Elasticsearch 版本一致。

- **資源參考**：
  - 官方文件：[elastic.co/guide/en/kibana/current](https://www.elastic.co/guide/en/kibana/current/index.html)。
  - 論壇：Elastic Discuss 或 Stack Overflow。
  - 範例資料：透過 Kibana 載入（Stack Management > Kibana > Sample Data）。

本指南可協助您開始使用 Kibana 進行日誌檢查。請從小規模開始：設定本地 ELK 堆疊、擷取範例日誌，並在 Discover 中進行實驗。生產環境建議考慮 Elastic Cloud 以簡化部署。若您有特定環境需求（例如 Docker、AWS），請提供更多細節以獲得客製化建議！