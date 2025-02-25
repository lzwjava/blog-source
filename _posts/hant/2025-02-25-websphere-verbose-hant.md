---
audio: true
lang: hant
layout: post
title: 詳細日誌記錄在 WebSphere Liberty Server
translated: true
---

關於您對 WebSphere Liberty Profile (WLP) 中 `server` 命令的詳細日誌選項的查詢，讓我們澄清 `server` 命令的功能以及如何控制其詳細程度。

WLP 中的 `server` 命令用於管理伺服器實例，包括 `start`、`stop`、`run` 或 `status` 等操作。例如：

- `server start <serverName>` 會在後台啟動伺服器，並將輸出重定向到日誌文件（例如 `logs/console.log`）。
- `server run <serverName>` 會在前台啟動伺服器，並直接在終端顯示輸出。

您的問題提到 `server` 命令的「詳細日誌選項」，這可能意味著命令本身的較詳細輸出或其管理的伺服器的較詳細日誌。經過探索，顯然 `server` 命令沒有直接的旗標（如 `--verbose` 或 `-v`）來增加其自身輸出的詳細程度。相反，詳細程度與伺服器的日誌行為有關，這可以在調用命令時影響。

### 啟用詳細日誌
在 WLP 中，日誌的詳細程度是通過伺服器的日誌配置來控制的，而不是直接通過 `server` 命令的旗標。以下是如何啟用詳細日誌的方法：

#### 1. **在 `server.xml` 中配置日誌**
啟用詳細日誌的主要方法是調整伺服器的 `server.xml` 文件中的 `<logging>` 元素，通常位於 `<WLP_HOME>/usr/servers/<serverName>/`。您可以設置詳細的追蹤規範來增加日誌的詳細程度。例如：

```xml
<logging traceSpecification="*=all" />
```

- `*=all` 啟用所有追蹤點，使日誌非常詳細（對於調試非常有用）。
- 如果需要更有針對性的詳細程度，可以指定組件，例如 `*=info:com.example.*=debug`，將默認級別設置為 `info`，但對於 `com.example` 包設置為 `debug`。

其他有用的屬性包括：
- `logLevel`：設置一般日誌級別（例如 `INFO`、`DEBUG`、`TRACE`）。
- `consoleLogLevel`：控制寫入 `console.log` 或終端的消息級別（例如 `DEBUG` 或 `TRACE`）。

具體的控制台級別示例：
```xml
<logging consoleLogLevel="DEBUG" traceSpecification="*=audit" />
```

當您運行 `server start` 時，日誌（包括詳細輸出）將寫入 `logs/console.log`。使用 `server run` 時，這些詳細輸出將直接顯示在您的終端。

#### 2. **使用環境變量**
您還可以通過環境變量來控制日誌的詳細程度，這些變量可以覆蓋或補充 `server.xml` 設置。例如，在運行 `server` 命令之前設置 `WLP_LOGGING_CONSOLE_LOGLEVEL` 變量：

```bash
export WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG
server start <serverName>
```

- 這將控制台日誌級別設置為 `DEBUG`，確保較詳細的輸出。
- 有效級別包括 `INFO`、`DEBUG`、`FINE`、`FINER`、`FINEST` 等。

對於 `server run`，這將使終端輸出更詳細；對於 `server start`，這將影響 `console.log`。

#### 3. **JVM 特定的詳細選項**
如果您對特定的詳細輸出感興趣，例如垃圾回收日誌，可以添加 JVM 選項（儘管這與 `server` 命令本身無關，而是與伺服器運行時相關）。將 `-verbose:gc` 添加到 `<WLP_HOME>/usr/servers/<serverName>/` 中的 `jvm.options` 文件中，或者通過 `server.xml` 包含它：

```xml
<jvmEntries verbose="gc" />
```

這將生成與 GC 相關的日誌，通常在 `console.log` 或使用 `server run` 時的終端中。

### 這與 `server` 命令的關係
- **沒有直接的 `--verbose` 選項**：`server` 命令本身（例如 `server start`）沒有 `--verbose` 或類似的旗標來詳細說明其執行步驟，超出基本狀態消息（例如「伺服器已啟動」）。
- **伺服器日誌控制詳細程度**：您看到的詳細程度取決於伺服器的日誌配置。使用 `server run` 可以在終端中實時觀察日誌，或者在 `server start` 後檢查日誌文件。

例如：
- 使用 `<logging traceSpecification="*=all"/>` 在 `server.xml` 中，運行 `server run <serverName>` 將在終端中顯示詳細日誌。
- 使用 `server start <serverName>`，相同的詳細程度將顯示在 `logs/console.log` 中。

### 建議
要在使用 `server` 命令時實現詳細日誌：
1. 編輯 `server.xml` 以包含詳細的 `traceSpecification`（例如 `*=all` 以獲得最大詳細程度或特定級別如 `*=debug`）。
2. 或者，在環境中設置 `WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG`。
3. 使用 `server run` 直接查看詳細輸出，或者使用 `server start` 並檢查 `logs/console.log`。

這種方法確保您獲得所需的詳細日誌，並根據您的調試或監控需求進行調整。

如果您指的是更具體的內容（例如命令執行的詳細程度而不是伺服器日誌），請隨時澄清！否則，按照上述方法配置伺服器的日誌是在 WLP 中使用 `server` 命令啟用詳細日誌的標準方法。