---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 快速安裝 Docker Compose 的方法
translated: true
type: note
---

### 在 Ubuntu 上快速下載/安裝 Docker Compose 的替代方法

假設您想快速取得最新的 Docker Compose 二進位檔（根據官方文件，截至 2025 年 10 月為 v2.37.3），而不想經過完整的 GitHub 發布頁面流程（例如手動 curl 加 sha256 驗證），這裡提供幾個可靠且更快速的選項。這些方法利用 Ubuntu 的套件管理員或 Docker 的軟體庫，實現近乎即時的安裝。我將優先考慮速度和簡便性——大多數方法只需不到 1 分鐘。

#### 1. **透過 Ubuntu APT（對多數使用者最快）**
   如果您已安裝 Docker（其中包含 `docker-compose-plugin`），只需使用子指令——無需單獨下載。這是現代化的整合方式，可避免二進位檔管理的麻煩。
   
   - **檢查是否已可用**：
     ```
     docker compose version
     ```
     如果顯示 v2.x，那就完成了——這是透過您的 Docker 安裝取得的最新版本。
   
   - **如需安裝/更新**（若缺少則添加外掛）：
     ```
     sudo apt update
     sudo apt install docker-compose-plugin
     ```
     - **為何快速？** 無需經過 GitHub 流量；使用本地軟體庫。會隨 `apt upgrade` 自動更新。
     - **用法**：執行時使用 `docker compose up`（注意是空格，而非連字號）。
     - **專業提示**：如果尚未安裝 Docker，請先添加 Docker 的軟體庫：
       ```
       sudo apt update
       sudo apt install ca-certificates curl
       sudo install -m 0755 -d /etc/apt/keyrings
       sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
       sudo chmod a+r /etc/apt/keyrings/docker.asc
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       sudo apt update
       sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
       ```

#### 2. **從 GitHub 單行 Curl（比完整發布版稍快）**
   跳過瀏覽發布頁面——curl 直接取得最新的 Linux x86_64 二進位檔並進行安裝。這比手動選擇資產更快，但仍使用 GitHub。
   
   ```
   VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4) && sudo curl -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version
   ```
   - **為何快速？** API 在幾秒內取得版本；單一指令處理下載和安裝。
   - **驗證**：結尾的 `--version` 會確認安裝。
   - **注意**：如需特定版本 v2.39.4，請將 `${VERSION}` 替換為 `v2.39.4`。

#### 3. **透過 Snap（Ubuntu 的通用套件管理員）**
   Snap 在 Ubuntu 24.04 上預先安裝，並能從 Canonical 的商店即時拉取最新版本。
   
   ```
   sudo snap install docker
   ```
   - **為何快速？** 無需設定軟體庫；並行下載且自動更新。包含 Compose 外掛。
   - **用法**：與 APT 方法相同（`docker compose`）。
   - **檢查版本**：`docker compose version`。

#### 4. **透過 Pip（既然您有 Python 3.13.4）**
   如果您偏好基於 Python 的方式（舊版 v1 風格，但 pip 有 v2 包裝器），這是一個無需系統依賴的快速安裝方法。
   
   ```
   sudo pip3 install docker-compose
   ```
   - **為何快速？** Pip 會快取並快速解析依賴；不涉及 GitHub。
   - **限制**：這更多是為了 v1 相容性——請使用 APT 來取得官方的 v2 外掛。
   - **驗證**：`docker-compose --version`（使用連字號）。

這些方法都比透過 GitHub 使用者介面更快，因為它們減少了點擊或使用了 API/快取。對於 Ubuntu，我首推 APT 或 Snap——它們無縫整合並處理更新。如果您所說的 "docker compose down" 是指其他意思（例如指令本身），請澄清！

[官方 Docker Compose 安裝指南](https://docs.docker.com/compose/install/linux/)  
[Docker 發布頁面](https://github.com/docker/compose/releases)