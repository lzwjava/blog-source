---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 在 Ubuntu 上安裝 LibreChat
translated: true
type: note
---

### 在 Ubuntu 24.04 LTS 上安裝 LibreChat

LibreChat 是一個開源 AI 聊天平台，透過網頁介面支援多種 AI 模型（例如 OpenAI、Gemini、Ollama）。推薦使用 Docker Compose 進行安裝，因為這種方法簡單、能自動處理 MongoDB 和 MeiliSearch 等依賴項，且在 Ubuntu 上運行可靠。您的系統（Ubuntu 24.04.2 LTS 與 Python 3.13.4）符合要求，但您需要先安裝 Docker 和 Git。

#### 先決條件
1. **更新系統**：
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **安裝 Git**（如果尚未安裝）：
   ```
   sudo apt install git -y
   ```

3. **安裝 Docker 和 Docker Compose**：
   - 安裝 Docker：
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     登出並重新登入（或執行 `newgrp docker`）以使群組變更生效。
   - 安裝 Docker Compose（最新版本）：
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     使用 `docker-compose --version` 驗證安裝。

#### 安裝步驟
1. **複製 LibreChat 儲存庫**：
   ```
   cd ~/projects  # 或您偏好的目錄
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **複製並設定環境檔案**：
   - 複製範例檔案：
     ```
     cp .env.example .env
     ```
   - 使用文字編輯器編輯 `.env`（例如 `nano .env`）。需要更新的關鍵設定：
     - 設定 MongoDB 主密鑰：生成一個強密碼並設定 `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` 和 `MONGODB_MASTER_KEY=your_generated_key_here`。
     - 對於 MeiliSearch：設定 `MEILI_MASTER_KEY=your_generated_key_here`（生成一個強密鑰）。
     - 如果需要，添加 AI API 金鑰（例如 `OPENAI_API_KEY=your_openai_key`）。對於本地模型如 Ollama，初始時不需要金鑰。
     - 儲存並退出。完整配置選項請參考文件。

3. **使用 Docker Compose 啟動 LibreChat**：
   ```
   docker-compose up -d
   ```
   - 這會拉取映像、啟動服務（LibreChat 應用程式、MongoDB、MeiliSearch），並在後台模式運行。
   - 等待完全啟動（使用 `docker-compose logs -f` 檢查）。

4. **存取 LibreChat**：
   - 開啟瀏覽器並前往 `http://localhost:3080`。
   - 在登入頁面建立帳戶。
   - 選擇 AI 模型（在設定中配置端點）並開始聊天。

#### 安裝後提示
- **停止/更新**：執行 `docker-compose down` 停止，然後執行 `git pull` 和 `docker-compose up -d --build` 進行更新。
- **資料持久化**：MongoDB 資料的儲存卷會自動建立（位於 `./data/mongodb`）。
- **疑難排解**：
  - 如果連接埠衝突，編輯 `docker-compose.yml` 更改 `3080:3080`。
  - 對於無頭/伺服器存取，使用您的伺服器 IP（例如 `http://your-server-ip:3080`）並確保防火牆允許連接埠 3080（`sudo ufw allow 3080`）。
  - 如果使用本地 LLM，請單獨安裝 Ollama 並在 `.env` 中將其添加為端點。
- **替代方案：NPM 方法**（不使用 Docker）：如果您偏好，可以手動安裝 Node.js 18+、Yarn、MongoDB 和 MeiliSearch，然後執行 `yarn install` 和 `yarn run frontend` + `yarn run backend`。但強烈推薦使用 Docker 以簡化流程。

這應該能讓您快速啟動並運行。如果遇到錯誤，請分享輸出以獲得更多幫助！

[LibreChat 官方文件](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Ubuntu Docker 指南](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[It's FOSS 教學](https://itsfoss.com/librechat-linux/)