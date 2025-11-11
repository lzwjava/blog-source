---
audio: false
generated: true
lang: hant
layout: post
title: 使用原始 HTTP 請求測試 NPM 註冊表
translated: true
type: note
---

要使用 `curl` 或 Insomnia 等工具透過原始 HTTP 請求測試你的 NPM registry，你可以透過檢查連線能力、認證狀態以及提供套件資料的能力來驗證其功能——完全無需依賴 NPM 客戶端。由於你的 registry 需要使用者名稱和密碼，你必須在請求中手動處理認證。以下是一份完整指南，用於透過原始 HTTP 請求測試你的 registry，假設它是一個支援基於令牌或基本認證的 NPM 相容 registry（例如 Verdaccio、Nexus 或自訂實作）。

---

## 使用原始 HTTP 請求測試 Registry 的步驟

### 1. 進行認證並取得令牌（如有需要）

大多數 NPM registry 使用基於令牌的認證，要求你先登入取得令牌才能進行後續請求。部分 registry 也可能直接支援基本認證。以下是使用 `curl` 進行認證的方法：

#### 使用 `curl` 登入
傳送 PUT 請求到 registry 的認證端點以取得令牌：

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **替換內容**：
  - `<username>`：你的 registry 使用者名稱。
  - `<password>`：你的 registry 密碼。
  - `<registry-url>`：你的 registry 完整 URL（例如 `https://my-registry.example.com`）。
- **預期回應**：如果成功，你將收到包含令牌的 JSON 回應：
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **儲存令牌**：複製 `your-auth-token` 的值以供後續請求使用。

**注意**：如果你的 registry 使用不同的認證端點或方法（例如基本認證或自訂 API），請查閱其文件。如果直接支援基本認證，你可以跳過此步驟，並在後續請求中改用 `-u "<username>:<password>"`。

---

### 2. 對 Registry 進行 Ping 測試

透過傳送 GET 請求到 registry 的根 URL 或 ping 端點，測試基本連線能力。

#### 使用 `curl` 進行 Ping 測試
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **替換內容**：
  - `your-auth-token`：來自步驟 1 的令牌。
  - `<registry-url>`：你的 registry URL。
- **預期回應**：成功回應（HTTP 200）可能會返回 registry 的首頁或簡單狀態訊息（例如，對於基於 CouchDB 的 registry，可能是 `{"db_name":"registry"}`）。
- **替代方案**：部分 registry 提供 `/-/ping` 端點：
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**如果使用基本認證**：如果你的 registry 不使用令牌且支援基本認證：
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. 取得套件元資料

透過請求特定套件的詳細資訊，驗證 registry 能否提供套件元資料。

#### 使用 `curl` 取得元資料
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **替換內容**：
  - `<package-name>`：你已知存在於 registry 上的套件（例如，如果它代理了公共 registry 則使用 `lodash`，或私有套件如 `my-org-utils`）。
- **預期回應**：包含套件元資料的 JSON 物件，包括版本、相依性及 tarball URL。例如：
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

**如果使用基本認證**：
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **成功標誌**：200 OK 回應及元資料確認 registry 正確提供套件資料。

---

### 4. 下載套件 Tarball（可選）

為全面測試 registry，下載套件 tarball 以確保它能提供實際的套件檔案。

#### 使用 `curl` 下載 Tarball
1. 從步驟 3 的元資料中，找到特定版本的 `tarball` URL（例如 `<registry-url>/lodash/-/lodash-4.17.21.tgz`）。
2. 下載它：
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **替換內容**：`<tarball-url>` 替換為元資料中的 URL。
- **`-O` 標誌**：以原始名稱儲存檔案（例如 `lodash-4.17.21.tgz`）。
- **如果使用基本認證**：
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **成功標誌**：檔案成功下載，你可以解壓縮它（例如使用 `tar -xzf <filename>`）以驗證其內容。

---

## 使用 Insomnia 進行測試

如果你偏好使用 GUI 工具如 Insomnia，請遵循以下步驟：

### 1. 設定認證
- 在 Insomnia 中建立新請求。
- 前往 **Auth** 標籤：
  - **Bearer Token**：如果你在步驟 1 取得了令牌，選擇 "Bearer Token" 並貼上 `your-auth-token`。
  - **Basic Auth**：如果 registry 使用基本認證，選擇 "Basic Auth" 並輸入你的 `<username>` 和 `<password>`。

### 2. 對 Registry 進行 Ping 測試
- **方法**：GET
- **URL**：`<registry-url>` 或 `<registry-url>/-/ping`
- 點擊 **Send**。
- **預期回應**：200 OK 狀態及簡單回應主體。

### 3. 取得套件元資料
- **方法**：GET
- **URL**：`<registry-url>/<package-name>`
- 確保在 Auth 標籤中已設定認證。
- 點擊 **Send**。
- **預期回應**：200 OK 狀態及 JSON 格式的套件元資料。

### 4. 下載 Tarball
- **方法**：GET
- **URL**：元資料中的 tarball URL（例如 `<registry-url>/<package-name>/-/<package-name>-<version>.tgz`）。
- 點擊 **Send and Download** 將檔案儲存到本地。
- **成功標誌**：檔案下載完成，確認 registry 能提供套件。

---

## 疑難排解

- **401 未經授權**：
  - 檢查你的令牌或憑證。
  - 確保 `Authorization` 標頭或基本認證格式正確。
- **404 找不到**：
  - 確認套件存在於 registry 上。
  - 如果測試公共套件（例如 `lodash`），請確認 registry 代理了公共 NPM registry。
- **連線錯誤**：
  - 仔細檢查 `<registry-url>`（例如，如需 HTTPS 請包含 `https://`）。
  - 對於 HTTPS registry，如果使用 `curl` 時出現 SSL 錯誤，可加入 `-k` 以跳過憑證檢查（僅供測試使用）。
- **自訂 Registry 行為**：
  - 如果這些步驟失敗，請查閱你的 registry 文件以了解特定端點或認證方法。

---

## 結論

透過遵循以上步驟使用 `curl` 或 Insomnia，你可以透過原始 HTTP 請求測試你的 NPM registry 的連線能力、認證狀態及套件提供能力。首先進行認證（如有需要），然後對 registry 進行 ping 測試，取得已知套件的元資料，並可選擇下載 tarball。此方法能確保你的 registry 在 HTTP 層面完全運作正常。