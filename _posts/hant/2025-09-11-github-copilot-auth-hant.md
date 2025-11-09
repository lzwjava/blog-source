---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: GitHub Copilot 認證流程
translated: true
type: note
---

好問題——GitHub Copilot 的認證流程基本上是一個標準的 **OAuth2 裝置授權碼流程**，但額外疊加了 GitHub 針對 Copilot 服務本身的特定令牌。讓我逐步拆解說明：

---

### 1. **裝置流程 (`/login/device/code`)**

* 當你首次登入時，Copilot 客戶端（例如 VS Code 擴充功能、JetBrains 外掛或 CLI）會呼叫 GitHub 的 OAuth 端點：

  ```
  POST https://github.com/login/device/code
  ```
* 它會同時傳送 **client_id**（GitHub Copilot 專用的識別碼）。
* GitHub 會回應：

  * `device_code`（用於輪詢的內部代碼），
  * `user_code`（你在瀏覽器中看到並輸入的代碼），
  * `verification_uri`（你輸入代碼的網址），
  * `interval`（客戶端輪詢的頻率）。

---

### 2. **輪詢存取令牌**

* Copilot 客戶端接著進行輪詢：

  ```
  POST https://github.com/login/oauth/access_token
  ```
* 它包含 `device_code` 和 `client_id`。
* 一旦你在瀏覽器中完成授權，GitHub 會傳回：

  * `access_token`（一個** GitHub OAuth 令牌**，授權範圍限於 Copilot 使用），
  * `token_type=bearer`，
  * `expires_in`（有效期限）。

這個 `access_token` 是一個**標準的 GitHub OAuth2 令牌**。

---

### 3. **兌換為 `copilot_internal` 令牌**

* Copilot 客戶端無法直接使用 GitHub OAuth 令牌呼叫 Copilot API。
* 取而代之的是，它會向 Copilot 服務兌換令牌：

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* 回應為：

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* 這個 **`copilot_internal` v2 令牌**才是 Copilot 客戶端用來與 **Copilot 推論服務**（例如 `https://copilot-proxy.githubusercontent.com`）通訊的憑證。

---

### 4. **使用 `copilot_internal` 令牌**

* 所有後續的自動完成或聊天請求均使用以下方式進行認證：

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* 此令牌有效期限較短（通常約 1 小時），並與你的 GitHub 帳戶及 Copilot 訂閱狀態綁定。
* 客戶端會透過重新兌換 GitHub OAuth 存取令牌來定期更新它。

---

✅ **總結來說：**

* `/login/device/code` → 提供你在瀏覽器中認證的代碼。
* `/login/oauth/access_token` → 提供你 GitHub OAuth 令牌。
* `/copilot_internal/v2/token` → 將 GitHub OAuth 令牌兌換為短期的 Copilot 令牌，這才是用於自動完成功能的*真實*憑證。

---

你是否希望我進一步繪製**確切的請求/回應範例**（包含標頭與 JSON 範例），以便你能實際查看負載的具體樣貌？