---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 JWT 密鑰錯誤
translated: true
type: note
---

### 修復 LibreChat 中的 JWT 密鑰錯誤

日誌顯示 API 正在啟動，但因缺少 JWT 密鑰而崩潰：`JwtStrategy requires a secret or key`。這是 LibreChat 中常見的設定問題——後端使用 JWT（JSON Web Tokens）進行身份驗證，若沒有密鑰，就無法初始化策略。RAG API、權限和其他服務運作正常，但此問題會阻礙主 API 完全啟動，導致無法訪問 http://localhost:3080。

#### 快速修復：設定 JWT_SECRET
1. **生成安全密鑰**：
   - 執行以下指令生成隨機 32 位以上字串（用作 JWT_SECRET）：
     ```
     openssl rand -base64 32
     ```
     範例輸出：`a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6`

2. **更新您的 `.env` 檔案**：
   - 開啟 `.env`（位於 LibreChat 專案根目錄）。
   - 新增或取消註解此行（替換為您生成的密鑰）：
     ```
     JWT_SECRET=your_generated_secret_here
     ```
   - 若已存在但為空/註解狀態，請直接填入。
   - 儲存檔案。

3. **重啟服務**：
   ```
   docker compose down
   docker compose up -d
   ```
   - 監視日誌：`docker logs -f api`（若名稱不同則使用 `docker logs -f librechat_api`）。
   - 檢查是否成功啟動且無 JWT 錯誤。應顯示類似 "Server running on port 3080" 的日誌。

#### 驗證運作狀態
- 重啟後，檢查運行中的容器：
  ```
  docker ps
  ```
  - `api` 容器狀態應為 "Up" 並暴露 3080 端口。
- 測試訪問：在瀏覽器中開啟 http://localhost:3080。應顯示 LibreChat 登入/設定頁面。
- 若仍有問題，請追蹤日誌以查找新錯誤：`docker logs api`。

#### 日誌中的其他注意事項
- **過時配置**：您目前使用 v1.2.1，但 v1.3.0 已發布。修復 JWT 後，請查閱[更新日誌](https://www.librechat.ai/changelog)了解新功能（例如更好的驗證選項）。可透過拉取最新映像更新：`docker compose pull`。
- **Turnstile 已停用**：本地開發環境無妨；後續部署至生產環境時可啟用 CAPTCHA 功能。
- **UID/GID 警告**：若持續出現，請按我先前提議設定，以避免未來權限問題。

以上步驟應能讓您正常運作——JWT_SECRET 是驗證端點的必填項。若修復後日誌顯示其他錯誤，請將內容貼至此處。

[LibreChat 環境變數](https://www.librechat.ai/docs/configuration/dotenv#jwt_secret)  
[常見 Docker 問題](https://github.com/danny-avila/LibreChat/issues?q=is%3Aissue+is%3Aopen+label%3Adocker)