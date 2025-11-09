---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 建立 Azure API 管理服務執行個體
translated: true
type: note
---

### 在 Azure 中使用 API 管理建立 API 閘道

Azure API 管理（APIM）是全託管服務，可作為 API 閘道，提供 API 發佈、安全性、分析和開發者入口網站等功能。以下將透過 Azure 入口網站逐步引導建立 APIM 執行個體。

#### 先決條件
- 有效的 Azure 訂閱。若尚未擁有，請建立 [免費 Azure 帳戶](https://azure.microsoft.com/free/)。

#### 建立 API 管理執行個體的步驟

1. **登入 Azure 入口網站**  
   前往 [Azure 入口網站](https://portal.azure.com) 並使用您的 Azure 帳戶登入。

2. **建立新資源**  
   - 從 Azure 入口網站選單中選取 **建立資源**。（或從 Azure 首頁選取 **建立資源**。）  
   - 在 **建立資源** 頁面中，於 **整合** 類別下搜尋並選取 **API 管理**。  
   - 按一下 **建立**。

3. **設定基本項目**  
   在 **建立 API 管理** 頁面中，切換至 **基本** 標籤並填寫詳細資料：  
   | 設定項目           | 說明                                                                         |
   |--------------------|-----------------------------------------------------------------------------|
   | 訂閱             | 選取此執行個體的 Azure 訂閱。                            |
   | 資源群組       | 選擇現有資源群組或建立新群組（例如 "APIM-RG"）。    |
   | 區域               | 選擇靠近使用者或後端服務的區域（例如 美國東部）。      |
   | 資源名稱        | 輸入唯一名稱（例如 "my-apim-instance"）。此名稱將成為預設網域的一部分：`<名稱>.azure-api.net`。後續無法變更。 |
   | 組織名稱    | 您的組織名稱（用於開發者入口網站和電子郵件）。             |
   | 管理員電子郵件  | 用於接收系統通知的電子郵件。                                        |
   | 定價層         | 開發/測試建議從 **Basic v2** 開始（快速部署，約 30-40 分鐘）。其他層級如 Developer 或 Standard 提供更多功能。 |
   | 單位                | 評估用途預設為 1。                                                |  
   檢閱後繼續。

4. **選用：設定監控與安全性**  
   在 **監控 + 安全** 標籤中：  
   - 啟用選用附加元件，例如用於記錄的 Log Analytics（可能產生額外費用）。  
   - 若為初學者建議暫時略過。

5. **檢閱並建立**  
   - 在 **檢閱 + 建立** 標籤中驗證您的設定。  
   - 按一下 **建立**。部署需時 30-40 分鐘或更長。  
   - 提示：建立完成後可將資源釘選到儀表板以便快速存取。

6. **驗證執行個體**  
   - 在 Azure 入口網站中搜尋 **API 管理服務**。  
   - 選取您的新執行個體。  
   - 在 **概觀** 頁面確認狀態為「上線」。現在您已準備好匯入 API、設定原則或配置開發者入口網站。

#### 後續步驟
- 匯入第一個 API：遵循 [匯入和發佈 API 的教學課程](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)。  
- 加強安全性：新增驗證、速率限制等原則。  
- 清理資源：若為測試用途，請透過入口網站刪除資源群組以避免產生費用（搜尋 **資源群組** > 選取群組 > **刪除資源群組**）。  

如需自訂網域或進階設定，請參閱 [APIM 文件](https://learn.microsoft.com/en-us/azure/api-management/)。

[快速入門：透過入口網站建立 Azure API 管理執行個體](https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance)  
[Azure API 管理概觀](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)