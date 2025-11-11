---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: GitHub OAuth 裝置代碼流程
translated: true
type: note
---

### 概述

這段 JavaScript 程式碼實作了 OAuth 2.0 裝置授權流程（亦稱為裝置碼授權），用於向 GitHub 進行身份驗證並取得存取權杖。此流程通常用於無介面應用程式（例如 CLI 工具或嵌入式系統），使用者無法直接透過網頁瀏覽器進行身份驗證授權。

在此特定案例中，程式碼模擬 GitHub Copilot 插件（例如 Neovim 或 Vim 版本）的請求，使用偽裝成 Copilot 客戶端的標頭，以潛在地整合或存取 GitHub 的身份驗證系統。目標是產生一個存取權杖，可用於需要使用者身份驗證的 GitHub API 呼叫，例如讀取使用者資訊（根據 `scope: "read:user"` 設定）。

此程式碼以 Node.js 腳本形式執行，使用 `fetch` 進行 HTTP 請求，並使用 `process` 讀取環境變數。它假設 Node.js 環境支援 `fetch`（例如新版本或透過 polyfill 實現）。若成功，它會持續輪詢 GitHub 伺服器，直到使用者授權請求或逾時為止。

**重要注意事項：**
- 此程式碼需要設定環境變數 `MY_COPILOT_CLIENT_ID`，應為註冊給 GitHub Copilot 的 GitHub OAuth App 客戶端 ID。
- 錯誤處理較為簡略——例如若取得資料失敗，僅記錄錯誤並繼續執行或退出。
- 從安全性角度來看，儲存或記錄存取權杖具有風險（它們授予 API 存取權限）。此程式碼直接將完整權杖物件輸出至控制台，在實際使用中可能引發隱私/安全問題。存取權杖應安全處理（例如加密儲存並定期輪換）。
- 此流程需要使用者互動：使用者必須造訪指定網址並在 GitHub 網站上輸入驗證碼以完成授權。
- 這並非 GitHub 官方文件提供的程式碼；似乎是從 GitHub Copilot 的行為反向工程得出。請依照 GitHub 服務條款負責任地使用 API。

### 逐步解析

#### 1. 環境檢查
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- 從環境變數中讀取 `MY_COPILOT_CLIENT_ID`（例如可透過在 shell 中執行 `export MY_COPILOT_CLIENT_ID=your_client_id` 設定）。
- 若未設定，則記錄錯誤並退出腳本（程序代碼 1 表示失敗）。
- 此客戶端 ID 來自已註冊的 GitHub OAuth App（為 OAuth 流程所必需）。

#### 2. 通用標頭設定
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- 建立 `Headers` 物件，包含用於 HTTP 請求的鍵值對。
- 這些標頭使請求看起來像是來自 GitHub Copilot Vim 插件（Neovim 0.6.1 的 1.16.0 版本）。這可能是為了偽裝使用者代理字串並模擬 Copilot 的 API 呼叫，這對於 GitHub 接受請求可能是必要或有幫助的。
- `"accept": "application/json"`：預期接收 JSON 格式的回應。
- `"content-type": "application/json"`：在請求主體中傳送 JSON 資料。
- `"accept-encoding"`：允許 gzip/deflate 壓縮以節省頻寬。

#### 3. `getDeviceCode()` 函數
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **目的**：透過向 GitHub 請求裝置碼來啟動裝置碼流程。
- 建構 JSON 承載資料，包含：
  - `client_id`：OAuth 客戶端 ID（用於驗證你的應用程式）。
  - `scope`：`"read:user"`——限制權杖僅能讀取基本使用者設定檔資訊（例如透過 GitHub API 讀取使用者名稱、電子郵件）。這是最小範圍的權限。
- 向 `https://github.com/login/device/code`（GitHub 的 OAuth 裝置碼端點）發送 POST 請求。
- 解析 JSON 回應（預期欄位：`device_code`、`user_code`、`verification_uri`、`expires_in`——程式碼中未顯示，但為此流程的標準欄位）。
- 若發生錯誤（例如網路問題），記錄錯誤但繼續執行（可能回傳 `undefined`）。
- 回傳從 GitHub 取得的已解析 JSON 資料物件。

#### 4. `getAccessToken(deviceCode: string)` 函數
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **目的**：在使用者授權後，輪詢 GitHub 以將裝置碼交換為存取權杖。
- 接收來自前一步驟的 `device_code`。
- 建構 JSON 資料，包含：
  - `client_id`：與之前相同。
  - `device_code`：識別此裝置/驗證嘗試的唯一代碼。
  - `grant_type`：指定此為裝置碼授權（標準 OAuth2 URN）。
- 向 `https://github.com/login/oauth/access_token` 發送 POST 請求。
- 回傳已解析的 JSON 回應，可能為：
  - 成功時：`{ access_token: "...", token_type: "bearer", scope: "read:user" }`。
  - 等待中/錯誤時：`{ error: "...", error_description: "..." }`（例如 "authorization_pending" 或 "slow_down"）。
- 錯誤（例如 fetch 失敗）會被記錄但未明確處理，因此呼叫者必須檢查回傳值。

#### 5. 主要執行邏輯（立即呼叫的非同步函數）
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **整體流程**：協調完整的 OAuth 2.0 裝置碼授權流程。
- 呼叫 `getDeviceCode()` 並將回應解構至變數（假設成功且包含這些屬性）。
- 記錄使用者操作說明：
  - `user_code`：短字母數字代碼（例如 "ABCD-EFGH"）。
  - `verification_uri`：通常為 `https://github.com/login/device`，使用者需在此進行身份驗證。
  - `expires_in`：代碼的有效期限（以秒為單位，例如 900 表示 15 分鐘）。
- 使用者必須造訪該網址，登入 GitHub 並輸入使用者代碼以授權應用程式。
- 進入無限迴圈以輪詢權杖：
  - 每次嘗試間隔 5 秒（輪詢間隔；GitHub 建議若請求過於頻繁應使用 slow_down）。
  - 呼叫 `getAccessToken(device_code)`。
  - 若回應包含 `error`：記錄錯誤（例如若為 "authorization_pending" 則繼續等待）。
  - 若包含 `access_token`：記錄完整權杖物件（以縮排格式化）並跳出迴圈。
- **邊界案例/問題**：
  - 若 `getDeviceCode()` 失敗，解構可能出錯（程式碼未檢查此情況）。
  - 無迴圈逾時機制——除非收到存取權杖或腳本崩潰，否則會持續輪詢。
  - 將存取權杖記錄至控制台會暴露其內容；在生產環境中，應安全地儲存它（例如寫入檔案或資料庫）。

### 端到端運作原理
1. **步驟 1：請求裝置碼** → 腳本從 GitHub 取得臨時代碼。
2. **步驟 2：使用者授權** → 使用者造訪 GitHub 並輸入代碼以授予權限。
3. **步驟 3：輪詢權杖** → 腳本持續向 GitHub 查詢，直到核發權杖為止。
4. **結果**：取得指定範圍（例如透過 GitHub API 讀取使用者資料）的存取權杖。

這是模擬如 GitHub CLI 等工具可能的工作方式，並針對 Copilot 進行調整。有關 GitHub OAuth 的官方文件，請參閱 https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow。若你正在建置類似功能，請確保符合 OAuth 標準與 GitHub 政策。若你對修改或執行此程式碼有疑問，請告訴我！