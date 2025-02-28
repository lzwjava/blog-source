---
audio: false
lang: hant
layout: post
title: 測試 NPM 註冊表使用原始 HTTP 要求
translated: true
---

要使用原始 HTTP 要求（如 `curl` 或 Insomnia）測試您的 NPM 註冊表，您可以通過檢查連接性、身份驗證和提供套件數據來驗證其功能，而不依賴於 NPM 客戶端。由於您的註冊表需要用戶名和密碼，您需要在要求中手動處理身份驗證。以下是使用原始 HTTP 要求測試您的註冊表的完整指南，假設它是一個支持基於令牌或基本身份驗證的 NPM 兼容註冊表（例如 Verdaccio、Nexus 或自定義實現）。

---

## 使用原始 HTTP 要求測試註冊表的步驟

### 1. 身份驗證並獲取令牌（如果需要）

大多數 NPM 註冊表使用基於令牌的身份驗證，要求您登錄以獲取令牌，然後再進行其他要求。某些註冊表可能也支持直接的基本身份驗證。以下是使用 `curl` 進行身份驗證的方法：

#### 使用 `curl` 登錄
向註冊表的身份驗證端點發送 PUT 要求以獲取令牌：

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **替換**：
  - `<username>`：您的註冊表用戶名。
  - `<password>`：您的註冊表密碼。
  - `<registry-url>`：您的註冊表的完整 URL（例如 `https://my-registry.example.com`）。
- **預期回應**：如果成功，您將獲得一個包含令牌的 JSON 回應：
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **保存令牌**：複製 `your-auth-token` 值以在後續要求中使用。

**注意**：如果您的註冊表使用不同的身份驗證端點或方法（例如基本身份驗證或自定義 API），請參閱其文檔。如果它支持直接的基本身份驗證，您可以跳過此步驟，並在後續要求中包含 `-u "<username>:<password>"`。

---

### 2. Ping 註冊表

通過向其根 URL 或 ping 端點發送 GET 要求來測試註冊表的基本連接性。

#### 使用 `curl` Ping
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **替換**：
  - `your-auth-token`：步驟 1 中的令牌。
  - `<registry-url>`：您的註冊表 URL。
- **預期回應**：成功的回應（HTTP 200）可能會返回註冊表的首頁或簡單的狀態消息（例如，對於基於 CouchDB 的註冊表，`{"db_name":"registry"}`）。
- **替代方案**：某些註冊表提供 `/-/ping` 端點：
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**如果使用基本身份驗證**：如果您的註冊表不使用令牌並支持基本身份驗證：
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. 检索套件元數據

通過請求特定套件的詳細信息來驗證註冊表是否可以提供套件元數據。

#### 使用 `curl` 获取元數據
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **替換**：
  - `<package-name>`：您知道存在於您的註冊表中的套件（例如，如果它代理公共註冊表，則為 `lodash`，或私有套件如 `my-org-utils`）。
- **預期回應**：包含套件元數據的 JSON 對象，包括版本、依賴項和壓縮文件 URL。例如：
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<registry-url>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**如果使用基本身份驗證**：
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **成功**：200 OK 回應與元數據確認註冊表正確提供套件數據。

---

### 4. 下載套件壓縮文件（可選）

為了全面測試註冊表，下載套件壓縮文件以確保它可以交付實際的套件文件。

#### 使用 `curl` 下載壓縮文件
1. 從步驟 3 中的元數據中找到特定版本的 `tarball` URL（例如 `<registry-url>/lodash/-/lodash-4.17.21.tgz`）。
2. 下載它：
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **替換**：將 `<tarball-url>` 替換為元數據中的 URL。
- **`-O` 旗標**：以其原始名稱保存文件（例如 `lodash-4.17.21.tgz`）。
- **如果使用基本身份驗證**：
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **成功**：文件成功下載，您可以提取它（例如，使用 `tar -xzf <filename>`）以驗證其內容。

---

## 使用 Insomnia 測試

如果您更喜歡使用圖形用戶界面工具如 Insomnia，請按照以下步驟操作：

### 1. 設置身份驗證
- 在 Insomnia 中創建一個新要求。
- 轉到 **Auth** 選項卡：
  - **Bearer Token**：如果您在步驟 1 中獲得了令牌，選擇 "Bearer Token" 並粘貼 `your-auth-token`。
  - **Basic Auth**：如果註冊表使用基本身份驗證，選擇 "Basic Auth" 並輸入您的 `<username>` 和 `<password>`。

### 2. Ping 註冊表
- **方法**：GET
- **URL**：`<registry-url>` 或 `<registry-url>/-/ping`
- 點擊 **Send**。
- **預期回應**：200 OK 狀態與簡單的回應體。

### 3. 检索套件元數據
- **方法**：GET
- **URL**：`<registry-url>/<package-name>`
- 確保在 Auth 選項卡中設置身份驗證。
- 點擊 **Send**。
- **預期回應**：200 OK 狀態與 JSON 格式的套件元數據。

### 4. 下載壓縮文件
- **方法**：GET
- **URL**：元數據中的壓縮文件 URL（例如 `<registry-url>/<package-name>/-/<package-name>-<version>.tgz`）。
- 點擊 **Send and Download** 以將文件保存到本地。
- **成功**：文件下載，確認註冊表提供套件。

---

## 故障排除

- **401 未經授權**：
  - 檢查您的令牌或憑證。
  - 確保 `Authorization` 標頭或基本身份驗證格式正確。
- **404 未找到**：
  - 驗證套件是否存在於註冊表中。
  - 如果測試公共套件（例如 `lodash`），確認註冊表代理公共 NPM 註冊表。
- **連接錯誤**：
  - 重新檢查 `<registry-url>`（例如，如果需要，請包含 `https://`）。
  - 對於 HTTPS 註冊表，如果使用 `curl` 時出現 SSL 錯誤，請添加 `-k` 以跳過憑證檢查（僅用於測試）。
- **自定義註冊表行為**：
  - 如果這些步驟失敗，請參閱您的註冊表文檔以獲取特定端點或身份驗證方法。

---

## 結論

通過使用 `curl` 或 Insomnia 遵循這些步驟，您可以使用原始 HTTP 要求測試您的 NPM 註冊表的連接性、身份驗證和套件提供功能。首先進行身份驗證（如果需要），然後 ping 註冊表，檢索已知套件的元數據，並可選地下載壓縮文件。這種方法確保您的註冊表在 HTTP 級別完全運作。