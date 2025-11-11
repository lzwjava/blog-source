---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Postman 功能
translated: true
type: note
---

Postman 是一款廣泛使用的 **API 開發與測試平台**，能簡化 API 的構建、測試及文件編寫流程。它提供直觀的使用介面與強大工具組，支援多種通訊協定，包括 **HTTP、REST、GraphQL、WebSockets 等**。無論是獨立開發或團隊協作，Postman 皆提供即時協作、自動化測試及環境管理等功能，助您優化 API 工作流程。本指南將帶您深入了解 Postman 核心功能，並逐步教學如何有效運用。

---

### Postman 核心功能

Postman 提供多項專為提升 API 開發效率設計的功能：

- **請求建構**：輕鬆建立並發送 HTTP 請求
- **集合管理**：將請求分門別類集中管理
- **環境變數**：管理不同環境的配置（如開發、測試、生產環境）
- **身份驗證**：無縫處理多種驗證方式
- **測試功能**：撰寫並執行測試以驗證 API 回應
- **模擬回應**：透過 Mock 服務模擬 API 回應
- **文件生成**：自動產生並分享 API 文件
- **團隊協作**：與團隊成員共享集合與環境設定

以下將詳細解析各項功能。

---

### 1. **請求建構**
請求建構是 Postman 的核心功能，讓您能輕鬆建立與發送 HTTP 請求。

- **操作步驟**：
  - 開啟 Postman，點擊 **New** > **Request**
  - 從下拉選單選擇 HTTP 方法（如 `GET`、`POST`、`PUT`、`DELETE`）
  - 在網址列輸入 API 端點（如 `https://api.example.com/users`）
  - 於 **Headers** 分頁添加標頭（如 `Content-Type: application/json`）
  - 若為 `POST` 或 `PUT` 等方法，請在 **Body** 分頁添加請求內容（可選擇 `JSON`、`form-data` 等格式）
  - 點擊 **Send** 發送請求，並在下方面板查看回應

- **秘訣**：進行 `GET` 請求時，可透過 **Params** 分頁為網址添加查詢參數（如 `?id=123`）

---

### 2. **集合管理**
集合能協助您整理相關請求，方便集中管理與批次執行。

- **操作步驟**：
  - 點擊 **New** > **Collection** 建立新集合
  - 為集合命名（如「用戶 API」）並可選填描述
  - 透過側邊欄拖曳請求，或點擊集合內的 **Add Request** 來添加請求
  - 點擊集合名稱旁的 **...** 選擇 **Run Collection** 即可執行完整集合。系統將開啟 **Collection Runner**，支援順序或並行執行

- **秘訣**：可在集合內建立資料夾，按功能類別進一步整理請求（如「身份驗證」、「用戶管理」）

---

### 3. **環境變數**
環境變數讓您能管理不同環境的配置（如基礎網址、API 金鑰），無需手動修改每個請求。

- **操作步驟**：
  - 點擊右上角 **Eye** 圖示開啟 **Environment Manager**
  - 點擊 **Add** 建立新環境（如「開發環境」、「生產環境」）
  - 為各環境設定鍵值對（如 `base_url: https://api.example.com`）
  - 在請求中使用雙花括號語法引用變數，如 `{{base_url}}/users`
  - 透過右上角下拉選單切換不同環境

- **秘訣**：跨環境通用的數值（如 API 金鑰）可設定為 **Global Variables**

---

### 4. **身份驗證**
Postman 簡化各種身份驗證方式的處理，確保 API 存取安全。

- **操作步驟**：
  - 在請求分頁中切換至 **Authorization** 分頁
  - 從下拉選單選擇驗證類型（如 **Basic Auth**、**Bearer Token**、**OAuth 2.0**、**API Key**）
  - 填寫所需憑證或令牌（如 Basic Auth 的帳號密碼，或 Bearer Token 的令牌）
  - Postman 將自動把驗證資訊加入請求標頭

- **範例**：
  - 使用 **Bearer Token** 時，貼入令牌後 Postman 會在 `Authorization` 標頭加入 `Bearer <token>`

---

### 5. **測試功能**
Postman 測試框架支援以 JavaScript 撰寫測試腳本，驗證 API 回應是否符合預期。

- **操作步驟**：
  - 在請求分頁中切換至 **Tests** 分頁
  - 撰寫 JavaScript 程式碼驗證回應，例如：
    ```javascript
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });
    ```
  - 發送請求後，於回應面板的 **Test Results** 區域查看測試結果

- **秘訣**：善用內建程式碼片段快速添加常見測試（如「狀態碼為 200」、「回應體 JSON 值檢查」）

---

### 6. **模擬回應**
Mock 功能可模擬 API 回應，在實際 API 尚未完成或不可用時特別實用。

- **操作步驟**：
  - 建立新集合或選擇現有集合
  - 點擊集合旁的 **...** 選擇 **Mock Collection**
  - 為集合中的每個請求定義模擬回應（如範例 JSON 資料）
  - Postman 將生成 Mock 伺服器網址（如 `https://<mock-id>.mock.pstmn.io`），可用於接收模擬回應

- **秘訣**：透過 Mock 服務讓前端開發者能在後端完成前獨立作業

---

### 7. **文件生成**
Postman 能根據集合中的請求自動產生 API 文件。

- **操作步驟**：
  - 開啟集合後點擊 **...** 圖示
  - 選擇 **View Documentation** 生成文件頁面
  - 為各請求添加描述、範例與標籤來自訂文件內容
  - 透過公開發布或分享連結與團隊共享文件

- **秘訣**：保持集合與文件同步更新，確保文件即時性

---

### 8. **團隊協作**
Postman 的協作功能讓團隊能高效合作開發 API 專案。

- **操作步驟**：
  - 點擊 **Workspaces** > **Create Workspace** 建立 **團隊工作區**
  - 透過電子郵件或連結邀請團隊成員加入工作區
  - 在工作區內共享集合、環境設定等資源
  - 使用 **版本控制** 功能分支集合，透過 Pull Request 合併變更

- **秘訣**：直接在 Postman 中使用 **評論** 功能於請求或集合中討論修改內容

---

### 進階使用技巧

- **運用腳本**：透過 **Pre-request Scripts** 在發送請求前設定資料或條件（如生成時間戳記）
- **監控 API**：設定 **Monitors** 定期執行集合，檢查 API 健康狀態與運作時間
- **CI/CD 整合**：使用 Postman 命令列工具 **Newman** 在 CI/CD 流程中執行集合（如 Jenkins、GitHub Actions）
- **探索 Flows**：使用 **Flows** 視覺化構建與自動化複雜 API 工作流程，無需編寫程式碼
- **保護敏感資料**：將 API 金鑰等機密資訊儲存於 **Postman Vault** 確保安全存取

---

### 結語

Postman 不僅是 API 測試工具，更提供完整的 API 開發、協作與自動化解決方案。透過精通請求建構、環境管理、測試與 Mock 等核心功能，將大幅提升開發效率並優化 API 工作流程。無論您是獨立開發者還是團隊成員，Postman 直觀的介面與進階功能皆使其成為現代 API 開發的必備工具。立即開始探索這些功能，釋放您 API 專案的完整潛能！