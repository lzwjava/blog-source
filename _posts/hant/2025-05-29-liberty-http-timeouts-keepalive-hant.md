---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 設定Liberty HTTP逾時與保持連線
translated: true
type: note
---

### 設定 Keep-Alive 設定

WebSphere Liberty Profile 透過 `server.xml` 中的 `<httpEndpoint>` 元素處理 HTTP keep-alive 連線。此元素控制持久連線以減少延遲和負擔。

- **keepAlive**：啟用或停用 keep-alive。設定為 `true`（預設值）允許在單一連線上進行多個請求。
- **keepAliveTimeout**：定義伺服器在關閉閒置 keep-alive 連線前的等待時間（以秒為單位）。預設為 30 秒。

要進行配置，請在 `server.xml` 的 `<server>` 根目錄下新增或修改 `<httpEndpoint>` 元素。範例：

```xml
<server>
    <!-- 其他配置 -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        keepAlive="true"
        keepAliveTimeout="60"/>
</server>
```

變更生效需重新啟動伺服器。TCP 層級的 keep-alive 可透過 `<tcpOptions>` 調整（如有需要），但 HTTP keep-alive 更常見於網路流量處理。

### 設定 Timeout 設定

Liberty 的 `server.xml` 中的逾時設定主要與 `<httpEndpoint>` 下的連線逾時相關，控制伺服器等待操作的時間。這些設定適用於 HTTP 通訊。

- **connectionTimeout**：建立新連線的最大時間（以秒為單位）。預設為 60 秒。
- **readTimeout**：在請求期間等待傳入資料的最大時間（以秒為單位）。預設為 60 秒。
- **writeTimeout**：等待傳出資料傳送的最大時間（以秒為單位）。預設為 60 秒。

工作階段特定的逾時設定（例如用於網路應用程式工作階段）是在 `web.xml` 或透過 `server.xml` 中的 `<sessionManager>` 配置，而非直接在 `<httpEndpoint>` 中設定。

範例 `server.xml` 配置：

```xml
<server>
    <!-- 其他配置 -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        connectionTimeout="30"
        readTimeout="120"
        writeTimeout="120"/>
</server>
```

請根據應用程式需求調整數值，例如針對慢速網路或長時間運行的請求設定較高的逾時值。監控日誌以檢查逾時相關錯誤，並在變更後重新啟動伺服器。詳細資訊請參閱 [IBM Liberty 關於 HTTP 端點的說明文件](https://www.ibm.com/docs/en/was-liberty/23.0.0?topic=configuration-http-endpoint-running-liberty)。