---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: Docker 註冊表連接逾時問題排查
translated: true
type: note
---

您遇到的錯誤 `Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)` 表示 Docker 客戶端因超時未能連接到 Docker Hub 倉庫。這可能由網絡問題、認證問題或配置錯誤引起。既然您正在嘗試網頁版登入，讓我們逐步排查並解決此問題。

### 解決步驟

1. **驗證網絡連接**
   - 確保您的網絡連接穩定。
   - 通過運行以下命令測試與 Docker Hub 的連接：
     ```bash:disable-run
     ping registry-1.docker.io
     ```
     或
     ```bash
     curl -v https://registry-1.docker.io/v2/
     ```
     如果這些命令失敗，您可能遇到網絡問題（例如防火牆、代理或 DNS 問題）。

2. **檢查網頁版認證**
   - 訊息顯示您正在使用一次性設備確認代碼 (`LVFK-KCQX`)。請確保您：
     - 按下了 `ENTER` 鍵以打開瀏覽器，或手動訪問了 `https://login.docker.com/activate`。
     - 在瀏覽器中正確輸入了代碼。
     - 在超時期限內於瀏覽器中完成了認證流程。
   - 如果瀏覽器沒有自動打開，請手動訪問該 URL 並輸入代碼。
   - 如果認證失敗或超時，請嘗試重新啟動流程：
     ```bash
     docker login
     ```

3. **處理超時問題**
   - 超時錯誤表明 Docker 客戶端無法連接到倉庫。通過設置 `DOCKER_CLIENT_TIMEOUT` 環境變量來增加超時時間：
     ```bash
     export DOCKER_CLIENT_TIMEOUT=120
     export COMPOSE_HTTP_TIMEOUT=120
     docker login
     ```
     這將超時時間延長至 120 秒。

4. **檢查代理或防火牆問題**
   - 如果您在代理後方，請配置 Docker 使用代理。編輯或創建 `~/.docker/config.json` 並添加：
     ```json
     {
       "proxies": {
         "default": {
           "httpProxy": "http://<proxy-host>:<proxy-port>",
           "httpsProxy": "https://<proxy-host>:<proxy-port>",
           "noProxy": "localhost,127.0.0.1"
         }
       }
     }
     ```
     將 `<proxy-host>` 和 `<proxy-port>` 替換為您的代理詳細信息。
   - 如果有防火牆阻止訪問，請確保允許 `registry-1.docker.io` 和 `login.docker.com`。

5. **使用憑證助手（可選但推薦）**
   - 關於 `~/.docker/config.json` 中未加密憑證的警告建議設置憑證助手。安裝一個憑證助手，例如 `docker-credential-pass` 或 `docker-credential-secretservice`：
     - 對於使用 `pass` 的 Linux 系統：
       ```bash
       sudo apt-get install pass
       curl -fsSL https://github.com/docker/docker-credential-helpers/releases/download/v0.7.0/docker-credential-pass-v0.7.0-amd64.tar.gz | tar -xz
       sudo mv docker-credential-pass /usr/local/bin/
       ```
       初始化 `pass`：
       ```bash
       gpg2 --gen-key
       pass init <your-gpg-key-id>
       ```
       更新 `~/.docker/config.json` 以使用助手：
       ```json
       {
         "credsStore": "pass"
       }
       ```
     - 配置憑證助手後重試登入。

6. **回退到命令行登入**
   - 如果網頁版登入持續失敗，請嘗試使用您的 Docker Hub 用戶名和密碼進行命令行登入：
     ```bash
     docker login -u <your-username>
     ```
     在提示時輸入您的密碼或個人訪問令牌 (PAT)。您可以從 Docker Hub 帳戶設置生成 PAT。

7. **檢查 Docker 守護進程狀態**
   - 確保 Docker 守護進程正在運行：
     ```bash
     sudo systemctl status docker
     ```
     如果未運行，請啟動它：
     ```bash
     sudo systemctl start docker
     ```

8. **清除 Docker 配置（最後手段）**
   - 如果問題仍然存在，請清除 Docker 配置文件並重試：
     ```bash
     mv ~/.docker/config.json ~/.docker/config.json.bak
     docker login
     ```

### 補充說明
- **Docker Hub 狀態**：訪問 `https://status.docker.com/` 檢查 Docker Hub 是否出現服務中斷。
- **DNS 問題**：如果 `registry-1.docker.io` 無法解析，請嘗試在您的網絡設置中使用公共 DNS，例如 Google (`8.8.8.8`) 或 Cloudflare (`1.1.1.1`)。
- **Docker 版本**：確保您的 Docker 客戶端是最新版本：
  ```bash
  docker --version
  ```
  如果需要，請按照您操作系統的說明更新 Docker。

### 參考資料
- [Docker Credential Store Documentation](https://docs.docker.com/go/credential-store/)
- [Docker Login Documentation](https://docs.docker.com/engine/reference/commandline/login/)
- [Docker Hub Status](https://status.docker.com/)