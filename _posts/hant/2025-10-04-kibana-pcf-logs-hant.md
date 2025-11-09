---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: PCF 日誌的 Kibana 設定
translated: true
type: note
---

看起來「kabana」很可能是指 **Kibana**——Elasticsearch 的開源資料視覺化儀表板。在 **Pivotal Cloud Foundry (PCF)**（現已重新品牌化為 VMware Tanzu Application Service）的環境中，Kibana 通常透過平台的日誌系統（Loggregator）用於搜尋、視覺化和分析日誌。PCF 本身並不原生獨立執行 Kibana，而是透過 **Log Search** 磚/服務進行整合，該服務將日誌儲存在 Elasticsearch 中並提供 Kibana 進行查詢。

如果這不是您所指的內容，請隨時澄清！以下我將說明如何設定並使用 Kibana 與 PCF 日誌。這假設您是具有 PCF Ops Manager 存取權限的管理員，且擁有正在運行的 PCF 部署（版本 2.0+）。請注意，PCF 的日誌功能已有演進；請查閱您版本的具體文件以獲取最新資訊。

### 先決條件
- **PCF 版本**：Log Search（含 Kibana）在 PCF 2.2+ 中可用。早期版本使用獨立的「ELK」（Elasticsearch、Logstash、Kibana）磚。
- **磚/服務**：確保您已透過 Pivotal Network（現為 Broadcom Support Portal）安裝 **Elastic Runtime** 磚（用於 Loggregator）和 **Log Search** 磚。
- **存取權限**：Ops Manager 和 PCF CLI（cf 命令列工具）中的管理員權限。
- **資源**：分配足夠的資源（例如，根據日誌量分配 4-8 GB RAM 給 Log Search）。

### 步驟 1：在 Ops Manager 中安裝並設定 Log Search 磚
Log Search 磚將 PCF 日誌（來自應用程式、平台和系統元件）轉發到 Elasticsearch，使其可透過 Kibana 進行搜尋。

1. **下載並匯入磚**：
   - 登入 Broadcom Support Portal（前身為 Pivotal Network）。
   - 下載 **Log Search for PCF** 磚（例如，與您的 PCF 版本匹配的版本）。
   - 在 Ops Manager（網頁 UI）中，前往 **Catalog** > **Import a Product** 並上傳該磚。

2. **設定磚**：
   - 在 Ops Manager 中，前往 **Elastic Runtime** 磚 > **Loggregator** 標籤頁：
     - 啟用 **Loggregator forwarding to external systems**（例如，如果需要，設定 syslog 或 HTTP 轉發，但對於 Log Search，這是內部轉發）。
     - 設定 **Loggregator log retention** 為一個值，例如 5-30 天。
   - 前往 **Log Search** 磚：
     - **Assign Availability Zones**：選擇至少一個 AZ 以實現高可用性。
     - **Elasticsearch Configuration**：
       - 設定執行個體數量（生產環境建議從 3 開始）。
       - 設定儲存空間（例如，100 GB 持久磁碟）。
       - 啟用安全性（例如，為 Elasticsearch 啟用 TLS）。
     - **Kibana Configuration**：
       - 啟用 Kibana（它是捆綁的）。
       - 設定管理員憑證（使用者名稱/密碼）。
     - **Loggregator Integration**：
       - 設定每秒最大日誌行數（例如，根據您的負載設定 1000-5000）。
       - 定義索引模式（例如，保留日誌 7-30 天）。
     - **Networking**：透過路由公開 Kibana（例如 `kibana.YOUR-PCF-DOMAIN.com`）。
   - 點擊 **Apply Changes** 進行部署。這可能需要 30-60 分鐘。

3. **驗證部署**：
   - 執行 `cf tiles` 或在 Ops Manager 中檢查是否成功。
   - 透過 SSH 連接到 Log Search VM（使用 BOSH CLI：`bosh ssh log-search/0`）並確認 Elasticsearch 正在運行（`curl localhost:9200`）。

### 步驟 2：存取 Kibana
部署完成後：

