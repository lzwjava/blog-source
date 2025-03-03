---
audio: false
generated: true
lang: hant
layout: post
title: SQuirreL SQL 客戶端及 DB2 資料庫
translated: true
---

要在 SQuirreL SQL Client 中使用您的 IBM DB2 JCC JAR (`db2jcc.jar`) 並連接到 DB2 資料庫，請按照以下詳細步驟進行。此過程涉及在 SQuirreL 中配置 DB2 驅動程序並設置連接別名。

---

### 第 1 步：驗證 JAR 文件
- 確保您擁有正確的 DB2 JDBC 驅動程序 JAR 文件。您提到的文件 `db2jcc.jar` 通常是 IBM DB2 的正確文件，但某些設置可能會使用 `db2jcc4.jar`，具體取決於版本。
- 檢查您的 DB2 安裝是否需要額外的授權文件（例如 `db2jcc_license_cisuz.jar`）。如果需要，請找到此文件，因為在連接時可能需要它以避免與授權相關的錯誤。

---

### 第 2 步：在 SQuirreL SQL Client 中配置 DB2 驅動程序
1. **打開 SQuirreL SQL Client**：
   - 在您的系統上啟動應用程序。

2. **訪問驅動程序標籤**：
   - 在左側面板中，點擊 **驅動程序** 標籤以查看可用的資料庫驅動程序列表。

3. **查找或添加 DB2 驅動程序**：
   - 在列表中查找現有的 DB2 驅動程序（例如 "IBM DB2 App Driver"）。如果配置不正確，可能會標記為紅色 X。
   - 如果存在，您可以修改它。如果不存在，您需要創建一個新的驅動程序：
     - **修改現有驅動程序**：雙擊 DB2 驅動程序條目。
     - **添加新驅動程序**：在驅動程序標籤中點擊 **+** 圖標以打開 "添加驅動程序" 向導。

4. **配置驅動程序設置**：
   - **名稱**：輸入描述性名稱，例如 "IBM DB2 JCC 驅動程序"。
   - **範例 URL**：將其設置為 `jdbc:db2://<host>:<port>/<database>`（您將根據具體資料庫稍後自定義此內容）。
   - **類名**：輸入 `com.ibm.db2.jcc.DB2Driver`（這是 DB2 JDBC 的標準驅動程序類）。

5. **添加 JAR 文件**：
   - 在驅動程序配置窗口中，轉到 **Extra Class Path** 標籤。
   - 點擊 **Add**，然後瀏覽並選擇您的 `db2jcc.jar` 文件的位置。
   - 如果您有授權 JAR（例如 `db2jcc_license_cisuz.jar`），再次點擊 **Add** 並包含它。

6. **保存配置**：
   - 點擊 **OK** 以保存驅動程序設置。DB2 驅動程序應該現在出現在驅動程序標籤中，並標有勾選標記，表示已正確配置。

---

### 第 3 步：創建資料庫別名
1. **切換到別名標籤**：
   - 在左側面板中，點擊 **別名** 標籤，該標籤管理您的資料庫連接。

2. **添加新別名**：
   - 點擊 **+** 圖標以打開 "添加別名" 向導。

3. **配置別名**：
   - **名稱**：為您的連接命名（例如 "我的 DB2 資料庫"）。
   - **驅動程序**：從下拉菜單中選擇您在第 2 步中配置的 DB2 驅動程序（例如 "IBM DB2 JCC 驅動程序"）。
   - **URL**：輸入資料庫的連接 URL，格式為：
     ```
     jdbc:db2://<host>:<port>/<database>
     ```
     將 `<host>`（例如 `localhost` 或您的伺服器的 IP）、`<port>`（例如 `50000`，DB2 的默認端口）和 `<database>`（您的資料庫名稱）替換為您的實際詳細信息。例如：
     ```
     jdbc:db2://localhost:50000/mydb
     ```
   - **用戶名** 和 **密碼**：提供您的 DB2 資料庫憑證。

4. **保存並連接**：
   - 點擊 **OK** 以保存別名。
   - 在別名標籤中，雙擊您的新別名以連接。如果提示，請輸入您的密碼。

---

### 潛在問題及解決方案
- **授權錯誤**：
  - 如果看到類似 "The IBM Data Server for JDBC and SQLJ license was invalid" 的錯誤，請確保授權 JAR（例如 `db2jcc_license_cisuz.jar`）已添加到驅動程序的 Extra Class Path。
- **找不到類錯誤**：
  - 如果 SQuirreL 報告 "Could not find class com.ibm.db2.jcc.DB2Driver"，請驗證：
    - `db2jcc.jar` 文件已正確添加到 Extra Class Path。
    - 類名設置為 `com.ibm.db2.jcc.DB2Driver`，沒有拼寫錯誤。
- **多個 JAR 衝突**：
  - 避免在 Extra Class Path 中包含多個版本的 DB2 JDBC 驅動程序（例如 `db2jcc.jar` 和 `db2jcc4.jar`），因為這可能會導致衝突。僅使用所需的 JAR 文件。
- **不正確的 URL 格式**：
  - 仔細檢查您的連接 URL 語法。格式不正確的 URL（例如缺少端口或資料庫名稱不正確）將阻止連接。

---

按照這些步驟，您應該能夠配置 SQuirreL SQL Client 以使用您的 `db2jcc.jar` 文件並成功連接到您的 DB2 資料庫。如果遇到任何問題，請查看上述故障排除技巧，或確保您的資料庫伺服器可從您的網絡訪問。