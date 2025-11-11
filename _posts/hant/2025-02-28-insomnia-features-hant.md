---
audio: false
generated: true
lang: hant
layout: post
title: Kong Insomnia 圖形介面功能應用
translated: true
type: note
---

Kong Insomnia 提供強大的圖形使用者介面（GUI）來簡化 API 開發。以下是關於如何在 Insomnia GUI 中使用 **params**、**body**、**auth**、**cookies**、**certificates**、**settings** 及 **proxy** 的詳細指南。

---

#### 1. **Params（查詢參數）**  
查詢參數用於在 URL 後附加資料，通常用於 GET 請求。

- **使用方法**：  
  - 開啟 **Debug 分頁**並選擇或建立請求（例如 GET）。  
  - 在 URL 欄位旁點擊 **Query** 分頁。  
  - 新增鍵值對作為查詢參數。例如，輸入 `key` 為 "id" 及 `value` 為 "123" 將會在 URL 後附加 `?id=123`。  
  - 要使用環境變數，請在值欄位中輸入 `{{variableName}}`（例如 `{{userId}}`）。  
  - 透過切換每個參數旁的核取方塊來啟用或停用特定參數。

- **範例**：  
  對於像 `https://api.example.com/users?id=123` 的 URL，請新增：  
  - 鍵：`id`  
  - 值：`123`  
  Insomnia 會自動將查詢字串格式化至 URL。

---

#### 2. **Body**  
Body 用於在 POST 或 PUT 等請求中傳送資料。

- **使用方法**：  
  - 在 **Debug 分頁**中選擇請求（例如 POST 或 PUT）。  
  - 切換至 URL 欄位下方的 **Body** 分頁。  
  - 從下拉選單中選擇 body 類型：  
    - **JSON**：輸入 JSON 資料（例如 `{"name": "John", "age": 30}`）。  
    - **Form URL-Encoded**：新增鍵值對，類似查詢參數。  
    - **Multipart Form**：為包含檔案附件的表單新增欄位或上傳檔案。  
    - **Raw**：輸入純文字或其他格式（例如 XML）。  
  - 在 body 內容中輸入 `{{variableName}}` 以使用環境變數。

- **範例**：  
  對於傳送 JSON 的 POST 請求：  
  - 從下拉選單中選擇 **JSON**。  
  - 輸入：`{"name": "John", "age": "{{userAge}}"}`。  
  Insomnia 會自動將 `Content-Type` 標頭設為 `application/json`。

---

#### 3. **Auth（身份驗證）**  
身份驗證設定允許您在請求中包含憑證或令牌。

- **使用方法**：  
  - 在 **Debug 分頁**中選擇您的請求。  
  - 前往 **Auth** 分頁。  
  - 從下拉選單中選擇身份驗證類型：  
    - **Basic Auth**：輸入使用者名稱和密碼。  
    - **Bearer Token**：貼上您的令牌（例如 JWT）。  
    - **OAuth 2.0**：為 OAuth 流程設定客戶端 ID、密鑰及其他詳細資訊。  
    - **API Key**：新增鍵值對（例如 鍵：`Authorization`，值：`your-api-key`）。  
  - Insomnia 會自動將身份驗證詳細資訊加入請求標頭。

- **範例**：  
  對於 Bearer Token：  
  - 選擇 **Bearer Token**。  
  - 貼上您的令牌（例如 `abc123xyz`）。  
  請求標頭將包含：`Authorization: Bearer abc123xyz`。

---

#### 4. **Cookies**  
Cookies 會自動管理，但亦可手動檢視或編輯。

- **使用方法**：  
  - Insomnia 會按工作空間儲存從伺服器回應接收的 cookies。  
  - 要管理 cookies：  
    - 前往 **Preferences**（Ctrl + , 或 macOS 上的 Cmd + ,）。  
    - 導覽至 **Data** > **Cookie Jar**。  
    - 按需要檢視、編輯或刪除 cookies。  
  - Cookies 會在同工作空間的請求間持續存在，並自動隨後續請求傳送。

- **提示**：  
  若需使用特定 cookies 進行測試，請在相關網域的 **Cookie Jar** 中手動新增。

---

#### 5. **Certificates**  
用戶端憑證用於需要雙向 TLS 身份驗證的 HTTPS 請求。

- **使用方法**：  
  - 前往 **Preferences**（Ctrl + , 或 Cmd + ,）。  
  - 選擇 **Certificates** 部分。  
  - 點擊 **Add Certificate**：  
    - 提供憑證檔案（例如 `.pem`、`.crt`）。  
    - 新增私鑰檔案及所需的通行密碼（可選）。  
    - 將憑證與特定主機關聯（例如 `api.example.com`）。  
  - Insomnia 會對指定主機的請求使用該憑證。

- **範例**：  
  對於需要憑證的 `api.example.com`：  
  - 上傳 `client.crt` 和 `client.key`。  
  - 將 Host 設為 `api.example.com`。  
  對此網域的請求將包含該憑證。

---

#### 6. **Settings**  
設定允許您自訂 Insomnia 的行為。

- **使用方法**：  
  - 透過 **Preferences**（Ctrl + , 或 Cmd + ,）存取。  
  - 主要選項包括：  
    - **Theme**：在淺色、深色或系統預設之間切換。  
    - **Proxy**：設定代理伺服器（見下文）。  
    - **Plugins**：安裝額外功能（例如自訂回應格式化工具）。  
    - **Data**：管理 Local Vault 以安全儲存敏感資料（如 API 金鑰）。  

- **提示**：  
  使用 **Local Vault** 安全儲存敏感值（例如令牌），而非將其硬編碼。

---

#### 7. **Proxy**  
代理伺服器將您的請求透過指定伺服器路由，對除錯或企業網路非常有用。

- **使用方法**：  
  - 前往 **Preferences** > **Proxy**。  
  - 啟用代理伺服器並輸入代理伺服器詳細資訊（例如 `http://proxy.example.com:8080`）。  
  - 若要全域使用，請在此處儲存。  
  - 若要為每個請求設定代理：  
    - 在 **Debug 分頁**中點擊請求名稱旁的齒輪圖示。  
    - 在請求特定設定中覆寫代理設定。  

- **範例**：  
  要透過企業代理伺服器路由請求：  
  - 在 **Preferences** 中啟用代理。  
  - 將 Proxy URL 設為 `http://proxy.example.com:8080`。  
  所有請求現將使用此代理，除非被覆寫。

---

### 總結  
以下是在 Insomnia GUI 中使用這些功能的快速回顧：  
- **Params**：在 **Query** 分頁中為 GET 請求新增查詢參數。  
- **Body**：透過 **Body** 分頁以選定格式傳送 POST/PUT 請求的資料。  
- **Auth**：在 **Auth** 分頁中為安全請求設定身份驗證。  
- **Cookies**：在 **Preferences** > **Cookie Jar** 中管理 cookies。  
- **Certificates**：在 **Preferences** > **Certificates** 中為 HTTPS 新增用戶端憑證。  
- **Settings**：在 **Preferences** 中自訂 Insomnia（主題、外掛程式等）。  
- **Proxy**：在 **Preferences** 或每個請求中設定代理伺服器。  

透過善用這些功能，您可以在 Kong Insomnia 中高效測試和除錯 API。嘗試每個部分以量身定制您的工作流程！