1. **透過 PCF Apps Manager (GUI)**：
   - 登入 Apps Manager（例如 `https://apps.YOUR-PCF-DOMAIN.com`）。
   - 搜尋「Log Search」服務執行個體（它會自動建立一個）。
   - 點擊服務執行個體 > **Logs** 標籤頁。這將開啟嵌入式 Kibana 視圖以進行快速日誌搜尋。

2. **直接存取 Kibana**：
   - 前往在磚中設定的 Kibana URL（例如 `https://kibana.YOUR-PCF-DOMAIN.com`）。
   - 使用您設定的管理員憑證登入。
   - 如果使用自訂網域，請確保 DNS 正確指向且路由已註冊（透過 `cf routes` 驗證）。

3. **CLI 存取（可選）**：
   - 使用 `cf logs APP-NAME` 獲取基本日誌，但對於進階查詢，請使用 Kibana UI 或 API。
   - 將 Log Search 綁定到您的應用程式：`cf create-service log-search standard my-log-search`，然後 `cf bind-service APP-NAME my-log-search`。

### 步驟 3：使用 Kibana 處理 PCF 日誌
Kibana 提供了一個基於網頁的介面，用於查詢、篩選和視覺化來自 PCF 元件的日誌（例如，應用程式日誌、Diego cells、Gorouter 等）。

1. **基本導覽**：
   - **Discover 標籤頁**：使用 Lucene 查詢語法搜尋日誌。
     - 範例：在特定應用程式中搜尋錯誤：`source_id:APP:your-app-name AND json.message:ERROR`。
     - 可用欄位：`timestamp`、`source_id`（例如 `APP:your-app`、`RTR:router`）、`message`、`deployment` 等。
   - **Visualize 標籤頁**：建立圖表的儀表板（例如，隨時間變化的日誌量、錯誤率）。
     - 範例視覺化：按 source_id 顯示的日誌長條圖。
   - **Dashboard 標籤頁**：儲存和分享預先建立的儀表板（Log Search 包含 PCF 日誌的預設儀表板）。

2. **常見查詢和提示**：
   - **按應用程式篩選**：`source_id:APP:your-app-name`（替換為實際的應用程式 GUID 或名稱）。
   - **按時間篩選**：使用時間選擇器（例如，過去 24 小時）。
   - **系統日誌**：`source_id:DEA`（用於 Diego cells）或 `source_id:LOGGREGATOR`。
   - **匯出日誌**：從 Discover 下載為 CSV/JSON。
   - **進階**：使用 Kibana 的 Dev Tools（控制台）直接查詢 Elasticsearch，例如：
     ```
     GET /logstash-*/_search
     {
       "query": { "match": { "message": "error" } },
       "sort": [ { "timestamp": { "order": "desc" } } ]
     }
     ```
   - **保留和索引**：日誌按天索引（例如 `logstash-YYYY.MM.DD`）。在磚中配置滾動更新以管理儲存空間。

3. **日誌疑難排解**：
   - **沒有日誌顯示？** 檢查 Loggregator 中的轉發規則（Ops Manager > Elastic Runtime > Loggregator）。確保應用程式正在發出日誌（例如，在 Node.js 中透過 `console.log`）。
   - **效能問題？** 擴展 Elasticsearch 執行個體或調整日誌速率限制。
   - **安全性**：在 Log Search 中啟用 UAA 整合以實現 Kibana 的單一登入。
   - **錯誤**：使用 `cf logs log-search` 或 Ops Manager errand 日誌檢查 PCF 日誌。

### 其他資源
- **官方文件**：VMware Tanzu 關於 [Log Search](https://docs.vmware.com/en/VMware-Tanzu-Application-Service/10.0/tas/GUID-log-search-index.html) 的文件（請搜尋您的版本）。
- **CLI 工具**：如果需要，安裝 `uaac` 用於 UAA 認證，或使用 `cf curl` 進行 API 存取。
- **替代方案**：對於更簡單的需求，使用 PCF 內建的 **Log Cache**（cf CLI：`cf tail APP-NAME`）或透過 syslog 轉發與外部工具（如 Splunk）整合。
- **升級**：如果您使用的是舊版 PCF，請遷移到 ELK 磚或聯繫 Broadcom 支援。

如果您能提供更多詳細資訊（例如，您的 PCF 版本、錯誤訊息或具體使用案例），我可以進一步完善這些說明！