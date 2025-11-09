---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 優化LibreChat的Docker記憶體設定
translated: true
type: note
---

### 理解 Docker 在 LibreChat 中的記憶體使用情況

LibreChat 是一個資源密集型應用程式，因為它運行了完整的技術堆疊：主 LibreChat 使用者介面、用於資料儲存的 MongoDB、用於搜尋索引的 Meilisearch、向量資料庫（可能是 Pinecone 或透過 vectordb 的類似服務），以及用於檢索增強生成的 RAG API。這些服務都在 Docker 中容器化，這會增加一些開銷——尤其是在 macOS 上，Docker Desktop 在輕量級 Linux 虛擬機器中運行所有內容。僅該虛擬機器閒置時就可能佔用 1-2GB，再加上像 MongoDB（預設使用最多主機 RAM 的 50%）和 Meilisearch（在記憶體中索引資料）這樣的資料庫，總共很容易達到 3GB。

Docker 的「簡便」在於它捆綁了依賴項、隔離了環境，並且只需一個指令（如 `docker compose up`）即可啟動，避免了手動設定的麻煩。但沒錯，代價就是資源佔用高：容器無法高效共享主機核心，如果不進行調整，它們會膨脹。

#### 快速降低記憶體使用量的方法
以下是一些實用步驟，可以在不完全放棄 Docker 的情況下優化你的設定：

1. **限制每個容器的資源**：
   - 編輯你的 `docker-compose.yml` 檔案（位於 LibreChat 儲存庫中）。在每個服務下添加資源限制。例如：
     ```
     services:
       chat-mongodb:
         deploy:
           resources:
             limits:
               memory: 512M  # 將 MongoDB 限制在 512MB
       chat-meilisearch:
         deploy:
           resources:
             limits:
               memory: 256M  # Meilisearch 不需要太多記憶體
       vectordb:  # 假設是 Qdrant 或類似服務
         deploy:
           resources:
             limits:
               memory: 256M
       rag_api:
         deploy:
           resources:
             limits:
               memory: 128M
       LibreChat:
         deploy:
           resources:
             limits:
               memory: 512M
     ```
     - 運行 `docker compose down`，然後運行 `docker compose up -d` 來應用更改。這不會破壞任何東西，但如果你觸及上限，可能會減慢查詢速度——使用 `docker stats` 進行監控。

2. **調整 Docker Desktop 設定**：
   - 打開 Docker Desktop > 設定 > 資源。將記憶體總量設定為 2-4GB（而不是無限制）。如果任何映像不是 ARM 原生（M2 Air 是 ARM，所以大多數應該沒問題），請啟用「對 Apple Silicon 上的 x86/amd64 模擬使用 Rosetta」。
   - 清理未使用的東西：`docker system prune -a` 以釋放磁碟/虛擬機器膨脹。

3. **停用不需要的服務**：
   - 如果你不使用 RAG/向量搜尋，請在 `docker-compose.yml` 中註解掉 `vectordb` 和 `rag_api`。
   - 對於基本聊天，僅 MongoDB + LibreChat 可能讓你降至約 1.5GB。

4. **使用 ARM 優化映像**：
   - 確保你使用的是最新的 LibreChat 版本（v0.7+ 原生支援 M1/M2）。使用 `docker compose pull` 拉取。

#### 不使用 Docker 運行：是的，它可能更快/更輕量
絕對是——跳過 Docker 可以移除虛擬機器開銷（節省 0.5-1GB）並讓服務在 macOS 上原生運行。LibreChat 有一個手動安裝指南，使用 Node.js、npm 和直接服務安裝。在你的 M2 Air 上可能會感覺更流暢，因為所有內容都利用 Apple 的統一記憶體而無需虛擬化。

**原生安裝的優點**：
- 更低的 RAM（預計總共 1-2GB）。
- 更快的啟動和 I/O（無容器網路）。
- 更容易除錯。

**缺點**：
- 更多設定步驟（透過 Homebrew 手動安裝 MongoDB/Meilisearch）。
- 潛在的依賴衝突。

**快速原生安裝指南**（適用於 macOS）：
1. 安裝先決條件：
   - Node.js (v18+)：使用 Homebrew `brew install node`。
   - MongoDB：`brew tap mongodb/brew && brew install mongodb-community`。使用 `brew services start mongodb/brew/mongodb-community` 啟動。
   - Meilisearch：`brew install meilisearch`。使用 `meilisearch --master-key=your-master-key` 啟動。
   - Yarn：`npm install -g yarn`。

2. 克隆並安裝 LibreChat：
   ```
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   cp .env.example .env
   # 編輯 .env：設定 MONGO_URI=mongodb://localhost:27017/librechat, MEILI_MASTER_KEY=your-master-key 等。
   yarn install
   yarn build
   yarn dev  # 或者 yarn start 用於生產環境
   ```

3. 在 http://localhost:3080 訪問。如果未使用 RAG，請調整 `.env` 來停用它。

如果你遇到問題（例如 ARM 相容性），官方文件有故障排除指南。這應該能讓你輕鬆低於 2GB。

#### 監控工具
- **Activity Monitor**（內建）：監視「記憶體」標籤頁中的 Docker 程序。
- **docker stats**：在終端機中即時監控容器使用情況。
- 如果問題持續存在，請查看 LibreChat 的 GitHub issues——許多 M1/M2 使用者報告了類似的問題。

如果這不能解決問題，或者你分享你的 `docker-compose.yml`，我可以進一步完善建議！

[LibreChat 官方文件 - Docker 優化](https://docs.librechat.ai/install/providers/docker.html)  
[LibreChat 手動安裝指南](https://docs.librechat.ai/install/installation/manual_install.html)  
[Docker Desktop 在 macOS 上的資源限制](https://docs.docker.com/desktop/settings/mac/)