---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 自由日誌輪替配置指南
translated: true
type: note
---

以下是簡短說明，以及可貼到 `server.xml` 的範例。

### Liberty 日誌輪替運作原理

* **會輪替的檔案：** `messages.log` 與 `trace.log`。
  輪替可基於**檔案大小**及/或**時間**。([openliberty.io][1])
* **不會輪替的檔案：** `console.log`（它只是 stdout/stderr）。您可以改為減少或停用它。([openliberty.io][2], [IBM][3])
* **設定位置：** `server.xml` 中的 `<logging …/>` 元素。（您也可以在 `bootstrap.properties`/環境變數中設定相同值，若需在 `server.xml` 載入*前*套用。）([openliberty.io][2])
* **存取日誌：** HTTP 存取日誌在 `httpAccessLogging` / `accessLogging` 下有**獨自**的基於時間的輪替設定。([openliberty.io][4])
* **同時使用大小與時間：** 現代 Liberty 除了傳統的基於大小的選項外，也支援基於時間的輪替，因此您可以擇一或同時使用（`console.log` 除外）。([IBM][5])

---

### 常見的 `server.xml` 設定範例

#### 1) 基於大小的輪替（傳統）

最多保留 10 個檔案，每個最大 256 MB。

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

效果：當 `messages.log` 或 `trace.log` 超過 256 MB 時，Liberty 會將其輪替為時間戳記檔案，並最多保留 10 個此類檔案。（不影響 `console.log`。）([openliberty.io][1])

#### 2) 基於時間的輪替（例如，每日午夜）

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

效果：`messages.log` 和 `trace.log` 每天於 00:00 輪替。您也可以使用分鐘 (`m`) 或小時 (`h`)，例如 `30m` 或 `6h`。([openliberty.io][2])

#### 3) 合併大小與時間輪替（典型生產環境）

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

效果：輪替條件以**先達到者為準**（大小或排程），並保留 14 個檔案的歷史記錄。([IBM][5])

#### 4) 控制或停用 `console.log` 增長

`console.log` 無法輪替；減少或關閉它，並依賴 `messages.log`。

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

注意：關閉 console 會停止 Liberty 自身對 `console.log` 的日誌複製，但 JVM 可能仍會將如 `-verbose:gc` 的內容寫入 stdout/stderr。([openliberty.io][2])

#### 5) 名稱/格式微調（可選）

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON 便於將日誌傳送至日誌堆疊；若不需要，請保留預設值。([openliberty.io][1])

---

### HTTP 存取日誌（與上述分開）

啟用存取日誌記錄並於每日午夜輪替：

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

（或直接將 `rolloverStartTime`/`rolloverInterval` 放在 `httpEndpoint` 的 `<accessLogging …/>` 子元素上。）([openliberty.io][4])

---

### 快速檢查清單

* 使用 **`maxFileSize` + `maxFiles`** 進行基於大小的輪替。([openliberty.io][1])
* 使用 **`rolloverStartTime` + `rolloverInterval`** 進行基於時間的輪替。([openliberty.io][2])
* **不要期望 `console.log` 會輪替**；若想避免過大的 console 檔案，請設定 `consoleLogLevel="OFF"` 和 `copySystemStreams="false"`。([openliberty.io][2], [IBM][3])

如果您提供當前的 `server.xml` 片段或保留目標（例如「保留約 7 天」或「上限為 2 GB」），我將為您調整確切數值。

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."