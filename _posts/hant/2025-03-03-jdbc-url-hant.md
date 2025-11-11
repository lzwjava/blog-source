---
audio: false
generated: true
lang: hant
layout: post
title: 構建 JDBC URL
translated: true
type: note
---

要為 WebSphere Liberty Profile 中 `server.xml` 檔案內的 `properties.db2.jcc` 元素建構用於連接 DB2 資料庫的 JDBC URL，您需要使用為特定關鍵屬性（如 `databaseName`、`serverName` 和 `portNumber`）提供的值。具體方法如下：

### DB2 的基本 JDBC URL 格式
使用 DB2 JDBC Type 4 驅動程式（在 Liberty Profile 設定中常用）的標準 JDBC URL 格式為：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - 這是使用 Type 4 驅動程式連接 DB2 資料庫的協定識別符，表示直接網路連接。
- **`<serverName>`** - DB2 伺服器的主機名稱或 IP 位址，由 `properties.db2.jcc` 中的 `serverName` 屬性指定。
- **`<portNumber>`** - DB2 實例監聽的連接埠，由 `portNumber` 屬性指定（若未指定，預設通常為 `50000`）。
- **`<databaseName>`** - 要連接的資料庫名稱，由 `databaseName` 屬性指定。

### 建構 URL 的步驟
1. **識別必要屬性**：從 `server.xml` 中的 `properties.db2.jcc` 元素提取 `serverName`、`portNumber` 和 `databaseName` 的值。這些是組成 URL 的基本要素。
2. **組合 URL**：將這些值按照上述格式組合，確保使用正確的分隔符號（伺服器與連接埠之間用 `:`，資料庫名稱前用 `/`）。
3. **處理其他屬性（如果存在）**：如果 `properties.db2.jcc` 包含其他屬性（例如 `currentSchema`、`sslConnection`），有時可以將它們附加到 URL 中，但這取決於屬性的性質。通常，像 `user` 和 `password` 這類屬性出於安全考慮，不會包含在 URL 中，而是在建立連接時單獨傳遞。

### 範例
假設您的 `server.xml` 包含以下 `properties.db2.jcc` 設定：

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

- `user` 和 `password` 不包含在 URL 中；它們通常在使用 JDBC 驅動程式（例如透過 `DataSource` 或 `DriverManager`）獲取連接時單獨提供。

### 包含其他屬性（可選）
如果在 `properties.db2.jcc` 中指定了其他屬性，例如 `currentSchema` 或 `sslConnection`，並且您希望將它們包含在 URL 中（儘管某些屬性更適合在連接屬性中設定），請在資料庫名稱後附加這些屬性，格式為冒號（`:`）後接分號分隔的 `property=value` 鍵值對。例如：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URL 可能變為：

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

但請注意：
- 像 `sslConnection=true` 這樣的屬性通常是在 `Properties` 物件或資料來源設定中設定，而非在 URL 中。
- 請查閱 DB2 JDBC 驅動程式文件，以確認哪些屬性可以在 URL 中使用，哪些需要單獨設定。

### 最終答案
根據您的查詢內容，假設 `properties.db2.jcc` 至少提供了 `databaseName`、`serverName` 和 `portNumber`，則 JDBC URL 的建構格式為：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

請將 `<serverName>`、`<portNumber>` 和 `<databaseName>` 替換為您 `properties.db2.jcc` 設定中的實際值。如果存在其他屬性且打算用於 URL，請以 `:property1=value1;property2=value2;` 的格式附加它們，但通常像 `user`、`password` 和 `sslConnection` 這類屬性會在連接設定中單獨處理。