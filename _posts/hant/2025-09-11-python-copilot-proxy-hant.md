---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: Python Copilot 代理伺服器實現
translated: true
type: note
---

這款 Python 腳本是一個能與 **GitHub Copilot** 互動生成代碼補全的**本地代理伺服器**。它通過處理身份驗證並將請求轉發至 Copilot 的 API，模擬了官方 GitHub Copilot 插件（例如 Neovim 版本）的行為。

---

### **核心組件與工作流程**
1. **身份驗證（`setup()` 與 `get_token()`）**
   - 使用 **OAuth 設備流程** 進行 GitHub 身份驗證
   - 向 GitHub 請求**設備代碼**與**用戶代碼**
   - 要求用戶訪問特定網址（`verification_uri`）並輸入`user_code`
   - 持續向 GitHub 查詢直到獲取**訪問令牌**
   - 將令牌保存至`.copilot_token`供後續使用
   - 將訪問令牌兌換為**Copilot 會話令牌**（API 調用必需）

2. **令牌刷新（`token_thread()`）**
   - 在後台線程中運行
   - 每**25分鐘**自動刷新 Copilot 令牌（因令牌會過期）

3. **Copilot API 交互（`copilot()`）**
   - 將**提示內容**（代碼片段）發送至 Copilot API
   - 以**流模式**（逐行傳輸）返回生成的補全內容
   - 處理錯誤情況（如無效/過期令牌）

4. **HTTP 伺服器（`HTTPRequestHandler`）**
   - 監聽**POST 請求**（例如來自本地編輯器）
   - 從請求中提取`prompt`與`language`參數
   - 調用`copilot()`並以純文本形式返回補全結果

5. **主函數（`main()`）**
   - 啟動**令牌刷新線程**
   - 在指定端口（默認：`8080`）啟動 **HTTP 伺服器**

---

### **運作原理逐步解析**
1. **首次運行（無令牌）**
   - 腳本調用`setup()`通過 OAuth 進行身份驗證
   - 用戶訪問 GitHub 並輸入授權碼完成授權
   - 腳本將訪問令牌保存至`.copilot_token`

2. **後續運行（令牌已存在）**
   - 腳本讀取`.copilot_token`並獲取 Copilot 會話令牌
   - 若令牌過期將自動刷新

3. **處理請求**
   - 本地編輯器（如 Neovim）發送包含代碼片段的 **POST 請求**
   - 腳本將提示內容轉發至 Copilot API
   - 生成的補全內容將返回至編輯器

4. **令牌管理**
   - 後台線程每**25分鐘**刷新令牌避免過期

---

### **開發背景**
- **繞過官方插件**：部分編輯器（如 Neovim）缺乏官方 Copilot 支援，此腳本可作為橋接工具
- **本地代理**：通過本地管理令牌避免觸發速率限制
- **自訂化**：可修改以適應不同編輯器或 API

---

### **安全與道德考量**
- **寫死客戶端 ID**：腳本使用 GitHub Copilot 官方`client_id`（`Iv1.b507a08c87ecfe98`），在非官方插件環境使用可能違反 GitHub 服務條款
- **令牌儲存**：訪問令牌以明文形式存儲於`.copilot_token`存在安全風險
- **速率限制**：頻繁請求可能觸發 GitHub 濫用檢測機制

---
### **使用指南**
1. 運行腳本：
   ```sh
   python copilot_proxy.py [端口號]
   ```
   （默認端口：`8080`）

2. 配置編輯器向 `http://localhost:8080` 發送 JSON 格式請求：
   ```json
   {
     "prompt": "def hello_world():",
     "language": "python"
   }
   ```

3. 腳本將返回 Copilot 的補全內容

---
### **優化方向**
- **強化錯誤處理**：重試失敗請求、處理網絡問題
- **安全令牌儲存**：採用加密儲存或環境變量
- **配置文件**：允許自訂`client_id`、端口等參數
- **日誌記錄**：添加除錯日誌方便問題排查

---
### **替代方案**
- 使用**官方 Copilot 插件**（VS Code、JetBrains 等版本）
- 嘗試**開源替代方案**如 **Codeium** 或 **Tabby**

此腳本雖是巧妙的解決方案，但因潛在的服務條款違規風險，使用時應保持謹慎。