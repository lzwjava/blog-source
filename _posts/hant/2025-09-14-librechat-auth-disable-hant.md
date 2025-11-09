---
audio: false
date: 2025-09-14
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 停用LibreChat身份驗證繞行方法
translated: true
type: note
---

簡短回答：你無法完全關閉 LibreChat 的身份驗證功能，但可以解決「持續要求登入」的問題，讓使用體驗接近「免登入」。以下是實際有效的方法（及原因說明）：

### 1) 無法完全停用身份驗證

維護者已確認：可以停用註冊功能，但身份驗證系統本身無法關閉。（[GitHub][1]）

### 2) 持續被登出的原因

若透過 **HTTP** 存取你的實例（例如區域網路 IP），在生產環境中 cookies 會被標記為 `secure`，導致瀏覽器無法保存而強制返回登入頁面。請改用 **HTTPS**（即使使用自簽憑證）或在開發模式下運行 API 以停用安全 cookies。（[GitHub][1]）

### 3) 兩種可靠解決方案

#### 選項 A — 正確/安全做法（推薦）

* 將 LibreChat 部署在 HTTPS 後方（可使用 nginx/caddy/traefik；區域網路內自簽憑證亦可）。
* 接著在 `.env` 文件中調整工作階段時長：

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24小時
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30天
  ```
* 修改環境設定後重新啟動容器。
  這樣可維持登入狀態數天/數週，並解決 cookie 遺失問題。（[GitHub][2]）

#### 選項 B — 「我在私有區域網路，只想解決頻繁登出問題」

* 建立 `docker-compose.override.yml` 並在開發模式下運行 API（停用安全 cookies）：

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* 執行 `docker compose up -d` 套用變更。
  此法安全性較低（cookies 未設為 `secure`），但可解決透過純 HTTP 連線時強制重新登入的問題。（[librechat.ai][3]）

### 4) 可選的便利性調整

* **停用新用戶註冊** 以實現類單一用戶模式：

  ```
  ALLOW_REGISTRATION=false
  ```

  （如需新增用戶，仍可透過 `npm run create-user` 指令操作。）（[librechat.ai][4]）
* 保留 `.env` 中的其他驗證開關（電子郵件/社交登入標記）以簡化登入流程。（[librechat.ai][5]）

### 5) 適用 v0.8.0-rc3 的快速檢查清單

1. 決定：採用 HTTPS 代理（最佳）**或** 開發模式（快速區域網路解決方案）。
2. 在 `.env` 中設定更長的 `SESSION_EXPIRY` 與 `REFRESH_TOKEN_EXPIRY`。
3. 重啟服務堆疊使環境變更生效。
4. （可選）關閉註冊功能以實現「單一用戶」體驗。

如需協助，請貼上你目前的 `docker-compose.yml` 與 `.env` 檔案內容（排除機密資訊）。我將直接標註需要新增/修改的設定項目。

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"