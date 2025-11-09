---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: LibreChat 本地主機存取疑難排解
translated: true
type: note
---

### 疑難排解在 localhost:3080 上存取 LibreChat 的問題

根據你的日誌，Docker 映像已成功拉取（經過一些初始逾時和重試後），並且啟動了 6 個元件：預設網路、`vectordb`、`chat-mongodb`、`chat-meilisearch`、`rag_api` 和 `LibreChat`。然而，`api` 服務（通常負責在連接埠 3080 提供後端服務）並未列在已啟動的容器中——這很可能是你無法存取網站的原因。`LibreChat` 容器很可能是前端，它依賴於 `api` 後端。

UID/GID 警告提示可能存在權限問題，可能導致 `api` 容器無法正常啟動。以下是一步一步的指南來診斷和修復此問題。

#### 1. **驗證執行中的容器和連接埠**
   執行以下指令以查看所有活動容器、它們的狀態以及連接埠映射：
   ```
   docker ps
   ```
   - 尋找 `api` 容器（它可能名為 `librechat_api` 或類似名稱）。如果它缺失或已退出，那就是問題所在。
   - 確認連接埠 `3080` 是否已映射（例如 `0.0.0.0:3080->3080/tcp`）。如果沒有，表示服務未暴露該連接埠。
   - 如果沒有容器顯示連接埠 3080，請繼續下一步。

#### 2. **檢查容器日誌**
   檢查啟動錯誤的日誌，特別是 `api` 和 `LibreChat` 服務：
   ```
   docker logs LibreChat
   docker logs api  # 或者如果名稱不同，使用 docker logs librechat_api
   docker logs rag_api  # 以防有依賴性問題
   ```
   - 常見錯誤：權限被拒絕（由於 UID/GID）、MongoDB/Meilisearch 連接失敗，或綁定問題（例如未監聽 0.0.0.0）。
   - 如果日誌顯示伺服器已啟動但僅綁定到容器內的 localhost，請在 `.env` 檔案中添加 `HOST=0.0.0.0`。

#### 3. **設定 UID 和 GID 以修復權限警告**
   你的 `.env` 檔案（從 `.env.example` 複製而來）很可能已將這些變數註釋掉。未設定的變數可能因檔案權限不匹配而導致容器無聲無息地失敗。
   - 編輯 `.env`：
     ```
     UID=1000  # 執行 `id -u` 以取得你的使用者 ID
     GID=1000  # 執行 `id -g` 以取得你的群組 ID
     ```
   - 儲存後重新啟動：
     ```
     docker compose down
     docker compose up -d
     ```
   這可確保卷（如 config/logs）由你的使用者擁有。

#### 4. **測試連線**
   - 檢查連接埠 3080 是否在本機監聽：
     ```
     curl -v http://localhost:3080
     ```
     - 如果逾時或拒絕連接，表示服務未執行/暴露。
   - 如果 `docker ps` 顯示連接埠已映射但 curl 失敗，請檢查防火牆（例如 `sudo ufw status`）或嘗試 `http://127.0.0.1:3080`。

#### 5. **如果需要，進行其他修復**
   - **映像拉取問題**：你的第一次嘗試對 `ghcr.io/v2/librechat/librechat/manifests/latest` 出現「拒絕」錯誤。如果再次拉取失敗，請向 GitHub Container Registry 進行身份驗證：
     ```
     echo $YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
     ```
     （在 github.com/settings/tokens 建立具有 `read:packages` 範圍的個人存取權杖。）
   - **使用推薦的 Compose 檔案**：預設的 `docker-compose.yml` 用於本機建置，可能不穩定。切換到 `deploy-compose.yml` 以使用穩定的遠端映像：
     - 重新命名或備份你當前的 `docker-compose.yml`。
     - 改用 `deploy-compose.yml`：`docker compose -f deploy-compose.yml up -d`。
     - 確保 `.env` 中有 `HOST=0.0.0.0` 和 `NODE_ENV=production`。
   - **使用 Prune 進行完整重啟**：如果卡住，請清理：
     ```
     docker compose down -v  # 同時移除卷
     docker system prune -f
     docker compose up -d
     ```
   - **依賴項**：確認 MongoDB 和 Meilisearch 健康狀況良好（`docker logs chat-mongodb` 等）。`api` 依賴於它們。

完成這些步驟後，重新嘗試存取 http://localhost:3080。如果日誌顯示特定錯誤（例如 Mongo 連接），請分享它們以獲得更有針對性的幫助。一旦 UID/GID 和依賴項問題解決，此設定對大多數使用者都有效。

[本機 Docker 建置無法在 localhost:3080 上提供服務](https://github.com/danny-avila/LibreChat/discussions/3425)  
[LibreChat Docker 文件](https://www.librechat.ai/docs/local/docker)  
[Env 檔案配置 (UID/GID)](https://www.librechat.ai/docs/configuration/dotenv)