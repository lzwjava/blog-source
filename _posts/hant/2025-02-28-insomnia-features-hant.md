---
audio: false
generated: false
lang: hant
layout: post
title: 使用 Kong Insomnia GUI 的功能
translated: true
---

Kong Insomnia 提供一個強大的圖形用戶界面 (GUI) 來簡化 API 開發。以下是如何在 Insomnia GUI 中使用 **params**、**body**、**auth**、**cookies**、**certificates**、**settings** 和 **proxy** 的詳細指南。

---

#### 1. **Params (查詢參數)**
查詢參數用於將數據附加到 URL，通常用於 GET 請求。

- **使用方法**：
  - 打開 **Debug** 標籤並選擇或創建一個請求（例如，GET）。
  - 在 URL 字段旁邊，點擊 **Query** 標籤。
  - 添加查詢參數的鍵值對。例如，將 `key` 設置為 "id" 並將 `value` 設置為 "123" 將 `?id=123` 附加到您的 URL。
  - 在值字段中輸入 `{{variableName}}` 以使用環境變量（例如，`{{userId}}`）。
  - 通過切換每個對的旁邊的複選框來啟用或禁用特定參數。

- **示例**：
  對於 URL 如 `https://api.example.com/users?id=123`，添加：
  - 鍵：`id`
  - 值：`123`
  Insomnia 將自動格式化 URL 並附加查詢字符串。

---

#### 2. **Body**
Body 用於與請求（如 POST 或 PUT）一起發送數據。

- **使用方法**：
  - 在 **Debug** 標籤中選擇請求（例如，POST 或 PUT）。
  - 切換到 URL 字段下方的 **Body** 標籤。
  - 從下拉菜單中選擇一種 body 類型：
    - **JSON**：輸入 JSON 數據（例如，`{"name": "John", "age": 30}`）。
    - **Form URL-Encoded**：添加鍵值對，類似於查詢參數。
    - **Multipart Form**：添加字段或上傳文件以用於具有文件附件的表單。
    - **Raw**：輸入純文本或其他格式（例如，XML）。
  - 在 body 內容中輸入 `{{variableName}}` 以使用環境變量。

- **示例**：
  對於發送 JSON 的 POST 請求：
  - 從下拉菜單中選擇 **JSON**。
  - 输入：`{"name": "John", "age": "{{userAge}}"}`
  Insomnia 將自動將 `Content-Type` 標頭設置為 `application/json`。

---

#### 3. **Auth (驗證)**
驗證設置允許您在請求中包含憑證或令牌。

- **使用方法**：
  - 在 **Debug** 標籤中選擇您的請求。
  - 轉到 **Auth** 標籤。
  - 從下拉菜單中選擇一種驗證類型：
    - **Basic Auth**：輸入用戶名和密碼。
    - **Bearer Token**：粘貼您的令牌（例如，JWT）。
    - **OAuth 2.0**：配置客戶端 ID、密鑰和其他詳細信息以進行 OAuth 流。
    - **API Key**：添加鍵值對（例如，鍵：`Authorization`，值：`your-api-key`）。
  - Insomnia 會自動將驗證詳細信息添加到請求標頭。

- **示例**：
  對於 Bearer Token：
  - 選擇 **Bearer Token**。
  - 粘貼您的令牌（例如，`abc123xyz`）。
  請求標頭將包括：`Authorization: Bearer abc123xyz`。

---

#### 4. **Cookies**
Cookies 會自動管理，但可以手動查看或編輯。

- **使用方法**：
  - Insomnia 會根據工作區存儲從伺服器響應接收到的 cookies。
  - 要管理 cookies：
    - 轉到 **Preferences** (Ctrl + , 或 macOS 上的 Cmd + ,)。
    - 導航到 **Data** > **Cookie Jar**。
    - 根據需要查看、編輯或刪除 cookies。
  - Cookies 會在同一工作區的後續請求中自動發送並持續。

- **提示**：
  如果需要使用特定的 cookies 進行測試，請在 **Cookie Jar** 中手動添加相關域的 cookies。

---

#### 5. **Certificates**
客戶端證書用於需要相互 TLS 驗證的 HTTPS 請求。

- **使用方法**：
  - 轉到 **Preferences** (Ctrl + , 或 macOS 上的 Cmd + ,)。
  - 選擇 **Certificates** 部分。
  - 點擊 **Add Certificate**：
    - 提供證書文件（例如，`.pem`，`.crt`）。
    - 添加私鑰文件和可選的密碼（如果需要）。
    - 將證書與特定主機（例如，`api.example.com`）關聯。
  - Insomnia 將使用證書發送到指定的主機的請求。

- **示例**：
  對於需要證書的 `api.example.com`：
  - 上傳 `client.crt` 和 `client.key`。
  - 將主機設置為 `api.example.com`。
  發送到該域的請求將包括證書。

---

#### 6. **Settings**
設置允許您自定義 Insomnia 的行為。

- **使用方法**：
  - 通過 **Preferences** (Ctrl + , 或 macOS 上的 Cmd + ,) 訪問。
  - 關鍵選項包括：
    - **Theme**：在輕、暗或系統默認之間切換。
    - **Proxy**：配置代理設置（見下文）。
    - **Plugins**：安裝額外功能（例如，自定義響應格式化程序）。
    - **Data**：管理 Local Vault 以安全存儲敏感數據（例如，API 密鑰）。

- **提示**：
  使用 **Local Vault** 安全存儲敏感值（例如，令牌）而不是硬編碼。

---

#### 7. **Proxy**
代理將您的請求路由到指定的伺服器，對於調試或企業網絡非常有用。

- **使用方法**：
  - 轉到 **Preferences** > **Proxy**。
  - 啟用代理並輸入代理伺服器詳細信息（例如，`http://proxy.example.com:8080`）。
  - 要全局使用，請在此處保存。
  - 要為每個請求代理：
    - 點擊 **Debug** 標籤中請求名稱旁邊的齒輪圖標。
    - 在請求特定配置中覆蓋代理設置。

- **示例**：
  要通過企業代理路由請求：
  - 在 **Preferences** 中啟用代理。
  - 將 Proxy URL 設置為 `http://proxy.example.com:8080`。
  所有請求現在都將使用此代理，除非覆蓋。

---

### 摘要
這是如何在 Insomnia GUI 中使用這些功能的快速回顧：
- **Params**：在 **Query** 標籤中為 GET 請求添加查詢參數。
- **Body**：通過 **Body** 標籤以選擇的格式發送 POST/PUT 請求的數據。
- **Auth**：在 **Auth** 標籤中設置驗證以進行安全請求。
- **Cookies**：在 **Preferences** > **Cookie Jar** 中管理 cookies。
- **Certificates**：在 **Preferences** > **Certificates** 中為 HTTPS 添加客戶端證書。
- **Settings**：在 **Preferences** 中自定義 Insomnia（主題、插件等）。
- **Proxy**：在 **Preferences** 或每個請求中配置代理。

通過利用這些功能，您可以高效地測試和調試 Kong Insomnia 中的 API。實驗每個部分以定制您的工作流程！