---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure Database for MySQL 靈活伺服器指南
translated: true
type: note
---

Azure Database for MySQL 是由 MySQL 社群版本提供技術支援的全受管關聯式資料庫服務。它會處理備份、修補程式和監視等日常工作，讓您能專注於應用程式。建議的部署選項是 **Flexible Server**，它比舊版的單一伺服器（現已逐步淘汰）提供更多組態選項和更佳效能。

本指南涵蓋建立伺服器、連線至伺服器及執行基本操作。為求簡便，本指南以 Azure 入口網站為基礎。

## 必要條件
- 有效的 Azure 訂用帳戶（如有需要，請在 [azure.microsoft.com](https://azure.microsoft.com/free/) 建立一個）。
- 可存取 Azure 入口網站 (portal.azure.com)。
- 對 MySQL 概念有基本認識。
- 連接埠 3306 的輸出網路存取權（MySQL 的預設值）。
- 已安裝 MySQL Workbench 以供連線（請從 [mysql.com](https://dev.mysql.com/downloads/workbench/) 下載）。

## 步驟 1：在 Azure 入口網站中建立 Flexible Server
請遵循以下步驟來佈建您的伺服器。

1. 登入 [Azure 入口網站](https://portal.azure.com)。

2. 在頂端搜尋列中搜尋「Azure Database for MySQL Flexible Servers」並選取它。

3. 按一下 **建立** 以啟動精靈。

4. 在 **基本** 索引標籤上，進行以下設定：
   - **訂用帳戶**：選取您的訂用帳戶。
   - **資源群組**：建立新的資源群組（例如 `myresourcegroup`）或選擇現有的。
   - **伺服器名稱**：唯一名稱（例如 `mydemoserver`），3-63 個字元，小寫字母/數字/連字號。完整主機名稱將為 `<名稱>.mysql.database.azure.com`。
   - **區域**：選擇最接近您使用者的區域。
   - **MySQL 版本**：8.0（最新主要版本）。
   - **工作負載類型**：開發（用於測試；生產環境請使用小型/中型）。
   - **計算 + 儲存體**：高載層，Standard_B1ms (1 個 vCore)，10 GiB 儲存體，100 IOPS，7 天備份。根據需求調整（例如，遷移時增加 IOPS）。
   - **可用性區域**：無偏好（或符合您應用程式的區域）。
   - **高可用性**：開始時停用（生產環境請啟用區域備援）。
   - **驗證**：MySQL 和 Microsoft Entra（以獲得彈性）。
   - **管理員使用者名稱**：例如 `mydemouser`（不能是 root/admin 等，最多 32 個字元）。
   - **密碼**：強式密碼（8-128 個字元，混合大寫/小寫/數字/符號）。

5. 切換至 **網路功能** 索引標籤：
   - **連線方法**：公用存取（為求簡便；生產環境安全性請使用私人 VNet）。
   - **防火牆規則**：新增目前用戶端 IP（或允許 Azure 服務）。之後無法變更此設定。

6. 在 **檢閱 + 建立** 上檢閱設定，然後按一下 **建立**。部署需要 5-10 分鐘。請透過通知監視。

7. 完成後，請釘選到儀表板並前往資源的 **概觀** 頁面。預設資料庫包括 `information_schema`、`mysql` 等。

## 步驟 2：連線至您的伺服器
使用 MySQL Workbench 進行 GUI 連線。（替代方案：Azure Data Studio、mysql CLI 或 Azure Cloud Shell。）

1. 在入口網站中，前往您伺服器的 **概觀** 並記下：
   - 伺服器名稱（例如 `mydemoserver.mysql.database.azure.com`）。
   - 管理員使用者名稱。
   - 如有需要，請重設密碼。

2. 開啟 MySQL Workbench。

3. 按一下 **新增連線**（或編輯現有連線）。

4. 在 **參數** 索引標籤中：
   - **連線名稱**：例如 `Demo Connection`。
   - **連線方法**：標準 (TCP/IP)。
   - **主機名稱**：完整伺服器名稱。
   - **連接埠**：3306。
   - **使用者名稱**：管理員使用者名稱。
   - **密碼**：輸入並儲存在保存庫中。

5. 按一下 **測試連線**。如果失敗：
   - 請確認入口網站中的詳細資料。
   - 確保防火牆允許您的 IP。
   - 強制執行 TLS/SSL (TLS 1.2)；如有需要，請從 [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) 下載 CA 憑證並在 Workbench 中繫結（在 SSL 索引標籤下：使用 SSL > 需要並指定 CA 檔案）。

6. 按一下 **確定** 以儲存。雙擊連線圖格以開啟查詢編輯器。

## 步驟 3：建立及管理資料庫
連線後，可透過入口網站或用戶端管理資料庫。

### 透過 Azure 入口網站：
1. 在您伺服器的頁面上，從左側功能表中選取 **資料庫**。
2. 按一下 **+ 新增**：
   - **資料庫名稱**：例如 `testdb`。
   - **字元集**：utf8（預設值）。
   - **定序**：utf8_general_ci。
3. 按一下 **儲存**。

若要刪除：選取資料庫，按一下 **刪除**。

### 透過 MySQL Workbench (SQL 查詢)：
在查詢編輯器中執行以下指令：

- 建立資料庫：`CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- 列出資料庫：`SHOW DATABASES;`
- 使用資料庫：`USE testdb;`
- 建立資料表：`CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- 插入資料：`INSERT INTO users (name) VALUES ('Alice');`
- 查詢：`SELECT * FROM users;`

如果未自動提交，請使用 `COMMIT;` 提交變更。

## 基本使用提示
- **調整規模**：從 **概觀** > **計算 + 儲存體**，調整 vCore/儲存體/IOPS（大多數變更無需停機）。
- **備份**：每日自動備份；最多 35 天的時間點還原（在 **備份** 設定中設定）。
- **監視**：使用 **計量** 取得 CPU/儲存體見解；設定警示。
- **安全性**：一律使用 SSL（強制執行）。生產環境請啟用 HA、私人網路和 Entra ID 驗證。
- **遷移**：小型資料庫使用 mysqldump；大型資料庫使用 DMS。
- **成本**：支付計算/儲存體費用；從小規模開始並擴充。請使用 [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/) 上的計算機。
- **清理**：刪除資源群組以移除伺服器並避免產生費用。

如需讀取複本或伺服器參數等進階功能，請探索入口網站的左側功能表。

## 參考資料
- [快速入門：使用 Azure 入口網站建立 Flexible Server](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal)
- [使用 MySQL Workbench 連線](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [建立及管理資料庫](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Azure Database for MySQL 文件](https://learn.microsoft.com/en-us/azure/mysql/)