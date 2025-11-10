---
audio: false
generated: true
lang: hant
layout: post
title: 配置 Logback 自訂日誌格式
translated: true
type: note
---

要達成您提供的日誌格式，您需要配置 `logback.xml` 檔案。關鍵在於在 appender 中使用 `PatternLayout` 並正確設定 `pattern` 屬性。

以下是您所需日誌格式中各組件的解析，以及如何將它們對應到 Logback 模式轉換器：

* **`2025-06-15T01:37:52.452+08:00`**：這是時間戳記。您將使用 `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`。
    * `yyyy-MM-dd'T'HH:mm:ss.SSS`：包含毫秒的日期和時間。
    * `XXX`：ISO 8601 標準的 UTC 時區偏移（例如 `+08:00`）。
* **`DEBUG`**：這是日誌級別。您將使用 `%-5p`（左對齊，5 個字元寬度）。
* **`302244`**：這是處理序 ID。Logback 並未在其標準轉換器中直接公開處理序 ID。然而，它*確實*公開了**執行緒 ID**（`%t` 或 `%thread`）。如果範例中的 "302244" 實際上是執行緒 ID（這在應用程式日誌中很常見），那麼 `%thread` 就是您需要的。如果它*必須*是作業系統處理序 ID，您可能需要自訂的 Logback 轉換器，或者如果您的環境允許，可以使用系統屬性。對於典型的 Spring Boot 應用程式，這通常是執行緒 ID。在此範例中，我將假設它是執行緒 ID。
* **`---`**：一個字面字串。
* **`[nio-8090-exec-1]`**：這是執行緒名稱。您將使用 `[%thread]`，或者如果您希望它是固定寬度，可以使用 `%-40.40thread`。
* **`o.s.w.s.m.m.a.HttpEntityMethodProcessor`**：這是記錄器名稱（通常是完整類別名稱）。您將使用 `%-40.40logger{39}` 來取得右對齊、最多 39 個字元的截斷記錄器名稱。
* **`:`**：一個字面冒號。
* **`Writing ["{"vnstatversion":"2.9","jsonversion":"2","interfaces":[{"name":"enp4s0","alias":"","created":{"date" (truncated)..."]`**：這是日誌訊息。您將使用 `%msg%n`。

以下是一個範例 `logback.xml` 配置，應該能產生非常相似的輸出：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight(%-5p) %thread --- [%thread] %-40.40logger{39} : %msg%n</pattern>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>

    <logger name="org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor" level="DEBUG"/>
    <logger name="org.springframework.web.servlet.DispatcherServlet" level="DEBUG"/>

</configuration>
```

**`pattern` 的解釋：**

* `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`：採用 ISO 8601 格式的日期和時間，包含毫秒和時區偏移。
* `%highlight(%-5p)`：這將輸出日誌級別（例如 DEBUG、INFO），左對齊，5 個字元寬度，並且如果您輸出到控制台，Logback 會嘗試對其進行色彩標記。
* `%thread`：記錄日誌事件的執行緒名稱。（如果您需要處理序 ID，會比較複雜，但對於 Spring 應用程式，執行緒 ID 通常是這裡相關的內容）。
* `---`：一個字面字串分隔符。
* `[%thread]`：用方括號括起來的執行緒名稱。
* `%-40.40logger{39}`：記錄器的名稱（通常是類別名稱）。
    * `%-40`：左對齊並填充至 40 個字元。
    * `.40logger`：如果記錄器名稱超過 40 個字元，則進行截斷。
    * `{39}`：這告訴 Logback 最多顯示記錄器名稱的 39 個字元，從套件名稱的末尾開始（例如，如果 `o.s.w.s.m.m.a.HttpEntityMethodProcessor` 能夠容納，則保持原樣，或者如果從開頭截斷，則可能變成 `...HttpEntityMethodProcessor`）。您可以調整此數字。
* ` :  `：一個字面冒號和空格。
* `%msg%n`：實際的日誌訊息，後接換行。

**重要注意事項：**

1.  **放置位置：** 將此 XML 儲存為 `logback.xml`，並置於您 Spring Boot 專案的 `src/main/resources` 目錄中。
2.  **處理序 ID 與執行緒 ID：** 如前所述，Logback 的標準模式轉換器並不直接公開作業系統處理序 ID。如果 `302244` *必須*是處理序 ID，您通常需要實作自訂的 `PatternLayoutConverter`，或者在啟動時設定一個系統屬性，然後在您的 logback pattern 中引用它。然而，對於大多數應用程式日誌記錄，執行緒 ID（`%thread`）已經足夠，並且通常在此位置使用。
3.  **Spring Boot 預設值：** 如果您沒有提供自訂配置，Spring Boot 通常會提供其預設的 Logback 配置。透過將 `logback.xml` 放在 `src/main/resources` 中，您將覆寫預設配置。
4.  **記錄器級別：** 如果您想看到特定記錄器（如 `HttpEntityMethodProcessor` 和 `DispatcherServlet`）的 DEBUG 訊息，請確保將它們的級別設定為 `DEBUG`。如果根級別是 `INFO`，那麼預設情況下，除非您為特定記錄器明確設定級別，否則不會顯示 DEBUG 訊息。

此配置應該能讓您非常接近所需的日誌格式。