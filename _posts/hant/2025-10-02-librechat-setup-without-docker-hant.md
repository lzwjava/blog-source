---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 不使用 Docker Compose 的 LibreChat 設定
translated: true
type: note
---

是的，你可以不使用 Docker Compose 來設置 LibreChat，只需使用獨立的 `docker run` 指令，甚至採用非 Docker 方法（手動安裝 Node.js、Yarn、MongoDB 和 MeiliSearch）。這樣可以避免下載 `docker-compose` 二進制文件本身（它體積很小，約 20-30MB，但我猜你指的是 LibreChat 服務的總鏡像拉取量約 70MB+）。然而，核心 Docker 鏡像（例如應用程式、MongoDB、MeiliSearch）在拉取後總共仍約為 500MB-1GB——Docker Compose 只是 Docker 之上的編排工具，並非主要的頻寬消耗者。在緩慢的 4G/5G 網絡下拉取鏡像仍然是瓶頸，但你可以採取一些緩解措施。

我將在下面概述幾種選項，優先考慮節省頻寬的技巧。如果流動數據非常有限，請考慮暫時連接至 WiFi 網絡，或在另一台機器上使用預先下載的設置（例如，通過 `docker save`/`docker load` 導出/導入鏡像）。

### 適用於任何 Docker 設置的節省頻寬技巧
- **在更快的連接上預先拉取鏡像**：在另一台網絡較好的設備上，運行 `docker pull node:20-alpine`（用於應用程式）、`docker pull mongo:7`（數據庫）和 `docker pull getmeili/meilisearch:v1.10`（搜索）。然後將它們保存為文件：
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  通過 USB/驅動器傳輸 .tar 文件（總計約 500-800MB 壓縮），然後在你的 Ubuntu 機器上運行：`docker load -i librechat-app.tar` 等。無需在線拉取。
- **使用更輕量的替代方案**：用於測試時，可以暫時跳過 MeiliSearch（它是可選的搜索功能；在配置中禁用）。MongoDB 鏡像約為 400MB——改用本地 MongoDB 安裝（見下面的非 Docker 部分）以節省約 400MB。
- **監控使用情況**：使用 `docker pull --quiet` 或 `watch docker images` 等工具來跟踪。
- **代理或緩存**：如果你有 Docker Hub 鏡像或代理，請在 `/etc/docker/daemon.json` 中配置以加速拉取。

### 選項 1：純 Docker（無 Compose）– 等同於 Compose 設置
你可以使用 `docker run` 和 `docker network` 複製 `docker-compose.yml` 的行為。這仍然會下載相同的鏡像，但讓你可以控制每個步驟。總下載量仍約為 700MB+（應用程式構建 + 數據庫）。

1. **創建 Docker 網絡**（隔離服務）：
   ```
   docker network create librechat-network
   ```

2. **運行 MongoDB**（將 `your_mongo_key` 替換為強密碼）：
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - 創建 `./data/mongodb` 用於持久化。

3. **運行 MeiliSearch**（將 `your_meili_key` 替換為你的密鑰）：
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - 如果頻寬緊張，可以跳過此步驟；稍後在應用程式配置中禁用。

4. **克隆並構建/運行 LibreChat 應用程式**：
   - 如果尚未完成，克隆倉庫：`git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat`（倉庫下載約 50MB）。
   - 構建鏡像（這會拉取 Node.js 基礎鏡像約 200MB 並構建應用程式層）：
     ```
     docker build -t librechat-app .
     ```
   - 運行它（連接到數據庫，使用環境變量——如我之前的回复所述創建一個 `.env` 文件）：
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - 在 `.env` 中，設置 `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` 和 `MEILI_HOST=http://meilisearch:7700` 等。

5. **訪問**：`http://localhost:3080`。日誌：`docker logs -f librechat`。

- **停止/清理**：`docker stop mongodb meilisearch librechat && docker rm 它們`。
- **優點/缺點**：與 Compose 相同，但更手動。鏡像拉取/構建的數據量仍然很大。

### 選項 2：非 Docker 安裝（手動，無鏡像拉取）– 推薦用於低頻寬情況
在 Ubuntu 上原生安裝依賴項。這避免了所有 Docker 開銷（容器約 0MB；僅通過 apt/yarn 下載軟件包，總計約 200-300MB）。間接使用你系統的 Python/Node 設置。

#### 先決條件（一次性安裝）
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # MongoDB 官方軟件包；MeiliSearch 約 50MB 二進制文件
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js：如果不是 v20+，通過 nvm 安裝：`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`，然後 `nvm install 20`。
- Yarn：`npm install -g yarn`。
- MongoDB 配置：編輯 `/etc/mongod.conf` 綁定到 localhost，然後重啟。

#### 安裝步驟
1. **克隆倉庫**：
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **安裝依賴項**：
   ```
   yarn install  # 軟件包下載約 100-200MB
   ```

3. **配置 `.env`**（從 `.env.example` 複製）：
   - `cp .env.example .env && nano .env`
   - 關鍵更改：
     - Mongo：`MONGODB_URI=mongodb://localhost:27017/LibreChat`（如果需要，通過 `mongo` shell 創建數據庫用戶）。
     - Meili：`MEILI_HOST=http://localhost:7700` 和 `MEILI_MASTER_KEY=your_key`。
     - 如果跳過 Meili，禁用搜索：`SEARCH=false`。
     - 根據需要添加 AI 密鑰。

4. **構建並運行**：
   - 在一個終端中：`yarn run backend`（在端口 3090 啟動 API）。
   - 在另一個終端中：`yarn run frontend`（在端口 3080 啟動 UI）。
   - 或用於生產環境的 PM2：`yarn global add pm2 && pm2 start yarn --name backend -- run backend` 等。

5. **訪問**：`http://localhost:3080`。創建帳戶並配置。

- **數據**：MongoDB 存儲在 `/var/lib/mongodb`，Meili 存儲在 `/var/lib/meilisearch`。
- **故障排除**：
  - Mongo 認證：運行 `mongo` 並創建用戶：`use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`。
  - 端口/防火牆：`sudo ufw allow 3080,3090,7700`。
  - 更新：`git pull && yarn install && 重啟服務`。
- **優點**：對頻寬更友好（無容器），直接使用系統資源。缺點：設置更繁瑣，可能出現依賴衝突（例如與你的 Python 3.13，但 Node 是獨立的）。

如果流動數據極其有限，非 Docker 方法是最佳選擇——分階段進行，使用 `du -sh` 監控目錄大小。對於錯誤，請分享日誌（例如來自 `yarn run backend`）。官方非 Docker 指南：https://docs.librechat.ai/install/installation/manual_install.html。如果你需要 Ollama 集成以用於本地 AI（節省 API 成本），請通過他們的腳本單獨安裝（約 100MB）。如需調整，請告訴我！