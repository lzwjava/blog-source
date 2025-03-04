---
audio: false
generated: true
lang: hant
layout: post
title: 將 Oracle JDBC 驅動程式添加到 Squirrel SQL 客戶端
translated: true
---

要將 Oracle JDBC 驅動程式添加到 Squirrel SQL Client，請按照以下詳細步驟進行。此過程涉及配置驅動程式並為您的 Oracle 資料庫設置別名。

### 第 1 步：定位所需文件
您需要 Oracle JDBC 驅動程式文件，具體是 `ojdbc.jar`。此文件包含必要的類，以使 Squirrel SQL Client 能夠連接到 Oracle 資料庫。請確保您已下載此文件（例如，從 Oracle 網站或您的資料庫管理員處）並知道其在系統中的位置。

### 第 2 步：啟動 Squirrel SQL Client
在您的電腦上打開 Squirrel SQL Client 應用程式。

### 第 3 步：訪問驅動程式標籤
在 Squirrel SQL Client 介面的左側，找到並點擊 **驅動程式** 標籤。此部分允許您管理應用程式可用的 JDBC 驅動程式。

### 第 4 步：添加新驅動程式
- 在驅動程式標籤中，點擊 **"+"** 按鈕以打開“添加驅動程式”對話框。

### 第 5 步：命名驅動程式
- 在“添加驅動程式”對話框的“名稱”欄位中，輸入 **Oracle Thin Driver**。這是一個描述性名稱，用於在 Squirrel SQL Client 中識別 Oracle 驅動程式。

### 第 6 步：添加 `ojdbc.jar` 文件
- 在“添加驅動程式”對話框中切換到 **Extra Class Path** 標籤。
- 點擊 **Add** 按鈕。
- 導航到系統中的 `ojdbc.jar` 文件位置，選擇它並確認將其添加到驅動程式的類路徑。

### 第 7 步：指定 Java 驅動程式類
- 在“類名”欄位中，輸入 Java 驅動程式類： **oracle.jdbc.OracleDriver**。這告訴 Squirrel SQL Client 從 `ojdbc.jar` 文件中使用哪個類來處理 Oracle 資料庫連接。

### 第 8 步：提供示例 URL
- 您可以選擇指定一個用於連接到 Oracle 資料庫的示例 URL 格式：
  - **通過 SID 連接**： `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **通過服務名稱連接**： `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- 在後來的別名配置中設置連接時，將 `HOST`、`PORT` 和 `DB` 替換為實際值。

### 第 9 步：保存驅動程式配置
- 點擊 **OK** 以保存驅動程式設置並關閉“添加驅動程式”對話框。“Oracle Thin Driver” 現在應該出現在驅動程式標籤中，並顯示綠色勾號，表示已正確配置。

### 第 10 步：為您的資料庫創建別名
- 在 Squirrel SQL Client 左側切換到 **別名** 標籤。
- 點擊 **"+"** 按鈕以打開“添加別名”對話框。

### 第 11 步：配置別名
- 在“添加別名”對話框中：
  - **名稱**：輸入此連接的名稱（例如，“My Oracle DB”）。
  - **驅動程式**：從下拉菜單中選擇 **Oracle Thin Driver**。
  - **URL**：輸入特定 Oracle 資料庫的連接 URL：
    - 通過 SID： `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - 通過服務名稱： `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - 將 `HOST`（例如 localhost 或 IP 地址）、`PORT`（默認值為 1521）和 `DB`（SID 或服務名稱）替換為您的資料庫的詳細信息。
  - **用戶名**：輸入資料庫用戶名。
  - **密碼**：輸入資料庫密碼。

### 第 12 步：測試連接
- 在“添加別名”對話框中點擊 **Test** 按鈕，以驗證 Squirrel SQL Client 是否能夠使用提供的詳細信息連接到您的 Oracle 資料庫。如果成功，您將看到確認消息。

### 第 13 步：保存別名
- 如果測試連接成功，點擊 **OK** 以保存別名。新別名現在應該出現在別名標籤中。

### 第 14 步：連接到資料庫
- 在別名標籤中選擇您新創建的別名（例如，“My Oracle DB”）。
- 點擊 **Connect** 按鈕以建立與 Oracle 資料庫的連接。連接後，您可以開始使用 Squirrel SQL Client 查詢您的資料庫。

### 關鍵信息摘要
- **所需文件**： `ojdbc.jar`
- **Java 驅動程式類**： `oracle.jdbc.OracleDriver`
- **URL 格式**：
  - SID： `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - 服務名稱： `jdbc:oracle:thin:@//HOST[:PORT]/DB`

按照這些步驟，您將成功將 Oracle JDBC 驅動程式添加到 Squirrel SQL Client，並配置與 Oracle 資料庫的連接。請確保所有詳細信息（文件路徑、URL、憑證）準確，以避免連接問題。