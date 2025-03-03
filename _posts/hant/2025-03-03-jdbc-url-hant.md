---
audio: false
generated: true
lang: hant
layout: post
title: JDBC URL 結構
translated: true
---

要構建一個用於連接到 DB2 資料庫的 JDBC URL，基於 `server.xml` 文件中的 `properties.db2.jcc` 元素，您需要使用某些關鍵屬性（如 `databaseName`、`serverName` 和 `portNumber`）提供的值。以下是如何進行的：

### DB2 的基本 JDBC URL 格式
使用 DB2 JDBC Type 4 驅動程序（通常在 Liberty Profile 設置中使用）的標準 JDBC URL 格式如下：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - 這是使用 Type 4 驅動程序的 DB2 資料庫的協議標識符，表示直接網絡連接。
- **`<serverName>`** - DB2 伺服器的主機名或 IP 地址，由 `properties.db2.jcc` 中的 `serverName` 屬性指定。
- **`<portNumber>`** - DB2 實例正在監聽的端口，由 `portNumber` 屬性指定（如果未指定，通常默認為 `50000`）。
- **`<databaseName>`** - 要連接的資料庫的名稱，由 `databaseName` 屬性指定。

### 构建 URL 的步驟
1. **識別所需屬性**：從 `server.xml` 中的 `properties.db2.jcc` 元素中提取 `serverName`、`portNumber` 和 `databaseName` 的值。這些是 URL 中所需的基本組件。
2. **組合 URL**：將這些值組合到上述格式中，確保正確的分隔符（伺服器和端口之間使用 `:`，資料庫名稱之前使用 `/`）。
3. **處理其他屬性（如果有）**：如果 `properties.db2.jcc` 包含其他屬性（例如 `currentSchema`、`sslConnection`），有時可以將它們附加到 URL 中，但這取決於它們的性質。通常，像 `user` 和 `password` 這樣的屬性在建立連接時會單獨傳遞，而不是在 URL 中，出於安全原因。

### 範例
假設您的 `server.xml` 包含以下 `properties.db2.jcc` 配置：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

JDBC URL 將是：

```
jdbc:db2://localhost:50000/SAMPLE
```

- `user` 和 `password` 不包含在 URL 中；它們通常在通過 JDBC 驅動程序獲取連接時單獨提供（例如，通過 `DataSource` 或 `DriverManager`）。

### 包含其他屬性（可選）
如果 `properties.db2.jcc` 中指定了其他屬性，例如 `currentSchema` 或 `sslConnection`，並且您希望將它們包含在 URL 中（儘管某些屬性可能更適合設置在連接屬性中），則在資料庫名稱後面附加它們，使用冒號 (`:`) 後面跟著分號分隔的 `property=value` 對。例如：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URL 可能會變成：

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

然而：
- 如 `sslConnection=true` 這樣的屬性通常在 `Properties` 對象或數據源配置中設置，而不是在 URL 中。
- 檢查 DB2 JDBC 驅動程序文檔，確認哪些屬性在 URL 中有效，哪些屬性需要單獨配置。

### 最終答案
在您的查詢的情境下，假設 `properties.db2.jcc` 提供至少 `databaseName`、`serverName` 和 `portNumber`，JDBC URL 將構建為：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

用您的 `properties.db2.jcc` 配置中的實際值替換 `<serverName>`、`<portNumber>` 和 `<databaseName>`。如果有其他屬性存在並且打算包含在 URL 中，則附加為 `:property1=value1;property2=value2;`，但通常，像 `user`、`password` 和 `sslConnection` 這樣的屬性在連接設置中單獨處理。