---
audio: false
generated: true
lang: hant
layout: post
title: 將 Oracle JDBC 驅動程式加入 Squirrel SQL 用戶端
translated: true
type: note
---

要將 Oracle JDBC 驅動程式加入 Squirrel SQL Client，請按照以下詳細步驟操作。此過程涉及配置驅動程式並為您的 Oracle 資料庫設定連線別名。

### 步驟 1：定位所需檔案
您需要 Oracle JDBC 驅動程式檔案，特別是 `ojdbc.jar`。此檔案包含必要的類別，使 Squirrel SQL Client 能夠連線到 Oracle 資料庫。請確保您已下載此檔案（例如從 Oracle 網站或資料庫管理員處取得），並知道其在系統中的位置。

### 步驟 2：啟動 Squirrel SQL Client
在您的電腦上開啟 Squirrel SQL Client 應用程式。

### 步驟 3：存取驅動程式標籤
在 Squirrel SQL Client 介面的左側，找到並點擊 **Drivers** 標籤。此部分允許您管理應用程式可用的 JDBC 驅動程式。

### 步驟 4：新增驅動程式
- 在 Drivers 標籤中，點擊 **"+"** 按鈕以開啟「Add Driver」對話方塊。

### 步驟 5：命名驅動程式
- 在「Add Driver」對話方塊的「Name」欄位中，輸入 **Oracle Thin Driver**。這是一個描述性名稱，用於在 Squirrel SQL Client 中識別 Oracle 驅動程式。

### 步驟 6：加入 `ojdbc.jar` 檔案
- 在「Add Driver」對話方塊中切換到 **Extra Class Path** 標籤。
- 點擊 **Add** 按鈕。
- 瀏覽至系統中 `ojdbc.jar` 檔案的位置，選取它並確認將其加入驅動程式的類別路徑。

### 步驟 7：指定 Java 驅動程式類別
- 在「Class Name」欄位中，輸入 Java 驅動程式類別：**oracle.jdbc.OracleDriver**。這告訴 Squirrel SQL Client 使用 `ojdbc.jar` 檔案中的哪個類別來處理 Oracle 資料庫連線。

### 步驟 8：提供範例 URL
- 您可以選擇性地指定用於連線到 Oracle 資料庫的範例 URL 格式：
  - **透過 SID 連線**：`jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **透過服務名稱連線**：`jdbc:oracle:thin:@//HOST[:PORT]/DB`
- 在後續設定連線時（在別名配置中），將 `HOST`、`PORT` 和 `DB` 替換為實際值。

### 步驟 9：儲存驅動程式配置
- 點擊 **OK** 以儲存驅動程式設定並關閉「Add Driver」對話方塊。「Oracle Thin Driver」現在應該出現在 Drivers 標籤中，並帶有綠色勾號，表示其已正確配置。

### 步驟 10：為您的資料庫建立別名
- 切換到 Squirrel SQL Client 左側的 **Aliases** 標籤。
- 點擊 **"+"** 按鈕以開啟「Add Alias」對話方塊。

### 步驟 11：配置別名
- 在「Add Alias」對話方塊中：
  - **Name**：輸入此連線的名稱（例如「My Oracle DB」）。
  - **Driver**：從下拉選單中選取 **Oracle Thin Driver**。
  - **URL**：輸入您的特定 Oracle 資料庫的連線 URL：
    - 透過 SID：`jdbc:oracle:thin:@HOST[:PORT]:DB`
    - 透過服務名稱：`jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - 將 `HOST`（例如 localhost 或 IP 位址）、`PORT`（預設為 1521）和 `DB`（SID 或服務名稱）替換為您的資料庫詳細資訊。
  - **Username**：輸入資料庫使用者名稱。
  - **Password**：輸入資料庫密碼。

### 步驟 12：測試連線
- 點擊「Add Alias」對話方塊中的 **Test** 按鈕，以驗證 Squirrel SQL Client 是否可以使用提供的詳細資訊連線到您的 Oracle 資料庫。如果成功，您將看到確認訊息。

### 步驟 13：儲存別名
- 如果測試連線成功，點擊 **OK** 以儲存別名。新別名現在將出現在 Aliases 標籤中。

### 步驟 14：連線到資料庫
- 在 Aliases 標籤中，選取您新建立的別名（例如「My Oracle DB」）。
- 點擊 **Connect** 按鈕以建立與您的 Oracle 資料庫的連線。連線成功後，您可以使用 Squirrel SQL Client 開始查詢您的資料庫。

### 關鍵資訊摘要
- **所需檔案**：`ojdbc.jar`
- **Java 驅動程式類別**：`oracle.jdbc.OracleDriver`
- **URL 格式**：
  - SID：`jdbc:oracle:thin:@HOST[:PORT]:DB`
  - 服務名稱：`jdbc:oracle:thin:@//HOST[:PORT]/DB`

按照這些步驟操作，您將成功將 Oracle JDBC 驅動程式加入 Squirrel SQL Client，並配置好與 Oracle 資料庫的連線。請確保所有詳細資訊（檔案路徑、URL、憑證）準確無誤，以避免連線問題。